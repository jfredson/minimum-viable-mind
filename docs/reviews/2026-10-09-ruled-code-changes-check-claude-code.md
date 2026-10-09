# Check of pull request 151 (the ruled code changes and the page 4 re-run) and of the free model's gate closure condition

*2026-10-09 (run the evening of 2026-10-08, Pacific). Claude Code, as the
checker, on branch `check-ruled-code-changes`, cut from the main line at
`5f698ab`. I wrote none of what I check: not the code changes, the method
note, the findings or the outputs of pull request 151 (branch
`ruled-code-changes-2026-10-09`, head `2245973`), and not the closure check of
RT-237, the fatal finding on the free model's gate. Laptop only, processor
only, $0: nothing rented, no paid service called. Scripts and their outputs
are beside this file, in `docs/reviews/2026-10-09-ruled-code-changes-check-scripts/`.
I edited nothing on the pull request's branch, nothing in version 5 and not
the red-team ledger.*

*Where the code ran.* I unpacked the branch's tree (`git archive`) into a
scratch folder and ran everything there. The branch merges into the current
main line with no conflict (`git merge-tree`), and nothing under
`experiments/` changed on the main line since the branch was cut (`760deef`),
so the branch's code is the code as it would merge.

## Verdicts

- **Pull request 151: ready to merge.** No must-fix. The code does what
  John ruled on 2026-10-08 (items 3, 4, 7 and 9 of
  `docs/rulings/2026-10-08-v5-open-items-rulings.md`) and nothing else that
  changes a computed figure or a decision. Every test passes when I run it.
  My own re-run of the twelve toy models reproduces the committed outputs
  exactly (section 5). Three should-fix items, one of which (S1, a
  misprinted table) should land before the registered commit is named
  (open item 10).
- **The free model's gate closure condition: holds.** I ran the three
  scripts of the RT-237 closure check on this branch's code. Two give
  output identical to the committed output; the third differs only by
  added lines for the folders this branch adds, with 740 of 740 clause
  states agreeing and no mismatches. The code's gate row differs from the
  committed record only by the new row-choice field on arm T, which is
  reporting only (part 2). The closure line can go in the ledger once this
  pull request merges. I have not edited the ledger.

## Must-fix

None.

## Should-fix

- **S1. The reporting table puts the lesion counts under the wrong
  headings on every withheld seed.** In `procedure.table`, a withheld seed's
  row prints 12 "withheld" cells where the header leaves room for 11
  (`" withheld |" * 12`). This bug was already on the main line: there the
  header had 15 columns and withheld rows had 16 (`out-a2-cases/toy/table.md`).
  This pull request edits that same line to add its new last column, so the
  error now lands on the new column. In
  `out-ruled-code-changes/passB-limit10000/table.md` the header has 16
  columns, rows T/0 to T/2 have 16, and every other row has 17. On those
  rows the own-directed count with the channel zeroed sits under "lesion
  candidates", and the free model's ownership-free count (2,100, 2,238 and
  2,324, the count RT-237 rests on) sits under "row choice, arm T". A
  Markdown viewer drops the extra cell. No figure and no decision changes,
  since the table only prints. But section 7.4 freezes the reporting
  table's columns, so the registered table would mislabel arm F's gate
  counts. The fix is 11 in place of 12. It should land, in this pull request
  or the next, before the registered commit is named.
- **S2. Version 5 changes the session missed** (findings, section 3, lists
  seven). Also owed:
  1. Section 7.1, the first bullet on development episodes: "(on the toy,
     the last 180 of 600)" is now out of date. The held-out 180 are the last
     of 1,980. The same bullet could also say that the 1,980 are now a named
     evaluation set that training refuses.
  2. Section 7.4's frozen list and section 9's row "The numbers of episodes
     at the registered size" give the 1,980, the 1,800 and the 180. Neither
     names the fitter's iteration limit of 10,000. It is a ruled number that
     can move a read, so it belongs on the frozen list beside the episode
     counts.
  3. Section 9's row "Arm M's predicted reading" still quotes the toy at
     0.4886, 0.4860 and 0.5449 "under the registered rules". Those are the
     figures fitted on 420 episodes. Under the registered rules (1,800 of
     1,980, limit 10,000) they are 0.5252, 0.4793 and 0.5208, within 0.0252,
     0.0033 and 0.0288 of the true-slot reading. The session's list of
     citations to update (its item 3) leaves this row out.
