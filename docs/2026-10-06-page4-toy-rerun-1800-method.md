# Method: the page 4 toy re-run, with every read fitted on 1,800 development episodes

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
branch `page4-toy-rerun-1800`, based on `main` at `865f108`. **Committed and
pushed with its code before anything in it was run.** Laptop only, processor
only, nothing trained beyond small straight-line fits, nothing rented: $0.*

*Written under the workspace plain-language rule. This is a rehearsal on the
committed toy models. Nothing here is a result about the scientific question,
and no number it produces is a bar for anything.*

## 1. Why this is being run

John ruled on 2026-10-06 on page 4 of the twelve-page packet about the
registration text of the successor experiment, version 4 (the inside review's
finding RT-240: the episode counts ruled on 2026-10-03 had only been tried at
a third of the registered model's width). He took option (a): **every
straight-line read is fitted on 1,800 development episodes**, with 180 more
held out (1,980 in all, so the floor stays 144 of 180), and the transplant
passes of the nomination stay on 600 development pairs. Option (c), training a
448-wide stand-in model on the laptop, was not taken, and nothing here trains
one.

The ruling owes, before registration, "one $0 toy re-run of the nomination and
reading with every read fitted on 1,800 episodes, method committed before
output, run by a session other than the one that drafted the dispositions,
and checked by another". It is owed because the directions that get
transplanted come from the read, so refitting it can move which site set and
size the nomination chooses, not only the printed counts.

Sources:

- the question: `docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`,
  page 4 (pull requests 95 and 96, and on pull request 103's branch);
- the drafted text and the work owed: `docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`,
  the section on RT-240;
- the ruling: `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`, page 4,
  and item 3 of its list of work before registration (pull request 103,
  branch `rulings-2026-10-06-gate-a-v4`, not yet merged or checked);
- the stand-in measurement the ruling rests on:
  `docs/2026-10-04-gate-a-v4-dispositions-measurements.md`, part B (same
  branch).

This session did not draft the dispositions, did not run that measurement,
and wrote none of the code it runs below except the three thin drivers named
in section 3.

**Why based on `main` and not on the rulings branch.** Everything this re-run
executes is on `main`: the committed toy models, the frozen measurement
procedure, and the committed solver run. The rulings branch adds only text
and the stand-in measurement, and is itself still owed its check, so basing
on it would tie this pull request to that one for no gain. The ruling files
are cited above by branch.

## 2. What "the toy" is, and what is re-run

**The toy** is the set of small trained models the measurement was rehearsed
on: four architectures (arm T, which keeps the ownership answer in a separate
slot; arm C, entangled; arm F, free; arm M, a mixture), three seeds each,
twelve models in `experiments/rehearsal-successor-measure/out-repairs/models/`
(fingerprints in `SHA256SUMS`), plus the competing solver: the same
architecture trained with no acting channel, three seeds.

**How many fitting episodes it used before: 420.** The toy record fits every
read on the first seven tenths of 600 development episodes (420) and counts
it on the last 180 (episodes 421 to 600). That is ruling 4 of 2026-10-03,
late evening ("the episode counts are the toy's"). It holds in every place
the toy record was made:

- the twelve models' nomination and reading,
  `experiments/rehearsal-successor-measure/out-controls-rerun/` (reads taken
  from `out-repairs/reads_*.npz`, fitted on the graphics chip on 420);
- the frozen measurement procedure, `experiments/08-successor-degree/src/procedure.py`,
  which reproduces that record exactly (the code freeze's test T3a) and, run
  with the reads fitted once on the processor as the registered run will
  (test T3b), changes no decision: `experiments/08-successor-degree/out-freeze-tests/t3b-fresh-fit/`;
- the competing solver, `experiments/rehearsal-successor-measure/out-competing-solver-run/`
  (its read fitted on the processor on 420).

**What is re-run.** Two things, each with the code that made the committed
record, unmodified on disk:

1. **The twelve toy models,** through the frozen procedure
   (`procedure.run_model`, then `procedure.summarise`): the gate, the reads,
   the 200-shuffle null, the nomination over the 45 site sets and four sizes,
   the reading on fresh episodes, controls 1, 3, 4, 6 and 7, the true-slot
   reference, the rider, the piece's counts at the other positions of its
   site, control 2, and the outcome term. The frozen procedure is used rather
   than the older rehearsal scripts because it is the code the registered
   run will execute, because it fits the reads on the processor once as the
   registered run will, and because its fresh-fit record at 420 (T3b) is a
   baseline that differs from this run in nothing but the fitting count.
2. **The competing solver,** through `competing_solver_run.main`, both of its
   readings (channel removed, the primary; channel left on), three seeds.

**What changes, and only this:**

- every straight-line read (the ownership read; the named agent's read used by
  control 2; the shuffled-label fits of the null; the counts of the piece at
  the other positions of its site) is **fitted on the first 1,800 and counted
  on the last 180 of a development pool of 1,980 episodes**, instead of the
  first 420 and last 180 of 600;
- the pool is drawn by the same generator with the same seed (4242, pool
  "dev") as the frozen 600. **Its first 600 pairs are the frozen 600**,
  checked pair by pair before anything is fitted; the drivers stop if not.

A consequence of the ruling, not a separate choice: the 180 held-out
episodes are now episodes 1,801 to 1,980, not 421 to 600. Some movement in
the counts will come from the different held-out set rather than from the
larger fit. The ruling fixes this split ("the first 1,800 fitted and the last
180 held out"), and part B of the stand-in measurement used the same one.

**What stays fixed:** the twelve model files and the three solver files
(fingerprints checked before loading); the seeds (models 0, 1, 2; episode
sets 4242 for development, 4243 for control 2's development donors, 777 fresh,
781 control 2's fresh donors, 778 relaxed, 99 gate; random pieces and null
shuffles as seeded in the code); the 600 development pairs every transplant
pass of the nomination runs on; the 800 fresh pairs of the reading; the
3,000 gate episodes; the site-set family; the four sizes (1, 2, 4, 8
directions); the floor of 144 of 180; the regularisation (C = 1.0) and the
iteration limit (3,000); every rule; the processor; the library versions in
the shared `.venv`.

## 3. The code, and the commands

Three drivers, new, in `experiments/rehearsal-successor-measure/src/`, and a
script that runs them in order:

- `page4_models_1800.py` imports the frozen procedure and, at run time only,
  replaces its fitting split (first seven tenths) with "all but the last 180",
  and hands the reads the pool wherever the procedure would hand them the
  frozen 600 development recipients. With `--pool 600` both changes do
  nothing. The shuffled-label null is copied line for line with the split
  changed, because the frozen function computes its split inline.
- `page4_solver_1800.py` does the same for `competing_solver_run.py`.
- `page4_compare.py` makes the reproduction checks and the comparison.
- `page4_run_all.sh` runs everything in order; arm T's three seeds go first
  because every other arm's rider reads arm T's site set for the same seed.

From `experiments/rehearsal-successor-measure/src/`:

    sh page4_run_all.sh 4

Outputs go to `experiments/rehearsal-successor-measure/out-page4-rerun-1800/`:
`models-420/` and `solver-420/` (the reproduction checks), `models-1800/` and
`solver-1800/` (the re-run), `comparison.json`, `comparison.md`, and a log
per step.

**Time limit.** The committed runs took about 66 minutes for the twelve
models (one at a time) and 14 minutes for the solver; nearly all of it is the
transplant passes, which this re-run does not change, and a timing of the
straight-line fit on random data showed no material slowdown from 420 to
1,800 rows. Models run four at a time. Expected: under an hour and a half for
both passes. **If the first pass (the reproduction checks) shows the whole
would take more than about two hours, the run stops and this is reported with
an estimate instead.**

## 4. The reproduction check, before the 1,800 run

With `--pool 600` the drivers must reproduce the committed records **exactly,
value for value**: every field of the twelve rows and the reads files in
`t3b-fresh-fit/`, and every file of `out-competing-solver-run/`, except run
times, file paths and the library list. This shows the drivers change nothing
but what section 2 says. **If either check differs anywhere, the 1,800 run is
not made**; the difference is reported and goes back to the caller.

## 5. Which numbers are compared, old against new

Old is the 420-fitted record (T3b for the twelve models;
`out-competing-solver-run` for the solver). New is the 1,800-fitted re-run.
For each of the twelve models:

- the nomination's status, the chosen site set and size, and the chosen
  piece's and whole read's held-out counts;
- the reading (the share of the whole-state transplant's effect the piece
  does not carry; arithmetic on fresh episodes);
- control 1 (the complement of the piece; holds on arm T only), control 3
  (where the piece sits among twenty random pieces), controls 4 and 7, the
  true-slot reference (arms T and M), the rider (the arm read at arm T's site
  set), the stricter variant's site set, control 2's status;
- the best piece count at any state and size (this is what decides whether
  the free model's read reaches the floor).

Across models: the separation, arm C's reading minus arm T's, per seed; the
outcome term and the gates. For the solver, per reading and seed: the best
piece count, the nomination's status, and whether a reading was returned.

Expected (ARGUED from part B of the stand-in measurement, where at the toy's
own width more fitting episodes changed no verdict): no status changes; arm T
unchanged; the free model's best piece stays far below 144 (part B's best was
41); the solver returns no reading; the separation stays above 0.5 on every
seed; arm C seeds 1 and 2, whose chosen pieces stood at 172 and 150, may move
to a different site set or size, because more pieces may clear the floor and
the rule picks among those that do.

## 6. What would be a concern

Each is checked mechanically by `page4_compare.py` and reported, whichever way
it comes out:

- **A.** A built model (arm T, C or M, any seed) loses its nomination.
- **B.** Arm T's reading is not 0.0000, or its control 1 does not hold.
- **C.** The separation, arm C minus arm T, is below 0.5 or missing on any
  seed.
- **D.** Arm M's reading falls outside 0.3 to 0.7 on any seed.
- **E.** The free model's read reaches the floor: a piece of 144 or more at
  any state and size, or a nomination. This would change the toy record
  version 4 describes (the free model unread at toy size) and goes to John.
- **F.** The solver returns a reading on any seed under either reading.
- **G.** Control 7 or control 4 fails anywhere. They do not depend on the
  read, so a failure would mean something other than the fit count changed.

**Reported, not a concern on its own:** a change of chosen site set or size.
That is the reason the re-run is owed. It is listed model by model, with the
reading before and after.

Any of A to G goes back to the caller and to John with the figures. None of
them is a pass line for registration; the ruling asks only that the re-run
be made, method first, and checked.

## 7. What it does not show

Anything about the registered width. The toy models are 160 wide; the
problem page 4 was about appears on a 448-wide stand-in made of noise, and
this re-run does not touch that. It shows only what fitting on 1,800 does to
the toy record that version 5 will quote, and whether it moves any toy
decision.

## 8. What is owed after it

A check by a session that ran none of it: re-run `page4_run_all.sh` from the
committed code, compare value for value with the committed outputs, and read
the comparison against sections 5 and 6.
