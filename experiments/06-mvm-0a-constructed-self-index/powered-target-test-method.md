# Powered test of a well-posed target — method, committed before the run

*2026-09-19. **UNREGISTERED**, diagnostic only. No verdict is read and no
cell here feeds one. Local, inference only, no training, no network, $0
[C1/C2]. Reads no registered verdict and touches no registered text.
Fresh output file per checkpoint, nothing overwritten [C6].*

*Committed before the test produces any output, under the same rule as
the two method files before it. The cells below were fixed while nobody
knew which would fire. If the numbers turn out to want a different rule,
that is a finding for a later run, not an edit to this file.*

## Why

The position sweep found that `own_slot` — the episode generator's index
for whichever agent the model is, and the target every probe in this
stack has predicted — **cannot be recovered from the model's states in
principle** (`position-sweep-findings.md`). For every one of its four
values, all four register indices and all twenty-five marker words occur.
It picks out nothing the model can see.

That left one well-posed question, asked in passing and badly
underpowered: **the model's own marker word, read at the registered
anchor position.** The marker has not been emitted yet at the anchor — it
comes after the value — so a model that knows which agent it is would
have to be *carrying* it. Unlike the generator index, this target is
decodable in principle, which is what makes a null mean something.

That first look read nothing, on about sixteen episodes per marker word
and against a 200-draw null that could not resolve a three-standard-
deviation margin at all. Both defects are fixed here.

**This is the first properly powered, well-posed test of whether these
models carry an own-agent identity.** It is still a diagnostic. It
decides nothing and reopens nothing.

## What is fixed relative to the underpowered look

| | before | here |
|---|---|---|
| episodes | 400 | **4,000** |
| examples per marker word | ~16 | **~160** |
| permutation draws | 50 (and 200 in the sweep) | **1,000** |
| finest resolvable probability | 0.02 (and 0.005) | **0.001** |
| is a three-standard-deviation margin resolvable? | **no** | **yes** |

The resolution point is the one that mattered. A margin quoted as three
standard deviations sits at a probability of about 0.0013 under a
bell-shaped null. With 200 draws the finest thing measurable is 0.005, so
the bar being used could not actually be checked against the draws — the
margin was an extrapolation past what the null could show. With 1,000
draws it can be checked, and every test reports the count directly.

## What is measured

### Checkpoints

The three A3 30-million-parameter checkpoints in hand, verified by
checksum: pilot `a3_30m_seed0.pt` (`f751228c…`), seed 1
`a3_30m_seed1.pt` (`eeed93b8…`), seed 2 `a3_30m_seed2.pt`
(`f1f131cb…`).

### Episodes

2,000 paired episodes from `localize_a3.paired_episodes` at content seed
20260917, giving **4,000 episodes**, all of which carry an own revision.
The marker pool is exactly 25 words, so each word falls to the model
about 160 times. The actual counts and the majority-class rate are
recorded per run rather than assumed.

Capture is chunked so that 4,000 episodes fit in memory, and only the two
positions below are kept. Chunking changes nothing about what is
computed: the model is causal and each episode is encoded independently.

### Positions

Two, both defined from `act_pos`, the token index of the value the model
emits at its own revision. A turn renders as `assign {item} to {value} by
{marker}`, so the marker sits two tokens after the value.

- **The anchor**, `act_pos − 1`. The registered probe position, the token
  that predicts the value. **The model's own marker has not appeared in
  this turn yet**, so anything read here is carried, not copied.
- **The marker position**, `act_pos + 2`. The model's own marker word, as
  an input token. **This is the positive control** and it tests the read
  rather than what the read is aimed at.

### Layers

3, 4, 5, 7 and 8, unchanged.

### The read

The plain difference-of-averages read, unchanged in definition from the
sweep: per class, that class's average training state minus the average
of the rest, scaled to unit length; held-out states assigned to the
nearest class average.

**The headline statistic is held-out nearest-average accuracy**, compared
against both its permutation null and the **majority-class rate** —
because with unequal class sizes a constant classifier already beats the
no-information value, and quoting only the latter flatters the result.

Macro separation (area under the curve, averaged over classes) is
reported beside it with its own null, carrying no cell.

Four-fold cross-validation. Every fitted quantity — class averages,
directions, nearest-average reference points — is fitted on the training
folds and applied to the held-out fold.

**A note on the implementation, because it is new.** The scorer used here
is a vectorised rewrite of the one the sweep used: the same mathematics
expressed as matrix products so that 1,000 draws are affordable at all
(11 ms per draw against 142 ms, about twelve times faster; the whole job
is minutes rather than hours). It is not a new method and must not become
one by accident, so the self-test checks it against the original scorer
and requires agreement to 1e-12 on accuracy and 1e-9 on separation, on
both a noise case and a planted-signal case. If they ever disagree, the
run does not report.

### The null

1,000 draws, each shuffling the labels and redoing the entire procedure
on the same folds. Every test reports the margin in standard deviations
of that null **and** how many of the 1,000 draws met or beat the real
score. Where the two disagree, the count is the honest number.

### The bar

**Three standard deviations, unchanged**, plus the count.

The family-adjusted bar, kept as asked: the two arms give 5 layers × 3
checkpoints × 2 targets = **30 discovery tests**. At a three-standard-
deviation bar one test in about 740 clears on its own, so across 30 the
chance of at least one false clearance is **4.0 per cent** — already
inside five per cent. The family-adjusted bar for 30 tests is 2.94
standard deviations, which the three-standard-deviation bar already
exceeds, so no adjustment is needed and none is made. Counting the 15
positive-control tests as well would put the bar at 3.06.

