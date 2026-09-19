# Position sweep — method, committed before the run

*2026-09-19. **UNREGISTERED**, diagnostic only. No verdict is read and no
cell here feeds one. Local, inference only, no training, no network, $0
[C1/C2]. Reads no registered verdict and touches no registered text.
Fresh output file per checkpoint, nothing overwritten [C6].*

*Committed before the sweep produces any output, under the same rule as
`denoised-direction-method.md`: the cells and the positions are fixed
while nobody knows which one will fire. If the numbers turn out to want a
different rule, that is a finding for a later run, not an edit to this
file.*

## Why

The denoise-before-probing diagnostic came back empty on all three
checkpoints (`denoised-direction-findings.md`): zero of fifteen tests
cleared, and about ten directions out of 448 carry ninety-nine per cent
of everything that varies at the probed position once ownership is taken
out. That result makes the **probe position** suspect, not only the
probe. Ownership is still measured to be load-bearing on the pilot —
zeroing the acting channel takes the ownership battery from 0.506 to
0.182 — so something carries it, and two different linear reads at one
position have now failed to find it.

Two questions follow, and this sweep asks both.

**Arm 1. Have we been looking in the wrong place?** Read own-agent
identity with the difference-of-averages read at every candidate position
in the episode, not only the one the registered pipeline probes.

**Arm 2. Have we been looking with the wrong instrument?** At the
original five layers and the original position, put the regularised
classifier and the difference-of-averages read head to head on identical
states and identical splits. The 2026-09-16 probes all sat *below* their
nulls, which is systematic; last night's difference-of-averages read of
the same states sat *above* its null on all five pilot layers. That
contrast was noticed in passing and its null spread was never recorded,
so it could not be quantified. This arm quantifies it.

**Nothing here is a verdict and nothing here reopens one.** Both arms are
descriptive. No result changes the 2026-09-16 not-testable reading, the
signed sensitivity rule, or any registered clause.

## What is common to both arms

Unchanged from the blind-arm positive control and the denoising
diagnostic, so every comparison is like for like:

- **Checkpoints.** The three A3 30-million-parameter checkpoints in hand,
  verified by checksum: the pilot `a3_30m_seed0.pt` (`f751228c…`), seed 1
  `a3_30m_seed1.pt` (`eeed93b8…`), seed 2 `a3_30m_seed2.pt`
  (`f1f131cb…`).
- **Episodes.** 200 paired episodes from `localize_a3.paired_episodes` at
  content seed 20260917, giving 400 episodes. Pairs share a content seed
  with the owning agent rotated, which is what makes a read attributable
  to ownership rather than to content.
- **Layers.** 3, 4, 5, 7 and 8, at every position.
- **Null.** The same construction throughout: 200 draws, each shuffling
  the own-agent labels and redoing the entire procedure, four-fold
  cross-validation, everything fitted on the training folds only.
- **Bar.** Clearance by three standard deviations of the null. Not moved.
- **Four owning agents**, so a classifier that always guesses scores
  0.25, and a separation score for one agent against the rest has 0.5 as
  its no-information value.

### Two things that will be reported and were not before

**The permutation count, beside the standard-deviation margin.** With 200
draws the finest resolution available is one draw in two hundred. A
margin quoted as "four standard deviations" assumes the null is roughly
bell-shaped further out than 200 draws can show. So every test also
reports **how many of the 200 shuffled draws met or beat the real
score**. Where the two disagree, the count is the more honest number and
the findings will say so. This applies to the earlier diagnostic too,
whose margins carry the same caveat and never stated it.

**A family-adjusted bar.** Arm 1 is 11 positions × 5 layers × 3
checkpoints = **165 tests**. At a three-standard-deviation bar, the
chance that at least one clears on its own is roughly twenty per cent —
high enough that a single clearance proves nothing. The per-test bar
stays at three standard deviations so the comparison with the earlier
probes is like for like, and every clearance is additionally labelled:

- **ROBUST** — also clears **3.43 standard deviations**, the bar at which
  165 independent tests give a five per cent chance of one false
  clearance, and beaten by every one of the 200 shuffled draws.
- **MARGINAL** — clears three standard deviations but not that.

A MARGINAL clearance standing alone is reported as what it is: consistent
with chance across a family this size.

## Arm 1 — the position sweep

### The read

The plain difference-of-averages read, with no denoising step. Last
night's run established that projecting out the loud directions moved
nothing at the anchor position, in either direction, so the plain read is
the right primary here. Denoising a position that does separate is a
follow-up with its own method file, not a flag on this one.

