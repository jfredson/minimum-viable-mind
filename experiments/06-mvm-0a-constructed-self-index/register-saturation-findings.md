# The register is constant in every trained checkpoint

*2026-09-16. Local, $0, inference only. Ruled by John. Descriptive
survey, no bin and no threshold a verdict turns on. Raw per-turn numbers
in `a3-gates/register_saturation_survey.json`.*

## What was asked and what was found

John ruled: *"Check whether the register is constant in the other
register-bearing checkpoints (pilot seed 0 full, s1 full, s2 full), and at
any saved intermediate steps, to see when it saturated. Report per
checkpoint."*

**It is constant in all of them.** Every trained register-bearing
checkpoint collapses at the same turn, and the writer emits the same
vector whatever it is given, from its very first write.

| checkpoint | step | collapse turn | written-row spread across episodes |
|---|---|---|---|
| pilot seed-0 full | 102095 | 3 | 7.6 × 10⁻⁸ |
| pilot seed-1 full | 102095 | 3 | 2.8 × 10⁻⁸ |
| pilot seed-2 full | 102095 | 3 | 5.9 × 10⁻⁸ |
| 10M pilot | 22369 | 3 | at floor |
| **untrained, same config** | **0** | **never** | **3.3 × 10⁻¹** |

The two twins are register-less by construction and have no register to
measure. They are listed and skipped rather than silently absent. One
older 10M checkpoint predates the current module and will not load
strictly; it was skipped rather than loaded loosely, because loading it
loosely would have measured randomly initialized weights and reported them
as that checkpoint's.

## A correction to what I wrote earlier today

The direct probe findings say the register "carried episode-specific
content early and that content was about something else". **That is
wrong and is withdrawn here.** The original sentence stays in place in
that note with an annotation pointing to this one.

The mistake was reading the flattened register. It mixes two things: what
was written, and which of the four agent rows it went into. Which row is
written varies by episode, because agents speak in different orders. So
the apparent variation at turns 0 to 2 was variation in **which rows had
been filled yet**, not in their contents.

Isolating the written row shows the truth. Across-episode spread of the
row just written sits at the floating-point floor from **turn 0**, in all
three 30M checkpoints. By turn 3 all four rows have been filled in every
episode, so even the fill-pattern difference disappears and the flattened
register goes constant too.

**The register never carried episode-specific information at any point.**
Not degraded, not lost after a few turns. Constant from the first write.

## When it saturated

No intermediate-step weights were saved by any of these runs, so the
training-time onset cannot be read off disk. That is a real limit and no
amount of care recovers it from what exists.

It can be bounded from the other end, and that bound is informative. An
untrained model at the same configuration does **not** collapse: its
written values vary across episodes with a spread of 0.33 rising to 0.54,
and all 200 episodes give distinct register states at every turn from turn
2 on. So the constancy is **trained in, not architectural**. The
architecture can carry episode-specific state. Training drove it to stop.

What is measured precisely is the within-episode onset: turn 3 in every
trained checkpoint, which is simply the turn by which all four rows have
been overwritten with the constant.

## What it looks like mechanically

The register moves away from its initialization in equal steps and then
freezes exactly. On seed 0 the mean distance from initialization goes
0.0817, 0.1633, 0.2450, 0.3267 and then stays at 0.3267 for every
remaining turn. Those are one, two, three and four quarters of the same
number, which is what you see when each turn overwrites one of four rows
with the same target vector and nothing changes after the fourth.

The writer's input varies enormously the whole time, with per-feature
spreads around 30 to 40 and maxima from 145 to 355. Episode-specific
content reaches the writer at every turn and does not come out. The
mechanism is consistent with gate saturation in the recurrent update at
those input magnitudes. **That remains an inference from the magnitudes,
not a measurement.** What is measured is that the input varies and the
output does not.

## The consequence John named

If the register contributes a constant, the trunk reads a constant through
cross-attention, and a constant input is a bias term. **The full model is
the twin plus a learned bias.** The manipulation the A2 design turned on,
having a per-agent register versus not having one, was never applied in
any effective sense.

The binding results line up with that exactly. Two of five checkpoints
bind, and they are one full and one twin:

| checkpoint | architecture | bound? |
|---|---|---|
| pilot seed-0 full | full | **yes** |
| seed-1 twin | twin | **yes** |
| seed-1 full | full | no |
| seed-0 twin | twin | no |
| seed-2 full | full | no |

Binding does not track architecture. It tracks seed. That is what a
lottery in a single architecture looks like, and it is what the wave-2
"prediction inverted" result was reading.

**So the wave-2 result should not be read as a prediction inverting.** A
prediction about register-bearing versus register-less models cannot
invert, or hold, on a comparison where both arms are the same model up to
a bias term. The honest description is two of five seeds binding in one
architecture.

This is recorded as an annotation on the wave-2 ledger row and findings
note. Per John's standing instruction those are **annotated, never
edited**: the original text and the original reading stay exactly as
written, with a dated note beside them.

## What this does not say

It does not say the A2 runs were wasted or that the binding measurements
were wrong. The batteries measured what they measured, and two checkpoints
really do bind. What is withdrawn is only the architectural
**interpretation** laid on top of that comparison.

It also says nothing about A3. A3 is register-less by construction and its
authorship signal is the acting channel, which is measured load-bearing on
the pilot at 0.506 against 0.182. Nothing here touches that.
