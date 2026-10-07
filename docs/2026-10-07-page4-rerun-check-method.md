# Method: the independent check of the page 4 toy re-run (pull request 121)

*Written 2026-10-07 (Pacific) by a Claude Code session that ran none of the
re-run, on branch `check-page4-rerun` (its own worktree), based on the re-run's
branch `page4-toy-rerun-1800` at `e6c5dbc`. **Committed before any check below
is run.** Laptop, processor only, $0.*

*Written under the workspace plain-language rule. A check of a rehearsal on the
committed toy models. NOT A RESULT about the scientific question.*

## What is being checked

Pull request 121: the toy re-run John ruled on 2026-10-06 (page 4 of the
twelve-page packet on version 4 of the successor experiment's registration
text, the inside review's finding RT-240, option (a)): every straight-line
read fitted on 1,800 development episodes and counted on 180 more. Its method
is `docs/2026-10-06-page4-toy-rerun-1800-method.md` (commit `ea2dad2`), its
findings `docs/2026-10-06-page4-toy-rerun-1800.md`, and its script-written
comparison `experiments/rehearsal-successor-measure/out-page4-rerun-1800/comparison.md`.

What it reports: no toy decision moves; the separation (arm C's reading minus
arm T's) is 1.0026, 1.0000 and 1.0000; none of the seven concerns stated in
its method (A to G) happened; the chosen site set or size moved on 5 of 15
models; the free model (arm F) fails its floor everywhere; the competing
solver returns no reading.

## The four steps

1. **Order and scope.** From the git history: the method and all four
   scripts are in a commit before any output; the scripts are not changed
   after it; the pull request touches nothing in the frozen procedure
   (`experiments/08-successor-degree/src/`) or the committed solver code. By
   reading the two drivers: they change only the fitting split (all but the
   last 180, instead of the first seven tenths) and hand the reads the
   1,980-episode pool where the frozen code would hand them the frozen 600,
   and nothing else. Also noted: whether `main` has moved under the frozen
   procedure since the re-run's base.
2. **An independent route, without the author's scripts.** A new script
   written here (`experiments/rehearsal-successor-measure/src/check_page4_refit.py`)
   that imports only the frozen grammar and model code, not the drivers and
   not the procedure's fitting functions:
   - rebuild the pool with the frozen generator,
     `make_pairs(1980, seed=4242, pool="dev", collide=False)`, and confirm
     its first 600 pairs equal the frozen 600 pair for pair;
   - load the committed toy model (fingerprint checked), take the running
     state at the own-directed action position, label each episode with the
     model's own marker, and fit `LogisticRegression(max_iter=3000, C=1.0)`
     on recipients 1 to 1,800, scored on 1,801 to 1,980;
   - for the pieces, take the top directions of the committed 1,800 read
     (as the frozen code does) and refit on the projected states;
   - compare with the `fits` field of the committed 1,800 row, state by
     state, whole read and every size.
   Covered at least: arm C seed 2 (its chosen piece 150 to 165), arm M seed 0
   (its site set moved), one arm T read, and one arm F read. A fit is checked
   against the committed counts exactly; any difference is reported.
3. **The full recompute,** only if the laptop's one-minute load is under
   about 15 when it starts: the steps in the findings' section "How to
   recompute the 1,800 run", one model at a time, into a separate folder
   (`out-page4-check-1800/`), then a value-for-value comparison with the
   committed `models-1800/` and `solver-1800/`, skipping run times, file
   paths and the library list (the keys `seconds`, `checkpoint`, `versions`,
   `torch`, and the solver log's output path), with every reads array
   compared array for array. If the load is high, this step is not made and
   that is said.
4. **The judgement.** Whether `page4_compare.py` checks the seven concerns as
   the method states them, and whether the findings overstate anything
   against the committed numbers.

## What would be a problem

- an output committed before the method, or a script changed after it;
- a driver changing anything beyond the fitting split and the pool;
- the pool's first 600 not equal to the frozen 600;
- an independent refit giving a count different from the committed `fits`;
- in the full recompute, any value differing (beyond run times, paths and
  library lists);
- a concern checked more loosely than the method states it, or a claim in the
  findings the numbers do not support.

The verdict is one of: **reproduced** (no problem), **reproduced with notes**
(problems that change no number or toy decision), or **not reproduced**.
