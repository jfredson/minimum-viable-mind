# Method: check of the training exclusion by pairing (pull request 115)

*Written 2026-10-06 (Pacific) by a Claude Code session that wrote none of the
work it checks, before any check is run. Laptop only; $0. Written under the
workspace plain-language rule.*

## What is checked

Pull request 115 (branch `training-exclusion-pairing`, at commit `9acc566`)
carries out John's ruling of 2026-10-06 (the rulings record of the version 4
registration review, `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`,
follow-up item 8): training must leave out every fresh and relaxed episode **by
its pairing**, meaning its table of which marker holds which value on which
item, so that "no such pairing occurs in the training stream" is guaranteed by
the code and not sampled. Its method note is
`docs/2026-10-06-successor-training-exclusion-pairing-method.md`; its findings
note is `docs/2026-10-06-successor-training-exclusion-pairing-findings.md`.

## What I will do, and what counts as a problem

1. **Every path by which training gets episodes.** Read the trainer
   (`experiments/08-successor-degree/src/train_successor.py`), its prefetching
   thread, the launcher (`src/launch_successor.sh`) and the stream
   (`src/grammar.py`, `TrainingStream`), and search all of the experiment's
   code for anything else that builds training episodes (`_content`,
   `make_pairs`, the stream's constructor called with its exclusion lists
   overridden). A problem: any route from the episode generator to an
   optimiser step that does not pass `TrainingStream.admits`, or a real
   training call that passes empty or partial exclusion lists.
2. **The meaning of "pairing".** Compare `pairing()` line by line with the
   table used by the stricter control 5 self-test on `main` (`table(c)` in
   `grammar.py`) and with version 4 of the proposal, section 7.1. Then, on
   the real evaluation sets, confirm the two functions give the same result
   for every fresh and relaxed episode and for a sample of training episodes.
   A problem: any input on which they differ, or a definition narrower or
   wider than the ruling's.
3. **Scope.** Confirm, from the full difference between the branch and
   `main`, that only the fresh and relaxed sets are excluded by pairing, that
   the whole-content list still covers all five evaluation sets
   (development, fresh, relaxed, gate, trajectory), and that nothing outside
   the files the pull request names changed. A problem: any other change to
   what training sees, to the evaluation sets, the models or the measurement.
4. **The relaxed half.** Relaxed episodes give two agents the same value on
   one item, which the training generator never does, so no real draw tests
   it. I will (a) confirm from the generator's code that a training draw can
   never have a shared value; (b) confirm that every one of the 800 relaxed
   pairings is in the stream's exclusion list and is refused by `admits`;
   and (c) run the stream itself, not only `admits`, with a relaxed pairing
   planted as if a draw had produced it, by feeding the stream a generator
   whose draw is replaced by that relaxed content, and see it skipped. A
   problem: any relaxed pairing that `admits` lets through.
5. **The replay script** (`out-pairing-exclusion-tests/count_old_stream.py`).
   Run the real old stream (the code on `main`, before this change) and the
   replay side by side for the first 2,000 steps of seed 0 and compare every
   content drawn, by its whole-content fingerprint, in order. Also confirm
   that the new stream draws the same contents as the old one over that span
   (it should, since no exclusion fires). Then count fresh and relaxed
   pairings over all 108,919 steps a second way, by calling the real old
   `pairs_for_step` itself rather than a copy of its draws, if the laptop
   allows it in the time. A problem: any difference in the first 2,000 steps,
   or a different count.
6. **Commit order.** Read the branch's history, including the record of the
   commits before the rebase, and confirm the method note came before the
   code. Report the gap between them.
7. **The self-test suite.** Run `src/run_self_tests.sh` on the branch.
   Expected: 227 passed, 0 failed, "ALL SELF-TESTS PASS".
8. **The pinned digests.** Confirm `EVAL_SETS_DIGEST` and
   `FIRST_BATCH_DIGEST` in `grammar.py` are the same as on `main` and that
   the checks of them pass. Say whether they should have changed, and why
   not: the first batch's digest can only change if step 1 of seed 0 draws a
   content the new rule refuses; I will check what that digest's stream is
   built with and whether step 1 draws anything the new rule refuses.
9. **The mutation check** the author reports (pairing rule removed; stream
   bypassing `admits`). I will repeat both in a scratch copy, not committed,
   and confirm the named checks fail.
10. **The whole-pipeline test T6** (`tests/pipeline.sh`, both sizes, as at
    the freeze), run in the background. Expected, from the freeze: every arm
    trains its 30 steps, every arm is withheld with no verdict, and the
    outcome is R3 at both sizes. The trainer's log should report 0 skipped
    contents. A problem: any crash, or an outcome other than the freeze's.

## Verdict

**Pass** if nothing in items 1 to 5 is a problem, the suite passes, the
digests are unchanged with a sound reason, and T6 runs to the end with the
freeze's outcome. **Pass with notes** if only wording or record-keeping points
are found. **Fail** if any route around the exclusion exists, the definitions
differ, the scope is wrong, or the replay is not faithful.
