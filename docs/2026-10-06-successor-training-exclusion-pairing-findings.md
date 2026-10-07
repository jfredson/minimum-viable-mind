# Findings: training leaves out fresh and relaxed pairings outright (2026-10-06)

*Written 2026-10-06 (Pacific) by the Claude Code session that made the change.
Laptop only; nothing trained beyond the existing short self-test and pipeline
runs; nothing rented; $0. Method, committed before any code changed or ran:
`docs/2026-10-06-successor-training-exclusion-pairing-method.md`. Written
under the workspace plain-language rule. Owed: a check by a session that did
not write this.*

## 1. In short

- **The training stream can no longer yield a fresh or relaxed pairing.**
  `TrainingStream.admits` in `experiments/08-successor-degree/src/grammar.py`
  refuses any episode whose table of (marker, item, value) triples is that of a
  fresh or relaxed episode, whatever its turn order, named agent, asked-about
  items, action order or listing order. Every episode the stream yields passes
  through it. The old whole-content rule stays, for every evaluation set.
- **Every new check passed on its first run, and the three made-up cases landed
  exactly as written in advance** (section 3).
- **The full self-test suite of the frozen code passes: 202 checks, none
  failed, none skipped** (195 before, plus 7 new ones). Both pinned digests are
  unchanged, so seed 0's first training batch is the same as before.
- **The development runs most likely saw no fresh pairing.** Replaying the old
  stream for seed 0 over its 108,919 steps (5,228,112 contents) finds none, in
  line with the 0.3 expected beforehand.

## 2. What changed

| File | Change |
|---|---|
| `src/grammar.py` | new `pairing()`, `held_out_pairings()` and `PAIRING_EXCLUDED_SETS`; `TrainingStream` gains `excluded_pairings` and `admits()`, and `pairs_for_step` calls `admits`; seven new self-test checks (G1 to G4); the opening description says so |
| `src/train_successor.py` | its description, and the data line written into each run's recipe, mention the pairing exclusion |
| `README.md` | a note of this change since the freeze, and the generator's row in the file table |

## 3. Results

| Check | Result |
|---|---|
| G1: the pairing list is exactly the fresh and relaxed pairings | PASS: 1,600 episodes, 1,600 distinct pairings |
| G2: the function refuses each of them and 48 re-listings of each, with everything but the table drawn again | PASS: 78,400 of 78,400 refused |
| G3: a training pairing planted only in the pairing list is skipped | PASS: skipped once, never yielded |
| G3: planting a same-table copy with a different turn order and listing makes training skip the original | PASS |
| G4, case A (a fresh table re-dressed) | old rule lets it through, new rule blocks it, as expected |
| G4, case B (a relaxed table re-dressed) | old rule lets it through, new rule blocks it, as expected |
| G4, case C (case A with two values swapped) | both rules let it through, as expected |

Two deliberately broken copies of the code, run in a scratch folder and not
committed, show the checks can fail: with the pairing rule removed from
`admits`, G2, both G3 checks and cases A and B fail (G2 refuses only 1,600 of
78,400, the originals themselves); with `pairs_for_step` bypassing `admits`
and using the old rule, both G3 checks fail.

Full suite (`src/run_self_tests.sh`, on the branch's last commit):
grammar 32 pass, measure 40, models 52, procedure 7, train_successor 12,
transplant 44, tripwire 15; 0 fail, 0 skip; "ALL SELF-TESTS PASS". Output:
`experiments/08-successor-degree/out-pairing-exclusion-tests/t1-self-tests.txt`.
The launcher's dry-run test (T7) passes, 21 checks as at the freeze; the only
difference from the freeze's output is one timing (8.0 seconds against 8.1).

## 4. The old stream, replayed (information only)

`out-pairing-exclusion-tests/count_old_stream.py` replays exactly what the old
stream drew for seed 0, the seed all four development runs used, without
rendering or training anything. Over 108,919 steps of 48 pairs: 5,228,112
contents, none skipped by the old rule, **0** carrying a fresh or relaxed
pairing. So, as far as this replay shows, the development runs did not see one;
they stay development evidence only either way.

The odds behind the ruling, for the record: one run's stream was expected to
hold about 0.3 fresh tables (about a one-in-four chance of at least one; about
three in five across three seeds), and the old whole-content rule would not
have stopped them. Relaxed tables can never arise in training, because
training never gives two agents the same value on one item. A narrower meaning
of "pairing" (a single marker, item and value) would fail at once: all 480 such
single combinations occur within the first 200 training steps. The coordinator
of this work confirmed both points independently from the check of the
decision-code additions.

## 5. Readings this change had to make

- **Which sets.** The pairing rule covers the fresh and relaxed sets only, as
  ruled. The development, gate and trajectory sets keep the whole-content rule;
  their tables can still appear in training.
- **The A2 work.** The A2 branch (pull request 105) adds a generator self-test,
  "control 5, stricter", that samples 200 training steps for fresh and relaxed
  tables and says the exclusion is by whole content. Once both are merged that
  sentence is out of date, and the sampled check becomes a secondary one beside
  G1 to G4. The two changes touch different parts of `grammar.py`'s self-test,
  so they should merge without a clash, but whoever merges second should fix
  that sentence. This branch was cut from `main`, not from the A2 branch,
  because nothing here depends on A2's code.
