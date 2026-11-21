*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the nine earlier reviews. It worked read-only in a detached worktree at commit 600d0bb, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.10

*Reviewer: a fresh Claude Code session. I did not write the design, version 0.10's changes, the three rented runs, their findings, or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure10-loop-design-2026-11-21` at commit 600d0bb and changed nothing in it; `git status` was clean when I finished. I used only my own scratch folder, `/private/tmp/claude-501/loop-review10-5XrAhL`, which was empty when I started, and every script and output is there. I did not open, list or use any other scratch or temporary folder, including earlier `loop-review*` folders and any session scratchpad. I downloaded nothing, installed nothing, spent nothing, pushed nothing and made no network calls. New findings are numbered from RT-449.*

---

## What I opened

- **The closure check of version 0.9**, `docs/reviews/2026-11-21-loop-removal-test-design-v0.9-closure-check-claude-code.md`, in full. I treated its filer's check as the author's note, not as part of the review.
- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.10 header (lines 1 to 20); sections 1 (lines 87 to 134), 3 (lines 280 to 324), 5 (lines 363 to 906), 6, 7, 8, 9 and 10 in full (lines 908 to 1186); and the change log "from version 0.9" (lines 1689 to 1726).
- **The diff** `git diff 4dbc4a3 600d0bb -- docs/loop-removal-test-design-2026-11-20.md`, in full.
- **Raw results:** `scoring-trial-run-2026-11-21/scoring-trial-results.json` (every per-cell rate and confidence share, all three sets); `chain-calibration-run-2026-11-21/chain-calibration-results.json` (the 640 per-item scores); `step4a-run-2026-11-21/step4a-results.json` (timing, noise floor, identity and bypass, memory).
- **The pilot set**, `batteries/pilot/` (`pairs.jsonl`, `donor_only.jsonl`, `build-report.json`, `step3-results.json`), and the step-3 results of `batteries/trial-instruction-start/` and `batteries/trial-instruction-end/`.
- **Code:** `src/build.py` in full; `src/check_overlap.py` in full; `src/step4a.py`, the `run`, `score` and `sweep` functions and the timing.
- **The research model's tokeniser and chat template**, read-only, through the generator's own `Model` class.

I did not open the battery specification, the findings files beyond the lines that give run times, any web page, or anything outside the worktree, the tokeniser folder and my scratch folder.

## What I ran

All under `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`, from my scratch folder. Each script's output is saved beside it as a `.out` file.

- `recompute.py`: every rule kind's accuracy at one, two and three passes, and its count of items passing the confidence filter, for both twins, weighted by the real number of pilot pairs in each pairing (from `pairs.jsonl`).
- `lookup_sub.py`: the same rates pairing by pairing, for the lookup kind's routine twins and the operator and unit kinds.
- `strike_sim.py`: a simulation of the strike-count rule at step 4b, with the present allocation and with choice 8, at both placements of the instruction. Its assumptions are stated at the top of the script and under RT-438 below.
- `pools.py`: half A's and half B's routine pools (one-token capitals, opposite questions, everyday objects), counted by the generator's own `Builder` with the real tokeniser.
- `testhalf.py`: the largest test half that the 25% cap on each routine kind allows under choice 8, and the pairs expected to pass the confidence filter.
- `bands.py`: the bands of five applied to the operator, unit, sum and product kinds under several shared operand ranges: pool sizes, distinct answers, mean answers, last digits, operand parity, how often the place-first candidate rule can be met, and operator operand pairs that fall in both halves.
- `ties.py`: exact ties and the smallest non-zero margins in the lookup calibration trial's 640 per-item scores.

---

## The earlier findings, one by one

### The outcome D finding (RT-437): closed with conditions

**What version 0.10 did.** Outcome D is now reported as "No excess in the cells", with no reading, while the bites items share kinds with the prompt-rule cell (section 6, lines 941 to 944; section 7, line 1002). Section 5 names the three ways to reach D and says the "Depends on one kind" rule does not cover D (lines 812 to 828). Section 7's last paragraph now names B or C, not D, as what would count against H1 (lines 1014 to 1016).

