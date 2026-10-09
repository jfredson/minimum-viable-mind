# Check of pull request 157: the end-to-end test of the decision code, re-run on the final code

*Written 2026-10-08 (Thursday night, Pacific) by a Claude Code session that
did none of the run it checks, on branch `check-e2e-final-code`, cut from
`origin/main` at `93f4e90` (the merge of pull request 156, the check of the
differently coded decoy test). Asked for by ruling 3 of
`docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`. Laptop
processor only, nothing rented, no paid service called: $0.*

*Pull request 157 is branch `e2e-final-code`, base main. It holds the method
(`docs/2026-10-08-end-to-end-final-code-method.md`), the findings
(`docs/2026-10-08-end-to-end-final-code-findings.md`), the outputs
(`experiments/08-successor-degree/out-e2e-final-code/`) and two comparison
scripts (`tests/e2e_compare_tables.py`, `tests/e2e_compare_rows.py`).*

## Verdict

**Ready to merge.** Nothing must be fixed. The code that ran is the code on
main now, byte for byte. The method was pushed before anything ran and has not
been edited since. My own re-runs on main give the same outputs as the
committed ones: all 31 made-up decision cases, the 14 in-use cases, and the toy
summary at the registered limit. I also re-ran the whole-pipeline test at 10
million parameters, and it gives the same reads, the same summary and the
same table, with weights identical bit for bit. Every claim in the findings
that I could test holds. Three wording points are worth fixing, but none of
them changes a result.

## Must fix

None.

## Should fix (wording; no result changes)

1. **The findings still describe pull request 153 (the last batch before the
   registration) as not yet merged.** Section 5 says "When pull request 153
   merges, the registration should name the main-line commit it produces".
   It merged at 21:58 Pacific, one minute before the findings commit. Main is
   now `93f4e90`, and its code folder is identical to the one that ran (check
   1 below). A line saying so would let the registration name main's commit
   directly.
2. **"And so are the training records" (section 4) is slightly too strong.**
   The training records (`ckpt_*.jsonl`) differ between the two runs in their
   timing fields (`sec`, `sec_per_step`) and in nothing else. The run's own
   compare output says this correctly ("non-timing values differing: 0"). The
   sentence should say the same: identical apart from timing.
3. **The in-use output folder differs from the method's, and nothing says
   so.** The method names `--out out-e2e-final-code/inuse`. The output sits in
   `out-e2e-final-code/tests/inuse_cases.json`, with its printout in
   `tests/inuse-cases-stdout.txt`. The content is right (check 3b). One line
   in the findings would close the gap.

## Notes (no change needed)

- In the findings' table, rows 29 and 30 (the short seed counts) show
  "none" and the reason in the term column. The runner's `results.md` prints
  `None` there. The reason given in the findings is the one in each case's
  `summary.json`, word for word, so it is a fair paraphrase and not a
  misquote.
- Section 3 describes arm C as "route use 0.269 on seed 0 and the built answer
  flat on seeds 1 and 2". On seeds 1 and 2 the table also shows route use
  below the bar (0.233 and 0.221). This is incomplete, but nothing in it is
  wrong.
- The findings say the two comparison scripts were "written after the method
  and before their output was read". Git cannot show this either way, because
  they were committed together with their outputs. They compare and do not
  decide anything, and my own independent comparisons agree with them.

## 1. The code

```
$ git rev-parse HEAD origin/main
93f4e90a0949b1be484e22ed6bee3700b6d41231
93f4e90a0949b1be484e22ed6bee3700b6d41231
$ git diff d4fd026 origin/main -- experiments/08-successor-degree/src | wc -c
       0
$ git diff 6c47c56 origin/main --stat -- experiments/08-successor-degree/src
(empty)
$ git ls-files experiments/08-successor-degree/src | wc -l
       9
$ (cd experiments/08-successor-degree/src && shasum -a 256 *) > main.sha
$ grep -E '^[0-9a-f]{64}  ' out-e2e-final-code/code-identity.txt > rec.sha   # from the PR
$ diff rec.sha main.sha && echo CHECKSUMS MATCH
CHECKSUMS MATCH
```

The code folder at `d4fd026` (the method note, the commit the run used) is
identical to main's. All nine recorded checksums match `shasum -a 256` of
main's files. `code-identity.txt` records the same readings at the start
(19:23:45) and the end (21:56:49), with no uncommitted change to `src/`.

## 2. The method came first

```
$ git log --format='%h %p %ad %s' --date=iso -1 d4fd026
d4fd026 6c47c56 2026-10-08 19:23:30 -0700 Method, written before running: ...
$ git show --stat d4fd026      # one file: docs/2026-10-08-end-to-end-final-code-method.md
$ gh api 'repos/jfredson/minimum-viable-mind/activity?ref=refs/heads/e2e-final-code' \
    --jq '.[]|[.timestamp,.activity_type,.before[0:7],.after[0:7]]|@tsv'
2026-10-09T04:59:13Z  push             d4fd026  21bb44e
2026-10-09T02:23:31Z  branch_creation  0000000  d4fd026
$ git diff d4fd026 origin/e2e-final-code -- docs/2026-10-08-end-to-end-final-code-method.md | wc -c
       0
```

