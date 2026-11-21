*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the six earlier reviews. It worked read-only in a detached worktree at commit 8a5aabb, using only its own scratch folder, which was created empty for it. It changed nothing in the repository. It also read two TimeAssembler worklog entries through the v1 API, read-only, to check what section 11 cites. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.7

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or any of the six earlier reviews. I worked read-only in the detached worktree `closure7-loop-design-2026-11-21` at commit 8a5aabb and changed nothing in it. I used only my own scratch folder, `/private/tmp/claude-501/loop-review7-CodRDC`, which was empty when I started. Every script and every output is in that folder. I opened no other scratchpad or temporary folder, including the author's session scratchpad and every earlier `loop-review*` folder. I downloaded nothing, installed nothing and spent nothing. New findings continue the red-team numbering from RT-403.*

---

**What I opened.**
- **Read in full:**
  - the closure check of version 0.6, `docs/reviews/2026-11-21-loop-removal-test-design-v0.6-closure-check-claude-code.md`. I treated its filer's check as the author's note, not as part of the review, and used it only for the words John was shown on choice 3;
  - John's rulings, `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`, including the new dated note;
  - `git diff 5bc172a 8a5aabb` on the design and on the ruling file;
  - the design's sections 3 and 5, the "depends on one kind" rule in section 6, sections 9 and 11, and the sixth change log;
  - the tokeniser download record, `docs/2026-11-21-loop-removal-tokeniser-download.md`.
- **Read in part:**
  - `docs/outside-review-protocol.md`: the tier 1 description and "The closure rule, which is the new part";
  - `experiments/09-split-removal-test/src/batteries.py`, its first 120 lines (the pools and the invented syllables);
  - section 10 of version 0.4 (`git show ddc5031`), to check what the ruling file and section 11 say John was shown;
  - the research model's `chat_template.jinja` and `REVISION` (657b53ba…).
- **Read outside the repository:** two TimeAssembler worklog entries, read through the v1 API with the workspace key. They were the decision entry "John rules the loop removal test's five choices, and paper work only for now (2026-11-21)" and the progress entry "Loop removal test: the fifth check confirms the shared-context fix with the real tokeniser, but finds the free check can no longer settle the dose question". I read them to check what section 11 and the ruling file's dated note cite.
- **Ran** these scripts with the research model's real tokeniser, loaded through `tokenizers.Tokenizer.from_file`, under the project Python with `-I`. I rendered the chat template in jinja2's sandboxed environment, with the reasoning setting "none". All scripts are in my scratch folder:
  - `single.py`: single-token counts and the opposites and products pools;
  - `gen.py` and `run.py`: my stand-in pair builder under version 0.7, the donor counts and the dose ratio;
  - `starved.py`: which scored pairs are left with no donor;
  - `feas.py`: whether the pairing exclusions and the 25% cap allow a given number of pairs.

**What I did not open.** I did not open:
- the earlier reviews other than the closure check of version 0.6;
- the committed pilot battery files;
- the three-hypotheses proposal and the design note;
- any external web page;
- any scratchpad except my own.

**What is real and what is a stand-in.**
- **Real:** the tokeniser and the chat template. Every token count and length below comes from them.
- **Stand-ins, written by me because the battery specification does not exist yet:**
  - every content pool: 193 UN member countries with capitals and a coarse region tag of my own, 99 opposite pairs (78 after removing words that belong to two pairs), 126 everyday objects with colours, and 253 three-letter words;
  - the rule wordings and operand ranges;
  - how pools are split into halves;
  - how pairs are allocated to pairings. I used a flow calculation that respects the exclusions and the 25% cap;
  - the opening of the model's reply. I assumed `<|message_model|><|content_text|>`, which step 4a has not yet settled.
- **The dose is a proxy.** It is the step-3 measure. Starting at the first position where recipient and donor differ, each position counts 1 if its token differs from the donor's token at the same place, and 0, 0.3 or 0.6 if the token is the same. It is not a measurement on the model.
- **A donor is eligible** when both of its twins are at least as long as the matching recipient's prompt, and when neither of its right answers is among the recipient's candidates.

---

