# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 12 of 22: The localization records, 1 of 3: the fitted sweep and its correction

*This is file 12 of 22 of one review packet, pasted into a single
conversation. It contains the fitted eleven-position sweep; the correction
note carrying the one-legible-episode-in-eleven figure. Reply with one short
line saying you have it, and wait for the rest: the brief you are answering is
in file 1, and your review comes only after file 22 arrives. If this file
looks cut short, say so now.*

---

===== RECORD 11 of 23 - the fitted eleven-position sweep - COMPLETE FILE: experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md =====

# The fitted linear read at all eleven positions — findings

*2026-09-20 (Pacific). **UNREGISTERED**, diagnostic only. No verdict is
read and no cell here feeds one. Local, inference only, no training, no
network, $0 [C1/C2]. Method committed in
`fitted-position-sweep-method.md` at commit `f84db43`, together with
`src/fitted_position_sweep_a3.py`, **before either produced any output**.
The cells, the bar and the instrument check were fixed while nobody knew
which would fire.*

*Runs decision 2 of the Gate B review of the linear-read closure: the
ledger's `RT-33` (the read used for the sweep is about half as sensitive
as a fitted classifier), `RT-44` (the closure claim is unsupported) and
`RT-47` (the cheapest follow-up was never run).*

## The cell

**FOUND NOWHERE.** Sub-pattern: **nothing was found on any checkpoint.**

Across nine testable positions, five layers and three checkpoints — 135
discovery tests — a fitted linear classifier does not find the model's
register index anywhere, on any checkpoint, at the family-adjusted bar of
3.38 standard deviations. One test on one checkpoint reached MARGINAL and
is reported in full below.

**This is not a finding of absence**, and the section at the end holds it
to that.

## The instrument check came back exact

Before any sweep number was computed, the run re-ran the recorded
400-episode configuration and compared all fifteen numbers already on the
record. **Every one reproduced**, on all three checkpoints, to
floating-point round-off — the largest difference on any cell was below
1e-15, which is summation order, not disagreement. The pre-stated
tolerance allowed a drift of one episode in 400; none was used.

| checkpoint | recorded (layers 3, 4, 5, 7, 8) | largest difference |
|---|---|---|
| pilot | 0.5025, 0.5125, 0.5225, 0.5250, 0.5175 | below 1e-15 |
| seed 1 | 0.4800, 0.5250, 0.5350, 0.5275, 0.5150 | below 1e-15 |
| seed 2 | 0.4600, 0.4700, 0.4950, 0.4475, 0.4825 | below 1e-15 |

The classifier used here is therefore demonstrably the same instrument
that produced the record, not a lookalike.

## The controls

**The positive control holds on all three checkpoints**, strongly and
uniformly. At position 6, where all four marker words have appeared and
the register index is derivable, every layer on every checkpoint is
FOUND:

| checkpoint | accuracy across layers | margin | draws beating it |
|---|---|---|---|
| pilot | 0.5548 – 0.5670 | +37.5 to +53.7 sd | 0 of 200 |
| seed 1 | 0.5488 – 0.5575 | +34.0 to +40.9 sd | 0 of 200 |
| seed 2 | 0.5390 – 0.5485 | +35.9 to +39.0 sd | 0 of 200 |

against a majority-class rate of 0.2582. No checkpoint is void.

**The negative control shows no leak anywhere.** At position 1, where the
model's own marker has not yet appeared and the answer is not knowable,
margins run from −1.38 to +0.49 standard deviations across all fifteen
tests and nothing is FOUND. As `RT-42` insists, that says the negative
control showed no leak at position 1 and no more than that.

## Every cell, as promised

Best layer per position, per checkpoint. Accuracy, margin in standard
deviations, and how many of the 200 shuffled draws met or beat it. The
no-information rate is 0.25 and the majority-class rate 0.2582.

