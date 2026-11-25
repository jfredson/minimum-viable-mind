*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the five earlier reviews. It worked read-only in a detached worktree at commit 5bc172a, using only its own scratch folder, created empty for it and kept apart from the author's files and from earlier reviewers' folders. It changed nothing in the repository. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.6

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or any of the five earlier reviews. I worked read-only in the detached worktree `closure6-loop-design-2026-11-21` at commit 5bc172a and changed nothing in it. I used only my own scratch folder, `/private/tmp/claude-501/loop-review6-zeFu1f`, which was empty when I started. Every script and every output is in that folder. I opened no other scratchpad or temporary folder. I downloaded nothing, installed nothing and spent nothing. New findings continue the red-team numbering from RT-398.*

---

**What I opened.**
- **Read in full:**
  - the target, `docs/loop-removal-test-design-2026-11-20.md` (version 0.6, with all five change logs);
  - the closure check of version 0.5, `docs/reviews/2026-11-21-loop-removal-test-design-v0.5-closure-check-claude-code.md`. I treated its filer's check as the author's note, not as part of the review;
  - John's rulings, `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`;
  - the tokeniser download record, `docs/2026-11-21-loop-removal-tokeniser-download.md`.
- **Read in part:**
  - `git diff b8579de 5bc172a` on the design. I read every removed line and checked where each removed rule went;
  - `docs/outside-review-protocol.md`: the tier 1 description and "The closure rule, which is the new part";
  - `experiments/09-split-removal-test/src/batteries.py`, its first 80 lines (the pools and syllables);
  - section 10's choice 3 in version 0.4 (`git show ddc5031`), to check the section 11 note against the words John was shown;
  - the research model's `chat_template.jinja`, its `REVISION` (657b53ba…), and the pre-tokeniser settings in `tokenizer.json`.
- **Ran** these scripts with the research model's real tokeniser, loaded through `tokenizers.Tokenizer.from_file`, under the project Python with `-I`. I rendered the template in jinja2's sandboxed environment, with `{% generation %}` treated as a plain block. My render matched the twelve tokens before and one token after the user text exactly.
  - `tok_table.py`: recounts section 5's wording table;
  - `single.py`: counts which candidates are one token;
  - `gen.py`: my stand-in pair builder under version 0.6;
  - `dose.py`: the stand-in dose ratio, the tail shares and the donor counts;
  - `align.py`: the alignment claims;
  - `dist.py`: how far each needed fact sits from the final question;
  - `feas.py`: the pool arithmetic and whether the lookup floor can be met;
  - `lookup_donors.py`: lookup's donor supply under different size rules.

**What I did not open.** I did not open:
- the inside review of version 0.1, or the closure checks of versions 0.2 to 0.4, beyond their titles;
- the three-hypotheses proposal and the design note;
- the committed pilot battery files;
- any external page;
- any scratchpad except my own.

**What is real and what is a stand-in.**
- **Real:** the tokeniser and the chat template. Every token count, position and length below comes from them.
- **Stand-ins (written by me, because the battery specification does not exist yet):**
  - every content pool: 193 countries with capitals and a coarse region tag, 84 opposite pairs, 50 everyday objects, 253 three-letter words, and invented syllables;
  - my own list of 105 "well-known" countries, which is my judgment and not the design's list;
  - the wording of each rule and each fact;
  - how pairs are allocated to pairings;
  - the opening of the model's reply. I assumed `<|message_model|><|content_text|>`, which step 4a has not yet settled.
- **The dose is a proxy.** It uses the step-3 rule. Starting at the first place where recipient and donor differ, each position counts 1 if its token differs from the donor's token at the same place, and 0, 0.3 or 0.6 if the token is the same. It is not a measurement on the model.

---

## Verdicts

