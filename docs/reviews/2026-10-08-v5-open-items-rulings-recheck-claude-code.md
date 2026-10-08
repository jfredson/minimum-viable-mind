# Re-check of the fixes to the branch that records John's answers to version 5's open items (2026-10-08)

*Written 2026-10-08 (Thursday night, Pacific) by a Claude Code session that
wrote none of the work and none of the first check. Laptop only; $0. Checked:
the fix commit `b58eb62` ("Apply the check of the open-items write-in") on
branch `v5-open-items-rulings-2026-10-08` (pull request 137, base main, still
open, head `b58eb62`), against the first check
(`docs/reviews/2026-10-08-v5-open-items-rulings-check-claude-code.md`, this
branch, pull request 138). Nothing was fixed here.*

## Verdict

**Ready to merge.** All three must-fix items of the first check are fully
fixed, every should-fix item was applied, the fix changed no figure, bar or
stop, and the site data validates. Three small pieces of stale wording are
left (below, L1 to L3). None changes a figure or a rule, and none blocks this
merge, but each should be cleared before John's registration commit, since
the registration text is what that commit freezes.

## How it was checked

```
git fetch origin
git log --oneline origin/main..origin/v5-open-items-rulings-2026-10-08
  b58eb62 Apply the check of the open-items write-in: three must-fix items and the should-fix items
  31c6931 Record John's answers to the eleven open items of registration text version 5, and write them in
git show --stat b58eb62
  data/project.toml                                  |  2 +-
  data/roadmap.toml                                  |  2 +-
  .../2026-10-08-flat-models-ruling-confirmed.md     | 15 ++++--
  docs/rulings/2026-10-08-v5-open-items-rulings.md   | 11 +++--
  .../successor-experiment-proposal-2026-10-07-v5.md | 53 +++++++++++++++-------
git show origin/v5-open-items-rulings-2026-10-08:docs/successor-experiment-proposal-2026-10-07-v5.md > v5new.md
git diff b58eb62^ b58eb62 > fix.diff
```

Line numbers below are in `v5new.md`, the branch's copy of version 5.

## The three must-fix items

**M1, stop S4b now carries the hand-set model (arm T): fixed.** The stop
list's definition (line 3580 onward) now reads: "(the stirred-in model or the
half-and-half model fails the in-use check at the bar section 5.6 fixes; and,
ruled 2026-10-08, open item 6, `docs/rulings/2026-10-08-v5-open-items-rulings.md`,
the hand-set model too) or do not do the task (fail their gate on learning)".
That matches section 5.6 (line 1500: "A failure of arm T's rerun, its in-use
check or its gate, also stops experiment C") and step 4b (line 3470). The
2026-10-07 ruling's own sentence at line 1493 is left as history, as the
first check advised.

**M2, section 9's two rows no longer call their items unruled: fixed.** The
training recipe row now ends "**ruled 2026-10-08** (open item 5,
`docs/rulings/2026-10-08-v5-open-items-rulings.md`)"; the spending alarm's
cadence row now ends "confirmed 2026-10-08 in
`docs/rulings/2026-10-08-flat-models-ruling-confirmed.md` (open item 2)".
A search for leftovers:

```
grep -n -i "not ruled\|no rulings file" v5new.md
902:  **The diagnosis, ARGUED and not ruled.** ...   (a different matter, unchanged)
5508: *Meanwhile:* the text carries the coded bars and says they are not ruled.   (section 21, as drafted)
5521: 2. **The 2026-10-06 ruling on the flat-models packet has no rulings file.**   (section 21, as drafted)
5650, 5666: earlier change notes quoting old words
```

None is a current claim that item 2 or item 5 is unruled.

**M3, the confirmation file: fixed, and its new citation is accurate.** In
`docs/rulings/2026-10-08-flat-models-ruling-confirmed.md` the "continue only
if the built route is shown to hold" condition is no longer a bullet under
"What that confirms". It now sits in a paragraph that opens "Not part of this
confirmation, and noted here only so the reader is not misled", says the
method notes do not record it as ruled on 2026-10-06, and says it is ruled by
the stop condition John added on 2026-10-07. Against the source:

```
git show origin/main:docs/rulings/2026-10-07-two-sided-question-rulings.md | grep -n -A12 "stop condition"
58:  **Addition, ruled later the same day (2026-10-07), in John's words "Yes,
59:  add the stop condition to decision 3."** If the verification of the repair
...
64:  release is not spent. This is the condition the ruling packet on the two
65:  flat models stated (continue only if the built route is shown to hold;
66:  otherwise stop or redesign), ...
```

John's words are quoted exactly, the file path is right, and the 2026-10-07
ruling itself says its stop condition is the packet's continue condition, so
"it is ruled by a later decision" is supported. With the condition moved out
of the confirmed list, the closing line "It adds nothing the method notes did
not already report" no longer contradicts the body.

## The should-fix items

