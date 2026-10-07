# Method: fixing the ownership sharpness at 4.0 in the built models, and failing a built model whose ownership route has gone flat

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `fix-sharpness-inuse-check`, cut from `origin/main` after the
decision code (pull request 105) was merged. **Committed before any code is
changed and before any model is retrained or measured.** Every expected
outcome below is written now; a result that lands elsewhere is a finding and
is reported as one, and this note is not edited afterwards. Laptop only,
nothing rented: $0.*

## What John ruled

On 2026-10-06 John ruled on the packet about the two built models that lost
their ownership route (pull request 109, branch `ruling-packet-cm-flat`,
`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`, checked in pull
request 112): **option 1(b) plus option 4.**

- **Option 1(b):** the number that sets how decisive the built-in "which
  agent am I" answer is (the *sharpness*) is fixed at 4.0, not learned, in
  all three built models: arm T (ownership kept in one swappable slot), arm C
  (ownership stirred into everything) and arm M (half and half, by item).
- **Option 4:** a check, run on every trained model, that fails a built
  model whose ownership route has gone flat. A built model that fails it gets
  "no verdict" for that seed, recorded as "construction did not hold".

The three reruns at the 10-million-parameter size are approved but run only
after this code change and its independent check pass. They are not part of
this work.

Background (the check of the development runs, pull request 106, sections 6
and 7): in the 10-million-parameter development runs the sharpness fell from
4.0 to −0.09 in arm C and −0.01 in arm M, so their built-in answer put about
a quarter on each of the four agents and carried nothing; arm T fell to
1.95 and still worked. On the small laptop ("toy") models arm C had already
drifted to 1.73, 0.70 and 0.93 on its three seeds.

## 1. What changes in the frozen model code (`experiments/08-successor-degree/src/models.py`)

The sharpness is `own_sharpness`, created as a learned number
(`nn.Parameter(torch.tensor(4.0))`) in both model classes.

- **In arms T, C and M it becomes a fixed stored value** (a PyTorch
  "buffer": saved with the model, never seen by the optimiser, so neither
  training nor weight decay can move it), set to 4.0.
- **Arm F (the freely trained model) is left as it is.** It computes the
  answer and never uses it, so its sharpness never receives a training
  signal and stays at 4.0 anyway (arm F's 10-million run ended at exactly
  4.000). Leaving it alone keeps the free model's code and parameter count
  untouched. The ruling names the three built arms only.
- **The name stays `own_sharpness`**, so every saved model still loads with
  no missing or extra entries. A model saved before this change loads with
  the value it learned (for example 1.73 for toy arm C seed 0), so old models
  are re-read exactly as they were; the in-use check below is what flags them.
- The built models each lose one learned number (the parameter count of T,
  C and M drops by one). Nothing else changes in what any model computes.
- **No change to the training code** (`train_successor.py`): it hands the
  optimiser `model.parameters()`, which no longer includes the sharpness in
  the built arms. This avoids the other open change to the training code
  (branch `training-exclusion-pairing`, which changes what training leaves
  out), so no overlapping edit there.

New self-tests in `models.py`: in arms T, C and M the sharpness is not among
the learned numbers, is 4.0, and is still exactly 4.0 after an optimiser step
with weight decay on a real loss; in arm F it is still a learned number; and
a saved model's sharpness value round-trips through save and load.

## 2. The in-use check: how it decides "flat"

**Where it lives.** It is computed in `procedure.gate` on the same 3,000
gate episodes as the learning gate, written into each row as
`gate.route_in_use`, and judged in `measure.withhold` as one more check that
withholds a reading (the decision code merged from pull request 105 lists
every check and every reason). It is not a learning condition: a built model
that fails it learned, but not through the route it was built to use. So it
never produces "substrate not a testbed" (R3); it produces no verdict for
that seed, and the decision code's own rules then say what that means for
the arm (two seeds of three must count): arm T with no verdict gives
"metric not validated"; arm C with no verdict gives the fallback to the
separable model only; arm M with no verdict is dropped. Arm F is not judged
(it has no built route); its figures are recorded as a reference.

**What it measures, per built model and seed, two parts. Both must pass.**

