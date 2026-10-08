# Ruling 2026-10-06: the twelve-page packet on the registration review of proposal version 4

*Recorded 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `rulings-2026-10-06-gate-a-v4`. **Authorship: mixed.** Every page,
recommendation and drafted text was proposed by Claude sessions; John ruled
each page himself, one page at a time, in a planning session on 2026-10-06,
and his answer to each page is quoted below in his own words. The choices are
his; none of the drafted wording is his. No compute was launched and no money
was spent: $0.*

*Written under the workspace plain-language rule. The session that recorded
this did not take part in the planning session. It has John's answers from
that session's word-for-word note, the same as the TimeAssembler decision
entry for that session ("Ruled: all twelve pages of the Gate A packet on
proposal version 4", entry `aa2a342f`). It wrote none of the packet, the
dispositions, the reviews or their checks.*

**What was ruled on.**

- **Pages 1 to 6**, the questions from the inside review of version 4 (the
  review's findings RT-237 to RT-246):
  `docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md` (pull
  request 95, checked in pull request 96). The drafted registration text for
  each is in `docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`,
  called **"the inside dispositions"** below.
- **Pages 7 to 12**, the questions from the two outside reviews (ChatGPT's
  findings A1 to A13, Gemini's G1 to G9):
  `docs/rulings/2026-10-04-successor-v4-gate-a-tier2-questions-PROPOSAL.md`
  (pull request 101, checked in pull request 102). The drafted text is in
  `docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`,
  called **"the outside dispositions"** below.

"Version 4" is `docs/successor-experiment-proposal-2026-10-03-v4.md`.
"Version 5" is the registration text still to be written from it. Line
numbers below are of the two dispositions files as merged on this branch.

**Three things about how this ruling was reached, stated so they are not
found later.**

1. The packet and both dispositions files were written by Claude sessions,
   and each was checked by a session that did not write it before John ruled
   (pull requests 96 and 102, and the re-check of the fixes on pull request
   102). The checks found defects; the fixed text is what was ruled on.
2. John ruled page by page, not with one "agreed on all". Pages 5 and 9 were
   taken together, as the packet asked.
3. **This record has not been checked.** Under the pairing rule of
   `docs/outside-review-protocol.md`, a session that did not write it checks
   it, and the dated notes it adds to earlier rulings, against the
   word-for-word note and the two dispositions files.

---

## What was ruled

### Page 1 — the free model's gate names "batteries" the task does not have (inside review, RT-237, fatal)

**Question.** The free model's channel-removal check ends with "the
ownership-free batteries must hold", but the successor's task has no
batteries; strike the clause, or replace it?

**John: "(a), go with the recommendation".**

**Adopted.** Option (a): the clause is replaced by a count the task can
evaluate. With the acting channel zeroed, the free model's own-directed answer
must still be the successor of one of the four agents' earlier values on the
item named, on **1,546 or more of the 3,000** held-out gate episodes, on two
seeds of three. The registered sentence says only what the check shows: **the
model still answers with the successor of a value it was shown.** It does not
show that the model still finds the right item; a model that had lost the item
would score about 2,257 and pass (the caveat found by the check in pull
request 96, section 6).

**Drafted text adopted:** the inside dispositions, RT-237, text changes 1 to 5
(lines 140 to 196). **Check owed:** the four-part measured check at lines 232
to 267, by a session that wrote neither the fix nor version 5.

**Amends** page 1h of the ruling of 2026-09-26
(`docs/rulings/2026-09-26-weekend-1-queue.md`), which wrote the batteries in;
it carries a dated note. The new line **sits beside** the collapse rule of
the Gate C ruling of the same day, RT-220
(`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`), and does not
amend it: RT-220 declined a second collapse threshold, and this is a
different condition, replacing page 1h's batteries. (RT-220 is amended by
page 7 only. Corrected 2026-10-06 after the check of this record, pull
request 104; the first version said page 1 amended RT-220.)

### Page 2 — a safeguard only in the code, and a wrong figure in an adopted sentence (inside review, RT-238 and RT-244)

**Question.** Should the floor's text carry the code's condition that the
requirement be above zero, and should the figure "0.11 or more" in the
competing-solver sentence be corrected?

**John: "yes, accept".**

**Adopted.** The floor's text gains the code's condition (the requirement on
the right must be above zero; where it is not, no site set is usable). The
competing-solver sentence is corrected to "0.109 or more above the
no-transplant formula and 0.091 or more outside the rule's allowance".

**Drafted text adopted:** the inside dispositions, RT-238 (lines 273 to 299)
and RT-244 (lines 572 to 584).

**Amends** the wording of ruling 2 of 2026-10-04
(`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`), which
carries a dated note.

### Page 3 — the episode format that keeps the model's own name out of the act (inside review, RT-239)

**Question.** Should the registration write down the exact episode format
instead of calling it an extension of the closed design's?

**John: "yes, accept".**

**Adopted.** The episode format is registered in full at the rehearsal's sizes
(four agents, two items, eight values, 56 tokens), with its two deliberate
departures from the closed design (no marker word of the model's own on the
action turn; the answer never shown), and the two self-tests that check them.
The closed design's twelve turns and batteries are not carried.

**Drafted text adopted:** the inside dispositions, RT-239 (lines 316 to 352).
Amends no earlier ruling.

### Page 4 — the episode counts at the registered width (inside review, RT-240)

**Question.** The ruled counts fit every read on 420 episodes, tried only at a
third of the registered width; keep them, or change them?

**John: "(a), go with the recommendation".**

**Adopted.** Option (a): every read is fitted on **1,800 development
episodes**, with the 180 held out kept (1,980 development episodes in all;
floor still 144 of 180) and the transplant passes still on 600 pairs. A new
weakness says 1,800 was chosen on a noise stand-in, not derived. **Option (c),
training a 448-wide stand-in on the laptop, was not taken.**

**Drafted text adopted:** the inside dispositions, RT-240, text changes 1 and
2 (lines 374 to 404). **Work owed before registration** (lines 406 to 411):
one $0 toy re-run of the nomination and reading with every read fitted on
1,800 episodes, method committed before output, run by a session other than
the one that drafted the dispositions, and checked by another.

**Amends** ruling 4 of 2026-10-03, late evening, for the read's fitting count
only, in both records of that ruling
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`, which stands, and
`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). Both carry
a dated note.

### Pages 5 and 9, ruled together — the outcome table and which outcome wins (inside review, RT-241; outside review, A10)

**Questions.** Page 5: some results the registered runs can reach have no
registered name; should one table name them all? Page 9, part 1: if the free
model passes its first run (step 5a) and then fails its learning gate at step
5b while the two built models separate, is that "substrate not a testbed"
(outcome R3) or the fifth term? Part 2: what if the middle model (arm M)
reads outside its predicted band?

**John: "accept all, go with the recommendations".**

**Adopted: page 5's outcome table as drafted, as changed by page 9.**

1. **Page 5, as drafted:** one table in section 3 of version 5, frozen in
   section 7.4. Arm M failing its gate drops arm M, as a no verdict on it
   already does. Three new registered terms, in the drafted words: **"metric
   checked against the separable model only, degree read"**; **"metric
   checked against the separable model only, degree not read"**, with the
   reason after a colon; and **"metric not validated"**, with the reason
   after a colon, not satisfactory. The one permitted re-run goes to the first
   registered run that fails its gate on learning: arm F at step 5a if it
   fails there; otherwise held for step 5b and given to the first failing run
   of arm T, C or M, on John's go naming it. *Drafted text:* the inside
   dispositions, RT-241, text changes 1 to 4 (lines 441 to 493).
2. **Page 9, part 1, changes page 5's rule 1:** if the free model passed at
   step 5a and then fails its gate at step 5b, with arms T and C learned and
   separated, the outcome is **"metric validated, degree not read: failed its
   gate on learning"**, not R3. **Step 5a and stop S4 are unchanged:** a
   failure at step 5a after its re-run is R3, and nothing else launches. This
   changes section 3's R3 and R2 rows, page 5's rule 1, page 5's change to
   section 8.1, the frozen code's outcome function, and version 4's toy
   sentence (under this rule the toy is the fifth term if its passing seed is
   taken as the step 5a run, R3 otherwise, and version 5 says so). *Drafted
   text:* the outside dispositions, A10, proposed rule 3 (lines 602 to 624)
   and text change 2 with its four matching changes (lines 641 to 660).
3. **Page 9, part 2:** if arm M reads outside 0.3 to 0.7, or more than 0.10
   from its true-slot reference, **no outcome term changes**. The report says
   so in the same sentence as the term, with the figures, and arm F's figure
   is placed against arms T and C only. *Drafted text:* the outside
   dispositions, A10, proposed rule 2 (lines 597 to 601) and text change 3
   (lines 662 to 665).

**Amends** the outcome list ruled on 2026-09-20 (section 2 of
`docs/december-result-roadmap-2026-09-20.md`: R3's "one or more arms" now
means arm T or C, or arm F at step 5a) and page 11 of the ruling of
2026-10-03 on what a no verdict maps to
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`). Both carry a dated
note. Page 9's split-seed half is page 7, below.

### Page 6 — four wording fixes (inside review, RT-242, RT-243, RT-245, RT-246)

**Question.** Accept the four wording fixes as drafted?

**John: "yes, accept all four and fold it in".**

**Adopted.** All four as drafted: one candidate's three seeds quoted as
such (RT-242, lines 532 to 536); the two forms of the floor said to disagree
where they do (RT-243, lines 545 to 564); the laptop timing cited and the
processor named for the whole nomination (RT-245, lines 597 to 617); the
competing-solver weakness stated with both halves (RT-246, lines 628 to 643),
all in the inside dispositions.

**"Fold it in"** refers to the page's small item: the review's test for the
known-failure list ("for every clause of every gate, name the field of a
committed rehearsal output file that evaluates it") is to be folded into the
drafted seventh entry of that list **when that entry is ruled**. That entry is
not ruled; nothing is added to the list now.

**Amends** ruling 7 of 2026-10-04 (RT-246, its wording) and the reach of
ruling 3 of 2026-10-03, late evening (RT-245: the processor now covers the
whole nomination and reading, not only the read's fit). Each carries a dated
note. See the second ambiguity under "What this record could not settle".

### Page 7 — split seeds (outside review, A10)

**Question.** When different seeds pass different conditions, does the arm
pass?

**John: "accept, go with the recommendation".**

**Adopted.** A seed counts only if it passes every gate condition and every
check that withholds a reading; an arm passes, or reads, only if two seeds
each do. Separate two-of-three counts per condition are not used. This closes
the frozen code's gap of 18 pass-or-fail patterns in which only one seed
passes everything and the arm still passes (measured by the check in pull
request 102). No toy verdict changes.

**Drafted text adopted:** the outside dispositions, A10, proposed rule 1
(lines 592 to 596) and text change 1 (lines 626 to 639), including the gate
rows of section 9.

**Amends** ruling 6 of 2026-10-03, late evening, in both records, and the
two-of-three collapse rule of the Gate C ruling of 2026-09-26, RT-220, which
is now counted on the same seeds as the other conditions. Each carries a
dated note.

### Page 8 — the no-transplant check (outside review, A9)

**Question.** The no-transplant check would refuse good models whose mistakes
go to other agents' values; keep it as a veto?

**John: "accept, go with the recommendation".**

**Adopted.** The no-transplant rate is **reported against the formula and no
longer refuses a reading.** The pairing is tested directly in the episode
generator's self-test, and **control 4** (the donor's states from before
either twin's own turn transplanted, output required to be bit-identical; it
already withholds a reading) is the registered check of the pairing. The
detection-margin sentence is kept in its replaced form, not dropped: the
chance that the formula would flag a broken pairing on 800 pairs is printed
beside the rate, about 56 per cent at the learning bar.

**Drafted text adopted:** the outside dispositions, A9 (lines 515 to 552).

**Amends** the Gate C ruling of 2026-09-26 on the allowance, RT-222, and
ruling 3 of 2026-10-04, which treated the formula as withholding. Each
carries a dated note.

### Page 10 — a $0 decoy test (outside review, A6)

**Question.** Should a $0 test check whether the read can be fooled by an
unused copy of the owner's marker before deciding to register?

**John: "yes, run it, go with the recommendation".**

**Adopted.** The decoy test runs: arm T's separable toy models with an exact,
unused copy of the owner's marker added, and the registered nomination and
reading run on them unchanged; **both ways round**, the copy at larger scale
than the slot and then at smaller scale, as fixed in its method before it
runs; method committed first; $0 on the laptop; checked by another session.
Page 12 is decided with its checked result. The wording changes A6 asks for go
into version 5 either way.

**Drafted text adopted:** the outside dispositions, A6, text changes 1 and 2
(lines 357 to 373) and the test as described at lines 375 to 397. Amends no
earlier ruling.

### Page 11 — the outcome words (outside review, A13)

**Question.** The outcome words claim more than the experiment shows; add a
fixed scope phrase, or rename the terms?

**John: "(a), go with the recommendation".**

**Adopted.** The ruled terms stay. Every use of "metric validated" carries,
in the same sentence, the fixed phrase **"on these constructed systems, for
this intervention procedure"**: in the registration, STATUS.md, the paper and
public writing. The reviewer's table of tempting summaries against what can
be said is registered in section 13, with control 6 added to its last row.

**Drafted text adopted:** the outside dispositions, A13, text changes 1 and 2
(lines 715 to 729). Amends no earlier ruling: the terms of 2026-10-03 are
kept, not renamed. See the third ambiguity below.

### Page 12 — the kill case (outside review)

**Question.** Is the narrow result the experiment can reach worth the
remaining spend?

**John: "decide after the decoy test, go with the recommendation".**

**Deferred to the decoy test.** No decision now. Continue, stop or redesign is
decided with the decoy test's checked result. The recommendation on the
record: if the read is fooled, stop or redesign before registration; if it is
not, continue.

---

## Outside findings adopted, with their ledger numbers

The outside dispositions (line 49) leave numbering to the session that records
the ruling, from RT-247 on, for outside findings John adopts. Those adopted by
a page above take these numbers in the red team ledger
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`):