| position | pilot | seed 1 | seed 2 |
|---|---|---|---|
| 1 `own_assign_1_value` *(negative control)* | 0.2515 +0.23 (86) | 0.2508 +0.08 (88) | 0.2540 +0.49 (65) |
| 2 `own_assign_2_value` | 0.2462 −0.49 (136) | 0.2558 +0.80 (40) | 0.2515 +0.23 (83) |
| 3 `own_revision_decision` *(the registered anchor)* | 0.2538 +0.46 (60) | 0.2512 +0.18 (88) | 0.2482 −0.26 (123) |
| 4 `own_revision_value` | 0.2558 +0.68 (50) | 0.2678 +2.07 (0) | 0.2470 −0.32 (127) |
| 5 `own_revision_by` | 0.2528 +0.34 (76) | 0.2610 +1.65 (10) | 0.2532 +0.38 (68) |
| 6 `own_revision_marker` *(positive control)* | **0.5670 +53.73 (0)** | **0.5575 +40.86 (0)** | **0.5390 +39.04 (0)** |
| 7 `before_own_revision_turn` | 0.2503 −0.04 (110) | 0.2528 +0.47 (57) | 0.2462 −0.41 (131) |
| 8 `other_revision_decision` | 0.2520 +0.24 (85) | 0.2518 +0.16 (89) | 0.2572 +0.88 (37) |
| 9 `other_revision_value` | 0.2688 +2.33 (2) | 0.2700 +2.39 (2) | **0.2770 +3.34 (0)** |
| 10 `query_answer_decision` | 0.2535 +0.48 (62) | 0.2615 +1.29 (24) | 0.2528 +0.46 (66) |
| 11 `query_answer_value` | 0.2528 +0.37 (79) | 0.2605 +1.19 (19) | 0.2550 +0.68 (56) |

Across all 45 testable tests per checkpoint the full range of margins is
−1.49 to +2.33 on the pilot, −1.30 to +2.39 on seed 1, and −3.01 to +3.34
on seed 2.

## The one MARGINAL, in full

**Seed 2, `other_revision_value`, layer 4**: accuracy 0.2770, margin
+3.34 standard deviations, zero of 200 draws met or beat it, and it beats
the majority-class rate. It clears the per-test bar of 3.0 and **not** the
family-adjusted bar of 3.38, so under the pre-stated rule it is MARGINAL
and triggers no cell.

It is worth naming rather than burying, because **the same position is
the highest testable position on all three checkpoints** — +2.33, +2.39,
+3.34 — which is more consistent than the other eight. Three cautions
against reading anything into it:

- It is the **other** agent's revision value, not the model's own. If
  something is readable there it is not obviously own-agent identity.
- Seed 2 is the checkpoint where the instrument is straining hardest:
  73.6% of its fits hit the optimiser's pass cap, against 13.5% on the
  pilot.
- One position rising on three checkpoints while never reaching the bar
  is exactly the shape a family of 135 tests produces by chance often
  enough to be unremarkable.

It is recorded as an open item, not a result.

## The smallest signal this run could have found

Per `RT-37`, computed from each test's own null spread: the accuracy
needed to clear the bar, expressed as the share of episodes that would
have to be perfectly legible with the rest at chance.

| checkpoint | at this run's 3.38 bar | at the powered sweep's 3.56 bar |
|---|---|---|
| pilot | 3.05%–4.08% (median 3.65%) | median 3.84% |
| seed 1 | 3.03%–4.05% (median 3.65%) | median 3.86% |
| seed 2 | 3.22%–4.03% (median 3.71%) | median 3.91% |

So the run would have found a register index legible in about one episode
in twenty-seven, and found none. Measured against the majority-class rate
instead of the no-information rate the figures are smaller still, about
2% to 3%.

**An honest surprise worth recording.** At the same 3.56 bar the previous
difference-of-averages sweep's figure was 3.9%, and this fitted read's is
3.84% to 3.91% — **essentially identical power in this measure**. The
reason is that the two reads have almost exactly the same noise floor at
these positions: the median spread of the shuffled-label null is 0.0081
for the fitted classifier and 0.0082 for the difference of averages. The
fitted read's advantage is not a quieter null; it is that it extracts far
more signal **where signal exists**, which is precisely what the next
section shows and what a null cannot.

## RT-33 confirmed and now measured directly