## Verdicts

| Item | Verdict | Label |
|---|---|---|
| RT-345 (fatal), the swap's dose differed between the two task groups | **Not closed, and it cannot be closed on paper.** It is owed at step 4b. The stand-in still passes by construction, at 0.997 to 1.001, with or without donor-only pairs | MEASURED (proxy); ARGUED for what remains |
| RT-398, lookup's donors and size classes | **Closed, with conditions** (RT-403, RT-404) | MEASURED |
| RT-399, single-token capitals | **Closed, with conditions** (RT-407, RT-408) | MEASURED |
| RT-400, the space before the answer | **Closed** | MEASURED (counts); ARGUED (rule) |
| RT-401, the section 11 note | **Closed, with a condition** (RT-405) | ARGUED (record) |
| RT-402, the baseline checks' calibration | **Closed, with conditions** | ARGUED |
| RT-390 condition, the "correct build" range | **Closed** | MEASURED |
| RT-394 condition, the order of the context's parts | **Closed** | ARGUED (text); MEASURED (dose with donors of either order) |
| RT-395 condition, the reverse copying rule | **Closed** | ARGUED |
| RT-396 condition, capitals without four close wrong answers | **Closed, with a condition** | MEASURED (stand-in) |

### RT-398, lookup's donors and size classes: closed, with conditions (MEASURED, stand-in)

**The text.** Section 3 now has six-entry tables at the pilot and the test, and the size classes are withdrawn. Donor-only pairs are added to a group until every scored pair has at least five eligible donors, or until the group holds three times as many donor-only pairs as scored ones. Donors are counted and reported.

**What I measured.** I ran `run.py pilot|200|300 reuse` at seeds 1 to 3. In this run, donor-only pairs may reuse routine questions (see RT-403).

```
pilot (120 pairs, half A)                lookup, scored pairs only    lookup, with donor-only pairs
  no donor (of 30)                         6 / 5 / 4                    1 / 1 / 3
  fewer than five donors (of 30)           28 / 30 / 28                 7 / 8 / 6
  mean eligible donors                     1.8 / 1.9 / 1.9              8.0 / 7.0 / 8.4
  donor-only pairs added, lookup            -                           81 / 90 / 90   (the cap is 90)
  other rule kinds with donor-only pairs: no donor 0 to 2 of 30; fewer than five 0 to 6 of 30
  donor-only pairs added, all kinds: 258 / 320 / 259, for 120 scored pairs
200 pairs (half B): lookup no donor 4 / 2 / 3 -> 2 / 0 / 1; fewer than five 23 / 26 / 23 -> 13 / 5 / 3;
  donor-only pairs added, all kinds: 504 / 568 / 507
300 pairs (half B, the two stand-in splits where 300 fits at all): lookup no donor 5 / 4 -> 0 / 1;
  donor-only pairs added: 541 / 632
```

- **Result.** Donor-only pairs cut lookup's starved pilot pairs from about 5 of 30 to about 2, and they raise its mean donor count from about 2 to about 8. That is what RT-398 asked for.
- **But two conditions.** The fix works only if donor-only pairs may reuse routine questions (RT-403). The pairs it still leaves without donors are almost always the longest pair of their group (RT-404).
- **The pilot now rehearses the test's lookup items.** Both use six-entry tables (ARGUED from the text).

### RT-345: the stand-in dose under version 0.7 (MEASURED, proxy)

The ratio is the routine cell's dose divided by the prompt-rule cell's, at weights 0, 0.3 and 0.6, per rule kind, from `run.py`:

```
pilot, scored pairs only      0.9974 to 1.0000
pilot, with donor-only pairs  0.9981 to 1.0005
200,   scored only / with     0.9981 to 1.0000 / 0.9979 to 1.0000
300,   scored only / with     0.9984 to 1.0002 / 0.9990 to 1.0000
```

- **Donor-only pairs do not change the ratio.** Every rule kind stays within 0.997 to 1.001, which is well inside the step-3 band.
- **That is expected.** A donor-only pair, like any donor, supplies both twins as a whole pair, so it reaches both cells alike.
- **RT-345 stays open.** Its remaining risk lies in the final question and the answer, which only the model can measure (step 4b).

