"""The standardised refit at the same positions: a DECLARED SECOND
INSTRUMENT.

**UNREGISTERED**, diagnostic only. No verdict is read and no cell here
feeds one. The method is committed in `standardised-refit-method.md`, in
the same commit as this file and before either produced any output. Read
that first: it fixes the cells.

WHY. The fitted read that came back FOUND NOWHERE left the 448 residual
directions on their original scale under a squared penalty. That penalty
is charged on the weight, not on the weight's effect. A direction
carrying a small share of the variation has a correspondingly small
typical value, so producing a given contribution to the decision needs a
proportionally larger weight — and a squared penalty charges the SQUARE
of that factor. The stack's own geometry measurement says ten of the 448
directions carry between 88 and 99.5 per cent of the variation, so the
remaining 438 share what is left and a signal resident in one of them is
pushed towards zero far harder than the same signal in a loud one. The
instrument was therefore worst-placed against exactly the hypothesis the
run existed to test: a self-index that is real, linear and quiet. That is
ledger item RT-58.

WHAT CHANGES. One thing: each residual direction is standardised to unit
variance before the fit, using TRAINING-FOLD STATISTICS ONLY. Everything
else — the target, the episodes, the positions, the layers, the
checkpoints, the fold helper, the per-test seeding, the 200-draw null,
the family-adjusted bar, the optimiser and its 2,000-pass cap, the
penalty and its strength — is imported from `fitted_position_sweep_a3`
rather than restated.

THE REGULARISATION STRENGTH IS NOT TUNED. It stays at the library default
of 1.0, unchanged. Standardising already changes what that strength means:
on unit-variance features the same penalty charges a quiet direction the
same as a loud one, which IS the fix. Choosing a strength from the data
would make the instrument's sensitivity depend on a number picked after
looking, and there is no honest place to pick it from — the positive
control is the one position where the signal is enormous and
unrepresentative, and the testable positions are the result. So exactly
one thing changes, and the method file says so before the run.

THIS INSTRUMENT WILL NOT REPRODUCE THE UNSCALED ANCHOR, AND THAT IS NOT A
FAILURE. The fifteen recorded numbers belong to the unscaled fit. A
standardised fit is a different estimator and will land somewhere else.
So the instrument check has two parts and they fail for different reasons:

  PART A, the shared check. The UNSCALED fit is re-run on the recorded
  400-episode configuration and must return the fifteen recorded numbers
  to within one episode in 400. This proves the capture path, the episode
  draw, the fold helper and the classifier configuration are unchanged —
  that this run differs from the recorded one by the scaling and by
  nothing else. Failing it makes the run a FAILED INSTRUMENT.

  PART B, this instrument's own declared anchor. The STANDARDISED fit is
  run on the same episodes, the same position and the same folds, and
  every one of the fifteen cells must reach an accuracy of at least 0.35
  against a majority-class rate of 0.2582 — that is, the standardised
  read must still find the answer where the answer is the input token.
  The bar is pre-stated, it is well below the unscaled fit's worst
  recorded cell (0.4475), and it is far above the majority-class rate, so
  it catches a broken implementation without being a lottery. Failing it
  makes the run a FAILED INSTRUMENT.

  PART C, in the self-test, not the run. With the standardiser replaced by
  an identity transform the standardised code path must reproduce the
  unscaled path's number exactly, cell for cell. That is the strongest
  available proof that the scaling is the only thing that changed.

THE CEILING. Every detectable-signal figure is calibrated against THIS
instrument's own measured ceiling at the positive control, not against
1.0 and not against the unscaled read's ceiling. The correction note of
2026-09-20 makes that mandatory.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock;
fresh output per checkpoint, nothing overwritten [C6]. This run reads no
verdict.

    ../../../.venv/bin/python standardised_position_sweep_a3.py --self-test
    ../../../.venv/bin/python standardised_position_sweep_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
    ../../../.venv/bin/python standardised_position_sweep_a3.py --summarize
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
import fitted_position_sweep_a3 as F
import lock_guard
import localize_a3 as L
import position_sweep_a3 as S
import powered_position_sweep_a3 as W
import powered_target_test_a3 as P
from model import MVM0aModel, Config

# --- imported, not restated: the same read but for the scaling
PROBE_LAYERS = F.PROBE_LAYERS
N_PAIRS = F.N_PAIRS
EPISODE_SEED = F.EPISODE_SEED
N_PERM = F.N_PERM
N_FOLDS = F.N_FOLDS
SD_BAR = F.SD_BAR
FAMILY_SD_BAR = F.FAMILY_SD_BAR          # 3.38, the same 135-test family
FAMILY_SD_EXACT = F.FAMILY_SD_EXACT
MAX_ITER = F.MAX_ITER
C_REG = F.C_REG                          # 1.0, unchanged and untuned
POSITIONS = F.POSITIONS
POSITIVE_CONTROL = F.POSITIVE_CONTROL
NEGATIVE_CONTROL = F.NEGATIVE_CONTROL
TESTABLE = F.TESTABLE
PILOT = F.PILOT
ANCHOR_PAIRS = F.ANCHOR_PAIRS
ANCHOR_TOL = F.ANCHOR_TOL
ANCHOR_RECORDED = F.ANCHOR_RECORDED

ARM = "register_index_standardised"

#: Part B: the standardised fit's own declared anchor. Every one of the
#: fifteen cells at the marker position must reach this accuracy. Chosen
#: before the run from two numbers already on the record: the unscaled
#: fit's worst recorded cell there is 0.4475 and the majority-class rate
#: is 0.2582. A standardised read below 0.35 at the one position where
#: the answer is the input token is not a usable instrument.
STANDARDISED_ANCHOR_FLOOR = 0.35
MAJORITY_AT_ANCHOR = 0.2582

#: A direction with no spread on a training fold carries no information in
#: that fold. Dividing by its spread is undefined, so it is set to zero on
#: both sides of the split. Pre-stated, and counted and reported per test.
ZERO_SPREAD_RULE = (
    "a residual direction whose spread on the TRAINING fold is zero is set "
    "to zero on both the training and the held-out rows: it carries no "
    "information in that fold and its scale is undefined. The count of such "
    "directions is reported per test")


def key(pos, layer):
    return f"{ARM}|{pos}|{layer}"


# ------------------------------------------------------- the standardiser

def standardise(X_tr, X_te):
    """Centre and scale to unit variance using the TRAINING rows only.

    Held-out rows are transformed with the training fold's mean and
    spread and never contribute to either, which is what keeps the
    held-out accuracy an honest estimate. Returns the transformed pair and
    the number of directions that had no spread on the training rows."""
    mu = X_tr.mean(axis=0)
    sd = X_tr.std(axis=0)
    dead = int((sd == 0).sum())
    safe = np.where(sd == 0, 1.0, sd)
    return (X_tr - mu) / safe, (X_te - mu) / safe, dead


def _identity(X_tr, X_te):
    """Part C's stand-in: the same code path with no scaling at all."""
    return X_tr, X_te, 0


