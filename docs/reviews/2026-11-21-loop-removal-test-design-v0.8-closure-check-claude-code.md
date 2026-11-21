*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the seven earlier reviews. It worked read-only in a detached worktree at commit 38148b1, using only its own scratch folder, which was created empty for it. It changed nothing in the repository. It also read two TimeAssembler worklog entries through the v1 API, read-only. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.8

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or any of the seven earlier reviews. I worked read-only in the detached worktree `closure8-loop-design-2026-11-21` at commit 38148b1 and changed nothing in it. `git status` was clean when I finished. I used only my own scratch folder, `/private/tmp/claude-501/loop-review8-H2GpRb`, which was empty when I started. Every script and every output is in that folder. I did not open, list or use any other scratchpad or temporary folder, including the author's session scratchpad and every earlier `loop-review*` folder. I downloaded nothing, installed nothing and spent nothing. New findings continue the red-team numbering from RT-409.*

---

**What I opened.**
- **Read in full:**
  - the closure check of version 0.7, `docs/reviews/2026-11-21-loop-removal-test-design-v0.7-closure-check-claude-code.md`. I treated its filer's check as the author's note, not as part of the review;
  - the ruling file, `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`;
  - `git diff 8a5aabb 38148b1` on the design and on the ruling file;
  - the design's sections 1 to 11 and its seventh change log;
  - the tokeniser download record, `docs/2026-11-21-loop-removal-tokeniser-download.md`.
- **Read in part:**
  - `docs/outside-review-protocol.md`: its opening sections, the tier 1 description and "The closure rule, which is the new part";
  - `experiments/09-split-removal-test/src/batteries.py`, lines 1 to 200 (the pools, the invented syllables and the old generators);
  - the research model's `chat_template.jinja` and `REVISION` (657b53ba…);
  - the earlier reviews named `*loop-removal-test-design*`, searched only for "intrud", to see whether any earlier review had raised the point in RT-411. None had.
- **Read outside the repository, read-only:** two TimeAssembler worklog entries, fetched with one GET request to the v1 API. They are the decision entry "John rules the loop removal test's five choices, and paper work only for now (2026-11-21)" and the progress entry "Loop removal test: the fifth check confirms the shared-context fix with the real tokeniser, but finds the free check can no longer settle the dose question". I read them to check what the ruling note and section 11 say about them. I then deleted the downloaded list from my scratch folder.
- **Ran** these scripts under the project Python with `-I`, using the research model's real tokeniser (`tokenizers.Tokenizer.from_file`). All of them are in my scratch folder.
  - `tok.py` renders the chat template in jinja2's sandboxed environment, with the reasoning setting "none" and `{% generation %}` treated as a plain block. The rendered template is identical to the string my builder assembles, which `single.py` checks.
  - `single.py` makes the single-token counts.
  - `build.py` and `run.py` are my stand-in pair builder under version 0.8, with the donor counts and the dose ratio.
  - `starved.py` lists which scored pairs are left without a donor.
  - `ctx.py` (with `build2.py`, a copy of `build.py` that adds two counters) counts what a donor's context names.
  - `feas.py` finds the largest test size that the pairing exclusions and the 25% cap allow.

**What I did not open.** I did not open:
- the earlier reviews, apart from the search above;
- the committed pilot battery files;
- the three-hypotheses proposal and the design note;
- any web page;
- any scratchpad except my own.

