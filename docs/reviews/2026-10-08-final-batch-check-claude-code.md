# Check of pull request 153 (the last batch before the registration)

*2026-10-08 (night, Pacific). Claude Code, as the checker, on branch
`check-final-batch`, cut from the main line at `362e2a2` (the merge of pull
request 152). I wrote none of what I check: not the table fix, not the
version 5 edits, not the ledger rows, and none of the findings or checks they
rest on. The pull request is branch `final-batch-before-registration`, one
commit, `6c47c56`, base main (confirmed with `gh pr view 153`). Laptop only,
processor only, $0. I fixed nothing; every item below is for the author.*

## Verdict: not ready to merge, two wording fixes away

The code fix is right and is the one number it claims to be. The ledger
closures are right, and the count note is exact. Version 5's new statements
match the findings and their check, figure for figure. But in version 5,
three places still say that work this batch records as done is still to do.
And one heading still calls the figures fitted on 420 episodes the toy's
figures "under the rules this version registers". Both are short wording
fixes. A re-read of just those lines by a session that did not make them is
enough after that; nothing needs re-running.

## Must-fix

1. **Three places in version 5 still say finished work is still to do.**
   - Section 10, the page 4 re-run paragraph (branch lines 3375 to 3377): "its
     outcome line was made under the rules frozen before pull request 105 and
     must be summarised again with the current decision code before it is
     quoted as an outcome". This batch records that the re-summary is done
     (R3, section 17 failure 4's new note). The findings name this paragraph
     too (their section 3, item 4).
   - Section 17, failure 4, the bullet "The toy's own outcome line" (lines
     5150 and 5151): "The page 4 re-run's outcome line was made under the
     pre-A2 rules and is to be summarised again (section 10)". This sits
     fifteen lines below the new note saying the re-summary was done, in the
     same failure.
   - Section 17, "What this pass leaves open, in one place" (lines 5193 to
     5195): "the work items 7, 8, 9 and 12 ask for is still owed". Items 7 and
     9 (the fitting limit and episode count; the three reporting changes) are
     done and checked (pull requests 151 and 152). Item 12 (the ledger rows)
     has its rows written, and this batch closes three more. Only item 8 (the
     test with a differently coded decoy) is still to do. The batch edited the
     next clause of this same sentence and left this one.
2. **Section 5.3 still labels the figures fitted on 420 episodes as the
   registered ones** (lines 1229 to 1232): "What the toy measured, under the
   rules this version registers ... The blind reading is 0.4886, 0.4860 and
   0.5449". Those are the figures fitted on 420 episodes. Under the rules this
   version registers (every read fitted on 1,800 of 1,980, limit 10,000) they
   are 0.5252, 0.4793 and 0.5208, as the paragraph at line 1266 and the
   corrected row in section 9 both say. The paragraph at line 1274 calls the
   420 figures "the earlier record", so the section contradicts itself. The fix
   is to the heading's words only, for example "under the rules of version 4,
   with every read fitted on 420". This is exactly the kind of place the batch
   set out to remove (the check of pull request 152, should-fix S2.3, found the
   same fault in section 9's row, which this batch fixed).

## Should-fix

1. **Section 7.1's new note on the held-out episodes is wrong about the
   2026-10-06 reads** (lines 1857 to 1859): "the toy's reads before
   2026-10-08 held out the last 180 of 600". The page 4 re-run of 2026-10-06,
   whose figures this text quotes, already held out the last 180 of 1,980.
   Its run-time wrapper sets `HELD = 180`, "the last 180 of the pool", with
   `--pool 1980` (`experiments/rehearsal-successor-measure/src/page4_models_1800.py`,
   lines 33, 60 and 153). Only the reads fitted on 420 held out the last 180
   of 600. Suggested words: "the toy's reads fitted on 420 held out the last
   180 of 600".
2. **Section 9's arm M row has the new figures but the old sources** (line
   3102). The sources column still cites only the review of version 3 and the
   controls re-run at `821f154`, which are the sources of the 420 figures. It
   should also cite the page 4 re-run (`e948899`, checked at `1e168f3`) and the
   re-run under the frozen code (pull request 151, checked in pull request
   152). The episode-count row just below now names the limit of 10,000, but
   its sources column does not cite item 7 of
   `docs/rulings/2026-10-08-v5-open-items-rulings.md`, which set that limit.
3. **Section 3's toy sentence is not yet qualified** (lines 596 to 599: "the
   anchors separate, the middle model reads in its band"). The findings (their
   section 3, item 4) ask for version 5 to say that, under the current
   decision code, the toy summary withholds arms C and M by the in-use check,
   so the separation and arm M's band are figures from each row's arithmetic,
   not from the summary. The batch says so only in section 17, failure 4.
   Section 3 is where a reader meets the sentence.