def fit_cv(X, y, cv, transform=standardise):
    """`fitted_position_sweep_a3.fit_cv` with a per-fold transform.

    Kept deliberately parallel to it, line for line, so that passing
    `_identity` reproduces it exactly — which the self-test asserts."""
    from sklearn.linear_model import LogisticRegression
    y = np.asarray(y)
    n_classes = len(np.unique(y))
    scores, iters, dead, zero_spread = [], [], False, 0
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for tr, te in cv:
            present = np.unique(y[tr])
            if len(present) < n_classes:
                dead = True
            if len(present) < 2:
                scores.append(float((y[te] == present[0]).mean()))
                iters.append(0)
                continue
            A_tr, A_te, z = transform(X[tr], X[te])
            zero_spread += z
            clf = LogisticRegression(max_iter=MAX_ITER,
                                     C=C_REG).fit(A_tr, y[tr])
            scores.append(float((clf.predict(A_te) == y[te]).mean()))
            iters.append(int(np.max(clf.n_iter_)))
    return float(np.mean(scores)), iters, dead, zero_spread


def measure_standardised(X, y, seed, family_bar=FAMILY_SD_BAR,
                         n_perm=N_PERM):
    """One test under the standardised instrument.

    The body mirrors `fitted_position_sweep_a3.measure_fitted` exactly —
    same null, same degeneracy preconditions, same label rule, same
    pre-stated cells — and differs only in calling the transforming
    `fit_cv` above and in reporting the zero-spread count."""
    y = np.asarray(y)
    n = len(y)
    fs = D.folds(n, N_FOLDS, np.random.default_rng(seed))
    cv = F.cv_from_folds(n, fs)
    rng = np.random.default_rng(seed + 1)

    acc, iters, dead, zero_spread = fit_cv(X, y, cv)
    capped = sum(1 for v in iters if v >= MAX_ITER)
    null = []
    for _ in range(n_perm):
        a, it, _, _ = fit_cv(X, rng.permutation(y), cv)
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
        "optimiser_passes_real_fit": iters,
        "fits_hitting_the_pass_cap": int(capped),
        "fits_total": int((1 + n_perm) * N_FOLDS),
        "zero_spread_directions_real_fit": int(zero_spread),
    }
    if bad:
        out["degenerate"] = bad
    return out


