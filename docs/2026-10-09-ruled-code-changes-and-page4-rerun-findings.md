# The code changes ruled on 2026-10-08, and the page 4 re-run under them: findings

*Written 2026-10-08 (Thursday evening, Pacific) by the Claude Code session
that made the changes and ran the passes, on branch
`ruled-code-changes-2026-10-09`; the file carries the date the task named for
it. The method was committed and pushed first, before any code changed:
`docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md` (commit
`3d31fd2`). Laptop only, processor only, $0: nothing rented, no paid service
called, no key handled.*

*Written under the workspace plain-language rule. Changes to frozen, not yet
registered code, and a rehearsal on the committed toy models. NOT A RESULT
about the scientific question. Owed: a check by a session that did not do
this (item 7 of the rulings asks for it before the registration commit).*

## The short version

- **The changes are in the frozen code** (`experiments/08-successor-degree/src/`,
  commit `70a6fb0`). Every read is fitted on the first 1,800 of 1,980
  development episodes and scored on the last 180, at an iteration limit of
  10,000; the transplant passes stay on the 600 pairs. The code prints
  version 5's outcome words, all eight, with their scope phrases. An arm with
  fewer than three seeds whose gate could still pass is reported as "gate not
  decidable on one seed" (or two), and no term is given. Arm T's row-choice
  split is written beside its gate and in the table, reporting only. Arm M's
  per-step copy is unchanged, as ruled.
- **Every test passes.** Every self-test (265 checks); the 31 made-up decision
  cases (28 old, 3 new); the in-use cases (14); the model-loading test; the
  launcher test; and the whole-pipeline test at 10 and 30 million parameters
  (section 4).
- **The port reproduces the checked record exactly.** Run with its limit set
  back to 3,000, the new code gives the page 4 re-run's 1,800-fitted figures
  value for value: 29,077 values and every read array, none different, and the
  same iteration-limit warnings on all twelve models.
- **Fits stopping at the limit: arm M from 471 to 0.** At 10,000 no fit stops
  at the limit on any model or in the solver: arm M 471 to 0, arm F 23 to 0,
  arm C 1 to 0, arm T 0 to 0, the solver 2 to 0. At 420 fitting episodes arm
  M had 27.
- **The old warnings were not the reads that decide anything.** The new count
  by kind shows that of arm M's 471, **467 were fits of the shuffled-label
  null** (a reference printed beside the floor, not a bar) and **4 the named
  agent's read**, which arm M never uses (control 2 does not apply to it). **The
  ownership read, the one registered read, never stopped at the limit on any
  model.** So version 5's sentence that arm M's reads at 1,800 "are partly a
  product of where the fitter stopped" is wrong and should be replaced
  (section 3).
- **No toy decision moves, and no figure version 5 quotes changes.** None of
  the pre-stated concerns happened. Every site set, piece, reading, true-slot
  reading, control, best piece, control 2's figures on the free model's seed
  0, and the solver's best pieces are identical to the checked 1,800 record.
  What moved: the shuffled-label null's mean by at most 0.05 of an episode
  (one maximum, arm M seed 1 at state 3, from 24 to 25 of 180), and the named
  agent's read directions on five models where control 2 is not used.
- **The outcome, summarised under the current decision code** (owed since the
  page 4 check): **R3, "substrate not a testbed": arm F failed its gate on
  learning (named-other condition, on seeds 1 and 2)**, as expected. In that
  summary arms C and M are withheld on every seed by the in-use check
  ("construction did not hold"), because these toy models were trained with
  the sharpness learned and their built route is not in use at the ruled bar.
  So the summary computes no separation; the separation from the rows'
  arithmetic, which version 5 quotes, is 1.0000, as before.
- **Two predictions were wrong, both on the cautious side.** I expected some
  of arm M's warnings to remain (under 25), and some of its figures to move
  slightly; none remained, and none of its quoted figures moved.

## 1. What changed, file by file

