# The other agent's index at the same positions — findings

*2026-09-20 (Pacific). **UNREGISTERED** as a verdict-bearing run,
diagnostic only. No verdict is read and no cell here feeds one. Local,
inference only, no training, no network, $0 [C1/C2]. Method committed in
`other-index-position-sweep-method.md` at commit `7745d4a`, together with
`src/other_index_position_sweep_a3.py`, **before either produced any
output**. The cells, the bar, the exclusion rule and the prediction below
were fixed while nobody knew which would fire.*

*Runs the first of the two follow-up runs ruled on 2026-09-20. It answers
the red-team ledger's item on the confound at the other agent's revision
value (`RT-82`, numbered `RT-64` in the review file) and runs an
instrument that was already registered and had never been run: Amendment
A3 section 3.1's matched control **L2(a)**, the other-index subspace.*

## The cell

**FOUND NOWHERE.** Sub-pattern: **nothing was found on any checkpoint.**

Across nine testable positions, five layers and three checkpoints — 135
discovery tests — a fitted linear classifier does not find the other
agent's index anywhere, on any checkpoint, at the family-adjusted bar of
3.38 standard deviations. **No test anywhere reached even MARGINAL.**

**This is not a finding of absence**, and the section at the end holds it
to that.

## What it means for the question it was asked

The fitted read of the model's own register index came back found
nowhere, with one pattern worth naming: at the other agent's revision
value the own index was positive on fifteen tests of fifteen and reached
MARGINAL once. Two readings fitted that, and this run was built to
separate them.

**The exclusion reading is not supported.** That reading held that the
state at the other agent's revision value represents *which agent is
speaking*; since an agent is never its own other, representing that would
remove one rank of four and lift attainable accuracy on the own index
from 0.25 to about 0.333 with no self-representation involved. For that
to work, agent B's index has to be **there**. Pointed straight at it,
with an instrument that finds the very same target at +52.81 standard
deviations where agent B's marker is the input token, that position
yields **+1.00, +1.40 and +1.73** — nothing, on all three checkpoints.

So the own-index pattern at that token is **not** explained away as an
exclusion artefact. It is left standing and unexplained. That is a
different outcome from either reading, and it is less comfortable than
both: the reason offered for setting the pattern aside has been tested
and does not hold, and no replacement reason has been established.

**What this does not establish.** It does not show the own-index pattern
is a self-index. A null on agent B's index removes one proposed
confound; it does not rule out others, and it does not make a MARGINAL
into a finding. The own-index pattern remains a sub-bar pattern in a
family of 135 tests, which is the shape chance produces often enough to
be unremarkable on its own.

## The prediction, and what happened to it

The method file stated in advance, from the episode builder and with no
checkpoint loaded, that agent B's identity is a function of the tokens
read at the other agent's revision value in **100%** of episodes and at
the other agent's revision decision one token earlier in **0%** — because
a revision turn's value pins its agent, while the "to" before it pins
nothing. The pre-stated prediction was:

> If the exclusion reading is right, this run finds the other agent's
> index at the other agent's revision value and not at the decision one
> token earlier. If it finds it at neither, the exclusion reading is not
> supported.

**It found it at neither.** The named outcome is the one that occurred,
and the method file said before the run what that would mean.

## The instrument check came back exact

Before any sweep number was computed, the run re-ran the recorded
400-episode configuration and compared all fifteen numbers already on
the record. This run changes the target and nothing else, so the matched
run's anchor is its anchor.

| checkpoint | recorded (layers 3, 4, 5, 7, 8) | largest difference |
|---|---|---|
| pilot | 0.5025, 0.5125, 0.5225, 0.5250, 0.5175 | below 1e-6 |
| seed 1 | 0.4800, 0.5250, 0.5350, 0.5275, 0.5150 | exactly 0 |
| seed 2 | 0.4600, 0.4700, 0.4950, 0.4475, 0.4825 | exactly 0 |

Every cell reproduced. The pre-stated tolerance allowed a drift of one
episode in 400; none was used. The pilot's largest difference is not
exactly zero but is below one part in a million, which is summation
order, not disagreement.

**The capture path was checked too**, because this run adds a twelfth
position and a capture step that quietly moved the other eleven would
invalidate the whole comparison. The self-test runs the capture twice on
a small randomly-initialised model — no checkpoint read — once through
the matched run's unmodified capture and once through this run's, and
requires the eleven to come back element for element identical with the
same episodes kept. It does. **That check earned its place**: it caught a
fault in the position helper that would have failed the live run after
the anchor step.

## The target really is matched

Amendment A3 section 3.1 asks for a control "matched in rank and probe
accuracy". Both halves were measured rather than assumed.

