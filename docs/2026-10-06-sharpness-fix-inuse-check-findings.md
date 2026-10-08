# Findings: the ownership sharpness fixed at 4.0, the in-use check, and the toy retrain

*Written 2026-10-06 (Pacific) by the Claude Code session that wrote the
method (`docs/2026-10-06-sharpness-fix-inuse-check-method.md`, committed
first, at `042dc17`), on branch `fix-sharpness-inuse-check`. Laptop only,
nothing rented: $0. **Owed its independent check before the three
10-million-parameter reruns John approved.** Nothing here is a result about
the scientific question.*

## In short

- **The fix is in and holds.** In arms T, C and M the sharpness is now a fixed
  4.0 that training cannot move; every retrained toy model ended at exactly
  4.0. Arm C's weight on the agent it actually is went from 0.914, 0.573 and
  0.681 (seeds 0 to 2) to 0.999 on every seed. Learning is not hurt: no
  retrained seed lost more than 36 of 3,000 own-directed answers.
- **The in-use check is in the decision code** and lands where the method
  said on all 14 made-up cases on real models and all 28 decision-code cases
  (the 25 from pull request 105 unchanged, plus 3 new).
- **A concern the method named has fired (concern 2), and it needs a ruling
  before the reruns.** Part B of the check (does the network actually use the
  built answer?) fails on **every toy arm C and arm M seed, before the fix and
  after it**. Swapping arm C's built answer to another agent loses only 24% to
  29% of its right own-directed answers (bar 50%); arm M's stirred-in half
  loses 9% to 11%. Arm T and arm M's separable half lose 100%. So on the toy
  the stirred-in route was never the main carrier of "which agent am I": the
  network mostly gets it from the "this turn is yours" signal through its
  attention layers, the same free route arm F uses. The fix does not change
  that (figures below). **With the bar as written, the reruns would very
  likely give arms C and M no verdict, which is version 4's fallback.**
- **The toy re-read was stopped early** to keep within about two hours:
  training took 1 hour 44 minutes, three at a time, and the processor was
  shared with another session's run. Arm T seed 0 was fully re-read (reading
  0.0000, all controls hold, same as before). The other 11 full re-reads are
  estimated at about an hour on a quiet laptop.

## 1. What changed in the code