The ledger's fatal finding was inferred from a comparison across
different targets. It can now be stated on the same target, at the same
position, on the same checkpoints — the register index at position 6:

| checkpoint | fitted classifier | difference of averages |
|---|---|---|
| pilot | 0.5548 – 0.5670 | 0.3045 – 0.3093 |
| seed 1 | 0.5488 – 0.5575 | 0.2605 – 0.2720 |
| seed 2 | 0.5390 – 0.5485 | 0.2865 – 0.2943 |

Against a no-information rate of 0.25, comparing the average lift above
that rate across the five layers, the fitted read recovers **5.5 times as
much on the pilot, 18.7 times on seed 1 and 7.5 times on seed 2**.
`RT-33` said "about half as sensitive"; on this target, at this position,
the gap is much wider than that, and it is now backed by a direct
measurement rather than an inference across different targets.

This is also what makes the null meaningful: the read that found nothing
at nine positions is demonstrably the sensitive one, not the weak one.

## The legibility gap, quoted and not resolved

`RT-36` requires this be carried as a caveat rather than argued away, so
it is. On the difference-of-averages marker-word control, the same input
token at the same position is read at 0.5450–0.5877 on the pilot and at
0.1022–0.1100 and 0.1323–0.1398 on seeds 1 and 2 — recovering the answer
on roughly one episode in eight **when the answer is the token it is
looking at**. That gap is unexplained; the one measurement aimed at it
came back empty; it remains open.

**What this run adds, and what it does not.** The fitted read's own
control does not show the gap: 0.5548–0.5670, 0.5488–0.5575 and
0.5390–0.5485 across the three checkpoints, which is flat. That is a fact
about this instrument on this target. It is **not** an explanation of the
difference-of-averages gap, and it is not offered as one: different read,
different target. The gap stays an open item exactly as the ruling
requires, and the nulls on seeds 1 and 2 here rest on a control that
holds on its own terms.

## Degeneracy, geometry, and the optimiser

**Degeneracy hits: none.** No test on any checkpoint had a null with zero
spread, a class missing from a training fold, or accuracy exactly equal to
the majority-class rate. The precondition that fired twice unreported in
the previous sweep (`RT-38`) did not fire here, and that is stated because
it was pre-stated.

**Geometry at every position (`RT-40`), not just the anchor.** The share
of variation carried by the top ten of 448 directions runs from **0.8524
to 0.9953** across all 165 tests. It is consistently lowest at position 6,
the one place the answer is present — 0.8579 on the pilot at layer 5,
against 0.9899 at the highest position. The stack's earlier figure of
about 99% in ten directions holds at the other positions and is now
measured at all of them rather than one.

**The optimiser's pass cap.** At 4,000 episodes the share of fits hitting
the 2,000-pass cap is 13.5% on the pilot, 22.3% on seed 1 and **73.6% on
seed 2**. Seed 2 is much the hardest to fit, is the slowest to run, and is
the only checkpoint producing a MARGINAL. A capped fit is a fit that
stopped early, so seed 2's numbers are the ones to treat most cautiously.

## Two corrections to the committed method file

Committed method files are not edited after the run (`RT-43`), so the
corrections go here.

**1. The method file says the classifier "hits the 2,000-pass cap on every
fold" at 400 episodes. That is wrong.** Measured during the anchor
reproduction: the pilot converges on every one of its twenty folds, using
158 to 933 passes. Seeds 1 and 2 do hit the cap, on 9 of 20 and 17 of 20
folds. The claim came from a cost probe run at 200 episodes, not 400, and
it was carried into the method file without being rechecked at the right
size. Nothing downstream depends on it: the instrument was kept identical
either way and reproduced the record exactly. The sentence in the method
file that follows from it — that the recorded numbers "come from a fit
that stopped early" — is true of seeds 1 and 2 and false of the pilot.

**2. The estimated cost was low.** The method file projected about six and
a half hours; the run took **10.8 hours** — 2.93 on the pilot, 3.36 on
seed 1, 4.47 on seed 2. The per-test cost varies more than the benchmark
suggested, and it tracks the pass-cap rate: the checkpoint whose fits
converge least is the one that takes longest. The processor-hours estimate
of about eleven was close; the parallel speed-up was the part that was
over-estimated.

