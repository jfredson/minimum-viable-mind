# The chained-lookup calibration trial: priced proposal

*Written 2026-11-21. The trial is set out in section 16 of `battery-authoring-spec.md`, written and committed
(e626ec2) before its code. John chose to redesign the lookups ("Redesign the lookups") after the scoring trial
found them at chance in every version. Nothing is rented until John gives his go.*

## What the trial asks

Can an easier version of the chained lookup be answered at once, at three passes, and does it need the
passes? Two things are varied, giving four versions:

| Version | Names in the list | The four other chains | Prompt length (tokens) |
|---|---|---|---|
| 1. The current task | invented, such as "pashnix" | two to six steps each | 169 to 319 |
| 2. | invented | one step each | 124 to 172 |
| 3. | common one-token nouns, such as "boat" | two to six steps each | 125 to 200 |
| 4. | common one-token nouns | one step each | 95 to 115 |

An example of version 4, the easiest: "Answer with the single word or number only. In this list: teacher is
yellow; chief is brown; book points to boot; coat is white; train is pink; artist points to train; camera
points to chief; pond points to arrow; engine points to teacher; arrow points to coat; boot is green. Start
at pond and follow the list to a colour. What colour do you reach?" The answer is white, three steps on.

Each version has 16 items for every chain length from two to six steps, 80 in all. That is twice the
scoring trial's count per length. Every item carries the answer-only instruction at the start.

## How a version is chosen (fixed before the run)

A version qualifies if, on chains of four to six steps, it is right at least half the time at three passes,
and three passes beat one pass by at least 0.15. Of the versions that qualify, the one closest to the
current task is chosen, in the table's order, because each step down moves further from the task the
design names. If none qualifies, the choice comes back to you. One option then is to ask the bites check for
three steps or more instead of four, which would change the design.

This choice is made on practice items from half A. The real bites check is made later, on half B, on its
own scale, so choosing here does not decide it.

## What is ready, and checked for free

- **The new name list** (`data/chain_names.json`) holds 135 common nouns, sharing no word with any other
  list. 49 of half A's are single tokens, enough for the longest item (35 names).
- **The four versions** are in `batteries/chain-calibration/`. The free checks find no problem in any of the
  320 items:
  - every candidate colour ends exactly one chain;
  - no name is in two chains;
  - every name in versions 3 and 4 is one token;
  - following the shuffled rows from the start name reaches the right colour in the stated number of steps.
- **The script** (`src/chain_calibration.py`) builds, checks and runs the trial. It reuses step 4a's loading,
  hooks and scoring, which reproduced step 4a exactly in the scoring trial.

## The machine and the cost

- **The card.** The same as before: one RTX PRO 6000 (96 GB), RunPod secure cloud, $2.69 an hour. A 5090
  cannot hold the model at 16-bit.
- **The time.** The scoring trial took 13 minutes from creating the machine to deleting it, for 840 item
  runs. This trial makes 960 item runs, most of them shorter, so about 15 minutes.
- **The expected cost** is about **$0.70**.
- **The proposed ceiling** is **$3**. RunPod's own shut-off would be set to 1 hour after creation, which is
  $2.69 at most.

## After the run

The findings are written up in plain words. The cost goes in the spending record, and the machine is deleted
as soon as the results are copied back. If a version is chosen, the change to the design and the test set's
generator is written next. It would go through a review before any test set is built.
