# Check of the A2 work: the successor's decision code brought to the 2026-10-06 rulings, and its run on 22 made-up cases

*Written 2026-10-06 (Pacific) by a Claude Code session that wrote none of the
code, the cases, the method note or the run. Checked: pull request 105, branch
`a2-decision-procedure` at `74967f8`. Rulings checked against:
`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` with its same-day
addenda (pull request 103, branch `rulings-2026-10-06-gate-a-v4`), and the
drafted texts it adopts: the inside dispositions' outcome table (RT-241), the
outside dispositions' seed rule and outcome precedence (A10), the
no-transplant change (A9), and the A2 work list and check (lines 247 to 323).
Laptop only, nothing trained or loaded: $0.*

*"Arm" is one of the four model designs (T, the separable model built to be
easy to read; C, the entangled model; M, the middle model; F, the free model
the experiment exists to read). A "seed" is one of an arm's three training
runs. "Withheld" means a reading is replaced by "no verdict" with its reasons.
"The fifth term" is "metric validated, degree not read".*

## Verdict in one paragraph

The code does what the rulings say on every one of the 22 cases: my own
rules, written from the ruling text without importing the author's decision
code, land every case on the same outcome as the code and as the expectation
written before it ran. No withheld reading appears in any output file or
table, and the field that used to carry them is gone. The inputs are the
committed toy records, byte for byte. All self-tests pass. **One part of the
check fails as the dispositions word it:** turning off the floor on fresh
episodes changes no case's outcome, so that rule is not tested by the cases
(it is tested by a unit test). Under the check's own words, "the finding
stays open" until a case is added. One small wording gap and three points
for John are below.

## The five points of the check

| # | Point | Verdict |
|---|---|---|
| 1 | Recompute every outcome independently | **Pass.** 22 of 22 agree (mine = code = written expectation) |
| 2 | No withheld reading in `summary.json` or `table.md` | **Pass.** 0 leaks; every coincidental number traced to another field |
| 3 | Turn each rule off, see at least one case change | **Fails for one rule: the floor on fresh episodes.** Every other listed rule passes |
| 4 | Every registered term reached; nothing unregistered | **Pass.** All seven reachable terms reached; R4 excepted, rightly |
| 5 | Inputs confirmed by SHA-256 | **Pass** |
| - | Method before output, by commit order | **Pass** |
| - | Expectations follow from the ruling text | **Pass**, with the readings assessed below |
| - | Existing self-tests | **Pass** (`ALL SELF-TESTS PASS`, 219 passing lines) |

### 1. Every outcome recomputed

`2026-10-06-a2-decision-procedure-check-scripts/recompute.py` imports only
`tests/a2_cases.py` (the case definitions: which fields of the toy rows each
case changes, which is the input under test) and neither `measure.py` nor
`procedure.py`. Its rules, from the ruling text:

- **Per seed (page 7):** a seed counts only if it passes its learning gate
  (own-directed answers at or above the bar; on arm F also named-other),
  recomputed from the counts, not the stored true/false flags; on arm F the
  channel-removal check (own-directed answers below the bar with the channel
  zeroed, and the ownership-free line, 1,546 or more of 3,000; an absent
  field fails, stop S8); and every check that withholds (nomination passed,
  not description-only, floor on fresh episodes, floor on development
  episodes, control 7, control 1 on arm T, control 4). The no-transplant rate
  withholds nothing (page 8).