# ------------------------------------------------------ anchor reproduction

@torch.no_grad()
def reproduce_anchor(model, ckpt_name, device):
    """Parts A and B together, on one capture.

    Part A re-runs the UNSCALED fit and compares it with the fifteen
    recorded numbers. Part B runs the STANDARDISED fit on the same states,
    target and folds and holds it to its own pre-stated floor. Part B is
    expected to disagree with Part A; it is not compared with it."""
    import probe_target_diagnostic_a3 as Q
    pairs = L.paired_episodes(ANCHOR_PAIRS, seed=S.EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, eps = S.capture(model, flat, device, with_query=False)
    y_all = Q.targets(eps)["register_index"]

    expected = ANCHOR_RECORDED.get(ckpt_name)
    cells, worst, floor_ok = {}, 0.0, True
    for Lr in PROBE_LAYERS:
        X, rows = states[(Lr, POSITIVE_CONTROL)]
        y = y_all[rows]
        fs = D.folds(len(y), N_FOLDS, np.random.default_rng(Lr))
        cv = F.cv_from_folds(len(y), fs)
        unscaled, u_iters, _ = F.fit_cv(X, y, cv)
        scaled, s_iters, _, zsp = fit_cv(X, y, cv)
        exp = expected[Lr] if expected else None
        diff = abs(unscaled - exp) if exp is not None else None
        if diff is not None:
            worst = max(worst, diff)
        if scaled < STANDARDISED_ANCHOR_FLOOR:
            floor_ok = False
        cells[str(Lr)] = {
            "recorded_unscaled": exp,
            "reproduced_unscaled": round(unscaled, 4),
            "difference": (round(diff, 6) if diff is not None else None),
            "standardised": round(scaled, 4),
            "standardised_clears_floor": bool(
                scaled >= STANDARDISED_ANCHOR_FLOOR),
            "optimiser_passes_unscaled": u_iters,
            "optimiser_passes_standardised": s_iters,
            "zero_spread_directions": zsp,
        }
    return {
        "part_a": ("the UNSCALED fit must return the fifteen recorded "
                   "numbers to within one episode in 400, which proves this "
                   "run differs from the recorded one by the scaling and "
                   "nothing else"),
        "part_b": (f"the STANDARDISED fit must reach at least "
                   f"{STANDARDISED_ANCHOR_FLOOR} on every cell, against a "
                   f"majority-class rate of {MAJORITY_AT_ANCHOR}. It is a "
                   f"different estimator and is NOT expected to match the "
                   f"recorded numbers; disagreeing with them is not a "
                   f"failure"),
        "episodes": int(len(eps)),
        "tolerance": ANCHOR_TOL,
        "tolerance_means": "one episode in 400",
        "standardised_floor": STANDARDISED_ANCHOR_FLOOR,
        "per_layer": cells,
        "largest_difference": round(worst, 6),
        "exact_on_every_layer": bool(worst == 0.0),
        "part_a_holds": bool(expected is not None and worst <= ANCHOR_TOL),
        "part_b_holds": bool(floor_ok),
        "reproduces": bool(expected is not None and worst <= ANCHOR_TOL
                           and floor_ok),
    }


# ---------------------------------------------------------- the parallel run

def _one_test(task):
    state_dir, ck_name, pos, lr, y = task
    X = np.load(Path(state_dir) / f"L{lr}__{pos}.npy")
    t = time.time()
    rec = measure_standardised(X, y, F.test_seed(ck_name, ARM, pos, lr))
    rec["geometry"] = F.geometry(X)
    rec["seconds"] = round(time.time() - t, 1)
    return key(pos, lr), rec


# ------------------------------------------------------------------ the run

@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int, workers: int) -> dict:
    lock_guard.require_known_answer_pass()
    table = F.check_recorded_table_against_files()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    head = {
        "diagnostic": ("the standardised refit at the same eleven "
                       "positions, four-answer register-index target, as a "
                       "DECLARED SECOND INSTRUMENT"),
        "registered": False, "verdict_bearing": False,
        "method_file": "standardised-refit-method.md",
        "method_committed_before_output": True,
        "answers_ledger_item": "RT-58 (the same number in the review file)",
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "anchor_table_checked_against_record": table,
    }

    print("  reproducing the anchor first (parts A and B)...", flush=True)
    anchor = reproduce_anchor(model, ckpt.name, device)
    head["anchor_reproduction"] = anchor
    for Lr, c in anchor["per_layer"].items():
        print(f"    layer {Lr}: unscaled recorded {c['recorded_unscaled']} "
              f"reproduced {c['reproduced_unscaled']} "
              f"(difference {c['difference']}) | standardised "
              f"{c['standardised']} "
              f"{'ok' if c['standardised_clears_floor'] else 'BELOW FLOOR'}",
              flush=True)
    if not anchor["reproduces"]:
        why = []
        if not anchor["part_a_holds"]:
            why.append("part A: the recorded unscaled numbers did not come "
                       "back to within one episode in 400, so something "
                       "other than the scaling has changed")
        if not anchor["part_b_holds"]:
            why.append(f"part B: the standardised fit fell below "
                       f"{STANDARDISED_ANCHOR_FLOOR} at the position where "
                       f"the answer is the input token, so it is not a "
                       f"usable instrument")
        head["FAILED_INSTRUMENT"] = "; ".join(why)
        print(f"  FAILED INSTRUMENT — {head['FAILED_INSTRUMENT']}",
              flush=True)
        head["elapsed_sec"] = round(time.time() - t0, 1)
        return head
    print(f"  anchor holds: part A largest difference "
          f"{anchor['largest_difference']}, part B every cell at or above "
          f"{STANDARDISED_ANCHOR_FLOOR}", flush=True)

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
    y = P.targets(eps)["register_index"]
    print(f"  captured {len(eps)} episodes at {len(POSITIONS)} positions",
          flush=True)

    del model, ck
    scratch = Path(tempfile.mkdtemp(prefix="standardised_sweep_"))
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
                print(f"  [{done:2d}/{len(tasks)}] {k:52s} "
                      f"acc {rec['accuracy']:.4f} "
                      f"({rec['margin_sd']:+.2f} sd, "
                      f"{rec['draws_beating_real']}/{rec['draws']}) "
                      f"{rec['label'] or '-'}"
                      f"{' DEGENERATE' if 'degenerate' in rec else ''}"
                      f" [{rec['seconds']}s]", flush=True)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)

    # this instrument's own measured ceiling, not the unscaled read's
    ceiling = max(results[key(POSITIVE_CONTROL, lr)]["accuracy"]
                  for lr in PROBE_LAYERS)
    for k, rec in results.items():
        rec["measured_ceiling_used"] = ceiling
        needed, ref = rec["accuracy_needed_for_bar"], rec["no_information"]
        rec["smallest_detectable_share_vs_measured_ceiling"] = (
            None if needed is None or ceiling <= ref
            else round(max(0.0, (needed - ref) / (ceiling - ref)), 4))
        maj = rec["majority_class_rate"]
        rec["smallest_detectable_share_vs_majority_class"] = (
            None if needed is None or ceiling <= maj
            else round(max(0.0, (needed - maj) / (ceiling - maj)), 4))

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
        "measured_ceiling": ceiling,
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
                            "checkpoints, the same family as the run this "
                            "refits; the two control positions are not "
                            "discovery tests and are not counted"),
            "probe_layers": PROBE_LAYERS, "positions": list(POSITIONS),
            "testable_positions": list(TESTABLE),
            "positive_control": POSITIVE_CONTROL,
            "negative_control": NEGATIVE_CONTROL,
            "arm": ARM,
            "second_instrument": (
                "DECLARED. This is not the instrument that produced the "
                "record and does not claim to be. It standardises each "
                "residual direction to unit variance before the fit and "
                "changes nothing else"),
            "standardisation": (
                "per fold, TRAINING ROWS ONLY: the mean and spread are "
                "computed on the training rows of that fold and applied to "
                "both the training and the held-out rows. Held-out rows "
                "contribute to neither statistic"),
            "zero_spread_rule": ZERO_SPREAD_RULE,
            "regularisation": {
                "C": C_REG,
                "chosen": ("not tuned. Left at the library default of 1.0, "
                           "the value the unscaled run used. Standardising "
                           "already changes what that strength means — on "
                           "unit-variance features the same penalty charges "
                           "a quiet direction the same as a loud one, which "
                           "is the fix. A strength picked from the data "
                           "would make the instrument's sensitivity depend "
                           "on a number chosen after looking, and there is "
                           "no honest place to pick it from: the positive "
                           "control is unrepresentative and the testable "
                           "positions are the result"),
                "solver": "lbfgs", "max_iter": MAX_ITER,
                "penalty": "squared, at the library default strength"},
            "ceiling_note": (
                "every detectable-signal figure is calibrated against THIS "
                "instrument's measured ceiling at the positive control, not "
                "against 1.0 and not against the unscaled read's ceiling "
                "(the correction note of 2026-09-20)"),
            "seeding": ("folds and shuffled draws seeded per test from a "
                        "digest of checkpoint, target, position and layer "
                        "(RT-39). The target name carries the standardised "
                        "tag, so no test shares a split with the unscaled "
                        "run's")},
        "results": results,
        "per_arm": per_arm,
        "positive_control_holds": bool(control_holds),
        "measured_ceiling": ceiling,
        "limits": (
            "UNREGISTERED and diagnostic. One fitted linear statistic, "
            "eleven positions, five layers, 4,000 episodes, three "
            "30-million-parameter checkpoints on a synthetic grammar, one "
            "target. Standardising removes the penalty's bias against quiet "
            "directions; it does not make the read unbiased, and a null "
            "everywhere remains consistent with identity being carried "
            "non-linearly, or distributed rather than resident at any one "
            "position, or at a position not on the list. Under Amendment A3 "
            "section 3.2 nothing counts as localized or as absent until "
            "causal patching has also run (RT-49, RT-50); the registered "
            "term for the line's state is NOT TESTABLE (LOCALIZATION) until "
            "it does. It does not touch red-team objection R1 and changes "
            "no registered result."),
        "elapsed_sec": round(time.time() - t0, 1),
    })
    return head