| Item | Verdict | Label |
|---|---|---|
| RT-345 (fatal), the swap's dose differed between the two task groups | **Not closed, and it cannot be closed on paper.** It is owed at step 4b, as the design says. The stand-in now passes by construction (0.996 to 1.001) | MEASURED (proxy); ARGUED for what remains |
| RT-390, the false alignment sentences | **Closed, with one condition** | MEASURED |
| RT-391, the free checks pass by construction | **Closed in the design text, with a condition on the section 11 note** (RT-401) | MEASURED (tail shares); ARGUED (record) |
| RT-392, the lookup size-class rule at the pilot | **Not closed.** The pilot part is met, but the problem has moved to the test size, and lookup's donor supply is poor at both sizes (RT-398) | MEASURED |
| RT-393, the baseline check's comparison item and the mirror check | **Closed, with conditions** (RT-402) | ARGUED (text) |
| RT-394, the context order and the ambiguous wordings | **Closed, with conditions** | MEASURED |
| RT-395, the copying rule's scope | **Closed.** One small residual case | ARGUED (text); MEASURED (word list) |
| RT-396, the colour pool and the half-A rule | **Closed, with a condition** | MEASURED (stand-in coverage) |
| RT-397, stale or conflicting text | **Closed as text.** But the new figure of 325 that it settles on is itself too high (RT-399) | MEASURED (grep and tokeniser) |

### RT-390, the alignment sentences: closed, with a condition (MEASURED)

```
python3 -I align.py     (seeds 1-3, the pilot build and the 300-pair build)
pairs whose two twins have the same token length: 1260 of 1260
donor draws where the first differing position is the same in both cells: 4756 of 4756
donor draws with the same context length as the recipient: 2193 of 4756 (46%)
prompt-rule tail tokens matching the donor's at the same place: 25006 of 58606 (43%)
```

- **The twins now line up.** Every candidate is one token, so the two twins of every pair have the same length, and both cells diverge from their donors at the same place. That is what section 3's "Length" bullet and section 5 now say.
- **The donors do not line up, and the text now says so.** Fewer than half of donor draws have the same context length as the recipient, and fewer than half of the tail tokens match the donor's at the same place. The new sentences in sections 3 and 5 say that donors' final questions usually start later, which matches these figures.
- **The condition.** Section 9, step 3 says that a correct build gives "about 1.00 to 1.03". My correct builds give 0.996 to 1.001 (below). The step-3 band of 0.95 to 1.05 still passes, but the sentence that describes a correct build should read "about 0.99 to 1.03". Otherwise a reader could take a value just under 1 as a sign that the generator is wrong.

### RT-345 and RT-391: the stand-in dose and the tail under version 0.6 (MEASURED, proxy)

**What I built.** I built pairs as version 0.6 describes them:
- the rule always comes first;
- the order of the rule's facts and the routine fact is balanced by a seed within each group of rule kind, routine kind and size;
- the fixed final questions are taken from section 5's table, and only the allowed pairings are used;
- every candidate is one token at the answer position;
- lookup uses six-entry tables at the pilot and 5, 6 and 7 entries at the test size, with donors drawn within each size class;
- a donor must be at least as long in both twins, and a donor's right answer is never one of the recipient's candidates;
- each pair gets five random donors, or all the eligible ones if there are fewer.

The pilot has 30 pairs per rule kind. The 300-pair build has 75 per rule kind, with lookup at 18 to 21 pairs per routine kind, so that its floor of six per size class is met.

```
python3 -I dose.py pilot <1|2|3> [routine_last]      ratio = routine cell / prompt-rule cell, at weights 0 / 0.3 / 0.6
  operator 0.9958-0.9982 / 0.9974-0.9988 / 0.9987-0.9994    unit 0.9970-0.9990 / 0.9980-0.9993 / 0.9990-0.9996
  code     0.9988-1.0009 / 0.9994-1.0004 / 0.9997-1.0002    lookup 0.9990-1.0007 / 0.9994-1.0005 / 0.9997-1.0003
python3 -I dose.py test <1|2|3>                       every ratio 0.9972-1.0002
tail share after the shared context (identical in the two cells to three decimals):
  operator 0.31   unit 0.34   letter code 0.20   lookup 0.18 (pilot) / 0.19 (300 pairs)
```

- **Result.** Every rule kind lies well inside the step-3 band, at the pilot size and at 300 pairs, in both context orders. That matches version 0.6's claim, and it confirms RT-391's point: the free check passes by construction and says nothing about the real dose.
- **The tail.** The tail shares agree with the fifth check (16% to 34%). Step 4b's 10% limit then tolerates a difference in real distance per position across the tail of about:
  - 30% for the unit kind;
  - 32% for the operator kind;
  - 49% for the letter-code kind;
  - 54% for the lookup kind.

  These are the numbers step 3 is now told to report. They describe the six-entry pilot tables only (RT-398).