GitHub received the method at 19:23:31 Pacific, 14 seconds before the run's
first code reading (19:23:45) and before the whole-pipeline test started
(19:24). The method commit holds only the method. Every output came in the
later commit `21bb44e`. The method has not changed since. Its expectations are
fixed in it: a term for each of the 31 cases, the toy summary's R3 sentence
and byte-identical `summary.json`, 14 in-use checks, and "not computed" with
11 withheld cells per row for the whole-pipeline test.

The expected term for each case comes from the case definitions, not from
the output. `tests/a2_cases.py` was last changed in `70a6fb0` (2026-10-08
15:06, the frozen code changes), hours before this run, and not on this
branch. Read through its own renaming map (`CODE_RENAMED`), it gives exactly
the method's list:

```
$ python -c "import a2_cases as a; [print(i, c['name'], a.CODE_RENAMED.get(c['expect'], c['expect'])) for i, c in enumerate(a.CASES, 1)]"
1 toy R3 | 2 toy-step5a-seed0 fifth | 3 toy-step5a-seed1 R3 | 4 r1 R1 | 5 r2 R2
6 fallback-read sixth | 7 fallback-not-read seventh | 8 T-no-verdict eighth
9 T-and-C-no-verdict eighth | 10-12 fifth | 13-16 R1 | 17 fifth | 18 sixth | 19 R1
20 fifth | 21 R3 | 22 R3 | 23 sixth | 24 eighth | 25 fifth | 26 sixth | 27 eighth
28 R1 | 29 None | 30 None | 31 R3
```

