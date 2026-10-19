**Verdict: PASS WITH CONDITIONS.** The spec commit is exact (checksum, three inserts, nothing else changed) and the numbering, rulings and tier 2 coverage of the 22 rows all hold. Four rows need changes before merge: RT-284's closure line miscounts the hits, RT-283's "what closes it" misses a second copy of the same comparison, RT-292 carries a figure the record contradicts and must go to Open, and RT-304 misquotes the Floor sentence. The changes are listed under "Conditions" below.

# Check of pull request 173: ledger rows RT-283 to RT-304, and section 2 version 3 written into the spec

*Filed 2026-10-18 (Sunday, Pacific). The file name keeps the date of the work it
checks (2026-10-17), as the brief named it. Run by a Claude Code session in its own worktree
(branch `check-ledger-rows-and-spec-commit`, cut from the head of pull request
173, the ledger-rows-and-spec-commit branch, at `1a9752e`). This session wrote none of: the
refounding proposal, the Gate A pass of 2026-10-09, the six rulings of
2026-10-12, version 3 of section 2, the closure checks of 2026-10-17, or
either commit of pull request 173. It read no session's chat. $0: no model
called, nothing rented. Nothing under check was edited. Under the pairing
rule of `docs/outside-review-protocol.md`, every finding below is labelled
MEASURED (a command was run and its output is given) or ARGUED (reasoning a
reader can dispute).*

*Scripts and their full output are beside this file, in
`2026-10-17-ledger-rows-and-spec-commit-check-scripts/`:
`check_pr173.py` (checks C1 to C8, reading committed git objects only) with
its output `check_pr173.out.txt`; `check_shell.sh`, plain-shell versions of
checks 1, 5 and 6, with `check_shell.out.txt`; and `pr165_last_comment.md`,
John's rulings of 2026-10-12 as posted on pull request 165, saved with
`gh pr view 165 --json comments --jq '.comments[-1].body'` (SHA-256
`9bb85f30…5f012498b`; posted 2026-10-12T17:43:16Z by the jfredson account). Re-run with
`python3 -I check_pr173.py` and `bash check_shell.sh`.*

## Commits named in this file

| Short id | What it is |
|---|---|
| `a99e8e9` | the main line where pull request 173's branch was cut |
| `2271b7d` | pull request 173, commit 1: the 22 ledger rows |
| `1a9752e` | pull request 173, commit 2 and branch head: section 2 written into the spec, dated note on version 3 |
| `bfd1d5d` | version 3 of section 2 as written (merged by pull request 170 at `03df5e3`) |
| `00b272e` | the closure checks of 2026-10-17, head of pull request 171 (merged to the main line at `57a5c95`; the file is byte-identical there, MEASURED in C3) |

## What was opened, and what was not

Opened and read: the new ledger section (all 22 rows and the four notes
above them); the dated note and the change log of version 3; the comment
on pull request 165; the covering note of the Gate A pass; the tier 1 note's
findings table, its RT-292 check C8 and the RT-283 to RT-295 headings; Gemini's
reply in full; GPT's reply's tables, A1, A5's last paragraph, A10 and its
"Differences from the inside reviewer"; the closure-check file of 2026-10-17
and its script output; both commit messages and the pull request body; the
writing session's hand-over note in the shared notes folder; experiment 1's
`removal_ci.json` and the interval paragraph of its findings file.

Read by script only (for quotes, not read through): the spec before and after;
the 2026-10-07 rulings file; the router-control note; the ledger before the rows.

Not opened: the tier 2 packet, the battery draft, the founding wager,
version 2 of the proposal, `STATUS.md`, `data/project.toml`, the book's
summary. So nothing below checks the rows' claims about those files (RT-302's
list of places ruling 4 still has to reach, for example).

## The six checks in the brief

### (1) One row per number RT-283 to RT-304, none before. MATCHES.

```
$ git show a99e8e9:experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | grep -cE 'RT-(28[3-9]|29[0-9]|30[0-4])\b'
0
$ git show 1a9752e:experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | grep -oE '^\| RT-(28[3-9]|29[0-9]|30[0-4])\b' | sort | uniq -c | awk '{print $1}' | sort | uniq -c
  22 1
```

