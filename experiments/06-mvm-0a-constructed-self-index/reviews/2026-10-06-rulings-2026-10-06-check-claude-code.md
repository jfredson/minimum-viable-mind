# Check of the record of John's rulings of 2026-10-06 on the twelve-page registration-review packet

*Written 2026-10-06 (Pacific) by a Claude Code checking session, on branch
`check-rulings-2026-10-06`, cut from `rulings-2026-10-06-gate-a-v4` at
`ccd3341` (pull request 103). Written under the workspace plain-language rule.
Nothing was rented, trained or spent: $0. This file edits no ruling, packet,
proposal, registered text or protocol text.*

**What was checked.** The record,
`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`, and everything else
the commit `ccd3341` changed: eleven dated notes beside earlier rulings, the
"ruled" header line on the two question packets and the two dispositions
files, the new top entry of `STATUS.md`, and `data/project.toml`.

**What it was checked against.** John's words come from two places, both
written by the planning session in which he ruled, which this session did not
take part in:

- the planning session's word-for-word note,
  `mvm-rulings-2026-10-06.md` in that session's scratch folder (not in the
  repository); and
- the TimeAssembler decision entry "Ruled: all twelve pages of the Gate A
  packet on proposal version 4" (entry `aa2a342f`), whose body agrees with the
  note page for page.

The drafted text John adopted is in the two dispositions files: the inside
dispositions (`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`)
and the outside dispositions
(`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`),
with the two question packets beside them. Every line number below is of
those files at `ccd3341`, which is how the record counts them (the new
two-line header is included).

**A follow-up after the record was written.** After the record listed what
John's note left open, the planning session put those items to him, and the
note gained a "Follow-up, same day" section. His words: **"accept all four,
yes, yes"**, meaning the four outside wording fixes (control 6 cannot tell who
is acting from the answer, A7; the toy is development evidence, A8; no verdict
is not absence, A11; the uncertainty belongs to the raw difference only, A12)
are accepted as drafted; both scope phrases apply, including to the three new
terms that contain "metric"; and control 4 is the pairing check that withholds
a reading, with the generator's self-test kept as a second check. These were
**ruled after the record was written**. They are not defects in what it
recorded at the time; the record needs one dated addendum carrying them
(section 6). The author of pull request 103 is adding it.

Findings are marked **MEASURED** (a file and line were opened, or a command
was run) or **ARGUED**.

## 1. The short version

| Check | Verdict |
|---|---|
| 1. John's words and what was adopted, page by page | **Pass.** All eleven quotations match the note word for word. No page is recorded as stronger or broader than his words. Every line-range pointer lands on the drafted text it names |
| 2. The amendments to earlier rulings | **Pass, with one wording defect.** Of the four the note did not name, three are real consequences of what John ruled. The fourth (page 1 "amending" the collapse rule of the 2026-09-26 Gate C ruling) is not an amendment, and its note misdescribes what that ruling declined. Nothing needs John's word |
| 3. The dated notes | **Pass.** Lines only added, each beside the ruling it names, each saying the ruling is left as written. One note carries the wording defect of check 2 |
| 4. STATUS.md, project.toml and the three scripts | **Pass, with two small defects.** The order of owed work puts page 1's closure check before the text it checks; and the owed list decides a choice the outside dispositions left to John (removing the withheld figure from the output). The site exporter passes; the citation and single-source checkers add nothing new except references to frozen code that is on main and not on this branch |
| 5. The record's list of what it could not settle | **Pass.** Each item is flagged in plain words and none is silently decided in the record itself. Four were then ruled in the follow-up; two remain (section 7) |

## 2. Check 1: John's words, and what each page records

