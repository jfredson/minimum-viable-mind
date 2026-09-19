"""Positive control for the blind arm — UNREGISTERED, ruled by John.

RULED BY JOHN, 2026-09-16 Pacific (decidedBy john), quoted:

  "Positive control: YES, run it. Same blind pipeline on the A3 pilot
  checkpoint, where zeroing the acting channel is measured load-bearing
  (0.506 to 0.182). Pre-state the criteria and commit before output,
  label it unregistered, same firewall."

**UNREGISTERED.** This is not part of the registered blind-localization
arm of RT-12 and must never be reported as though it were. It runs the
same pipeline on a different checkpoint to answer a different question,
and it was proposed after the A3 pilot's result was known. That costs it
weight and any write-up must say so. The proposal is
`blind-arm-positive-control-proposal.md`.

WHY IT IS NOW THE ONLY ROUTE. The registered arm returned NOT FLAGGED,
and the unblinded follow-up then established that the A2 register never
encoded own-agent identity at any turn: constant across episodes at the
read point, and at chance before the collapse. So the registered arm had
no valid target and says nothing about sensitivity in either direction
(`register-direct-probe-findings.md`). This control is the only remaining
way to ask whether the localization stack can find a self-structure that
is measured to matter.

THE GROUND TRUTH HERE IS MEASURED, NOT ASSUMED. On the A3 pilot
checkpoint, zeroing the acting channel takes the primary battery from
0.506 to 0.182, while the ownership-free batteries do not move (1.000 to
0.999, and 1.000 to 1.000). Across 120 content-blind ablations not one
pushed that battery below its ceiling, the worst reaching 0.2758, against
1.515 for the authorship lesion.

WHAT BLINDNESS MEANS HERE, STATED PRECISELY RATHER THAN ASSERTED. The
subspace search and the ablation operate on generic residual-stream
states and never reference the acting channel, which is the known ground
truth. A name scan enforces that this module does not touch `act_proj`.
Running the model normally does inject the acting channel, because that
is the model's ordinary operation and not knowledge of the answer; the
firewall is about where the SEARCH is allowed to look, not about
disabling the model's inputs.

PRE-STATED CRITERIA (committed before this module produced any output)
----------------------------------------------------------------------
`probe` is the best per-layer probe accuracy with its label-permutation
null. `d_found` is the ceiling-corrected drop on the primary battery
under ablating the subspace the blind search returned, at the inherited
rank. θ is 0.1777 on T_act, from John's committed threshold lock
(`6ad4362`). The lock carries no threshold for T_other, so `lock_guard`
refuses any run that tries to read the control battery for a verdict.

  SENSITIVE.      probe clears its null by 3 sd AND |d_found| >= θ.
    The stack finds a structure whose removal degrades an action known to
    depend on ownership. With the registered arm's not-flagged result,
    this is the case where the instruments look trustworthy in both
    directions, subject to the limits below.

  INSENSITIVE.    (probe clears AND |d_found| < θ)
                  OR (probe fails AND |d_found| < θ).
    The stack cannot carve a structure that is known to be there, either
    because it located a direction whose removal does not bite, or
    because it located nothing. THIS IS THE OUTCOME THAT WOULD SHIFT THE
    HONEST READING OF EXPERIMENT 1'S NULL TOWARD INSTRUMENT FAILURE, which
    RT-12 named as possibly outweighing the headline.

  NOT TESTABLE.   probe fails AND |d_found| >= θ.
    The ablation bites without a valid probe behind it, so the drop cannot
    be attributed to a located structure. Experiment 1's convergence rule.

AMBIGUITY IN MY OWN DRAFT, RESOLVED BEFORE THE RUN AND NOT AFTER. The
proposal listed INSENSITIVE as "probe clears but d inside θ, or probe
fails to clear", and NOT TESTABLE as "probe and ablation disagree". Those
overlap: probe-fails-and-d-large satisfies both as worded. The four cells
above are exhaustive and disjoint and assign that cell to NOT TESTABLE,
which is the reading that matches Experiment 1's convergence rule. This
is a clarification of wording, not a change of substance, and it is
recorded here before any output exists. It is written down because the
register probe was run on a rule with an unnoticed hole in it and the
lesson is to state the cells, not the sentences.

NON-DEGENERATE NULL IS A PRECONDITION, added from that same lesson. If
the permutation null has zero spread, or the probe accuracy exactly equals
the majority-class rate, the 3-sd comparison is vacuous and NO bin is
assigned. The run reports DEGENERATE and stops short of a verdict. In the
register probe this condition was discovered after the fact; here it is
stated in advance.

AMENDMENT RULED 2026-09-19 — APPLIES TO FUTURE RUNS ONLY
--------------------------------------------------------
John ratified Claude's proposal in conversation on 2026-09-19, verbatim:
"Yes to your view" (decidedBy mixed — Claude proposed, John approved).
The worklog entry is
"RULED 2026-09-19 — sensitivity test counts a bite by DEGRADATION
(signed), not magnitude; applies to future runs only; n >= 800 paired; a
fourth cell for 'located, wrong structure'", and it reads:

  "John ratified Claude's proposal in conversation 2026-09-19 ('Yes to
  your view'). Applies to every future run of the blind-arm
  positive-control / sensitivity pipeline. The 2026-09-16 NOT TESTABLE
  verdict is not reopened and is not reread under this rule.

  The ruling, four parts:

  1. SIGN. The ablation 'bites' only when the signed corrected drop on
  the primary battery is >= theta (theta, the locked bite threshold,
  0.1777 from the committed lock). An improvement never counts as a
  bite. Reasons recorded: the ground truth the control is checked
  against is a degradation (channel zeroing, 0.506 -> 0.182); the
  registered A3 endpoint's corrected drop is already signed, so this
  aligns the unregistered control with the registered instrument; the
  pre-stated outcome cells were written in degradation language.

  2. NOISE. Evaluate at n >= 800 episodes, with intact and ablated
  readings paired on the same evaluation seed (as endpoint_a3.py already
  does for the seeds endpoint). Rationale: theta is about 0.038 raw
  battery points on this checkpoint; evaluation noise is sd 0.0284 at
  n=400 (1.3 sd) and 0.0169 at n=800 (2.2 sd).

  3. FOURTH CELL. Add, before the next run, the cell 'probe passes AND
  the ablation improves the primary battery beyond noise' = LOCATED,
  WRONG STRUCTURE. It is neither PASS, INSENSITIVE, nor NOT TESTABLE.

  4. PROCESS. The rule is committed to the criteria file (successor to
  a3c5fbf) before anything executes, with this ruling quoted. No
  registered text changes; the control remains unregistered.

  Open, not ruled: whether to replace the single-threshold bite with a
  partial-ablation dose ladder requiring monotone degradation
  (research-note-pain-axis-2026-09-19.md item 4). That belongs to the
  reframed 2026-10-04 proposal."

WHAT THIS CHANGES, AND WHAT IT DELIBERATELY DOES NOT.

FUTURE RUNS ONLY. The cells stated above this block are the criteria the
2026-09-16 run was read against, and they stand exactly as committed.
That run's verdict — NOT TESTABLE — is not reopened, not reread and not
rewritten under this amendment. The record of what was committed before
output is the whole value of the file; annotate, never rewrite.

STILL UNREGISTERED. This control is not part of the registered
blind-localization arm and this amendment does not make it one. No
registered text is touched.

THE CODE BELOW STILL IMPLEMENTS THE 2026-09-16 LETTER, AND MUST BE
CHANGED BEFORE THE NEXT RUN. As committed here, `verdict()` tests
`abs(d_primary) >= theta` and reports the signed reading only as a
diagnostic beside the pre-stated bin, and `--n-eval` defaults to 400.
Under this ruling the next run must instead (a) make the signed drop the
bite test, (b) evaluate at 800 episodes or more with intact and ablated
readings paired on the same evaluation seed, and (c) carry the fourth
cell, LOCATED, WRONG STRUCTURE, for a probe that passes while the
ablation improves the primary battery beyond noise. Until those three
land in the code, this module must not be run for a verdict. The rule is
recorded before the implementation on purpose: it is the ruling that
binds, and a rule written after its own run is worth nothing.

HOW THE RULING IS IMPLEMENTED, WRITTEN DOWN BEFORE IT RAN
---------------------------------------------------------
Implemented 2026-09-19, in the same commit as this paragraph and before
this module produced any output under the new rule. The paragraph above
stands as written; it was true when committed and is now discharged.

WHICH RULE RUNS. `--rule` selects the criteria. It defaults to
`2026-09-19`, the signed rule. `--rule 2026-09-16` reaches the original
cells unchanged, so the criteria the first run was read against stay
executable and anyone can reproduce that reading. The old cells are
reachable for the record; they are not the default and must not be used
for a fresh verdict.

1. SIGN. Under `2026-09-19` the ablation bites when the signed corrected
drop on the primary battery is at least theta. An improvement never
counts. The old absolute-value test lives on only under `--rule
2026-09-16`.

2. NOISE. `--n-eval` defaults to 800 and the run refuses fewer than 800
episodes under the signed rule. Intact and ablated readings are taken
with the same `--eval-seed`, so both read the SAME held-out episodes and
the drop is paired within the seed, the way the seeds endpoint already
pairs its draws. The seed used is recorded in the output.

3. FOURTH CELL, and what "beyond noise" was fixed to mean. The cell is
"the probe clears its null by 3 standard deviations AND the ablation
improves the primary battery beyond noise" = LOCATED, WRONG STRUCTURE.
"Beyond noise" needs a number, and choosing one after seeing a result
would be worthless, so it is fixed here:

    an improvement counts when the signed corrected drop is at most
    minus the IMPROVEMENT BAR, where

        improvement bar = max(theta, 3 x noise, in corrected units)

    and "noise" is the measured spread of this evaluation between
    independent draws at 800 episodes on the primary battery — 0.0169
    raw accuracy points, twelve draws, from `a3-gates/eval_noise_a3.json`
    — divided by this run's own corrected-drop denominator (baseline
    minus the battery's measured shortcut ceiling), which is what turns
    raw accuracy points into the units theta is written in.

Why the larger of the two, rather than either alone. Theta alone is the
exact mirror of the bite and is already about 2.2 standard deviations of
this evaluation's noise at 800 episodes, so it is a defensible reading of
"beyond noise" on its own. Three standard deviations alone matches the
bar the probe side already has to clear, and refusing to hold an
improvement to a weaker standard than a probe clearance is the more
conservative choice. Taking the larger means an improvement is harder to
declare than a bite. That asymmetry is deliberate: this control is
unregistered and was proposed after a result was known, so the cell that
would be most interesting to land in should be the hardest to reach, not
the easiest. Between the two candidate bars the stricter one governs, and
which one that is depends on the baseline, so both are reported.

Note the measured noise figure comes from the PILOT checkpoint. Applied
to any other checkpoint it is an assumption, not a measurement, and the
output says so on its face for every checkpoint that is not the pilot.

A GAP BETWEEN THE TWO BARS IS NOT A FIFTH CELL. When three standard
deviations of noise exceeds theta, drops between minus the bar and minus
theta are improvements too small to call, and they land in INSENSITIVE
along with every other reading that neither bites nor clears the
improvement bar. That is the same place the old rule's small drops went.
No bin is added.

WHEN THE DROP CANNOT BE COMPUTED AT ALL — a design call made while
building, not part of John's ruling (decidedBy agent, 2026-09-19). The
corrected drop is undefined when the primary battery's baseline sits at
or below its own measured shortcut ceiling, because the denominator is a
range the battery cannot traverse; the metric returns nothing rather
than a number. The 2026-09-16 code treated that silence as "did not
bite" and would have reported INSENSITIVE, which claims the stack was
tested when it was not. Under the signed rule the run instead reports
NOT READABLE and assigns no bin. This matters in advance and not in
hindsight: the control battery on the pilot is already known to sit
below its ceiling, so a checkpoint whose primary battery does the same
is a live possibility on the seeds this has not yet run on. Recorded
here before any such run, so it cannot be mistaken for a repair made
after seeing one.

WHAT IS UNCHANGED. The blind search, the ablation, the rank, the probe
layers, the 3-standard-deviation probe bar, the degeneracy precondition,
the blindness scan, the lock gate, the refusal to overwrite a result
file, and every word of the criteria committed on 2026-09-16.

WHAT A SENSITIVE RESULT STILL CANNOT SHOW. That ownership is load-bearing
on this checkpoint was established by removing an INPUT CHANNEL, not an
internal structure. So a sensitive result shows the stack can find
something whose removal hurts the action. It does not establish that the
thing found is a carried self-index rather than the input trace passed
forward. That is objection R1 in the amendment's own red team and this
control does not answer it.

No bin is added after the fact. A result fitting none of these is reported
as fitting none.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on John's threshold lock; fresh output file, nothing overwritten.

    ../../../.venv/bin/python blind_control_a3.py --self-test
    ../../../.venv/bin/python blind_control_a3.py --ckpt <a3> --lock <lock> --run
    ../../../.venv/bin/python blind_control_a3.py --ckpt <a3> --lock <lock> \
        --run --rule 2026-09-16      # the original cells, for the record
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import encoding_a3 as E
import lock_guard
import localize_a3 as L
import null_calibration_a3 as NC3
import train_a3 as T
from model import MVM0aModel, Config

PRIMARY = "T_act"
SD_BAR = 3.0
RANK_CAP = L.RANK_CAP

# The criteria in force. The signed rule of 2026-09-19 is the default; the
# 2026-09-16 cells stay reachable so the first run's reading reproduces.
RULE_SIGNED = "2026-09-19"
RULE_ORIGINAL = "2026-09-16"
RULES = (RULE_SIGNED, RULE_ORIGINAL)

# The ruling's noise clause: at least 800 episodes, intact and ablated
# paired on one evaluation seed.
MIN_EVAL_N = 800

# Measured spread of this evaluation between independent draws at 800
# episodes on the primary battery, twelve draws, on the PILOT checkpoint
# (`a3-gates/eval_noise_a3.json`). Raw accuracy points; converted into the
# corrected units theta is written in at run time, by this run's own
# denominator. On any other checkpoint this is an assumption, and the
# output says so.
EVAL_NOISE_SD_RAW = 0.0169
EVAL_NOISE_N = 800
EVAL_NOISE_SOURCE = "a3-gates/eval_noise_a3.json (pilot, a3_30m_seed0.pt)"
NOISE_SD_BAR = 3.0
PILOT_CHECKPOINT = "a3_30m_seed0.pt"

# The search must never name the known ground truth.
FORBIDDEN = ("act_proj",)


def assert_search_blind() -> None:
    """Fail if this module names the acting channel, which is the known
    ground truth. The firewall is a property of the code, not a promise."""
    src = Path(__file__).read_text()
    body = src[src.index("def assert_search_blind"):]
    body = body[body.index("\n\n"):]
    hits = sorted({n for n in FORBIDDEN if n in body})
    if hits:
        raise AssertionError(
            f"BLINDNESS VIOLATED: the search references {hits}. The "
            f"pipeline must not know where the ground truth lives.")


def degenerate(p, majority_rate):
    """Preconditions for the 3-sd rule to mean anything. Stated in advance,
    unlike in the register probe where this was found afterwards."""
    bad = []
    if p["null_sd"] == 0:
        bad.append("the label-permutation null has zero spread; the 3-sd "
                   "comparison would compare a number to itself")
    if p.get("margin_sd") is None:
        bad.append("margin in standard deviations is undefined")
    if abs(p["accuracy"] - majority_rate) < 1e-9:
        bad.append(f"accuracy ({p['accuracy']}) equals the majority-class "
                   f"rate ({round(majority_rate, 4)}) exactly, the score of "
                   f"a constant classifier")
    return bad


def verdict_20260916(p, d_primary, theta, majority_rate):
    """The four cells committed on 2026-09-16, unchanged, body and all.

    NOT THE DEFAULT since 2026-09-19. Kept executable so the reading the
    first run was scored against can be reproduced exactly, and so the
    amendment can be checked against something rather than described.
    Reached only by `--rule 2026-09-16`. `bites` here is the absolute
    value, which is the hole the amendment closes.
    """
    bad = degenerate(p, majority_rate)
    if bad:
        return {"verdict": "DEGENERATE — no bin assigned",
                "degeneracy": bad,
                "note": "the 3-sd rule's precondition fails; see the "
                        "module docstring"}
    clears = p["accuracy"] >= p["null_mean"] + SD_BAR * p["null_sd"]
    bites = d_primary is not None and abs(d_primary) >= theta
    if clears and bites:
        v, m = "SENSITIVE", (
            "the stack found a structure whose removal degrades an action "
            "known to depend on ownership")
    elif clears and not bites:
        v, m = "INSENSITIVE", (
            "the stack located a direction, but removing it does not bite; "
            "it cannot carve a structure known to be there")
    elif not clears and not bites:
        v, m = "INSENSITIVE", (
            "the stack located nothing, and what it did ablate does not "
            "bite")
    else:
        v, m = "NOT TESTABLE", (
            "the ablation bites without a valid probe behind it, so the "
            "drop cannot be attributed to a located structure")
    # SIGN DIAGNOSTIC, added 2026-09-16 AFTER the first run, reported
    # BESIDE the pre-stated verdict and never replacing it.
    #
    # The pre-stated rule says the ablation bites when |d| >= theta. The
    # first run returned d = -0.3516 on the primary battery: the magnitude
    # clears theta, but the sign is negative, meaning the ablation made
    # the battery BETTER. A sensitivity test asks whether removing the
    # located structure DEGRADES the action, so an absolute value lets an
    # improvement count as a bite. That is a hole in the rule as I wrote
    # it, and this records it rather than repairing the output.
    #
    # The signed reading is what the cells would say if "bites" meant
    # "degrades". It assigns no bin. John rules on which is authoritative.
    degrades = d_primary is not None and d_primary >= theta
    if clears and degrades:
        signed = "SENSITIVE"
    elif not clears and not degrades:
        signed = "INSENSITIVE"
    elif clears and not degrades:
        signed = "INSENSITIVE"
    else:
        signed = "NOT TESTABLE"
    return {"verdict": v, "means": m, "probe_clears_3sd": bool(clears),
            "ablation_reaches_theta": bool(bites),
            "d_primary_sign": (None if d_primary is None else
                               ("degrades" if d_primary > 0 else
                                "IMPROVES the battery" if d_primary < 0
                                else "no change")),
            "signed_reading": signed,
            "signed_reading_note": (
                "diagnostic only, assigns no bin. The pre-stated rule uses "
                "|d| >= theta; this is what the same cells give if 'bites' "
                "means 'degrades'. Where the two disagree, the pre-stated "
                "verdict above is what was committed and the disagreement "
                "is the finding. See blind-control-findings.md."),
            "readings_agree": bool(signed == v)}


def improvement_bar(base_primary, ceil_primary, theta, checkpoint_name):
    """What "improves beyond noise" was fixed to mean, before any run.

    The measured eval-to-eval spread is in raw accuracy points; theta is
    in corrected-drop units. This run's own denominator converts one into
    the other, so the bar tracks the checkpoint's own headroom instead of
    importing the pilot's. The bar is the larger of theta and three of
    those standard deviations; see the module docstring for why the
    stricter of the two governs.
    """
    den = base_primary - ceil_primary
    if den < NC3.FLOOR_MARGIN:
        return {"computable": False,
                "reason": ("the primary battery's baseline is at or below "
                           "its own measured shortcut ceiling, so the "
                           "corrected drop has no denominator"),
                "baseline": base_primary, "ceiling": ceil_primary,
                "bar": None}
    noise_corrected = EVAL_NOISE_SD_RAW / den
    bar = max(theta, NOISE_SD_BAR * noise_corrected)
    return {
        "computable": True,
        "baseline": base_primary, "ceiling": ceil_primary,
        "denominator": round(den, 4),
        "eval_noise_sd_raw": EVAL_NOISE_SD_RAW,
        "eval_noise_n": EVAL_NOISE_N,
        "eval_noise_source": EVAL_NOISE_SOURCE,
        "eval_noise_sd_corrected": round(noise_corrected, 4),
        "candidate_bar_theta": theta,
        "candidate_bar_3sd_noise": round(NOISE_SD_BAR * noise_corrected, 4),
        "bar": round(bar, 4),
        "bar_governed_by": ("theta" if theta >= NOISE_SD_BAR *
                            noise_corrected else
                            "3 standard deviations of evaluation noise"),
        "noise_figure_measured_on_this_checkpoint":
            checkpoint_name == PILOT_CHECKPOINT,
        "noise_caveat": (
            "the spread was measured on the pilot checkpoint; on this one "
            "it is an assumption carried over, not a measurement"
            if checkpoint_name != PILOT_CHECKPOINT else
            "the spread was measured on this checkpoint"),
    }


def verdict_20260919(p, d_primary, theta, majority_rate, bar_rec):
    """The cells in force after John's ruling of 2026-09-19.

    Four cells, exhaustive and disjoint over (does the probe clear, what
    did the signed drop do), plus two no-bin outcomes that were stated in
    advance: the degenerate null, carried over from 2026-09-16, and an
    undefined drop, added here.

      SENSITIVE.              probe clears AND the signed drop >= theta.
      LOCATED, WRONG STRUCTURE.
                              probe clears AND the ablation IMPROVES the
                              primary battery past the improvement bar.
      INSENSITIVE.            probe clears and the drop does neither;
                              or the probe fails and the drop does not
                              reach theta, improvement or not.
      NOT TESTABLE.           probe fails AND the signed drop >= theta.
    """
    bad = degenerate(p, majority_rate)
    if bad:
        return {"rule": RULE_SIGNED,
                "verdict": "DEGENERATE — no bin assigned",
                "degeneracy": bad,
                "note": "the 3-sd rule's precondition fails; see the "
                        "module docstring"}
    clears = p["accuracy"] >= p["null_mean"] + SD_BAR * p["null_sd"]
    if d_primary is None or not bar_rec.get("computable"):
        return {"rule": RULE_SIGNED,
                "verdict": "NOT READABLE — no bin assigned",
                "probe_clears_3sd": bool(clears),
                "improvement_bar": bar_rec,
                "note": ("the corrected drop on the primary battery is "
                         "undefined, so neither the bite test nor the "
                         "improvement test can be applied. Reporting a "
                         "cell here would claim the stack was tested when "
                         "it was not. Stated in advance; see the module "
                         "docstring.")}
    bar = bar_rec["bar"]
    bites = d_primary >= theta
    improves = d_primary <= -bar
    if clears and bites:
        v, m = "SENSITIVE", (
            "the stack found a structure whose removal degrades an action "
            "known to depend on ownership")
    elif clears and improves:
        v, m = "LOCATED, WRONG STRUCTURE", (
            "the probe cleared its null, so something was located, but "
            "removing it makes the ownership battery BETTER by more than "
            "this evaluation moves on its own. Whatever was carved is not "
            "the structure the action depends on. This is neither a pass, "
            "nor insensitivity, nor a missing probe")
    elif clears:
        v, m = "INSENSITIVE", (
            "the stack located a direction, but removing it neither "
            "degrades the action by theta nor improves it past the bar; "
            "it cannot carve a structure known to be there")
    elif not bites:
        v, m = "INSENSITIVE", (
            "the stack located nothing, and what it did ablate does not "
            "bite. An improvement, however large, is not a bite under "
            "this rule and does not reach the fourth cell without a probe "
            "behind it")
    else:
        v, m = "NOT TESTABLE", (
            "the ablation bites without a valid probe behind it, so the "
            "drop cannot be attributed to a located structure")
    return {
        "rule": RULE_SIGNED,
        "verdict": v, "means": m,
        "probe_clears_3sd": bool(clears),
        "signed_drop": d_primary,
        "bites_signed": bool(bites),
        "improves_beyond_noise": bool(improves),
        "theta": theta,
        "improvement_bar": bar_rec,
        "d_primary_sign": ("degrades" if d_primary > 0 else
                           "IMPROVES the battery" if d_primary < 0
                           else "no change"),
        "absolute_value_reading": (
            "the superseded 2026-09-16 test, |drop| >= theta, would call "
            f"this {'a bite' if abs(d_primary) >= theta else 'no bite'}; "
            "reported so the two rules can be compared, and carrying no "
            "weight"),
    }


def verdict(p, d_primary, theta, majority_rate, *, rule=RULE_SIGNED,
            bar_rec=None):
    """Dispatch to the criteria named by `rule`. Defaults to the signed
    rule; the 2026-09-16 cells are reachable and never automatic."""
    if rule == RULE_ORIGINAL:
        out = verdict_20260916(p, d_primary, theta, majority_rate)
        out.setdefault("rule", RULE_ORIGINAL)
        out["rule_note"] = (
            "SUPERSEDED criteria, run on request. These are the cells the "
            "2026-09-16 run was read against. John's ruling of 2026-09-19 "
            "replaced the absolute-value bite test with a signed one for "
            "all future runs; a fresh verdict must not be taken from here.")
        return out
    if rule != RULE_SIGNED:
        raise ValueError(f"unknown rule {rule!r}; expected one of {RULES}")
    return verdict_20260919(p, d_primary, theta, majority_rate, bar_rec)


@torch.no_grad()
def run(ckpt: Path, lock: str | None, device: str, n_pairs: int,
        n_eval: int, rule: str = RULE_SIGNED,
        eval_seed: int = T.HELDOUT_SEED) -> dict:
    assert_search_blind()
    if rule not in RULES:
        raise SystemExit(f"unknown --rule {rule!r}; expected one of {RULES}")
    if rule == RULE_SIGNED and n_eval < MIN_EVAL_N:
        raise SystemExit(
            f"REFUSING to run: the ruling of 2026-09-19 requires at least "
            f"{MIN_EVAL_N} evaluation episodes and --n-eval is {n_eval}. "
            f"Theta is about 0.038 raw battery points on this checkpoint "
            f"and this evaluation moves 0.0284 between draws at 400, which "
            f"is why the floor exists.")
    rec = lock_guard.require_lock(lock, batteries=(PRIMARY,))
    # the lock keys theta by battery and carries NO entry for the
    # control battery, which is the strict ruling encoded in data
    theta = float(rec["theta"][PRIMARY])

    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    # PAIRED: intact and ablated read the SAME held-out episodes, because
    # the evaluation is seeded and both calls are given the same seed. The
    # drop is therefore a within-seed difference and is not exposed to the
    # between-seed spread the noise clause is about.
    base = T.eval_heldout(model, device, n=n_eval, seed=eval_seed)
    ceil = NC3.ceilings()

    pairs = L.paired_episodes(n_pairs, seed=20260917)
    flat = [e for p in pairs for e in p]
    acts, eps = L.residuals_at(model, flat, device)
    y = [e.own_slot for e in eps]
    counts = {int(c): y.count(c) for c in sorted(set(y))}
    majority = max(counts.values()) / len(y)

    probes = {str(Lr): L.fit_probe(acts[Lr], y, seed=Lr)
              for Lr in L.PROBE_LAYERS}
    best = max(L.PROBE_LAYERS, key=lambda k: probes[str(k)]["accuracy"])
    p_best = probes[str(best)]

    # ablate what the blind search found, at the inherited rank
    d = L.own_direction(acts[best], y, rank=RANK_CAP)
    m2 = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    m2.load_state_dict(ck["state"])
    D = torch.as_tensor(d, device=device, dtype=torch.float32)
    ref = torch.as_tensor(acts[best], device=device, dtype=torch.float32)
    mu = (ref @ D.T).mean(0)
    blk = m2.blocks[best]
    orig = blk.forward

    def abl(x, kv, rr, _o=orig, _D=D, _mu=mu):
        x, ctx = _o(x, kv, rr)
        return x + (_mu - x @ _D.T) @ _D, ctx

    blk.forward = abl
    try:
        lesioned = T.eval_heldout(m2, device, n=n_eval, seed=eval_seed)
    finally:
        del m2.blocks[best].__dict__["forward"]

    d_found = NC3.d_metric(base, lesioned, ceil)
    bar_rec = improvement_bar(base[PRIMARY], ceil[PRIMARY], theta, ckpt.name)
    return {
        "arm": "UNREGISTERED positive control for the blind arm",
        "registered": False,
        "ruled_by": ("john, 2026-09-16 Pacific; amended 2026-09-19 "
                     "(decidedBy mixed — Claude proposed, John approved)"),
        "criteria_rule": rule,
        "criteria_note": (
            "the signed rule of 2026-09-19: a bite is a signed corrected "
            "drop of at least theta, an improvement is never a bite, and "
            "a probe that clears while the ablation improves the battery "
            "beyond noise is the fourth cell, LOCATED, WRONG STRUCTURE"
            if rule == RULE_SIGNED else
            "SUPERSEDED — the 2026-09-16 cells, run on request for the "
            "record. Not a fresh verdict."),
        "eval": {"harness": "train_a3.eval_heldout", "n": n_eval,
                 "seed": eval_seed, "paired_on_one_seed": True,
                 "min_required_under_signed_rule": MIN_EVAL_N,
                 "note": ("intact and ablated readings are taken on the "
                          "same seeded episode set, so the drop is paired "
                          "within the seed")},
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "lock": rec["locked_utc"],
        "lock_checkpoint": rec["checkpoint"],
        "theta_calibrated_on_this_checkpoint":
            rec["checkpoint"] == ckpt.name,
        "theta_used": theta,
        "primary_battery": PRIMARY,
        "sd_bar": SD_BAR,
        "rank": int(d.shape[0]),
        "probe_layers": L.PROBE_LAYERS,
        "probes": probes,
        "best_layer": best,
        "label_counts": counts,
        "majority_class_rate": round(majority, 4),
        "baseline": base,
        "lesioned_found_subspace": lesioned,
        "ceilings_used": ceil,
        "d_found": d_found,
        "improvement_bar": bar_rec,
        "verdict": verdict(p_best, d_found.get(PRIMARY), theta, majority,
                           rule=rule, bar_rec=bar_rec),
        "limits": (
            "UNREGISTERED and proposed after the pilot result was known. "
            "The ground truth is an INPUT CHANNEL removal, not an internal "
            "structure, so a sensitive result does not establish that what "
            "was found is a carried self-index rather than the input trace "
            "passed forward (red-team objection R1). Theta comes from a "
            "lock calibrated on the pilot checkpoint; on any other "
            "checkpoint it is a borrowed threshold, and the field "
            "theta_calibrated_on_this_checkpoint says which case this "
            "is."),
    }


def self_test() -> None:
    assert_search_blind()
    TH = 0.1777
    ok = {"accuracy": 0.9, "null_mean": 0.25, "null_sd": 0.02,
          "margin_sd": 32.5}
    no = {"accuracy": 0.26, "null_mean": 0.25, "null_sd": 0.02,
          "margin_sd": 0.5}
    deg = {"accuracy": 0.27, "null_mean": 0.27, "null_sd": 0.0,
           "margin_sd": None}

    # ---- the 2026-09-16 cells, still reachable and still passing ----
    R0 = {"rule": RULE_ORIGINAL}
    assert verdict(ok, 0.9, TH, 0.27, **R0)["verdict"] == "SENSITIVE"
    assert verdict(ok, 0.01, TH, 0.27, **R0)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.01, TH, 0.27, **R0)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.9, TH, 0.27, **R0)["verdict"] == "NOT TESTABLE"
    # the sign diagnostic: a NEGATIVE d clears |theta| but is an
    # improvement, so the letter says not-testable and the signed reading
    # says insensitive. The two must disagree and say so.
    v = verdict(no, -0.9, TH, 0.27, **R0)
    assert v["verdict"] == "NOT TESTABLE", "the letter of the rule stands"
    assert v["signed_reading"] == "INSENSITIVE", "signed reading differs"
    assert v["readings_agree"] is False, "disagreement must be flagged"
    assert "IMPROVES" in v["d_primary_sign"], "sign reported plainly"
    v = verdict(ok, 0.9, TH, 0.27, **R0)
    assert v["readings_agree"] is True, "agreement when d is positive"
    assert "SUPERSEDED" in verdict(ok, 0.9, TH, 0.27, **R0)["rule_note"]
    # the degeneracy precondition, stated in advance this time
    v = verdict(deg, 0.9, TH, 0.27, **R0)
    assert v["verdict"].startswith("DEGENERATE"), "degenerate null caught"
    assert len(v["degeneracy"]) == 3, "all three signs caught"

    # ---- the improvement bar, fixed before any run read it ----
    # pilot-shaped numbers: baseline 0.566, ceiling 0.2921 -> denominator
    # 0.2739, so one standard deviation of evaluation noise is about 0.062
    # corrected and three of them just clear theta.
    bar = improvement_bar(0.566, 0.2921, TH, PILOT_CHECKPOINT)
    assert bar["computable"] and bar["bar"] == max(
        TH, bar["candidate_bar_3sd_noise"]), "the stricter bar governs"
    assert bar["noise_figure_measured_on_this_checkpoint"] is True
    assert improvement_bar(0.566, 0.2921, TH, "a3_30m_seed1.pt")[
        "noise_figure_measured_on_this_checkpoint"] is False, \
        "a borrowed noise figure must say so"
    # a battery at or under its ceiling has no denominator and no bar
    floored = improvement_bar(0.29, 0.2921, TH, PILOT_CHECKPOINT)
    assert floored["computable"] is False and floored["bar"] is None

    # ---- the cells in force: signed, with the fourth ----
    B = {"bar_rec": bar}
    big = bar["bar"] + 0.1
    assert verdict(ok, 0.9, TH, 0.27, **B)["verdict"] == "SENSITIVE"
    assert verdict(ok, 0.01, TH, 0.27, **B)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.01, TH, 0.27, **B)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.9, TH, 0.27, **B)["verdict"] == "NOT TESTABLE"
    # SIGN. An improvement is never a bite, however large, so the cell
    # that the absolute-value rule gave to NOT TESTABLE now turns on
    # whether a probe cleared.
    v = verdict(no, -big, TH, 0.27, **B)
    assert v["verdict"] == "INSENSITIVE", "no probe, so no fourth cell"
    assert v["bites_signed"] is False, "an improvement is not a bite"
    assert "would call this a bite" in v["absolute_value_reading"], \
        "the superseded reading is reported beside, not instead"
    assert verdict(no, -big, TH, 0.27, **R0)["verdict"] == "NOT TESTABLE", \
        "the two rules must part company on exactly this reading"
    # FOURTH CELL. Probe clears, ablation improves past the bar.
    v = verdict(ok, -big, TH, 0.27, **B)
    assert v["verdict"] == "LOCATED, WRONG STRUCTURE", "fourth cell fires"
    assert v["improves_beyond_noise"] is True
    # An improvement inside the bar is not the fourth cell; it lands in
    # INSENSITIVE with everything else too small to call.
    v = verdict(ok, -(bar["bar"] - 0.01), TH, 0.27, **B)
    assert v["verdict"] == "INSENSITIVE", "the gap is not a fifth cell"
    assert v["improves_beyond_noise"] is False
    # exactly on the bar counts, exactly on theta counts
    assert verdict(ok, -bar["bar"], TH, 0.27, **B)["verdict"] == \
        "LOCATED, WRONG STRUCTURE", "the bar is inclusive"
    assert verdict(ok, TH, TH, 0.27, **B)["verdict"] == "SENSITIVE", \
        "theta is inclusive"
    # NOT READABLE: an undefined drop assigns no bin under either branch
    for probe in (ok, no):
        v = verdict(probe, None, TH, 0.27, **B)
        assert v["verdict"].startswith("NOT READABLE"), "undefined drop"
        v = verdict(probe, 0.9, TH, 0.27, bar_rec=floored)
        assert v["verdict"].startswith("NOT READABLE"), "no denominator"
    # the degeneracy precondition still comes first
    v = verdict(deg, 0.9, TH, 0.27, **B)
    assert v["verdict"].startswith("DEGENERATE"), "degenerate null caught"

    # ---- the 2026-09-16 run, replayed under the new rule ----
    # That run: probe did NOT clear, corrected drop -0.3516, baseline
    # 0.44 at 400 episodes. Signed, it is INSENSITIVE, which is what the
    # sign diagnostic said at the time. The amendment must not quietly
    # move it into the new fourth cell, which needs a probe behind it.
    bar400 = improvement_bar(0.44, 0.2921, TH, PILOT_CHECKPOINT)
    v = verdict(no, -0.3516, TH, 0.2725, bar_rec=bar400)
    assert v["verdict"] == "INSENSITIVE", \
        "a failed probe cannot reach the fourth cell"
    assert verdict(no, -0.3516, TH, 0.2725, **R0)["verdict"] == \
        "NOT TESTABLE", "the 2026-09-16 reading is untouched"

    # ---- an unknown rule is refused rather than guessed at ----
    try:
        verdict(ok, 0.9, TH, 0.27, rule="2026-09-18", bar_rec=bar)
        raise AssertionError("an unknown rule must refuse")
    except ValueError:
        pass
    # ---- the noise floor on the evaluation ----
    try:
        run(Path("nonexistent.pt"), None, "cpu", 4, 400)
        raise AssertionError("fewer than 800 episodes must refuse")
    except SystemExit as e:
        assert "800" in str(e), "the refusal must say what it wants"
    # the lock gate must refuse without a lock
    try:
        lock_guard.require_lock(None, batteries=(PRIMARY,))
        raise AssertionError("must refuse without a lock")
    except lock_guard.LockError:
        pass
    print(f"self-test OK — signed rule ({RULE_SIGNED}) default: four "
          f"cells including LOCATED, WRONG STRUCTURE, the improvement "
          f"bar, undefined-drop and degeneracy guards, the 800-episode "
          f"floor, the blindness scan and the lock gate; the "
          f"{RULE_ORIGINAL} cells still reachable and still passing; no "
          f"result inspected")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--lock")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=200)
    ap.add_argument("--n-eval", type=int, default=MIN_EVAL_N)
    ap.add_argument("--eval-seed", dest="eval_seed", type=int,
                    default=T.HELDOUT_SEED,
                    help="one seed for BOTH the intact and the ablated "
                         "reading, so the drop is paired")
    ap.add_argument("--rule", default=RULE_SIGNED, choices=list(RULES),
                    help="which committed criteria to score against; the "
                         "2026-09-16 cells are reachable for the record "
                         "and are not the default")
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.ckpt is None:
        raise SystemExit("--run needs --ckpt")
    if a.out is None:
        tag = "signed" if a.rule == RULE_SIGNED else "rule20260916"
        a.out = Path(f"../a3-gates/blind_control_a3_{tag}_"
                     f"{a.ckpt.stem}_n{a.n_eval}.json")
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite")
    res = run(a.ckpt, a.lock, a.device, a.n_pairs, a.n_eval, a.rule,
              a.eval_seed)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
