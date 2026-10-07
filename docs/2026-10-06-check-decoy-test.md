# Check of the decoy test (pull request 108): findings

*Written 2026-10-06 (Pacific) by a Claude Code session that did not write the
decoy test, on branch `check-decoy-test-a6`. The check's method and probe
script were committed and pushed at `8acf77f`, before anything was re-run
(`docs/check-decoy-test-method-2026-10-06.md`). Laptop, processor only, 4
threads per run. Nothing rented, trained or spent: $0.*

*What was checked: the decoy test that John ordered on page 10 of the Gate A
addendum, to answer finding A6 of the ChatGPT outside review of version 4 ("a
readable but unused copy of the owner's marker could make a separable model
read as entangled"). It is a constructed stand-in: the committed separable
toy model (arm T) with extra numbers added by hand. Nothing here is about a
trained model.*

## 1. The short version

- **The numbers reproduce exactly.** Every check, every reading, every site
  choice and every share, at all four scales and all three seeds, came out
  the same. The saved reads are byte-identical; the result files differ only
  in the folder path and the run time.
- **The test is the one John ruled, and its method came first.** The method
  and code were committed before any output, and the code was not changed
  afterwards. One small departure: the two main runs ran side by side, not
  one after another as the method said. It changes no number.
- **But the test could not have failed.** An exact copy of the ownership
  block can never pull the read away from the block: the read's directions
  always carry the block along in step with the copy. The decoy test's own
  method said so before the run (its section 7). My first probe confirms it
  numerically: with or without the copy, the chosen piece leaves the same 3
  to 4 per cent of the block's change unmoved. So "not fooled" is a correct
  result, but it is not evidence that the read resists a decoy.
- **A differently coded decoy does partly fool it.** As a probe (not a ruled
  test, and skipping the registered nomination), I replaced the exact copy
  with an unused one-of-12 code of the owner's marker word, four times the
  block's size. At the site the decoy test always chose (the first running
  state, the action position, 8 directions) the readings were **0.28, 0.23
  and 0.29** on the three seeds, against 0.00 for the exact copy. With fewer
  directions they rise to 0.66 to 0.96. Under the decoy test's own bands,
  0.23 to 0.29 is "inconclusive", not "not fooled". I had predicted 0.20 or
  less; I was wrong, and section 4 says why.
- **Verdict: confirmed as a reproduction, with corrections to how it is
  used.** The "not fooled" result stands for the exact copy. It should not be
  read as the read passing A6, and it should not by itself carry page 12.

## 2. Did the numbers reproduce? Yes, exactly

Re-run from the decoy test's committed code, unchanged, with the pinned
versions (torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, scipy 1.18.0, Python
3.12.13):

    python decoy_test.py --checks-only
    python decoy_test.py --scale 4        # side by side with the next, as the original ran
    python decoy_test.py --scale 0.25
    python decoy_test.py --scale 16
    python decoy_test.py --scale 0.0625
    python decoy_test.py --report

Compared with `git diff` against the decoy test's branch tip `6794155`:

| What | Result |
|---|---|
| `checks_only.json`, every `checks_T_seed*.json` | byte-identical |
| every `reads_T_seed*.npz` (the fitted reads) | byte-identical |
| every `summary.json`, every `table.md`, `table.md`, `verdicts.json` | byte-identical |
| every `row_T_seed*.json` | identical except two fields: the model file's folder path and the run time in seconds |
| run logs | identical except times and paths |

So the six ruled readings (0.0000 at scales 4 and 1/4 on seeds 0, 1 and 2),
the six supplementary ones (0.0000 at 16 and 1/16), the site chosen (first
running state, action position, 8 directions) everywhere, the piece shares
(for example 0.9370 / 0.0586 / 0.0045 for seed 0 at scale 4) and the verdict
"not fooled" in both orientations all reproduce to every printed place. The
reproduced files were not committed (they would only change the path and
time fields); the committed originals are left as they were.

## 3. Is the test the one John ruled, and was the method first? Yes

