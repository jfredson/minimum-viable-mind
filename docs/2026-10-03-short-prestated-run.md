# The short pre-stated run: findings

*Written 2026-10-03 (Pacific) by the Claude Code checking session that ran
it, on branch `w2a-job2-short-prestated-run`. The method,
`docs/2026-10-03-short-prestated-run-method.md`, and the code,
`experiments/rehearsal-successor-measure/src/short_prestated_run.py`, were
committed and pushed with no output at `eb13dba`, before the run. **The code
was not changed after that commit; it ran as committed, first time.** Laptop,
processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-short-prestated-run/`, and the
tables are the script's own. Sentences that explain a figure are marked
**ARGUED**. This is a rehearsal record on twelve particular trained toy
models. Figures for the entangled, free and mixed models are properties of
those models, not of the code.*

**What this session opened and what it did not.** Committed files only (the
list is in the method file). It did not open any chat or transcript of the
session that wrote the rulings, the re-run or the diagnostic. It is not the
session that wrote the diagnostic. It did write the check of the re-run
(pull request 79) before this, and the method says what it had already seen
because of that. **This run was written and run by one session and is owed a
check by another.**

## 1. The short version

- **(a) The too-early-position control, as redefined, holds on all twelve
  models.** The model's outputs with the transplant are bit-identical to its
  outputs without it. Expected, and by construction: section 3.
- **(b) The new reported figure is filled for all twelve, and it is not
  flattering.** Away from the action position the chosen piece often does not
  carry the label at four fifths, **including on the mixed model, where this
  session's expectation was wrong.** No pass line applies. One thing here is
  John's: how the registered column is to be computed, because two fair ways
  of computing it disagree about the mixed model. Section 4.
- **(c) NOT A RESULT.** The other-agent control's code ran end to end on the
  free model's seed 0 with the accuracy floor switched off, and returned its
  figures. That is all it shows. Section 5.
- **No stop fired.**

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python short_prestated_run.py
...
done in 71s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. (The method
gives the command with the relative path `../../../.venv/bin/python`; this
session ran from a separate working folder, where the project's Python is
reached by its full path. Same program.) Everything the run printed is in
`out-short-prestated-run/stdout.txt`.

## 3. Part (a): the too-early-position control, positions before both twins' first own turns

The script's table (`out-short-prestated-run/table.md`, from `part_a.json`):

| arm/seed | layers | outputs bit-identical (holds) | share landing on the donor's value | no-transplant share | trials whose action changed |
|---|---|---|---|---|---|
| T/0 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| T/1 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| T/2 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| C/0 | (2,) | identical | 0.0512 | 0.0512 | 0 |
| C/1 | (1,) | identical | 0.0488 | 0.0488 | 0 |
| C/2 | (1,) | identical | 0.0600 | 0.0600 | 0 |
| F/0 | (1,) | identical | 0.0587 | 0.0587 | 0 |
| F/1 | (1,) | identical | 0.0563 | 0.0563 | 0 |
| F/2 | (1,) | identical | 0.0688 | 0.0688 | 0 |
| M/0 | (1,) | identical | 0.0125 | 0.0125 | 0 |
| M/1 | (1,) | identical | 0.0175 | 0.0175 | 0 |
| M/2 | (1,) | identical | 0.0138 | 0.0138 | 0 |

(T, C, F and M are the separable, entangled, free and mixed models.) Also in
`part_a.json`, for every model: the largest difference between any two output
numbers is 0.0; a null transplant at the same positions is bit-identical; the
twins' states at those layers and positions are identical. Across the 800
pairs the control transplants at between 1 and 21 positions per pair, about
5 on average (`positions_per_pair`), never none, so it is never an empty test.

**Against what was expected.** As expected on every line. The method said in
advance that this was not a blind prediction: this session had already
observed it with different code.

**What it means (ARGUED).** The control holds, and it holds for a reason that
has nothing to do with these models: before either twin has been told a turn
is its own, the two have read the same input, so the state being transplanted
is the state already there. The control as redefined is a known-answer test
of the pairing and the code. **For the registration it should be described
that way, and not as evidence that a model does not yet know its identity.**

## 4. Part (b): the chosen piece's accuracy at the other positions of its site

**Reported only. No pass line.** Each cell is *whole state / piece*: how many
of 180 held-out development episodes a fresh straight-line read gets right,
given the whole state at that position, and given only the state's
coordinates inside the chosen piece. For comparison, the rule at the action
position asks for 144. The free model's rows are at the site the re-run used
for description; it has no reading.

| arm/seed | site set | at the action position | at each other position | average over the other positions |
|---|---|---|---|---|
| T/0, T/1, T/2 | layer 0 at the action position, 8 directions | 180 / 180 | single position | |
| C/0 | layer 2 at the action position, 8 directions | 180 / 180 | single position | |
| C/1 | layer 1 at the action position and the three before it, 8 directions | 177 / 172 | 1 before: 180 / 139; 2 before: 179 / 139; 3 before: 179 / 33 | 179 / 113 |
| C/2 | layer 1 from the first own turn to the action, 4 directions | 176 / 150 | first own turn, tokens 1 to 5: 180 / 63; 180 / 82; 167 / 46; 149 / 30; 180 / 84. Before the action, 5 to 1: 180 / 71; 180 / 112; 180 / 129; 180 / 88; 180 / 139 | 180 / 123 |
| F/0 (described only) | layer 1 from the first own turn to the action, 1 direction | 32 / 22 | first own turn, tokens 1 to 5: 180 / 21; 66 / 15; 31 / 15; 61 / 18; 51 / 15. Before the action, 5 to 1: 32 / 14; 21 / 13; 21 / 18; 26 / 15; 41 / 17 | 91 / 25 |
| F/1 (described only) | layer 1 at the action position and the three before it, 4 directions | 12 / 17 | 1 before: 22 / 14; 2 before: 20 / 20; 3 before: 24 / 23 | 19 / 11 |
| F/2 (described only) | layer 1 from the first own turn to the action, 8 directions | 18 / 18 | first own turn, tokens 1 to 5: 180 / 145; 85 / 36; 46 / 13; 99 / 17; 51 / 22. Before the action, 5 to 1: 11 / 18; 28 / 18; 14 / 21; 16 / 16; 43 / 19 | 73 / 25 |
| M/0 | layer 1 from the first own turn to the action, 8 directions | 180 / 180 | first own turn, tokens 1 to 5: 180 / 151; 180 / 153; 178 / 95; 179 / 34; 180 / 130. Before the action, 5 to 1: 180 / 67; 180 / 148; 180 / 180; 179 / 133; 180 / 120 | 180 / 163 |
| M/1 | the same | 180 / 180 | first own turn, tokens 1 to 5: 180 / 151; 180 / 136; 180 / 119; 177 / 71; 178 / 124. Before the action, 5 to 1: 180 / 171; 180 / 177; 180 / 143; 174 / 143; 180 / 172 | 180 / 174 |
| M/2 | the same | 180 / 180 | first own turn, tokens 1 to 5: 180 / 174; 180 / 152; 179 / 102; 177 / 33; 180 / 162. Before the action, 5 to 1: 180 / 178; 179 / 157; 180 / 174; 175 / 136; 180 / 172 | 180 / 175 |

(The script's own table, with the same figures one row per model, is
`out-short-prestated-run/table.md`; the figures are in `part_b.json`. "The
average over the other positions" is the read taken on the state averaged
over every position of the site except the action position.)

**Against what was expected, line by line.**

- *The action-position figures equal the re-run's on all twelve.* **Yes**
  (`matches_the_controls_rerun` true on all twelve). Stop S3 did not fire.
- *The separable model and the entangled model's seed 0 have a single
  position.* **Yes.**
- *At the first token of the first own turn the whole state is right on
  nearly all 180, on every model with a span site.* **Yes:** 180 of 180 on
  all six.
- *The mixed model's piece is right on at least 144 at most of the ten
  positions and on the average.* **Wrong on the first half, right on the
  second.** On the average: 163, 174 and 175. Position by position the piece
  reaches 144 at only 4 of 10 positions on seed 0, 4 of 10 on seed 1 and 7 of
  10 on seed 2. At the fourth token of the model's first own turn (the value
  word) it is right on 34, 71 and 33 of 180. **This session expected better
  and is writing down that it was wrong.**
- *The entangled model's seeds 1 and 2: a guess, low confidence, that the
  piece falls below 144 at one or more other positions.* **Yes, and by more
  than guessed.** Seed 1: 139, 139 and 33. Seed 2: below 144 at all ten, from
  30 to 139; 123 on the average.
- *The free model: about 21, 71 and 145 at the first token of its first own
  turn; well under 144 elsewhere.* 21 and 145 on seeds 0 and 2, as seen
  beforehand. **The 71 for seed 1 was this session's mistake in the method:**
  seed 1's site is the action position and the three before it, so it has no
  first-own-turn figure in this table. Everywhere else the free model's piece
  is between 11 and 36 of 180.

**What this does and does not show (ARGUED).**

- At every position of every span site the **whole state** holds the label
  (149 to 180 of 180 on the built models). So a low piece figure there means
  the label is present and is not held in the chosen directions at that
  position. That is what the ruling packet anticipated: directions fitted
  where the model acts need not be the ones that hold the label at its
  earlier turns.
- It bears on one sentence a reader might write: "the piece held the label
  and the transplant of it did nothing" (the entangled model) or "did half"
  (the mixed model). **On this evidence that sentence is true at the action
  position and not true across the whole site**, for the entangled model's
  seeds 1 and 2 and, position by position, for the mixed model too. John
  ruled that this is reported and not gated; this is the report.
- It does not change any reading. The readings come from what the
  transplants do to the action, and those are unchanged.
- **A limit of the figures.** Each is a fresh read fitted on 420 episodes
  with twelve possible answers, in a piece of 4 or 8 directions. A figure
  like 139 against 144 is a few episodes and should not be read finely.

**One thing that is John's.** The ruling says "the chosen piece's accuracy at
the other positions of its site" and does not say how it is computed. The
method chose position by position, plus the average, and marked that as this
session's reading. **The two give different pictures of the mixed model:** on
the average its piece clears four fifths on every seed; position by position
it does not at three to six of ten positions. Whichever goes in the
registered reporting table should be chosen and named before the registered
runs, and this session's suggestion (ARGUED) is to print both, since each
hides something the other shows. Not reported at all here: the positions in
the middle of a span, which do not line up from one episode to the next and
are covered only through the average.

## 5. Part (c): the other-agent control's code path. NOT A RESULT

**This is a test that the code runs end to end. It is not a result, and its
figures are not a pass or a fail of anything.** The read of the named agent's
marker on this model misses its floor, so the piece transplanted here is not
known to carry the named agent at all, and John withdrew the control's pass
line on 2026-10-03.

What was run: the re-run's own function for the control
(`rerun_controls.control2`), unchanged, called once for the free model's seed
0 with the piece's accuracy floor set to zero for that one call.

What it returned (`out-short-prestated-run/part_c_NOT_A_RESULT.json`):

```
(c) NOT A RESULT. F/0 with the floor switched off: ran end to end True
    site set: layer 1, the action position and the three before it, 8 directions
              (piece right on 92 of 180, whole read on 95; the floor would have asked for 144)
    own-directed action moved in 0.0012 of trials; under a random piece 0.0063
    named-other action moved in 0.0962 of trials