**Is it coherent with section 6?** Yes, on the mechanics.
- The order of outcomes is unchanged: A, B, C, D, then E. D is still a pattern (R and P both below δ) with a gate (the bites check), so every case still lands in exactly one outcome.
- The "Depends on one kind" rule still treats D as a definite outcome in the readings with one kind left out (lines 959 to 966). That remains right. There D is used as a pattern ("with this kind left out, no excess is left"), not as a reading, and that pattern is exactly what shows an A was carried by one kind. Giving D no reading as a final outcome does not change what it does as a test inside the renaming rule.
- "C, D and E are never renamed" (line 980) is harmless, because a D with no reading has nothing to rename.

**What is left saying D is a failure, or near it.** Nothing says it outright. But two places still lean on the old meaning:
- **Section 1, lines 125 to 130.** The new sentence about D was put before the old one, so "That is a result against the placement, not against H1 itself" now follows "outcome D gives no reading". A reader takes "That" to mean D. It should point at B and C, so the sentence must be moved back above the D sentence or its noun written out.
- **Section 7, lines 1009 to 1012.** The one sentence allowed in advance is tied to D: "on the paired questions, what the extra passes supply survived a message built from other inputs of the same kind". But D is reached only when the bites check passed, which means the same removal cost the held-out operator and unit problems at least half of what the passes supply. So the sentence is attached to the case where it is least true. See RT-449 for the case it belongs to.

**Is the stated loss right?** No. It is understated, and something worse is hidden in it. The design says what is lost is "the one result that would have said the removal took nothing selective from either kind of question" (lines 826 to 828). The larger loss is that the plainest way the prediction could fail now has no readable outcome at all. That is a new serious finding, RT-449, and it is the condition on this closure.

### The operator-risk finding (RT-438): closed for the pilot, with a condition for the test half

**The counts against the raw data.** All right. Recomputed from the scoring trial, weighting each pairing by its pilot pairs (`recompute.out`):
- prompt-rule items passing the confidence filter at three passes, start then end: operator 8 then 12, unit 23 then 24, letter code 1 then 1, lookup 30 then 30, each of 30. These match lines 845 to 848.
- the whole-pair estimates quoted from the earlier check (about 7 or 9 operator pairs, about 22 unit, 1 letter-code and 29 lookup) are that check's own figures, quoted as such.
- the operator's pairings hold 7, 12 and 11 pilot pairs, as line 852 says.

**The routine-cap arithmetic for choice 8, in the pilot.** Right. 60 operator and 30 unit pairs can pair only with capitals, opposites and everyday colours. The 25% cap allows 30 of each routine kind in 120 pairs, so the 90 fill them exactly, and the 30 lookup pairs must take sums and products. Half A's pools are large enough for this: 44 capitals, 76 opposite questions and 61 objects (`pools.out`).

**Does choice 8 help the pilot?** Yes, more than the text claims. `strike_sim.py` assumes that each pair passes the confidence filter if both twins pass, independently, at the trial's per-pairing rates, and that each surviving pair then fails one of the two "does not get in the way" checks with a chance f of 0, 5% or 10%. Under the strike-count rule as written (lines 711 to 715):
- **With the present four kinds,** the design returns to John in essentially every run, at either placement. The letter-code kind is left with one routine kind or none, which the rule counts as a return (line 714), not as a kind quietly dropped.
- **With choice 8,** the chance of a return is 2% to 29% at the start placement and 0% to 24% at the end, rising with f. Operator pairs kept rise from about 6 to 7 to about 15 to 18 at the start placement, which is the "roughly doubles" of line 859.
- **The catch** is that the operator's survivors sit almost all in its capitals pairing. At the start placement, 71% of operator-with-capitals items pass the filter, against 18% with opposites and 8% with everyday colours (`lookup_sub.out`). So with 20 pairs a pairing, the colours pairing keeps about one pair and is often empty. The operator kind then survives on two routine kinds, with no slack.

**What dropping the letter-code kind costs.** Three things, of which version 0.10 states only the first:
1. **No spare kind.** With three rule kinds, all three must survive (stated, line 1180).
2. **The test half's size.** This is a new serious finding, RT-450: under the 25% cap and half B's 36 one-token capitals, choice 8 limits the test half to about 144 pairs, not 270 to 300.
3. **A narrower prompt-rule cell, and routine arithmetic tied to one rule.** The letter code was the only rule kind that was not arithmetic or a table lookup. Without it, every sum and product twin sits behind the lookup rule. This is a new finding, RT-454.