- **Per arm:** passes its gate if two seeds learn; reads if two seeds count.
- **Outcome (pages 5 and 9):** arm F failing its learning gate on its step 5a
  seed is R3 (stop S4). Arm T or C failing its gate is R3. Arm F failing its
  gate with no step record is R3 (the author's reading 2, assessed below).
  Then arm T no verdict gives "metric not validated"; arm C no verdict gives
  one of the two "checked against the separable model only" terms, by whether
  arm F reads; otherwise arm C's lowest counted reading minus arm T's highest
  under 0.5 gives R2, and if they separate arm F reading gives R1, else the
  fifth term. Arm M never changes the term.

Result (`base.json`): every case agrees.

| Case | Written expectation | Code | Mine |
|---|---|---|---|
| toy | R3 | R3 | R3 |
| toy, seed 0 as step 5a | fifth | fifth | fifth |
| toy, seed 1 as step 5a | R3 | R3 | R3 |
| r1 | R1 | R1 | R1 |
| r2 | R2 | R2 | R2 |
| fallback-read | checked vs separable only, read | same | same |
| fallback-not-read | checked vs separable only, not read | same | same |
| T-no-verdict | not validated | same | same |
| T-and-C-no-verdict | not validated | same | same |
| split-review-table | fifth | fifth | fifth |
| split-learning-passes | fifth | fifth | fifth |
| split-one-seed-everything | fifth | fifth | fifth |
| overlap-one-seed | R1 | R1 | R1 |
| M-outside-band | R1 | R1 | R1 |
| M-fails-gate | R1 | R1 | R1 |
| withheld-seed | R1 | R1 | R1 |
| never-run-line | fifth | fifth | fifth |
| never-run-control | checked vs separable only, read | same | same |
| no-transplant-outside | R1 | R1 | R1 |
| F-channel-removal | fifth | fifth | fifth |
| T-fails-gate | R3 | R3 | R3 |
| F-fails-5a | R3 | R3 | R3 |

### 2. Withheld readings appear nowhere

`leaks.py` takes every seed that **my** rules withhold and that has a computed
figure (48 seed-cases in all), and lists every value in that case's
`summary.json` equal to the figure, with its full path, and that seed's
reading cell in `table.md`. Output: `leaks.txt`. **No figure sits at its own
seed's reading or degree in either file. Every table cell for a withheld seed
reads "no verdict: …" with the reasons. `arithmetic_withheld` appears in no
output.**

The author warned that 1.0 / 1.0000 and 0.0 occur for other reasons. The
hits are all elsewhere, traced in `coincidences.txt`: for 0.0, other arm T
seeds' legitimate readings (arm T's readings are all 0.0 by design), the
no-transplant fields, seed number 0 in lists of seeds, and the step record's
seed number; for 1.0, seed number 1 in the same lists and the step record.
In the table, the 1.0000 hits the author's search found on the toy are in
arm T's and other columns' cells (whole and ownership-only accuracies,
control 6), never in arm F's reading column. The test figure 0.123456
(withheld-seed) and the 1.0108 of arm F seed 2 appear nowhere at all.

### 3. Each rule turned off in turn

Each rule was switched off in my recompute and the 22 cases rerun
(`off_*.json`). Changes:

| Rule turned off | Cases whose outcome changes |
|---|---|
| control 7 | fallback-read (to R1), fallback-not-read (to fifth) |
| control 1 on arm T | T-no-verdict (to R1), T-and-C-no-verdict |
| control 4 | never-run-control (to R1) |
| **floor on fresh episodes** | **none** |
| piece floor (nomination) | fallback-not-read |
| learning gate | toy, toy seed 1, split-one-seed-everything, T-fails-gate |
| seed rule (back to separate two-of-three counts) | split-learning-passes, split-one-seed-everything (both to R1) |
| collapse (arm F channel removal) | split-one-seed-everything, F-channel-removal |
| ownership-free line | never-run-line |
| floor on development episodes (not on the dispositions' list) | none |

**Defect 1 (the check's point 3 is not met).** No case fails the floor on
fresh episodes on enough seeds to matter, so removing that rule changes
nothing. The dispositions' check (outside dispositions, A2, point 3) names
"the fresh floor" and says "a rule whose removal changes no case is untested,
and the finding stays open". The rule is coded and has a unit test
(`withhold: floor missed on fresh episodes -> no verdict`, passing), so this
is a gap in the cases, not in the code. **Fix:** one added case (for
example, arm C's fresh floor failing on two seeds, expected "metric checked
against the separable model only, degree read"), with its expectation
committed before it runs. The floor on development episodes is in the same
state, though the dispositions' list does not name it.

### 4. Every term reached, nothing unregistered

Terms in the 22 `summary.json` outcomes and `table.md` "outcome:" lines: R1,
R2, R3, the fifth term, both "metric checked against the separable model
only" terms, and "metric not validated". That is every registered term the
records can reach. R4 is a missed date, not something records can show, and
is rightly excepted. No other term appears; every reason follows its term
after a colon. The scope phrase "on these constructed systems, for this
intervention procedure" follows every "metric validated" and the three new
terms in the reported sentence, and "as a ratio of two transplants at the
sites this procedure chose" follows "degree read" (r1 table, checked by eye
and by the author's `sentence_has`).

### 5. Inputs

The 12 toy rows in `out-freeze-tests/t3a-committed-reads/` hash to the same
SHA-256 values in my run as in the author's `results.json`
(`inputs_sha256`), and the directory is byte-identical to `origin/main`, last
touched by the code-freeze commit `db49cd2`. The values are in `base.json`.

### Method before output

`590a630` (10:08) adds only the method note and `tests/a2_cases.py`, no code.
`6583a5f` (10:11) changes the code. `74967f8` (10:15) adds the outputs and the
findings note. `a2_cases.py` is unchanged after `590a630`
(`git diff 590a630 HEAD -- tests/a2_cases.py` is empty).

### Expectations against the ruling text

Every expected outcome follows from the ruling text under the readings below;
my independent rules reproduce all 22. The two checks I made by hand on the
borrowed inputs: the ownership-free line, 1,546 of 3,000, is the smallest
count whose chance of arising at a coin-flip rate is 5 per cent or less
(exact binomial, recomputed); and the borrowed counts match the committed
rehearsal check (`lesion_content_check.json` on the rulings branch), whose
channel-zeroed own-correct counts equal the toy rows' (528, 555, 582 on arm F;
740, 753, 820 on arm T), so both were taken on the same episodes.

**Minor gap (defect 2).** RT-241's rule 1 says R3 names "the arm and the
condition". The code's R3 sentences name the arm and "its gate on learning",
but not which condition failed (on the toy, arm F's named-other condition;
in T-fails-gate, own-directed). The per-seed reasons carry it, so nothing is
lost, but the outcome sentence itself falls short of the drafted text. A
one-line fix.

## The author's seven readings

| # | Reading | Assessment |
|---|---|---|
| 1 | A step record, `steps.json`, names arm F's step 5a seed; with no record and arm F failing, R3 | **Faithful, but version 5 must register it.** The ruling makes the outcome depend on which seed ran at step 5a, and the rows do not record that, so something must. R3 by default is the cautious choice: the fifth-term exception exists only for a free model shown to have passed at 5a. The ruling's toy sentence ("fifth term if its passing seed is taken as the step 5a run, R3 otherwise") is reproduced by the three toy cases. The step record is a new registered input; version 5 should name it and say the launcher writes it. No ruling needed unless John wants it said differently. |
| 2 | "Not run" (field absent) versus "could not be evaluated" (field present but empty); both count against, under stop S8 | **Faithful.** Labels differ, consequence is stop S8's. |
| 3 | Only the learning gate triggers R3; arm F's channel-removal failure gives no verdict | **Faithful.** RT-241's table lists "fails the channel-removal check of section 8.2" in arm F's column, mapped to the fifth term or the fallback's "not read", so it is not an R3 cause. |
| 4 | Scope phrases placed after every "metric validated" and the three new terms; none on R2 | **Faithful to the letter; one question for John.** The addendum names "metric validated" and "the three new terms of page 5". R2, "metric does not separate", is in neither group. But it makes a claim about the metric on the same constructed systems and procedure, so the same limit arguably applies. |
| 5 | R4 unreachable | **Faithful.** R4 is a schedule outcome. |
| 6 | "Combination" for control 5 read as the episode's whole content | **Faithful as a minimum; question for John.** The adopted line asserts "no fresh or relaxed episode's combination occurs in the training stream". Whole-content non-overlap is the weakest reading: a fresh episode whose defining combination (whatever makes it "fresh" or "relaxed") also occurs inside some training episode with other content changed would pass this test. If "combination" means the defining feature pairing, the check should test that. |
| 7 | Borrowed ownership-free counts 2,100 / 2,238 / 2,324 for arm F (and the other arms) | **Faithful.** They are the committed rehearsal check's counts on the same 3,000 episodes, used only in made-up cases; the toy-as-is case leaves the field absent, as the real toy records are. |

## Questions for John

1. **The scope phrase on R2.** Should "metric does not separate" also carry
   "on these constructed systems, for this intervention procedure"? The ruling
   does not cover it; the code leaves it off.
2. **Control 5's "combination".** Does the generator self-test's "no fresh or
   relaxed episode's combination occurs in training" mean the whole episode
   content (as built), or the specific pairing that makes an episode fresh
   or relaxed (a stronger test)?

Not a question, for the version 5 writer: register the step record that names
arm F's step 5a seed.

## Owed before this check closes

Defect 1: one case that fails the fresh-episode floor, expectation committed
first, rerun, and this script's point 3 rerun. Defect 2 is a wording fix to
the R3 sentence.

## Files

- `2026-10-06-a2-decision-procedure-check-scripts/recompute.py`: independent
  rules; `python recompute.py [rule ...]` with rule names `c7 c1 c4 fresh
  piece dev gate seedrule collapse line` to switch one off.
- `base.json`, `off_*.json`: its outputs, with the input hashes.
- `leaks.py`, `leaks.txt`, `coincidences.txt`: point 2.
- `self-tests.txt`: `run_self_tests.sh` output on this branch.