- **RT-345 stays open.** Its remaining risk sits in the last 11 to 13 positions of each item, where the two final questions are different words. Only the model can measure that.
- **RT-391 in the design text.** Step 3's estimates are restated as checks that the generator builds what section 5 describes. The tail-share report is added. Telling John when step 4 is priced is written into step 3. All three are in place (lines 808 to 819). The section 11 note has an accuracy problem (RT-401).

### The wording table (MEASURED, real tokeniser)

```
python3 -I tok_table.py
all 14 rows: prompt-rule count = routine count = the table's count, with a leading space, without one,
after a newline (each +1), and measured after four real contexts joined by a space or a newline. mismatching rows: 0
```

The four rewritten lookup rows are 9 tokens on each side, as stated. The table still covers exactly the fourteen allowed pairings.

### The single-token rule: what survives (MEASURED, real tokeniser; stand-in pools)

```
python3 -I single.py
capitals, all 193 UN-member-style entries: one token at the answer position 90 (47%); with a leading space 23
capitals, reviewer's 105 well-known: one token 71 (68%)
capitals of the other 88 countries: one token 19
single-token capitals barred by the copying rule as right answers: Djibouti, Bissau, Luxembourg, Monaco, Singapore, Tunis
single-token, not barred: 84    of which 69 are on my well-known list
by region, kept/all: Europe 32/43, Middle East 11/15, Africa 13/53, Oceania 1/14, Caribbean 2/13, Central America 1/8
half B (20 random splits): 42 capitals; items with at least 4 same-region single-token half-B wrong answers: 16 to 27 (median 22)
adjectives: 138 of 156 one token        colours: all 17 tested one token (11 basic, plus violet, gold, silver, teal, tan)
three-letter words: 252 of 253 one token; 245 with three different letters
numbers 0 to 999: all one token; 1000 and above: two tokens; with a leading space no number is one token
```

- **The claim of 82 of 105 capitals did not reproduce on my list.** My list of 105 well-known countries gives 71 of 105. My list is not the design's, so this difference alone settles nothing.
- **The claim of about 55 capitals in half B is too high, whichever list is used.** Across every country I listed (193), only 90 capitals are one token, and 84 after the copying rule. Half B can therefore hold about 42, not about 55. A list of "at least 150 countries" cannot do better than the whole world (RT-399).
- **The capitals that survive are the easy ones.**
  - 69 of the 84 survivors are on my list of well-known countries. Only 19 of the 88 less-known capitals are one token.
  - Europe's share rises from 22% to 38%, and Africa's falls from 27% to 15%.
  - So the capitals cell now asks mostly about famous capitals. Its close wrong answers are also famous capitals, so recognising the right one among five is easier, which weakens the answer to RT-349 (the finding that choosing among five tests recognition, not producing an answer).
- **Close wrong answers can be built for only about half the capitals.** In half B, only about 22 of 42 capitals have four single-token same-region alternatives. The design does not say what happens to the rest (RT-396 condition).
- **The other kinds barely change.**
  - Opposites lose about 12% of adjectives.
  - Colours, three-letter words, and numbers up to 999 all pass.
  - The prompt-rule kinds are therefore untouched, as long as the operator kind's half-B answers stay at or below 999. The design does not state that range, and the specification must.
- **Everything depends on there being no space before the answer.** With a leading space, only 23 capitals and no numbers at all are one token (RT-400).

### RT-392 and lookup's donors (MEASURED, stand-in)

```
python3 -I lookup_donors.py      (10 seeds each)
pilot 30, one size (6)                  no donor 2-9 of 30 (mean 6.0); fewer than 5 donors: 28 of 30; mean eligible 2.1
   same, without the donor-answer exclusion: no donor mean 2.6; fewer than 5: 17; mean eligible 3.8
test 75, three size classes (v0.6)      no donor 12-21 of 75 (mean 17.0); fewer than 5: 73.5; mean eligible 1.6
test 75, one size (6)                   no donor mean 5.5; fewer than 5: 28; mean eligible 5.5
test 75, sizes 5-7 mixed, no class rule no donor mean 5.4 (all of them seven-entry tables); mean eligible 5.1
python3 -I dose.py pilot <seed>          other kinds at the pilot: 1-3 of 30 with no donor, 8-15 with fewer than five
python3 -I feas.py
lookup keeping all four routine kinds at the test floor (6 pairs x 3 size classes = 18 per routine kind) is possible
only from 288 pairs upward (four kinds x 18 = 72 lookup pairs). With 42 capitals in half B it fails even at 300;
with the design's 55 it just fits at 300. With lookup on sums and products only, every size from 200 to 300 fits.
```

