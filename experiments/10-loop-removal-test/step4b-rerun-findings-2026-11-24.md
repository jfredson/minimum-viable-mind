# The loop removal test, the step-4b rerun: findings

*Written 2026-11-24 by the session that wrote the rerun's code and ran it. It is the measurement rehearsal again,
on the pilot rebuilt for design version 0.14 (`batteries/pilot-v0.14/`), analysed by margin under design
version 0.16 and specification sections 19 and 20. The raw results, analysis and simulation are in
`step4b-rerun-2026-11-24/`. These findings are owed a check by a session that did not write them.*

## In short

**The dose question is answered, and the test as designed cannot be read on this model.** The machinery is
exact. The two kinds of question get swaps of the same size. Several checks that previously failed now pass:
- the reply rendering;
- the unit C;
- the bites gate;
- the change ratio;
- the factor of two between the swap and the average.

But five of the design's return-to-John conditions fired. Three of them come from the same root: **a wrong
message does far more harm than random change of the same size, and more than having no message at all.**

1. **The in-loop random comparisons cannot be matched.** Random noise inside the loop stops doing more
   damage at about 0.88, even at 56,000 to 93,000 times the swap's size. The swap's damage is 1.74, and the
   average's 3.29.
2. **The removals fall far outside the normal range.** On the prose, the swap raises perplexity by 32.7 and
   the average by 161. The bound from random noise of the same size is 0.37 and 0.20.
3. **There is too little room.** The swap already costs the rule questions 11.7 nats of margin, 2.5 times what
   dropping to one pass costs. So the cell's mean room for an extra, selective loss is 0.72 C under the swap,
   and 0.55 C under the average. The target gap is 1.0 C, and with room capped the simulation never reads
   outcome A.

Two further conditions fired:

4. **The simplified operator kind still fails.** Only 5 of its 40 pairs are confident. All three of its
   pairings are struck, so two rule kinds survive, below the minimum of three. It also gains almost nothing
   from the extra passes: 0.56 nats, against 5.84 for the unit kind.
5. **The two averages differ by a factor of 5.3.** On the prose as the model's reply, the user-built average
   does damage of 3.29, and the reply-built one 0.62.

## The run and its cost

| | |
|---|---|
| John's go | "Go, up to $10" (2026-11-24) |
| Machine | One RTX PRO 6000 Blackwell Server Edition, RunPod secure cloud, $2.69 an hour, pod `tnkqyhw5g8117e`. No community-cloud card was free |
| Created, deleted | 17:58:20 and 18:54:41 UTC, 2026-11-24, so 56 minutes. The quick try took 7 minutes, the full collection 45 |
| Cost | **About $2.53** from the time. The balance fell $2.43 at first reading ($51.96 to $49.54) |
| Within the ceiling | Yes. The ceiling was $10, and the estimate about $3 |
| Code | Ran unchanged from the committed versions. No fix was needed after the quick try |

## What passed

- **The code checks.** The noise floor, the identity check and the bypass check all came out at 0.0.
- **The dose question (RT-345), after the filters.** After the baseline checks and margin matching, the
  routine cell's mean swap size divided by the prompt-rule cell's is:

  | Rule kind | Under the swap | Under the average | Pairs dropped |
  |---|---|---|---|
  | lookup | 1.004 | 1.000 | 0 |
  | unit | 1.004 | 0.998 | 0 |

  Every ratio is within 10%, as the design asks, with no pairs dropped. The design's formal closure asks for
  a session that did not write the construction to read these figures; this is the author's reading.
- **The 1-nat check.** On the prose as the model's reply, the loss is 2.38 nats per token. As plain text it is
  2.36, and in the user's turn 7.66. The reply rendering works as intended.
- **The unit C.** C is 4.64 nats, with a 95% interval of 4.07 to 5.25, so it passes its check.
- **The bites gate in margin.** The bites set's pooled one-pass cost is 4.11 nats, with an interval of 3.43 to
  4.72, against C/4 of 1.16. The branch choice picks **unit alone**, which meets all three targets in 100% of
  resampled sets. Both kinds together fail on "does not bite" (6%).
- **The change ratio** is 0.69 under the swap and 0.67 under the average, both above 0.5.
- **Swap against average.** Their damages differ by a factor of 1.89, within two.
- **Baseline checks for lookup and unit.** All five of these pairings survive the accuracy-based interference
  rule. 39 lookup pairs and 31 unit pairs remain, before margin matching drops 12.

## What fired, and what it means

**Root: a wrong message is worse than none.** The rerun measured the swap's margin loss against the cost of
dropping to one pass:

| | Swap's margin loss | One pass's margin loss | Ratio |
|---|---|---|---|
| Prompt-rule items | 11.65 nats | 4.64 nats | 2.51 |
| Routine twins | 10.03 nats | 5.43 nats | 1.85 |

Dropping to one pass removes the message and the extra passes together. Giving the model another input's
message is much worse than that, for both kinds of question. Random noise of any size in the same place
cannot do this much harm, because the readers normalise what they read. That is why the in-loop comparison
reaches a ceiling, and why same-size noise sets a normal-range bound the removals far exceed.

The design rests on three things, and this finding breaks all three:
- a random comparison matched on damage;
- a removal that stays within the normal range;
- room for a selective loss on top of the removal.

The design cannot be repaired by tuning, because none of the three is a threshold that is set wrong. It needs
a different kind of comparison, or a gentler removal.

**This is a finding about the model.** In this looped model, the message between passes carries information
specific to its input. A message built from another input actively misleads the next pass. It does not merely
withhold help. The split removal test found a related pattern, a structured removal far more damaging than
same-size noise. Here the gap is wider still.

**The simplified operator kind.** It is not confident enough (5 of 40 pairs) and gains too little from the
extra passes (0.56 nats). John's ruling to simplify it did not rescue it on this model.

**The two averages.** The user-built average does five times the damage of the reply-built one on the reply
rendering. So the average built where the items' text sits is far from what the reply positions carry. The
role mismatch the closure check of version 0.13 warned of is real.

## What John is asked to decide

Nothing more is spent until he rules. The options:

1. **Pause the test (recommended).** The design's comparisons cannot be met on this model. The rehearsals have
   settled two findings worth recording:
   - the dose question: the shared-context construction gives the two kinds of question equal swaps, within 1%;
   - the model finding: a wrong message does about twice the harm of no message, and far more than random
     change.

   Both can go into the project's record. The paper work stands, and the test can be taken up again with a
   new comparison design.
2. **Redesign the comparison.** For example, compare the swap with a structured removal of another kind, such
   as swapping a message from another position in the same input, rather than random noise. That is a new
   design, with its own reviews and rehearsals.
3. **Try a gentler removal.** For example, mix the true and donor messages, so that the loss sits inside the
   normal range. Again, that is a new design.

## Record

- **Spending.** The spending record's rows for the rerun carry the cost.
- **The code** ran as committed.
- **Owed.** An independent check of these findings, and of the earlier rented runs' findings.