| First check's item | What the fix did | Standing |
|---|---|---|
| S1, section 10's "What happens next" | dated note added: check and re-check done (pull requests 130, 132), every open item ruled, branches on the main line; closure check, owed work and John's commit remain | applied |
| S1, weakness W18 | "was open item 8; ruled 2026-10-08 ... to run before the registration commit, or, failing that, before step 5b with this weakness named" | applied |
| S1, the source table's ten "unmerged" rows | each now "on the main line since 2026-10-08 (pull request 136); filed on branch ..."; the sharpness row's "owed its check" now cites its check | applied; see L1 and L2 |
| S1, "What this version does not do" | dated note: "John has since ruled all twelve on 2026-10-08" | applied |
| S2, step N42 (the site's record of the rulings) said two reporting changes "are made" | now "approved (the code for them is owed, N43)", N43 being the site's step for the owed work; consistent with version 5's own "code changes of items 3, 7 and 9" (line 5691) | applied |
| S3, the rulings file's account of where the packet differed from section 21 | now names items 10 and 12 (updated to the main line's state), item 3 (section 21's own alternative words) and item 9 ("no, for now") | applied; item 12 is still called "updated" though its text matched section 21 and only its fact was re-confirmed, a nuance, left |
| S4, roadmap goal W3.2 | note added: two of three parts done (pull requests 130, 132, 136); the commit remains; status stays planned | applied |

**Every cited commit is on the main line.** The fifteen branch commits the
source table's ten rows name:

```
git merge-base --is-ancestor <commit> origin/main; echo $?
525a625 0   135c1f7 0   6136407 0   8da74c4 0   7583326 0
51ec07d 0   644238e 0   e948899 0   1e168f3 0   6794155 0
ba5d64f 0   9acc566 0   7278309 0   5e2faf9 0   b01e564 0
```

All fifteen are on main, every file the ten rows name exists on main
(`git ls-tree -r --name-only origin/main`), and the sharpness check the row
now cites (`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`) is on
main and checks `644238e`. The date "since 2026-10-08" is true for every row.
The pull request number is only partly true (L1).

## Checked that the fix changed nothing else

```
grep '^-[^-]' fix.diff | grep -oE '[0-9][0-9.,$]*[0-9]|[0-9]' | sort -u > old_nums
grep '^+[^+]' fix.diff | grep -oE '[0-9][0-9.,$]*[0-9]|[0-9]' | sort -u > new_nums
comm -23 old_nums new_nums      (numbers removed)  ->  none
comm -13 old_nums new_nums      (numbers added)    ->  130 132 136 138 43
```

No number was removed. The only numbers added are pull request numbers (130,
132, 136, 138) and the site step number 43. Reading the whole diff: the
changes in `data/project.toml` and `data/roadmap.toml` are one line each (N42's
wording, W3.2's note); the version 5 edits are the rows, notes and stop wording
listed above, plus a new closing change note that describes them. No bar,
figure, stop or outcome term moved beyond arm T's addition to S4b, which is
the ruling itself. STATUS.md is untouched, which is correct: the fix adds no
new "where things stand" entry.

## The site check

```
git checkout -q --detach origin/v5-open-items-rulings-2026-10-08     (at b58eb62)
python3 scripts/export_site.py --check; echo "exit=$?"
export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 24 findings, 43 next steps, 48 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
exit=0
```

## Left (should-fix, before the registration commit; none blocks this merge)

**L1. Seven of the ten source-table rows credit the wrong pull request.**
Each row now says "on the main line since 2026-10-08 (pull request 136)". For
three rows that is exact. For seven, the branch commit named reached main
through its own pull request earlier the same day, and only the checks
beside it came in with pull request 136 (whose description says it merged
"the registration-review branch ..., the four updated drafting branches with
their checks, the sharpness branch ... and its check"). Which main-line merge
first brought each commit in:

```
git log --first-parent --ancestry-path <commit>..origin/main --format='%h %s' | tail -1
```

| Row | Branch commit | First reached main through |
|---|---|---|
| the twelve-page ruling on the review of version 4 | `525a625` | pull request 136 |
| the two outside reviews | `6136407`, `8da74c4` | pull request 136 |
| the sharpness fix and in-use check | `644238e` | pull request 136 |
| the inside Gate A review of version 4 | `135c1f7` | pull request 134 |
| the flat-models ruling packet | `7583326` | pull request 109 |
| the check of the four development runs | `51ec07d` | pull request 106 |
| the page 4 toy re-run | `e948899` (its check `1e168f3`: 136) | pull request 121 |
| the decoy test | `6794155` (its check `ba5d64f`: 136) | pull request 108 |
| the training exclusion | `9acc566` (its check `7278309`: 136) | pull request 115 |
| the spending alarm's fixes | `5e2faf9` (its checks `b01e564`: 136) | pull request 116 |

Nothing a reader relies on is false (all are on main, all since 2026-10-08),
and the same shorthand ("the fifteen branches merged, pull request 136") is
in STATUS, the site and the first check. A plain fix: "on the main line since
2026-10-08 (the landing of the fifteen branches, pull requests 106 to 136)",
or the exact number per row.

**L2. The paragraph above the source table still says the rows are
unmerged.** Lines 70 to 74: "**Ten of them sit on fifteen branches that have
not reached the main line**, and are cited by branch and commit; each is
marked 'unmerged' and listed again in section 16. The registration commit
cannot be made until they are on the main line". The rows below it no longer
say "unmerged", so the paragraph now contradicts its own table. It needs the
same kind of dated note the header and section 16 already carry.

**L3. Three other places still say the sharpness branch is "owed its
check".** The fix cleared the source-table row but not these:

```
grep -n "owed its check" v5new.md
3322:  owed its check). The registered runs use this code unchanged. *Exercised.*      (rehearsal item R-13)
3345:  learning and for the fix; eleven of twelve re-reads owed; owed its check.*      (rehearsal item R-14)
3430:  in-use check (branch `fix-sharpness-inuse-check`, owed its check); the         (section 11, step 3)
5705:  ... the sharpness row's "owed its check" ...                                    (the new change note, history)
```

The check is `docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`
(pull request 135, merged with pull request 136). The first check did not
name these three, so this is new, not a missed fix.

Two other "unmerged" mentions are fine as they stand: line 4995 is a quoted
command output from when version 5 was drafted, and line 5591 is section 21's
original text.

## Cannot be checked

The packet John answered and its numbering live only in the chat, as the first
check said; the rulings file's new sentence on where the packet differed from
section 21 (items 3, 9, 10 and 12) matches the caller's account given to the
first check.
