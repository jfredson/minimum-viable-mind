"""The OTHER agent's index at the same positions: registered matched
control L2(a).

**UNREGISTERED as a verdict-bearing run**, diagnostic only, but the
instrument itself is registered: Amendment A3 section 3.1 lists, as
matched control L2(a), "the *other-index* subspace: the same localization
run for a named non-self agent ('which marker is agent B's'), matched in
rank and probe accuracy". It has never been run. The method is committed
in `other-index-position-sweep-method.md`, in the same commit as this
file and before either produced any output. Read that first: it fixes the
cells.

WHY. The fitted linear read at eleven positions came back FOUND NOWHERE,
with one pattern worth naming: at the other agent's revision value the
model's own register index read positive on fifteen tests out of fifteen
(+2.33, +2.39, +3.34 at the best layer per checkpoint) and reached
MARGINAL once. Two readings fit that. Either the model carries a
self-index away from its own act position, which is close to what the
registration defines the target to be; or the state at that token
represents WHICH AGENT IS SPEAKING, and because an agent is never its own
other, representing that excludes one rank of four and lifts the best
attainable accuracy on the own index from 0.25 to about 0.333 with no
own-agent representation involved. That is ledger item RT-82 (RT-64 in
the review file). This run separates them by pointing the identical read
at the other agent's index instead of the model's own.

WHAT CHANGES FROM THE RUN IT MATCHES. One thing: the target function.
The classifier, its penalty and strength, the optimiser and its 2,000-pass
cap, the fold helper, the per-test seeding, the 200-draw null, the
episodes, the capture path and the family-adjusted bar are all the ones
`fitted_position_sweep_a3` used, imported from it rather than copied so
that "the same read" is a fact about the code and not a claim about it.

WHAT IS ADDED. One position, `other_revision_marker` — the token that IS
agent B's marker word. It is the positive control and nothing else: it is
not a discovery test and is not counted in the family. The run it matches
had such a position for its own target (position 6, the model's own
marker token) and this target had none, which would have left the run
with no gate and no measured ceiling. The nine testable positions are the
same nine, so the two runs compare cell for cell.

THE POSITIVE CONTROL is therefore `other_revision_marker`. A checkpoint
failing it is VOID.

THE NEGATIVE CONTROL is the model's first assignment value restricted to
the half of episodes in which agent B's marker word has not yet appeared
anywhere. Nothing about agent B is in context there, so a clearance is a
leak, not carrying. This is the one place rows are restricted, and the
method file says so in advance.

POSITION 6 IS NO LONGER A CONTROL. The model's own marker token says
which rank is the model's, which is not agent B's rank; it is reported as
a diagnostic, is not a control and is not in the family.

THE PRE-STATED PREDICTION. Measured on the episode builder before this
run, and written into the method file: agent B's identity is a function
of the tokens read at `other_revision_value` in 100% of episodes and at
`other_revision_decision` in 0% of them, because a revision turn's VALUE
pins its agent while the "to" one token earlier does not. So if the
exclusion reading of the MARGINAL is right, this run finds the other
agent's index at `other_revision_value` and not at
`other_revision_decision`. If it finds it at neither, the exclusion
reading is not supported and the own-index pattern is not explained away.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock;
fresh output per checkpoint, nothing overwritten [C6]. This run reads no
verdict.

    ../../../.venv/bin/python other_index_position_sweep_a3.py --self-test
    ../../../.venv/bin/python other_index_position_sweep_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
    ../../../.venv/bin/python other_index_position_sweep_a3.py --summarize
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import os
import shutil
import tempfile
import time
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import encoding_a3 as E
import fitted_position_sweep_a3 as F
import lock_guard
import localize_a3 as L
import position_sweep_a3 as S
import powered_position_sweep_a3 as W
from model import MVM0aModel, Config

# --- everything below this line is imported, not restated: same instrument
PROBE_LAYERS = F.PROBE_LAYERS
N_PAIRS = F.N_PAIRS
EPISODE_SEED = F.EPISODE_SEED
N_PERM = F.N_PERM
N_FOLDS = F.N_FOLDS
SD_BAR = F.SD_BAR
MAX_ITER = F.MAX_ITER
C_REG = F.C_REG
PILOT = F.PILOT

ARM = "other_index"

# The eleven, unchanged, plus one declared control position.
CONTROL_POSITION = "other_revision_marker"
POSITIONS = tuple(W.POSITIONS) + (CONTROL_POSITION,)
POSITIVE_CONTROL = CONTROL_POSITION
TESTABLE = W.TESTABLE                    # the same nine, so the runs compare
DIAGNOSTIC_ONLY = ("own_revision_marker", "own_assign_1_value")

# The negative control is a RESTRICTED test, not a position: the model's
# first assignment value on the episodes where agent B's marker word has
# not yet appeared anywhere.
NEGATIVE_BASE = "own_assign_1_value"
NEGATIVE_CONTROL = "own_assign_1_value__agent_b_not_yet_named"

# Measured on the episode builder before the run, no checkpoint touched,
# and written into the method file. Asserted in the self-test so neither
# can drift from the other.
GRAMMAR_EXPECTED = {
    # position: (share where agent B's marker word has appeared,
    #            share where agent B's IDENTITY is determinable)
    "own_assign_1_value":       (0.5000, 0.0000),
    "own_assign_2_value":       (0.8377, 0.0000),
    "own_revision_decision":    (1.0000, 0.5000),
    "own_revision_value":       (1.0000, 0.5000),
    "own_revision_by":          (1.0000, 0.5000),
    "own_revision_marker":      (1.0000, 0.5000),
    "before_own_revision_turn": (1.0000, 0.5000),
    "other_revision_decision":  (1.0000, 0.0000),
    "other_revision_value":     (1.0000, 1.0000),
    "other_revision_marker":    (1.0000, 1.0000),
    "query_answer_decision":    (1.0000, 1.0000),
    "query_answer_value":       (1.0000, 1.0000),
}
GRAMMAR_TOL = 0.02

PREDICTION = (
    "Agent B's identity is a function of the tokens read at "
    "other_revision_value in 100% of episodes and at "
    "other_revision_decision in 0% of them: a revision turn's VALUE pins "
    "its agent, because the four agents hold four distinct values for a "
    "contested item and the revision rule is a bijection, while the 'to' "
    "one token earlier pins nothing. So if the exclusion reading of the "
    "own-index MARGINAL is right, this run finds the other agent's index "
    "at other_revision_value and not at other_revision_decision. Finding "
    "it at neither does not support the exclusion reading and leaves the "
    "own-index pattern unexplained.")


def family_bar(n_tests: int) -> tuple[float, float]:
    """The per-test margin that spreads a 5% family-wise error over
    `n_tests`, one-sided Bonferroni, and the value actually applied —
    rounded UP to two decimals so the bar in force is never looser than
    the bar the arithmetic asks for. This is the rule the matched run
    used (135 tests -> 3.3740 -> 3.38); it is recomputed here for the
    tests actually run rather than assumed."""
    from statistics import NormalDist
    exact = NormalDist().inv_cdf(1.0 - 0.05 / n_tests)
    return round(exact, 4), math.ceil(exact * 100) / 100


FAMILY_SIZE = len(TESTABLE) * len(PROBE_LAYERS) * 3
FAMILY_SD_EXACT, FAMILY_SD_BAR = family_bar(FAMILY_SIZE)


def key(pos, layer):
    return f"{ARM}|{pos}|{layer}"


# ------------------------------------------------------------- the target

def other_reviser_slot(ep):
    """Agent B: the one non-self agent that revises in this episode.

    `position_sweep_a3.position_indices` already requires exactly one, and
    returns None otherwise, so every episode this run scores has one."""
    o = [t.agent for t in ep.turns if t.revised and t.agent != ep.own_slot]
    return o[0] if len(o) == 1 else None


def marker_rank(ep, agent):
    """The rank of an agent's marker word among the episode's four, in
    vocabulary order — the same quantity the own-index target uses, read
    off a different agent."""
    order = sorted(range(ep.n_agents), key=lambda a: E.VOCAB[ep.markers[a]])
    return order.index(agent)


def targets(eps):
    """The other-agent index. Four answers, matched in rank to the own
    register index: measured on 4,000 episodes the two have the same class
    shares to four decimals, and they are never equal, which is the
    exclusion that makes this control the one that settles RT-82."""
    return np.asarray([marker_rank(e, other_reviser_slot(e)) for e in eps])


def own_targets(eps):
    """The own register index, for the matched comparison only."""
    return np.asarray([marker_rank(e, e.own_slot) for e in eps])


# -------------------------------------------------- availability in context

def availability(eps):
    """Per position and episode: has agent B's marker word appeared, and
    is agent B's identity determinable, from the tokens read so far?

    Reported per position beside every cell so that a null is read against
    the right ceiling rather than against 1.0.

    Both encodings are walked, because the two appended-question positions
    exist only in the with-question pass; reading them off the no-question
    encoding would report them as unavailable when in fact they sit after
    the whole episode."""
    span = 7
    seen = {p: [] for p in POSITIONS}
    det = {p: [] for p in POSITIONS}
    for ep in eps:
        b = other_reviser_slot(ep)
        bmark = E.VOCAB[ep.markers[b]]
        oth_turn = [i for i, t in enumerate(ep.turns)
                    if t.revised and t.agent != ep.own_slot][0]
        b_val = 1 + span * oth_turn + A.VALUE_WORD_IDX
        for wq in (False, True):
            enc = E.encode_episode(ep, query=(ep.queries[0] if wq else None))
            ids = [int(t) for t in enc["input_ids"]]
            idx = position_indices(ep, len(ids), wq)
            for p in POSITIONS:
                if (p in S.QUERY_POSITIONS) != wq or p not in idx:
                    continue
                i = idx[p]
                seen[p].append(bmark in ids[:i])
                det[p].append(i >= b_val)
    return ({p: np.asarray(v) for p, v in seen.items()},
            {p: np.asarray(v) for p, v in det.items()})


# ------------------------------------------------------------ the capture

#: Bound once, at import. `capture` substitutes `S.position_indices` for
#: the wrapper below; without a reference taken beforehand the wrapper
#: would call itself and recurse until the stack ran out.
_BASE_POSITION_INDICES = S.position_indices


def position_indices(ep, enc_len, with_query):
    """The eleven exactly as the matched run computes them, plus the one
    control position: the marker token of agent B's revision turn, two
    after its value, by the same six-words-and-a-newline arithmetic the
    rest of the stack uses."""
    idx = _BASE_POSITION_INDICES(ep, enc_len, with_query)
    if idx is None:
        return None
    if not with_query:
        idx[CONTROL_POSITION] = idx["other_revision_value"] + 2
    return idx


@torch.no_grad()
def capture(model, eps, device, with_query):
    """`powered_position_sweep_a3.capture`, unmodified, taught about the
    one extra position by substituting the position list and the index
    helper for the duration of the call.

    The substitution is what keeps the capture path identical to the
    matched run's rather than a near-copy of it that could drift. The
    self-test asserts that the eleven come back bit for bit the same as an
    unpatched call, and that both globals are restored."""
    old_pos, old_idx = W.POSITIONS, S.position_indices
    W.POSITIONS, S.position_indices = POSITIONS, position_indices
    try:
        return W.capture(model, eps, device, with_query)
    finally:
        W.POSITIONS, S.position_indices = old_pos, old_idx


# ------------------------------------------------------------- the ceiling

def detectable_share(needed, reference, ceiling):
    """RT-37's measure, calibrated against the read's OWN measured ceiling
    rather than against 1.0.

    The correction note of 2026-09-20 makes this mandatory: a perfectly
    legible episode does not score 1.0 under this read, it scores whatever
    the read reaches where the answer is the input token. The share of
    episodes that would have to be legible, the rest at chance, to reach
    `needed` is (needed - reference) / (ceiling - reference)."""
    if needed is None or ceiling is None or ceiling <= reference:
        return None
    return round(max(0.0, (needed - reference) / (ceiling - reference)), 4)


# ---------------------------------------------------------- the parallel run

def _one_test(task):
    scratch, ck_name, name, fname, lr, y = task
    X = np.load(Path(scratch) / fname)
    t = time.time()
    rec = F.measure_fitted(X, y, F.test_seed(ck_name, ARM, name, lr),
                           family_bar=FAMILY_SD_BAR, n_perm=N_PERM)
    rec["geometry"] = F.geometry(X)
    rec["seconds"] = round(time.time() - t, 1)
    return key(name, lr), rec


# ----------------------------------------------------------------- the cells

def arm_cell(per_checkpoint):
    """The cells fixed in `other-index-position-sweep-method.md`. Same
    shape as the matched run's, with the positive control changed."""
    pilot = per_checkpoint.get(PILOT)
    if pilot is None or not pilot["control_holds"]:
        return {"cell": "VOID — no cell assigned",
                "means": ("the positive control at the other agent's marker "
                          "token fails on the pilot, so nothing in this arm "
                          "can be interpreted")}
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
                "means": ("a fitted linear read finds the OTHER agent's "
                          "index at a testable position. Where those "
                          "positions are is the finding: a clearance at "
                          "other_revision_value supports the exclusion "
                          "reading of the own-index MARGINAL, a clearance "
                          "only elsewhere does not")}
    return {**base, "cell": "FOUND NOWHERE",
            "sub_pattern": ("nothing was found on any checkpoint"
                            if not found else
                            "found on the pilot only" if PILOT in found
                            else "found on seeds but not the pilot"),
            "means": ("at these positions, five layers and three "
                      "checkpoints, a fitted linear read does not find the "
                      "other agent's index anywhere except where its marker "
                      "is the input token. This is NOT a finding of "
                      "absence: see the limits")}


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
        "diagnostic": ("the other agent's index at the same positions: "
                       "registered matched control L2(a)"),
        "registered_instrument": ("Amendment A3 section 3.1, matched "
                                  "control L2(a)"),
        "registered": False, "verdict_bearing": False,
        "method_file": "other-index-position-sweep-method.md",
        "method_committed_before_output": True,
        "answers_ledger_item": "RT-82 (RT-64 in the review file)",
        "prediction_stated_before_the_run": PREDICTION,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "anchor_table_checked_against_record": table,
    }

    # The instrument is unchanged, so the matched run's anchor is this
    # run's anchor: the same fifteen recorded numbers, reproduced with the
    # same classifier on the same 400 episodes.
    print("  reproducing the recorded anchor first...", flush=True)
    anchor = F.reproduce_anchor(model, ckpt.name, device)
    head["anchor_reproduction"] = anchor
    head["anchor_note"] = (
        "this run changes the target and nothing else, so its instrument "
        "check is the matched run's: the fifteen recorded own-index "
        "accuracies at the model's own marker token must come back to "
        "within one episode in 400")
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
    states, kept = capture(model, flat, device, with_query=False)
    qstates, qkept = capture(model, flat, device, with_query=True)
    if kept != qkept:
        raise SystemExit(
            "REFUSING to report: the two capture passes kept different "
            "episodes, so the in-episode and appended-question positions "
            "would not line up episode for episode.")
    states.update(qstates)
    eps = [flat[i] for i in kept]
    y = targets(eps)
    y_own = own_targets(eps)
    print(f"  captured {len(eps)} episodes at {len(POSITIONS)} positions",
          flush=True)

    # availability, and the negative control's row restriction
    seen, det = availability(eps)
    neg_rows = np.flatnonzero(~seen[NEGATIVE_BASE])
    avail = {p: {"agent_b_marker_seen": round(float(seen[p].mean()), 4),
                 "agent_b_identity_determinable": round(float(det[p].mean()),
                                                        4)}
             for p in POSITIONS if p in seen}
    print(f"  negative control keeps {len(neg_rows)} of {len(eps)} episodes "
          f"(agent B's marker not yet named)", flush=True)

    del model, ck
    scratch = Path(tempfile.mkdtemp(prefix="other_index_sweep_"))
    try:
        tasks = []
        for (lr, pos), X in states.items():
            fn = f"L{lr}__{pos}.npy"
            np.save(scratch / fn, X)
            tasks.append((str(scratch), ckpt.name, pos, fn, lr, y))
            if pos == NEGATIVE_BASE:
                fn2 = f"L{lr}__{NEGATIVE_CONTROL}.npy"
                np.save(scratch / fn2, X[neg_rows])
                tasks.append((str(scratch), ckpt.name, NEGATIVE_CONTROL,
                              fn2, lr, y[neg_rows]))
        states.clear()

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

    # the measured ceiling: the best the read reaches where agent B's
    # marker IS the input token. Every detectable-signal figure is
    # calibrated against this, not against 1.0.
    ceiling = max(results[key(POSITIVE_CONTROL, lr)]["accuracy"]
                  for lr in PROBE_LAYERS)
    for k, rec in results.items():
        rec["smallest_detectable_share_vs_measured_ceiling"] = \
            detectable_share(rec["accuracy_needed_for_bar"],
                             rec["no_information"], ceiling)
        rec["measured_ceiling_used"] = ceiling

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
            "family_size": FAMILY_SIZE,
            "family_note": ("the same nine testable positions x five layers "
                            "x three checkpoints as the run this matches. "
                            "The positive control, the negative control and "
                            "the two diagnostic positions are not discovery "
                            "tests and are not counted. The bar is "
                            "recomputed from that count, not assumed"),
            "draw_resolution_note": F.__dict__.get("_DRAW_NOTE", (
                "zero of 200 draws establishes only p<0.005, about 2.58 "
                "standard deviations, BELOW the bar the family needs. The "
                "margin supplies the rest under a normal approximation, so "
                "a single FOUND cell is suggestive and wants a targeted "
                "rerun with far more draws, not settled")),
            "probe_layers": PROBE_LAYERS, "positions": list(POSITIONS),
            "testable_positions": list(TESTABLE),
            "positive_control": POSITIVE_CONTROL,
            "positive_control_note": (
                "the token that IS agent B's marker word, added to the "
                "eleven solely as this target's control — the matched "
                "analogue of the model's own marker token in the run this "
                "matches. It is the only place a ceiling for this target "
                "can be measured. A failure VOIDs the checkpoint; a pass "
                "does not certify sensitivity at any other position"),
            "negative_control": NEGATIVE_CONTROL,
            "negative_control_note": (
                "the model's first assignment value, restricted to the "
                "episodes in which agent B's marker word has not yet "
                "appeared anywhere. Measured on the episode builder before "
                "the run: that is half of them. Nothing about agent B is in "
                "context there, so a clearance is a leak, not carrying, and "
                "is excluded from the cells. This is the only test whose "
                "rows are restricted"),
            "diagnostic_positions": list(DIAGNOSTIC_ONLY),
            "diagnostic_note": (
                "the model's own marker token was the positive control for "
                "the OWN index and is not one for this target: it says "
                "which rank is the model's, which is the one rank agent B's "
                "cannot be. The unrestricted first assignment value is "
                "likewise reported without a role. Neither is in the "
                "family"),
            "availability": avail,
            "availability_note": (
                "per position: the share of episodes in which agent B's "
                "marker word has appeared, and the share in which agent B's "
                "IDENTITY is determinable from the tokens read. The second "
                "is the ceiling that matters and it is not 1.0 everywhere: "
                "a revision turn's value pins its agent, the 'to' one token "
                "earlier does not"),
            "exclusion_rule": (
                "no episode is dropped from any test in the family: every "
                "position is read on all episodes, exactly as the run this "
                "matches, so the two compare cell for cell. What differs "
                "between positions is the attainable ceiling, and that is "
                "reported per position as the availability shares above "
                "rather than hidden by dropping rows. The single exception "
                "is the negative control, whose restriction IS its "
                "definition"),
            "arm": ARM,
            "target_note": (
                "the rank of the OTHER REVISER's marker word among the "
                "episode's four, in vocabulary order. Four answers. "
                "Measured on 4,000 episodes before the run: the same class "
                "shares as the own register index to four decimals "
                "(0.2582, 0.2410, 0.2547, 0.2460), and never equal to it — "
                "which is the exclusion that makes this the control that "
                "settles RT-82"),
            "classifier": {
                "kind": "multinomial logistic regression (scikit-learn)",
                "penalty": "squared, at the library default strength",
                "C": C_REG, "solver": "lbfgs", "max_iter": MAX_ITER,
                "features_scaled": False,
                "note": ("imported from fitted_position_sweep_a3, not "
                         "restated, so that 'the same read' is a fact about "
                         "the code")},
            "seeding": ("folds and shuffled draws seeded per test from a "
                        "digest of checkpoint, target, position and layer "
                        "(RT-39); the target name differs from the matched "
                        "run's, so no test shares a split with it either")},
        "results": results,
        "per_arm": per_arm,
        "positive_control_holds": bool(control_holds),
        "measured_ceiling": ceiling,
        "own_index_class_shares": {
            str(int(v)): round(float((y_own == v).mean()), 4)
            for v in sorted(set(y_own.tolist()))},
        "other_index_class_shares": {
            str(int(v)): round(float((y == v).mean()), 4)
            for v in sorted(set(y.tolist()))},
        "own_and_other_never_equal": bool(np.all(y != y_own)),
        "limits": (
            "UNREGISTERED as a verdict-bearing run, diagnostic only. One "
            "fitted linear statistic, twelve positions, five layers, 4,000 "
            "episodes, three 30-million-parameter checkpoints on a "
            "synthetic grammar, one target. A null everywhere is consistent "
            "with the other agent's index being carried non-linearly, or "
            "distributed rather than resident at any one position, or in a "
            "quiet direction an unscaled fit is pulled away from (RT-34, "
            "RT-58). Under Amendment A3 section 3.2 nothing counts as "
            "localized or as absent until causal patching has also run "
            "(RT-49, RT-50); the registered term for the line's state is "
            "NOT TESTABLE (LOCALIZATION) until it does. It does not touch "
            "red-team objection R1 and changes no registered result."),
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
        "registered_instrument": "Amendment A3 section 3.1, matched control L2(a)",
        "answers_ledger_item": "RT-82 (RT-64 in the review file)",
        "prediction_stated_before_the_run": PREDICTION,
        "family_sd_bar": FAMILY_SD_BAR,
        "family_size": records[0]["settings"]["family_size"],
        "cell": detail["cell"],
        "detail": detail,
        "per_checkpoint": per,
        "measured_ceiling": {r["checkpoint"]: r["measured_ceiling"]
                             for r in records},
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
    # the instrument really is the matched run's, not a copy of it
    assert F.MAX_ITER == 2000 and F.C_REG == 1.0
    for name in ("measure_fitted", "fit_cv", "geometry", "test_seed",
                 "reproduce_anchor"):
        assert hasattr(F, name), name
    table = F.check_recorded_table_against_files()
    assert all(v == 5 for v in table.values()), table

    # the bar is recomputed, and it reproduces the matched run's on the
    # matched run's family size
    assert FAMILY_SIZE == 135, FAMILY_SIZE
    assert (FAMILY_SD_EXACT, FAMILY_SD_BAR) == (3.374, 3.38), (
        FAMILY_SD_EXACT, FAMILY_SD_BAR)
    assert family_bar(120)[1] == 3.35, family_bar(120)
    assert FAMILY_SD_BAR > SD_BAR

    # twelve positions: the eleven unchanged, plus the one control
    assert POSITIONS[:11] == tuple(W.POSITIONS) and len(POSITIONS) == 12
    assert POSITIVE_CONTROL == CONTROL_POSITION
    assert POSITIVE_CONTROL not in TESTABLE and NEGATIVE_BASE not in TESTABLE
    assert TESTABLE == W.TESTABLE and len(TESTABLE) == 9, \
        "the nine testable positions must be the matched run's nine"
    assert "own_revision_marker" not in TESTABLE

    pairs = L.paired_episodes(60, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]

    # the target: four answers, matched in rank, and never the own index
    y = targets(flat)
    yo = own_targets(flat)
    assert set(y.tolist()) <= {0, 1, 2, 3} and len(set(y.tolist())) == 4
    assert np.all(y != yo), "an agent is never its own other"
    # and it is the same quantity the own-index arm reads, off another agent
    import powered_target_test_a3 as P
    assert np.array_equal(yo, P.targets(flat)["register_index"]), \
        "the own index must be one quantity across modules"

    # the control position is agent B's marker token, and it is in range
    for ep in flat:
        enc = E.encode_episode(ep)
        ids = [int(t) for t in enc["input_ids"]]
        idx = position_indices(ep, len(ids), False)
        b = other_reviser_slot(ep)
        assert idx[CONTROL_POSITION] < len(ids)
        assert int(ids[idx[CONTROL_POSITION]]) == E.VOCAB[ep.markers[b]], \
            "the positive control must be agent B's marker token"
        # and the eleven are untouched
        base = S.position_indices(ep, len(ids), False)
        assert all(idx[p] == base[p] for p in W.POSITIONS
                   if p in base), "the eleven must not move"

    # the negative control's premise, against real episodes: on the rows
    # it keeps, agent B's marker word is nowhere in context
    seen, det = availability(flat)
    for i, ep in enumerate(flat):
        if seen[NEGATIVE_BASE][i]:
            continue
        enc = E.encode_episode(ep)
        ids = [int(t) for t in enc["input_ids"]]
        idx = position_indices(ep, len(ids), False)
        bm = E.VOCAB[ep.markers[other_reviser_slot(ep)]]
        assert bm not in ids[:idx[NEGATIVE_BASE]], \
            "the negative control's premise fails"
    assert 0 < seen[NEGATIVE_BASE].mean() < 1, \
        "the negative control must keep some episodes and drop some"

    # the grammar measured before the run, asserted so the method file and
    # the code cannot drift apart
    big = [e for p in L.paired_episodes(2000, seed=EPISODE_SEED) for e in p]
    bseen, bdet = availability(big)
    for p, (want_seen, want_det) in GRAMMAR_EXPECTED.items():
        got_seen = float(bseen[p].mean())
        got_det = float(bdet[p].mean())
        assert abs(got_seen - want_seen) <= GRAMMAR_TOL, (p, got_seen,
                                                          want_seen)
        assert abs(got_det - want_det) <= GRAMMAR_TOL, (p, got_det, want_det)
    # the prediction's premise, stated as a fact about the grammar
    assert bdet["other_revision_value"].mean() == 1.0
    assert bdet["other_revision_decision"].mean() == 0.0

    # the ceiling calibration: the correction note's worked example. The
    # own run needed 0.2774 against a no-information rate of 0.25, which
    # is 3.65% of a perfect episode but 9% of one at the measured ceiling
    assert detectable_share(0.2774, 0.25, 1.0) == 0.0365, detectable_share(
        0.2774, 0.25, 1.0)
    assert detectable_share(0.2774, 0.25, 0.553) == 0.0904, detectable_share(
        0.2774, 0.25, 0.553)
    assert detectable_share(0.2774, 0.25, 0.25) is None

    # the cells
    def cp(control=True, found=(), leak=()):
        return {"control_holds": control, "found_positions": list(found),
                "leak": list(leak)}
    V = "other_revision_value"
    assert arm_cell({PILOT: cp(control=False)})["cell"].startswith("VOID")
    assert arm_cell({PILOT: cp(), "b.pt": cp()})["cell"] == "FOUND NOWHERE"
    c = arm_cell({PILOT: cp(found=[V]), "b.pt": cp(found=[V])})
    assert c["cell"] == "FOUND SOMEWHERE"
    c = arm_cell({PILOT: cp(found=[V]), "b.pt": cp()})
    assert c["cell"] == "FOUND NOWHERE"
    assert c["sub_pattern"] == "found on the pilot only"
    c = arm_cell({PILOT: cp(), "b.pt": cp(found=[V])})
    assert c["sub_pattern"] == "found on seeds but not the pilot"
    c = arm_cell({PILOT: cp(leak=[NEGATIVE_CONTROL]), "b.pt": cp()})
    assert c["negative_control_clearances"] == {PILOT: [NEGATIVE_CONTROL]}

    # the capture substitution restores both globals, including on failure
    before = (W.POSITIONS, S.position_indices)
    try:
        capture(None, [], "cpu", False)
    except Exception:
        pass
    assert (W.POSITIONS, S.position_indices) == before, \
        "the capture substitution must restore what it patched"

    # and it does not disturb the eleven: on a small randomly-initialised
    # model — no checkpoint is read — the patched capture and an unpatched
    # `powered_position_sweep_a3.capture` must return the SAME states at
    # the eleven, element for element, and keep the same episodes
    import copy
    torch.manual_seed(0)
    toy = MVM0aModel(Config(d_model=64, n_layers=12, n_heads=2)).eval()
    small = [e for p in L.paired_episodes(12, seed=EPISODE_SEED) for e in p]
    for wq in (False, True):
        # a fresh copy per call: capture enacts the model's own turns in
        # place, so handing both calls the same objects would compare two
        # different episode sets and prove nothing
        got, got_kept = capture(toy, copy.deepcopy(small), "cpu", wq)
        want, want_kept = W.capture(toy, copy.deepcopy(small), "cpu", wq)
        assert got_kept == want_kept, "the substitution changed which " \
            "episodes are kept"
        for k, v in want.items():
            assert np.array_equal(got[k], v), f"the eleven moved at {k}"
        extra = [k for k in got if k not in want]
        assert bool(extra) is (not wq), \
            "the twelfth position is captured exactly on the no-question pass"

    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass

    print("self-test OK — the classifier, folds, seeding and null are "
          "imported from fitted_position_sweep_a3, not restated; the "
          "family bar is recomputed and reproduces 3.38 on 135 tests; the "
          "eleven positions are unmoved and the twelfth is agent B's "
          "marker token on every episode; the other-agent index has four "
          "answers, is matched in rank to the own index and is never equal "
          "to it; the negative control's premise holds against real "
          "episodes; the grammar shares asserted in the method file "
          "reproduce, including the prediction's premise that agent B is "
          "determinable at the other revision value and not at the "
          "decision one token earlier; the ceiling calibration reproduces "
          "the correction note's worked example; every cell; the capture "
          "substitution restores what it patched and returns the eleven "
          "element for element identical to an unpatched call on a "
          "randomly-initialised model. No checkpoint touched")


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
            "other_index_position_sweep_a3_a3_*.json"))
        if not paths:
            raise SystemExit("no per-checkpoint files to summarize")
        s = summarize(paths)
        out = a.out_dir / "other_index_position_sweep_a3_summary.json"
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
        out = a.out_dir / f"other_index_position_sweep_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs, a.workers)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)


if __name__ == "__main__":
    main()
