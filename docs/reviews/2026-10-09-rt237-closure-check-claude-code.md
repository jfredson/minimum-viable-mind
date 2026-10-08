# Closure check of the fatal finding RT-237: findings

*2026-10-09. Claude Code, as the checker, on branch `rt237-closure-check`, cut
from the main line at commit `760deef`. Laptop only, $0. This session wrote
neither the repair (the gate code in `experiments/08-successor-degree/src/measure.py`
and `procedure.py`) nor the registration text (version 5 of the successor
experiment's proposal, `docs/successor-experiment-proposal-2026-10-07-v5.md`).
The method was committed before any check ran:
`docs/reviews/2026-10-09-rt237-closure-check-method.md`. Scripts and their
output are beside this file, in `docs/reviews/2026-10-09-rt237-closure-check-scripts/`.*

**What I opened:** the inside review's finding and its scripts
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`),
the ruling on its repair (`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`,
page 1), the drafted repair it adopts and the four-part check it owes
(`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`, the
RT-237 section), the closure rule (`docs/outside-review-protocol.md`), version
5, the two code files, the case builder `experiments/08-successor-degree/tests/a2_cases.py`,
and the committed rows and records named below. **Not opened:** chat history,
uncommitted files, the parallel branch's code (not yet pushed when I looked).

## Verdict: closed, with two named conditions

Every clause of the free model's gate (arm F, the freely trained system) is
judged by the code on a named field of the gate row; every one of those
fields exists in committed output files; the counts behind the new line
recompute exactly from code that does not import the code under check; and
the text and the code agree clause for clause. Nothing in sections 0 to 16 of
version 5 still sets a condition on question sets the task does not have.

The two conditions:

1. **The field is not yet in any committed full-size row that the gate code
   itself wrote.** The decision-procedure cases carry arm F's candidate counts
   (2,100, 2,238 and 2,324 of 3,000), but those were copied in by hand from the
   rehearsal record by the case builder; the toy's own rows and the 10-million
   development row predate the field; the only rows the gate code wrote with
   the field are the scaled pipeline-test rows (750 episodes, line 399). This
   check closes most of that gap by running the main line's own gate code on
   the twelve committed toy models and committing what it wrote
   (`code_gate_on_toy.json`, below): the field is there, and it equals the
   independent recount on every model. But that file is a checker's record,
   not a row of the experiment. Version 5 says this itself (section 17,
   failure 3: "the first registered rows to carry the field are the reruns of
   step 4b"), and the drafted repair's check, part 4, names it as owed. **The
   condition: when step 4b's reruns are written, confirm their gate rows
   carry `lesioned_candidate_own_correct`, `lesioned_candidate_other_correct`
   and `ownership_free_line`.** One line of the row recount script does it.
2. **The parallel change on branch `ruled-code-changes-2026-10-09`.** If it
   touches anything beyond wording, the fitting limit and the summary for
   fewer than three seeds (in particular `measure.seed_gate`,
   `measure.withhold`, `measure.arm_outcome` or `procedure.gate`), rerun the
   three scripts here on the merged code before the closure line goes in the
   ledger. They take about a minute. Detail at the end.

## 1. The clauses of arm F's gate, as version 5 states them

Arm F is read only after it passes the gate on learning, the channel-removal
check (its collapse line and its ownership-free line) and the fit floor
(section 5.4, lines 1315 to 1317). The fit floor is a separate check on the
read, not part of this gate, and is left out here. The gate's clauses:

| Plain name | What version 5 says | Where |
|---|---|---|
| L1, own-directed learning | own-directed accuracy above one in four at the 0.05 level, one-sided: 790 or more of 3,000 | 8.1, line 2915; section 9 row "Gate on learning", line 3062 |
| L2, named-other learning | the same bar on the named-other condition; arm F only ("both conditions on arm F") | 8.1, lines 2898 to 2907 and 2915 |
| L3, seeds for learning | on at least two seeds of three, the same seeds passing every condition | 8.1, line 2918; section 3, line 662; line 3083 |
| C1, collapse | with the acting channel zeroed, own-directed accuracy falls below the 8.1 bar (under 790) | 8.2, line 2966; line 3075 |
| C2, seeds for collapse | at least two of three seeds collapse, the same seeds that pass every other condition, the third reported | 8.2, line 2968 |
| C3, named-other with channel zeroed | reported, not gated | 8.2, line 2980 |
| C4, ownership-free line (the repair) | with the channel zeroed, the own-directed answer is the successor of one of the four agents' earlier values on the item named, on 1,546 or more of 3,000 | 8.2, line 2984; line 3075; 7.4, line 2794 |
| C5, seeds for the ownership-free line | at least two seeds of three, the same seeds, the third reported | 8.2, line 2995; 7.4, line 2794 |
| C6, named-other candidate count | the same count on the named-other condition, reported, not gated | 8.2, lines 3002 to 3003 |
| C7, what the code writes | for every arm and seed, the lesioned own-directed count and the lesioned candidate count | 8.2, line 3003 |
| Scope | the channel-removal clauses gate arm F only | 8.2 title, line 2957; line 3075 |

**The word search for leftovers.** `grep -i batter` over sections 0 to 16
(lines 121 to 4773) finds seven lines: 329, 629, 631 (the closed design's
record), 712 ("none of those is carried"), 2427 ("the control battery", an
idiom), 2986 (the sentence recording the replacement) and 4523 (the ruling's
record). I read each; none sets a condition. "question set" and
"end-of-episode" find only lines 711 and 2987, both saying the successor's
task has none. The finding's own test ("a clause with no field is the
finding") is answered in part 2.

## 2. The field each clause is judged on, and that it is in committed output

How the code judges each clause (main line, `measure.py`):

| Clause | Code | Field of the gate row |
|---|---|---|
| L1 | `seed_gate`: `at_least("own_correct")`, that is `own_correct >= bar` | `own_correct`, `bar` |
| L2 | `seed_gate`, arm F only: `other_correct >= bar` | `other_correct`, `bar` |
| C1 | `seed_gate`, arm F only: `lesioned_own_correct < bar` | `lesioned_own_correct`, `bar` |
| C4 | `seed_gate`, arm F only: `lesioned_candidate_own_correct >= g.get("ownership_free_line", 1546)`; field absent gives "not run", which counts against the seed | `lesioned_candidate_own_correct`, `ownership_free_line` |
| L3, C2, C5 | `withhold` gives a seed "no verdict" if any check is not passed; `arm_outcome` reads the arm only if two or more seeds each pass everything, and lists the rest under `reported_not_deciding` and `no_verdict` | (per-seed states above) |
| C3, C6 | written by `procedure.gate`; read by nothing in `seed_gate` | `lesioned_other_correct`, `lesioned_candidate_other_correct` |
| C7 | `procedure.gate` writes both counts for every arm, before the arm-F-only judgement | all of the above |

`procedure.gate` (lines 205 to 234) writes every one of these fields; it
asserts the line is 1,546 whenever there are 3,000 episodes.

The fields in committed rows, from `recount_from_rows.py`, part (b) (full
output in `recount_from_rows.out.txt`; columns are own, other, lesioned own,
lesioned other, lesioned candidate own, lesioned candidate other,
`ownership_free_line`, with "-" for a field that is absent):

```
$ python3 -I docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_rows.py
    out-a2-cases/r1: n=3000 bar=790  s0 1679/900/528/646/2100/-/-  s1 1654/900/555/636/2238/-/-  s2 1664/900/582/570/2324/-/-
    out-a2-cases/never-run-line: n=3000 bar=790  s0 1679/900/528/646/-/-/-  s1 1654/900/555/636/-/-/-  s2 1664/900/582/570/-/-/-
    out-a2-cases/toy: n=3000 bar=790  s0 1679/994/528/646/-/-/-  s1 1654/781/555/636/-/-/-  s2 1664/746/582/570/-/-/-
    out-check-training-exclusion/t6/10M/measure: n=750 bar=208  s0 86/88/86/88/350/372/399
    out-check-training-exclusion/t6/30M/measure: n=750 bar=208  s0 97/108/97/108/388/392/399
    out-dev-10m-check: n=3000 bar=790  s0 1689/924/435/690/-/-/-
```

So:

- **L1, L2, C1, C3** have their fields in every committed arm F row, the
  toy's real rows included.
- **C4's field** (`lesioned_candidate_own_correct`) is in 23 of the 28
  decision-procedure case folders at full size, filled from the rehearsal
  record by `tests/a2_cases.py` (`add_candidate_counts`), and deliberately
  absent in the cases built to test a missing field (case 17,
  "never-run-line", and the toy cases). It is in the two scaled pipeline rows
  written by the gate code itself, with its line and the named-other count
  (C6) beside it. It is **not** in the toy's own rows or the development row,
  which predate it; the code reports those as "the ownership-free line was
  not run", as the text says it will. This is condition 1.
- **`ownership_free_line`** is absent from every full-size committed row, so
  on those rows the code uses its constant, 1,546. The constant equals the
  rule's output (part 3a) and the code's self-test checks it ("the
  ownership-free line is 1,546 of 3,000, computed from the binomial tail":
  PASS; all 70 checks of `measure.py --self-test` pass).

**The field written at full size by the main line's own gate code.**
`code_gate_on_toy.py` runs `procedure.gate` on the twelve committed toy
models and commits the gate field it wrote (`code_gate_on_toy.json`):

```
$ ~/Code/minimum-viable-mind/.venv/bin/python docs/reviews/2026-10-09-rt237-closure-check-scripts/code_gate_on_toy.py
F/0: code writes lesioned_candidate_own_correct=2100, lesioned_candidate_other_correct=2214, ownership_free_line=1546, bar=790; independent recount same on all five counts; decision code's clause states {'own-directed learning': 'passed', 'named-other learning': 'passed', 'channel-removal collapse': 'passed', 'ownership-free line': 'passed'}
F/1: code writes lesioned_candidate_own_correct=2238, lesioned_candidate_other_correct=2542, ownership_free_line=1546, bar=790; independent recount same on all five counts; decision code's clause states {'own-directed learning': 'passed', 'named-other learning': 'failed', 'channel-removal collapse': 'passed', 'ownership-free line': 'passed'}
F/2: code writes lesioned_candidate_own_correct=2324, lesioned_candidate_other_correct=2366, ownership_free_line=1546, bar=790; independent recount same on all five counts; decision code's clause states {'own-directed learning': 'passed', 'named-other learning': 'failed', 'channel-removal collapse': 'passed', 'ownership-free line': 'passed'}
RESULT: the code's counts equal the independent recount on every model
```

On arms T, C and M the code writes the same fields (T: 3,000 on every seed;
C: 2,236, 2,160, 2,132; M: 2,770, 2,686, 2,660) and judges only own-directed
learning, as the text says (C7 and the scope row hold).

## 3. The recount from independent code

**(a) The lines.** `recount_from_rows.py` imports nothing from the project and
computes the exact binomial tail in whole-number arithmetic:

```
(a) the lines, exact binomial tail, integer arithmetic
    learning bar on 3,000 at one in four: 790 (tail 0.04851)
    ownership-free line on 3,000 at one half: 1546 (tail 0.04831)
    the same rule on 750 episodes (the scaled pipeline rows): bar 208, ownership-free line 399
```

Both match the text (790 and 1,546) and the code (`bar` and
`ownership_free_line` fields, and the scaled rows' 208 and 399).

**(b) The per-seed and arm-level decisions, from the committed rows.** For
every committed folder whose `summary.json` carries per-clause states (the 28
decision-procedure cases and the two scaled pipeline rows), my script judged
L1, L2, C1 and C4 from the raw counts by the text's rule and compared each
state with the code's; it also checked that a seed failing any clause is
never a reading seed, that the arm is never read with fewer than two seeds
passing every clause, that the seeds passing learning agree, and that the
reported-only counts (C3, C6) never appear among the gated checks (excerpt, lines picked from the output):

```
    out-a2-cases/split-learning-passes: clauses L1 L2 C1 C4 per seed s0:PPPP s1:PPFP s2:PPPF; seeds passing every gate clause (mine) [0]; code: learning [0, 1, 2], read False, seeds read []; outcome fifth
    out-a2-cases/F-channel-removal: clauses L1 L2 C1 C4 per seed s0:PPFP s1:PPFP s2:PPPP; seeds passing every gate clause (mine) [2]; code: learning [0, 1, 2], read False, seeds read [2]; outcome fifth
    out-a2-cases/never-run-line: clauses L1 L2 C1 C4 per seed s0:PPP- s1:PPP- s2:PPP-; seeds passing every gate clause (mine) []; code: learning [0, 1, 2], read False, seeds read []; outcome fifth
    out-a2-cases/r1: clauses L1 L2 C1 C4 per seed s0:PPPP s1:PPPP s2:PPPP; seeds passing every gate clause (mine) [0, 1, 2]; code: learning [0, 1, 2], read True, seeds read [0, 1, 2]; outcome R1
    clause states compared: 344; mismatches of any kind: 0
```

(P passed, F failed, "-" not run.) 344 of 344 clause states agree. The five
older summaries (the toy's freeze-test rows, the development row, the first
pipeline test) were written before the code recorded per-clause states, so
there is nothing to compare; my states for them are printed in the output.

**(c) The copied counts against their source.** The candidate counts in the
cases equal the committed rehearsal record
(`experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json`)
on all twelve models, and the toy rows' lesioned counts equal the record's,
which shows the record was taken on the same 3,000 episodes: "differences: 0".

**(d) The counts themselves, from the committed models.**
`recount_from_models.py` uses the project's episode generator and network
definitions only as the instrument, and builds the four candidates from the
token sequence (the item on the own-directed action turn, the four values
assigned to that item, each one's successor), not from the generator's stored
values or the code's `candidate_ids` (excerpt; every line is in the output file):

```
$ ~/Code/minimum-viable-mind/.venv/bin/python docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_models.py
gate episodes: the generator's evaluation-set digest matches the committed one: True
gate episodes: 3000 (from 1500 pairs, generator seed 99, pool 'dev')
the scored own-directed answer is one of my four candidates on 3000 of 3000 episodes
F/0: weights match SHA256SUMS True; own/other 1679/994; zeroed own/other 528/646; zeroed own-directed candidate count 2100 (passes 1,546); record (1679, 994, 528, 646, 2100): same
F/1: weights match SHA256SUMS True; own/other 1654/781; zeroed own/other 555/636; zeroed own-directed candidate count 2238 (passes 1,546); record (1654, 781, 555, 636, 2238): same
F/2: weights match SHA256SUMS True; own/other 1664/746; zeroed own/other 582/570; zeroed own-directed candidate count 2324 (passes 1,546); record (1664, 746, 582, 570, 2324): same
blind/0: zeroed own-directed candidate count 2784 (passes 1,546); record 2784: same
untrained-F/0: zeroed own-directed candidate count 0 (fails 1,546); record 0: same
untrained-F/1: zeroed own-directed candidate count 620 (fails 1,546); record 620: same
untrained-F/2: zeroed own-directed candidate count 726 (fails 1,546); record 726: same
arm F candidate counts: [2100, 2238, 2324] lowest margin over 1,546: 554
RESULT: every count equals the committed record
```

All eighteen models (arms T, C, M and F, the ordinary competing solver
called "blind" in the files, and three untrained models of arm F's
architecture) give exactly the record's counts. Both ends hold: every
trained model passes the line, the lowest being arm F seed 0 at 554 above it,
and every untrained model fails. These are the figures version 5 prints in
section 8.2 and section 17, failure 3.

**(e) The code against the recount.** `code_gate_on_toy.py` (part 2) shows
the main line's `procedure.gate` writes the same five counts as my recount on
every one of the twelve trained models.

## 4. Text and code, clause for clause

| Clause | Text | Code | Agree? |
|---|---|---|---|
| L1 | 790 or more of 3,000 | `own_correct >= bar`, bar 790 at full size | yes |
| L2 | same bar, arm F | `other_correct >= bar`, only when arm is F | yes |
| L3 | two of three, the same seeds passing everything | `withhold` per seed over every check; `arm_outcome` reads with two or more | yes |
| C1 | below the bar | `lesioned_own_correct < bar` | yes |
| C2 | two of three, same seeds, third reported | as L3; the third is listed with its reasons | yes |
| C3 | reported, not gated | written; not judged | yes |
| C4 | candidate count 1,546 or more of 3,000; candidates are the successors of the four agents' values on the item the action names | `>= ownership_free_line` (1,546); `candidate_ids` uses the own-directed item and all four agents' values; my token-built candidates give the same counts | yes |
| C5 | two of three, same seeds | as L3 | yes |
| C6 | reported, not gated | written; not judged | yes |
| C7 | both counts for every arm and seed | written for T, C, M and F (part 2) | yes |
| Missing field | stop S8: a gate that cannot be evaluated counts as failed | absent field gives "not run", which withholds the seed; case 17 lands on the fifth outcome term with "the ownership-free line was not run", as section 8.2 says | yes |
| Scope | arm F only | channel-removal clauses added only for arm F; self-test "the ownership-free line is not asked of arms T, C and M" passes | yes |

**Worth noting, not conditions** (none changes a decision):

- **The reason sentence hard-codes the full-size line.** `measure.withhold`
  writes "line 1,546 of 3,000" whatever the row's size. On the scaled
  pipeline rows (750 episodes), the seed was judged against 399, correctly,
  but the summary's reason reads "1,546 of 3,000"
  (`out-check-training-exclusion/t6/10M/measure/summary.json`). Registered
  rows are always 3,000, so the sentence is right where it counts. This is
  outcome wording, which the parallel branch is changing.
- **The two reported-only counts are not in the printed table.** The
  lesioned named-other accuracy (C3) and its candidate count (C6) are written
  to the row file, which is a report, but `procedure.table` prints only the
  own-directed lesion counts. Section 7.5, item 15, asks only for the
  collapse line and the ownership-free count in the table, so text and code
  agree; a reader of the table alone will not see C3 or C6.
- **What the line does not show** is stated in version 5 (section 8.2): a
  model that lost which item the action names would score about 2,257 and
  pass. I did not re-derive that figure; it is the earlier dispositions
  check's (pull request 96, section 6), and it limits what the clause claims,
  not whether the clause can be evaluated.

## What the parallel change could affect

The other session is changing, on branch `ruled-code-changes-2026-10-09`, the
fitting limit, the outcome wording, and the summary's wording for fewer than
three seeds. Against this verdict:

- **The fitting limit** changes how reads are fitted, so which seeds return a
  reading. It does not touch the gate fields or how a clause is judged. It
  could change which case seeds read, which my script compares only as "a
  reading seed never fails a gate clause"; that test would still apply.
- **The outcome wording** changes reason strings and outcome sentences. My
  scripts compare clause states and decisions, not wording, so the recount is
  unaffected; the first worth-noting item above may be fixed or reworded.
- **The summary for fewer than three seeds** could rename or reshape the
  arm-level fields (`seeds_passing_learning`, `read`, `readings`) my row
  recount reads; if so the script needs its key names updated, and the "two
  seeds of three" decision should be rechecked on the merged code.
- **Not affected:** the lines (790 and 1,546), the candidate counts, the
  model recount, and the clause-by-clause agreement of the text, unless the
  change also touches `seed_gate`, `withhold`, `arm_outcome` or
  `procedure.gate`. That is condition 2.

## Files

- `docs/reviews/2026-10-09-rt237-closure-check-method.md`, the method, committed first
- `docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_rows.py` and `.out.txt`: the lines, the fields and the decisions, standard library only
- `docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_models.py`, `.out.txt` and `recount_from_models.json`: the candidate counts from the eighteen models
- `docs/reviews/2026-10-09-rt237-closure-check-scripts/code_gate_on_toy.py`, `.out.txt` and `code_gate_on_toy.json`: the main line's gate code on the twelve trained models
