# Position sweep — result

*2026-09-19. **UNREGISTERED**, diagnostic only. No verdict is read and
nothing here reopens one. Method and code committed before any output at
`af7232b`. Local, inference only, no training, no network, $0. Three
checkpoints verified by checksum.*

## The short version

**Arm 1 is SWEEP INVALID on all three checkpoints.** The positive control
failed, which under the pre-stated rule means no position on any
checkpoint can be interpreted. Zero of the 165 tests cleared.

**And the reason matters far more than the sweep did.** The positive
control failed because the thing every probe in this stack has been
predicting — `own_slot`, the episode generator's index for whichever
agent the model is — **has no consistent surface realisation and cannot
be recovered from the model's states in principle.** Not on these
checkpoints, not at any position, not with any instrument.

If that holds, then the 2026-09-16 blind-arm probes, the
denoise-before-probing diagnostic, and this sweep were all asking a
question with no answer, and their nulls are uninformative rather than
evidence of absence.

**Arm 2 ran and is reported below, but the same finding undercuts it**:
comparing two instruments on an undecodable target measures how they
behave on noise, not their relative sensitivity.

## Arm 1 — what came back

Best separation across the five layers, per position and checkpoint. No
information is 0.5; the bar is three standard deviations of each test's
own 200-draw permutation null.

| position | pilot | seed 1 | seed 2 |
|---|---|---|---|
| `own_assign_1_value` (injection) | 0.5403 (+1.85) | 0.5426 (+1.87) | 0.5044 (+0.19) |
| `own_assign_2_value` (injection) | 0.5162 (+0.38) | 0.5242 (+1.00) | 0.5481 (+2.17) |
| `own_revision_decision` (**the anchor**) | 0.5373 (+1.60) | 0.5110 (+0.35) | 0.5212 (+0.85) |
| `own_revision_value` (injection) | 0.5401 (+1.87) | 0.5358 (+1.42) | 0.5361 (+1.44) |
| `own_revision_by` | 0.5100 (+0.42) | 0.5224 (+0.95) | 0.5327 (+1.63) |
| `own_revision_marker` (**positive control**) | 0.5355 (+1.61) | 0.5525 (+2.39) | 0.5283 (+1.40) |
| `before_own_revision_turn` | 0.5080 (+0.23) | 0.5075 (+0.15) | 0.5273 (+1.35) |
| `other_revision_decision` | 0.5191 (+0.96) | 0.5149 (+0.67) | 0.5191 (+0.87) |
| `other_revision_value` | 0.5376 (+1.53) | 0.5426 (+1.76) | 0.5231 (+0.87) |
| `query_answer_decision` | 0.4989 (−0.12) | 0.5364 (+1.65) | 0.5166 (+0.89) |
| `query_answer_value` | 0.5570 (+2.46) | 0.5192 (+0.67) | 0.5268 (+1.24) |

All 165 separation scores lie between 0.4436 and 0.5570. The best margin
anywhere was 2.46 standard deviations, at the appended question's answer
position on the pilot, which across 165 tests is well inside what chance
produces. Nothing was labelled ROBUST because nothing cleared at all.

**The anchor reproduces the registered pipeline exactly.** The states at
the registered position were compared token for token against what
`localize_a3.residuals_at` produces, on every checkpoint and every layer,
and the largest difference was 0.0. The run was built to refuse to report
otherwise. So the comparisons here are on the same states the 2026-09-16
probes read.

### One observation with no cell attached

Across all 165 margins the mean is **+0.20 standard deviations** with 101
of 165 above zero, where pure noise would centre on zero. The tests are
badly non-independent — five layers read the same states, and positions
within a turn are adjacent — so this is much weaker than the arithmetic
suggests and no inference is drawn from it. It is recorded because it was
there.

## Why the positive control failed, which is a mistake in my own method

The method file pre-stated: at the model's own marker token, which agent
the model is has just been read off the input, so it should decode almost
perfectly, and if it does not, the read is broken.

**The premise was wrong, and it was wrong in a way that indicts far more
than this sweep.** The episode generator draws four marker words at
random for each episode and hands them to agents in index order. So the
marker belonging to `own_slot = 0` is a different word in nearly every
episode, and the marker token at the model's own turn says nothing
whatever about `own_slot`.