### Single-token counts (MEASURED, real tokeniser; stand-in lists)

```
python3 -I single.py
capitals, 193 countries: one token at the answer position 90; with a leading space 23
barred by the copying rule: Djibouti, Bissau, Luxembourg, Monaco, Singapore, Tunis -> 84 kept
kept by region: Europe 32/43, Middle East 14/19, Asia 13/29, Africa 13/53, South America 6/12,
  Caribbean 2/13, Central America 1/7, Oceania 1/14
half B over 20 random splits: 36 to 50 single-token capitals, median 43
opposites: 78 unambiguous pairs, 156 questions; answer one token 131 (84%); 12 more barred by the copying rule
  (happy/unhappy, possible/impossible and the like)
products, half B (answer 40 or more): 64 ordered pairs, 35 unordered, 31 distinct answers
colours all one token; three-letter words 252 of 253; numbers 0 to 999 one token, 1000 two tokens
```

- **The capitals figures reproduce.** There are 90 single-token capitals, 84 after the copying rule, and about 42 in half B. The words "about 42" are right, but the split alone moves this between 36 and 50.
- **"About 70 opposites" is reachable only with a careful list.** My list gives about 58 per half. One reason is that it holds prefix opposites ("unhappy"), which the copying rule bars. The other is words that sit in two pairs ("light" is the opposite of both "dark" and "heavy").
- **"60 products" counts both orders of the same multiplication.** Half B has only 35 different multiplications, with 31 different answers (RT-407).

### Whether the exclusions and the 25% cap allow the expected sizes (MEASURED)

```
python3 -I feas.py
design's own half-B figures (75 / 60 / 42 / 70 / 60 = 307): largest feasible test size 307; 300 fits
  same, capitals 36: 301        capitals 50: 315        products counted once per multiplication (35): 273
stand-in pools, 10 splits: largest feasible size 286 to 316; 200 fits in every split; 300 fails in 3 of 10
```

- **120 to 200 pairs is safe.** Every split allows it.
- **300 pairs has no slack.** It fails in 3 of 10 of my splits. It fails outright if each multiplication counts once.

### RT-399, single-token capitals: closed, with conditions (MEASURED)

- **What is fixed.** The figures are corrected to about 42 and about 307. The cost is stated, and capitals are kept with reporting by region.
- **The operator kind's range is stated.** Every operator answer and candidate lies between 0 and 999, which my count confirms is what single-token numbers allow.
- **The conditions:**
  - the opposites list must avoid prefix opposites and words that belong to two pairs;
  - the products count needs a stated rule (RT-407);
  - the cost statement should say which way the cost points (RT-408).

### RT-400, the space before the answer: closed (MEASURED counts, ARGUED rule)

With a leading space, 23 capitals are one token and no number is, which matches the design. Section 5 now says that the pools, the pilot and the counts are rebuilt before any pilot item is scored if step 4a finds different tokens before the answer. That answers the finding.

### RT-401, the section 11 note: closed, with a condition (ARGUED from the record)

**What is fixed.**
- Section 11 now quotes both texts separately: the option John picked, and section 10's sentence.
- It cites the worklog entry.
- The ruling file has a dated note at its end.

**I checked the ruling file with `git diff 5bc172a 8a5aabb`: 19 lines added and none removed.** So John's answers are unchanged.

**I also checked the cited worklog entry.** It exists under the exact title cited.

**The condition is RT-405.**
- The dated note says one thing that the record contradicts.
- The exact wording of the option rests only on the author's own account.

### RT-402, the baseline checks: closed, with conditions (ARGUED)

**What is fixed.**
- Both checks are now one-sided: they fail only when the full context lowers the margin by more than 1.0.
- The mirror check's rules are written out.
- Strike counts per pairing are reported before the pairing table is fixed.
- The trigger for returning to John is stated: fewer than three rule kinds left, or a rule kind left with only one routine kind.

