# The loop removal test, step 4b: findings

*Written 2026-11-23 by the session that wrote the step-4b code and ran it. The raw results are in
`step4b-run-2026-11-23/`:
- `collect-summary.json` and `items.jsonl`, from the rented card;
- `step4b-analysis.json`, from the Mac;
- `quick/`, the ten-item try;
- `run-log.txt`.

The code is at commits 4c7cbaf (collection and analysis) and 1237fd4 (simulation, committed before the
results were opened). These findings are owed a check by a session that did not write them.*

## In short

**One long-open question is answered, and two of the design's return-to-John conditions fired.**

1. **The dose question (RT-345) is answered on the real model: the two kinds of question get swaps of the
   same size.** Across all pilot pairs, the routine cell's mean swap size divided by the prompt-rule cell's is
   1.004 to 1.007 under the swap, and 0.999 to 1.000 under the average, in every rule kind. The design's limit
   is 10%. This finding has been open since the first review. The design's formal closure reads the sizes
   after the baseline filters and asks for a session that did not write the construction, so it waits on
   point 2.
2. **Every pairing fails the baseline checks for interference** (return to John). No pair survives, so the
   test cannot go on as written. Most of the strikes come from a threshold set in nats of margin, while the
   model's margins here run near 10. In many struck pairings the routine answers stay 100% right.
3. **The normal-range check cannot be read as designed** (return to John). In the chat format, the model
   predicts the user's own text almost at random. So damage and perplexity on prose placed in the user's
   turn measure changes in noise, not in the model's real predictions.

The rest passed:
- the code checks were exact;
- the swap and the average stayed within a factor of two;
- every comparison was matched on damage;
- the bites check's pooled one-pass condition passed, just;
- the change ratio was well above 0.5 under both methods.

## The run and its cost

| | |
|---|---|
| John's go | "Go, up to $20" (2026-11-23) |
| Machine | One RTX PRO 6000 Blackwell Server Edition, RunPod secure cloud, $2.69 an hour, pod `u0sk3t5ioug90x`. No community-cloud card was free |
| Created, deleted | 00:16:46 and 00:59:46 UTC on 2026-11-24 (2026-11-23 Pacific), so 43 minutes |
| Cost | **About $1.93** from the time. The balance fell $1.81 at first reading ($54.06 to $52.25), which is probably the last minutes not yet billed |
| Within the ceiling | Yes. The ceiling was $20 and the estimate about $7. The run went faster than estimated: the full collection took 35 minutes, and batching the draws worked well |
| Software | PyTorch 2.9.1, transformers 5.24.0.dev0 from commit 046bdb8, at 16-bit (choice 7); peak memory 70.8 GB |

**The quick try** ran every phase on 10 pairs, 10 bites items and 20 prose passages in under 4 minutes,
with no error. No code was changed after it. It also prompted a one-minute diagnostic, `diag.py`, whose
output is in the run log (finding 3).

## What each measurement found

### The code checks: exact

On 20 items:
- the noise floor is 0.0;
- the identity check gives 0.0;
- the bypass check gives 0.0.

The block sums the readers receive hold one loop block sum and the running state, each 2,304 wide.

### The dose question (RT-345): the swap sizes are equal

These are the means over all pilot pairs, before any filter. A scored pair with no donor (A-0060) is left
out of the swap figure.

| Rule kind | Swap: routine cell / prompt-rule cell | Average: routine cell / prompt-rule cell |
|---|---|---|
| operator | 1.007 | 0.999 |
| unit | 1.005 | 0.999 |
| lookup | 1.004 | 1.000 |

The design feared, from the first review on, that the routine twins would get a different dose of swap
from the prompt-rule items. On the real model they do not. The shared-context construction does on the
model what the free checks showed on paper. The swap changes the same amount of message in both cells,
measured in the model's own normalised block sums.

### The baseline checks: every pairing is struck (returns to John)

**The rule is needed.** It passes for every kind. Without the rule sentence, accuracy is 21% for lookup,
18% for operator and 14% for unit. Chance is 20%, and the limit is 30%.

**The confidence check.** Both twins need a margin of at least 2.2 to pass:
- every lookup pair passes;
- 33 of 40 unit pairs pass;
- only 9 of 40 operator pairs pass.

