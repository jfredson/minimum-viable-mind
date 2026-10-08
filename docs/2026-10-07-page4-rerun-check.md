# Check of the page 4 toy re-run (pull request 121): findings

*Written 2026-10-07 (Pacific) by a Claude Code session that ran none of the
re-run, on branch `check-page4-rerun` in its own worktree. Method committed
and pushed first, at `aab668e`: `docs/2026-10-07-page4-rerun-check-method.md`.
Laptop, processor only, $0.*

*Written under the workspace plain-language rule. A check of a rehearsal on
the committed toy models. NOT A RESULT about the scientific question.*

## Verdict: reproduced, with notes

Every number in the re-run reproduces exactly, by two routes. No toy decision
moves, and none of the seven concerns stated in advance happened. The notes
are about the write-up and the checks, not the numbers. The main one: the
findings miss one changed status. On the free model's seed 0, control 2 (the
check on the other agent) went from no verdict to a reported description,
because the read of the named other agent now clears the floor (171 of 180).

## 1. Order and scope

- **The method came first.** The method and all four scripts were committed
  at `ea2dad2` (2026-10-06 19:03). The 420-episode reproduction outputs came
  next at `f5bb7a4` (23:13), then the 1,800 outputs and findings at `e6c5dbc`
  (2026-10-07 01:19). No script changed after `ea2dad2`, which
  `git diff ea2dad2 e6c5dbc` confirms: only the findings and outputs changed.
- **The frozen procedure is untouched by this pull request.** It changes
  nothing under `experiments/08-successor-degree/` and nothing in the
  committed solver code. It only adds four files in
  `experiments/rehearsal-successor-measure/src/` and the outputs.
- **The drivers change only the split and the pool.** In
  `page4_models_1800.py`, the replaced fitting step fits on all but the last
  180. Every function that fits or scores a read (the fit, the count, the
  shuffled-label null and the counts elsewhere on the site) gets the
  1,980-episode pool wherever the frozen code would pass the frozen 600, and
  only there. Everything that calls the count step is reached only through
  those functions, so nothing outside the reads changes its split. The
  transplant passes, control 2's grid, the fresh, relaxed and gate sets, the
  floor of 144 of 180 and every rule stay the frozen code's own. The solver
  driver makes the same two changes to `competing_solver_run.py`.
- **`main` has moved since the re-run's base.** The re-run is based on `main`
  at `865f108`. Since then, the decision-procedure work (pull request 105, "A2")
  has changed `procedure.py`, `measure.py` and `grammar.py` on `main`. Those
  changes touch the gate report, the withholding rules, the outcome and the
  table. They do not touch the reads, the nomination or the transplants. The
  per-model figures stand. But the outcome line and `summary.json` were made
  under the pre-A2 rules, and running these drivers from `main` after a merge
  would not reproduce the committed rows field for field, because the gate
  row gained fields. Recompute from the branch commit, not from `main`.

## 2. The independent route, without the re-run's scripts

`src/check_page4_refit.py`, written here, imports only the frozen episode
generator, the frozen model code, and the frozen definition of a piece (the
top directions of a read). It builds the pool, the labels, the states at the
action position, and the fit and count itself.

- `make_pairs(1980, seed=4242, pool="dev", collide=False)`: **its first 600
  pairs equal the frozen 600, 600 of 600.** None of the 180 held-out
  recipients (1,801 to 1,980) repeats a fitting recipient exactly.
- `LogisticRegression(max_iter=3000, C=1.0)` fitted on recipients 1 to 1,800
  and counted on 1,801 to 1,980, at every state, the whole read and all four
  sizes, on **arm C seed 2, arm M seed 0, arm T seed 0, arm F seed 0, arm C
  seed 1 and arm F seed 2**: **150 counts compared, 0 differ** from each
  row's `fits`. Every refitted read is identical to the committed reads file
  (largest difference 0).
- Arm C seed 2 at state 1 gives 165 at four directions (it was 150 at 420)
  and 180 for the whole read. Arm M seed 0's new site set, state 3 at the
  action with 8 directions, gives 180. The free model's best piece is 40
  (seed 0) and 36 (seed 2), as reported.

Output: `out-page4-check/refit.json`.

## 3. The full recompute

The one-minute load was 1.9 to 3.4 throughout, under the limit of about 15.
The findings' "How to recompute the 1,800 run" steps ran one model at a time,
through `src/check_page4_recompute.sh`, into
`out-page4-check/recompute-1800/`, from 01:23 to 02:45, **1 hour 22 minutes**.
They were compared with the committed `models-1800/` and `solver-1800/` by
`src/check_page4_compare_recompute.py`, written here (not `page4_compare.py`).
It skips only `seconds`, `checkpoint`, `versions`, `torch` and the solver
log's output-path line.

