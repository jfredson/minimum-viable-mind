# The decoy test (page 10, finding A6): method, committed before any output

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `decoy-test-a6`, cut from the main line at `53ae82c`. **Committed
and pushed before the code it describes is run.** The commit that carries
this file and the code carries no output; the findings, with every command
and its output, are a later commit, and the commit order is the check that
this came first. Laptop only, on the processor. Nothing is rented, trained
or spent: $0.*

*Written under the workspace plain-language rule. What is tested is a
**constructed stand-in**: a committed toy model with extra numbers bolted on
by hand. It is not a trained model, and nothing it shows is a property of
any trained model.*

## 1. Why this test exists

John ruled page 10 of the Gate A addendum on 2026-10-06: "yes, run it, go
with the recommendation" (the addendum is
`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-questions-PROPOSAL.md` on
branch `gate-a-v4-tier2-dispositions`; the drafted test is in the A6 section
of `docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`
on the same branch). Page 12, whether the experiment is still worth running,
is to be decided with this test's checked result.

**The question** (the ChatGPT outside review of version 4, finding A6). The
measurement fits a straight-line read of "which marker word is mine" and
transplants only the directions that read uses. If a model also held an
easily read but **unused** copy of its marker, could the registered
nomination pick the copy? Then transplanting the chosen directions would
change nothing, the whole-state transplant (which carries both) would change
everything, and a model whose ownership answer is in fact separable would
read near 1, as if fully entangled.

**The test as ruled.** Take the separable toy model (arm T), add extra
coordinates holding an exact copy of the owner's marker that nothing
downstream reads, and run the registered nomination and reading unchanged.
Run it both ways round: the copy stronger (more easily read) than the
model's own ownership block, then weaker. Report both. Near 0 means the read
finds the slot that is used; near 1 means it can be fooled this simply.

## 2. How the decoy is built

**The models.** The three committed arm T toy models,
`experiments/rehearsal-successor-measure/out-repairs/models/ckpt_T_base_seed{0,1,2}.pt`,
the ones the controls re-run used (`docs/2026-10-03-controls-rerun.md`), each
checked against `SHA256SUMS` in that folder before use. Stop K1 below if one
does not match.

**Where the extra coordinates go.** Arm T's running state is 160 numbers:
136 of content, then a 24-number ownership block that no layer reads or
writes and that the action head reads to pick whose row of the table to
use. The decoy widens every running state to 184:

    [ content (136) | decoy (24) | ownership block (24) ]

at every running state (after the input embedding and after each of the four
blocks, so states 0 to 4) and at every position of the episode. So the decoy
sits at the same states and positions as the ownership block, and the
nomination rule's order (smallest layer set, earlier position set) cannot
exclude it.

**What the decoy holds.** Exactly `s` times the vector the model writes into
its ownership block at state 0: the owner's marker as the model computes it
from the acting channel (`_own_vec` in the frozen `models.py`). It is
recomputed from the episode's input at every running state. In a run with no
transplant the decoy equals `s` times the ownership block, number for number,
at every state and position.

**How "stronger" and "weaker" are set.** By the scale `s`, the same at every
state:

- **stronger: `s = 4`** (the copy's numbers four times the block's);
- **weaker: `s = 1/4`**.

Why scale is what decides it. The registered read is scikit-learn's
`LogisticRegression(C=1.0)` on the raw running state, with a penalty on the
squared size of its weights and no rescaling of the inputs. Two exact copies
of the same feature are equally readable in the sense of accuracy (both are
read perfectly), so the fit chooses between them by the penalty: the copy
with larger numbers needs smaller weights for the same effect, so it gets
more of the weight. At the fit's optimum the weight splits in the ratio of
the scales, so the copy carries `s²/(1+s²)` of the read's squared weight:
about 0.94 at `s = 4` and about 0.06 at `s = 1/4`. That is the sense in which
the copy is "more easily read" or "less easily read" by this read. An exact
tie, `s = 1`, is deliberately not run: there the fit's internal tie-breaking,
not ease of reading, would decide (as the check of the dispositions, pull
request 102, warned).

