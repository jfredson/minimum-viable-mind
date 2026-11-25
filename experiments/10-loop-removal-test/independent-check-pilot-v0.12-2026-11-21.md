*Filed 2026-11-21 by the session that wrote the specification's section 17, the generator changes and the pilot, verbatim as the checker returned it. The checker was a fresh Claude Code session with no history of this conversation, which wrote none of the code, the specification or the design. It worked read-only in a detached worktree at commit 66740a8, using only its own scratch folder, which was created empty for it. It changed nothing in the repository (`git status` clean, checked by the filer), downloaded nothing, spent nothing and sent nothing to the model. Nothing in its text was changed in filing. The filer's check follows, below a rule, and is not part of it.*

---

# Independent check: the loop removal test's pilot rebuilt for design version 0.12

*Checked 2026-11-21 by a fresh Claude Code session that wrote none of the design, the specification, the generator, the content lists or the pilot. I worked read-only in the detached worktree `/Users/john/Code/minimum-viable-mind/.claude/worktrees/pilot-check-v012-2026-11-21`, at commit 66740a8 (the commit titled "the pilot rebuilt for design version 0.12"). Every script, rebuilt file and result is in my own scratch folder, `/private/tmp/claude-501/pilot-check12-hy5oco`. I changed nothing in the worktree (its `git status` is clean at the end), and I downloaded nothing, installed nothing, spent nothing, pushed nothing and made no network call. Nothing went to the model.*

## What I opened

- `experiments/10-loop-removal-test/battery-authoring-spec.md`, the whole file. I read section 17 closely, and sections 2 to 8, 11, 12 and 14 that it relies on.
- The code, line by line: `src/build.py` (the generator), `src/split.py` (the split between halves), `src/check_overlap.py` (the overlap check) and `src/step3_checks.py` (the free step-3 checks).
- The pilot folder `batteries/pilot-v0.12/`: `build-report.json`, `overlap-check.json` and `step3-results.json` in full, and every line of the five item files through my own scripts.
- The design, `docs/loop-removal-test-design-2026-11-20.md` (version 0.12): its header, the passages of section 5 on the instruction, the numbers and the split, the bites check, the pilot's size and the neutral passages; the average method in section 3; the donor rules; the outcome section's resampling scheme; choices 1 to 8 in section 10; and the rulings in section 11.
- The earlier check, `independent-check-2026-11-21.md`, for its format and for the findings that carry over: the place of the right number (RT-416), the incomplete overlap check (RT-417), the neutral set's lengths (RT-425) and what the step-3 checks measure (RT-427). I glanced at the list of its fixes in `independent-check-fixes-2026-11-21.md`.
- The first 30 lines of the model's `chat_template.jinja`, to see how the reasoning setting "none" is rendered.

I did not open the rulings file for choices 6 to 8, the closure checks of the design, or the step-4a and trial findings.

## What I ran

All with `/Users/john/Code/minimum-viable-mind/.venv/bin/python -I -B`, so that no cache file was written into the worktree.

1. **The rebuild.** `build.py --half A --seed 1 --tokdir <the research model's tokeniser folder> --instruction start --out <scratch>/rebuild`. Then `check_overlap.py --pilot <scratch>/rebuild` (its printed output saved as `overlap-check.json`) and `step3_checks.py --pilot <scratch>/rebuild --tokdir <tokeniser folder>`.
2. **`verify_items.py`**, my own check of every item file. It does not import the generator. It renders every prompt through the chat template itself and re-tokenises it, recomputes every right answer from the item's content, and checks the instruction, the candidates, the cross-cell and copying rules, the donors, the bites rules and the content of the other half.
3. **`split_check.py`**, my own recomputation of the split from the specification's text: the pools, the decade dealing, the seed search up to 1,000 and every tolerance figure. It also checks the committed values against the dealing rule's structure in a way that does not depend on the random stream.
4. **`sim_places.py`**, which runs the committed generator's pair and bites steps for seeds 1 to 200 (half A only), to see whether the right number's place is uniform and how the drawn answers compare with the pool.
5. **`analytic_draw.py`**, which computes exactly, from the pools alone and without generating any item, what share of each pool item the generator's draw gives in each half. No half-B item was generated.
6. **`faults.py`**, which plants nine deliberate faults in copies of the rebuilt pilot and runs both committed checks on each copy.

