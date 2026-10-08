# Re-check of the five must-fix edits to version 5 of the successor registration text (2026-10-08)

*Written 2026-10-08 (Pacific) by a Claude Code session that wrote neither
version 5 (`docs/successor-experiment-proposal-2026-10-07-v5.md`), nor its
check (`docs/reviews/2026-10-08-successor-v5-check-claude-code.md`, pull
request 130), nor the edit that applied the check's five must-fix items (the
commit on the main line whose message begins "Version 5 of the registration
text: the five must-fix items", `064f734`, merged as pull request 131). Its
job is narrow: did the five land as the check asked, and did anything else
move. It edits nothing, merges nothing, rules nothing, rents, spends and
trains nothing. Plain-language rule throughout; counts are marked MEASURED
with the command that produced them, judgments ARGUED.*

---

## 1. What was read, and what was run

Read in full: the workspace and repository working guides; the check's
sections 3 ("Edits version 5 owes to the two rulings of 2026-10-08"), 4
("Verdict", with its five one-line must-fix items) and the text of its
findings 1, 3, 8, 9, 12 and 13; the two rulings of 2026-10-08
(`docs/rulings/2026-10-08-verification-bar-ruling.md`, the bar ruling;
`docs/rulings/2026-10-08-december-result-restatement-rulings.md`, the
restatement rulings); the whole diff of the edit; and, in the edited file,
every passage the check named plus the file's last fifty lines.

**Which commits.** MEASURED: `git log --oneline -8 -- docs/successor-experiment-proposal-2026-10-07-v5.md`
lists two commits: `064f734` (the edit) and `c9b0259` (the draft of version
5). `git rev-parse 064f734^` gives `362314c`, the merge of pull request 130
(the check), so the version before the edit is the file at that merge.
`git diff 064f734 HEAD -- <the file> | wc -l` prints 0: the file on the main
line today is the edit's file, unchanged since. The handoff for this
re-check named the bar ruling's commit (`ada10a9`) as the one the edit
follows; the edit's parent is in fact the merge of the check. Nothing turns
on it; noted so the record is exact.

**What the edit touched.** MEASURED: `git show --stat --format= 064f734`
prints one file, the registration text, 107 lines added and 37 removed. No
other file moved.

Run: the two checking scripts on the edited file and on the version before
the edit (section 5 below); the four searches the handoff asked for
(section 4); and a search of the main line for the words of John's the
change note quotes.

---

## 2. Every hunk of the edit, assigned

MEASURED: `git diff 362314c 064f734 -- docs/successor-experiment-proposal-2026-10-07-v5.md | grep -c '^@@'`
gives 21 hunks. Each is assigned below by the line it starts at in the
version before the edit. "Item n" means the check's must-fix item n, in the
numbering of its section 4; "place n" means the numbered place in the
check's section 3, part A.

| Hunk (old line) | Where in the text | Belongs to |
|---|---|---|
| 48 | Header, "Three things a reader of version 4 should know first" | Item 4, place 10 (the bar is ruled); also announces the S4b sentence of item 5 |
| 72 | Source table, the sharpness-fix row | Item 4 (removes a live pointer to open item 1; not one of the ten named places, but inside the item's purpose, "the text otherwise says a ruled bar is unruled") |
| 80 | Source table, two new rows | Item 4, place 9 (a row for the bar ruling); item 5 with the check's B.4 (a row for the restatement rulings) |
| 348 | Section 3, opening sentence | The check's should-fix B.2 (cites the roadmap's dated head note) |
| 382 | Section 3, the scope rule | Item 2 |
| 480 | Section 3, the fifth-term sentence | Item 3 (line 483 of the check) |
| 1465 | Section 5.6, "are not ruled" | Item 4, place 1 |
| 1478 | Section 5.6, the stop condition | Item 5 (the ruled sentence; registered ending) |
| 1506 | Section 5.6, the four options and the open-item bracket | Item 4, place 1 |
| 2755 | Section 7.4, the frozen list | Item 4, place 4 |
| 3055 | Section 9, the in-use row | Item 4, place 3 (partly; finding 1 below) |
| 3408 | Section 11, step 3 | Item 4, place 5 |
| 3517 | Section 11, step 8 | Item 3 (line 3520 of the check) |
| 3554 | Section 11, stop S4b | Item 5 |
| 4157 | Section 13, weakness W17 | Item 4, place 6 |
| 4534 | Section 15, entries 35 and 36 | Item 4, place 8 (entry 35); item 5 with the check's B.4 (entry 36) |
| 4878 | Section 17, failure 3, the printed block | Item 4, place 7 |
| 4891 | Section 17, failure 3, the prose | Item 4, place 7 |
| 5065 | Section 17, candidate 7 | Item 4, place 7 |
| 5412 | Section 21, open item 1 | Item 4, place 2 |
| 5538 | End of file: version 4's closing section removed; the dated change note added | Item 1; the change note |

