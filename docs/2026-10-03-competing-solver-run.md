# The ordinary competing solver under the rules as now ruled: findings

*Written 2026-10-03 (Pacific) by the Claude Code session that wrote and ran
it, on branch `w2b-job1-competing-solver-run`, cut from the main line at
`41b0bd3`. The method, `docs/2026-10-03-competing-solver-run-method.md`, and
the code, `experiments/rehearsal-successor-measure/src/competing_solver_run.py`,
were committed and pushed with no output at `744a8b3`, before the run. **The
code was not changed after that commit; it ran as committed, first time.**
Laptop, processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-competing-solver-run/`, and the
tables are the script's own. Sentences that explain a figure are marked
**ARGUED**. This is a rehearsal record on three particular trained toy
models; its figures are properties of those models.*

**What this session opened and what it did not.** The same as the method's
list: committed files only, at `41b0bd3`. It did not open the other record of
the seven-question ruling, any ruling packet, or any chat or transcript of
another session. **This run was written and run by one session and is owed a
check by a session that did not write it** (ruling 7 requires that check
before the registration review).

## 0. Said first, as the method asks

- **No reading was returned on any seed, under either reading of the
  solver.** Stop B2 did not fire. No other stop fired.
- **Two figures surprised this session and are written down here, unchanged**
  (section 4). The whole-state floor is not what holds this solver back by
  any margin. On seeds 0 and 1 the floor asks for less than nothing, and the
  check treats that as a miss. Under the second reading, on seed 2, **33 of
  45 site sets clear the floor on fresh episodes**, by one or two episodes of
  800, while none clears on development episodes. The nomination is made on
  development episodes, so nothing was nominated; and had it been, the piece
  rule would have refused every size by a wide margin (best piece 21 of 180).

## 1. The short version

- **The expected result came back: no verdict on every seed.** Its reason is
  the first kind on every seed and both readings: "no site set clears the
  whole-state floor". The stricter row says the same.
- **The read of the solver's own marker word is near chance.** The whole read
  is right on 11 to 21 of 180 held-out episodes; the best piece at any layer
  and size on 20 to 25. The piece rule asks for 144.
- **The gate, recomputed on the processor, matches the committed figures
  exactly** under the primary reading: 702, 715 and 702 of 3,000 on the
  own-directed condition, 712, 726 and 650 on the named-other. The bar is 790.
- **Under the primary reading the twins are one input**, so every transplant
  puts back the state already there. That no verdict follows from the pairing
  and is a test of the code more than of the solver, as the method said. The
  second reading, which feeds the solver its unused acting channel, is the
  one that tests the solver, and it also returns no verdict.
- **The no-transplant rule fails on every seed** (about 0.22 to 0.25 against
  a formula's 0.11), as predicted. It would withhold a reading on its own.
- **Description only:** with no floor applied, the arithmetic under the
  primary reading is zero divided by zero at all 180 comparisons. Under the
  second reading it comes to **1.0000** at most comparisons, the figure an
  entangled model gives. Section 5 says why that is noise and what it shows.

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python competing_solver_run.py > ../out-competing-solver-run/stdout.txt 2>&1
...
done in 839s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. (The method
gives the project's Python by a relative path; this session ran from its own
worktree, where it is reached by its full path. Same program.) The three
model files matched `SHA256SUMS` before any was loaded. Everything the run
printed is in `out-competing-solver-run/stdout.txt`.

"Reading A" is the method's primary reading: the solver's acting channel is
removed, as it was in training and scoring. "Reading B" feeds it the channel,
as a registered procedure handed the file would. Both are defined in the
method, section 3, as this session's reading and John's to overturn.

## 3. The figures, per seed

### 3.1 The read: correct of 180 held-out development episodes, every layer

Reading A, the primary reading:

| seed | layer | whole read | piece, 1 direction | 2 | 4 | 8 |
|---|---|---|---|---|---|---|
| 0 | 0 | 13 | 13 | 13 | 13 | 13 |
| 0 | 1 | 16 | 20 | 23 | 20 | 11 |
| 0 | 2 | 20 | 17 | 20 | 24 | 23 |
| 0 | 3 | 19 | 19 | 12 | 16 | 17 |
| 0 | 4 | 20 | 14 | 15 | 21 | 18 |
| 1 | 0 | 13 | 13 | 13 | 13 | 13 |
| 1 | 1 | 16 | 12 | 9 | 19 | 15 |
| 1 | 2 | 11 | 15 | 23 | 11 | 14 |
| 1 | 3 | 16 | 11 | 13 | 11 | 21 |
| 1 | 4 | 15 | 18 | 15 | 14 | 10 |
| 2 | 0 | 13 | 14 | 13 | 13 | 13 |
| 2 | 1 | 13 | 18 | 16 | 19 | 17 |
| 2 | 2 | 20 | 22 | 23 | 16 | 16 |
| 2 | 3 | 21 | 15 | 18 | 19 | 20 |
| 2 | 4 | 16 | 14 | 13 | 17 | 20 |

Reading B, for description:

| seed | layer | whole read | piece, 1 direction | 2 | 4 | 8 |
|---|---|---|---|---|---|---|
| 0 | 0 | 13 | 13 | 14 | 14 | 14 |
| 0 | 1 | 16 | 20 | 23 | 19 | 11 |
| 0 | 2 | 20 | 17 | 21 | 25 | 23 |
| 0 | 3 | 20 | 19 | 12 | 16 | 18 |
| 0 | 4 | 20 | 13 | 14 | 22 | 17 |
| 1 | 0 | 13 | 14 | 13 | 13 | 13 |
| 1 | 1 | 16 | 12 | 11 | 17 | 13 |
| 1 | 2 | 12 | 18 | 20 | 11 | 11 |
| 1 | 3 | 16 | 11 | 13 | 10 | 17 |
| 1 | 4 | 15 | 18 | 14 | 14 | 10 |
| 2 | 0 | 13 | 14 | 13 | 13 | 13 |
| 2 | 1 | 14 | 18 | 18 | 20 | 17 |
| 2 | 2 | 20 | 19 | 20 | 16 | 16 |
| 2 | 3 | 20 | 16 | 17 | 15 | 21 |
| 2 | 4 | 15 | 14 | 12 | 18 | 19 |

(A piece is sometimes right on more episodes than the whole read. Each is a
fresh read fitted on 420 episodes with twelve possible answers, and near
chance a smaller read can land a few episodes higher. ARGUED.)

### 3.2 Nomination and status

| seed, reading | gate: own, named-other, of 3,000 (bar 790) | site sets clearing the whole-state floor, development / fresh, of 45 | best piece of 180 (band sampling alone would put round it) | nomination | stricter row | status |
|---|---|---|---|---|---|---|
| 0, A | 702, 712 | 0 / 0 | 24 (16 to 34) | no site set clears the whole-state floor | the same | **no verdict** |
| 1, A | 715, 726 | 0 / 0 | 23 (16 to 33) | the same | the same | **no verdict** |
| 2, A | 702, 650 | 0 / 0 | 23 (16 to 33) | the same | the same | **no verdict** |
| 0, B | 707, 710 | 0 / 0 | 25 (17 to 35) | the same | the same | **no verdict** |
| 1, B | 716, 722 | 0 / 0 | 20 (13 to 30) | the same | the same | **no verdict** |
| 2, B | 698, 653 | 0 / **33** | 21 (14 to 31) | the same | the same | **no verdict** |

On every seed and both readings: the null transplant is bit-identical at all
45 site sets on fresh episodes (stop B4 did not fire). Under reading A the
twins' inputs and states are identical on development and fresh episodes,
largest difference 0.0 (stop B3 did not fire). Under reading B they differ,
and the twins' own-directed actions differ on 3 to 12 trials of 600 or 800.

### 3.3 The no-transplant rate against its formula, fresh episodes

| seed, reading | rate | (1 − accuracy) ÷ 7 | inside the 0.018 allowance |
|---|---|---|---|
| 0, A | 0.2487 | 0.1107 | no |
| 1, A | 0.2300 | 0.1116 | no |
| 2, A | 0.2200 | 0.1109 | no |
| 0, B | 0.2500 | 0.1107 | no |
| 1, B | 0.2313 | 0.1116 | no |
| 2, B | 0.2225 | 0.1109 | no |

### 3.4 Against what was expected (the method, section 6)

| Quantity | Expected | Came back |
|---|---|---|
| The gate | close to the committed figures, fails | **Reading A: identical to the committed figures.** Reading B: within 5 of them. Fails on every seed |
| The twins' states | identical under A; differ under B | **as expected** |
| Site sets clearing the floor | none under A, by construction; probably none under B, about one chance in six per seed of a clearance by noise | **None on development episodes anywhere.** Under B on seed 2, **33 on fresh episodes** (section 4) |
| The read | a guess of 10 to 65 of 180 under A, 10 to 70 under B | **9 to 25.** Lower than the guess: near the 13 to 15 that knowing nothing gives, and nowhere near the 45 of guessing among the episode's four agents |
| The nomination | no verdict, every seed | **as expected** |
| The arithmetic | 0 ÷ 0 at all 180 under A; not predicted under B | **as expected under A.** Under B, 1.0000 at most comparisons (section 5) |
| The null transplant | bit-identical at all 45 | **as expected** |
| The no-transplant rate | outside the allowance, about 0.25 against 0.11 | **as expected**: 0.22 to 0.25 against 0.11 |

## 4. What surprised this session, written down and not changed

**4.1 On seeds 0 and 1 the floor asks for less than nothing.** On
development episodes the solver lands on the donor twin's value more often
than on its own right answer (seed 0, reading A: 0.2400 against 0.2333; seed
1: 0.2300 against 0.2100). The floor asks the whole-state transplant to raise
the donor's share by four fifths of (accuracy − untouched), which here is
below zero. `repairs.floor_check` counts a requirement at or below zero as a
miss, whatever the transplant does. So on seeds 0 and 1, under both readings,
the floor could not have been cleared by any transplant. That clause, not a
measured shortfall, is what returns no verdict there. (Under reading A the
transplant changes nothing anyway.)

**4.2 Under reading B, seed 2 clears the floor on fresh episodes at 33 of 45
site sets.** On development episodes seed 2's requirement is +0.0053, about
3 episodes of 600, and the largest raise any site set gives is +0.0017, one
episode. On fresh episodes the requirement is +0.0010, under one episode of
800, and 33 site sets raise the donor's share by one or two episodes. The
nomination is made on development episodes only, so none was nominated and
the fresh clearances are never used. Had they been, the piece rule would have
refused every size: the best piece is 21 of 180 against 144.

**What these mean (ARGUED).** The whole-state floor is set relative to how
far the model is above its own no-transplant rate. For a solver that cannot
tell whose value it needs, that distance is about zero, so the floor is
about zero, and one or two episodes decide it either way. On this solver the
floor is not a margin; it is a coin. What holds the solver back with room to
spare is, in order: **the gate on learning** (it fails by 64 to 140 of 3,000,
and in the registered experiment a model that fails the gate is not read at
all); **the piece rule** (best piece 20 to 25 of 180 against 144, the whole
sampling band far below); and **the no-transplant rule** (the rate misses
its formula by 0.11 to 0.14, against an allowance of 0.018). The floor's verdict on this solver should not be
cited as the reason it returns no verdict.

## 5. Description only: what the arithmetic would have returned

**None of this is a reading.** The number is (whole − piece) ÷ (whole −
untouched), on fresh episodes, at all 180 comparisons, with no floor applied.

| seed, reading | accuracy, untouched | whole − untouched, over 45 site sets | room the floor asks for | of 180: division by zero / defined | defined values: smallest, middle, largest |
|---|---|---|---|---|---|
| 0, A | 0.2250, 0.2487 | 0 to 0 | −0.0190 | 180 / 0 | none defined |
| 1, A | 0.2188, 0.2300 | 0 to 0 | −0.0090 | 180 / 0 | none defined |
| 2, A | 0.2238, 0.2200 | 0 to 0 | +0.0030 | 180 / 0 | none defined |
| 0, B | 0.2250, 0.2500 | −0.0025 to 0 | −0.0200 | 32 / 148 | 1.0000, 1.0000, 1.0000 |
| 1, B | 0.2188, 0.2313 | −0.0013 to 0 | −0.0100 | 20 / 160 | 1.0000, 1.0000, 1.0000 |
| 2, B | 0.2238, 0.2225 | −0.0013 to +0.0025 | +0.0010 | 20 / 160 | 0.0000, 1.0000, 1.0000 |

**What it shows (ARGUED).** Under reading B the transplant of the whole state
moves the donor's share by one or two episodes, often downwards, and the
transplant of the piece moves nothing, so the ratio is very nearly always
exactly 1. **Without its floors the formula would describe the ordinary
competing solver the way it describes the entangled model.** That is the
inflation the floors and the gate exist to stop, and on this solver they
stop it. It is also a reason never to print the arithmetic for a model that
did not clear the floors without the words "not a reading" beside it, as
this file and the re-run both do.

## 6. Against the method's stops

| Stop | Fired? |
|---|---|
| B1, a model file does not match its fingerprint | No |
| B2, a reading is returned on any seed | **No**, under either reading |
| B3, under reading A the twins' inputs or states are not identical | No |
| B4, the null transplant is not bit-identical somewhere | No |

## 7. Which sentences of version 4 these figures bear on

Version 4 is `docs/successor-experiment-proposal-2026-10-03-v4.md`. This file
does not edit it; another session is working on it.

- **Section 7.3, the last paragraph** ("The ordinary competing solver has not
  yet been measured under the piece rule [...]"): the run it says is owed now
  exists, and **its stated expectation, "no verdict", is what came back**, on
  every seed. Its reason as written ("a solver with no acting channel should
  have no read of its own marker word that reaches four fifths") holds (best
  piece 20 to 25 of 180), but it is **not the rule that stopped the run
  first**: no site set cleared the whole-state floor, so the piece rule was
  never consulted. Its sentences "This version quotes no figure for it" and
  "until then this text does not go to the registration review" can be
  replaced once this run is checked.
- **Section 8.1, the reference points:** the ownership-blind solver's
  own-directed accuracy, 0.2340 to 0.2383, is reproduced exactly on the
  processor (702, 715 and 702 of 3,000). The clause "the ownership-blind
  solver is to be put through the nomination under it before the
  registration review" is answered by this run.
- **Section 10, item R-5** ("The ownership-blind solver's run through the
  nomination under that rule is owed before the registration review") and
  **"What happens next"** ("The ordinary competing solver is run under the
  piece rule, method first, by another session, and checked"): the run is
  done, method first; the check is still owed.
- Also the header's item 2 ("One more short run is owed"), the same.
- **Section 4 of these findings bears on any sentence that says the
  whole-state floor protects against a solver like this.** This session did
  not find one by search, but did not read version 4 through.

## 8. Questions for John, each with a suggestion

Not asked in chat; for the session that routes rulings.

1. **Which reading of the solver the registration cites.** *Suggestion:*
   reading A, the channel removed, as the primary, because that is how the
   solver was trained and scored; and reading B stated beside it, because
   under reading A the no verdict follows from the pairing alone and says
   little about the solver.
2. **Whether the registration says what actually stops this solver.**
   *Suggestion:* one sentence, that on the toy the competing solver's no
   verdict comes from the gate on learning, the piece rule and the
   no-transplant rule, each with room to spare, and that the whole-state
   floor is close to zero for a model near chance and is decided there by one
   or two episodes (section 4). No change to any rule.
3. **The no-transplant rule's formula on a solver that cannot tell owners
   apart.** It assumes wrong answers spread evenly over the seven other
   values; this solver's land on the other agents' values, one of which is
   the donor's, so the rate is about twice the formula's. *Suggestion:*
   report only; it withholds a reading here, which is the right outcome, but
   the registration should not describe the formula as a property of every
   model.

## 9. Files

`experiments/rehearsal-successor-measure/out-competing-solver-run/`:
`reads_blind_seed{0,1,2}_{channel_removed,channel_left_on}.npz` (the fitted
reads, development episodes only), `nominate_blind_seed*_*.json` (fits, the
full development grid, the floors, the choice, the description-only
arithmetic), `measure_blind_seed*_*.json` (the gate, the fresh-episode floors,
the null transplant, the twins, the no-transplant rate, the description-only
arithmetic), `summary.json`, `table.md`, `stdout.txt`. Code:
`src/competing_solver_run.py`, unchanged since `744a8b3`.