The operator kind is weak, as the scoring trial warned.

**The two interference checks.** Each asks that an item's margin in the full shared context be "no more
than 1.0 below" its margin with the other half of the context left out. The table gives medians over each
pairing's pairs:

| Pairing | Routine margin: full / bare | Routine right: full / bare | Prompt-rule margin: full / bare | Struck by |
|---|---|---|---|---|
| lookup + products | 9.4 / 12.2 | 100% / 100% | 10.3 / 10.7 | routine (14 of 20 fail) |
| lookup + sums | 9.5 / 10.4 | 100% / 100% | 10.2 / 12.1 | both (10 and 11 of 20) |
| operator + capitals | 9.2 / 12.8 | 100% / 100% | 0.2 / 2.6 | routine (5 of 5 confident) |
| operator + colours | 0.4 / 5.1 | 54% / 93% | 1.0 / 2.6 | too few confident (2) |
| operator + opposites | 7.2 / 7.1 | 69% / 69% | 0.0 / 1.0 | too few confident (2) |
| unit + capitals | 10.2 / 12.5 | 100% / 100% | 8.0 / 7.7 | routine (12 of 14) |
| unit + colours | 6.1 / 6.5 | 85% / 100% | 6.7 / 10.4 | mirror (8 of 10) |
| unit + opposites | 7.3 / 9.3 | 100% / 92% | 3.9 / 7.6 | both (7 and 7 of 9) |

**What this shows.**
- **Most strikes are the threshold, not interference.** The "1.0 below" limit was written when margins
  were expected near the confidence bar of 2.2. With the answer-only instruction, the model's margins run
  near 10. A routine twin that drops from a margin of 12 to one of 9 is still right every time, but it
  fails the check. In five of the eight pairings, the routine answers are right on every item, with the
  rule or without it.
- **Some interference is real.** Behind the operator rule, everyday colours drop from 93% right to 54%.
  Unit and colours also show a real drop in the prompt-rule margin, from 10.4 to 6.7, and in routine
  accuracy, from 100% to 85%.
- **The operator kind's prompt-rule items are barely confident.** Their median margins are 0.0 to 1.0, so
  the operator kind would fail the confidence check whatever the interference rule said.

**The return-to-John rule fired.** The checks leave no rule kind with two routine kinds. So no pair
reaches margin matching, swap-size matching or the simulation. Those steps have no input, and the
simulation was not run.

### The normal-range check cannot be read (returns to John)

The diagnostic took one prose passage:
- **In the chat format, as the user's message,** the model's mean loss per token was 8.7 nats. Its top
  guesses were tokens such as "$", "{" and "\\".
- **The same passage as plain text, with no chat format,** gave 2.3 nats.

