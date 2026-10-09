# The end-to-end test of the decision code, re-run on the final code: findings

*Written 2026-10-08 (Thursday night, Pacific) by the Claude Code session that
ran it, on branch `e2e-final-code`. The method was committed and pushed first,
before anything ran: `docs/2026-10-08-end-to-end-final-code-method.md`
(commit `d4fd026`). Laptop processor only, nothing rented, no paid service
called: $0. Outputs in `experiments/08-successor-degree/out-e2e-final-code/`.*

*Written under the workspace plain-language rule. A test of the decision
code, not a result about the scientific question. Owed: the check ruling 3
asks for, by a session that did not do this run.*

## The short version

- **Everything landed where the method said it would. No case missed, nothing
  surprising.**
- **All 31 made-up decision cases land on the term written for each in
  advance**, with every expected text piece in the sentence, and no withheld
  figure appears in any output. The terms and sentences are the same, word
  for word, as the run on the code of 2026-10-08 (pull request 151).
- **The toy case and the toy summary at the registered limit** both read
  **"substrate not a testbed: arm F failed its gate on learning (named-other
  condition, on seeds 1 and 2)"**. The toy summary's `summary.json` is
  byte-for-byte the committed one.
- **The in-use cases**: 14 checks, none different from expectation; the output
  file is identical to the last run's.
- **The self-tests**: all 265 checks pass.
- **The whole-pipeline test** (test T6 of the code freeze) runs to the end at
  10 million and 30 million parameters, exit 0, and at both sizes says "not
  computed: arm T: gate not decidable on one seed; arm C: gate not decidable
  on one seed; arm F: gate not decidable on one seed".
- **The one visible change is the one pull request 153 made**: every table row
  for a withheld seed now has 11 "withheld" cells, not 12, so every row has as
  many cells as its header. Nothing else in any output moved.
- **The code that ran**: commit `d4fd02658426987d256c595d09197e82fa14e5ec`
  (the method note on top of `6c47c56`, the last batch before the
  registration, pull request 153; the code folder is the same as at
  `6c47c56`). Checksums in section 5, the same at the start and the end.

## 1. The made-up decision cases, expected against printed

`tests/a2_run_cases.py out-e2e-final-code/a2-cases`, exit 0:
"31 cases; 0 differ from expectation or leak". Inputs are the committed toy
rows (`out-freeze-tests/t3a-committed-reads/`), checked by SHA-256 against the
same twelve digests as before.

The codes stand for version 5's eight outcome words: R1 "instrument
discriminates specified constructed mechanisms, degree read"; R2 "instrument
does not discriminate the specified constructed mechanisms"; R3 "substrate not
a testbed"; fifth "instrument discriminates specified constructed mechanisms,
degree not read"; sixth "instrument checked against the separable mechanism
only, degree read"; seventh "instrument checked against the separable
mechanism only, degree not read"; eighth "instrument returned no reading on
the separable mechanism". "None" means no term is given, because a gate is not
decidable on the seeds present (cases 29 and 30, the short seed counts).