| File | Change |
|---|---|
| `src/grammar.py` | A named evaluation set `dev_reads`: 1,980 pairs from the same generator and seed as the 600, whose first 600 are the 600 (self-test). As an evaluation set its 1,380 new contents join what training refuses. The pinned digest of the evaluation sets is re-pinned (`a5a39300...`); the first training batch's digest is unchanged. |
| `src/measure.py` | The numbers: 600 transplant pairs; reads on 1,980, fitted on 1,800, 180 held out; iteration limit 10,000. Version 5's eight registered terms, codes R1, R2, R3, fifth, sixth, seventh, eighth (version 4's names kept beside them as history, never printed); every sentence carries its scope phrases. `arm_outcome` reports whether the gate is decidable; `outcome` gives no term, with the reason "arm X: gate not decidable on one seed", when a gate is not decidable and none has failed outright. Arm M with an undecidable gate is "not decidable", not "dropped". |
| `src/procedure.py` | Every read, its held-out counts, the null, control 2's counts and the counts elsewhere on the site use the 1,980 (`EvalData.read_pool`); the transplant passes use the 600. One fitting function at the ruled limit, counting fits that stop at the limit by kind, written into each row (`fits_stopped_at_iteration_limit`) and the log. Each row records its split (`read_split`). `gate` writes arm T's row-choice split (`row_choice`), and the table prints it in a new last column. `summarise` passes an undecidable gate on as such. |
| `tests/a2_cases.py`, `tests/a2_run_cases.py` | A dated addendum maps the old codes and words to the new ones, so the 28 original expectations stand unedited; three new cases for short seed counts; the runner writes to a folder named on its command line, leaving `out-a2-cases/` as committed. |
| `tests/page4_ruled_*.py`, `tests/page4_ruled_lanes.sh`, `tests/replay_stream_dev_reads.py`; `../rehearsal-successor-measure/src/page4_solver_10k.py` | The drivers, the comparison, the training-stream replay and the solver wrapper, each committed before its outputs existed. |
| `README.md` | A paragraph on these changes. |

**Two checks of the new pieces against earlier records.** The row-choice
split, run on the 10-million arm T checkpoint, gives the development-runs
check's figures exactly: the right row on 2,586 of 3,000, 164 of the 414
wrong-row episodes right by coincidence (0.396), 2,999 with the row forced,
and the same six confused pairs of name words. On the twelve toy models it
gives the right row on 3,000 of 3,000 for every arm T seed, as predicted. And
the training stream, replayed over the registered 108,919 steps of 48 pairs,
**draws none of the 1,380 new development episodes on seed 0, 1 or 2**
(5,228,112 contents each; `out-ruled-code-changes/tests/replay_stream_dev_reads.txt`),
so adding them to the exclusion changes no training step.

## 2. The page 4 re-run under the new code

The same twelve committed toy models (checked against `SHA256SUMS`) and the
competing solver, three models side by side, 3 processor threads each. Pass A
ran 15:06 to 15:52, pass B 15:52 to 16:32, the solver 12.7 minutes after; the
one-minute load, read at the start and at checks along the way, was between
about 2.5 and 5.6.

### 2a. Pass A, the reproduction check: passes

    reproduction check, pass A (the ruled code, limit set back to 3,000) against the checked 1,800 record:
    29077 values compared, 0 differ; iteration-limit warnings equal on 12 of 12 models: PASSES

Against `experiments/rehearsal-successor-measure/out-page4-rerun-1800/models-1800/`
(the page 4 re-run, checked). Fields present in one record only are listed
and not compared: the ones added since that run (the ownership-free line, the
in-use check, the row-choice split, the split and the limit counts, and four
no-transplant fields), and one it had that the current code no longer writes
(`detection_margin_at_the_bar`). Read arrays: identical on all twelve.
Output: `out-ruled-code-changes/reproduction.json`.

### 2b. Fits that stopped at the iteration limit