**Two gaps remain:**
- **What "a fifth" is counted from.** The text does not say whether a fifth means a fifth of all pilot pairs in the pairing, or of those that pass the confidence check. Margin matching says the second, and the two baseline checks should say the same.
- **A rule kind left with no routine kind.** The trigger names a rule kind left with only one routine kind. It should also name a rule kind left with none, which is plainly meant but not written.

### The conditions on RT-390, RT-394, RT-395 and RT-396

- **RT-390 (MEASURED).** Section 9 now reads "about 0.99 to 1.03". My correct builds give 0.997 to 1.001, which lies inside that range. Closed.
- **RT-394.** Three things are now in section 5: results by order are a report only and rename nothing; the extra pair of an odd group gets its order from the seed; and donors need not share the order. My builds draw donors of either order and give the ratios above. Closed.
- **RT-395 (ARGUED).** The prompt-rule item's right answer is now never one of the routine twin's candidates, so "red" and "tan" are covered. Closed.
- **RT-396 (MEASURED, stand-in).** The rule now falls back from the same region to the nearest neighbouring region, and drops an item only after that. The condition is about how "region" is drawn:
  - with my coarse continental regions, a median of 39 of 43 half-B capitals have four same-region single-token alternatives, and 40 of 43 have them once the nearest region is included;
  - the sixth check, with its own regions, found about half.

  So the share that falls back or is dropped depends entirely on the region map. The text's "about half" is one reviewer's figure, not a property of the design. **Condition:** the battery specification writes out the region map and the neighbouring regions before any item exists.

---

## Press on what version 0.7 changes (item 3 of the brief)

- **Donor-only pairs and differences between the cells (MEASURED).** They introduce none:
  - each donor-only pair is a whole pair, built from one shared context, and it serves both twins of its recipient;
  - the dose ratio is unchanged when they are added (above).
- **Donor-only pairs and pilot-test leakage (ARGUED).** No new route opens, as long as two things hold:
  - donor-only pairs are drawn from the same half, as the text says;
  - the overlap script counts them as part of the set they serve.

  The script's text names only "the test set" and "pilot prompts". It should say that donor-only pairs are included on both sides.
- **Is their cost small? Yes, but the sentence is wrong in its detail (MEASURED count, ARGUED cost).**
  - Each donor-only pair needs two unaltered runs, one per twin, not one.
  - My builds add about 2.1 to 2.8 donor-only pairs per scored pair, so about five extra unaltered runs per scored pair. Against roughly a hundred runs per scored pair for its own conditions, that is about 5%: unaltered, five swaps, the average, 20 random draws, 20 outside-the-loop draws, two with fewer passes, and the baseline variants, for each twin.
  - The block sums of each donor run must also be stored. That is about 1.7 MB per run at 16 bits for two sums, two passes and about 90 positions, or about 2.5 GB at 300 pairs.
  - The text should give the multiplier and the storage.
- **The one-sided checks and the strike rule.** They are well defined, apart from the two gaps under RT-402 above.
- **The cost of famous capitals (ARGUED; RT-408).** The statement is honest about the skew, but it does not say which way the skew pushes the result. The safeguards are also weaker than they read.
- **The section 11 note and the ruling file's dated note.** Both now quote the option and section 10 separately, and John's answers are unchanged (MEASURED by diff). One sentence in the dated note does not match the record (RT-405).
- **Rules stated only in a change log, or contradicted between sections (MEASURED by grep).** I found no rule that lives only in a change log. I found one contradiction between sections and some stale text (RT-406).

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-403 | Whether donor-only pairs may reuse routine questions is not stated. Under the "no routine question is used twice" rule, they cannot be built where they are needed, and the fix for RT-398 fails | serious | MEASURED (stand-in) |
| RT-404 | Donor-only pairs cannot reach the longest scored pair of a group. The pairs still left without donors are almost all the longest of their group, and most groups hit the threefold cap | worth-noting | MEASURED (stand-in) |
| RT-405 | The ruling file's dated note says the questions were put in section 10's words, which the record contradicts. The option's exact wording rests only on the author's account | worth-noting | ARGUED (record) |
| RT-406 | Section 5 still says lookup tables have "five to seven entries". Section 9 still names the fifth check's findings and figures | worth-noting | MEASURED (grep) |
| RT-407 | The 307 figure counts both orders of each multiplication. Counted once, the ceiling is about 273. 300 pairs has no slack | worth-noting | MEASURED |
| RT-408 | The capitals cost does not say that it pushes toward outcome A (the predicted pattern), and two of its three safeguards do not address the recognition worry | worth-noting | ARGUED |