- **The pilot part is met as written.** At the pilot, lookup is spread over four routine kinds, with six-entry tables only.
- **But the pilot does not leave enough donors.** On average, 6 of 30 lookup pilot pairs have no donor and are dropped before any matching. 28 of 30 are averaged over fewer than five donors, and about two on average.
  - **The main cause** is the rule that a donor's right answer is never one of the recipient's candidates. Lookup answers come from eleven colours, and five of them are the recipient's candidates, so about half of all possible donors are barred.
- **The floor at the test size repeats RT-392's conflict.**
  - The test size is set by the sample-size simulation, which the design expects at about 120 to 200 pairs. It is not fixed at 300.
  - Below 288 pairs, lookup cannot keep all four routine kinds and still meet six pairs per size class. At 200 pairs it can keep two, and at 120 pairs one. Yet the pilot's pairing table covers all four.
- **Three size classes make donors scarcer, not more plentiful.**
  - About 17 of 75 lookup pairs lose every donor, against about 5.5 with one table size.
  - The longest pair in each class still has no donor, so the stated aim ("so that the longest pairs are not the ones left without donors") is not met.
- **The pilot does not rehearse the test's lookup items.** The pilot uses six-entry tables only, so it never sees the five- and seven-entry tables the test uses.

---

## Press on what version 0.6 changes (item 3 of the brief)

- **The two baseline checks are defined, but they could strike too much (ARGUED; RT-402).** Both now compare against an item that can be answered, and both are needed. But:
  - **Both are two-sided.** "Within 1.0" also fails an item whose margin rises in the full context, which has nothing to do with the rule getting in the way.
  - **Margins can swing by more than 1.0.** Famous single-token capitals are likely to give large margins, and a large margin can easily move by more than one unit of log-probability when the context changes.
  - **The pilot decides on very few pairs.** At the pilot, a pairing has 6 to 11 pairs. "More than a fifth" then means that two failures strike a pairing.
  - **The two checks compound.** The mirror check doubles the chances to strike a pairing, and it says only that "the same rules apply".

  The result could be a pairing table thinner than the cap and the pools assume, or fewer than three rule kinds surviving.
- **Single-token candidates change what the capitals cell tests (MEASURED skew, ARGUED effect).** The cell is now weighted toward the most famous capitals. Its close wrong answers can be built for only about half of them. Opposites and colours change little, and the prompt-rule cells not at all. "Close" wrong answers can still be built where a region has enough single-token capitals, which in practice means Europe and the Middle East.
- **Balancing the context order (MEASURED with `dist.py`).**
  - **The old gap is much smaller.** The prompt-rule item's own fact now ends 2.8 to 3.9 tokens before the question on average, and the routine fact 4.3 to 5.9 tokens before it. Under version 0.5 the gap was 6 to 8 tokens the other way.
  - **A small gap remains in the other direction.** That is because the rule's facts are longer sentences than the routine fact. The table or rule itself still sits 14 to 18 tokens back in every item.
  - **The dose ratio is unchanged** in both orders (above).
  - **Power is not halved.** The outcome is read on all pairs together, and results by order are a report only. The text should say that by-order results rename nothing.
  - **Donors need not share the order.** Requiring it would halve the eligible donors (operator pilot: 4.6 down to 2.1; lookup: 2.2 down to 0.9) and would not change the proxy. I do not recommend it.
- **The section 11 note on John's ruling (ARGUED from the record; RT-401).** The note puts in quotation marks words that are not in the record in that form. It also leaves out that the question John was shown already said "then measured on the model at step 4b".
- **Rules stated only in a change log, or contradicted between sections.** I found no rule that lives only in a change log. Two figures conflict with measurement rather than with other text: "82 of 105" with "about 55" and "about 325", and "about 1.00 to 1.03". The ruling file still says that the dose question is "to be settled by the free check" and carries no dated note (RT-401).

---

## The other findings

- **RT-393, the baseline checks: closed, with conditions (ARGUED).**
  - **The routine side.** It now compares the full shared context with the routine fact and its final question alone (lines 548 to 551), which can be answered.
  - **The prompt-rule side.** The mirror check is added (lines 559 to 563).
  - **The conditions are in RT-402.**