ARGUED: no hunk falls outside the five items, the should-fix B.2 and the
change note. The one hunk not at a place the check named by number (old
line 72, the sharpness row of the source table) does only what item 4 asks
everywhere else: it replaces a pointer to open item 1 with the ruling's
citation.

---

## 3. The five items, each against the check's own words

| Item | The check's one line | Landed? | Where it is checked below |
|---|---|---|---|
| 1 | Cut the stray heading off the end of the file's last paragraph and delete version 4's closing section | Landed | 3.1 |
| 2 | Add "instrument not validated" to the scope rule of section 3 | Landed | 3.2 |
| 3 | Replace "metric validated, degree not read" with the fifth term's renamed words at the two registered sentences | Landed | 3.3 |
| 4 | Write the verification-bar ruling in (ten places) | Partly landed: nine of ten places fully, place 3 half (finding 1) | 3.4 |
| 5 | Write the ruled early-stop sentence in at S4b and section 5.6 | Landed | 3.5 |

### 3.1 Item 1: version 4's closing section

The diff's last hunk removes the eight lines beginning "It edits nothing:
not version 3" and the heading that had been joined to the end of version
5's last paragraph ("...written in.**## What this version does not do").
MEASURED, in the edited file: `grep -n 'What this version does not do'`
finds one heading, at line 5572, on its own line and preceded by a rule;
`grep -n 'It edits nothing'` finds one paragraph, at line 5574, which reads
"It edits nothing: not version 4, not any ruling..." (version 5's own
closing, which names version 4; version 4's named version 3). The file
ends with the dated change note (section 4 below). **Landed.**

### 3.2 Item 2: the scope rule

Lines 391 to 393 of the edited file: "Wherever a term containing
"instrument discriminates", "instrument checked" or "instrument not
validated" appears, in this text, `STATUS.md`, the paper or in public, it is
followed in the same sentence by "on these constructed systems, for this
intervention procedure"; so is R2." The eighth term's words are in the
rule. **Landed.**

### 3.3 Item 3: the fifth term's words in the two registered sentences

Section 3, lines 490 to 493: "If arms T and C separate and arm F returns
no verdict, the outcome is the fifth term, "instrument discriminates
specified constructed mechanisms, degree not read", with its reason after a
colon; it is not reported under R1". Section 11, step 8, lines 3534 to
3537: "if it returns no verdict, the outcome is the fifth term, "instrument
discriminates specified constructed mechanisms, degree not read", with its
reason." MEASURED: `grep -n 'metric validated, degree not read'` finds
only line 385 (section 3's table, the old-name column) and line 4355
(section 15's record of the 2026-10-03 ruling, kept as history, as the
check allowed). **Landed.**

### 3.4 Item 4: the verification-bar ruling, at the ten places

1. **Section 5.6** (lines 1476 to 1479): "The bars 0.9 and 0.5 are the
   method note's, stated before any figure was seen, and **are ruled: on
   2026-10-08, in John's words "Rule the verification bar now, keep it at
   0.5" (`docs/rulings/2026-10-08-verification-bar-ruling.md`, authorship
   mixed), they are fixed here as written.**" The bracket "[OPEN ITEM 1 for
   John ...]" is gone (MEASURED: `grep -n 'OPEN ITEM 1\b'` finds nothing).
   The four options stay, followed by (lines 1522 to 1527): "*(Ruled
   2026-10-08: option (a) taken; (b), (c) and (d) declined, (d) staying the
   named route to a real reference if the stop fires, with its own toy work
   and ruling; ... Open item 1 of section 21 is closed by that ruling.)* The
   bar is ruled at 0.5 and fixed here before the reruns launch, as the
   2026-10-07 ruling requires, and the route-use figure is recorded for
   every built arm and seed." **Landed.**
