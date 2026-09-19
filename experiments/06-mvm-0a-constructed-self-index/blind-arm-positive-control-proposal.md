# Companion positive control for the blind arm — PROPOSAL, UNREGISTERED

*2026-09-16. **Status: PROPOSAL. Not registered, not run, not
authorized.** Written on John's instruction to propose rather than run it
(2026-09-16 Pacific). It sits outside the registered blind-localization
arm of RT-12 and must never be reported as part of it. John rules on this
separately. Local, $0, no compute.*

## Why the registered arm alone cannot settle the question

The registered arm runs on the A2 register-bearing checkpoints. John
ruled on 2026-09-16 that it runs there as a **false-positive test**,
because the register exists by construction but was measured inert:
removing its injection entirely left every battery unchanged.

That gives a clean read on **specificity** — whether the localization
stack cries wolf on a structure that does not matter. It gives **nothing
on sensitivity**, and the reason is structural rather than a matter of
effort: that checkpoint contains no load-bearing self-structure for the
stack to find, so no result there can show whether the stack would find
one. A not-flagged outcome on the registered arm therefore supports
specificity only, which is stated in the arm's own pre-committed criteria
so the overclaim is foreclosed before the number is seen.

Sensitivity needs a checkpoint where something is **measured** to be
load-bearing. Until 2026-09-16 the programme had none. It now has one.

## What changed

The A3 pilot established a ground truth of the shape the programme has
been missing. Zeroing the acting channel — the only authorship signal in
the design — takes the primary battery from **0.506 to 0.182**, while the
ownership-free batteries do not move at all (1.000 to 0.999, and 1.000 to
1.000). Across 120 content-blind ablations not one pushed that battery
below its ceiling, the worst reaching 0.2758, against 1.515 for the
authorship lesion.

So on that checkpoint, ownership is load-bearing and the fact is
measured, not assumed. What is *not* known is where it lives, which is
exactly the condition a sensitivity test needs: the answer exists, and
the grader does not know it either.

## The proposal

Run the same blind pipeline, unchanged, on the A3 pilot checkpoint
`a3_30m_seed0.pt` (md5 `f751228c…`). Same rank cap, same layer depths,
same permutation null, same generic residual-stream search. The only
difference is the checkpoint.

**Pre-stated criteria, committed before any run.** Let `probe` be the
best per-layer probe accuracy with its permutation null, and `d_found`
the ceiling-corrected drop under ablating the found subspace.

- **SENSITIVE.** `probe ≥ null_mean + 3·null_sd` **and** `|d_found|` on
  the primary battery `≥ θ` (0.1777, from the committed threshold lock).
  Reads: the stack finds a structure whose removal degrades an action
  that is known to depend on ownership. Combined with a not-flagged
  result on the registered arm, this is the case where the instruments
  look trustworthy in both directions.
- **INSENSITIVE.** `probe` clears its null but `|d_found|` stays inside
  θ, **or** `probe` fails to clear. Reads: the stack cannot carve a
  structure that is known to be there. **This is the outcome that would
  shift the honest reading of Experiment 1's null toward instrument
  failure**, which RT-12 named as possibly outweighing the headline.
- **NOT TESTABLE.** Probe and ablation disagree under Experiment 1's
  convergence rule.

**What it still cannot show.** That ownership is load-bearing on this
checkpoint is established by removing the *input channel*, not by
removing an internal structure. So a sensitive result shows the stack can
find *something* whose removal hurts the action; it does not establish
that the thing found is a carried self-index rather than the input trace
passed forward. That is objection R1 in the amendment's own red team, and
this control does not answer it.

## Why it is unregistered, and what that costs

The registered arm is fixed: Experiment 1's pipeline, blind, on a
register-bearing checkpoint. Running the same pipeline on a different
checkpoint to answer a different question is a new test, and calling it
part of the registered arm would be exactly the scope creep the
registration exists to prevent.

The cost of that honesty is that a sensitive result here carries less
weight than a registered one would. It is an unregistered control,
proposed after the pilot's result was known, and any write-up must say
so. What it buys in exchange is the only available check on the
direction the registered arm structurally cannot test.

## What is asked

A yes or no on running it. It is local, free, needs no pod, and touches
no registered text. If yes, the criteria above are committed first and
the run follows, in the same verdict-first order the registered arm used.
If no, the registered arm's specificity-only limitation stands on the
record unrelieved, which is a defensible position and should then be
stated plainly in the paper rather than left implicit.