| File | Change |
|---|---|
| `src/models.py` | `own_sharpness` is a fixed stored value (a buffer) of 4.0 in arms T, C and M; arm F unchanged. Same name, so every saved model loads strictly; an old model loads with the value it learned. Self-tests: not learned, exactly 4.0 after optimiser steps with heavy weight decay, old values load. |
| `src/procedure.py` | `gate` now writes `route_in_use` for every arm: the sharpness, the weight on the true agent (part A), and per built route the right answers with the true answer and with the answer swapped to the next agent round (part B). `swap_answer` makes the swapped episodes. |
| `src/measure.py` | `route_check` judges it (part A: weight at least 0.9; part B: route use at least 0.5 on every built route; a route with nothing right to lose "could not be evaluated"; a missing field "not run"; all of these count against). `withhold` adds the check "built ownership route in use" for arms T, C and M; a failure gives no verdict with the reason "construction did not hold". It is not a learning condition, so it never gives "substrate not a testbed" by itself. Self-tests added. |
| `tests/a2_cases.py`, `tests/a2_run_cases.py` | The committed toy rows predate the check, so the runner gives built-arm rows a passing made-up `route_in_use` first (as the method said it would); three new cases. |
| `tests/inuse_cases.py`, `tests/retrain_toy_fixed.py`, `tests/retrained_toy_inuse.py` | New: the made-up cases on real models, the toy retrain, and the retrained figures. |
| `README.md` | A short section at the end (placed away from the other branch's edit). |

No change to the training code, the generator, or the spending alarm.

**Merging.** The decision code (pull request 105) is already on main, and
this branch is cut from it, so the check sits directly in it. The other open
change to the frozen code, branch `training-exclusion-pairing` (training
leaves out fresh and relaxed pairings: `grammar.py`, `train_successor.py`,
`README.md`), merges with this branch with no conflict (checked with
`git merge-tree` at `0064ef3`).

## 2. The made-up cases on real models (`out-sharpness-fix/inuse-cases/`)

All 14 landed as written in the method (`inuse_cases.json`, `stdout.txt`):

| # | Case | Weight on true agent | Route use | Check |
|---|---|---|---|---|
| 1 | toy arm T seed 0, unchanged | 0.999 | slot 1.000 | passed |
| 2 | same, sharpness 0 | 0.250 | slot 0.000 | failed |
| 3 | same, sharpness −0.09 | 0.218 | slot 0.012 | failed |
| 4 | toy arm C seed 0, sharpness 4.0, scale-and-shift and binding zeroed | 0.999 | 0.000 | failed |
| 5 | toy arm T seed 0, slot reader zeroed | 0.999 | slot 0.000 | failed |
| 6 | toy arm M seed 0, sharpness 4.0, separable slot reader zeroed | 0.999 | stirred-in 0.076, separable 0.452 | failed |
| 7 | toy arm M seed 0, sharpness 4.0, scale-and-shift and binding zeroed | 0.999 | stirred-in 0.000, separable 0.995 | failed |
| 8 | toy arm C seeds 1 and 2, unchanged | 0.573, 0.681 | 0.233, 0.221 | failed |
| 9 | toy arm F seed 0 (reference, not judged) | 0.999 | 0.000 | not applicable |
| 10 | real 10-million arm C | 0.218 | 0.018 | failed |
| 11 | real 10-million arm M | 0.247 | stirred-in 0.000, separable 0.000 | failed |
| 12 | real 10-million arm T | 0.942 | slot 0.924 | passed |
| 13 | untrained toy arm C | 0.999 | 0.000 | failed |

Two things the cases did not aim at but show: in case 6 the stirred-in route
fails too (0.076), not only the separable one; and case 6's separable route
still shows 0.452 with its slot reader zeroed. Both are explained by the
reference run below: the stirred-in route was low already.

**Reference run, not a pre-stated case** (`committed_toy_reference.txt`): the
check on all twelve committed toy models, unchanged. Arm T passes (route use
1.000 on all seeds). **Arm C fails on all three seeds** (route use 0.269,
0.233, 0.221; seeds 1 and 2 also fail part A). **Arm M fails on all three**
(stirred-in route 0.071, 0.090, 0.109; separable 1.000). Arm F: 0.000.

## 3. Decision-code cases (`out-a2-cases/`, `out-sharpness-fix/tests/a2-cases-results.md`)

28 of 28 land as expected, none leaks a withheld figure. The 25 cases of pull
request 105 land exactly where they did. New: arm C flat on seeds 0 and 1
gives "metric checked against the separable model only, degree read"; arm T
flat on seeds 0 and 1 gives "metric not validated" with the reason "the
built ownership route has gone flat (construction did not hold)"; arm M flat
on seeds 0 and 1 leaves the outcome at R1 with arm M without a verdict. (One
cosmetic point: the made-up arm T row is labelled with the stirred-in route's
name, because the made-up record uses one route name for all arms. Real rows
name arm T's route "the slot route".)

## 4. The toy retrain (`out-sharpness-fix/models/`, `retrained_inuse.txt`)

Nine models, the committed recipe exactly, sharpness fixed. Training took
1,660 to 2,200 seconds each, three at a time on the graphics processor,
19:18 to 21:02. Gate figures on the 3,000 gate episodes, committed toy then
retrained:

| Model | Own-directed right | Named-other right | Sharpness | Weight on true agent | Route use | Check |
|---|---|---|---|---|---|---|
| T/0 | 3000 → 3000 | 3000 → 3000 | 3.88 → 4.00 | 0.999 → 0.999 | 1.000 → 1.000 | passed → passed |
| T/1 | 3000 → 3000 | 3000 → 3000 | 3.88 → 4.00 | 0.999 → 0.999 | 1.000 → 1.000 | passed → passed |
| T/2 | 3000 → 3000 | 3000 → 3000 | 3.88 → 4.00 | 0.999 → 0.999 | 1.000 → 1.000 | passed → passed |
| **C/0** | 1711 → 1731 | 760 → 768 | **1.73 → 4.00** | **0.914 → 0.999** | 0.269 → 0.285 | failed → failed |
| **C/1** | 1703 → 1671 | 751 → 932 | **0.70 → 4.00** | **0.573 → 0.999** | 0.233 → 0.273 | failed → failed |
| **C/2** | 1727 → 1691 | 708 → 750 | **0.93 → 4.00** | **0.681 → 0.999** | 0.221 → 0.244 | failed → failed |
| M/0 | 2592 → 2590 | 1663 → 1701 | 2.84 → 4.00 | 0.990 → 0.999 | stirred-in 0.071 → 0.090; separable 1.000 → 1.000 | failed → failed |
| M/1 | 2584 → 2563 | 1699 → 1676 | 2.69 → 4.00 | 0.986 → 0.999 | 0.090 → 0.106; 1.000 → 1.000 | failed → failed |
| M/2 | 2600 → 2622 | 1655 → 1695 | 2.42 → 4.00 | 0.977 → 0.999 | 0.109 → 0.100; 1.000 → 1.000 | failed → failed |

**Against the concerns written in the method:**

1. **Learning: no concern.** Largest drop 36 of 3,000 (C/2), against a
   stated limit of 150. Every seed clears the 790 bar.
2. **The in-use check: concern fires** on all six arm C and arm M seeds, on
   part B only. It is not caused by the fix (the committed models fail the
   same way, and the fix raises route use slightly). It is what the toy
   design already was: arm C (and arm M's stirred-in half) also receive the
   acting signal in their trunk, so they can and do learn "which agent am I"
   through attention, as arm F does, and lean on the built route for only
   about a quarter (arm C) or a tenth (arm M) of their right answers.
3. **Readings: not tested beyond arm T seed 0.** Arm T seed 0's full re-read
   (`reread/row_T_seed0.json`): nominated (states 0, action, 8 directions,
   180 of 180), reading 0.0000, controls 1, 4 and 7 hold, both floors clear,
   check passed. Identical to the committed figure. The other 11 were not run.
4. **Toy outcome:** not re-summarised, because 11 rows are missing.

## 5. What this means, and what John needs to decide before the reruns

The ruling asked for a check that fails a built model whose route "has gone
flat". Part A is that check in its literal sense, and with the sharpness
fixed it now passes everywhere. Part B, added to catch the network routing
round the fixed answer (the risk the packet named for option 1), shows that
on the toy the route was already mostly bypassed in arms C and M. That does
not stop the toy measurement reading arm C at about 1.0 (the procedure finds
ownership entangled in the running state whichever way it got there), but it
does mean arm C is "entangled by construction" only in part.

Options, none chosen here:

- **(a) Keep part B at 0.5.** The 10-million reruns will very likely give
  arms C and M no verdict, so the outcome falls back to version 4's
  two-model plan. The $1.14 would mostly confirm that.
- **(b) Set part B's bar by comparison with the free model**, for example
  "route use clearly above arm F's 0.000" (a fixed small bar such as 0.1, or
  a one-sided test against zero). Toy arm C passes; toy arm M's stirred-in
  half sits at the edge (0.09 to 0.11). It detects a route switched off, as
  at 10 million (0.018 and 0.000), but not a route that is a minority
  carrier.
- **(c) Part A only**, the literal reading of the ruling. Toy passes
  everywhere; the "route round it" risk is then not checked.
- **(d) Change arm C (and arm M's stirred-in half) so the built route is the
  only route**, for example by not adding the acting signal to their trunk.
  That is a change to what the arms are, and would need its own toy retrain
  and check.

The code as committed implements (a), exactly as the method stated it before
any figure was seen. Changing the bar is one constant in `measure.py`
(`ROUTE_USE_MIN`) plus its stated reason.

## 6. Tests run, exactly

- `src/run_self_tests.sh`: **ALL SELF-TESTS PASS**, exit 0; seven files
  (grammar, models, transplant, measure, procedure, train_successor,
  tripwire), 237 checks passed, 0 failed (`out-sharpness-fix/tests/self-tests.txt`).
- Test T2 (`tests/load_toy_models.py`): **T2 PASSES**, exit 0; all twelve
  committed toy models load with no missing or extra weights and give
  bit-identical outputs and running states on 400 episodes.
- `tests/a2_run_cases.py`: 28 cases, 0 differ from expectation or leak.
- `tests/inuse_cases.py`: 14 checks, 0 differ from expectation.
- Not run: test T3 (the procedure on the twelve committed toy models, about
  half an hour, longer on a shared processor) and test T6 (the whole pipeline
  at 10 and 30 million). T3's committed-figure comparison now also meets the
  in-use check, which arms C and M fail; that is expected under (a).

## 7. Not done here

No rented machine, no spending, no rerun. The 11 remaining toy re-reads
(about an hour; `out-sharpness-fix/logs/run_reread.sh` runs them). The
independent check of this work.

*Corrected 2026-10-08 after the branch's independent check (`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`, its one must-fix item): the summary's ranges for route use now cover all six seeds, before and after the fix: arm C loses 22 to 29 per cent of its right own-directed answers (the earlier text said 24 to 29, omitting the before-fix 0.221 and 0.233), and arm M's stirred-in route 7 to 11 per cent (the earlier text said 9 to 11, omitting the before-fix 0.071). The direction of the claim is unchanged. Every figure in the tables reproduced in that check.*
