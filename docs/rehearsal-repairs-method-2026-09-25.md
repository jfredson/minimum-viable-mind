# The rehearsal repairs — method, committed before any of it was built or run

*Written 2026-09-25 (Pacific), on branch `worktree-w1c-rehearsal-repairs`, by
the Claude Code session commissioned as "MVM W1c rehearsal repairs" (session (c)
of `docs/weekend-1-session-prompts.md`). **UNREGISTERED.** Nothing here is a
ruling, nothing here registers anything, and no number below is a bar for the
successor experiment. Every bar used here was ruled by John on 2026-09-25 in
`docs/rulings/2026-09-26-weekend-1-queue.md` (the "Weekend 1 queue ruling"
below), and is quoted from there; where this file had to choose how to turn a
ruled sentence into code, it says so and marks the choice ARGUED.*

*Committed **before** the code it describes and before any output, as the
programme's discipline requires. The session prompt for this work runs a day
earlier than the prompts file planned (it planned Saturday 2026-09-26), because
the rulings it depends on were made on the evening of 2026-09-25. The findings
file keeps the name every other document points at,
`docs/2026-09-26-rehearsal-repairs.md`, for the same reason the ruling file kept
its name.*

*Local, toy scale, on the laptop, no network, no rented machine, **$0**. Nothing
in this work creates, starts or rents anything. If a step turned out to need
money, the session would stop and say so; none is planned.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).*

---

## 0. Words used here, once

- **Arm**: one version of the tiny system being compared. **Arm T** keeps the
  ownership answer (which agent the model is) in a slot of its own, so the
  degree to which it is entangled is zero by construction. **Arm C** stirs it
  through every layer, so the degree is high by construction. **Arm F** is
  trained freely, with no constraint on where the answer lives. All three are
  defined in `experiments/rehearsal-successor-measure/src/arms.py`.
- **Own-directed condition**: the action "revise *your own* earlier value".
  **Named-other condition**: "revise *agent m7's* earlier value". The grammar is
  `experiments/rehearsal-successor-measure/src/grammar.py`.
- **Transplant**: copying part of the model's internal state from a twin
  episode (the **donor**, identical text, a different agent being the model)
  into the episode being run (the **recipient**) and seeing whether the action
  follows the donor. **Whole-state** copies everything at the chosen places;
  **ownership-only** copies only the part lying in the nominated **ownership
  subspace** (a handful of directions in the state).
- **Site set**: the layers and token positions where a transplant happens.
- **Nomination**: the procedure that chooses the site set and the subspace,
  blind, on development episodes only.
- **The reading**, in the form John ruled on page 2 (the **chance-corrected
  form**): `(whole − ownership_only) / (whole − untouched)`, where each term is
  the share of trials whose action lands on the donor's value, and *untouched*
  is that share with no transplant at all. Zero: the ownership subspace does
  everything the whole state does (separable). One: it does nothing
  (entangled).
- **Learn-both bar** (page 1b): a condition is learned when its held-out
  accuracy is above one in four, significantly at the 0.05 level under a
  one-sided binomial test, on at least two seeds of three. On 3,000 held-out
  episodes that is 790 correct or more, which is "above 0.2630" (checked in §7,
  command 1).

---

## 1. What this session is asked to do, and the one assumption about the ask

The session prompt John pasted is cut off after its item 2's first words ("2.
Make the"). The full prompt for this session is in
`docs/weekend-1-session-prompts.md`, section "(c) Rehearsal repairs", whose
item 2 begins with the same words. This session therefore takes items 2 to 5
from that file, adjusted to what the Weekend 1 queue ruling decided (page 3's
rider on item 2; page 5 ruled yes to the fourth arm, so item 4 runs). Item 1 is
taken as John's pasted text. **This is an assumption, stated so that John can
overturn it**; guessing wrong costs one extra session, not a spend.

1. **The named-other condition** (ruling page 4): attempt redesign (b), a
   curriculum, and (a), loss re-weighting, on the free arm, with the pass line
   in §2.3 fixed here before the run.
2. **One instrument for the nomination step** (ruling page 3): the label fixed
   to which marker word in the code, one blind rule on every arm, a table
   showing it, and the rider (every arm also read at arm T's nominated site set
   and rank).
3. **Control 2 built as the proposal states it** (proposal section 7.3, item 2).
4. **The fourth, partly separable arm** (ruling page 5), with its predicted
   reading stated here before it runs.
5. **The measure re-run** with the ruled form and the ruled numbers on every arm.

