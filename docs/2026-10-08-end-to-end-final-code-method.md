# Method: the end-to-end test of the decision code, re-run on the final code

*Written 2026-10-08 (Thursday, Pacific) by a Claude Code session in its own
worktree, on branch `e2e-final-code`, cut from
`origin/final-batch-before-registration` (pull request 153, the last batch
before the registration, not yet merged) at commit `6c47c56`. **Committed
before anything below has run.** Laptop processor only, nothing rented, no
paid service called: $0.*

*Plain language. "Arm" is one of the four model designs (T: the separable
model built to be easy to read; C: the entangled model, the high anchor; M:
the middle model; F: the free model whose degree the experiment exists to
read). A "seed" is one of an arm's three training runs. "Withheld" means a
reading is replaced by "no verdict" with its reasons, and the figure itself is
written nowhere. "The term" is one of version 5's eight registered outcome
words.*

## Why this is run

Ruling 3 of John's rulings of 2026-10-08
(`docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`): the
end-to-end test of the decision code, which closed the decision-procedure
finding (ledger row RT-256, the outside finding A2), ran on the code of
2026-10-06, and the code changes ruled on 2026-10-08 altered that code again.
It is to be re-run on the final registered code, checked, and named in the
registration. That test is the made-up decision cases and the toy run
(`docs/2026-10-06-successor-a2-decision-procedure-method.md` and its findings,
outputs in `experiments/08-successor-degree/out-a2-cases/`).

The final code is main (after pull request 152, the check of the ruled code
changes) plus one change on pull request 153: the reporting table printed 12
"withheld" cells on a withheld seed where the header has 11; now 11
(`experiments/08-successor-degree/src/procedure.py`, one number). No figure is
computed differently.

## What runs, in this order

All from `experiments/08-successor-degree/`, with the project's Python
(`~/Code/minimum-viable-mind/.venv/bin/python`), all outputs in
`out-e2e-final-code/`. Nothing in `src/` is edited or patched at run time.

1. **The exact code.** `git rev-parse HEAD` and
   `shasum -a 256 src/*`, written to `out-e2e-final-code/code-identity.txt`
   before the first test and again after the last, with `git status` showing
   no change to `src/`.
2. **The self-tests** (`src/run_self_tests.sh`, test T1 of the code freeze).
   Not named in the ruling; run because it is cheap and covers the table
   writer the fix touched.
3. **Every made-up decision case**: `tests/a2_run_cases.py
   out-e2e-final-code/a2-cases`. The 31 cases (the 22 of the method, the three
   of its addendum, three for the in-use check, three for short seed counts)
   built from the committed toy rows (`out-freeze-tests/t3a-committed-reads/`,
   checked by SHA-256), each summarised by `procedure.summarise`, each output
   searched for every withheld seed's figure.
4. **The in-use cases**: `tests/inuse_cases.py --out out-e2e-final-code/inuse`
   (14 checks on the committed toy models and the four 10-million development
   checkpoints).
5. **The toy summary at the registered limit**: the stored rows of the page 4
   re-run at the iteration limit of 10,000
   (`out-ruled-code-changes/passB-limit10000/`, twelve toy models) copied into
   `out-e2e-final-code/toy-summary-limit10000/` and re-summarised there with
   `procedure.py summarise --dir`. The committed folder is not touched.
6. **The whole-pipeline test** (`tests/pipeline.sh`, test T6 of
   `docs/2026-10-04-successor-code-freeze.md`) at 10 million and 30 million
   parameters: each arm trained 30 steps by the trainer the rented machine
   runs, measured at a quarter of the episode counts with three shuffles, and
   summarised. The trained checkpoints are not committed. This takes about an
   hour and a half.

## What I expect, written before running

- **Self-tests:** all pass (265 checks at the last run).
- **Made-up cases: all 31 land on the term written for each in advance, and
  no withheld figure appears in any output.** The expected codes, from
  `tests/a2_cases.py` (original 22 plus addendum and later cases, with the
  2026-10-08 mapping of old codes to version 5's words):
  R3 on cases 1 (the toy), 3, 21, 22 and 31; R1 on 4, 13, 14, 15, 16, 19 and
  28; R2 on 5; the fifth term on 2, 10, 11, 12, 17, 20 and 25; the sixth on 6,
  18, 23 and 26; the seventh on 7; the eighth on 8, 9, 24 and 27; and no term
  ("gate not decidable") on 29 and 30. The table fix touches only the
  printed table, never a term, so the run should match the previous run
  (`out-ruled-code-changes/a2-cases/results.md`) term for term and sentence
  for sentence.
- **The toy case (case 1)** reads, as before: "substrate not a testbed: arm F
  failed its gate on learning (named-other condition, on seeds 1 and 2)".
- **In-use cases:** 14 checks, none different from expectation.
- **The toy summary at the registered limit** is the one recorded in
  `docs/2026-10-09-ruled-code-changes-and-page4-rerun-findings.md`
  (section 2d): **R3, "substrate not a testbed: arm F failed its gate on
  learning (named-other condition, on seeds 1 and 2)"**; arm T reads 0.0000
  on all three seeds; arms C and M no verdict on every seed by the in-use
  check ("construction did not hold"); arm F no verdict (the read's floor on
  seed 0, the named-other gate on seeds 1 and 2); so no separation is
  computed in the summary. Its `summary.json` should be byte-for-byte the
  committed one, and its table should differ from the committed table only in
  the nine withheld rows, now 16 cells each where they had 17 (as
  `out-ruled-code-changes/table-layout-fix/` already showed).
- **Whole-pipeline test:** runs to the end at both sizes, exit 0; every arm
  trains and is measured; the summary at each size says "not computed: arm T:
  gate not decidable on one seed; arm C: gate not decidable on one seed; arm
  F: gate not decidable on one seed", as in the 2026-10-08 run; the withheld
  rows of its table now have 11 "withheld" cells, not 12. The models are
  barely trained, so no reading is a registered figure, and I do not expect
  the per-row figures to match the earlier run exactly (training on the
  processor may not repeat bit for bit); I will compare them and say.

## What would count against it

- Any made-up case landing on a term other than the one written for it, or
  any expected text piece missing from its sentence.
- Any withheld seed's figure, or the field `arithmetic_withheld`, found in a
  case's output.
- Any in-use check different from its expectation.
- The toy summary giving anything other than R3 with that reason, or its
  `summary.json` differing from the committed one in any byte.
- The whole-pipeline test failing to finish at either size, giving a term
  where it should give "not computed", or printing a table row whose cell
  count does not match its header.
- The code's checksums changing between the start and the end of the run, or
  any uncommitted change to `src/` at either point.

Any of these is reported as found; no expectation here is edited afterwards.

## What this does not do

It does not edit version 5, any ruling or the code, merges nothing and issues
no go. The check the ruling asks for is by a session that did not do this run.
