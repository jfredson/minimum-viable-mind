# The split removal test: what the rehearsal's first phase found

*Written 2026-10-24 (Saturday, Pacific). The method was committed before the run (`experiments/09-split-removal-test/rehearsal-method.md`, commit 5632e5d), and the numbers are in `rehearsal/phase1-2026-10-24.json`. The run used pilot items only, on `google/gemma-2-2b-it` on this Mac, and cost $0.*

## In one paragraph

Both removal methods fail the design's removal check on this model, and both also fail its normal-range check. The information that marks a sentence as the model's own rather than the user's was located cleanly. The sentence's last word alone could not tell the two apart (accuracy 0.50, which is chance), but the model's internal activity a few layers in told them apart perfectly. Removing the 16 located directions at five layers did not erase that information:
- A probe trained on the model's activity after the removal still told the model's own sentences from the user's with accuracy 0.95 to 1.00 at every layer from 10 onward.
- The model still answered "which of these words did you say?" correctly 93% of the time, against 97% with nothing removed. The design requires a fall to at most half.

At the same time, the removal disturbed the model's handling of ordinary text far more than random removals of the same size did. Under the design (section 8, step 3), a failed removal check sends the design back to John before any registration. Phase 2 has not run. Separately, the baseline checks found that only one of the four kinds of prompt-rule problem is answered reliably by this model, so the design's "at least three kinds" cannot be met here as the items stand.

## The numbers

**Locating** (step 2). The fit used 144 items and the held-out set 96. Layer-0 check: accuracy 0.50, shuffled-label accuracy 0.50, a margin of 0.00, so it passes. Below, the fit margin is the accuracy above the shuffled-label baseline on the fitting items. A margin near 0.50 means near-perfect reading.

| Layer | 8 | 11 | 14 | 18 | 22 |
|---|---|---|---|---|---|
| Fit margin | 0.51 | 0.49 | 0.50 | 0.53 | 0.52 |

**The removal check, probe test** (step 4). These are the highest accuracies of the linear and nonlinear probes on the held-out items. The design's limit is 0.55 at every layer from 8 to 25. Shuffled-label accuracy sits near 0.47 throughout.

| Layer | Nothing removed | Mean-ablation | Projection |
|---|---|---|---|
| 8 (removal applied) | 0.96 | 0.71 | 0.71 |
| 9 | 1.00 | 0.85 | 0.84 |
| 10 | 1.00 | 0.98 | 0.97 |
| 13 | 1.00 | 1.00 | 1.00 |
| 18 (removal applied) | 1.00 | 1.00 | 0.98 |
| 25 (last) | 1.00 | 1.00 | 0.95 |
| Highest, layers 8 to 25 | 1.00 | 1.00 | 1.00 |

**The removal check, task test.** Accuracy on the 60 which-did-you-say items: 0.967 with nothing removed, 0.933 under mean-ablation and 0.933 under projection. Passing needs 0.483 or lower. Both methods fail.

**The normal-range check** (step 5) and the damage (step 6), on 200 neutral passages. "Rise" is the increase in the model's surprise at ordinary text, in nats per word. The bound is the 95th percentile of 20 random removals the same size.

| | Mean-ablation | Projection |
|---|---|---|
| Bound (95th percentile of 20 random) | 0.144 | 0.200 |
| The split removal's rise | 0.920 | 1.007 |
| Room under the bound | −0.776 | −0.806 |
| Split's damage (divergence of predictions) | 0.645 | 0.857 |
| Median damage of the random removals | 0.069 | 0.088 |
| Split's damage as a multiple of random | 9.4 | 9.7 |

**Baseline checks** (step 1). Every routine item passes, on greedy and on at least 9 of 10 samples. Only one of the four prompt-rule kinds survives on this model:

| Kind | Candidates | Right, greedy | Kept (right greedy and at least 9 of 10 samples) | Right without the rule (chance) |
|---|---|---|---|---|
| Invented operator | 114 | 0.92 | 90 | 0.00 (0.00); the plain sum in 9% of replies |
| Letter code | 120 | 0.13 | 1 | 0.00 (0.00) |
| Two rules on a list | 120 | 0.24 | 2 | 0.11 (0.20) |
| Next token on a ring | 120 | 0.08 | 0 | 0.17 (0.17) |
| Routine, all six kinds | 145 | 1.00 | 145 | — |

All four prompt-rule kinds pass the check that the rule is needed, so none is dropped by that rule. After matching on pass rate, each cell keeps 80 items, above the 40-item floor. **But the prompt-rule cell is then almost entirely one kind, the invented operator** (at most 3 of its 80 items come from any other kind). The design requires at least three kinds, each read separately and each left out in turn (section 4). On this model that requirement cannot be met with these items. The other three kinds are too hard for a 2-billion-parameter model to answer reliably. The reason is not the scorer: replies that are right are scored right. On the two list kinds, 21 of 120 replies in each ran out of room before their "Answer:" line, but that does not explain accuracies of 0.08 and 0.24. This is a second finding for John, separate from the removal check: on the bench model, the prompt-rule items need easier kinds before the cell can carry three.

## What this says, and what it does not

**It is a fact about the instrument, not about the theory.** The removal did not erase what it was meant to erase, so no outcome in section 5 of the design can be read. Under the design's own words, that result is "not testable: the information was not removed", for both methods. Nothing here counts for or against the theory's prediction.

**The information is rebuilt, not just missed.** At layer 8, where the removal is first applied, the probes fall from 0.96 to 0.71. Two layers later they are back at 0.97 or more. The design warned of this (section 2): on the 8-billion-parameter model, the July record showed the signal fully readable by layer 3, so later layers can rebuild it from the role headers that are still in the input. That is what happens here. A removal of 16 directions at five layers is too narrow for information the model can recompute at every layer from the turn markers.

**The removal is also not clean.** It moves the model's predictions on ordinary text nine to ten times as much as a random removal of the same size. So even if it had erased the information, it could not have passed the normal-range check as the design defines it. Matching comparisons on damage (section 3) would then have needed random removals far larger than the split's.

**The two failures point the same way.** The located directions carry much more than the own-or-user mark, which is why removing them does harm. Yet they do not carry all of the mark, which is why the model still knows who spoke.

## What could be done next (for John to choose; nothing is started)

1. **Remove the information at the source.** The design could remove it at every layer, or at the earliest layers before it spreads. Either is a design change. Experiment 01's record suggests the signal sits on the turn markers themselves, so this may amount to removing the headers, which the template conditions already test from the input side.
2. **Change the target from "erase" to "scramble".** The model's own and the user's internal activity could be swapped (patched) at the located directions, instead of being erased. Activity would then stay in its normal range by construction. That is a new method with no record on this pipeline, and it needs its own review.
3. **Accept that the candidate cannot be removed in this model with these tools,** and record that as the instrument's result. This is not a result against the theory's prediction.

Any of these goes back through the design's review (an inside pass at the advisory gate) before a registration.