For each owning agent, its average state minus the average of the other
three, fitted on the training folds and scaled to unit length. Held-out
states are projected onto the four directions.

- **Headline: the separation score.** For each agent, the chance that one
  of its episodes projects higher than an episode of another agent — the
  area under the receiver operating characteristic curve — averaged over
  the four agents. No information is 0.5.
- **Beside it: nearest-average accuracy.** Assigning each held-out
  episode to whichever agent's average it lands nearest. No information
  is 0.25. This is the statistic arm 2 compares against the classifier,
  so it is on the same scale as the 2026-09-16 probe table.

Both carry their own 200-draw null, both nulls' spreads are recorded this
time, and the cells turn on the separation score.

### The positions

Every turn renders as `assign {item} to {value} by {marker}`, six words
then a line break, so within a turn beginning at position *s*: *s* is
`assign`, *s+1* the item, *s+2* `to`, *s+3* the value, *s+4* `by`, *s+5*
the agent's marker, *s+6* the line break. **The marker comes after the
value**, by design, so at the moment a value is emitted the turn has not
yet said whose turn it is.

Every episode in this set has exactly three turns by the model — two
assignments and one revision — exactly one other agent that revises, and
the model's revision falling in the ninth or tenth turn, evenly split.
All four facts were checked before the positions were chosen.

Nine positions come from the episode as the registered pipeline encodes
it. Two more need a question appended, and the model is causal — a
token's state cannot depend on tokens after it — so appending a question
cannot disturb the other nine.

| # | name | where | why it is here |
|---|---|---|---|
| 1 | `own_assign_1_value` | the value in the model's first assignment | acting channel injects here |
| 2 | `own_assign_2_value` | the value in the model's second assignment | acting channel injects here |
| 3 | `own_revision_decision` | one before the model's revision value | **the registered position — the anchor** |
| 4 | `own_revision_value` | the model's revision value | acting channel injects here |
| 5 | `own_revision_by` | one after the revision value | immediately after the revision |
| 6 | `own_revision_marker` | two after, the model's own marker | **the positive control** |
| 7 | `before_own_revision_turn` | the line break ending the previous turn | before the revision turn begins |
| 8 | `other_revision_decision` | one before the other reviser's value | the matched other-agent position |
| 9 | `other_revision_value` | the other reviser's value | the other agent's acting position |
| 10 | `query_answer_decision` | the answer marker of an appended question | where the model is about to answer |
| 11 | `query_answer_value` | the answer token itself | where the answer sits |

Positions 1, 2 and 4 are **the three positions where the acting channel
injects**: the channel is a projection of the model's own preceding state
added at the value token of each of its own turns.

**The positive control, position 6, and what the sweep costs if it
fails.** At the model's own marker token, which agent the model is has
just been read off the input. It should be decodable almost perfectly. If
position 6 does *not* separate, the read is broken and **no other result
in arm 1 means anything** — the sweep is reported as having failed to run
rather than as having answered. Stating this in advance is the point:
without it, a sweep of eleven positions that finds nothing anywhere is
indistinguishable from a sweep that was never working.

**What a pass at positions 1, 2 or 4 would and would not mean.** These
are the positions the acting channel injects into, and the channel is
built from the model's own state. Identity being decodable there is close
to reading back the injection, and it is *not* evidence of a carried
self-index. The registered pipeline probes position 3 precisely because
the injection has not reached it. A clearance at 1, 2 or 4 alongside
nothing at 3 is the uninteresting outcome and the cells say so.

### The appended question

The other-agent battery question, which every episode carries first —
checked, the order is the same in all 400. It is the battery the
differential clause turns on and the one whose failure to learn is the
open question, which is why it is the one appended.

**Confidence: moderate, a judgment call rather than a standard one.** The
strongest alternative is the ownership-free state battery, which every
episode also carries and which did learn. I chose the other-agent
question because a position is only interesting here if ownership could
plausibly matter there, and the other-agent question is the one that
mentions another agent at all. If a later session wants the state
battery's answer position, that is another position with its own method
file, not a knob on this one.

### Cells for arm 1, fixed here

Read across all three checkpoints. Exhaustive and disjoint.

**SWEEP INVALID.** The positive control at position 6 fails to clear on a
checkpoint. No cell is assigned for that checkpoint and its other
positions are reported without interpretation.

**NOTHING SEPARATES ANYWHERE.** The positive control clears, and no other
position clears on any checkpoint.

