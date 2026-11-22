*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the ten earlier reviews. It worked read-only in a detached worktree at commit b211fa7, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.11

*Reviewer: a fresh Claude Code session. I did not write the design, version 0.11's changes or any earlier version's, the three rented runs, their findings, or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure11-loop-design-2026-11-21` at commit b211fa7 and changed nothing in it; `git status` was clean when I finished. I used only my own scratch folder, `/private/tmp/claude-501/loop-review11-Fe6Yaj`, which was empty when I started, and every script and output is there. I did not open, list or use any other scratch or temporary folder, including earlier `loop-review*` folders and any session scratchpad. I downloaded nothing, installed nothing, spent nothing, pushed nothing and made no network calls. New findings are numbered from RT-457.*

---

## What I opened

- **The closure check of version 0.10**, `docs/reviews/2026-11-21-loop-removal-test-design-v0.10-closure-check-claude-code.md`, in full. I treated its filer's check as the author's note, not as part of the review.
- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.11 header (lines 1 to 37); sections 1 (lines 101 to 153), 3 (lines 197 to 345), 4 (lines 347 to 382), 5 (lines 384 to 979), 6 (lines 981 to 1070), 7 (lines 1072 to 1099), 8 (lines 1101 to 1137), 9 (lines 1139 to 1211), 10 (lines 1213 to 1294) and 11 (lines 1296 to 1340); and the change log "from version 0.10" (lines 1836 to 1887).
- **The diff** `git diff 600d0bb b211fa7 -- docs/loop-removal-test-design-2026-11-20.md`, in full.
- **Raw results:** `scoring-trial-run-2026-11-21/scoring-trial-results.json` (every per-cell rate, confidence share and summary, all three sets). I looked at the structure of the other two runs' folders but used no figure from them beyond what the earlier check already verified.
- **The pilot set and the two trial sets**, `batteries/pilot/` (`build-report.json` for the pools, `step3-results.json` for its keys), and `batteries/trial-instruction-start/` and `batteries/trial-instruction-end/` (`pairs.jsonl`, `donor_only.jsonl`).
- **Code:** `src/build.py` in full; `src/scoring_trial.py` in full.

I did not open the battery specification, the findings files, any web page, or anything outside the worktree and my scratch folder. I did not need the tokeniser beyond what the committed `prompt_ids` in the trial sets already record.

## What I ran

All under `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`, from my scratch folder. Each script's output is saved beside it as a `.out` file.

- `pools_split.py`: the per-decade split of version 0.11, drawn with 2,000 seeds, applied to products (2 to 12, one order), the unit kind (factor 2 to 9, count 2 to 12), sums (2 to 49, one order) and the operator kind (the generator's four shapes, operands 2 to 15 and 2 to 30), two-digit answers only. For each half: items, distinct answers, mean answer, and the item-weighted share of answers ending in 0, and in 0 or 5.
- `ceilings.py`: the largest test half each allocation allows, by an exact flow fit of rule kinds to routine pools under the pairing exclusions and the 25% cap, with half B's pools (36 capitals, 75 opposite questions, 61 objects, sums ample) and a products pool of 13, 18, 23, 28 or 33. Then the expected pairs passing the confidence filter, from the scoring trial's per-pairing rates (prompt-rule rate times routine rate, as the author did), under two placements of routine kinds: the generator's even spread (its stated rule) and the allocation that maximises survivors (an upper bound).
- `arith_share.py`: for the recommended allocation, the share of sums and products in the built routine cell and in the surviving one.
- `strike_sim.py` and `strike_sim_combined.py`: the strike-count rule at step 4b on a 120-pair pilot, for four kinds as built, the 2 : 1 : 1 of version 0.10, and the 40 / 40 / 40 of version 0.11, at both placements of the instruction. Assumptions are stated at the top of each script and under the choice 8 finding (RT-463) below.
- `prefix_share.py`: for every operator and unit prompt-rule item in the two trial sets and every donor the generator's own `eligible` rule allows, the share of the item's scored positions that come before the item and its donor first differ.
- `unit_range.py`: the unit kind's facts under the trial's half A range against version 0.11's range.

---

## The earlier findings, one by one

### The plainest-failure finding (RT-449): closed in form, open in substance

**What version 0.11 did.** It adds outcome F, "The replacement does not bite" (section 6, lines 1014 to 1019; section 7, line 1085). F is reached when the cells show no excess, the one-pass run costs the held-out problems, the main removal's excess over the random comparison on those problems has an interval whose upper end is below a quarter of the one-pass cost, and the swap changed the message by at least half its size (section 5, lines 850 to 856). F is read as the prediction failing for this placement. Section 7's allowed sentence moves from D to F (lines 1092 to 1095). A pattern of A, B or C with a removal that does not bite is renamed "Cells and bites check disagree" (lines 1022 to 1026).

**Is every case still in exactly one outcome?** Yes, mechanically.
- Stage two still runs A, B, C, then the no-excess branch, then E, and the first that applies decides.
- Inside the no-excess branch, "bites" and "does not bite" cannot both hold. "Bites" needs a point estimate of at least half the one-pass cost, so its interval's upper end is at least half, which is above a quarter. Anything else is "too weak to read".
- The disagreement rename is applied before "Not specific", "Specificity not checked" and "Depends on one kind", so an A or B renamed by it cannot be renamed again. Each method is classified on its own and then combined, as before.

**Is F the right kind of answer?** Yes. It reads the case the tenth check said was lost. Requiring both methods to land in F is also a real protection. A swap donor is a problem of the same rule kind, so it could carry what the passes supply about the kind of problem without anything about this item. The average method carries no such thing. So if the swap lands in F but the average does not, the result is "methods disagree", not a failure.

**But F, as defined, does not say what its reading says.** Three new serious findings follow, and each must be fixed before F can carry the reading "the prediction failed":
- F is defined by the excess over random damage, not by the swap's own loss (RT-457).
- The disagreement rename is wrong for B and too broad for A and C (RT-458).
- The swap-size condition is not defined well enough to compute, and on one reading it is likely out of reach (RT-459).

A further worth-noting finding (RT-461) is that F, unlike A, has no protection against one kind carrying the result.

### The test-half ceiling finding (RT-450): closed, with corrections to the figures

**The ceilings.** I recomputed every row of choice 8's table with an exact flow fit (`ceilings.out`):

| Allocation | Ceiling, products 13 / 18 / 23 | Surviving, even spread (products 13 / 23) | Surviving, best case (products 13 / 23) |
|---|---|---|---|
| four equal kinds | 196 / 216 / 236 | 96 / 114 | 108 / 126 |
| three equal kinds | 196 / 216 / 220 | 130 / 145 | 136 / 150 |
| operator 2 : unit 1 : lookup 1 | 145 / 145 / 145 | 86 / 86 | 90 / 90 |
| operator 1 : unit 1 : lookup 2 | 196 / 216 / 236 | 140 / 168 | 151 / 178 |

These are at the start placement. The end placement gives nearly the same totals.

The author's ceilings are right. The 220 for three equal kinds needs the shares 73, 73 and 74, and with exact thirds it is 216. The author's survivor counts (133 to 149, 108 to 126, 88) lie between my even-spread and best-case figures and match the best case closely. The generator's stated rule, spreading each rule kind evenly, gives about 130 to 145. That is a few pairs lower and still inside the 120 to 200 the simulation is expected to ask for.

**The products pool.** The change log's "products 13" cannot happen under the new split. Over 2,000 seeds, half B's two-digit products ran from 17 to 40, with a 5th percentile of 22 and a median of 28 (`pools_split.out`). The body's "about 23 to 27" (line 535) is about right. So the recommended allocation's ceiling is about 216 to 220, not "196 to 220", and about 140 to 150 pairs survive, not 133 to 149. The error is on the cautious side and changes no recommendation, but the change log and the body disagree.

**The 1 : 1 : 2 option.** It is rejected because "almost no operator pairs survive" (lines 1859 to 1860). That is not right. Under the even spread it keeps about 10 to 12 operator pairs, against about 17 to 18 for three equal kinds, and it gives the most survivors of any option (about 154 to 168). See RT-463.

**The arithmetic share.** I checked the share of sums and products in the routine cell under the recommended allocation:
- **In the built cell:** 32% to 34%.
- **In the surviving cell:** 46% to 51%, because sums and products behind the lookup rule pass the filter almost always. Sums alone are 35% to 38% of the surviving routine cell (`arith_share.out`).

So the design's "roughly 40% to 50% arithmetic" (line 1283) is right. But sums alone exceed the 25% cap once the filter has run, and the design does not say whether the cap binds on the built cell or the surviving one (RT-463).

### The last-digit finding (RT-451): closed for the value grid, open for the items

The per-decade draw (lines 688 to 693) does give each half one of each decade's two values ending in 0 or 5, two other even endings and two other odd endings. So the systematic split of version 0.10 is gone, and both halves now see every ending.

But the halves are matched on the grid of answer values, not on the items, and the items are what the pilot measures. For products and for the unit kind, the items sit unevenly on the values. A value ending in 0 often has two or more factorisations (20, 30, 40 and 60 each have two among products), while values ending in 5 have one, and a prime such as 23 has none. The draw for each decade is independent, so one half can hold most of the round numbers. The result, over 2,000 seeds (`pools_split.out`):
- **Items ending in 0, half A's share minus half B's:** the 5th to 95th percentile is −0.26 to +0.25 for products and −0.25 to +0.24 for the unit kind. In about one seed in ten, one half has more than a quarter more of its items on round numbers than the other. That is the very difference RT-451 named as the easiest case.
- **Mean answer, half B minus half A:** −9.6 to +9.6 for products and −8.6 to +8.6 for the unit kind (5th to 95th percentile).
- **Half B's unit facts:** 26 to 59 across seeds.
- **Operator and sums:** much better balanced on 0-or-5 endings (within ±0.04), but the share ending in 0 still differs by up to about ±0.13 to ±0.22.

Step 3 reports these, and "the halves are not called equally hard until the pilot's report shows these match" (line 705). But nothing says what "match" means, or what is done if they do not. See RT-460, which is the condition on this closure.

### The overlap finding (RT-452): closed, with one wording fix

- **The operator's split key** is now the shape with its operands (lines 708 to 710). Since the split is by answer value, this follows from the value rule and is harmless.
- **Numeric wrong answers are exempt** (lines 710 to 712), with the reason.
- **The script** is to be rewritten before step 3 and listed there.
- **The "about 2.5 higher" figure** is gone.

But the same paragraph still says "The script also fails if any test item's candidate comes from a half-A pool" (lines 718 to 719), with only colours named as exempt. The text should say that numeric candidates are exempt from that check too, since that is what "the half check" (line 710) appears to mean.

### The excess-condition finding (RT-453): closed, with two definitions owed

- "Bites" and "does not bite" now decide D, F and the disagreement rename (lines 859 to 860), so the excess condition has work again.
- The one-pass condition gets an interval, with its lower end at or above 0.15 (lines 838 to 844).
- The size rule aims at all three conditions (lines 861 to 868).

Two definitions are owed:
- **"A quarter of the one-pass cost"** (line 851) should say that it is the point estimate of the one-pass cost on the same items and under the same resampling.
- **The size rule's target for "does not bite"** should include the swap-size condition, because "does not bite" needs it. Otherwise the simulation sizes a condition the design does not use.

### The routine-arithmetic finding (RT-454): closed

Choice 8 now states every consequence the tenth check listed (lines 1278 to 1285). The figures are right (above). The 25% cap's base is RT-463.

### The repeated-facts finding (RT-455): closed with conditions

- **The unit range** is fixed at factor 2 to 9 and count 2 to 12. That gives 81 facts, and about 40 per half (26 to 59 across seeds, `pools_split.out`), which matches "about 35 to 45" (line 803) only for the middle seeds.
- **Resampling by fact** is written into the bites section only (line 806). Section 6 still says "paired resampling of pairs" (line 986), and the sample-size section says "differences are resampled by item" (line 937). See RT-462.
- **"Close to the trial's difficulty"** (line 702) is not supported. Two thirds of the facts lie outside the range the trial measured (RT-464).

### The stale-text finding (RT-456): mostly closed

Every item the tenth check listed was fixed except one: the "270 to 300" ceiling survives at lines 921 to 924. New stale text is listed under RT-465.

### The conditions set on RT-437 to RT-448

- **The outcome D finding (RT-437): closed.**
  - Section 1's drifting "That" is fixed: line 146 now names "a failure in either kind of case".
  - Section 7's allowed sentence has moved to F.
  - The loss from D's lost reading is restated correctly (lines 888 to 891).
- **The operator-risk finding (RT-438), its condition for the test half: closed** by the recomputed ceilings above.
- **The halves finding (RT-439): open until RT-460 is answered.** Its conditions were RT-451 and RT-452. RT-452 is closed, but RT-451 is closed only on the value grid.
- **The keep-apart finding (RT-440): closed.** The "32 combinations" sentence is now marked as describing version 0.9's ranges (lines 800 to 802).
- **The trial-figures finding (RT-441): closed.** From the raw file:
  - 0.236, 0.543 and 0.557 of 280 items are 66, 152 and 156 items. None of the 40 chained items passed, so over the 240 pair items that is 28%, 63% and 65%, as lines 414 to 415 and choice 6 now say.
  - The routine twins at three passes were 0.842 at the start and 0.833 at the end, the "84% and 83%" of choice 6.
- **The bites sample-size and what-the-bites-check-gates findings (RT-442, RT-444): closed**, now under RT-453.
- **The opposite-directions finding (RT-445): closed.** The routine gain is placed on sums and products (lines 904 to 907), and the simulation draws effects by routine kind as well as by rule kind (line 908).
- **The 16-bit finding (RT-446): closed.** Lines 399 to 402 now say "will usually fail on any real difference", with the reason.
- **The choice 6 finding (RT-447): closed**, but its recommendation should be weighed again under the revised choice 8 (RT-463).
- **The stale-text finding (RT-448): closed.** Both time caveats are in (lines 1130 to 1133), and so is the note that the count rests on 300 pairs.

The dose question (RT-345) stays open until step 4b, and nothing here bears on it.

---

## New findings

| # | Finding | Grade |
|---|---|---|
| RT-457 | F is defined by the excess over random damage, so it can be reached when the swap costs the held-out problems as much as the passes supply, and its reading then says the opposite of what happened | serious |
| RT-458 | The "Cells and bites check disagree" rename takes away the clearest B, and for A and C it compares the bites items with a cell they only half represent | serious |
| RT-459 | F's swap-size threshold of 0.5 cannot be computed as written, and on the plain reading about 41% of the swap's positions count as unchanged, so F may be out of reach | serious |
| RT-460 | The per-decade split matches the halves on the value grid but not on the items, and nothing says what happens when they do not match | serious |
| RT-461 | F, now a reading that the prediction failed, has no check that one kind of bites item carries it | worth noting |
| RT-462 | Resampling by fact is not carried into the outcome intervals or the simulation, and the simulation must now model the bites items and the cells together | worth noting |
| RT-463 | Choice 8's revised allocation is somewhat worse for the pilot at the recommended placement, one alternative is rejected for a wrong reason, and the 25% cap's base is unstated | worth noting |
| RT-464 | The unit range is called close to the trial's difficulty, but two thirds of its facts lie outside what the trial measured | worth noting |
| RT-465 | Stale and inconsistent text | worth noting |

### RT-457, F does not require the swap to leave the held-out problems intact (serious)

**Lines:** 139 to 144 (section 1), 318 to 324 (section 3), 850 to 856 ("does not bite"), 1014 to 1019 (section 6), 1085 (F's row), 1092 to 1095 (the allowed sentence).

**The case.** "Does not bite" asks only that the main removal's loss on the bites items, minus the random comparison's loss, be small. Suppose the swap costs the held-out problems 0.3, close to everything the extra passes supply, and random noise matched on damage to the neutral set also costs them 0.3. The excess is then about zero, so the removal "does not bite". If the cells also show no excess, the outcome is F.

**What F then reports.**
- Section 1 says "a message built from other inputs serves as well as the true one".
- The allowed sentence says "what the extra passes supply survived a message built from other inputs".
- F's reading says "what the extra passes supply on these problems does not depend on this input's own message".

All three are false here. The message from other inputs took away most of what the passes supply. All that was shown is that the swap did no more harm than random damage of the same size. That is "nothing selective about the content", the kind of no-excess result that D now reports with no reading. It is not "the content does not matter".

**Why it is not far-fetched.** The random comparison is scaled so that its damage on the neutral set matches the swap's within 20% (section 4). If the swap does real damage on ordinary text, which it will if the message's content matters to the model at all, the matched noise is large too. Both could then knock over the same fragile items.

**What must change.** "Does not bite" should also require that **the main removal's own loss on the bites items**, measured against the unaltered three-pass run, have an interval whose upper end is below a quarter of the one-pass cost, under each method. Then "survived" is true. A case where the swap costs a lot but no more than random would fall to "too weak to read", which is honest. F's row in section 7 should then say "cost them little", not "no more than matched random damage". The size rule should aim at this condition too.

### RT-458, the disagreement rename is inverted for B and too broad for A and C (serious)

**Lines:** 1022 to 1026 (the rename), 139 to 141 (section 1), 1086 (section 7, E row).

**For B.** B means a loss beyond the comparisons on routine questions, with P's interval below δ, which means no excess on the prompt-rule problems. The bites items are prompt-rule problems of the operator and unit kinds. So a B whose removal does not bite on them is the most coherent B there is: no loss on rule problems in the pairs, and none on the held-out rule problems either. Version 0.11 renames exactly that B to "Cells and bites check disagree", with no reading. It removes the readable failure the test most needs.

Meanwhile, a B whose removal does bite the held-out problems keeps its name. That is the B where the two kinds of evidence pull against each other: P shows no excess, but the same kinds of problem held out do. So the rule renames the coherent B and keeps the incoherent one.

**For A and C.** The stated reason is that "the held-out problems are the same two kinds, in the same form, as half of the prompt-rule cell". But that is only half. On the trial's pass rates, the lookup pairs are about half of the surviving prompt-rule cell (`ceilings.out`: about 74 of about 145 surviving pairs under the recommended allocation). The two cases look like this:
- **An A whose P loss is carried by the lookup pairs.** That is consistent with no loss on the held-out operator and unit problems. "Depends on one kind" is the rule built to catch it, and it names the kind.
- **A C whose P loss sits on the lookup pairs.** It can likewise be a real general loss with nothing on the held-out kinds.

**What must change.**
- Drop B from the rename.
- For A and C, rename only when the **operator and unit part** of P has an excess whose interval lies above zero while the removal does not bite. That is the case the stated reason actually covers. State it with that reason.
- Section 1 (lines 140 to 141) says B and C need "the replacement is shown to bite". Section 6 does not require that: B and C stand when the bites check falls between the two thresholds. Section 1 should say what section 6 requires.

### RT-459, the swap-size threshold cannot be computed as written, and may be out of reach (serious)

**Lines:** 306 to 309 (the swap size), 850 to 856 (the 0.5 condition), 1085 (F's sentence).

**What is undefined.**
- **"Changed positions"** (line 307). The removals act "at every position the item uses" (line 200). But before the item and its donor first differ, their block sums are identical, because the model reads left to right. It is not said whether those positions are "changed", and so whether they enter the denominator, "the size of the true normalised block sums at the same positions".
- **"Size".** It could be a sum of per-position lengths or the root of a sum of squares, and it could be over both block sums or each one alone.
- **"Normalised".** Each of the 48 readers normalises with its own learned weights (section 2), so it matters whether the normalisation includes those weights or not.

Each reading gives a different number, and the threshold 0.5 is fixed now, with no measurement behind it.

**What the plain reading does.** I measured, on the trial sets' operator and unit prompt-rule items and every donor the generator's `eligible` rule allows (`prefix_share.out`), the share of an item's scored positions that come before it diverges from its donor:
- **with the instruction at the start**, the recommended placement: 41% for the operator kind and 43% for the unit kind, about 27 tokens of the template, the instruction and the rule's opening words;
- **at the end:** 28% and 29%.

If those positions count in the denominator, the swap's distance is exactly zero over about 41% of it. To reach 0.5 overall, the positions after divergence must then average a distance of about 0.86 of their own size. For vectors of equal length, that is a cosine similarity of about 0.63 or less at every such position.

Section 2 says one coordinate of block 3's normalised sum carries about 46% of its squared size at the end of every pass but the last, and the design itself argues that the donor's sums carry the same pass-counting signal on the same pass (lines 298 to 301). That shared part pushes the cosine up. So under this reading F may be unreachable for the swap. If it is, the asymmetry of RT-449 comes back unannounced, reported as "too weak to read".

**The two methods differ in kind here.** The average is one vector per pass and layer source over every text position, so its distance from the true sums has a different scale from the swap's. F needs both methods to clear 0.5, and nothing says the two scales are comparable.

**A mean hides small swaps.** The condition is a mean over items. A minority of items with near-identical donors can sit under a comfortable mean.

**What must change.**
1. Define the ratio exactly: which positions (I suggest those from the first position where the item and its donor differ, through the candidate), which norm, which normalisation, and both blocks or each.
2. Have step 4b report the pilot's ratio under each method, with its spread over items.
3. Add a return-to-John rule: if the pilot's mean ratio is below the threshold under either method, the design returns to John before registration. Then whether F can be reached is known before any test data, and the threshold is never chosen after seeing results.
4. Have section 7's F sentence say "on average".

### RT-460, the per-decade split matches the value grid but not the items (serious)

**Lines:** 688 to 705 (the split), 795 to 796, 826 to 828 (the bites check made on half B).

**The problem.** Figures are in the last-digit entry above (RT-451) and `pools_split.out`. The draw matches the halves on the grid of values, but the items sit unevenly on that grid, most of all for products and the unit kind. The unit kind is half of the bites check. In about one seed in ten, one half has more than a quarter more of its items on answers ending in 0, the easiest case that RT-451 named. Mean answers can differ by about 9, and half B's unit facts can number anything from 26 to 59. The cause is that the value ending in 0 or 5 is drawn for each decade independently, so across nine decades one half can collect most of the round numbers.

**Why it matters.** The one-pass condition gates every outcome, and the reason for matching the halves is that the pilot must forecast it on the test half (RT-439). Step 3 reports the mixes, but "the halves are not called equally hard until the pilot's report shows these match" (line 705) gives no tolerance and no consequence. A seed that fails would leave the design with no rule, and choosing a new seed after seeing the report is a choice made after data. These are model-free data, but they are still not fixed in advance.

**What must change, before any item exists.**
- Balance the endings in 0 and 5 across decades, for example by alternating which half gets the 0, by kind.
- Fix tolerances on the item-weighted mixes: the share ending in 0, the share ending in 5, the mean answer, operand parity, and the number of distinct facts.
- Fix a seed rule: take the first seed in a fixed order whose split meets every tolerance, per kind.

All of this can be computed without the model, so it can be fixed now.

### RT-461, F has no check against one kind carrying it (worth noting)

**Lines:** 850 to 856, 1061 to 1062.

F now reports that the prediction failed. Its evidence is the bites check pooled over the operator and unit kinds. A gets the readings with one kind left out. F gets none: "C, D, E and F are never renamed by these checks". If the operator bites items lose clearly and the unit items not at all, the pooled excess can fall below a quarter of a pooled one-pass cost. That is likelier if the unit kind's one-pass cost is the larger, as in the end-placement trial (0.43 against 0.30 raw).

**What should change.** Require "does not bite" to hold in each of the two bites kinds separately, or rename F to "Depends on one kind" when it does not. Size the bites set for that.

### RT-462, the resampling scheme and the simulation (worth noting)

**Lines:** 803 to 808 (by fact), 936 to 953 (sample size, "resampled by item"), 986 to 987 (section 6, "paired resampling of pairs").

1. **The resampling scheme.** Resampling by fact appears only in the bites section. The R and P intervals mix unit pairs, which share facts with one another and with the bites items, with every other kind. So the scheme must be written for section 6 too. I suggest this: resample within each rule kind, with whole unit facts as the units for the unit kind (taking every bites item and pair that shares a fact together), and pairs elsewhere. The simulation should use the same scheme.
2. **The simulation must model the bites items and the cells together.** The simulation must find the chance of an A "after every check in section 6 that can rename an A" (line 940). The disagreement rename is now one of those checks, and it turns on the bites items. The bites items share two kinds and many facts with the P cell, so their results are correlated with it. A simulation that draws them independently would misstate how often an A survives. The same holds for F's chance, which the size rule now targets.

### RT-463, choice 8's costs as revised (worth noting)

**Lines:** 1259 to 1291 (choice 8), 1237 to 1250 (choice 6), 545 to 549 (the cap), 1851 to 1862 (the change log).

**1. The pilot, simulated as the design asks** (`strike_sim.out`, `strike_sim_combined.out`). The assumptions:
- Pairing sizes come from the generator's even spread under the 25% cap with half A's pools. That gives the operator kind 13 pairs with capitals, 12 with opposites and 15 with everyday colours under 40 / 40 / 40, and 20, 20 and 20 under 60 / 30 / 30.
- A pair passes the confidence filter if both twins do, independently, at the trial's per-pairing rates.
- Each surviving pair fails a "does not get in the way" check with a chance f, of 0, 5% or 10%.
- A pairing is struck if its failures exceed a fifth of its surviving pairs, and a pairing with none left is lost.
- Margin matching and donor losses are ignored, so the figures are lower bounds on how often the design returns to John.

The results:

| Allocation | Return to John, start, f = 0 / 5% / 10% | Return to John, end, f = 0 / 5% / 10% | Operator pairs kept, start (end), f = 0 |
|---|---|---|---|
| four kinds as built | 100% / 100% / 100% | 100% / 100% / 100% | 7 (9) |
| 60 / 30 / 30 (version 0.10) | 2% / 9% / 29% | 0% / 5% / 24% | 18 (22) |
| 40 / 40 / 40 (version 0.11) | 9% / 15% / 29% | 0.2% / 7% / 22% | 12 (14) |

These count one combined failure chance per pair, as the earlier check did. Counting two independent checks, each at f, raises both choice-8 rows to about 50% at f = 10%.

So at the recommended start placement, 40 / 40 / 40 returns the design about four times as often as 60 / 30 / 30 when the checks rarely fail, and it keeps about a third fewer operator pairs. The reason is the operator's colours pairing, which passes the filter at 5% at the start: with 15 pairs it is empty about half the time.

At the end placement, where the colours pairing passes at 29%, the return rate at f = 0 falls from 9% to 0.2%. Choice 6 recommends the start partly because "choice 8 answers the operator's survival more directly than the placement does" (lines 1249 to 1250). Under the revised choice 8 that is weaker, and the trade should be put to John with these numbers.

**2. The 1 : 1 : 2 option** is rejected because "almost no operator pairs survive". Under the even spread it keeps about 10 to 12 operator pairs against about 17 to 18 for three equal kinds, and it has the largest ceiling and the most survivors (`ceilings.out`). It would make RT-454's arithmetic tie worse, which is a fair reason, but the stated reason is wrong. Either correct the reason or offer the option with its numbers.

**3. The survivor figures** are the survivor-maximising allocation, not the generator's even spread. The low ends of 196 pairs and 133 survivors rest on 13 products, which the split cannot produce (above). State which allocation, and use the products pool the split gives.

**4. The cap's base.** After the filter, sums alone are 35% to 38% of the surviving routine cell under three equal kinds (`arith_share.out`). Say whether the 25% cap applies to the built cell, which it meets, or to the surviving cell. If it applies to the surviving cell, the sums pairs must be cut after the filter, and survivors fall to roughly 125.

### RT-464, the unit range is not close to the trial's difficulty (worth noting)

**Lines:** 701 to 703, 807 to 808.

The trial's half A unit items used a factor of 2 to 5 and a count of 2 to 9. Version 0.11 uses a factor of 2 to 9 and a count of 2 to 12 (`unit_range.out`):
- **Facts:** 81 two-digit facts against 26.
- **Outside the trial's range:** 55 of the 81 facts (68%), including all 28 with an answer above 45, the trial's highest.
- **Mean answer:** 40.0 against 22.1.

So the unit figures the design leans on were all measured on easier problems: 83% to 93% right, a confidence rate of 61% to 100% by pairing, and the one-pass gain behind the forecast of the one-pass condition. So were the survivor estimates of choice 8. The rebuilt pilot will measure the real figures, because both halves now share the range. But "close to the trial's difficulty" should be dropped or marked as unmeasured. The operator kind's shared range is not stated either, and the same applies to it.

### RT-465, stale and inconsistent text (worth noting)

- **Lines 139 to 141:** B and C said to need "the replacement is shown to bite" (RT-458).
- **Lines 318 to 324, section 3:** F's summary omits that the cells must show no excess.
- **Lines 652 to 654:** operator answers "between 0 and 999", against "every right answer at two digits" (line 702).
- **Lines 710 and 718 to 719:** the numeric exemption, and the check on half-A candidates (RT-452 entry above).
- **Lines 921 to 924:** "Of the test half's 270 to 300 pairs, about half would pass the filter", the one remnant RT-456 listed.
- **Line 937 and line 986:** "resampled by item" and "paired resampling of pairs", against resampling by fact (RT-462).
- **Lines 965 to 966:** "With 30 pairs a kind, a tenth is three pairs". The tenth is counted from the pairs left after the confidence filter and margin matching (lines 778 to 780), and under choice 8 a kind has 40 pairs before them.
- **Lines 1040 to 1046 and 1061 to 1062:** "F counts as a definite outcome, like D" in the readings with one kind left out. Those readings ignore the bites check, and "no excess loss counts as D in them" (line 1044), so F can never arise there. The list of definite outcomes, "(B, C or D for an A; A, C or D for a B)", is unchanged.
- **Line 1061:** "C, D, E and F are never renamed by these checks" follows a rule that renames C. Say "by the checks that apply only to A or B".
- **Lines 1141 to 1147, section 9:**
  - Step 1's note ends "version 0.10 answers it", which should now record that the closure check of version 0.10 also found it not ready, and that version 0.11 answers that check.
  - Step 2 says John's rulings were made and further rulings are asked for only when a return-to-John rule fires. But choices 6, 7 and 8 are unruled (section 11 records choices 1 to 5 only), and step 3 cannot be written until choices 6 and 8 are ruled. Step 2 should list them.
- **Lines 1853 and 535:** "products 13 or 23" in the change log, against "about 23 to 27" in the body.
- **Line 1085:** F's sentence says the message "differed from the true message by at least half its size", but the condition is a mean over items (RT-459).

---

## Verdict

**Version 0.11 is not ready for the battery specification and the pilot to be rebuilt (step 3). It needs a version 0.12 first.**

It answers the tenth check's arithmetic well:
- the test-half ceilings are right, and the recommended allocation fits inside what the simulation is expected to ask for;
- the confidence shares, the identity sentence, the time caveats, the placement of the routine gain and the overlap rules are done;
- the systematic last-digit split is gone;
- outcome F is the right kind of answer to RT-449.

But F, the new reading that the prediction failed, is not yet safe to read, and the split's fix holds only on paper. Version 0.12 must:

1. **Require the swap to leave the held-out problems intact for F (RT-457).** Add that the main removal's own loss on the bites items, against the unaltered run, has an interval below a quarter of the one-pass cost under each method. Rewrite F's sentence and the allowed sentence to match.
2. **Fix the disagreement rename (RT-458).** Remove B from it. For A and C, rename only when the operator-and-unit part of P shows an excess while the removal does not bite. Make section 1 say what section 6 requires of B and C.
3. **Define the swap-size ratio and make F's reachability known in advance (RT-459).** Fix the positions, the norm, the normalisation and the blocks, with the measurement starting where item and donor first differ. Report it on the pilot at step 4b under each method, and return to John if it is below 0.5 there.
4. **Match the halves at the level of items (RT-460).** Balance the endings in 0 and 5 across decades, fix item-level tolerances, and fix a model-free seed rule, all before any item exists.

These can go in the same version:
- a per-kind check for F (RT-461);
- the resampling scheme in section 6, and a simulation that models the bites items and the cells together (RT-462);
- choice 8's pilot figures, the 1 : 1 : 2 reason, the allocation behind the survivor counts, and the cap's base (RT-463);
- the unit range's claim (RT-464);
- the stale text (RT-465);
- two definitions under the excess-condition entry (RT-453): "a quarter of the one-pass cost" as a point estimate, and the size rule's target for "does not bite" including the swap-size condition.

Choices 6, 7 and 8 also need John's rulings before step 3, and choice 6 should go to him with the revised choice 8's pilot figures.

The dose question (RT-345) stays open until step 4b, and nothing here bears on it.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **F can be reached by a removal that costs a lot (RT-457).** Confirmed by reading section 5's "does not bite" condition. It bounds only the excess of the main removal's loss over the random comparison's loss. If the swap and the matched random noise both cost the held-out problems heavily, the excess is small and F's condition holds, although the swap took away much of what the passes supply. The author missed this when writing F.
- **Not rechecked by the filer:** the swap-size positions behind RT-459, the seed-by-seed round-number shares behind RT-460, and the strike-count simulation behind RT-463.
- **Where things stand.** The reviewer finds version 0.11 **not ready** for step 3: four serious findings (RT-457 to RT-460), five worth noting (RT-461 to RT-465). The choice 8 ceilings are confirmed within a few pairs. The halves finding (RT-451, with RT-439) stays open until RT-460 is answered. The dose finding (RT-345) stays open until step 4b.
- **A pattern worth John's attention.** This is the third version in a row (0.9, 0.10, 0.11) in which a fix introduced a new serious finding: replacing the lookups exposed outcome D; the bands of five split the last digit; outcome F has a loophole. Each round is cheap, but the design is not converging quickly.