- **S3. Two claims in the findings are not backed by a committed output,
  or are timed by a commit they share.**
  1. The row-choice split on the 10-million arm T checkpoint (2,586 of
     3,000 right rows, and so on) has no committed output. The checkpoint
     is not committed either. I re-ran it on the checkpoint on John's laptop
     (`experiments/08-successor-degree/artifacts/succ_t_10m_seed0/succ_t_10m_seed0.pt`).
     The branch's `row_choice` gives 2,586 right rows, 164 of the 414
     wrong-row episodes right anyway (0.396), 2,999 with the row forced, and
     the same six confused pairs of name words, with the same counts as the
     development-runs check's `arm_t_errors_output.txt`. The claim holds. My
     output (`row_choice_10m.out.txt`) is the committed record of it now.
  2. The made-up-case addendum in `tests/a2_cases.py` says it was "written
     before the changed code ran on any case". But the addendum, the code
     and the outputs of every test (T1, the 31 cases, the in-use cases, T2,
     T7) all land in one commit, `70a6fb0`, so git cannot show the order.
     This changes no verdict: the 28 old expectations are untouched (the
     diff to `a2_cases.py` only adds lines), and the three new cases are
     simple. Next time, committing the expectations before their outputs
     would let git show the order.

**Worth noting, not items.** Seed-level reasons still say "failed its gate
on learning" for a seed that failed. That is true of the seed, and the
ruling concerned the arm's summary. `summary.json` still carries
`gate_passes: false` beside the new `gate_status: "gate not decidable on one
seed"`, so a reader of the raw file should read `gate_status`. One design
call is the session's, not ruled: an arm that has failed outright gives R3
even when another arm is undecided. That follows from rule 1 of section 3 (a
failed gate decides by itself), and I agree with it.

## Part 1. Pull request 151, point by point

### 1. Method first, each driver before its outputs: holds

```
$ git log --format='%h %ad %s' --date=iso origin/main..origin/ruled-code-changes-2026-10-09
2245973 2026-10-08 18:19:39 -0700 Findings: ...; the whole-pipeline test
784da42 2026-10-08 16:45:29 -0700 Page 4 pass B under the ruled code (limit 10,000), the solver at 10,000, and the comparison
fc7c253 2026-10-08 15:52:46 -0700 Page 4 pass A, the reproduction check: ...
d4b03b8 2026-10-08 15:09:09 -0700 Comparison, training-stream replay and solver wrapper for the page 4 pass, committed before their outputs exist
70a766c 2026-10-08 15:06:43 -0700 Drivers for the page 4 toy pass under the ruled code, committed before they run
70a6fb0 2026-10-08 15:06:13 -0700 Frozen successor code: the changes John ruled 2026-10-08 (open items 3, 4, 7 and 9)
3d31fd2 2026-10-08 14:55:48 -0700 Method note, before any code change: ...
```

From `git log --name-status` (saved in the scratch folder): the method note
`3d31fd2` adds only the method file. `70a6fb0` changes `src/grammar.py`,
`src/measure.py`, `src/procedure.py`, `README.md`, `tests/a2_cases.py` and
`tests/a2_run_cases.py`, and adds the test outputs (`a2-cases/`, `tests/`;
see S3.2). `70a766c` adds the two drivers (`tests/page4_ruled_model.py`,
`tests/page4_ruled_lanes.sh`). `d4b03b8` adds the comparison, the replay and
the solver wrapper. Pass A's outputs and the replay output arrive in
`fc7c253`, pass B's and the solver's in `784da42`, and the pipeline test's
in `2245973`. Each script arrives before its outputs. The commit title says
items "3, 4, 7 and 9" where the task said 3, 7 and 9. Item 4 is the ruling
that the scope phrases go with the renamed terms, so that is right.

### 2. The code does what was ruled, and nothing else: holds