**40,855 values and 150 read arrays compared, 0 differ.** That covers the
twelve model rows, the summary and table, and every solver file (both
readings, three seeds). Four processor threads were used, as in the re-run.

*One note on order:* the comparison script was written after the method
commit, while the recompute was running and before its outputs existed. It
does what the method's step 3 states.

## 4. The seven concerns, and the write-up

**How `page4_compare.py` checks them.** Each concern matches the method's
wording, and each verdict is right on the committed numbers. Two of them check
less than the method's wording:

- **G** ("control 7 or control 4 fails anywhere") looks only at the chosen
  site set's controls. It skips the stricter and sensitivity rows, which also
  carry controls 4 and 7. Checked here: both hold on every model that has
  them. The verdict does not change.
- **E** ("the free model's read reaches the floor") looks at the ownership
  read only, which is what the method means. The free model's *named-agent*
  read, which control 2 uses, is outside E. See the first problem below.

Concerns C and D, and arm M's prediction, were also confirmed from the
recomputed summary. Separation by seed is 1.0026, 1.0000 and 1.0000. Arm M
reads 0.5252, 0.4793 and 0.5208, each within its tolerance of the true-slot
reference.

**Problems, most important first:**

1. **One changed status goes unreported, and the findings say "it changes no
   status".** On arm F (the free model) seed 0, control 2 moved from "no
   verdict: read failed its floor" to "reported; no pass line". The named
   other agent's read rose from a best piece of 140 to 176. Control 2's
   nomination now picks state 3 at the action, 8 directions, piece 171 of
   180. That run's own-directed answers moved 0.0 against twenty random
   pieces. `comparison.md` marks it "**no**". The findings' short version, its
   section 2 table and its line "it changes no status" leave it out. The
   method lists control 2's status among the compared numbers (section 5).
   Control 2 has no pass line, and arm F fails its learning gate anyway, so no
   toy decision moves. But version 5 should not say that 1,800 fitting
   episodes changed no status. A fair line: the free model's ownership read
   stays far below the floor (best 40 of 180), while its read of the named
   other agent now clears it on one seed.
2. **The straight-line fits stop at the iteration limit far more often at
   1,800 episodes, and the findings don't say so.** The solver warning that
   the fit "failed to converge after 3000 iterations" appears 471 times across
   arm M's three logs at 1,800, against 27 at 420 (arm F: 23 against 30; arms
   T and C: 1 against 2). The method fixes the limit at 3,000, so the run is
   correct to its method, and the figures reproduce to the bit. But arm M's
   reads at 1,800 are partly products of where the fitter stopped. That is
   worth a sentence in version 5, and worth carrying to the registered width,
   where page 4's question sits.
3. **The time limit was reset by an agent, not by John.** The method said to
   stop and report an estimate if the run would take more than about two
   hours. The reproduction pass alone took 4 hours 8 minutes under heavy
   load. The 1,800 pass was stopped as required. The coordinating session then
   set a new three-hour limit and restarted it. The findings say this openly,
   and the limit was an operational guard, not a scientific rule, so nothing
   is wrong with the numbers. But the record should name it as an agent's
   call, not a ruling.
4. **The outcome line uses the pre-A2 rules** (section 1 above). "Substrate
   not a testbed", from arm F failing its learning gate, will most likely
   survive under the A2 rules, but `summary.json` was not made by them.
   Re-summarise under the current `main` before version 5 quotes the outcome.
5. **Small wording points.** "No reading by more than 0.037" is right (arm M
   seed 0 moved 0.0366). "The pieces nearest the floor moved away from it" is
   right for arm C seeds 1 and 2. Arm C seed 0's chosen piece fell 180 to 178,
   still far above the floor. The rider (each arm read at arm T's site set)
   gives no verdict on arms C, M and F both before and after. That is
   unchanged, so not a problem here, but the table shows it only as a dash.

Nothing found overstates the main result. No toy decision moved; the
separation, the free model's ownership read, and the solver are as reported.

## Files

- `docs/2026-10-07-page4-rerun-check-method.md`: the method, committed first
- `experiments/rehearsal-successor-measure/src/check_page4_refit.py`: step 2
- `experiments/rehearsal-successor-measure/src/check_page4_recompute.sh`: step 3, the run
- `experiments/rehearsal-successor-measure/src/check_page4_compare_recompute.py`: step 3, the comparison
- `experiments/rehearsal-successor-measure/out-page4-check/`: `refit.json`,
  `recompute-1800/`, `recompute_comparison.json`, `log_recompute.txt`
