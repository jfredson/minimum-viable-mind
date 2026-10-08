# The code changes ruled on 2026-10-08, and the page 4 re-run under them: method

*Written 2026-10-08 (Thursday afternoon, Pacific) by a Claude Code session, on
branch `ruled-code-changes-2026-10-09`, before any code was changed or any
figure below was computed. The file carries the date the task named for it.
Laptop only, processor only, $0: nothing rented, no paid service called, no
key handled.*

*Written under the workspace plain-language rule. A method for changes to
frozen, not yet registered code, and a rehearsal on the committed toy models.
NOT A RESULT about the scientific question.*

## 1. What John ruled, and what this does

John ruled on 2026-10-08 that the open items of version 5 of the registration
text be settled as recommended (`docs/rulings/2026-10-08-v5-open-items-rulings.md`,
"Agreed on all."; authorship mixed). Three of those rulings ask for changes to
the frozen successor code in `experiments/08-successor-degree/src/`:

1. **The fitting step (item 7).** The straight-line fitter's iteration limit
   goes from 3,000 to 10,000. In the same change the frozen procedure fits
   every read on 1,800 of 1,980 development episodes and scores it on the last
   180, as ruled on 2026-10-06 (page 4 of that day's rulings) and as version 5
   registers (sections 7.2, item 1, and 7.4). Today the code fits on 420 of
   600. The page 4 re-run of 2026-10-06 made the change only at run time, by
   wrapping the frozen code (`experiments/rehearsal-successor-measure/src/page4_models_1800.py`);
   this change puts the same thing in the frozen code itself. The
   nomination's transplant passes stay on the 600 development pairs, as
   version 5 says.
2. **The outcome words (items 3 and 4).** The code prints version 5's
   registered terms (section 3, the "Registered term" column) instead of
   version 4's names, including the eighth term, "instrument returned no
   reading on the separable mechanism", and the scope phrases section 3's
   scope rule requires: "on these constructed systems, for this intervention
   procedure" after every "instrument ..." term and after R2; "as a ratio of
   two transplants at the sites this procedure chose" after "degree read".
3. **Fewer than three seeds (item 9).** When an arm has fewer than three seeds
   in and the missing seeds could still change its gate, the summary says
   "gate not decidable on one seed" (or two seeds) instead of "failed its
   gate".
4. **Arm T's row-choice split (item 9).** The frozen code does not output it
   today (checked: nothing in `src/` computes the row the ownership answer
   selects). It is added as reporting only, beside arm T's gate: how often the
   row chosen is the right agent's, the accuracy where it is right and where
   it is wrong, the accuracy with the row forced onto the right agent, and
   which pairs of agent name words are confused. It decides nothing. It is the
   development-runs check's script (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-scripts/arm_t_errors.py`)
   brought into `procedure.gate`.
5. **Not changed:** arm M's per-step copy (declined, item 9).

## 2. Choices this session makes in doing it (an agent's calls, not rulings)

- **The 1,980 development episodes become a named evaluation set**,
  `dev_reads` in `grammar.EVAL_SETS`, built by the same generator with the
  same seed as the 600 (`make_pairs(1980, seed=4242, pool="dev")`), whose
  first 600 pairs are the 600; a self-test asserts that. Being an evaluation
  set, its 1,380 new contents join the list the training stream refuses, as
  every evaluation set's do (version 5, section 7.1: training and
  development episodes are disjoint). The pinned fingerprint of the
  evaluation sets changes accordingly. **Expected effect on training: none**,
  because no training draw has ever matched an evaluation episode exactly (a
  replay of the 10-million run's 5,228,112 training contents found none). A
  replay of seeds 0, 1 and 2 over the registered 108,919 steps checks it: the
  count of training draws that are one of the 1,380 must be 0 on each seed.
- **Every fit is counted when it stops at the limit**, by kind (the
  ownership read, the named agent's read, the held-out counts, the shuffled
  labels of the null, the counts elsewhere on the site), and written into each
  row as reporting only. The page 4 re-run could not say which fit its 471
  warnings came from; this lets the next run say. The warnings scikit-learn
  prints are left on, so the log count can be compared with the old one by the
  old command (`grep -c "failed to converge"`).
- **Outcome codes are renamed with the words**, so no output carries the
  retired word: "fallback_read", "fallback_not_read" and "not_validated"
  become "sixth", "seventh" and "eighth", after section 3's table. The
  made-up-case expectations of `tests/a2_cases.py` are not edited; a dated
  addendum maps old codes and old words to new, written before the runner
  runs, and the runner writes to a new folder so the committed record of
  `out-a2-cases/` stays as it was.
- **"Not decidable" means exactly this**: an arm with fewer than three seeds
  in whose learning gate has not passed (fewer than two seeds passing every
  learning condition) but could still pass if the missing seeds passed. Such
  a gate is reported as "gate not decidable on N seed(s)" and the outcome is
  not computed, with that reason. An arm with two seeds in, both failing, has
  failed (no third seed can make two). Arm F's step 5a record is unchanged:
  the step 5a ruling already decides that run by itself.
- **On a pipeline test with every set scaled down**, the read pool is scaled
  and split in the same proportion (1,800 of 1,980). A scaled run is never a
  registered figure and says so, as before.

## 3. The page 4 re-run under the new code

The same twelve committed toy models (`experiments/rehearsal-successor-measure/out-repairs/models/`,
checked against `SHA256SUMS`) and the competing solver, measured on the
laptop's processor.

- **Pass A, the reproduction check.** The new frozen procedure, run directly
  (`procedure.py model`), with only its iteration limit set back to 3,000 at
  run time. Every figure the committed 1,800-fitted rows carry
  (`out-page4-rerun-1800/models-1800/`) must come back identical, and every
  read array too. Fields added to the rows since that run (the in-use check,
  the ownership-free line, the row-choice split, the limit counts) are
  outside the comparison; run times, paths, library versions and that run's
  own note are skipped, as that run's check skipped them. The warning count
  per model must equal the old one (arm M 132, 240 and 99; arm F 2, 11 and 10;
  arm C 0, 0 and 1; arm T 0). **If pass A does not reproduce, pass B does not
  run**: the port is wrong and is fixed first.
- **Pass B, the registered code.** The same, at the new limit of 10,000.
  Then `procedure.py summarise` under the current decision code, which is
  also the re-summary the page 4 check said was owed. The solver at 10,000
  through a run-time wrapper of the committed page 4 solver driver (the
  solver is rehearsal code, not frozen code, so it is not edited).

Three models run side by side, one lane per seed (arm T first in each lane,
because the rider reads arm T's site set); the page 4 run showed thread count
and side-by-side running change no figure. If pass B runs past four hours,
it is stopped and the time reported.

## 4. What I expect before looking

- **Arm T** (no fit stopped at the limit before): pass B identical to pass A,
  bit for bit. Its row-choice split: right row on 3,000 of 3,000 gate episodes
  on every seed, no confused pairs (seed 0 was measured so by the
  development-runs check).
- **Arm C** (one warning, seed 2): identical on seeds 0 and 1; on seed 2
  identical figures unless its one stopped fit was a read; no site set,
  piece or reading moves.
- **Arm M**: the warnings fall from 471 to under 25 in all, and most of what
  is left, if anything, is the shuffled-label null. Its readings move by less
  than 0.05 from 0.5252, 0.4793 and 0.5208, stay inside 0.3 to 0.7 and within
  0.10 of the true-slot reading; its site set moves on at most one seed.
- **Arm F**: warnings fall from 23 to under 5; still no reading on every seed,
  best piece anywhere well under 144 (it was 40, 19 and 36). Control 2 on
  seed 0 may or may not keep its "reported" status; no prediction.
- **The solver**: still no reading under both readings.
- **No toy decision moves**: none of the page 4 method's seven concerns
  happens (a built model losing its nomination; arm T not reading 0.0000 or
  its control 1 failing; the separation, arm C's lowest minus arm T's
  highest, under 0.5 or missing; arm M outside 0.3 to 0.7; the free model's
  read reaching the floor; the solver returning a reading; control 7 or 4
  failing).
- **The outcome under the current decision code**: R3, "substrate not a
  testbed", naming arm F's named-other condition, because the free model
  passes that condition on one seed of three. In the summary, arms C and M
  are also withheld on every seed by the in-use check ("construction did not
  hold"), because these toy models were trained before the sharpness fix and
  their built route is not in use at the ruled bar (the sharpness findings,
  section 4), so the summary itself computes no separation. Their per-model
  arithmetic, which version 5 quotes, is still in each row, and the
  separation is computed from it beside the summary.

## 5. What would count against the change

- Pass A not reproducing the checked 1,800 figures: the port is wrong.
- Arm M's real reads (not the null) still stopping at 10,000: the limit is
  still short. Reported, not changed: the ruling set the number.
- Any toy decision moving: the reads cut short at 3,000 were materially off,
  and version 5's toy sentences need more than new figures.
- A self-test, the made-up cases, the in-use cases, the model-loading test
  or the launcher test failing; or the training replay finding a drawn
  content among the 1,380.

## 6. The tests, as the freeze and the later findings name them

- `src/run_self_tests.sh` (test T1, every self-test), updated for the new
  words, the new set and the new numbers.
- `tests/load_toy_models.py` (test T2).
- `tests/a2_run_cases.py` (the 28 made-up cases), into a new folder.
- `tests/inuse_cases.py` (the in-use check's made-up cases).
- `tests/check_launcher.sh` (test T7, creates nothing).
- `tests/pipeline.sh` (test T6, the whole pipeline at 10 and 30 million
  parameters, every set at a quarter, three shuffles), after the page 4
  passes.
- Test T3 (`tests/reproduce_toy.py`) compares against the 420-fitted toy
  record, so under the new fitting count it differs by design; pass A
  replaces it as the reproduction check.

## 7. What this does not do

It does not edit version 5, any ruling or the rehearsal's code, and does not
merge. The figures version 5 would need to change are listed in the findings.
The check of this work by a session that did not do it is owed (item 7 of the
rulings asks for it before the registration commit).