**John's words (MEASURED).** A script extracted every `John: "…"` from the
note and every `**John: "…"**` from the record and compared them in order.
All eleven page answers are identical, character for character. (The note's
twelfth quotation is the follow-up's, which postdates the record.)

**Page by page.** For each page: what John's note says, what the record says
was adopted, where the pointer lands, and whether the record says more than
his words.

| Page | Note | Record | Pointer lands on | Stronger or broader? |
|---|---|---|---|---|
| 1, the battery clause (RT-237, the inside review's fatal finding) | (a); the in-range count, 1,546 of 3,000, two seeds of three; the sentence claims only "answers with the successor of a value it was shown" | Same, with the 2,257 caveat | Text changes 1 to 5, lines 140 to 196: yes. The four-part check, lines 232 to 267: yes | No |
| 2, the floor's missing safeguard and the "0.11" figure (RT-238, RT-244) | Accept; positive-room condition; 0.109 and 0.091 | Same | Lines 273 to 299 (the floor) and 572 to 584 (the sentence): yes | No |
| 3, the episode format (RT-239) | Accept; rehearsal sizes; two departures; two self-tests; closed design not carried | Same | Lines 316 to 352: yes | No |
| 4, the fitting count (RT-240) | (a); 1,800 fitted, 180 held out, 600 transplant pairs; one $0 toy re-run, method first, checked; no 448-wide training | Same, plus the new weakness the drafted text adds | Text changes, lines 374 to 404; work owed, lines 406 to 411: yes | No |
| 5 and 9, the outcome table and which outcome wins (RT-241, A10) | Accept all; the table as drafted; arm M's gate failure drops it; the three new terms in the drafted words; the re-run allocation; a step 5b failure of the free model is the fifth term "failed its gate on learning"; step 5a and stop S4 unchanged; arm M's miss changes no term | Same, in three numbered parts | Table and rules, lines 441 to 493; page 9's rule 3, lines 602 to 624; its text change 2 and four matching changes, lines 641 to 660; rule 2, lines 597 to 601; text change 3, lines 662 to 665: all yes | No. The record says "with arms T and C learned and separated", which is the note's condition. The drafted text adds that if they do not separate the result is R2; the record does not repeat this, but it is in the adopted text |
| 6, four wording fixes (RT-242, RT-243, RT-245, RT-246) | Accept all four; the known-failure-list test folded into the seventh entry when that entry is ruled | Same; "nothing is added to the list now" | Lines 532 to 536, 545 to 564, 597 to 617, 628 to 643: yes | No |
| 7, split seeds (A10) | Accept; a seed counts only if it passes everything; two such seeds per arm | Same; "an arm passes, or reads, only if two seeds each do" | Rule 1, lines 592 to 596; text change 1, lines 626 to 639: yes | No |
| 8, the no-transplant check (A9) | Accept; report, not a veto; pairing tested in the generator's self-test; control 4 is the registered pairing check; restore the detection-margin sentence (about 56 per cent) | Same | Lines 515 to 552: yes | **No, and watched closely.** The record names both checks as the drafted text does, and does not make the self-test the withholding one. It does not say the formula is wrong for every model, only that it no longer withholds |
| 10, the decoy test (A6) | Run it both ways round, method first, checked; decide page 12 with it | Same, plus "the wording changes A6 asks for go into version 5 either way" | Text changes, lines 357 to 373; the test, lines 375 to 397: yes | No. "Either way" is the packet's own words on page 10 (tier 2 packet, line 164) |
| 11, the outcome words (A13) | (a); keep the terms; "every use carries the fixed scope phrase"; register the reviewer's table | The phrase on every use of "metric validated"; the table, with control 6 added to its last row | Lines 715 to 729: yes | **No, and watched closely.** If anything narrower: the record ties the phrase to "metric validated" only, which is what the page showed, and flags the rest (its open item 3). "Control 6 added to its last row" is in the adopted text change 2, not an addition by the recorder |
| 12, the kill case | Decide after the decoy test | Deferred; the planning session's recommendation on record | — | No |

**The ledger numbers** (MEASURED against the outside dispositions, line 49
and lines 84 to 104): the four outside findings adopted by a page take the
next four numbers, from RT-247, as the outside dispositions say they should;
those that repeat an inside finding take its number. Correct. The record
says no ledger rows were written; none were.

## 3. Check 2: does each amendment really follow from what was ruled?

John's note itself names these: page 1h of the 2026-09-26 queue ruling
(page 1), ruling 2 of 2026-10-04 (page 2, via the packet), ruling 4 of
2026-10-03 late evening (page 4), the December-result outcome list (pages 5
and 9, via the packet), ruling 6 of 2026-10-03 late evening (page 7), the
Gate C ruling on the allowance, RT-222 (page 8), and ruling 7 of 2026-10-04
(page 6). Each of those notes matches. The record adds four:

**(a) The Gate C ruling of 2026-09-26 on the collapse rule, RT-220 (the
lesion description, and when the free model is read).** The record cites it
under two pages.

- *Under page 7 (the seed rule): a real consequence.* RT-220 registered "arm F
  is read if at least two of three seeds collapse", a separate two-of-three
  count. Page 7's adopted text change 1 (lines 636 to 639) rewrites the
  section 9 row "Ownership-lesion collapse threshold" to "the same seeds
  passing every condition", and John's note says page 7 amends "the gate rows
  of section 9". MEASURED.
- *Under page 1 (the battery clause): not an amendment, and the note
  misdescribes RT-220.* RT-220 says (lines 160 to 162 of the Gate C ruling)
  that "a separate collapse bar below the learn-both bar was considered and
  not taken". That is a second *threshold for the collapse*. Page 1's
  1,546 line is not a collapse threshold; it replaces the battery clause of
  page 1h, which sat beside the collapse when RT-220 was ruled and which
  RT-220 did not touch. So page 1 changes nothing RT-220 decided. The dated
  note's phrase "unlike the line declined here, it was measured on every toy
  model" reads as if RT-220 had declined the kind of line page 1 now adopts.
  The phrasing comes from the inside dispositions' own reasoning (lines 214
  to 216, "the reason a second collapse line was not taken"), which John
  adopted with page 1, so the recorder did not invent it. ARGUED. **Effect:
  none on any rule; no word from John needed.** Fix: in the record and the
  note, say page 1 "sits beside" RT-220's collapse rule rather than amending
  it, and drop "unlike the line declined here" or reword it to "RT-220
  declined a second collapse threshold; this is a different condition,
  replacing page 1h's batteries".

**(b) Ruling 3 of 2026-10-03, late evening (the device for the registered
fit).** A real consequence. Page 6's RT-245 says, in the packet John ruled
(questions packet, page 6), "name the processor for the whole nomination,
not only the read's fit", and the inside dispositions' tally (lines 676 to
680) lists "RT-245 the device ruling's reach" among the changes that need
his words. The note's phrase "RT-245 and RT-246 amend wording ruled
2026-10-04" is outside John's quotation in the note; it is the planning
session's gloss, and the record was right to correct the date rather than
follow it (its open item 2). Placed beside ruling 3 in both records of
that evening. MEASURED.

**(c) Page 11 of the 2026-10-03 Gate C ruling (what a no verdict maps
to).** A real consequence. That page created the fifth term for arm F and
the fallback and drop rules for arms C and M. The adopted table's own
heading (inside dispositions, lines 443 to 446) says it was "ruled
2026-10-03, page 11 … completed for every arm by … RT-241". Pages 5 and 9
extend it: arm M also dropped on a gate failure; the fifth term also for a
failed channel-removal check and a step 5b gate failure; three new terms.
The dated note says exactly this and claims nothing else. MEASURED.

**(d) Ruling 3 of 2026-10-04 (the no-transplant formula on the competing
solver).** A real consequence. Ruling 3 says the formula "withholds a reading
here, which is the right outcome". Page 8's adopted text deletes the
no-transplant miss from the list of things that withhold a reading (outside
dispositions, lines 547 to 548). The note adds that the solver still returns
no verdict because no site set cleared the floor; ruling 2 of the same file
says so. MEASURED.

**Not noted, and not needed.** Page 2 of the 2026-09-26 queue ruling first
set "room for the miss of up to 0.0175" for the no-transplant rule. RT-222
refined it, and RT-222 carries the page 8 note, so a reader following the
chain finds it. A note beside queue page 2 would be tidy; it is not owed.

## 4. Check 3: the dated notes

MEASURED (`git show --numstat ccd3341`): every ruling file, the roadmap and
the four packet and dispositions files gained lines only; nothing was
removed. Each note starts "*Dated note, 2026-10-06 (Pacific), beside …,
which is left as written*" (the roadmap's is "Third dated note", following
its two earlier ones), points to the record by path, and sits directly below
the ruling it names, as the notes of 2026-10-03 did. The four header lines
on the packets and dispositions say "ruled", point to the record, and say the
text below still reads PROPOSED. Content of each note checked against the
record and the drafted text: all match, except the page 1 half of the RT-220
note (section 3a).