Measured directly on the 400 episodes this sweep used:

| quantity | what it should look like if `own_slot` were readable | what it is |
|---|---|---|
| marker words sharing `own_slot = 0` | one | **20** (across 53 episodes) |
| register index given `own_slot` | one value | near-uniform over all four |
| own-turn position patterns for `own_slot = 0` | few | **36 distinct** (across 53 episodes) |

Nothing the model can see is consistently tied to that index. `own_slot`
is a label that exists inside the generator and nowhere else.

### The diagnosis, run to check this rather than assert it

`src/probe_target_diagnostic_a3.py`, and it is **not pre-stated** — it
was written after seeing the sweep fail, which makes it worth less than a
measurement designed in advance, and it is labelled that way in the file
and here. It points the same read at three targets:

First, the scrambling, measured rather than argued. For every one of the
four values of `own_slot`, the number of distinct values of each
consistently defined quantity that share it:

| quantity | distinct values sharing one `own_slot` |
|---|---|
| `register_index` | **4 of 4** — every value, for every index |
| `marker_token` | **25 of 25** — every word, for every index |

`own_slot` is completely scrambled with respect to both. It picks out
nothing.

Held-out nearest-average accuracy on the pilot at the model's own marker
token, each against its own 50-draw permutation null. Majority-class rate
is 0.273 for the four-class targets and 0.060 for the marker word:

| target | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
| `register_index` — consistently defined | 0.330 (+2.93) | 0.320 (+2.79) | 0.295 (+1.87) | 0.303 (+2.02) | 0.303 (+1.93) |
| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |

**The read works, and on the pilot not marginally.** The marker word
sitting at that position decodes at 0.550 against a permutation null of
0.041 — a margin of **51.6 standard deviations**, against a
no-information value of 0.04 and a majority-class rate of 0.060. Capture,
position indexing and the difference-of-averages read are all sound. The
sweep's machinery was never the problem, and this is the positive control
the method file should have used.

**The target is unreadable.** `own_slot` clears nothing at any layer, at
the very position where the model's own marker word is in the input and
decoding at fifty standard deviations. The states carry the marker; the
marker carries no information about the index we have been asking for.

### Across all three checkpoints, which changes two of the claims above

How many of the five layers clear their null by three standard
deviations, at each position and target:

| position | target | pilot | seed 1 | seed 2 |
|---|---|---|---|---|
| own marker token | `marker_token` | **5/5** (acc 0.49–0.55) | 3/5 (acc 0.06–0.10) | **5/5** (acc 0.10–0.12) |
| own marker token | `register_index` | 0/5 (all above majority) | 0/5 (**none** above majority) | 0/5 (all above majority) |
| own marker token | `own_slot` | 0/5 | 0/5 | 0/5 |
| the anchor | `marker_token` | 0/5 | 0/5 | 0/5 |
| the anchor | `register_index` | 0/5 | 0/5 | 0/5 |
| the anchor | `own_slot` | 0/5 | 0/5 | 0/5 |

**The claim that survives, and it is the one that matters: `own_slot`
clears nothing in any of the thirty tests** — three checkpoints, two
positions, five layers — while the input token at the marker position
clears on all three checkpoints. The target is unreadable everywhere the
read is working.

**Two things I said on the pilot alone do not generalise, and are
corrected here rather than left standing.**

*The read is far weaker on seeds 1 and 2 than on the pilot.* The marker
word is the input token at that position on every checkpoint, yet the
pilot decodes it at 0.49–0.55 while seeds 1 and 2 manage only 0.06–0.12
against a majority-class rate of 0.060. It still clears its null on both
— comfortably on seed 2, at three of five layers on seed 1 — so the read
is working there, but the margin between "the token is legible" and
"nothing" is thin on seed 1 in a way it is not on the pilot. The three
checkpoints were trained identically apart from their seed, on the same
episodes, and this difference is unexplained. It is reported rather than
tidied away, and it means the positive control is strong evidence on the
pilot and weaker evidence on seed 1.

*The register index is a weaker candidate than the pilot suggested.* On
the pilot it sits above its null at all five layers (+2.93, +2.79, +1.87,
+2.02, +1.93) and above the majority-class rate at all five, and seed 2
repeats that pattern (+1.88 to +2.24, all above majority). **Seed 1 does
neither** — no layer above the majority-class rate. So the lift is not
consistent across checkpoints. Nothing clears the bar anywhere. It
remains the most plausible correctly posed target, because it is the only
own-agent quantity here that is both consistently defined and recoverable
from the input, but "obvious candidate" overstates what two of three
checkpoints support. It needs its own committed method and its own null.

