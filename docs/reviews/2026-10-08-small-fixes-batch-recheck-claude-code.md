# Re-check of the small-fixes batch (pull request 149) after its repair commit

*Written 2026-10-08 (Thursday evening, Pacific) by a Claude Code session that
wrote none of what it checks: not the batch, not its repair commit, not the
first check of it, and not the closure check of the free model's gate. It
read no chat of any session. Laptop only, $0: nothing was run but `git`, the
project's citation checker, and short Python scripts that only read files.
Nothing was fixed. Written under the workspace plain-language rule.*

*What was checked:* pull request 149 (branch `small-fixes-batch-2026-10-08`,
base main, still open), now two commits on the main line's head `44a9adf`:
the batch itself, `e705b1a`, and the repair commit `9204b51` ("Apply the
check of the small-fixes batch: the free model's gate stays open until its
fired condition is met"). The first check is
`docs/reviews/2026-10-08-small-fixes-batch-check-claude-code.md` (branch
`check-small-fixes-batch`, pull request 150), called "the first check" below.
The closure check of the free model's gate is
`docs/reviews/2026-10-09-rt237-closure-check-claude-code.md`, called "the
free-gate closure check".

## Verdict

**Ready to merge.** The must-fix and all six should-fix items are applied as
the first check asked. The free model's gate row (RT-237) now quotes both of
the free-gate closure check's conditions in its own words and is open, which
is right because the second condition has fired. The new count (checked 18,
accepted 18, open 9) matches the rows. Both data paths in the dated note
resolve. Every edited ledger row keeps its five cells, and no figure, bar,
term or stop moved.

One thing to do at merge time, not a fix: the repair commit adds two
references to the first check's file, which lives only on pull request 150's
branch. Merge pull request 150 with or before pull request 149, or those two
references point at nothing on the main line (section 4).

## 1. The must-fix: the free model's gate row (RT-237)

**The two conditions, against the free-gate closure check.** That check's
"The two conditions" (its lines 31 to 54) and the row
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, line
1010 at `9204b51`):

| | The free-gate closure check | The row now |
|---|---|---|
| Condition 1 | "when step 4b's reruns are written, confirm their gate rows carry `lesioned_candidate_own_correct`, `lesioned_candidate_other_correct` and `ownership_free_line`" | (1) "when step 4b's reruns are written, confirm their gate rows carry `lesioned_candidate_own_correct`, `lesioned_candidate_other_correct` and `ownership_free_line`" |
| Condition 2 | "If it touches anything beyond wording, the fitting limit and the summary for fewer than three seeds (in particular `measure.seed_gate`, `measure.withhold`, `measure.arm_outcome` or `procedure.gate`), rerun the three scripts here on the merged code before the closure line goes in the ledger." ("it" is "the parallel change on branch `ruled-code-changes-2026-10-09`") | (2) "if the parallel change on branch `ruled-code-changes-2026-10-09` touches anything beyond wording, the fitting limit and the summary for fewer than three seeds ("in particular `measure.seed_gate`, `measure.withhold`, `measure.arm_outcome` or `procedure.gate`"), "rerun the three scripts here on the merged code before the closure line goes in the ledger"" |

Condition 1 is word for word, with all three field names and step 4b.
Condition 2 puts the check's "it" back as the branch it names and otherwise
quotes the check exactly: the same exemptions (wording, the fitting limit,
the summary for fewer than three seeds), the same four functions, and
"before the closure line goes in", not "if". Both gaps the first check named
are closed.

**Open, not closed.** The row's closure cell now begins "**Open, its closure
check passed.**", says "Condition 2 has fired: that branch changes
`procedure.gate`", and says what closes it: "the three scripts re-run on the
merged code, by a session that wrote neither, then the closure line here,
with condition 1 carried to step 4b". That is what condition 2 requires. The
dated count note says the same.

**The branch really changes `procedure.gate`.** Command 1:

```
$ git diff origin/main...origin/ruled-code-changes-2026-10-09 -- experiments/08-successor-degree/src/procedure.py
...
@@ -230,9 +251,63 @@ def gate(m, arm: str, data: EvalData) -> dict:
     row["route_in_use"] = route_in_use(m, arm, data.gate)
+    if arm == "T":
+        row["row_choice"] = row_choice(m, data.gate)
     return row
+
+@torch.no_grad()
+def row_choice(m, b: dict, chunk: int = 512) -> dict:
+    """Arm T's row-choice split, beside its gate (version 5, sections 5.1 and
+    7.5, item 15; ruled 2026-10-08, open item 9). Reporting only: ...
```

