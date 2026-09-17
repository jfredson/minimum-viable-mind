# Measuring the control battery's ceiling — method, before running

*2026-09-17. **Written and committed BEFORE anything runs**, as with the
diagnostic. Local, $0, no model inference, no network. **Not run.
Awaiting John.***

John made this a precondition of any Amendment A4. The diagnostic now
points at it independently.

## What is being measured

The **ownership-blind ceiling** of the control battery: the best score
reachable by a solver that cannot tell which agent it is.

The registered figure is **0.3227**. The registered text says it was
verified by the attack sweep. It was not: the sweep contains no
control-battery code and attacks the primary battery only. The figure
rests on one reference solver which never reads the marker the control
question names.

## The definition, quoted from the sweep itself

The attack sweep states the rule every ownership-blind attack obeys:

> **The rule every attack here obeys:** it may use the full rendered
> episode, every structural fact about it, and the shared revision rule.
> It may NOT use `own_slot`, the acting channel, or anything derived from
> them.

**This is the crux and it should be settled before any number appears.**
Under that rule, a solver answering the control question **may read the
marker in the query and the markers in the turns**. Neither is `own_slot`
and neither derives from it. The control question names the agent it asks
about, so knowing which agent you are is irrelevant to answering it.

If that reading is right, an ownership-blind solver can answer the control
question every time, and its ceiling is near 1.0 rather than 0.3227.
**The measurement is the test of that reading, not an assumption of it.**

## Two known-answer checks, run first

The harness must reproduce numbers already on the record before it is
allowed to produce a new one. Same discipline as the endpoint module,
which was validated against the pilot before it touched the seeds.

1. **Name-blind mode must reproduce 0.3227** on the control battery,
   matching the registered reference solver.
2. **The same harness must reproduce 0.2921** on the primary battery,
   matching its registered ceiling.

**If either check fails, no outcome is assigned and the run reports
HARNESS UNVERIFIED.** A ceiling measured by a harness that cannot
reproduce known values is not evidence.

## The solvers

All are programmatic, read only the rendered episode and the shared
revision rule, and never touch `own_slot` or the acting channel.

**S1, name-keyed lookup.** Read the marker in the query. Find that
marker's turn for the queried item. Take its value. Apply the revision
rule. This is the solver the sweep's rule permits and the registered
reference solver omits.

**S2, the registered reference solver.** The existing name-blind
enumeration, reported unchanged, as the comparison and as check 1.

**S3, a learned attack**, mirroring the sweep's second kind. Fit a
classifier on ownership-blind features of the episode to predict the
answer, and score its top pick. This is the stronger test because it finds
structure a hand-written rule might miss.

**S4, best-of-family.** The maximum over S1 to S3, because an adversary
picks the best attack available. This is the reported ceiling.

## Pre-stated outcomes

Let `C` be the best-of-family score. The floor rule requires
`baseline − ceiling ≥ 0.10` for a battery's drop to be defined.

**A. STRUCTURALLY UNSATISFIABLE.** `C > 0.90`.

> Then a defined drop needs a baseline above 1.0, which no model can
> reach. **The registered differential clause was never computable, for
> any model, at any training budget, on any architecture.** It has been
> unsatisfiable since registration. The control battery's failure to learn
> would then be beside the point: the clause was dead before the first
> checkpoint existed. This is the outcome that reframes the October
> decision entirely, and it is upstream-reportable.

**B. REGISTERED NUMBER WRONG, CLAUSE STILL REACHABLE.**
`0.3727 < C ≤ 0.90`.

> The registered 0.3227 is wrong by more than the stated band, but a model
> could in principle clear `C + 0.10`. Report the measured ceiling and the
> accuracy a model would need. An A4 would then have a target to aim at.

**C. REGISTERED NUMBER SURVIVES.** `C ≤ 0.3727`.

> The number stands despite never having been verified, the permissive
> reading of the sweep's rule is wrong, and the control's failure is an
> ordinary learning failure. The October decision proceeds on the evidence
> already in hand.

**D. NOT MEASURABLE.** A known-answer check fails, or the solvers
disagree in a way the method cannot adjudicate.

The 0.05 band around the registered figure, giving the 0.3727 boundary, is
a **stated convention and mine**, not inherited. Raw scores for every
solver are reported so another band can be applied.

## What this cannot do

**It does not re-open any verdict.** The control fails its floor under
every candidate ceiling, since every candidate is at or above 0.3227 and
the models score 0.29 to 0.32. No result here rescues the comparison on
these checkpoints.

**It does not decide A4.** It measures one quantity that the decision
needs. Outcome A would argue against an amendment built on this clause;
outcome C would leave the decision exactly where it is.

**It is not a model measurement.** No checkpoint is loaded and no
inference runs. It measures what the *grammar* permits, which is what a
ceiling is.

**It is unregistered.** The original ceiling is registered; this
measurement of it is not, and any write-up must say so.

## Cost and status

Generating episodes and fitting a small classifier. **No model, no pod, no
spend, no network.**

**Status: not run.** Method committed first, as instructed.
