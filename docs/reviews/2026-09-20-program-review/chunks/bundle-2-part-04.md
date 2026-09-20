> DIAGNOSTIC ONLY. No rule is rewritten after the data.**
>
> That settles it, and it is the right call for a reason worth recording.
> I found the absolute-value hole *because* of what the data did, and a
> rule changed at that moment is not a pre-stated rule any more, however
> sound the correction looks. The discipline only works if the criteria
> that were committed are the criteria that are read. Anything else lets
> the result choose its own test.
>
> So: **the verdict of this run is NOT TESTABLE.** The signed reading is
> recorded, is not a verdict, and does not become one later. What the
> absolute-value form should be for any FUTURE run of this pipeline is a
> separate question, to be settled before that run rather than after it.

## The lesion behaves like a non-specific one

Whatever the blind search carved, its removal **improved** the battery
that depends on ownership and **damaged** a battery that does not, past
that battery's own locked threshold of 0.1172. The syntax control did not
move.

That is close to the inverse of a self-location signature. A structure
that indexes the act to its own center should degrade the primary battery
and leave the state battery alone. This did the opposite on both counts.

## What this says, given that ownership *is* load-bearing here

This is the point of the control. On this exact checkpoint, ownership is
measured to matter: zeroing the acting channel takes the primary battery
from 0.506 to 0.182, while the ownership-free batteries hold at 0.999 and
1.000, and across 120 content-blind ablations the worst reached 0.2758
against 1.515 for the authorship lesion.

So there is something here to find, and the localization stack did not
find it. It returned five probes below their nulls and a subspace whose
removal helps the action it was supposed to be carrying.

**Taken with the registered arm, the stack has now come up empty on both
checkpoints it has been pointed at**: once where there was nothing to find,
which was uninformative, and once where something is known to be there.
Only the second is evidence, and it is evidence of insensitivity at this
scale.

> **WITHDRAWN 2026-09-16 on John's ruling. The paragraph above stays as
> written; its last clause is the one withdrawn.** John: *"Withdraw
> 'evidence of insensitivity at small scale' for now... The result cannot
> yet distinguish an insensitive stack from a broken pipeline."*
>
> He is right that I claimed more than the run could carry, and he was
> right before the known-answer test existed to settle it. Two facts were
> ruled to sit beside the withdrawal, and both were measured.
>
> **FACT ONE: the five probes falling below their nulls is systematic,
> not chance scatter.** All five margins are negative: −0.75, −0.54,
> −0.96, −0.24 and −1.01 standard deviations. If the five were
> independent, all falling below their own null means would happen about
> **1 time in 32**. They are not independent: they read the same episodes
> at different depths, so they are positively correlated and the true
> probability is **higher** than 1 in 32. That figure is a floor on how
> surprising this is, not a p-value, and it is reported as one.
>
> **FACT TWO: the +0.052 movement is inside evaluation noise.** Measured
> rather than argued, twelve independent draws of the same evaluation on
> the same checkpoint at each sample size:
>
> | episodes | scored denominator | mean | sd | min | max | range |
> |---|---|---|---|---|---|---|
> | 400 | ~200 | 0.5621 | 0.0284 | 0.520 | 0.599 | **0.079** |
> | 800 | ~397 | 0.5663 | 0.0169 | 0.542 | 0.593 | **0.051** |
>
> The control ran at 400 episodes, where one standard deviation of pure
> evaluation noise is 0.0284. The movement under test is 0.052, which is
> **1.8 standard deviations** and sits well inside the observed range of
> 0.079. So the ablation's apparent effect on the ownership battery
> carries no information. The scored denominator is about half the episode
> count because the action is scored only where the model revises, which
> is why the noise is larger than the nominal sample size suggests.
>
> **A CORRECTION TO THE RULING'S PREMISE, at John's instruction, with his
> original wording kept.** The ruling as issued read: *"the ownership
> battery's baseline has read 0.506, 0.483, 0.4975 and 0.440 across
> evaluations, so +0.052 is inside evaluation noise."* John then wrote:
> *"Ruling 2's premise contained an error from the Cowork session: 0.483
> and 0.4975 are Gate 3 detector scores, not ownership-battery baselines.
> Note the correction beside the ruling, original wording kept. Your
> twelve-draw measurement supersedes the argument."* Those two numbers are
> areas under the curve from the Gate 3 fingerprint detector's two arms,
> where chance is 0.5 and the equivalence bound was [0.45, 0.55]. The
> conclusion is unaffected, because it now rests on the measurement rather
> than on the comparison.
>
> **AND A THING WORTH KNOWING, found while checking that premise.** The
> two genuine on-record readings, 0.506 and 0.440, are **not two
> independent draws**. Both come from the single default evaluation seed,
> 987654321, which reproduces them exactly at 800 and 400 episodes. Both
> also sit below all twelve fresh draws at their own sample size. So the
> programme's headline ownership number rests on one unlucky evaluation
> seed, and the checkpoint's typical score is nearer **0.566** than 0.506.
> That does not change any verdict — every drop is measured against its
> own baseline in the same run — but any write-up quoting 0.506 as the
> pilot's ownership score should quote the spread with it.
>
> **WHAT THE WITHDRAWAL LEAVES STANDING.** The probe result is the only
> signal this run carries, and it is "found nothing". The ablation result
> is noise. Whether "found nothing" means an insensitive stack or a broken
> pipeline was exactly John's open question, and the known-answer test he
> ordered in the same breath now answers the pipeline half: it passes at
> ceiling, accuracy 1.0 against a null of 0.1306, a margin of 32.9
> standard deviations (`known-answer-test-findings.md`). That test
> validates residual capture, position indexing, probe fitting and null
> construction. It does not exercise the ablation path, and it probes a
> different layer and position than the blind runs did. So the pipeline's
> shared machinery is sound and the claim stays withdrawn until something
> tests the rest.