- **RT-394, the order and the wordings: closed, with conditions (MEASURED).**
  - **The order** is balanced, and the distances are given above.
  - **The wordings.** "The name to look up" and "give the name" are in place and recount correctly. One mild ambiguity remains: in the lookup kind with capitals, "France" is also a name. "The name to look up" settles it.
  - **The conditions:**
    - say that the by-order results are a report only and rename nothing;
    - say how a group with an odd number of pairs is split between the two orders.
- **RT-395, the copying rule: closed (ARGUED).** The rule now covers both cells, and the reverse rule is stated (lines 344 to 351).
  - **One small residual.** In the letter-code kind with everyday colours, the letter-code answer itself (for example "red") may still appear among the routine twin's colour candidates. Only "red" and "tan" are both three-letter words and colours.
  - **A side effect of the general rule.** It bars "cod" in letter-code items, because "cod" is contained in "coded" in the final question. That costs little.
- **RT-396, colours and capitals: closed, with a condition (MEASURED, stand-in).** The shared colour pool and capitals drawn from half B only are both in the body.
  - **The condition.** About half of the half-B capitals cannot get four same-region single-token wrong answers. The specification must say what happens then: the item is dropped, or a wider area is used. Step 3 must report how often each happens.
- **RT-397, stale text: closed as text (MEASURED, grep).**
  - The pair count is 325 in both places.
  - Step 1 describes this check.
  - Results are reported by wording.
  - Choice 3 is marked as describing version 0.4.
  - "360" survives only inside the historical change log, which is correct.
  - The figure of 325 is itself too high (RT-399).

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-398 | Lookup's size-class floor cannot be met at test sizes below 288 pairs if lookup keeps its four pairings. Three size classes leave about 17 of 75 lookup pairs with no donor, and the pilot leaves about 6 of 30. The pilot's six-entry tables do not rehearse the test's tables | serious | MEASURED |
| RT-399 | The single-token rule leaves about 42 capitals in half B, not about 55, so the pool total is about 312, not 325. The surviving capitals skew toward famous European and Middle Eastern ones | serious | MEASURED (stand-in pools, real tokeniser) |
| RT-400 | The single-token pools depend on there being no space before the answer, which step 4a settles after step 3 has generated the pilot | worth-noting | MEASURED |
| RT-401 | The section 11 note quotes words not in the record and leaves out that the question John saw said "then measured on the model at step 4b". The ruling file has no matching note | worth-noting | ARGUED (record) |
| RT-402 | The two baseline checks are two-sided, decide a pairing on 6 to 11 pilot pairs, and the mirror check's rules are given only by reference | worth-noting | ARGUED |

**RT-398, the lookup kind's donors and size classes (serious, MEASURED).**
- **The arithmetic.** Six pairs × three size classes × four routine kinds needs 72 lookup pairs, which means a test set of at least 288 pairs. The simulation is expected to ask for 120 to 200.
- **The donor supply.**
  - With three size classes, about 17 of 75 lookup pairs have no donor, and nearly all have fewer than five. With one size, about 5.5 have no donor.
  - At the pilot, about 6 of 30 have no donor, and about two donors per pair is typical.
  - The donor-answer rule halves lookup's donors, because the colour set is small.
- **Fix:**
  - use six-entry tables at both the pilot and the test, and drop the size classes;
  - add unscored donor-only lookup pairs, which need only their unaltered runs; or, for lookup, bar only a donor answer that equals the recipient's right answer;
  - report donor counts per kind at step 3 from the stand-in build.

**RT-399, single-token capitals (serious, MEASURED).**
- **The count.** Only about 90 capitals in the world are one token at the answer position, and 84 after the copying rule. That gives about 42 for half B.
- **The cost to the arithmetic.**
  - At 300 pairs, the floor in RT-398 then cannot be met.
  - The pool total under the cap falls to about 316, or about 312 if opposites also lose some adjectives.
- **The cost to what the cell measures.** The capitals cell is now mostly famous capitals, which weakens the close-wrong-answer safeguard.
- **Fix:**
  - correct the figures;
  - state the skew as a cost;
  - say whether capitals are kept on those terms. The alternative, keeping multi-token capitals and reporting by candidate length, was offered by the fifth check;
  - have step 3 report the spread of right answers by region.