2. **Section 21, item 1** (lines 5452 to 5456): "**The bar for "the
   repaired route holds" (section 5.6; the largest). CLOSED, ruled
   2026-10-08 in John's words "Rule the verification bar now, keep it at
   0.5" (..., authorship mixed): option (a), the recommendation below,
   taken; the number is kept so that the body's cross-references still
   land. The text below is as it stood before the ruling.**" Date,
   authorship and number kept, as asked. **Landed** (see finding 4 on the
   kept text).
3. **Section 9, the in-use row** (line 3072). The term column now reads
   "part A: the built-in answer's weight on the true agent at least 0.9;
   part B: route use at least 0.5 on every built route; ruled 2026-10-08 at
   these figures (`docs/rulings/2026-10-08-verification-bar-ruling.md`)";
   the words "as coded, pending John's ruling on the bar (open item 1)" are
   gone. But the row's source column still ends: "the bars from
   `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, branch
   `fix-sharpness-inuse-check` at `644238e`, not ruled". The check asked
   that both phrases become "ruled 2026-10-08"; the second was not changed.
   **Partly landed** (finding 1).
4. **Section 7.4, the frozen list** (lines 2771 to 2773): "the in-use check
   on the built arms, both parts, with its bars as section 5.6 fixes them
   (ruled 2026-10-08, `docs/rulings/2026-10-08-verification-bar-ruling.md`;
   the bar);". The citation is in; a fragment "; the bar)" is left over from
   the old "until John sets the bar)". **Landed** in substance (finding 2
   on the fragment).
5. **Section 11, step 3** (lines 3422 to 3427): "**Two changes still owed
   in the code:** the read fitted on 1,800 of 1,980 development episodes
   (...), and the renamed outcome words (open item 7 for the episode count;
   the bar of the in-use check is ruled at 0.9 and 0.5, which the frozen
   code already carries)." This is what the check's place 5 asked, word for
   word in substance. **Landed** (see finding 7 on "the frozen code").
6. **Section 13, W17** (line 4179): "the bar is ruled at 0.5
   (2026-10-08)". **Landed.**
7. **Section 17, failure 3 and candidate 7.** The printed block (line 4916)
   ends "fail at 0.5 (the bar ruled 2026-10-08)"; the prose (line 4929)
   reads "that is weakness W17 (the bar ruled 2026-10-08), stated rather
   than stepped over"; candidate 7 (lines 5102 to 5105) reads "**This is
   the one place the candidate fires on this version.** The bar is ruled at
   0.5 (2026-10-08), and the firing stands as the record's own prediction
   that the stop of S4b will most likely fire, which the ruling says in its
   own words." The ruling's words are "The record predicts this is the
   likelier outcome." **Landed.**
8. **Section 15, entry 35** (lines 4556 to 4562): records the ruling,
   John's words, "authorship mixed: the drafting session recommended option
   (a), John chose it", and the three options not taken, each in the
   ruling's terms. **Landed.**
9. **The source table** (line 86): a row for the ruling, "main line (pull
   request 126)". MEASURED: `gh pr view 126` is MERGED, "Ruling 2026-10-08:
   the verification bar stays at 0.5". **Landed.**
10. **The header** (lines 51 to 54): "Since 2026-10-08 two more things: the
    bar for "the repaired route holds" is ruled at 0.9 and 0.5 (section
    5.6), and an early stop at that verification is a registered ending of
    experiment C with its own ruled sentence (stop S4b)." **Landed.**

### 3.5 Item 5: the ruled early-stop sentence

**Stop S4b** (lines 3573 to 3579): "Not one of the eight outcome terms,
which are unchanged, but **a registered ending of experiment C, reached by
its own stop rule**, reported in the words ruled on 2026-10-08: **"the
built arms as designed are not references; the measure was not reached"**
(`docs/rulings/2026-10-08-december-result-restatement-rulings.md`, decision
2; `docs/rulings/2026-10-08-verification-bar-ruling.md`), with the figures,
and goes to John; the redesign of the arms so the built route is the only
route is the named route to a real reference and needs its own ruling."
The old words "the repaired construction did not hold at 10 million
parameters" are gone (MEASURED: `grep -n 'repaired construction did not
hold'` finds nothing).