## Results by item

### 1. The rebuild, byte for byte

**Reproduced exactly.** All six generated files (`pairs.jsonl`, `donor_only.jsonl`, `bites.jsonl`, `bites_donor_only.jsonl`, `neutral.jsonl` and `build-report.json`) are byte-identical to the committed ones. The overlap check passes (exit 0), and its output is byte-identical to the committed `overlap-check.json`. The step-3 script writes a `step3-results.json` that is byte-identical to the committed one. So the committed pilot is exactly what the committed code makes with the command the build report implies.

### 2. The split (section 17, item 4)

- **The pools match the text.** I enumerated them myself. The operator pool has 611 items (four shapes, operands 2 to 15, two-digit answers), with answers from 10 to 45, which bears out the correction to 45 (RT-468, the operator's range). The unit pool has 81 items making 55 facts, as item 6 says. The sums pool has 1,164 items with answers 10 to 98. The products pool has 55 items.
- **The dealing follows the rule.** For every kind and every decade, the value ending in 0 and the value ending in 5 go to different halves. The half that gets the round number alternates from one decade to the next, and a decade with only one round value gives it to the half due the 0. In each decade the even endings and the odd endings split between the halves at most one apart. I checked this on the committed values directly, which does not depend on the random stream.
- **The seeds recompute.** My own code, written from the text, finds the same first passing seed for every kind: operator 1, unit 3, sums 1 and products 3. It gives the same half-A and half-B values and every pool figure in the build report, to four decimals. Unit and products share one value split, because they have the same 42 answer values and the same seed. That is consistent, not a fault.
- **The halves do not overlap.** In every kind the two halves' values are disjoint and together cover every value. The overlap check confirms that every numeric right answer in all four item files lies in half A's values.
- **The margins.** The products split passes the mean-answer tolerance by 0.008 (a gap of 1.992 against a limit of 2). Only 50 of the first 1,000 seeds pass for products, and 63 for unit, against 950 for the operator and 997 for sums. See the thin products margin (RT-482).
- **Is the draw uniform over the half's pool? No, not exactly.** The generator draws the right number's place first and then redraws items until one fits that place. An answer at the edge of the range, such as 10, can fill only the lowest place, so it is drawn about a fifth as often as the pool says. Over 200 seeds the operator answer 10 came up at 0.21 of its pool rate, and the unit answer 10 at 0.20. In half B the edges are different values (11 for the operator, 99 for unit, and 12, 96 and 99 for products). So the two halves are thinned in different places. My exact calculation shows the expected gap between the halves, as drawn, exceeds the tolerances in three kinds. This is the most important finding below (RT-473, the drawn items do not follow the pools).

### 3. The allocation and kinds (items 1 and 2)

- **Pair counts** match the table exactly. Operator: 13 capitals, 13 opposites and 14 everyday colours. Unit: 14, 13 and 13. Lookup: 20 sums and 20 products. That is 40 per rule kind.
- **The 25% cap holds.** The routine cell holds 27 capitals, 26 opposites, 27 everyday colours, 20 sums and 20 products, all at or below 30 of 120.
- **No letter-code item is built.** Only the operator, unit and lookup kinds appear, in all four item files.
- **The instruction** "Answer with the single word or number only." opens every text of every scored pair, donor-only pair, bites item and donor-only bites item. That covers both twins, the version without the rule and both baseline variants. It appears exactly once in each, and the rule follows it directly. None of the 200 neutral passages carries it.
- **The order of the facts** is balanced within every group: seven and six (or six and seven) in each odd group, and ten and ten in the lookup groups.

### 4. The bites items (item 5)

- **Counts by group** match the table: operator 13, 13 and 14, and unit 13, 14 and 13 (capitals, opposites, everyday colours). That is 80 in all, plus 67 donor-only bites items.
- **Built as the prompt-rule side.** Every bites text is exactly the instruction, the shared context and the prompt-rule question, in the same form as the pairs' prompt-rule items. No bites file carries a routine side. The generator does build the routine twin while making each bites item and then drops it. The design says the twin is not built (see RT-477, the unbuilt twin is built).
- **The no-repeat rule.** No bites item, and no donor-only bites item, repeats a scored pair's or a donor's rule content and routine content together. No two bites items share a rule content. But the operator's "rule content" includes the symbol, so the same sum (for example "3 times a, minus b" with a = 6 and b = 4) can return under a different symbol. Three operator problems repeat within the bites items, and four bites items repeat a scored pair's problem (RT-475, operator problems repeat under a new symbol). In the unit kind, 40 bites items use 22 distinct problems and 18 facts, which the design expects and handles by resampling by fact.
- **Donors.** Recomputed independently: every bites item has at least 5 eligible donors (from 5 to 24, median 12). From the bites items alone, 51 of the 80 would have fewer than five. So the donor-only additions do the work, and every one of the 67 serves at least one item. No group exceeds three times its scored count, and no group used more than its budget of 200 draws per item. Twenty-seven eligible donor links share the recipient's routine content (RT-478, bites donors may repeat the routine fact).
- **Every candidate is one token.** All 735 bites and donor-only bites candidates are single tokens under the real tokeniser, and so are all candidates of the pairs and donor-only pairs.

### 5. The pairs (sections 6 to 8 and 14)

- **Twin lengths are equal** in all 120 scored pairs and all 141 donor-only pairs. The twins share the instruction and the whole context, and they differ only in the final question. My own rendering and tokenisation reproduce every stored list of token ids, for every item and every neutral passage.
- **Right answers recompute** from the content in every item: operator shapes, unit products, sums and products.
- **Candidates.** Five distinct candidates in every item, with the right answer among them. Every numeric right answer has two digits. Every wrong number has two digits and lies within 5 of the right one (within 12 for products), and every product candidate is a real product of two numbers from 2 to 12.
- **The cross-cell rules and the copying rule** hold in every scored and donor-only pair: neither twin's right answer is among the other twin's candidates, and no non-numeric candidate contains, or is contained in, a content word of the routine fact or either final question. The copying rule also holds for the bites items.
- **The place of the right number, drawn first.** By kind in the scored pairs, the counts at places 1 to 5 (lowest to highest) are: operator 12, 6, 3, 12, 7; unit 6, 10, 7, 8, 9; sums 8, 3, 5, 3, 1; products 3, 4, 6, 4, 3. In the bites items they are: operator 6, 10, 10, 9, 5; unit 9, 11, 9, 9, 2. The operator pairs (a chi-square test gives p = 0.10), the sums (p = 0.14) and the unit bites items (only 2 of 40 at the top place, p = 0.20) look lopsided. But over 200 seeds the generator's places are uniform for every kind (p from 0.13 to 0.84). So these are chance in this one draw, not a fault in the code. Two items have the answer 10, and in both it is the lowest candidate, by construction (part of RT-473). The step-3 script reports places for the pairs only, not for the bites items (RT-479, gaps in the step-3 report).
- **Copying lures.** A wrong number equals a number in the item's own text in 4 scored prompt-rule items and 1 bites item, down from 11 in the first pilot (this is RT-429, wrong numbers copying the item's own numbers, which the specification allows).
- **Donors for the pairs.** Recomputed independently: every scored pair has at least one eligible donor, and one, A-0005 in the operator-and-capitals group, has only four. That group stopped on its draw budget, and the build report says so. Every donor-only pair serves at least one scored pair, and no group exceeds its cap.
- **The stand-in dose ratio** of the routine twin's dose to the prompt-rule item's (check 6 of section 12) lies between 0.9946 and 0.9999 at weights 0, 0.3 and 0.6, for all three kinds. That is within the bands, as it must be by construction, since the twins share every token before the final question.
- **No half-B content** appears in the pilot: no half-B country, capital, object or opposite word in any item's routine content or candidates, and no half-B syllable in any invented word.