The gate function now writes a new field (`row_choice`) into arm T's gate
row. That is neither wording, nor the fitting limit, nor the summary for
fewer than three seeds, so condition 2's trigger is met. (The rest of that
diff is the fitting limit, the 1,800-of-1,980 read split, and the "gate not
decidable" summary in `summarise`, which the check exempts.) The branch is
not merged: `git log --merges --oneline origin/main | grep -i ruled-code`
prints nothing, and `git branch -r --contains origin/ruled-code-changes-2026-10-09`
lists only that branch.

**The commit named as landing the fix.** The row says the fix "lands at
`6583a5f` (the decision code brought to the 2026-10-06 rulings, pull request
105) and in version 5 of the registration text". Command 2:

```
$ git show --stat --format="%h %ad %s" --date=short 6583a5f
6583a5f 2026-10-06 A2: the decision code brought to the 2026-10-06 rulings, with unit tests
 experiments/08-successor-degree/src/grammar.py   |  19 +
 experiments/08-successor-degree/src/measure.py   | 426 +++++++++++++++++------
 experiments/08-successor-degree/src/procedure.py | 126 +++++--
$ git branch -r --contains 6583a5f | grep -w origin/main
  origin/main
$ git log --format="%h %s" bd0de26^1..bd0de26^2 | grep 6583a5f
6583a5f A2: the decision code brought to the 2026-10-06 rulings, with unit tests
$ git show -s --format="%h %s" bd0de26
bd0de26 Merge pull request #105 from jfredson/a2-decision-procedure
$ git show 6583a5f -- experiments/08-successor-degree/src/procedure.py | grep -n "^+.*\(lesioned_candidate\|ownership_free_line\)"
104:+               lesioned_candidate_own_correct=candidate_count(l_pred, data.gate_candidates, G.OWN),
105:+               lesioned_candidate_other_correct=candidate_count(l_pred, data.gate_candidates, G.OTHER),
106:+               ownership_free_line=line,
$ git log -S lesioned_candidate_other_correct --format="%h %s" origin/main -- experiments/08-successor-degree/src
6583a5f A2: the decision code brought to the 2026-10-06 rulings, with unit tests
```

`6583a5f` is on the main line, came in with pull request 105, and is the
commit that first writes the three fields into the gate row (and, in
`measure.py`, the 1,546 line and the check that withholds arm F when the
count is missing or under it). It lands the fix.

## 2. The six should-fix items