**What is real and what is a stand-in.**
- **Real:** the tokeniser and the chat template. Every token count and length below comes from them.
- **Stand-ins, written by me, because the battery specification does not exist yet:**
  - **the content pools.** 193 UN member countries with capitals and a coarse region tag of my own. 89 opposite pairs with no prefix opposites and no word in two pairs. 137 everyday objects with colours. 212 three-letter words with three different letters. 11 colours. Invented words built from 20 + 20 syllables;
  - **the rule wordings and operand ranges.** Half A operator operands run 2 to 15, and half B 25 to 99. Half A unit counts run 2 to 9, and half B 42 to 99;
  - **the wrong answers.** Numbers within 5 of the right answer, with the same number of digits. Same-region capitals first. Other opposites from the pool. Other colours. Four of the five other table colours. For the letter code, four random words: I did not build the "extra letters chosen to fit" rule;
  - **the pool halves.** They are random splits by seed;
  - **how pairs are allocated to pairings.** I used a flow allocation that keeps the exclusions and the 25% cap;
  - **the opening of the model's reply.** I assumed `<|message_model|><|content_text|>`, which step 4a has not yet settled.
- **The aimed rule as I built it.**
  - Each candidate donor-only pair is drawn with a routine question chosen from the whole half, so reuse is allowed.
  - It is kept only if it can serve a scored pair in its group that still has fewer than five donors.
  - Drawing stops when every scored pair has five donors, when the group holds three times as many donor-only pairs as scored pairs, or when a draw limit is reached. I chose that limit: 200 draws per scored pair in the group, and 5,000 in one rerun. The design states no limit (RT-409).
- **A donor is eligible** when two things hold. Each of its twins must be at least as long as the matching recipient's prompt plus one token. And each twin's right answer must not be among the matching recipient twin's candidates.
- **The dose is a proxy.** It is the step-3 measure. Starting at the first position where recipient and donor differ, and running to the end of the recipient's prompt and candidate, each position counts 1 if its token differs from the donor's token at that place. It counts 0, 0.3 or 0.6 if the token is the same. Five donors are drawn at random from the eligible ones. This is not a measurement on the model.
- **My stand-in starves more pairs than the seventh check's did.** Without donor-only pairs, it leaves 8 to 14 of 30 lookup pilot pairs with no donor, where the seventh check found about 5. My counts are therefore a harder test of the fix, not a reproduction of the seventh check's numbers.

---

## Verdicts

| Item | Verdict | Label |
|---|---|---|
| RT-345 (fatal), the swap's dose differed between the two task groups | **Not closed, and it cannot be closed on paper.** It is owed at step 4b. Under version 0.8's rules the stand-in ratio is 0.9953 to 1.0005 | MEASURED (proxy); ARGUED for what remains |
| RT-403 (serious), whether donor-only pairs may reuse routine questions | **Closed** | MEASURED (stand-in); ARGUED (overlap script) |
| RT-404, the longest pairs left without donors | **Closed, with conditions** (RT-409) | MEASURED (stand-in) |
| RT-405, the ruling note and the record | **Closed, with one small wording fix** (RT-413) | MEASURED (diff, worklog read); ARGUED |
| RT-406, stale text | **Closed, with one leftover** (RT-413) | MEASURED (grep) |
| RT-407, the pool arithmetic | **Closed, with a condition** (RT-410) | MEASURED |
| RT-408, which way the capitals cost points | **Closed, with a condition** (RT-414) | ARGUED |
| RT-402 condition, two gaps in the baseline checks | **Closed** | ARGUED |
| RT-396 condition, the region map | **Closed on paper.** The map itself is owed in the battery specification (step 3) | ARGUED |
| The cost sentence | **Closed, with notes** (RT-413) | MEASURED (arithmetic, stand-in) |

### RT-403, donor-only pairs may reuse content: closed (MEASURED, stand-in)

**The text.** Section 3 says that donor-only pairs may reuse any routine question, rule content or invented word from their own half. They sit outside the rule that no routine question is used twice, outside the pool budget and outside the 25% cap. The overlap script counts them with the set they serve.

**What I measured.** I ran `run.py pilot|200 none|unaimed|aimed`, five splits each.