**Matched in rank.** On the 4,000 episodes actually scored, the
other-agent index has the same class shares as the own register index to
four decimal places — 0.2582, 0.2410, 0.2547, 0.2460 — so the
majority-class rate a classifier gets for free is identical and the
no-information rate is 0.25 for both. The two are **never equal**, which
is the exclusion the run exists to test.

**Matched in probe accuracy.** Where each target's marker word is the
input token, the two read alike:

| checkpoint | own index at its marker token | agent B's index at its marker token |
|---|---|---|
| pilot | 0.5548 – 0.5670 | 0.5428 – 0.5665 |
| seed 1 | 0.5488 – 0.5575 | 0.5483 – 0.5600 |
| seed 2 | 0.5390 – 0.5485 | 0.5310 – 0.5530 |

## The controls

**The positive control holds on all three checkpoints**, strongly and
uniformly. At agent B's marker token every layer on every checkpoint is
FOUND:

| checkpoint | accuracy across layers | margin | draws beating it |
|---|---|---|---|
| pilot | 0.5428 – 0.5665 | +35.15 to +52.81 sd | 0 of 200 |
| seed 1 | 0.5483 – 0.5600 | +34.29 to +39.53 sd | 0 of 200 |
| seed 2 | 0.5310 – 0.5530 | +32.93 to +39.38 sd | 0 of 200 |

against a majority-class rate of 0.2582. No checkpoint is void.

**The negative control shows no leak anywhere.** On the model's first
assignment value restricted to the 2,000 episodes in which agent B's
marker word has not yet appeared anywhere, margins run from −0.96 to
+1.52 across all fifteen tests and nothing is FOUND. That says the
negative control showed no leak at that position and no more than that.

**The restriction does what it was meant to do.** The same position read
on all 4,000 episodes gives +1.85, +1.30 and +1.81; restricted to the
half where agent B has not yet been named it gives +1.14, +1.28 and
+1.52 on the best layer. The information the restriction removes is
information the read was using.

## The exclusion effect is real, and it is measured here

The model's own marker token is **not** a control for this target and is
not in the family; the method file said so in advance and reported it as
a diagnostic. It is the one place where the exclusion arithmetic can be
watched directly: the token says which rank is the model's, which is the
one rank agent B's cannot be, so a reader with no representation of agent
B at all can reach 1/3.

| checkpoint | agent B's index at the model's own marker token | margin |
|---|---|---|
| pilot | 0.2797 – 0.3030 | +4.65 to +7.67 sd, FOUND |
| seed 1 | 0.3077 – 0.3205 | +6.94 to +8.22 sd, FOUND |
| seed 2 | 0.2895 – 0.3010 | +5.15 to +6.34 sd, FOUND |

Every cell sits just under the 0.3333 that pure exclusion allows. **So
the mechanism the ledger's `RT-82` describes is real, is the right size,
and this run can see it** — which is exactly why its absence at the other
agent's revision value is informative rather than a null of an instrument
that could not have found anything.

## Every cell, as promised

Best layer per position, per checkpoint: accuracy and margin in standard
deviations. The no-information rate is 0.25 and the majority-class rate
0.2582. The last column is the share of episodes in which agent B's
identity is determinable from the tokens read, measured on the episode
builder before the run.

| position | pilot | seed 1 | seed 2 | determinable |
|---|---|---|---|---|
| `own_assign_1_value` *(diagnostic, unrestricted)* | 0.2642 +1.85 | 0.2622 +1.30 | 0.2647 +1.81 | 0% |
| `own_assign_1_value`, agent B not yet named *(negative control)* | 0.2645 +1.14 | 0.2680 +1.28 | 0.2700 +1.52 | 0% |
| `own_assign_2_value` | 0.2735 +2.79 | 0.2630 +1.47 | 0.2510 +0.14 | 0% |
| `own_revision_decision` *(the registered anchor)* | 0.2635 +1.65 | 0.2595 +1.15 | 0.2492 −0.16 | 50% |
| `own_revision_value` | 0.2652 +1.93 | 0.2638 +1.79 | 0.2515 +0.24 | 50% |
| `own_revision_by` | 0.2572 +1.12 | 0.2685 +2.30 | 0.2642 +1.75 | 50% |
| `own_revision_marker` *(diagnostic, exclusion only)* | **0.3030 +7.67** | **0.3205 +8.22** | **0.3010 +6.34** | 50% |
| `before_own_revision_turn` | 0.2565 +0.78 | 0.2580 +0.97 | 0.2495 +0.03 | 50% |
| `other_revision_decision` | 0.2608 +1.18 | 0.2560 +0.81 | 0.2457 −0.55 | 0% |
| `other_revision_value` | 0.2580 +1.00 | 0.2625 +1.40 | 0.2632 +1.73 | 100% |
| `other_revision_marker` *(positive control)* | **0.5553 +52.81** | **0.5600 +39.53** | **0.5530 +39.38** | 100% |
| `query_answer_decision` | 0.2508 +0.13 | 0.2520 +0.23 | 0.2540 +0.63 | 100% |
| `query_answer_value` | 0.2545 +0.38 | 0.2490 −0.08 | 0.2505 +0.16 | 100% |

