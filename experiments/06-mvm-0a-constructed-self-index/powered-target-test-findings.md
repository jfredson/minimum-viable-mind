# Powered test of a well-posed target — result

*2026-09-19. **UNREGISTERED**, diagnostic only. No verdict is read and
nothing here reopens one. Method and code committed before any output at
`6ef60ac`. Local, inference only, no training, no network, $0. Three
checkpoints verified by checksum.*

## The short version

**NOT CARRIED, on both arms, on all three checkpoints, with the positive
control holding on every one.** With the target well posed, the power
adequate, the null able to resolve the bar, and the read demonstrably
working *two tokens away*, own-agent identity is **not linearly present
at the registered probe position** on any checkpoint in hand.

Thirty tests at the anchor. Margins from −1.85 to +0.49 standard
deviations against a bar of three. Between 308 and 980 of every 1,000
shuffled draws matched or beat the real score. This is not a near miss.

This is the first informative null the localization stack has produced.
Everything before it — the 2026-09-16 blind-arm probes, the
denoise-before-probing diagnostic, the position sweep — asked for the
episode generator's agent index, which cannot be recovered in principle
(`position-sweep-findings.md`). Those nulls said nothing. This one says
something.

**It is a null about a position and a read, not about the models.** A
linear difference of averages at one position does not exhaust the ways
an identity could be carried.

## What the numbers look like

Held-out nearest-average accuracy, 4,000 episodes, 1,000 permutation
draws, four folds, per layer. The bar is three standard deviations of
each test's own null.

### The positive control: the marker word where it *is* the input token

Read at the marker position, two tokens past the anchor. Majority-class
rate 0.0475, no-information value 0.04.

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot | 0.5877 (**+159.1**) | 0.5735 (+157.4) | 0.5635 (+157.8) | 0.5533 (+152.4) | 0.5450 (+152.7) |
| seed 1 | 0.1100 (**+20.5**) | 0.1055 (+19.5) | 0.1087 (+20.2) | 0.1077 (+20.7) | 0.1022 (+18.6) |
| seed 2 | 0.1358 (**+27.2**) | 0.1323 (+27.4) | 0.1363 (+27.7) | 0.1398 (+29.5) | 0.1328 (+26.7) |

Not one of the 1,000 shuffled draws met or beat the real score at any
layer on any checkpoint. **The read works on all three**, and the
instrument is not in question.

### Arm 1: the model's own marker word, carried to the anchor

The marker has not been emitted when the anchor is reached — it comes
after the value — so anything here is carried, not copied.

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot | 0.0398 (−0.02) | 0.0385 (−0.39) | 0.0340 (−1.66) | 0.0362 (−1.07) | 0.0382 (−0.48) |
| seed 1 | 0.0370 (−0.77) | 0.0355 (−1.20) | 0.0385 (−0.38) | 0.0360 (−1.11) | 0.0390 (−0.26) |
| seed 2 | 0.0338 (−1.70) | 0.0387 (−0.33) | 0.0367 (−0.89) | 0.0350 (−1.38) | 0.0338 (−1.85) |

Every one of the fifteen margins is negative or within a rounding of
zero. Between 502 and 980 of the 1,000 shuffled draws met or beat the
real score. No layer on any checkpoint reaches the majority-class rate of
0.0475.

### Arm 2: the register index

The rank of the model's own marker among the four in the episode.
Majority-class rate 0.2582, no-information value 0.25.

At the anchor:

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot | 0.2445 (−0.64) | 0.2540 (+0.49) | 0.2437 (−0.75) | 0.2540 (+0.47) | 0.2497 (−0.02) |
| seed 1 | 0.2402 (−1.10) | 0.2400 (−1.14) | 0.2472 (−0.36) | 0.2532 (+0.34) | 0.2440 (−0.70) |
| seed 2 | 0.2470 (−0.34) | 0.2520 (+0.22) | 0.2497 (−0.04) | 0.2507 (+0.06) | 0.2485 (−0.17) |

At the marker position, where all four markers have been seen and the
rank is computable:

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot | 0.3093 (**+7.40**) | 0.3075 (+7.04) | 0.3063 (+7.01) | 0.3045 (+6.83) | 0.3058 (+6.89) |
| seed 1 | 0.2695 (+2.62) | 0.2720 (+2.72) | 0.2680 (+2.38) | 0.2615 (+1.46) | 0.2605 (+1.32) |
| seed 2 | 0.2878 (**+4.75**) | 0.2908 (+4.73) | 0.2885 (+4.64) | 0.2865 (+4.50) | 0.2943 (+5.54) |

**This settles the inconsistency the underpowered look left.** The
register index is genuinely represented on the pilot and on seed 2 — it
clears at all five layers on both, at around seven and around five
standard deviations, with no shuffled draw beating it — and it does not
clear at any layer on seed 1. So the earlier hints were real on two
checkpoints of three, and the odd one out is seed 1, which is also the
checkpoint where the marker word itself reads weakest. The underpowered
look had the pattern right and could not establish it.

**And it makes the anchor null sharper.** On the pilot and on seed 2 the
register index is a quantity the model demonstrably carries *somewhere* —
it reads at four to seven standard deviations at the marker position —
and it is flatly absent at the anchor two tokens earlier. That is not a
target problem and not an instrument problem.

## What the null does and does not support

**Does.** At the registered probe position, on these checkpoints, neither
the model's own marker word nor its register index is recoverable by a
linear difference of averages. The position the registered pipeline
probes is empty of a linearly decodable own-agent identity. Both
quantities are recoverable two tokens later, so this is a fact about the
position, not about the target or the read.