| Point | Holds? |
|---|---|
| The ruling (page 10, recorded in the 2026-10-06 rulings record, pull request 103) adopts: arm T toy models, an exact unused copy of the owner's marker, the registered nomination and reading unchanged, the copy larger then smaller than the slot, same states and positions, method first, $0, checked. The method and code do exactly this. | yes |
| The frozen measurement folder, `experiments/08-successor-degree/`, is unchanged between the main line at `53ae82c` and the decoy test's branch tip. | yes (empty diff) |
| `decoy_test.py` replaces only the model-loading function, and only for the length of each call. | yes, by reading |
| The widened model throws the copy away before every block and before the action head (`DecoyArmT._split`); the checks that overwriting or transplanting the copy changes nothing reproduce bit for bit. | yes |
| The method-and-code commit `f3481a2` carries no output; every output commit comes after it; the code is not changed after it. | yes |
| Timing. Method committed 09:58:13 Pacific. The checks finished and were committed at 10:09:04; the resume note says the two main runs started about 10:09; each took about 14 minutes; the readings were committed at 10:24:57. GitHub's record of the 10:09:06 push shows the branch already stood at `f3481a2` before it, so the method was on GitHub before the readings started. I cannot see the exact time `f3481a2` itself was pushed (the first push is not in GitHub's event list), so "pushed before the checks ran" rests on the commit time and the note's word. | yes, with that one gap |
| Departure: the method said the scale runs would go "one after another"; they ran side by side (so two runs of 4 threads each). Results are deterministic and reproduce, so this changes nothing. | minor departure |

## 4. Did the test have power? No, for the exact copy; a different code does have some

**Why the exact copy cannot fool the read (argued, and confirmed below).**
The registered read is a straight-line fit with a penalty on the size of its
weights. Such a fit builds its weights out of the training states
themselves. When the copy is always exactly `s` times the block, every
weight direction is "some direction in the block, and `s` times it in the
copy". A transplant along those directions moves the block by the same
amount it would without the copy. The scale only changes where the piece's
length sits (94 per cent in the copy at scale 4), not what it does to the
block. The decoy test's method and findings say this themselves (method
section 7; findings sections 1 and 5).

**Probe 1, measured.** On the 800 fresh pairs, the share of the block's
donor-minus-recipient change that the chosen 8-direction piece leaves
unmoved:

| seed | no copy (unaltered model) | copy ×4 | ×1/4 | ×16 | ×1/16 |
|---|---|---|---|---|---|
| 0 | 0.027 | 0.030 | 0.028 | 0.029 | 0.027 |
| 1 | 0.030 | 0.034 | 0.030 | 0.032 | 0.030 |
| 2 | 0.038 | 0.041 | 0.037 | 0.029 | 0.038 |

The copy changes the unmoved share by at most 0.004, so the read behaves the
same with or without it, as argued. (My prediction had a second part, that
the unmoved share would be under 0.01; it is 0.03 to 0.04 even with no copy
at all, because 8 directions do not quite cover the block's change. That
part of my prediction was wrong, and it does not affect the reading, which
needs only enough of the change to flip the action.)

**Probe 2.** The model's 20 marker vectors (24 numbers each) are linearly
independent on every seed (rank 20; smallest-to-largest spread about 0.03).
From that I argued in the method that *any* code of the owner's marker word
would be a straight-line function of the block, and so would also fail to
fool the read. **Probe 3 shows that argument was incomplete.**

**Probe 3, a one-of-12 code as the decoy** (held in 20 numbers, one per marker word, of which the 12 words these episodes use are ever set; an unused code of the owner's
marker word, built the same way as the block, four times the block's typical
size, discarded before the next layer; both "unused" checks hold bit for
bit). The frozen fit, then the frozen transplant at the first running state,
action position, and the frozen reading formula; **not** the registered
nomination, controls or null:

| seed | 1 direction | 2 | 4 | 8 | piece share in the code (8 directions) | block change left unmoved (8 directions) |
|---|---|---|---|---|---|---|
| 0 | 0.95 | 0.89 | 0.66 | **0.28** | 0.94 | 0.30 |
| 1 | 0.91 | 0.82 | 0.52 | **0.23** | 0.94 | 0.21 |
| 2 | 0.96 | 0.94 | 0.75 | **0.29** | 0.94 | 0.29 |

(Exact copy at the same site, 8 directions: reading 0.0000 and about 0.03
left unmoved.)

Why my argument failed: it is true that the read's weights always carry the
block in step with the code, but the transplant keeps only the top 8
directions. The code and the block are related by a lopsided straight-line
map (the marker vectors are spread unevenly), so the 8 directions that
matter most for reading the code are not the 8 that matter most for moving
the block. A fifth to a third of the block's change is left behind, and the
action follows the recipient often enough to lift the reading to about 0.25.
With an exact copy the two geometries are the same, which is why it showed
nothing.