## 5. Check 4: STATUS.md, data/project.toml and the scripts

**STATUS.md and project.toml say what the record says** (ARGUED, read line
by line). Two small defects and one inconsistency:

1. **The closure check of page 1 is placed before the text it checks.** The
   record's owed list (item 4) and STATUS.md (item 4) put "page 1's closure
   check" before version 5 (item 6). The check itself (inside dispositions,
   line 234) runs "on the registration text once written", so it can only
   follow version 5. `data/project.toml` gets this right: its step N29 runs
   "once the registration text carries the repair". Fix: move it after
   version 5 in the record and STATUS.md.
2. **One choice the dispositions left to John is decided in the owed list.**
   The outside dispositions on the fatal finding about the decision procedure
   (A2, lines 269 to 278) recommend removing the withheld figure
   (`arithmetic_withheld`) from the output file, and give John an
   alternative: keep it under one named field. The record's owed item 5,
   STATUS.md's item 5 and project.toml's step N30 all say it is removed. A2
   was never put to John as a question, and nothing in his words covers this.
   It belongs with the A2 question in section 7.
3. **When the $0 work may start.** The record calls its list "the order
   things wait on each other" and puts the decoy test second, saying "if he
   stops or redesigns, nothing below runs as planned". `project.toml` marks
   the toy re-run (N28) and the decision-code changes (N30) as "now". Both
   readings are defensible, since the work is free, but they should agree.
   This is for the author, not John.