| # | case | expected | printed | every expected piece found | withheld figure found in outputs | term as printed |
|---|---|---|---|---|---|---|
| 1 | toy | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2) |
| 2 | toy-step5a-seed0 | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: failed its gate on learning |
| 3 | toy-step5a-seed1 | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning at step 5a (named-other condition, on seed 1), after its re-run; nothing else launches (stop S4) |
| 4 | r1 | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 5 | r2 | R2 | R2 | yes | none | instrument does not discriminate the specified constructed mechanisms |
| 6 | fallback-read | sixth | sixth | yes | none | instrument checked against the separable mechanism only, degree read |
| 7 | fallback-not-read | seventh | seventh | yes | none | instrument checked against the separable mechanism only, degree not read: read failed its floor: no size's piece reaches four fifths; reported for description only (the site set was chosen with the piece rule switched off) |
| 8 | T-no-verdict | eighth | eighth | yes | none | instrument returned no reading on the separable mechanism: control 1, the content transplant, on arm T failed |
| 9 | T-and-C-no-verdict | eighth | eighth | yes | none | instrument returned no reading on the separable mechanism: control 1, the content transplant, on arm T failed |
| 10 | split-review-table | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: failed its gate on learning |
| 11 | split-learning-passes | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: read failed its floor: no size's piece reaches four fifths; the channel removal did not collapse own-directed answers below the gate bar; the ownership-free line failed (with the channel zeroed, own-directed answers among the four candidates, line 1,546 of 3,000) |
| 12 | split-one-seed-everything | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: failed its gate on learning (named-other condition: failed); the channel removal did not collapse own-directed answers below the gate bar |
| 13 | overlap-one-seed | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 14 | M-outside-band | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 15 | M-fails-gate | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 16 | withheld-seed | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 17 | never-run-line | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: the ownership-free line was not run |
| 18 | never-run-control | sixth | sixth | yes | none | instrument checked against the separable mechanism only, degree read |
| 19 | no-transplant-outside | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 20 | F-channel-removal | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: the channel removal did not collapse own-directed answers below the gate bar |
| 21 | T-fails-gate | R3 | R3 | yes | none | substrate not a testbed: arm T failed its gate on learning (own-directed condition, on seeds 0 and 1) |
| 22 | F-fails-5a | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning at step 5a (named-other condition, on seed 1), after its re-run; nothing else launches (stop S4) |
| 23 | C-fresh-floor | sixth | sixth | yes | none | instrument checked against the separable mechanism only, degree read |
| 24 | T-dev-floor | eighth | eighth | yes | none | instrument returned no reading on the separable mechanism: floor on development episodes failed |
| 25 | F-fresh-floor | fifth | fifth | yes | none | instrument discriminates specified constructed mechanisms, degree not read: floor on fresh episodes failed |
| 26 | inuse-C-flat | sixth | sixth | yes | none | instrument checked against the separable mechanism only, degree read |
| 27 | inuse-T-flat | eighth | eighth | yes | none | instrument returned no reading on the separable mechanism: the built ownership route has gone flat (construction did not hold): the stirred-in route is not in use: route use 0.005, bar 0.5 |
| 28 | inuse-M-flat | R1 | R1 | yes | none | instrument discriminates specified constructed mechanisms, degree read |
| 29 | one-seed-each | none (not decidable) | none | yes | none | no term; reason "arm T: gate not decidable on one seed; arm C: gate not decidable on one seed; arm F: gate not decidable on one seed" |
| 30 | two-seeds-T-split | none (not decidable) | none | yes | none | no term; reason "arm T: gate not decidable on two seeds" |
| 31 | two-seeds-T-both-fail | R3 | R3 | yes | none | substrate not a testbed: arm T failed its gate on learning (own-directed condition, on seeds 0 and 1) |

Every term the code can give is reached: R1, R2, R3, the fifth to eighth, and
"no term" for an undecidable gate.

**Against the run of 2026-10-08** (`out-ruled-code-changes/a2-cases/`, the
code before pull request 153's fix): `results.md` and `results.json` are
identical, and in all 31 case folders `summary.json` and `steps.json` are
identical. The tables differ in 63 lines, each a withheld seed's row losing
exactly one "withheld" cell, and every row of every new table has as many
cells as its header (`tests/e2e_compare_tables.py`, output in
`out-e2e-final-code/tests/a2-cases-compare-to-2026-10-08-run.txt`).

## 2. The in-use cases

`tests/inuse_cases.py`: "14 checks; differ from expectation: []", on the
committed toy models (checked against their checksums) with named weights
changed, and the four 10-million development checkpoints.
`out-e2e-final-code/tests/inuse_cases.json` is identical to the last run's.

## 3. The toy summary at the registered limit

The twelve stored rows of the page 4 re-run at the iteration limit of 10,000
(`out-ruled-code-changes/passB-limit10000/`), copied unchanged into
`out-e2e-final-code/toy-summary-limit10000/` and re-summarised there.

    outcome: substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2)

As recorded in `docs/2026-10-09-ruled-code-changes-and-page4-rerun-findings.md`,
section 2d: arm T reads 0.0000 on all three seeds; arms C and M no verdict on
every seed by the in-use check ("construction did not hold"; arm C route use
0.269 on seed 0 and the built answer flat on seeds 1 and 2, arm M route use
0.071, 0.090, 0.109); arm F no verdict (the read's floor on seed 0, the
named-other gate and the floor on seeds 1 and 2). No separation is computed in
the summary. `summary.json` is byte-for-byte the committed one; the table is
identical to the one the layout fix rebuilt
(`out-ruled-code-changes/table-layout-fix/table-passB-rebuilt.md`), and
differs from the committed pass B table only in its nine withheld rows, one
cell shorter each.

