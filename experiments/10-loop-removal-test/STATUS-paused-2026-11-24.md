# The loop removal test (experiment 10): paused, and what it found

*Written 2026-11-24, on John's ruling to pause and record (`docs/rulings/2026-11-24-loop-removal-test-pause-ruling.md`).
This is the place to start if the test is taken up again.*

## What the test was for

Minimum Viable Mind's hypothesis H1 says a conscious machine would need a shared workspace: one place whose
contents many processes read and use together. Thinking Machines' research model TML-d24-varloop-research
runs a block of its layers three times, and passes a "message" from each pass to the next. The test asked
whether that message does a workspace's job.

The method was to replace the message with one built from other inputs, or with an average, and see whether
that costs problems solved from a rule in the prompt more than routine questions that ask about the same
context. The answer would be read against random damage of the same size. The design is
`docs/loop-removal-test-design-2026-11-20.md`, version 0.16 at the pause, after sixteen closure checks.

## What it found

1. **The swap gives both kinds of question the same dose.** This is the dose finding, RT-345, open from the
   first review to the last rented run. The concern was that the routine twins and the rule questions would
   get swaps of different sizes. If they did, a difference in loss could come from the dose rather than from
   the message's job.
   - **The fix.** The construction built for it puts both kinds of question on one shared context and lets
     them differ only in a fixed final question.
   - **The result on the real model.** After every filter, the routine cell's mean swap size divided by the
     rule cell's is 1.004 for lookup and 1.004 for unit under the swap, and 1.000 and 0.998 under the average.
     No pair was dropped to reach that (`step4b-rerun-findings-2026-11-24.md`).
2. **A message from another input is worse than no message.** In this model, replacing the message with one
   from another input lowers the model's confidence in the right answer by about 2.5 times what dropping to
   one pass costs on the rule questions, and 1.85 times on the routine questions. Dropping to one pass removes
   the message and the extra passes together.

   So the message carries information specific to its input, and a wrong one actively misleads the next pass;
   it does not merely withhold help. Random noise in the same place cannot do comparable harm, at any size:
   its damage stops at about 0.88 on prose, against 1.74 for the swap. The readers normalise what they read.
   The split removal test (experiment 09) found a related, smaller pattern.
3. **Smaller findings along the way.** Each is recorded in its findings file:
   - **Reasoning.** The model always begins its reply with written reasoning, even at the setting "none"
     (step 4a).
   - **Forced answers.** Answers forced as the first word are near chance unless the prompt says "Answer with
     the single word or number only." (the scoring trial).
   - **Chained lookups.** The model cannot follow even two linked lookups without writing them out (the lookup
     calibration).
   - **User-turn text.** In the chat format the model predicts the user's own text almost at random: 7.7 to 8.7
     nats per token, against about 2.4 as plain text or as its own reply (step 4b and its rerun).
   - **Scoring.** Scoring each item by its margin rather than right or wrong cuts the per-item noise to about a
     third (the margin check).

## Why the test cannot be read as designed

Finding 2 breaks three things the design rests on, and none of them is a threshold set wrong:
- **the random comparison matched on damage,** because random noise in the loop cannot reach the removal's
  damage;
- **the normal-range check,** because the removals raise perplexity on prose by 33 and 161, against bounds of
  0.37 and 0.20 from random noise of the same size;
- **room for a selective loss,** because the swap already takes most of each answer's margin, leaving the rule
  questions 0.72 C of room under the swap and 0.55 C under the average, against a target of 1.0 C.

The simplified operator kind also failed (5 of 40 pairs confident), which leaves two rule kinds against the
design's minimum of three. The average built where the items' text sits and the one built in the model's
reply differed by a factor of 5.3.

## What a resumed test would need

- **A different comparison.** It cannot be random noise. One candidate is a structured removal of another
  kind, such as a message taken from another position in the same input.
- **Or a gentler removal.** For example, a blend of the true and donor messages that keeps the damage inside
  the normal range.
- **A third rule kind** the model answers confidently, and one that gains from the extra passes.
- **The settled parts can be reused as they are:**
  - the shared-context construction;
  - the item-level split of the halves;
  - the reply rendering for damage;
  - scoring by margin with the unit C;
  - the resampling simulation;
  - the code in `src/`.

## What it cost

Five rented runs, on one RTX PRO 6000 each, came to about **$8.91**:

| Run | Cost |
|---|---|
| Step 4a | $3.61 |
| The scoring trial | $0.56 |
| The lookup calibration | about $0.28 |
| Step 4b | about $1.93 |
| The step-4b rerun | about $2.53 |

Every run was within the ceiling John set for it. The rest was paper work, done at no cost.

## What is still owed, if the test is taken up again

- An independent check of the five rented runs' findings.
- The list and overlap checks before any test set:
  - the test half's shares above about 160 pairs (RT-480);
  - the overlap check's content comparison (RT-484);
  - the earlier list checks (RT-417 and others).

The branch `claude/loop-removal-note-2026-11-20` holds all of this. It is committed and not pushed.