### The well-posed version of the question, and its answer

The interesting target is the model's **own marker word read at the
registered anchor position**. The marker has not been emitted yet there —
it comes after the value — so a model that knows which agent it is would
have to be *carrying* it. Unlike the generator index, this target is
decodable in principle, which is exactly what makes a null meaningful.

On the pilot it reads 0.050, 0.045, 0.038, 0.053, 0.055 against a
majority-class rate of 0.060, at +1.02, +0.71, −0.10, +1.00 and +1.49
standard deviations. Nothing clears. At the same position `own_slot` and
`register_index` also sit at or below their nulls at every layer.

**This is underpowered and should not be leaned on.** Twenty-five marker
words across 400 episodes is about sixteen episodes per word, and a
difference of averages built from sixteen examples is weak. It is the
first well-posed null this stack has produced, and it is soft.

The diagnostic's own summary of the pilot: *the read works and the target
is wrong, with no obvious replacement* — the input token decodes, and
neither the generator's index nor the register index clears at either
position.

## Arm 2 — classifier against difference of averages

At the registered position, both instruments on identical states and one
shared set of folds. Margins in standard deviations of each instrument's
own null; no information is 0.25.

| checkpoint | layer | classifier | difference of averages | gap | cell |
|---|---|---|---|---|---|
| pilot | 3 | 0.2325 (−0.80) | 0.2625 (+0.58) | +1.38 | CLASSIFIER PENALISED |
| pilot | 4 | 0.2300 (−0.84) | 0.2275 (−0.84) | +0.00 | BOTH BELOW |
| pilot | 5 | 0.2100 (−1.67) | 0.2325 (−0.60) | +1.07 | BOTH BELOW |
| pilot | 7 | 0.2200 (−1.06) | 0.2400 (−0.35) | +0.71 | BOTH BELOW |
| pilot | 8 | 0.2175 (−1.25) | 0.2400 (−0.42) | +0.83 | BOTH BELOW |
| seed 1 | 3 | 0.2875 (+1.35) | 0.2850 (+1.42) | +0.07 | BOTH ABOVE |
| seed 1 | 4 | 0.2600 (+0.42) | 0.2375 (−0.46) | −0.88 | REVERSED |
| seed 1 | 5 | 0.2725 (+0.81) | 0.2650 (+0.54) | −0.27 | BOTH ABOVE |
| seed 1 | 7 | 0.2825 (+1.23) | 0.2775 (+1.03) | −0.20 | BOTH ABOVE |
| seed 1 | 8 | 0.2675 (+0.75) | 0.2550 (+0.20) | −0.55 | BOTH ABOVE |
| seed 2 | 3 | 0.2150 (−1.45) | 0.2700 (+0.98) | +2.43 | CLASSIFIER PENALISED |
| seed 2 | 4 | 0.2300 (−0.75) | 0.2375 (−0.50) | +0.25 | BOTH BELOW |
| seed 2 | 5 | 0.2275 (−0.89) | 0.2600 (+0.38) | +1.27 | CLASSIFIER PENALISED |
| seed 2 | 7 | 0.2225 (−0.96) | 0.2450 (−0.18) | +0.78 | BOTH BELOW |
| seed 2 | 8 | 0.2575 (+0.34) | 0.2575 (+0.34) | +0.00 | BOTH ABOVE |

Counts across the fifteen: **3 classifier penalised, 6 both below, 5 both
above, 1 reversed.** Median gap where the classifier is penalised: **1.38
standard deviations.** As pre-stated, neither instrument clears three
standard deviations anywhere — that was expected and is not the question
arm 2 asked.

**The answer to the pre-stated question, with the caveat that now
governs it.** The classifier does sit below its null where the difference
of averages sits above it, but only in 3 of 15 cases, and the pattern is
checkpoint-dependent rather than systematic: the pilot and seed 2 put the
classifier below its null at almost every layer, while seed 1 puts both
instruments above. Given the diagnosis above, all of this is two
instruments behaving on a target that carries no signal. **A gap between
them on noise is not a measure of relative sensitivity**, and this arm
cannot be read as one. It would have to be rerun against a well-posed
target to mean what it was designed to mean.

