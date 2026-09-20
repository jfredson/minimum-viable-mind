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


===== FILE: experiments/06-mvm-0a-constructed-self-index/register-direct-probe-findings.md =====

# Unblinded direct register probe — result

*2026-09-16. Local, $0, inference only. Ruled by John after the blind
arm's verdict was committed. Criteria committed before the run at
`8884b31`. Unregistered and labelled so. This is a follow-up diagnostic,
not a registered arm.*

## The headline

**The register never encoded own-agent identity, at any turn.** Not at
the end, where it is a constant vector identical across every episode,
and not in the early turns, where it does vary across episodes but
carries nothing about which agent the model is.

So the blind arm's sub-bin name is wrong. **"Instrument failure to locate"
presumed there was something to locate. There was not.**

> **ANNOTATION, 2026-09-16 (John's ruling).** The name is **not retired**;
> the sentence above is left as written. What is wrong is the
> interpretation the name invites, not the bin the result fell into under
> the criteria in force. The committed verdict carries a dated annotation
> beside it reading *superseded in interpretation by the unblinded
> register probe: no valid target.* Reasoning at the end of this note.

## First, a defect in my own pre-stated rule

The pre-stated rule was `accuracy >= null_mean + 3 * null_sd`. Applied to
the primary probe it returns **reading 1, sensitivity failure**. That is
an artifact and I am reporting it rather than quietly repairing it.

| quantity | value |
|---|---|
| probe accuracy | 0.2700 |
| null mean | 0.2700 |
| null standard deviation | 0.0000 |
| margin | undefined |
| majority-class rate | 0.2700 |

The inequality reads `0.27 >= 0.27 + 0`, which is true. The separation is
**zero** standard deviations, not three. Three independent signs say the
input was degenerate:

1. The permutation null has zero spread. Every permutation scored
   identically, so the rule compared a number to itself.
2. The margin in standard deviations is undefined, a division by zero.
3. The accuracy equals the majority-class rate **exactly**. That is the
   score of a classifier that ignores its input and predicts one constant
   class, which is all it can do when every episode hands it the same
   vector.

I did not change the rule's output. A degeneracy guard was added to the
module afterwards, reporting the literal result unchanged alongside the
three signs, and it assigns no bin. The guard is a validity check on the
rule's **input**, in the same category as the Gate 0 escalation check. It
is not a new bin, and the self-test now covers the degenerate case.

**Formally this result fits none of the pre-stated readings as written**,
because reading 1's inequality is satisfied but void. John rules on how
to record it. My reading of the evidence is below, and it is reading 2.

Stated plainly because it cuts against me: the pre-stated criteria were
written by me and this is a hole in them. A rule of this shape needs a
non-degenerate null as a precondition, and mine did not say so.

## The evidence, which is not ambiguous

**The register is constant across episodes at the point the primary probe
read it.** Across-episode standard deviation averages 1.68 × 10⁻⁷, with a
maximum of 8.34 × 10⁻⁷. That is float32 rounding. The 107 nominally
distinct rows out of 400 differ only at that level.

It is not untouched, though. It moves from its initialization by 0.327 on
average and 1.29 at most. **The register is saturated, not idle.** It
holds a fixed vector that is the same whoever the model is and whatever
happened in the episode.

**The one probe with a valid null also sits at chance.** The
trunk-visible projection, which the model actually reads through
cross-attention, does vary across episodes because the marker keys differ.
Its null is healthy.

| probe | accuracy | null mean | null sd | margin |
|---|---|---|---|---|
| trunk-visible projection | 0.2375 | 0.2369 | 0.0234 | 0.03 sd |

Against a bar of three standard deviations, that is 0.03.

## Was identity there earlier and destroyed?

This mattered enough to check, because "empty" is ambiguous between a
register that never held identity and one that held it and lost it. The
two have different consequences for the design.

The register is not constant at every turn. Within a forward pass it
varies across episodes for the first three writes and collapses
thereafter. Probing every turn of the graded pass, same imported probe and
null:

| turn | across-episode sd | accuracy | margin |
|---|---|---|---|
| 0 | 1.41 × 10⁻¹ | 0.3050 | 1.82 sd |
| 1 | 1.63 × 10⁻¹ | 0.2600 | 0.17 sd |
| 2 | 1.41 × 10⁻¹ | 0.2500 | −0.11 sd |
| 3 to 7 | ~1.68 × 10⁻⁷ | degenerate, constant across episodes | — |

The pre-collapse turns have real variation and healthy nulls, and their
margins are 1.82, 0.17 and −0.11 standard deviations. All are under the
bar. **The register never encoded own-agent identity.** It carried
episode-specific content early and that content was about something else.

> **ANNOTATION, 2026-09-16, later the same day. The last sentence above
> is WRONG and is withdrawn.** It stays in place rather than being
> deleted, so the correction is visible.
>
> The register carried no episode-specific content early either. I had
> read the *flattened* register, which mixes what was written with which
> of the four agent rows it went into, and which row is written varies by
> episode because agents speak in different orders. The apparent variation
> at turns 0 to 2 was variation in **which rows had been filled yet**, not
> in their contents.
>
> Isolating the row just written shows across-episode spread at the
> floating-point floor from **turn 0** in all three 30M full checkpoints.
> The writer emits one constant vector whatever it is given, from its
> first write. So the conclusion in bold above is not merely right, it is
> stronger than the evidence I gave for it: the register was never
> carrying episode-specific information of any kind, rather than carrying
> something that turned out not to be identity.
>
> Measured in `register-saturation-findings.md`.

This diagnostic was added after seeing the primary result and carries no
pre-stated bin. It is reported as description.

The 1.82 at turn 0 is the largest margin anywhere in this work and still
falls short. It should not be read as a near-miss: it is one of three
valid tests here, and more were run across the blind arm's five layers, so
the multiple-comparison correction pushes it further down. Nothing turns
on it.

## Where the collapse happens

Inside the writer. The writer's input, the attention-pooled top-layer
states, varies enormously across episodes at **every** turn, with
per-feature standard deviations around 30 to 40 and maxima from 145 to
355. So episode-specific content reaches the writer and does not come out.

The mechanism is consistent with gate saturation in the recurrent update
given inputs of that magnitude, which would drive the hidden state to a
fixed point regardless of input. **That is an inference from the
magnitudes, not a measurement**, and it is labelled as one. What is
measured is that the input varies and the output does not.

## What this does to the blind arm's record

**The blind arm result says nothing about the localization stack's
sensitivity, in either direction.** Not because the evidence is weak, but
because the arm had no target. A search for a structure that is not there
cannot demonstrate either that the instrument finds things or that it
misses them.

This sharpens both of John's corrections rather than softening them:

- On specificity, the corrected record already said no false positive was
  produced by an instrument that produced no positive of any kind. That
  now reads as generous. The instrument was pointed at a checkpoint whose
  designated self-structure was constant.
- On Experiment 1, the record already said this result is not evidence
  that Experiment 1's null was instrument blindness. That stands, and the
  ground under it is firmer: nothing here is evidence about instrument
  blindness at all.

The sub-bin name **"instrument failure to locate" should be retired** for
this arm, and the honest description is **no valid target**. That is a
change to how the blind result is described and John should rule on it,
since the sub-bin was part of the pre-stated criteria.

> **RULED 2026-09-16: NOT RETIRED.** The recommendation above is left
> standing rather than deleted, so the record shows both what was proposed
> and what was decided. John: "The committed verdict and its pre-stated
> name stand as written. Add a dated annotation beside it ... Annotate,
> never rewrite."
>
> His ruling is the better discipline and the reason is worth stating. A
> pre-stated name records which bin a result fell into under the criteria
> in force when it ran. Renaming it afterwards, even for a good reason,
> makes those criteria unfalsifiable in retrospect, because a later reader
> cannot tell which names were committed and which were fitted to the
> result. Annotation keeps both the commitment and the correction visible.
>
> The superseding interpretation is recorded as a dated annotation beside
> the verdict in `blind-arm-findings.md` and in `STATUS.md`: *superseded
> in interpretation by the unblinded register probe: no valid target.*

## What it says about the A2 architecture

This is a finding about the build, not only about the instruments. The
register was constructed to hold per-agent state. In the trained 30M
checkpoint it holds a constant after three turns and never encoded agent
identity at any point.

It also explains the earlier register lesion result rather than merely
agreeing with it. Removing the register injection entirely changed
nothing, and deranging which register is read moved logits by a mean
absolute 0.014. Of course it did. A constant injection is a bias term, and
permuting which constant you read changes nothing because they have
converged to the same place.

## What this changes downstream

The companion positive control, which John ruled yes on, is now **the only
remaining route to any sensitivity reading** on the localization stack.
Before this probe it was the better of two routes. It is now the only one.

The control-battery proposal due 2026-10-04 should carry this: whatever
else Amendment A4 decides, a register that saturates to a constant after
three turns is a design defect, and any future architecture claiming to
carry a self-index needs a check that the carrier still varies at the
point where it is read.


===== FILE: experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md =====

# The control battery's ceiling is 1.0, and the clause was never computable

*2026-09-17. Method committed before running at
`ceiling-measurement-method.md` (`2fba2ea`). No checkpoint loaded, no
inference, no spend. 4,000 episodes.*

## Verdict: A — STRUCTURALLY UNSATISFIABLE

**The registered differential clause could never have been computed. Not
by these models, not by any model, at any training budget, on any
architecture. It has been dead since registration.**

## The harness proved itself first

Both known-answer checks reproduced their registered values **exactly**,
to four decimal places, before any new number was reported:

| check | measured | registered |
|---|---|---|
| control, name-blind reference | 0.3227 | 0.3227 |
| primary battery reference | 0.2921 | 0.2921 |

So the harness reproduces the registration's own arithmetic. What follows
is not a different calculation quietly substituted.

## The measurement

| solver | score |
|---|---|
| name-keyed lookup | **1.0000** |
| registered name-blind reference | 0.3227 |
| learned attack | **1.0000** |
| **best of family** | **1.0000** |

Two independent solvers reach a perfect score. The hand-written one reads
the marker in the question, finds that marker's turn for the queried item,
and applies the shared revision rule. The learned one was given only
ownership-blind features and found the same structure by itself.

Neither touches the model's own slot or the acting channel. A scan of the
code, with docstrings and comments stripped, enforces that.

## Why this kills the clause

The floor rule defines a battery's drop only when
`baseline − ceiling ≥ 0.10`.

With a ceiling of 1.0, a defined drop needs a baseline of **1.10**.
Accuracy cannot exceed 1.0. So the control battery's drop is undefined for
**every possible model**, including a hypothetical one scoring a perfect
1.0, which would give a denominator of exactly zero.

The registered signature requires the primary battery's drop **minus the
control's**. One of its two terms can never exist.

## The reason is not what we thought, and the correction matters

Until today the record said A3 could not return a positive **because the
control battery never learned**. That conclusion was right and the reason
was wrong.

The control's failure to learn is **beside the point**. A perfectly
learning control would have made no difference whatever. The clause was
unsatisfiable the day it was registered, months before any checkpoint
existed.

**This also moots the proposal I wrote this morning.** Both routes I
offered, extra supervision and a scaffolded intermediate question, aimed
at making the control learn. Neither would have fixed anything. I was
proposing to spend $27 to $39 on a repair to the wrong component, and I
would have recommended it had this measurement not been run first. John's
instruction to measure the ceiling before opening an amendment is what
caught it.

## The structural point, which generalises past A3

This is not a slip in one number. It follows from two registered choices
that are individually reasonable and jointly incoherent.

1. The control battery is **designed to be answerable without ownership**.
   That is its entire purpose: same binding demand, no self-reference.
2. The metric divides by the distance from baseline to the **best score an
   ownership-blind solver reaches**.

Any control that is fully determined by the visible episode and does not
require ownership has an ownership-blind ceiling of 1.0 by construction.
Divide by the distance to 1.0 and you divide by zero or less.

**So the ceiling-corrected metric and the concept of an ownership-free
control are incompatible by construction**, not by accident. Any future
design pairing them inherits this, which is why it is worth reporting
upstream rather than filing as an A3 defect.

Worth stating fairly: the ceiling denominator was itself a registered
revision, adopted because dividing by chance manufactured a spurious
differential of 0.035 between the two batteries. That was a real problem
and the fix was a real fix. It simply traded a small artifact for an
unsatisfiable clause, and nobody noticed because the control never got
close enough to its floor for anyone to check the arithmetic.

## What this does not change

**The primary result is untouched.** Its ceiling is 0.2921, the models
score about 0.57, so its drop is well defined and enormous, between 7.5
and 8.6 times the locked threshold. Nothing here bears on it.

**No verdict is reopened.** Every finding that said the comparison was
uncomputable remains correct. Only the explanation changes.

**The other batteries are fine.** The state battery's ceiling is 0.0676
against a baseline of 1.0. The problem is specific to a control designed
to be ownership-free.

## What it means for 4 October

The question is no longer whether to make the control learn. **It is
whether the clause can be repaired at all, and if so whether repairing it
is a metric change rather than a training change.**

That is a different decision from the one the proposal framed, and it
