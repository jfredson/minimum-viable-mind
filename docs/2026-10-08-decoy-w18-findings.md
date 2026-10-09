# The test of a differently coded decoy (weakness W18): findings

*Written 2026-10-08 (Pacific) by the Claude Code session that ran it, on
branch `decoy-test-w18`. The method, `docs/2026-10-08-decoy-w18-method.md`,
was committed and pushed alone at `ddef906`, before any test code existed;
the test code, `experiments/08-successor-degree/out-decoy-w18/decoy_w18.py`,
was committed and pushed at `a517316`, before any of its outputs existed,
and was not changed afterwards. Laptop, processor only, 4 threads per run.
Nothing rented, trained or spent, no paid service called: $0.*

***A constructed stand-in, not a trained model.*** *Everything below was
measured on the committed separable toy model (arm T) with 20 extra numbers
bolted onto its running state by hand. It says what the registered
measurement does with that construction. It says nothing about any trained
model.*

*This session wrote the method, the code and this note. It is owed a check
by a session that did not, which re-runs the script from the committed code
(section 8).*

## 1. The short version

- **Verdict against the bands fixed in advance: inconclusive.** The
  stronger decoy (variant V1, four times the ownership block's size, the
  decoy the earlier check's probe used) returned **no verdict on all three
  seeds**, so under the bands it is "inconclusive" (fewer than two seeds
  with a reading). The weaker decoy (V2, a quarter of the block's size) read
  **0.0000 on all three seeds: not fooled.** Overall, by the method's rule:
  **inconclusive.**
- **Why there was no verdict: one of the procedure's own checks caught the
  decoy.** On arm T the registered procedure transplants everything *except*
  the chosen piece and requires that this moves the action no more than the
  allowance (control 1, "the content transplant, on arm T"). With the decoy
  in place it moved 10 to 16 per cent of the actions (0.1313, 0.1638 and
  0.1038 against an allowance of 0.018), so the procedure refused to give a
  reading. Run as the registered experiment would run it, a separable model
  carrying this decoy ends in the eighth registered term, **"instrument
  returned no reading on the separable mechanism"**, not in a false
  "entangled".
- **But the read was partly pulled into the decoy, and the arithmetic under
  the refusal shows it.** The piece the nomination chose lay about 94 per
  cent in the unused code and left about a fifth of the block's change
  behind (0.199, 0.215 and 0.190). The reading the procedure computed and
  then withheld was **0.1488, 0.2137 and 0.1162**, on a model whose true
  reading is 0. One of those (seed 1, 0.2137) is above 0.20 with the piece
  mostly in the code, which the method listed in advance as counting against
  the measure. So the honest description of V1 is: **the read was partly
  fooled, and a control caught it.**
- **The guard that caught it works on arm T only.** Control 1 withholds a
  reading on arm T alone; on arms C, M and F it is reported and withholds
  nothing (version 5, section 7). So if the free model (arm F, whose reading
  is the scientific question) were in fact separable and carried a code like
  this, the registered procedure would print its reading, which on these
  figures would be somewhere around 0.1 to 0.4, not withhold it.
- **No decoy of this kind came near making a separable model read as fully
  entangled.** Across all five variants, the highest reading computed was
  0.41 (V3, sixteen times the block's size, withheld). The nomination chose
  8 directions on every seed of every variant, so the much higher readings
  at fewer directions that the probe found (0.52 to 0.98 here) were never
  chosen. So a reading near 1 on arm C cannot be explained by a decoy of
  this family.
- **My prediction was half right.** I expected V1 inconclusive with readings
  of about 0.2 to 0.3 and V2 not fooled. V2 and the overall verdict came out
  as expected; V1 came out inconclusive for a different reason (no verdict,
  from control 1), and its withheld arithmetic was lower than I expected
  (0.12 to 0.21 against the probe's 0.23 to 0.29), most likely because the
  reads are now fitted on 1,800 episodes instead of 420.

## 2. The checks that the code is unused and built as stated

From `out-decoy-w18/checks_only.json` (every variant, every seed) and each
variant's `checks_T_seed*.json`, all hold on all fifteen:

| Check | Result |
|---|---|
| (a) widened model's outputs bit-identical to the committed model's | yes, all fifteen |
| (b) transplanting the donor's code alone, every state, every position | bit-identical, all fifteen |
| (b') overwriting the code with large random numbers everywhere | bit-identical, all fifteen |
| (c) the code's largest number at the action is on the owner's word; every number between 0 and `k`; sums as stated | yes, all fifteen; 12 marker words ever set |
| (d) a straight-line read of the owner's word from the code alone, correct of 180 at states 0 to 4 | 180 at every state, all fifteen (and from the block alone, 180) |
| (e) at state 0, the action: share moved by the whole state / block alone / code alone | 1.0000 / 1.0000 / 0.0000, all fifteen; readings 0 with the block, 1 with the code |
| (f) the frozen gate record (accuracy, lesion, in-use check, row-choice split) equal to the committed model's | yes, all fifteen |

So the code is as easily read as the block and causally inert, and check
(e) is the decoy worry in miniature: had the procedure transplanted the code
alone, it would have read 1. The size `k` was 20.57, 22.20 and 21.05 for V1
on seeds 0, 1 and 2 (four times the block's size of 5.14, 5.55 and 5.26),
the probe's values exactly. At the action the soft code put on average
0.9987 of its weight on the owner's word.

No stop fired (K1 model fingerprints, K2 checks, K3 errors). No fit stopped
at the iteration limit in any run.

## 3. The readings, every variant, every seed

The script's table (`out-decoy-w18/table.md`), shortened. "Computed" is the
arithmetic the frozen procedure wrote into the row before `summarise`
decided whether to withhold it; the **registered figure** is the second
column.

| variant | seed | registered figure | computed (withheld if no verdict) | site set chosen | piece in code / block | block change left unmoved | control 1 (allowance 0.018) |
|---|---|---|---|---|---|---|---|
| V1, soft code ×4 | 0 | **no verdict** (control 1 failed) | 0.1488 | state 0, action, 8 directions | 0.935 / 0.065 | 0.199 | 0.1313 |
| V1, soft code ×4 | 1 | **no verdict** (control 1 failed) | 0.2137 | state 1, action and the step before, 8 directions | 0.939 / 0.061 | 0.215 | 0.1638 |
| V1, soft code ×4 | 2 | **no verdict** (control 1 failed) | 0.1162 | state 0, action, 8 directions | 0.935 / 0.065 | 0.190 | 0.1038 |
| V2, soft code ×1/4 | 0 | **0.0000** | 0.0000 | state 0, action, 8 directions | 0.086 / 0.914 | 0.027 | 0.0000 |
| V2, soft code ×1/4 | 1 | **0.0000** | 0.0000 | state 0, action, 8 directions | 0.079 / 0.920 | 0.029 | 0.0000 |
| V2, soft code ×1/4 | 2 | **0.0000** | 0.0000 | state 0, action, 8 directions | 0.096 / 0.903 | 0.040 | 0.0000 |
| V3, soft code ×16 (beside) | 0 | no verdict (control 1 failed) | 0.3500 | state 0, action, 8 directions | 0.996 / 0.004 | 0.311 | 0.2363 |
| V3, soft code ×16 (beside) | 1 | no verdict (control 1 failed) | 0.2788 | state 0, action, 8 directions | 0.996 / 0.004 | 0.240 | 0.1513 |
| V3, soft code ×16 (beside) | 2 | no verdict (control 1 failed) | 0.4100 | state 1, action and the step before, 8 directions | 0.996 / 0.004 | 0.318 | 0.2963 |
| V4, soft code ×1 (beside) | 0 | 0.0000 | 0.0000 | state 0, action, 8 directions | 0.521 / 0.479 | 0.053 | 0.0000 |
| V4, soft code ×1 (beside) | 1 | 0.0000 | 0.0000 | state 0, action, 8 directions | 0.506 / 0.494 | 0.039 | 0.0000 |
| V4, soft code ×1 (beside) | 2 | 0.0000 | 0.0000 | state 0, action, 8 directions | 0.533 / 0.467 | 0.068 | 0.0000 |
| V5, hard code ×4 (beside) | 0 | no verdict (control 1 failed) | 0.1488 | state 0, action, 8 directions | 0.935 / 0.065 | 0.199 | 0.1313 |
| V5, hard code ×4 (beside) | 1 | no verdict (control 1 failed) | 0.2125 | state 1, action and the step before, 8 directions | 0.939 / 0.061 | 0.215 | 0.1638 |
| V5, hard code ×4 (beside) | 2 | no verdict (control 1 failed) | 0.1162 | state 0, action, 8 directions | 0.935 / 0.065 | 0.190 | 0.1038 |

Everything else about each seed passed: the gate (3,000 of 3,000), the
in-use check, the floors on development and fresh episodes, control 7 (the
null transplant) and control 4 (the pairing check). The true-slot reference
(transplanting the ownership block itself) read 0.0000 everywhere. No seed
of any variant was withheld for anything but control 1.

**The readings at every size, at the chosen site (fresh pairs), for V1:**
seed 0: 0.98, 0.89, 0.65, 0.15 at 1, 2, 4 and 8 directions; seed 1: 0.95,
0.81, 0.63, 0.21; seed 2: 0.93, 0.86, 0.54, 0.12. So the probe's pattern
reproduces (high at few directions, low at 8). The nomination picks the size
whose ownership-only transplant moves the action most on development pairs,
which was 8 directions every time; it never chose a smaller size.

**V5 (the hard code) behaves like V1** to the printed precision on seeds 0
and 2 and within 0.002 on seed 1. That is expected: at the action the soft
code is already almost one-hot (0.9987 on the owner's word), so making it
exactly one-hot changes almost nothing where the read is fitted. V5 does not
add a genuinely different, non-straight-line test, and section 6 says so.

**The stricter and sensitivity rows** (reported beside, never instead) agree:
on V1 the stricter row (state 1 only) computed 0.18, 0.21 and 0.13, and the
sensitivity row 0.07, 0.04 and 0.07; control 1 failed on every one of them.
On V2 and V4 every row read 0.0000 with control 1 holding.

## 4. Verdict by the method's section 7

| Variant | Seeds with a reading | Verdict |
|---|---|---|
| V1, soft ×4 | 0 of 3 | **inconclusive** (fewer than two seeds returned a reading) |
| V2, soft ×1/4 | 3 of 3, all 0.0000 | **not fooled** |
| V3, soft ×16 (beside) | 0 of 3 | inconclusive |
| V4, soft ×1 (beside) | 3 of 3, all 0.0000 | not fooled |
| V5, hard ×4 (beside) | 0 of 3 | inconclusive |

**Overall (V1 and V2): inconclusive.** The method's section 7 said this is
not a pass, and it is not.

Against the method's section 8 list of what would count against the
measure, said before the run:

- "a fooled verdict": **did not happen.**
- "any seed of V1 or V2 whose nominated reading is above 0.20 with the piece
  mostly in the code": **happened in the arithmetic, not in a registered
  figure.** V1 seed 1 computed 0.2137 with the piece 0.94 in the code; the
  procedure withheld it.
- "the nomination choosing a size below 8 directions": **did not happen**,
  on any seed of any variant.

And what would count for it: "V1 and V2 both not fooled, with the same site
and size as on the unaltered model". **Half**: V2 yes; V1 no.

## 5. What this means for W18 and for a high reading on arm C

**What W18 said** (version 5, section 13): an unused code, coded differently
from the block, could partly fool the read; in the probe, outside the
registered procedure, it read 0.23 to 0.29, so a separable model carrying
such a code "could read part way to entangled", and nothing in the design
excluded it.

**What this test adds.**

1. **On arm T, the design does exclude the false reading, by refusing to
   give one.** Run through the whole registered procedure, the decoy that
   partly fooled the probe did not produce a reading at all on any seed:
   control 1 failed and the seed was withheld, so the arm would end in the
   eighth registered term. That is a failure of the instrument, in the
   direction that does not mislead: it says "no reading", not
   "entangled". This was not foreseen in the method and is the main new
   fact.
2. **The read itself is still partly fooled.** Under the refusal, the chosen
   piece lay mostly in the unused code, left about a fifth of the used
   block's change behind, and the arithmetic came to 0.12 to 0.21 at four
   times the block's size and 0.28 to 0.41 at sixteen times. The weakness is
   real; what is new is that, on arm T, a control catches it.
3. **On arms C, M and F nothing catches it.** Control 1 is a check that
   withholds on arm T only, because only on arm T is it known that the
   content should carry no ownership. On arm C and the free model it is
   reported and withholds nothing, and on an entangled model the complement
   of the piece would be expected to move the action anyway, so a large
   control 1 figure there could not tell a decoy from real entanglement. So
   for the free model, which is where the experiment's answer comes from,
   W18 stands: if it were separable but carried an easily read, unused code
   of its owner, its reading could be lifted to somewhere around 0.1 to 0.4
   on these figures, and the registered procedure would print it.
4. **A high reading on arm C, or near 1 on the free model, is not explained
   by a decoy of this kind.** No variant computed more than 0.41, and the
   nomination never chose the small sizes where the readings are high. A
   decoy of this family can account for part of a middling reading (for
   example, inside arm M's band of 0.3 to 0.7), not for a reading near 1.
5. **What it does not show.** Only one family of decoy was tried: a
   one-number-per-word code of the owner, soft or hard, at five sizes, at
   every state and position. V5 was meant as a code that is not a
   straight-line function of the block, but at the action it is almost the
   same numbers as V1, so that form is still effectively untested. A decoy
   built differently (spread over many more numbers, present at only some
   states, or with a geometry chosen to defeat control 1) might do more.
   Nothing here is about a trained model.

**For John, plainly.** The decoy that partly fooled the read in the earlier
probe was run through the full registered procedure. On the separable toy
model the procedure did not report it as entangled; it refused to give a
reading, because one of its own checks noticed that the part it left
untouched still moved the model's answer. Under that refusal, the read had
been pulled about a fifth of the way off, much as the probe found. That
check only guards the separable model, though. On the free model, a decoy
of this kind could lift a reading by roughly 0.1 to 0.4 and nothing would
flag it. It could not make a model read near 1. So W18 should stay in the
registered text as an open weakness, now with a measured size and with the
new fact that the separable arm is protected and the free arm is not.
Whether that is enough to register, or whether a guard like control 1 is
wanted for the other arms, is John's call, not this session's.

**A wording suggestion for version 5's W18, not made here** (version 5 is
not edited by this branch): replace "So a separable model carrying such a
decoy could read part way to entangled" with something like "Run through the
registered procedure (`docs/2026-10-08-decoy-w18-findings.md`), the
separable toy model carrying this code gave no reading on any seed, because
control 1 failed; the reading it computed and withheld was 0.12 to 0.21 at
four times the block's size and 0.28 to 0.41 at sixteen times. Control 1
withholds on arm T only, so on arms C, M and F such a code could lift a
reading by about that much unflagged; it could not produce a reading near
1."

## 6. Departures from the method

- **None in the numbers.** The checks, the five variants, the settings and
  the commands are as the method says; the code was not changed after its
  commit.
- **Before the code was committed** it was run once end to end at tiny
  episode counts (5 per cent of every set, one seed, two shuffles) into a
  scratch folder outside the repository, which found one misplaced bracket
  in check (c) for the hard code; the code commit's message says so. That
  run is a pipeline test, not a figure, and nothing from it is kept.
- **Run order.** V1 then V3 then V5 ran one after another, side by side with
  V2 then V4 (two runs of 4 threads at a time), as the method allowed. Each
  run is deterministic, so the order changes no number.
- **The method expected 20 to 30 minutes a variant;** they took 15 to 23.

## 7. Files

`experiments/08-successor-degree/out-decoy-w18/`:

- `decoy_w18.py`, the test code (committed before any output);
- `checks_only.json` and `checks_only.log`, the checks for every variant and
  seed, before any reading;
- `V1/` to `V5/`, one folder per variant: `checks_T_seed*.json`,
  `row_T_seed*.json` (the frozen procedure's row, with a `decoy_w18` section
  added after it for reporting only), `reads_T_seed*.npz`, and the frozen
  `summary.json` and `table.md`;
- `run_V1.log` to `run_V5.log`, the run logs;
- `table.md` and `verdicts.json`, the table and verdicts across variants.

Nothing under `experiments/08-successor-degree/src/`, version 5 of the
registration text or the red-team ledger was edited.

## 8. What the checker must recompute

From this branch, with the pinned versions (torch 2.12.1, scikit-learn 1.9.0,
numpy 2.5.0, scipy 1.18.0, Python 3.12.13), from
`experiments/08-successor-degree/out-decoy-w18/`:

    python decoy_w18.py --checks-only
    python decoy_w18.py --variant V1
    python decoy_w18.py --variant V2
    python decoy_w18.py --report

(and V3 to V5 if wanted), then compare with `git diff`. Confirm: every check
in section 2 holds; the registered figures, the computed arithmetic, the
site sets, the piece shares and the control 1 figures in section 3 match to
four places; and the verdict follows from the method's section 7 as written.
Also worth checking independently: that `decoy_w18.py` replaces nothing in
the frozen procedure but `load_model`, and only for the length of each call;
that `CodeDecoyArmT._split` really throws the code away before the next
block; that the code built is the check's probe 3 code (compare `k` with
`experiments/rehearsal-successor-measure/out-decoy-check/p3.json`); and that
control 1 is right to withhold on arm T here (on arm T the content and the
code carry no ownership the action reads, so the complement of the piece
moving the action means the piece missed part of the block).
