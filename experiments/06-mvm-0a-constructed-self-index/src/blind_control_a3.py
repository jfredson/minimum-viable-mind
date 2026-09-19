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


def verdict(p, d_primary, theta, majority_rate):
    """The four pre-stated cells: exhaustive, disjoint, fixed above."""
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


@torch.no_grad()
def run(ckpt: Path, lock: str | None, device: str, n_pairs: int,
        n_eval: int) -> dict:
    assert_search_blind()
    rec = lock_guard.require_lock(lock, batteries=(PRIMARY,))
    # the lock keys theta by battery and carries NO entry for the
    # control battery, which is the strict ruling encoded in data
    theta = float(rec["theta"][PRIMARY])

    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    base = T.eval_heldout(model, device, n=n_eval)
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
        lesioned = T.eval_heldout(m2, device, n=n_eval)
    finally:
        del m2.blocks[best].__dict__["forward"]

    d_found = NC3.d_metric(base, lesioned, ceil)
    return {
        "arm": "UNREGISTERED positive control for the blind arm",
        "registered": False,
        "ruled_by": "john, 2026-09-16 Pacific",
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "lock": rec["locked_utc"],
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
        "verdict": verdict(p_best, d_found.get(PRIMARY), theta, majority),
        "limits": (
            "UNREGISTERED and proposed after the pilot result was known. "
            "The ground truth is an INPUT CHANNEL removal, not an internal "
            "structure, so a sensitive result does not establish that what "
            "was found is a carried self-index rather than the input trace "
            "passed forward (red-team objection R1)."),
    }


def self_test() -> None:
    assert_search_blind()
    # the four cells, exercised without touching a checkpoint
    ok = {"accuracy": 0.9, "null_mean": 0.25, "null_sd": 0.02,
          "margin_sd": 32.5}
    no = {"accuracy": 0.26, "null_mean": 0.25, "null_sd": 0.02,
          "margin_sd": 0.5}
    assert verdict(ok, 0.9, 0.1777, 0.27)["verdict"] == "SENSITIVE"
    assert verdict(ok, 0.01, 0.1777, 0.27)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.01, 0.1777, 0.27)["verdict"] == "INSENSITIVE"
    assert verdict(no, 0.9, 0.1777, 0.27)["verdict"] == "NOT TESTABLE"
    # the sign diagnostic: a NEGATIVE d clears |theta| but is an
    # improvement, so the letter says not-testable and the signed reading
    # says insensitive. The two must disagree and say so.
    v = verdict(no, -0.9, 0.1777, 0.27)
    assert v["verdict"] == "NOT TESTABLE", "the letter of the rule stands"
    assert v["signed_reading"] == "INSENSITIVE", "signed reading differs"
    assert v["readings_agree"] is False, "disagreement must be flagged"
    assert "IMPROVES" in v["d_primary_sign"], "sign reported plainly"
    v = verdict(ok, 0.9, 0.1777, 0.27)
    assert v["readings_agree"] is True, "agreement when d is positive"
    # the degeneracy precondition, stated in advance this time
    deg = {"accuracy": 0.27, "null_mean": 0.27, "null_sd": 0.0,
           "margin_sd": None}
    v = verdict(deg, 0.9, 0.1777, 0.27)
    assert v["verdict"].startswith("DEGENERATE"), "degenerate null caught"
    assert len(v["degeneracy"]) == 3, "all three signs caught"
    # the lock gate must refuse without a lock
    try:
        lock_guard.require_lock(None, batteries=(PRIMARY,))
        raise AssertionError("must refuse without a lock")
    except lock_guard.LockError:
        pass
    print("self-test OK — four cells, degeneracy guard, blindness scan, "
          "lock gate; no result inspected")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--lock")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=200)
    ap.add_argument("--n-eval", type=int, default=400)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/blind_control_a3.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite")
    res = run(a.ckpt, a.lock, a.device, a.n_pairs, a.n_eval)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
