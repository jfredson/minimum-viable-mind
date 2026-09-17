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