## What a pass would and would not have shown, per John's ruling

John ruled that when this reported, the record must say what a pass does
and does not show. It did not pass, so this is written as the scoping that
*would* have applied, and it matters more now rather than less, because it
shows how generous the test was that the stack still failed.

**A pass would have shown:** sensitivity to an **input-side** signal whose
removal produces a measured drop of about **0.32** in raw battery points,
from 0.506 to 0.182. That is a large, deliberately constructed, single
channel.

**A pass would NOT have shown:**

- Sensitivity to **weaker** structure. Nothing here speaks to whether the
  stack could find something whose removal costs a tenth of that. The
  ground truth was chosen because it is the strongest signal the programme
  has, which is exactly what makes it a weak basis for generalising
  downward.
- Sensitivity to **purely internal** structure. The ground truth is the
  removal of an input channel, not of a structure the network built. A
  pass would show the stack can find something whose removal hurts the
  act; it would not establish that the thing found is a carried
  self-index rather than the input trace passed forward. That is red-team
  objection R1 and this control never addressed it.
- Anything registered. The control is **unregistered** and was proposed
  after the pilot result was known. A pass would have carried less weight
  than a registered result, and any write-up would have had to say so.

Since it failed rather than passed, the honest summary is narrower still:
the stack did not find the strongest, most deliberately constructed,
input-side ownership signal available to it, at 30M.

## Honest notes

- The baseline primary score here is **0.440**, against **0.506** at the
  pilot endpoint. The endpoint used 800 episodes and this used 400, so
  this is sampling variation on a different draw, not a discrepancy in the
  checkpoint. The checksum matches the ledger exactly.
- The probes read residual states at revision positions, which is the A3
  pipeline's registered choice. A different position choice might read
  differently, and nothing here tests that.
- The lock was honoured throughout. It supplied θ = 0.1777 on the primary
  battery and carries no threshold at all for the control battery, so the
  control battery is reported and never read for a verdict.
- This is one checkpoint and one seed. Seeds 1 and 2 are still training.