Every clearance is labelled:

- **ROBUST** — clears three standard deviations, clears 3.06 (the
  strictest reading of the family bar, counting all 45 tests), and **no
  shuffled draw out of 1,000 met or beat it**.
- **MARGINAL** — clears three standard deviations but not all of that.

## Arm 1 — the model's own marker word

Target: which of the 25 marker words belongs to the model, read at the
anchor. No information is 0.04; the majority-class rate is about 0.045
and is measured per run.

## Arm 2 — the register index

Identical procedure, identical positions, identical layers, identical
null, identical bar. Target: the rank of the model's own marker among the
four markers in the episode, sorted by vocabulary order — which
`encoding_a3` already computes as `turn_reg`. Four classes, no
information 0.25, majority-class rate about 0.27.

This target is consistently defined and recoverable from the input once
all four markers have appeared, which is why it is worth asking. The
sweep's underpowered look found it above its null at all five layers on
the pilot and on seed 2, at all five layers **below** on seed 1, and
clearing nowhere. That inconsistency is what this arm is powered to
settle.

## Preconditions, stated in advance

- A null with **zero spread** makes the comparison vacuous: that test is
  DEGENERATE and gets no cell.
- A class missing from a training fold means the procedure had nothing to
  fit: DEGENERATE, no cell.
- Accuracy exactly equal to the majority-class rate: DEGENERATE, no cell.

## The cells, fixed here

Applied **separately to each arm**, read across the three checkpoints.

First, per checkpoint, the positive control: **the marker word read at
the marker position**, where it is the input token. It must clear three
standard deviations on at least one layer for that checkpoint's anchor
result to be interpretable.

**CARRIED.** The anchor read clears on **the pilot and at least one other
seed**.

> Reading: these models carry an own-agent identity to the decision point,
> in a form a linear difference of averages can find. This would be the
> first positive result the localization stack has produced, and it would
> name the target the stack should have been using. It would still not
> settle red-team objection R1 — that what is carried is a self-index
> rather than the acting channel's trace passed forward.

**NOT CARRIED.** The anchor read clears on **no checkpoint**, and the
positive control holds on **every** checkpoint.

> Reading: with the target well posed, the power adequate and the read
> demonstrably working at a position two tokens away, own-agent identity
> is still not linearly present at the registered probe position. That is
> an informative null — the first this stack has produced — and it says
> the registered position is empty of a linearly decodable self-index,
> not that the instrument is broken.

**UNREADABLE.** The positive control fails on the pilot.

> Reading: the read does not work on the checkpoint it works best on, and
> nothing else in the arm can be interpreted. A seed whose positive
> control fails while the pilot's holds is excluded and named, and the
> arm is decided on the rest.

**Any other pattern fits no cell and is reported as fitting none** —
clearing on the pilot alone, clearing on seeds but not the pilot, or
clearing nowhere while a positive control failed somewhere. No bin is
added after the fact. Naming this in advance is the point: the three
cells above are not exhaustive over all possible outcomes, and pretending
otherwise is how a result gets forced into a bin it does not belong in.

## What this cannot do

It reads one statistic, linearly, at one position, five layers, on
30-million-parameter models trained on a synthetic grammar. A null is
consistent with identity being carried non-linearly, or distributed, or
at a position not tested. A clearance would not establish that what is
carried is a self-index rather than the acting channel's input trace
passed forward — red-team objection R1, which nothing here touches.

It also does not revisit `own_slot`. That question is closed: the target
is unrecoverable and the sweep's findings record why.

## The separate third measurement, which carries no cell at all

**Why the marker word is far more legible on the pilot than on the other
two.** The sweep found the same input token at the same position and
layers decoding at 0.55 on the pilot and 0.06 to 0.12 on seeds 1 and 2,
on checkpoints differing only by training seed. That is unexplained, and
until it is understood a null on seeds 1 and 2 rests on a positive
control that barely holds.

This is a **bounded look, and it reports rather than theorises.** Two
quantities, across the three checkpoints:

1. **Marker-token embedding norms.** The length of the embedding row for
   each of the 25 marker words, summarised per checkpoint, against the
   mean length over the whole vocabulary as a reference.
2. **Attention mass from the anchor to marker positions.** At the anchor
   row, the attention weight paid to marker tokens earlier in the
   episode, per layer, averaged over episodes — split into the model's
   own earlier markers and the other agents'.

Attention weights are obtained by recomputing each block's attention with
weights requested, then handing the block's own forward the same inputs
so the model's actual output path is untouched.

**No cell, no threshold, no hypothesis.** The numbers go in the findings
with a plain statement of what they are. Anything that looks like an
explanation is a candidate for a later measurement with its own method
file, and the findings will say so rather than assert it.

## Cost and where the output goes

Inference on three checkpoints on a laptop, then matrix products.
Estimated single-digit minutes for the scoring plus capture; no spend, no
network.

One fresh file per checkpoint under `a3-gates/`, named
`powered_target_test_a3_<checkpoint>.json`, a summary file,
`marker_legibility_a3_<checkpoint>.json` for the third measurement, and
`powered-target-test-findings.md`. Nothing existing is overwritten.

Implementations: `src/powered_target_test_a3.py` and
`src/marker_legibility_a3.py`, committed together with this file and
before either produced any output. Gated on the known-answer test, and
deliberately not on the threshold lock, for the reason given in
`denoised-direction-method.md`: nothing here ablates anything or is
scored against the bite threshold.