So the model's predictions on user text in the chat format are close to noise. On the 100 measure passages
the baseline perplexity was about 1,870 (corrected 2026-11-23 from "about 2,600", which was the quick try's figure; RT-497). Random noise in the loop moved that perplexity by hundreds in
either direction. The average and the fallback both lowered it. The bound came out negative: −14 for the
swap and −24 for the average.

The design measures damage and perplexity on prose placed where the items' text sits, in the user's turn.
That keeps the average comparable with the items, but it measures movement in predictions the model never
makes well. **The damage matching and the normal-range check are therefore not informative as designed.**
For the record:
- the swap's perplexity rise was +945, and the average's −409;
- noise outside the loop failed the bound under both methods;
- in-loop noise "passed" by lowering perplexity.

None of these figures can be read.

A likely fix, for John and a review: keep the user-turn passages for building the average, which is where
the items' text sits. Measure damage and perplexity on the same prose placed as the model's own reply, where
its predictions are trained. It is a design change.

### Damage matching and the factor-of-two rule

Measured as designed:
- **The swap against the average.** Their damages on the prose differ by a factor of 1.85 (swap 1.13,
  average 0.61). That is within the factor of two, so the average stands and the fallback is not needed.
- **The comparisons.** All four were matched within 20%:
  - in-loop noise for the swap: 0.93 against 1.13, which is 18% short, at a factor of 987;
  - in-loop noise for the average: at a factor of 3.9;
  - outside the loop: at factors of 0.70 and 0.57.
- **What the swap's factor shows.** In-loop noise of the swap's own size does little damage. Noise about a
  thousand times larger was needed to match the swap, and even then it came out 18% short, which suggests
  the damage is near its ceiling. The swap's damage is far from what random change of the same size would
  do, as the split removal test also found.

Since these damages were measured on near-noise predictions (finding 3), they are reported as measured and
are to be measured again once that is fixed.

### The bites check's one-pass condition: passes, just

These are normalised costs of dropping to one pass, on the 80 bites items. Intervals are resampled by fact
in the unit kind.

| | Cost | 95% interval | Lower end at least 0.15? |
|---|---|---|---|
| pooled | 0.27 | 0.150 to 0.39 | **yes, by 0.0003** |
| operator | 0.28 | 0.09 to 0.47 | no |
| unit | 0.25 | 0.11 to 0.42 | no |

The design gates every outcome on the pooled figure, so the condition passes, but only just.

*Correction, 2026-11-23, after the closure check of design version 0.13 (RT-492, the bites condition's
seed).* "Passes, just" was too strong. The interval above came from one resampling seed. Rerun with seeds 1
to 20, its lower end reaches 0.15 for only 9 of the 20. On the pilot the condition is a coin flip, not a
pass, and the table's "yes" should be read that way. The cost is
smaller than the scoring trial's figure of about 0.4. That trial used the old unit range, which was easier,
and only 30 items a kind. At the test half's 100 items a kind, the interval would be narrower.

### The change ratio: well above 0.5

On the bites items, the swap's mean change ratio is 0.71 (spread 0.04, lowest 0.55), and the average's is
0.67. Both clear the 0.5 that outcome F needs. **F can be reached.**

### Ties

5 of 320 items had an exact tie at the top in the unaltered run. The tie rule counted them as shares.

## Which return-to-John conditions fired

| Condition | Fired? |
|---|---|
| The identity or bypass check fails, or the noise floor is above 0.01 | No |
| Fewer than three rule kinds survive, or a rule kind is left with one routine kind or none | **Yes**: every pairing struck |
| Margin matching removes more than a third of a rule kind | Not reached |
| Swap-size matching needs more than a tenth of a rule kind | Not reached after filtering. Before filtering the sizes differ by under 1% |
| The average and its fallback both differ from the swap by more than a factor of two | No (1.85 and 1.88) |
| A comparison cannot be matched within 20% on damage | No, but see finding 3 |
| The main removal or a comparison fails the normal-range check | **Yes**, but the check cannot be read (finding 3) |
| The bites check's one-pass condition fails | No, just |
| The change ratio is below 0.5 under either method | No |

## What John is asked to decide

Nothing more is spent until he rules. Each fix is a design change with its own review.

1. **The interference checks' threshold.** The fixed limit of 1.0 in margin is too strict when margins run
   near 10. The options:
   - (a) a relative limit, for example a margin may not fall by more than a fifth;
   - (b) judge interference by accuracy, so that an item counts as interfered with only if it is wrong in
     the full context and right without the other half;
   - (c) keep a limit in margin, but only for items close to the confidence bar.

   The real interference the pilot shows, everyday colours behind the operator rule, would be caught by
   each of these.
2. **Where damage and perplexity are measured.** Keep the user-turn prose for building the average, and
   measure damage and perplexity on the same prose as the model's own reply.
3. **The operator kind.** Only 9 of its 40 pairs are confident, and its prompt-rule margins sit near 0.
   Even with a fixed interference check, it is unlikely to keep two routine kinds. The options:
   - accept that it falls, which leaves two rule kinds, below the design's minimum of three;
   - replace it with another invented-rule kind the model answers confidently;
   - lower its difficulty, for example to single-step rules.

   The minimum of three rule kinds is the design's own rule, so this needs a ruling.

The swap-dose result (point 1 of "In short") stands whatever is decided. It is the main thing step 4b has
settled.

## Record

- **Spending.** The spending record's rows for step 4b carry the cost.
- **The code.** It ran unchanged from the committed versions. The diagnostic script is in the run log's
  section, not in `src/`, because it was a one-off check.
- **Owed.** These findings are owed an independent check, as are those of step 4a, the scoring trial and the
  lookup calibration trial. The simulation waits until pairs survive the baseline checks.
