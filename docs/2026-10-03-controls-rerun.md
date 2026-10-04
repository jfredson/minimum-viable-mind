# The controls re-run under the registered rules: findings

*Written 2026-10-03 (Pacific) by the Claude Code session that ran it, on
branch `controls-rerun-2026-10-03`. The method,
`docs/controls-rerun-method-2026-10-03.md`, and the code,
`experiments/rehearsal-successor-measure/src/rerun_controls.py`, were
committed and pushed with no output at `f2d836b`, before the run. The code
was not changed between that commit and the run. Laptop, processor only.
Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-controls-rerun/`, and the table
is the script's own. Sentences that explain a figure are marked **ARGUED**.
This is a rehearsal record on twelve particular trained toy models. Figures
for the entangled, free and mixed models (arms C, F and M) are properties of
those models, not of the code
(`docs/rulings/2026-09-23-range-and-direction-only.md`).*

*This session also wrote the review, the ruling packet and the ruling record
this run follows from. It is owed a check by a session that did not write or
run it, which re-runs the script from the committed code.*

## 1. The short version

- **No stop fired.** Every model file matched its committed fingerprint; the
  null transplant left every output bit-identical at every site set; every
  built model read on every seed; the free model read on none.
- **The ruled change works on the toy.** With only pieces that themselves
  carry the label allowed, arm T (separable) reads 0.0000 on every seed, arm
  C (entangled) reads **1.0051, 0.9926 and 0.9974**, and arm M (mixed) reads
  0.4886, 0.4860 and 0.5449. The separation between arm C and arm T clears 0.5
  on every seed. Arm F (free) returns "no verdict, read failed its floor" on
  every seed: its best piece is right on 34 of 180 held-out episodes against
  144 needed.
- **One prediction of this session's was wrong.** On arm C seed 1 the method
  file predicted layer 4 at the action position; the rule chose layer 1 at
  the action position and the three before it. Section 3.
- **Two things go to John.**
  1. **Control 2, the other-agent control, has no figure on any toy model,
     and cannot have one.** The one model that learned the other-agent
     condition (arm F seed 0) has a read of the named agent's marker that
     misses the floor (at best 137 of 180 for the whole read). Its tolerance
     of 0.05, ruled on 2026-10-03, has therefore never been exercised.
     Section 5.
  2. **Control 4, the too-early-position control, comes back above "nothing"
     on six of twelve models, and an after-the-fact diagnostic says the
     cause is the control and not the models.** It transplants at positions
     before the *recipient's* first own turn; in about half the pairs the
     donor twin's first own turn comes earlier, so the donor's state there
     already carries who the donor is. Restricted to positions before both
     twins' first own turns, the control returns exactly the no-transplant
     rate on all twelve. That diagnostic was not pre-stated. Section 6.

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ ../../../.venv/bin/python rerun_controls.py
...
done in 967s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. The script's
table, as it printed it (also `out-controls-rerun/table.md`). "Whole read /
piece" is the count correct of 180 held-out development episodes, for the
whole straight-line read and for the transplanted piece. For arm F the site
set shown is the one the rule would choose with the piece requirement switched
off, as the method's rule 12 says, and its number is in parentheses and is
not a reading.

| arm/seed | status | site set | whole read / piece, correct of 180 | whole, ownership-only, untouched | reading | control 1 complement | control 3 median, 95th; below/equal/above | control 4 share (minus untouched) | control 6 same moved (n), different moved (n) | control 7 | control 2 | true slot | rider |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T/0 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| T/1 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| T/2 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| C/0 | nominated | layers (2,) at action, 8 directions | 180 / 180 | 0.5400, 0.0488, 0.0512 | 1.0051 | 0.5450 | 0.0587, 0.0639; 0/0/20 | 0.0537 (+0.0025) | 0.5062 (81), 0.8220 (719) | identical | no verdict |  | no verdict (whole 0.0512) |
| C/1 | nominated | layers (1,) at action+3, 8 directions | 177 / 172 | 0.5550, 0.0525, 0.0488 | 0.9926 | 0.5625 | 0.0550, 0.0575; 6/1/13 | 0.0500 (+0.0013) | 0.6296 (81), 0.8860 (719) | identical | no verdict |  | no verdict (whole 0.0488) |
| C/2 | nominated | layers (1,) at post-identity, 4 directions | 176 / 150 | 0.5463, 0.0612, 0.0600 | 0.9974 | 0.5312 | 0.0612, 0.0663; 6/5/9 | 0.1313 (+0.0713) | 0.5679 (81), 0.9138 (719) | identical | no verdict |  | no verdict (whole 0.0600) |
| F/0 | read failed its floor: no size's piece reaches four fifths | layers (1,) at post-identity, 1 directions | 32 / 22 | 0.4850, 0.0587, 0.0587 | (1.0000) reported for description; no reading | 0.4838 | 0.0587, 0.0625; 6/7/7 | 0.1375 (+0.0788) | 0.7284 (81), 0.8999 (719) | identical | no verdict |  | no verdict (whole 0.0587) |
| F/1 | read failed its floor: no size's piece reaches four fifths | layers (1,) at action+3, 4 directions | 12 / 17 | 0.5675, 0.0563, 0.0563 | (1.0000) reported for description; no reading | 0.5637 | 0.0587, 0.0650; 2/1/17 | 0.0612 (+0.0050) | 0.6790 (81), 0.8790 (719) | identical | no verdict |  | no verdict (whole 0.0563) |
| F/2 | read failed its floor: no size's piece reaches four fifths | layers (1,) at post-identity, 8 directions | 18 / 18 | 0.5300, 0.0638, 0.0688 | (1.0108) reported for description; no reading | 0.5400 | 0.0638, 0.0664; 8/3/9 | 0.1338 (+0.0650) | 0.6296 (81), 0.8915 (719) | identical | no verdict |  | no verdict (whole 0.0688) |
| M/0 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7800, 0.4050, 0.0125 | 0.4886 | 0.3875 | 0.0150, 0.0190; 20/0/0 | 0.1138 (+0.1013) | 0.2222 (81), 0.9499 (719) | identical | not applicable | 0.4837; formula 0.4837 | no verdict (whole 0.4088) |
| M/1 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7738, 0.4062, 0.0175 | 0.4860 | 0.3762 | 0.0187, 0.0226; 20/0/0 | 0.0975 (+0.0800) | 0.2716 (81), 0.9360 (719) | identical | not applicable | 0.4760; formula 0.4760 | no verdict (whole 0.4138) |
| M/2 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7937, 0.3688, 0.0138 | 0.5449 | 0.4288 | 0.0150, 0.0213; 20/0/0 | 0.0988 (+0.0850) | 0.3210 (81), 0.9485 (719) | identical | not applicable | 0.4920; formula 0.4920 | no verdict (whole 0.4100) |

separation, arm C minus arm T: {"0": {"C_minus_T": 1.0051150895140666, "clears_0_5": true}, "1": {"C_minus_T": 0.9925925925925926, "clears_0_5": true}, "2": {"C_minus_T": 0.9974293059125964, "clears_0_5": true}}

## 3. The nomination under the ruled change

| Arm and seed | Expected (method, section 4) | What the rule chose | Piece, correct of 180 |
|---|---|---|---|
| T, every seed | layer 0, `action`, 8 directions | the same | 180 |
| M, every seed | layer 1, `post-identity`, 8 directions | the same | 180 |
| C seed 0 | layer 2, 8 directions | layer 2, `action`, 8 directions | 180 |
| C seed 1 | **layer 4**, 8 directions | **layer 1, `action+3`, 8 directions** | 172 |
| C seed 2 | layer 1, 4 directions | layer 1, `post-identity`, 4 directions | 150 |
| F, every seed | no size reaches four fifths | the same | at most 34 |

**The miss on arm C seed 1.** This session had assumed the site would stay
where the proposal's rule put it (layer 4 at the action position) and only the
size would change. The candidates are one layer set per position set, and
once the small pieces are excluded the highest development ownership-only
share is 0.0533 at layer 1, 8 directions, at both `action+3` and
`post-identity`, against 0.0517 at layer 4, 8 directions, at `action`
(`out-controls-rerun/nominate_C_seed1.json`, `candidates`). The tie goes to
the earlier position set. Those shares differ by one episode of 600: on an
arm where nothing moves the action, the choice among candidates is still made
among sampling noise, as the review's finding RT-235 says. What the ruled
change fixes is that whichever candidate wins, its piece carries the label.
The reading at the chosen site is 0.9926; at layer 4 it would have been
0.9975 (the review, finding RT-230).

**One thing the rule as run does not check.** On arm C seeds 1 and 2 the
chosen position set covers several positions, and the piece's accuracy is
taken at the action position only (the method's rule 7, this session's
reading). The review measured the one-direction piece on seed 2 at the other
positions and found it far lower there. The 4- and 8-direction pieces were
not measured at the other positions in this run.

**The free arm on the processor.** Its whole read is right on 32, 12 and 18 of
180 at the layers shown, and no piece at any layer of any seed exceeds 34
(`nominate_F_seed*.json`, `fits`). The committed figures from the graphics
chip were 31, 12 and 19 (0.172, 0.067, 0.106).

## 4. The controls that came back as expected

- **Control 7, the null transplant (holds):** bit-identical on all twelve
  primary site sets, on the nine stricter-row site sets, and on arm F's three
  described ones (`measure_*_seed*.json`, `controls.7`).
- **The no-transplant rule (holds):** inside the 0.018 allowance on all
  twelve. The largest miss is 0.0132, arm C seed 0.
- **Control 1, the complement of the piece (holds on arm T):** arm T 0.0000
  on every seed. Arm C: 0.5450, 0.5625 and 0.5312 against whole-state shares
  of 0.5400, 0.5550 and 0.5463, so the complement does about what the whole
  state does, as expected of an entangled model. Arm M: 0.3875, 0.3762 and
  0.4288 against 0.78; about half, which is what a mixture would give (ARGUED).
- **Control 3, twenty random pieces (reported):** arms T and M above all
  twenty on every seed; arm C below all twenty on seed 0 and among them on
  seeds 1 and 2; arm F among them.
- **Control 6, on the relaxed set (reported):** both cells have trials, 81
  and 719. Arm T moves nothing in the same-value cell and everything in the
  other. The same-value cell moves on arm C (0.51 to 0.63), arm M (0.22 to
  0.32) and arm F (0.63 to 0.73), as the proposal's weakness W11 expects: on
  those models the whole-state transplant carries more than who is acting.
- **The true-slot reference:** arm T 0.0000; arm M 0.4837, 0.4760 and 0.4920,
  the route formula agreeing to four decimals, and the blind reading within
  0.10 of it on every seed (0.0049, 0.0100, 0.0529).
- **The rider:** at arm T's site set, arms C and F return no verdict with the
  whole-state transplant at the no-transplant rate, and arm M returns no
  verdict with about 0.41 moved, the two different reasons the proposal
  describes.
- **The stricter row** changes only arm T, to layer 1, still 0.0000.
- **The whole-state floor on fresh episodes** clears on all twelve.

## 5. Control 2 has no figure, on any model

The method expected it to run on arm F seed 0 only. It did not run there
either.

```
F/0 control 2: status 'no verdict', reason "read failed its floor: no size's piece reaches four fifths",
               named_other_correct 994, dev_named_other_accuracy 0.3217, dev_untouched 0.1933