Across all 45 testable tests per checkpoint the full range of margins is
−1.21 to +2.79 on the pilot, −2.27 to +2.30 on seed 1, and −2.15 to
+1.75 on seed 2.

## Consistency across layers and checkpoints

The Gate B review asked that any future sweep of this shape report
consistency rather than only per-test clearance, because the analysis
that found nothing had no way of seeing the one thing in its own data
that looked like something (`RT-62`). So it is reported, for both targets
side by side: the mean margin over all fifteen tests, the best, and how
many of the fifteen are positive.

| position | own index: mean / best / positive | agent B's index: mean / best / positive |
|---|---|---|
| `own_assign_1_value` | −0.07 / +0.49 / 8 of 15 | +0.85 / +1.85 / 13 of 15 |
| `own_assign_2_value` | −0.45 / +0.80 / 5 of 15 | +0.54 / +2.79 / 9 of 15 |
| `own_revision_decision` | −0.63 / +0.46 / 4 of 15 | +0.02 / +1.65 / 7 of 15 |
| `own_revision_value` | +0.13 / +2.07 / 8 of 15 | +0.47 / +1.93 / 11 of 15 |
| `own_revision_by` | +0.10 / +1.65 / 8 of 15 | +0.84 / +2.30 / 13 of 15 |
| `own_revision_marker` | +40.06 / +53.73 / 15 of 15 | +6.58 / +8.22 / 15 of 15 |
| `before_own_revision_turn` | −0.58 / +0.47 / 1 of 15 | −0.03 / +0.97 / 8 of 15 |
| `other_revision_decision` | −0.17 / +0.88 / 7 of 15 | −0.17 / +1.18 / 7 of 15 |
| **`other_revision_value`** | **+1.73 / +3.34 / 15 of 15** | **+0.46 / +1.73 / 13 of 15** |
| `query_answer_decision` | −0.12 / +1.29 / 7 of 15 | −0.48 / +0.63 / 7 of 15 |
| `query_answer_value` | +0.14 / +1.19 / 9 of 15 | −0.33 / +0.38 / 2 of 15 |

**The sharpest way to put the result.** Rank the nine testable positions
by mean margin, for each target separately:

- For the model's **own** index, the other agent's revision value ranks
  **first of nine** (+1.73; the next two are +0.14 and +0.13). It is
  distinctively the strongest testable position.
- For **agent B's** index, the same position ranks **fourth of nine**
  (+0.46; the top three are +0.84, +0.54 and +0.47). It is unremarkable.

And agent B's index carries a mild positive offset across this sweep
generally — +0.85 and +0.84 at two positions where nothing should be —
so its +0.46 at the position in question is **below its own baseline**,
not above it.

The position is special for the model's own index and ordinary for the
other agent's. The confound requires the reverse.

## The smallest signal this run could have found

Computed from each test's own null spread, and calibrated against **this
read's own measured ceiling** at the positive control rather than against
a perfect score — which the correction note of 2026-09-20 requires, and
which is not a small adjustment.

| checkpoint | measured ceiling | smallest detectable signal across the testable tests |
|---|---|---|
| pilot | 0.5665 | 6.89% – 10.27% (median 8.59%) |
| seed 1 | 0.5600 | 7.06% – 9.74% (median 8.74%) |
| seed 2 | 0.5530 | 7.89% – 10.17% (median 9.11%) |

So the run would have found agent B's index if it were legible in about
one episode in eleven, and found none. **This matters for the
comparison**: the matched own-index run's corrected figure is the same
one-in-eleven, so the two runs are comparably powered and the difference
between them at the position in question is not a difference in
sensitivity.

## Degeneracy, geometry, and the optimiser

**Degeneracy hits: none.** No test on any checkpoint had a null with zero
spread, a class missing from a training fold, or accuracy exactly equal to
the majority-class rate.

**Geometry at every position.** The share of variation carried by the top
ten of 448 directions runs from **0.8524 to 0.9953** across the three
checkpoints — 0.8524 to 0.9907 on the pilot, 0.9430 to 0.9953 on seed 1,
0.8729 to 0.9877 on seed 2. This matches the matched run and carries the
same caveat it does: the positive control sits in a far less concentrated
part of the space than the positions where the question is actually
asked, so a pass there is weaker evidence about the nine than its size
suggests.

