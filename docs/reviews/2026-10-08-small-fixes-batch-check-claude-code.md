# Check of the small-fixes batch (pull request 149)

*Written 2026-10-08 (Thursday evening, Pacific) by a Claude Code session that
wrote none of what it checks: not the batch, not the four checks it draws
from, not the ledger rows, not version 5 of the registration text, and not the
rehearsal findings. It read no chat of any session. Branch
`check-small-fixes-batch`, cut from the main line at `44a9adf` (the merge of
pull request 148). Laptop only, $0: nothing was run but `git`, `grep`, the
project's citation checker, and short Python scripts that read files or call
the episode generator once. Nothing was fixed. Written under the workspace
plain-language rule.*

*What was checked:* pull request 149, branch `small-fixes-batch-2026-10-08`,
base main, one commit `e705b1a` ("Batch of small fixes from the evening's
checks"), cut from the main line at `44a9adf`. It edits four files: version 5
of the registration text (`docs/successor-experiment-proposal-2026-10-07-v5.md`),
the red-team ledger (`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`,
the list of every problem a review has found and how each was settled), the
rehearsal repairs findings (`docs/2026-09-26-rehearsal-repairs.md`), and the
findings note for ledger rows 212 to 229 (`docs/2026-10-09-ledger-rows-rt212-229-findings.md`).

*The four source checks, with the short names used below:*

- "the rows-and-wording check": `docs/reviews/2026-10-09-ledger-rows-and-v5-wording-check-claude-code.md`
  (its should-fix items A-S1 to A-S3 on the ledger, B-S1 on version 5);
- "the serious-findings check": `docs/reviews/2026-10-09-serious-findings-closure-check-claude-code.md`
  (the closure check of the floor's missing condition, RT-238; the episode
  format, RT-239; control 6, RT-251);
- "the ledger-packet check": `docs/reviews/2026-10-09-ledger-packet-and-rows-212-229-check-claude-code.md`
  (its should-fix items 1 to 4);
- "the free-gate closure check": `docs/reviews/2026-10-09-rt237-closure-check-claude-code.md`
  (the closure check of the fatal finding on the free model's gate, RT-237).

## Verdict

**Not ready to merge: one must-fix item**, the wording of the free model's
gate row (RT-237). Everything else the batch does is what its source says, the
figures in the one new dated note are right against the committed files, the
token arithmetic matches the generator, both count notes match the rows, and
no figure, bar, term or stop changed. Six should-fix items, none of which
blocks the merge once the must-fix is done.

## Must-fix

1. **The free model's gate row (RT-237) does not carry the closure check's
   two conditions as the check states them, and its second condition is
   already set off by a branch that is waiting to merge.** The free-gate
   closure check's verdict is "closed, with two named conditions" (its lines
   22 to 54). The row's version of them:

   > Conditions: (1) no full-size row written by the gate code carries the new
   > field yet, so the three reruns' rows are checked for it; (2) the
   > checker's three scripts are re-run on the merged code if the ruled code
   > changes touch the gate code beyond wording

   What the check says:

   - Condition 1: "when step 4b's reruns are written, confirm their gate rows
     carry `lesioned_candidate_own_correct`, `lesioned_candidate_other_correct`
     and `ownership_free_line`." The row drops the three field names and
     step 4b, and says "the new field", singular. A later session reading the
     row alone would not know which three fields to look for.
   - Condition 2: "If it touches anything beyond wording, the fitting limit
     and the summary for fewer than three seeds (in particular
     `measure.seed_gate`, `measure.withhold`, `measure.arm_outcome` or
     `procedure.gate`), rerun the three scripts here on the merged code
     **before the closure line goes in the ledger**." The row changes when the
     scripts must be re-run (from "before the closure line goes in" to
     "if"), and changes the trigger (the check exempts the fitting limit and
     the summary for fewer than three seeds; the row exempts only wording,
     and names no function).

   This matters now, not later. The branch the check meant,
   `ruled-code-changes-2026-10-09` (John's ruled code changes of 2026-10-08),
   is not merged yet, and it changes two of the four functions the check
   named. One of the two changes is outside what the check exempted (command
   C.3):

   ```
   measure.py, main against ruled-code-changes-2026-10-09:
   seed_gate: identical
   withhold: identical
   arm_outcome: CHANGED     (the summary for fewer than three seeds: exempt)
   procedure.py:
   gate: CHANGED            (adds arm T's row-choice report to the gate row: not exempt)
   ```

   The main line's gate code is still exactly what the check checked
   (`git diff --stat 760deef origin/main -- experiments/08-successor-degree/src`
   prints nothing), so closing the row today is sound. But the row should
   carry both conditions in the check's own terms, and say that the ruled
   code changes branch changes `procedure.gate`, so the re-run of the three
   scripts is owed when it merges and the row goes back to open if the re-run
   disagrees. Writing the conditions out in full, as the check states them,
   fixes it.

## Should-fix

1. **The free model's gate row (RT-237) should name the commits that land
   the fix.** The ledger-packet check's should-fix 2 cites the protocol's
   closure rule (`docs/outside-review-protocol.md`, "The closure rule"): a
   fatal finding's closure line gives "the commit that lands the fix" as
   well as the measured check. The batch applies this to the empty-read
   finding (RT-212) and to the decision-procedure finding (RT-256), but not
   to the one fatal row it newly closes. The repair's code came in with
   `6583a5f` ("A2: the decision code brought to the 2026-10-06 rulings",
   part of pull request 105, merged as `bd0de26`) and its text with
   version 5 (first drafted at `c9b0259`) (command C.4).
2. **The second count note says "Four rows moved" and then names five**: the
   free model's gate (RT-237), the floor's condition (RT-238), the episode
   format (RT-239), control 6 (RT-251) and the first-side finding (RT-266).
   The totals it gives are right (section 3); only the word "Four" is wrong.
3. **Version 5's section 4.1 says "46 words in all" right after the twelve
   marker words and five items of the training, development and fresh pools,
   which reads as if 46 were the words those pools use.** The 46 is the
   whole vocabulary: 8 special words, "assign" and "revise", 20 marker words,
   8 items and 8 values, including the unseen-vocabulary pool's extra eight
   marker words and three items. The pools named use 35 of them (command
   C.2). This is the same kind of misreading the serious-findings check
   flagged for "56 tokens"; saying what the 46 counts closes it.
4. **The change note at the end of version 5 says "from the should-fix items
   of four checks" and lists three.** The fourth, the free-gate closure
   check, gave nothing to version 5; either name it or say three.
5. **The findings note for ledger rows 212 to 229 still says RT-219 (the two
   entangled shares) is open.** Its count ("Open: 1") and its point 1
   ("RT-219's owed correction was never made") are now overtaken by the
   batch's dated note in the repairs findings. The batch added a dated note
   to that file for the heading edit but not for this; one more line there
   would keep the two records in step.
6. **The new dated note in the repairs findings gives the two fields in
   different forms.** The gate figure's field is given in full,
   `runs.M/base/*.own_by_route.entangled_share`; the fresh-trial figure's as
   `fourth_arm.entangled_share`, whose full path in `measure_base_M.json` is
   `arms.M/base/*.fourth_arm.entangled_share`. The short form is the one the
   review of version 2 used (its line 172), so nothing is wrong; giving both
   in full would let a reader find the second without opening the file.

## A note for John (a decision, not a fix)

Ruling 5 of `docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`
names four ledger rows on the refounding proposal that "may stand open,
named as open" (RT-263, RT-267, RT-269, RT-273). The batch reopens a fifth,
the first-side finding (RT-266), as the rows-and-wording check's A-S2
suggested. The reopening follows the method note's rule and is the right
reading of the record, but ruling 5's list of four no longer matches the
ledger.

---

## 1. Each change against its source

Commands A.1 to A.3 below. Every edit in the diff traces to an item in one of
the four checks; nothing else was changed.

| Change | Source | What the source asked | Found |
|---|---|---|---|
| Six refounding rows (RT-274, the records-not-on-the-branch finding; RT-257; RT-258; RT-260; RT-268; RT-270) now say "checked ... (at `5de5fff`; later edits to version 2 are not covered by that check)" | rows-and-wording check, A-S1 | each of the six should say it was checked at `5de5fff` | Done, all six, and nothing else in those rows changed |
| The first-side finding (RT-266) reopened, with "what closes it" | rows-and-wording check, A-S2 | open it, or say why it differs from the control's specification (RT-263) | Done: open, with the same kind of closing test as RT-263. See the note for John |
| The free model's gate (RT-237): "is running separately" gone | rows-and-wording check, A-S3 | stop saying the closure check is running | Done, by closing the row on the merged check. See must-fix 1 for the new wording |
| Version 5, three places that credited pull request 136 alone (now lines 3389, 3447, 4628) | rows-and-wording check, B-S1 | say several branches came by their own pull requests | Done; the three now say "the last of them through pull request 136" or "several through their own pull requests and the rest through pull request 136", which matches that check's B.3 (seven by their own pull requests, eight through 136) |
| Version 5, section 4.1: vocabulary 46 words; episode 56 tokens with the start, line-break and end words | serious-findings check, its first two "worth noting" points under RT-239 | 56 is not the vocabulary; the renderings omit the start, line-break and end words | Done, and right against the generator (section 2). Its third point (the turn count is guarded only by the pinned digest) asked for nothing, since the text makes no claim about it; the batch rightly leaves it. See should-fix 3 |
| The floor's condition (RT-238), the episode format (RT-239), control 6 (RT-251) closed as checked | serious-findings check, its three verdicts | each "the claim was checked (closed)" | Done. Each row's summary is that check's own result (see below) |
| Findings note for rows 212 to 229: a dated note on the heading edit | ledger-packet check, should-fix 1 | say the refounding section's heading was edited | Done, quoting the heading before and after exactly |
| The empty-read finding (RT-212) names `9d9d31a` and `6d4ec3a` | ledger-packet check, should-fix 2 | name the commits that land the fix: the toy re-run under the version 3 rules and version 3 | Done (command A.3). The batch also does this for the decision-procedure finding (RT-256, `bd0de26`), which the same item says has the same gap; that is within the item. It does not do it for RT-237 (should-fix 1) |
| The site-set rule never run (RT-215): "the first pass, the primary and the stricter row" | ledger-packet check, should-fix 3 | replace "primary, and both layer-0 variants" | Done, word for word as the check proposed |
| Version 5, section 13, weakness W9: arm M's code "had run only on this laptop when this was ruled", with a dated note that the 2026-10-04 development runs trained all four arms on rented machines; "step 4 of section 11 is where arm M first does" removed | ledger-packet check, should-fix 4 | name an owner for the out-of-date sentence, and its last sentence is out of date too | Done more directly: both sentences fixed in place. The cited development-runs check exists and its item 1 reads "every arm, arm M for the first time ... Holds" (command A.2) |
| The two entangled shares (RT-219) closed as accepted, after a dated note in the repairs findings | ledger-packet check (the row "rightly open"), and the rows 212 to 229 findings note's "what closes it: a dated note beside that sentence" | add the dated note | Done, and the note's figures are right (section 1.2) |
| The free model's gate (RT-237) closed as checked, with two conditions | free-gate closure check, its verdict | "closed, with two named conditions" | Closed correctly; conditions not as stated (must-fix 1) |

### 1.1 Each row now marked "checked": did its check really measure that claim?

- **The floor's missing condition (RT-238).** The row: "they agree on all
  426,981 inputs tried, and the code clears 0 of 45 site sets where
  own-directed accuracy is at or under the no-transplant rate." The
  serious-findings check, part 2, ran its own function against
  `measure.floor_check` on 226,981 combined inputs plus 200,000 random ones
  (226,981 + 200,000 = 426,981), and part 3 shows "code clears 0" of 45 in
  each of its three cases at or under the no-transplant rate. Measured.
- **The episode format (RT-239).** The row: "all 21 registered details of
  section 4.1 hold on 13,800 generated episodes; both self-tests pass and
  each fails when its departure is undone in a scratch copy." The check's
  section 2: twenty-one fields, 13,800 episodes, every field holds; undoing
  departure 1 fails the name-badge check (and the token-identity check),
  undoing departure 2 fails the token-identity check. Measured.
- **Control 6 (RT-251).** The row: "no surviving claim in version 5, its
  reporting table or the code's output labels that control 6 tells the two
  kinds of copying apart." The check's section 3 is a committed search
  (`control6_grep.sh` and its output) read hit by hit. This is the measured
  check the outside dispositions named for this finding ("a search showing no
  sentence claims control 6 separates the two"). Measured.
- **The free model's gate (RT-237).** The row's summary ("all eleven clauses
  ... judged on named fields of committed output; both lines (790 and 1,546
  of 3,000) and all 344 clause states recompute from independent code; the
  text and the code agree clause by clause") matches the check's verdict and
  its parts 2 to 4. "Eleven" counts the check's clause table, which has ten
  clauses and a scope row; that is the table's own row count, and harmless.
  The conditions are must-fix 1.
- **The six refounding rows** were already "checked"; the batch only adds
  the commit the check ran at, which is the check's own header.

### 1.2 The new dated note on the two entangled shares (RT-219)

The note, in `docs/2026-09-26-rehearsal-repairs.md` section 5, says: 0.6033 is
1,810 of the 3,000 held-out gate episodes, `gate_base.json`, field
`runs.M/base/*.own_by_route.entangled_share`; the share of the 800 fresh
measurement trials is 0.60375, 483 of 800, `measure_base_M.json`, field
`fourth_arm.entangled_share`. Against the committed files in
`experiments/rehearsal-successor-measure/out-repairs/` (command B.1):

```
M/base/0 n_trials 800 share 0.60375 x n = 483.0
M/base/1 n_trials 800 share 0.60375 x n = 483.0
M/base/2 n_trials 800 share 0.60375 x n = 483.0
M/base/0 n 3000 share 0.6033333333333334 x n = 1810.0000000000002
M/base/1 n 3000 share 0.6033333333333334 x n = 1810.0000000000002
M/base/2 n 3000 share 0.6033333333333334 x n = 1810.0000000000002
```

Every figure, file and field is right. The fresh-trial field's full path is
`arms.M/base/*.fourth_arm.entangled_share` (should-fix 6). The review of
version 2 did measure both (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`,
lines 159 to 182). The only other "0.6033" in the file (line 178) is an
unrelated fit figure for arm C.

### 1.3 The commits named as landing fixes

```
$ git log --no-walk --format="%h %ad %s" --date=short 9d9d31a 6d4ec3a bd0de26
bd0de26 2026-10-06 Merge pull request #105 from jfredson/a2-decision-procedure
6d4ec3a 2026-10-03 Successor experiment proposal, version 3 (from the Gate C rulings of 2026-09-26) (#71)
9d9d31a 2026-09-26 Toy re-run under the version 3 rules (RT-212 to RT-216) (#62)
```

All three are on the main line. `9d9d31a` (pull request 62) is the toy
re-run that applies the four-fifths fit floor to the committed models; its
message lists the fit floor with its permutation null. `6d4ec3a` (pull
request 71) is version 3, written from the rulings on RT-212 to RT-229.
`bd0de26` brings in pull request 105, whose commits include `6583a5f`, "A2:
the decision code brought to the 2026-10-06 rulings, with unit tests", and
`74967f8`, the end-to-end run on the toy and the made-up cases: the fix the
decision-procedure finding (RT-256) asked for. Each lands its fix.

## 2. Section 4.1's token arithmetic against the generator

```
$ ~/Code/minimum-viable-mind/.venv/bin/python -I -c "...grammar.make_pairs(1, seed=0, pool='dev')..."
vocab size 46 SEQ_LEN 56
tokens in one episode: 56
<bos> m7 assign it0 v6 <nl> m6 assign it4 v7 <nl> m6 assign it0 v4 <nl> m5 assign it0 v5 <nl> m7 assign it4 v6 <nl> m3 assign it4 v3 <nl> m5 assign it4 v2 <nl> m3 assign it0 v3 <nl> <act> revise <self> it0 <ans> <mask> <nl> <act> revise m7 it0 <ans> <mask> <nl> <eos>
first <bos> last <eos>
turn lengths incl. line-break word: [5, 5, 5, 5, 5, 5, 5, 5, 7, 7]
vocabulary by kind: {'special': 8, 'assign/revise': 2, 'marker': 20, 'item': 8, 'value': 8}
words usable in train/dev/fresh pools: 35
```

One start word, eight assignment turns of five tokens (marker, "assign",
item, value, line-break), two action turns of seven (act word, "revise",
who-word, item, answer cue, mask, line-break), one end word: 1 + 40 + 14 + 1
= 56. `grammar.py` line 117 is `SEQ_LEN = 1 + 8 * 5 + 2 * 7 + 1`, and its
docstring (line 39) says "a closed vocabulary of 46 words, 56 tokens". The
text's renderings now match the generator's `render` (lines 185 to 241)
token for token. What the 46 counts is should-fix 3.

## 3. The two count notes against the rows

A script (`count.py`, in this session's scratch folder; it reads each row of
the form `| RT-n ... |`, takes the last cell, and sorts it by its first
words) on the main line's ledger and the pull request's (command D.1):

```
ledger_main.md RT-212..RT-229: {'checked': 6, 'accepted': 11, 'open': 1}; missing []; duplicated []
    open: [219]
ledger_main.md RT-230..RT-274: {'checked': 15, 'accepted': 22, 'open': 8}; missing []; duplicated []
    open: [237, 240, 247, 250, 263, 267, 269, 273]
ledger_pr.md RT-212..RT-229: {'checked': 6, 'accepted': 12}; missing []; duplicated []
    open: None
ledger_pr.md RT-230..RT-274: {'checked': 19, 'accepted': 18, 'open': 8}; missing []; duplicated []
    open: [240, 247, 250, 263, 266, 267, 269, 273]
```

The first dated note says "checked 6, accepted 12, open 0": right. The
second says "checked 19, accepted 18, open 8 (RT-240, RT-247, RT-250 ...;
RT-263, RT-266, RT-267, RT-269 and RT-273 ...)": right, with the same eight
numbers. The arithmetic: 15 + 4 (the free gate and the three serious
findings) = 19; 22 − 3 − 1 (the first-side finding reopened) = 18; 8 − 1 + 1
= 8. The note's "Four rows moved" is should-fix 2.

## 4. No figure, bar, term or stop changed; every edited row keeps its columns

**Numbers.** A script (`nums.py`) compared every number in the removed lines
with every number in the added lines, per file (command D.2):

```
docs/successor-experiment-proposal-2026-10-07-v5.md
   only in removed lines: {'4': 1, '11': 1}
   only in added lines:   {'46': 2, '56': 2, '5': 3, '7': 2, '1': 5, '40': 1, '14': 1, '2026': 7, ...}
experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
   only in removed lines: {'216': 1, '58': 1, '232': 1}
   only in added lines:   {..., '426,981': 1, '13,800': 1, '344': 1, '790': 1, ...}
docs/2026-09-26-rehearsal-repairs.md
   only in removed lines: {}
docs/2026-10-09-ledger-rows-rt212-229-findings.md
   only in removed lines: {}
```

In version 5 the only numbers removed are "step 4 of section 11", in the
sentence should-fix 4 of the ledger-packet check asked to correct. The
numbers added are the token arithmetic (section 2), the vocabulary size
already in the code's docstring, dates, section numbers and the pull request
number in the reworded credit. In the ledger the numbers removed are from old
closure text (the old commit `d216dbc` and pull request 58 in the shares row,
"lines 232 to 267" in the free gate row); the numbers added are each check's
own results, quoted above. No bar, line, outcome term or stop condition
appears in any changed line except as text that was already there. The
change note at the end of version 5 says the same, and it is true.

**Columns.** The same script compared every row that changed (command D.1):

```
   RT-212: 5 -> 5 cells (same)      RT-215: 5 -> 5 cells (same)
   RT-219: 5 -> 5 cells (same)      RT-237: 5 -> 5 cells (same)
   RT-238: 5 -> 5 cells (same)      RT-239: 5 -> 5 cells (same)
   RT-251: 5 -> 5 cells (same)      RT-256: 5 -> 5 cells (same)
   RT-257: 5 -> 5 cells (same)      RT-258: 5 -> 5 cells (same)
   RT-260: 5 -> 5 cells (same)      RT-266: 5 -> 5 cells (same)
   RT-268: 5 -> 5 cells (same)      RT-270: 5 -> 5 cells (same)
   RT-274: 5 -> 5 cells (same)
```

Fifteen rows changed, each still five cells, matching their tables' header
`| ID | Finding | Severity | Disposition | Closure |`. No other row changed.
Of the first four cells (number, finding, severity, disposition) none changed
in any row; every edit is in the closure cell.

## 5. Anything the batch missed from the four checks' should-fix lists

- The rows-and-wording check: A-S1, A-S2, A-S3 and B-S1 all applied.
- The serious-findings check: its two wording points on section 4.1 applied;
  its third (the turn count guarded only by the pinned digest) and its note
  on the comment in `grammar.py` line 159 asked for no change. The three rows
  closed as checked.
- The ledger-packet check: should-fix 1 to 4 all applied. The rule behind
  should-fix 2 (a fatal row names the commit that lands the fix) is not
  applied to the newly closed free gate row (should-fix 1 here).
- The free-gate closure check: the verdict applied; the two conditions not as
  stated (must-fix 1). Its three "worth noting" points asked for no change.

The citation checker on the pull request's copy of the four files
(`python3 -I scripts/check_citations.py --only <each file> --part paths`,
run on a `git archive` extract) gives two confident findings, both on lines
of version 5 the batch did not touch (4786 and 5179, scripts kept in earlier
sessions' scratch folders). Nothing new.

## Commands

**A. The diff and its sources**

```
$ git fetch origin
$ git log --oneline origin/main..origin/small-fixes-batch-2026-10-08
e705b1a Batch of small fixes from the evening's checks: version 5 wording, ledger closures, one dated note
$ git merge-base origin/main origin/small-fixes-batch-2026-10-08
44a9adfbc3ce07923c20e63fef0ae3027e7e404e        (the main line's head)
$ gh pr view 149 --json baseRefName,headRefName,state
{"baseRefName":"main","headRefName":"small-fixes-batch-2026-10-08","state":"OPEN"}
$ git diff --stat origin/main...origin/small-fixes-batch-2026-10-08
 docs/2026-09-26-rehearsal-repairs.md               |  7 +++-
 docs/2026-10-09-ledger-rows-rt212-229-findings.md  |  7 ++++
 .../successor-experiment-proposal-2026-10-07-v5.md | 46 ++++++++++++++++------
 .../red_team_ledger.md                             | 45 ++++++++++++++-------
 4 files changed, 77 insertions(+), 28 deletions(-)
$ git diff --word-diff=plain origin/main...origin/small-fixes-batch-2026-10-08 -- <ledger>   (read row by row)
```

A.2: `grep -n "every arm, arm M for the first time" experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md`
gives line 40, verdict "Holds". A.3: section 1.3 above.

**B. The shares (RT-219)**

B.1: a Python one-liner (`python3 -I`) reading
`experiments/rehearsal-successor-measure/out-repairs/measure_base_M.json`
(`arms[*].n_trials`, `arms[*].fourth_arm.entangled_share`) and
`out-repairs/gate_base.json` (`runs['M/base/*'].n`,
`runs['M/base/*'].own_by_route.entangled_share`); output in section 1.2.

**C. The generator and the gate code**

- C.2: section 2's command, with the project's own Python, importing
  `experiments/08-successor-degree/src/grammar.py` and building one pair of
  development episodes.
- C.3: `git diff --stat 760deef origin/main -- experiments/08-successor-degree/src`
  prints nothing. Then `funcs.py` (scratch folder; parses both copies with
  `ast` and compares each named function's source) on `git show` copies of
  `measure.py` and `procedure.py` from the main line and from
  `origin/ruled-code-changes-2026-10-09`; output in must-fix 1. The branch is
  not merged (`git log --merges origin/main` has no merge of it; its six
  commits run from `3d31fd2`, its method note, to `784da42`).
- C.4: `git log -S "lesioned_candidate_own_correct" origin/main -- experiments/08-successor-degree/src`
  gives `6583a5f 2026-10-06 A2: the decision code brought to the 2026-10-06 rulings, with unit tests`.

**D. Counts, columns and numbers**

- D.1: `python3 -I count.py ledger_main.md ledger_pr.md` (both ledgers from
  `git show`); output in sections 3 and 4.
- D.2: `git diff origin/main...origin/small-fixes-batch-2026-10-08 | python3 -I nums.py`;
  output in section 4.

The scripts live in this session's scratch folder, not in the repository;
each only reads files, apart from C.2, which calls the episode generator.