**Reported beside, not part of the verdict:** the same run at `s = 16` and
`s = 1/16`, to show whether the result moves with how lopsided the split is.

**How the decoy is guaranteed to be causally unused.** In the widened model
(`DecoyArmT` in the code below) the transplant hook runs on the 184-number
state, and then the decoy coordinates are thrown away: the next block and the
action head receive exactly the 136 content numbers and the 24-number
ownership block, as in the committed model. Whatever the hook writes into the
decoy is never read by anything. The decoy at the next state is recomputed
from the input, not carried.

**The checks that confirm it** (on the 800 fresh pairs, every seed, both
orientations, before any reading; stop K2 if (a), (b), (b') or (c) fails):

- **(a)** the widened model's outputs are bit-identical to the committed
  model's;
- **(b)** transplanting the donor twin's decoy coordinates alone, at every
  running state and every position, leaves every output bit-identical;
- **(b')** overwriting the decoy with large random numbers (standard
  deviation 100) at every state and position leaves every output
  bit-identical;
- **(c)** in a run with no transplant, the decoy equals `s` times the
  ownership block exactly, at every state and position;
- **(d)** reported: a straight-line read of the owner's marker from the decoy
  alone, and from the block alone, held-out correct of 180 at each state
  (expected 180, so the copy is easily read);
- **(e)** reported: at state 0, `action`, the share moved by the whole-state
  transplant, by the block alone and by the decoy alone, and the readings
  those give (expected: block alone gives 0, decoy alone gives about 1).

## 3. Which code runs the nomination and the reading, and why

**The frozen code**, `experiments/08-successor-degree/src/procedure.py`,
function `run_model`, with `grammar.py`, `measure.py`, `models.py` and
`transplant.py` beside it, at main `53ae82c`, **not changed**. Why that and
not the rehearsal's `rerun_controls.py`: the frozen code is what the
registration will name by commit, so it is the procedure whose foolability
page 12 is about; and its test T3a reproduced the rehearsal's committed toy
figures to the printed precision, so the two agree on these models
(`docs/2026-10-04-successor-code-freeze.md`).

**What is substituted, and only that:** `procedure.load_model`, the function
that loads a model file, is replaced for the length of each call so that it
returns the widened model. Everything after it is the frozen code: the gate;
the one fit of the reads on the 600 development episodes (the last 180 held
out), written to disk and reloaded; the full family of 45 site sets at
sizes 1, 2, 4 and 8; the pick rule with the piece floor of 144 of 180; the
reading on the 800 fresh pairs; controls 1, 3, 4, 6 and 7; the stricter and
sensitivity rows; the rider; the 200-shuffle null; and `summarise`, whose
`measure.withhold` decides whether each seed has a reading or "no verdict".
The reads are fitted fresh on the widened model, never taken from a file.

**One thing the frozen code does not yet carry.** John's ruling of page 4
(2026-10-06) moves the fit to 1,800 development episodes. The frozen code
still fits on 600, and is run as frozen. Said here so no one reads this as
the page-4 procedure.

**What the code adds, outside the frozen procedure, for reporting only:**
where the chosen piece lies (the share of its squared size in the decoy, in
the block and in the content coordinates), and the share of the fitted
read's squared weight in each, at every state. It changes nothing the frozen
code computes.

The code is `experiments/rehearsal-successor-measure/src/decoy_test.py`,
committed with this note. Output goes only to
`experiments/rehearsal-successor-measure/out-decoy-test/`, a new folder.

## 4. Seeds, sets and settings

- Models: arm T seeds 0, 1 and 2, all three.
- Evaluation sets: the frozen `grammar.EVAL_SETS`, unchanged (development
  600 pairs, seed 4242; fresh 800, seed 777; relaxed 800, seed 778; gate
  1,500 pairs, seed 99).
- Shuffles for the null: the registered 200.
- Processor threads: 4 (another session is measuring on the laptop),
  recorded in every row. torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0,
  scipy 1.18.0, Python 3.12, from the main checkout's environment, as pinned
  in `experiments/08-successor-degree/requirements-measure.txt`.

## 5. Commands

From `experiments/rehearsal-successor-measure/src/`, with the main
checkout's `.venv` Python:

    python decoy_test.py --checks-only
    python decoy_test.py --scale 4
    python decoy_test.py --scale 0.25
    python decoy_test.py --scale 16
    python decoy_test.py --scale 0.0625
    python decoy_test.py --report

Each `--scale` run also writes its own checks file and stops at K2 before
any reading if a check fails. Each takes roughly a quarter of an hour
(three models at about four minutes each, judged from the freeze's test
T3b), so nothing approaches the 90-minute limit; they run one after another
in the background.

## 6. What counts as fooled, not fooled and inconclusive

Per seed, the figure is the frozen procedure's reading for arm T after
`summarise` (a number, or "no verdict" with its reasons). Per orientation
(`s = 4`, then `s = 1/4`), from its three seeds:

- **Not fooled:** at least two seeds return a reading, and every seed that
  returns one reads **0.20 or less**.
- **Fooled:** at least two seeds read **0.50 or more**, and on each of them
  the chosen piece lies **more than half** in the decoy (by squared size).
  0.50 is chosen because a reading that high on arm T would by itself stop
  arm C (which reads about 1 on the toy) clearing the registered separation
  of 0.5. Readings of 0.80 or more are called "fully fooled" in the findings.
- **Inconclusive:** anything else. That includes readings between 0.20 and
  0.50; seeds split across the bands; fewer than two seeds with a reading
  (a "no verdict" on a separable model is itself a failure of a different
  kind and is reported as one); and two or more seeds reading 0.50 or more
  with the piece *not* mostly in the decoy (the read failing on the
  separable model for some other reason).

**Overall:** fooled if either orientation is fooled; not fooled if both are
not fooled; otherwise inconclusive. The supplementary scales (16 and 1/16)
are reported beside and do not enter the verdict.

**Ties.** In the nomination, the frozen rule's own order decides, unchanged:
highest ownership-only share on development episodes, then the smaller
size, then the earlier position set. A reading exactly on a band edge counts
as inside the band (0.20 is "near 0"; 0.50 is "fooled" if the piece
condition holds). The exact tie between copy and block in the fit is avoided
by design (section 2).

## 7. What this session expects, said before running

**ARGUED, not measured.** Because the copy is an exact copy (a fixed multiple
of the block), the fit's directions, at its optimum, run along "block and
copy together" in the ratio of the scales. Transplanting along such a
direction moves the decoy part and the block part together, and the block
part is moved by exactly as much as a read of the block alone would move it.
So this session expects **a reading of about 0 at every scale**, with the
chosen piece lying mostly in the decoy at `s = 4` (about 0.94 of it) and
mostly in the block at `s = 1/4`. Departures would come from the fit
stopping short of its optimum, from content coordinates that also carry the
marker, or from the cut to 1, 2, 4 or 8 directions.

**What that would and would not show, said now so the result is not
over-read.** A reading of 0 here would show that the registered read is not
fooled by an exact, scaled copy of the used slot. It would **not** show that
the read cannot be fooled by an unused representation coded *differently*
from the one the action uses (a different arrangement, or not a straight-line
function of it), which is the general form of A6; this test, as ruled, does
not probe that.

## 8. Stops

| Stop | What happens |
|---|---|
| K1, a model file does not match `SHA256SUMS` | stop, report, run nothing on it |
| K2, check (a), (b), (b') or (c) fails | stop before any reading, report |
| K3, the frozen procedure raises an error | stop, report the error; the code is not changed and re-run without a new committed note saying why |

## 9. After the run

A findings note, `docs/2026-10-06-decoy-test.md`, with both orientations and
every seed, labelled as a constructed stand-in, saying what it does and does
not show for page 12. A pull request, not merged, owed a check by another
session that re-runs `decoy_test.py` from this commit.
