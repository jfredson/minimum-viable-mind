# Control-battery diagnostic — result

*2026-09-17. Rule committed before running at `control-diagnostic-rule.md`
(`c3e9bc1`). Unregistered, post hoc, local, $0. Three checkpoints, 2,400
control queries each across three evaluation seeds, 200 permutations.*

## Verdict: it decides nothing, and that holds under both readings

**By the letter of my implementation: DEGENERATE on all three.** The
precondition fired because a null had zero spread.

**Under the narrowest defensible reading of the written rule: AMBIGUOUS
on all three.** Neither decision cell clears its null, and the dominant
cell is not off-structure.

I am reporting both rather than choosing, because choosing between two
readings *after* seeing the numbers is exactly the move this programme
forbids. It happens not to matter: the committed rule says an ambiguous
result "must not be reported as pointing anywhere," and a degenerate one
assigns no bin. **Both outcomes mean the October decision rests on the
evidence already in hand.**

## The third rule defect of the week, and this one is mine twice over

The degeneracy is not a property of the data. **It is a flaw in the null I
designed**, and it fires on every possible run.

The off-structure cell is *"the prediction matches none of the four
agents' values or successors."* That set is the union over **all** agents.
Permuting which agent the question named does not change a union over all
of them. So off-structure is **invariant by construction**, its null
spread is necessarily zero, and my guard trips every time regardless of
what any model does.

Confirmed exactly, not approximately: the cell's rate equals its null mean
to the last digit on all three checkpoints, 0.0883, 0.0808 and 0.0563.

That is the third defect found in criteria I wrote this week, after the
zero-spread null in the register probe and the absolute value in the
positive control. This one is worse than those two, because I wrote the
precondition specifically in response to the first, and then built a null
that violates it by construction.

**Nothing is repaired here and nothing is rerun.** A fix is proposed
below, for John.

## What the numbers show, which is not a verdict

The decision cells have healthy nulls, spreads of 0.0056 to 0.0077, so the
comparisons below mean something even though no bin turns on them.

| cell | pilot | seed 1 | seed 2 | reads as |
|---|---|---|---|---|
| correct | **+17.7 sd** | **+24.0 sd** | **+20.3 sd** | far above coincidence |
| untransformed | −2.8 sd | −3.3 sd | −2.4 sd | below |
| wrong agent, transformed | −13.9 sd | −16.4 sd | −16.1 sd | far below |
| wrong agent, raw | +0.6 sd | +0.7 sd | −0.9 sd | at coincidence |

**The models are binding by name, and substantially.** The correct cell
sits 18 to 24 standard deviations above what the same predictions would
score had a different agent been named. They are not guessing, and they
are avoiding wrong-agent bindings well below coincidence.

**So none of the three causes I enumerated is what happened.** Not absent
retrieval, not retrieval without the rule, not binding defeated by word
order. The models retrieve by name, apply the rule, and get it right about
three times in ten when coincidence gives one and a half.

I did not anticipate this pattern, and the rule I committed has no cell
for it. Per that rule, a result fitting none of the outcomes is reported
as fitting none. **This is that.**

## What it suggests about the ceiling defect, as description only

The registered ceiling for this battery is 0.3227, the score of a solver
that cannot read names. These models score 0.2921, 0.3104 and 0.3192.

So the picture is not a battery that failed to learn anything. It is a
battery that learned **real but partial** name binding, and landed at
roughly the level of a solver doing something else entirely. The two
numbers coincide without measuring the same thing, which is precisely why
the ceiling being wrong matters: it made a partially-working battery look
like a dead one.

This sharpens the registered ceiling defect rather than changing it. It
does not change any verdict, and the registered comparison stays
uncomputable on all three checkpoints.

## Proposed fix, not applied

Drop the off-structure cell from the degeneracy precondition, since its
invariance is structural rather than evidential, and check the spread only
on the cells a decision actually turns on. That is a one-line change and it
would make the guard test what it was written to test.

**It is proposed, not made.** Changing a rule after the data exposed it is
the thing I have now got wrong three times, and the correct move is to
hand it to John rather than to fix it and rerun. If he approves, the rerun
should also carry a cell for the pattern actually observed, decided before
it runs.

## What stands regardless

The control battery fails its floor on all three checkpoints, the
registered differential clause is uncomputable everywhere, and the
control's ceiling was registered as verified and never was. None of that
depends on this diagnostic, and none of it moved.

---

# Rerun, 2026-09-17, after John approved the fix and a fifth outcome

*Fix and new cell committed at `aa71845`, **before** this rerun. Same
checkpoints, same data, same classification.*

## Result: PARTIAL BINDING — MEASURE THE CEILING FIRST, on all three

**The fix changed only the guard, and nothing else.** Every cell rate and
every margin is **bit-identical** to the first run on all three
checkpoints. That is the verification that matters: the one-line change
touched the degeneracy check and did not disturb the measurement.

| checkpoint | verdict |
|---|---|
| pilot (seed 0) | partial binding — measure the ceiling first |
| seed 1 | partial binding — measure the ceiling first |
| seed 2 | partial binding — measure the ceiling first |

## This is not independent confirmation, and should not be read as any

I predicted this outcome before the rerun, and that is not to my credit.
**The fifth cell was written to describe a pattern I had already seen in
the first run.** Of course it fires. A cell fitted to observed data and
then found to match that data has confirmed nothing.

What the rerun establishes is narrower and worth having: the pattern is
consistent across all three checkpoints, and the fixed guard now lets a
verdict through instead of tripping unconditionally. The module carries
the lower weight in its own output on every checkpoint, so the caveat
travels with the number rather than living only here.

## What it says, at the weight it deserves

The models bind by name substantially — 18 to 24 standard deviations above
what the same answers would score had a different agent been named — and
they avoid wrong-agent bindings far below coincidence. So the control
battery is **partially learned**, not dead.

Its registered ceiling is the score of a solver that **cannot read
names**. The models land at roughly that level while doing something the
comparator does not do at all. Two numbers coinciding without measuring
the same thing is how a partially-working battery came to look like a
failed one.

## The indicated next step, which is free and not yet run

**Measure the control battery's ceiling properly.** John has already made
this a precondition of any Amendment A4. The diagnostic now points at it
independently.

It is local and costs nothing, but it needs its own method fixed in
advance, because "the ceiling" is exactly what turned out to be
ill-defined. At minimum that means deciding, before running anything, what
solver defines it: a name-keyed lookup solver, an adversarial sweep of the
kind the primary battery got and this one never did, or both reported
separately. **That method should be written and reviewed before it runs**,
on the same discipline as everything else this week.

**Not run. Awaiting John.**

## What still has not moved

The control fails its floor on all three checkpoints. The registered
differential clause is uncomputable everywhere. The ceiling was registered
as verified and never was. None of that depends on this diagnostic, and
none of it changed.