---

## 2. Item 1 — the named-other condition

### 2.1 What failed, from the record

`docs/2026-09-21-successor-measure-rehearsal.md`, section 8: on 3,000 held-out
episodes the named-other condition cleared 0.2630 on one seed of three on the
entangled arm (0.2590 / 0.2370 / 0.2637) and on the free arm (0.2547 / 0.2680 /
0.2393); doubling the budget moved the free arm from 0.2547 to 0.2657
(`experiments/rehearsal-successor-measure/out/budget_check.json`).

### 2.2 The two redesigns, each fixed to exactly one recipe

Both keep **everything** else in the rehearsal's recipe
(`experiments/rehearsal-successor-measure/src/rehearse.py`: 2,500 steps, batch
256, learning rate 0.003, 15,000 training pairs, the same one-cycle schedule,
the same data seeds `1000 + seed`). Only one thing changes in each, so any
difference is attributable to it. Neither is tuned: no second recipe is tried
in this session for either redesign. That matters because a bar just above
chance, tried across many recipes, will eventually be cleared by luck.

- **(b) Curriculum.** For the first 1,000 of the 2,500 steps (40 per cent), the
  loss is the named-other condition's alone; the own-directed position is not
  scored. From step 1,000 to 2,500 both conditions are scored with equal
  weight, as in the original recipe. The reasoning (ARGUED): the own-directed
  condition is the easier one for these arms (0.56 to 0.59 against 0.24 to
  0.27, section 8 of the findings), and a model that learns it first may
  settle into a solution that never learns to match a marker word; training the
  harder lookup first removes that competition.
- **(a) Loss re-weighting.** Throughout training the named-other condition's
  loss is weighted four times the own-directed condition's, normalised so the
  two weights average one: 0.4 on own-directed and 1.6 on named-other. Four
  times is the programme's own precedent, the Amendment A3 control-learnability
  pilot's weighting (proposal section 3, citing
  `experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md`),
  which "changed nothing" there. That precedent is the reason to expect (a) to
  fail, and it is stated before the run.

Both are implemented as options on the existing training function
(`src/training.py`) whose defaults leave the original recipe byte-for-byte the
same code path.

**A baseline run in the same session.** The re-run of 2026-09-22 found that the
entangled and free arms do not reproduce from the same code and seed on this
laptop's graphics chip: their readings moved by up to 0.0506
(`docs/rulings/2026-09-23-range-and-direction-only.md`). So each redesign is
compared not only with the record but with the unchanged recipe re-trained in
this session on the same three seeds, and every free-arm figure is reported as
a range and a direction, as that ruling requires.

### 2.3 The pass line, fixed now

From the ruling, page 4, unchanged: **the named-other condition above the page
1b bar on at least two seeds of three on the free toy arm.** Concretely: on the
3,000 held-out development episodes the rehearsal's gate stage uses
(`make_data(1500, seed=99, pool="dev")`), at least 790 correct on at least two
of seeds 0, 1 and 2.

Two further things are reported with it, and are **not** part of the pass line:

- **Own-directed accuracy on the same runs.** A redesign that lifts the
  named-other condition by breaking the own-directed one has not fixed the
  learn-both gate. If a redesign passes the ruled line but its own-directed
  condition falls below the same bar on two seeds of three, the finding says
  both things and does not call it a fix.
- **How far above the bar.** Because 0.2630 sits just above one in four, a pass
  by a few episodes is recorded as a pass *and* as thin.

**Outcomes, pre-stated.** Pass on (b) alone, (a) alone, both, or neither. If
neither passes, that is the finding, and the ruling's fallback (d) applies
(the registration records the failure; the staggered first run reads the
learn-both result of one free-arm run before the other eight are committed).
If both pass, (b) is carried into item 5, because it was ruled first; (a) is
reported beside it.

### 2.4 What is carried into item 5

If a redesign passes, item 5 is run twice: once on arms trained with the
original recipe (so the rest of the record stays comparable) and once on every
arm re-trained with the passing recipe, because page 4 says a passing redesign
changes the training recipe for the successor, which trains all arms the same
way. If none passes, item 5 is run on the original recipe only.

---

## 3. Item 2 — the nomination step as one instrument

### 3.1 What changes in the code

The 2026-09-21 driver (`src/rehearse.py`) searched over three readings of the
label (`READ_LABELS`, its line 69) and six rank caps, and nominated the single
best configuration across all of them, so the label was chosen by the search.
That file is left exactly as it is, as the record of what ran on 2026-09-21. A
new driver, `src/repairs.py`, carries the ruled procedure:

- **The label is fixed** to which marker word is the model's own
  (`docs/rulings/2026-09-23-nomination-label.md`; page 3 of the Weekend 1 queue
  ruling). The code has one label, not a tuple, and asserts it.
- **Rank caps 1, 2, 4 and 8** (page 1d).
- **The site sets**: the rehearsal's nine layer sets times five position sets,
  with the set of every layer at every position excluded by name (page 1c and
  1e), which leaves 44. So the family is 44 × 4 × 1 = **176 comparisons per arm
  and seed**, the count page 1e prints; the code asserts it.

### 3.2 The rule, one function, applied to every arm

Written here as the code will implement it. On development episodes only (600
matched pairs, `seed=4242`, pool `dev`, as in the 2026-09-21 run):

1. For every one of the 44 site sets, measure the whole-state transplant's
   donor share, the untouched donor share, and the arm's own-directed accuracy
   on the same recipients.
2. **The floor** (page 1c, written on the chance-corrected scale per page 2): a
   site set clears it when `whole − untouched ≥ 0.8 × (own_accuracy − untouched)`.
   *How this sentence was turned into code is a choice, marked ARGUED:* the
   ruling says "four fifths of the arm's own own-directed accuracy" and that the
   floor is "written on this scale"; subtracting the untouched share from both
   sides is what writing it on the chance-corrected scale means, here. The plain
   form, `whole ≥ 0.8 × own_accuracy`, is printed beside it everywhere so a
   reader can see whether the two readings of the sentence ever disagree.