## A correction to `denoised-direction-findings.md`

That file reported that the five 2026-09-16 probes all sat below their
nulls while "all five nearest-average accuracies are above theirs", and
concluded that the below-null pattern "was a property of fitting a
regularised classifier to these states, not a property of the states
themselves".

**The column quoted there was the *denoised* read.** It was labelled as
such in the table, but the conclusion drawn from it went further than the
table supports. The plain difference-of-averages read — reproduced
exactly by arm 2 today, at 0.2625, 0.2275, 0.2325, 0.2400, 0.2400 — sits
**below** its null on four of the five pilot layers, the same side as the
classifier.

So what lifts that column above its null is the denoising step, not the
change of instrument. The sentence about the regularised classifier
should not be relied on. It is corrected here rather than edited there,
per the same rule that keeps the 2026-09-16 verdict intact: annotate,
never rewrite.

A second correction to the same file: its margins were quoted in standard
deviations of a 200-draw null, which cannot resolve beyond about one part
in two hundred. That caveat was never stated there. Every test in this
sweep reports how many shuffled draws met or beat the real score
alongside the margin, and that convention should be carried backwards
when those numbers are quoted.

## What this changes, and what it does not

**Does not change any registered result.** The blind arm's NOT FLAGGED
was a registered outcome read against registered criteria, and it stands
exactly as recorded. The 2026-09-16 not-testable verdict on the
unregistered positive control stands. The signed sensitivity rule stands.
Nothing here touches registered text and nothing here is a verdict.

**Does change what those nulls license.** The reading that the
localization stack is *insensitive*, and the competing reading that the
ownership signal is *absent*, were both inferences from probes that
predicted `own_slot`. If that quantity cannot be recovered in principle,
neither inference is supported by those runs. They are not evidence
either way. RT-12 named instrument failure as possibly outweighing the
headline; this is a third thing, and worse in one respect and better in
another — the instrument works, and it was aimed at a coordinate that
does not exist outside the generator.

**Does not show the model has no self-index.** It shows we have not yet
asked in a coordinate system the model could answer in. A model that
knows which agent it is would represent that as something like "the agent
whose marker is *this*", not as the generator's array index.

## What should happen next

1. **Settle the target before running anything else through this stack.**
   The candidates are the register index, which is consistently defined
   and already computed by the encoder, and the model's own marker word,
   which is the most direct statement of "which agent am I" the grammar
   affords. Each needs a committed method file and a real null. Neither
   is a safe bet: the register index lifts on two checkpoints of three
   and clears on none.
2. **Power.** Twenty-five marker words over 400 episodes is too thin. A
   well-posed marker-word test needs either far more episodes or a
   restricted marker pool.
3. **Explain the gap between checkpoints first.** The same input token at
   the same position and layers decodes at 0.55 on the pilot and 0.06 to
   0.12 on seeds 1 and 2. Until that is understood, any read of those two
   checkpoints rests on a positive control that barely holds, and a null
   on them means correspondingly less.
4. **Re-read what the earlier nulls are worth** once a well-posed target
   has been run. Until then they should be quoted as uninformative, not
   as null results.
5. Arm 2's question is still open and worth asking again against a target
   that carries signal.

None of this is a proposal to change a registered clause, and none of it
is urgent in the way the 2026-10-04 proposal is. It is the localization
stack's own foundation and it should be fixed before that stack is used
to argue anything.

## Record

- Outputs: `a3-gates/position_sweep_a3_a3_30m_seed0.json`, `…seed1.json`,
  `…seed2.json`, `a3-gates/position_sweep_a3_summary.json`, and
  `a3-gates/probe_target_diagnostic_a3_*.json`. Fresh files, nothing
  overwritten.
- Method committed before output: `position-sweep-method.md` (`af7232b`).
- Implementations: `src/position_sweep_a3.py` (pre-stated),
  `src/probe_target_diagnostic_a3.py` (**not** pre-stated, written after
  the failure).
- Runtime about 18 minutes per checkpoint for the sweep. No spend.
- Gated on the known-answer test, which passes. Not gated on the
  threshold lock, and the method file says why.