*Part A, the answer is decisive.* At the own-directed action of each gate
episode, the weight the built-in answer puts on the agent the model actually
is (the agent on whose turns the "this turn is yours" signal fired). Mean
over the 3,000 episodes. **Passes at 0.9 or above.**

Why 0.9: every gate episode has the signal firing twice before the action,
so with the sharpness at 4.0 every episode gives e^8 / (e^8 + 3) = 0.999. A
flat answer gives 0.25. The mean falls below 0.9 only if the sharpness falls
below about 1.65, that is, loses more than half its value. With the
sharpness fixed this part can fail only if the fix is undone or an old model
is read; it is a guard, and states the literal meaning of "flat". It is set
well below what a fixed model gives so that it never fires on noise.

*Part B, the network actually uses the answer.* The risk the packet names is
that the network routes round a fixed sharpness by shrinking the layers that
apply the answer (arm C's scale-and-shift and binding, arm T's row reader).
Part B swaps the answer: each gate episode is run again with the built-in
answer pointing at a different agent (every agent label in the tally moved
on by one, so the answer names the next agent round; the text, the acting
signal and everything else are unchanged). On the own-directed actions that
go through the built route and that the model got right with the true
answer, it counts how many it no longer gets right:

    route use = (right with the true answer − right with the swapped answer)
                / right with the true answer

1.0 means every right answer depended on the built answer; 0 means none did.
**Passes at 0.5 or above.**

Why 0.5: it is the midpoint between "the built route decides every right
answer" (what the construction claims) and "it decides none" (what the
10-million arms C and M showed: forcing the right row changed nothing). Below
it, most of the model's right answers come from somewhere other than the
route it was built around, so the arm is not the built model the
measurement relies on. It is a judgement, stated here before any figure is
seen, and John may set it elsewhere; the figure itself is always recorded.

Which actions count as "the built route": arm T, every own-directed action
(its head reads only the ownership slot); arm C, every own-directed action;
**arm M, its two routes separately** (actions about items it1 to it3, the
stirred-in route; it0 and it4, the separable route), and **both must pass**,
since arm M is built to have both and the 10-million arm M lost its
separable half.

If the model got no own-directed action right on a route, part B "could not
be evaluated", which counts as failing (stop S8: a check that cannot run
counts against). A row with no `route_in_use` field on a built arm is "not
run", which also withholds, as for every other check in the decision code.

The reason written for a failure names the part, the route and the figure,
for example "the built ownership route has gone flat (construction did not
hold): route use 0.03 on the separable route, bar 0.5".

## 3. Made-up cases and their expected outcomes

Run by a new test script, `tests/inuse_cases.py`, on the committed toy
models (checked by SHA-256 first) with named weights changed, and on the real
10-million development checkpoints already on the laptop. Expected outcomes,
written now:

| # | Case | Expected |
|---|---|---|
| 1 | Committed toy arm T seed 0, unchanged (learned sharpness 3.88) | passes both parts |
| 2 | Same, sharpness set to 0 (flat) | fails part A (0.25); part B fails too |
| 3 | Same, sharpness set to −0.09 (the 10-million arm C value) | fails part A |
| 4 | Committed toy arm C seed 0, sharpness set to 4.0, the scale-and-shift and binding layers zeroed (the "route round it" case) | passes part A (0.999), fails part B (route use 0) |
| 5 | Committed toy arm T seed 0, the slot reader zeroed (the row choice no longer depends on the slot) | passes part A, fails part B |
| 6 | Committed toy arm M seed 0, sharpness 4.0, separable slot reader zeroed only | fails, naming the separable route; the stirred-in route passes |
| 7 | Committed toy arm M seed 0, sharpness 4.0, scale-and-shift and binding zeroed only | fails, naming the stirred-in route; the separable route passes |
| 8 | Committed toy arm C seeds 1 and 2, unchanged (learned 0.70, 0.93) | fail part A (weights 0.57 and 0.68) |
| 9 | Committed toy arm F seed 0 | not judged; route use about 0 recorded |
| 10 | Real 10-million arm C | fails part A (about 0.22) and part B |
| 11 | Real 10-million arm M | fails part A (about 0.25); fails part B on the separable route |
| 12 | Real 10-million arm T | passes part A (0.94); part B expected to pass |
| 13 | A model that gets no own-directed action right (untrained toy arm C, sharpness 4.0) | part B could not be evaluated: fails |

