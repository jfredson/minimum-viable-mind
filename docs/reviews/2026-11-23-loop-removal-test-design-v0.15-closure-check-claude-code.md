*Filed 2026-11-23 by the session that wrote the design, its fixes, the step-4b code and the margin check, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote none of the design, its fixes, its reviews or its code. It worked read-only in a detached worktree at commit 7b1fdf3, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check of the loop removal test design, version 0.15: the switch to scoring by margin

*I am a fresh reviewer. I wrote none of the design, none of its fixes, none of its reviews and none of its code. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure15-loop-design-2026-11-23` at commit 7b1fdf3, and put every script and output in my own scratch folder, `/private/tmp/claude-501/loop-review15-BgfAua`. I changed nothing in the worktree (`git status` is clean), downloaded nothing, installed nothing, made no network calls and spent nothing. Written 2026-11-23.*

## What I opened

- The version 0.15 header (design lines 3 to 13) and `git diff c9cfa08 7b1fdf3 -- docs/loop-removal-test-design-2026-11-20.md`.
- Section 5's scoring paragraphs (lines 490 to 547), and every place the diff touches: the bites one-pass condition (lines 1039 to 1048), the simulation's conditions (lines 1179 to 1185), δ in section 6 (line 1217), section 9's order of work (lines 1386 to 1392 and 1432 to 1437), the note on the margin ruling in section 11 (lines 1612 to 1615), and the change log "from version 0.14" (lines 2312 to 2329).
- For context: section 1 (lines 157 to 211), section 3 (lines 255 to 403), section 4 (lines 405 to 486), the baseline checks, matching and the bites check in section 5 (lines 884 to 1185), section 6 (lines 1212 to 1314) and section 7 (lines 1316 to 1344).
- John's ruling, `docs/rulings/2026-11-23-loop-removal-test-margin-scoring-ruling.md`.
- The margin check: the write-up `experiments/10-loop-removal-test/margin-power-check-2026-11-23.md`, the script `src/margin_power_check.py`, and its output `step4b-rerun-code-test-2026-11-23/margin-power-check.json`.
- The simulation code `src/step4b_simulate.py`, the part of `src/step4b_analyse.py` that builds the simulation's inputs (lines 253 to 271), and the code-test analysis `step4b-rerun-code-test-2026-11-23/step4b-analysis.json`.
- The rehearsal data `step4b-run-2026-11-23/items.jsonl` (320 item records) and the pilot it ran on, `batteries/pilot-v0.12/` (pairs and bites items).

## What I ran

All with `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`, from my scratch folder, importing the committed simulation code read-only.

- `recheck.py` (output `recheck.json`). It rebuilds the margin check's 72 pairs and recomputes: the conversion constant K; K by rule kind and by cell; a 10,000-draw bootstrap of K, resampling by pair and, in the unit kind, by multiplication fact; the ratio of K computed on two random halves of the pilot; the ratio of nats lost to normalised accuracy lost under every condition; the real spread of each cell's excess loss (main removal minus its comparison) and of the gap, against the spread the simulation assumes; observed t statistics of real contrasts on both scales, which need no K; how many items stay right while losing a large margin; starting margins by cell; and the bites constant K_b by kind, with bootstrap intervals.
- `resample_power.py` (output `resample_power.json`). The power of outcome A from **resampled real per-pair excess losses**, not normal draws. Both methods are read on the same resampled pairs, so their real correlation is kept. The losses are centred within each pairing, a gap is planted on the prompt-rule cell, and the outcome is read with every rename by kind, using the committed `outcome_with_renames`. It is run on both scales, at gaps of 0.20 and 0.10, with K fixed and with K drawn as a 72-pair pilot would give it. It also runs the bites one-pass condition for the unit-alone branch with K_b fixed and with K_b drawn from a noisy 80-item pilot. 1,000 runs per cell.
- `extra.py` (output `extra.json`). A stress test of A's power with the comparison not subtracted at all, as if the rerun's comparisons carried no information; and the bites conditions' ratios (own loss and excess, as shares of the one-pass cost) on both scales.

## Results for each item

### 1. The ruling

The ruling file is short and clear. John was asked "Switch the test to margin scoring in a version 0.15?" and answered "Yes, write 0.15". It covers the outcome measure, keeps choice 1, the confidence check, the interference checks by accuracy and "the outcomes' order and meanings", and says that restating the thresholds is the author's design.

The design writes this in faithfully. The margin's definition at lines 507 to 510 matches the one the ruling records. The confidence and interference checks are left on their old footing (lines 546 and 547). The scale, K, its anchor and its return to John are marked as the author's at lines 520 and 1612 to 1615, and in the change log.

Three things are not marked, or do not match the ruling's words:
- **How a condition's margin is formed is the author's choice, but it sits under "John's ruling".** The average of the margins over the donors and over the comparison's draws, and the margin of the fewer-passes run (lines 511 to 515), are reasonable, but they are design choices. So are the quantile reporting (line 543) and the claim that "every threshold keeps its number" (line 533), which sits in the author's paragraph but is not listed among the author's additions in section 11. This goes into the stale-text finding (RT-511).
- **"The outcomes' order and meanings" are unchanged in the ruling's words, but their meanings shift.** A removal can now win outcome A without changing which answers are right (item 2). That follows from John's ruling, not against it, but the design should say it plainly (RT-508).
- The header (line 7) quotes the check's 11 to 64% for right-or-wrong scoring. My resampling with real losses puts it lower still (item 5). That does not weaken the case for the ruling.

### 2. The margin measure

**Well defined in most places.** Taking the margin among the five candidates or from the whole vocabulary gives the same number, as line 509 says, because both subtract the same constant from every candidate. A tie for the top gives 0, consistent with the formula. Under the swap the donors' margins are averaged, and under a comparison the 20 draws' margins are averaged. Both are linear, so the item's loss is the average of its losses. Fewer passes uses the one- or two-pass run. On the data, every condition's record carries a margin, including the fallback.

**Gaps.**
- The loss definition names the swap, the comparisons and fewer passes, but **not the average method or its fallback** (lines 511 to 515). The meaning is obvious, but the code will be written from this list.
- Line 513 says "over its five donors", but section 3 (lines 320 to 323) uses all eligible donors when fewer than five exist.
- Both go into RT-509.

**The confidence check (margin of at least 2.2) and the interference checks (by accuracy) interact correctly.** They are selection rules applied at three passes. Because the model is deterministic at 16-bit (the noise floor was 0.0 at step 4a), selecting on the unaltered margin does not create a pull back toward the average in the loss. The bites items are not filtered, and 14 of the 40 operator bites items start with a negative margin. That is allowed, and the margin handles it.

**A margin loss can be large while every answer stays right.**
- **At one pass:** 62 of the 72 prompt-rule items stayed right, and 20 of those lost at least 0.20 in the design's units. In the routine cell, 24 of 57 did.
- **Under the removals:** nearly every item is pushed to about chance, so few stay right: 8 prompt-rule items under the swap and 14 under the average, and almost all of those lost at least 0.20.
- **What that means for the outcomes:** A, B, C, D and F now describe losses in how strongly the model prefers the right answer, not in how many answers it gets right. Section 1 still states the prediction as "flexible handling of anything new collapses" (lines 161 and 162). Section 7's sentences say "cost more on problems solved from a rule" (line 1325), which a reader will take to mean wrong answers. That is RT-508.

**The scale's link to the item's starting margin.** Because the removals flatten items to about chance, an item's loss under the main removal mostly measures how confident it was to start with.
- **The size of the link:** the correlation between the starting margin and the swap's loss is 0.84 in the prompt-rule cell and 0.63 in the routine cell.
- **Under the swap, the comparison cancels it:** the swap's loss and its comparison's loss correlate at 0.91 per item, and subtracting one from the other removes the starting margin.
- **Under the average, it does not:** that correlation is only 0.12. So a difference in starting margins between the cells passes straight into the gap.
- **What limits it:** margin matching holds each rule kind's two cell means within 0.5 nats, which bounds this at about 0.02 in the design's units, a fifth of δ.
- **How much it matters:** before matching, the unit kind's cells differed by 2.0 nats (7.1 against 9.1), so the matching step now carries more weight than it did. That is RT-512.

**Sections 1, 6 and 7.** Section 6 needed no rewording, because it is written in losses and intervals. Sections 1 and 7 are covered above. Section 3 (lines 384 to 388) and the section 4 table (line 412) still say that fewer passes decide no outcome. Yet the one-pass run on the pilot now sets the scale of every threshold (RT-511).

### 3. The scale K

**Can it be computed?** Mostly. K is the prompt-rule items' mean one-pass loss in margin, divided by their mean one-pass loss in normalised accuracy, on the pilot at the step-4b rerun (lines 524 to 526). Three things are left open:
- **Which items count.** It says "the prompt-rule items that survive the baseline checks". That could mean before or after margin matching and swap-size matching, and could mean only pairs whose routine twin is also confident. The check used 72 pairs before matching, while the code-test analysis's simulation inputs use the 61 left after margin matching.
- **Which passes.** One pass against three. That is clear.
- **A denominator near zero.** It is handled only by "an interval that reaches 0" (lines 531 and 532).

**I recomputed the anchor on step 4b's data.** One-pass loss: 0.174 in normalised accuracy and 4.19 nats, so K = 24.1. That matches the check.

**But K is the ratio of a precise number to an imprecise one.**
- **The two numbers:** the one-pass margin loss has a t statistic of 13.9, while the one-pass accuracy loss, a right-or-wrong count on 72 items, has one of 3.4.
- **The uncertainty this gives K:** its 95% bootstrap interval is 14.4 to 64.2 nats, a factor of 4.5. The accuracy loss's own interval, 0.067 to 0.30, does not reach 0, so the return-to-John rule would let it through.
- **A K measured on other data:** K computed on one random half of the pilot, divided by K on the other half, ranges from 0.25 to 3.65 (95%).

**What a different K does to the thresholds.** δ = 0.10 means 0.10 × K nats. With K anywhere in its interval, δ is anywhere from about 1.4 to 6.4 nats.
- **If the pilot's K is too high:** a real gap reads small, and R's "upper end below δ" becomes easier to meet.
- **If it is too low:** δ shrinks, so D becomes harder to reach and C easier.
- **The effect on power:** with K fixed at its true value, a true gap of 0.20 is read as A in 99.5 to 100% of runs from 80 pairs (resampled real losses). With K drawn as a 72-pair pilot would give it, A is read in 92 to 94% of runs, **and that does not rise with the test half's size**. The error in K is not reduced by more test pairs, so it sets a ceiling on power. The ceiling is still above 80%, but it is a cost the design does not state.

**K depends on which kinds are in the cell.**
- **Lookup prompt-rule items** lose 2.75 nats at one pass and no accuracy at all.
- **Unit items** lose 5.98 nats and 0.39 in accuracy, a ratio of 15.3.
- **Pooled**, the ratio is 24.1, so it is inflated by lookup's confidence-only loss.
- **What follows:** K is not "what one unit of accuracy is worth in margin". It is a mix-weighted ratio, and it will move when the simplified operator kind enters the rerun pilot.

**Fixing K on half A and applying it to half B** is sound in principle, because a constant fixed before the test data cannot be tuned to them. The trouble is not where K is fixed but how noisy the quantity fixed is.

**Does dividing by K keep δ and the gap's meaning?** Only at the anchor. On step 4b's data, the nats lost per unit of normalised accuracy lost were:

| Condition | Prompt-rule cell | Routine cell |
|---|---|---|
| One pass | 24.1 | 20.8 |
| Two passes | 58.2 | 43.1 |
| Swap | 11.6 | 12.9 |
| Average | 11.4 | 11.8 |
| Fallback | 11.1 | 11.9 |
| In-loop comparison, swap | 10.7 | 13.9 |
| In-loop comparison, average | 16.7 | 15.4 |

So the swap's loss on the prompt-rule cell reads 0.45 in "accuracy-equivalent" units, while its normalised accuracy loss was 0.93. The two figures the design reports side by side (line 544) would contradict each other by a factor of two. The thresholds are new thresholds on a new measure, chosen by carrying the old numbers over. That may be fine, but it is not "the same share" of anything except the one-pass loss (RT-507).

**One K shared by both cells is right for the gap,** because G = P − R is only a difference of like quantities if both cells are in nats divided by the same constant. Separate constants would mix units. The routine cell's own pooled ratio (20.8) is close to the prompt-rule cell's (24.1), but its per-kind ratios are not: 18.9 for lookup and 47.2 for unit. "Accuracy-equivalent" is therefore not true of the routine cell at all, which is one more reason to rename the unit (RT-507).

### 4. The bites constant K_b and the bites conditions

**The one-pass condition of 0.15** (lines 1039 to 1048). On the pilot, dividing by K_b makes the bites set's one-pass cost in K_b units equal to its accuracy cost, by construction. The check's output shows this: 0.28125 and 0.25 on both scales. So the pilot-level reading of the condition is the old right-or-wrong point estimate (40 items a kind), given a spread from the margin.

On the test half, the condition asks that the test's one-pass margin loss be at least (0.15 ÷ the pilot's accuracy cost) times the pilot's margin loss. So it has become a check that half B's margin gain is not much smaller than the pilot's, scaled by a right-or-wrong count on the pilot.

**What K_b's noise does to the gate.**
- **How noisy K_b is:** for the unit kind it is 23.7, with a 95% bootstrap interval of 13.6 to 62.1 on 40 items.
- **The pass rate:** in my resampling for the unit-alone branch (200 test items over 29 facts), the condition passes in 99.9% of runs with K_b fixed. With K_b drawn from an 80-item pilot it passes in 88.8%.
- **Why:** the threshold in nats ranges from 2.5 to 5.9 (5th to 95th percentile).
- **What failing costs:** this condition gates every outcome. A fail makes the result "not testable", so about one run in nine would end that way from pilot noise alone.

**K_b is circular, and the check did not compute it as the design says.** The design computes K_b "from the bites items in the branch that is chosen" (lines 527 and 528). But the branch is chosen by a simulation that needs the losses already in K_b units. The check's script sidesteps this with a separate K_b for each kind (operator 6.45, unit 23.7). Pooled over the "both kinds" branch, K_b would be 14.6.
- **Why the operator's is so low:** a third of its bites items start with a negative margin.
- **Where the difference shows:** the "does not bite" and "bites" conditions are ratios, so the choice does not touch them. It does touch the pooled one-pass gate and its spread.
- **What it means for the code:** the code cannot be written until this is settled (RT-509).

**"Half", "three quarters" and "a quarter" are right as arithmetic.** Both sides are in the same units, so K_b cancels. They are not the same conditions as before, though. Because the removals flatten items while one pass only weakens them, a removal's loss as a share of the one-pass cost roughly halves on the margin. On the pilot:

| Bites set and method | Own loss ÷ one-pass cost, accuracy | Own loss ÷ one-pass cost, margin | Excess ÷ one-pass cost, accuracy | Excess ÷ one-pass cost, margin |
|---|---|---|---|---|
| Operator, swap | 2.06 | 1.95 | 0.22 | 0.31 |
| Unit, swap | 2.92 | 1.43 | −0.09 | 0.01 |
| Unit, average | 3.88 | 1.55 | 0.67 | 0.06 |

So "half of the one-pass cost" is a different bar on the margin, and the direction differs by kind and method. The unit kind under the average method would have passed "bites" on accuracy (0.67, above one half) and fails it badly on the margin (0.06). This is not an error, because the conditions now apply to a new measure by ruling. But the design's sentence "which are ratios and need no conversion" (lines 537 and 538) implies they mean what they meant, and they do not (RT-507).

### 5. The margin check itself

**Recomputed from the raw data, these match.**
- 72 pairs, K = 24.13.
- The margin spreads: 0.166, 0.146, 0.148 and 0.129, which the write-up gives as 0.17, 0.15, 0.15 and 0.13.
- The accuracy spreads: 0.449, 0.472, 0.495 and 0.575. The write-up's 0.50 and 0.58 are rounded up from 0.495 and 0.575.
- The swap loss quantiles, 0.149 to 0.695.
- The power figures, which I read from the output file.

**Its method has four faults. They cut both ways, and the conclusion survives them.**
- **The comparison's spread is divided by the square root of 20 twice.** `step4b_analyse.py` (lines 265 to 270) and `margin_power_check.py` (line 68) already average each item's 20 draws before taking the spread across items. `step4b_simulate.py` (line 89) then divides that spread by √20 again. This shrinks the comparison's per-item spread about 4.5-fold. It is older than version 0.15, it affects both scales, and it was not raised by the earlier reviews I searched.
- **The main removal and its comparison are drawn independently.**
  - **Under the swap:** they correlate at 0.91 per item on the margin, so the real spread of the excess is 0.072, not the 0.168 the simulation uses. The simulation is cautious here.
  - **Under the average:** the two cells' excesses correlate at −0.64, so the real spread of the gap is 0.29, not 0.20. The simulation flatters the margin here.
  - **On the old right-or-wrong scale, under the average:** the real gap spread is 1.05 against 0.78 assumed, so it flatters accuracy too.
- **The normal draws ignore the tails, and the 72 pairs are taken before margin matching** (61 after it).
- **The bites figures for the one-pass condition (100%) are partly true by construction** (item 4). They ignore K_b's error.

**My own check, with resampled real per-pair losses** (`resample_power.json`): A is read under both methods in

| Test-half pairs | 80 | 140 | 200 | 260 |
|---|---|---|---|---|
| Right or wrong, real losses | 3.6% | 5.3% | 6.9% | 6.3% |
| Margin, real losses, K fixed | 99.5% | 100% | 100% | 100% |
| Margin, real losses, K from a noisy pilot | 91.9% | 92.8% | 93.9% | 93.3% |
| Margin, true gap 0.10 (at δ), K fixed | 28.5% | 29.6% | 26.5% | 25.8% |

With no planted gap, A was never read on the margin (0 of 1,000 at 80 and at 200 pairs).

**A stress test.** With the comparison not subtracted at all, as if the rerun's comparisons, matched properly on the reply rendering, carried no information, A is still read in 98.6% of runs at 80 pairs and 99.5% at 140.

**A check that needs no K.** It compares the t statistics of real contrasts on step 4b's data, so it does not rest on the conversion at all. The margin's are higher in every case:

| Contrast | Accuracy | Margin |
|---|---|---|
| One-pass loss, prompt-rule cell | 3.4 | 13.9 |
| Two-pass loss, prompt-rule cell | 2.1 | 19.6 |
| Swap loss, routine cell | 14.0 | 24.1 |
| Average loss, routine cell | 12.7 | 27.4 |

**Is the conclusion sound?** Yes. The margin does fix the power problem, and right-or-wrong scoring is worse than the check said. The parts of the check that flatter the margin, the normal draws and the independence of the average's two cells, are outweighed on the real data. The one real cost it does not state is K's error, which caps A's power at about 93% and the bites gate's at about 89%. Both are above 80%, but they come from the anchor, not from the test's size. The check's caveat that "a different anchor would give different numbers, though not a threefold change in the spread" understates how wide the anchor's error is: the anchor's own interval spans a factor of 4.5.

### 6. New problems, and stale text

- **Line 1163** still says "a true normalised gap of 0.20". It should be the margin units of section 5.
- **Lines 1165 to 1170** quote the old simulation sizes (about 120 and 200 pairs), which were measured on the right-or-wrong scale. They are history now, and line 1180 supersedes them. A short note would stop a reader taking them as current.
- **Lines 1045 to 1047** reason that the one-pass gate "is expected to be met" from accuracy figures. On the pilot that is now true by construction of K_b, and on the test half it rests on K_b.
- **Section 3 (lines 384 to 388) and the section 4 table (line 412)** say fewer passes decide no outcome, but the pilot's one-pass run now sets the scale of every threshold.
- **The section 11 note on the author's additions** (lines 1617 onward) covers versions 0.13 and 0.14 only. Version 0.15's own additions are not listed there: the averaging rules, "every threshold keeps its number", the quantile reporting and the anchor rule.
- **The simulation's docstring** (`step4b_simulate.py`, line 28) says "Items are scored right or wrong". That is code to be rewritten, and is noted for the specification.
- **"Normalised scale" in other places** (lines 236, 241, 355, 361 and 365) refers to the readers' normalisation of the block sums, not to accuracy, and is correct. Line 1046's "about 0.4 on the normalised scale" describes past accuracy figures and is correct as history.

## Findings

**The anchor finding (RT-506). Serious.**
- **What it concerns:** lines 520 to 532 (K and K_b, "If the anchor fails"), and through them line 1217 (δ), lines 1039 to 1048 (the bites one-pass condition) and lines 1179 to 1185 (the simulation).
- **The problem:** K is fixed by dividing a precise margin loss by a right-or-wrong loss, which is exactly the noisy count the change was meant to leave behind. On step 4b's data its 95% interval runs from 14 to 64 nats, and K on one half of the pilot against the other ranges over a factor of 0.25 to 3.65. Yet the return-to-John rule, which fires only if the accuracy loss's interval reaches 0, lets it through.
- **What follows:** δ means anything from about 1.4 to 6.4 nats. A's power is capped at about 93% whatever the test half's size. The bites gate, which decides "not testable" for every outcome, fails in about 11% of runs from pilot noise alone.
- **A second cause of drift:** K also depends on the mix of kinds. Lookup items lose margin at one pass but no accuracy, so the pooled 24.1 sits well above the unit kind's own 15.3, and K will move when the operator kind returns.
- **What would fix it:** anchor the thresholds on the margin alone. For example, state δ, the gap and the bites condition's 0.15 as fixed shares of the pilot's one-pass margin loss (a quantity with a t statistic near 14). Alternatively, fix K in nats now from step 4b's data before the rerun. Failing either, require K's interval to lie within a stated factor and return to John otherwise. Whichever is chosen also needs:
  - the item set named exactly;
  - the circularity of K_b and the branch choice resolved (see RT-509);
  - the residual cost written into the simulation.
- **Who decides:** carrying the old numbers over unchanged sets the effect size the test is built to find, so the choice should be put to John.

**The units finding (RT-507). Serious, because reported figures would mislead. It is a wording fix.**
- **What it concerns:** lines 520 to 523 ("accuracy-equivalent margin units", "the same share of what the extra passes supply on either scale"), lines 533 to 538 ("every threshold keeps its number", ratios that "need no conversion"), line 1040 and line 1217.
- **The problem:** the units equal accuracy only at the one-pass anchor. Under every removal and comparison, one unit of accuracy is worth 11 to 17 nats, not 24. So the swap's loss reads 0.45 "accuracy-equivalent" units beside a real normalised accuracy loss of 0.93. And the bites ratios move by up to a factor of ten: the unit kind's excess under the average was 0.67 of the one-pass cost in accuracy and 0.06 in margin.
- **What would fix it:**
  - rename the units, for example "margin units scaled to the one-pass loss";
  - say that δ, the gap and the bites conditions are new thresholds on a new measure, chosen by carrying the numbers over, and mark that as the author's;
  - report each threshold's value in nats beside it.

**The wording finding (RT-508). Worth noting.**
- **What it concerns:** lines 161 and 162 (section 1's "collapses"), lines 170 to 172, and the outcome sentences at lines 1325 to 1329.
- **The problem:** an outcome can now be reached by losses in the model's preference for the right answer with no change in which answers are right. At one pass, 20 of the 62 prompt-rule items that stayed right lost at least 0.20 units. Section 7's "cost more on problems solved from a rule" will be read as more wrong answers.
- **What would fix it:**
  - say in section 1 what the measure is;
  - word section 7's sentences as a loss in how strongly the model favours the right answer;
  - require the gap in accuracy to be reported beside any outcome.

**The definitions finding (RT-509). Worth noting, to be settled in the specification or version 0.16 before the code is written.**
- **What it concerns:** lines 511 to 515 and 524 to 528.
- **The gaps:**
  - the loss definition omits the average method and its fallback;
  - "five donors" ignores section 3's rule that all eligible donors are used when fewer than five exist;
  - "survive the baseline checks" does not say whether margin matching and swap-size matching come before K. The check used 72 pairs and the analysis 61.
- **The circularity:** K_b is taken "from the bites items in the branch that is chosen", but the branch is chosen by a simulation that already needs K_b. The check's script used a separate K_b for each kind (6.45 and 23.7), not the design's single constant (14.6 if pooled).

**The margin check's method (RT-510). Worth noting. The conclusion stands.**
- **What it concerns:** `src/step4b_simulate.py` line 89, `src/step4b_analyse.py` lines 265 to 270, `src/margin_power_check.py` lines 68 and 110 to 114, and the write-up's caveats.
- **The faults:**
  - the comparison's spread is divided by √20 twice. This is older than version 0.15 and affects both scales;
  - the main removal and the comparison are drawn independently, and so are the two cells, while the real correlations are 0.91 under the swap and −0.64 between the cells' excesses under the average. So the simulation is too cautious under the swap and too generous under the average;
  - the 72 pairs are taken before margin matching;
  - the bites one-pass condition's 100% is true by construction and ignores K_b's error.
- **Why the conclusion stands:** resampling real losses confirms it. The margin reads A in 99.5 to 100% of runs from 80 pairs with K fixed, while right-or-wrong scoring reads it in only 4 to 7%.
- **What would fix it:** the committed simulation for the rerun should resample real per-pair losses, keeping the two methods and the two cells joint, rather than draw normal variables.

**Stale text and marking (RT-511). Worth noting.**
- **What it concerns:** line 1163 ("normalised gap"), lines 1165 to 1170 (old sizes on the old scale), lines 1045 to 1047, lines 384 to 388 and line 412 ("fewer passes ... not used for any outcome"), the section 11 note on the author's additions (lines 1617 onward), and the simulation's docstring.
- **The problem:** version 0.15's own choices, namely the averaging rules, "every threshold keeps its number", the quantile reporting and the anchor rule, are not listed as the author's.

**Starting margins and margin matching (RT-512). Worth noting.**
- **What it concerns:** lines 939 to 943 (margin matching to within 0.5 nats) and the loss definition.
- **The problem:** under the margin, the main removal's loss tracks the item's starting margin (correlation 0.84 in the prompt-rule cell under the swap), because the removals push items to about chance. The swap's comparison cancels this. The average's does not (correlation 0.12), so the 0.5-nat tolerance passes up to about 0.02 units, a fifth of δ, straight into the gap. Before matching, the unit kind's cells differed by 2 nats.
- **What would fix it:** state this, and report the gap's sensitivity to starting margins. A tighter tolerance or an adjustment for starting margin is the author's call.

## Verdict

Nothing is fatal. The switch to the margin is well supported: on the real data, with real tails and real correlations, it turns an outcome the test could not read into one it reads nearly every time. John's ruling is written in faithfully.

Version 0.15 should still get a **short version 0.16 before the margin analysis code is written**, because the code's central constant is not yet defined in a way that does what the design says it does. Exactly what must change:

1. **The anchor finding (RT-506).** Replace K's anchor, and the "interval reaches 0" rule, with one that does not rest on a right-or-wrong count. One way is to state δ, the gap and the bites condition's 0.15 as fixed shares of the pilot's one-pass margin loss, or to fix the constants in nats now from step 4b's data. Name the exact item set, resolve K_b's circularity with the branch choice, and put the choice of carried-over effect sizes to John.
2. **The units finding (RT-507).** Drop "accuracy-equivalent" and "keeps its meaning", say the thresholds are carried over by number onto a new measure, and report each in nats.
3. **The wording finding (RT-508).** Reword sections 1 and 7 for what the margin measures, and report the accuracy gap beside every outcome.

These can be carried into the specification instead of version 0.16:
- **The definitions finding (RT-509):** the average and fallback in the loss definition, the donor count and the filter order.
- **The margin check's method (RT-510):** a committed simulation that resamples real losses jointly and drops the double √20.
- **Stale text and marking (RT-511).**
- **Starting margins and margin matching (RT-512).**

**Pricing the rerun need not wait.** The pilot and the collection are unchanged by any of this. K and K_b are computed after the rerun, from data it collects anyway, so the price does not depend on how they are defined.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-23. It closes nothing.*

- **K's range (RT-506).** Confirmed in substance. Resampling the 72 surviving prompt-rule items 5,000 times gives K a 95% range of about 15 to 51 nats around its estimate of 24. The reviewer's 14 to 64 used its own resampling. Either way, K is set by a noisy count of right answers, and the "interval reaches 0" rule does not catch that.
- **The double division (RT-510).** Confirmed by reading the code. `src/step4b_simulate.py`, line 89, divides the comparison's spread by √20. That spread comes from `step4b_analyse.py` as the spread across items of the 20-draw average, so it is already averaged. The bug is the author's, from the first version of the simulation. The reviewer's resampling of real per-pair losses, which has no such bug, still finds margin scoring's power at 99.5 to 100% from 80 pairs.
- **Not rechecked by the filer:** the reviewer's resampled power figures, the bites gate's 11% failure from pilot noise, and the starting-margin figures of RT-512.
- **Where things stand.** Nothing is fatal, and the margin fixes the power. A short version 0.16 is owed before the margin analysis code is written. It must replace K's anchor, putting the carried-over effect sizes to John; drop the "accuracy-equivalent" wording; and reword sections 1 and 7. Pricing the rerun can go ahead now, because the pilot and the collection do not change.