```
                                   donor-only pairs added   no donor   fewer than 5   mean eligible donors
pilot, no donor-only pairs           0                      35 to 47   104 to 107     1.8 to 2.0   (of 120)
pilot, version 0.7 (unaimed)         346 to 360             8 to 16    49 to 64       7.8 to 8.9
pilot, version 0.8 (aimed)           176 to 199             0 to 3     0 to 4         8.7 to 9.9
  lookup only, version 0.8           56 to 71 (cap 90)      0          0 to 1         7.2 to 9.2   (of 30)
200,  no donor-only pairs            0                      24 to 44   135 to 146     3.4
200,  version 0.7 (unaimed)          584 to 600             12 to 16   45 to 62       14.0 to 14.5
200,  version 0.8 (aimed)            179 to 203             2 to 10    2 to 11        10.3 to 11.6
```

- **With reuse allowed, donor-only pairs can be built where they are needed.** No pool ran out at either size, and every build reached its full 120 or 200 scored pairs.
- **Reuse opened no route for an intruding answer that I could find.** Among about 2,900 chosen donors at the pilot and 4,800 at 200, none shared its recipient's routine question, and none shared its rule facts. That is because a repeated routine question carries the recipient's right answer, so the existing rule against intruding answers bars it, exactly as the text argues. I also counted how often a donor's context names the recipient's right answer. The rates are the same with and without donor-only pairs: about 49% in lookup's rule cell, and 0% to 3% elsewhere (see RT-411). Reuse does not change that number.
- **Reuse opened no leak between pilot and test.** Every donor-only pair is drawn from its own half. Since the overlap script counts donor-only pairs with the set they serve, the existing script check covers them (ARGUED).
- **Reuse opened no difference between the cells.** Each donor-only pair is a whole pair, and it serves both twins of its recipient. The dose ratio is unchanged (below).
- **One thing the text allows that random drawing never produced** is described in RT-412.

### RT-345: the stand-in dose under version 0.8 (MEASURED, proxy)

The ratio is the routine cell's proxy dose divided by the rule cell's, per rule kind, at weights 0, 0.3 and 0.6. All figures are the lowest and highest over five splits.

```
pilot, no donor-only pairs   0.9965 to 1.0008      200, no donor-only pairs   0.9974 to 1.0004
pilot, unaimed               0.9967 to 1.0004      200, unaimed               0.9978 to 1.0001
pilot, aimed (version 0.8)   0.9953 to 1.0000      200, aimed (version 0.8)   0.9956 to 1.0005
twins of unequal length: 0 in every build
```

- Every rule kind lies well inside the step-3 band and inside section 9's "about 0.99 to 1.03".
- **Aiming does not move the ratio.** The same donor pair serves both cells, and the twins of a pair are always the same length, so the length test and the aiming test treat both cells alike.
- **RT-345 stays open.** Its remaining risk lies in the final question and the answer, which only the model can measure, at step 4b.

### RT-404, the longest pairs: closed, with conditions (MEASURED, stand-in)

**The text.** A candidate donor-only pair is kept only if it can serve a scored pair still short of five donors. Any scored pair left with no donor is dropped, and its content is reported. That makes both of the fixes the seventh check offered.

**What I measured** (`run.py`, `starved.py`).

```
pilot, aimed, 5 splits: pairs with no donor 3 / 2 / 2 / 0 / 3 of 120
  their place by length within their group: 9 of 10 were the longest, 1 the second longest
  groups where the draw limit (200 per scored pair) ran out: 3 / 3 / 3 / 0 / 3 of 14
  same, with the limit raised to 5,000 per scored pair: still 3 / 2 / 2 / 3 pairs with no donor;
    up to 137,685 draws in one build
200, aimed, 5 splits: pairs with no donor 4 / 6 / 10 / 8 / 2 of 200
  20 of 30 were the longest of their group, and all 30 were among the four longest
  groups where the draw limit ran out: 3 / 5 / 8 / 4 / 2 of 14
groups at the threefold cap: 0 or 1 of 14 in every aimed build
where they fall: mostly letter code with sums or products, and operator with capitals or colours.
  The cause is a long code table, a long object ("sea on a sunny day") or a long country
  ("Bosnia and Herzegovina") that no other routine question in the half can match in length.
```