### 6. The checks themselves

**What they test against section 17, item 10.** The overlap check does the three things item 10 lists. It fails on a numeric right answer outside its half's values, on operator content outside the half's pool (which, since the pools are split by value, is the same test as the first), and on a capital, three-letter word or opposite candidate from the other half. It also keeps the list-level checks. The step-3 script reports what section 12 and item 10 ask for, with the gaps listed under RT-479 (gaps in the step-3 report).

**Planted faults.** I planted nine faults, each in its own copy of the rebuilt pilot.

| Planted fault | Overlap check | Step-3 script |
|---|---|---|
| A sum's right answer set to 11, a half-B value | **fails, correctly** | exits 0, reports nothing |
| A half-B capital put among a pair's candidates | **fails, correctly** | exits 0, reports nothing |
| A unit item's stated answer changed to a wrong candidate (31, which happens to be outside half A's values) | **fails**, but only because 31 is a half-B value | exits 0, reports nothing |
| One scored pair with the instruction removed from both twins | passes | passes |
| The instruction added to a neutral passage | passes | passes |
| Two bites items given the same rule content | passes | passes, "repeats" still 0 |
| The instruction removed from every bites item, and the instruction's name removed from the build report | passes | passes, and still reports "instruction_at_start": true |
| One twin made a token longer | passes | exits 0; the twin count drops from 120 to 119 |
| A pair relabelled as the letter-code kind | passes | passes |