===== FILE: experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-findings.md =====

# Powered eleven-position sweep — result

*2026-09-20. **UNREGISTERED**, diagnostic only. No verdict is read and
nothing here reopens one. Method and code committed before any output at
`68f7708`. Local, inference only, no training, no network, $0. Three
checkpoints verified by checksum.*

## The result

**CARRIED NOWHERE, on both arms.**

Across eleven positions, five layers, two well-posed targets and three
checkpoints — **270 testable tests** — **not one reached even three
standard deviations**, let alone the family-adjusted bar of 3.56. The
largest margin anywhere was **+2.73**, the smallest **−2.59**, and the
mean across all 270 was **−0.085**. Zero marginal clearances. Zero robust
clearances.

The only things that cleared in the entire sweep were the positive
controls, which are the positions where the answer is the input token.

**Which positions clear: none.** That was the question, and that is the
answer.

## Every position, best margin across the five layers

Margins in standard deviations of each test's own 1,000-draw permutation
null. The cells turn on 3.56; three standard deviations is shown for
continuity with earlier runs.

### Arm 1 — the model's own marker word

| position | pilot | seed 1 | seed 2 | |
|---|---|---|---|---|
| `own_assign_1_value` | +0.60 | +0.03 | +0.36 | *negative control* |
| `own_assign_2_value` | +1.16 | +0.42 | +0.64 | |
| `own_revision_decision` | −0.02 | −0.26 | −0.33 | *the registered anchor* |
| `own_revision_value` | +0.55 | +1.36 | +1.78 | |
| `own_revision_by` | +0.12 | +0.06 | +1.51 | |
| `own_revision_marker` | **+159.08** | **+20.66** | **+29.45** | *positive control* |
| `before_own_revision_turn` | +0.92 | +0.97 | +0.83 | |
| `other_revision_decision` | +0.43 | −0.04 | +0.63 | |
| `other_revision_value` | −0.03 | **+2.73** | +0.04 | |
| `query_answer_decision` | +0.83 | +1.00 | +0.97 | |
| `query_answer_value` | +0.60 | +1.96 | +0.20 | |

### Arm 2 — the register index

| position | pilot | seed 1 | seed 2 | |
|---|---|---|---|---|
| `own_assign_1_value` | +0.76 | +0.74 | −0.71 | *negative control* |
| `own_assign_2_value` | −0.42 | +0.56 | +1.25 | |
| `own_revision_decision` | +0.49 | +0.34 | +0.22 | *the registered anchor* |
| `own_revision_value` | +0.46 | +1.68 | −0.08 | |
| `own_revision_by` | +0.60 | +1.67 | +0.14 | |
| `own_revision_marker` | **+7.40** | +2.72 | **+5.54** | *positive control* |
| `before_own_revision_turn` | +1.51 | +0.48 | +1.10 | |
| `other_revision_decision` | +1.06 | −0.12 | +0.22 | |
| `other_revision_value` | +0.94 | +1.17 | +1.07 | |
| `query_answer_decision` | −0.21 | −0.14 | +0.34 | |
| `query_answer_value` | +1.36 | +0.28 | +1.42 | |

## Both controls behaved, which is what lets the null be read

**The positive control holds on all three checkpoints.** The marker word
read where it *is* the input token clears at +159, +21 and +29 standard
deviations, with no shuffled draw out of 1,000 beating it. The read
works everywhere it is applied. The register index also clears at that
position on the pilot (+7.40) and seed 2 (+5.54), reaching +2.72 on seed
1; the control that governs both arms is the marker word, and it holds
without qualification.

**The negative control shows no leak.** At the value token of the model's
first own turn, where its own marker has not yet appeared anywhere in the
episode and neither target is determinable, the margins are +0.60, +0.03
and +0.36 for the marker word and +0.76, +0.74 and −0.71 for the register
index. Nothing clears.