| Ledger number | Outside finding | What it is | Page |
|---|---|---|---|
| RT-247 | A6 | A readable but unused copy of the owner's marker could make a separable model read as entangled | 10 |
| RT-248 | A9 | The no-transplant check refuses correctly paired, competent models | 8 |
| RT-249 | A10 | Split seeds, the middle model's missed band, and which outcome wins | 7 and 9 |
| RT-250 | A13 | The outcome words claim more than the experiment shows | 11 |

Outside findings that repeat inside ones (A1, A3, A4, A5, the first half of
A10, and Gemini's G1 to G9) take the inside finding's number, as the outside
dispositions dispose them (lines 84 to 104). **No ledger rows were written by
this session**; rows for RT-237 to RT-250 are owed, with the earlier rows
already listed as owed. *Later the same day, four more outside findings were
ruled and take RT-251 to RT-254, and one unlettered remark takes RT-255: see the addendum at the end of this file, "Follow-up, same day".*

---

## What this record could not settle from the word-for-word note

1. **Five outside findings no page put as a question, and the note has no
   answer for them.** The fatal finding A2 (the final decision procedure must
   be brought to these rulings and run on made-up failure cases) was put to
   John as a notice, "do that straight after you rule". The four wording fixes
   A7 (control 6 cannot tell "who is acting" from "the answer"), A8 (the toy
   is development evidence), A11 (no verdict is not absence) and A12 (the
   uncertainty is for the raw difference only) sat in the addendum's index as
   "accept all four as drafted", with no page of their own. **The note
   records no ruling on any of the five.** This record treats the A2 work as
   owed, because pages 5, 7, 8 and 9 cannot be registered without it, but
   gives none of the five a ledger number, and the four wording fixes need
   John's word before version 5 carries them. The same is true of one small
   item in the outside dispositions (lines 122 to 129: a line in the generator
   self-test asserting no fresh or relaxed combination occurs in training).
   **Now ruled, in part (2026-10-06, follow-up):** A7, A8, A11 and A12 are
   accepted as drafted and take RT-251 to RT-254. **A2 stays owed work**, with
   no ledger number (A2 was ruled later still, item 6 of the follow-up
   section, and takes RT-256). The generator self-test line was ruled later still (item
   4 of the follow-up section) and takes RT-255.
2. **Page 6's note says RT-245 and RT-246 amend wording ruled 2026-10-04.**
   RT-246 does (ruling 7 of 2026-10-04). RT-245 does not: the device it
   widens was ruled on 2026-10-03, late evening (ruling 3), and the
   2026-10-04 rulings say nothing about the device. This record notes RT-245
   beside ruling 3 of 2026-10-03. **Not put to John as a question. Left to
   the checker as housekeeping (2026-10-06, follow-up); John was told and did
   not object.**
3. **Page 11's scope phrase.** John's note names one phrase, for "metric
   validated". The drafted text he adopted by "go with the recommendation"
   also pairs "degree read" with a second phrase ("as a ratio of two
   transplants at the sites this procedure chose"), which the page itself did
   not show. Neither says whether the three new terms of page 5, all of which
   contain "metric", carry the phrase too. This record adopts the drafted text
   as written; the writer of version 5 should apply the phrase to every term
   containing "metric validated" and ask John about the other new terms.
   **Now ruled (2026-10-06, follow-up):** both phrases apply, and the three
   new terms containing "metric" carry the phrase too.
4. **Page 8's "control 4 ... is the registered pairing check".** The drafted
   text has two pairing checks: the generator's self-test and control 4. This
   record reads John's words as naming control 4 as the check that withholds,
   with the self-test kept as drafted. **Now ruled (2026-10-06, follow-up):**
   as read here.
5. **The word "restore" on page 8.** The drafted text does not drop the
   detection-margin sentence; it replaces it with the 56 per cent figure. This
   record reads "restore" as keeping that replacement. **Not put to John as
   a question. Left to the checker as housekeeping (2026-10-06, follow-up);
   John was told and did not object.**

---

## What is now owed before the registration commit, in the order things wait on each other

All at $0, on the laptop, with no new money. *Corrected 2026-10-06 after the
check of this record (pull request 104): page 1's closure check runs on the
registration text, so it now follows version 5; and items 3 and 4 proceed
now, alongside the decoy test, since they cost nothing and wait on nothing
but their own method notes. If John stops or redesigns after the decoy test,
their results are kept on the record and version 5 is not written as
planned.*

1. **The check of this record**, by a session that did not write it.
2. **The decoy test** (page 10), method committed first, both ways round,
   **and its check**. Then John decides page 12 with the checked result.
3. **The page 4 toy re-run** of the nomination and reading with every read
   fitted on 1,800 development episodes, method first, **and its check**.
4. **The A2 additions to `procedure.py` and `measure.py`** in
   `experiments/08-successor-degree/src/` (on main): the ruled outcome table;
   the seed rule of page 7 in one place; the ownership-free line; the
   no-transplant check moved from the vetoes to the reported fields; every
   reason listed and `arithmetic_withheld` removed from the summary file
   `summarise` writes (ruled by John in the follow-up, item 6); the
   freeze's self-test updated (the outside dispositions, A2, lines 247 to
   281). Then the run through `summarise` on the toy and the made-up failure
   cases, method first, **and its check** (lines 303 to 323).
   *Added 2026-10-06 after John's ruling in item 8 of the follow-up:* the
   frozen training code in `experiments/08-successor-degree` leaves fresh and
   relaxed pairings out of training outright, with a self-test asserting it,
   method first, then the self-tests re-run **and its check** (branch
   `training-exclusion-pairing`).
5. **Version 5**, the registration text, written with every change ruled here
   and earlier, **and checked** by a session that did not write it.
6. **Page 1's closure check**: the four-part measured check of the
   replacement clause, run on version 5 (the inside dispositions, lines 232
   to 267).
7. **The registration commit.** Outer limit: the first kill date, 2026-10-18.

---

## What this changes, and where

- **Dated notes** beside each amended earlier ruling, each left otherwise as
  written: page 1h of `docs/rulings/2026-09-26-weekend-1-queue.md`; RT-220 and
  RT-222 of `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`; page 11
  of `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`; rulings 3, 4
  and 6 of both 2026-10-03 records
  (`docs/rulings/2026-10-03-version-4-questions-rulings.md` and
  `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`); rulings
  2, 3 and 7 of `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`;
  and section 2 of `docs/december-result-roadmap-2026-09-20.md`.
- **A dated header line** on each of the two question packets and the two
  dispositions files, saying they were ruled on 2026-10-06 and pointing here.
  Their text is otherwise unchanged.
- **STATUS.md and `data/project.toml`**: a new top entry and the list of what
  is owed.

## What this file does not do

It releases no money and issues no go. It does not write version 5, edit
version 4, the reviews, the ledger, the known-failure list, the protocol or
the frozen code. It does not decide page 12.

---

## Follow-up, same day: the items this record listed as unruled

*Dated addendum, 2026-10-06 (Pacific), added on branch
`rulings-2026-10-06-addendum` for pull request 103. **Authorship: mixed.**
After this record listed what the word-for-word note left unruled, the
coordination session put three questions to John, and he answered in the
words **"accept all four, yes, yes"**. The questions and his answer are in the
"Follow-up, same day" section of the same word-for-word note. No compute was
launched and no money was spent: $0.*

1. **The four wording fixes from the outside review: "accept all four".**
   Accepted as drafted in the outside dispositions:
   - **A7**, control 6 cannot tell "who is acting" from "the answer": the
     claim that control 6 tells them apart is struck, its two cells are kept
     as description, and weakness W11 is retitled and rewritten (lines 426 to
     474).
   - **A8**, the toy runs are development evidence, not an untouched test of
     the final rule: one sentence in section 10 and weakness W5 (lines 478 to
     486).
   - **A11**, a no verdict does not mean the structure is absent: one
     paragraph in section 3 (lines 686 to 695).
   - **A12**, the registered uncertainty covers the raw difference only; the
     reading and the separation are labelled as descriptions with no
     registered uncertainty (lines 701 to 707).
2. **The scope phrases: "yes".** Both apply. "Metric validated" is followed in
   the same sentence by "on these constructed systems, for this intervention
   procedure", and "degree read" by "as a ratio of two transplants at the
   sites this procedure chose". **The three new terms of page 5, which all
   contain "metric", carry the first phrase too**: "metric checked against
   the separable model only, degree read", the same with "degree not read",
   and "metric not validated". This widens page 11 as drafted (lines 715 to
   729), which named only "metric validated".
3. **The pairing check: "yes".** Control 4 (the donor's states from before
   either twin's own turn transplanted, output required to be bit-identical)
   is the pairing check that withholds a reading. The generator's self-test
   on every matched pair is kept as a second check, as drafted under A9
   (lines 515 to 552).

**Ledger numbers**, continuing the table above, in the red team ledger
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`; rows still
owed, not written here):

| Ledger number | Outside finding | What it is |
|---|---|---|
| RT-251 | A7 | Control 6 cannot tell copying who is acting from copying the answer |
| RT-252 | A8 | The toy runs are development evidence |
| RT-253 | A11 | A no verdict is not evidence of absence |
| RT-254 | A12 | The registered uncertainty belongs to the raw difference only |
| RT-255 | the ChatGPT review's feasibility table, unlettered remark on control 5 | Different random seeds alone do not show that unseen combinations never appear in training |

4. **The generator self-test on unseen combinations: "yes to the self-test,
   go with the recommendation".** Ruled later the same day, in John's words
   as quoted, and recorded in the word-for-word note's follow-up section.
   Adopted as the outside dispositions draft it (lines 122 to 129): one line
   added to the registered generator's self-test at section 11, step 3,
   asserting that no fresh or relaxed episode's combination occurs in the
   training stream, with its output cited in version 5. It answers an
   unlettered remark in the ChatGPT review's feasibility table, numbered
   RT-255 above. (The note's summary says "fresh episode"; the drafted text
   John adopted says "fresh or relaxed", and that is what is recorded.)
5. **The two recording readings** (that RT-245 amends the device ruling of
   2026-10-03, not one of 2026-10-04; and that "restore" on page 8 means
   keeping the drafted 56 per cent sentence) were left to the checker as
   housekeeping, as the planning session framed them. John was told and did
   not object.

6. **The fatal finding on the decision procedure (A2): "yes, remove".**
   Ruled later the same day, recorded in the word-for-word note. John was
   asked whether to accept the finding as drafted, and whether to remove the
   withheld figure (`arithmetic_withheld`) from the decision code's output or
   keep it under one named field. **Accepted as drafted** (outside
   dispositions, A2, lines 158 to 333): the frozen decision code
   (`procedure.py` and `measure.py` in `experiments/08-successor-degree/src/`,
   on main) is brought to the ruled rules (the item list at lines 247 to
   281); it is run end to end on the toy and on made-up failure cases, method
   first; a session that wrote neither the code nor its run checks it (lines
   303 to 323); and version 5 carries the item "R-13. The final decision
   procedure, run end to end before registration" (lines 283 to 301).
   **The withheld figure is removed** from the output file, not kept under a
   named field. The work itself is item 4 of the owed list above and is still
   to be done.

| Ledger number | Outside finding | What it is |
|---|---|---|
| RT-256 | A2 (fatal) | The final decision procedure that withholds bad readings and assigns the outcome had not run end to end on the rules as ruled |

7. **Two refinements: "yes, stricter, go with the recommendation".** Ruled
   later the same day (TimeAssembler decision entry `f4aa2083`). Both refine
   items already numbered, so neither takes a new ledger number.
   - **R2, "metric does not separate", also carries the scope phrase** "on
     these constructed systems, for this intervention procedure", in the same
     sentence, as "metric validated" and the three new terms do (refines
     page 11, RT-250, and item 2 above).
   - **The generator self-test on unseen combinations (RT-255, item 4 above)
     takes the stricter reading:** it checks the specific pairing that makes
     an episode fresh or relaxed, not only the whole episode's content, and
     asserts that no such pairing occurs in the training stream. It is the
     stricter reading because an overlap on that pairing alone would have
     passed the self-test as built.
   - Both were raised by the independent check of the decision-code work
     (pull request 107, checking pull request 105).

8. **How training keeps those pairings out: "(a), go with the
   recommendation".** Ruled later the same day (TimeAssembler decision entry
   `9fbca0db`). After item 7, the re-check of the decision-code work (pull
   request 107, at commit `d776c70`) found that the self-test samples only
   200 training steps, so it cannot promise the registered claim that no
   fresh or relaxed pairing "occurs in the training stream". John was offered
   three options: (a) change training to leave those pairings out outright, a
   small change to the frozen training code, $0, with the frozen code
   re-tested; (b) check every training step in full; (c) reword the claim to
   "in a sample of 200 steps". **Chosen: (a).**
   - **Owed:** in `experiments/08-successor-degree`, the exclusion changes
     from whole episode content to the pairing of marker, item and value,
     with a self-test asserting it; the method committed first; then the
     self-tests re-run and an independent check, all before registration.
   - **The four 10-million development runs** used the old exclusion. They
     are development evidence only and need no re-run.
   - That work is being done separately, on branch
     `training-exclusion-pairing`. This record does not do it.

**Nothing from the packet or its follow-ups is now unruled**, except page 12,
which waits on the decoy test.

This addendum, like the rest of the file, is owed a check by a session that
did not write it.
