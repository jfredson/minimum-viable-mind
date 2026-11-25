# The loop removal test, step 4b: runbook

*Written 2026-11-23, before the step-4b code, on John's instruction ("Yes, write it"). Step 4b is the
measurement rehearsal of the design's section 9 (`docs/loop-removal-test-design-2026-11-20.md`, version
0.12, with John's rulings on choices 6 to 8). It runs on the rebuilt pilot, `batteries/pilot-v0.12/`.
Nothing here runs on a rented machine until John has given his go in his own words, with a ceiling. His go
is recorded first in `docs/spending-record.md` and the worklog.*

## What the model's source fixes

The model's public source (transformers commit 046bdb8,
`src/transformers/models/inkling2_loop/modular_inkling2_loop.py`, read again 2026-11-23) fixes how the
hooks work.

- **What the readers receive.** On each pass after the first, before each of the 12 looped layers, the text
  model calls `message_input(previous_block_states, previous_hidden_states, loop_layer_idx)`.
  - `previous_block_states` has the shape [batch, position, sum, width]. It holds the previous pass's
    completed loop block sums.
  - `previous_hidden_states` has the shape [batch, position, width]. It holds the previous pass's final
    running state.
  - The reader stacks the two along the sum axis and normalises them, then reads them with learned
    queries.

  These stacked sums are the design's "two previous-pass block sums that the message readers read". The
  same two inputs go to all 12 calls of a pass, so replacing them in every call replaces what every
  reader reads.
- **Block 1's output.** The pre-loop running state is the output of layer 5, the last layer before the
  loop. Each pass after the first restarts from it, and pass 1 starts from it too. The comparison for
  damage outside the loop adds its noise there, through a forward hook on layer 5.
- **The width is 2,304.** The script reads it from the tensors and assumes nothing.

## What step 4b measures

There are two parts. The collection runs on the rented card. The analysis runs free on the Mac, from the
collection's output files.

**1. The collection** (`src/step4b_collect.py`), in order:

1. Load the model at 16-bit, as in step 4a. Find the text model and its `message_input`.
2. **The noise floor, the identity check and the bypass check,** on the first 20 scored items, as in
   step 4a.
3. **Unaltered runs, recorded.** Every scored item, donor-only item, bites item and neutral passage is run
   once at three passes. Its two block-sum inputs on passes 2 and 3 are recorded, and so is block 1's output.
   Scored items and bites items also get a second unaltered run, for the noise floor.
4. **The averages** (design, section 3, method b). They are built from the 100 neutral "build" passages:
   - pooled over text positions, separately for each pass and each sum;
   - by template slot, counted from the start of the template's opening part and from the end of its
     closing part;
   - and, for the fallback, in ten bins of relative position in the text span.
5. **The neutral set's damage and perplexity** under the main removal, on the 100 "measure" passages:
   - **The swap.** Five donor passages each, drawn with seed 1 from the other half-A passages at least as
     long.
   - **The average,** and **the fallback.**

   Damage is the mean, over the text span's positions, of the divergence between the unaltered and altered
   next-word predictions. Perplexity is taken over the text span's tokens.
6. **Damage matching** (design, section 4). There are four comparisons:
   - random noise in the loop, scaled to the swap or to the average;
   - noise outside the loop, scaled to the swap or to the average.

   For each one, the shared factor is searched on the measure passages, with 5 draws a passage, then
   confirmed with 20 draws. The aim is a mean damage within 20% of the main removal's for that method. A
   comparison that cannot be brought within 20% is recorded as unmatched.
7. **The normal-range bound** (design, section 4). For each method, 20 draws of in-loop noise are made at a
   factor of 1, each passage scaled to its own swap distances. The bound is the 95th percentile of the
   perplexity rise over the draws. Every removal and comparison then has its own rise recorded against it.
8. **Every scored pair item, and every bites item,** is run under each condition:
   - unaltered, twice;
   - the swap, with five donor pairs drawn with seed 1. These are whole pairs, under the pair donor rule;
     a bites item gets its donors under its own rule;
   - the average, and the fallback;
   - random noise in the loop, at the matched factor, 20 draws, for each method;
   - for pair items only, noise outside the loop, at the matched factor, 20 draws, for each method;
   - one pass, and two passes.

   Pair items also get the baseline variants, run unaltered at three passes:
   - the prompt-rule item without its rule;
   - the prompt-rule item with only its rule, its facts and its question;
   - the routine twin with only its fact and its question.
9. **For every item and method:** the swap size (the total distance over the changed positions and both
   passes) and the change ratio, as section 17, item 7 of the specification defines them. Under the swap,
   both are computed for each donor and then averaged. The positions changed by each donor, and the
   distance at each position, are kept, because the noise is scaled from them.

**2. The analysis** (`src/step4b_analyse.py`). It runs on the Mac from the collection's files and produces
these figures:
- the noise floor, the identity check and the bypass check against the tolerance;
- the baseline checks, with the strike counts for each pairing, and the pairing table;
- confidence filtering, margin matching and swap-size matching, each with its limit;
- the survival of the three rule kinds;
- the damage of the two methods side by side, and the factor-of-two rule;
- the normal-range check, and the room under the bound;
- the bites check's one-pass condition, pooled and per kind, with intervals resampled as section 6 sets
  out;
- the change ratio under each method against 0.5;
- the spreads and the comparisons' losses that the sample-size simulation needs.

Each return-to-John condition of design sections 4 to 6 is printed as fired or not fired.

**What the analysis does not compute.** It does not compute the main removal's gap between the two cells.
It does not compute any outcome, and it reads no pattern. The pilot rehearses the measurements; it is not a
test.

**The sample-size simulation** (`src/step4b_simulate.py`) is written and committed before the collection's
results are opened. It runs on the Mac.

**What step 4b leaves out.** The design asks the rehearsal to report two descriptive figures: how much the
pass-counting coordinates vary, and how far the swap moves the keep and gain settings. Neither decides
anything, and neither is collected here. They are left for the registered run's report, and that is said
here so that the omission is visible.

## The run

1. **Before anything is created.** Record John's go in his words, the estimate and the ceiling, in the
   spending record and the worklog. Note the RunPod balance.
2. **Create one pod.** It is an RTX PRO 6000 (96 GB), secure cloud unless a community one is free, on the
   step-4a image. RunPod's terminate-after setting is set at the time the ceiling would be reached.
3. **Copy and install.** Copy `src/` and `batteries/pilot-v0.12/` to the pod. Set up a virtual environment
   over the image's PyTorch, then install transformers at commit 046bdb8 and accelerate, as in step 4a.
4. **A quick try first:**

   ```bash
   python -I src/step4b_collect.py --pilot batteries/pilot-v0.12 --out out-quick --limit 10
   ```

   This runs every phase on 10 items and 20 neutral passages, with a short factor search. Fix anything
   that breaks. Every fix is copied back and committed with the findings.
5. **The full run:**

   ```bash
   python -I src/step4b_collect.py --pilot batteries/pilot-v0.12 --out out
   ```

   Wait with a check that cannot match its own command line: `pgrep -f "[p]ython -I src/step4b"`.
6. **Copy back and delete the pod.** Copy back `out/`, the log and the package list, then delete the pod.
   Note the balance.
7. **On the Mac:** run the analysis, then the simulation. Write `step4b-findings-<date>.md`, and add the cost
   to the spending record.

## What would stop the run and return to John

- The identity or bypass check fails, or the noise floor is above 0.01.
- The card runs out of memory with the batch of 20 draws. The script falls back to batches of 5, and says
  so.
- The run would pass the ceiling.

The design's own return-to-John conditions are read in the analysis, not on the card.
