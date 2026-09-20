"""A powered test of a well-posed target: is own-agent identity carried?

**UNREGISTERED**, diagnostic only. The method is committed in
`powered-target-test-method.md`, in the same commit as this file and
before either produced any output. Read that first: it fixes the cells.

WHY. The position sweep established that `own_slot` — the generator's
index for whichever agent the model is, and the target every probe in
this stack has predicted — cannot be recovered from the model's states in
principle. For every one of its four values, all four register indices
and all twenty-five marker words occur.

That left one well-posed question, asked in passing and badly
underpowered: the model's OWN MARKER WORD, read at the registered anchor.
The marker has not been emitted yet there — it comes after the value — so
a model that knows which agent it is would have to be CARRYING it. Unlike
the generator index this target is decodable in principle, which is what
makes a null mean something.

WHAT IS FIXED HERE. 4,000 episodes instead of 400, so each of the 25
marker words falls to the model about 160 times instead of 16. And 1,000
permutation draws instead of 50, because with 200 draws the finest
resolvable probability is 0.005 while a three-standard-deviation margin
sits at 0.0013 — the bar in use could not be checked against the draws at
all. Now it can, and every test reports the count.

ARM 1 is the marker word. ARM 2 is the register index, through an
identical procedure: consistently defined, recoverable from the input
once all four markers have appeared, and found above its null on two
checkpoints and below on the third by the underpowered look. That
inconsistency is what arm 2 is powered to settle.

THE POSITIVE CONTROL is the marker word read at the MARKER POSITION, two
tokens along, where it is the input token. It tests the READ. A checkpoint
whose positive control fails cannot have its anchor result interpreted.

THE SCORER IS A VECTORISED REWRITE of the one the sweep used — the same
mathematics as matrix products, about twelve times faster, which is what
makes 1,000 draws affordable. It is not a new method and must not become
one by accident: the self-test checks it against the original and
requires agreement to 1e-12 on accuracy and 1e-9 on separation, on a
noise case and a planted-signal case. If they disagree the run refuses.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock,
for the reason given in the method file; fresh output per checkpoint,
nothing overwritten [C6].

    ../../../.venv/bin/python powered_target_test_a3.py --self-test
    ../../../.venv/bin/python powered_target_test_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import denoised_direction_a3 as D
import encoding_a3 as E
import lock_guard
import localize_a3 as L
from model import MVM0aModel, Config, to_torch

PROBE_LAYERS = L.PROBE_LAYERS
N_PAIRS = 2000                 # 4,000 episodes
EPISODE_SEED = 20260917        # unchanged, so the episodes are the same ones
N_PERM = 1000                  # resolves a three-standard-deviation margin
N_FOLDS = 4
SD_BAR = 3.0
FAMILY_SD_BAR = 3.06           # strictest reading: all 45 tests
CHUNK = 250                    # episodes per capture pass
TURN_SPAN = 7                  # six words and a line break

ANCHOR = "anchor"
MARKER = "marker_position"
ARMS = ("marker_word", "register_index")


# ------------------------------------------------------------- the scorer

def score_fast(X, y, classes, fold_sets, want_auc=True):
    """Held-out nearest-average accuracy and macro separation, fitting
    every quantity on the training folds only.

    Identical in mathematics to `denoised_direction_a3.score_once` with
    denoising off, expressed as matrix products. The class averages come
    from one indicator matrix product; the average of the rest follows
    from the total minus that class's sum; the nearest average is found
    by `2 x.mu - |mu|^2` rather than by forming every difference, which is
    what keeps 1,000 draws affordable.
    """
    n, d = X.shape
    C = len(classes)
    cls_index = {c: i for i, c in enumerate(classes)}
    yi = np.array([cls_index[v] for v in y], dtype=np.int64)
    proj = np.zeros((n, C), dtype=np.float64)
    pred = np.empty(n, dtype=np.int64)
    dead = False
    for held in fold_sets:
        mask = np.zeros(n, dtype=bool)
        mask[held] = True
        tr = ~mask
        Xtr, Xte, ytr = X[tr], X[mask], yi[~mask]
        onehot = np.zeros((C, len(ytr)))
        onehot[ytr, np.arange(len(ytr))] = 1.0
        counts = onehot.sum(1)
        if (counts == 0).any():
            dead = True
        sums = onehot @ Xtr
        nz = counts > 0
        mus = np.zeros((C, d))
        mus[nz] = sums[nz] / counts[nz, None]
        total, ntr = Xtr.sum(0), len(ytr)
        denom = ntr - counts
        ok = denom > 0
        rest = np.zeros((C, d))
        rest[ok] = (total - sums[ok]) / denom[ok, None]
        Dm = mus - rest
        nrm = np.linalg.norm(Dm, axis=1)
        Dm[nrm > 0] /= nrm[nrm > 0, None]
        proj[mask] = Xte @ Dm.T
        sc = 2.0 * (Xte @ mus.T) - (mus ** 2).sum(1)
        sc[:, ~nz] = -np.inf
        pred[mask] = sc.argmax(1)
    acc = float((pred == yi).mean())
    if not want_auc:
        return acc, None, dead
    order = np.argsort(proj, axis=0, kind="mergesort")
    ranks = np.empty_like(proj)
    ar = np.arange(1, n + 1, dtype=np.float64)
    for i in range(C):
        ranks[order[:, i], i] = ar
    aucs = []
    for i in range(C):
        pos = yi == i
        npos = int(pos.sum())
        if npos == 0 or npos == n:
            continue
        rs = ranks[pos, i].sum()
        aucs.append((rs - npos * (npos + 1) / 2.0) / (npos * (n - npos)))
    return acc, (float(np.mean(aucs)) if aucs else None), dead


def verify_scorer_matches_original():
    """The vectorised scorer must be the old one, not a new method. Run
    before anything reports; a disagreement stops the run."""
    rng = np.random.default_rng(0)
    n, d, C = 400, 60, 25
    X = rng.normal(0, 1, (n, d))
    y = np.array([i % C for i in range(n)])
    classes = sorted(set(y.tolist()))
    fs = D.folds(n, N_FOLDS, np.random.default_rng(3))
    checks = []
    for tag, Xc in (("noise", X), ("planted signal", None)):
        if Xc is None:
            Xc = X.copy()
            for c in range(C):
                Xc[y == c, c % d] += 3.0
        sep_o, acc_o, _, _, _ = D.score_once(Xc, y, classes, False, fs)
        acc_n, sep_n, _ = score_fast(Xc, y, classes, fs)
        checks.append({"case": tag,
                       "accuracy_difference": abs(acc_o - acc_n),
                       "separation_difference": abs(sep_o - sep_n)})
        if abs(acc_o - acc_n) > 1e-12 or abs(sep_o - sep_n) > 1e-9:
            raise SystemExit(
                f"REFUSING to report: the vectorised scorer disagrees with "
                f"denoised_direction_a3.score_once on the {tag} case "
                f"(accuracy {acc_o} vs {acc_n}, separation {sep_o} vs "
                f"{sep_n}). It is meant to be the same measurement.")
    return checks


# --------------------------------------------------------------- capture

def position_indices(ep):
    """The two positions, from the template. A turn beginning at s has its
    value at s+3 and the agent's own marker at s+5; the marker comes AFTER
    the value, so at the anchor the turn has not said whose turn it is."""
    rev = A.own_revision_index(ep)
    act = 1 + TURN_SPAN * rev + A.VALUE_WORD_IDX
    return {ANCHOR: act - 1, MARKER: act + 2}


@torch.no_grad()
def capture(model, eps, device, chunk=CHUNK):
    """States at the two positions, per layer, in chunks so 4,000 episodes
    fit in memory. Chunking changes nothing: the model is causal and every
    episode is encoded independently."""
    out = {(Lr, p): [] for Lr in PROBE_LAYERS for p in (ANCHOR, MARKER)}
    kept = []
    rng = random.Random(0)
    for e in eps:
        A.enact_own_turns(e, rng)
    for start in range(0, len(eps), chunk):
        part = eps[start:start + chunk]
        encs = [E.encode_episode(e) for e in part]
        batch = to_torch(E.collate(encs), device)
        B, Ltok = batch["input_ids"].shape
        act = torch.zeros(B, Ltok, model.cfg.d_model, device=device)
        own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
                   for e in part]
        for k in range(max(len(o) for o in own_idx)):
            _, h = model.forward(batch, act_inject=act, return_hidden=True)
            bs, ps = [], []
            for b, e in enumerate(part):
                if k < len(own_idx[b]):
                    sp = (batch["turn_ids"][b]
                          == own_idx[b][k]).nonzero().flatten()
                    bs.append(b)
                    ps.append(int(sp[0]) + A.VALUE_WORD_IDX)
            bi = torch.tensor(bs, device=device)
            pi = torch.tensor(ps, device=device)
            act = act.index_put((bi, pi), model.act_proj(h[bi, pi - 1]))

        caps = {Lr: [] for Lr in PROBE_LAYERS}
        for Lr in PROBE_LAYERS:
            blk = model.blocks[Lr]
            orig = blk.forward

            def patched(x, kv, reg_repr, _o=orig, _L=Lr):
                x, ctx = _o(x, kv, reg_repr)
                caps[_L].append(x.detach())
                return x, ctx
            blk.forward = patched
        model.forward(batch, act_inject=act)
        for Lr in PROBE_LAYERS:
            del model.blocks[Lr].__dict__["forward"]

        idx = [position_indices(e) for e in part]
        rows = [b for b, e in enumerate(part)
                if all(0 <= idx[b][p] < len(encs[b]["input_ids"])
                       for p in (ANCHOR, MARKER))]
        kept += [start + b for b in rows]
        for Lr in PROBE_LAYERS:
            hs = torch.cat(caps[Lr], dim=1)
            bi = torch.tensor(rows, device=hs.device)
            for p in (ANCHOR, MARKER):
                pos = torch.tensor([idx[b][p] for b in rows], device=hs.device)
                out[(Lr, p)].append(hs[bi, pos].float().cpu().numpy())
    return ({k: np.concatenate(v, axis=0) for k, v in out.items()}, kept)


def targets(eps):
    """The two well-posed targets. `own_slot` is deliberately absent: the
    sweep established it is unrecoverable and the question is closed."""
    mk = np.asarray([E.VOCAB[e.markers[e.own_slot]] for e in eps])
    reg = np.asarray([
        sorted(range(e.n_agents), key=lambda a: E.VOCAB[e.markers[a]])
        .index(e.own_slot) for e in eps])
    return {"marker_word": mk, "register_index": reg}


# --------------------------------------------------------------- measure

def measure(X, y, seed):
    """The read and its 1,000-draw null, with the count beside the
    margin because the count is what the draws can actually show."""
    y = np.asarray(y)
    classes = sorted(np.unique(y).tolist())
    fs = D.folds(len(y), N_FOLDS, np.random.default_rng(seed))
    rng = np.random.default_rng(seed + 1)
    acc, sep, dead = score_fast(X, y, classes, fs)
    na, ns = [], []
    for _ in range(N_PERM):
        a, s, _ = score_fast(X, rng.permutation(y), classes, fs)
        na.append(a)
        ns.append(s)
    vals, counts = np.unique(y, return_counts=True)
    majority = float(counts.max() / len(y))
    out = {"classes": int(len(classes)), "n": int(len(y)),
           "no_information": round(1 / len(classes), 4),
           "majority_class_rate": round(majority, 4),
           "examples_per_class_min": int(counts.min()),
           "examples_per_class_median": int(np.median(counts)),
           "draws": N_PERM}
    for tag, real, null in (("accuracy", acc, na), ("separation", sep, ns)):
        if real is None:
            continue
        m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
        margin = round((real - m) / sd, 2) if sd > 0 else None
        beat = int(sum(1 for v in null if v >= real - 1e-12))
        clears = bool(sd > 0 and real >= m + SD_BAR * sd)
        out[tag] = {
            "value": round(real, 4), "null_mean": round(m, 4),
            "null_sd": round(sd, 5), "margin_sd": margin,
            "clears_3sd": clears, "draws_beating_real": beat,
            "beats_majority_class": bool(real > majority)
            if tag == "accuracy" else None,
            "label": ("ROBUST" if (clears and margin is not None
                                   and margin >= FAMILY_SD_BAR and beat == 0)
                      else "MARGINAL" if clears else None)}
    bad = []
    if out["accuracy"]["null_sd"] == 0:
        bad.append("the permutation null has zero spread")
    if abs(acc - majority) < 1e-12:
        bad.append("accuracy exactly equals the majority-class rate")
    if dead:
        bad.append("a class was missing from a training fold")
    if bad:
        out["degenerate"] = bad
        out["accuracy"]["clears_3sd"] = False
    return out


# ----------------------------------------------------------------- cells

def arm_cell(per_checkpoint, pilot_name):
    """The cells fixed in `powered-target-test-method.md`, for one arm.

    `per_checkpoint` maps a checkpoint name to
    {"control_holds": bool, "anchor_clears": bool}.
    """
    pilot = per_checkpoint.get(pilot_name)
    if pilot is None:
        return {"cell": "NO PILOT IN THIS RUN — no cell assigned"}
    if not pilot["control_holds"]:
        return {"cell": "UNREADABLE",
                "means": ("the positive control fails on the pilot, the "
                          "checkpoint the read works best on, so nothing "
                          "in this arm can be interpreted")}
    excluded = [k for k, v in per_checkpoint.items()
                if not v["control_holds"]]
    readable = {k: v for k, v in per_checkpoint.items() if v["control_holds"]}
    clears = sorted(k for k, v in readable.items() if v["anchor_clears"])
    others = [k for k in clears if k != pilot_name]
    if pilot_name in clears and others:
        return {"cell": "CARRIED", "clears_on": clears,
                "excluded_checkpoints": excluded,
                "means": ("these models carry an own-agent identity to the "
                          "decision point, in a form a linear difference of "
                          "averages can find. It would not settle red-team "
                          "objection R1: what is carried may be the acting "
                          "channel's trace passed forward")}
    if not clears and not excluded:
        return {"cell": "NOT CARRIED", "clears_on": [],
                "excluded_checkpoints": [],
                "means": ("with the target well posed, the power adequate "
                          "and the read demonstrably working two tokens "
                          "away, own-agent identity is still not linearly "
                          "present at the registered position. An "
                          "informative null, not a broken instrument")}
    return {"cell": "FITS NO CELL — reported as fitting none",
            "clears_on": clears, "excluded_checkpoints": excluded,
            "means": ("the pattern is neither the pilot plus another seed, "
                      "nor nothing anywhere with every control holding. "
                      "The method file names this outcome in advance rather "
                      "than forcing it into a bin it does not belong in")}


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int) -> dict:
    lock_guard.require_known_answer_pass()
    checks = verify_scorer_matches_original()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    pairs = L.paired_episodes(n_pairs, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, kept = capture(model, flat, device)
    eps = [flat[i] for i in kept]
    tg = targets(eps)
    print(f"  captured {len(eps)} episodes", flush=True)

    results = {}
    for arm in ARMS:
        y = tg[arm]
        for pos in (ANCHOR, MARKER):
            for Lr in PROBE_LAYERS:
                results[f"{arm}|{pos}|{Lr}"] = measure(
                    states[(Lr, pos)], y, seed=Lr)
            best = max(PROBE_LAYERS,
                       key=lambda k: results[f"{arm}|{pos}|{k}"]
                       ["accuracy"]["value"])
            r = results[f"{arm}|{pos}|{best}"]["accuracy"]
            print(f"  {arm:15s} {pos:15s} best layer {best}: "
                  f"accuracy {r['value']} (majority "
                  f"{results[f'{arm}|{pos}|{best}']['majority_class_rate']}, "
                  f"{r['margin_sd']} sd, {r['draws_beating_real']}/{N_PERM} "
                  f"draws beat it) clears={r['clears_3sd']}", flush=True)

    control_holds = any(
        results[f"marker_word|{MARKER}|{Lr}"]["accuracy"]["clears_3sd"]
        for Lr in PROBE_LAYERS)
    per_arm = {}
    for arm in ARMS:
        per_arm[arm] = {
            "control_holds": bool(control_holds),
            "anchor_clears": bool(any(
                results[f"{arm}|{ANCHOR}|{Lr}"]["accuracy"]["clears_3sd"]
                for Lr in PROBE_LAYERS)),
            "anchor_layers_clearing": [
                Lr for Lr in PROBE_LAYERS
                if results[f"{arm}|{ANCHOR}|{Lr}"]["accuracy"]["clears_3sd"]],
        }

    return {
        "diagnostic": "powered test of a well-posed own-agent target",
        "registered": False, "verdict_bearing": False,
        "method_file": "powered-target-test-method.md",
        "method_committed_before_output": True,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "scorer_agrees_with_original": checks,
        "settings": {"episodes": len(eps), "pairs_requested": n_pairs,
                     "content_seed": EPISODE_SEED, "permutations": N_PERM,
                     "folds": N_FOLDS, "sd_bar": SD_BAR,
                     "family_sd_bar": FAMILY_SD_BAR,
                     "probe_layers": PROBE_LAYERS,
                     "positions": {ANCHOR: "act_pos - 1, the registered "
                                           "probe position; the model's own "
                                           "marker has NOT appeared yet",
                                   MARKER: "act_pos + 2, the model's own "
                                           "marker as an input token — THE "
                                           "POSITIVE CONTROL"},
                     "arms": list(ARMS)},
        "results": results,
        "per_arm": per_arm,
        "positive_control_holds": bool(control_holds),
        "limits": (
            "UNREGISTERED and diagnostic. One statistic, linear, one "
            "position, five layers, 30-million-parameter models on a "
            "synthetic grammar. A null is consistent with identity being "
            "carried non-linearly, or distributed, or at an untested "
            "position. A clearance would not establish that what is carried "
            "is a self-index rather than the acting channel's input trace "
            "passed forward (red-team objection R1)."),
        "elapsed_sec": round(time.time() - t0, 1),
    }


def summarize_run(records, pilot="a3_30m_seed0.pt"):
    out = {"pilot": pilot, "checkpoints": [r["checkpoint"] for r in records],
           "arms": {}}
    for arm in ARMS:
        per = {r["checkpoint"]: r["per_arm"][arm] for r in records}
        out["arms"][arm] = {"cell": arm_cell(per, pilot)["cell"],
                            "detail": arm_cell(per, pilot),
                            "per_checkpoint": per}
    out["discovery_tests"] = len(ARMS) * len(PROBE_LAYERS) * len(records)
    out["note"] = ("diagnostic only; no verdict is read and no registered "
                   "text is touched")
    return out


# ------------------------------------------------------------- self-test

def self_test() -> None:
    checks = verify_scorer_matches_original()
    for c in checks:
        assert c["accuracy_difference"] <= 1e-12, c
        assert c["separation_difference"] <= 1e-9, c

    # the two positions, against real encodings rather than my arithmetic
    pairs = L.paired_episodes(8, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    for e in flat:
        enc = E.encode_episode(e)
        idx = position_indices(e)
        ids = enc["input_ids"]
        assert idx[ANCHOR] == int(enc["act_pos"]) - 1, "the anchor"
        assert E.IVOCAB[int(ids[idx[MARKER]])] == e.markers[e.own_slot], \
            "the positive control must be the model's own marker"
        assert E.IVOCAB[int(ids[idx[ANCHOR]])] != e.markers[e.own_slot], \
            "the anchor must not already hold the marker"
        for p in (ANCHOR, MARKER):
            assert 0 <= idx[p] < len(ids), f"{p} out of range"

    # the targets invert
    tg = targets(flat)
    for e, m in zip(flat, tg["marker_word"]):
        assert E.IVOCAB[int(m)] == e.markers[e.own_slot]
    for e, r in zip(flat, tg["register_index"]):
        order = sorted(range(e.n_agents), key=lambda a: E.VOCAB[e.markers[a]])
        assert order[r] == e.own_slot
    assert "own_slot" not in tg, "the unrecoverable target stays out"

    # the label, now that 1,000 draws can resolve the bar
    rng = np.random.default_rng(1)
    n, d, C = 600, 40, 4
    y = np.array([i % C for i in range(n)])
    X = rng.normal(0, 1, (n, d))
    for c in range(C):
        X[y == c, c] += 2.5
    r = measure(X, y, seed=0)
    assert r["accuracy"]["clears_3sd"], "a planted signal must clear"
    assert r["accuracy"]["label"] == "ROBUST", "and be robust"
    assert r["accuracy"]["draws_beating_real"] == 0
    assert r["accuracy"]["beats_majority_class"] is True
    assert r["draws"] == 1000, "the null must actually be 1,000 draws"
    Z = rng.normal(0, 1, (n, d))
    rz = measure(Z, y, seed=0)
    assert not rz["accuracy"]["clears_3sd"], "noise must not clear"
    assert rz["accuracy"]["label"] is None

    # the cells
    P = "a3_30m_seed0.pt"
    def pc(**kw):
        return {"control_holds": True, "anchor_clears": False, **kw}
    assert arm_cell({P: pc(control_holds=False)}, P)["cell"] == "UNREADABLE"
    assert arm_cell({P: pc(), "b.pt": pc()}, P)["cell"] == "NOT CARRIED"
    assert arm_cell({P: pc(anchor_clears=True),
                     "b.pt": pc(anchor_clears=True)}, P)["cell"] == "CARRIED"
    # pilot alone is NOT carried-by-two-checkpoints, and must not be forced
    assert arm_cell({P: pc(anchor_clears=True), "b.pt": pc()},
                    P)["cell"].startswith("FITS NO CELL")
    # seeds but not the pilot likewise
    assert arm_cell({P: pc(), "b.pt": pc(anchor_clears=True)},
                    P)["cell"].startswith("FITS NO CELL")
    # nothing anywhere but a control failed on a seed: not a clean null
    assert arm_cell({P: pc(), "b.pt": pc(control_holds=False)},
                    P)["cell"].startswith("FITS NO CELL")

    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass
    print("self-test OK — the vectorised scorer agrees with the original to "
          "1e-12 on accuracy and 1e-9 on separation (noise and planted "
          "signal), both positions check against real encodings, both "
          "targets invert, the 1,000-draw null resolves the bar, every cell "
          "including the fits-none cases, and the known-answer gate; no "
          "checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=N_PAIRS)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    records = []
    for c in a.ckpt:
        out = a.out_dir / f"powered_target_test_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)
        records.append(rec)
    s = summarize_run(records)
    path = a.out_dir / "powered_target_test_a3_summary.json"
    if path.exists():
        raise SystemExit(f"{path} exists; refusing to overwrite")
    path.write_text(json.dumps(s, indent=2))
    print(json.dumps({k: v["cell"] for k, v in s["arms"].items()}, indent=2))


if __name__ == "__main__":
    main()