and from C1 of the script:

```
  highest row number at base: RT-282; at head: RT-304
  rows numbered 283..304 at base: 0 (expected 0)
  base lines mentioning any of RT-283..RT-304 in any form (heading, prose, row): 0 []
  numbers with exactly one row: 22 of 22; with none: []; with two or more: []
  rows numbered above 304 at head: 0
  the 22 rows sit at lines 1280..1301; contiguous and in number order: True
  cells per new row (pipes minus one): [5] (expected [5])
  ledger diff base..commit 1: +145 -0 (expected -0: append only); commit 1..head: no change
  base ledger is a prefix of head ledger: True
```

MEASURED. Before the rows, no line of the ledger named any of the 22 numbers
in any form, not just as a row. After them, each number has exactly one row.
Commit 1 only appends (no line removed or changed) and commit 2 does not
touch the ledger. This matches what the rows and the pull request claim.

### (2) Each row's ruling cell quotes "all as recommended" and names a ruling that exists. MATCHES.

C2 parses the six numbered rulings from the pull request 165 comment and the
numbered list in version 3's change log, then, for every row: is
"all as recommended" quoted, does "Ruled by John 2026-10-12" appear, which
rulings does it cite, is each cited ruling in both sources, does the cited
ruling's text name this finding (its RT number or its Gemini/GPT id), and does
any ruling name this finding without the row citing it?

```
  numbered rulings in the comment: [1, 2, 3, 4, 5, 6]
  numbered rulings in version 3's change-log list: [1, 2, 3, 4, 5, 6]
  the 'closing line' quoted by the rows, in the comment: True
  "everything else is the author's to fix" in the covering note (any case): True
  RT-283 | True | True | - + closing line | True | -
  RT-284 | True | True | [2, 6] | True | {2: True, 6: True}
  RT-285 | True | True | [3] | True | {3: True}
  ...
  RT-302 | True | True | [4, 6] | True | {4: True, 6: True}
  RT-303 | True | True | [3, 6] | True | {3: True, 6: True}
  RT-304 | True | True | [6] | True | {6: True}
  rows failing any part: 0 of 22
```

(Full table in `check_pr173.out.txt`.) MEASURED. All 22 rows quote "all as
recommended". Every ruling a row cites exists in both sources and names that row's
finding. No ruling names a finding whose row fails to cite it. The ten rows
under no numbered ruling cite the comment's closing line, and that line is
quoted as it stands in the comment. ARGUED, one note: the "closing line" is
the comment's "What happens next" paragraph, not a seventh ruling. The rows
say so plainly ("none of the six numbered calls"), so this is not a fault.

### (3) The three closure lines against the closure-check file, sentence by sentence. TWO DIFFER (conditions 1 and 2).

C3 splits each closure cell into sentences. It pulls every quoted phrase,
code span and number out of each sentence and looks for it in the
closure-check file and its output. Only these were not found: the closure
file's own path and "pull request 171" (the closure file does not name itself
or its pull request, which is expected), and RT-283's "lines 249 to 252" (see below).
Then sentence by sentence:

**RT-289, "Closed: the claim was checked".** Every sentence matches.
MEASURED: the closure output has "degree measured" 0 and 0, "at a degree" 0
and 0, "non-zero" 1 in the inserts and the hit is the sentence about Scope's
phrase, "non-zero" in John's unchanged text at lines [10, 14, 149], and
"degree" once in the section, in the "no validated degree" sentence. The row
says each of these.

**RT-284, "Closed: the claim was checked, with one reading stated".** The
fix, the check, the precedence rule, the empty "definition, not an
instrument" group, the reading (ARGUED, as the closure file labels it) and the
"not shown" sentence all match. The line numbers match: C8 finds each
phrase on the stated line of the spec at the branch point (10, 10, 17, 39, 45, 45,
68, 87, 87, 105). **The counts do not match.** The row (and the pull
request body) says "nine hits" and "three of the nine are quoted verbatim;
six are covered by section name or with the phrase altered (the script's
strict substring test flagged those six)". The closure check's output says:

```
    'named ... True': 4; 'named ... False': 6; total hits: 10
    rows of the closure file's table: 9
```

MEASURED. The closure output lists ten hits. Four pass its strict test and six
are flagged. The closure file's table has nine rows because it puts the two
Measuring It hits (both on line 87) in one row, and it describes five hits
as "quoted verbatim". The row's "nine" counts table rows rather than hits,
and its "three" matches neither the output (4) nor the table (5). The
conclusion does not change, since the six flagged are the six the reading
covers, but a closure line is binding text and its numbers should be the
output's. Condition 1.

**RT-283, "Open".** The fix, the counts ("fluency measures" 0, "no better
than" 1 against 0, ruling 10 with its path within 400 characters), the
quoted sentence, the "question and not a finding" guard, and the reference to decision 7
all match the closure file. Two things differ:

- *Line numbers.* The row says "version 3, lines 249 to 252"; the closure
  file says "version 3, lines 176 to 178". MEASURED in C3: the hit is on
  version 3's file line 251, which is line 177 counted from the section's
  first line (line 75). So both are right in their own counting. The row
  uses file lines and the closure file uses section lines, and neither says
  so. No change needed. A reader comparing the two should know this.
- *What the row leaves out.* The row's "What closes it" offers "the sentence
  reworded and the same check re-run ... returning 0". But the same
  comparison is in the spec a second time, under other words, in the
  paragraph added to "What Would Count Against It":

  ```
  $ git show 1a9752e:spec/minimum-viable-mind-proposal-v0.1.md | grep -n -o -E 'no better than in the frontier|no more presence in the constructed systems than'
  196:no better than in the frontier
  365:no more presence in the constructed systems than
  ```

  MEASURED. The closure file quotes both sentences: the second one in its
  RT-283 discussion, as the sixth condition. Its search only finds the first.
  ARGUED: if line 196 alone were reworded, the stated check would return 0
  while line 365 still made the same pre-stated observer comparison. So the
  row's second closure path could close RT-283 by the letter while leaving
  its defect in the spec. Condition 2.

### (4) Every tier 2 finding is a numbered row or a listed duplicate, none missing, none twice. MATCHES.

```
  ids in the two replies' finding tables: 23: G1 G2 G3 G4 G5 G6 G7 G8 G9 A1 A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 A12 A13 A14
  ids with a numbered row: 9: A4 A5 A6 A7 A8 A11 A12 A13 G8
  ids recorded as duplicates in the section note: 14: G1 G2 G3 G4 G5 G6 G7 G9 A1 A2 A3 A9 A10 A14
  missing from both: []
  appearing more than once across both: []
  in the rows but not in the replies: []
  ruling 6's named list ['A4', 'A5', 'A6', 'A7', 'A8', 'A11', 'A12', 'A13', 'G8'] == the numbered rows' ids in order: True
```

MEASURED. All 23 are accounted for, and each appears once. The numbers RT-296
to RT-304 are the ones version 3 gave the same nine findings, in the same
order (C8: `same: True`). Every row's severity matches its sources (C4: the
tier 1 grade, raised to fatal for RT-284 and RT-289 by ruling 6, and the
outside grade for the nine numbered tier 2 rows; 22 of 22 "ok").

Duplicate pairings against version 3's change log (C4): twelve of fourteen
are the same. Two differ, and neither is a fault:

- **A10.** The rows pair it with RT-284, RT-287 *and RT-290*; version 3 pairs it with RT-284
  and RT-287 only. MEASURED in C8: GPT's A10 names the founding wager
  (`founding-wager` is in its text: True), which is RT-290's subject. So the rows
  follow the source more fully than version 3 does. No change.
- **G3.** Version 3 pairs it with RT-288 "with the ordinary competing solver of
  RT-297 as the second half of the answer"; the rows say RT-288 only. ARGUED: this
  is something the source says that the rows leave out. It is small, because RT-297 is
  its own row and G3's number is not in doubt. Optional, not a condition.

### (5) The spec at the branch head: checksum, and only the three inserts. MATCHES.