4. **The ledger row for the outcome map's holes (RT-241) still says the new
   words are not in the code.** Its closure cell, unchanged by this batch,
   ends: "The renamed outcome words of item 3 of the 2026-10-08 rulings are not
   yet in the code; that is the open item on RT-250's row". This batch closes
   the row for the outcome words (RT-250) because they now are in the code.

**Worth noting, not items.**
- In the row for the free model's gate (RT-237), condition 2 is quoted
  exactly but only in part: the ledger quotes its action, "rerun the three
  scripts here on the merged code before the closure line goes in the
  ledger", and gives the trigger in its own words ("which changes
  `procedure.gate`"). That is faithful. Main's earlier wording quoted the
  trigger too.
- The same row says "two outputs identical, the third adding only the new
  folders' rows". That follows the verdict summary of the check of pull
  request 152. Its detail (part 2) also shows that `code_gate_on_toy.json`
  gains a reporting-only `row_choice` block on arm T's three rows. Nothing
  changes.
- The row for the outcome words (RT-250) says the code prints "version 5's
  eight registered terms". The code holds seven worded terms
  (`measure.OUTCOME_TERMS`); the eighth outcome, R4 (the programme
  hibernates), has no term in section 3's table ("(none)"), as the check of
  pull request 152 notes. "All the registered terms" would be exact.
- The table bug passed every self-test because no self-test counts cells per
  row. A one-line test (every row of `table()` has as many cells as the
  header) would guard the frozen reporting table. It is not needed for this
  batch.

## 1. The code fix: holds

**The diff of `src/` is one number.**

```
$ git diff origin/main...origin/final-batch-before-registration -- experiments/08-successor-degree/src
-            out.append(f"| {arm}/{s} | {verdict} |" + " withheld |" * 12
+            out.append(f"| {arm}/{s} | {verdict} |" + " withheld |" * 11
```

It is one line in `procedure.table` and nothing else under `src/`. The header
has 16 columns: arm and seed, the verdict, eleven columns computed from a
reading, the two lesion counts and arm T's row choice. So 11 is right.

**The self-tests pass** (run on the branch's head, `6c47c56`):

```
$ sh experiments/08-successor-degree/src/run_self_tests.sh
... grammar, models, transplant, measure, procedure, train_successor, tripwire: all checks passed
ALL SELF-TESTS PASS
```

**Re-summarised from a scratch copy, the summary is byte-identical and every
row has 16 cells.**

```
$ cp -R experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000 $SCRATCH/passB
$ (cd experiments/08-successor-degree/src && ~/Code/minimum-viable-mind/.venv/bin/python procedure.py summarise --dir $SCRATCH/passB)
outcome: substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2)
$ diff -rq out-ruled-code-changes/passB-limit10000 $SCRATCH/passB
Files .../table.md and $SCRATCH/passB/table.md differ          (the only file that differs)
$ cmp committed/summary.json $SCRATCH/passB/summary.json        -> identical
  b9a27891d5e21990064395310a6fa093af777f78 for both
$ cmp $SCRATCH/passB/table.md out-ruled-code-changes/table-layout-fix/table-passB-rebuilt.md   -> identical
cells per row (awk -F'|' '{print NF-2}'):
  rebuilt:   header 16, divider 16, all twelve rows 16
  committed: header 16, T/0 to T/2 16, C, M and F rows (9) 17
non-withheld lines, committed against rebuilt: identical
committed table with one " withheld |" removed from each line: identical to the rebuilt table
```

So the fix removes exactly one cell from each of the nine withheld rows and
changes nothing else. The evidence file is what the fixed code writes. The
evidence README's claims (summary identical, non-withheld rows identical,
16 cells everywhere, 17 on the nine withheld rows before) all hold.