**RT-403, donor-only pairs and the no-reuse rule (serious, MEASURED, stand-in).**
- **The gap.** Section 5 says that no routine question is used twice, and section 3 says that donor-only pairs are "built exactly like scored pairs". Nothing says whether a donor-only pair may reuse a routine question (a country, an adjective, an object, a multiplication) that a scored pair or another donor-only pair already uses.
- **What happens under the strict reading.** I ran `run.py pilot|200 noreuse`:
  - at the pilot, the capitals, colours and opposites groups ran out of unused questions with no donor-only pair added;
  - lookup was left with 4, 0 and 4 of 30 pairs with no donor and 13 to 18 of 30 with fewer than five, little better than before the fix;
  - at 200 pairs, lookup still had 4 of about 48 pairs with no donor and 28 to 30 with fewer than five.
- **What happens under the loose reading.** Reuse is harmless:
  - a donor-only pair that repeats a recipient's routine question has the recipient's right answer, so the existing donor-answer rule already bars it as that recipient's donor;
  - donor-only pairs are never scored, so reuse adds no repeated item to either cell.
- **Fix.** State that donor-only pairs may reuse routine questions and prompt-rule content from their own half. State that they sit outside the 307 budget, the 25% cap and the "no routine question used twice" rule. State that the overlap script includes them.

**RT-404, the longest pairs (worth-noting, MEASURED, stand-in).**

```
python3 -I starved.py      (10 seeds each)
pilot: 82 of 120 groups hit the threefold cap; 2.52 donor-only pairs per scored pair;
       2.4 scored pairs per build left with no donor; 21 of 24 were the longest in their group, all 24 among the two longest
200:   89 of 131 groups hit the cap; 2.46 per scored pair; 2.5 left with no donor per build; 23 of 25 the longest
```

- **Why this happens.** A random new pair is rarely longer than the longest of 6 to 35 scored pairs in both twins, so the cap is reached first.
- **Why it matters.** The drops fall systematically on the longest items. For example, these are lookup tables with long invented words, or long country names. That is the pattern the withdrawn size classes were meant to avoid.
- **The cost is small.** It comes to two or three pairs per build, dropped whole and counted.
- **Fix.** Either let the generator keep only donor-only pairs that are eligible for a scored pair still short of five, or state plainly that the longest pairs are the ones dropped and report their content.

**RT-405, the dated note and the record (worth-noting, ARGUED).**
- **What the note says.** The ruling file's dated note says that each question "was put in the words shown in section 10", and that this "is true of the questions".
- **What the record says.**
  - The ruling's own body records that John "was also told that the latest check found the twins still do not get an equal swap".
  - The decision worklog entry records the same.
  - The filer's check quotes it as words in the question itself.
  - Section 10 of version 0.4 (`ddc5031`) says nothing of the kind. It says that the closure check of version 0.3 "forecast" a failure without the change.

  So the question for choice 3 was also not in section 10's words.
- **The source of the option wording.** The exact option wording ("Keep the twin design and settle the dose question with the free real-word-splitter check before any rental") is quoted in section 11 and in the dated note. It comes only from the author's account in the filer's check. No committed file or worklog entry that I could open records it.
- **What the cited worklog entry holds.** The fifth-check worklog entry records the finding that contradicts the premise. It does not itself record that John was told.
- **Fix:**
  - correct "That is true of the questions" to say that the question text in the form also differed from section 10;
  - name the source of the quoted option wording, the session's question form as the author reports it;
  - say that the worklog entry records the finding.

  John's answers need no change.