**The optimiser's pass cap.** The share of fits hitting the 2,000-pass
cap is 11.9% on the pilot, 20.4% on seed 1 and **74.0% on seed 2** —
closely tracking the matched run's 13.5%, 22.3% and 73.6%. Seed 2's fits
are mostly stopped early and its numbers are the ones to treat most
cautiously. That cuts both ways: an early-stopped fit is an under-fitted
one, so seed 2's null is the least likely to be hiding a signal it could
have reached.

## What these findings may and may not say

They may say that at these positions, five layers and three checkpoints,
a fitted linear read does not find the other agent's index anywhere
except where its marker word is the input token or where exclusion from
the model's own marker token allows it; and that the exclusion reading of
the own-index pattern is therefore not supported.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index.

- Under **Amendment A3 section 3.2** nothing counts as localized or as
  absent until causal patching has also run. Patching has never been run
  (the ledger's item on it, `RT-49`, and the item on what a probe-only
  null means, `RT-50`). **The registered term for the line's state is
  *not testable (localization)***, and that is the term used here.
- The features were left unscaled, so this read is pulled towards the ten
  loud directions and a signal living in a quiet one is harder for it to
  reach (the ledger's items on the lopsided state space, `RT-34`, and on
  what a squared penalty charges a quiet direction, `RT-58`). The second
  follow-up run addresses exactly that; this one does not.
- A clearance is not a mechanism and a null is not one either. This run
  shows a confound large enough to produce the own-index pattern is **not
  demonstrably present** at that token. It does not show what is.
- The pilot-versus-seeds legibility gap on the difference-of-averages
  control is unchanged and unresolved.
- It does not touch red-team objection **R1** and changes no registered
  result.

## What this cannot do

One fitted linear statistic, twelve positions, five layers, 4,000
episodes, three 30-million-parameter checkpoints on a synthetic grammar,
one target. A null everywhere is consistent with the other agent's index
being carried non-linearly, or distributed across positions rather than
resident at any one of them, or in a quiet direction an unscaled fit is
pulled away from.

The three checkpoints also read **one** draw of 4,000 episodes, so they
are three models reading one sample rather than three samples, and the
five layers are five reads of one running state. The family bar of 3.38
is computed as though the 135 tests were independent; they are not
(`RT-59`). Nothing here turns on that, since nothing cleared, but it
would matter to a positive result.

## Open items

1. **Causal patching has still never run.** Under the registration it is
   required before anything counts as localized or absent. It remains the
   binding item.
2. **The own-index pattern at the other agent's revision value is now
   unexplained rather than explained.** The reason the earlier findings
   gave for setting it aside was wrong (the review's `RT-63`), and the
   confound offered in its place has now been tested and is not
   supported. It is still sub-bar and still the shape chance produces,
   but it is the one thing in this line that has survived two attempts to
   dismiss it. A targeted rerun at that one position with far more draws
   is the cheap next move.
3. **The marker-word target at these positions** remains unrun, at about
   seventy processor-hours.
4. **Seed 2's fits are mostly capped** (74.0%), unchanged and untested.

## Cost and where the output is

Local, inference only, no training, no network, $0 [C1/C2], on three
existing checkpoints verified by checksum. **11.63 hours** of wall-clock
time — 2.78 on the pilot, 3.31 on seed 1, 5.54 on seed 2 — at four
workers. The method file predicted twelve to thirteen processor-hours and
more than the matched run's 10.8 hours of wall-clock time; both held.

**A cost note that is not in the method file, recorded because it was
paid.** The run was first launched as three concurrent processes at three
workers each, on the reasoning that ten cores could carry nine workers.
Measured, that layout produced **6.7 tests per hour** against the four-
worker layout's **15.3** — per-test times of 2052 to 3615 seconds against
744 to 1103. The fit is limited by how fast the machine moves the state
table through memory, not by how fast it multiplies, exactly as the
matched run's method said ("six workers are no faster than four"). The
attempt was stopped after about an hour, before it had written anything,
and the run was restarted at four workers. **The restarted run reproduced
the aborted one's cells exactly** — 0.2592, 0.2585 and 0.2435 at the same
three tests — which is what the per-test seeding is for: a result depends
on the test's identity, not on how many workers happen to be running.

Outputs, none overwritten [C6]:

- `a3-gates/other_index_position_sweep_a3_a3_30m_seed0.json`
- `a3-gates/other_index_position_sweep_a3_a3_30m_seed1.json`
- `a3-gates/other_index_position_sweep_a3_a3_30m_seed2.json`
- `a3-gates/other_index_position_sweep_a3_summary.json`

These findings go through a Gate B review before any of this enters
`STATUS.md`.
