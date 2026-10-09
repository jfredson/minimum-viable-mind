# Re-check of pull request 153 after its fixes (the last batch before the registration)

*2026-10-08 (night, Pacific). Claude Code, as the re-checker, committed on top
of branch `check-final-batch` (pull request 154, base main). I wrote none of
what I check: not the batch, not the first check
(`docs/reviews/2026-10-08-final-batch-check-claude-code.md`), and not the fix
commit. The fix is commit `ed4b7ca` on branch
`final-batch-before-registration`, now the head of pull request 153 (base
main, confirmed with `gh pr view 153`). It touches two files: version 5 of the
proposal (`docs/successor-experiment-proposal-2026-10-07-v5.md`) and the
red-team ledger. Nothing needed re-running; this is a re-read. Laptop only,
$0. I fixed nothing.*

## Verdict: ready to merge

Both must-fix items and all four should-fix items are fixed as the first check
asked. The new heading notes in sections 5.2 and 5.3 are true. No figure, bar,
term or stop changed. The ledger row keeps its column count. Three small
things are left, none of which blocks the merge (end of this note).

## 1. The two must-fix items: fixed

**Must-fix 1, done work still called owed, in three places.**

- Section 10, the page 4 re-run paragraph (now lines 3382 to 3385): "must be
  summarised again ... before it is quoted as an outcome" is replaced by "has
  since been summarised again with the current decision code (R3, with arms C
  and M withheld by the in-use check; section 17, failure 4; [the findings of
  the ruled code changes])". Fixed.
- Section 17, failure 4, the bullet "The toy's own outcome line" (now lines
  5157 and 5158): "is to be summarised again (section 10)" becomes "has since
  been summarised again under the current decision code: R3 (see the note
  above)". Fixed.
- Section 17, "What this pass leaves open, in one place" (now lines 5202 to
  5204): "the work items 7, 8, 9 and 12 ask for is still owed" becomes "the
  work items 7, 9 and 12 ask for is done and checked, and item 8's test with a
  differently coded decoy is still owed". That is exactly the split the first
  check gave (the fitting limit and episode count, and the three reporting
  changes, done in pull requests 151 and 152; the ledger rows written; only
  the decoy test still to do). Fixed.

**Must-fix 2, section 5.3's heading over the figures fitted on 420.** The
heading now reads "What the toy measured with every read fitted on 420
episodes, under the rules this version registers otherwise (the registered
fitting count of 1,800 gives the figures later in this section; ...)". The
author applied the same change to section 5.2's heading, which had the same
fault (it sat over arm C's 1.0051, 0.9926 and 0.9974). Fixed in both.

## 2. The four should-fix items: fixed

1. **Section 7.1's note on the held-out episodes** (now lines 1864 to 1866):
   "the toy's reads before 2026-10-08 held out the last 180 of 600" becomes
   "as in the page 4 re-run of 2026-10-06; the toy's earlier reads, fitted on
   420, held out the last 180 of 600". True: the run-time wrapper of the page
   4 re-run holds out 180 at either pool size, so 600 gives 420 fitted.

   ```
   $ git show ed4b7ca:experiments/rehearsal-successor-measure/src/page4_models_1800.py | grep -nE "HELD|1980"
   33:    $PY page4_models_1800.py --pool 1980 --out ../out-page4-rerun-1800/models-1800 --arm T --seed 0
   60:HELD = 180                          # the last 180 of the pool are held out, at every pool size
   66:    n_tr = len(y) - HELD
   128:    ap.add_argument("--pool", type=int, choices=(600, 1980))
   ```

2. **Section 9's sources columns.** Arm M's row now cites "the toy figures
   fitted on 1,800 from the page 4 re-run at `e948899` (checked at
   `1e168f3`), reproduced at the 10,000 limit
   (`docs/2026-10-09-ruled-code-changes-and-page4-rerun-findings.md`); the
   figures fitted on 420 from the review of version 3, RT-231, and the controls
   re-run at `821f154`". The episode-count row now ends "the iteration limit of
   10,000, item 7 of `docs/rulings/2026-10-08-v5-open-items-rulings.md`". Both
   commits exist (`git cat-file -t`: commit, commit), both files exist at
   `ed4b7ca`, and item 7 of the rulings file reads "Raise the limit to 10,000".
   Fixed. One citation is a little short of what the first check suggested;
   see what is left, item 2.
3. **Section 3's toy sentence** (now lines 599 to 602) gains: "The separation
   and arm M's band below are each toy row's own arithmetic: the current
   decision code withholds arms C and M on every toy seed by the in-use check
   (these toy models were trained with the sharpness learned), so its summary
   computes no separation". This is what the findings asked for (their
   section 3, item 4), and the reason in brackets is the findings' own (their
   lines 57 to 59). Fixed.