named read, correct of 180, whole read then pieces of 1 / 2 / 4 / 8 directions:
  layer 0:  16 | 20 / 16 / 16 / 16
  layer 1:  95 | 22 / 43 / 74 / 92
  layer 2: 137 | 40 / 64 / 96 / 139
  layer 3: 127 | 31 / 50 / 79 / 115
  layer 4: 102 | 38 / 51 / 67 / 102
```

(`out-controls-rerun/measure_F_seed0.json`, `control2`.) The straight-line
read of the named agent's marker at the other-agent action never reaches 144
of 180: at best 137 for the whole read, at layer 2. So this is not an effect
of the ruled change. Under the proposal's earlier rule, with the floor on the
whole read, it would also have returned no verdict.

The other eleven: arms T and M are not applicable by ruling; arm C on every
seed and arm F seeds 1 and 2 have not learned the other-agent condition (760,
751, 708, 781 and 746 of 3,000 against 790).

**Why this goes to John.** Control 2 is frozen by the registration with a
tolerance of 0.05. Item 5 of the ruling of 2026-09-21 makes a pre-stated
quantity the rehearsal never exercised a fatal finding at the registration
review. This run was meant to exercise it and has shown that the toy cannot.
The options, none of them this session's to take: register control 2 as a
reported control whose no verdict is expected, saying in terms that it was
never exercised at toy scale; drop it; or exercise it on a made-up case
built for the purpose.

## 6. Control 4 comes back above nothing, and why

As run, control 4 is above the no-transplant rate by 0.065 to 0.10 on arm M
(every seed), arm C seed 2 and arm F seeds 0 and 2, and by 0.005 or less on
the rest. Those six are exactly the ones whose site set is layer 1 at the
`post-identity` position set, which reaches back to the model's first own
turn.

**After the output was seen**, this session wrote a diagnostic,
`src/posthoc_control4.py`. **It was not pre-stated**, it changes nothing in
the re-run, and it is labelled post hoc in its own first line.

```
$ ../../../.venv/bin/python posthoc_control4.py
pairs where the donor's first own turn comes before the recipient's: 0.5088
arm/seed | layers | untouched | control 4 as run | positions before both twins' first own turn
T/0 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
T/1 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
T/2 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
C/0 | (2,) | 0.0512 | 0.0537 (+0.0025) | 0.0512 (+0.0000)
C/1 | (1,) | 0.0488 | 0.0500 (+0.0013) | 0.0488 (+0.0000)
C/2 | (1,) | 0.0600 | 0.1313 (+0.0713) | 0.0600 (+0.0000)
F/0 | (1,) | 0.0587 | 0.1375 (+0.0788) | 0.0587 (+0.0000)
F/1 | (1,) | 0.0563 | 0.0612 (+0.0050) | 0.0563 (+0.0000)
F/2 | (1,) | 0.0688 | 0.1338 (+0.0650) | 0.0688 (+0.0000)
M/0 | (1,) | 0.0125 | 0.1138 (+0.1013) | 0.0125 (+0.0000)
M/1 | (1,) | 0.0175 | 0.0975 (+0.0800) | 0.0175 (+0.0000)
M/2 | (1,) | 0.0138 | 0.0988 (+0.0850) | 0.0138 (+0.0000)
```

The control transplants the donor twin's state at the positions before the
recipient's first own turn. The twins are different agents, and in 0.5088 of
pairs the donor's first own turn is the earlier one, so at some of those
positions the donor's state already carries the donor's identity. With the
positions restricted to those before both twins' first own turns, the control
returns exactly the no-transplant rate on all twelve models.

**What that suggests (ARGUED, and John's to rule).** The proposal's account,
that arms C and F "receive the ownership signal by other routes", is not what
the diagnostic shows; the control was transplanting at positions where the
identity is already known, in the donor. Defined on both twins, control 4
does what it was written to do. John ruled on 2026-10-03 (the proposal's
decision 16) that it is reported and cannot veto, on the earlier account.
Whether to redefine its positions, and whether it could then hold again, is a
new question for him. The diagnostic is one after-the-fact run and is owed
the same check as the rest.

## 7. Against the method's stops

| Stop | Fired? |
|---|---|
| K1, a model file does not match its fingerprint | No |
| K2, the null transplant fails anywhere | No |
| K3, an arm T, C or M seed returns no verdict | No |
| K4, arm F reads on any seed | No |

## 8. What this run does and does not settle for the registration review

**Settled, subject to the check:** under the registered rules with the ruled
change, controls 1, 3, 4, 6 and 7 have figures on every arm and seed; the
readings and the separation hold; arm M's true-slot check holds.

**Not settled:** control 2 (section 5); control 4's definition (section 6);
whether a multi-position piece should be checked at every position it is
transplanted at (section 3). The first is a blocker under item 5 of the
2026-09-21 ruling until John rules how it is registered.

## 9. Files

`experiments/rehearsal-successor-measure/out-controls-rerun/`:
`nominate_{arm}_seed{seed}.json` (the fits, the full development grid, the
candidates, the primary and stricter choices), `measure_{arm}_seed{seed}.json`
(everything on fresh episodes), `summary.json`, `table.md`. Code:
`src/rerun_controls.py` (unchanged since `f2d836b`) and
`src/posthoc_control4.py` (post hoc).