Everything else matches: the summary of each page, the eleven amended
rulings, $228 of the $450 ceiling spent (unchanged), the two kill dates,
steps N24 and N25 marked done, N26 to N31 added. The STATUS entry and step
N25's text both say the four wording fixes "wait on his word"; the addendum
should update them (section 6).

**The scripts** (MEASURED; outputs compared with the same scripts run on the
parent commit `227cfb7`):

- `python3 scripts/export_site.py --check`: passes. "data/project.toml is
  valid (8 stages, 7 questions, 12 ideas, 20 findings, 31 next steps, 44
  timeline rows)"; roadmap valid.
- `python3 scripts/check_citations.py`: exit 1, as on the parent. Confident
  findings 93 before, 97 after. **All four new ones** are references to
  `procedure.py` and `experiments/08-successor-degree/src/` in the record
  (line 386) and STATUS.md. Those files are on main (`git ls-tree origin/main`
  lists both); this branch was cut before the frozen code was merged, and
  both texts say "on main". Not a defect. The rest is line numbers shifted by
  the two-line headers.
- `python3 scripts/check_single_source.py`: exit 1, as on the parent.
  Confident findings unchanged at 117. Unsourced figures 367 before, 368
  after: one in the record, a "$0" of the kind every ruling file carries.

## 6. Check 5: the record's list of what it could not settle

| Item | Honestly flagged, not silently decided? | Settled since? |
|---|---|---|
| A7, A8, A11, A12 (four wording fixes) not ruled | Yes. "The four wording fixes need John's word before version 5 carries them"; no ledger numbers given | **Ruled in the follow-up**: accepted as drafted |
| A2 (the decision procedure, fatal) treated as owed | Yes. The record says it treats the work as owed and why (pages 5, 7, 8 and 9 cannot be registered without it), and gives A2 no ledger number. But see section 5, item 2: the owed list then fixes one of A2's open choices | **Not settled.** The follow-up did not cover it |
| The generator self-test line on unseen combinations (outside dispositions, lines 122 to 129) | Yes, named beside the four wording fixes | **Not settled** |
| The date of the ruling RT-245 amends | Yes, and resolved correctly from the record (section 3b) | Needs nothing from John |
| Page 11's second phrase, and whether the new "metric …" terms carry the phrase | Yes. The record adopts the drafted text and tells the writer of version 5 to ask | **Ruled in the follow-up**: both phrases apply, including to the three new terms |
| Page 8's two pairing checks | Yes, with the record's reading stated as a reading | **Ruled in the follow-up**: control 4 withholds; the self-test is a second check. The record's reading was right |
| Page 8's word "restore" | Yes, with the record's reading stated | Needs nothing from John (ARGUED): the note's own parenthesis, "about a 56 per cent chance at the learning bar", is the drafted replacement sentence, so "restore" can only mean keep that sentence |

**What the addendum should carry** (for the author of pull request 103):
John's follow-up words and date; A7, A8, A11 and A12 accepted as drafted
(outside dispositions, lines 407 to 489 and 684 to 711), with the next ledger
numbers (RT-251 to RT-254, if A2 stays unnumbered); both scope phrases on
every use, including the three new terms containing "metric"; control 4 as
the withholding pairing check and the self-test as a second; and the matching
updates to STATUS.md and step N25 of `project.toml`. Together with the two
fixes of section 5 (order of the closure check, the withheld-figure choice)
and the RT-220 wording of section 3a.

## 7. Questions still needing John's word

1. **The decision procedure (A2, the outside review's fatal finding).** Accept
   its drafted disposition: bring the frozen decision code to the new rules,
   run it on made-up failure cases, have it checked, and add a "run end to end
   before registration" item to version 5's rehearsal section? The record
   treats this as owed; John has not said yes to it. It would also take a
   ledger number.
2. **Inside that: the withheld figure.** Remove `arithmetic_withheld` from the
   output file (recommended), or keep it under one named field and reword the
   closure check to allow it there?
3. **The generator self-test line** asserting that no fresh or relaxed
   episode's combination occurs in training (outside dispositions, lines 122
   to 129). Accept it?

Nothing else in the record needs his word.
