# Page 4 toy re-run: comparison (written by page4_compare.py)

- reproduction check, models at 420 fitted: 29154 values compared, 0 differ: PASSES
- reproduction check, solver at 420 fitted: 11712 values compared, 0 differ: PASSES

## The twelve toy models: fitted on 420 (old) against 1,800 (new)

| model | field | old, 420 fitted | new, 1,800 fitted | same? |
|---|---|---|---|---|
| T/0 | status | nominated | nominated | yes |
| T/0 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/0 | piece_correct | 180 | 180 | yes |
| T/0 | whole_read_correct | 180 | 180 | yes |
| T/0 | reading | 0.0000 | 0.0000 | yes |
| T/0 | described_only | False | False | yes |
| T/0 | control1_complement | 0.0000 | 0.0000 | yes |
| T/0 | control1_holds | True | True | yes |
| T/0 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| T/0 | control4_holds | True | True | yes |
| T/0 | control7_holds | True | True | yes |
| T/0 | true_slot | 0.0000 | 0.0000 | yes |
| T/0 | rider | 0.0000 | 0.0000 | yes |
| T/0 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/0 | best_piece_anywhere | 180 | 180 | yes |
| T/0 | control2 | not applicable | not applicable | yes |
| T/1 | status | nominated | nominated | yes |
| T/1 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/1 | piece_correct | 180 | 180 | yes |
| T/1 | whole_read_correct | 180 | 180 | yes |
| T/1 | reading | 0.0000 | 0.0000 | yes |
| T/1 | described_only | False | False | yes |
| T/1 | control1_complement | 0.0000 | 0.0000 | yes |
| T/1 | control1_holds | True | True | yes |
| T/1 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| T/1 | control4_holds | True | True | yes |
| T/1 | control7_holds | True | True | yes |
| T/1 | true_slot | 0.0000 | 0.0000 | yes |
| T/1 | rider | 0.0000 | 0.0000 | yes |
| T/1 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/1 | best_piece_anywhere | 180 | 180 | yes |
| T/1 | control2 | not applicable | not applicable | yes |
| T/2 | status | nominated | nominated | yes |
| T/2 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/2 | piece_correct | 180 | 180 | yes |
| T/2 | whole_read_correct | 180 | 180 | yes |
| T/2 | reading | 0.0000 | 0.0000 | yes |
| T/2 | described_only | False | False | yes |
| T/2 | control1_complement | 0.0000 | 0.0000 | yes |
| T/2 | control1_holds | True | True | yes |
| T/2 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| T/2 | control4_holds | True | True | yes |
| T/2 | control7_holds | True | True | yes |
| T/2 | true_slot | 0.0000 | 0.0000 | yes |
| T/2 | rider | 0.0000 | 0.0000 | yes |
| T/2 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/2 | best_piece_anywhere | 180 | 180 | yes |
| T/2 | control2 | not applicable | not applicable | yes |
| C/0 | status | nominated | nominated | yes |
| C/0 | site_set | states (2,) at action, 8 directions | states (2,) at action, 4 directions | **no** |
| C/0 | piece_correct | 180 | 178 | **no** |
| C/0 | whole_read_correct | 180 | 180 | yes |
| C/0 | reading | 1.0051 | 1.0026 | **no** |
| C/0 | described_only | False | False | yes |
| C/0 | control1_complement | 0.5450 | 0.5437 | **no** |
| C/0 | control1_holds | — | — | yes |
| C/0 | control3_below_equal_above | [0, 0, 20] | [0, 1, 19] | **no** |
| C/0 | control4_holds | True | True | yes |
| C/0 | control7_holds | True | True | yes |
| C/0 | true_slot | — | — | yes |
| C/0 | rider | — | — | yes |
| C/0 | stricter | [[2], 'action', 8, 180] | [[2], 'action', 4, 178] | **no** |
| C/0 | best_piece_anywhere | 180 | 180 | yes |
| C/0 | control2 | no verdict | no verdict | yes |
| C/1 | status | nominated | nominated | yes |
| C/1 | site_set | states (1,) at action+3, 8 directions | states (4,) at action, 8 directions | **no** |
| C/1 | piece_correct | 172 | 178 | **no** |
| C/1 | whole_read_correct | 177 | 180 | **no** |
| C/1 | reading | 0.9926 | 1.0000 | **no** |
| C/1 | described_only | False | False | yes |
| C/1 | control1_complement | 0.5625 | 0.5587 | **no** |
| C/1 | control1_holds | — | — | yes |
| C/1 | control3_below_equal_above | [6, 1, 13] | [0, 0, 20] | **no** |
| C/1 | control4_holds | True | True | yes |
| C/1 | control7_holds | True | True | yes |
| C/1 | true_slot | — | — | yes |
| C/1 | rider | — | — | yes |
| C/1 | stricter | [[1], 'action+3', 8, 172] | [[4], 'action', 8, 178] | **no** |
| C/1 | best_piece_anywhere | 175 | 180 | **no** |
| C/1 | control2 | no verdict | no verdict | yes |
| C/2 | status | nominated | nominated | yes |
| C/2 | site_set | states (1,) at post-identity, 4 directions | states (1,) at post-identity, 4 directions | yes |
| C/2 | piece_correct | 150 | 165 | **no** |
| C/2 | whole_read_correct | 176 | 180 | **no** |
| C/2 | reading | 0.9974 | 1.0000 | **no** |
| C/2 | described_only | False | False | yes |
| C/2 | control1_complement | 0.5312 | 0.5400 | **no** |
| C/2 | control1_holds | — | — | yes |
| C/2 | control3_below_equal_above | [6, 5, 9] | [3, 3, 14] | **no** |
| C/2 | control4_holds | True | True | yes |
| C/2 | control7_holds | True | True | yes |
| C/2 | true_slot | — | — | yes |
| C/2 | rider | — | — | yes |
| C/2 | stricter | [[1], 'post-identity', 4, 150] | [[1], 'post-identity', 4, 165] | **no** |
| C/2 | best_piece_anywhere | 178 | 180 | **no** |
| C/2 | control2 | no verdict | no verdict | yes |
| M/0 | status | nominated | nominated | yes |
| M/0 | site_set | states (1,) at post-identity, 8 directions | states (3,) at action, 8 directions | **no** |
| M/0 | piece_correct | 180 | 180 | yes |
| M/0 | whole_read_correct | 180 | 180 | yes |
| M/0 | reading | 0.4886 | 0.5252 | **no** |
| M/0 | described_only | False | False | yes |
| M/0 | control1_complement | 0.3875 | 0.4200 | **no** |
| M/0 | control1_holds | — | — | yes |
| M/0 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| M/0 | control4_holds | True | True | yes |
| M/0 | control7_holds | True | True | yes |
| M/0 | true_slot | 0.4837 | 0.5000 | **no** |
| M/0 | rider | — | — | yes |
| M/0 | stricter | [[1], 'post-identity', 8, 180] | [[3], 'action', 8, 180] | **no** |
| M/0 | best_piece_anywhere | 180 | 180 | yes |
| M/0 | control2 | not applicable | not applicable | yes |
| M/1 | status | nominated | nominated | yes |
| M/1 | site_set | states (1,) at post-identity, 8 directions | states (1,) at post-identity, 8 directions | yes |
| M/1 | piece_correct | 180 | 180 | yes |
| M/1 | whole_read_correct | 180 | 180 | yes |
| M/1 | reading | 0.4860 | 0.4793 | **no** |
| M/1 | described_only | False | False | yes |
| M/1 | control1_complement | 0.3762 | 0.3762 | yes |
| M/1 | control1_holds | — | — | yes |
| M/1 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| M/1 | control4_holds | True | True | yes |
| M/1 | control7_holds | True | True | yes |
| M/1 | true_slot | 0.4760 | 0.4760 | yes |
| M/1 | rider | — | — | yes |
| M/1 | stricter | [[1], 'post-identity', 8, 180] | [[1], 'post-identity', 8, 180] | yes |
| M/1 | best_piece_anywhere | 180 | 180 | yes |
| M/1 | control2 | not applicable | not applicable | yes |
| M/2 | status | nominated | nominated | yes |
| M/2 | site_set | states (1,) at post-identity, 8 directions | states (1,) at post-identity, 8 directions | yes |
| M/2 | piece_correct | 180 | 180 | yes |
| M/2 | whole_read_correct | 180 | 180 | yes |
| M/2 | reading | 0.5449 | 0.5208 | **no** |
| M/2 | described_only | False | False | yes |
| M/2 | control1_complement | 0.4288 | 0.4100 | **no** |
| M/2 | control1_holds | — | — | yes |
| M/2 | control3_below_equal_above | [20, 0, 0] | [20, 0, 0] | yes |
| M/2 | control4_holds | True | True | yes |
| M/2 | control7_holds | True | True | yes |
| M/2 | true_slot | 0.4920 | 0.4920 | yes |
| M/2 | rider | — | — | yes |
| M/2 | stricter | [[1], 'post-identity', 8, 180] | [[1], 'post-identity', 8, 180] | yes |
| M/2 | best_piece_anywhere | 180 | 180 | yes |
| M/2 | control2 | not applicable | not applicable | yes |
| F/0 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/0 | site_set | states (1,) at post-identity, 1 directions | states (1,) at post-identity, 1 directions | yes |
| F/0 | piece_correct | 19 | 18 | **no** |
| F/0 | whole_read_correct | 32 | 34 | **no** |
| F/0 | reading | 1.0000 | 1.0000 | yes |
| F/0 | described_only | True | True | yes |
| F/0 | control1_complement | 0.4875 | 0.4850 | **no** |
| F/0 | control1_holds | — | — | yes |
| F/0 | control3_below_equal_above | [6, 7, 7] | [6, 7, 7] | yes |
| F/0 | control4_holds | True | True | yes |
| F/0 | control7_holds | True | True | yes |
| F/0 | true_slot | — | — | yes |
| F/0 | rider | — | — | yes |
| F/0 | stricter | — | — | yes |
| F/0 | best_piece_anywhere | 36 | 40 | **no** |
| F/0 | control2 | no verdict | reported; no pass line | **no** |
| F/1 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/1 | site_set | states (1,) at action+3, 4 directions | states (4,) at action, 1 directions | **no** |
| F/1 | piece_correct | 16 | 16 | yes |
| F/1 | whole_read_correct | 12 | 14 | **no** |
| F/1 | reading | 1.0000 | 1.0000 | yes |
| F/1 | described_only | True | True | yes |
| F/1 | control1_complement | 0.5637 | 0.5713 | **no** |
| F/1 | control1_holds | — | — | yes |
| F/1 | control3_below_equal_above | [2, 1, 17] | [0, 0, 20] | **no** |
| F/1 | control4_holds | True | True | yes |
| F/1 | control7_holds | True | True | yes |
| F/1 | true_slot | — | — | yes |
| F/1 | rider | — | — | yes |
| F/1 | stricter | — | — | yes |
| F/1 | best_piece_anywhere | 19 | 19 | yes |
| F/1 | control2 | no verdict | no verdict | yes |
| F/2 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/2 | site_set | states (1,) at post-identity, 8 directions | states (3,) at action, 1 directions | **no** |
| F/2 | piece_correct | 18 | 22 | **no** |
| F/2 | whole_read_correct | 18 | 30 | **no** |
| F/2 | reading | 1.0108 | 1.0000 | **no** |
| F/2 | described_only | True | True | yes |
| F/2 | control1_complement | 0.5387 | 0.5138 | **no** |
| F/2 | control1_holds | — | — | yes |
| F/2 | control3_below_equal_above | [8, 3, 9] | [4, 8, 8] | **no** |
| F/2 | control4_holds | True | True | yes |
| F/2 | control7_holds | True | True | yes |
| F/2 | true_slot | — | — | yes |
| F/2 | rider | — | — | yes |
| F/2 | stricter | — | — | yes |
| F/2 | best_piece_anywhere | 29 | 36 | **no** |
| F/2 | control2 | no verdict | no verdict | yes |