def summarize(paths) -> dict:
    records = [json.loads(Path(p).read_text()) for p in paths]
    failed = [r["checkpoint"] for r in records if "FAILED_INSTRUMENT" in r]
    if failed:
        return {"checkpoints": [r["checkpoint"] for r in records],
                "FAILED_INSTRUMENT": failed,
                "note": ("the anchor did not hold on at least one "
                         "checkpoint; no cell is assigned")}
    per = {r["checkpoint"]: r["per_arm"] for r in records}
    detail = F.arm_cell(per)
    return {
        "checkpoints": [r["checkpoint"] for r in records],
        "arm": ARM,
        "second_instrument": True,
        "answers_ledger_item": "RT-58",
        "family_sd_bar": FAMILY_SD_BAR,
        "family_size": records[0]["settings"]["family_size"],
        "cell": detail["cell"],
        "detail": detail,
        "per_checkpoint": per,
        "measured_ceiling": {r["checkpoint"]: r["measured_ceiling"]
                             for r in records},
        "anchor_reproduction": {r["checkpoint"]: {
            "part_a_largest_difference":
                r["anchor_reproduction"]["largest_difference"],
            "part_a_holds": r["anchor_reproduction"]["part_a_holds"],
            "part_b_holds": r["anchor_reproduction"]["part_b_holds"],
            "standardised_per_layer": {
                k: v["standardised"] for k, v in
                r["anchor_reproduction"]["per_layer"].items()}}
            for r in records},
        "note": ("diagnostic only; no verdict is read and no registered "
                 "text is touched"),
    }


