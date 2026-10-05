# Freezing the successor's code: method, written before any test runs (2026-10-04)

*Written 2026-10-04 (Pacific) by a Claude Code session, before the code it
describes was run. Laptop only, nothing rented, $0. Nothing here is a ruling.
Every choice below that no ruling makes is marked **(this session's call)** and
listed again in section 6 so it can be ruled on.*

*Written under the workspace plain-language rule.*

## 1. What this is for

Step 3 of section 11 of the successor proposal, version 4
(`docs/successor-experiment-proposal-2026-10-03-v4.md`), is: implementation
frozen; unit tests; the even-split rule and the one-scored-token self-test run
on the built generator; a training entry point for the constructed models on
the rented machine; and the spending tripwire written into the launch
preconditions. Step 4, the four development runs at the 10-million size, needs
all of that, and John's go naming them.

John ruled on 2026-10-04 that no step waits for a date, only for what it needs.
This step waits on no ruling. It does not register anything: the registration
text, its review and its commit are separate steps, and what is frozen here is
what the registration text will name by commit.

## 2. What is built, and where

A new experiment folder, `experiments/08-successor-degree/` **(this session's
call: the name; version 4 section 12.2 says only `experiments/08-…`)**. The
compute ledger stays in experiment 06's folder, as ruled (decision 8 of
2026-10-03). Code in `src/`:

| File | What it is | Built from |
|---|---|---|
| `grammar.py` | the episode generator for the matched-role task, the evaluation sets, the streamed training data | `experiments/rehearsal-successor-measure/src/grammar.py`, with the episode code copied unchanged |
| `models.py` | the four models (T, C, M, F) at three sizes: the toy's, 10 million and the registered 30 million | `arms.py` and `arm_middle.py` from the same folder, unchanged in what they compute |
| `transplant.py` | the transplanting code and its known-answer tests | `transplant.py` from the same folder |
| `measure.py` | the reading, its no-verdict rules, the withholding of a reading, the two-of-three rule and the separation | `measure.py`, `repairs.py` and the 2026-10-03 rulings |
| `procedure.py` | the whole measurement procedure for one trained model, and for an arm's three seeds | `rerun_controls.py`, `control2_twenty_draws.py`, `short_prestated_run.py` and `rerun_v3.py` |
| `train_successor.py` | the training entry point on the rented machine, all four arms | the toy loop in `training.py`, with the run-file conventions of `train_a3.py` |
| `tripwire.py` | the spending tripwire of section 12.5 | new |
| `launch_successor.sh` | the launcher for one run | derived from `experiments/06-…/src/launch_a3_fetch_first.sh`, the launcher version 4 names |
| `run_self_tests.sh` | every self-test, in one command | new |
| `../requirements-measure.txt` | the pinned library versions the registered fit is computed with | the laptop's environment |

The rehearsal folder is left exactly as it is.

## 3. What the training recipe is, and what is not settled

