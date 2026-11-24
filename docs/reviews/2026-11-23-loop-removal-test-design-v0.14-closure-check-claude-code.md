*Filed 2026-11-23 by the session that wrote the design, its fixes and the step-4b code, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote none of the design, its fixes, its reviews or its run code. It worked read-only in a detached worktree at commit c9cfa08, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.14

*Reviewer: a fresh Claude Code session. I did not write the design, any of its versions or fixes, the step-4b code or run, its findings, the rulings record or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure14-loop-design-2026-11-23` at commit c9cfa08, and put every script and output in my own scratch folder, `/private/tmp/claude-501/loop-review14-NMaJwc`. I changed nothing in the worktree, downloaded and installed nothing, made no network call and spent nothing. Dates are year-month-day; today is 2026-11-23. Line numbers are those of `docs/loop-removal-test-design-2026-11-20.md` at c9cfa08 unless another file is named.*

---

## What I opened

- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.14 header (lines 1 to 17); section 1's summary of how the prediction can fail (lines 183 to 195); section 3 in full (lines 243 to 392), because the reply rendering leans on its slot, donor and fallback rules; section 4 in full (lines 393 to 475); section 5 from the operator kind (line 580) to the neutral set (line 1160), which holds the interference checks, the new minimum-pairs rule, the bites check and its branch rule, the size rule and the pilot's size; section 6 in full (lines 1162 to 1265); section 7's outcome table (lines 1266 to 1295); section 9, "Order of work" (lines 1334 to 1412); section 11's new note on the author's additions (lines 1560 to 1572); and the change logs "from version 0.12" and "from version 0.13" (lines 2187 to 2254).
- **The diff** `git diff 795cba2 c9cfa08 -- docs/loop-removal-test-design-2026-11-20.md`, in full, and the same diff for the step-4b findings.
- **The closure check of version 0.13**, `docs/reviews/2026-11-23-loop-removal-test-design-v0.13-closure-check-claude-code.md`, in full, including the filer's note, which I read as the author's and not as part of that review.
- **John's rulings after step 4b**, `docs/rulings/2026-11-23-loop-removal-test-after-step4b-ruling.md`, in full.
- **The step-4b findings**, `experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`, the sections on the normal-range check and the bites one-pass condition, and the dated correction added in commit 978bf7b.
- **The step-4b run folder**, `experiments/10-loop-removal-test/step4b-run-2026-11-23/`: `collect-summary.json`, `quick/collect-summary.json`, `step4b-analysis.json`, `run-log.txt`, and `items.jsonl` (the bites items' unaltered and one-pass results).
- **The pilot bites set**, `experiments/10-loop-removal-test/batteries/pilot-v0.12/bites.jsonl`, for each item's rule kind and unit fact.
- **The code that ran or will be reused**: `src/step4b_collect.py` (the noise functions and the factor search, lines 295 to 421), `src/step4b_analyse.py` (the resampling and the bites one-pass condition), `src/step4b_simulate.py` in full (the committed sample-size simulation that version 0.14 now asks to choose the bites branch), and `src/build.py` (how items are rendered).
- **The battery specification's handling of the small gaps in F's sentence and gates (RT-471)**, `experiments/10-loop-removal-test/battery-authoring-spec.md` lines 530 to 545, because version 0.14's F sentence now cites it.
- **The model's tokeniser and chat template**, read-only, in `/Users/john/Code/minimum-viable-mind/.hf-cache.nosync/tml-d24-varloop-research-tokenizer/` (`chat_template.jinja` in full; `tokenizer.json` through the `tokenizers` library).

The highest finding number in the reviews and the experiment folder is RT-497, so my new findings start at RT-498.

## What I ran

All scripts are in my scratch folder, run with `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`. Their printed output is saved beside each one (`*-out.txt`).

1. **`render.py`**: the real chat template, rendered with the real tokeniser, for (a) an item-style user turn as `build.py` renders it, (b) a reply rendering with a stand-in fixed request at the template's default thinking setting, (c) the same at the setting the items use ("none"), and (d) the fixed opening alone. It counts the opening's tokens, checks that the prose tokenises identically after the opening, and lists the closing tokens the template itself writes.
2. **`seeds.py`**: the pooled bites one-pass interval's lower end on the step-4b data, recomputed over many resampling seeds, at 10,000 and at 100,000 resamples, with resampling by fact in the unit kind, both stratified within rule kind (as section 6 says) and unstratified (as `step4b_analyse.py` does for the pooled figure).
3. **`minpairs.py`**: the minimum-pairs rule applied to step 4b's confident-pair counts; the binomial chance that a pilot pairing of 13 pairs falls below three confident pairs, for several true confidence rates; and the path the factor search's halving takes when every evaluation falls short, over the old range (to 1,000) and the new one (to 100,000), set beside the two recorded searches (the quick try and the full run).

At the end, `git status --short` in the worktree printed nothing.

---

## The earlier findings, one by one

### The minimum pairing rule (RT-485): closed, with two points for the specification

**What version 0.14 does.** Lines 884 to 888 strike any pairing with fewer than three pilot pairs that pass the confidence check, and any pairing whose counting base is empty, "whatever the interference checks find". The number is marked as the author's.

**Is it well placed?**
- **Against the confidence check.** Consistent. It counts whole pairs that pass the confidence check, the same pairs that are scored, so it re-links the pairing table to the pairs that will actually be scored. That is what the hole needed.
- **Against the two interference checks.** Consistent. It is independent of them, so the order does not matter. An empty counting base is now handled. A counting base of one or two is struck by a single interfered item, which is accepted behaviour.
- **Against the strike-count rule.** Here there is a wording gap. The return to John at lines 880 to 883 reads "If **the two checks** together would leave fewer than three rule kinds, or would leave any rule kind with one routine kind or none". The new rule is a third way to strike a pairing, and the sentence does not name it. The new bullet's own reason ("the 'one routine kind or none' return to John would be bypassed") shows that the author means the count to include it, but a builder reading line 880 literally would count only the two interference checks. The specification should say "the two checks and the minimum-pairs rule together" (finding RT-499, below).

**Is three sensible at the pilot's allocation?** On step 4b's counts it does what it should. The operator pairings with colours and with opposites each had 2 confident pairs of 13 or 14, so both would be struck by this rule alone, leaving the operator kind with one routine kind, which returns the design to John. Every lookup and unit pairing (9 to 20 confident pairs) clears it easily. But three is a floor against emptiness, not a measure of a real second routine kind:
- A pilot pairing has about 13 pairs. If its true confidence rate is 20%, it falls below three about half the time; at 30%, about a fifth of the time; at 15%, it clears three about a third of the time. So the rule decides on a noisy count, in a region where the operator kind is likely to sit.
- **What it implies for the test half.** The test half holds roughly 1.7 times the pilot's pairs per pairing (about 22 against 13). A pairing that just clears three on the pilot will hold about 5 confident test pairs, before margin matching may drop up to a third and swap-size matching up to a tenth. Such a pairing counts as a second routine kind in the table, but it carries almost no weight in the cell, and leaving it out (the "Depends on one kind" reading) changes almost nothing. So the rule stops an empty pairing from hiding the one-routine-kind case, but it does not ensure that a rule kind's result rests on two routine kinds in any real sense. Nothing is checked on the test half itself: a test pairing that ends with zero pairs after the filters is not caught.

None of this makes an outcome wrong, because a thin pairing only weakens a protection, and a strike only returns the design to John. I grade it worth noting and ask only that the specification report the test half's pairs per pairing after every filter, and that the design not describe three as ensuring two routine kinds (finding RT-499).

### The fixed opening (RT-486): closed, with three small points for the specification

**What version 0.14 does.** Lines 418 to 425: everything before the first prose token is one fixed opening (the template's opening, the fixed request, the end of the user's message, the reply opening); all its positions are template slots counted from the start; the reply's end-of-message token is rendered and is the only closing slot; "plain text" is the prose's tokens alone.

**Is it buildable without guessing?** Nearly. With the real template and tokeniser, at the thinking setting the items use, and a stand-in request ("Write a short passage of ordinary prose."), the fixed opening is 23 tokens:

`<|message_system|> <|content_text|> Think ing Ġeffort Ġlevel : Ġ 0 <|end_message|> <|message_user|> <|content_text|> Write Ġa Ġshort Ġpassage Ġof Ġordinary Ġprose . <|end_message|> <|message_model|> <|content_text|>`

The prose then tokenises exactly as it does alone. Because every passage shares this opening and the model reads left to right, the true block sums at every opening position are the same for every passage. So the donor's sums there, the slot averages there and the passage's own sums are all one and the same vector, and neither method changes the opening. The claim at line 424 holds for the opening. Three points remain:
- **The thinking setting is not named.** The template writes "Thinking effort level: 0.9" when no setting is passed, which adds two tokens and a different instruction. The items are rendered with the setting "none", which writes "0" (`build.py`, `render`). The specification must fix the reply rendering's setting, and should use the items' setting.
- **The closing differs from the template's own.** The template renders a model reply as prose, then `<|end_message|>`, then `<|content_model_end_sampling|>`. The design renders only the first. That is a reasonable choice, because nothing after the prose enters damage, but it means the rendering cannot be produced by calling the template on a two-message conversation. The specification should say that the second closing token is dropped on purpose.
- **"Those are identical" is true of the opening only.** Line 424 says the slots get the reply rendering's slot averages under the average and "the donor's own sums under the swap; those are identical, because the opening is shared". The closing slot is not in the opening. Under the swap, a donor is at least as long as the recipient, so at the recipient's closing position the donor has a prose token, and the recipient's closing slot receives prose sums. Under the average it receives the closing-slot average. The two are not identical. This matters only for the swap size (the closing slot's distance counts toward it) and for any prediction made at the closing slot, which has no next token if the second closing token is dropped. The specification should say which predictions enter damage and the 1-nat check: I read it as the predictions of the prose tokens and of the end-of-message token, made at the last opening position through the last prose position.

These are specification matters. I grade the residue worth noting (finding RT-502).

### The role mismatch and the second average (RT-487): closed, with conditions

**What version 0.14 does.** Lines 426 to 437 mark the reading as the author's, measure a second, reply-built text average's damage beside the user-built one, return to John if the two damages differ by more than a factor of two, and otherwise use the user-built one "because it is the one the items get".

**Is it coherent?** Yes, as a bound. If the role mismatch inflates the user-built average's damage by more than a factor of two, John is asked; below that, it is tolerated. Two consequences should be stated rather than left implicit:
- **The tolerances stack.** The methods' own factor-of-two rule (section 6, lines 1258 to 1264) compares the swap's damage with the user-built average's. If the role mismatch inflates the average's damage by up to a factor of two without triggering the new rule, the methods' rule can pass an average that, judged by the reply-built average, is up to about four times milder than the swap. And the average's random comparison is matched to the inflated damage, so on the items, where the average is not inflated, the comparison may be harsher than the average and its excess understated. That pushes the average toward "no excess", so toward "methods disagree", or toward D or F if the swap lands there too. This is the residue of the earlier finding, now bounded at a factor of two.
- **Which average is "used" is clear in intent but not in every rule.** "The first ... is the one used" should be spelled out: the user-built average's damage feeds the methods' factor-of-two rule and its fallback trigger, the average's damage matching, and the average's normal-range bound. The reply-built average is measured and reported only, and feeds nothing else. A builder could otherwise read "used" as "applied to the items" only and match the comparison on either.
- **The fallback is not covered.** If the user-built average trips the methods' factor-of-two rule, it is replaced by the ten-bin fallback (section 3). The fallback is also built in the user's turn, so it carries the same mismatch. The design does not say whether a reply-built ten-bin twin is measured, or whether the factor-of-two check between the two averages applies to the fallback. Under section 3's "Nothing else may be chosen after seeing results", this must be fixed before the rerun's results are opened.

I grade the open points worth noting, to be fixed in the specification before the rerun's analysis is committed (finding RT-503).

### The unit-only branch carried through sections 5 to 7 (RT-488): closed, with stale text left

**What version 0.14 does.** The disagreement rename (lines 1208 to 1214) is restricted to the pairs whose rule kinds are in the bites set. D's and F's sentences (lines 1278 and 1279) carry bracketed words naming the kinds in the bites set, and F's drops "in each kind" when there is only one. F's sentence also now says "more than δ beyond matched comparisons", which the battery specification already carried for the gaps in F's sentence (RT-471).

**Are the conditional sentences right for both branches?**
- **D**, unit-only: "cost the held-out unit problems beyond matched comparisons ... The held-out problems share one kind with the prompt-rule cell". Right: the unit kind is in both, so D still has no reading.
- **F**, unit-only: "the extra passes helped the held-out unit problems ... cost them little". Right: in that branch the one-pass gate is on unit items alone, so "helped" is measured. Both kinds: "helped the held-out operator and unit problems ... in each kind". This is right only with the battery specification's reading of RT-471, which requires each kind's one-pass point estimate to be above zero; the design's gate is pooled. The citation at line 1279 covers that.
- **The rename**, unit-only: restricted to unit pairs. Coherent: without operator bites items there is no held-out operator result for operator pairs to contradict. A reader should know the consequence: in the unit-only branch, an A carried by the operator pairs has one fewer guard than in the both-kinds branch. That is a property of the branch, fixed before any test data, not a bias.

**What was not carried through.** Several places still assume two kinds:
- **Line 1139, the pilot's size**: "plus 80 bites items (40 of the operator kind, 40 of the unit kind; version 0.9)". The closure check of version 0.13 named this line under RT-488, and it is unchanged. It now contradicts line 953 (40 operator and 80 unit).
- **Line 990, "How many"**: "and 40 of each in the pilot". Same contradiction.
- **Line 1015, condition 2 of "does not bite"**: "In each of the two kinds ... for the operator bites items and for the unit bites items separately". Line 966 overrides it in words, but the condition itself should say "in each kind in the bites set".
- **Lines 186, 189 and 195, section 1's summary**: "the cell's operator and unit pairs contradict each other", "in each of the two kinds", "share two kinds with the prompt-rule cell".
- **Line 1219**: "does not contradict the held-out operator and unit problems".

None of these changes an outcome, because the branch bullet and the outcome table govern. But the pilot's-size line is a build instruction, and a builder reading section 5's own size paragraph would build 40 unit bites items, which cannot read the unit-only branch. I grade the remainder worth noting, with the two pilot-size lines to be followed from line 953 in the specification (finding RT-505).

### The bites threshold (RT-489): closed in intent; the rule that replaces it is not yet defined

Version 0.14 replaces the cut at 0.15 with the committed simulation's choice (lines 955 to 962), marked as the author's. That is the fix the closure check suggested, and it removes the near coin-flip and the trap in which keeping a barely qualifying operator kind made F unreachable. But the rule is not yet well enough defined to be run without a fresh judgement after the pilot is opened. That is a new finding (RT-500, below), so I count RT-489 as closed with a condition.

### The unit-only branch's power and pilot (RT-490): closed

The rerun pilot carries 40 operator and 80 unit bites items (line 953), so either branch can be read from one rental, and line 963 says the unit-only branch is expected to need John, quoting the closure check's 47% sketch accurately. Half A has 26 unit facts, so 80 unit bites items average about three per fact, which the "no whole-content repeat" rule allows. The two stale size lines are under RT-488 above. The rerun's price should include the extra 40 bites items and their donor-only items.

### The normal-range and in-loop comparison risk (RT-491): closed in part; the statement is not quite accurate, and the new factor rule does not catch the step-4b case

**What version 0.14 does.** Lines 444 to 455 state the risk for John at pricing; fix the factor search at 0.001 to 100,000 (the author's choice); and count a best factor "at either end of the range" as unmatched "unless its damage lies within 20%".

**Is the stated risk accurate against `collect-summary.json`?**
- "Matching the swap's damage took a factor of 987, at the top of the search's range, and it still fell 18% short." Accurate: factor 986.6, damage 0.930 against a target of 1.130, 17.7% short, with the code's range ending at 1,000.
- "The swap's damage is far beyond what random change of the same size does." Supported in direction, but not measured: the summary does not record the damage of noise at factor one, only its perplexity rises. What is known is that noise about 1,000 times the swap's own size still did 18% less damage.
- "That is the pattern on which the split removal test failed, where the ratio was 9.4, and here it is larger." This compares unlike measures. The split test's 9.4 is a ratio of damages at the same size. The figure here is a ratio of sizes (987) needed to approach equal damage, which is not the same thing. The damage ratio at the same size, the measure comparable to 9.4, was not recorded, so "here it is larger" cannot be checked. It should say what was measured: same-size noise was not measured on damage; noise a thousand times larger fell 18% short.
- **The statement names the swap only.** The average's in-loop comparison needed a factor of 3.9. By construction, a comparison matched at a factor above one is larger than same-size noise, so whenever perplexity rises with the size of the noise it will also lie above the normal-range bound, which is set by same-size noise (factor one). So the risk is not only that the swap's comparison cannot be matched: any comparison matched well above factor one, under either method, is likely to fail the normal-range check, and "the normal-range check fails ... for the random comparison" is itself a stage-one "not testable" (line 1183). In the user turn the signs were unreadable, so step 4b cannot show this. But it is a structural expectation, and John should hear it with the rest.

**Is the new factor-search range and edge rule sound?** No, for two reasons, and this is the most consequential point in this check (finding RT-498, below):
- **The step-4b data point to a ceiling, not to a range that was too short.** The design itself says that "past some size more noise stops adding damage" (line 458), because the readers normalise what they read. The two recorded searches agree on where that ceiling is: the quick try's best factor was 274, with damage 0.932, and its search found 422 at or above its target of 0.945; the full run evaluated factors from 422 up to about 999, all short of 1.13, and its best, 987, gave 0.930. So the damage is about 0.93 to 0.95 from a factor of about 270 to 1,000, on two different sets of passages. That is a plateau. Extending the range to 100,000 adds only more plateau.
- **The edge rule does not catch the step-4b case, and on a plateau it may not fire at all.** At step 4b the best factor's damage was within 20% of the target (17.7% short), so under version 0.14's rule it would count as **matched**, although the design's own text calls it 18% short and the cause is the ceiling. And when every evaluation falls on a plateau, the halving search's "best" factor is whichever plateau evaluation came closest by the luck of its five draws. With the new range, the halving visits 10, 1,000, 10,000, 31,623 and then climbs toward 100,000, so the best may be 1,000 or 31,623, which is not "at either end", and the rule does not fire. "At either end" is also undefined for a halving search, which never evaluates the endpoints themselves.

So the edge rule can admit a random comparison that is systematically about a fifth weaker than the main removal because it has hit its ceiling. A weaker comparison inflates the excess loss in both cells (the main removal's loss minus the comparison's), which makes C likelier and D and F harder to reach. That would make a reported outcome misleading.

**Is anything else owed before the rerun is priced?** Yes, and it is cheap:
- John should be told that step 4b already shows a ceiling for in-loop random noise at about 0.93 to 0.95 in damage, and that the swap exceeded it in the user turn. The rerun on the reply rendering will show whether it exceeds the ceiling there too. If it does, the in-loop comparison as defined cannot be matched at any factor.
- The closure check of version 0.13 asked that, if a different comparison or bound might be wanted, John be asked now rather than after another rental. Version 0.14 says instead that the risk is stated "so that no different bound or comparison is chosen after seeing more results" (lines 451 to 453). That protects against choosing after the fact, but it leaves the most likely result of the rerun as "the design returns to John" with no alternative written down. Whether to write a fallback comparison now (for example, noise added after the readers' normalisation, or a replacement by a random real message), or to accept that the swap may end unmatched, is John's call, and it should be put to him when the rerun is priced, before any rerun data exist.
- The rerun should report the damage at a fixed ladder of factors (for example 1, 10, 100, 1,000, 10,000), not only the search's best, so that a plateau is visible and the damage of same-size noise, the measure comparable to the split test's 9.4, is recorded.

### The bites one-pass gate and the resampling seed (RT-492): closed, with conditions

**What version 0.14 does.** Line 994: "Gate decisions use 100,000 resamples", with the 20-seed spread reported when a decision lies within 0.005 of its threshold. Lines 996 to 997 report step 4b's near miss. The findings carry a dated correction.

**What I found on the step-4b data** (`seeds.py`). With 10,000 resamples, the pooled lower end ran from 0.1453 to 0.1526 over 20 seeds and reached 0.15 on 7 of 20 (my random stream differs from the analysis code's, which gave 9 of 20; the spread is the same). With 100,000 resamples it settles at 0.1484 to 0.1500, reaching 0.15 on 1 seed of 10, stratified within rule kind or not. So **under version 0.14's own rule, step 4b's one-pass gate fails**, narrowly. That is the reading John should have when the rerun is priced: the gate is not a coin flip at 100,000 resamples but a narrow miss, and the simplified operator may lower the pooled cost further. Lines 996 to 997 should say so.

Three smaller points:
- **The two resample counts conflict.** Section 6 (line 1167) still says intervals come from 10,000 resamples, and "gate decisions" is not defined. Is the bites "bites" and "does not bite" test a gate? Are the cells' intervals for A to F? The specification should list which intervals use 100,000 (I suggest all intervals that decide anything, since the cost is computing time only) and correct line 1167.
- **The sentence order is broken.** The new sentences sit between "with the interval's lower end at or above 0.15" and "Otherwise the setup is wrong, and the result is not testable" (line 997), so "Otherwise" now follows the report of step 4b's seeds.
- **The pooled resampling is not stratified in the code.** Section 6 says resampling is done within each rule kind; `step4b_analyse.py` resamples the pooled bites units across kinds. On step 4b's data it makes no difference (above), but the rerun's code should follow the design.

I grade these worth noting (finding RT-501).

### The single-step operator's side effects (RT-493): closed, carried into the specification

Line 813 now hands the operator's operands and constants to the specification, and section 11 marks "with a written constant" as the author's (line 1570). The one-digit answers, crowded answers, the practised sum as a candidate and the donor counts are left to the specification, as the earlier check allowed. Two residues:
- The in-place text at lines 580 to 582 still attributes "with a written constant" to "John's ruling after step 4b" with no mark beside it; only the section 11 note marks it.
- The two-step operator's figures (the pass gain of 0.37, the survival rates by pairing, "Its pairings hold 7, 12 and 11 pilot pairs") still stand as reasons in section 5 without a "superseded" mark. The change log says they go to the specification, which is acceptable, but a reader of the design is not told.

### The author's additions (RT-494): closed, with the list incomplete

Section 11's note (lines 1560 to 1572) lists nine additions. Against the version 0.13 and 0.14 changes, these are also the author's and are missing (finding RT-504):
- version 0.13's rewriting of the "single items" rule as automatic, which the closure check of version 0.13 named;
- the factor of two between the two averages, as a threshold (the note lists the second average but not the number or its return to John);
- the edge rule for the factor search, beside its range;
- gate decisions at 100,000 resamples, the 0.005 window and the 20 seeds;
- the rerun pilot's 40 operator and 80 unit bites items;
- the restriction of the disagreement rename to the kinds in the bites set, which is a change to an outcome rule, not only to wording;
- dropping `<|content_model_end_sampling|>` from the reply rendering, and the definition of "plain text";
- the decision to state the RT-491 risk rather than ask John now about a different comparison or bound.

### Items pushed below the confidence bar (RT-495): closed

Lines 878 to 880 add the per-pairing report the earlier check asked for.

### The 1-nat check (RT-496): closed

Lines 438 to 443 report three renderings and say plainly that the check shows only that the model predicts the prose there, not that damage there tracks the items. The positions it averages over are a specification point (RT-502).

### Stale text (RT-497): mostly closed

Fixed: the pilot's-size counting base (lines 1141 to 1145), the operator's range (line 813), the pairs per pairing (line 881), the unit facts (lines 935 to 936), the neutral passages' wording (lines 1149 to 1150), and the findings' perplexity figure (1,870, which I confirmed against `collect-summary.json`, 1,869.2, and the quick try's 2,617). Version 0.13's change log line is left as written and corrected in version 0.14's log, which is reasonable. Left: the two-step operator figures (under RT-493 above), and new stale text listed under RT-505.

---

## New findings

**RT-498. The factor search's edge rule cannot catch a ceiling, and step 4b already shows one. Serious; it does not hold back the rebuild, but the specification must replace the rule before the rerun's analysis is committed, and John must hear the ceiling evidence when the rerun is priced.**
Lines 444 to 461; `collect-summary.json` and `quick/collect-summary.json` (`factors.loop_swap`); `src/step4b_collect.py` lines 401 to 421.
- In-loop noise has a damage ceiling, which the design itself predicts (line 458). Both recorded searches sit on it: about 0.93 to 0.95 from a factor of about 270 to 1,000, on two different passage sets. Widening the range to 100,000 adds only more ceiling.
- At step 4b the best factor's damage was within 20% of the swap's, so version 0.14's rule would count it as matched, although it was 18% short because of the ceiling. And on a ceiling, the halving search's best factor lands wherever its draws happened to come closest, often not "at either end", so the rule need not fire at all. "At either end" is also undefined for a search that never evaluates its endpoints.
- A comparison held about a fifth below the main removal by its ceiling inflates the excess loss in both cells, which makes C likelier and D and F harder.
- **Fix, for the specification:** a comparison counts as matched only if the search brackets the target, meaning at least one evaluated factor gave damage above the target and one below, and the final twenty-draw damage is within 20%. Otherwise it is unmatched, and the design returns to John (lines 459 to 461). The rerun reports damage on a fixed ladder of factors, including factor one.
- **Fix, for the design or the pricing note:** state the ceiling evidence; restate the comparison with the split test in like measures (the same-size damage ratio was not recorded); add that a comparison matched well above factor one, under either method, will likely fail the normal-range check too; and ask John, before the rerun, whether a fallback comparison should be written down now.

**RT-499. The minimum-pairs rule is not named in the return-to-John count, and three is a floor, not two real routine kinds. Worth noting.**
Lines 876 to 888.
- Line 880 counts what "the two checks together" leave. The new rule is a third way to strike a pairing; the count should name it.
- At about 13 pilot pairs a pairing, a true confidence rate of 20% falls below three about half the time. A pairing that clears three will hold about 5 confident test pairs before matching. It then counts as a second routine kind while carrying almost no weight.
- **Fix, for the specification:** count the minimum-pairs rule in the return to John; report the test half's pairs per pairing after every filter; do not describe the rule as ensuring two routine kinds.

**RT-500. The branch choice by simulation is not yet defined well enough to run without a choice made after the pilot is opened. Serious; it can be carried into the specification, but the branch simulation must be written and committed before the rerun's results are opened.**
Lines 951 to 970 and 1095 to 1104; `src/step4b_simulate.py` lines 152 to 176.
- **Which spreads.** "Each kind's measured one-pass cost and spread" fixes the one-pass target. The "bites" target needs the spread of the excess loss (main removal minus random comparison), and the "does not bite" target needs the spread of the removal's own loss and the change ratio (all three conditions, line 1099). The committed code uses the one-pass spread for all three, omits the change ratio, and tests each kind alone at 100 items, not the pooled gate.
- **Shared facts.** The unit kind is resampled by fact, and the unit-only branch rests on about 29 facts. The code models shared facts only in the cells, with a share of variance (0, 0.3 or 0.6) that it says is "not measured"; its bites part ignores facts. The branch decision turns on that share, and the rule does not say which value decides. The pilot, with about three unit bites items per fact, can estimate it; the rule should say so, or fix the most cautious value.
- **Sizes.** The rule tests both kinds only "at 100 items a kind". "The size" (line 1095) finds the smallest size giving 80%, and the battery specification lets the simulation go up to 300 a kind. So a both-kinds set that reaches the targets at 150 a kind would be passed over for the unit-only branch, or for a return to John. The rule should test both kinds at every size the pools allow up to the specification's ceiling.
- **Order and ties.** Clear: both kinds if they qualify, else unit alone if it qualifies, else John. Good.
- **Bias.** The choice is made on half A and the outcome is read on half B, and it uses the one-pass cost and spreads, not the removal's effect, so it does not select on the result. Two residues: if spreads are taken from the pilot's removal runs, the pilot's removal data enter only through their spread, which is acceptable if fixed in advance; and keeping the operator because its pilot cost came out high will, on average, overstate its test cost, so the per-kind F conditions will be harder than simulated. That makes "Too weak to read" or "Depends on one kind" likelier, not a false A or F. The real risk is latitude: if the branch simulation is written after the pilot is opened, its spreads, shared-fact value and sizes can be chosen with the answer in view.
- **Fix, for the specification:** write the branch simulation now, committed before the rerun's results are opened, naming the spread used for each target, how the change ratio enters, resampling by fact in the unit kind with the shared-fact value fixed or estimated by a stated rule, the pooled one-pass gate in the both-kinds branch, and the sizes tested.

**RT-501. The resample counts conflict, and under the new count step 4b's one-pass gate fails. Worth noting.**
Lines 994 to 997 and 1167; `step4b_analyse.py` lines 31 to 39 and 164 to 177.
- At 100,000 resamples the pooled lower end on the step-4b data is 0.1484 to 0.1500 over 10 seeds, reaching 0.15 once. Lines 996 to 997 and the findings' correction call it a coin flip; under version 0.14's rule it is a narrow fail. John should hear that at pricing.
- Section 6 still says 10,000 resamples, and "gate decisions" is undefined.
- "Otherwise the setup is wrong" (line 997) now follows the wrong sentence.
- The analysis code resamples the pooled bites units across rule kinds, where section 6 says within each.
- **Fix:** name the intervals that use 100,000; correct line 1167; restore the sentence order; stratify the pooled resampling in the rerun's code; restate step 4b's result under the new rule.

**RT-502. The reply rendering's remaining build details. Worth noting; for the specification.**
Lines 418 to 425 and 438 to 443; `chat_template.jinja`; `src/build.py` line 100 to 103.
- The thinking setting is not named; the template's default ("0.9") differs from the items' ("none", rendered "0").
- The template's own reply closing is two tokens; the design renders one. Say that the second is dropped on purpose.
- "Those are identical" (line 424) holds for the opening, not the closing slot, where the swap gives a donor's prose sums and the average the closing-slot average.
- Which predictions enter damage and the 1-nat check is not stated (for plain text, the first prose token has no context).

**RT-503. The second average: what "used" covers, and the fallback. Worth noting; for the specification before the rerun's analysis.**
Lines 426 to 437, 327 to 340 and 1258 to 1264.
- Say that the user-built average's damage alone feeds the methods' factor-of-two rule and its fallback trigger, the average's damage matching and its normal-range bound; the reply-built average is reported only.
- Say whether the ten-bin fallback gets a reply-built twin and the same factor-of-two check. It is built in the user's turn and carries the same mismatch.
- State that the two factor-of-two tolerances stack, so the methods' rule can pass an average up to about four times milder than the swap on the items.

**RT-504. The author's-additions note is incomplete. Worth noting.**
Lines 1560 to 1572. Missing: the "single items" rule made automatic (version 0.13); the factor of two between the averages and its return to John; the edge rule; 100,000 resamples, the 0.005 window and the 20 seeds; the rerun pilot's 40 operator and 80 unit bites items; the narrowing of the disagreement rename to the bites set's kinds; the dropped closing token and the definition of plain text; and the choice to state the RT-491 risk rather than ask John now about another comparison. Also, the F sentence's "more than δ" edit (line 1279) is not in the version 0.14 change log, though it is cited in place.

**RT-505. Stale text introduced or left by the branch rule and the version change. Worth noting, except the two pilot-size lines, which the specification must follow from line 953.**
- **Line 1139:** "80 bites items (40 of the operator kind, 40 of the unit kind; version 0.9)". Named under RT-488 in the last check; unchanged; contradicts line 953.
- **Line 990:** "40 of each in the pilot". Same.
- **Line 1015:** condition 2 "In each of the two kinds ... operator ... and ... unit".
- **Lines 186, 189 and 195:** section 1's two-kind wording.
- **Line 1219:** "the held-out operator and unit problems".
- **Lines 1336 to 1342 and 1384:** section 9 says the closure check covers "version 0.13's changes" and that the pilot is rebuilt "for version 0.13".
- **Lines 580 to 582:** "with a written constant" attributed to John's ruling in place.
- **Line 17:** "the twelfth change log"; counting from version 0.1, the log "from version 0.13" is the thirteenth. (Version 0.13's header miscounted in the same way.)
- **The step-4b findings, the correction paragraph:** the original sentence "The cost is smaller than the scoring trial's figure ..." now runs on inside the dated, italic-headed correction, so it reads as part of the correction.

---

## Verdict

**Version 0.14 is ready for the specification and pilot to be rebuilt. Nothing found here should hold back that rebuild, and no version 0.15 is needed before it.** Every finding of the last check is answered: the minimum-pairs rule closes the empty-pairing hole; the fixed opening is buildable with the real template; the second average bounds the role mismatch; the unit-only branch reaches the outcome rules and sentences; the risk is stated for John. What remains is either a specification matter or text to tidy.

**The specification must carry these, before the rerun's results are opened:**
- **The factor search (RT-498):** replace the edge rule. A comparison is matched only if the search brackets the target and the final damage is within 20%; report damage at a fixed ladder of factors, including factor one.
- **The branch simulation (RT-500):** written and committed before the rerun, with its spreads, change ratio, shared-fact value, pooled gate and sizes stated.
- **The second average (RT-503):** what "used" covers, and how the fallback is treated.
- **The reply rendering (RT-502):** the thinking setting, the dropped closing token, the closing slot, and which predictions count.
- **The minimum-pairs rule (RT-499):** counted in the return to John; test-half pairs per pairing reported.
- **The resampling (RT-501):** which intervals use 100,000 resamples, stratified within rule kind in the code.
- **The pilot's bites set (RT-505):** 40 operator and 80 unit bites items, following line 953, not lines 990 and 1139.
- **The single-step operator (RT-493):** as the last check listed.

**Owed before the rerun is priced, to John, not before the rebuild:**
- The ceiling evidence for in-loop noise (about 0.93 to 0.95 in damage at factors from about 270 to 1,000, against a swap of 1.13 in the user turn), the likelihood that any comparison matched well above factor one fails the normal-range check, and the question whether a fallback comparison should be written down now (RT-498).
- That under the design's own 100,000-resample rule, step 4b's one-pass gate narrowly fails (RT-501).
- The rerun's added cost: 40 more bites items and their donor-only items, the reply-built average, and the three-rendering check.

**Text to tidy whenever the design is next touched** (no closure check needed for these alone): the stale lines of RT-505, the author's-additions list of RT-504, the sentence order and line 1167 of RT-501, and the "same-size" comparison in the stated risk (RT-498).

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-23. It closes nothing.*

- **The bites one-pass condition at 100,000 resamples (RT-492).** Confirmed. With 100,000 resamples and seeds 1 to 3, the pooled lower end is 0.1484, 0.1491 and 0.1488. On step 4b's pilot data, the condition fails narrowly under version 0.14's own rule. Version 0.14 and the step-4b correction called it a coin flip. At the larger number of resamples, it is a narrow fail.
- **Not rechecked by the filer:** the ceiling on in-loop noise damage behind RT-498, the reading of the simulation code behind RT-500, the template's thinking setting behind RT-502, and the list of missing additions behind RT-504.
- **Where things stand.** The reviewer finds version 0.14 **ready for the specification and pilot to be rebuilt**, with no version 0.15. Two serious points, the edge rule (RT-498) and the branch choice and its code (RT-500), must be settled in the specification and committed before the rerun's results are opened. Two facts go to John when the rerun is priced: in-loop noise appears to have a damage ceiling, and the pilot's bites one-pass condition narrowly fails at 100,000 resamples. The dose finding (RT-345) waits for the rerun.