# --------------------------------------------------------------- self-test

def self_test() -> None:
    # the read is the matched run's but for the scaling
    table = F.check_recorded_table_against_files()
    assert all(v == 5 for v in table.values()), table
    assert (FAMILY_SD_BAR, FAMILY_SD_EXACT) == (3.38, 3.3740)
    assert C_REG == 1.0 and MAX_ITER == 2000, "the strength is not tuned"
    assert POSITIONS == F.POSITIONS and TESTABLE == F.TESTABLE
    assert len(POSITIONS) == 11 and len(TESTABLE) == 9

    rng = np.random.default_rng(0)
    n, d, C = 400, 12, 4
    y = np.array([i % C for i in range(n)])
    X = rng.normal(0, 1, (n, d)) * np.array([100.0, 0.01] + [1.0] * (d - 2))
    for c in range(C):
        X[y == c, c] += 2.0
    fs = D.folds(n, N_FOLDS, np.random.default_rng(3))
    cv = F.cv_from_folds(n, fs)

    # PART C: with the transform replaced by an identity, this code path
    # must reproduce the unscaled path's number exactly
    a_id, it_id, dead_id, z_id = fit_cv(X, y, cv, transform=_identity)
    a_un, it_un, dead_un = F.fit_cv(X, y, cv)
    assert a_id == a_un and it_id == it_un and dead_id == dead_un, \
        "the standardised path must be the unscaled path when it does not scale"
    assert z_id == 0

    # (that standardising really changes the fit is asserted below, on the
    # quiet-direction case that is the reason for this run; a planted
    # signal this loud saturates both reads and would show nothing)

    # the transform uses TRAINING statistics only
    tr, te = cv[0]
    A_tr, A_te, z = standardise(X[tr], X[te])
    assert np.allclose(A_tr.mean(0), 0, atol=1e-9)
    assert np.allclose(A_tr.std(0), 1, atol=1e-9)
    assert not np.allclose(A_te.mean(0), 0, atol=1e-6), \
        "the held-out rows must NOT be centred on their own mean"
    assert z == 0
    # and it must reproduce the held-out rows from the training statistics
    assert np.allclose(A_te, (X[te] - X[tr].mean(0)) / X[tr].std(0))

    # the zero-spread rule
    Z = X.copy()
    Z[:, 5] = 7.0
    A_tr, A_te, z = standardise(Z[tr], Z[te])
    assert z == 1 and np.all(A_tr[:, 5] == 0) and np.all(A_te[:, 5] == 0), \
        "a direction with no spread on the training fold must go to zero"

    # the label, on a planted signal and on noise, under this instrument
    r = measure_standardised(X, y, seed=7, n_perm=30)
    assert r["found"] and r["label"] == "FOUND", r
    assert r["draws_beating_real"] == 0 and r["beats_majority_class"]
    assert r["zero_spread_directions_real_fit"] == 0
    Zn = rng.normal(0, 1, (n, d))
    rz = measure_standardised(Zn, y, seed=7, n_perm=30)
    assert not rz["found"] and rz["label"] is None, rz

    # an unreachable family bar must demote the same planted signal
    rm = measure_standardised(X, y, seed=7, family_bar=1e6, n_perm=30)
    assert rm["label"] == "MARGINAL" and not rm["found"], rm

    # the degeneracy precondition must fire and must suppress the label
    yc = np.zeros(n, dtype=int)
    yc[:1] = 1
    rd = measure_standardised(X, yc, seed=7, n_perm=5)
    assert "degenerate" in rd and not rd["found"], rd

    # the quiet-direction claim, which is the whole reason for this run: a
    # signal planted ONLY in a direction 10,000 times quieter than the
    # loudest must be easier to reach after standardising
    q = rng.normal(0, 1, (n, d)) * np.array([1e4] + [1.0] * (d - 1))
    q[:, 1] = rng.normal(0, 1e-4, n) + y * 3e-4
    a_q_un, _, _ = F.fit_cv(q, y, cv)
    a_q_sc, _, _, _ = fit_cv(q, y, cv)
    assert a_q_sc > a_q_un, (
        "standardising must help where the signal is in a quiet direction; "
        f"unscaled {a_q_un}, standardised {a_q_sc}")

    # part B's floor is pre-stated, below the unscaled record's worst cell
    # and well above the majority-class rate
    worst = min(v for rows in ANCHOR_RECORDED.values() for v in rows.values())
    assert MAJORITY_AT_ANCHOR < STANDARDISED_ANCHOR_FLOOR < worst, (
        STANDARDISED_ANCHOR_FLOOR, worst)

    # the cells are the matched run's, unchanged
    def cp(control=True, found=(), leak=()):
        return {"control_holds": control, "found_positions": list(found),
                "leak": list(leak)}
    A_ = "own_revision_value"
    assert F.arm_cell({PILOT: cp(control=False)})["cell"].startswith("VOID")
    assert F.arm_cell({PILOT: cp(), "b.pt": cp()})["cell"] == "FOUND NOWHERE"
    c = F.arm_cell({PILOT: cp(found=[A_]), "b.pt": cp(found=[A_])})
    assert c["cell"] == "FOUND SOMEWHERE"
    c = F.arm_cell({PILOT: cp(found=[A_]), "b.pt": cp()})
    assert c["sub_pattern"] == "found on the pilot only"

    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass

    print("self-test OK — the cells, the family bar, the positions and the "
          "null are the unscaled run's, imported not restated; the "
          "regularisation strength is the untouched library default; with "
          "the transform replaced by an identity this code path reproduces "
          "the unscaled fit exactly, pass counts included (part C); the "
          "transform uses training-fold statistics only and never the "
          "held-out rows; the zero-spread rule fires and zeroes the "
          "direction; a signal planted in a direction ten thousand times "
          "quieter than the loudest is reachable after standardising and "
          "not before; part B's floor sits above the majority-class rate "
          "and below the unscaled record's worst cell; the label, the "
          "family bar and the degeneracy precondition all behave. No "
          "checkpoint touched")


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
        paths = sorted(a.out_dir.glob(
            "standardised_position_sweep_a3_a3_*.json"))
        if not paths:
            raise SystemExit("no per-checkpoint files to summarize")
        s = summarize(paths)
        out = a.out_dir / "standardised_position_sweep_a3_summary.json"
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
        out = a.out_dir / f"standardised_position_sweep_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs, a.workers)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)


if __name__ == "__main__":
    main()