3. **The whole-state layer set** (proposal 7.2, item 4, and page 1c: "the
   smallest that clears it"): for each of the five position sets, the layer set
   with the fewest layers that clears the floor, ties going to the earliest
   layers. A position set with no clearing layer set drops out.
4. **Nominate by causal effect** (proposal 7.2, item 3): over the surviving
   (position set, its smallest clearing layer set) pairs and the four rank
   caps, the configuration with the highest ownership-only donor share.
   Ties go to the lower rank, then the earlier position set in the
   rehearsal's list.
5. If no site set clears the floor, the arm returns **no verdict** at
   nomination, and that is recorded, not repaired.

*Why this order, ARGUED:* the ruled text fixes the layer set by the floor and
leaves the causal-effect choice to what remains. The alternative — highest
ownership-only share over every site set that clears the floor — is also
computed and printed beside it as a sensitivity row, so that if the two
readings of "smallest that clears it" pick different things, it shows.

### 3.3 What "shows, with the table, that the same procedure selects the same
way on each" means here

A table, one row per arm and seed, with: the floor, how many site sets clear
it, the chosen position set, layer set and rank, the development-set
whole-state and ownership-only shares, and the sensitivity row's choice. The
code runs the one function for every arm with no argument that names the arm.
What the table can show is that one rule was applied; it cannot show that the
rule's outputs are the same on every arm, and page 3 says they will not be.

### 3.4 The rider (John's addition on page 3)

For every arm and seed, the reading is also taken at **arm T's** nominated
site set and rank for the same seed, using that arm's own read fitted at those
sites. Reported beside the reading at the arm's own nomination, so a reader can
see whether what differs between arms is their degree or where the procedure
looked.

---

## 4. Item 3 — control 2 as the proposal states it

### 4.1 What was run before, and what the proposal says

Run on 2026-09-21: the ownership subspace of an *unmatched* episode,
transplanted in (rehearsal findings, section 6). The proposal (section 7.3,
item 2): "**Nominate, by the identical procedure, a representation of a named
agent who is not acting, and transplant it. The own-directed action should not
move.**"

### 4.2 How it is built

- **The agent.** The agent the named-other turn names. By construction it is
  never the agent acting (`grammar.eligible_models`).
- **The label.** Which marker word is that named agent's — the same kind of
  label as the ownership read, pointed at a different agent.
- **The donor.** A new twin, the **named-swap twin**: the same content and the
  same acting agent, with the named agent replaced by a different agent that is
  neither the actor nor the original named agent. The text differs in exactly
  one token, the marker word in the named-other turn. So transplanting from it
  changes who is *named* and should leave who is *acting* alone.
- **The identical procedure.** The rule of §3.2, unchanged, with every
  own-directed quantity replaced by its named-other twin: position sets anchored
  at the named-other action rather than the own-directed one (the "post-identity"
  set anchored at the named agent's first assignment turn), the floor written
  against the arm's named-other accuracy, and the causal effect being whether the
  **named-other** action lands on the value the donor's named agent dictates.
- **The test.** Transplant the nominated named-agent subspace, at its
  nominated sites, from the named-swap twin into the recipient, and count the
  share of trials whose **own-directed** action changes from what the untouched
  recipient does.

### 4.3 The cell, fixed now

- **Pass:** the own-directed action changes in no more trials than it does
  under a random subspace of the same rank at the same sites from the same
  donor, plus 0.05. (0.05 is a rehearsal-only tolerance, fixed here, and **not**
  a registered number.)
- **Fail:** it changes in more.
- **No verdict:** the named-agent representation cannot be nominated because
  no site set clears the floor, which is what happens if the arm has not learned
  the named-other condition. **This is expected on arms C and F if item 1 fails,
  and on arm T for a structural reason:** arm T selects the named agent's row
  from the turn's metadata (`action_who` in `arms.py`), not from its running
  state, so no transplant into the state can move its named-other action. If
  that happens it is reported as a property of the construction, not a fail.
- **Beside it, reported and not gated:** the share of trials whose named-other
  action moved (whether the representation is live at all; a control that moves
  nothing is vacuous), and a fixed-site variant — the named-agent read fitted at
  the arm's *ownership* nomination's sites and rank — so that the control has a
  number on every arm even where the full procedure returns no verdict.

---

## 5. Item 4 — the fourth arm, built to be partly separable

### 5.1 The construction

A new architecture, **arm M** (for middle), in a new file `src/arm_middle.py`
so that `arms.py` and the three-arm loops of the 2026-09-21 driver are not
touched. It has both of the constructed arms' routes to the answer, and uses one
or the other depending on the **item** the action is about:

- a slot of its own for the ownership answer, carried unchanged through every
  layer and read only by an arm-T-style head (the **separable route**);
- the ownership answer multiplied into every block and into the value
  representations, read by an ordinary output layer, as in arm C (the
  **entangled route**);
- actions about items `it1`, `it2` and `it3` go through the entangled route;
  actions about `it0` and `it4` through the separable one. The training and
  fresh pools use items `it0` to `it4` with equal chance
  (`grammar.POOLS`), so about **three fifths** of actions are entangled.

So every trial is either fully separable or fully entangled, and the arm's
degree is the share of the identity-driven effect carried on the entangled
route. This is a mixture by item, not a partial separation inside every trial;
**that is a limitation of the construction, stated before it runs**, and page
5's strongest argument against applies to it in full: its degree is a design
intention, and it differs from both anchors in more than degree.

### 5.2 The prediction, stated before it runs

Write `p = 3/5` for the entangled share, `a_T` and `u_T` for the separable
route's whole-state and untouched donor shares, `a_C` and `u_C` for the
entangled route's. If the ownership-only transplant catches the separable
route's slot exactly and nothing on the entangled route, the chance-corrected
reading is

    predicted = p·(a_C − u_C) / [ (1 − p)·(a_T − u_T) + p·(a_C − u_C) ]

Plugging in the constructed arms' record (arm T: whole 1.0000 and untouched
0.0000; arm C: whole and untouched 0.5400 and 0.0600, 0.5750 and 0.0663, 0.5525
and 0.0638 on its three seeds, section 4 of the rehearsal findings) gives
**0.4186, 0.4328 and 0.4230**:

```
$ python3 -c "
p=0.6
for aC,uC in ((0.5400,0.0600),(0.5750,0.0663),(0.5525,0.0638)):
  d=p*(aC-uC)/((1-p)*(1.0-0.0)+p*(aC-uC)); print(aC,uC,round(d,4))
"
0.54 0.06 0.4186
0.575 0.0663 0.4328
0.5525 0.0638 0.423
```

The entangled route in arm M is trained on three fifths of the actions rather
than all of them, so its accuracy may differ from arm C's; that is why the
prediction below is a band and is also checked against the formula evaluated on
arm M's own measured route accuracies. The prediction, fixed now: **the blind reading lies
between 0.30 and 0.60 on every seed, and within 0.10 of the formula above
evaluated on the route accuracies measured on the same fresh episodes.** The
second half is the check that the construction behaves as built; the first is
the number the arm is meant to produce.

### 5.3 The pass, from the ruling (page 5), unchanged

A chance-corrected reading between 0.3 and 0.7 on all three seeds. On a pass
the arm is a candidate for the main registration, whose three runs come from
page 6's envelope; on a fail it is carried as extension E0 on the weekend
roadmap. Either way, **folding it in is John's call**; this session reports.

Arm M is trained with the original recipe on seeds 0, 1 and 2, and put through
the same nomination, reading, controls and gate as the other arms. Its oracle
reading (the transplant handed its true slot, as arm T's is) is reported
separately.

---

## 6. Item 5 — the measure re-run with the ruled form and the ruled numbers

On every arm (T, C, F and M), three seeds each (page 1f), with the numbers of
page 1:

| ruled number | as implemented |
|---|---|
| 1a separation bar 0.5 | per seed, arm C's chance-corrected reading minus arm T's; and the smallest across seeds |
| 1b learn-both | ≥ 790 of 3,000 on both conditions, on at least two seeds of three |
| 1c floor | §3.2, step 2 |
| 1d rank cap | 8, family reports 1, 2, 4 and 8 |
| 1e site list | the 44 site sets of §3.1; the rule's list for the registered 12-layer model is printed beside the toy's 176 |
| 1f seeds | 0, 1, 2 |
| 1g uncertainty | across-seed standard deviation of the raw difference, with the within-seed bootstrap over matched pairs beside it; neither measures drift between runs of one seed |
| 1h lesion | arm F only: own-directed accuracy with the acting channel removed falls to 789 of 3,000 or fewer; named-other reported, not gated |
| page 2 form | chance-corrected, with the raw difference, both accuracies and the untouched share always printed beside it |

Also run on every arm: controls 1 and 3 to 7 as the 2026-09-21 driver runs
them, control 2 as §4, the rider of §3.4, and the no-transplant rate against
the review's formula `(1 − own accuracy) / 7`, with the miss printed (page 2
says the rule needs room for a miss of up to 0.0175).

**Fresh episodes** are the 2026-09-21 run's: 800 matched pairs, `seed=777`,
pool `fresh`. Development and fresh sets are generated from separate seeds and
the reads are frozen on development data before any fresh episode is scored,
as before.

**How entangled and free-arm figures are reported.** Under
`docs/rulings/2026-09-23-range-and-direction-only.md` these arms do not
reproduce from code and seed, so their figures are reported as a range across
seeds and a direction, and no decimal is offered as a property of the code.
The separable arm's figures are exact when they reproduce.

---

## 7. Checks run while writing this file (MEASURED)

Command 1 — the learn-both bar at 3,000 episodes:

```
$ ~/Code/minimum-viable-mind/.venv/bin/python -c "
from scipy.stats import binom
n=3000
k=min(k for k in range(n) if binom.sf(k-1,n,0.25)<0.05)
print('smallest count significant above 1/4 at 0.05, one-sided, n=3000:',k, k/n)
"
smallest count significant above 1/4 at 0.05, one-sided, n=3000: 790 0.2633333333333333
```

So "above 0.2630" (789 of 3,000) and "significant at 0.05" (790 or more) are
the same rule.

Command 2 — the laptop, the training time per run on the record, and the
missing checkpoints:

Run from `experiments/rehearsal-successor-measure/`; the output is seconds per
training run, read from the committed `out/train.json`, then the count of
checkpoint files in the main checkout's `out/`:

```
$ python3 -c "
import json;d=json.load(open('out/train.json'))
for k,v in d.items(): print(k, round(v['seconds'],1))
"; ls ~/Code/minimum-viable-mind/experiments/rehearsal-successor-measure/out/ | grep -c '\.pt$'
C/0 489.0
C/1 523.5
C/2 525.4
F/0 512.5
F/1 453.0
F/2 441.1
T/0 442.8
T/1 401.1
T/2 399.9
blind/0 482.0
0
```

So one run is about seven to nine minutes, and every arm must be re-trained:
the 2026-09-21 checkpoints were never committed (`out/*.pt` is ignored) and are
not on disk.

---

## 8. Cost, and what this cannot do

About 27 to 36 training runs of seven to nine minutes each, plus inference:
roughly four to six hours of laptop time, on wall power, **$0**. No rented
machine, no network call, no vendor. Outputs go to a new directory,
`experiments/rehearsal-successor-measure/out-repairs/`, so that nothing in the
2026-09-21 record (`out/`) is overwritten.

It cannot say what happens at the registered size. Page 4's strongest argument
against — that toy redesigns may be fixing a problem scale removes — stands
whatever this returns.