I read the whole diff of `src/` (`git diff origin/main...origin/ruled-code-changes-2026-10-09 -- experiments/08-successor-degree/src`,
three files, 393 lines).

- **Every fit at 10,000.** Every `LogisticRegression` in the frozen code now
  goes through one function, `procedure._logreg`, with
  `max_iter=MS.FIT_MAX_ITER` (10,000) and `C=1.0`. A search of `src/` finds
  no other call (`grep -rn "LogisticRegression\|max_iter"`). That function
  also counts the fits that stop at the limit, by kind, and only writes the
  count into the row.
- **Reads fitted on the first 1,800 of 1,980.** `grammar.EVAL_SETS` gains
  `dev_reads = (1980, 4242, "dev", False)`: same generator and seed as the
  600, so its first 600 pairs are the 600 (asserted twice: by the grammar
  self-test and by `EvalData` at load time). `fit_count(n) = n*1800//1980`
  gives 1,800 at full size. `_fit`, `correct_count` and the null all fit on
  `h[:fit_count]` and score on the rest. The own read and the named read
  (`fit_reads`), their held-out counts, the null, control 2's counts and the
  counts elsewhere on the site take `data.read_pool`. The nomination's
  transplant grid and control 2's grid stay on the 600 (`data.dev`). This is
  the same split as the checked run-time wrapper of 2026-10-06
  (`experiments/rehearsal-successor-measure/src/page4_models_1800.py`,
  changes 1 to 3). Pass A shows the two give the same figures (point 5).
- **The eight terms and the scope phrases.** `measure.OUTCOME_TERMS` matches
  version 5 section 3's "Registered term" column word for word, all seven
  coded terms, the eighth being "instrument returned no reading on the
  separable mechanism". R4 is not coded, as before. `measure.sentence` puts
  "on these constructed systems, for this intervention procedure" after
  every "instrument discriminates", "instrument checked" and "instrument
  returned no reading" term and after R2, and puts "as a ratio of two
  transplants at the sites this procedure chose" after "degree read" (R1 and
  the sixth term). Section 3's scope rule asks for exactly this. Version 4's
  names are kept in `VERSION_4_NAMES`, which nothing prints. A search of
  `src/` for "validated", "metric" and the old codes finds only that
  history table and the self-test that checks for the old words.
- **"Gate not decidable on one seed".** `arm_outcome` adds
  `gate_decidable = len(learned) >= 2 or len(learned) + missing < 2` (missing
  = 3 minus the seeds in) and a `gate_status`. `summarise` passes a gate it
  cannot decide as `None`. `outcome` then gives no term, with the reason
  "arm X: gate not decidable on N seed(s)", unless another arm has failed
  outright. Arm M with a gate it cannot decide is "not decidable", not
  "dropped". With three seeds in, nothing changes. `seed_gate` and
  `withhold` are untouched.
- **Arm T's row-choice split, reporting only.** `procedure.row_choice` is
  called from `gate` for arm T only and written as `gate["row_choice"]`
  (`reported_only: True`). Nothing in `measure.py` reads it, and in
  `procedure.py` only `table` prints it. It runs under `torch.no_grad` and
  draws no random number. On the 10-million checkpoint it reproduces the
  development-runs check exactly (S3.1).
- **Arm M's per-step copy untouched.** `models.py`, `transplant.py`,
  `train_successor.py` and `tripwire.py` are not in the diff.
- **Nothing else that computes.** The other changes are the outcome codes
  renamed (`fallback_read`, `fallback_not_read` and `not_validated` to
  `sixth`, `seventh` and `eighth`), new row fields (`read_split`,
  `fits_stopped_at_iteration_limit`), the table's new column, new
  self-tests and the re-pinned digest (point 3). In the `held_out` counting,
  `n - int(0.7*n)` becomes `n - fit_count(n)`. At full size that is the
  ruled 180. In a scaled pipeline test it keeps the 1,800-to-1,980
  proportion, a choice the method states.

### 3. The session's own choices: the replay holds; the digest re-pin does not need John's word first

