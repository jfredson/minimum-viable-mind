# The loop removal test, the step-4b rerun: priced proposal, and what the code test already shows

*Written 2026-11-23. The rerun is step 4b run again on the pilot rebuilt for design version 0.14
(`batteries/pilot-v0.14/`), under specification section 19. The code is at commit 36c2b9a. Nothing is rented
until John gives his go.*

## Before the price: what testing the code showed

The updated analysis and simulation were tested end to end on step 4b's real data, from the old pilot, so
that bugs would surface before any rental. The test also produced the first real power figures. They bear
on whether the rerun is worth doing at all. They are kept in `step4b-rerun-code-test-2026-11-23/`.

**1. Under the new interference rule, the old pilot's lookup and unit pairings survive.** The old two-step
operator pairings do not, as expected. After the baseline checks, margin matching and swap-size matching, 40
lookup pairs and 32 unit pairs remain. The two cells' swap sizes stay equal: the ratios are 1.004 and 1.004
under the swap, and 1.000 and 0.998 under the average.

**2. Outcome A looks underpowered.** The simulation used the spread of the removal's per-item loss measured
at step 4b, about 0.46 to 0.58 on the normalised scale. With that spread, a true gap of 0.20 is read as
outcome A, under both methods and after every rename, with these chances:

| Test-half pairs | 80 | 140 | 200 | 260 |
|---|---|---|---|---|
| The gap spread evenly | 12% | 38% | 55% | 71% |
| The gap on the operator and unit pairs only | 9% | 17% | 26% | 18% |

No size up to 300 reaches the 80% the design asks for, and the test half can hold about 216 pairs. The main
limit is the rule that the routine cell's interval must end below δ (0.10). With items scored right or
wrong, each item's loss is 0 or about 1.25, so its spread is large. The figures are from 300 runs a cell
and assume the two methods are drawn independently, which is cautious. They are rough, but not far off.

**3. Outcome F looks out of reach.** The branch choice found neither branch of the bites set qualifying:

| Target | Both kinds | Unit alone | Needed |
|---|---|---|---|
| The one-pass condition | 68% | 45% | 80% |
| "Bites" | 92% | 85% | 80% |
| "Does not bite", when the swap truly costs nothing | 4% | 17% | 80% |

"Does not bite" needs the removal's own loss to have an interval ending below a quarter of the one-pass
cost: about 0.07 here. With right-or-wrong scoring at 100 to 200 items, that interval is wider than 0.07
even when the true loss is zero. So F, the plainest way the prediction could fail, could almost never be
read.

**4. The two warnings from the last review still stand.**
- In-loop noise of the swap's own size did little damage, and matching the swap took about a thousand times
  that size. That match was made in the user's turn, so it was measured badly. At that factor, in-loop noise
  cost the pilot's rule questions almost everything: a normalised loss of 0.96.
- The bites check's one-pass condition narrowly failed at 100,000 resamples, with a lower end of 0.148
  against 0.15.

**What this means.** The rerun would measure the new setup properly: the prose as the model's reply, the
simplified operator kind and the 80 unit bites items. It could move the damage figures and the one-pass
cost. It is unlikely to move points 2 and 3, because they come mostly from scoring each item as right or
wrong. Those spreads will be much the same on the new pilot. Even a clean rerun would then most likely
return to John with "underpowered" and "F out of reach".

**One idea, offered rather than recommended, because it is a large change.** Score each item by its margin, a
continuous number, instead of right or wrong. That would cut the per-item spread a great deal and could
fix both points 2 and 3. But it changes how every outcome is read, and so it would need a new design round
and its own reviews.

## The price, if John wants the rerun anyway

- **The card.** One RTX PRO 6000 (96 GB), RunPod secure cloud, $2.69 an hour.
- **The work.** It is about 1.3 times step 4b's work:
  - each prose passage is run in two renderings;
  - a second average is measured;
  - there are 120 bites items instead of 80;
  - the factor search runs 18 steps over a wider range.

  Step 4b took 43 minutes in all.
- **The expected cost** is about **$3**, within about $2.50 to $4.
- **The proposed ceiling** is **$10**, enforced by RunPod's terminate-after setting.
- **The order.** A ten-item quick try runs first, then the full run. The simulation is already committed, so
  it runs on the Mac before the results are opened.

## What John is asked to decide

1. **Rent the rerun, up to $10.** It measures the new setup and gives the formal answer on the dose
   question. It most likely confirms points 2 and 3.
2. **Pause the test here.** The paper record stands. The dose result, equal swap sizes within 1%, is the
   main thing settled.
3. **Explore scoring by margin.** This is a new design round, at no cost until a rental.
