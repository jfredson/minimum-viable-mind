*Filed 2026-11-23 by the session that wrote the design, its fixes and the step-4b code, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote none of the design, its fixes, its reviews or its run code. It worked read-only in a detached worktree at commit 795cba2, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing and spent nothing. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.13

*Reviewer: a fresh Claude Code session. I did not write the design, any of its versions or fixes, the step-4b code or run, its findings, the rulings record or any earlier review. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/closure13-loop-design-2026-11-23` at commit 795cba2, and put every script and output in my own scratch folder, `/private/tmp/claude-501/loop-review13-z9Rhqn`. I changed nothing in the worktree, downloaded and installed nothing, made no network call and spent nothing. Dates are year-month-day; today is 2026-11-23.*

---

## What I opened

- **The design**, `docs/loop-removal-test-design-2026-11-20.md`: the version 0.13 header (lines 1 to 17); section 3, "What is removed" (lines 226 to 375), because the reply rendering leans on its slot and fallback rules; section 4, "The comparison removals" (lines 376 to 429), in full; section 5 from "The operator's answers have two digits" to the neutral set (lines 520 to 560 and 690 to 1092), which holds the interference checks, the bites check and its new rule, the size rule and the pilot's size; section 6, "The outcomes" (lines 1093 to 1195), in full; section 7, the outcome sentences (lines 1196 to 1225); section 9, "Order of work" (lines 1264 to 1342); the section 11 notes added in c3f55d2 and de5a8eb; and the change log "from version 0.12" (lines 2103 to 2132).
- **The diff** `git diff 0596831 795cba2 -- docs/loop-removal-test-design-2026-11-20.md`, in full.
- **The ruling record**, `docs/rulings/2026-11-23-loop-removal-test-after-step4b-ruling.md`, in full.
- **The step-4b findings**, `experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`, in full.
- **The step-4b run folder**, `experiments/10-loop-removal-test/step4b-run-2026-11-23/`: `items.jsonl` (320 records: 240 pair items, 80 bites items), `collect-summary.json`, `step4b-analysis.json` and `run-log.txt` (including the one-passage diagnostic).
- **The pilot set**, `experiments/10-loop-removal-test/batteries/pilot-v0.12/`: `pairs.jsonl`, `bites.jsonl`, the first records of `neutral.jsonl`, and the unit-kind and products sections of `build-report.json` (the half A and half B pool sizes and fact counts).
- **The code that ran**, `experiments/10-loop-removal-test/src/step4b_collect.py` and `src/step4b_analyse.py`, in full.
- **The model's tokeniser and chat template**, read-only, in `/Users/john/Code/minimum-viable-mind/.hf-cache.nosync/tml-d24-varloop-research-tokenizer/` (`chat_template.jinja` in full, `tokenizer.json` through the `tokenizers` library).
- **The first lines of the previous closure check**, `docs/reviews/2026-11-21-loop-removal-test-design-v0.12-closure-check-claude-code.md`, to learn its last finding number and its form. I did not rely on its content. The highest finding number in the reviews and the experiment folder is RT-484, so my findings start at RT-485.

## What I ran

All scripts are in my scratch folder, run with `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I`.

1. **`recompute.py`**: the accuracy-based interference rule, recomputed per pairing from `items.jsonl` and `pairs.jsonl`. "Right" is computed from the five candidates' log-probabilities as "the right candidate alone is highest", which is the design's definition with ties counted as not right. I also checked that this agrees with the stored `right` field on every pair item in both the `unaltered` (full context) and `baseline` (other half left out) conditions: it does, with no mismatch. The script also gives confident-pair counts and median margins.
2. **`bites.py`**: the one-pass cost on the 80 pilot bites items, by kind and by operator shape; the number of distinct unit facts in the pilot bites set; the operator pair items' accuracy at one and three passes by shape; and a rough resampling sketch of the unit-only branch (200 unit items over 29 facts, each fact's items drawn from the pilot's unit facts), counting how often the one-pass interval's lower end reaches 0.15.
3. **`dose_tok.py`**: the swap-dose ratios (routine cell over prompt-rule cell) for each rule kind under both methods, recomputed from `items.jsonl`; the chat template rendered with a user request and an assistant reply, tokenised with the real tokeniser; a check that the same prose tokenises identically after the user header and after the model header; and the share of one-digit answers and the number of distinct answers for single-step shapes "a plus b plus c" with operands 2 to 15.
4. **`extra.py`**: per pairing, how many twins were confident without the other half and stayed right with it but fell below the confidence bar of 2.2, and how many stayed right but lost more than 3 nats of margin; and the pooled bites one-pass interval's lower end recomputed with 20 different resampling seeds.

At the end, `git status --short` in the worktree printed nothing.

---

## Results

### 1. The rulings: are they written in faithfully?

**Ruling 1, interference judged by accuracy.** Faithful. The design's wording (lines 796 to 826) matches the option John picked: an item counts as interfered with only if it is right without the other half of the shared context and wrong with it. Three things are added beyond what John chose, and none is marked as the author's own:
- a tie counts as "not right" (line 800);
- the share of a fifth is now counted over the pairs whose twin is right without the other half, not over the confident pairs (lines 805 to 807 and 824 to 825). The header (lines 6 to 8) explains why, but presents it as following from the ruling, not as a choice;
- the "single items" rule is rewritten as automatic (lines 808 to 809 and 826).

All three are reasonable, and the second is needed. But the house rule on authorship asks for them to be marked as the author's (finding RT-494).

**Ruling 2, damage measured on the model's reply.** Faithful in substance: the prose is rendered as the model's reply for damage, perplexity, damage matching and the normal-range bound, and stays in the user's turn for building the average (lines 393 to 405 and 1083 to 1086). Three things are added and none is marked as the author's:
- the 1-nat check with its return to John (lines 406 to 409);
- the "one fixed short request" (line 394);
- the reading that the average applied on the reply rendering is the user-built text average at prose positions, with reply-built averages at template slots (lines 401 to 405).

The third is one of two possible readings of John's words, and it matters (finding RT-487).

**Ruling 3, the operator kind simplified.** Faithful: single-step rules, three rule kinds kept, checked on the pilot before any test set (lines 534 to 538 and 896 to 906). Two additions:
- "with a written constant" turns John's example into a requirement (line 534). That is a narrowing, though a sensible one, because an operator with no constant would be practised arithmetic and not an invented rule;
- the bites rule (lines 896 to 906) is the gap the ruling record itself named. It is the author's rule, and line 2124 says it was fixed "for the case the ruling's question did not name", which comes close to marking it. The 0.15 point-estimate threshold within it is the author's choice and should say so.

**The dose claim in the header** (lines 14 to 16) checks out. Recomputed from `items.jsonl`, the routine cell's mean swap size over the prompt-rule cell's is 1.0071 (operator), 1.0048 (unit) and 1.0040 (lookup) under the swap, and 0.9986, 0.9986 and 1.0003 under the average. That matches the findings and the change log. The design rightly leaves the formal closure of the dose finding (RT-345) to the rerun, after the filters.

### 2. The accuracy-based interference rule

**Is it well defined?**
- **Ties.** Defined: a tie counts as not right in both conditions. A tie without the other half keeps the item out of the counting base. A tie with the full context makes a right-without item interfered. Ties are rare (the findings report 5 of 320 items at the unaltered run).
- **"Right".** Defined as the right candidate alone having the highest probability among the five. My strict computation agrees with the stored `right` field on all 240 pair items in both conditions.
- **The counting base.** Defined for both checks (lines 805 and 824). One case is missing: the base can be empty or tiny. A pairing in which no twin is right without the other half is "more than a fifth of zero", which is undefined. A pairing with a base of 1 to 4 is struck by one interfered item. That second case is accepted behaviour, but the empty case needs a rule (finding RT-485).
- **Single items against whole pairings.** Correct. An interfered item is wrong in the full context, so its margin is at most 0, below the confidence bar of 2.2, so its pair is dropped by the confidence check anyway.

**Does the new counting base avoid the emptiness problem?** Yes, for the reason the author gives. A confident item has a margin of at least 2.2, so it is always right, so no confident item can be interfered with. A share counted over confident pairs would therefore always be zero. Counting over the items right without the other half removes that problem.

But the new base introduces a different hole. The base is now decoupled from the pairs that will be scored. A pairing can pass both checks while holding no confident pair. The step-4b analysis code treated a pairing with no confident pair as struck (`struck = (not conf) or ...` in `step4b_analyse.py`). The design's text never said so, and under version 0.13 such a pairing stays in the pairing table and counts toward "two routine kinds per rule kind" (finding RT-485).

**Interaction with the other rules.**
- **The confidence check.** Consistent, as above.
- **The strike-count rule** (lines 829 to 836). Its reporting is updated: right-without counts, interfered counts and margins. Its old sentence "a pilot pairing has only about 6 to 11 pairs" (line 832) is stale: the step-4b pilot pairings hold 13 to 20 pairs, and the counting base is 9 to 20. The return-to-John rule counts routine kinds in the table, which is where the hole in RT-485 bites.
- **Margin matching.** Unaffected. It acts on confident pairs within each rule kind (lines 838 to 847).
- **The "Depends on one kind" readings.** Unaffected in form. Under the new rule more pairings survive (every lookup and unit pairing on the pilot), so there are more kinds to leave out, which is good. A pairing kept with zero or one scored pair would make its leave-one-out reading trivial (finding RT-485 again).

**The author's descriptive pilot figures, recomputed.** For each pairing below: the routine twins right without the rule, and how many of them were interfered with; then the prompt-rule items right without the routine fact, and how many of them were interfered with.

| Pairing | Routine twins: right without rule, interfered | Prompt-rule items: right without routine fact, interfered | Struck under version 0.13 |
|---|---|---|---|
| lookup + products | 20, 0 (0.00) | 20, 0 (0.00) | no |
| lookup + sums | 20, 0 (0.00) | 20, 0 (0.00) | no |
| operator + capitals | 13, 0 (0.00) | 9, 4 (0.44) | yes, by the mirror check |
| operator + colours | 13, 6 (0.46) | 12, 2 (0.17) | yes, by the routine check |
| operator + opposites | 9, 2 (0.22) | 9, 4 (0.44) | yes, by both |
| unit + capitals | 14, 0 (0.00) | 14, 0 (0.00) | no |
| unit + colours | 13, 2 (0.15) | 13, 0 (0.00) | no |
| unit + opposites | 12, 0 (0.00) | 13, 1 (0.08) | no |

Every figure the design gives at lines 810 to 813 is right:
- every lookup and unit pairing survives;
- the routine shares are 0, 0, 0, 0 and 0.15;
- all three operator pairings are struck;
- everyday colours behind the operator rule is the worst routine case at 6 of 13.

The design reports only the routine side. The mirror side, which strikes operator with capitals, is not mentioned, and neither is unit with opposites at 1 of 13. This is minor, but the table above is what the strike-count rule asks to see. The confident-pair counts also match the findings: 33 of 40 unit pairs and 9 of 40 operator pairs.

**Is the rule too lenient?** Somewhat, in a way that the confidence check partly absorbs. An item whose margin collapses but stays above 2.2 is kept. An item whose margin falls below 2.2 while staying right is dropped by the confidence check, but it is not counted toward the pairing's strike. On the pilot:
- In unit with opposites, 3 prompt-rule items were confident without the routine fact and fell below 2.2 with it, while staying right. Another 8 stayed right but lost more than 3 nats.
- In operator with colours, 4 routine twins fell from confident to below the bar while staying right.

Under the accuracy rule, unit with opposites passes the mirror check at 1 of 13. If "fell below the confidence bar because of the other half" were counted too, it would be 4 of 13, which is over a fifth. So the rule lets through a pairing in which the routine fact visibly pushes prompt-rule items off the confidence bar. The pairs that fall are dropped, so they do not enter the cells. But the survivors are then selected for robustness to the other half, on one side of the pair only. Margin matching works on means, not on that selection, and the random comparison corrects only for generic fragility. This is within John's ruling, and the option he picked promised only to catch the colours case, which it does. I grade it worth noting and ask only for reporting (finding RT-495).

### 3. Damage on the model's reply

**Is the reply rendering defined well enough to build?** Almost. The real chat template renders a user request and an assistant reply as:

`<|message_system|><|content_text|>Thinking effort level: 0<|end_message|><|message_user|><|content_text|>` + request + `<|end_message|><|message_model|><|content_text|>` + prose + `<|end_message|><|content_model_end_sampling|>`

I checked with the real tokeniser that the prose tokenises identically after `<|content_text|>` in either role, and identically to the pilot's neutral `prompt_ids`. So "the two renderings carry the same prose" holds token for token. Three things are not defined:
- **The fixed request and the three template tokens between it and the prose.** Section 3's slot rule counts template slots "from the start of the template's opening part and from the end of its closing part" (lines 299 to 301). In the reply rendering, three template tokens sit in the middle, after the request and before the prose. The request itself is user text that is neither prose nor template. The fallback's text span for a neutral passage is "every position of its prose" (line 315 to 316), so the request is outside it too. The design does not say what the average puts at these positions (finding RT-486).
- **The closing tokens** `<|end_message|><|content_model_end_sampling|>`: whether they are rendered at all. They carry no prose, so they do not enter damage, but they decide the slot counting "from the end".
- **"Plain text"** for the 1-nat check: with or without any leading special token. The step-4b diagnostic's plain-text figure of 2.3 nats is for one passage, and its rendering is not recorded in the design.

**Are the swap, the average, the slots, the comparisons and the normal-range bound well defined on it?**
- **The swap** is well defined. Every passage shares the same fixed opening, and the model reads left to right, so a donor's sums equal the recipient's at every position before the prose. The swap changes the prose only, as before.
- **The comparisons** are scaled to each position's own swap distance. They are therefore zero before the prose under the swap, and well defined.
- **The average** is defined at prose positions and at template slots that the slot rule can place, but not at the request (RT-486). If the request is treated as text, as the items' user text is, the average changes positions the swap never changes. The noise comparison for the average would then also act there, because it follows the average's distances. If the request is treated as part of a fixed opening, the reply-built slot averages there equal the true sums, and the average changes the prose only. The two readings give different damages for the average. That feeds the factor-of-two rule, which stood at a factor of 1.85 at step 4b, and the average's damage matching.
- **The normal-range bound** is "the same rendering" (line 405), and well defined once the above is.

**Is it coherent to build the average in the user's turn and apply it at reply positions?** Partly. The average the items get is applied at user-turn positions, where it was built. On the neutral reply rendering, the same vector is applied at reply positions, where the true sums come from a different role. The swap, by contrast, uses donors from the same reply rendering. So on the neutral set, the swap is applied within its own role and the average across roles. The average's measured damage then includes a mismatch of role that it never meets on the items' user text. Two uses of that damage follow:
- **The factor-of-two rule** (lines 1188 to 1194) asks whether the two methods are comparably harsh. An average inflated by the mismatch can pass the rule even when, on the items, it is much milder than the swap.
- **The average's comparisons** are scaled to the inflated damage, and then act on the items, where the average itself is not inflated. Its excess loss in the cells would then be understated. That pushes the average toward the "no excess" pattern, so toward "methods disagree", or toward D or F if the swap also lands there.

The other reading of John's words, a reply-built text average used only to measure the average method's damage, has the opposite fault: it is not the vector the items get. Neither is clean. The design picked one without saying it was a choice (finding RT-487).

**Is the 1-nat check sensible?** Yes, as a floor. It catches the failure step 4b found (8.7 nats against 2.3). It is coarse: 1 nat is a factor of about 2.7 in perplexity. And it checks only that the model predicts the prose, not that damage there tracks what the removal does to the items. It is a sanity check and should be read as one. Defining "plain text" is a specification matter.

**Do the factor-of-two rule and damage matching stay meaningful?** Yes for the swap. For the average, only with the qualification in RT-487.

**What I expect to change from step 4b's figures** (average 0.61, swap 1.13, a factor of 1.85, all measured in the user's turn):
- **The baseline perplexity** should fall from about 1,900 to the order of 10 to 30, if the reply rendering behaves like plain text. The findings say "about 2,600" for the baseline perplexity, but `collect-summary.json` records 1,869. That is a small error in the findings.
- **The swap's damage** should stay large. In the reply, the model's predictions depend on the earlier prose, and the swap gives the loop another passage's message, so I expect damage of the same order or larger.
- **The average's damage** should rise relative to the swap's, because of the role mismatch. So the factor of 1.85 is more likely to shrink than grow, and the factor-of-two rule is more likely to pass, partly for the reason in RT-487.
- **The normal-range check** is where I expect trouble. At step 4b, in-loop noise of the swap's own size did little. Matching the swap's damage needed a factor of 987, which is at the factor search's upper limit of 1,000 in `step4b_collect.py`, and even then fell 18% short. The swap raised perplexity by 945 while the bound was −14. The findings set all of this aside as unreadable, and the signs are unreadable, but the size gap is the same pattern that sank the split removal test, there at 9.4 times. In the reply rendering the main removal is likely to fail the normal-range check, and the in-loop comparison for the swap may not be matchable at all. Either would make every outcome "not testable" at stage one (lines 1110 to 1115) (finding RT-491).

### 4. The simplified operator kind and its bites rule

**The rule** (lines 896 to 906): if the simplified operator's one-pass cost on the pilot bites items has a point estimate below 0.15, the bites set holds unit items only.

- **Half B's unit pool.** `build-report.json` gives half B's unit pool as 44 problems over 29 facts, and half A's as 37 over 26. The design's "about 29" matches. The older sentence at lines 882 to 884 ("each half holds about 35 to 45 two-digit multiplications ... serve 100 unit bites items") is now stale on both counts.
- **Facts and resampling by fact.** With unit items only, 200 test-half bites items share 29 facts, about 7 items per fact. The intervals are resampled by fact, so the bites set's effective size is near 29, as the design says. My rough sketch drew 29 facts from the pilot's 22 unit facts, with each fact's items from that fact's pilot items. At the pilot's unit one-pass cost of 0.25, only about 47% of such 200-item sets had a one-pass interval whose lower end reached 0.15. So the unit-only branch is likely to fail the size simulation's 80% target for the one-pass condition, and so to return to John. The design routes that case to John correctly. It should say now that this is the likely result, so that John is not surprised by it (finding RT-490).
- **"80 in the pilot".** The rerun pilot will hold 40 operator and 40 unit bites items. If the rule fires at the rerun, the unit-only branch needs a pilot of 80 unit items: a new pilot bites set from half A's 26 unit facts, and another model run to measure it. The order of work does not say this. Building the rerun pilot with 80 unit bites items as well as the 40 operator items would let one rental read either branch (finding RT-490).
- **The threshold sits badly with the per-kind "does not bite" condition** (lines 943 to 950). Condition 1 asks that a kind's own loss have an upper end below a quarter of that kind's one-pass cost. An operator kind kept at a point estimate of, say, 0.16 then needs its loss interval's upper end below 0.04, which 100 items cannot deliver. So with the operator kept just above the threshold, F is out of reach. A result in which the pooled condition holds but this kind fails becomes "Depends on one kind (operator)": a label produced by that kind's small one-pass cost, not by anything the removal did. The size simulation should catch this, because its "does not bite" target includes all three conditions. But then the rule as written guarantees a return to John in a region it was meant to settle. The threshold is also a near coin flip on 40 pilot items: the operator's one-pass cost had a standard error of about 0.10 at step 4b. A better rule lets the committed simulation choose: keep the operator bites items if the simulation reaches its targets with them, use unit items only if it reaches them without, and otherwise return to John (finding RT-489).
- **"Does not bite" in each kind, and F, with one kind.** The design says the per-kind conditions then apply to the unit kind alone (line 901 to 902), which is coherent: condition 2 collapses into condition 1. But three other places still assume two kinds (finding RT-488):
  - **The "cells and bites check disagree" rename** (lines 1139 to 1150) reads the operator and unit pairs together, "the same two kinds ... as the held-out problems". With unit-only bites items, an A or C carried by operator pairs, with no bite on unit items, would be renamed for a contradiction that does not exist.
  - **The outcome sentences for D and F** (lines 1208 to 1209) say "the held-out operator and unit problems". Under the unit-only branch, F's mandated sentence would state something that was not measured.
  - **The pilot's size** (line 1072) still says 40 of each kind.

**Does the simplification threaten anything else?**
- **The split between halves.** No structural threat. The operator's split key is its shape and operands together (lines 787 to 789). But an additive shape gives few answer values: "a plus b plus c" with operands 2 to 15 gives 27 distinct answers, about 13 per half after the split by decade. Answers then crowd together, so a donor's answer will more often fall among a recipient's five candidates, which bars it as a donor. Expect fewer eligible donors and more donor-only pairs for the operator kind, as with lookup. The specification should check this at step 3 (finding RT-493).
- **The two-digit answers.** Line 702 to 704 correctly hands the range to the specification. Line 767 still says "the operator kind uses operands of 2 to 15 (above)", and the "(above)" now points at text that was removed. With operands 2 to 15, "a plus b plus 3" gives one-digit answers for 3% of operand pairs. The constant must be at least 6, or the operand floor raised (finding RT-493).
- **The operator's own pass gain in the cells.** Lines 1008 to 1013 and 1019 to 1041 quote the two-step operator's figures (a gain of 0.37 from one pass to three; survival rates by pairing). They no longer describe the kind. The step-4b data cannot forecast the single-step kind: the existing shapes' three-pass accuracy on the pilot pairs ranged from 0.44 to 0.76, with no sign that the simpler-looking shape ("a plus 2 times b", 0.44) was easier. The unit kind, which is one multiplication, was right on all 40 bites items at three passes and on 80% at one. That suggests a single arithmetic step can still gain from the passes, but it is the rerun that will tell. If the simplified operator gains nothing, the prompt-rule cell would hold two of three kinds with little pass gain (lookup has none). That weakens what the cells can show, though it does not bias them (finding RT-493).

### 5. Order of work, stale text, and what step 4b showed that version 0.13 did not answer

- **Order of work** (lines 1264 to 1342). This closure check comes first, then the specification and pilot rebuild, then a full step-4b rerun priced for John's go. That is coherent. Missing:
  - the pilot bites composition needed for the unit-only branch (RT-490);
  - an expectation about the normal-range check, for John when the rerun is priced (RT-491);
  - the independent check that the step-4b findings say they are owed. Version 0.13 rests on those findings. My recomputations confirm the interference figures, the confidence counts, the dose ratios and the bites one-pass costs. I did not check the collection code's hooks.
- **The bites one-pass condition "passed by 0.0003".** It passed by chance of the resampling seed. Recomputed with 20 resampling seeds, the pooled interval's lower end ran from 0.1471 to 0.1518, and reached 0.15 for only 9 of the 20 seeds. The step-4b pass is a seed coincidence, not a measured margin. The registered run fixes its seed, so its decision is reproducible, but a decision inside the resampling's own seed-to-seed spread should be reported as such. Version 0.13 is silent on it, and the simplified operator may lower the pooled cost further (finding RT-492).
- **The in-loop factor near 1,000** (finding RT-491). In the findings it is a description; in the design it should be a risk. The code's search ran over factors from 0.001 to 1,000. The best factor, 987, sits at the top of that range, with damage 18% short of the target. So "matched within 20%" at step 4b came from where the search stopped, not from a factor shown to fit. Section 4 says that if no shared factor brings the damage within 20%, the design returns to John (lines 413 to 415). The specification should fix the search range and say that a best factor at the range's edge is reported as "not matched", unless the damage is within 20% there.
- **Stale text** (finding RT-497), each line still true of version 0.12 but not of 0.13:
  - line 1074 to 1076: the pilot limits "counted from the pairs left after the confidence filter". This contradicts lines 805 to 807 for the interference checks, and read literally it makes the rule empty;
  - line 767: operands of 2 to 15;
  - lines 832 to 833: "about 6 to 11 pairs";
  - lines 882 to 884: unit facts "about 35 to 45" and "100 unit bites items";
  - lines 907 to 916 and 1008 to 1041: two-step operator figures given as reasons;
  - line 2122: "Section 5 says how the replacements act on the reply rendering". They are described in section 4, lines 401 to 405;
  - line 1079 to 1081: "the neutral passages carry no instruction". This needs a word about the fixed request now added in the reply rendering.

---

## Findings

**RT-485. The minimum pairing rule: a pairing with no scored pair can count as a surviving routine kind. Serious.**
Lines 803 to 807, 823 to 825 and 832 to 836.
- Version 0.13 counts the share of a fifth over items right without the other half. That base no longer coincides with the pairs that will be scored, and the design says nothing about an empty base.
- A pairing whose prompt-rule items are almost all unconfident can pass both checks and stay in the pairing table with zero or one scored pair. The rule "any rule kind with one routine kind or none returns to John" counts routine kinds in that table. So the return to John that the design relies on for the weak operator kind (lines 1038 to 1041: "Losing two pairings leaves it with one routine kind, which returns the design to John") can be bypassed by an empty pairing.
- The step-4b code struck such pairings (`struck = (not conf) or ...`), but the design text never said so, and the new base removes the implicit link.
- **Fix:** a pairing with fewer than a stated number of pairs that pass the confidence check (the step-4b code used one) is struck, and an empty counting base counts as struck. Mark the number as the author's choice.
- This is one sentence and can go into the specification. It must be in place before the rerun's analysis.

**RT-486. The fixed opening: the reply rendering's fixed request and middle template tokens have no defined replacement under the average. Serious.**
Lines 299 to 301, 314 to 316 and 393 to 405.
- The real template puts `<|end_message|><|message_model|><|content_text|>` between the request and the prose. Section 3's slot rule counts slots only from the start of the opening and the end of the closing.
- The request itself is neither prose nor, as written, a template slot. If it is treated as text, the average and its noise comparison change positions the swap never changes. If it is treated as part of a fixed opening, the average changes the prose only.
- The two readings give different average damages, which feed the factor-of-two rule (1.85 at step 4b) and the average's damage matching. The closing tokens and whether they are rendered are also undefined.
- **Fix:** say that everything before the first prose token (system block, user header, request, end of user message, model header) is one fixed opening of template slots, so that the average and the swap both change only the prose. State whether the closing tokens are rendered. Say what "plain text" is for the 1-nat check.
- This can be carried into the specification if the design says which reading it takes.

**RT-487. The role mismatch: the average is measured across roles on the neutral set, while the swap is measured within its role. Serious.**
Lines 399 to 405 and 1188 to 1194.
- On the reply rendering, the swap's donors are reply renderings, but the average's prose vector is built in the user's turn and applied at reply positions. So the average's measured damage includes a mismatch of role that it never meets on the items' user text.
- That can let the factor-of-two rule pass an average that is much milder than the swap on the items.
- It can also scale the average's comparisons to an inflated damage, which understates the average's excess in the cells. That pushes the average toward "no excess", and so toward "methods disagree", or D or F.
- This is the author's reading of John's ruling, not stated as such. The other reading, a reply-built average for measuring damage, has the opposite fault.
- **Fix:**
  - mark the reading as the author's;
  - also measure and report the damage of a reply-built text average beside it, at no extra rental cost beyond one more pass over the neutral set;
  - add a rule fixed now: if the two averages' damages differ by more than a factor of two, the design returns to John before registration.

**RT-488. The unit-only branch is not carried through sections 5 to 7. Serious.**
Lines 948 to 950, 1072, 1139 to 1150, 1208 and 1209.
- If the bites set becomes unit-only, F's mandated sentence still says "the extra passes helped the held-out operator and unit problems ... in each kind", which would then be false.
- D's sentence says the held-out problems "share two kinds" with the cell.
- The "cells and bites check disagree" rename still reads the operator and unit pairs together, so an A or C carried by operator pairs would be renamed for a contradiction that no longer exists.
- **Fix:** conditional wording in each place, naming the kinds actually in the bites set, with the disagreement rule restricted to the pairs of those kinds.
- This is design text, not specification, so it needs a small version 0.14 edit before registration. It does not hold back the rebuild.

**RT-489. The bites threshold: keeping the operator bites items at any point estimate of 0.15 or more can make F unreachable. Worth noting.**
Lines 896 to 902 and 943 to 950.
- Condition 1 of "does not bite", applied per kind, needs a kind's loss interval's upper end below a quarter of that kind's own one-pass cost. An operator kept at 0.16 needs an upper end below 0.04, which 100 items cannot give.
- So F becomes unreachable, and a pooled pass with an operator failure reads as "Depends on one kind (operator)" for a reason unrelated to the removal.
- The threshold is also a near coin flip on 40 pilot items (standard error about 0.10). The size simulation would catch the result and return to John, so no outcome is wrong, but the rule does not settle what it was written to settle.
- **Suggested fix:** let the committed simulation choose between both kinds and unit-only, with a return to John if neither reaches the targets. Mark the rule as the author's.

**RT-490. The unit-only branch: it is likely underpowered, and the rerun pilot cannot read it. Worth noting.**
Lines 896 to 906 and 1070 to 1074; `build-report.json` (half B: 44 unit problems, 29 facts; half A: 37, 26).
- With unit items only, 200 test-half bites items rest on 29 facts. My rough resampling at the pilot's unit cost of 0.25 gave the one-pass condition's lower end at or above 0.15 in only about 47% of simulated sets, below the 80% target. So this branch probably returns to John.
- "80 in the pilot" needs a new pilot bites set from half A's 26 unit facts, and another model run, which the order of work does not mention.
- **Suggested fix:**
  - build the rerun pilot with 80 unit bites items as well as 40 operator ones, so that either branch is read from one rental;
  - say now that the unit-only branch is expected to need John.

**RT-491. The normal-range and in-loop comparison risk: step 4b's random-noise results point to a failure that version 0.13 does not anticipate. Serious, but it does not hold back the rebuild.**
Lines 411 to 428 and 1110 to 1115; `collect-summary.json` (`factors.loop_swap.factor` 986.6, damage 0.93 against 1.13; normal-range bound −14.3 against the swap's +944.7); `step4b_collect.py` (factor search from 0.001 to 1,000).
- In-loop noise of the swap's own size did little damage at step 4b. Matching the swap took a factor of 987, at the very top of the code's search range, and still fell 18% short. Its "within 20%" is where the search stopped, not a factor shown to fit.
- The findings set the normal-range figures aside as unreadable, which is right for their signs. But the gap in size between the swap and same-size noise is the failure pattern of the split removal test (9.4 times there), and here it is far larger.
- In the reply rendering, the main removal is likely to fail the normal-range check, and the in-loop swap comparison may not be matchable at all. Either makes every outcome "not testable" at stage one.
- **Fix:**
  - say this expectation in the design;
  - tell John when the rerun is priced;
  - have the specification fix the factor search range and report a best factor at the edge of the range as unmatched unless its damage is within 20% there;
  - if this design wants a different normal-range bound or comparison, that is a ruling for John, to ask now rather than after another rental.
- The rebuild costs nothing and the rerun is what measures this in the reply rendering, so it need not hold back the rebuild. It should be stated before the rerun is priced.

**RT-492. The bites one-pass pass: step 4b's pass was a resampling-seed coincidence. Worth noting.**
Step-4b findings, "The bites check's one-pass condition: passes, just"; `step4b-analysis.json`.
- With 20 resampling seeds, the pooled interval's lower end ran from 0.1471 to 0.1518 and reached 0.15 for 9 of 20 seeds. The step-4b "pass by 0.0003" is inside the seed-to-seed spread of the resampling itself.
- Version 0.13 does not mention the near miss. The simplified operator may lower the pooled cost further.
- **Suggested fix:** report the resampling's seed-to-seed spread beside any gate decision closer than about 0.005, or use more resamples. Note that this gate is likelier to fail at the rerun than step 4b suggests.

**RT-493. The single-step operator's side effects, for the specification. Worth noting.**
Lines 534 to 538, 702 to 704, 767 and 787 to 789; lines 1008 to 1041.
- **One-digit answers.** With operands 2 to 15, "a plus b plus c" gives one-digit answers unless c is at least 6 (3% of operand pairs at c = 3). Line 767's "2 to 15 (above)" is stale.
- **Crowded answers.** An additive shape gives about 27 distinct answers, about 13 per half. Donors' answers will more often fall among recipients' candidates, so expect fewer eligible operator donors.
- **"A plus b" as a candidate.** The practised sum "a plus b" lies within five of the right answer and will often be a candidate. That keeps the "rule is needed" check honest but may lower confidence.
- **A narrowed ruling.** "With a written constant" narrows John's example into a requirement; mark it as the author's.
- **Stale figures.** The operator's two-step pass-gain and survival figures still stand as reasons and should be marked as superseded.
- The specification can carry all of this.

**RT-494. Additions are not marked as the author's. Worth noting.**
Lines 1 to 17, 800, 805 to 807, 394, 401 to 409, 534 and 896 to 906.
- The tie rule, the new counting base, the fixed request, the reading of how the average acts on the reply rendering, the 1-nat check with its return to John, "with a written constant", and the 0.15 point-estimate threshold are all the author's. The design presents them inside John's rulings.
- The house rule on decision authorship asks for them to be marked as the author's, not John's. That matters most for RT-487, where the reading is a real choice.

**RT-495. The accuracy rule does not count items pushed off the confidence bar. Worth noting.**
Lines 796 to 826.
- An item right with and without the other half, but pushed below the confidence bar by it, is dropped without counting toward a strike.
- On the pilot, 3 prompt-rule items in unit with opposites fell from confident to below 2.2 because of the routine fact. Counting them would give 4 of 13 and strike the pairing; the accuracy rule gives 1 of 13 and keeps it. In operator with colours, 4 routine twins did the same.
- This is within John's ruling. The survivors are selected for robustness on one side of the pair only.
- **Suggested fix:** the strike-count report should show, per pairing, the items that fell below the bar while staying right, so that John and the reader can see it.

**RT-496. The 1-nat check is a floor, not a validation. Worth noting.**
Lines 406 to 409.
- It shows that the model predicts the prose in the reply rendering. It does not show that damage measured there tracks what a removal does to items in the user's turn.
- 1 nat is a factor of about 2.7 in perplexity.
- **Suggested fix:** report the user-turn loss beside the reply and plain-text losses, and keep the check's wording modest.

**RT-497. Stale text. Worth noting, except the first item, which must be corrected in the specification.**
- **Lines 1074 to 1076:** "counted from the pairs left after the confidence filter" for "the 'answered as well behind its rule' check". This contradicts lines 805 to 807, and read literally it makes the interference rule empty.
- **Line 767:** "operands of 2 to 15 (above)".
- **Lines 832 to 833:** "about 6 to 11 pairs".
- **Lines 882 to 884:** "about 35 to 45" unit facts and "100 unit bites items".
- **Lines 907 to 916 and 1008 to 1041:** two-step operator figures given as reasons.
- **Line 2122:** "Section 5 says how the replacements act". They are in section 4, lines 401 to 405.
- **Lines 1079 to 1081:** "carry no instruction", which now needs a word on the fixed request.
- **Step-4b findings** (not the design): "baseline perplexity was about 2,600", where `collect-summary.json` records 1,869.

---

## Verdict

**Version 0.13 is ready for the specification and pilot to be rebuilt. Nothing found here should hold back that rebuild.** All three rulings are written in faithfully. The interference rule's counting base is right, and the author's pilot figures recompute exactly. The reply rendering is buildable once one point is defined. The dose result stands.

**Carried into the specification** (it must say each of these explicitly):
- **The minimum pairing rule (RT-485):** a pairing with fewer than a stated number of confident pairs, or an empty counting base, is struck.
- **The fixed opening (RT-486):** everything before the first prose token in the reply rendering is a fixed opening of template slots, so both methods change only the prose. State whether the closing tokens are rendered, and what "plain text" means for the 1-nat check.
- **The rerun pilot's bites set (RT-490):** 80 unit bites items as well as 40 operator ones, so that either branch of the bites rule can be read from one rental.
- **The factor search (RT-491):** fix its range in the specification, and report a best factor at the edge of the range as unmatched unless its damage is within 20% there.
- **The single-step operator (RT-493):** operand range and constants giving two-digit answers, and a step-3 report of operator donor counts.
- **The stale counting base (RT-497):** follow lines 805 to 807 for the interference checks, not lines 1074 to 1076.

**Owed as a small version 0.14 before the rerun is priced, but not before the rebuild:**
- **The unit-only branch (RT-488):** carry it through the disagreement rename and the D and F sentences.
- **The role mismatch (RT-487):** mark the reading of how the average acts on the reply rendering as the author's; report a reply-built average's damage beside it, with a return to John if the two differ by more than a factor of two.
- **The normal-range and in-loop comparison risk (RT-491):** state the expectation, so that John hears it when the rerun is priced. If he wants a different normal-range bound or comparison, ask him now.
- **The bites threshold (RT-489):** replace the 0.15 point-estimate rule with a choice made by the committed simulation, or at least mark it as the author's.
- **Authorship (RT-494):** mark the author's additions.
- **Stale text (RT-497):** correct the lines listed.

These are edits of a few sentences each. A closure check of version 0.14 can be narrow: it needs to check only these points.

---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-23. It closes nothing.*

- **The bites condition hangs on the resampling seed (RT-492).** Confirmed. Rerunning the analysis's resampling with seeds 1 to 20 on the step-4b data, the pooled one-pass condition's lower end reaches 0.15 for 9 of 20 seeds. The step-4b findings reported "passes, just", on seed 1. That should have been reported as no pass at all: the condition is a coin flip on the pilot.
- **The stale counting base (RT-497).** Confirmed. The pilot's-size paragraph still says the fifth "is counted from the pairs left after the confidence filter". That contradicts the new counting base and would make the accuracy rule empty. The author missed it.
- **Not rechecked by the filer:** the pairing-table gap of RT-485, the reply-rendering readings of RT-486 and RT-487, the unit-only power sketch of RT-490, and the figures of RT-495.
- **Where things stand.** The reviewer finds version 0.13 **ready for the specification and pilot to be rebuilt**. The serious findings RT-485 to RT-488 and RT-491 are to be settled, some in the specification and some in a short version 0.14 owed before the step-4b rerun is priced. The reviewer says none should hold back the rebuild. The dose question (RT-345) stays formally open until the rerun reads it after the filters.