## 2. Version 5: the new statements match, with the gaps above

I read the whole diff of `docs/successor-experiment-proposal-2026-10-07-v5.md`
(12 places changed, 103 lines) against the findings
(`docs/2026-10-09-ruled-code-changes-and-page4-rerun-findings.md`) and their
check (`docs/reviews/2026-10-09-ruled-code-changes-check-claude-code.md`).

| What changed | Matches? |
|---|---|
| Section 7.2, item 1, the corrected caution: 471 early stops on arm M at 3,000, "467 were fits of the shuffled-label comparison and 4 were fits of the named agent's read, which arm M does not use"; "the registered ownership read never stopped at the limit on any model"; 0 such fits at 10,000 on every toy model; every quoted page 4 figure unchanged | Yes: findings 2b (130 + 239 + 98 = 467 null, 2 + 1 + 1 = 4 named read, 0 ownership read); check part 1, point 6. The old ruled note ("until then the frozen code still fits on 420 of 600") is gone |
| Weakness W15: the limit of 3,000 named; never at 10,000 on the toy; the ownership read never stopped at either limit | Yes. "Either limit" is at 1,800 fitting episodes, where pass A's count by kind shows 0 ownership-read stops at 3,000 |
| Section 9, arm M row: 0.5252, 0.4793, 0.5208, within 0.0252, 0.0033, 0.0288; the 420 figures kept as history | Yes: findings 2c; check part 1, point 6. Sources column not updated (should-fix 2) |
| The limit of 10,000 in section 7.4's frozen list and section 9's episode-count row | Yes (the check of pull request 152, S2.2) |
| Section 7.4: the re-pinned digest of the evaluation sets "a session's call, decided by: agent", with the replay showing no training step changes | Yes: the check of pull request 152, part 1, point 3, says it needs no ruling first and should be named as an agent's call (decided by: agent). The replay result is as the check reports (0 of the 1,380 new episodes drawn, on all three seeds) |
| Section 7.1: the held-out 180 are the last of 1,980 | Yes for the registered code; the note on earlier reads is wrong for the 2026-10-06 reads (should-fix 1) |
| Section 17, failure 4's re-summary: R3, "substrate not a testbed", arm F failing the named-other condition on seeds 1 and 2; arms C and M withheld on every seed by the in-use check; no separation computed; 1.0000 is each row's arithmetic | Yes: findings 2d; pass B's `table.md`, which I re-made above |
| Section 17, the outcome-terms bullet: the code prints the registered words with their scope phrases; 31 made-up cases land | Yes: check part 1, points 2 and 4 |
| Section 11, step 3; section 7.5, item 15; section 21's header; the source table's new row (29,077 values, 740 of 740 clause states) | Yes, each against the findings and the check |
| The change note at the end of the file | Lists what changed. It is accurate, except that it lists section 17's failure 4 as updated while one bullet in it is still stale (must-fix 1) |

**Nothing else changed.** Every changed place is listed above. Section 9's
episode-count row gains only the limit's words. No bar, term, stop or other
figure is touched.

**Searches for leftovers** (on the branch's version 5): `grep -nE
"0\.4886|0\.4860|0\.5449|0\.0049|0\.0099|0\.0529|still owed|to be
re-summarised|summarised again|not yet in the code|still fits on 420|last 180
of 600"`. Every hit is one of these:
- history, labelled as history: section 3 line 609; section 10's R-3 at
  3215, followed by the 1,800 figures "as now registered"; section 20's page 4
  entry at 5447; section 21's items, kept "as they stood"; the code-block
  output at 5132, with the new note under it;
- a true statement: the header at line 33, since item 8's work is still to
  do; the reviewer's own pass at 5200;
- one of the must-fix or should-fix places above (lines 1232, 1243, 1859,
  3376, 5151, 5194).

## 3. The ledger: holds

**RT-237, the free model's gate.** Condition 1 is quoted word for word from
`docs/reviews/2026-10-09-rt237-closure-check-claude-code.md` (its line 46 to
48): "when step 4b's reruns are written, confirm their gate rows carry
`lesioned_candidate_own_correct`, `lesioned_candidate_other_correct` and
`ownership_free_line`". Condition 2's action is quoted word for word (its
lines 52 to 54), with the trigger paraphrased (see worth noting). The other
figures in the cell match the closure check: eleven clauses in its table, the
lines 790 and 1,546, and 344 clause states.

