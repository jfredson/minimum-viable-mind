*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the eleven earlier reviews. It worked read-only in a detached worktree at commit 4fb7e73, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.12

*Reviewer: a fresh Claude Code session. I did not write the design, version 0.12's changes or any earlier version's, the three rented runs, their findings, or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure12-loop-design-2026-11-21` at commit 4fb7e73, and changed nothing in it; `git status` was clean when I finished. I used only my own scratch folder, `/private/tmp/claude-501/loop-review12-veBcSP`, which was empty when I started, and every script and output is there. I did not open, list or use any other scratch or temporary folder, including earlier `loop-review*` folders and any session scratchpad. I downloaded nothing, installed nothing, spent nothing, pushed nothing and made no network calls. New findings are numbered from RT-466.*

---

## What I opened

- **The closure check of version 0.11**, `docs/reviews/2026-11-21-loop-removal-test-design-v0.11-closure-check-claude-code.md`, in full. I treated its filer's check as the author's note, not as part of the review.
- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.12 header (lines 1 to 20); sections 1 to 11 (lines 114 to about 1425), read in full because the diff touches sections 1, 3, 5, 6, 7, 9 and 10; and the change log "from version 0.11" (lines 1981 to 2021).
- **The diff** `git diff b211fa7 4fb7e73 -- docs/loop-removal-test-design-2026-11-20.md`, in full.
- **The generator**, `experiments/10-loop-removal-test/src/build.py`, lines 140 to 325: the number-candidate rule, the operator and unit rules, and the sums and products routines, so that my pools follow the generator's shapes.
- **Raw results:** the structure of `scoring-trial-run-2026-11-21/scoring-trial-results.json`, to look for per-item scores. It holds per-cell rates only, so I could not draw item-level noise from it. I listed the other two run folders and the pilot set folder, `batteries/pilot/`, but used no figure from them beyond what the earlier checks already verified.

I did not open the battery specification, the findings files, any web page, or anything outside the worktree and my scratch folder. Nothing in this check turned on token counts, so I did not load the tokeniser.

## What I ran

All under `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`, from my scratch folder. Each script's output is saved beside it as a `.out` file.

- `split_sim.py`: version 0.12's split of the halves, with no model. The pools follow the stated ranges, with two-digit answers only:
  - the operator kind: the generator's four shapes, operands 2 to 15, answers 10 to 49;
  - the unit kind: factor 2 to 9 and count 2 to 12, each (factor, count) one item;
  - sums: operands 2 to 49, one order;
  - products: 2 to 12, one order.

  Within each decade, one half gets the value ending in 0 and the other the value ending in 5. Which half gets the 0 alternates from decade to decade, starting from a half drawn by the seed. Each half then gets two of the other four even endings and two of the other four odd endings, drawn by the seed. For seeds 1 to 1,000 it applies the five tolerances (shares ending in 0 and in 5 within 0.05, mean answers within 2, shares of even operands within 0.05, and, for the unit kind and products, distinct facts in the smaller half at least 80% of the larger). It reports the first passing seed for each kind, how many seeds pass, which tolerances fail, and the half sizes.
- `split_sim_unit_unordered.py`: the same check for the unit kind with a "fact" counted as the unordered multiplication (3 × 4 and 4 × 3 one fact). It also reports the real answer ranges and the decades that have values missing.
- `own_loss_power.py`: a rough, model-free power check of F's per-kind own-loss condition when the swap's true own loss is zero. The assumptions are stated at the top of the script and under the per-kind finding (RT-470) below.

---

## The earlier findings, one by one

### The swap's-own-loss finding (RT-457): closed

**What version 0.12 did.** "Does not bite" now needs the main removal's own loss on the bites items, measured against the unaltered three-pass run, to have an interval whose upper end is below a quarter of the one-pass cost, under each method (lines 886 to 891). F's sentence now says "cost them little" (line 1152).

**Is F now safe to read as the prediction failing?** Yes, for the case the eleventh check raised. A swap that costs the held-out problems as much as the passes supply can no longer reach F, however much matched random noise also costs them. That case now falls to "too weak to read", which is honest. With the change ratio (RT-459) and the per-kind condition (RT-461), F now says three checkable things:
- the passes help;
- the message was moved;
- a moved message costs the held-out problems little in each kind.

That is the plain failure the test needs.

**Do the loopholes stay shut?** The main one does. Three smaller ones remain, and none of them reverses F's reading:
- F's sentence says the swap "cost neither cell of the pairs more than matched comparisons". F is reached when R's and P's intervals have upper ends below δ (0.10), and that allows an interval such as [0.02, 0.09], which lies above zero. The sentence should say "by less than δ" (RT-471).
- The one-pass gate is pooled over the two bites kinds. F's per-kind condition can still be met in a kind the passes did not help, if the swap happened to raise that kind's accuracy (RT-471).
- F does not check the pairs' own loss, only their excess over random damage. So the loophole RT-457 closed for the bites items is still open on the operator and unit pairs, which are the same kinds of problem. It is unlikely, because the pairs are the confident items and harder to knock over. But if it happened, F's reading would rest on the bites items while the pairs said otherwise (RT-471).

The point estimate of the one-pass cost and the per-kind cost are both stated (lines 887 to 888, 893), which settles the first definition owed under RT-453 (below).

### The disagreement-rename finding (RT-458): closed, with one scope point

**What version 0.12 did.**
- B is no longer renamed.
- An A or C is renamed "Cells and bites check disagree" only when the removal does not bite and the operator and unit pairs, read on their own, have an excess whose interval lies above zero (lines 1082 to 1093).
- Section 1 now says B and C need no result from the bites check, except that a C is set aside under that rule (lines 153 to 155).

That is what the eleventh check asked for, and the reasons given are right.

**What is left.**
- **The rename is gated on all of "does not bite", including the change ratio.** The contradiction it catches is a loss on the operator and unit pairs with none on the held-out problems of the same kinds. Whether the swap moved the message by half its size does not bear on that contradiction. A small change ratio would make a loss on the pairs harder to explain, not easier. As written, an A whose bites items lost nothing but whose change ratio was 0.45 keeps its name, with contradicting evidence beside it. The rename should use conditions 1 and 2 of "does not bite" (own loss small, pooled and in each kind), not condition 3 (RT-467).
- **Section 1 is slightly off.** B and C do need one result from the bites items: the one-pass condition, which gates every outcome (lines 872 to 878, 1056). Section 1 should say "need no result from the bites check beyond the one-pass condition" (RT-472).

### The change-ratio finding (RT-459): closed with conditions

**Is it now computable as defined?** For the swap, nearly. For the average, not yet.
- **Five donors.** Each bites item has five donors (line 843), and each donor run gives a different replacement and a different first point of difference. The text says "the first position where the item and its donor differ" (line 896), in the singular. The natural reading is that the ratio is computed for each donor run and averaged over the five, which matches how scores are averaged (line 278). It should say so.
- **The average method has no donor.** The text says "Under the average method the given sum is the average" (line 903), but it does not say which positions the average's ratio covers. The positions are defined by where a donor differs, and the average changes every position, including the template slots and, at the start placement, the instruction's words, which are text positions and get the pooled prose average. Section 5's swap-size matching already uses "every position that is not a template slot" for the average (lines 807 to 809). The ratio should name its positions for the average in the same way.

**Is the choice of positions right?** For the swap, yes. Starting where item and donor first differ drops positions whose distance is zero by construction, because the model reads left to right. It fixes the 41% dilution the eleventh check measured.

**Are the scaling and "the true sum's length" consistent?** Yes, but they say more than the text lets on.
- After each sum is scaled to a root-mean-square of 1, its length is exactly the square root of the width (48 for a width of 2,304, apart from the normalisation's small constant), not "about".
- So the ratio is the distance between two unit-length directions. It runs from 0 to 2, not from 0 to 1. A ratio of 0.5 means a cosine similarity of 0.875 between the true and the given sum, an angle of about 29 degrees.

That is a much lower bar than the plain reading of version 0.11, which needed a cosine of about 0.63 or less at every position after divergence. The change is made before any data, so it is allowed. But the design should state the cosine equivalent, because "about half its own size away" will be read as more than a 29-degree turn.

**Is the average method's ratio comparable?** The formula is the same, but the number does not mean the same thing under the two methods. Here is a simple model. Suppose every true sum is a shared direction plus an item-specific part. Then a donor's sum shares only the shared direction with the true sum, while the average is the shared direction itself. The average is therefore closer to every true sum than a typical donor is. In that model, a swap ratio of exactly 0.5 goes with an average ratio of about 0.36. Equally, the average reaches 0.5 only when the swap is at about 0.68. The pooling over positions pushes the other way, by an amount not known before step 4b. So "at least 0.5 under each method" may bind on the average far more than on the swap. Step 4b will show this, which is why the return-to-John rule matters (next point, and RT-466).

**Does the return-to-John rule at step 4b keep the 0.5 from being chosen after seeing results?** Yes. The threshold is fixed now, the pilot measures it on half A only, and "the threshold is not changed after seeing it" (line 910). But the rule names no way forward. If the pilot's mean is below 0.5 under the average, and the threshold cannot move, John is left with four options: run with F out of reach (the imbalance of the plainest-failure finding, RT-449, returns, though now announced), change a method, change the donors, or stop. These should be listed now, so that the choice made at step 4b is one of them and is not designed after seeing the pilot. There is also no margin: a pilot mean of 0.51 passes, while the test half could come in under 0.5 (RT-466).

**Two further points.**
- **The two blocks are weighted equally.** The readers "almost always" read block 3 (section 2, line 191). Block 3 also carries the pass-counting coordinate, about 46% of its squared size (lines 198 to 202), which the donor shares, so block 3's ratio is held down. The mean over both blocks can therefore pass 0.5 while block 3, which carries most of the message, moved less. The ratio should be reported for each block, and either weighted by the readers' learned mix or required of block 3 on its own (RT-466).
- **Section 3's swap size** (lines 321 to 324) still uses "changed positions" and "normalised" without saying how. It scales the random comparison and the 10% dose match. For the swap the undefined positions add nothing to a total, because their distance is zero. But "normalised" should be the same scaling as the change ratio's, so that the two figures agree (RT-472).

F's sentences now say "on average" (lines 1152, 1161 to 1162). Step 4b reports the spread. The conditions on this closure are RT-466.

### The item-level split finding (RT-460): closed, and the seed rule works

**The simulation** (`split_sim.out`). With the alternating round values and the five tolerances:

| Kind | Pool | First seed meeting every tolerance | Seeds of 1 to 1,000 that do | Smaller half, among passing seeds |
|---|---|---|---|---|
| operator | 611 items, answers 10 to 45 | 1 | 865 | 274 to 305 items |
| unit | 81 (factor, count) items | 8 | 28 | 36 to 40 facts |
| sums | 1,164 items | 1 | 1,000 | 561 to 582 items |
| products | 55 items | 71 | 15 | 25 to 27 items |

So a seed from 1 to 1,000 meets every tolerance for every kind, and the return to John will not fire. For the unit kind and products, the tolerance that fails most is the mean answer: 75% and 78% of seeds fail it. The distinct-facts rule and the parity rule fail 38% to 70%. The unit result is the same if a fact is counted as the unordered multiplication (`split_sim_unit_unordered.out`: first seed 8, 28 seeds pass).

**Does the rule create problems of its own?**
- **Too few items.** No. Products in half B come out at 25 to 30 (whichever half the seed labels B), against the body's "about 23 to 27" (line 550) and choice 8's "22 to 28" (line 1349). Those figures are cautious, not wrong. The unit kind keeps 36 to 45 facts per half, inside the stated "about 35 to 45" (line 837).
- **Bias from choosing the seed.** None that bears on the outcome. The seed is chosen on figures computed from the lists with no model, so it cannot select on how the model does. It narrows products and the unit kind to a few percent of possible splits, which is the purpose.

**Three things the specification must settle** (RT-468):
- **"Items" is ambiguous.** "Both halves are built and these figures computed over their items" (line 712) could mean the full pools or the drawn pilot and test items. The seed rule says "computed from the lists" (line 721), which suggests the pools, and only pools can be checked before the test seed exists. But the drawn sets are what the pilot measures. Forty pilot unit bites items and 100 test unit bites items, drawn from matched pools, can still differ by chance in their share ending in 0 by around 0.06 to 0.1 (one standard deviation of about 0.06). The text should say that the tolerances are on the pools, and that step 3 and the registered run report the same figures for the drawn sets, as a description.
- **Short decades.** The operator kind's answers run from 10 to 45, not 10 to 49 (line 669), because no shape reaches 46 with operands up to 15. So its forties decade has only 41 to 45, two other even endings and two other odd ones. Sums stop at 98, so the nineties lack 99. The rule "each half gets two of the other even endings and two of the other odd endings" cannot be met in those decades. The specification should say how they are split (I gave all of a short group to one half, and the tolerances still pass).
- **What a "fact" is.** The distinct-facts tolerance and the resampling by fact both need it. The unit pool has 81 (factor, count) items, 55 unordered multiplications and 42 answer values. Those give about 40, 27 or 21 resampling units per half. It changes the width of every unit interval (RT-469).

### The one-kind-carries-F finding (RT-461): closed, with a labelling problem

"Does not bite" now needs the own-loss condition in each of the two bites kinds, each against its own one-pass cost, and the outcome is "Depends on one kind" if it holds pooled but not in one kind (lines 892 to 894). That shuts the case the eleventh check raised. Two problems come with it, both in RT-470:
- **Scope.** The sentence sits inside the definition of "does not bite", which is also used by the disagreement rename on an A or a C. Read literally, an A whose bites items show a small pooled own loss but not a small one in one kind becomes "Depends on one kind". That is a rename of an A that the "checks that apply only to A or B" (lines 1095 to 1129) do not list. It also contradicts "C, D, E and F are never renamed" for a C. Nor is its order against condition 3 stated: when the change ratio also fails, it is not said whether the outcome is "Depends on one kind" or "too weak to read". The sentence should be confined to stage two's no-excess branch, after the change ratio is checked.
- **The label says more than the evidence.** Under a true own loss of zero, the unit kind's interval will often be too wide to clear a quarter of its smaller one-pass cost. That is imprecision, not a loss carried by one kind. But "Depends on one kind, with the kind named" will be read as "the removal cost the unit problems".

### The resampling and joint-simulation finding (RT-462): closed with conditions

Section 6 now sets the scheme. Resampling is done within each rule kind; in the unit kind the unit is a multiplication fact, taking every pair and bites item that uses it together; elsewhere it is the pair, or the bites item alone (lines 1042 to 1047). Section 5 and the sample-size section point to it (lines 840, 991). The simulation must model the bites items and the cells together. This is the right scheme.

Two things are still needed (RT-469):
- **What a "fact" is** (above).
- **Where the joint simulation gets its correlation.** The pilot is the only source, at 40 bites items per kind and about 40 pairs per kind, and the text does not say so. Products twins (behind the lookup rule) share multiplications with unit items, across rule kinds. That is a small dependence that the scheme ignores, and it can stay ignored if it is stated.

### Choice 8's figures, the 1 : 1 : 2 reason and the cap's base (RT-463): closed, with stale figures elsewhere

- **The table** (lines 1353 to 1358) matches the eleventh check's even-spread figures, and the pilot column matches its simulation (9% and 0.2% at f = 0, 2% and 0%, 100%).
  - The rows for four kinds and for 1 : 1 : 2 say "about 216 to 236". That range came from products pools of 18 to 23, not the 22 to 28 the header names. At 22 or more the bottom is nearer 232, so the range is low. Neither row is recommended.
  - The header names the even spread. The figures for three equal kinds sit near the eleventh check's even-spread figures at products 23 (145).
- **The 1 : 1 : 2 reason** is corrected (lines 1362 to 1366). The stated reasons, a weaker operator kind in the pilot and a worse arithmetic tie, are fair. The "17 to 18 for three equal kinds" there are test-half figures, while "about 12" at line 1380 is the pilot's. Each should be labelled.
- **The cap's base** is now the built cell (lines 1373 to 1376), which the built cell meets, and the surviving mix is reported. One of the two reasons given is weak. Cutting sums pairs at random after the filter would not "select on how the model did" any more than the filter already does. The cost in survivors is the real reason, and it is enough.
- **Stale elsewhere** (RT-472): section 5 still says "about 196 to 220, depending on the products pool" and "the arithmetic is in the tenth change log" (lines 553 to 555). The sample-size section still says "about 196 to 236 ... about 130 to 150" (lines 1003 to 1005).

### Choice 6 under the revised choice 8 (part of RT-463): closed, with one reason overstated

The pilot figures (lines 1320 to 1325) are the eleventh check's, correctly copied. They leave out its note that counting the two baseline checks as two independent chances raises both placements to about 50% at f = 10%, which John should see.

The recommendation is now "narrowly" the start, with the end "a fair choice" (lines 1327 to 1329). That is the right weight. But one of its reasons is overstated: "a dose imbalance found at the registered run would cost the result". At either placement the dose is first measured at step 4b, on the pilot. So the risk the start lowers is the smaller one: a test half that fails the 10% dose rule after the pilot passed it. That risk is larger at the end, because the tail after the shared context is longer (lines 1310 to 1313). The sentence should say that (RT-472).

### The unit-range finding (RT-464): closed, with one stale sentence

"Close to the trial's difficulty" is gone. The gap is stated with the right figures: 55 of 81 facts outside the trial's range, mean answers 40 against 22, and about 13 facts per half under the narrower range (lines 733 to 738). The operator kind's range is stated, but as "10 to 49" where the real range is 10 to 45 (line 669; RT-468).

The repeated-facts paragraph still ends "Widening the range to repeat facts less would make the unit problems harder than the trial measured, which is the trade the range above accepts" (lines 841 to 842). That implies the present range is not already harder, which line 734 now says it is (RT-472).

### The stale-text finding (RT-465): closed

Every item listed is fixed:
- section 1's B and C sentence;
- section 3's summary of F;
- the operator's "0 to 999";
- the numeric exemption, and the check on half-A candidates (lines 744 to 746, 753);
- "270 to 300";
- the resampling wording;
- the "tenth" count (lines 1018 to 1021);
- the rule on F in the readings with one kind left out (lines 1128 to 1129);
- "never renamed by the checks that apply only to A or B";
- section 9's steps 1 and 2;
- F's "on average".

**Section 9's statement that choices 6 to 8 are unruled** (lines 1215 to 1218) is right. Section 11 records rulings on choices 1 to 5 only, made on version 0.4. New stale text is under RT-472.

### The two definitions owed under the excess-condition finding (RT-453): closed

- "A quarter of the one-pass cost" is now the point estimate on the same bites items, and on each kind's own items for the per-kind condition (lines 887 to 888, 893).
- The size rule's target for "does not bite" includes all three conditions, in both kinds, at the change ratio step 4b measures (lines 917 to 918).

But see RT-470 on whether 200 bites items can meet that target.

### The dose finding (RT-345)

It stays open until step 4b, and nothing here bears on it.

---

## Do the outcomes still form a partition?

Yes, mechanically, once RT-470's scope point is fixed.
- **Stage two** still runs A, B, C, then the no-excess branch, then E, and the first that applies decides.
- **In the no-excess branch,** "bites" is tested before "does not bite". In version 0.11 the two could not both hold. Now they can, in one corner: "bites" is about the excess over random damage, and "does not bite" is about the own loss, so both can hold if random noise *raised* accuracy on the bites items by more than a quarter of the one-pass cost. The order then gives D. That corner is far-fetched and the order settles it, but the text should say that D takes precedence.
- **The disagreement rename** acts only on A and C, before the checks that apply only to A or B. So no case gets two names from it.
- **"Depends on one kind" for F** is the one place where a case can get two readings, because of where the sentence sits (RT-470).
- **The two methods** are classified separately and then combined, so "Depends on one kind" under one method and F under the other is "methods disagree", as it should be.

---

## New findings

| # | Finding | Grade |
|---|---|---|
| RT-466 | The change ratio is not yet defined for the average method or over the five donors. The same 0.5 means different things under the two methods. The two blocks are weighted equally though the readers mostly read block 3. And the step 4b return to John names no way forward | worth noting |
| RT-467 | The disagreement rename is gated on the change ratio, which does not bear on the contradiction it catches, so an A can keep its name with contradicting evidence | worth noting |
| RT-468 | The split's tolerances do not say whether they apply to pools or drawn items, the short decades cannot meet the per-decade rule, and the operator's range is 10 to 45, not 10 to 49 | worth noting |
| RT-469 | "Fact" is undefined, and the joint simulation's correlation has no stated source | worth noting |
| RT-470 | F's per-kind rename has no stated scope or order, its label reads imprecision as a one-kind effect, and the bites size has no return-to-John rule if the per-kind condition cannot be met | worth noting |
| RT-471 | F's sentence overstates the cells' result, the one-pass gate is not per kind, and F does not check the pairs' own loss | worth noting |
| RT-472 | Stale and inconsistent text | worth noting |

None is graded serious. I looked hard for one in four places:
- F's new own-loss condition;
- the narrowed rename;
- the change ratio's scale;
- the split's seed rule.

In each, the problem I found either changes only which no-reading name a case gets, or is caught by a return to John before registration, or needs one sentence in the specification. None makes a reported reading of the prediction wrong.

### RT-466, the change ratio's remaining gaps (worth noting)

**Lines:** 895 to 907 (the ratio), 908 to 910 (the step-4b rule), 191 and 198 to 202 (section 2, the readers and the pass-counting coordinate), 321 to 324 (the swap size).

1. **Five donors.** Say that the ratio is computed for each donor run, from that donor's first difference, and averaged over the item's donors.
2. **The average's positions.** Name them: I suggest every position that is not a template slot, from the first word of the user text through the answer position. That is the span section 5 already uses for the average's swap size (lines 807 to 809).
3. **State the scale.** The ratio is the distance between two unit-length directions, from 0 to 2. 0.5 is a cosine of 0.875, an angle of about 29 degrees. "About the square root of the width" is exact after the scaling.
4. **Comparability.** The average is nearer every true sum than a typical donor is. In a simple model with a shared direction, a swap ratio of 0.5 goes with an average ratio of about 0.36. So the 0.5 binds on the average much harder. Step 4b should report both, and the design should expect that the average is the method that fails.
5. **The blocks.** Report the ratio for block 2 and for block 3 separately. Either weight the two by the readers' learned mix, measured at step 4b, or require 0.5 of block 3 alone. Block 3's ratio is held down by the shared pass-counting coordinate, so an equal mean can pass while the block the readers use moved less.
6. **The way forward at step 4b.** List now what John may choose if the pilot's mean is below 0.5 under either method. The options are: run with F out of reach, saying so in advance; replace the average by its fallback for this purpose only; or stop. Consider a margin, such as a pilot mean of at least 0.55, so that a pilot that passes narrowly is not followed by a test half that fails.
7. **Section 3's swap size.** Use the same per-position scaling as the ratio, so that "normalised" means one thing throughout.

None of this changes a reading once fixed. It must be fixed before step 4b's code is written, so it belongs in the specification.

### RT-467, the disagreement rename uses the change ratio (worth noting)

**Lines:** 1082 to 1087; 884 to 907.

The rename catches a loss on the operator and unit pairs with none on the held-out problems of the same two kinds. That is a contradiction whatever the change ratio is. Gating it on the full "does not bite" means that an A or C whose bites items lost little, but whose change ratio fell below 0.5, keeps its name although the same kinds of problem held out were not hurt. Base the rename on conditions 1 and 2 of "does not bite" alone (own loss small, pooled and in each kind). The change ratio guards F's reading that the message's content does not matter. The rename makes no such claim.

### RT-468, the split's remaining definitions (worth noting)

**Lines:** 667 to 670 (the operator's range), 706 to 722 (the split, the tolerances and the seed rule).

- **Pools or drawn items.** Say that the tolerances apply to the pools of each half, which is all that can be checked before the test seed is drawn. Also say that step 3 and the registered run report the same five figures for the drawn pilot and test sets, as a description.
- **Short decades.** The operator kind's forties hold only 40 to 45, and sums have no 99. Say how a decade with fewer than four other even or odd endings is split, for example one each where there are two.
- **The operator's range** is 10 to 45 (`split_sim_unit_unordered.out`), not 10 to 49 as line 669 and the change log say.
- **Which half is A.** The alternation starts "with a half drawn by the seed". Say which label the first half takes, so that the commitment is reproducible.

### RT-469, "fact" and the joint simulation's correlation (worth noting)

**Lines:** 837 to 842 (repeated facts), 1042 to 1047 (the resampling scheme), 718 to 719 (the distinct-facts tolerance).

- **Define a fact.** For the unit kind it could be the (factor, count) item, the unordered multiplication or the answer value. In the unit pool those number 81, 55 and 42, so about 40, 27 or 21 resampling units per half. The choice changes every unit interval, and with it the chance of F (RT-470). I suggest the unordered multiplication, since "3 florps each, 4 blicks" and "4 florps each, 3 blicks" ask the model for the same fact.
- **The correlation's source.** Say that the joint simulation takes its correlation between the bites items and the cells from the pilot, by kind and by fact. Also say what it assumes if the pilot is too small to estimate it, for example a stated range run as a sensitivity.
- **Cross-kind sharing.** Products twins behind the lookup rule share multiplications with the unit items. The scheme treats them as independent. That is acceptable if it is said.

### RT-470, F's per-kind rename and the bites size (worth noting)

**Lines:** 892 to 894 (condition 2), 1074 to 1079 (stage two's step 4), 1128 to 1129, 870 to 871 and 914 to 922 (the size).

1. **Scope and order.** Move the sentence "If it holds pooled but not in one kind, the outcome is Depends on one kind" out of the definition of "does not bite" and into stage two's step 4. Apply it only when conditions 1 and 3 hold, so that a case where the change ratio also fails stays "too weak to read". As written, it can be read as renaming an A or a C through the disagreement rule's use of "does not bite".
2. **The label.** Rename to "Depends on one kind" only if the failing kind's own loss is shown, for example with its interval's lower end above zero. Otherwise call it "too weak to read". Without that, imprecision in the unit kind is reported as an effect carried by the unit kind.
3. **The size.** My rough check (`own_loss_power.out`) used 100 items per kind, the trial's one-pass gains at the start placement (a quarter of the cost is 0.115 for the operator kind and 0.083 for the unit kind), a true own loss of zero, and a chance q that each donor run flips an item. At q = 0.10, the per-kind condition held:
   - 99% of the time for the operator kind;
   - 72% for the unit kind over 40 facts, and 61% if facts differ from one another with a standard deviation of 0.10.

   At q = 0.20 the unit kind held 26% of the time. More unit items help (83% at 200 items with fact effects), but with only about 40 facts per half there is a floor. The unit range is also harder than the trial's, so its one-pass cost, and with it the quarter, may differ. So "200 bites items are expected to be enough" (line 921) rests only on "bites", not on "does not bite" as now defined. Add the rule the pairs already have: if the simulation asks for more unit bites items than the fact pool and budget allow, the design returns to John.

### RT-471, small gaps in F's sentence and gates (worth noting)

**Lines:** 1074, 1152, 1159 to 1162, 872 to 878, 892 to 894.

- **"Cost neither cell of the pairs more than matched comparisons"** is not what the branch requires. R's and P's intervals need upper ends below δ, not intervals reaching zero. Say "cost neither cell of the pairs as much as δ (0.10) beyond matched comparisons". The same holds for D's sentence.
- **A per-kind one-pass floor for F.** The one-pass gate is pooled. A kind whose one-pass cost is near zero can meet F's per-kind condition only if the swap raised its accuracy. That is unlikely, but then F's reading, "what the extra passes supply on these problems", covers a kind that the passes did not help. Require each kind's one-pass point estimate to be at least 0.15 for F, or report the kind.
- **The pairs' own loss.** F requires the bites items' own loss to be small, but only the pairs' excess over random. If the operator and unit pairs' own loss has an interval above a quarter of the one-pass cost, while the bites items' own loss is small, rename to "Cells and bites check disagree". This is the same contradiction the rename catches for A and C, turned the other way.

### RT-472, stale and inconsistent text (worth noting)

- **Lines 153 to 155:** B and C "need no result from the bites check". They need the one-pass condition.
- **Lines 549 to 555:** "about 23 to 27" products, "about 196 to 220", "the arithmetic is in the tenth change log". Choice 8 now says 22 to 28 and about 216 to 220, recomputed under RT-463. Under version 0.12's seed rule, products per half come out at 25 to 30.
- **Lines 669 and 2011 to 2012:** the operator's answers are 10 to 45, not 10 to 49.
- **Lines 841 to 842:** "widening the range ... would make the unit problems harder than the trial measured". The range is already harder (line 734).
- **Lines 943 to 944:** F described as "a message from other inputs serves as well". The condition is now that it costs those problems little in each kind.
- **Lines 1003 to 1005:** "about 196 to 236 pairs ... about 130 to 150". Choice 8 now says about 216 to 236 and about 140 to 145 for the recommended allocation.
- **Lines 321 to 324:** the swap size's "changed positions" and "normalised" (RT-466, point 7).
- **Lines 1327 to 1329:** "a dose imbalance found at the registered run would cost the result". The dose is first measured at step 4b at either placement. The start lowers the risk that the test half fails the 10% rule after the pilot passed it.
- **Lines 1320 to 1325:** leave out the eleventh check's note that two independent baseline checks raise both placements to about 50% at f = 10%.
- **Lines 1355 and 1358:** "about 216 to 236" for four kinds and for 1 : 1 : 2 came from products pools of 18 to 23, not the 22 to 28 in the header.
- **Lines 1363 and 1380:** "17 to 18" operator pairs (test half) and "about 12" (pilot) are not labelled by half.
- **Lines 1373 to 1376:** "select on how the model did" is a weak reason. The cost in survivors is enough.

---

## Verdict

**Version 0.12 is ready for the battery specification and the pilot to be rebuilt (step 3), once John has ruled on choices 6 and 8. The remaining points can be carried into the specification and the registration text, without a version 0.13.**

It answers the eleventh check's four serious findings:
- **F is now safe to read as the prediction failing** (RT-457). The swap's own loss must be small, in each kind and under each method, and the message must have moved.
- **The disagreement rename** no longer takes away the clearest B, and for A and C it now fires only on the contradiction it was built for (RT-458).
- **The change ratio** can be computed for the swap, starts where it should, and is checked on the pilot before any test data, with the threshold fixed (RT-459).
- **The split** now matches the halves on the items within fixed tolerances, and a seed meets every tolerance in every kind: seeds 1, 8, 1 and 71 for the operator kind, the unit kind, sums and products (RT-460).

The worth-noting findings, the resampling scheme, choice 8's table, the cap's base, the unit range and the stale text are also answered.

What remains is seven worth-noting findings. None of them makes a reported reading of the prediction wrong. Each is either a definition the specification needs, a scope or label fix in the outcome rules, or stale text.

**For the battery specification (step 3), because step 3 and step 4b's code depend on them:**
- the change ratio for the five donors and for the average, the scale stated, the ratio reported by block, the swap size on the same scaling, and the options John has at step 4b if the ratio fails (RT-466);
- whether the split's tolerances apply to pools or drawn items, the short decades, the operator's range of 10 to 45, and which half is A (RT-468);
- what a "fact" is, and where the joint simulation's correlation comes from (RT-469);
- a return-to-John rule if the bites size the simulation asks for cannot be supplied (RT-470, point 3).

**For the registration text (step 5), before any data:**
- the disagreement rename gated on own loss alone (RT-467);
- F's per-kind rename placed in stage two's step 4, after the change ratio, and labelled "Depends on one kind" only when the failing kind's loss is shown (RT-470, points 1 and 2);
- F's sentence, a per-kind one-pass floor, and the pairs' own-loss check (RT-471);
- the stale text (RT-472).

**For John, with choices 6 and 8:**
- the corrected reason under choice 6 (RT-472);
- the eleventh check's note that two independent baseline checks raise both placements to about 50% at f = 10%;
- the expectation that the average method is the one likelier to fail the change ratio at step 4b (RT-466).

On the pattern the filer noted, that each round's fix has added a new serious finding: this round did not. The surface added in version 0.12 needs care in wording, but its logic holds.

The dose question (RT-345) stays open until step 4b, and nothing here bears on it.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **The operator's answer range (RT-468).** Confirmed: with operands 2 to 15 and the four rule shapes, the two-digit answers run from 10 to 45, not 10 to 49 as version 0.12 says.
- **Not rechecked by the filer:** the seed simulation behind RT-468 and the verdict (first passing seeds 1, 8, 1 and 71), the change-ratio arithmetic of RT-466, and the own-loss power estimate of RT-470.
- **Where things stand.** The reviewer finds version 0.12 **ready for step 3**, the battery specification and the pilot, once John has ruled on choices 6 and 8, with no version 0.13 needed. All four serious findings of the eleventh check are closed, RT-459 with conditions. RT-466 to RT-472 are worth noting, and each is to be settled in the battery specification. Choice 7 is needed before registration. The dose finding (RT-345) stays open until step 4b.
