# Check of the training exclusion by pairing (pull request 115): findings

*Written 2026-10-06 (Pacific) by a Claude Code session that wrote none of the
work it checks. Method, committed before any check ran:
`2026-10-06-training-exclusion-pairing-check-method-claude-code.md` beside
this file (commit `25bb7f9`). Laptop only; nothing rented; $0. Outputs and the
checker's own scripts: `experiments/08-successor-degree/out-check-training-exclusion/`.
Written under the workspace plain-language rule.*

## Verdict: pass, with three small notes

The change does what John ruled on 2026-10-06 (the rulings record of the
version 4 registration review, follow-up item 8): every episode training sees
passes one function, `TrainingStream.admits`, and that function refuses any
episode whose pairing (the table of which marker holds which value on which
item) is that of a fresh or relaxed episode. I found no route around it. The
pairing is the same table the stricter control 5 self-test on `main` uses.
Only the fresh and relaxed sets are excluded by pairing; the other evaluation
sets keep the whole-content rule; nothing else changed. The replay script
draws exactly what the real stream draws, and a second, independent count
through the real old stream agrees with its 0. The full self-test suite
passes, 227 of 227, and the pinned digests are unchanged, rightly.
**The whole-pipeline test (T6) passes at both sizes**, every figure the same
as at the freeze (section 9).

None of the three notes (section 10) affects the guarantee.

## 1. Every path by which training gets episodes: no way around `admits`

Read in full, on the branch at `9acc566`:

- The rented machine runs one training program, `src/train_successor.py`
  (the launcher `src/launch_successor.sh` builds exactly one training
  command, `python train_successor.py ...`).
- The trainer builds one stream, `G.TrainingStream(args.seed)`, with **no**
  exclusion arguments, so both lists take their full defaults: every
  evaluation content (3,900 contents) and every fresh and relaxed pairing
  (1,600).
- Every optimiser step takes its batch from the prefetching thread
  (`Prefetch.get`), which calls only `stream.batch_for_step`, which calls only
  `pairs_for_step`. Resuming a run uses the same stream.
- In `pairs_for_step` the one line that adds an episode to the batch comes
  after `if not self.admits(content): ... continue`. There is no other
  append.
- Nothing else in the experiment's code builds training episodes: the other
  users of the episode generator (`make_pairs`) are the evaluation sets, the
  measurement and self-tests; none feeds an optimiser in a real run. The only
  calls that pass shortened exclusion lists are inside self-tests.

So the guarantee rests on the code, not only on the behavioural test G3.
The two broken copies the author describes, repeated in a scratch folder and
not committed, fail as stated: with the pairing rule removed from `admits`,
G2 (1,600 of 78,400 refused), both G3 checks and cases A and B fail; with
`pairs_for_step` bypassing `admits`, both G3 checks fail.

## 2. The meaning of "pairing": the same table as control 5 and version 4

`pairing()` returns the set of eight (marker, item, value) triples, one per
agent and item, built from the markers, items and values only. Line for line
it is the `table(c)` of `main`'s "control 5, stricter" self-test, and it is
what version 4, section 7.1, calls a combination of marker words, items and
values. Run on the real data (`check_stream.py`): the two functions give the
same result on all 1,600 fresh and relaxed episodes and on 20,000 training
contents; every table has its eight triples; and the exclusion list equals
`main`'s set of held-out tables.

## 3. Scope: only fresh and relaxed by pairing; nothing else changed

The full difference between the branch and `main` touches nine files: the
generator (`grammar.py`), the trainer's description and one recipe line, the
README, the two notes and four test outputs. The pairing rule's list is
`("fresh", "relaxed")`. The whole-content list is unchanged: the same 3,900
contents from all five evaluation sets (development, fresh, relaxed, gate,
trajectory), and the set definitions are byte-identical to `main`. The
models, the measurement and the decision code are untouched.

## 4. The relaxed half

No real draw tests it, as the author says, so I tested it four ways:

- **It cannot arise.** The generator fills each item's values with a draw
  without replacement, and training never asks for a shared value. Over all
  5,228,112 contents of seed 0's full run, no content gives two agents the
  same value on an item; every relaxed episode does.
- **It is fully listed.** All 800 relaxed pairings are in the list, they are
  800 distinct tables, none is also a fresh table (so the fresh half does
  not cover them by accident), and `admits` refuses all 800 episodes.
- **The stream itself skips it.** I replaced two of the stream's own draws,
  inside `pairs_for_step`, with relaxed episodes re-dressed so that no
  whole-content rule matches (agents and items listed in reverse, turn order
  reversed). The stream skipped both and still filled its 48 pairs.
- **Negative control.** With the pairing list emptied, the same planted
  relaxed episodes got through, so the test above can fail.

## 5. The replay script, and a second count