| First check's item | Asked | Found at `9204b51` |
|---|---|---|
| 1. Name the commits that land the free gate's fix | the fix's commit, per the protocol's closure rule | Done: `6583a5f` (pull request 105) and version 5. Right (section 1) |
| 2. "Four rows moved" named five | fix the count word | Done: the note now names four rows that moved (the floor's condition RT-238, the episode format RT-239, control 6 RT-251 closed as checked; the first-side finding RT-266 reopened) and says separately that RT-237 stays open. Four is now right |
| 3. "46 words in all" read as the words the named pools use | say what the 46 counts | Done: "(twelve marker words and five items in the training, development and fresh pools; the whole vocabulary, special words included, is 46 words, `grammar.py`'s own count)". `grammar.py`'s docstring still says 46 |
| 4. "four checks", three listed | name the fourth or say three | Done: "three checks", the same three paths, and it adds that they were themselves checked in the first check's file (see section 4) |
| 5. The rows 212 to 229 findings note still calls the two entangled shares (RT-219) open | one dated line | Done: a dated note, 2026-10-08 evening, says RT-219 is now closed with the argument accepted after the dated note in the repairs findings (pull request 149) |
| 6. The two data fields given in different forms | give both in full | Done: `out-repairs/gate_base.json`, field `runs.M/base/*.own_by_route.entangled_share`; `out-repairs/measure_base_M.json`, field `arms.M/base/*.fourth_arm.entangled_share` |

**The count, recounted.** A script (`count.py`, in this session's scratch
folder; it reads the ledger at each commit with `git show`, takes the last
cell of every row that starts `| RT-n` or `| RT-n (label)`, and sorts it by
its opening words: "Closed: the claim was checked", "Closed: the argument
was accepted", or "Open"). Command 3:

```
$ python3 -I count.py origin/main e705b1a 9204b51
origin/main RT-212..RT-229: {'checked': 6, 'accepted': 11, 'open': 1} open: [219]
origin/main RT-230..RT-274: {'checked': 15, 'accepted': 22, 'open': 8} open: [237, 240, 247, 250, 263, 267, 269, 273]
e705b1a RT-212..RT-229: {'checked': 6, 'accepted': 12} open: []
e705b1a RT-230..RT-274: {'checked': 19, 'accepted': 18, 'open': 8} open: [240, 247, 250, 263, 266, 267, 269, 273]
9204b51 RT-212..RT-229: {'checked': 6, 'accepted': 12} open: []
9204b51 RT-230..RT-274: {'checked': 18, 'accepted': 18, 'open': 9} open: [237, 240, 247, 250, 263, 266, 267, 269, 273]
```

No number missing or doubled in either range. For RT-230 to RT-274 the note
claims checked 18, accepted 18, open 9, and names the nine open rows as
RT-237, RT-240, RT-247, RT-250, RT-263, RT-266, RT-267, RT-269 and RT-273:
the same nine the script finds, and 18 + 18 + 9 = 45 rows. Against the main
line: 15 checked + 3 (the floor's condition, the episode format, control 6)
= 18; 22 accepted − 3 − 1 (the first-side finding reopened) = 18; 8 open + 1
(the first-side finding) = 9, with the free gate still among them. The first
count note, for RT-212 to RT-229 (checked 6, accepted 12, open 0), is
unchanged and still right.

**Both data paths resolve.** The note's short paths are relative to
`experiments/rehearsal-successor-measure/`, as the file's other citations
(`out-repairs/self-tests.txt`) are. The branch does not touch those files
(`git diff --quiet origin/main 9204b51 -- experiments/rehearsal-successor-measure/`
exits 0). Command 4, a `python3 -I` one-liner that follows each path key by
key:

```
top keys gate_base: ['bar', 'name_only_solver', 'runs', 'verdicts']
top keys measure_base_M: ['arms']
gate_base.json runs.M/base/0.own_by_route.entangled_share = 0.6033333333333334; n=3000; x n = 1810.0000
gate_base.json runs.M/base/1.own_by_route.entangled_share = 0.6033333333333334; n=3000; x n = 1810.0000
gate_base.json runs.M/base/2.own_by_route.entangled_share = 0.6033333333333334; n=3000; x n = 1810.0000
measure_base_M.json arms.M/base/0.fourth_arm.entangled_share = 0.60375; n_trials=800; x n = 483.0000
measure_base_M.json arms.M/base/1.fourth_arm.entangled_share = 0.60375; n_trials=800; x n = 483.0000
measure_base_M.json arms.M/base/2.fourth_arm.entangled_share = 0.60375; n_trials=800; x n = 483.0000
```

Both paths exist exactly as written, and the figures (0.6033 is 1,810 of
3,000; 0.60375 is 483 of 800) are the note's.

## 3. Nothing else changed

**Columns.** A script (`cols.py`, scratch folder) compares every ledger row
between two commits, cell by cell. Command 5:

```
$ python3 -I cols.py e705b1a 9204b51 experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
rows only in old: [] only in new: []
RT-237: 5 -> 5 cells; cells changed: [5]; raw pipes 6 -> 6
$ python3 -I cols.py origin/main 9204b51 experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
rows only in old: [] only in new: []
RT-212 ... RT-274: the same fifteen rows the first check listed, each "5 -> 5 cells; cells changed: [5]; raw pipes 6 -> 6"
```

The repair commit edits one ledger row, the free gate's, and only its closure
cell. Across the whole pull request the fifteen edited rows all keep five
cells, and none of the first four cells (number, finding, severity,
disposition) changed in any row.

**Numbers.** A script (`nums.py`, scratch folder) lists, per file, the
numbers found only in removed lines and only in added lines of the repair
commit's diff. Command 6:

```
$ git diff e705b1a 9204b51 | python3 -I nums.py
docs/2026-09-26-rehearsal-repairs.md
   only in removed lines: {}
   only in added lines:   {}
docs/2026-10-09-ledger-rows-rt212-229-findings.md
   only in removed lines: {}
   only in added lines:   {'2026': 1, '10': 1, '08': 1, '219': 1, '149': 1}
docs/successor-experiment-proposal-2026-10-07-v5.md
   only in removed lines: {}
   only in added lines:   {'2026': 1, '10': 1, '08': 1}
experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
   only in removed lines: {'8': 1, '1,546': 1, '3,000': 1, '142': 1, '790': 1, '344': 1, '19': 1}
   only in added lines:   {'237': 1, '1': 1, '6583': 1, '5': 2, '2026': 3, '10': 3, '06': 1, '105': 1, '09': 1, '4': 2, '2': 1, '149': 1, '08': 1, '18': 1, '9': 1}
```

In the version 5 text and the two findings notes, the only new numbers are
dates, a finding number and a pull request number. In the ledger, the
numbers removed are the old count (19 checked, 8 open) and the free gate
row's summary of what its closure check measured (790 and 1,546 of 3,000,
344 clause states, pull request 142 as the label of the check). The 1,546
line itself is untouched: it still stands in the row's disposition cell,
which did not change, and in the code. The summary was dropped because the
row now quotes the conditions instead; the check's file, still cited in the
row, carries those results. The numbers added are dates, the fix's commit
and pull request, the new count (18, 9), and condition and step numbers. No
bar, line, outcome term or stop condition appears in any changed line except
as text that was already there.

## 4. Worth noting (none blocks the merge)

- **Two new references point at a file only pull request 150 has.** The
  free gate row and version 5's change note now cite
  `docs/reviews/2026-10-08-small-fixes-batch-check-claude-code.md`, which is
  on branch `check-small-fixes-batch`, not on pull request 149's branch or
  the main line. The citation checker (`python3 -I scripts/check_citations.py
  --only <file> --part paths`, run on a `git archive` extract of `9204b51`)
  reports exactly these two as files not in the repository (version 5 line
  5732, ledger line 1010), alongside the two older version 5 findings the
  first check already noted (lines 4787 and 5180, scripts kept in scratch
  folders). Merging pull request 150 with or before pull request 149 settles
  it.
- **The free gate row drops the summary of what its closure check found**
  (all clauses on named fields, the 790 and 1,546 lines and the 344 clause
  states recomputed). That is consistent with the row now being open; the
  closing session will write the closure line, and can carry it back then.
- **The dated count note lists seven of its nine open rows by number alone**
  (RT-240, RT-247, RT-250, RT-263, RT-267, RT-269 and RT-273; it labels only
  the free gate, RT-237, and the first-side finding, RT-266). The count
  paragraph just above it labels all seven, so a reader is one paragraph
  from the meaning; under the workspace rule each would carry its short
  label. The batch's first version had the same list, and the first check
  did not raise it.

## Commands

Run from a worktree of this repository after `git fetch origin`.

1. `git diff origin/main...origin/ruled-code-changes-2026-10-09 -- experiments/08-successor-degree/src/procedure.py`;
   `git log --merges --oneline origin/main | grep -i ruled-code`;
   `git branch -r --contains origin/ruled-code-changes-2026-10-09`.
2. The `6583a5f` commands shown in section 1.
3. `python3 -I count.py origin/main e705b1a 9204b51` (scratch folder; reads
   the ledger with `git show` at each commit).
4. `git diff --quiet origin/main 9204b51 -- experiments/rehearsal-successor-measure/`,
   then a `python3 -I -c` one-liner that loads
   `experiments/rehearsal-successor-measure/out-repairs/gate_base.json` and
   `.../measure_base_M.json` and follows `runs[M/base/*].own_by_route.entangled_share`
   and `arms[M/base/*].fourth_arm.entangled_share`.
5. `python3 -I cols.py e705b1a 9204b51 <ledger>` and
   `python3 -I cols.py origin/main 9204b51 <ledger>` (scratch folder).
6. `git diff e705b1a 9204b51 | python3 -I nums.py` (scratch folder).
7. The citation checker, as in section 4, on each of the four files.
8. `gh pr view 149 --json baseRefName,headRefName,state` gives
   `{"baseRefName":"main","headRefName":"small-fixes-batch-2026-10-08","state":"OPEN"}`;
   pull request 150 likewise has base main.

The scripts live in this session's scratch folder, not in the repository;
each only reads files.
