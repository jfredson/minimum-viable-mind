# The scoring trial: findings

*Written 2026-11-21 by the session that wrote the trial and ran it. The trial is set out in section 15 of
`battery-authoring-spec.md`, and its price in `scoring-trial-priced-proposal-2026-11-21.md`. The raw results
are in `scoring-trial-run-2026-11-21/`. These findings are owed a check by a session that did not write them.*

## In short

**The answer-only instruction fixes the scoring for the paired questions, but not for the chained lookups.**
In either place, the instruction lifts the paired everyday questions (the routine twins) from about 51% to
about 84% at three passes. It also roughly doubles the share of items that pass the confidence filter. Two of
section 15's three criteria are met. The third is not: the chained lookups stay at or below chance at every
number of passes, in every version, and not one chained item passes the confidence filter.

So by section 15's own rule, neither placement counts as a working fix, and the next choice goes to John. The
chained lookups look like the problem now, more than the scoring method.

## The run and its cost

| | |
|---|---|
| John's go | "Go, up to $5" (2026-11-21) |
| Machine | One RTX PRO 6000 Blackwell Server Edition (96 GB), RunPod secure cloud, $2.69 an hour, pod `foxsrxnhgmi1xo`. No community-cloud card was free |
| Created, deleted | 22:54:45 UTC and 23:07:27 UTC, 2026-11-21, so 13 minutes. Deleted by hand once the results were copied back. RunPod's own shut-off was set for 00:39 UTC |
| Cost | **$0.56**, from the balance: $55.40 before and $54.84 after (`runpodctl me`). That matches 13 minutes at $2.69 an hour |
| Within the ceiling | Yes. The ceiling was $5, and the estimate was about $1.80. The run was quicker than step 4a because the setup went cleanly |
| Software | As in step 4a: PyTorch 2.9.1, transformers 5.24.0.dev0 from commit 046bdb8, accelerate 1.16.0, at 16-bit |

**A check on the run itself.** The unchanged pilot set gave exactly the same accuracy figures as step 4a's
full run, kind for kind and pass for pass. So the trial script reproduces step 4a, and the two runs can be
compared directly.

## The figures

All are descriptive figures on the practice items. Chance is 20%. "Prompt-rule items" are the questions that
need the rule stated in the question. "Routine twins" are their partners, which can be answered from
everyday knowledge. The chained lookups follow a list of invented names to a colour.

**Accuracy at three passes, and the confidence filter**

| Set | Prompt-rule items | Routine twins | Chains of 4 to 6 steps | Items passing the confidence filter |
|---|---|---|---|---|
| No instruction (the pilot) | 34% | 51% | 17% | 24% |
| Instruction at the end | 72% | **83%** | 8% | **56%** |
| Instruction at the start | 66% | **84%** | 25% | **54%** |

**Section 15's criteria** (stated before the run)

| Criterion | No instruction | At the end | At the start |
|---|---|---|---|
| Routine twins at least 80% at three passes | No | **Yes** | **Yes** |
| At least half of items pass the confidence filter | No | **Yes** | **Yes** |
| Chains of 4 to 6 steps at least 50% at three passes | No | No | No |

**Accuracy by number of passes**

| Set | Passes | Prompt-rule | Routine twins | Chains of 4 to 6 steps |
|---|---|---|---|---|
| No instruction | 1 / 2 / 3 | 27% / 22% / 34% | 54% / 48% / 51% | 29% / 13% / 17% |
| At the end | 1 / 2 / 3 | 53% / 62% / 72% | 68% / 78% / 83% | 38% / 17% / 8% |
| At the start | 1 / 2 / 3 | 53% / 50% / 66% | 75% / 79% / 84% | 29% / 4% / 25% |

## What stands out

1. **The instruction works for the paired questions.** With it, more passes give better answers on both
   kinds of question, which is what a working loop should show. Without it, the figures barely move with
   the number of passes. The two placements give much the same result.
2. **Some kinds are still weak with the instruction.** At three passes, with the instruction at the end:
   - the letter-code rule is right on 19% of prompt-rule items, which is chance;
   - sums are right on 56% to 62%, and everyday colours on 50% to 78%;
   - capitals, opposites, the lookup rule and the unit rule are at 75% to 100%.

   Each kind has only 6 to 16 items, so these figures are rough.
3. **The chained lookups fail in every version.** Even chains of two steps are at chance or below. No chained
   item, at any length, passes the confidence filter. With only 8 items per chain length, the single figures
   are noisy, but the pattern is the same everywhere. More passes do not help, and with the instruction at
   the end, three passes do worse than one.
4. **So the bites check still cannot be met,** and the reason is now the chained lookups themselves. The
   check needs three passes to beat one pass by at least 0.15 on chains of four or more steps (design,
   section 5). That cannot happen while three passes are at chance. The likeliest explanation is that following a
   list of 20 or more invented names through several steps is too hard to answer at once, with no written
   reasoning, for a model of this size. This is a hypothesis, not a measurement. The task looks to be the
   problem rather than the scoring, since the same scoring now works on the paired questions.

## What John is asked to decide

Nothing more is spent until he rules. The answer-only instruction meets two of the three criteria. The
choice is about the third:

1. **Keep the instruction, and change the bites check's task.** For example, use shorter lists, so the model
   tracks fewer invented names. Another option is a kind of multi-step question the model can already answer
   at three passes. This would be a change to the design and to the task specification, with its own review
   and a short priced run.
2. **Try option (b), a fixed lead-in such as "The answer is",** on top of the instruction, to see if the
   chains improve. Nothing here suggests they would, because the paired questions already work.
3. **Option (c), let the model reason in writing.** This drops choice 2, and with it the claim that the test
   reads one moment.

Whether 16-bit is accepted as the working precision (the step-4a findings, item 2) is still open.

## Record

- **Spending.** The spending record's rows for this trial carry the cost.
- **The script.** `src/scoring_trial.py`, as committed at 8c9dcd0, is the version that ran, unchanged.
- **Owed.** These findings, and the step-4a findings, are owed an independent check. RT-345 stays open.