```

- *Expected: it runs end to end and returns the site set and three shares.*
  **Yes.** Stop S4 did not fire. No figure was predicted and none is
  interpreted.
- The pass-or-fail label the function attaches was dropped from the output
  file, as the method said it would be.
- **What is now true that was not before:** every line of the other-agent
  control's code has been executed once, on the processor, at $0. The
  registered run will not be the first time it runs.
- **What is still true:** the control has never been exercised on a model
  whose read of the named agent clears its floor. Nothing here changes that.

## 6. Against the method's stops

| Stop | Fired? |
|---|---|
| S1, a model file does not match its fingerprint | No |
| S2, part (a) not bit-identical on any model | No |
| S3, an action-position figure differs from the re-run's | No |
| S4, part (c) returns no verdict or raises an error | No |

## 7. What this run settles, and what it leaves

**Settled, subject to a check by another session:** the redefined
too-early-position control has been run as a pre-stated quantity and holds on
all twelve toy models; the new column is filled for all twelve; the
other-agent control's code has run end to end. Those were the three things
the ruling of 2026-10-03 asked for before the registration review.

**Left for John:** how the new column is computed in the registered table
(section 4). **Left for version 4 of the proposal:** to describe the
redefined control as a known-answer test (section 3), and to say plainly that
the piece's four fifths is established at the action position only
(section 4).

## 8. Files

`experiments/rehearsal-successor-measure/out-short-prestated-run/`:
`part_a.json`, `part_b.json`, `part_c_NOT_A_RESULT.json`, `table.md`,
`stdout.txt`. Code: `src/short_prestated_run.py`, unchanged since `eb13dba`.