```
$ git show 1a9752e:spec/minimum-viable-mind-proposal-v0.1.md | shasum -a 256
3d0baaca5fbf1af08d86652e455ca4e0462c98f7fb424fde09292623256df119  -
$ git diff -U0 a99e8e9 1a9752e -- spec/minimum-viable-mind-proposal-v0.1.md | grep -E '^@@'
@@ -19,0 +20,222 @@ ...
@@ -41 +263 @@ ...
@@ -142,0 +365,2 @@ ...
$ git diff -U0 a99e8e9 1a9752e -- spec/minimum-viable-mind-proposal-v0.1.md | grep -c '^-[^-]'
1
```

and from C5, which sorts every added line into one of the three inserts or
layout, and counts whatever is left:

```
  removed line is the Floor anchor line: True; its replacement is the old line + ' ' + the Floor sentence de-quoted and joined: True
  added lines by kind: {'section': 219, 'floor line': 1, 'paragraph': 1, 'blank': 3, 'rule ---': 1, 'other': 0}  (section lines matched in order: 219 of 219)
  spec at head: 377 lines; section heading at line 20; line before it: '---'; '## What This Proposal Is' at line 243, preceded by 2 blank line(s)
  paragraph at line 365; two lines up starts: 'And if the depth mechanisms produced systems that pass the f'
```