Warnings counted as the page 4 re-run counted them (`grep -c "failed to converge"`
on each model's log), and, new, counted by the code in each row:

| | at 420, limit 3,000 | at 1,800, limit 3,000 | at 1,800, limit 10,000 |
|---|---|---|---|
| Arm T, three seeds | 0 | 0 | 0 |
| Arm C | 2 | 1 | 0 |
| **Arm M** | **27** | **471** (132, 240, 99) | **0** |
| Arm F | 30 | 23 | 0 |
| Solver, both readings | 0 | 2 | 0 |

Where the 3,000-limit stops were (pass A's per-kind count, which reproduces
the warnings exactly):

| Model | Shuffled-label null | Named agent's read | Ownership read, its counts, counts elsewhere |
|---|---|---|---|
| Arm M seeds 0, 1, 2 | 130, 239, 98 (of 1,000 each) | 2, 1, 1 (of 5) | 0 |
| Arm F seeds 0, 1, 2 | 2, 10, 10 | 0, 1, 0 | 0 |
| Arm C seed 2 | 0 | 1 | 0 |

At 10,000 the most iterations any fit took was 7,385 (arm M seed 0's null);
the most any ownership read took was 2,960 (arm F seed 2), and on the built
arms 80. The full table, model by model and kind by kind, is in
`out-ruled-code-changes/comparison.md`.

### 2c. Old against new: every figure version 5 quotes

Old is the checked 1,800 record (limit 3,000); new is pass B (limit 10,000).
Counts are correct of 180 held-out episodes; the floor is 144.

| Figure, as version 5 quotes it | Old | New |
|---|---|---|
| Arm T readings, seeds 0, 1, 2 | 0.0000, 0.0000, 0.0000 | 0.0000, 0.0000, 0.0000 |
| Arm T site set and piece | state 0 at the action, 8 directions; 180 | same; 180 |
| Arm C seed 0: site set, piece, reading | state 2 at the action, 4 directions; 178; 1.0026 | same; 178; 1.0026 |
| Arm C seed 1 | state 4 at the action, 8 directions; 178; 1.0000 | same; 178; 1.0000 |
| Arm C seed 2 | state 1 from the first own turn, 4 directions; 165; 1.0000 | same; 165; 1.0000 |
| Separation, arm C's lowest minus arm T's highest | 1.0000 | 1.0000 (from the rows; see 2d) |
| Arm M readings | 0.5252, 0.4793, 0.5208 | 0.5252, 0.4793, 0.5208 |
| Arm M true-slot readings | 0.5000, 0.4760, 0.4920 | 0.5000, 0.4760, 0.4920 |
| Arm M distance from its true slot | 0.0252, 0.0033, 0.0288 | 0.0252, 0.0033, 0.0288 |
| Arm M seed 0's site set | state 3 at the action, 8 directions | same |
| Arm F best piece anywhere (ownership read) | 40, 19, 36 | 40, 19, 36 |
| Arm F status | no verdict on every seed | no verdict on every seed |
| Control 2 on arm F seed 0 | reported; named read's best piece 176; chosen state 3 at the action, 8 directions, piece 171; own-directed moved 0.0000 against a random median 0.0025 | identical |
| Control 2 returns a figure on | 1 toy model of 6 | 1 of 6 |
| Solver best piece, both readings, three seeds | 17 to 20; no reading | 17 to 20; no reading |
| Section 17's failure 1 table (no-transplant, whole and own accuracy per model; smallest denominator 0.4863 on arm C seed 2) | as printed | identical |
| Section 17's failure 2 grid (whole read and best piece per state) | as printed | identical |
| Controls 7 and 4 (chosen, stricter and sensitivity rows) | hold | hold |

The script compares 18 fields per model (`model_line` in
`tests/page4_ruled_compare.py`); **none changed on any model**. Pass B
against pass A, all fields: 65 of 29,514 values differ, and every one is the
limit count, the recorded limit, the shuffled-label null's mean (by at most
0.05 of an episode) or maximum (one: arm M seed 1, state 3, 24 to 25), or the
null printed beside arm M's chosen site. The read arrays differ only in the
named agent's read, on arm M (all three seeds), arm C seed 2 and arm F seed 1,
where control 2 is not used (not applicable on arm M; no verdict on the other
two, which fail the named-other gate).

### 2d. The seven concerns, and the outcome

    - A: a built model (arm T, C or M) loses its nomination: no
    - B: arm T's reading is not 0.0000, or its control 1 does not hold: no
    - C: the separation (arm C's lowest minus arm T's highest) is below 0.5 or missing: no
    - D: arm M's reading is outside 0.3 to 0.7 on a seed: no
    - D2 (arm M's prediction): further than 0.10 from its true-slot reading on a seed: no
    - E: the free model's read reaches the floor (a piece of 144 or more anywhere): no
    - F: the solver returns a reading: no
    - G: control 7 or control 4 fails anywhere (the chosen, stricter and sensitivity rows): no
    - Fields that changed, by model: none

**No toy decision moves.**

The summary under the current decision code (`passB-limit10000/summary.json`,
`table.md`), the re-summary the page 4 check said was owed:

    outcome: substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2)

Per seed: arm T reads 0.0000 on all three, each row passing the in-use check
and showing the right row on 3,000 of 3,000. Arms C and M return no verdict on
every seed, "the built ownership route has gone flat (construction did not
hold)" (arm C: route use 0.269 on seed 0, the built answer flat on seeds 1 and
2; arm M: its stirred-in route's use 0.071, 0.090 and 0.109). Arm F: no
verdict, the read's floor on seed 0 and the named-other gate on seeds 1 and 2.
This is what the method expected: these toy models were trained before the
sharpness was fixed, and the sharpness findings already showed their built
routes fail the ruled bar. **So, under the current code, the toy summary
itself no longer reads arms C and M and computes no separation**; the
per-model arithmetic version 5 quotes is in each row, and the separation from
it is 1.0000. Version 5's toy sentence ("the anchors separate, the middle
model reads in its band") is about that arithmetic, and should say so (section
3, item 4).

## 3. What version 5 would need to change

Not edited here. No quoted figure changes; what changes is wording, citations
and the status of owed work.