- **What aiming achieves.** It cuts the pairs left without a donor by about four times, from 8 to 16 to 0 to 3 at the pilot. It does this with about half as many donor-only pairs.
- **What it cannot do.** The pairs it still leaves without a donor are the same kind as before: almost always the longest of their group. A recipient whose routine question is the longest in its half cannot be served by a pair that reuses that question, because the reused question has the same right answer. A random draw almost never produces another pair that long.
- **The threefold cap no longer binds.** It is reached in 0 or 1 groups of 14. What actually ends the drawing is the draw limit, and the design states none (RT-409).
- **Reporting the dropped pairs' content**, which the text now requires, is the right safeguard. The loss of the longest items is real.

### RT-405, the ruling note and the record: closed (MEASURED by diff and worklog read; ARGUED)

- **John's answers are unchanged.** `git diff 8a5aabb 38148b1` on the ruling file touches only the dated note at its end. I also compared the ruling's body, the part above the rule line, at commit 25e55f8, where it was first recorded, with commit 38148b1. The only difference is one blank line added before the rule. So John's answers are as he gave them.
- **The note now says what the record supports.**
  - The question for choice 3 was not in section 10's words. It added the sentence about the latest check, as both the ruling's body and the decision worklog entry record.
  - The option wording comes from the session's question form, and the session transcript is the primary record.
  - The fifth-check worklog entry records the finding.
- **I read the cited progress entry.** It says the free check "contradicts a premise in John's ruling on choice 3". It does not record that John was told. That matches section 11's new sentence. The note's last sentence, that section 11 records the telling, is accurate as a pointer, but section 11 is itself the author's account.
- **One small wording fault** (RT-413). The note says "The source of these quotations is the session". But "these quotations" also covers the section 10 quotation, whose source is commit ddc5031, not the session.

### RT-406, stale text: closed, with one leftover (MEASURED by grep)

- "Five to seven entries", "63%" and the fifth check's findings no longer appear in the body.
- Section 9's steps 1 to 3 are current.
- The seventh change log's header marks the earlier rules that were replaced.
- **The leftover.** The pilot paragraph in section 5 still says "a fifth of a kind" for the "answered as well behind its rule" check. The rule is now "a fifth of a pairing's pairs that pass the confidence check" (RT-413). Several "300 pairs" anchors are also left over (RT-410).

### RT-407, the pool arithmetic: closed, with a condition (MEASURED)

```
python3 -I single.py
products 2 to 12, one order each: half with answer >= 40: 35 (31 distinct answers); half < 40: 31
capitals one token at the answer position 90; after the copying rule 84; with a leading space 23
python3 -I feas.py     (largest test size the pairing exclusions and the 25% cap allow)
design's stated pools, capitals 42, opposites 60 or 70, colours 60: 262 or 273
capitals 36 to 50 (the spread a split gives, per the seventh check): 254 to 286
products counted in both orders (60): 307, which is the old figure
300 fits only if opposites and colours are both larger than the text states (for example 80 each: 326)
200 fits in every case
```

- "A multiplication counts once" is now stated, and it reproduces 35 products and 273.
- **The condition (RT-410).** The text's "at most about 270 to 300 pairs" overstates the top. On the pool sizes the text itself gives, the ceiling is about 255 to 285, and 300 does not fit.

### RT-408, which way the capitals cost points: closed, with a condition (ARGUED)

- **What is fixed.** The direction is stated: the cost favours outcome A, the predicted pattern. Margin matching is withdrawn as a safeguard. Any A is reported beside its reading with the capitals pairs left out, including a reading that lands in E.
- **No conflict with section 6.** Section 6 already reports every reading with one kind left out, and it renames only on a different definite outcome. If the capitals-out reading lands in B, C or D, section 6 renames the A, so there is no A left to report it beside.
- **The condition (RT-414).** Section 7, which fixes the words of every summary, does not say whether the capitals-out reading travels with an A into STATUS.md, the site and public summaries.