So **yes, both checks can pass while something is wrong.** The step-3 script never fails at all: it exits 0 whatever it finds, and a person must read its counts. Its instruction test looks only at the bites items. It compares their start with the instruction text named in the build report, and if the report names none, the test compares with an empty string and passes on anything. Neither check recomputes a right answer, so a wrong answer that is still a half-A value would pass both. On this pilot my own checks found none of these faults, so nothing is hidden now (RT-474, the checks can pass a faulty set).

### 7. Section 17's other items (6 to 9)

- **Item 6, what a fact is.** The counts hold: 81 unit items make 55 facts, 26 in half A's pool and 29 in half B's. The pilot's 80 unit items (pairs and bites together) use 25 facts, one of them 6 times. Step 3 reports the count and the largest use, not how often each fact is used, as item 6 asks (RT-479).
- **Item 7, the change ratio.** It agrees with the design's definition in section 5 (the bites check, condition 3). The arithmetic of "what 0.5 means" is right: if both sums are scaled to the same length, a distance of half that length means a cosine of 1 − 0.5²/2 = 0.875. The specification's reading of the average method's positions (the whole text span) follows the design's text-span definition in section 3. No code touches this yet.
- **Item 8, the three readings.** Each one departs from the design's text in a stated way, and each is marked for the registration review to adopt or reject. That is the honest way to carry them. One note on the last part: "up to 300 per kind" means little for the unit kind, because half B holds only 44 unit items and 29 facts, and the design resamples the unit kind by fact. So the unit kind's effective sample is bounded near 29, however many bites items are drawn. The design says the simulation models this, and it should be visible in its report.
- **Item 9, errors in the design's text.** The operator's range (10 to 45) checks out against the pool. I did not check the pair-count arithmetic ("about 216 to 236"), which needs the tenth change log.
- **Item 2's two side remarks.** The stated reason for the lookup kind taking only sums and products does not follow (RT-481, the lookup allocation's reason), and "the same shares" in the test half cannot hold above about 160 pairs (RT-480, the test half's shares hit the pools).

## Findings

**RT-473 (serious, MEASURED): the drawn items do not follow the pools the tolerances were checked on, and the expected gap between the halves, as drawn, breaks three tolerances.**

- **Where.** The specification, section 17, item 4, "How items are drawn" (`battery-authoring-spec.md`, lines 484 to 488), together with section 14, item 2 (lines 310 to 314). The code is `build.py`, `near_numbers` (lines 149 to 162), `rule_op` (lines 205 to 218), `rule_unit` (lines 220 to 234), `rt_sum` (lines 297 to 308) and `rt_prod` (lines 310 to 322). The tolerances are applied in `split.py`, `figures` and `check` (lines 75 to 93) and `choose` (lines 104 to 116), to the pools only.
- **What happens.** The specification says both "each item is drawn uniformly from its half's pool, so that the drawn items follow the pool the tolerances were checked on" and "the right answer's place is drawn first", with an item that cannot fill its place redrawn. These two rules conflict at the edges of the range. An answer of 10 has no two-digit number below it, so it can only take the lowest place, and the generator then draws it a fifth as often as the pool. The same happens at the top of the range and, for products, wherever the nearby products are sparse.
- **Measured.** Over 200 seeds of half A, the operator answer 10 came up at 0.21 of its pool rate, and the unit answer 10 at 0.20. An exact calculation from the pools (`analytic_draw.py`, no items generated) agrees with that simulation to within 0.001 on the operator and unit shares.
- **Why it matters.** The two halves lose different values. Half A loses its 10s, which are round numbers. Half B loses 11 (operator), 99 (unit), and 12, 96 and 99 (products). So the halves drift apart in the very figures the tolerances guard. Expected gap between the halves, on the pool and as drawn:

  | Kind | Figure | Tolerance | Gap on the pools | Gap as drawn |
  |---|---|---|---|---|
  | products | share of answers ending in 0 | 0.05 | 0.011 | **0.075** |
  | unit | mean answer | 2 | 1.12 | **2.81** |
  | operator | share of answers ending in 5 | 0.05 | 0.047 | **0.054** |
  | operator | share of answers ending in 0 | 0.05 | 0.015 | 0.037 |
  | unit | share of answers ending in 0 | 0.05 | 0.012 | 0.037 |

  The design brought in item-by-item matching (RT-460, matching the halves on items) so that the pilot would forecast the test half. As built, the specification's own drawing rule undoes part of that in expectation. The step-3 report cannot show it, because it gives the pilot's drawn figures beside the pools but has nothing to set them against for half B.
- **A caveat.** The calculation ignores the rule that no routine question is used twice, which matters for products (20 of half A's 26 are used). It is the expected gap, not a forecast of one particular test set.
- **Fix.** Either of these is free and model-free:
  - Compute the tolerances on the as-drawn weights instead of the raw pools. The calculation is exact and short (my `analytic_draw.py` does it), and the seed rule then picks a split that is matched as drawn.
  - Or draw the item first, uniformly from the pool, then draw its place uniformly among the places it can fill, and report the place counts. The places then lose a little uniformity, but only for the few edge values.

  Either fix changes the pilot's items, or at least the seeds, so it is cheapest to make before step 4b runs on the pilot.

**RT-474 (worth noting now, to fix before the test set, MEASURED by planted faults): the overlap check and the step-3 script can both pass a faulty set.**

- **Where.** `step3_checks.py` returns no failure at all (`main`, lines 38 to 234, ends without a non-zero exit). Its instruction test is at line 201: `x["P"]["text"].startswith(rep.get("instruction_text", ""))`. It covers the bites items only, and it passes vacuously when the build report names no instruction. `check_overlap.py` (lines 76 to 93) checks answers by value and candidates by list, but not the content.
- **What the planted faults showed.** These all passed: a scored pair without the instruction; a neutral passage with it; two bites items sharing a rule content; a letter-code pair; and a whole bites file without the instruction, together with a build report that names none. A twin one token longer only lowered a count from 120 to 119, with exit 0. Neither check recomputes a right answer from the item's content, so a wrong stated answer that is still a half-A value would pass both. My planted wrong unit answer was caught only because it happened to be a half-B value.
- **Why worth noting, not serious.** My own independent checks found none of these faults in the committed pilot, so nothing is hidden today.
- **Fix.** Make step 3 exit non-zero on any failed condition, and add to its conditions:
  - the instruction in every scored, donor and bites text, and in no neutral passage;
  - right answers recomputed from the content;
  - only the three rule kinds;
  - no shared rule content among the bites items.

  This matters most for the test set, which will be checked by these scripts.

**RT-475 (worth noting, MEASURED): an operator problem can repeat under a different symbol, and still count as new content.**

- **Where.** `build.py`, line 216: the operator's content key includes the symbol. The no-reuse tests at lines 415 and 492 use that key.
- **What happens.** In the scored pairs, three operator problems appear twice each, for example "3 times a, minus b" with a = 6 and b = 4. In the bites items, three problems appear twice. Four bites items repeat a scored pair's problem, which the design allows ("numbers and answers may repeat").
- **Why it matters.** The design resamples operator items one at a time (section 6, the resampling scheme), which treats them as independent. Two items that differ only in the symbol are not quite independent. Half A's operator pool holds 312 items, so there is no shortage to excuse it.
- **Fix.** Key the operator's no-reuse rule, among the scored pairs and among the bites items, on the shape and operands, not on the symbol.

**RT-476 (worth noting, MEASURED by reading the code): the bites items are not drawn from their own random stream.** The design says the bites items are drawn "from their own random stream" (section 5, the bites check, line 830 of the design). `build_bites` (`build.py`, lines 482 to 499) uses the same stream as the pairs and their donors, after them. So any change to the pairs or donors changes every bites item. This does not affect the pilot's validity, but it departs from the design, and the specification's item 5 does not mention it. Fix: seed a separate stream for the bites items, or record the departure.

**RT-477 (worth noting, MEASURED by reading the code): the bites items' unused routine twin is still built and filtered on.** The design says the routine twin "is not built". `build_bites` calls `b.pair` (`build.py`, line 491), which builds both twins. So a bites item can be rejected because its discarded twin has a different length, or because a candidate clashes with the discarded routine question. The effect is a small, harmless filter on the bites items. Fix: state it in the specification, or build the prompt-rule side alone.

**RT-478 (worth noting, MEASURED): a bites item's donor may repeat its routine fact.** For the pairs, a donor that repeats the recipient's rule content or routine fact is barred (RT-412, donors copying their own recipient; `build.py`, line 433). For the bites items, the specification bars only a shared rule content (lines 501 to 503), and `bites_eligible` (`build.py`, lines 537 to 542) follows it. In the pilot, 27 eligible donor links share the recipient's routine fact, for example the same country. The routine fact does not bear on a bites item's answer, so this is probably harmless. But it can make a swap a little milder than the pairs' swaps, at a few positions. Fix: apply RT-412 in full to the bites donors, or say why not.

**RT-479 (worth noting, MEASURED by reading the code): gaps in what step 3 reports against the specification.** These are all in `step3_checks.py` unless a line says otherwise.
- The right number's place is reported for the scored pairs only (lines 184 to 191), though the bites items are numeric too and section 14, item 2 asks for the counts "by kind".
- The facts are reported as a count and a maximum use (lines 224 to 230), not "how often each is used" (item 6).
- The bites items' donor report (`build.py`, lines 524 to 527) lacks the reason drawing stopped, and the length-place of any item left without donors, which section 8's terms ask for. None lacks donors in this pilot.

**RT-480 (worth noting, for the test set, ARGUED from the design's pool counts): "the same shares" in the test half fail above about 160 pairs.** Item 2 (spec, lines 443 to 444) says the test half uses the pilot's shares. At those shares capitals are 27 of 120 and products 20 of 120. Half B has 36 capitals usable as right answers (design, section 5) and 29 products, and no routine question may be used twice. So the shares hold only up to about 160 pairs for capitals and about 174 for products, while the simulation is expected to ask for 120 to 200. The edge products of half B (12, 96 and 99) are also the ones RT-473 (the drawn items do not follow the pools) thins out. Fix: state the rule for sizes above 160 pairs now, before the simulation sets the size.

**RT-481 (worth noting, ARGUED): the stated reason for the lookup allocation does not follow.** Item 2 (lines 441 to 443) says the lookup kind takes only sums and products "because operator and unit can take nothing else". That explains why sums and products must come from the lookup kind. It does not explain why the lookup kind takes no capitals or opposites. Within the cap it could take up to 3 capitals and 4 opposites, which section 5's "as evenly as possible" would favour. The table is explicit, and section 17 governs, so the build is right by the text. Only the reason should be restated, or the choice made explicitly.

**RT-482 (worth noting, MEASURED): the products split is accepted by a hair.** The products seed (3) gives a gap in mean answer of 1.992, against a tolerance of 2. Only 50 of the first 1,000 seeds pass for products, and 63 for unit. Nothing is wrong with this. But any change to the pools or to the figures, including the fix for RT-473 (the drawn items do not follow the pools), will move these seeds, and the pilot with them.

**RT-483 (worth noting, MEASURED; carries RT-425, the neutral set's lengths): the neutral passages stop short of the longest items.** The longest neutral passage is 105 tokens. Sixteen scored pairs (up to 107 tokens) and 40 donor-only pairs (up to 109) are longer. `build_neutral` (`build.py`, lines 633 to 652) stops before the target length, and takes its range from the scored pairs only. The pooled average of section 3 is defined at every position anyway. But the design asks for passages "up to the longest item" (section 5, the neutral set), and the measuring half is used to match damage.

**RT-484 (worth noting, for the test set, MEASURED by reading the code; carries RT-417, the incomplete overlap check): the overlap check does not look at the objects or invented words used in an item's text.** The design (section 5) says that for the lookup and everyday-colours kinds the check applies to "the invented words and tables" and "the objects". `check_overlap.py` checks those only at the level of the lists. An everyday-colours item that named a half-B object would pass, because its candidates are colours, which are exempt. It also does not compare pilot and test prompts or tables, which the design asks for. My own check found no half-B object, syllable, country or opposite word in the pilot.

## Verdict

The rebuilt pilot is exactly what the committed code makes. The code does what section 17 says in almost every particular:
- the counts, kinds and cap;
- the instruction at the start of every item, and in no neutral passage;
- the bites items and their donors;
- equal twin lengths, the cross-cell and copying rules, single-token candidates and right answers;
- the split's pools, dealing, seeds and tolerances, all of which I reproduced independently.

**One thing should be fixed before step 4b: the drawn items do not follow the pools (RT-473).** The specification's drawing rules contradict each other at the edges of the range, and the code follows the place-first rule. As drawn, the expected gap between the halves then breaks three of the tolerances that RT-460 (matching the halves on items) set up so that the pilot would forecast the test half. Either fix is free:
- check the tolerances on the as-drawn weights and re-choose the seeds; or
- draw the item first and its place second.

Either one changes the pilot, so it is cheaper to make now, then rebuild and rerun the two checks, than after a rented run. If the author would rather run step 4b on this pilot as it stands, the gap should be stated beside every figure step 4b passes on to the test half's simulation.

**While the generator is open,** it would be cheap to also fix the following:
- make the step-3 script fail on a failed condition, and close the vacuous instruction test (RT-474, the checks can pass a faulty set);
- key the operator's no-reuse rule on the problem, not the symbol (RT-475).

**The rest are worth noting, and none blocks step 4b:**
- the bites stream (RT-476);
- the unbuilt twin that is built (RT-477);
- bites donors repeating the routine fact (RT-478);
- the gaps in the step-3 report (RT-479);
- the test half's shares (RT-480);
- the lookup allocation's reason (RT-481);
- the thin products margin (RT-482);
- the neutral lengths (RT-483);
- the overlap check's content gaps (RT-484).

The test half's shares (RT-480) and the overlap check's content gaps (RT-484) must be settled before any test set is generated.

---

## The filer's check (not part of the independent check)

*Written by the author of section 17 and the generator changes, 2026-11-21. It closes nothing.*

- **The drawing rule (RT-473).** Confirmed by reading the code. `rule_op`, `rule_unit`, `rt_sum` and `rt_prod` draw the right answer's place first and keep it while they redraw the item. An answer at the edge of the range, such as 10, can fill only some places, because its wrong answers must have two digits. So an edge item is accepted only when the drawn place fits it, and edge values are drawn less often than the pool says. Section 17, item 4 asked for both "uniformly from the pool" and "place drawn first" without seeing that they conflict at the edges. The mistake is the author's.
- **Not rechecked by the filer:** the nine planted faults of RT-474, the simulations of the places and the drawn distribution, and RT-475 to RT-484.
- **Where things stand.** The pilot rebuilds byte for byte, and the split recomputes exactly. One serious finding (RT-473) must be fixed before step 4b, and the pilot rebuilt and rechecked. The checker suggests fixing RT-474 and RT-475 at the same time. RT-480 and RT-484 must be settled before any test set.
