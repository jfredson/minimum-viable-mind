# Experiment 08: the successor experiment, reading the degree

**FROZEN CODE, NOT YET REGISTERED.** The code in `src/` was frozen on
2026-10-04 under `docs/successor-code-freeze-method-2026-10-04.md` and tested
as that note says; the findings are `docs/2026-10-04-successor-code-freeze.md`.
The registration text, which will name this code by commit, does not exist
yet. Nothing in this folder is a result about the scientific question.

**One change since the freeze (2026-10-06, ruled by John):** the training
stream in `src/grammar.py` now also leaves out every episode whose pairing
(which marker holds which value on which item) is that of a fresh or relaxed
episode, so no such pairing can reach training. Method and expected results:
`docs/2026-10-06-successor-training-exclusion-pairing-method.md`. The four
10-million development runs predate it and stay development evidence only.

What the experiment is: `docs/successor-experiment-proposal-2026-10-03-v4.md`.
In one sentence: four small language models, two built so that how much their
action depends on "who am I" is known (arm T separable, arm C entangled), one
built half and half by item (arm M), and one trained freely (arm F), are put
through one measurement, a transplant of the state between twin episodes that
differ only in which agent the model is; if the measurement separates the two
built models, it is used to read the free one.

The compute ledger is not here. It stays in experiment 06's folder as the
programme's one record of money (ruled 2026-10-03, decision 8):
`../06-mvm-0a-constructed-self-index/compute-ledger.md`.

## The files

| File | What it is |
|---|---|
| `src/grammar.py` | the episode generator, the evaluation sets and their seeds, the streamed training data (which leaves out every evaluation episode, and every fresh or relaxed pairing whatever its turn order), the even-split rule and the one-scored-token check |
| `src/models.py` | the four arms at three sizes (`toy`, `10M`, `30M`; 30M is the registered size) |
| `src/transplant.py` | the transplanting code and its known-answer tests |
| `src/measure.py` | the reading, its no-verdict rules, the withholding of a reading, two of three, the separation and the outcome terms |
| `src/procedure.py` | the whole measurement for one trained model (`model`), and the outcome from all of them (`summarise`) |
| `src/train_successor.py` | the trainer, on the rented machine or the laptop |
| `src/tripwire.py` | the spending tripwire of section 12.5 |
| `src/launch_successor.sh` | the launcher for one run; refuses to create anything without its settings, the ledger row, a passing tripwire and the launch gate |
| `src/run_self_tests.sh` | every self-test in one command |
| `requirements-measure.txt` | the pinned library versions the registered fit is computed with |
| `tests/` | the freeze's tests T2, T3, T6 and T7 |
| `out-freeze-tests/` | what those tests printed and wrote |

## Running it

```
src/run_self_tests.sh                                  # every self-test, about two minutes
python tests/load_toy_models.py                        # T2
python tests/reproduce_toy.py --mode committed-reads --out DIR   # T3a, about half an hour
tests/pipeline.sh DIR "10M 30M"                        # T6
tests/check_launcher.sh                                # T7, creates nothing
```

A training run on a rented machine is launched only by `src/launch_successor.sh`,
only on John's go naming it, quoted in its ledger row before the machine
exists. The go packet for the four development runs is
`docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md`.

Measuring a trained model, on the laptop's processor:

```
python src/procedure.py model --ckpt artifacts/<run>/<run>.pt --seed 0 --out DIR
python src/procedure.py summarise --dir DIR
```

## Change after the freeze: the ownership sharpness and the in-use check (2026-10-06, ruled by John)

In arms T, C and M the number that sets how decisive the built-in "which
agent am I" answer is (the sharpness) is now fixed at 4.0, not learned
(`src/models.py`); arm F is unchanged. And a check fails a built model whose
ownership route has gone flat (`procedure.route_in_use`, judged in
`measure.route_check` and `measure.withhold`): such a seed gets no verdict,
recorded as "construction did not hold". Method:
`docs/2026-10-06-sharpness-fix-inuse-check-method.md`. Tests:
`tests/inuse_cases.py` (made-up cases on real models), the decision-code case
runner `tests/a2_run_cases.py` (cases 26 to 28), and the toy retrain
`tests/retrain_toy_fixed.py`; outputs in `out-sharpness-fix/`.
