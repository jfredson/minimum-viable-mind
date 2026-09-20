"""The fitted linear read at all eleven positions: is identity found anywhere?

**UNREGISTERED**, diagnostic only. The method is committed in
`fitted-position-sweep-method.md`, in the same commit as this file and
before either produced any output. Read that first: it fixes the cells.

WHY. The powered eleven-position sweep read every position with a plain
difference of averages and found nothing at any of the nine testable
ones. But on these same checkpoints, at the position where the answer is
sitting in plain sight as the input token, that read scores 0.25 to
0.2675 while the fitted classifier already written in
`probe_target_diagnostic_a3.py` scores 0.48 to 0.535, against a
no-information rate of 0.25. The read used for the sweep is about half as
sensitive as one that was already built and never pointed at the nine
positions that matter. That is the red-team ledger's fatal finding
RT-33, and this run is the Gate B review's decision 2 answering it.

WHAT IS RUN. The same eleven positions, five layers and three 30-million-
parameter checkpoints as the powered sweep, 4,000 episodes, read with
that classifier, on the FOUR-ANSWER REGISTER-INDEX target.

THE MARKER-WORD TARGET IS NOT RUN, and the method file says so in advance
with the arithmetic: at 7.56 seconds a fit against the register index's
1.19, it would cost about 70 processor-hours against about 11, which does
not fit in a session on this machine.

THE CLASSIFIER IS NOT A NEW ONE. Same library, same squared penalty at
the same strength, same optimiser, same 2,000-pass cap, features left
unscaled — identical to `probe_target_diagnostic_a3.probe`, so that the
numbers already on the record can be used as an instrument check. The cap
is part of the instrument: at 400 episodes it is hit on every fold, so
the recorded numbers come from a fit that stopped early. Every fit
records how many passes it used.

SEEDING IS PER TEST (RT-39). The previous sweep gave all 270 of its tests
the same five fold splits and the same five sets of shuffled labels,
seeded by layer alone. Here both are seeded from a digest of the whole
test identity — checkpoint, target, position and layer — so no two of the
165 tests share a split or a draw.

THE ANCHOR REPRODUCTION RUNS FIRST. The fifteen recorded marker-position
numbers must come back to within one episode in 400 or the run is a
FAILED INSTRUMENT and reports nothing else.

THE POSITIVE CONTROL is position 6, the register index where all four
marker words have appeared. It is not guaranteed present, only guaranteed
derivable, and the method file states what that costs. A checkpoint
failing it is VOID.

THE NEGATIVE CONTROL is position 1, where the model's own marker has not
yet appeared anywhere. A clearance there is a leak, not carrying, and is
excluded from the cells.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock;
fresh output per checkpoint, nothing overwritten [C6].

    ../../../.venv/bin/python fitted_position_sweep_a3.py --self-test
    ../../../.venv/bin/python fitted_position_sweep_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
    ../../../.venv/bin/python fitted_position_sweep_a3.py --summarize
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import os
import shutil
import tempfile
import time
import warnings
from pathlib import Path

import numpy as np
import torch

import denoised_direction_a3 as D
import lock_guard
import localize_a3 as L
import position_sweep_a3 as S
import powered_position_sweep_a3 as W
import powered_target_test_a3 as P
from model import MVM0aModel, Config

PROBE_LAYERS = W.PROBE_LAYERS
N_PAIRS = W.N_PAIRS                  # 2,000 pairs = 4,000 episodes
EPISODE_SEED = W.EPISODE_SEED        # 20260917, the same episodes
N_PERM = 200                         # shuffled-label draws per test
N_FOLDS = 4
SD_BAR = 3.0                         # reported for continuity
FAMILY_SD_BAR = 3.38                 # 135 discovery tests, 5% family-wise
FAMILY_SD_EXACT = 3.3740             # applied rounded UP, never looser
ARM = "register_index"
MAX_ITER = 2000                      # part of the instrument; do not change
C_REG = 1.0                          # ditto

POSITIONS = W.POSITIONS
POSITIVE_CONTROL = W.POSITIVE_CONTROL        # own_revision_marker
NEGATIVE_CONTROL = W.NEGATIVE_CONTROL        # own_assign_1_value
TESTABLE = W.TESTABLE                        # the nine
PILOT = W.PILOT                              # a3_30m_seed0.pt

# The recorded fitted-classifier register-index accuracies at the marker
# position, 400 episodes, from `probe_target_diagnostic_a3_*.json`. Written
# here as a pre-stated claim AND checked against those files, so that
# neither can be quietly edited to fit the other.
ANCHOR_PAIRS = S.N_PAIRS             # 200 pairs = 400 episodes, as recorded
ANCHOR_TOL = 0.0025                  # one episode in 400
ANCHOR_RECORDED = {
    "a3_30m_seed0.pt": {3: 0.5025, 4: 0.5125, 5: 0.5225, 7: 0.5250,
                        8: 0.5175},
    "a3_30m_seed1.pt": {3: 0.4800, 4: 0.5250, 5: 0.5350, 7: 0.5275,
                        8: 0.5150},
    "a3_30m_seed2.pt": {3: 0.4600, 4: 0.4700, 5: 0.4950, 7: 0.4475,
                        8: 0.4825},
}


def key(pos, layer):
    return f"{ARM}|{pos}|{layer}"


def test_seed(ckpt_name, arm, pos, layer):
    """RT-39: the fold split and the shuffled draws are seeded from the
    WHOLE test identity, so no two tests share either."""
    tag = f"{ckpt_name}|{arm}|{pos}|{layer}"
    h = hashlib.blake2b(tag.encode(), digest_size=8).digest()
    return int.from_bytes(h, "big") % (2 ** 31 - 1)


# ---------------------------------------------------------- the classifier

def cv_from_folds(n, fold_sets):
    """The same held-out/training split the recorded run built."""
    return [(np.setdiff1d(np.arange(n), h), h) for h in fold_sets]


def fit_cv(X, y, cv):
    """Mean held-out accuracy across folds, with the optimiser's pass
    count, using the classifier exactly as `probe_target_diagnostic_a3`
    configures it.

    The mean of the per-fold accuracies is what `cross_val_score` returns,
    and it is what the recorded numbers are, so it is what is computed
    here rather than pooled accuracy."""
    from sklearn.linear_model import LogisticRegression
    y = np.asarray(y)
    n_classes = len(np.unique(y))
    scores, iters, dead = [], [], False
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for tr, te in cv:
            present = np.unique(y[tr])
            if len(present) < n_classes:
                dead = True
            if len(present) < 2:
                # the optimiser cannot be asked for a fit here; the fold
                # can only name the one class it saw. Flagged dead above,
                # so the test carries no cell either way.
                scores.append(float((y[te] == present[0]).mean()))
                iters.append(0)
                continue
            clf = LogisticRegression(max_iter=MAX_ITER,
                                     C=C_REG).fit(X[tr], y[tr])
            scores.append(float((clf.predict(X[te]) == y[te]).mean()))
            iters.append(int(np.max(clf.n_iter_)))
    return float(np.mean(scores)), iters, dead


def detectable_share(needed, reference):
    """RT-37's measure: the share of episodes that would have to be
    perfectly legible, the rest at chance, to reach `needed`."""
    if needed is None or reference >= 1.0:
        return None
    return round(max(0.0, (needed - reference) / (1.0 - reference)), 4)


def measure_fitted(X, y, seed, family_bar=FAMILY_SD_BAR, n_perm=N_PERM):
    """One test: the fitted read, its shuffled-label null, the pre-stated
    label, the degeneracy preconditions and the smallest signal it could
    have found."""
    y = np.asarray(y)
    n = len(y)
    fs = D.folds(n, N_FOLDS, np.random.default_rng(seed))
    cv = cv_from_folds(n, fs)
    rng = np.random.default_rng(seed + 1)

    acc, iters, dead = fit_cv(X, y, cv)
    capped = sum(1 for v in iters if v >= MAX_ITER)
    null = []
    for _ in range(n_perm):
        a, it, _ = fit_cv(X, rng.permutation(y), cv)
        null.append(a)
        capped += sum(1 for v in it if v >= MAX_ITER)

    vals, counts = np.unique(y, return_counts=True)
    majority = float(counts.max() / n)
    no_info = 1.0 / len(vals)
    m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
    margin = round((acc - m) / sd, 2) if sd > 0 else None
    beat = int(sum(1 for v in null if v >= acc - 1e-12))
    clears3 = bool(sd > 0 and acc >= m + SD_BAR * sd)
    beats_majority = bool(acc > majority)
    needed = (m + family_bar * sd) if sd > 0 else None

    bad = []
    if sd == 0:
        bad.append("the shuffled-label null has zero spread")
    if abs(acc - majority) < 1e-12:
        bad.append("accuracy exactly equals the majority-class rate")
    if dead:
        bad.append("a class was missing from a training fold")

    found = bool(clears3 and margin is not None and margin >= family_bar
                 and beat == 0 and beats_majority and not bad)
    label = ("FOUND" if found
             else "MARGINAL" if (clears3 and not bad)
             else None)

    out = {
        "accuracy": round(acc, 4),
        "null_mean": round(m, 4),
        "null_sd": round(sd, 5),
        "margin_sd": margin,
        "draws": n_perm,
        "draws_beating_real": beat,
        "clears_3sd": clears3,
        "clears_family_bar": bool(margin is not None
                                  and margin >= family_bar),
        "beats_majority_class": beats_majority,
        "label": label,
        "found": found,
        "family_bar_used": family_bar,
        "classes": int(len(vals)),
        "n": int(n),
        "no_information": round(no_info, 4),
        "majority_class_rate": round(majority, 4),
        "examples_per_class_min": int(counts.min()),
        "accuracy_needed_for_bar": (round(needed, 4) if needed is not None
                                    else None),
        "smallest_detectable_share_vs_no_information":
            detectable_share(needed, no_info),
        "smallest_detectable_share_vs_majority_class":
            detectable_share(needed, majority),
        "optimiser_passes_real_fit": iters,
        "fits_hitting_the_pass_cap": int(capped),
        "fits_total": int((1 + n_perm) * N_FOLDS),
    }
    if bad:
        out["degenerate"] = bad
    return out


def geometry(X, k=10):
    """RT-40: the share of variation in the top ten directions, at every
    position rather than only the anchor."""
    Xc = X - X.mean(0)
    sv = np.linalg.svd(Xc, compute_uv=False)
    v = sv ** 2
    return {"top_10_share_of_variation": round(float(v[:k].sum() / v.sum()),
                                               4),
            "dimensions": int(X.shape[1])}


# ------------------------------------------------------ anchor reproduction

@torch.no_grad()
def reproduce_anchor(model, ckpt_name, device):
    """Re-run the recorded 400-episode configuration exactly and compare.

    The recorded classifier accuracy depends only on the states, the
    target and the fold split; the shuffled draws in the original did not
    touch it. So reproducing it needs the original capture path, the
    original 200 paired episodes, and folds seeded by layer as the
    original seeded them."""
    import probe_target_diagnostic_a3 as Q
    pairs = L.paired_episodes(ANCHOR_PAIRS, seed=S.EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, eps = S.capture(model, flat, device, with_query=False)
    y_all = Q.targets(eps)["register_index"]

    expected = ANCHOR_RECORDED.get(ckpt_name)
    cells, worst = {}, 0.0
    for Lr in PROBE_LAYERS:
        X, rows = states[(Lr, POSITIVE_CONTROL)]
        y = y_all[rows]
        fs = D.folds(len(y), N_FOLDS, np.random.default_rng(Lr))
        acc, iters, _ = fit_cv(X, y, cv_from_folds(len(y), fs))
        exp = expected[Lr] if expected else None
        diff = abs(acc - exp) if exp is not None else None
        if diff is not None:
            worst = max(worst, diff)
        cells[str(Lr)] = {"recorded": exp, "reproduced": round(acc, 4),
                          "difference": (round(diff, 6) if diff is not None
                                         else None),
                          "optimiser_passes": iters}
    return {
        "what": ("the fitted classifier's register-index accuracy at the "
                 "marker position, 400 episodes, as recorded in "
                 "probe_target_diagnostic_a3_*.json"),
        "episodes": int(len(eps)),
        "tolerance": ANCHOR_TOL,
        "tolerance_means": "one episode in 400",
        "per_layer": cells,
        "largest_difference": round(worst, 6),
        "exact_on_every_layer": bool(worst == 0.0),
        "reproduces": bool(expected is not None and worst <= ANCHOR_TOL),
    }


def check_recorded_table_against_files(out_dir=Path("../a3-gates")):
    """The pre-stated table in this file must match the committed record,
    so neither can be edited to fit the other."""
    seen = {}
    for name, rows in ANCHOR_RECORDED.items():
        f = out_dir / f"probe_target_diagnostic_a3_{Path(name).stem}.json"
        if not f.exists():
            raise SystemExit(f"REFUSING: the record file {f} is missing, so "
                             f"the anchor table cannot be checked.")
        rec = json.loads(f.read_text())
        for Lr, want in rows.items():
            got = rec["probes"][f"{POSITIVE_CONTROL}|{Lr}|{ARM}"][
                "classifier"]["accuracy"]
            if abs(got - want) > 1e-9:
                raise SystemExit(
                    f"REFUSING: the anchor table in this file says {want} "
                    f"for {name} layer {Lr}, the committed record says "
                    f"{got}. One of them has been edited.")
        seen[name] = len(rows)
    return seen


# ---------------------------------------------------------- the parallel run

def _one_test(task):
    state_dir, ck_name, pos, lr, y = task
    X = np.load(Path(state_dir) / f"L{lr}__{pos}.npy")
    t = time.time()
    rec = measure_fitted(X, y, test_seed(ck_name, ARM, pos, lr))
    rec["geometry"] = geometry(X)
    rec["seconds"] = round(time.time() - t, 1)
    return key(pos, lr), rec


# ----------------------------------------------------------------- the cells

def arm_cell(per_checkpoint):
    """The cells fixed in `fitted-position-sweep-method.md`.

    `per_checkpoint` maps a checkpoint name to
    {"control_holds": bool, "found_positions": [...], "leak": [...]}.
    """
    pilot = per_checkpoint.get(PILOT)
    if pilot is None or not pilot["control_holds"]:
        return {"cell": "VOID — no cell assigned",
                "means": ("the positive control fails on the pilot, so "
                          "nothing in this arm can be interpreted")}
    void = [k for k, v in per_checkpoint.items() if not v["control_holds"]]
    readable = {k: v for k, v in per_checkpoint.items() if v["control_holds"]}
    found = {k: v["found_positions"] for k, v in readable.items()
             if v["found_positions"]}
    others = [k for k in found if k != PILOT]
    leaks = {k: v["leak"] for k, v in per_checkpoint.items() if v["leak"]}
    base = {"void_checkpoints": void, "found_by_checkpoint": found,
            "negative_control_clearances": leaks}
    if PILOT in found and others:
        return {**base, "cell": "FOUND SOMEWHERE",
                "means": ("a fitted linear read finds own-agent identity at "
                          "a position where it has to have been carried "
                          "rather than read off the current token. The "
                          "positions are the finding. It does not settle "
                          "red-team objection R1 and localizes nothing "
                          "until causal patching has run")}
    return {**base, "cell": "FOUND NOWHERE",
            "sub_pattern": ("nothing was found on any checkpoint"
                            if not found else
                            "found on the pilot only" if PILOT in found
                            else "found on seeds but not the pilot"),
            "means": ("at these eleven positions, five layers and three "
                      "checkpoints, a fitted linear read does not find the "
                      "register index anywhere except where the answer is "
                      "most explicitly available. This is NOT a finding of "
                      "absence: see the limits")}


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int, workers: int) -> dict:
    lock_guard.require_known_answer_pass()
    table = check_recorded_table_against_files()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    head = {
        "diagnostic": ("the fitted linear read at all eleven positions, "
                       "four-answer register-index target"),
        "registered": False, "verdict_bearing": False,
        "method_file": "fitted-position-sweep-method.md",
        "method_committed_before_output": True,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "anchor_table_checked_against_record": table,
    }

    print("  reproducing the recorded anchor first...", flush=True)
    anchor = reproduce_anchor(model, ckpt.name, device)
    head["anchor_reproduction"] = anchor
    for Lr, c in anchor["per_layer"].items():
        print(f"    layer {Lr}: recorded {c['recorded']} reproduced "
              f"{c['reproduced']} (difference {c['difference']})", flush=True)
    if not anchor["reproduces"]:
        head["FAILED_INSTRUMENT"] = (
            "the recorded marker-position numbers did not reproduce to "
            "within one episode in 400. Under the method file this run is a "
            "failed instrument: it reports these differences and says "
            "nothing about any position.")
        print("  FAILED INSTRUMENT — the anchor did not reproduce", flush=True)
        head["elapsed_sec"] = round(time.time() - t0, 1)
        return head
    print(f"  anchor reproduces (largest difference "
          f"{anchor['largest_difference']})", flush=True)

    pairs = L.paired_episodes(n_pairs, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, kept = W.capture(model, flat, device, with_query=False)
    qstates, qkept = W.capture(model, flat, device, with_query=True)
    if kept != qkept:
        raise SystemExit(
            "REFUSING to report: the two capture passes kept different "
            "episodes, so the in-episode and appended-question positions "
            "would not line up episode for episode.")
    states.update(qstates)
    eps = [flat[i] for i in kept]
    y = P.targets(eps)[ARM]
    print(f"  captured {len(eps)} episodes at {len(POSITIONS)} positions",
          flush=True)

    del model, ck
    scratch = Path(tempfile.mkdtemp(prefix="fitted_sweep_"))
    try:
        for (lr, pos), X in states.items():
            np.save(scratch / f"L{lr}__{pos}.npy", X)
        states.clear()

        tasks = [(str(scratch), ckpt.name, pos, lr, y)
                 for pos in POSITIONS for lr in PROBE_LAYERS]
        for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                  "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
            os.environ[v] = "1"
        results, done = {}, 0
        ctx = mp.get_context("spawn")
        with ctx.Pool(workers) as pool:
            for k, rec in pool.imap_unordered(_one_test, tasks):
                results[k] = rec
                done += 1
                print(f"  [{done:2d}/{len(tasks)}] {k:42s} "
                      f"acc {rec['accuracy']:.4f} "
                      f"({rec['margin_sd']:+.2f} sd, "
                      f"{rec['draws_beating_real']}/{rec['draws']}) "
                      f"{rec['label'] or '-'}"
                      f"{' DEGENERATE' if 'degenerate' in rec else ''}"
                      f" [{rec['seconds']}s]", flush=True)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)

    control_holds = any(results[key(POSITIVE_CONTROL, lr)]["found"]
                        for lr in PROBE_LAYERS)
    per_arm = {
        "control_holds": bool(control_holds),
        "found_positions": sorted({pos for pos in TESTABLE
                                   for lr in PROBE_LAYERS
                                   if results[key(pos, lr)]["found"]}),
        "marginal_positions": sorted({pos for pos in TESTABLE
                                      for lr in PROBE_LAYERS
                                      if results[key(pos, lr)]["label"]
                                      == "MARGINAL"}),
        "leak": sorted({NEGATIVE_CONTROL for lr in PROBE_LAYERS
                        if results[key(NEGATIVE_CONTROL, lr)]["found"]}),
        "degenerate_tests": sorted(k for k, v in results.items()
                                   if "degenerate" in v),
    }

    head.update({
        "settings": {
            "episodes": len(eps), "pairs_requested": n_pairs,
            "content_seed": EPISODE_SEED, "permutations": N_PERM,
            "folds": N_FOLDS, "sd_bar": SD_BAR,
            "family_sd_bar": FAMILY_SD_BAR,
            "family_sd_bar_exact": FAMILY_SD_EXACT,
            "family_size": len(TESTABLE) * len(PROBE_LAYERS) * 3,
            "family_note": ("nine testable positions x five layers x three "
                            "checkpoints; the two control positions are not "
                            "discovery tests and are not counted"),
            "draw_resolution_note": (
                "zero of 200 draws establishes only p<0.005, about 2.58 "
                "standard deviations, BELOW the 3.38 the family bar needs. "
                "The margin supplies the rest under a normal approximation, "
                "so a single FOUND cell is suggestive and wants a targeted "
                "rerun with far more draws, not settled"),
            "probe_layers": PROBE_LAYERS, "positions": list(POSITIONS),
            "testable_positions": list(TESTABLE),
            "positive_control": POSITIVE_CONTROL,
            "positive_control_note": (
                "the register index at the marker position is NOT guaranteed "
                "present, only guaranteed derivable — all four marker words "
                "have appeared by then. A failure VOIDs the checkpoint; a "
                "pass does not certify sensitivity at any other position"),
            "negative_control": NEGATIVE_CONTROL,
            "negative_control_note": (
                "at the value of the model's FIRST own turn its own marker "
                "has not yet appeared anywhere, so the target is not "
                "determinable there; a clearance means a leak, not carrying, "
                "and is excluded from the cells"),
            "arm": ARM,
            "marker_word_arm": (
                "NOT RUN. Stated in the method file before the run: at 7.56 "
                "seconds a fit against 1.19, it would cost about 70 "
                "processor-hours against about 11, which does not fit in a "
                "session on this machine"),
            "classifier": {
                "kind": "multinomial logistic regression (scikit-learn)",
                "penalty": "squared, at the library default strength",
                "C": C_REG, "solver": "lbfgs", "max_iter": MAX_ITER,
                "features_scaled": False,
                "note": ("identical to probe_target_diagnostic_a3.probe, so "
                         "the recorded numbers can be used as an instrument "
                         "check. The pass cap is part of the instrument")},
            "seeding": ("folds and shuffled draws seeded per test from a "
                        "digest of checkpoint, target, position and layer "
                        "(RT-39), not by layer alone")},
        "results": results,
        "per_arm": per_arm,
        "positive_control_holds": bool(control_holds),
        "limits": (
            "UNREGISTERED and diagnostic. One fitted linear statistic, "
            "eleven positions, five layers, 4,000 episodes, three "
            "30-million-parameter checkpoints on a synthetic grammar, one "
            "target. A null everywhere is consistent with identity being "
            "carried non-linearly, or distributed rather than resident at "
            "any one position, or at a position not on the list, or in a "
            "quiet direction an unscaled fit is pulled away from. It does "
            "not touch red-team objection R1 and changes no registered "
            "result. Under Amendment A3 section 3.2 nothing counts as "
            "localized or as absent until causal patching has also run "
            "(RT-49, RT-50), so a null here is instrument failure under the "
            "registered text, not absence."),
        "elapsed_sec": round(time.time() - t0, 1),
    })
    return head


def summarize(paths) -> dict:
    records = [json.loads(Path(p).read_text()) for p in paths]
    failed = [r["checkpoint"] for r in records if "FAILED_INSTRUMENT" in r]
    if failed:
        return {"checkpoints": [r["checkpoint"] for r in records],
                "FAILED_INSTRUMENT": failed,
                "note": ("the anchor did not reproduce on at least one "
                         "checkpoint; no cell is assigned")}
    per = {r["checkpoint"]: r["per_arm"] for r in records}
    detail = arm_cell(per)
    return {
        "checkpoints": [r["checkpoint"] for r in records],
        "arm": ARM,
        "family_sd_bar": FAMILY_SD_BAR,
        "family_size": records[0]["settings"]["family_size"],
        "cell": detail["cell"],
        "detail": detail,
        "per_checkpoint": per,
        "anchor_reproduction": {r["checkpoint"]: {
            "largest_difference": r["anchor_reproduction"]
            ["largest_difference"],
            "exact": r["anchor_reproduction"]["exact_on_every_layer"]}
            for r in records},
        "note": ("diagnostic only; no verdict is read and no registered "
                 "text is touched"),
    }


# --------------------------------------------------------------- self-test

def self_test() -> None:
    # the pre-stated anchor table must match the committed record
    table = check_recorded_table_against_files()
    assert set(table) == set(ANCHOR_RECORDED), table
    assert all(v == 5 for v in table.values()), table

    # the two modules' register index must be the same quantity
    import probe_target_diagnostic_a3 as Q
    pairs = L.paired_episodes(8, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    assert np.array_equal(Q.targets(flat)[ARM], P.targets(flat)[ARM]), \
        "the register index must be one quantity, not two"

    # the eleven positions and their roles, unchanged from the powered sweep
    assert len(POSITIONS) == 11 and len(TESTABLE) == 9
    assert POSITIVE_CONTROL not in TESTABLE and NEGATIVE_CONTROL not in TESTABLE

    # RT-39: every test gets its own split and its own draws
    seeds = {test_seed("c.pt", ARM, p, lr)
             for p in POSITIONS for lr in PROBE_LAYERS}
    assert len(seeds) == len(POSITIONS) * len(PROBE_LAYERS), \
        "two tests would share a fold split"
    assert test_seed("c.pt", ARM, POSITIONS[0], 3) == \
        test_seed("c.pt", ARM, POSITIONS[0], 3), "and it must be stable"
    assert test_seed("a.pt", ARM, POSITIONS[0], 3) != \
        test_seed("b.pt", ARM, POSITIONS[0], 3), "and differ by checkpoint"

    # the bar is stricter than the per-test bar, and rounded the safe way
    assert FAMILY_SD_BAR > SD_BAR and FAMILY_SD_BAR >= FAMILY_SD_EXACT

    # RT-37's arithmetic, against the worked example in the review: a null
    # centred on 0.25 needing 0.2793 means a signal legible in 3.9% of
    # episodes
    assert detectable_share(0.2793, 0.25) == 0.0391, detectable_share(
        0.2793, 0.25)
    assert detectable_share(0.0523, 0.04) == 0.0128

    # the label, on a planted signal and on noise
    rng = np.random.default_rng(1)
    n, d, C = 400, 12, 4
    y = np.array([i % C for i in range(n)])
    X = rng.normal(0, 1, (n, d))
    for c in range(C):
        X[y == c, c] += 2.0
    r = measure_fitted(X, y, seed=7, n_perm=30)
    assert r["found"] and r["label"] == "FOUND", r
    assert r["draws_beating_real"] == 0 and r["beats_majority_class"]
    Z = rng.normal(0, 1, (n, d))
    rz = measure_fitted(Z, y, seed=7, n_perm=30)
    assert not rz["found"] and rz["label"] is None, rz

    # an unreachable family bar must demote the same planted signal
    rm = measure_fitted(X, y, seed=7, family_bar=1e6, n_perm=30)
    assert rm["label"] == "MARGINAL" and not rm["found"], rm

    # the degeneracy precondition must fire and must suppress the label
    yc = np.zeros(n, dtype=int)
    yc[:1] = 1                      # one class of size 1: it will go missing
    rd = measure_fitted(X, yc, seed=7, n_perm=5)
    assert "degenerate" in rd and not rd["found"], rd

    # the geometry helper
    g = geometry(X)
    assert 0.0 < g["top_10_share_of_variation"] <= 1.0
    assert g["dimensions"] == d

    # the cells
    def cp(control=True, found=(), leak=()):
        return {"control_holds": control, "found_positions": list(found),
                "leak": list(leak)}
    A_ = "own_revision_value"
    assert arm_cell({PILOT: cp(control=False)})["cell"].startswith("VOID")
    assert arm_cell({PILOT: cp(), "b.pt": cp()})["cell"] == "FOUND NOWHERE"
    c = arm_cell({PILOT: cp(found=[A_]), "b.pt": cp(found=[A_])})
    assert c["cell"] == "FOUND SOMEWHERE" and c["found_by_checkpoint"][PILOT]
    c = arm_cell({PILOT: cp(found=[A_]), "b.pt": cp()})
    assert c["cell"] == "FOUND NOWHERE"
    assert c["sub_pattern"] == "found on the pilot only", \
        "an exhaustive pair of cells must not hide the sub-pattern"
    c = arm_cell({PILOT: cp(), "b.pt": cp(found=[A_])})
    assert c["sub_pattern"] == "found on seeds but not the pilot"
    c = arm_cell({PILOT: cp(leak=[NEGATIVE_CONTROL]), "b.pt": cp()})
    assert c["negative_control_clearances"] == {PILOT: [NEGATIVE_CONTROL]}

    # the negative control's premise, against real episodes
    import encoding_a3 as E
    for e in flat:
        enc = E.encode_episode(e)
        ids = enc["input_ids"]
        idx = S.position_indices(e, len(ids), False)
        own = E.VOCAB[e.markers[e.own_slot]]
        assert own not in [int(t) for t in ids[:idx[NEGATIVE_CONTROL] + 1]], \
            "the negative control's premise fails"
        assert int(ids[idx[POSITIVE_CONTROL]]) == own

    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass

    print("self-test OK — the pre-stated anchor table matches the committed "
          "record on all fifteen cells; the register index is one quantity "
          "across both modules; every one of the 55 tests gets its own fold "
          "split and its own draws (RT-39); the family bar 3.38 binds and "
          "demotes; the smallest-detectable-signal arithmetic reproduces the "
          "review's worked example (RT-37); the degeneracy precondition "
          "fires and suppresses the label (RT-38); every cell including the "
          "sub-patterns; the negative control's premise holds against real "
          "episodes; the known-answer gate. No checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--summarize", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=N_PAIRS)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if a.summarize:
        paths = sorted(a.out_dir.glob("fitted_position_sweep_a3_a3_*.json"))
        if not paths:
            raise SystemExit("no per-checkpoint files to summarize")
        s = summarize(paths)
        out = a.out_dir / "fitted_position_sweep_a3_summary.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        out.write_text(json.dumps(s, indent=2))
        print(json.dumps({k: s[k] for k in ("cell",) if k in s}, indent=2))
        return
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    for c in a.ckpt:
        out = a.out_dir / f"fitted_position_sweep_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs, a.workers)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)


if __name__ == "__main__":
    main()