### The RT-402, RT-396 and cost conditions

- **RT-402, the baseline checks (ARGUED).** Both baseline checks now count "a fifth" from the pairs that pass the confidence check. "One routine kind or none" now returns the design to John. Closed. The leftover wording in the pilot paragraph is under RT-413.
- **RT-396, the region map (ARGUED).** The battery specification must now write out the region map and each region's nearest neighbouring region before any item exists. The text's "about one in ten" matches the seventh check's figure of 39 to 40 of 43. Closed on paper. Whether the map is written, and the counts under it, can only be checked at step 3.
- **The cost sentence (MEASURED, arithmetic).** It now says two unaltered runs per donor-only pair. 1.7 MB per run reproduces: 2 sums × 2 passes × 90 positions × 2,304 numbers × 2 bytes ≈ 1.66 MB. Closed, with notes under RT-413.

---

## Press on what version 0.8 changes (item 3 of the brief)

- **Reuse and intruding answers (MEASURED, stand-in).** No chosen donor repeats its recipient's routine question or rule facts, and the rate at which a donor's context names the recipient's right answer does not change when reuse is added. So reuse opens no route of its own. A separate difference between the cells that existed before version 0.8 is in RT-411. A permission that random drawing never used, but that the text allows, is in RT-412.
- **Reuse and leaks between pilot and test (ARGUED).** None. Donor-only pairs come from their own half and are counted with the set they serve.
- **Aimed pairs and differences between the cells (MEASURED, stand-in).** Aiming chooses whole pairs by a test that the two twins pass or fail together, because they have equal length. The other part of the test, the answer check, is applied to each cell's own answer. So it cannot steer different donors to the two cells. The dose ratio is unchanged, at 0.9953 to 1.0005. Aiming does favour long donors, because those are the ones that can serve the long recipients that are short of donors. That favours them equally in both cells.
- **The ruling note (MEASURED).** It is accurate to the record, apart from one pointing word. John's answers are unchanged since commit 25e55f8 (diff above).
- **The capitals rule for outcome A and sections 6 and 7 (ARGUED).** There is no conflict with section 6. There is a gap in section 7 (RT-414).
- **Rules stated only in a change log, or contradicted between sections (MEASURED by grep).** Every item in the seventh change log is also in the body. I found no outright contradiction. I found one leftover wording and several stale "300 pairs" anchors, under RT-410 and RT-413.

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-409 | The aimed rule has no stopping rule for its draws, and the pairs it still cannot serve are the longest of their group | worth-noting | MEASURED (stand-in) |
| RT-410 | The ceiling of "about 270 to 300 pairs" overstates the top. On the text's own pool sizes it is about 255 to 285, and several figures are still pegged to 300 pairs | worth-noting | MEASURED |
| RT-411 | In lookup pairings, a donor's context names the rule item's candidate colours about half the time, but almost never names the routine twin's candidates. This difference between the cells existed before version 0.8, and the stand-in dose cannot see it | worth-noting | MEASURED (rates); ARGUED (effect) |
| RT-412 | "Reuse is harmless" rests on answers alone. The text would let a donor-only pair copy its own recipient's rule content, which gives that recipient a weaker swap | worth-noting | ARGUED |
| RT-413 | Small text faults: the stale donor-pair figure and storage basis in the cost sentence, "a fifth of a kind" in the pilot paragraph, and "these quotations" in the ruling note | worth-noting | MEASURED (grep, arithmetic) |
| RT-414 | Section 7 does not say whether the capitals-out reading, or the leave-one-kind-out sentence of RT-371, travels with an A into STATUS.md and public summaries | worth-noting | ARGUED |