### The halves finding (RT-439): closed with conditions

**What version 0.10 did.** The operator, unit, sum and product kinds now share operand ranges, and an item goes to half A if its right answer divided by five, rounded down, is even, and to half B if it is odd (lines 660 to 670).

**Does it keep the answers apart?** Yes. Within a kind, no answer value can be in both halves.

**Does it keep the halves equally hard?** Much closer than the split by size, but not "equally hard" by construction, as the header (line 15) and section 5 (line 665) claim:
- **The last digit is split, not shared.** Half A holds every answer ending in 0 to 4 and half B every answer ending in 5 to 9 (`bands.out`). So the pilot never sees a right answer ending in 5 to 9, and the test half never sees one ending in 0 to 4. This is a new serious finding, RT-451.
- **The mean answers.** The statement that half B's answers "run on average about 2.5 higher" (line 670) is not right in general. Before the candidate rule, the gap is 1.6 to 3.9 depending on kind and range. After the place-first rule, the gap shrinks to zero or reverses (for example, unit with factor 2 to 9 and count 2 to 49: 55.0 in half A against 53.9 in half B). For a uniform spread over 10 to 99 it would be 5, not 2.5.

**Pools under plausible shared ranges** (`bands.out`), two-digit answers only:

| Kind and range | Half A: items, distinct answers | Half B: items, distinct answers |
|---|---|---|
| operator, operands 2 to 15 (the trial's range) | 327, 20 | 284, 16 |
| operator, operands 2 to 30 | 1,460, 41 | 1,377, 40 |
| unit, factor 2 to 5, count 2 to 9 (the trial's half A range) | 14, 9 | 12, 9 |
| unit, factor 2 to 9, count 2 to 12 | 47, 24 | 34, 18 |
| unit, factor 2 to 9, count 2 to 49 | 91, 34 | 73, 35 |
| sums, operands 2 to 49, one order | 590, 45 | 574, 44 |
| products, 2 to 12, one order | 32, 24 | 23, 18 |

**Are there enough items for the allocations?** Yes for every rule kind, because the content key includes the symbol or the invented unit names, and since version 0.10 numbers may repeat. Choice 8's 60 operator pairs, 40 operator bites items, the test half's operator pairs and 100 operator bites items can all be built from any of the operator ranges above. But:
- **The unit kind repeats its facts heavily.** If the trial's half A range is kept, half B has 12 two-digit multiplications for 100 unit bites items and the test half's unit pairs. Widening the range to keep the pool larger makes the unit problems harder than the trial measured (for example 7 × 13 against 3 × 7), so the 83% to 93% the choice of kinds rests on no longer applies. The design does not name this trade, and the battery specification is left to choose the range blind. See RT-455.
- **Products shrink.** Half B holds 23 two-digit products under the bands, against the 35 that line 512 still gives. That lowers the test half's ceiling even without choice 8 (RT-450, RT-456).

**Does it break the candidate rule?** No. The wrong answers are still within five of the right one, with the same number of digits, and the right answer's place is still drawn first. The place rule can be met slightly less often in half A (80% to 96% of draws) than in half B (95% to 100%), because half A's lowest band, 10 to 14, cannot have one-digit wrong answers below it. That is small.

**Does it break the 25% cap?** Not by itself, but the products pool falls, and with choice 8 the cap binds hard (RT-450).

**Does it break the overlap check?** Yes, in two places, as the text stands. See RT-452: operator operand pairs fall in both halves, and every numeric item's wrong answers are the other half's answer values.

**Condition for closing.** RT-451's last-digit split must be answered, and the overlap rules corrected (RT-452), before the battery specification is written.

### The keep-apart finding (RT-440): closed

The rule is narrowed to what it needs to protect: no bites item repeats a scored pair's or donor's whole content, and numbers and answers may repeat (lines 756 to 761). The reason given, that each item is scored in its own run with nothing carried between items, is right, and the half split is what keeps pilot and test apart. The pilot can now be built.

Two small points. The narrowed rule is close to empty, because the content includes the symbol or the invented unit names, so a bites item can repeat a scored item's shape and numbers with only the symbol changed. That is harmless while D has no reading. Also, the reason quoted ("32 combinations ... the pilot's scored pairs already use 19") describes version 0.9's ranges; under the bands the counts change (RT-455).

### The trial-figures finding (RT-441): closed, with one figure left

Every rule-kind figure in lines 770 to 776 now counts items, and all are right against `recompute.out`:
- operator 11 and 22 of 30 at the start, 13 and 22 at the end;
- unit 17 and 25 at the start, 15 and 28 at the end;
- letter code 2 to 6 of 30 at every number of passes (start 6, 5, 2; end 5, 6, 6);
- lookup 30 of 30 at every number of passes.

Choice 6's figures are right too: prompt-rule items right on 79 of 120 (66%) at the start and 86 of 120 (72%) at the end; the operator and unit gain 0.317 and 0.367 raw.

Left over: line 391 to 392 still gives the confidence share as "from 24% to 54% or 56%" with no base. Those shares count the 40 chained-lookup items, which all fail and no longer exist. Over the 240 pair items the trial gives 66, then 152 and 156 items passing (28%, then 63% and 65%). Choice 6 (line 1160) now says "of all items", which is honest but still the wrong base for a design without chained items.

### The bites sample-size finding (RT-442): closed, but now moot

The target is rewritten as asked: both parts of the condition at three quarters of the one-pass cost (lines 788 to 794). The quoted figures (95% to 100% at 80 items, 99% to 100% at 200) are the earlier check's table, quoted correctly. But since version 0.10, the condition this size rule serves decides only between two names that both carry no reading, so the rule sizes a check with no consequence (RT-453).

### The bites filters-and-donors finding (RT-443): closed

Bites items pass no filter, all are scored, and the filtered reading is reported beside as a description (lines 766 to 769). The donor conditions are restated for the single item (lines 762 to 765), and they match the generator's `eligible` function: the donor must be at least one token longer, and its right answer must not be among the item's candidates.

### The what-the-bites-check-gates finding (RT-444): closed

Lines 799 to 800 now say the one-pass condition gates every outcome, and lines 805 to 806 say the excess condition gates only D. Both are right as written. The consequence that the second now gates only a label is RT-453.

### The opposite-directions finding (RT-445): closed with conditions

The figures in lines 835 to 841 are right against `recompute.out`: operator +0.37 (+0.30) with twins 0.00 (+0.10); unit +0.27 (+0.43) with twins 0.00 (+0.03); lookup 0.00 (0.00) with twins +0.27 (+0.37).

But the paragraph puts the routine gain on "the lookup pairs", and the data put it on two routine kinds. Behind the lookup rule, the capitals twins were right on every item at one pass, and the opposites twins on 75% to 100%. The sums twins rose from 29% (start) and 14% (end) at one pass to 100% at three, and the products twins from 57% to 100% (`lookup_sub.out`). So the gain belongs to sums and products, which in the trial happened to sit behind the lookup and letter-code rules. Choice 8 makes this structural (RT-454). The committed simulation should therefore draw effects by routine kind as well as by rule kind, and line 841 should say so.

### The 16-bit finding (RT-446): closed, with one sentence to soften

- **Choice 7** now says "the same to within 16-bit rounding", and that no accuracy was compared with the native path (lines 1166 to 1169). Right.
- **The tie rule** (lines 373 to 379) is clear and workable: a tie counts as right in the share 1/k, with a margin of 0. The figures are right: 8 exact ties in 640 scores, 7 of which the old sort counted as right; the smallest non-zero margin was 0.0475 (`ties.out`).
- **Precision named:** section 7 now says "[model], at 16-bit" (line 999 and lines 1005 to 1007). The second model's precision is stated beside its result (line 1023).
- **One sentence overstates.** Lines 377 to 379 say that, because the smallest margin seen was 0.047, the identity and bypass checks "pass only when the runs match exactly". The tolerance applies to each candidate's log-probability, not to a margin. A log-probability is the logit minus a sum taken over the whole vocabulary in 32-bit arithmetic, and that sum can move by much less than 0.01 when only unlikely tokens change. So a sub-tolerance difference is possible. The practical point stands (any real difference will usually exceed 0.01). The sentence should say "will usually fail on any difference", not "only when the runs match exactly".

### The choice 6 finding (RT-447): closed

Both sides are given (lines 1151 to 1164), and every figure is right. The tail shares, from the committed step-3 results, are 0.276, 0.336, 0.165 and 0.171 at the start, the pilot's own values, against 0.409, 0.468, 0.262 and 0.265 at the end. The absorbable difference falls from 0.36, 0.30, 0.61 and 0.58 to 0.24, 0.21, 0.38 and 0.38, which is about a third. The neutral passages are now said to carry no instruction, with the reason (lines 895 to 897). The recommendation to keep the start, because choice 8 does more for the operator than the placement does, is borne out by `strike_sim.out`.

### The stale-text finding (RT-448): closed, with caveats on the time estimate

- **The noise floor** (lines 310 to 314): updated and right (0.0 over 280 items).
- **The memory** (lines 1030 to 1032): right (49.2 GB, peak 50.9 GB, 96 GB card).
- **The run count** (lines 1041 to 1048). About 100 runs of 800 items is 80,000, and the pilot's ratio of donor-only pairs to scored pairs (204 to 120) gives roughly 1,000 to 1,500 more donor-only items at the test size. So "about 85,000" is right. The time, 85,000 ÷ 280 × 65 seconds, is 5.5 hours, so "five to six hours" is right as arithmetic. Two caveats should be stated:
  - the 65 seconds was timed on an unaltered sweep of 280 items, while the swap's runs also record and inject block sums, which were not timed;
  - the count assumes each donor's block sums are recorded once and kept. If they are not kept, the swap's runs double.
- **The count rests on 300 pairs**, which choice 8 would cut to at most about 144 (RT-450).

---

## New findings

| # | Finding | Grade |
|---|---|---|
| RT-449 | The plainest way the prediction could fail now reads as "Too weak to read", so the test can fail the prediction only if the removal also damages routine questions | serious |
| RT-450 | Under choice 8 and the 25% cap, the test half can hold at most about 144 pairs, and about 85 would pass the confidence filter | serious |
| RT-451 | The bands of five give every answer ending in 0 to 4 to the pilot and every answer ending in 5 to 9 to the test, so the halves are not equally hard by construction | serious |
| RT-452 | The overlap rules, as written, fail under the bands of five | worth noting |
| RT-453 | The bites check's excess condition now decides only between two names that both give no reading | worth noting |
| RT-454 | Under choice 8, every sum and product twin sits behind the lookup rule, and those twins carry the trial's routine gain from the passes | worth noting |
| RT-455 | The unit kind's few multiplication facts repeat across many items, and resampling treats them as independent | worth noting |
| RT-456 | Stale text left in the body | worth noting |

### RT-449, the plainest failure of the prediction has no reading (serious)

**Lines:** 125 to 130 (section 1), 801 to 806 (the excess condition), 807 to 834 (what the replacement costs), 941 to 944 (D in section 6), 1002 to 1003 and 1009 to 1016 (section 7).

**The case.** Suppose this placement is wrong in the simplest way: the extra passes help the operator and unit problems, but the message's content about this particular input does not matter, so a message built from other inputs serves as well. That is exactly what H1's prediction for this placement denies, so it is the case a test of the prediction most needs to read.

**What the design reports in that case.**
1. The one-pass run costs the bites items well over 0.15, so stage one passes.
2. The main removal costs the bites items no more than the random comparison, so the excess condition fails.
3. The pairs show no excess either, so R and P both fall below δ.
4. Section 6 then gives **"Too weak to read"**, because D needs the excess condition (line 942).

So the plainest failure of the prediction is reported as a removal too weak to read. Until version 0.9 this case was not lost, because the bites task was a different kind of task: a removal could fail to cost the rule problems while biting the chained lookups, which gave D, the prediction failing. Now that the bites items are the same operator and unit problems, "the removal does not take what the passes supply on rule problems" and "the removal is too weak" are the same observation.

**What the test can still show.** A, the prediction holding. B or C, the prediction failing, but only if the removal costs routine questions beyond the comparisons. So the prediction can fail only in a world where the feedback matters, but not selectively. In the world where it does not matter, the test is silent. This asymmetry is what version 0.10 should state as the loss, in place of "the one result that would have said the removal took nothing selective". Section 1's "That is a result against the placement" should not stand next to D (see RT-437 above).

**Weighed plainly.** The test is still worth running only if one of the following is true:
- **John accepts the asymmetry, stated in sections 1 and 7:** a readable positive (A) and a failure only through general or routine damage (C or B), with the plainest negative reported as "Too weak to read". On the trial's figures C is a live route, because the sums and products twins need the passes (RT-454). But C is not the failure that H1's prediction most plainly risks.
- **Or the design reads that case.** For example, it could add a "replacement does not bite" result: the one-pass condition is met, and under both methods the main removal's excess on the bites items has an interval whose upper end is below a stated share of the one-pass cost (a quarter, say). It should be read as the prediction failing for this placement only if the swap's size and its damage on the neutral set show the message was actually changed. That last condition is what separates "the content does not matter" from "the swap changed little". Section 7's one allowed sentence about the fewer-passes runs (lines 1009 to 1012) belongs to this case, not to D.

Either is a ruling before any data. Writing the second would need its own closure check.

### RT-450, choice 8 caps the test half (serious)

**Lines:** 509 to 518 (the pools and the 270 to 300 ceiling), 521 to 523 (the cap), 854 to 857 (the test half), 879 to 881, and choice 8 at lines 1173 to 1182 ("the test half's allocation shifts the same way").

**The arithmetic.** Under choice 8, the operator and unit kinds (three quarters of the pairs, at 2 : 1 : 1) can pair only with capitals, opposites and everyday colours. No routine question is used twice, and no routine kind may exceed 25% of the cell. Half B holds 36 one-token capitals with no name overlap (38 before that rule), 75 opposite questions and 61 objects (`pools.out`; line 594 still says about 42 capitals). For a test half of T pairs, the operator and unit pairs, three quarters of T, must fit into at most 36 capitals plus a quarter of T opposites plus a quarter of T colours. That holds only up to **T = 144** (`testhalf.out`). With 42 capitals it would be 168. Even at three equal kinds the limit is 216.

**What survives.** At T = 144 and the trial's per-pairing rates, about 85 pairs (start) or 87 (end) are expected to pass the confidence filter, before margin and swap-size matching. That is below the 120 to 200 the sample-size simulation is expected to ask for, so the design would return to John at step 4b for want of pairs. The pilot hides this, because half A has 44 capitals and the pilot needs only 30.

**What must change.** Before John rules on choice 8, recompute the test-half ceiling for each option under the bands of five (products fall to 23 in half B), and state it beside the choice. Possible answers include:
- a 1 : 1 : 1 allocation;
- giving the letter code's share partly to the lookup kind, whose sums pool is large;
- lifting the cap on everyday colours or opposites;
- accepting a smaller test half with the simulation's verdict.

The recommendation should follow from those numbers.

### RT-451, the bands of five split the last digit (serious)

**Lines:** 15 to 16 (header), 660 to 670 (the bands), 780 ("version 0.10 makes [half B] as hard as half A"), 795 to 800 (the one-pass condition).

**The problem.** Under the bands, every pilot answer ends in 0 to 4 and every test answer ends in 5 to 9 (`bands.out`). Two things follow:
- **The arithmetic differs.** For the unit kind, 87% to 93% of half A's multiplications have an even factor or count, against 50% to 67% in half B. Every product ending in 0 (such as 4 × 5 or 6 × 5) is in half A. Multiplying to a round number is the easiest case, and half B has none.
- **Guessing differs.** The wrong answers lie within five of the right one, so they cross the band. In half A a right answer ending in 0 is the only multiple of ten among its candidates. In half B every multiple of ten offered is wrong. If the model leans toward round numbers when unsure, as one pass may make it, half A gains and half B loses. That inflates the one-pass condition's forecast from the pilot.

**Why it matters.** The one-pass condition gates every outcome. The point of the halves finding (RT-439) was that the pilot must forecast it on the test half. The pilot cannot measure answers ending in 5 to 9 at all, so it cannot say whether the difference is real.

**What must change.** Assign answer values to the halves so that each half gets the same mix of last digits. For example, within each decade, draw with a fixed seed which five values go to each half, so that each half gets one of {0, 5}, two of the other even digits and two of the other odd digits. Step 3 should report each half's last-digit mix and operand parity by kind. Stop calling the halves "equally hard" until the pilot can show it.

### RT-452, the overlap rules fail under the bands (worth noting)

**Lines:** 670 to 679.

- **Operand pairs.** "A committed check script fails if any pilot ... operand pair appears in the test set" (line 671). Under shared ranges, the same operator operands give different answers under different shapes: with operands 2 to 15, 138 of the 192 operand pairs that occur at all occur in both halves (`bands.out`). Say that the operator's split key is the shape with its operands, or the answer.
- **Candidates.** "The script also fails if any test item's candidate comes from a half-A pool" (lines 677 to 678). A numeric wrong answer within five of the right one nearly always lies in the other half's band, so for numbers this cannot hold. Exempt numeric candidates, as colours are exempt, with the reason. The present script does not check numbers, so it would not fail, but the text and the script would disagree.
- **The script's ranges.** `src/check_overlap.py` hard-codes version 0.9's ranges (sums split at 50, products at 40, unit factor 2 to 5 against 6 to 9, operator 2 to 15 against 25 to 99). It must be rewritten for the bands, and step 3 should list it.
- **The mean answer.** Replace "about 2.5 higher" (line 670) with the figure step 3 measures, or drop it.

### RT-453, the excess condition now decides only a label (worth noting)

**Lines:** 788 to 794 (the size rule), 801 to 806 (the excess condition), 941 to 944.

Since version 0.10, when the pairs show no excess, the excess condition picks between "No excess in the cells" and "Too weak to read". Both carry no reading. The condition renames nothing else, because the one-kind readings ignore it (line 962). So the 200 test bites items, and the simulation that may raise their number, size a check with no consequence. Meanwhile the one condition on the bites items that gates every outcome, the one-pass cost of at least 0.15, is a bare point estimate with no interval and no size rule. If RT-449 is answered by a readable "does not bite" result, the excess condition regains its work, and the size rule should then aim at that result. If it is not, say so and size the bites set for the one-pass condition instead.

### RT-454, routine arithmetic tied to the lookup rule under choice 8 (worth noting)

**Lines:** 525 to 533 (the pairing rules), 835 to 841 (the opposite directions), 1173 to 1182 (choice 8).

Under choice 8, sums and products can pair only with the lookup rule, and the lookup rule pairs only with sums and products. In the trial, sums and products were the routine twins that needed the extra passes: sums rose from 14% to 29% at one pass to 100% at three, products from 57% to 100% (`lookup_sub.out`). Three consequences follow:
- **The surviving routine cell is about 42% arithmetic** in the test half (`testhalf.out`). That is against the cap's stated purpose, "so 'routine' is not mostly arithmetic" (line 521).
- **The leave-one-kind-out readings cannot separate** a lookup-rule effect from a routine-arithmetic effect. Leaving out the lookup rule removes every sum and product twin.
- **The routine cell's sensitivity to the passes sits wholly behind one rule kind.**

None of this favours A, and C is likelier for it. But choice 8 should state it, and so should section 5's paragraph on opposite directions, which puts the gain on "the lookup pairs".

### RT-455, repeated facts in the unit kind (worth noting)

**Lines:** 756 to 761, 788 to 789, 865 to 866 ("differences are resampled by item").

Depending on the range the battery specification chooses, half B has 12 to 73 two-digit unit multiplications (`bands.out`). Those must serve 100 unit bites items and the test half's unit pairs. Items sharing a multiplication fact are not independent, so intervals resampled by item or by pair are too narrow by an amount that grows with the repetition. Either choose a range that keeps repetition low and say what that does to difficulty (RT-439 above), or resample by fact within the unit kind. In both cases, report the number of distinct facts per kind.

### RT-456, stale text in the body (worth noting)

- **Lines 497 to 498:** sums "split at an answer of 50" and products "split at an answer of 40", which contradicts the bands of five at line 661.
- **Lines 511 to 518, 855 and 879:** "35 products", "42 capitals" and the 270 to 300 ceiling. Under the bands, half B has 23 two-digit products and the generator finds 36 capitals. Under choice 8 the ceiling is about 144 (RT-450).
- **Lines 522 to 523:** "The prompt-rule kinds are kept as nearly equal in number as the filters allow", which contradicts choice 8's 60, 30 and 30. It should be made conditional on John's ruling.
- **Lines 888 to 889:** "120 pairs, 30 for each rule kind" should be made conditional on choice 8 in the same way.
- **Lines 391 to 392:** the confidence share over the wrong base (RT-441 above).
- **Line 303:** "If the replacement does not bite there, no null result is read", and **lines 803 to 804:** "too weak to read a null, and outcome D cannot be read". Since version 0.10, no null is read in either case, so both sentences describe a distinction that no longer exists, unless RT-449 restores one.
- **Lines 1101 to 1102:** "The battery specification and the pilot set are rebuilt for version 0.9 before step 4b" should name version 0.10, or the version that is closed.
- **Lines 125 to 130:** the drifting "That" (RT-437 above).
- **Line 780 and header line 15:** "as hard as half A" and "equally hard" (RT-451).

---

## Verdict

**Version 0.10 is not ready for the battery specification and the pilot to be rebuilt (step 3). It needs a short version 0.11 first.** It answers most of the ninth check well:
- the trial figures now count items, and every one I recomputed is right;
- the keep-apart rule is fixed;
- the tie rule, the 16-bit wording, choice 6 and the stale noise-floor and memory text are done;
- D no longer claims a reading it cannot have;
- choice 8 does make the pilot far likelier to pass the strike-count rule.

But three serious problems remain. Each would make a reported outcome misleading, or would stop the test half or the pilot from doing its job.

1. **The readable negative (RT-449).** State in sections 1, 5 and 7 that the plainest failure of the prediction, "the extra passes help but this input's message does not matter", is now reported as "Too weak to read". Put that, not the narrower loss in lines 826 to 828, before John. Or add a readable "replacement does not bite" result, with a swap-size condition, and move section 7's allowed sentence to it. Fix the drifting "That" in section 1.
2. **Choice 8's test-half ceiling (RT-450).** Recompute the test-half ceiling for each option under the 25% cap and the bands (about 144 pairs, about 85 after the filter, for the recommended option as written). Revise the recommendation or the allocation before John rules.
3. **The last-digit split (RT-451).** Replace the bands of five with a split that gives each half the same mix of last digits, or state plainly that the pilot cannot forecast the one-pass condition on the test half. Have step 3 report last digits and operand parity by half.

These can go in the same version: the overlap rules and the check script's ranges (RT-452), the job of the excess condition and the bites set's size (RT-453), choice 8's tie between routine arithmetic and the lookup rule (RT-454), the unit kind's operand range and repeated facts (RT-455), and the stale text (RT-456). There are also three small fixes under the earlier findings: the confidence share's base (RT-441), the identity-check sentence (RT-446) and the time estimate's caveats (RT-448).

The dose question (RT-345) stays open until step 4b, and nothing here bears on it.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **The bands give each half its own last digits (RT-451).** Confirmed by arithmetic. An answer from 10 to 99 whose value divided by five, rounded down, is even always ends in 0 to 4, and one whose value is odd always ends in 5 to 9. The author's band rule therefore splits by last digit, which is the opposite of what it was written to do. The mistake is the author's.
- **The capital pool (RT-450).** Confirmed with the generator and the real tokeniser: half B has 36 capitals usable as right answers (38 single-token capitals in all), and half A has 44.
- **Not rechecked by the filer:** the pair-count and cap arithmetic behind RT-450, the operand-overlap counts of RT-452, and the multiplication-fact counts of RT-455.
- **Where things stand.** The reviewer finds version 0.10 **not ready** for step 3. Three serious findings (RT-449 to RT-451) need a version 0.11 first. Five worth-noting findings (RT-452 to RT-456) go with them. Every trial figure the reviewer recomputed is right. The dose finding (RT-345) stays open until step 4b.