That second result is worth its own sentence, because it was the outcome
that would have undermined everything else. The acting channel injects at
exactly that token, and had it been leaking the model's own identity
there, every other position in the sweep would have been in doubt. It is
not. **The channel does not carry the marker identity into that
position**, which is a small positive finding in its own right and the
reason the other 270 numbers can be taken at face value.

## The anchor reproduces the previous run exactly

The registered position reads −0.02, −0.26 and −0.33 in the marker-word
arm — identical to the powered anchor test of the previous run, on the
same episodes with the same seeds. The sweep widened the measurement from
two positions to eleven and did not perturb the one number that was
already known. That is the consistency check it should be expected to
pass, and it passed.

## The family bar: the right call, and moot in the event

Setting it was not a formality. With 270 discovery tests, leaving the bar
at three standard deviations would have given a **30.6 per cent** chance
of a false clearance somewhere — for a sweep whose entire question is
"does anything clear anywhere", that is the error that would have
manufactured a finding. The bar was raised to 3.56 before the run.

In the event it made no difference: nothing reached 3.0 either. The
distinction between the two bars never had to be exercised, and the
honesty note attached to it in the method file — that 1,000 draws resolve
only to p < 0.001, or about 3.09 standard deviations, and so cannot on
their own certify a family-safe clearance — never had to be called on.
Both are recorded because they were committed in advance and would have
governed a different outcome.

## What this settles, and what it does not

**Settles.** Combined with the anchor result, the linear-read line of
attack on these checkpoints is closed. Own-agent identity — in either of
the two forms the grammar makes well-posed — is not linearly recoverable
by a difference of averages at any of eleven positions across the
episode, at any of five layers, on any of three checkpoints, except at
the one position where it is present as an input token. The instrument
demonstrably works: at that position it reads the answer at 159 standard
deviations.

**Does not settle.** It reads one statistic, linearly, at eleven
positions out of an episode of seventy-one tokens. Identity could be
carried non-linearly. It could be distributed across positions rather
than resident at any one of them, which a per-position read cannot see by
construction. It could sit at a position not on the list. None of that is
excluded, and a null from a linear probe is weak evidence about a
non-linear representation.

It also does not touch red-team objection R1, and it **changes no
registered result**: the blind arm's not-flagged outcome, the 2026-09-16
not-testable verdict and the signed sensitivity rule all stand exactly as
recorded.

**What it is not evidence for.** It is not evidence that these models
have no self-index, and it should not be written up as though it were.
The honest statement is narrower and duller: a linear difference of
averages, at the positions and layers we chose, does not find one.

## Where this leaves the line of work

This was the last run in this line, and it ends on a clean negative with
working controls, which is a better place to stop than the three
uninformative nulls that preceded it.

What the sequence established, in order: the target every earlier probe
used could not be recovered in principle; with a well-posed target and
real power the registered probe position is empty; and now, the rest of
the episode is empty too under the same read. Each of those is a fact
about the instrument and the position rather than about the models, and
the write-up should say so in those terms.

The open questions that a future session would have to take up — a
non-linear read, a distributed read across positions, and the unexplained
gap in how legible the marker token is between checkpoints — each need
their own committed method file. None of them is started here.

## Record

- Outputs: `a3-gates/powered_position_sweep_a3_a3_30m_seed{0,1,2}.json`
  and `a3-gates/powered_position_sweep_a3_summary.json`. Fresh files,
  nothing overwritten.
- Method committed before output: `powered-position-sweep-method.md`
  (`68f7708`).
- Implementation: `src/powered_position_sweep_a3.py`.
- The vectorised scorer was verified against the original before each
  run reported: differences exactly 0.0 on accuracy and separation, on
  both the noise and planted-signal cases, on all three checkpoints.
- 4,000 episodes, 1,000 draws, four folds, layers 3/4/5/7/8, three
  checkpoints run as parallel processes. No spend.
- Gated on the known-answer test, which passes. Not gated on the
  threshold lock, and the method file says why.


===== FILE: experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md =====

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