**RT-400, the leading space (worth-noting, MEASURED).** With a space before the answer:
- only 23 capitals are one token;
- no number is one token, because the space becomes its own token;
- so every arithmetic candidate would fail the rule as written.

**Fix:** step 4a confirms the tokens before the answer. If they differ from what step 3 assumed, the pools and the pilot are rebuilt before any pilot item is scored.

**RT-401, the note on choice 3 (worth-noting, ARGUED).**
- **What the record says.**
  - The ruling file says that each question "was put in the words shown in section 10" of version 0.4.
  - Those words end: "Whether it now passes is first estimated for free at step 3 and then measured on the model at step 4b."
  - "Settled by the free check" is the ruling file's own summary ("The dose question is to be settled by the free check with the real tokeniser before any rental").
  - The note's quotation mixes that summary with section 11's bullet.
- **Why it matters.** John was told that the model would measure the dose at step 4b, so the note overstates how far the premise has moved.
- **What is missing.** No record is cited for "John was told of this in the session".
- **Fix:**
  - quote both texts exactly;
  - cite the worklog entry or session record for the 2026-11-21 telling;
  - add a dated pointer note to the ruling file, without editing John's answers.

**RT-402, the baseline checks' calibration (worth-noting, ARGUED).**
- **Fix:**
  - make both checks one-sided: fail only when the full context lowers the margin by more than 1.0;
  - write out the mirror check's rules for a whole kind and a single pair in full;
  - have step 4b report strike counts per pairing for both checks before the pairing table is fixed.

---

## Verdict

**Version 0.6 is not yet ready for the battery specification at step 3. It is one short revision away, with RT-345 (the finding that the swap's dose differed between the two task groups) carried as an open fatal item, which only step 4b on a rented machine can close.**

- **What holds, measured with the real tokeniser:**
  - the wording table recounts exactly;
  - the twins now have equal lengths, and they diverge from their donors at the same place;
  - the stand-in dose ratio is 0.996 to 1.001 in every rule kind, in both context orders, at 120 and at 300 pairs;
  - the step-3 restatement and the tail shares (0.18 to 0.34) are in place.
- **Two things must be fixed first, because the specification must follow them:**
  - lookup's donor and size-class rule (RT-398). The floor cannot be met below 288 pairs, three size classes drop about a quarter of lookup's test pairs, and the pilot's six-entry tables do not match the test. Using one table size, together with donor-only pairs or a narrower answer rule for lookup, would answer all three;
  - the capital counts and what the single-token rule does to the capitals cell (RT-399).
- **Can go with the specification:** RT-400 to RT-402, and the conditions on RT-390, RT-394 and RT-396.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **RT-401, what John was shown on choice 3. The record the reviewer had was incomplete, and the author can supply the missing part.** John ruled from a question form in the session, not from the repository text. The option he picked for choice 3 was labelled "Twins (Recommended)". Its description read, word for word: "Keep the twin design and settle the dose question with the free real-word-splitter check before any rental." The question itself also told him that "the latest check found the twins still don't get an equal swap". So the premise that the dose question would be settled by the free check before any rental was put to him in those words. Section 10 of version 0.4, which the reviewer read, says it differently: "first estimated for free at step 3 and then measured on the model at step 4b". Even so, the reviewer is right on two points:
  - section 11's note quotes the premise in words that match neither text exactly;
  - the ruling file says each question "was put in the words shown in section 10", which is not accurate for the option descriptions.

  Both are to be corrected in version 0.7, by quoting the option description exactly and adding a dated note to the ruling file that leaves John's answers unchanged. The telling of 2026-11-21 is in the session's closing message after the fifth check and in the worklog entry "Loop removal test: the fifth check confirms the shared-context fix with the real tokeniser, but finds the free check can no longer settle the dose question".
- **RT-399, the capital count.** The author's figure of 82 of 105 came from the author's own list of 105 well-known capitals. The reviewer's list of 105 gave 71, and across all 193 it gave 90. The two lists differ, but the reviewer's point stands either way: half B cannot hold 55 single-token capitals from any real list.
- **Where things stand.** RT-390 and RT-394 to RT-397 close, some with conditions. RT-391 and RT-393 close in the design text, with conditions. RT-392 does not close, and its problem moves to RT-398. RT-345 stays open until step 4b. The reviewer finds version 0.6 one short revision from the battery specification. RT-398 (lookup's donors and size classes) and RT-399 (the single-token capitals) must be fixed first.