**Section 5.6** (lines 1493 to 1496): "That ending is reported in the words
ruled on 2026-10-08, "the built arms as designed are not references; the
measure was not reached", and is a registered ending of experiment C, not
a failure of the year (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`)."

**Section 15, entry 36** and the **source table row** (line 87, "main line
(pull request 128)"; MEASURED: `gh pr view 128` is MERGED, "Rulings
2026-10-08 on the December-result restatement: all three decisions as
proposed") carry the same sentence and the cross-references. **Landed.**

---

## 4. The two rulings, quoted faithfully?

**The bar ruling.** Its bars: part A, mean weight on the true agent at
least 0.9 over the 3,000 gate episodes; part B, route use at least 0.5 on
every built route; a seed counts only when both parts and the learning gate
pass; the repaired route holds when arms C and M each pass. Version 5 states
these figures unchanged in section 5.6, section 9 and the header. What
follows a miss: the 2026-10-07 stop condition fires, experiment C stops
before the free-arm run, the rest of the first release is not spent, and C
is written up as instrument research with the finding "the built arms as
designed are not references". Version 5's S4b and section 5.6 say the same
and cite the file. What is declined: (b) a small bar such as 0.1, (c) part
A alone, (d) redesigning arms C and M's stirred-in half, with (d) staying
"the named route to a real reference if the stop fires" and needing "its
own toy work and its own ruling". Section 5.6's bracket, entry 35 and S4b
each carry this. John's words, "Rule the verification bar now, keep it at
0.5", are quoted exactly at section 5.6, section 21 and entry 35. ARGUED:
faithful; nothing in the new text goes beyond the ruling.

**The restatement rulings.** Decision 2's sentence, word for word: "the
built arms as designed are not references; the measure was not reached."
MEASURED: the sentence wraps across lines everywhere it appears, so a
one-line `grep -c` for it returns 0; a three-line Python command that
collapses runs of whitespace to one space and counts the sentence in the
edited file gives 4 (section 5.6, S4b, entry 36, the change note), each
exact. Decision 2's "registered result
reached by its own stop rule, and it is not a failure of the year" appears
as "a registered ending of experiment C, reached by its own stop rule"
(S4b) and "not a failure of the year" (section 5.6); decision 1's "changes
none of its registered terms, kill dates or caps" appears at section 3's
opening, the source row and entry 36. John's words, "Merge it and approve
all the decisions from the doc", are quoted exactly at entry 36. ARGUED:
faithful. One wording point: the ruling says "registered result"; version 5
says "registered ending" and, in the same breath, "not one of the eight
outcome terms". That is the restatement's own distinction (an ending
counted as a result, not a ninth term) and the check's B.1 asked for it in
those words.

---

## 5. The four searches, and the file's end

All MEASURED on the edited file, `docs/successor-experiment-proposal-2026-10-07-v5.md`:

- `grep -n 'metric validated, degree not read'`: lines 385 (section 3's
  table, old-name column) and 4355 (section 15, the 2026-10-03 ruling's
  record). Nothing else. As required.
- `grep -n 'open item 1\b'`: lines 86 (the source row: "open item 1
  closed") and 5607 (the change note: "open item 1 closed in section 21").
  `grep -n 'OPEN ITEM 1\b'`: nothing. No live pointer remains. As required.
- `grep -c` for the em-dash character: 0. For the en-dash character: 0. As
  required.
- `wc -l`: 5,620 lines (the version before the edit: 5,550). `tail -6`
  prints the change note's last paragraph, ending "This edit is owed a
  short re-check that the five landed and nothing else moved." The last
  heading before it (line 5586) is "## Changes after the check
  (2026-10-08)"; the heading before that (line 5572) is version 5's own
  closing, "## What this version does not do", whose paragraph names
  version 4, not version 3. No text of version 4's closing remains.

Other leftover searches, all MEASURED: `grep -n 'are not ruled\|open items
1 and 7\|pending John.s ruling\|until John sets\|Whichever bar is ruled'`
finds only line 5465 (section 21, item 1's kept "Meanwhile" text; finding
4) and line 5606 (the change note quoting the words it replaced).

---

## 6. The two scripts, edited file against the version before

Run with `python3 -I`, from the root of this checkout. The version before
the edit was written to `docs/zz-parent.md` with `git show 362314c:docs/successor-experiment-proposal-2026-10-07-v5.md > docs/zz-parent.md`,
run, and deleted (`git status --short` clean afterwards).

| Script | Edited file | Version before | Same? |
|---|---|---|---|
| `scripts/check_citations.py --only <file>` | Confident findings 55; things to look at 50 | 55; 50 | Yes |
| `scripts/check_single_source.py --only <file>` | Confident findings 4; 5 unsourced figures; 0 widely repeated | 4; 5; 0 | Yes |

MEASURED, both runs. The applying session reported identical counts; they
are identical. ARGUED: the edit added no figure the scripts flag and
removed none they had flagged, which is what "no figure changed" should
look like.

---

## 7. The three new passages, for plain language and overreach

- **Section 5.6, the ruled-bar sentences** (lines 1476 to 1479; 1493 to
  1496; 1522 to 1527). Plain, apart from "authorship mixed", which is the
  record's own word for "the session proposed, John chose" and is used that
  way across the rulings. No claim beyond the ruling: the figures, the
  option taken, the three declined and (d)'s standing are each in the
  ruling's words.
- **Stop S4b** (lines 3573 to 3579). Plain. "Reached by its own stop rule"
  and "not one of the eight outcome terms, which are unchanged" are the
  restatement's and the check's words. The last clause ("the redesign ...
  is the named route to a real reference and needs its own ruling") is the
  bar ruling's "What is declined" paragraph; it drops the earlier text's
  mention of "version 4's fallback" as an alternative, which the ruling
  does not name among the declined options and does not keep. ARGUED: that
  drop follows the ruling rather than exceeding it, since the ruling names
  only option (d) as the route forward.
- **Section 15, entries 35 and 36** (lines 4556 to 4570). Plain. Entry
  36's heading, "The December result restated under the refounding", uses
  "the refounding" from the proposal's title without saying what it means
  here; the body of the entry does say (the measurement target moved). A
  reader outside the record would want one more word. Note only (finding
  8).

---

## 8. Findings

1. **Must-fix (small).** Section 9's in-use row, line 3072, still ends its
   source column with "not ruled", two words the check's place 3 asked to
   become "ruled 2026-10-08", while the same row's term column now says
   "ruled 2026-10-08 at these figures". One table cell reads both ways.
   MEASURED: the tail of line 3072 is "the bars from
   `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, branch
   `fix-sharpness-inuse-check` at `644238e`, not ruled |". Fix: replace
   "not ruled" with "ruled 2026-10-08" in that cell. This is the only
   part of the five that did not fully land.
2. **Should-fix.** Section 7.4, lines 2772 to 2773: "(ruled 2026-10-08,
   `docs/rulings/2026-10-08-verification-bar-ruling.md`; the bar);" ends in
   a fragment left from the old "until John sets the bar)". Drop "; the
   bar". Meaning is unaffected.
3. **Note.** The should-fix B.2 was applied to section 3's opening only;
   the check also named section 14 and R4's row. The change note says
   exactly what was done ("Section 3's opening cites the roadmap's dated
   head note"), so nothing is misreported; the rest of B.2 stays owed with
   the other should-fix items. MEASURED: `sed -n 4215,4253p | grep roadmap`
   finds nothing in section 14.
4. **Note.** Section 21, item 1 is marked CLOSED with the ruling, and its
   old text is kept beneath, by design ("The text below is as it stood
   before the ruling"). That kept text includes "*Meanwhile:* the text
   carries the coded bars and says they are not ruled" (line 5465), which
   is no longer true of the text. The CLOSED heading governs; a reader who
   skims to the "Meanwhile" line could be misled for a sentence. The
   check's place 2 asked only for the closed marker and the kept number,
   so this is not a miss; a one-line "(as it then did)" would remove the
   doubt.
5. **Note.** Version 5's own closing section (lines 5572 to 5582) still
   ends "with everything ruled by 2026-10-07 written in" and says the text
   "does not rule any of the twelve open items of section 21: each is
   John's". Both remain true (the 2026-10-08 rulings are written in as
   well; the text itself ruled nothing; John closed item 1). The change
   note after it says what changed. Nothing owed; the next edit could add
   "and 2026-10-08".
6. **Note.** The change note (line 5593) and the pull request 131 body
   quote John's word "Merge both and apply the version 5 fixes". MEASURED:
   `git grep -n 'Merge both and apply' HEAD` finds only the change note;
   `grep -n 'Merge both and apply' STATUS.md` finds nothing. The words are
   an instruction to apply ruled changes, not a ruling, so no rulings file
   is owed; the record of them is the change note and the pull request.
7. **Note.** Section 11, step 3 says the bar is "ruled at 0.9 and 0.5,
   which the frozen code already carries" (the check's own phrase, place
   5). MEASURED: `git grep -n 'ROUTE_WEIGHT_MIN *=\|ROUTE_USE_MIN *=' 644238e -- experiments/08-successor-degree/src`
   finds `ROUTE_WEIGHT_MIN = 0.9` and `ROUTE_USE_MIN = 0.5` in `measure.py`
   on the sharpness branch at `644238e`, which is unmerged. The main-line
   frozen commit has no in-use check. The source table's code-freeze row
   defines the registered code as the freeze "as changed since by pull
   request 105 and the three branches above", so the sentence is
   consistent with the text's own definition; the merge is still owed
   (open item 10).
8. **Note.** Entry 36's heading uses "the refounding" without a plain
   phrase beside it (section 7 above). The proposal it names uses the same
   word in its title; the entry's body says what moved.
9. **Note.** The restatement rulings file says the restatement lands "at
   the head of" the December-result roadmap; version 5 repeats "at the
   head". MEASURED: `grep -n '2026-10-08' docs/december-result-roadmap-2026-09-20.md`
   finds the dated note at line 55, after the roadmap's status block and
   before its first section. "At the head" is fair.
10. **Note.** The re-check's handoff named `ada10a9` (the bar ruling's
    commit) as the commit the edit follows. The edit's parent is `362314c`,
    the merge of the check (pull request 130); the bar ruling is an
    ancestor of both. The diff in this report is against the true parent.

---

## 9. Verdict

**ARGUED.** The edit may stand: four of the five must-fix items landed
fully and the fifth at nine of its ten places, with two words in one
table cell of section 9 ("not ruled", finding 1) still to change before
the registration commit; no hunk of the edit falls outside the five items,
the declared should-fix B.2 and the dated change note; both rulings are
quoted faithfully; and both checking scripts return the same counts before
and after.

---

## 10. What this re-check did not do

It did not re-check version 5 as a whole, the check's should-fix items 4 to
7 or its open items 2 to 12; it did not re-read the rulings of 2026-10-06
or 2026-10-07; it did not run any model, read or transplant; it did not
check the sharpness branch, which remains owed its own check. It did not
edit version 5 or any other existing file, merge, rule, rent, spend or
train.

## 11. Files

- This report: `docs/reviews/2026-10-08-successor-v5-fixes-recheck-claude-code.md`,
  on branch `recheck-v5-fixes-2026-10-08`.
- The diff this report assigns hunk by hunk: `git diff 362314c 064f734 -- docs/successor-experiment-proposal-2026-10-07-v5.md`
  (21 hunks). Every other command is named beside its result above; the
  temporary copy of the version before the edit was deleted after the two
  script runs and is not committed.