Decision-code cases, in `measure.py`'s self-test and in the end-to-end
case runner of pull request 105 (`tests/a2_run_cases.py`):

| # | Case | Expected |
|---|---|---|
| 14 | A clean arm C row with a passing `route_in_use` | reads |
| 15 | Same, part B failing | no verdict, reason names "construction did not hold" |
| 16 | Arm T/C/M row with no `route_in_use` | no verdict, "the built-route check was not run" |
| 17 | Arm F row with no `route_in_use` | unaffected |
| 18 | End to end: every arm reads (case 4 of pull request 105, which gives R1) but arm C fails the in-use check on seeds 0 and 1 | "metric checked against the separable model only, degree read" |
| 19 | End to end: arm T fails the in-use check on seeds 0 and 1 | "metric not validated" |
| 20 | End to end: arm M fails on seeds 0 and 1 | R1, arm M has no verdict |

The 25 existing cases of pull request 105 are run from the toy's committed
rows, which predate this check and so have no `route_in_use` field. Under
the decision code's rules those rows would now be "not run" on arms T, C
and M and withhold everything. **The case runner will give every committed
built-arm row a passing `route_in_use` before applying a case's changes**,
so the 25 cases keep testing what they tested, and each must land where it
did before. That is stated here so it is not mistaken for a quiet change.

## 4. The toy retrain and re-read

**Retrain.** Arms T, C and M, seeds 0, 1 and 2 (nine models), at the toy
size, with the exact recipe that made the committed toy models
(`experiments/rehearsal-successor-measure/src/repairs.py`: 2,500 steps,
batch 256, learning rate 0.003, 15,000 training pairs from seed 1000 plus the
seed, AdamW with weight decay 0.01, one-cycle schedule, gradients clipped at
1.0), through the rehearsal's `training.train_arm` with the model built by
the changed `models.py`. The only difference from the committed toy models is
the fixed sharpness. Arm F is not retrained (its code is unchanged); its
committed models are re-read alongside. On the laptop's graphics processor,
three at a time (a 60-step timing: about 0.54 seconds a step each with three
running), so about 70 to 90 minutes; the re-reads run on the processor beside
it. Estimated total under two hours; if it runs over, the session stops and
reports.

**Re-read.** Every model through the registered procedure
(`procedure.py model`, the reads fitted fresh on the processor, the
registered episode counts, 200 shuffles), then `procedure.py summarise`.
Compared against the committed toy figures (the fresh-fit run of the code
freeze, `out-freeze-tests/t3b-fresh-fit/`).

**What would be a concern** (each reported if seen):

1. Any retrained built seed fails its learning gate, or its own-directed
   count falls more than 150 of 3,000 below the committed seed's: fixing the
   number would be costing learning.
2. Any retrained built seed fails the in-use check: the network routes round
   the fixed answer even at the toy size, which is the risk option 1 named.
3. The readings move: arm T above 0.2, arm C below 0.8, or arm M outside 0.3
   to 0.7 or more than 0.10 from its true-slot reading, on any seed; or any
   built seed fails to nominate a site set or loses a control. The
   measurement's built ends would then be less clean with the fix than
   without it.
4. The outcome on the toy changes for any reason other than the arms
   T, C and M rows (the toy's outcome was "substrate not a testbed" because
   arm F fails its gate; that should not change).

Expected: none of these; arm C's weight on the true agent goes from 0.91,
0.57 and 0.68 to 0.999 on every seed, and all nine built seeds pass the
in-use check.

## 5. Tests

`src/run_self_tests.sh` (every self-test), the freeze's test T2 (the
committed toy models load into the changed code bit for bit), the new case
script, and the decision code's case runner. Results reported exactly.

## What this does not do

No rented machine, no spending, no rerun at the 10-million size. It does not
touch the spending-alarm code (page 2 of the packet), the training code, or
the generator.