MEASURED. The checksum is the one claimed. The spec did not change on the main line
since the branch point (`git diff --stat a99e8e9 origin/main` on it is empty), so
"against the main line" and "against the branch point" give the same diff. Every added line
is section text, the joined Floor line, the joined paragraph, a blank
line or the one `---` rule after the section. Nothing else was added. The
single removed line is the Floor anchor, and its replacement is that line plus the
Floor sentence, byte for byte. The layout notes in the pull request (no
blank line after Scope's rule, two blank lines before "What This Proposal
Is", the section heading at `###` where the spec's sections are `##`) are
all borne out.

### (6) The inserted section equals version 3's lines 75 to 293, and version 3 below its note equals `bfd1d5d`. MATCHES.

```
$ diff <(git show bfd1d5d:docs/rulings/2026-10-12-two-sided-question-section-2-v3.md | sed -n 75,293p) <(git show 1a9752e:spec/minimum-viable-mind-proposal-v0.1.md | sed -n 20,238p) && echo IDENTICAL
IDENTICAL
$ diff <(git show bfd1d5d:docs/rulings/2026-10-12-two-sided-question-section-2-v3.md) <(git show 1a9752e:docs/rulings/2026-10-12-two-sided-question-section-2-v3.md | sed 3,25d) && echo IDENTICAL
IDENTICAL
```

and from C6: both blocks are 14,679 bytes with SHA-256 `5bbf98bc…6ff8b01e`.
Version 3's line 294 is blank and line 295 is `---`. Version 3 did not change between
`bfd1d5d` and the branch point. The diff of version 3 from `bfd1d5d` to the
branch head is one block of 23 added lines (the note and its blank line)
with nothing removed. MEASURED. The section in the spec is version 3's lines
75 to 293 byte for byte. With the note's 23 lines (its lines 3 to 25) taken out, version 3 is exactly what
`bfd1d5d` merged.

## Beyond the six: what the rows say that the sources do not

**Every quoted phrase in the new section was looked for in the sources (C7).**
163 double-quoted phrases. Each was found word for word in at least one source,
once a quotation inside a quotation is allowed to flip its marks. MEASURED. A stricter
test then asked: is each phrase a row presents as "Applied ..." text actually
in the applied text (the section, the Floor sentence and the paragraph)?
Six are not. Four are headings or phrases named as removed ("What This
Proposal Is", "What Would Count Against It", "section 10", "the identity"),
which is correct. One is a near-paraphrase carried over from version 3's change log ("the
reference profile"; the text says "a reference profile" and "the frontier
reference profile"). That is harmless and no change is asked. The sixth is a misquote:

```
    "this project's definition of the floor and not" in the Floor sentence: False; in section 2: False; in version 3's change log: True
    'treats the test as its definition of the floor and not as an instrument for it': Floor sentence True; section 2 False
    "this project's definition of the floor, not its instrument for it": Floor sentence False; section 2 True
```

MEASURED. RT-304's row says the Floor sentence calls the removal test "this
project's definition of the floor and not ... an instrument for it". The
Floor sentence's words are "this project treats the test as its definition
of the floor and not as an instrument for it". The row's wording comes from
version 3's change log, which itself paraphrases. Condition 4.

**RT-292's "each interval above zero" is contradicted by the record (C8).**
RT-292's row says it was not re-checked ("no session has re-run that read
against version 3's rounded figures"). This check re-ran it:

```
    drop on T_self_irrelevant: 0.2188 [0.0938, 0.3750]  lower bound above zero: True
    drop on T_self_relevant: 0.1000 [0.0000, 0.2000]  lower bound above zero: False
    drop on T_syntax: 0.1333 [0.0333, 0.2667]  lower bound above zero: True
    router gap: +0.0333 [-0.1333, +0.2000]
    the Floor sentence (now spec line 263) says 'each interval above zero': True
    the RT-292 row says it too: True
    the findings file's own word for a lower bound of 0.000: ['lower bound touches zero']
```

MEASURED. The figures 0.22, 0.10, 0.13, +0.033 and −0.133 to +0.200 all match
the interval file. The clause "each interval above zero" does not hold for the
self-relevant drop: its interval is [0.0000, 0.2000]. Experiment 1's findings
file calls a lower bound of 0.000 one that "touches zero" (its words about the
headline differential). ARGUED: "above zero" is therefore true of two of the
three intervals, and the sentence now in the spec (line 263) says it of all three. This is
version 3's error, and commit 2 wrote version 3 faithfully, as it was asked to. But
RT-292's row marks the finding "Closed: the argument was accepted" and repeats
the clause as applied. By the ledger's own closure words, a finding whose
fix a measured check contradicts is "Open". Condition 3.

**Smaller things, no change asked.** The new section's top heading is a single `#`,
as are eleven earlier sections of the ledger besides its title (C8), so it follows the
ledger's own practice. The section's count line (checked 2, accepted 18,
open 2) matches the closure words on the 22 rows (C8). Condition 3 changes it.

## Conditions (each a change to make before merge)

1. **RT-284's closure line, and the pull request body:** replace "nine hits"
   with "ten hits (nine rows in the check file's table; line 87 holds
   two)", and "three of the nine are quoted verbatim; six are covered ..." with
   "four pass the script's strict substring test and six are flagged; the six
   are covered by section name or with the phrase altered".
2. **RT-283's closure line, "What closes it":** add that the same
   comparison stands a second time in the paragraph added to "What Would Count
   Against It" (spec line 365, "may detect no more presence in the
   constructed systems than in the frontier reference profile"), which a
   search for "no better than" does not find. Then say either closure covers both
   places: John's ruling that both stand, or both reworded, with the re-run
   check searching for both wordings.
3. **RT-292's row:** change the closure from "Closed: the argument was
   accepted" to "**Open.**" and record this check's output (the self-relevant
   drop is 0.1000 with interval [0.0000, 0.2000]; the record calls such a
   bound one that touches zero). In the Disposition cell, mark "each interval
   above zero" as version 3's words that this check contradicts, not as the record's. Say what closes it:
   the clause corrected in version 3's Floor sentence and in spec line 263
   (for example "two of the three intervals above zero and the third
   touching it") by a session that did not write version 3, then
   re-checked; or John's ruling that it stands. Update the section's count
   line to accepted 17, open 3. Correcting spec line 263 changes the spec's
   checksum. That is John's call, and this check does not ask for it before the
   merge, only that the row says it is open.
4. **RT-304's row:** quote the Floor sentence as it reads: the removal test
   is what "this project treats ... as its definition of the floor and not as
   an instrument for it".

Nothing else needs to change. The spec commit itself (checks 5 and 6) passes as it stands.

## For John, not decided here

- Whether to merge the spec commit with "each interval above zero" in it
  and fix it afterwards, or fix version 3 and the spec first (condition 3
  allows either).
- The writing session's three open questions (RT-283's sentence, RT-292's
  grade, RT-287's closure choice) stand as they put them. Condition 2 adds the
  second sentence to the first of those.