**Does not.** It does not show these models have no self-index. It reads
one statistic, linearly, at one position, at five layers. Identity could
be carried non-linearly, or distributed across positions, or at a
position not tested, and none of those is excluded. It also does not
touch red-team objection R1: even a clearance would not have
distinguished a carried self-index from the acting channel's input trace
passed forward.

**Does not change any registered result.** The blind arm's not-flagged
outcome, the 2026-09-16 not-testable verdict and the signed sensitivity
rule all stand exactly as recorded. Nothing here is a verdict and nothing
here reopens one.

## Why this null counts where the earlier ones did not

Four things had to be true at once, and this is the first run where they
were:

1. **The target is recoverable in principle.** Both arms use quantities
   that decode at the marker position. The generator index, which every
   earlier probe used, decodes nowhere because it picks out nothing.
2. **The power is adequate.** About 160 examples per marker word rather
   than 16.
3. **The null can resolve the bar.** With 1,000 draws the finest
   measurable probability is 0.001; a three-standard-deviation margin
   sits at 0.0013. With the 200 draws used before, the bar could not be
   checked against the draws at all — the margin was an extrapolation
   past what the null could show.
4. **The read is shown working on the same states, at a nearby
   position**, at 159 standard deviations on the pilot.

A null missing any one of those is uninformative. This one is missing
none.

## The family bar, and why it needed no adjustment

The two arms give 5 layers × 3 checkpoints × 2 targets = 30 discovery
tests. At a three-standard-deviation bar one test in about 740 clears on
its own, so across 30 the chance of a single false clearance is 4.0 per
cent — already inside five. The family-adjusted bar for 30 tests is 2.94
standard deviations, which the three-standard-deviation bar already
exceeds, so no adjustment was made. The question is moot in the event: across
all thirty anchor tests the margins run from −1.85 to +0.49 standard
deviations, so nothing came within two and a half standard deviations of
the bar.

## A note on the scorer, because a rewrite is how a method changes by accident

Running 1,000 draws needed a vectorised scorer — the same mathematics as
matrix products, about twelve times faster, which is the difference
between five minutes and an hour and a quarter. Rewriting a measurement
to make it affordable is exactly how a method quietly becomes a different
method, so the run verifies the new scorer against the original before
reporting anything, on a noise case and a planted-signal case, and
refuses to report on any disagreement. The recorded differences are
exactly 0.0 on both accuracy and separation, on both cases, on every
checkpoint. This check is in the output file of every run.

## The separate measurement: why the marker word is far more legible on the pilot

Descriptive. **No cell, no threshold, and deliberately no explanation.**
The sweep found the same input token at the same position decoding at
0.55 on the pilot and 0.06 to 0.12 on the other two, on checkpoints
differing only by training seed. Two quantities were measured.

**Marker-token embedding norms**, against the whole vocabulary:

| checkpoint | marker norm (mean) | vocabulary norm (mean) | ratio |
|---|---|---|---|
| pilot | 18.0415 | 17.9553 | 1.0048 |
| seed 1 | 17.9332 | 18.0229 | 0.9950 |
| seed 2 | 17.8898 | 17.9101 | 0.9989 |

Effectively identical, both across checkpoints and against the rest of
the vocabulary.

**Attention paid by the anchor to earlier marker tokens**, averaged over
episodes:

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot | 0.0854 | 0.0896 | 0.0696 | 0.0270 | 0.0070 |
| seed 1 | 0.1246 | 0.1202 | 0.0811 | 0.0803 | 0.0832 |
| seed 2 | 0.0308 | 0.0117 | 0.0053 | 0.0011 | 0.0179 |

(Own earlier markers are roughly a quarter of each figure; the rest is
other agents'. The model's own marker in the revision turn sits after the
anchor, where causal attention cannot reach it.)

**What these two numbers say, and nothing further.** The embedding norms
do not differ between checkpoints, so they do not distinguish them. The
attention figures do differ, but not in an order that lines up with
legibility: seed 1 pays the *most* attention to earlier markers and is
the checkpoint where the marker word reads *worst* at the marker
position, while seed 2 pays the least. These are also measurements at
different places — attention *from the anchor* against legibility *at the
marker position* — so they are not two views of one quantity.

The gap is not explained by either. Anything further would be a guess,
and the method file committed this measurement as reporting rather than
theorising. A real account would need its own method file and its own
measurement.

## What should happen next

1. **Record that the registered probe position is empty**, and that this
   is now established rather than suspected. Any future argument resting
   on a located structure at that position has to reckon with it.
2. **If the localization stack is to continue, the next question is where
   identity is carried, if anywhere** — the marker position is the only
   place either quantity reads, and that is a position where the identity
   is simply present in the input, which is not interesting on its own.
   A non-linear read, or a read across positions, is the honest next
   move, and it needs its own committed method.
3. **The legibility gap between checkpoints is still open** and is worth
   one bounded measurement rather than speculation.
4. **Quote the earlier nulls as uninformative**, not as null results.
   That instruction from the sweep's findings still stands and is
   reinforced: this run shows what an informative null looks like, and
   they are not it.

## Record

- Outputs: `a3-gates/powered_target_test_a3_a3_30m_seed{0,1,2}.json`,
  `a3-gates/powered_target_test_a3_summary.json`, and
  `a3-gates/marker_legibility_a3_a3_30m_seed{0,1,2}.json`. Fresh files,
  nothing overwritten.
- Method committed before output: `powered-target-test-method.md`
  (`6ef60ac`).
- Implementations: `src/powered_target_test_a3.py`,
  `src/marker_legibility_a3.py`.
- Gated on the known-answer test, which passes. Not gated on the
  threshold lock, and the method file says why.