**RT-409, no stopping rule for the aimed draws (worth-noting, MEASURED, stand-in).**
- **The gap.** Section 3 says that a candidate pair which cannot serve a short pair "is discarded and another is drawn, up to the threefold cap". But the cap counts kept pairs. When a pair is out of reach, the draws never end.
- **What I measured.**
  - In my builds, the draw limit I imposed ran out in 3 of 14 groups in four of five pilot splits, and in 2 to 8 groups at 200 pairs.
  - Raising the limit 25 times, to 5,000 draws per scored pair, rescued none of those pairs.
  - What remains is almost always the longest pair of its group: 9 of 10 at the pilot, and 20 of 30 at 200, all among the four longest.
- **Fix.**
  - The battery specification fixes a draw budget per group before generation, and states that reaching it ends the drawing.
  - Step 3 reports the draws used, and the place by length of each pair dropped, beside its content.

**RT-410, the ceiling and the 300-pair anchors (worth-noting, MEASURED).**
- **The ceiling.** With 35 products, 42 capitals, 60 to 70 opposites and 60 colours, the pairing exclusions and the 25% cap allow 262 to 273 pairs. As capitals move between 36 and 50, that becomes 254 to 286. 300 fits only if opposites and colours are both larger than the text states.
- **Figures still pegged to 300 pairs:**
  - section 3's storage, "about 2.5 GB at 300 pairs";
  - section 5's opening, "a cell of 300 pairs allows 75 questions of each routine kind";
  - section 8's "roughly 700 items (300 pairs, 100 chained lookups)".
- **What is unaffected.** The expected 120 to 200 pairs fits in every case.
- **Fix.** Say "about 255 to 285 on these pool sizes", or state the pool sizes 300 would need. Rest the storage and run counts on the ceiling or on 200 pairs.

**RT-411, candidate words in the donor's context (worth-noting, MEASURED rates, ARGUED effect).** I ran `ctx.py`, five splits.

```
lookup pairings, rule cell: the donor's table names the recipient's right colour 41% to 51% of the time,
  and each wrong candidate 49% to 50%
routine cells, every pairing: the donor's context names the recipient's right answer 0% to 3%,
  and each wrong candidate 0% to 1.5%
code and operator rule cells: 0% to 2%; unit rule cell 3% at the pilot and 0% at the test
these rates are the same with no donor-only pairs, with the version 0.7 rule and with the version 0.8 rule
```