(output condensed onto fewer lines here; every case matches the method's list)

The in-use cases' expectations are written in `tests/inuse_cases.py`, last
changed `ffcaa51` (2026-10-06).

## 3. My re-runs on main

All from `experiments/08-successor-degree/` on main `93f4e90`, with
`~/Code/minimum-viable-mind/.venv/bin/python`, outputs to my scratch folder.
The scripts I wrote for the comparisons are in
`docs/reviews/2026-10-08-end-to-end-final-code-check-scripts/`.

**3a. The 31 made-up decision cases.**

```
$ python tests/a2_run_cases.py <scratch>/a2
...
31 cases; 0 differ from expectation or leak: []
$ diff -r <scratch>/a2 <PR>/out-e2e-final-code/a2-cases && echo "A2 OUTPUTS IDENTICAL (all files)"
A2 OUTPUTS IDENTICAL (all files)
$ python a2cmp.py <scratch>/a2 out-ruled-code-changes/a2-cases
results.md identical: True
results.json identical: True
case folders: 31 old: 31
summary/steps differing: []
row files differing: []
table lines changed: 63 each exactly one withheld cell dropped: True rows whose cell count differs from header: 0
```

Every file of my run is byte-identical to the PR's. Against the earlier run
(`out-ruled-code-changes/a2-cases/`, the code before pull request 153's table
fix), the only change is 63 table lines that each lose exactly one "withheld"
cell. Every row now has as many cells as its header.

**3b. The 14 in-use cases.**

```
$ python tests/inuse_cases.py --out <scratch>/inuse
...
14 checks; differ from expectation: []
$ cmp <scratch>/inuse/inuse_cases.json <PR>/out-e2e-final-code/tests/inuse_cases.json && echo SAME-AS-PR
SAME-AS-PR
same: ./out-sharpness-fix/inuse-cases/inuse_cases.json
same: ./out-ruled-code-changes/tests/inuse_cases.json
```

All 14 checks (13 numbered, number 8 covering two seeds) match the
expectations written in the script, and the output is identical to the PR's
and to the last two committed runs.

**3c. The toy summary at the registered limit**, on a scratch copy of
`out-ruled-code-changes/passB-limit10000/`:

```
$ cp -R out-ruled-code-changes/passB-limit10000 <scratch>/toy
$ python src/procedure.py summarise --dir <scratch>/toy      # exit 0
outcome: substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2)
$ cmp <scratch>/toy/summary.json out-ruled-code-changes/passB-limit10000/summary.json   # same
$ cmp <scratch>/toy/summary.json <PR>/.../toy-summary-limit10000/summary.json            # same
$ cmp <scratch>/toy/table.md <PR>/.../toy-summary-limit10000/table.md                    # same
$ cmp <scratch>/toy/table.md out-ruled-code-changes/table-layout-fix/table-passB-rebuilt.md  # same
$ python cells.py <scratch>/toy/table.md:out-ruled-code-changes/passB-limit10000/table.md
header 16 cells, 14 rows, mismatched 0; vs old: 9 lines differ, all exactly one withheld cell dropped: True; old header 16, old withheld row cells [17]
```

The result is R3 with the expected reason, and `summary.json` is
byte-identical to the committed one. The table matches the layout fix's
rebuilt table and differs from the committed pass B table only in the nine
withheld rows (17 cells before, 16 now). The PR's twelve row files are the
committed pass B rows, unchanged. The table shows what the findings say: arm T
reads 0.0000 on all three seeds; arms C and M give no verdict, because the
in-use check found the construction did not hold (arm M route use 0.071,
0.090, 0.109); arm F gives no verdict, on its floor for seed 0 and on the
named-other gate plus the floor for seeds 1 and 2.

**3d. The self-tests** (cheap, so I ran them too): `sh src/run_self_tests.sh`
gives exit 0, 265 `[PASS]` lines and "ALL SELF-TESTS PASS". The output is
identical to the PR's `tests/t1-self-tests.txt`.

**3e. The whole-pipeline test at 10 million parameters** (time allowed; I did
not re-run 30 million):

```
$ sh tests/pipeline.sh <scratch>/t6 10M
  [10M T measure] [T/0] done in 174s ...   (C 183s, M 210s, F 211s)
  [10M summary] outcome: not computed: arm T: gate not decidable on one seed; arm C: gate not decidable on one seed; arm F: gate not decidable on one seed
T6 ran to the end at: 10M
exit 0
$ python t6cmp.py <scratch>/t6 <PR>/out-e2e-final-code/t6-pipeline
  measure/reads_{T,C,M,F}_seed0.npz: identical   measure/summary.json: identical
  measure/table.md: identical   ckpt_*.DONE: identical
  ckpt_*.jsonl, row_*.json: differ
$ python jdiff.py <scratch>/t6 <PR>/out-e2e-final-code/t6-pipeline 10M
10M T row keys differing: ['.checkpoint', '.checkpoint_sha256', '.seconds'] | training-record keys differing: ['.sec_per_step']
10M C/M/F: the same three row keys | training-record keys differing: ['.sec', '.sec_per_step']
$ python wcmp.py <scratch>/t6/10M <the PR session's worktree>/out-e2e-final-code/t6-pipeline/10M
T 114 / C 140 / M 150 / F 106 tensors; identical across 2 runs: True
```

My run, the PR's run and the 2026-10-08 run agree. The reads, the summary and
the table are identical. Rows differ only in the measuring time, the
checkpoint's path and its digest. Training records differ only in timing
fields. Every weight tensor is identical.

## 4. Every claim in the findings against the outputs

| Claim | Checked by | Holds |
|---|---|---|
| 31 cases on their terms, every expected text piece found, no withheld figure leaks | 3a (my re-run; runner reports 0 differ or leak) | yes |
| Findings table, cases 1 to 28 and 31 | `diff` of its rows against my `results.md` rows: identical | yes |
| Cases 29 and 30: no term, with the stated reasons | each case's `summary.json` (`term: None`, reason word for word) | yes (see Notes) |
| Same as the 2026-10-08 run: results, summaries and steps identical; 63 table lines one cell shorter | 3a, `a2cmp.py` | yes |
| In-use: 14 checks, none off; same file as the last run | 3b | yes |
| Toy summary: R3 with the stated reason; `summary.json` byte-for-byte; table equal to the layout fix's; nine rows one cell shorter | 3c | yes |
| Per-arm description of the toy summary | the table in 3c | yes (arm C incomplete, see Notes) |
| Self-tests: 265 pass | 3d | yes |
| Whole-pipeline test: exit 0 at both sizes, "not computed" with the stated reason | PR's `t6-stdout.txt`; my 10-million re-run | yes |
| Measuring times: 4 to 7 minutes (10 million), 18 to 38 minutes (30 million) | `t6-stdout.txt`: 253 to 400 s; 1,104 to 2,275 s | yes |
| Every pipeline table row has as many cells as its header; withheld rows have 11 withheld cells | `cells.py` on both sizes: header 16, no mismatch; vs 2026-10-08, 2 and 3 lines each one cell shorter | yes |
| Against the 2026-10-08 run, only measuring time, checkpoint path and digest differ in rows; reads and summary identical | `t6cmp.py`, `jdiff.py` on the PR's outputs against `out-ruled-code-changes/t6-pipeline/`, both sizes | yes |
| "So are the training records" | `jdiff.py`: only `sec` and `sec_per_step` differ | identical apart from timing (should-fix 2) |
| Every weight tensor identical on all eight models | `wcmp.py` on the PR session's checkpoints against the 2026-10-08 session's, both sizes, all True; `shack.py`: those checkpoints' digests match the ones recorded in each run's rows | yes |
| Code that ran: `d4fd026`, code folder as at `6c47c56`, checksums the same at start and end | check 1 | yes, and identical to main now |

## What this does not do

It edits nothing in pull request 157 and fixes nothing. It merges nothing,
names no registered commit and issues no go.