**RT-406, stale text and one contradiction (worth-noting, MEASURED by grep).**
- **The contradiction.** Section 5 (line 345) still says the lookup table "has five to seven entries". That contradicts section 3's six entries everywhere.
- **Stale text in section 9:**
  - step 1 still describes checking "the fifth check's findings (RT-390 to RT-397)";
  - step 2 still has John ruling on section 10, which he has done;
  - step 3 still quotes "about 30% for the unit kind to 63% for the lookup kind". The sixth check gave 30% to 54% for six-entry tables.
- **The sixth change log's header.** It names the replaced rules of the fifth change log. But the size classes in the version 0.5 change log (RT-388) and "five to seven entries" in the version 0.4 change log (RT-377) are not marked as replaced.

**RT-407, the pool arithmetic (worth-noting, MEASURED).**
- **The products count.** Half B's "60 products" is reached only by counting "5 and 8" and "8 and 5" as different questions. There are 35 different multiplications, with 31 different answers.
- **What happens if each multiplication counts once.** The pairing exclusions and the cap then allow at most about 273 pairs.
- **The stand-in splits.** Under my splits, 300 pairs fails in 3 of 10, while 120 to 200 holds in all.
- **Fix.** State whether both orders count as separate questions, and give the ceiling as "about 270 to 307, depending on that and on the split". The expected 120 to 200 is unaffected.

**RT-408, what the capitals cost points toward (worth-noting, ARGUED).**
- **The direction.** Famous capitals among famous wrong answers can be recognised after they could no longer be produced. That holds routine losses down, which widens the gap the test reads in the direction of outcome A, the predicted result. The text should say so.
- **The safeguards:**
  - **Margin matching** acts on baseline margins, not on recognition after the removal, and it is capped at a third of a kind. So it does not answer this worry.
  - **The capitals-out reading** is real: section 6 renames an A when leaving capitals out lands in a different definite outcome. But it does not rename when the reading lands in E.
  - **The report by region** is description only.
- **Fix.** State the direction. Describe margin matching as unrelated to this worry. Report any A beside its capitals-out reading, whatever that reading lands in.

---

## Verdict

**Version 0.7 is ready for the battery specification at step 3 once one sentence of rule is added, with RT-345 (the finding that the swap's dose differed between the two task groups) carried as an open fatal item, which only step 4b on a rented machine can close.**

- **What holds, measured with the real tokeniser and my stand-in build:**
  - one six-entry table size, with donor-only pairs, lifts lookup's pilot donors from about 2 to about 8 per pair and cuts its starved pairs from about 5 of 30 to about 2;
  - the stand-in dose ratio stays within 0.997 to 1.001 in every rule kind at 120, 200 and 300 pairs, with or without donor-only pairs;
  - the capitals counts (90, 84, about 42) reproduce;
  - 120 to 200 pairs fits the pairing exclusions and the 25% cap in every split I tried.
- **What must be fixed first:** RT-403. The design must say that donor-only pairs may reuse routine questions and sit outside the no-reuse rule, the pool budget and the cap. Under the strict reading, the RT-398 fix fails at the pilot.
- **What can go with the specification:**
  - RT-404 to RT-408;
  - the two gaps on RT-402;
  - the region map that RT-396 needs;
  - correcting the two-runs and storage detail of the cost sentence.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **RT-406, the stale lookup sentence.** Confirmed. Section 5 (line 345) still says the lookup table "has five to seven entries", against section 3's six entries everywhere.
- **RT-405, where the option's exact wording is recorded.** The reviewer is right that no committed file or worklog entry records the wording, apart from the author's own account. The wording comes from the session in which John ruled, on 2026-11-21. In that session, the question form the author put to him carried each option's label and description, and the form returned John's picks. That session transcript is the primary record. It is not in the repository. Version 0.8 should say so, and should correct "That is true of the questions" as the reviewer asks. The reviewer is also right on a second point: the question text for choice 3 itself included the sentence about the latest check, which section 10 of version 0.4 did not contain.
- **Where things stand.** RT-398 to RT-402 close, with conditions, and so do the four conditions carried from the sixth check. RT-345 stays open until step 4b. The reviewer finds version 0.7 ready for the battery specification once one rule is added (RT-403: donor-only pairs may reuse routine questions, and sit outside the no-reuse rule, the pool budget and the cap). RT-404 to RT-408 can go with the specification.
