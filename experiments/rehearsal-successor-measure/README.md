# The successor experiment's measurement rehearsal — code

**UNREGISTERED. This is a rehearsal directory, not an experiment directory.**
Nothing in it is registered, nothing in it may be cited as a result about the
scientific question, and no number it produces is a bar for anything.

It exists because the outside-review protocol
(`docs/outside-review-protocol.md`, amended by pull request 13 and ruled on
2026-09-21) makes a complete measurement rehearsal a hard precondition for any
registration review. This is that rehearsal for the successor experiment
proposed in `docs/successor-experiment-proposal-2026-09-21.md`.

## What was committed when

The discipline the programme runs on is **method before output**. In commit
order:

1. `docs/successor-measure-rehearsal-method-2026-09-21.md` — what would be
   built, what each check would show, and passing, failing and no-verdict for
   every one of them, written down while nobody knew which would fire.
2. `docs/successor-measure-rehearsal-method-addendum-denominator-2026-09-21.md`
   — four further checks, added after a review returned two findings marked
   fatal in the measure itself, and again committed before their code.
3. This code.
4. `docs/2026-09-21-successor-measure-rehearsal.md` — the findings, with every
   command and its output.

## The files

| file | what it is |
|---|---|
| `src/grammar.py` | the matched-role revision episode generator, shrunk, with the matched-difficulty checks, the even-split rule and the one-scored-token check |
| `src/arms.py` | the three architectures: the ownership answer kept separable, entangled, and free |
| `src/transplant.py` | the transplanting code and its known-answer tests, including the proof that the ownership-only transplant is the whole-state one restricted to a subspace |
| `src/measure.py` | the reading, its no-verdict rule, and the candidate floor-corrected form beside it |
| `src/training.py` | toy training and scoring, and the competing solvers |
| `src/rehearse.py` | the driver: train, gate, nominate, transplant, outcomes, throughput |
| `src/denominator.py` | the four checks that answer the two findings the review marked fatal |
| `src/bench_arms.py` | seconds per step per architecture, on whatever machine it runs on |
| `src/stage_rented_slice.sh` | stages the one short slice of rented time — and cannot run it |
| `out/` | checkpoints and results; nothing is overwritten across stages |
| `src/repairs.py` | the 2026-09-25 repairs driver: the ruled nomination rule (one label, 176 comparisons), the chance-corrected reading, control 2 as the proposal states it, the rider; method in `docs/rehearsal-repairs-method-2026-09-25.md`, findings in `docs/2026-09-26-rehearsal-repairs.md` |
| `src/arm_middle.py` | arm M, the fourth arm, built to be partly separable (a mixture by item) |
| `src/diagnose_named_other.py` | an exploratory, not pre-stated, classification of the free arm's named-other answers |
| `out-repairs/` | the repairs' outputs; `out/` is left as the 2026-09-21 record |

## Running it

```
cd src
../../../.venv/bin/python grammar.py     --self-test
../../../.venv/bin/python arms.py        --self-test
../../../.venv/bin/python transplant.py  --self-test
../../../.venv/bin/python measure.py     --self-test
../../../.venv/bin/python rehearse.py    --stage all
../../../.venv/bin/python denominator.py --stage all
sh stage_rented_slice.sh
```

Everything above is local, toy scale, and costs nothing. `stage_rented_slice.sh`
prints a plan and writes it to a file; it contains no command that creates a
rented machine.