What probe 3 does **not** show: what the registered procedure would read.
The nomination searches 45 site sets and four sizes and picks the one that
moves the action most on development episodes; it might pick a site that
reads lower, or confirm about 0.25, and its withholding rules and null have
not been run. The probe is enough to say the exact-copy result does not carry
over to a decoy coded differently, even a simple one. It is not a verdict.

## 5. Problems, ranked

1. **Significant, and bears on page 12: the ruled test had no power.** An
   exact copy cannot produce "fooled" when the fit is near its optimum, which
   it was (the copy carried 0.93 to 0.94 of the read's weight, against 0.94
   expected). The decoy test's authors say so in their method and findings.
   But page 12's recommendation ("if it is fooled, stop or redesign; if not,
   continue") was written on the premise that the decoy test "answers the
   sharpest form" of the worry. It answered the weakest form: one it could
   not fail. "Not fooled" is a correct result and confirms the frozen code
   runs end to end on a widened model; it adds little evidence that the read
   resists a decoy.
2. **Significant: a differently coded decoy reads 0.23 to 0.29 at the
   decoy test's site** (probe 3), which the decoy test's bands would call
   inconclusive. This is the "general form of A6" the findings name as
   untested, and it is not clean. It should go to John as part of page 12,
   not after it. If John wants it settled, the natural next step is the
   one-of-12 decoy run through the full frozen procedure under its own
   committed method (also $0, about an hour on a quiet laptop). I did not
   run that.
3. **Significant (wording): claims that lean further than the evidence.**
   - Findings section 6, "For John, plainly": "The sharp, cheap form of the
     worry came back clean." Suggest: "The simplest form of the worry, an
     exact copy, came back clean, as the method predicted it must; this form
     could not have failed."
   - Findings section 1: "So the test reached the case A6 worries about: the
     read's directions were mostly in the unused copy." A6's case is
     directions in the copy *without* the matching part in the used block.
     Here the matching part is always there. Suggest: "The read's directions
     lay mostly in the copy, but always carried the block in step with it,
     so this is not yet the case A6 worries about."
   - Findings section 6: "on the planning session's recommendation already on
     record (page 12), it points to continue." Suggest adding: "That
     recommendation assumed the test could fail; this one could not, and a
     differently coded decoy partly fools the read (the check of this test,
     section 4)."
   - Pull request description: "The result: not fooled, both ways round"
     should carry, in the same paragraph, "a result the method showed in
     advance could not have come out otherwise".
   - The drafted test text adopted by the ruling says a near-0 reading means
     "the read finds the used slot even with a cleaner decoy beside it". The
     copy was not cleaner; it was identical up to scale. Worth correcting
     when the wording for version 5 is written.
4. **Minor: the scale runs ran side by side, not one after another** as the
   method said. No effect on any number.
5. **Minor: the push time of the method commit itself is not visible** on
   GitHub's event list; its commit time (09:58) and the push record of the
   next commit (the branch already at the method commit before 10:09:06)
   are consistent with "method first".

Nothing found changes the "not fooled" verdict *for the exact copy*.

## 6. What bears on page 12 (continue or stop)

Page 12 was deferred to "the decoy test's checked result", with the
recommendation "continue if not fooled". The checked result is: not fooled,
reproduced exactly, but by a test that could not fail; and a cheap,
differently coded decoy, probed outside the registered procedure, moves the
reading to about 0.25 where the exact copy gave 0. So the honest summary for
John is that **the decoy question is open, not closed**. That does not by
itself say stop: 0.25 is below the 0.50 the decoy test's method set for
"fooled", and the full procedure has not been run on it. But it does mean
"continue" would rest on the recommendation's premise rather than on
evidence, and John may want the one-of-12 decoy run properly (method first,
$0) before deciding page 12. That choice is his.

## 7. Files

- Method: `docs/check-decoy-test-method-2026-10-06.md` (committed first, `8acf77f`)
- Probe script: `experiments/rehearsal-successor-measure/src/check_decoy_power.py`
- Probe output: `experiments/rehearsal-successor-measure/out-decoy-check/`
  (`p1.json`, `p2.json`, `p3.json`, `p3.log`)
- Reproduction: not committed; re-run the commands in section 2 and compare
  with `git diff`.