4. **The ledger row for the outcome map's holes (RT-241).** Its closure cell's
   last sentence, "are not yet in the code; that is the open item on RT-250's
   row", becomes "are printed by the code since 2026-10-08 (pull request 151,
   checked in pull request 152), which closed RT-250". Fixed.

## 3. The heading notes in sections 5.2 and 5.3 are true

Each heading now promises that "the registered fitting count of 1,800 gives
the figures later in this section". Both sections deliver, below their
heading and before the next section starts:

```
$ grep -nE "^### 5\.(2|3)" v5.md
1027:### 5.2 Arm C: the ownership answer entangled, by construction
1172:### 5.3 Arm M: a mixture of the two, by item
$ grep -nE "1,800|1\.0026" v5.md | awk -F: '$1>=1027 && $1<1300'
1047:rules this version registers otherwise (the registered fitting count of 1,800     <- 5.2's heading
1161:**The toy figures for this arm with every read fitted on 1,800 development      <- 5.2's 1,800 paragraph
1165:directions right on 178 of 180, reading 1.0026; seed 1, now state 4 at the
1235:rules this version registers otherwise (the registered fitting count of 1,800     <- 5.3's heading
1273:**With every read fitted on 1,800 development episodes (ruled 2026-10-06,         <- 5.3's 1,800 paragraph
```

