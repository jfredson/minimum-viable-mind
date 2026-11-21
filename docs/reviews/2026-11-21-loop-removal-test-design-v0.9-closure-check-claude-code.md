*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the eight earlier reviews, nor the three rented runs' findings. It worked read-only in a detached worktree at commit 4dbc4a3, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.9

*Reviewer: a fresh Claude Code session. I did not write the design, version 0.9's changes, the three rented runs, their findings, or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure9-loop-design-2026-11-21` at commit 4dbc4a3 and changed nothing in it; `git status` was clean when I finished. I used only my own scratch folder, `/private/tmp/claude-501/loop-review9-HFx8Wu`, which was empty when I started, and every script and output is there. I did not open, list or use any other scratch or temporary folder, including earlier `loop-review*` folders and any session scratchpad. I downloaded nothing, installed nothing, spent nothing, pushed nothing and made no network calls. New findings are numbered from RT-437.*

---

## What I opened

- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.9 header (lines 1 to 11), sections 1 (lines 100 to 121), 3, 4, 5, 6, 7, 8, 9 and 10 in full, and the change log "from version 0.8" (lines 1538 to 1564).
- **The diff** `git diff 38148b1 4dbc4a3 -- docs/loop-removal-test-design-2026-11-20.md`.
- **The three findings files** in `experiments/10-loop-removal-test/`: `step4a-findings-2026-11-21.md`, `scoring-trial-findings-2026-11-21.md` and `chain-calibration-findings-2026-11-21.md`.
- **The raw results:** `scoring-trial-run-2026-11-21/scoring-trial-results.json` and `chain-calibration-run-2026-11-21/chain-calibration-results.json` in full; the key list of `step4a-run-2026-11-21/step4a-results.json`.
- **The committed batteries:** `batteries/pilot/`, `batteries/trial-instruction-start/` and `batteries/trial-instruction-end/` (`pairs.jsonl`, `donor_only.jsonl`, `neutral.jsonl`, `step3-results.json`), and the item files of `batteries/chain-calibration/`.
- **Code, in part:** `src/build.py` (the instruction, lines 30 and 159 to 194; the operator and unit generators, lines 198 to 233; the routine ranges, lines 296 to 314); `src/scoring_trial.py` in full; `src/step4a.py`, the `run` and `score` functions (lines 91 to 119).
- **The research model's tokeniser and chat template**, read-only, from `.hf-cache.nosync/tml-d24-varloop-research-tokenizer/`.
- **The previous closure check**, `docs/reviews/2026-11-21-loop-removal-test-design-v0.8-closure-check-claude-code.md`, for its form only.

I did not open the battery specification's sections 15 and 16 beyond what the findings files quote, any web page, or anything outside the worktree, the tokeniser folder and my scratch folder.

## What I ran

All under `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`, from my scratch folder. Each script's output is saved beside it.

