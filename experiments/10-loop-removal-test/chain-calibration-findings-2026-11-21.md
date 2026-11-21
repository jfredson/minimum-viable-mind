# The chained-lookup calibration trial: findings

*Written 2026-11-21 by the session that wrote the trial and ran it. The trial is set out in section 16 of
`battery-authoring-spec.md`, and its price in `chain-calibration-priced-proposal-2026-11-21.md`. The raw
results are in `chain-calibration-run-2026-11-21/`. These findings are owed a check by a session that did
not write them.*

## In short

**No version qualifies. Even the easiest lookup puzzle is at chance.** That puzzle has eleven rows, familiar
one-word names, and only two steps to follow. Answered at once with no written reasoning, the model gets it
right about as often as guessing, at one pass and at three. Across all four versions and 320 puzzles, 6 are
answered right with enough confidence to pass the confidence filter.

So by section 16's own rule, no version is chosen, and the next choice goes to John. Making the puzzle
easier was not enough. The findings point away from the lookup puzzle as the bites check's task altogether
(see "What John is asked to decide").

## The run and its cost

| | |
|---|---|
| John's go | "Go, up to $3" (2026-11-21) |
| Machine | One RTX PRO 6000 Blackwell Server Edition, RunPod secure cloud, $2.69 an hour, pod `bv7fg322jpjvui`. No community-cloud card was free |
| Created, deleted | 23:14:51 and 23:21:10 UTC, 2026-11-21, so 6 minutes 19 seconds. The trial itself ran from 23:18:53 to 23:20:55 |
| Cost | **About $0.28** from the time (6 minutes 19 seconds at $2.69 an hour). The balance fell only $0.10 at first reading ($54.82 to $54.72, `runpodctl me`), probably because RunPod had not yet billed the last minutes. The spending record carries the time-based figure until the balance settles |
| Within the ceiling | Yes. The ceiling was $3, and the estimate about $0.70 |

## The figures

Accuracy at three passes, by the number of steps to follow. Chance is 20%. There are 16 puzzles in each
cell, so one puzzle moves a figure by about 6 points.

| Version | 2 steps | 3 | 4 | 5 | 6 | Chains of 4 to 6 steps: 1 pass, then 3 passes |
|---|---|---|---|---|---|---|
| 1. Invented names, full distractor chains (current) | 13% | 19% | 44% | 31% | 38% | 21%, then 38% |
| 2. Invented names, one-step distractors | 19% | 25% | 13% | 13% | 31% | 19%, then 19% |
| 3. One-word names, full distractor chains | 6% | 6% | 31% | 13% | 19% | 23%, then 21% |
| 4. One-word names, one-step distractors | 25% | 31% | 19% | 25% | 6% | 13%, then 17% |

**Against section 16's rule.** To qualify, a version needed at least 50% at three passes on chains of four to
six steps, and three passes beating one pass by at least 0.15. Version 1 beat one pass by 0.17, but reached
only 38%. The others reached at most 21%, and none gained more than 0.04 from the extra passes. None
qualifies.

## What stands out

1. **Easier puzzles did not help.** Shorter lists and familiar names made no measurable difference. The
   easiest version, with only eleven rows, is no better than the current one. With 16 puzzles in each cell,
   the scatter between lengths (6% to 44%) is about what guessing would give.
2. **Even two steps fail.** Every version is at or below chance on two-step chains.
3. **One step works.** The scoring trial's "lookup" rule kind asks the model to read one name's colour from a
   table, a one-step lookup. With the answer-only instruction it was right on 100% of items at three passes.
   So the model can read a colour out of a list and give it as its first word. What it cannot do, answering at
   once, is compose two lookups.
4. **What this suggests.** At its size, this model may not follow even two linked lookups inside its own
   computation, at any number of passes, unless it writes them out. This is a hypothesis, not a measurement.
   It agrees with step 4a, where the model always chose to start by writing reasoning. It does not tell us
   whether the loop's message carries anything. It only says that this task cannot show it.
5. **The current version's gain is weak evidence.** Version 1's three passes beat one by 0.17 on chains of
   four to six steps. But it scored 13% to 19% on the easier two- and three-step chains, and in the scoring
   trial the same task gained nothing. With 48 puzzles, 0.17 is about 8 puzzles, within what chance gives.

## What John is asked to decide

Nothing more is spent until he rules. Each choice would change the design and go through a review.

1. **Use a different task for the bites check, one the model already does better with more passes.** The
   scoring trial offers one. With the answer-only instruction, the prompt-rule items rose from 53% at one pass
   to 72% at three, and from 53% to 66% with the instruction at the start. These are the invented-rule
   problems, such as "a ⊛ b means a plus 2 times b". A separate set of such problems, kept out of the
   outcome, could serve as the task "known to need the loop". This would rest the check on a measured gain,
   not on the task the model card names. The pilot gain is 0.13 to 0.19 against the check's 0.15, so it would
   need a larger set to measure reliably. I recommend this.
2. **Allow written reasoning for the lookup puzzles only.** The bites check could then use the task the
   design names. But the check would measure something the main test does not: the main test still reads
   one moment.
3. **Accept that this model cannot show the loop biting, and stop the test** before the registered run. The
   paper work stands, and nothing more is spent.

Whether 16-bit is accepted as the working precision is still open.

## Record

- **Spending.** The spending record's rows for this trial carry the cost.
- **The script.** `src/chain_calibration.py` as committed at 0e71408 is the version that ran, unchanged.
- **Owed.** These findings, and those of step 4a and the scoring trial, are owed an independent check.
  RT-345 stays open.