| seed | separation, arm C minus arm T: old | new |
|---|---|---|
| 0 | 1.0051 | 1.0026 |
| 1 | 0.9926 | 1.0000 |
| 2 | 0.9974 | 1.0000 |

Outcome term, old: substrate not a testbed; new: substrate not a testbed. Gates old {'C': True, 'F': False, 'M': True, 'T': True}, new {'C': True, 'F': False, 'M': True, 'T': True}.

## The competing solver: fitted on 420 (old) against 1,800 (new)

| reading / seed | old: best piece of 180, nomination, status | new: best piece of 180, nomination, status |
|---|---|---|
| channel_removed / 0 | 24, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 19, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_removed / 1 | 23, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_removed / 2 | 23, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 0 | 25, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 18, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 1 | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 2 | 21, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |

## The pre-stated concerns (method, section 6)

- A: a built model (arm T, C or M) loses its nomination: no
- B: arm T's reading is not 0.0000, or its control 1 does not hold: no
- C: the separation (arm C minus arm T) is below 0.5 or missing on a seed: no
- D: arm M's reading is outside 0.3 to 0.7 on a seed: no
- E: the free model's read reaches the floor (a piece of 144 or more anywhere): no
- F: the solver returns a reading: no
- G: control 7 or control 4 fails anywhere: no
- Reported, not a concern on its own: the chosen site set or size changed on C/0, C/1, M/0, F/1, F/2
