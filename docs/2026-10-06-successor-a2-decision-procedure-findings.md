# Findings: the successor's decision code under the 2026-10-06 rulings, run end to end on the toy and 22 made-up failure cases (outside finding A2)

*Written 2026-10-06 (Pacific) by the Claude Code session that wrote the method
(`docs/2026-10-06-successor-a2-decision-procedure-method.md`, committed first
at `590a630`, before any changed code ran) and the code. Branch
`a2-decision-procedure`. Laptop, no model trained or loaded: $0. **Not
checked.** The independent check listed under A2 is owed (end of this file).*

## What was run

- `experiments/08-successor-degree/tests/a2_run_cases.py`, which confirms the
  toy's committed rows by SHA-256, builds the 22 cases of
  `tests/a2_cases.py` (committed with the method), runs
  `procedure.summarise` on each, and compares. Output:
  `experiments/08-successor-degree/out-a2-cases/results.md` and
  `results.json`, and each case's `summary.json`, `table.md` and
  `steps.json`. The copied row files are not committed (18 MB, rebuilt by the
  runner from the SHA-checked toy rows).
- `src/run_self_tests.sh`: every self-test of the successor code, including
  the new outcome, seed-rule and withholding tests in `measure.py`, the
  ownership-free field tests in `procedure.py`, and the control 5 check in
  `grammar.py`. **All pass** (`out-a2-cases/self-tests.txt`).

## Results

**Every case landed on the outcome written for it in advance (22 of 22), on
the second run.** On the first run, also 22 of 22 outcome codes matched, but
two cases failed a text expectation: the R3 reason read "arm(s) F failed the
gate on learning" and "arm(s) T ...", which does not contain the expected
"arm F" / "arm T". **That is a finding, kept as such:** the code's wording
was changed to "arm F failed its gate on learning"; the expectations were not
touched. The first run's output is kept unchanged in
`experiments/08-successor-degree/out-a2-cases-first-run/`.

| # | Case | Expected | Got |
|---|---|---|---|
| 1 | The toy as it actually is (no step record, no ownership-free field) | R3 | R3: "substrate not a testbed: arm F failed its gate on learning" |
| 2 | Toy, seed 0 taken as arm F's step 5a run | fifth term | "metric validated, degree not read: failed its gate on learning" |
| 3 | Toy, seed 1 taken as step 5a | R3 | R3, arm F at step 5a, nothing else launches |
| 4 | Every arm reads | R1 | R1, with both scope phrases in the sentence |
| 5 | Anchors do not separate | R2 | R2 |
| 6 | Arm C no verdict, arm F reads | fallback, degree read | same |
| 7 | Arm C no verdict, arm F not read | fallback, degree not read | same, reason: the piece floor |
| 8 | Arm T no verdict | metric not validated | same, reason: control 1 |
| 9 | Arms T and C both no verdict | metric not validated | same |
| 10 | Split seeds, the review's A10 table | fifth term (failed its gate on learning) | same |
| 11 | Split seeds, learning passes, each seed fails a different later check | fifth term | same; the frozen code would have given R1 |
| 12 | Split seeds, exactly one seed passes everything | fifth term | same; the frozen code would have given R1 |
| 13 | Four failures on one arm T seed | R1, all four reasons listed | same |
| 14 | Arm M reads 0.80 to 0.90 | R1, sentence says arm M missed its band | same |
| 15 | Arm M fails its gate | R1, arm M dropped | same |
| 16 | Arm F seed 2 computes 0.123456 but fails control 4 | R1, figure nowhere | same |
| 17 | Ownership-free line never ran on arm F | fifth term, "not run" | same |
| 18 | Control 4 never ran on two arm C seeds | fallback, degree read | same; listed as "not run" |
| 19 | Arm T's no-transplant rate 0.05 off | R1 (reported, not a veto) | same |
| 20 | Arm F's channel removal does not collapse | fifth term | same |
| 21 | Arm T fails its gate, arm C no verdict too | R3 naming arm T | same |
| 22 | Arm F fails at step 5a, only arm F's records exist | R3 | same |

Every term the records can reach is reached: R1, R2, R3, the fifth term, both
fallback terms and "metric not validated". No output carries an unregistered
term. R4 is a schedule outcome and is not reachable from records.

**Withheld readings.** No withheld seed's figure appears in its own table row
or in `summary.json`'s readings, and the field `arithmetic_withheld` appears
in no output. A plain text search does find the same *numbers* elsewhere in
some cases, and these are coincidences the checker should know about: the
toy's withheld arm F figures are exactly 1.0, and "1.0000" is also arm T's
printed whole and ownership-only accuracies; in case 13 the withheld arm T
figure is 0.0, which is also arm T's across-seed spread. A search by number
alone cannot tell these apart; `results.json` lists every such hit with its
surroundings (`same_number_elsewhere`). The first run's search also used
too-short strings ("1.", "0.62") and flagged false hits; it was replaced by a
whole-number search.

**Control 5 (RT-255).** The default training stream excludes all 1,600 fresh
and relaxed contents, and in 200 sampled steps (9,600 training contents) none
appeared. The exclusion never had to skip one in that sample, so the sample
shows the contents are rare; the guarantee is the exclusion list, which the
check also asserts.

## What the toy's records lack

The toy's records were written before the ownership-free line existed, so on
the toy that check is listed as "not run" on every arm F seed (case 1). It
does not change the toy's outcome, which turns on arm F's learning gate. The
committed rehearsal check's counts (2,100, 2,238 and 2,324 of 3,000) were
used where a case needed arm F to pass; they were taken on the same 3,000
gate episodes (their lesioned own-correct counts equal the toy rows').

## Owed: the independent check (outside dispositions, A2, lines 303 to 323)

By a session that wrote neither this code nor this run: (1) recompute every
outcome from the ruling text with independent code, not importing
`measure.py` or `procedure.py`; (2) show no withheld reading appears in
either output; (3) turn off each veto in turn (control 7, control 1 on arm T,
control 4, the fresh floor, the piece floor, the gate, the seed rule) and see
at least one case's outcome change; (4) every registered term reached and no
unregistered one; (5) inputs confirmed by SHA-256 (listed in `results.md`);
(6) file it.

---

## Addendum, 2026-10-06: after the independent check (pull request 107) and John's follow-ups

The method addendum and the three new cases were committed first (`400c265`). Then the code changed:
- R3 now names the gate condition that failed and the seeds it failed on.
- R2's sentence now carries the scope phrase.
- Control 5 now also checks each fresh and relaxed episode's assignment table, meaning which marker holds which value on which item.

**All 25 cases match their expectations on the first run**, including the
addendum's expectations on cases 1, 3, 5, 21 and 22:
- **Case 23, arm C misses the fresh-episode floor:** "metric checked against the separable model only, degree read".
- **Case 24, arm T misses the development-episode floor:** "metric not validated: floor on development episodes failed".
- **Case 25, arm F misses the fresh-episode floor:** "metric validated, degree not read: floor on fresh episodes failed".

The fresh and development floors are each now exercised by a case. The
stricter control 5 check found 1,600 fresh and relaxed tables, and none of
them among 9,600 sampled training tables. It is a sampled check, because the
stream's exclusion is still by whole content. All self-tests pass
(`experiments/08-successor-degree/out-a2-cases/self-tests.txt`). Still
unchecked: the checker's point 3 needs rerunning with the new cases.