## 4. The whole-pipeline test, both sizes

`tests/pipeline.sh out-e2e-final-code/t6-pipeline`, 19:24 to 21:56, exit 0,
"T6 ran to the end at: 10M 30M" (`t6-stdout.txt`). Each arm trained 30 steps
and was measured at a quarter of the episode counts with three shuffles.
Measuring took 4 to 7 minutes per 10-million model and 18 to 38 minutes per
30-million model (other work shared the laptop; load about 5 to 6).

At both sizes the summary says:

    outcome: not computed: arm T: gate not decidable on one seed; arm C: gate not decidable on one seed; arm F: gate not decidable on one seed

as the 2026-10-08 run did. Every row in both tables has as many cells as its
header (the withheld rows now 11 "withheld" cells).

**Against the 2026-10-08 run** (`tests/e2e_compare_rows.py`, outputs
`out-e2e-final-code/tests/t6-10M-compare-to-2026-10-08-run.txt` and
`t6-30M-...`): I expected the figures might not repeat exactly; they did.
On all eight models every value in the row is the same except three: the
measuring time, the checkpoint's path and the checkpoint's SHA-256. The read
arrays and `summary.json` are identical, and so are the training records. The
checkpoint digests differ only because each checkpoint stores its training
log, which includes seconds per step: loaded side by side with the earlier
run's checkpoints (still on this laptop in the 2026-10-08 session's worktree),
every weight tensor is identical on all eight models. Training on the
processor repeats bit for bit.

## 5. The code that ran

Recorded at the start (19:23) and again at the end (21:56), identical both
times (`out-e2e-final-code/code-identity.txt`):

    git rev-parse HEAD: d4fd02658426987d256c595d09197e82fa14e5ec
    git status of src/: no change

    466ccca1fa6353843a85fa979a2dd228740e414004f09f5ed9c4b9239727c1cc  grammar.py
    9c60cb41d4a5425752ac5bee1ee0088b604d17b746bab1588e275e5c42eb11e4  launch_successor.sh
    4ed6beee1085dd6beb221832b925d01933b40153f3871095d3768c40001fad37  measure.py
    6a62c0e4f9706034e133dc3ed026cc46ea452f1a9544b90996b3540d93b42eed  models.py
    4cc908909f782f4e1e1803efbfbdc5f3d343f779ae81417fdf0a781bc6741ecc  procedure.py
    d7b31ba38a79778199eb4ed38e98b0003e2f8c6c99249caed401db38fc51c9e2  run_self_tests.sh
    9fe876e43533b39dee05e9620a5789a4e6a715e2c49d6ffa3a3b2b7d9a3002c1  train_successor.py
    6cf6abd11c8b5cedf87c295517d1278d45db76dc79cb9f2ce1ca4129c5faad1f  transplant.py
    e300bb34b484c0a56cd1d9f9ea9ae2357d21e245e80c62d692b9c1611698f51d  tripwire.py

These are the files of `experiments/08-successor-degree/src/`. The commit
`d4fd026` adds only the method note to `6c47c56`; `git diff 6c47c56 d4fd026 --
experiments/08-successor-degree/src/` is empty. When pull request 153 merges,
the registration should name the main-line commit it produces and can check
these nine checksums against it.

## 6. Against the method's list of what would count against it

- A case on another term, or a missing text piece: none.
- A withheld figure, or the field `arithmetic_withheld`, in any output: none.
- An in-use check off its expectation: none.
- The toy summary not R3 with that reason, or its `summary.json` differing: no.
- The whole-pipeline test failing at either size, giving a term, or a table
  row with the wrong cell count: no.
- The checksums changing, or a change to `src/`: no.

## Added for this run

Two comparison scripts, written after the method and before their output was
read: `tests/e2e_compare_tables.py` (summaries byte for byte; tables line for
line, allowing only the one-cell change; cell counts against the header) and
`tests/e2e_compare_rows.py` (row fields and training records between two
whole-pipeline runs). The trained checkpoints are not committed (the repo
ignores `.pt` files).

## What this does not do

It edits no code, no version 5 text and no ruling; merges nothing; names no
registered commit; issues no go. The check ruling 3 asks for is owed, by a
session that did not do this run.