1. **Section 7.2, item 1, the second caution** ("at 1,800 the straight-line fit
   stopped at its iteration limit of 3,000 far more often on arm M (471
   warnings against 27 at 420), so arm M's reads there are partly a product of
   where the fitter stopped, and a wider model may hit the limit more often
   still"): the second half is wrong. The 471 were 467 fits of the
   shuffled-label null and 4 of the named agent's read; the ownership read
   never stopped short. At 10,000 no fit stops on any toy model. The ruled
   note after it ("until then the frozen code still fits on 420 of 600 at
   3,000") is now out of date: the code fits on 1,800 of 1,980 at 10,000. A
   wider model may still need more iterations, which the per-row count will
   now show.
2. **Weakness W15** (section 13: "At 1,800 the fitter stopped at its iteration
   limit far more often on arm M"): the same correction.
3. **Every citation of the page 4 figures** (section 3, twice; sections 5.2 and
   5.3; section 7.3, item 2, and its last paragraph on the solver; section
   10, R-3, R-4, R-10 and the page 4 paragraph; section 17, failures 1 to 4):
   the figures stand; they can now also cite this re-run under the frozen
   code itself, once it is checked.
4. **The toy outcome line** (section 3; section 10's page 4 paragraph;
   section 17, failure 4, "pre-A2 rules, to be re-summarised"): now
   re-summarised under the current decision code, R3 as above. Version 5
   should add that under the current code the toy summary withholds arms C
   and M by the in-use check, so its separation and arm M's band are figures
   from the rows' arithmetic, not from the summary (it already says these toy
   models had the sharpness learned, section 3's last caution).
5. **Section 11, step 3** ("Two changes still owed in the code"), **section
   17, failure 4** ("The renamed words are not yet in the code"), and the
   ruled notes of section 21, items 3, 7 and 9: done, at the commit this
   branch merges as; owed only its check.
6. **Section 7.4**: the registered code is named after these changes land
   (open item 10), at the main-line commit this pull request makes. Its pinned
   digest of the evaluation sets has changed (section 1).
7. **Section 7.5, item 15**: arm T's row-choice split is now printed, in the
   table's last column.

## 4. Tests, exactly

All outputs in `experiments/08-successor-degree/out-ruled-code-changes/`.

- `src/run_self_tests.sh` (test T1): **ALL SELF-TESTS PASS**, exit 0; 265
  checks passed, 0 failed (`tests/t1-self-tests.txt`).
- `tests/a2_run_cases.py out-ruled-code-changes/a2-cases`: 31 cases, 0 differ
  from expectation or leak (`tests/a2-cases-stdout.txt`, `a2-cases/results.md`).
- `tests/inuse_cases.py`: 14 checks, 0 differ (`tests/inuse-cases-stdout.txt`).
- `tests/load_toy_models.py` (test T2): **T2 PASSES** (`tests/t2-load-toy-models.txt`).
- `tests/check_launcher.sh` (test T7): all checks pass; nothing created,
  nothing spent (`tests/t7-check-launcher.txt`).
- `tests/pipeline.sh` (test T6, every set at a quarter, three shuffles):
  **runs to the end at both sizes**, exit 0, 16:45 to 18:18 (`t6-stdout.txt`,
  `t6-pipeline/`; the trained checkpoints are not committed). Every arm trains
  30 steps and is measured; each row records its split (495 reads'
  development episodes at a quarter, fitted on 450, 45 held out; 150
  transplant pairs) and that no fit stopped at the 10,000 limit; at 30 million
  the family is 325 site sets and 1,300 comparisons. Arm T's row-choice split
  is written at both sizes (750 of 750 on these barely trained models). The
  summary, with one seed per arm, now says **"not computed: arm T: gate not
  decidable on one seed; arm C: gate not decidable on one seed; arm F: gate
  not decidable on one seed"**, where the freeze's run of the same test said
  R3. That is the ruled change of item 9, seen on a real pipeline. Measuring
  one 30-million model at a quarter of the episodes took 18 to 22 minutes.
- Test T3 compares against the 420-fitted toy record, so under the new
  fitting count it differs by design and was not run; pass A replaces it.

## 5. How to recompute

From `experiments/08-successor-degree/`, on a quiet laptop (about 45 minutes a
pass with three lanes):

    sh tests/page4_ruled_lanes.sh out-ruled-code-changes/passA-limit3000 3000
    sh tests/page4_ruled_lanes.sh out-ruled-code-changes/passB-limit10000
    (cd ../rehearsal-successor-measure/src && ~/Code/minimum-viable-mind/.venv/bin/python \
       page4_solver_10k.py --pool 1980 --out ../../08-successor-degree/out-ruled-code-changes/solver-limit10000)
    ~/Code/minimum-viable-mind/.venv/bin/python tests/page4_ruled_compare.py

A checker going around these scripts can run `procedure.py model` on any
committed toy model directly; nothing is patched at run time for pass B.

## What this does not do

It does not edit version 5, any ruling or the rehearsal's committed code, and
merges nothing. It does not name the registered commit (open item 10). It
issues no go and spends nothing.
