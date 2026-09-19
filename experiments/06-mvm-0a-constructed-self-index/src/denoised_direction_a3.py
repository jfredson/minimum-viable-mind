"""Denoised own-agent direction — a known-answer test for the stack.

**UNREGISTERED** diagnostic. The method is committed in
`denoised-direction-method.md`, in the same commit as this file and
before either produced any output. Read that file first: it fixes the
outcome cells, and the point of the whole exercise is that they were
fixed while nobody knew which one would fire.

WHERE THIS COMES FROM. The research note on The Pain Axis paper
(`docs/research-note-pain-axis-2026-09-19.md`), item 2, "denoise before
probing". Their direction is a difference of averages taken AFTER
removing the directions that account for half the variation in their
control data. Our five linear probes on the pilot checkpoint all landed
below their own permutation nulls, on a checkpoint where ownership is
measured to be load-bearing. If the residual stream at the probed
position is dominated by variation that has nothing to do with ownership,
a probe fitted to the raw states can fail where a denoised difference of
averages would not.

WHAT IS ASKED. Per layer, per checkpoint: after projecting out the
principal components accounting for half the variation in the control
condition, does a difference-of-averages own-agent direction separate
held-out episodes above the same permutation null the failed probes were
scored against?

WHAT A PASS WOULD NOT SHOW. That whatever separates is a carried
self-index rather than the acting channel's input trace passed forward.
That is red-team objection R1 and nothing here answers it.

THE CONTROL CONDITION, MADE CONCRETE. The same states with the own-agent
signal taken out: each state minus the average state of the episodes
sharing its owning agent. What is left is everything the residual stream
carries at that position except which agent the model is. Its principal
components are the nuisance directions. The strongest alternative — the
principal components of the PAIR averages, since the episodes come in
pairs sharing content with the owning agent rotated — is named in the
method file and deliberately not implemented here: it is a different
measurement and would need its own committed method, not a flag on this
one.

THE PART THAT IS EASY TO GET WRONG. Every fitted quantity — the class
averages used for centring, the nuisance components, the directions, the
nearest-average reference points — is fitted on the training folds and
applied to the held-out fold. If any of them sees the held-out episodes,
the separation is not held out and the number means nothing. The
splitting is four-fold, the same as the probes used, and the null is the
same construction: 200 draws, each shuffling the labels and redoing the
ENTIRE procedure.

THE CONTRAST ARM is not in item 2 and is mine. The same direction, splits,
statistic and null WITHOUT the denoising step. Item 2's claim is that
denoising is specifically what would rescue the signal; without this arm a
pass would not say whether the denoising is why.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock,
for the reason given in the method file; fresh output file per
checkpoint, nothing overwritten [C6].

    ../../../.venv/bin/python denoised_direction_a3.py --self-test
    ../../../.venv/bin/python denoised_direction_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import torch

import lock_guard
import localize_a3 as L
from model import MVM0aModel, Config

PROBE_LAYERS = L.PROBE_LAYERS          # 3, 4, 5, 7, 8 — unchanged
N_PAIRS = 200                          # 400 episodes, as the control used
EPISODE_SEED = 20260917                # the control's content seed
N_PERM = L.N_PERM                      # 200, the probes' null
N_FOLDS = 4                            # the probes' cross-validation
SD_BAR = 3.0                           # the probes' bar, not moved
VARIANCE_KEPT = 0.50                   # "half the variation", from item 2
NO_INFORMATION = 0.5                   # separation score with no signal


# ------------------------------------------------------- the measurement

def control_condition(X, y):
    """The states with the own-agent signal taken out: each state minus
    the average of the states sharing its owning agent. Everything the
    residual stream carries here EXCEPT which agent the model is."""
    out = np.array(X, dtype=np.float64, copy=True)
    for c in np.unique(y):
        m = y == c
        out[m] -= out[m].mean(0, keepdims=True)
    return out


def nuisance_components(C, keep=VARIANCE_KEPT):
    """The smallest set of principal components of the control condition
    whose variation adds up to at least `keep` of the total. Returned as
    rows. The count is the number worth reporting: a layer where half the
    variation sits in one direction is telling a different story from one
    where it takes forty."""
    C = C - C.mean(0, keepdims=True)
    _, s, vt = np.linalg.svd(C, full_matrices=False)
    var = s ** 2
    total = var.sum()
    if total <= 0:
        return vt[:0], 0, 0.0
    frac = np.cumsum(var) / total
    k = int(np.searchsorted(frac, keep) + 1)
    k = min(k, vt.shape[0])
    return vt[:k], k, float(frac[k - 1])


def project_out(X, V):
    """Remove the span of the rows of V from every row of X."""
    if V.shape[0] == 0:
        return np.array(X, dtype=np.float64, copy=True)
    return X - (X @ V.T) @ V


def one_vs_rest_directions(X, y, classes):
    """The difference of averages, in the only form that makes sense with
    four conditions: for each owning agent, its average minus the average
    of the others. Unit length."""
    D = []
    for c in classes:
        m = y == c
        if m.sum() == 0 or (~m).sum() == 0:
            D.append(np.zeros(X.shape[1]))
            continue
        d = X[m].mean(0) - X[~m].mean(0)
        n = np.linalg.norm(d)
        D.append(d / n if n > 0 else d)
    return np.stack(D)


def auc(pos, neg):
    """Probability that a random positive projects above a random
    negative — the area under the receiver operating characteristic
    curve, by rank, with ties counted as half."""
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    allv = np.concatenate([pos, neg])
    r = np.empty(len(allv), dtype=np.float64)
    order = np.argsort(allv, kind="mergesort")
    sv = allv[order]
    i = 0
    while i < len(sv):
        j = i
        while j + 1 < len(sv) and sv[j + 1] == sv[i]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2.0 + 1.0
        i = j + 1
    return float((r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2.0)
                 / (len(pos) * len(neg)))


def folds(n, k, rng):
    """Deterministic k-fold assignment for a given generator."""
    idx = rng.permutation(n)
    return [idx[i::k] for i in range(k)]


def score_once(X, y, classes, denoise, fold_sets):
    """Held-out separation and nearest-average accuracy, fitting every
    quantity on the training folds only.

    Returns (mean separation score across agents, accuracy, components
    kept per fold, whether any fold was degenerate)."""
    n = len(y)
    proj = np.zeros((n, len(classes)))
    pred = np.empty(n, dtype=int)
    kept = []
    dead = False
    for held in fold_sets:
        mask = np.zeros(n, dtype=bool)
        mask[held] = True
        tr, te = ~mask, mask
        if len(np.unique(y[tr])) < len(classes):
            dead = True
        Xtr, Xte = X[tr], X[te]
        if denoise:
            V, k, _ = nuisance_components(control_condition(Xtr, y[tr]))
            if V.shape[0] >= Xtr.shape[1]:
                dead = True
            kept.append(k)
            Xtr, Xte = project_out(Xtr, V), project_out(Xte, V)
        D = one_vs_rest_directions(Xtr, y[tr], classes)
        proj[te] = Xte @ D.T
        mus = np.stack([Xtr[y[tr] == c].mean(0)
                        if (y[tr] == c).any() else np.zeros(Xtr.shape[1])
                        for c in classes])
        dist = ((Xte[:, None, :] - mus[None, :, :]) ** 2).sum(-1)
        pred[te] = np.asarray(classes)[dist.argmin(1)]
    aucs = [auc(proj[y == c, i], proj[y != c, i])
            for i, c in enumerate(classes)]
    return (float(np.mean(aucs)), float((pred == y).mean()),
            kept, dead, [round(a, 4) for a in aucs])


def measure(X, y, denoise, seed):
    """The real score and its label-permutation null: 200 draws, each one
    shuffling the labels and redoing the ENTIRE procedure."""
    y = np.asarray(y)
    classes = sorted(np.unique(y).tolist())
    rng = np.random.default_rng(seed)
    fold_sets = folds(len(y), N_FOLDS, rng)
    sep, acc, kept, dead, per_class = score_once(
        X, y, classes, denoise, fold_sets)
    null_sep, null_acc = [], []
    for _ in range(N_PERM):
        yp = rng.permutation(y)
        s, a, _, _, _ = score_once(X, yp, classes, denoise, fold_sets)
        null_sep.append(s)
        null_acc.append(a)
    m, sd = float(np.mean(null_sep)), float(np.std(null_sep, ddof=1))
    rec = {
        "denoised": bool(denoise),
        "separation": round(sep, 4),
        "separation_per_agent": per_class,
        "null_mean": round(m, 4),
        "null_sd": round(sd, 4),
        "margin_sd": round((sep - m) / sd, 2) if sd > 0 else None,
        "clears_3sd": bool(sd > 0 and sep >= m + SD_BAR * sd),
        "nearest_average_accuracy": round(acc, 4),
        "nearest_average_null_mean": round(float(np.mean(null_acc)), 4),
        "nearest_average_note": (
            "on the same scale as the five probe accuracies in "
            "blind-control-findings.md (no information 0.25); reported "
            "so the two tables read against each other, and carrying no "
            "outcome cell"),
        "components_removed_per_fold": kept,
        "n": int(len(y)),
        "no_information_value": NO_INFORMATION,
    }
    bad = []
    if sd == 0:
        bad.append("the label-permutation null has zero spread, so the "
                   "three-standard-deviation comparison would compare a "
                   "number to itself")
    if abs(sep - NO_INFORMATION) < 1e-12:
        bad.append("the separation score is exactly the no-information "
                   "value")
    if dead:
        bad.append("a fold left the procedure with nothing to fit: either "
                   "an owning agent is missing from a training split, or "
                   "the nuisance directions span the whole space")
    if bad:
        rec["degenerate"] = bad
        rec["clears_3sd"] = False
    return rec


# ------------------------------------------------------------- the cells

def cells(layers):
    """The outcome cells fixed in `denoised-direction-method.md`, read
    across every layer of one checkpoint. The run-level cell is assembled
    across checkpoints by `summarize_run`."""
    live = [r for r in layers.values() if "degenerate" not in r["denoised_arm"]]
    if not live:
        return {"cell": "DEGENERATE THROUGHOUT — no cell assigned",
                "means": "every layer tripped a precondition stated in "
                         "advance; the diagnostic failed to run rather "
                         "than answered"}
    cleared = {k: r for k, r in layers.items()
               if r["denoised_arm"].get("clears_3sd")}
    if not cleared:
        return {"cell": "DOES NOT SEPARATE",
                "layers_cleared": [],
                "means": "own-agent identity is not linearly decodable at "
                         "the probed positions on this checkpoint, even "
                         "after the loudest ownership-irrelevant "
                         "directions are removed"}
    because_denoising = []
    for k, r in cleared.items():
        raw = r["undenoised_arm"]
        dm = r["denoised_arm"]["margin_sd"]
        rm = raw.get("margin_sd")
        if not raw.get("clears_3sd") or (
                rm is not None and dm is not None and dm > rm):
            because_denoising.append(k)
    if because_denoising:
        return {"cell": "SEPARATES",
                "layers_cleared": sorted(cleared, key=int),
                "layers_where_denoising_is_why": sorted(
                    because_denoising, key=int),
                "means": "the ownership signal is linearly present at the "
                         "probed positions and the nuisance variation was "
                         "hiding it; the stack was insensitive rather "
                         "than the signal absent"}
    return {"cell": "SEPARATES, BUT NOT BECAUSE OF THE DENOISING",
            "layers_cleared": sorted(cleared, key=int),
            "layers_where_denoising_is_why": [],
            "means": "a linear read of own-agent identity exists at these "
                     "positions and the five probes missed it for some "
                     "other reason; projecting out the nuisance "
                     "directions is not what did it"}


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int) -> dict:
    lock_guard.require_known_answer_pass()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    pairs = L.paired_episodes(n_pairs, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    acts, eps = L.residuals_at(model, flat, device)
    y = np.asarray([e.own_slot for e in eps])
    counts = {int(c): int((y == c).sum()) for c in sorted(set(y.tolist()))}

    layers = {}
    for Lr in PROBE_LAYERS:
        X = np.asarray(acts[Lr], dtype=np.float64)
        layers[str(Lr)] = {
            "layer": Lr,
            "dimensions": int(X.shape[1]),
            "denoised_arm": measure(X, y, True, seed=Lr),
            "undenoised_arm": measure(X, y, False, seed=Lr),
        }
        d = layers[str(Lr)]["denoised_arm"]
        print(f"layer {Lr}: denoised separation {d['separation']} "
              f"({d['margin_sd']} sd) clears={d['clears_3sd']}", flush=True)

    return {
        "diagnostic": "denoised own-agent direction (Pain Axis note, "
                      "item 2)",
        "registered": False,
        "method_file": "denoised-direction-method.md",
        "method_committed_before_output": True,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "episodes": {"pairs_requested": n_pairs, "episodes_probed": len(y),
                     "content_seed": EPISODE_SEED,
                     "positions": "revision (localize_a3.residuals_at)",
                     "label_counts": counts,
                     "no_information_accuracy": round(1 / len(counts), 4)},
        "settings": {"probe_layers": PROBE_LAYERS, "folds": N_FOLDS,
                     "permutations": N_PERM, "sd_bar": SD_BAR,
                     "control_variance_kept": VARIANCE_KEPT},
        "layers": layers,
        "checkpoint_cell": cells(layers),
        "limits": (
            "UNREGISTERED. A separation above the null would show the "
            "localization stack was insensitive rather than the signal "
            "absent; it would NOT show that what separates is a carried "
            "self-index rather than the acting channel's input trace "
            "passed forward (red-team objection R1). Fifteen tests across "
            "three checkpoints at a three-standard-deviation bar clear by "
            "chance about two per cent of the time, so the count of "
            "clearances matters and is reported."),
        "elapsed_sec": round(time.time() - t0, 1),
    }


def summarize_run(records: list[dict]) -> dict:
    """The cell across every checkpoint, and the count of the family."""
    per = {r["checkpoint"]: r["checkpoint_cell"]["cell"] for r in records}
    tests, cleared = 0, []
    for r in records:
        for k, lr in r["layers"].items():
            tests += 1
            if lr["denoised_arm"].get("clears_3sd"):
                cleared.append({"checkpoint": r["checkpoint"], "layer": k,
                                "margin_sd": lr["denoised_arm"]["margin_sd"]})
    separates = [c for c in per.values() if c.startswith("SEPARATES")]
    if not separates:
        live = [c for c in per.values() if not c.startswith("DEGENERATE")]
        cell = "DOES NOT SEPARATE" if live else \
            "DEGENERATE THROUGHOUT — no cell assigned"
    elif any(c == "SEPARATES" for c in per.values()):
        cell = "SEPARATES"
    else:
        cell = "SEPARATES, BUT NOT BECAUSE OF THE DENOISING"
    return {
        "cell": cell, "per_checkpoint": per,
        "denoised_tests_run": tests,
        "denoised_tests_cleared": len(cleared),
        "cleared": cleared,
        "triggers_blind_control_rerun": cell.startswith("SEPARATES"),
        "trigger_note": (
            "John's instruction of 2026-09-19: a separation above the null "
            "on ANY checkpoint reruns the blind-arm positive control under "
            "the signed rule on the pilot and seeds 1 and 2 at 800 paired "
            "episodes. No separation anywhere means say so and stop."),
    }


# ----------------------------------------------------------- the self-test

def self_test() -> None:
    rng = np.random.default_rng(0)
    n, dim = 240, 40
    y = np.asarray([i % 4 for i in range(n)])

    # A planted signal under nuisance variation shaped the way the
    # hypothesis says the real thing is shaped: most of the variation in
    # a few very loud directions, with the ownership signal small and
    # elsewhere. This is the case the denoising is supposed to rescue,
    # and it is what the fixture has to contain for the contrast arm to
    # mean anything.
    #
    # It will NOT rescue every case, and the first version of this
    # fixture was one it cannot: six nuisance directions of equal size,
    # where removing half the variation leaves three still louder than
    # the signal. Both arms then landed BELOW the no-information value,
    # because a difference of averages fitted on noisy training folds can
    # point the wrong way on held-out episodes. That is worth knowing —
    # it is a mechanism by which a read can land below its own null, which
    # is what the five real probes did — so it is kept as its own check
    # rather than quietly deleted.
    sig = np.zeros((n, dim))
    for c in range(4):
        v = np.zeros(dim)
        v[4 + c] = 1.0
        sig[y == c] = v
    loud = rng.normal(0, 1, (n, 1)) @ np.eye(1, dim) * 30.0
    X = sig * 1.0 + loud + rng.normal(0, 0.3, (n, dim))

    C = control_condition(X, y)
    for c in range(4):
        assert abs(C[y == c].mean()) < 1e-9, "each class must centre to zero"
    V, k, frac = nuisance_components(C)
    assert 1 <= k <= dim and frac >= VARIANCE_KEPT, "half the variation"
    assert k == 1, "one loud direction should be reached by one component"

    # HOW THIS RECIPE CAN LEAVE THE NUISANCE STANDING, found while
    # building the fixture and worth a check of its own. "Half the
    # variation" stops at the first component that crosses the line. Two
    # loud directions of similar size, and the first may cross it alone,
    # leaving the second untouched and still louder than the signal. This
    # is a property of the rule item 2 prescribes, not a bug, and the
    # count of components removed is reported per layer so a run that
    # lands in it can be recognised rather than guessed at.
    two = rng.normal(0, 1, (n, 2)) @ np.eye(2, dim) * 30.0
    V2, k2, _ = nuisance_components(control_condition(two, y))
    if k2 == 1:
        left = project_out(two, V2)
        assert left[:, :2].std(0).max() > 10.0, \
            "a second loud direction can survive removing half the "\
            "variation; that is the property being recorded here"
    P = project_out(X, V)
    assert abs((P @ V.T).max()) < 1e-8, "the nuisance span must be gone"

    # the separation score behaves: perfect, reversed, and no information
    assert auc(np.array([3.0, 4.0]), np.array([1.0, 2.0])) == 1.0
    assert auc(np.array([1.0, 2.0]), np.array([3.0, 4.0])) == 0.0
    assert auc(np.array([1.0, 1.0]), np.array([1.0, 1.0])) == 0.5

    # nothing fitted may see the held-out fold: scoring pure noise with
    # labels that carry no signal must sit at the no-information value,
    # not above it. A leak here shows up as separation on noise.
    Z = rng.normal(0, 1, (n, dim))
    leak = score_once(Z, y, [0, 1, 2, 3], True,
                      folds(n, N_FOLDS, np.random.default_rng(1)))[0]
    assert abs(leak - NO_INFORMATION) < 0.12, \
        f"held-out separation on pure noise should be near 0.5, got {leak}"

    # the planted signal is found once the nuisance directions are gone,
    # and the contrast arm is what says the denoising is why
    fs = folds(n, N_FOLDS, np.random.default_rng(2))
    den = score_once(X, y, [0, 1, 2, 3], True, fs)[0]
    raw = score_once(X, y, [0, 1, 2, 3], False, fs)[0]
    assert den > raw, f"denoising must help here (denoised {den}, raw {raw})"
    assert den > 0.8, f"the planted signal should be recovered, got {den}"

    # The case the denoising cannot rescue, kept deliberately: nuisance
    # variation spread evenly over more directions than removing half of
    # it reaches. Both arms should fail, and either may land below the
    # no-information value rather than at it.
    flat = rng.normal(0, 1, (n, 6)) @ rng.normal(0, 1, (6, dim)) * 12.0
    Xf = sig * 0.6 + flat + rng.normal(0, 0.05, (n, dim))
    den_f = score_once(Xf, y, [0, 1, 2, 3], True, fs)[0]
    raw_f = score_once(Xf, y, [0, 1, 2, 3], False, fs)[0]
    assert den_f < 0.6 and raw_f < 0.6, (
        f"evenly spread loud nuisance should defeat both arms "
        f"(denoised {den_f}, raw {raw_f})")

    # the cells, exercised on hand-built layer records
    def rec(clears, margin, raw_clears=False, raw_margin=None, deg=False):
        d = {"clears_3sd": clears, "margin_sd": margin}
        if deg:
            d["degenerate"] = ["stated in advance"]
            d["clears_3sd"] = False
        return {"denoised_arm": d,
                "undenoised_arm": {"clears_3sd": raw_clears,
                                   "margin_sd": raw_margin}}

    assert cells({"3": rec(False, 0.4)})["cell"] == "DOES NOT SEPARATE"
    assert cells({"3": rec(True, 9.0)})["cell"] == "SEPARATES"
    c = cells({"3": rec(True, 9.0, raw_clears=True, raw_margin=9.5)})
    assert c["cell"] == "SEPARATES, BUT NOT BECAUSE OF THE DENOISING", \
        "a raw arm clearing by more means the denoising is not why"
    c = cells({"3": rec(True, 12.0, raw_clears=True, raw_margin=4.0)})
    assert c["cell"] == "SEPARATES", "a bigger denoised margin still counts"
    assert cells({"3": rec(False, None, deg=True)})["cell"].startswith(
        "DEGENERATE"), "a precondition stated in advance assigns no cell"

    # the run-level cell and the trigger
    def ck(name, cell):
        return {"checkpoint": name, "checkpoint_cell": {"cell": cell},
                "layers": {"3": {"denoised_arm": {
                    "clears_3sd": cell.startswith("SEPARATES"),
                    "margin_sd": 9.0}}}}

    s = summarize_run([ck("a.pt", "DOES NOT SEPARATE"),
                       ck("b.pt", "SEPARATES")])
    assert s["cell"] == "SEPARATES" and s["triggers_blind_control_rerun"]
    assert s["denoised_tests_run"] == 2 and s["denoised_tests_cleared"] == 1
    s = summarize_run([ck("a.pt", "DOES NOT SEPARATE"),
                       ck("b.pt", "DOES NOT SEPARATE")])
    assert s["cell"] == "DOES NOT SEPARATE"
    assert s["triggers_blind_control_rerun"] is False, \
        "no separation anywhere must not trigger the rerun"

    # the known-answer gate is real
    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass
    print("self-test OK — control condition, half-variance components, "
          "projection, separation score, no held-out leak, planted signal "
          "recovered, all cells, the run-level trigger and the "
          "known-answer gate; no checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=N_PAIRS)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    ap.add_argument("--summary", type=Path, default=None)
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    records = []
    for c in a.ckpt:
        out = a.out_dir / f"denoised_direction_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}  cell: {rec['checkpoint_cell']['cell']}")
        records.append(rec)
    s = summarize_run(records)
    path = a.summary or (a.out_dir / "denoised_direction_a3_summary.json")
    if path.exists():
        raise SystemExit(f"{path} exists; refusing to overwrite")
    path.write_text(json.dumps(s, indent=2))
    print(json.dumps(s, indent=2))


if __name__ == "__main__":
    main()
