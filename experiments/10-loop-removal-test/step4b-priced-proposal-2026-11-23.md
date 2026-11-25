# The loop removal test, step 4b: priced proposal

*Written 2026-11-23. Step 4b is the measurement rehearsal of the design (`docs/loop-removal-test-design-2026-11-20.md`,
version 0.12, section 9), on the rebuilt pilot (`batteries/pilot-v0.12/`). What it does, step by step, is in
`step4b-runbook.md`. The code is committed (commit 4c7cbaf). Nothing is rented until John gives his go.*

## What step 4b settles

Step 4b is the first time the test's real measurements are made, on practice items only. It settles the
questions the free checks cannot:
- **The dose question (RT-345).** After the baseline checks and margin matching, it asks whether the two
  kinds of question receive swaps of the same size, within 10%, under both methods. This finding has been
  open since the first review.
- **Whether the swap and the average are comparable.** It measures their damage on ordinary prose. If both
  the average and its fallback differ from the swap by more than a factor of two, the test stops (choice 5).
- **Whether the random comparisons can be matched to the removal's damage,** and whether all of them stay
  within the normal range.
- **Whether the bites check can pass.** It measures how much dropping to one pass costs the 80 held-out
  problems, with its interval, pooled and for each of the two kinds.
- **Whether outcome F can be reached.** It measures the change ratio under each method against 0.5.
- **Which rule kinds survive** the baseline checks, and the table of which rule kinds go with which
  routine kinds.
- **The spreads the sample-size simulation needs,** which then sets the size of the test half.

Each of the design's return-to-John conditions is printed as fired or not. The analysis does not compute
the gap between the two kinds of question, or any outcome. The pilot rehearses; it is not the test.

## What is ready, and checked for free

- **The runbook** was written first (commit 5b42a51). It rests on the model's public source, read again on
  2026-11-23. That reading confirmed the shapes of the block sums the hooks replace, and where block 1's
  output is.
- **The baseline variants' token ids** were made on the Mac (`baseline_ids.jsonl`). The script first checks
  that the stored ids are what the generator's renderer makes, for all 120 pairs.
- **The analysis** was run on made-up collection files with the real pilot's ids. It runs end to end: the
  baseline checks, the strike counts, both matchings, the bites interval resampled by fact, and every
  return-to-John flag.
- **What cannot be checked here.** This Mac has no PyTorch, so the collection script has only been checked
  for syntax. The run therefore starts with a quick try on 10 items and 20 prose passages, as step 4a did,
  so that any mistake costs minutes rather than the full run.

## The machine and the cost

- **The card.** One RTX PRO 6000 (96 GB), RunPod secure cloud, $2.69 an hour, the same card as before. The
  model needs about 50 GB, and the recorded block sums a few more.
- **The work.** About 11,000 model runs. The largest part is the search for the comparisons' noise sizes on
  the prose passages: about 5,600 runs of 5 draws each. Each item's 20 noise draws run together in a batch
  of 20.
- **The time.** Step 4a timed a single run at about 0.23 seconds. Batches of 5 and 20, and the full
  predictions the prose passages need, were not timed. Allowing for those, the full collection should take
  about 1.5 hours. Setup takes about 25 minutes, the quick try about 15, and there is slack for one round of
  fixes.
- **The expected cost:** about **$7**, within a range of about **$5 to $12**.
- **The proposed ceiling: $20,** about 7.4 hours. RunPod's own terminate-after setting would be set at the
  time the ceiling would be reached, so the machine cannot run past it. The pod is deleted by hand as soon
  as the results are copied back.
- **The balance:** $54.07 (`runpodctl me`, 2026-11-23). No pod is running.

## One thing for John to know about the account

The RunPod account shows a standing charge of about $0.01 an hour with no pod running, probably storage
such as a network volume. Over two days that is about $0.50. It explains most of the gap between the
lookup trial's time-based cost ($0.28) and the balance's fall. It has nothing to do with this run, and it
is left as it is unless John wants it looked at.

## After the run

The analysis runs on the Mac. The sample-size simulation (`src/step4b_simulate.py`) is written and
committed before the collection's results are opened. The findings are written up in plain words, and the
cost goes in the spending record. If any return-to-John condition fires, the design comes back to John
before anything else is spent.
