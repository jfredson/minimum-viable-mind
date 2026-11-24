*Filed 2026-11-23 by the session that wrote the design, its fixes, the step-4b code and the margin check, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote none of the design, its fixes, its reviews or its code. It worked read-only in a detached worktree at commit db53673, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check of the loop removal test design, version 0.16: the unit C and the ruled thresholds

*I am a fresh reviewer. I wrote none of the design, none of its fixes, none of its reviews and none of its code. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure16-loop-design-2026-11-23` at commit db53673, and put every script and output in my own scratch folder, `/private/tmp/claude-501/loop-review16-CTUb1c`. I changed nothing in the worktree (`git status` is clean), downloaded nothing, installed nothing, made no network calls and spent nothing. Written 2026-11-23.*

## What I opened

- The design, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.16 header (lines 3 to 19); section 1 (lines 174 to 233); the "other conditions" paragraph of section 3 and the section 4 table (lines 406 to 436); section 5's scoring and scale paragraphs (lines 513 to 586); the baseline checks, matching and bites check (lines 920 to 1198); the sample size and the simulation's conditions (lines 1199 to 1225); sections 6 and 7 (lines 1252 to 1387); section 9's order of work (lines 1427 to 1506); choice 9 in section 10 (lines 1610 to 1622); the section 11 notes on the margin ruling and the author's additions (lines 1668 to 1683); and the change log "from version 0.15" (lines 2398 to 2421).
- `git diff 7b1fdf3 db53673 -- docs/loop-removal-test-design-2026-11-20.md`, and the smaller diff of the ruling commit, `git diff 22b84af db53673`.
- The closure check of version 0.15, `docs/reviews/2026-11-23-loop-removal-test-design-v0.15-closure-check-claude-code.md`, in full, including the filer's check.
- John's ruling on choice 9, `docs/rulings/2026-11-23-loop-removal-test-choice-9-ruling.md`.
- The rehearsal data `experiments/10-loop-removal-test/step4b-run-2026-11-23/items.jsonl` (320 item records), and the pilot it ran on, `batteries/pilot-v0.12/` (pairs and bites items).
- The margin check's write-up `margin-power-check-2026-11-23.md` and its script `src/margin_power_check.py`.
- The code test's analysis `step4b-rerun-code-test-2026-11-23/step4b-analysis.json`, the analysis code `src/step4b_analyse.py` (the matching, the bites gate and the simulation inputs) and the simulation code `src/step4b_simulate.py`.
- The step-4b findings' paragraphs on damage matching (`step4b-findings-2026-11-23.md`, lines 140 to 200).

## What I ran

All with `python3 -I` from my scratch folder. The committed simulation module was imported read-only. Nothing was written into the worktree.

- `common.py`: loads the data, rebuilds the 72 pairs that pass the pairing table, the confidence check on both twins and donor eligibility (the margin check's set), and reproduces margin matching (61 pairs: 35 lookup, 26 unit, as the analysis reports). Resampling is within each rule kind, and by multiplication fact in the unit kind, as section 6 sets out.
- `unit_c.py` (output `unit_c.json`). C under four readings of its item set, each with a 10,000-draw interval; C by kind; the routine twins' one-pass cost and its paired difference from C; C on one random half of the pilot against the other; and how often the "wider than half of C" check would fire on pilots of 30 to 100 pairs.
- `power.py` (output `power.json`). Outcome A's power from **resampled real per-pair excess losses** in units of C. Each pair's excess is the main removal's loss minus its comparison's loss. The comparison's margin is the mean over its 20 draws, taken once and not divided again. Both methods and both cells come from the same resampled pair, so their real correlations are kept. The excesses are centred within each pairing, a gap is planted on the prompt-rule cell, and the outcome is read with the committed `outcome_with_renames` (every rename by kind), with δ = 0.5. It was run at 80, 140 and 200 pairs, with true gaps of 1.0, 0.75, 0.5 and 0, with C fixed and with C drawn as a 72-pair pilot would give it, plus three "no true gap" cases built to tempt a false A. There were 1,000 runs per cell, and a small check of the normal-approximation interval against a percentile resampling interval.
- `bites.py` (output `bites.json`). The bites items' one-pass costs and the ratios of own loss, comparison loss and excess to the one-pass cost, by kind and method. It also resamples real bites items at the test half's sizes (both kinds at 100 and 100, the unit kind alone at 200 over 29 facts, and the operator alone at 100, with its pass gain also halved) to read three things: the one-pass condition against a quarter of C, "bites" when the true excess is three quarters of the one-pass cost, and "does not bite" when the true own loss is zero. 1,000 runs each.
- `room.py` (output `room.json`). The average margins under each condition, in units of C, and how far below the comparison's margin a removal could push the cells before it reaches the 5th percentile of the single-run margins seen in step 4b.

## The earlier findings

### The anchor finding (RT-506): closed

Version 0.16 replaces K, the ratio of a margin loss to a right-or-wrong loss, with C, the prompt-rule items' mean one-pass loss in margin (lines 547 to 552). The thresholds are shares of C, and John ruled their values (lines 555 to 558; the ruling file).

**C is well defined and computable, apart from one detail** (the C-definition finding, RT-515, below).
- **Which items.** Prompt-rule items that pass the baseline checks and the confidence check, before margin and swap-size matching (line 548).
- **Which passes.** The unaltered three-pass margin minus the one-pass margin (line 549).
- **Where it is fixed.** On the pilot at the step-4b rerun, never recomputed on the test half (lines 550 and 551).

**Recomputed on step 4b's data.**

| Reading of the item set | Items | C, nats | 95% interval |
|---|---|---|---|
| Pairs with both twins confident and a donor (the margin check's set) | 72 | 4.19 | 3.69 to 4.68 (−12% to +12%) |
| Prompt-rule item confident, twin not required | 76 | 4.24 | 3.72 to 4.73 |
| The same, with a donor | 75 | 4.23 | 3.71 to 4.73 |
| After margin matching, for comparison only | 61 | 4.32 | 3.80 to 4.82 |

The design's 4.19 nats, 3.6 to 4.8, matches. C on one random half of the pilot divided by C on the other half lies between 0.75 and 1.33 (95%), against 0.25 to 3.65 for K. **The noise that sank K is gone.**

**What C's noise now costs.** Outcome A's power is the same with C fixed and with C drawn as a 72-pair pilot would give it (99.0% against 99.1% at 80 pairs; table under item 2 below). The only visible effect is at a true gap equal to δ, where A appears in 23 to 24% of runs with C fixed and 28 to 30% with C drawn. That is the expected small loosening, and it is not a false A, because a true gap of δ meets the threshold.

**The "wider than half of C on either side" check** (lines 553 and 554) is sensible in direction. It is very loose. On pilots resampled from step 4b's items, the 95th percentile of the interval's wider side was 30% of C at 30 pairs and 22% at 72 pairs, and the check fired in none of 300 pilots at any size from 30 to 100 pairs. So it guards only against a degenerate pilot, such as one where a kind is lost and C rests on a handful of items. At its limit it would let δ in nats vary by a factor of three, from 0.5C to 1.5C. That is harmless at the precision C actually has, but a bound of about a quarter of C would match what the check is for (RT-515).

**Fixing C on half A and applying it to half B is sound.** C is computed before any test data, so it cannot be tuned to them. Its error does not shrink with the test half's size, but it is now about ±12%, and it costs no measurable power.

**C still depends on the mix of kinds, but much less than K did.** The lookup items cost 2.75 nats at one pass and the unit items 5.98, so C is a weighted mix. It will move when the simplified operator kind enters and the letter-code kind leaves. That is what option (a) of choice 9 says it wants ("follows the rebuilt pilot"). Because both cells are divided by the same C, the gap is unaffected in sign and only rescaled.

One historical note. Choice 9's recommended values "round the values the accuracy scale implied on step 4b's data, 0.57 and 1.15" (lines 557, 558 and 1614). Those two numbers were derived through the withdrawn K (0.10 × 24.1 ÷ 4.19 and 0.20 × 24.1 ÷ 4.19), so with K's own range they could have been anywhere from about 0.36 to 1.2 for δ. John ruled the values on their plain meaning, "half of what one pass costs" and "as much as one pass costs", so this does not weaken the ruling. The sentence should not be read as independent support.

### The units finding (RT-507): closed for the cells; closed with conditions for the bites conditions

- **"Accuracy-equivalent" is gone.** The cells' thresholds are now named as new thresholds on a new measure, ruled by John (lines 543 to 568).
- **The thresholds in nats.** The design gives C in nats and a quarter of C as about 1.05. δ (2.09 nats on step 4b) and the target gap (4.19 nats) follow from C, which is written into the registration. That meets the request to report each threshold in nats. The registration should still print δ and the gap in nats beside C.
- **The bites conditions are not closed as asked.** Line 559 still says "The bites items need no conversion. Their conditions are ratios of their own one-pass cost in margin". The closure check of version 0.15 found exactly that sentence misleading, because the ratios do not mean on the margin what they meant on accuracy, and it asked that they be marked as carried over by number. They are not in the section 11 list of the author's choices (lines 1674 to 1679). On step 4b's data, on the margin:

| Bites items | One-pass cost, nats (95%) | Own loss ÷ one-pass, swap / average | Excess ÷ one-pass, swap / average |
|---|---|---|---|
| Operator (40) | 1.81 (1.00 to 2.69) | 1.95 / 1.75 | 0.31 / 0.06 |
| Unit (40, 22 facts) | 5.93 (5.25 to 6.62) | 1.43 / 1.55 | 0.01 / 0.06 |
| Pooled | 3.87 (3.25 to 4.45) | 1.55 / 1.60 | 0.08 / 0.06 |

So "the removal bites", which needs an excess of at least half the one-pass cost, would have been met by neither method on step 4b's margins. That is partly because step 4b's comparisons were matched with noise about a thousand times the swap's size, and pushed items as far as the removal did (the room finding, RT-513). The consequence is limited. A failed "bites" turns D into "too weak to read", and both carry no reading. The condition that carries a reading, "does not bite", is reachable (item 3). **Condition:** add the three ratios to the section 11 list as carried over by number onto the margin, and replace "need no conversion" with a sentence saying they are the same numbers on a new measure.

### The wording finding (RT-508): closed

- **Section 1.** A new bullet at lines 210 to 214 says every loss is a loss of margin, that an outcome can be reached with no change in which answers are right, and that the share of right answers is reported beside every outcome.
- **Section 7.** A new preamble at lines 1363 and 1364 says the same. Outcome A's sentence now reads "lowered the model's confidence in the right answer (its margin among five fixed choices)" (line 1368). The sentences for B, C, D and F are written as continuations ("...cost more on the routine questions...") and inherit the preamble.
- **Section 1's "collapses"** (line 179) is H1's own prediction, quoted from the proposal, and the new bullet says how this test measures it. That is acceptable.
- **A small imprecision, not graded.** "Confidence in the right answer" is a fair plain gloss, but the margin is the right answer's lead over the best wrong one. A fall from +2 to −3 means the model now prefers a wrong answer, which is more than lower confidence. "How far the model's preference for the right answer over its best wrong rival fell" would be exact.
- **Is anything else in sections 1 to 7 still read as accuracy?** I searched sections 1 to 7 for thresholds, "normalised", "accuracy" and "right or wrong". What remains is either the interference and rule-is-needed checks (lines 924 to 966), which stay on accuracy by John's ruling, or history (lines 1046 to 1048, 1058 to 1068 and 1161 to 1187). The live stale passages are in section 5's bites and sample-size paragraphs. They are listed under the stale-text finding, RT-516.

### The definitions finding (RT-509): closed, with one detail carried into the code

- **Each condition's margin** is now defined (lines 577 to 582): the swap over up to five donors, as section 3 sets out; the average and its fallback; a comparison as the mean over its 20 draws; and fewer passes. Lines 536 to 538 still say "its five donors", while line 578 says "up to five". That is harmless, but the code should follow line 578.
- **C's item set** says "before margin and swap-size matching". It does not say whether the routine twin must also pass the confidence check, or whether a prompt-rule item with no eligible donor counts. The differences on step 4b are about 1% (table above), but the code needs one answer (RT-515).
- **K_b's circle is gone**, because K_b is withdrawn and the bites conditions are ratios of the bites items' own cost (lines 559 to 561). The one-pass condition needs only C, which comes from the cells, so it no longer depends on the branch choice.

### The margin check's method (RT-510): carried into the code, as the design says, with one addition

The change log (lines 2416 and 2417) assigns the double division by √20 to `src/step4b_simulate.py`, which is right. The closure check of version 0.15 also asked that the committed simulation **resample real per-pair losses, keeping the two methods and the two cells joint**, in place of independent normal draws. Version 0.16 does not carry that forward. The text of "The simulation's conditions" (lines 1219 to 1225) still describes a simulation built on "the spread and the comparison loss". My own run shows why it matters. The real per-pair gap under the average has a spread of 1.55 C, against 0.65 C under the swap. The two methods' per-pair gaps correlate at 0.46. Normal draws with independent cells would misstate both. **Condition:** the specification for the margin simulation should say it resamples real per-pair excesses jointly, as `power.py` here does.

### Stale text and marking (RT-511): partly closed

Fixed:
- the role of fewer passes in section 3 and the section 4 table (lines 406, 407 and 435);
- the section 11 list of the author's additions (lines 1674 to 1679).

Not fixed, or only half fixed:
- line 1202 now says "a true **normalised** gap equal to the target of choice 9 (in units of C)", which is self-contradictory;
- lines 1205 to 1216 still quote the old sizes on the right-or-wrong scale without saying they are history;
- lines 1084 to 1086, which the closure check of version 0.15 named (as lines 1045 to 1047), are unchanged.

These and the new stale passages are gathered under the stale-text finding (RT-516).

### Starting margins and margin matching (RT-512): closed

Lines 583 to 586 state the risk and requires the two cells' mean starting margins beside every outcome, which is what was asked. The sensitivity analysis was left as the author's call, which is acceptable. In units of C, the closure check's bound of "about a fifth of δ" is about 0.1 C, or 0.5 nats.

## Checks on the ruled thresholds

### 2. δ = 0.5 and a target gap of 1.0, in units of C

**Coherent and written in everywhere they act:**
- section 5 (lines 555 to 558);
- section 6, where "δ is choice 9's value, in units of C" (line 1257), and every outcome rule refers to δ;
- section 10 (lines 1610 to 1622);
- section 11 (lines 1681 and 1682);
- the sample-size paragraph (lines 1202 and 1203).

The exception is the simulation's conditions (lines 1219 to 1221), which still say "a true gap of 0.20" in "the margin units of section 5 (version 0.15)". A coder reading that paragraph could plant 0.20 (RT-516).

Choice 9's own text in section 10 is not marked as ruled. The ruling file says the design "needs no change beyond a note that the choice is ruled". That note was added in sections 5 and 11, but not under choice 9 itself (RT-516).

**Outcome A's power, from resampled real per-pair losses, in units of C** (A under both methods, after every rename; 1,000 runs each):

| True gap (units of C) | C | 80 pairs | 140 pairs | 200 pairs |
|---|---|---|---|---|
| 1.0 (the target) | fixed | 99.0% | 100% | 100% |
| 1.0 | drawn from a 72-pair pilot | 99.1% | 99.8% | 100% |
| 0.75 | fixed | 98.2% | 100% | 99.8% |
| 0.5 (at δ) | fixed | 24.7% | 22.6% | 23.8% |
| 0.5 | drawn | 27.6% | 30.3% | 29.5% |
| 0 (no gap) | fixed or drawn | 0% | 0% | 0% |

**False A when the true gap is zero:**

| No-gap case | 80 pairs | 200 pairs |
|---|---|---|
| Both cells carry the same real excess of 0.45 C | 0% | 0% |
| The routine cell alone carries 0.2 C | 0% | 0% |
| The prompt-rule cell alone carries 0.45 C, just under δ (a true gap of 0.45) | 5.3% | 1.2% |

The last case is a true gap just under δ read as A. That is the price of a point-estimate threshold, and it is small.

The normal-approximation interval the committed code uses agreed with a percentile resampling interval in 150 of 150 runs at 80 pairs, both at the target gap and at δ.

**What this means.** With the ruled thresholds and C as the unit, the test is very well powered **if a true gap of 1.0 C can exist in the data**. On step 4b's comparisons it nearly cannot (the room finding, RT-513). The power figures above plant the gap without limit, as the version 0.15 check did.

### 3. The bites set in margin

**The one-pass condition, a lower end of at least a quarter of C (1.05 nats).** Against step 4b's figures:
- **Pooled** (3.87 nats, lower end 3.25): passes by a factor of three.
- **The unit kind** (5.93): passes by a factor of five.
- **The operator kind alone** (1.81, lower end 1.00): fails on the pilot's 40 items.

Resampled at the test half's sizes:

| Bites set | One-pass condition | "Bites" at three quarters | "Does not bite" at zero own loss |
|---|---|---|---|
| Both kinds, 100 + 100 | 100% | 99.9% | 14% |
| Both kinds, operator gain halved | 100% | 99.7% | 4% |
| Unit alone, 200 over 29 facts | 100% | 99.9% | 88% (90% with C drawn) |
| Operator alone, 100 | 82% | 99% | 15% |
| Operator alone, gain halved | 0% | 84% | 5% |

The "does not bite" column centres the real own losses, which is cautious. A removal that truly cost nothing would leave margins nearly unchanged, and its per-item spread would be smaller than that of a removal that flattens items.

- **Is a quarter of C sensible?** Yes, as a floor. It is about 1 nat, a factor of e in the odds of the right answer over its best rival. It is looser than the old 0.15 was in nats (about 2.2 nats through the pooled K_b of 14.6), and it compares unfiltered bites items with filtered prompt-rule items, so it is a sanity floor rather than a like-for-like share. Because the gate is pooled, a simplified operator kind that gained nothing from the passes would still pass inside a strong unit kind. That does no harm, because each kind's own one-pass cost then sets that kind's "does not bite" bar, and the branch choice would move to the unit kind alone.
- **Are "half", "three quarters" and "a quarter" coherent?** As arithmetic, yes, because both sides are in the bites items' own nats. As meaning, they are new bars on a new measure, covered under the units finding (RT-507) above.
- **Does "does not bite" become reachable?** Yes, through the unit-alone branch: 88% at zero own loss under the cautious spread, against the 80% target, with the one-pass condition and "bites" both near 100%. The both-kinds branch fails "does not bite" (14%) because of the operator kind's noise. So the branch choice should land on the unit kind alone. That is the reverse of lines 1049 to 1051, which still say the unit-only branch "is expected to need John" (RT-516).

## New findings

**The room finding (RT-513). Worth noting, but carried into the simulation code before the rerun is read.**
- **What it concerns:** line 569 ("It has no ceiling"); the simulation's conditions (lines 1199 to 1225); "the removal bites" (lines 1088 to 1092) and its size target (line 1125).
- **The problem:** the margin has no ceiling in principle, but in practice it has a floor. Once a removal scrambles an item, the right answer's margin sits a little below zero, and going much further would need the model to steer actively away from the right answer. On step 4b's data, in units of C:
  - **The prompt-rule cell under the swap's comparison** already sat at a mean margin of −0.34 C (−1.44 nats), and the swap itself at −0.44 C.
  - **What the target gap would need.** A true excess of 1.0 C would need the swap's five-donor average to fall to about −1.34 C (−5.6 nats), lower than the 5th percentile of single-run margins (−5.45 nats).
  - **The room on the bites items.** Under the comparisons, the unit bites items' "bites" target would need about 3 nats more loss than the comparison caused, from a starting point already below zero.
  - **The room under the average.** Its comparison was weaker, which left more room: about 1.7 C above the floor, and a real prompt-rule excess of 1.05 C.
- **Why it matters:** the power figures, the version 0.15 check's and mine alike, plant the gap with no limit, so they report 99% power for a gap that step-4b-like comparisons could hardly let through. Step 4b's comparisons were matched with noise about a thousand times the swap's size, and are to be remeasured on the reply rendering, so the rerun may well leave room. But nothing in the design checks for it.
- **What would fix it:**
  - The rehearsal reports, for each cell and method, the mean margin under the comparison and its distance above the floor, measured as the 5th percentile of single-run margins, in units of C.
  - The committed simulation caps a planted excess at that room, or reports power only for gaps the room allows.
  - Section 5's "no ceiling" sentence says that the scale has a practical floor near chance.
  - If the room in either cell is below the target gap, the design returns to John before registration. This adds no cost to the rerun.

**The routine cell's one-pass cost (RT-514). Worth noting.**
- **What it concerns:** lines 551 and 552 ("as much margin as dropping to one pass costs these items"), lines 556 and 557, choice 9 (lines 1614 to 1616), and the ruling's "no excess means less than half of what the extra passes supply".
- **Is one shared C right?** Yes. The gap G = P − R is only a difference of like quantities if both cells are divided by the same constant, and a separate routine constant would mix units.
- **The problem is the wording.** "What the extra passes supply" is true only of the prompt-rule cell. On the same 72 pairs:
  - the routine twins lost 5.42 nats at one pass against 4.19 for the prompt-rule items, a paired difference of 1.23 nats (95%: 0.43 to 2.09);
  - by kind the two run in opposite directions. The routine twins behind the lookup rule (sums and products) lost 8.27 nats, while those behind the unit rule (capitals, colours, opposites) lost 1.84;
  - on accuracy the routine twins lost 0.26 against 0.17.
  
  So R's bar, an upper end below δ = 0.5 C, is 0.39 of what one pass costs the routine twins themselves. A reader told that δ is "half of what the extra passes supply" would assume it is half for both cells.
- **What would fix it:**
  - say that C is the prompt-rule cell's one-pass cost and is used for both cells so that the gap is a difference of like quantities;
  - report the routine cell's own one-pass cost beside C at the rerun.

  This is the pass-gain pattern already recorded under the opposite-direction pass gains (RT-445), now visible in the unit itself.

**The C-definition finding (RT-515). Worth noting, for the specification.**
- **What it concerns:** lines 547 to 549 and 553 to 554, and section 11's "its ±50% check" (line 1678).
- **The gaps:**
  - it does not say whether a prompt-rule item counts when its routine twin fails the confidence check;
  - it does not say whether a prompt-rule item counts when it has no eligible donor.
  
  On step 4b these give 4.19, 4.24 and 4.23 nats, so the numbers barely move, but the code needs one rule. The natural choice is the pair-level set, both twins confident and a donor present, the 72 pairs the margin check used. That set is the one the cells are drawn from.
- **The anchor's own check:** "wider than half of C on either side" fired in none of 300 resampled pilots at 30 to 100 pairs. It is a guard against a degenerate pilot only. A bound of about a quarter of C would still never fire on a healthy pilot (the 95th percentile was 22% at 72 pairs, 30% at 30), and would catch a pilot where C rests on too few items. This is the author's call.

**Stale text after version 0.16 (RT-516). Worth noting. The first three items should be fixed before the margin code is written, because a coder would read them.**
- **Lines 1219 to 1221.** "in the margin units of section 5 (version 0.15). On step 4b's data, a true gap of 0.20 spread evenly was read as A in 94 to 96%". These are K's units, which are withdrawn, and figures from a simulation with the double division. They should be in units of C, a target gap of 1.0, citing a resampled simulation.
- **Line 1202.** "a true normalised gap equal to the target of choice 9 (in units of C)": drop "normalised".
- **Lines 1084 to 1086.** "The 0.15 is this design's own choice ... about 0.4 on the normalised scale, so the threshold is expected to be met". There is no 0.15 any more. The bar is a quarter of C, and on step 4b it was passed by a factor of three.
- **Lines 1080 and 1081.** The seed-spread rule, "within 0.005 of its threshold", was set for accuracy-scale gates. In nats, 0.005 is negligible next to a quarter of C (1.05). Say what tolerance applies on the margin.
- **Lines 1049 to 1051.** "The unit-only branch is expected to need John" was true on accuracy. On the margin the unit-only branch is the one that qualifies, and both kinds fail "does not bite".
- **Lines 1185 and 1186, and 1205 to 1216.** "the 120 to 200 the sample-size simulation is expected to ask for" and the older sizes are right-or-wrong history. On the margin the simulation will ask for the smallest size it tries. A one-line "history, on the old scale" note is enough.
- **Line 559.** "The bites items need no conversion" (see the units finding, RT-507).
- **Lines 570 and 571.** "The analysis resamples, so the tails widen the intervals honestly" is printed twice.
- **Section 9, step 1 (lines 1429 to 1434).** It still says the closure check "checks version 0.15's change of the outcome measure". **Step 2 (lines 1436 and 1437)** lists rulings to 2026-11-23's three questions after step 4b, but not the margin ruling or choice 9. The order the version 0.15 change log set out, a closure check, then the margin code, then the rerun priced, is not restated for version 0.16. It still holds.
- **Section 10, choice 9 (lines 1610 to 1622).** It still reads as an open choice, with no note that John ruled option (a).
- **Section 11's list of the author's choices (lines 1674 to 1679).** It omits three things:
  - the bites ratios carried over onto the margin;
  - the quantile reporting (line 572), which the closure check of version 0.15 named;
  - the choice to compute C before matching.
- **Line 1010.** The bites task is still labelled "K, held-out rule problems". It is an old label, unrelated to the withdrawn constant K, but a reader of versions 0.15 and 0.16 will stumble on it.

## Verdict

**Nothing is fatal and nothing is serious.** Version 0.16 does what the closure check of version 0.15 asked on the central point. C is measured in margin alone, is steady to about ±12% on step 4b's data, and costs no measurable power. With John's ruled thresholds, outcome A is read in 99% of runs at 80 pairs and 100% from 140 when the true gap is 1.0 C. It is never read when the true gap is zero. The anchor finding (RT-506), the wording finding (RT-508), the definitions finding (RT-509) and the starting-margins finding (RT-512) are closed. The units finding (RT-507) is closed for the cells, and closed with a condition for the bites ratios. The stale-text finding (RT-511) is only partly closed.

**Version 0.16 is ready for the margin analysis and simulation code. It does not need a version 0.17**, provided these points are carried into the specification and a short text fix:
1. **Before the code is written,** fix the three stale passages a coder would read: lines 1219 to 1221 (0.20 in K's units), line 1202 ("normalised") and lines 1084 to 1086 (the old 0.15) (RT-516).
2. **The simulation** resamples real per-pair excesses, keeping the methods and cells joint, and drops the double division by √20 (the margin check's method, RT-510). It caps planted gaps at the measured room, and the rehearsal reports that room, with a return to John if the room is below the target gap (RT-513).
3. **C's item set** is fixed in one sentence: pair-level, both twins confident, donor present (RT-515).
4. **The bites ratios** are marked in section 11 as carried over by number, and "need no conversion" is reworded (RT-507).
5. **The routine cell's own one-pass cost** is reported beside C, and the wording says C is the prompt-rule cell's cost (RT-514).
6. **The remaining stale lines** (RT-516) are tidied when convenient.

**Pricing the rerun need not wait for any of this.** The pilot and the collection are unchanged, and C and the room are computed from data the rerun collects anyway: the one-pass run, and the 20 draws of each comparison, which `items.jsonl` already records per draw. Nothing found here changes what is collected or how much of it.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-23. It closes nothing.*

- **The three stale passages (RT-516).** Confirmed by reading. Three passages still use the withdrawn units:
  - lines 1082 to 1086 give the old one-pass condition of 0.15 on the normalised scale;
  - line 1202 says "true normalised gap";
  - lines 1219 to 1221 give a gap of 0.20 "in the margin units of section 5 (version 0.15)".

  They are corrected in the commit after this filing, with dated notes, because a coder would read them.
- **Not rechecked by the filer:** the reviewer's resampled power figures (99% at 80 pairs, none when the gap is zero), the room figures behind RT-513, and the 300 resampled pilots behind RT-515.
- **Where things stand.** Nothing is fatal or serious. The reviewer finds version 0.16 **ready for the margin code without a version 0.17**, with points carried into the specification:
  - the bites ratios' wording and their marking as the author's (RT-507);
  - the simulation resampling real per-pair losses, with both methods and both cells together (RT-510);
  - the room cap on planted gaps, with a return to John (RT-513);
  - the one-pass meaning for the routine cell (RT-514);
  - C's item set (RT-515).

  Pricing the rerun need not wait. The dose finding (RT-345) waits for the rerun.