`check_stream.py` runs the author's replay loop beside the real old stream
(`main`'s code, before this change) for steps 1 to 2,000 of seed 0 and
compares every content, in order, by its whole-content fingerprint, **and**
which two agents the eligible-model draw picks. They agree on all 2,000 steps
(96,000 contents). A replay with the eligible-model draw left out diverges at
step 1, so the comparison would catch that mistake. The new stream also draws
exactly the old stream's episodes over those steps, with nothing skipped.

Then, independently of the replay, `count_real_old_stream.py` calls the real
old `pairs_for_step` itself (rendering and all) for every one of the
development runs' 108,919 steps of 48 pairs: **5,228,112 contents, 0 skipped
by the old rule, 0 carrying a fresh or relaxed pairing**, the same as the
replay. The development runs' own logs confirm the settings this assumes:
seed 0, 96 rows a step (48 pairs), 108,919 steps, none resumed, 0 skipped.

## 6. Commit order: method first

On the branch, and in the record of the commits from before the rebase, the
method note (`bca4dda`, before the rebase `e378075`, at 18:58:22) comes
before the code (`bf88d91`, before the rebase `e3e67e0`, at 18:59:38). The
method note was not touched afterwards. See note 1 on the 76-second gap.

## 7. The self-test suite

`src/run_self_tests.sh` on the branch: **227 passed, 0 failed, 0 skipped,
"ALL SELF-TESTS PASS"** (`t1-self-tests.txt`), matching the author's count.

## 8. The pinned digests: unchanged, and rightly

Both constants (`EVAL_SETS_DIGEST` and `FIRST_BATCH_DIGEST`) are the same as
on `main`, and both checks pass. They should not have changed:

- The evaluation sets are not touched by this change.
- The exclusion can change a training batch only when a draw is refused, so
  that the stream draws a replacement. Step 1 of seed 0 draws nothing either
  rule refuses (no draw in the first 2,000 steps does), so its batch is the
  same under the full exclusion, the pairing rule alone, no exclusion at all,
  and `main`'s code: all four give the pinned digest.
- One detail: the pinned-digest check builds its stream with
  `excluded=set()`. Before this change that meant no exclusion; now the
  pairing list still applies by default. That makes no difference to step 1,
  as shown.

## 9. The whole-pipeline test (T6): passes, the same as at the freeze

Started after the method commit and finished on 2026-10-07, with
`tests/pipeline.sh` exactly as at the freeze: both sizes, each arm trained for
30 steps by `train_successor.py` as the rented machine runs it, then measured
with a quarter of the episodes and three shuffles. Output:
`out-check-training-exclusion/t6-stdout.txt` and `t6/` (logs, measurement rows,
fitted reads and summaries; checkpoints not committed).

- **It ran to the end at both sizes** ("T6 ran to the end at: 10M 30M"), with
  no crash and no separate command needed.
- **Every one of the eight trainings skipped 0 contents.**
- **The outcome at both sizes is "substrate not a testbed" (R3)**, as at the
  freeze; untrained models return no verdict, which is a pass here.
- **Every figure is the freeze's.** All eight training logs match the freeze's
  T6 logs figure for figure (apart from timings), and all eight measurement
  rows have the same value in every field the two share (7,216 to 17,344
  fields a row; none differs). The only differences are the checkpoint's path
  and digest, the run time, and fields the decision-code work added on `main`
  after the freeze. That is as expected: in these steps the new stream draws
  exactly the old stream's episodes.
- It was slow: the laptop was heavily loaded by other work for the first
  hours, so measurements took up to eight times as long as at the freeze.

## 10. Notes, ranked

1. **Commit order holds, but the 76 seconds between the method note and the
   code (about 150 lines, 100 of them self-test) mean the code was almost
   certainly drafted alongside the note**, even though the method note says
   it was written "before any code is changed or run". What matters for the
   discipline does hold: the three made-up cases and their expected results
   are in the method commit, before any code that could run them, and were
   not edited after. Record-keeping only.
2. **The stricter control 5 self-test can no longer fail.** It samples 200
   steps from a stream that now has the pairing exclusion by default, so it
   checks the exclusion against itself. The amended comment says it is
   secondary to G1 to G4, which is true; its claim that the sample "finds no
   shared table even with the exclusion switched off" also holds (none in the
   first 2,000 steps). If an independent sample is wanted, build that stream
   with `excluded_pairings=set()`. Low.
3. **The method note says the trainer's recipe stays as frozen, but the
   recipe's data line changed** (it now ends "fresh and relaxed pairings
   excluded"). That line is written into every checkpoint and compared when a
   run resumes, so a checkpoint from before this change cannot be resumed by
   the new trainer. Nothing needs to resume one; the registration text should
   quote the new line. Wording only.

## Checker's outputs

All in `experiments/08-successor-degree/out-check-training-exclusion/`:
`check_stream.py` and its output `check_stream.txt` (16 of 16 pass; it needs
`main`'s `grammar.py` at `93501f7` saved to a file, given as its second
argument); `count_real_old_stream.py` and `count_real_old_stream.txt`;
`t1-self-tests.txt`; `t6-stdout.txt` and the T6 logs, measurement rows and
summaries under `t6/` (checkpoints not committed).