- **What it is not.** The right colour is named no more often than a wrong one. So this is not the intruding answer that RT-346 (the donor's answer intruding among the candidates) dealt with, and reuse did not cause it.
- **What it is.** In the lookup kind, the swapped message in the rule cell names the item's own candidates about half the time, while in the routine cell it almost never does. That is a difference in what the replacement carries between the cells, inside the very part RT-345 leaves to the model, and the proxy cannot see it.
- **A pilot detail.** The pilot's small numbers let a donor's numbers equal the recipient's answer: about 3% of unit-kind donors, and 2% to 4% of sum and product donors. The test half's operand ranges cannot do that. So the pilot slightly misrepresents the test here.
- **A rare case.** A donor asking the opposite of "cold" can serve a recipient whose answer is "cold". It turned up 0 to 5 times per build, no more often than the naming of wrong candidates.
- **Fix.** Report these rates per kind at step 3. Note the lookup case beside the reading with lookup left out at step 4b.

**RT-412, a donor that copies its own recipient (worth-noting, ARGUED).**
- **What the text allows.** It lets a donor-only pair reuse any rule content from its half, which includes the rule content of the very recipient it serves: the same lookup table asked for another name, or the same operator rule with other operands. Its answer then differs, so the rule against intruding answers does not bar it.
- **Why that matters.** Such a donor matches the recipient's tokens for longer, so the recipient gets a weaker swap. It is also the obvious way for a generator to reach the longest pairs of RT-409.
- **What I saw.** Random drawing never produced one (0 in every build).
- **Fix.** Bar a donor-only pair from reusing the rule content or the routine question of any recipient it serves. It may still reuse other pairs' content.

**RT-413, small text faults (worth-noting, MEASURED by grep and arithmetic).**
- **The cost sentence.**
  - Its figure of 2.1 to 2.8 donor-only pairs per scored pair comes from the seventh check's unaimed rule. Under the aimed rule my stand-in adds 1.5 to 1.7 at the pilot and 0.9 to 1.0 at 200. So the sentence overstates the cost, which is the safe direction, but it should say which rule its figure belongs to.
  - "About 5%" sets runs of one twin against runs of a whole pair. Measured per twin, it is about 2.5%, and each donor run scores one answer, not five.
  - The storage figure counts donor-only runs only. Scored twins donate too, and their runs add about 1 GB at 300 pairs.
  - Section 8's run count leaves out donor-only pairs, and it says it will be recounted from the code.
- **Section 5's pilot paragraph.** It still says "a fifth of a kind". It should say "a fifth of a pairing's pairs that pass the confidence check".
- **The ruling note.** "The source of these quotations is the session" should exclude the section 10 quotation, whose source is commit ddc5031.

**RT-414, how far the capitals-out reading travels (worth-noting, ARGUED).**
- **The gap.** Section 5 requires any A to be reported beside its capitals-out reading. Section 6 requires the RT-371 sentence (about the effect left when one kind carries most of it) beside any A at the smaller sizes. Section 7 fixes the words of every summary in STATUS.md, on the site and in public, but it mentions neither.
- **Fix.** State in section 7 whether both readings go with an A wherever the A sentence is used.

---

## Verdict

**Version 0.8 is ready for the battery specification at step 3. RT-345, the finding that the swap's dose differed between the two task groups, is carried as an open fatal item that only step 4b on a rented machine can close. Nothing has to be fixed in a version 0.9 first.**

- **What holds, measured with the real tokeniser and my stand-in build:**
  - with reuse allowed, donor-only pairs can be built at both sizes;
  - the aimed rule cuts the pairs left with no donor from 8 to 16 to 0 to 3 at the pilot, and from 12 to 16 to 2 to 10 at 200, with about half as many donor-only pairs;
  - lookup is left with no starved pilot pair in any split;
  - the stand-in dose ratio stays between 0.9953 and 1.0005 in every rule kind, with or without donor-only pairs;
  - no chosen donor shares its recipient's routine question or rule facts, and reuse did not change how often a donor's context names the recipient's right answer;
  - John's answers are unchanged since they were first recorded.
- **What goes into the specification:**
  - the draw budget and the reporting of RT-409;
  - the ceiling wording of RT-410;
  - the per-kind report of RT-411;
  - the bar on copying a recipient in RT-412;
  - the wording fixes of RT-413 and RT-414;
  - the region map that RT-396 requires.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **RT-413, the leftover wording.** Confirmed. Section 5's pilot paragraph (line 738) still says "a fifth of a kind".
- **RT-405, John's answers.** Confirmed independently. `git diff 25e55f8 38148b1` on the ruling file removes no line. The only changes since the ruling was first recorded are the dated note and one blank line.
- **Where things stand.** RT-403 to RT-408 and the three conditions close, some with conditions. RT-345 stays open until step 4b. **The reviewer finds version 0.8 ready for the battery specification (step 3), with nothing to fix in a version 0.9 first.** RT-409 to RT-414 are worth noting and go into the specification:
  - a draw budget for donor-only pairs;
  - the ceiling wording, at about 255 to 285 pairs on the stated pools;
  - a per-kind report of candidate colours named in donors' lookup tables;
  - a bar on a donor-only pair copying its own recipient's content;
  - small wording fixes;
  - stating in section 7 that the capitals-out reading travels with any outcome A.

  The specification also owes the region map that RT-396 requires.