> Reading: own-agent identity is not linearly decodable anywhere in the
> episode by this read, on any checkpoint in hand, despite being decodable
> where it is written in the input. The wrong-position explanation for the
> earlier nulls is not supported.

**SEPARATES ONLY WHERE THE CHANNEL INJECTS.** Beyond the positive
control, the only clearances are at positions 1, 2 or 4.

> Reading: what is decodable is the acting channel being read back, not a
> carried self-index. The registered position remains the right place to
> look and it remains empty.

**SEPARATES AWAY FROM THE INJECTION.** At least one clearance at position
3, 5, 6-excluded, 7, 8, 9, 10 or 11 — that is, anywhere other than the
injection positions and the positive control.

> Reading: ownership is legible somewhere the channel does not put it.
> This is the outcome that would say the registered probe position is the
> problem. It names a candidate position for a follow-up experiment; it
> does not license reinterpreting any registered result, and the
> follow-up would need its own registration.

Every clearance is labelled ROBUST or MARGINAL, and a cell reached only
by MARGINAL clearances says so in its own name.

## Arm 2 — classifier against difference of averages

### What is compared

At **the original five layers and the original position** (position 3,
the anchor), on **identical captured states** and **one shared set of
folds**:

- **The regularised classifier**, `localize_a3.fit_probe` — logistic
  regression, held-out accuracy, its 200-draw label-permutation null.
- **The difference-of-averages read**, scored by nearest-average accuracy
  so the two are the same statistic on the same scale, with its own
  200-draw null built the same way.

Both get the **same explicit fold assignment**, which is the part that
makes this a head-to-head rather than two separate runs compared after
the fact.

**This is not a reproduction of the 2026-09-16 probe table.** That table
used the classifier's own default splitting, which balances the classes
across folds; this arm hands both instruments one shared split so the
comparison is clean. The 2026-09-16 numbers are reported alongside for
context and any difference between them and this arm's classifier column
is attributable to the split, which the findings will state rather than
leave for a reader to discover.

### The pre-stated question

*Does the classifier sit below its null where the difference-of-averages
read sits above it, and by how much?*

Per layer and checkpoint, both margins are recorded in standard
deviations of each instrument's own null, with permutation counts beside
them, and the **gap** is their difference.

### Cells for arm 2, fixed here

Read per layer, then counted across all fifteen layer-and-checkpoint
combinations.

**CLASSIFIER PENALISED.** The classifier's margin is below zero and the
difference-of-averages margin is above zero.

> Reading: on these states the classifier scores worse than the same
> classifier trained on shuffled labels, while a difference of averages
> scores better than its own shuffled baseline. The below-null pattern is
> a property of fitting a regularised classifier to this data, not of the
> states.

**BOTH BELOW.** Both margins below zero. The below-null pattern is a
property of the states, not the instrument.

**BOTH ABOVE.** Both margins above zero.

**REVERSED.** The classifier above zero and the difference of averages
below it.

The headline for arm 2 is the count of the fifteen in each cell and the
median gap in the CLASSIFIER PENALISED cell. **Neither instrument is
expected to clear three standard deviations at this position** — the
whole point is that both fail there — so arm 2's cells are about the
*sign* of each margin, not about clearance. Any clearance that does occur
is reported and labelled, and would be a finding in its own right.

## What this sweep cannot do

It cannot show that a self-structure exists or does not. It reads one
statistic, linearly, at eleven positions, five layers, 400 episodes,
three checkpoints, on 30-million-parameter models trained on a synthetic
grammar. A null everywhere is consistent with ownership being carried
non-linearly, or distributed, or at a position not on the list. A
clearance away from the injection positions would name a place to look
next and nothing more.

It also cannot settle red-team objection R1. Even a clean separation at
the anchor position would not establish that what separates is a carried
self-index rather than the acting channel's input trace passed forward.

## Cost and where the output goes

Inference on three 30-million-parameter checkpoints on a laptop, then
linear algebra and repeated small fits on matrices of a few hundred rows.
Minutes, no spend, no network.

One fresh file per checkpoint under `a3-gates/`, named
`position_sweep_a3_<checkpoint>.json`, plus a summary file and
`position-sweep-findings.md`. Nothing existing is overwritten.

Implementation: `src/position_sweep_a3.py`, committed together with this
file and before either produced any output. Gated on the known-answer
test, and deliberately not on the threshold lock, for the same reason
given in `denoised-direction-method.md`: nothing here ablates anything or
is scored against the bite threshold.