**The replay, re-run with the frozen code itself.** The session's replay
(`tests/replay_stream_dev_reads.py`) writes the stream's draw loop out again
by hand. Mine (`replay_real_stream.py`) calls the frozen code's own
`TrainingStream.pairs_for_step`. It uses the pull request's default exclusion
(all 5,280 evaluation contents, the 1,980 included, and the 1,600 fresh and
relaxed pairings) and switches off only the rendering of episodes into
tokens, which draws no random number. Every one of the 108,919 registered
steps of 48 pairs, on all three seeds:

```
$ python replay_real_stream.py 0   (and 1, 2; run from the branch's root)
seed 0: 5228112 training contents over 108919 steps under the new default exclusion (5280 contents, 1600 pairings); skipped by it: 0; drawn contents among the 1,380: 0
seed 1: 5228112 training contents over 108919 steps under the new default exclusion (5280 contents, 1600 pairings); skipped by it: 0; drawn contents among the 1,380: 0
seed 2: 5228112 training contents over 108919 steps under the new default exclusion (5280 contents, 1600 pairings); skipped by it: 0; drawn contents among the 1,380: 0
```

The new exclusion skips nothing, so every training batch is the same as
under the old exclusion. No draw is one of the 1,380. The session's claim
holds, and holds more strongly than it stated: training never draws any
evaluation content at all, under either list.

**Does re-pinning the digest need John's word?** In my judgement, not before
this merge. But it should be named to him as an agent's call in the packet
for the registered commit (open item 10). My reasons:
- The 1,980 are the ruled development episodes (2026-10-06, page 4, and
  item 7 of 2026-10-08). Version 5 section 7.1 already says development and
  training episodes are disjoint, and the ruled training recipe (item 5)
  excludes "every evaluation set". Making the 1,980 an evaluation set is what
  the text already asks for. It is not a new rule.
- The digest is a fingerprint of the evaluation sets. When a set is added,
  the fingerprint has to change. The digest of the first training batch is
  unchanged (self-test passes), and the replay shows no training step
  changes on any registered seed.
- No other file pins the old digest: a search of `experiments/`, `docs/`,
  `scripts/`, `src/` and `spec/` finds `0cc3dafb` only in the comment beside
  the new pin.
- What it does change is the registered code's fingerprint, which John's
  registration commit will cite. So it belongs in the list of agent's calls
  that the registration names (decided by: agent).

### 4. Tests: all pass when I run them

`rerun_tests.sh` (outputs in `tests-rerun/`), run in the branch's
`experiments/08-successor-degree/`:

- T1, `src/run_self_tests.sh`: **ALL SELF-TESTS PASS**, exit 0, 265 checks
  passed, 0 failed. Apart from timings, the output matches the committed
  `t1-self-tests.txt` line for line.
- The made-up decision cases, `tests/a2_run_cases.py`: **31 cases, 0 differ
  from expectation or leak**, exit 0. Output identical to the committed
  `a2-cases-stdout.txt`.
- The in-use cases, `tests/inuse_cases.py`: **14 checks, none differ**, exit
  0. Output identical to the committed file.
- T2, `tests/load_toy_models.py`: **T2 PASSES**.
- T7, `tests/check_launcher.sh`: "all checks pass. nothing was created and
  nothing was spent."

I did not re-run T6, the whole-pipeline test (about 90 minutes). I read its
committed outputs. Both sizes ran to the end. The summary says "not
computed: arm T: gate not decidable on one seed; arm C: ...; arm F: ...",
which is item 9's change seen on a real pipeline.

### 5. The reproduction claim: holds on my sample, and my full pass B reproduces the committed pass B

I ran `rerun_models.sh` from 18:25 to 19:14. It does two things. All twelve
toy models at the code's own limit of 10,000, calling `procedure.py model`
directly rather than through the session's driver (my pass B). And a sample
for the reproduction check: arm M seed 1 (240 warnings in the old record,
the most of any model) and arm C seed 2 (the one arm C warning), each after
its arm T seed, at the old limit through the driver's `--limit 3000`, the
only way to set it (my pass A). Before loading each model, the driver
checks it against `SHA256SUMS`. `compare_checker.py mine` (output in
`compare_mine.out.txt`) compares every value in both files, apart from run
times and paths, and every read array:

```
my pass A row_M_seed1.json vs checked 1,800 record: 2447 values compared, 0 differ; read arrays differing: none; warnings mine 240 vs 240
my pass A row_C_seed2.json vs checked 1,800 record: 2433 values compared, 0 differ; read arrays differing: none; warnings mine 1 vs 1
my pass A row_T_seed1.json vs checked 1,800 record: 2411 values compared, 0 differ; read arrays differing: none; warnings mine 0 vs 0
my pass A row_T_seed2.json vs checked 1,800 record: 2411 values compared, 0 differ; read arrays differing: none; warnings mine 0 vs 0
(each also 0 differ against the committed pass A)
my pass B, all twelve rows vs committed pass B: 2,358 to 2,564 values each, 0 differ; read arrays differing: none; warnings 0 vs 0
my pass B table.md: identical to the committed passB-limit10000/table.md (same outcome line)
```

The 18 or 19 fields present in only one file are the ones added since the
old record (the in-use check, the ownership-free line, the row-choice
split, the split and the limit counts, and the four no-transplant fields
the findings name). So, on my sample, the ruled code at limit 3,000 gives
the checked record value for value, with the same warnings. My full pass B
equals the committed pass B. I did not re-run the other eight models at
3,000, so the full count of 29,077 values rests on the session's
`reproduction.json`, which my sample agrees with.

### 6. The headline claims: hold

From the committed outputs (`compare_checker.py headline`, output in
`compare_headline.out.txt`), and on my own pass B in point 5:

- **The warning table.** Counting "failed to converge" in the logs: the
  checked 1,800 record has arm T 0, 0, 0; arm C 0, 0, 1; arm M 132, 240, 99
  (471); arm F 2, 11, 10 (23). Pass A has the same on all twelve models.
  Pass B has 0 on all twelve.
- **467 of arm M's 471 were the shuffled-label null.** Pass A's own count
  by kind: arm M null 130, 239 and 98 stops of 1,000 fits each (200 shuffles
  times five states), and the named agent's read 2, 1 and 1 of 5. That makes
  467 plus 4. Arm F: null 2, 10, 10, named read 0, 1, 0. Arm C seed 2: named
  read 1.
- **"The ownership read never stopped at the limit."** In pass A, "the read
  (own)", "held-out counts (own)" and "counts elsewhere on the site" have
  zero stops on every model. In pass B the most iterations any ownership
  read took is 2,960 (arm F seed 2). On the built arms it is at most 80
  (arm C seed 1). The null's largest is 7,385 (arm M seed 0). All match the
  findings.
- **Every toy figure version 5 quotes, the same at 10,000.** I compared 11
  quoted fields per model (status, site set and piece, reading, true-slot
  reading, best piece anywhere, controls 1, 4 and 7, control 2's status and
  its own-directed shift) between the checked 1,800 record and pass B, on
  all twelve models. None differs. Spot checks against the findings'
  table 2c: arm T 0.0000 on all three seeds, state 0 at the action, 8
  directions, piece 180. Arm C seed 0: state 2, 4 directions, 178, 1.0026.
  Arm C seed 2: state 1 from the first own turn, 4 directions, 165, 1.0000.
  Arm M 0.5252, 0.4793, 0.5208, with true-slot readings 0.5000, 0.4760,
  0.4920. Arm F best piece 40, 19, 36. Control 2 on arm F seed 0 "reported",
  own-directed shift 0.0000. All as stated.
- **The solver** (the ordinary competing model, rehearsal code): 2 warnings
  in the 1,800 record's log, 0 in `log_solver_limit10000.txt`. Best pieces
  19, 17 and 20 on the primary reading, no site set clears the floor, no
  reading. I did not re-run the solver.
- **The outcome:** pass B's `table.md` reads "substrate not a testbed: arm F
  failed its gate on learning (named-other condition, on seeds 1 and 2)", as
  claimed.

### 7. The listed version 5 changes: correct, three missed