- `recompute.py`: every per-kind, per-pass accuracy and confidence-filter rate of the scoring trial, weighted by the real number of items in each sub-cell (taken from the pilot's `pairs.jsonl`), and the operator-and-unit gain from one pass to three, raw and normalised.
- `unweighted.py`: the same figures as plain averages of the sub-cell rates, to find where the design's figures come from.
- `pairconf.py`: bounds on how many whole pairs pass the confidence filter in each rule kind. A pair survives only if both twins pass, and the trial saved only per-cell rates, so I give the lowest and highest counts those rates allow, and the count if the twins passed independently.
- `tok.py` and `tok2.py`: with the real tokeniser, the instruction's length, the twins' lengths in all three battery sets, how far the two twins of a pair run apart at the end, and whether the instruction shifts any later token.
- `inline_checks.py`: the step-3 results of the three sets side by side (equal twins, dose ratio, tail shares, absorbable difference, donors); exact ties in the calibration trial's per-item scores; the size of half A's number pools for the operator and unit kinds against what the pilot already uses.
- `power.py`: a simulation of the bites check's second condition at 80, 200 and 400 items. Its assumptions are stated under RT-442 (the sample-size finding) and at the top of the script.

---

## The numbers quoted from the trials (item 1 of the brief)

Accuracy is the share of items right; the normalised scale is (accuracy − 0.20) / 0.80. "Start" and "end" are the two placements of the instruction.

| Figure in version 0.9 | Where | What the raw results give, item by item | Verdict |
|---|---|---|---|
| Routine twins "from 51% to 83% or 84%" at three passes | line 369 | 50.8%, then 83.3% (end) and 84.2% (start) | right |
| Confidence filter "from 24% to 54% or 56%" | line 369 | 23.6%, then 55.7% (end) and 54.3% (start), but over 280 items including the 40 chained lookups, which all fail. Over the 240 pair items: 27.5%, then 65.0% and 63.3% | right as computed, but the wrong base (RT-441) |
| Choice 6: "routine twins 84% and 83%; confidence filter 54% and 56%" | line 1049 to 1050 | start 84.2% and 54.3%; end 83.3% and 55.7% | right, same base caveat |
| Operator kind "from 37% to 47% at one pass to 75% at three" | line 728 | one pass: 36.7% (start), 43.3% (end). Three passes: 73.3% at both | 47% and 75% are wrong as item rates |
| Unit kind "from 53% to 59% at one pass to 86% to 94% at three" | line 729 | one pass: 50.0% (end), 56.7% (start). Three passes: 83.3% (start), 93.3% (end) | all four figures are off by 2 to 3 points |
| Letter-code kind "6% to 19% of prompt-rule items at three passes" | line 770 | 6.7% (start), 20.0% (end) | off by one point |
| Lookup kind "right on every item from one pass" | line 730 | 100% at one, two and three passes in both placements (40% at three passes without the instruction) | right |
| "30 items a kind" | line 731 | 30 prompt-rule items in each kind (operator 7 + 12 + 11; unit 7 + 12 + 11) | right |
| "about 0.3 raw, about 0.4 normalised" (operator and unit together, one pass to three) | line 747 | start: 46.7% to 78.3%, a gain of 0.317 raw, 0.396 normalised. End: 46.7% to 83.3%, 0.367 raw, 0.458 normalised | right for the recommended start placement; understates the end placement |
| "about $4.45 in all" | step 4 note | $3.61 + $0.56 + about $0.28 | right |

**Where the wrong figures come from.** The operator, unit and letter-code figures are plain averages of the sub-cell rates. The sub-cells hold 7, 12 and 11 items, so a plain average weights a 7-item cell like a 12-item one. For example, the operator's 47% at one pass is the average of 71%, 42% and 27%, while 13 of its 30 items (43%) were right. The design quotes these as rates for "the operator kind" on "30 items a kind", which a reader takes as item rates. See RT-441.

---

## New findings

| # | Finding | Grade |
|---|---|---|
| RT-437 | Outcome D's meaning now contradicts the bites check, and D is reached mostly by artefacts that no check catches | serious |
| RT-438 | The three-kind risk is understated: on the trial's own figures the operator kind is at risk too, not just the letter code | serious |
| RT-439 | The two halves differ in difficulty for the operator and unit kinds, so the pilot cannot forecast the bites check on the test half, and that check gates every outcome | serious |
| RT-440 | The rule keeping the bites items' numbers apart from the scored pairs cannot be met in half A for the unit kind | serious |
| RT-441 | Several trial figures are plain averages of unequal sub-cells, and the confidence-filter share is over the wrong base | worth noting |
| RT-442 | The sample-size rule for the bites items aims at the part of the condition that never binds | worth noting |
| RT-443 | The bites items' filters and donor rule are not stated | worth noting |
| RT-444 | "The bites check only gates D" is wrong: its one-pass half gates every outcome | worth noting |
| RT-445 | The trials already show the pass gain running in opposite directions by rule kind, and the design does not say so | worth noting |
| RT-446 | Choice 7 overstates what 16-bit keeps, and leaves out the coarse scores and the ties it brings | worth noting |
| RT-447 | Choice 6's argument is right, but it leaves out what the start placement costs | worth noting |
| RT-448 | Stale text: the run count, the noise-floor reason and the memory figure | worth noting |

### RT-437, outcome D after the change (serious)

**Lines:** 754 to 769 (what the replacement costs), 847 to 848 (outcome D), 884 ("C, D and E are never renamed"), 906 (D's row in section 7), and section 1, lines 113 to 116.

**The problem.** Under version 0.9 the bites items are prompt-rule problems of the operator and unit kinds, in the same form as the prompt-rule cell's operator and unit pairs. So if the bites check passes, the removal has been shown to cost prompt-rule problems. Section 7 still says that outcome D means "The model does not need this input's feedback for either kind of task". When D is reached under version 0.9, that sentence is false by construction, because the bites check has just shown that the model needs the feedback for one kind of prompt-rule problem.

**Version 0.9's account of D is incomplete.** It names two ways to reach D: chance differences between the bites items and the pairs, and dilution by the letter-code and lookup kinds. The second is not a small effect. On the trial's figures, the prompt-rule cell left after the confidence filter will be roughly half lookup pairs (RT-438). The lookup kind is right on every item from one pass, so a removal of the message has little to take away from it. A removal that costs operator and unit items, and nothing else, would then show only about half its effect in the pooled prompt-rule cell. That can put the cell's interval below δ (0.10), which gives D. There is a third way the design does not name. The scored pairs pass the confidence filter, and the bites items may not (RT-443). Items with a large margin are likely to be harder to knock over, so the filtered cell can lose less than the unfiltered bites items.

**No check catches it.** The leave-one-kind-out rule ("Depends on one kind") applies only to A and B (line 884). So a D that comes from an operator-and-unit effect hidden by lookup pairs is never renamed. That pattern is in fact closer to the predicted A, a selective loss on prompt-rule problems. Reporting it as "the prediction failed" would misread the result.

**Weighed against stopping the test.** I would not stop. Task K does the bites check's job for what it claims: under each method it compares the removal with damage-matched random noise on items measured to need the extra passes. A, B and C are still read from the cells, and none of them is moved by the change (RT-444 corrects the one way the bites check reaches them). What is lost is a readable "no excess loss" result. That cost should be stated as a loss, not as D being "harder to reach and narrower".

**What must change in version 0.10.**
1. Either retire D as a definite outcome while the bites items share kinds with a cell, so that a no-excess pattern with a passed bites check is reported under its own name with no reading. Or keep D only when the prompt-rule cell's operator-and-unit pairs, read on their own, also have an excess interval whose upper end is below δ. If they do not, the result is renamed (for example, "the cells and the bites check disagree"), with no reading.
2. Rewrite D's row in section 7, so that it never says the model does not need the feedback for either kind of task while the bites check has shown that it does.
3. Section 5, lines 759 to 763: name all three ways to reach D, and say that the leave-one-kind-out rule does not cover D.

### RT-438, the three-kind risk includes the operator kind (serious)

**Lines:** 770 to 773 (the three-kind risk), 680 to 684 (the strike-count rule), 694 to 696 and 705 (the limit on margin matching), and the change log, line 1558.

**What the trial shows.** A pair stays only if both twins pass the confidence filter: a margin of at least 2.2 at three passes. These are the item pass rates for the prompt-rule items at three passes, and the bounds on whole pairs that `pairconf.py` derives from them (30 pilot pairs a kind):

| Rule kind | Prompt-rule items passing (start / end) | Whole pairs passing, start | Whole pairs passing, end |
|---|---|---|---|
| operator | 27% / 40% | 5 to 8 (about 7 if independent) | 6 to 12 (about 9) |
| unit | 77% / 80% | 21 to 23 | 19 to 22 |
| letter code | 3% / 3% | 1 | 0 to 1 |
| lookup | 100% / 100% | 29 | 29 |

**Why the operator kind is at risk.** Its pairings have 7, 12 and 11 pilot pairs. With the instruction at the start, the operator's prompt-rule items pass the filter at 14% (operator with capitals), 8% (operator with everyday colours) and 18% (operator with opposites). So two of its three pairings will keep one or two pairs each. In a pairing that small, a single failure of the "does not get in the way" checks exceeds "a fifth" and strikes the pairing. The strike-count rule returns the design to John if any rule kind is left with one routine kind or none. That is the likely result for the operator kind. With the letter code also gone, only unit and lookup remain, which is fewer than three, so the design returns to John. Margin matching adds to the risk: the operator's prompt-rule margins run far below its routine twins' margins (its routine items pass at 73%), and matching may not remove more than a third of a kind's pairs.

**What else follows.**
- **The test half.** About 59 of 120 pilot pairs pass the filter (49%). At the test half's ceiling of about 270 to 300 pairs, that leaves about 135 to 150 before margin and swap-size matching. That is at the bottom of the 120 to 200 the sample-size simulation is expected to ask for.
- **The mix.** The surviving prompt-rule cell would be about half lookup, a third unit, a tenth operator, and almost no letter code. That bears on RT-437 and RT-445.

**What must change.** Section 5 should state these pair counts, say that the operator kind (not only the letter code) may fail, and say what is done before step 4b if the rebuilt pilot confirms it. Two possible responses are a larger operator allocation, or accepting a return to John at that point. Choice 6 should carry the operator figures (RT-447).

### RT-439, the halves differ in difficulty, and the bites check rests on it (serious)

**Lines:** 728 to 732 ("These are pilot figures... The check itself is made on half B"), 743 to 748 (the one-pass condition), 829 (stage one), and the operand ranges in section 5 at lines 638 to 642 ("the two halves draw from operand ranges whose answers cannot coincide"). In the generator, `src/build.py` lines 199 and 207 to 209 (operator) and line 219 (unit).

**The problem.** The two halves are split by size of number:
- **Operator, half A (pilot):** operands 2 to 15, answers 10 to 45.
- **Operator, half B (test):** operands 25 to 99, answers 100 to 999. For example, "3 times a, minus b" with a = 87.
- **Unit, half A:** a factor of 2 to 5 times a count of 2 to 9.
- **Unit, half B:** a factor of 6 to 9 times a count of 11 to 99.

So every test-half operator and unit item is harder arithmetic than anything in the pilot. Version 0.9 chose these kinds because, on half A, they rise from about 47% at one pass to about 78% to 83% at three. Nothing measured says what they do on half B. If three-pass accuracy on half B is much lower, the one-pass cost can fall below 0.15. The result is then not testable, for every outcome (stage one, line 829), for a reason unrelated to the loop: the very failure RT-432 warned of for chained lookup. The pilot cannot rehearse this, because by design it uses only half A. The same split already made the pilot's operator and unit pairs easier than the test's. The bites check now turns that into a risk to the gate.

**What must change.** Split the operator and unit pools between halves by a rule that keeps difficulty equal and still stops answers coinciding. One way is to give each half its own answers within the same range by a fixed residue, for example odd answers to one half and even to the other, or interleaved bands of ten. If the size split is kept, the design should say plainly that the bites check's one-pass condition on the test half is untested, and that the pilot's 0.3 to 0.4 gain does not forecast it.

### RT-440, the keep-apart rule cannot be met in half A (serious)

**Lines:** 723 to 725 ("the overlap check keeps their rule content, numbers and invented words apart from the scored pairs and their donors"), 740 (40 unit bites items in the pilot).

**What I counted** (`inline_checks.py`):
- **The unit kind in half A** has only 32 combinations of factor and count, which give 22 distinct answers.
- **What the pilot already uses.** The 30 scored unit pairs use 19 of those combinations and 15 of the answers. Its donor-only pairs, which may reuse content, use 21 combinations.
- **So** 40 unit bites items with numbers apart from the scored pairs and their donors cannot be built. At most 13 combinations and 7 answer values are left.
- **The operator kind in half A** has 611 combinations but only 36 answer values, of which the scored pairs use 17. If "numbers" includes answers, 40 operator bites items cannot be built either without repeating answers among themselves.

**Why the rule may not be needed.** Each item is scored in its own forward pass, with nothing carried between items. So a bites item that shares numbers with a scored pair leaks nothing into it. What matters is that the bites items stay out of the other half, which the half split already ensures.

**What must change.** Narrow the rule to what it needs to protect. For example: no bites item repeats a scored item's rule, facts and routine content all together, and bites items obey the half split like everything else. Or widen half A's unit range. Either must be settled before step 3, because the generator cannot build the pilot as the text now stands.

### RT-441, the trial figures (worth noting)

**Lines:** 369 to 370, 728 to 731, 746 to 748, 770 to 771, 1049 to 1050.

- **Plain averages.** The operator, unit and letter-code figures are plain averages of unequal sub-cells (see "The numbers quoted from the trials" above). The item rates are: operator 37% to 43% at one pass and 73% at three; unit 50% to 57% at one pass and 83% to 93% at three; letter code 7% to 20% at three.
- **The operator's one-pass figure.** With the instruction at the start, the operator kind did not improve from one pass to two (36.7% at both). The whole gain came on the third pass. With 30 items this is noise-sized, but the design's wording ("rose from 37% ... to 75%") hides it.
- **The base of the confidence share.** The 54% and 56% count the 40 chained-lookup items, which version 0.9 removes. Over the pair items the share is 63% and 65%. And what governs how many pairs survive is the share of whole pairs, about 49% (RT-438), which the trial could not give exactly.
- **Per-item results.** The scoring trial saved only per-cell rates, not per-item margins, so the pair-level rate cannot be recomputed from the record. Step 4b should save per-item results, as the calibration trial did.
- **The gain.** "About 0.3 raw, about 0.4 normalised" is right for the start placement (0.32 and 0.40). Give both placements, or say that it is the start figure.

### RT-442, the bites items' sample size (worth noting)

**Lines:** 740 to 744 (the size), 749 to 753 (the condition).

**The condition has two parts:**
1. the main removal's excess loss over the random comparison must be at least half the one-pass cost;
2. that excess's interval must lie above zero.

**What the size rule aims at.** Line 742 sizes the set so that part 2 has an 80% chance of passing when the true excess is exactly half the one-pass cost.

**What I simulated** (`power.py`, 300 to 600 runs a cell). The assumptions:
- three-pass accuracy is 0.78 and one-pass 0.47 (start placement, operator and unit together), so the one-pass cost is 0.39 normalised;
- the model is deterministic per item;
- a removal turns a right item wrong with an item-specific chance, spread either widely or narrowly between items;
- five donors for the swap and twenty draws for the random comparison;
- the random comparison's own loss is 0.05 or 0.15 raw;
- the interval is a normal approximation to the resampling interval.

The results:

| True excess, as a share of the one-pass cost | Part 2 alone (interval above zero), at 80 / 200 / 400 items | Both parts, at 80 / 200 / 400 items |
|---|---|---|
| a quarter | 0.45 to 0.93 / 0.87 to 1.00 / 0.98 to 1.00 | 0.00 to 0.05 at every size |
| a half | 0.95 to 1.00 / 1.00 / 1.00 | 0.45 to 0.52 at every size |
| three quarters | 1.00 / 1.00 / 1.00 | 0.95 to 1.00 / 0.99 to 1.00 / 1.00 |

**What this means.**
- **The interval is never the hard part.** At the effect the rule names, part 2 passes nearly always, even at 80 items. The bar is part 1, the point estimate against half the measured one-pass cost. Exactly at that bar it is a coin toss, whatever the number of items.
- **So 200 is defensible.** It is more than part 2 needs, and the pilot's 80 is enough to measure the one-pass cost to about ±0.15 normalised.
- **But the stated simulation will return a number that means nothing.** Rewrite line 742 so that the simulation finds the smallest number giving an 80% chance that both parts pass when the true excess is a stated amount above the bar. Three quarters of the one-pass cost is one choice. The amount should be written down before step 4b.

### RT-443, the bites items' filters and donors (worth noting)

**Lines:** 720 to 727.

The text says how the bites items are built, but not which baseline checks they pass through:
- **the confidence filter**, which only 27% to 40% of operator prompt-rule items pass;
- **"the rule is needed"**;
- **"the routine fact does not get in the way"**.

If the bites items were kept only when confident at three passes, the one-pass cost measured on them would be inflated by the selection. If they are all kept, about a fifth are already wrong at three passes and cannot lose. Either is workable, but it must be chosen before step 4b, because it changes the one-pass cost and RT-437's third route to D. My recommendation is to keep all of them, score them all, and report the confidence-filtered reading beside it.

The text also says that the bites items get donors "under the pair donor rule". That rule is written for pairs: the length condition and the ban on a donor's right answer appearing among the candidates apply to both twins. Say that for a bites item they apply to the single item.

### RT-444, what the bites check gates (worth noting)

**Lines:** 764 to 765 ("The bites check only gates D") against line 829 (stage one).

The one-pass half of the bites check makes the result not testable for every outcome, including A. Only the second half, the excess over the random comparison, gates D alone. Correct the sentence. This matters more now because of RT-439.

### RT-445, the pass gain runs in opposite directions by rule kind (worth noting)

**Lines:** 728 to 732 and section 6, the "Depends on one kind" rule (lines 858 to 882).

Accuracy from one pass to three, by rule kind (item rates; start placement, with the end placement in brackets):

| Rule kind | Prompt-rule items | Their routine twins |
|---|---|---|
| operator | +0.37 (+0.30) | 0.00 (+0.10) |
| unit | +0.27 (+0.43) | 0.00 (+0.03) |
| lookup | 0.00 (0.00) | +0.27 (+0.37) |
| letter code | −0.13 (+0.03) | +0.10 (+0.13) |

**What this means.** For the operator and unit kinds, the prompt-rule items gain from the extra passes and their routine twins do not. For the lookup kind, the reverse holds. If what the passes supply is what the removal takes away, the operator and unit pairs lean toward A and the lookup pairs toward B. The lookup pairs will also be about half of the filtered cell (RT-438). So a pooled result may land in C or E, or in "Depends on one kind", for a reason the trials already show.

**This does not make the change biased.** Version 0.9 does not cause it, and it does not favour A. But the design should state it beside the kind mix. The committed sample-size simulation should also draw its effects by rule kind, not as one shared gap.

### RT-446, choice 7 and 16-bit (worth noting)

**Lines:** 1053 to 1058 (choice 7), 296 to 299 (the noise floor and its tolerance), 357 (the model's answer).

- **"The weights are the same numbers"** is stated as fact. The step-4a findings said only "should be". The checkpoint stores 4-bit values with a block scale and an outer scale denominator (`w13_weight_outer_scale_denominator`). Dividing by an arbitrary denominator and rounding to 16-bit is not exact in general. So the accurate statement is "the same numbers to within 16-bit rounding". The last four layers use another layout, and the findings do not say how they were unpacked. No accuracy was compared with the native path.
- **The scores are coarse.** The logits come out of the model at 16-bit and are converted to 32-bit only afterwards (`step4a.py` line 99). In the calibration trial's 640 per-item scores, the smallest margin that was not zero was 0.047. That is coarser than the 0.01 tolerance of section 3. So any difference at all between two runs would fail the identity check. That is fine while the runs match exactly, as they did, but the text should say so.
- **Ties.** Exact ties between the right candidate and the best wrong one occurred in 8 of the 640 scores. The sort counted 7 of those 8 as right. The design has no rule for ties (line 357). Add one, for example that a tie counts as wrong, or as a share of the tied candidates. Report how often ties occur at step 4b.
- **Smaller points.** The second model's precision is not addressed. Section 3 still gives "4-bit arithmetic" as a reason two runs may differ (RT-448). The argument for accepting 16-bit is sound for comparisons within the model. Every outcome sentence in section 7 should then name the precision, which "saying so in every report" covers only loosely.

### RT-447, choice 6 (worth noting)

**Lines:** 1048 to 1052.

**The argument for the start placement is right, and measured.** With the real tokeniser and the committed step-3 results:
- the instruction is 9 tokens, and both twins of every pair carry it, so all 120 pairs keep equal lengths in both placements;
- at the start, the only later token that changes is the first word of the body ("In" becomes " In"), which is the same in every item;
- at the start, the dose ratios, tail shares, absorbable difference per position, and donor counts are identical to the pilot's. The tail shares are 0.276, 0.336, 0.165 and 0.171 for the four rule kinds;
- at the end, the tail shares rise to 0.409, 0.468, 0.262 and 0.265, and the difference per position that the 10% limit can absorb falls from 0.36, 0.30, 0.61 and 0.58 to 0.24, 0.21, 0.38 and 0.38.

**What choice 6 leaves out.** The start placement had a cost in the trial, and John should see both sides:
- prompt-rule items at three passes were 66% against 72% at the end;
- operator prompt-rule items passed the confidence filter at 27% against 40%;
- the operator kind gained nothing from the second pass;
- the bites gain was 0.32 against 0.37 raw.

All of these come from 30-item cells. Given RT-438, the operator's survival is the cost that matters.

**One more gap.** Section 5 says that "every scored item, donor and bites item" carries the instruction. The neutral passages do not, as the committed `neutral.jsonl` files show. That is probably right, but say so, because the average method's average and the damage matching are both built on those passages.

### RT-448, stale text (worth noting)

- **The run count, line 942.** It now says "roughly 800 items (300 pairs and 200 bites items)" but keeps "about 330,000 short continuations", which was the figure for 700 items. On the same arithmetic, 800 items give about 400,000. The bites items' donor-only items also need unaltered runs.
- **The noise floor, lines 296 to 297.** It still says "Mixture-of-experts routing and 4-bit arithmetic may make them differ". The runs are at 16-bit, and the noise floor measured 0.0.
- **The memory figure, lines 929 to 930.** It still gives "about 53 GB ... an 80 GB card". Step 4a measured 49.2 GB, with a peak of 50.9 GB, on a 96 GB card.

**Chained lookup.** There is no stale mention left in the design's body. The only mentions of chained lookup are the header (lines 6 to 8) and the deliberate "Why not chained lookup" paragraph (lines 733 to 739). There is no remaining mention of task L, chains of four or more, GraphWalks, or 40 chained items outside the change logs. Section 3's "the one task known to need the loop" is correctly changed (lines 287 to 289). Section 8's code list (line 948) and the pilot's size (lines 798 to 800) are updated.

---

## Verdict

**Version 0.9 is not ready for the battery specification to be rebuilt. It needs a version 0.10 first.** The replacement of chained lookup by the operator and unit bites items is the right call against stopping the test. Chained lookup could not show anything with this model, and task K does the bites check's narrow job under both methods against matched random noise. But four things must change before step 3, because each either makes a reported outcome wrong or stops the pilot being built or forecast.

1. **Outcome D (RT-437).** Retire D while the bites items share kinds with the prompt-rule cell, or require that the cell's operator-and-unit pairs also show no excess before D is read. Rewrite D's row in section 7, and name all three ways to reach it.
2. **The three-kind risk (RT-438).** State that the operator kind is at risk as well as the letter code, with the measured pair counts. Say in advance what happens if the rebuilt pilot confirms it.
3. **The halves (RT-439).** Split the operator and unit pools by a rule that keeps both halves equally hard, or state plainly that the pilot cannot forecast the bites check's one-pass condition on the test half.
4. **The keep-apart rule (RT-440).** Narrow it so that the half-A pilot can be built.

These can be made in the same version: the bites items' filters and single-item donor rule (RT-443), the sample-size target (RT-442), the "only gates D" sentence (RT-444), and the tie rule and the 16-bit wording (RT-446). The other points (RT-441, RT-445, RT-447, RT-448) are corrections to figures and text. The quoted trial figures that are wrong are the operator, unit and letter-code rates at lines 728 to 729 and 770, which are plain averages of unequal sub-cells. The headline gain of about 0.3 raw and about 0.4 normalised holds for the recommended start placement.

The dose question (RT-345) stays open until step 4b, and nothing here bears on it.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **The rule-problem figures (RT-441).** Confirmed. Recomputed from the scoring trial's results, weighting each rule-and-routine group by its number of pilot pairs:
  - operator: 13 of 30 (43%) at one pass and 22 of 30 (73%) at three with the instruction at the end; 11 of 30 (37%) and 22 of 30 (73%) at the start;
  - unit: 15 of 30 (50%) and 28 of 30 (93%) at the end; 17 of 30 (57%) and 25 of 30 (83%) at the start;
  - letter code: 5 of 30 (17%) and 6 of 30 (20%) at the end; 6 of 30 (20%) and 2 of 30 (7%) at the start.

  Version 0.9 quoted plain averages of the groups (for example operator 47% and 75%, unit 86% to 94%). The mistake is the author's and is fixed in version 0.10. The pattern stands: operator and unit gain about 30 to 40 points from one pass to three, and the letter code does not.
- **Not rechecked by the filer:** the number-combination count behind RT-440, the confidence-filter counts behind RT-438, and the simulation behind RT-442. Version 0.10 will recompute each from the committed pilot before relying on it.
- **Where things stand.** The reviewer finds version 0.9 **not ready** for step 3. Four serious findings (RT-437 to RT-440) and the figures of RT-441 must be answered in a version 0.10 first. The reviewer judges that the operator and unit bites problems are the right call rather than stopping the test. RT-442 to RT-448 are worth noting. RT-345 stays open until step 4b.