## What these findings may not say

They may say that at these eleven positions, five layers and three
checkpoints, a fitted linear read does not find the register index
anywhere except where the answer is derivable from the current context.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index.

- Under **Amendment A3 §3.2** nothing counts as localized or as absent
  until causal patching has also run. Patching has never been run
  (`RT-49`), so under the registered text a probe-only null is
  **instrument failure, not absence** (`RT-50`).
- The register index has **no guaranteed-present positive control**, only
  the derivable one at position 6, as the method file stated in advance
  (`RT-35`). So a null everywhere cannot separate "the models do not carry
  the register index away from that position" from "this read cannot find
  it away from that position". Position 6 shows the read can find the
  answer where it is most accessible; it certifies nothing at a position
  where it is less so.
- One target was read. The **marker-word target was not run**, and the
  method file said so before the run with the arithmetic: about 70
  processor-hours against about 11.
- The features were left unscaled, so the fit is pulled towards the ten
  loud directions and a signal living in a quiet one is harder for it to
  reach (`RT-34`). This is a more sensitive read than the last one, not a
  sensitivity ceiling.
- It does not touch red-team objection **R1** and changes no registered
  result.

## Open items

1. **Causal patching has still never run.** Under the registration it is
   required before anything counts as localized or absent. This is the
   binding item, and it is already on the 2026-10-04 control-battery
   decision.
2. **`other_revision_value` rises on all three checkpoints** (+2.33,
   +2.39, +3.34) and reaches MARGINAL on seed 2. If any position deserves
   a targeted rerun with far more draws, it is this one — though it is the
   other agent's turn, not the model's own.
3. **The marker-word target at these eleven positions** remains unrun, and
   is the obvious remaining cheap-ish read if about 70 processor-hours can
   be found.
4. **The pilot-versus-seeds legibility gap** on the difference-of-averages
   control is still unexplained.
5. **Seed 2's fits are mostly capped** (73.6%). Whether raising the cap
   changes anything there is unknown and untested; it would be a different
   instrument and would need its own anchor.

## Cost and where the output is

Local, inference only, no training, no network, $0 [C1/C2]. 10.8 hours of
wall-clock time, about eleven processor-hours, on three existing
checkpoints. Outputs, none overwritten [C6]:

- `a3-gates/fitted_position_sweep_a3_a3_30m_seed0.json`
- `a3-gates/fitted_position_sweep_a3_a3_30m_seed1.json`
- `a3-gates/fitted_position_sweep_a3_a3_30m_seed2.json`
- `a3-gates/fitted_position_sweep_a3_summary.json`

These findings go through a Gate B review before any of this enters
STATUS.md.

===== END OF RECORD 11 =====

===== RECORD 12 of 23 - the correction note carrying the one-legible-episode-in-eleven figure - COMPLETE FILE: experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md =====

# Correction note — the sensitivity figure in `fitted-position-sweep-findings.md`

*2026-09-20 (Pacific). The findings file is committed method-then-output
text and is not edited. This note sits beside it and is cited wherever the
figure is used. Ruled by John 2026-09-20 on Gate B review finding RT-74
(ledger numbering; RT-56 in the review file), "agreed on all".*

The findings state that the run would have detected the register index if
it were legible in about one episode in twenty-seven. That figure assumes a
perfectly legible episode scores 1.0. This read never does: the only ceiling
the run measures is 0.539 to 0.567, at the position where the answer is the
input token. Recalibrated against that ceiling, the run's reach is a signal
legible in about **one episode in eleven**. The same correction applies to
the "essentially identical power" comparison between the two reads
(review RT-73 / ledger RT-91): the conclusion drawn there stands, the
reasoning given for it does not.

Anywhere the one-in-twenty-seven figure has been quoted (STATUS.md, the
step 4 proposal, the paper draft), it reads one in eleven and cites this
note.

===== END OF RECORD 12 =====