**Condition 2 is really met.** The check of pull request 152 (part 2) ran the
three scripts on the code of pull request 151. It had shown that code is what
the merge gives: `git merge-tree` showed no conflict, and nothing under
`experiments/` had changed on the main line. Result: 740 of 740 clause states
agreeing, two outputs identical, and the third differing only by lines for
new folders. I re-ran the three scripts myself on this batch's head
(the merged code plus the one-number table fix), from scratch copies so the
committed outputs were not overwritten:

```
$ python3 -I $SCRATCH/rt237/recount_from_rows.py      > .../recount_from_rows.out.txt     # exit 0
$ .venv/bin/python $SCRATCH/rt237/recount_from_models.py > .../recount_from_models.out.txt # exit 0
$ .venv/bin/python $SCRATCH/rt237/code_gate_on_toy.py    > .../code_gate_on_toy.out.txt   # exit 0
each of the five outputs, against docs/reviews/2026-10-09-ruled-code-changes-check-scripts/rt237-rerun-on-pr151/: identical
    clause states compared: 740; mismatches of any kind: 0
RESULT: every recount matches
```

So the closure holds on the code this batch leaves, too.

**RT-240, the episode counts.** Closed by what the check of pull request 152
measured: the fit on the first 1,800 of 1,980 at limit 10,000 (part 1,
point 2), all twelve toy models re-run with 0 values different from the
committed pass B (point 5), 0 early stops, and every quoted figure the same
(point 6). The row keeps the finding's own subject, the registered width, as
weakness W15, first seen at step 5a. That is honest.

**RT-250, the outcome words.** Closed by what that check measured: the terms
word for word against section 3, the scope phrases, "validated" found only in
the history table and the self-test, and 31 of 31 cases (part 1, points 2
and 4). See worth noting on "eight".

**The count.** I recounted the closure words at the head of the fifth column
for every row RT-230 to RT-274:

```
$ grep -nE "^\| RT-2(3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-4])\b" red_team_ledger.md | awk -F'|' '{...count "Closed: the claim was checked", "Closed: the argument was accepted", "Open"...}'
branch: rows 45 checked 21 accepted 18 open 6
main:   rows 45 checked 18 accepted 18 open 9
open on the branch: RT-247, RT-263, RT-266, RT-267, RT-269, RT-273
```

That is the note's 21, 18 and 6. Of the open rows only RT-247 (the decoy)
bears on the registration. The other five are the refounding proposal's, as
the note says.

**Column counts are unchanged.** I counted the cells on every table line of
the ledger, on main and on the branch: 1 line of 10 fields, 23 of 6, 232 of 7
and 20 of 8 on both. RT-237, RT-240 and RT-250 each have 7 on both. The
branch is 12 lines longer, which is the new dated note.

## Commands, in order

    git fetch origin
    git diff origin/main...origin/final-batch-before-registration
    gh pr view 153 --json baseRefName,headRefName,title        # base main
    git checkout --detach origin/final-batch-before-registration
    sh experiments/08-successor-degree/src/run_self_tests.sh
    cp -R experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000 $SCRATCH/passB
    (cd experiments/08-successor-degree/src && ~/Code/minimum-viable-mind/.venv/bin/python procedure.py summarise --dir $SCRATCH/passB)
    cmp, diff -rq and awk -F'|' cell counts, as in section 1
    the three RT-237 scripts copied to $SCRATCH/rt237 and run from the repository root, as in section 3
    grep and awk over version 5 and the ledger, as in sections 2 and 3

`$SCRATCH` is this session's scratch folder; nothing there is committed.

## What this does not do

It fixes nothing, and edits neither version 5, the ledger, the code nor the
pull request's branch. It merges nothing and spends nothing.