The seven the findings list (section 3) are each correct. I checked each
cited sentence against version 5: section 7.2 item 1's second caution, W15,
section 11 step 3, section 17 failure 4, the ruled notes of section 21, and
section 7.5 item 15. Section 7.2's caution is wrong in the way the findings
say. Missed: S2's three.

## Part 2. The free model's gate closure condition: holds

The RT-237 closure check (`docs/reviews/2026-10-09-rt237-closure-check-claude-code.md`)
set its condition 2: rerun its three scripts on the merged code if the
branch touches `measure.seed_gate`, `measure.withhold`, `measure.arm_outcome`
or `procedure.gate`. This branch touches `arm_outcome` (the new
"decidable" fields) and `gate` (the row-choice split), so the condition
fired. I copied the three scripts unchanged into a scratch folder, so that
their outputs would not overwrite the committed ones, and ran them from the
root of the branch's tree. Outputs are in `rt237-rerun-on-pr151/`.

```
$ python3 -I recount_from_rows.py            # exit 0
$ python recount_from_models.py              # exit 0
$ python code_gate_on_toy.py                 # exit 0
$ diff <committed>/recount_from_models.out.txt rerun/recount_from_models.out.txt   -> identical
$ diff <committed>/recount_from_models.json    rerun/recount_from_models.json      -> identical
$ diff <committed>/code_gate_on_toy.out.txt    rerun/code_gate_on_toy.out.txt      -> identical
$ diff <committed>/code_gate_on_toy.json       rerun/code_gate_on_toy.json
   only additions: a "row_choice" block in each of arm T's three gate rows
   (3,000 of 3,000 right rows, reported_only true); nothing else
$ diff <committed>/recount_from_rows.out.txt   rerun/recount_from_rows.out.txt
   only additions: the folders this branch adds (out-ruled-code-changes/a2-cases/*,
   passA-limit3000, passB-limit10000, t6-pipeline/10M and 30M), and the count line
   "clause states compared: 344; mismatches of any kind: 0" becomes
   "clause states compared: 740; mismatches of any kind: 0"; "RESULT: every recount matches"
```

So, on the branch's code:
- the gate code writes the same free-model counts as the independent
  recount on all twelve trained models (2,100, 2,238 and 2,324 on arm F, line
  1,546);
- all 740 clause states judged from raw counts agree with the code's,
  including in the 31 new case folders and in passes A and B, where the
  rows are now written by the gate code itself with
  `lesioned_candidate_own_correct`, `lesioned_candidate_other_correct` and
  `ownership_free_line` present at full size (2,100/2,214/1,546,
  2,238/2,542/1,546, 2,324/2,366/1,546);
- the "two seeds of three" decision is unchanged at three seeds. The new
  decidability field changes only the summary when fewer than three seeds
  are in, which the recount's case folders (one-seed-each,
  two-seeds-T-split) show without a mismatch.

**The closure holds.** Its condition 1 (that step 4b's real rows carry the
three fields) is unchanged and still owed, though passes A and B now show
the code writing them at full size. The closure check's worth-noting point
that `withhold` writes "line 1,546 of 3,000" whatever the row's size is also
unchanged: this branch does not touch `withhold`. S1 above concerns the same
counts as printed in the table.

## How to recompute

From the root of a checkout of `ruled-code-changes-2026-10-09` (scripts in
`docs/reviews/2026-10-09-ruled-code-changes-check-scripts/`, on this branch):

    sh .../rerun_models.sh OUT_B OUT_A          # 49 minutes here, three lanes plus two
    (cd experiments && python .../compare_checker.py headline)
    (cd experiments && python .../compare_checker.py mine OUT_B OUT_A)
    python .../replay_real_stream.py 0          # and 1, 2; about 5 minutes each
    (cd experiments/08-successor-degree && sh .../rerun_tests.sh OUT_T)
    python .../row_choice_10m.py experiments/08-successor-degree/artifacts/succ_t_10m_seed0/succ_t_10m_seed0.pt
    # the three RT-237 scripts, copied elsewhere first so they do not overwrite their committed outputs

## What this does not do

It does not fix anything, edit version 5, the rulings, the ledger or the
pull request's branch, merge anything, or name the registered commit.
