# Check of two pull requests: the red-team ledger's rows from entry 230 on (pull request 141) and three wording fixes in version 5 (pull request 140)

*Written 2026-10-08 (Pacific; the file carries the date of the two branches
it checks) by a Claude Code session that wrote none of what it checks: not
the ledger rows, their method note or findings note, not the version 5
registration text or its wording fixes, and none of the reviews, rulings or
checks the rows summarise. It read no chat of any session. Branch
`check-ledger-rows-and-v5-wording`, cut from the main line. Laptop only,
nothing run but `git`, `grep` and three short Python scripts that only read
files: $0. Written under the workspace plain-language rule.*

*What was checked:*

- *Pull request 141, branch `ledger-rows-rt230-on` at `1eeaa51`: 45 new rows
  at the end of `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`
  (the red-team ledger, the list of every problem a review has found in the
  successor experiment and how each was settled), the method note
  `docs/2026-10-09-ledger-rows-method.md` and the findings note
  `docs/2026-10-09-ledger-rows-findings.md`. Written under item 12 of
  `docs/rulings/2026-10-08-v5-open-items-rulings.md` (John's answers to
  version 5's open items).*
- *Pull request 140, branch `v5-wording-leftovers-2026-10-09` at `ec340fb`:
  three wording fixes in `docs/successor-experiment-proposal-2026-10-07-v5.md`
  (version 5 of the successor experiment's registration text), answering the
  three leftovers (L1 to L3) of
  `docs/reviews/2026-10-08-v5-open-items-rulings-recheck-claude-code.md`.*

*A note on the main line moving during the check.* When this check started
the main line was at `760deef` (the merge of pull request 138). While it ran,
pull request 139 (the site footer change, commit `3c56d3c`) was merged, and
the main line is now `1c3b6c8`. Before that merge, the footer commit showed
up in pull request 140's diff against the main line. It no longer does, and
pull request 140 now carries only the one commit on version 5. Neither
branch touches the files pull request 139 changed.

## Verdicts

- **Pull request 141 (the ledger rows): ready to merge.** No must-fix items.
  Every row's finding matches its source, every disposition matches its
  ruling, the counts are right, the number collision and the gap are real,
  and nothing above the new section was changed. Three should-fix items and
  four notes for John, below.
- **Pull request 140 (version 5 wording): ready to merge.** No must-fix
  items. All fifteen cited commits are on the main line, the paragraph and
  the three "owed its check" places are corrected, the check they now cite
  exists, and no figure, bar, term or stop changed. One should-fix item,
  outside this pull request's scope.

---

## A. Pull request 141: the red-team ledger's rows from entry 230 on

### A.1 Nothing above the new section was edited

```
$ git diff origin/main...origin/ledger-rows-rt230-on -- experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | head -6
diff --git a/experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md b/...
index ae39fff..fbc5045 100644
--- a/experiments/...red_team_ledger.md
+++ b/experiments/...red_team_ledger.md
@@ -865,3 +865,166 @@ without ledger rows:
$ git diff origin/main...origin/ledger-rows-rt230-on -- experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | grep -c '^-[^-]'
0
$ git diff --stat origin/main...origin/ledger-rows-rt230-on
 docs/2026-10-09-ledger-rows-findings.md            | 137 +++++++++++++++++
 docs/2026-10-09-ledger-rows-method.md              | 120 +++++++++++++++
 .../red_team_ledger.md                             | 163 +++++++++++++++++++++
 3 files changed, 420 insertions(+)
```

One hunk, starting after the old last line (865), and no line removed
anywhere. Run again after the main line moved to `1c3b6c8`: the same.

### A.2 The counts

A short script (`count.py`, reading the branch's copy of the ledger from line
868 on, sorting each row by its closure word):

```
checked 15
accepted 22
open 8
```

Forty-five rows; every number RT-230 to RT-273 has exactly one row except
RT-256, which has two:

```
$ git show origin/ledger-rows-rt230-on:<ledger> | grep -oE "^\| RT-2[0-9]+" | sort | uniq -c
   ... 1 | RT-230 ... 1 | RT-255
   2 | RT-256
   1 | RT-257 ... 1 | RT-273
```

These match the row section's own count and the findings note: 15 closed as
"the claim was checked", 22 as "the argument was accepted", 8 open, with the
same lists of numbers.

### A.3 Every cited file exists on the main line

All 36 files the rows, the method note and the findings note cite were
tested with `test -f` on the main line; every one printed `ok`, none
`MISSING`. The commits the rows cite are what they say:

```
$ git log -1 --format='%h %s' 4cb7f8e
4cb7f8e Gate C tier 1 review of successor proposal v3 at 37269ad: RT-230 to RT-236, nothing fatal, two serious (#74)
$ git log -1 --format='%h %s' 821f154
821f154 Controls re-run under the registered rules: the ruled change holds; controls 2 and 4 go to John (#76)
$ git log --format='%h %s' -- experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md
e184a6e Check of the controls re-run of 2026-10-03: it reproduces exactly, and the too-early-position diagnostic holds (#79)
$ git log --oneline --merges origin/main | grep -E "#(107|113)\b"
f609c9d Merge pull request #113 from jfredson/check-a2-additions
e6dd8fa Merge pull request #107 from jfredson/check-a2-decision-procedure
$ git log -1 --format='%h %s' 5de5fff
5de5fff PROPOSAL version 2: the two-sided question, applying all eighteen Gate C findings (RT-256 to RT-273) and John's two rulings after the pass; owed a check
$ git log -1 --format='%h %s' 32c3b78
32c3b78 Proposal version 2: the six must-fix items of its pairing check applied in place, with a dated change note; three points restated as open questions for John
```

### A.4 The number collision on RT-256: confirmed

```
$ git merge-base --is-ancestor 380612a 9184ad9; echo "exit $?"
exit 1
$ git log -1 --format='%h %ad %s' --date=iso 380612a
380612a 2026-10-06 10:09:51 -0700 Addendum: John accepts the decision-procedure finding (A2, RT-256), "yes, remove"; fix the four defects from the check (pull request 104)
$ git log -1 --format='%h %ad %s' --date=iso 9184ad9
9184ad9 2026-10-07 17:28:32 -0700 Proposal: dated note recording John's approval in principle (...), pending the Gate C tier 1 pass
$ git merge-base --is-ancestor 380612a origin/main; echo "exit $?"
exit 0
$ grep -n "RT-256" docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md
358: ... section, and takes RT-256). ...
537:| RT-256 | A2 (fatal) | The final decision procedure that withholds bad readings and assigns the outcome had not run end to end on the rules as ruled |
$ grep -n "RT-256\|RT-255\|9184ad9" docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md | head -4
5:`docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md` at commit `9184ad9`
24:serious or minor. Finding numbers continue the red-team ledger from RT-256;
25:the highest number in use is RT-255 (the a2 decision-procedure finding, in
343:**RT-256 (the records-not-on-the-branch finding). Serious. MEASURED.** The
```

The addendum that gave RT-256 to the outside reviewer's fatal finding on the
decision procedure (finding A2, commit `380612a`, 2026-10-06) is on the main
line, but it is not in the history of `9184ad9`, the commit of the refounding
proposal that the Gate C pass reviewed. The pass then numbered its first
finding (the records-not-on-the-branch finding) RT-256 too. The collision is
real, and the findings note describes it correctly. The misdescription the
findings note adds is also real: the pass calls RT-255 "the a2
decision-procedure finding", but RT-255 is the unseen-combinations remark:

```
$ grep -n "RT-255" docs/2026-10-06-successor-a2-decision-procedure-findings.md
76:**Control 5 (RT-255).** The default training stream excludes all 1,600 fresh
```

Version 5 uses RT-256 in the decision-procedure sense at lines 88, 1804,
3306 and 5443, as the findings note says (checked with `grep -n "RT-256"` on
the main line's copy).

### A.5 The gap: no rows for RT-212 to RT-229, confirmed

```
$ grep -nE "RT-2(1[2-9]|2[0-9])" <branch copy of the ledger>
(no output)
$ grep -oE "RT-2(1[2-9]|2[0-9])\b" docs/successor-experiment-proposal-2026-10-07-v5.md | sort | uniq -c
  25 RT-212    8 RT-213    6 RT-214    3 RT-215   10 RT-216    3 RT-217
   1 RT-218    1 RT-219    6 RT-220    5 RT-222    5 RT-223    1 RT-224
   2 RT-225    2 RT-226    4 RT-228    8 RT-229
```

The ledger, with the new rows, does not mention any number from RT-212 to
RT-229 at all. Version 5 cites sixteen of those eighteen (all but RT-221 and
RT-227), RT-212 (the empty-read finding) 25 times, exactly as the findings
note says. No number above RT-273 is in use: a search of every Markdown and
TOML file finds RT-274 and RT-299 only in line 23 of
`docs/reviews/2026-10-07-filtered-battery-check.md`, the sentence saying
nobody uses them.

### A.6 Row by row

I checked all 15 "checked" rows and all 8 open rows against their source
review, their ruling and the check they cite. Of the 22 "accepted" rows I
checked 11 in full (two of the version-3 review rows: RT-232, RT-236;
RT-238, RT-239, RT-242, RT-244, RT-246 from the version-4 inside review; the
outside findings RT-251 and RT-252; RT-262 and RT-266 from the Gate C pass)
and read the other eleven against their source line.

**Findings against their sources.** Each row's finding was compared with the
source's own one-line summary: the version 3 review's table (lines 94 to
102), the version 4 inside review's table (lines 125 to 136), the outside
dispositions' table (lines 138 to 149, which also gives the severities used
for RT-247 to RT-254), the 2026-10-06 rulings' follow-up table for RT-251 to
RT-255, and the Gate C pass's finding headings (lines 343 to 730) and counts
line (line 920: "1 fatal (RT-262), 13 serious ..., 4 minor (RT-257, RT-259,
RT-270, RT-271)"). Every finding matches, every severity matches its source's
word, and every figure quoted in a finding (0.544 and 0.306; 0.0049, 0.0099,
0.0529; 45 of 45; 0.733, 0.417, 0.633; 576, 892, 1,080; 0.109 to 0.139 and
0.091 to 0.121; 4.6 seconds, about 25 hours) is the source's.

**Dispositions against their rulings.** Every quotation of John was found in
the ruling it is attributed to: "Agreed on all" (2026-10-03 rulings, line 7);
"(a), go with the recommendation" (2026-10-06 rulings, pages 1, 4 and 11);
"yes, accept" (pages 2 and 3); "accept all, go with the recommendations"
(pages 5 and 9); "yes, accept all four and fold it in" (page 6); "accept, go
with the recommendation" (pages 7 and 8); "yes, run it, go with the
recommendation" (page 10); "accept all four", "yes", "yes to the self-test",
"yes, remove", "yes, stricter, go with the recommendation" and "(a), go with
the recommendation" (follow-up items 1, 3, 4, 6, 7 and 8); "Keep the second
release conditional, and withdraw the calendar dates" and "Yes to all three,
as recommended" (2026-10-07 rulings, lines 121 and 168). The 2026-10-08
rulings' items 3, 7 and 8 say what the RT-240, RT-247 and RT-250 rows say
they say (lines 33, 37 and 38). The dated notes RT-236, RT-244 and RT-246
point to are in place (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`
line 366; `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`
lines 34 and 73).

**The 15 "checked" rows.** Each names a committed check by a session that
did not write the fix, and each check ran commands whose output bears on the
fix:

| Row | The check it names, and what I found there |
|---|---|
| RT-230, the floor on the transplanted piece | The controls re-run check (`e184a6e`, pull request 79): "it wrote the same 26 files"; arm C 1.00512, 0.99259, 0.99743. The row says honestly that its reading of the code against the rule is labelled argued (the check's line 145) |
| RT-231, arm M's blind reading | The same check, line 135: 0.0049, **0.0099**, 0.0529, correcting the re-run's 0.0100 |
| RT-233, controls with no figure | The same check: 26 files reproduced; null transplant "12 of 12 primary; 9 of 9 stricter" (line 130) |
| RT-234, the floor applied twice | The same check (fresh floor "12 of 12", line 137) and the additions check (pull request 113): case 23, arm C failing the fresh floor, gives no verdict for arm C; switching the fresh floor off changes cases 23 and 25 |
| RT-241, holes in the outcome map | Decision-procedure check (pull request 107: "22 of 22 agree (mine = code = written expectation)") and additions check (pull request 113: 25 of 25) |
| RT-248, the no-transplant check | Pull request 107's own recompute: "The no-transplant rate withholds nothing (page 8)", line 60 |
| RT-249, split seeds | Pull request 107's table: "toy, seed 0 as step 5a: fifth / fifth / fifth"; "toy, seed 1 as step 5a: R3 / R3 / R3" |
| RT-255, unseen combinations | The training-exclusion check: "Verdict: pass, with three small notes", "I found no route around it" |
| RT-256, the decision-procedure finding | Pull requests 107 and 113 as above; the row names both reviewers' files, as the closure rule asks of a fatal item |
| RT-256, the records-not-on-the-branch finding; RT-257, the superseded figure; RT-258, the kill-date rule; RT-260, the missing heading; RT-268, the dates; RT-270, the misdescribed record | The version 2 check (`docs/reviews/2026-10-07-proposal-v2-check.md`): each marked MEASURED there, with `git show` and `shasum -a 256` (lines 85 to 105), the recompute 149.06 and 171.9 (line 133), the spec search exiting 1 (line 173 on), the list of every date (line 342 on) and the printed line 44 |

None of the 15 rests only on someone reading text, and none is marked
checked because the finding itself was measured (the findings note's point
6 is right about that). See should-fix A-S1 for a limit on the last six.

**The 8 open rows.** Each is open for a reason the record bears out:

- RT-237, the free model's gate (fatal): the ruling owes "the four-part
  measured check at lines 232 to 267, by a session that wrote neither the fix
  nor version 5" (2026-10-06 rulings, page 1); no such check is on the main
  line.
- RT-240, episode counts at the registered width: the 1,800-episode re-run
  and its check exist (`docs/2026-10-07-page4-rerun-check.md`, "Verdict:
  reproduced, with notes"), but item 7 of the 2026-10-08 rulings (the
  iteration limit of 10,000, re-run, check) is not done.
- RT-247, the decoy: the check of the decoy test found a differently coded
  decoy partly fools the read, "0.28, 0.23 and 0.29" (lines 37 to 38); item 8
  of the 2026-10-08 rulings is not done.
- RT-250, the outcome words: the renamed words are not in the code:
  ```
  $ grep -rn -i "metric validated\|metric not validated\|metric does not separate" experiments/08-successor-degree/src/*.py | head -3
  experiments/08-successor-degree/src/measure.py:63:    "R1": "metric validated, degree read",
  experiments/08-successor-degree/src/measure.py:64:    "R2": "metric does not separate",
  experiments/08-successor-degree/src/measure.py:66:    "fifth": "metric validated, degree not read",
  $ grep -rn -i "instrument returned no reading" experiments/08-successor-degree/src/
  (no output)
  ```
- RT-263 (the control's specification), RT-267 (the observer side), RT-273
  (the loss conditions that cannot lose): the version 2 check's must-fix
  items 4, 2 and 1 respectively (its lines 640 to 660); repaired only at
  `32c3b78`, which no committed file checks:
  ```
  $ grep -rl "32c3b78" docs experiments data STATUS.md
  (no output)
  ```
  The two later battery checks read version 2 at `5de5fff` (the first one's
  line 8) or read sections of it without checking that commit (the third
  one's lines 48 to 49).
- RT-269 (the book's prediction): the version 2 check marks it "Partial"
  (line 376) and its should-fix list asks for the chapter 5 quotation (line
  668); version 2 still says the quotation "waits on the book's text" (line
  430 on the main line).

**The closure rule.** Against `docs/outside-review-protocol.md`, lines 400 to
439: every "checked" row has a committed check by another session with a
command and its output; every "accepted" row has a ruling that accepted the
finding and a fix in a committed file; and the open rows are the ones with
work owed. I found no row marked closed that the record shows should be
open, with one borderline case (A-S2).

### A.7 Should-fix (none blocks the merge)

**A-S1. Six "checked" rows rest on a check of a version that has changed
since.** The rows for the records-not-on-the-branch finding (RT-256, Gate C
pass), the superseded figure (RT-257), the kill-date rule (RT-258), the
missing heading (RT-260), the dates (RT-268) and the misdescribed record
(RT-270) cite the version 2 check, which ran at `5de5fff`. The file has
changed a good deal since, in commits no check covers:

```
$ git diff --stat 5de5fff origin/main -- docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md
 .../2026-10-07-two-sided-question-PROPOSAL-v2.md   | 194 +++++++++++++++------
 1 file changed, 136 insertions(+), 58 deletions(-)
```

I re-ran four of the checks on the main line's copy and each still holds:
the spec search exits 1 (`grep -n -i 'founding wager\|structure suffices'
spec/minimum-viable-mind-proposal-v0.1.md`); the second release still reads
"about $150 to $172" (line 216); item 23 is still read as "the dates do not
move" (line 321), matching line 280 of the 2026-09-21 ruling; and the date
list now has two more dates, 2026-08-04 and 2026-10-03, both citations (a
file name at line 217 and an addendum's date at line 430), neither a
scheduled step. So nothing is wrong today. But the section header is the only
place that says the check ran at `5de5fff`; each of the six rows should say
"checked at `5de5fff`", so a reader does not take the closure as covering the
later edits.

**A-S2. The control's specification (RT-263) and the undecidable first side
(RT-266) are treated differently on the same facts.** The version 2 check
calls both "Complete" (RT-263 "with one wording slip", RT-266 "on the
demand"), gives each a must-fix item on its fix (items 4 and 5), and both
repairs sit only in the unchecked commit `32c3b78`. RT-263's row is open;
RT-266's is accepted. The method note's own rule ("when unsure whether ...,
the row says 'open'") points to open for RT-266, or the row should say why it
differs (for example, that must-fix item 5 is on new spec text that goes to
its own Gate A, not on the finding's demand). Either way the reader should
not have to work out the difference.

**A-S3. RT-237's row says the closure check "is running separately".** That
describes work in progress and will go stale in the ledger. Say "is owed"
(it is now open as pull request 142, branch `rt237-closure-check`, not yet
merged).

### A.8 Notes for John (decisions, not fixes)

1. **Eight rows are open, though item 12 asked that each be closed.** Item 12
   says the rows are to be written "each closed with 'the claim was checked'
   or 'the argument was accepted'". The rows rightly do not close what the
   record shows is not done; four of the eight (the free model's gate, the
   episode counts, the decoy, the outcome words) are the work the
   2026-10-08 rulings already list as owed before the registration commit.
2. **"Accepted" closures and the protocol's rule for serious findings.** The
   protocol (line 436) asks that, before a registration commit, serious
   findings be "closed the same way" as fatal ones (a measured check) "or
   carried as an open item named in the registered text". Item 12 allows
   "the argument was accepted". Three serious successor findings are closed
   that way: the floor's missing condition (RT-238), the episode format
   (RT-239) and control 6 (RT-251). For RT-251 the outside dispositions even
   named the measured check that would close it ("a search showing no
   sentence claims control 6 separates the two", line 143). Whether item 12's
   "accepted" satisfies the protocol here is for John or the Gate A closure
   check, not for the rows.
3. **The fatal Gate C finding (RT-262) is closed as accepted.** The protocol's
   measured-check rule for fatal findings is written for the time "before a
   registration commit at Gate A" (line 402), and the refounding proposal
   registers nothing; the row says this. Version 5 keeps both releases, so
   the fix has no registered text of its own to check.
4. **Which finding keeps RT-256** is John's call, as the findings note says.

---

## B. Pull request 140: three wording fixes in version 5

### B.1 The diff

```
$ git log --oneline origin/main..origin/v5-wording-leftovers-2026-10-09
ec340fb Fix three wording leftovers in registration text version 5 that the re-check found
$ git diff --stat origin/main...origin/v5-wording-leftovers-2026-10-09
 .../successor-experiment-proposal-2026-10-07-v5.md | 45 ++++++++++++++--------
 1 file changed, 29 insertions(+), 16 deletions(-)
```

### B.2 Every cited commit in the ten rows is on the main line

The ten rows cite fifteen commits. Each was tested on its own:

```
$ git merge-base --is-ancestor 525a625 origin/main; echo "525a625 $?"
525a625 0
135c1f7 0
6136407 0
8da74c4 0
7583326 0
51ec07d 0
644238e 0
e948899 0
1e168f3 0
6794155 0
ba5d64f 0
7278309 0
9acc566 0
5e2faf9 0
b01e564 0
```

All fifteen exit 0: on the main line. "On the main line (each cited commit
verified there 2026-10-08)" is true.

A script (`rows.py`) compared each removed row with its replacement:

```
removed table rows: 10 added table rows: 10
rows identical apart from the one phrase: 10
```

Each row changed only from "on the main line since 2026-10-08 (pull request
136); filed on" to "on the main line (each cited commit verified there
2026-10-08); filed on". Nothing else in any row moved.

### B.3 The paragraph above the table is corrected, and it is accurate

It no longer says the ten rows "sit on fifteen branches that have not
reached the main line" in the present tense; it says they were written when
they did, and adds a dated note that every cited commit is now on the main
line, "several ... through their own pull requests earlier that day, the rest
through pull request 136". Which merge first brought each commit in:

```
$ git log --first-parent --ancestry-path 135c1f7..origin/main --format='%h %ad %s' | tail -1
22f1399 10-08 13:15 Merge pull request #134 from jfredson/gate-a-tier1-successor-v4
(7583326: #109, 13:10; 51ec07d: #106, 13:11; e948899: #121, 13:12;
 6794155: #108, 13:11; 9acc566: #115, 13:11; 5e2faf9: #116, 13:12)
$ git log -1 --format='%ad' --date=format:'%m-%d %H:%M' 9e9daa3      (the merge of pull request 136)
10-08 13:21
$ git merge-base --is-ancestor 525a625 9e9daa3^1; echo $?            (on the main line before pull request 136?)
1
(also 1 for 6136407, 8da74c4, 644238e, 1e168f3, ba5d64f, 7278309, b01e564)
$ git merge-base --is-ancestor 525a625 9e9daa3; echo $?
0
```

Seven commits came in through their own pull requests, all before pull
request 136; the other eight came in with pull request 136. That matches the
new sentence and the re-check's table for its leftover L1.

### B.4 R-13, R-14 and section 11's step 3

```
$ git show origin/v5-wording-leftovers-2026-10-09:docs/successor-experiment-proposal-2026-10-07-v5.md | grep -n "owed its check"
3431:   each by ruling and each checked or owed its check:** the decision code
5709:verified on the main line), the sharpness row's "owed its check", and a note
```

The three places the re-check named (rehearsal items R-13 and R-14, and
section 11's step 3) now say "checked 2026-10-08" and cite
`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`. The two
remaining matches are a general phrase and a change note, both fine. The
check exists on the main line, by a session that wrote none of the work, and
checked the branch the three places name, at the commit they name:

```
$ git log --format='%h %ad %s' --date=short -- docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md
d23be2a 2026-10-08 Check of the sharpness-fix branch: code, bars, cases and every figure reproduce; one must-fix wording range (...); the branch may be merged
$ sed -n 4,6p docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md
work it checks, under the repository's pairing rule. Checked: branch
`fix-sharpness-inuse-check` at its head commit `644238e` (the toy retrain and
```

It also reran "28 of 28 decision-code cases" (its line 209), the figure R-13
quotes. Its one must-fix (arm C's range is 22 to 29 per cent, not 24 to 29)
is already corrected on the main line, both in the findings file (line 190)
and in version 5 (lines 1509 and 4187).

### B.5 No figure, bar, term or stop changed

A script (`nums.py`) compared every number in the removed lines with every
number in the added lines:

```
numbers only in removed lines: {'136': 8}
numbers only in added lines: {'2026': 8, '10': 8, '08': 7, ...}
```

The only number removed is the pull request number 136 (net eight times:
ten removals from the rows, one put back in the paragraph's note and one in
the change note). The numbers added are the dates of "verified there
2026-10-08" and "checked 2026-10-08", and the item and step numbers the new
change note names. Section B.2 shows the ten rows are
otherwise unchanged; the other edits are the paragraph, three
"owed its check" phrases and the change note at the end. No figure, bar,
outcome term or stop condition appears in any changed line except as
unchanged text.

### B.6 Should-fix (outside this pull request's scope; does not block it)

**B-S1. Three other places still credit pull request 136 alone.** On the
branch, line 3386 ("the branches are on the main line, pull request 136"),
line 3444 ("the cited branches are on the main line (pull request 136)") and
line 4622 ("all fifteen branches landed on the main line 2026-10-08, pull
request 136") use the shorthand the re-check's L1 corrected in the table.
Nothing in them is false in substance (every branch is on the main line
since 2026-10-08), and the re-check only named the table, so this is new,
not a missed fix. A later pass can write "pull requests 106 to 136".

---

## Commands not run, and why

No model was called and no code under test was run; this was a check of
records against records. The three scripts this check wrote only read files
and live in the session's scratch folder, not in the repository. The
closure-rule judgement for each row is ARGUED, from the files named above.