Version 4 says the arms train "on the same token budget" as the closed design
and that "the training recipe is the rehearsal's unchanged recipe". Those two
sentences do not fix a recipe at full size: the rehearsal trained for 2,500
steps of 96 episodes on a fixed set of 12,000 matched pairs, while the closed
design's token budget is 585,544,960 tokens. So the trainer takes every recipe
number as an argument, writes the numbers it used into its output, and has
these defaults **(this session's call; the registration text must fix them)**:

- the rehearsal's optimiser and schedule, unchanged: AdamW at a learning rate
  of 0.002 with weight decay 0.01, a one-cycle schedule with a tenth of the
  steps warming up, gradients clipped at 1.0;
- 96 episodes a step, 48 matched pairs, so the even-split rule holds;
- the closed design's token budget, 585,544,960 tokens, which at 56 tokens an
  episode is 108,919 steps;
- training episodes generated fresh at every step from the training pool,
  seeded by the run's seed and the step, rather than drawn from a fixed set of
  12,000 pairs. At that budget a fixed set would be shown to the model about
  430 times over. Any episode whose content matches one in the development,
  fresh, relaxed, gate or trajectory sets is skipped, so the three sets of
  section 7.1 are disjoint by construction and not only by chance, and the
  count skipped is written to the log.

The development runs use these same defaults at the 10-million size, so that
what they test is the registered loop and not a shortened one.

## 4. The tests, and what passing looks like

Each is written down here before it runs.

**T1. Self-tests, every file.** `run_self_tests.sh` runs each module's
self-test. Passing: every check prints PASS and the script exits 0. Among
them, the two carried-over rules on the built generator:

- *the even-split rule* (ledger item RT-58): the trainer refuses a batch size
  that is odd, and every streamed batch holds whole matched pairs;
- *the one-scored-token check* (ledger item RT-59): exactly two positions per
  episode are scored, each holds the mask word and never the answer, the
  answer token appears nowhere in the input, and the loss the models actually
  compute equals the cross-entropy over exactly those positions and no others,
  checked on the models' own loss function and not on a copy of it.

**T2. The frozen code is the rehearsal's code.** The twelve committed toy
models (`experiments/rehearsal-successor-measure/out-repairs/models/`, checked
against its `SHA256SUMS`) are loaded into `models.py` at the toy size.
Passing: every model loads with no missing or extra weights, and its outputs
on 400 episodes are bit-identical to the rehearsal's `arms.py` or
`arm_middle.py` on the same weights. The generator's episodes for the toy's
seeds are identical, array for array, to the rehearsal generator's.

**T3. The frozen procedure reproduces the committed toy figures.** The
procedure is run on the twelve committed toy models on the laptop's processor,
in two ways:

- *(a) with the straight-line reads taken from the committed files* the
  controls re-run used. Passing: for every arm and seed, the nomination
  status, site set and size of piece, the whole read's and piece's counts at
  the action position, the whole-state, ownership-only and no-transplant
  shares, the reading, controls 1, 3, 6 and 7, control 4 as redefined, the
  true-slot reading on arms T and M, and the separation equal the committed
  values in `out-controls-rerun/` and `out-short-prestated-run/` to the
  printed precision; control 2 on arm F equals `out-control-2-twenty-draws/`
  with the floor switched off the same way. A difference fails T3 and is
  reported, not repaired by changing what the procedure computes;
- *(b) with the reads fitted fresh, once, on the processor*, which is how the
  registered run works. No pass line: the differences from (a) are reported.
  The controls re-run's directions came from an earlier fit on the graphics
  chip (the check at `e184a6e`, section 4, item 2), so small differences are
  expected and are what (b) is for.

**T4. The site-set rule at three depths.** Passing: 45 site sets on the toy
(5 running states), 325 on the registered model (13), and the stricter variant
40 and 312, as version 4 sections 7.2 and 18 print; the 10-million model (9
running states) gets whatever the rule produces, printed.

**T5. The new rules, on cases built to break them.** The withholding of a
reading (a failed control 7, control 1 on arm T, control 4, a no-transplant
miss outside 0.018, or the floor missed on fresh episodes each replaces the
reading with "no verdict" and its reason), the two-of-three rule, the
separation as arm C's lowest reading minus arm T's highest, the outcome map
(arm C no verdict gives the two-arm fallback; arm M no verdict drops arm M;
arm F no verdict after the anchors separate gives "metric validated, degree
not read"), and the tripwire's arithmetic (ratio A, ratio B, a reading at
1.25 trips, a check that cannot run trips, the in-flight clause). Passing:
each case lands where it is written down in the test before it runs.

**T6. The full pipeline at the 10-million size and at the registered size,
untrained.** On the laptop, each of the four arms is built at 10 million and
30 million, trained for a handful of steps by `train_successor.py` exactly as
the rented machine would run it, and the whole procedure is run on the result
at a reduced episode count. Passing: every stage finishes and writes its file;
untrained models are expected to return "no verdict", and that is what a pass
looks like here. Nothing about learning is read.

**T7. The launcher, without creating anything.** `DRYRUN=1` prints the plan
for one development run and creates nothing; the argument guard check
(`check_launcher_argument_guard.sh`, pointed at the new launcher) and the
remote-start check (`check_remote_forms.py`) pass on it; the tripwire refuses a
launch when its halt file is present or when the balance cannot be read.

## 5. What this does not do

It rents nothing, contacts no vendor except for reading the account's balance
and machine list if the tripwire test needs a real reading, and spends
nothing. It does not launch the development runs: their go packet and ledger
rows are prepared with estimates, and John's own words naming them are what
launches them. It does not write the registration text. It edits no
registered file and nothing in the rehearsal folder.

## 6. Choices this session made that no ruling made

1. The folder name, `experiments/08-successor-degree/`.
2. The full-size recipe of section 3: the token budget, a fresh stream of
   training episodes rather than a fixed set, and the rehearsal's optimiser
   settings carried to 30 million parameters unchanged.
3. The widths of arm T's slot (24) and lookup entries (64) kept at every size,
   as the rented slice timed them.
4. The seeds of the evaluation sets, carried from the toy: development 4242,
   fresh 777, relaxed 778, gate 99, and the two swaps 4243 and 781; plus a new
   trajectory set (seed 31337, 200 pairs) watched during training only.
5. The sampling band printed beside every count against the floor: the
   95 per cent Wilson interval around the observed count, and beside it the
   range a piece whose true accuracy is exactly four fifths lands in 95 times
   in 100.
6. How the tripwire reads the vendor: ratio B from `runpodctl user`
   (`clientBalance`, read twice an hour apart) and the machine list; ratio A
   from `runpodctl billing`. What it does on a trip: writes a halt file the
   launcher refuses to run past, writes the ledger figures to a file for the
   row, and deletes an in-flight machine only when the in-flight clause's
   arithmetic says it must.