Section 5.2's paragraph at line 1161 gives arm C at 1,800: 1.0026, 1.0000 and
1.0000, the pieces 178, 178 and 165, and calls the table at 420 "the earlier
record". Section 5.3's paragraph at line 1273 gives arm M at 1,800: 0.5252,
0.4793 and 0.5208, within 0.0252, 0.0033 and 0.0288 of the true-slot reading,
and calls the 420 figures "the earlier record". Both match section 9's row and
section 3. (`v5.md` here is `git show ed4b7ca:` of version 5, saved to this
session's scratch folder.)

## 4. Leftovers in version 5

```
$ grep -nE "0\.4886|1\.0051|owed|summarised again|rules this version registers|to be re-summarised|not yet in the code|still fits on 420|last 180 of 600" v5.md
```

Every hit, by kind:

- **True statements of work still to do:** line 27 and 33, the header (item
  8's decoy test is still owed before the commit); line 630 and 1556, the
  eleven re-reads of the hand-set toy models (section 17 lists them as open
  too); line 3373, the same eleven; line 4635 and 5209, the check of this
  version and the reviewer's own pass; line 5204, item 8.
- **History, labelled as history or quoted from a superseded record:** line
  531 (the review of version 3's range); 612 ("at the earlier fitting count of
  420"); 1052, 1058, 1069, 1097 and 1239 (under the two fixed headings, or
  the forecast this version says it does not use); 1248 ("which version 3
  listed as owed", now done); 3221 and 3222 (section 10's R-3, followed at once
  by the 1,800 figures "as now registered", as the first check found); 3239
  ("is done"); 5041, 5042 and 5054 (the code-block output of an earlier pass);
  5139 (a code block whose output line says "to be re-summarised", with the
  dated note under it saying it was); 5456 (section 20's page 4 entry, which
  says the 420 figures are superseded); 5609, 5610 and 5649 (section 21's
  items, which its header at line 5535 says are "kept as they stood before the
  rulings").
- **The fix's own change notes:** 5801, 5803; and 5748, an earlier change
  note.
- **Not about owed work at all** ("showed", "followed", or a quoted command):
  lines 49, 406, 408, 1407, 2646, 4412, 5004; and 958, which says two things
  version 4 called owed now exist.
- **The source table at the top:** 83, 84, 107, 108 and 121 are rows about
  other records (rulings of 2026-10-03 to 2026-10-07 and their checks, one
  saying "owed a check", one saying version 3 wrongly called a check owed);
  none concerns items 7, 9 or 12. I did not re-trace whether each of those
  older checks has since landed; that is outside this batch.
- **The fixed places themselves:** 1047, 1235 and 3109 (the two headings and
  section 9's row) and 1866 (section 7.1's note).
- **Two places where an old figure or label is used but not called
  registered,** both left (see what is left, items 1 and 3): line 987, section
  5.1's arm T paragraph; lines 1660 and 3243, which give "arm C at 1.0051" as
  the example of a reading above one.

No place calls the work of items 7, 9 or 12 owed, and no place presents arm C's
or arm M's 420 figures as the registered ones.

## 5. The ledger row keeps its column count

```
$ for f in ledger-main.md ledger-6c47c56.md ledger-ed4b7ca.md; do  # main, the batch, the fix
    RT-241 cells: grep '^| RT-241 ' | awk -F'|' '{print NF-2}'
    every table line: awk -F'|' '{print NF-2}' | sort -n | uniq -c
  done
ledger-main.md    RT-241: 5   all table lines: 23 of 4; 232 of 5; 20 of 6; 1 of 8
ledger-6c47c56.md RT-241: 5   all table lines: 23 of 4; 232 of 5; 20 of 6; 1 of 8
ledger-ed4b7ca.md RT-241: 5   all table lines: 23 of 4; 232 of 5; 20 of 6; 1 of 8
RT-241's pipe count, before and after the fix: 6 and 6
RT-241's first four cells, before and after: identical (cmp)
the table's header (line 344): | ID | Finding | Severity | Ruling | Reason / closure |   (5 cells)
```

(This counts cells between the outer pipes; the first check counted awk fields,
which is two more, 7, for the same row.) Only the closure cell changed, and
only its last sentence.

## 6. No figure, bar, term or stop changed

```
$ git diff --stat 6c47c56 ed4b7ca
 docs/successor-experiment-proposal-2026-10-07-v5.md                | 49 +++++++++++-----
 experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md    |  2 +-
$ git diff -U0 6c47c56 ed4b7ca > fix.diff     # 10 changed places in all
numbers on removed lines that are missing from added lines: none
numbers on added lines that are missing from removed lines: 09, 1, 151, 152, 168, 17, 5.2, 7.1, 948899
```

The added-only numbers are the date in a file name (`2026-10-09-...`), pull
request numbers 151 and 152, section numbers 5.2, 7.1 and 17, and pieces of the
commit names `e948899` and `1e168f3`. No reading, bar, count or limit is added,
removed or altered. No code, bar, registered term or stop condition is touched:
the only changes are the eight wording places in version 5, its change note,
and the one ledger cell.

## What is left, one line each

1. Section 5.1's arm T paragraph (line 987) still says "under the rules this
   version registers" over figures from the 420 re-run at `821f154`; harmless,
   since the page 4 comparison shows every arm T field identical at 1,800
   (`out-page4-rerun-1800/comparison.md`: no arm T line differs), but its
   source could add the page 4 re-run.
2. Section 9's arm M row cites the findings of pull request 151 for the
   10,000-limit reproduction but not the check of it
   (`docs/reviews/2026-10-09-ruled-code-changes-check-claude-code.md`, pull
   request 152), which the first check also named.
3. Section 6.3 (line 1660) and section 10's R-4 (line 3243) give arm C's 1.0051
   (fitted on 420) as the example of a reading above one; at 1,800 arm C reads
   1.0026, still above one, so the point holds.
4. Not in this batch and outside the brief, found on the way: section 5.6
   (line 1465, also on main) still says the sharpness fix "is owed its
   independent check before the reruns", while section 10's R-15 and section
   11 say it was checked 2026-10-08
   (`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`).
5. The 420 headings say "under the rules this version registers otherwise";
   the 420 reads also ran at the old iteration limit of 3,000
   (`rerun_controls.py` at `821f154`), so "otherwise" is a touch loose; no
   figure is affected.

## Commands, in order

    git fetch origin
    git show origin/check-final-batch:docs/reviews/2026-10-08-final-batch-check-claude-code.md
    git show --stat ed4b7ca; git show ed4b7ca
    git show ed4b7ca:docs/successor-experiment-proposal-2026-10-07-v5.md > $SCRATCH/v5.md
    sed -n and grep over $SCRATCH/v5.md, as in sections 3 and 4
    git show ed4b7ca:experiments/rehearsal-successor-measure/out-page4-rerun-1800/comparison.md | grep -E "^\| T/" | grep -v "| yes |"   # no lines
    git grep -nE "max_iter" 821f154 -- experiments/rehearsal-successor-measure
    git show <main | 6c47c56 | ed4b7ca>:experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md > $SCRATCH/ledger-*.md, then grep and awk, as in section 5
    git diff -U0 6c47c56 ed4b7ca > $SCRATCH/fix.diff, then the number comparison of section 6
    git cat-file -t e948899; git cat-file -t 1e168f3
    gh pr view 153 --json baseRefName,headRefName,state,headRefOid   # base main, head ed4b7ca
    gh pr view 154 --json baseRefName,headRefName,state              # base main

`$SCRATCH` is this session's scratch folder; nothing there is committed.

## What this does not do

It fixes nothing, and edits neither version 5, the ledger, the code nor pull
request 153's branch. It merges nothing and spends nothing.
