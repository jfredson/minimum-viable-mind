# The rehearsal repairs — findings

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c rehearsal
repairs", session (c) of `docs/weekend-1-session-prompts.md`, on branch
`worktree-w1c-rehearsal-repairs`. The file keeps the name the prompts file gives
it (dated 2026-09-26, the Saturday it was planned for); the work ran a day early
because the rulings it depends on were made on the evening of 2026-09-25.
**UNREGISTERED.** Nothing here is a result about the scientific question, nothing
here is a bar, and nothing here is a ruling. Every bar used below was ruled by
John in `docs/rulings/2026-09-26-weekend-1-queue.md` (the "Weekend 1 queue
ruling"); every other threshold is a rehearsal-only one fixed in the method note
before the run.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent: $0.***

*Method, committed before any code or output:
`docs/rehearsal-repairs-method-2026-09-25.md`. Code and every output file:
`experiments/rehearsal-successor-measure/src/` (new: `repairs.py`,
`arm_middle.py`, `diagnose_named_other.py`; changed: `training.py`) and
`experiments/rehearsal-successor-measure/out-repairs/`. The 2026-09-21 record in
`out/` and its driver `rehearse.py` are untouched.*

*Every finding is labelled **MEASURED** (a command was run and its output is
reported, with the committed file it wrote) or **ARGUED** (reasoning a reader can
dispute). Figures from the entangled and free arms are quoted as a range and a
direction, as `docs/rulings/2026-09-23-range-and-direction-only.md` requires:
those arms do not reproduce from code and seed on this laptop. Written under the
workspace plain-language rule.*

---

## 0. What to read if you read nothing else

- **Item 1, the named-other condition: neither redesign clears the ruled pass
  line, so page 4's fallback (d) applies.** The curriculum clears the bar on 0
  seeds of 3 and the loss re-weighting on 0 of 3; the unchanged recipe, re-trained
  in this session, clears on 1 of 3, as it did on 2026-09-21. Both redesigns made
  things worse: the curriculum teaches the model to answer the named-other turn
  with **its own** value, and the re-weighting costs the own-directed condition
  without buying the named-other one. MEASURED.
- **Why, most likely: the grammar signals "this is your turn" on both action
  turns**, so the only thing telling the two apart is one word, and the two
  conditions compete for one route. That points at page 4's redesign (c), a
  grammar change, which this session did not attempt. ARGUED.
- **Item 4, the fourth arm: it passes page 5's pre-stated line.** Built to be
  partly separable, it reads **0.48 to 0.53** on the chance-corrected form on all
  three seeds, inside 0.3 to 0.7, and within 0.02 to 0.04 of what its construction
  predicts from its own route accuracies. Folding it into the registration is
  John's call under page 5 and page 6. MEASURED.
- **Item 2, one instrument: done in code, and it exposed two things the ruled
  text does not settle.** The ruled exclusion ("every layer at every position")
  is too narrow, because copying **any** layer at every position hands the donor's
  whole forward pass downstream; the nomination picked such a set on two of arm
  C's three seeds. And the ruled site-list rule does not produce the toy's 176
  comparisons even on the toy: it produces 296. MEASURED.
- **The rider (John's addition): at arm T's site set, arms C, F and M give no
  verdict at all** — their whole-state transplant does not move the action
  there. So what differs between arms is, first, where the procedure has to look.
  MEASURED.
- **Item 3, control 2 as the proposal words it: no verdict on arms T, C and M,
  a pass on arm F that means little.** It needs the arm to carry the named
  agent in its running state and to have learned the named-other condition;
  arm T carries it outside the state by construction, and arms C and F have not
  learned the condition. MEASURED.
- **Item 5, the measure with the ruled form and numbers:** arm T reads 0.0000
  on every seed, exactly as on 2026-09-21; arm C reads at the entangled end
  (0.99 to 1.00); the free arm reads at the entangled end too (1.00 to 1.003),
  and **fails the learn-both gate**, so under the ruled numbers it would not be
  read at all. The separation bar of 0.5 is cleared on every seed. MEASURED.

---

## 1. What was committed when

| order | commit | what |
|---|---|---|
| 1 | `426b6e8` | the method note, before any code or output |
| 2 | `16d75f6` | training options, arm M, the driver's train and gate stages (code only) |
| 3 | `9e341e6` | nomination, measure and summary stages (code only) |
| 4 | `81dc84d` | two additions **not pre-stated**, labelled so in the code (§8) |
| 5 | `004d134` | the outputs |
| 6 | this file | the findings |

The method note precedes the first output commit. Two dry runs of the
measurement code were made on scratch checkpoints outside the repository before
commit 3 (one on untrained models, one on a trained arm T and a 400-step arm M,
on 120 episodes); nothing from them is committed or reported as a result.

---

## 2. Item 1 — the named-other condition (ruling page 4)

    ../../../.venv/bin/python repairs.py --stage train --arms F --recipes base,curriculum,reweight
    ../../../.venv/bin/python repairs.py --stage gate --arms F --recipes <recipe>

The pass line, fixed in the method note (§2.3) from the ruling: the named-other
condition at 790 or more correct of 3,000 held-out episodes (above 0.2630) on at
least two of three seeds, on the free arm. MEASURED, from
`out-repairs/gate_base.json`, `gate_curriculum.json` and `gate_reweight.json`:

| free arm, recipe | named-other, seeds 0 / 1 / 2 | seeds clearing | own-directed, seeds 0 / 1 / 2 |
|---|---|---|---|
| unchanged (re-trained here) | 0.3313 / 0.2603 / 0.2487 | **1 of 3** | 0.5597 / 0.5513 / 0.5547 |
| (b) curriculum: named-other only for the first 1,000 of 2,500 steps | 0.0773 / 0.1933 / 0.1430 | **0 of 3** | 0.5507 / 0.5643 / 0.5637 |
| (a) re-weighting: named-other loss four times own-directed | 0.2317 / 0.2063 / 0.2377 | **0 of 3** | 0.1700 / 0.1723 / 0.1760 |

**Neither redesign passes. Page 4's fallback (d) applies**, in the ruling's
words: the registration records that the named-other condition failed its bar on
two of three toy arms, that doubling the budget did not fix it, and that the
staggered first run reads the learn-both result of one free-arm run before the
remaining eight are committed. This session adds a sentence it can support:
**neither a curriculum nor loss re-weighting fixed it either.**

As a range and a direction, as the 2026-09-23 ruling requires for this arm:
the unchanged recipe's named-other accuracy ran 0.25 to 0.33, just around the bar
(on 2026-09-21 it ran 0.24 to 0.27, `out/gate.json`); both redesigns moved it
**down**. The unchanged recipe's seed 0 moved from 0.2547 on the record to 0.3313
here — the drift between runs the 2026-09-23 ruling describes, and the reason no
decimal here is offered as a property of the code.

**What the model answers instead.** An exploratory diagnostic, **not
pre-stated** (§8), classes each named-other prediction on the same 3,000
episodes. MEASURED, `out-repairs/diagnose_named_other.json`:

| free arm, recipe, seed | the named agent's value (right) | the model's own value | another agent's value in the item | a value not in the item |
|---|---|---|---|---|
| unchanged, 0 / 1 / 2 | 0.33 / 0.26 / 0.25 | 0.06 / 0.07 / 0.05 | 0.39 / 0.48 / 0.51 | 0.22 / 0.18 / 0.19 |
| curriculum, 0 / 1 / 2 | 0.08 / 0.19 / 0.14 | **0.55** / 0.14 / 0.28 | 0.17 / 0.38 / 0.30 | 0.20 / 0.30 / 0.28 |
| re-weighting, 0 / 1 / 2 | 0.23 / 0.21 / 0.24 | 0.17 / 0.18 / 0.18 | 0.47 / 0.49 / 0.45 | 0.13 / 0.13 / 0.13 |

The unchanged model knows *which item* and not *whose value*. After the
curriculum it often gives **its own** value at the named-other turn — on seed 0,
more than half the time. Under re-weighting it picks among the item's four values
in both conditions without knowing whose.

**The reading, ARGUED.** In this grammar the acting channel — the signal that
tells the model "this turn is yours" — fires on **both** action turns
(`grammar.py`, `render`: `acting.extend([1] * 7)` for each action turn). The two
turns differ only in the word after `revise`: the word meaning *your own*, or a
marker word. So the easy route to the own-directed answer (follow the acting
channel back to your own assignment turn) is equally available at the
named-other turn, and a model that learns it applies it at both. The curriculum's
first phase evidently did not survive the second; the re-weighting made the model
give up the acting-channel route rather than add the marker-matching one. If that
reading is right, a training change cannot fix it and a grammar change can —
page 4's option (c), for instance an action turn whose acting-channel pattern
differs between the two conditions, or the named agent's marker placed where the
model's own sits. **That is a design question for John, not attempted here**: it
re-opens rehearsal items R-1 to R-6 and the Gate C review of the proposal.

Page 4's strongest argument against — that every toy redesign may be fixing a
problem scale removes — stands whatever this shows.

---

## 3. Item 2 — the nomination step as one instrument (ruling page 3)

    ../../../.venv/bin/python repairs.py --stage nominate --arms <arm> --recipes base

**What changed in code.** `repairs.py` has one label, `READ_LABEL =
"marker-word"`, not a tuple; rank caps `(1, 2, 4, 8)`; 44 site sets (the
rehearsal's nine layer sets times five position sets, less "every layer at
every position"); and `assert len(SITE_SETS) == 44 and FAMILY_SIZE == 176`. One
function, `nominate`, takes no argument that names an arm and is called
identically for every arm. MEASURED (the assertion runs on import; every
`nominate_base_*.json` records `"family_size": 176` and `"label": "marker-word"`).

**What it selected**, on 600 development pairs. MEASURED, from
`out-repairs/nominate_base_T_C.json`, `nominate_base_F.json`,
`nominate_base_M.json`:

| arm, seed | site sets clearing the floor | nominated (positions, layers, rank) | development whole-state / ownership-only | the other reading of "smallest that clears" would pick |
|---|---|---|---|---|
| T, 0 / 1 / 2 | 44 / 44 / 44 | action, first layer, rank 8 — all three | 1.0000 / 1.0000 on all three | the same, all three |
| C, 0 | 38 | **every position**, first layer, rank 2 | 0.5867 / 0.0550 | the same |
| C, 1 | 35 | **every position**, first layer, rank 4 | 0.6033 / 0.0567 | after identity, all five layers, rank 8 |
| C, 2 | 38 | after identity, first layer, rank 2 | 0.5300 / 0.0550 | after identity, all five layers, rank 2 |
| F, 0 | 35 | after identity, first layer, rank 2 | 0.4883 / 0.0633 | after identity, second layer, rank 1 |
| F, 1 | 35 | action and three before, second layer, rank 4 | 0.5533 / 0.0500 | every position, layers 1 to 4, rank 8 |
| F, 2 | 35 | after identity, first layer, rank 1 | 0.4933 / 0.0700 | after identity, second layer, rank 8 |
| M, 0 | 35 | after identity, first layer, rank 8 | 0.7900 / 0.3683 | after identity, third layer, rank 8 |
| M, 1 | 35 | action, fourth layer, rank 8 | 0.7250 / 0.3783 | after identity, second layer, rank 8 |
| M, 2 | 35 | after identity, first layer, rank 8 | 0.7717 / 0.3700 | after identity, all five layers, rank 8 |

("First layer" is the state after the input embedding, layer index 0 in the
code; "after identity" is every position from the model's first own turn to the
action.)

What this shows, MEASURED:

- **One rule was applied, and it no longer picks arbitrarily on arm T.** The
  2026-09-21 findings (section 7, item 5) said every site set gives arm T 1.0000,
  so "the smallest layer set that clears the floor" had nothing to choose between.
  With ties broken as the method note fixed, it chooses the same site set on all
  three seeds.
- **The rule's outputs differ by arm**, as page 3 said they would, and they
  differ by seed within arms C, F and M.
- **The two readings of "the smallest layer set that clears it" disagree on 7
  of the 12 arm-and-seed pairs** (last column). The ownership-only shares they
  reach are close (0.0200 apart or less on every pair, from the same files), so no
  reading below moves much, but a registration has to say which reading it
  means. ARGUED: the one implemented (smallest clearing layer set per position
  set, then highest ownership-only share) follows the ruled words more closely.
- **The two forms of the floor never disagree.** Whether the four-fifths floor is
  written on the chance-corrected scale or plainly, the same site sets clear, on
  every arm and seed (0 disagreements across all 44 site sets, counted from the
  `floor` fields in the same files).

**The ruled exclusion is too narrow. MEASURED, then ARGUED.** On arm C seeds 0
and 1 the rule nominated the first layer **at every position**. Copying the
running state at every position of any layer makes everything downstream of that
layer the donor's own computation, wherever ownership lives only in the running
state. Arm C escapes being fully degenerate only because its ownership signal also
reaches every block by a side route the transplant does not touch (`arms.py`, the
scale-and-shift from `_own_vec`). On the free arm the first layer at every
position *is* the donor's forward pass. Page 1c excludes by name only "every layer
at every position"; the registration should exclude **every site set whose
positions are all positions**. A sensitivity row with those sets removed, **not
pre-stated** (§8), changes arm C's nomination on seeds 0 and 1 and nothing else;
the readings stay at the entangled end (1.0051 and 0.9863 on those two seeds,
`measure_base_T_C.json`, field `sensitivity_without_all_positions`).

**The ruled site-list rule does not produce 176, even on the toy. MEASURED.**
Page 1e registers the rule ("all contiguous layer sets", among other things) and
prints "176 comparisons per arm and seed" beside it as the toy's count. The 176
comes from the rehearsal's nine hand-listed layer sets, not from the rule:

```
$ python3 -c "
def contiguous(n_states): return [tuple(range(a,b+1)) for a in range(n_states) for b in range(a,n_states)]
toy=[(0,),(1,),(2,),(3,),(4,),(3,4),(2,3,4),(1,2,3,4),(0,1,2,3,4)]
c5=contiguous(5); c13=contiguous(13)
print('toy states (embedding + 4 blocks):', 5, '-> all contiguous layer sets:', len(c5))
print('toy hand-listed layer sets:', len(toy), '; all contiguous?', all(s in c5 for s in toy))
print('contiguous toy sets not in the hand list:', [s for s in c5 if s not in toy])
print('registered states (embedding + 12 blocks):', 13, '-> all contiguous layer sets:', len(c13))
print('toy family as run: 9 x 5 - 1 =', 9*5-1, 'site sets x 4 ranks =', (9*5-1)*4)
print('rule on the toy, with the same 5 position sets: 15 x 5 - 1 =', 15*5-1, 'x 4 =', (15*5-1)*4)
print('rule on the 12-layer model, same 5 position sets: 91 x 5 - 1 =', 91*5-1, 'x 4 =', (91*5-1)*4)
"
toy states (embedding + 4 blocks): 5 -> all contiguous layer sets: 15
toy hand-listed layer sets: 9 ; all contiguous? True
contiguous toy sets not in the hand list: [(0, 1), (0, 1, 2), (0, 1, 2, 3), (1, 2), (1, 2, 3), (2, 3)]
registered states (embedding + 12 blocks): 13 -> all contiguous layer sets: 91
toy family as run: 9 x 5 - 1 = 44 site sets x 4 ranks = 176
rule on the toy, with the same 5 position sets: 15 x 5 - 1 = 74 x 4 = 296
rule on the 12-layer model, same 5 position sets: 91 x 5 - 1 = 454 x 4 = 1816
```

Two further gaps, ARGUED: the rule's position clause ("the action position and
the positions between the source assignment and the action") does not say how
those positions are grouped into sets, and two of the toy's five position sets
("after identity" and "every position") reach outside it. And if every
all-positions set is excluded, as argued above, the counts change again. So the
registration has to print the list, as page 1e's strongest argument against
said, and the list and the rule have to agree.

### The rider: every arm read at arm T's site set

MEASURED, field `rider_at_arm_T_site_set` in the three `measure_base_*.json`
files. Arm T's nomination is the action position, first layer, rank 8, on every
seed.

| arm | at its own nomination | at arm T's site set |
|---|---|---|
| T | 0.0000 on all three seeds | the same site set: 0.0000 |
| C | 0.99 to 1.00 | **no verdict on all three seeds**: whole-state 0.0512 / 0.0488 / 0.0600, equal to the untouched rate |
| F | 1.00 to 1.003 | **no verdict on all three seeds**: whole-state 0.0587 / 0.0563 / 0.0688, equal to the untouched rate |
| M | 0.48 to 0.53 | **no verdict on all three seeds** |

At the first layer, at the action position, nothing about ownership has yet
reached the running state of arms C, F or M (the acting channel adds the same
vector at the action turn in both twins), so copying the donor's state there
changes nothing. **The first answer the rider gives, then, is that the arms
cannot be read at the same place at all.** What differs between arms is first of
all *where* the procedure has to look; whether their degrees differ can only be
asked at the site sets the rule chooses per arm. ARGUED: the rider as ruled should
stay in the reporting table, because "no verdict at arm T's site set" is exactly
the information it was added to surface.

---

## 4. Item 3 — control 2 as the proposal states it

Proposal section 7.3, item 2: "Nominate, by the identical procedure, a
representation of a named agent who is not acting, and transplant it. The
own-directed action should not move." Built as the method note (§4) fixed:
the named agent's marker word as the label; a named-swap twin as donor (same
content and actor, a different named agent, one token of text different); the
§3.2 rule anchored at the named-other action; pass if the own-directed action
changes in no more trials than under a random subspace of the same rank at the
same sites, plus 0.05 (a rehearsal-only tolerance).

MEASURED, field `control2` in the `measure_base_*.json` files and
`control2_named_agent` in the `nominate_base_*.json` files:

| arm | full procedure | why, or what it returned | fixed-site variant (the arm's own ownership sites) |
|---|---|---|---|
| T | **no verdict** on all three seeds | 0 of 44 site sets clear the floor, although the arm scores 1.0000 on the named-other condition: arm T selects the named agent from the turn's metadata, not from its running state, so no transplant into the state can move that action. Predicted in the method note | pass, vacuous: nothing moves |
| C | **no verdict** on all three seeds | 0 of 44 clear; the arm's named-other accuracy on development episodes is 0.2617 / 0.2483 / 0.2333 | pass; named-other action moved in 0.055 / 0.000 / 0.080 of trials |
| F | **pass** on all three seeds | own-directed moved in 0.0075 / 0.0000 / 0.0012 of trials, against 0.0125 / 0.0000 / 0.0000 under a random subspace | pass |
| M | **no verdict** on all three seeds | 0 of 44 clear, although the arm scores 0.5517 to 0.5663 on the named-other condition. ARGUED: two fifths of its named-other actions are answered by the separable route from metadata, as in arm T, so no transplant into the state can move enough of them | pass |

**The one pass means little. ARGUED.** On the free arm the nominated named-agent
subspace moves the *named-other* action itself in only 0.115, 0.001 and 0.035 of
trials. A representation that barely moves the action it is about cannot show
much by failing to move a different one. And the arm has not learned the
named-other condition (§2).

**So control 2, as the proposal words it, cannot be run as a check on the arms
that matter until the named-other condition is learned** — and on the
constructed arms it cannot be run at all, because they select the named agent
outside the running state. ARGUED: the registration should either say so and
record control 2 as "not applicable" on arms T and M, or reword it; it should not
be carried as a control that holds.

The old control 2 (an unmatched episode's ownership subspace), kept for
continuity, returns the one-in-four rate on arm T again (0.2512 / 0.2350 /
0.2562), as on 2026-09-21.

---

## 5. Item 4 — the fourth arm, built to be partly separable (ruling page 5)

**The construction** (`src/arm_middle.py`, method note §5): arm T's slot and
head, and arm C's entangling and ordinary output layer, in one network; actions
about items `it1` to `it3` go through the entangled route, `it0` and `it4`
through the separable one, about three fifths entangled (0.6033 of the fresh
episodes, `measure_base_M.json`). Its self-test passes all seven checks,
including "perturbing the slot never moves an entangled-route action" (largest
logit movement 0.00e+00) — `out-repairs/self-tests.txt`. **It is a mixture by
item, not partial separation within each trial**, and page 5's strongest
argument against applies in full: its degree is a design intention, and it
differs from both anchors in more than degree.

**The prediction, from the method note, fixed before the run:** the blind
reading between 0.30 and 0.60 on every seed, and within 0.10 of the formula
`p·(a_C − u_C) / [(1 − p)·(a_T − u_T) + p·(a_C − u_C)]` on the arm's own route
accuracies; and, from the record's arm C figures, a number near 0.42 to 0.43.

MEASURED, from `out-repairs/measure_base_M.json` and `gate_base.json`:

| seed | blind reading | the formula on this arm's route accuracies | handed its true slot | separable route: whole / untouched | entangled route: whole / untouched |
|---|---|---|---|---|---|
| 0 | **0.5105** | 0.4895 | 0.4895 | 1.0000 / 0.0000 | 0.6501 / 0.0207 |
| 1 | **0.4846** | 0.4572 | 0.4572 | 1.0000 / 0.0000 | 0.5818 / 0.0290 |
| 2 | **0.5322** | 0.4904 | 0.4904 | 1.0000 / 0.0000 | 0.6542 / 0.0228 |

- **Page 5's pass, 0.3 to 0.7 on all three seeds: passes.**
- **The method note's band, 0.30 to 0.60: passes. Within 0.10 of the formula:
  passes** (misses 0.021, 0.027, 0.042).
- **The number predicted from the record, 0.42 to 0.43, was low.** The entangled
  route learned better in arm M than arm C does alone: 0.77 to 0.78 on the
  own-directed condition on the gate episodes (`gate_base.json`,
  `own_by_route`), against arm C's 0.57 to 0.58. It therefore carries more of
  the effect. The formula, evaluated on the measured routes, is the prediction
  that held.
- **The blind reading is slightly above the true-slot reading** on every seed,
  because the blind ownership subspace catches 0.92 to 0.96 of the separable
  route's effect rather than all of it (`ownership_only_by_route`).
- Arm M passes the learn-both gate on both conditions on all three seeds
  (own-directed 0.8613 to 0.8667, named-other 0.5517 to 0.5663, `gate_base.json`).
- Control 6 is cleaner than on arms C and F: the same-value cell moves in 0.235 /
  0.173 / 0.321 of trials (the entangled route's share), and the different-value
  cell in 0.846 to 0.953.
- Arm M has an entangled route, so it is not expected to reproduce exactly from
  code and seed; quote it as **0.48 to 0.53, in the middle of the scale**.

**What passing buys, ARGUED.** It shows the measure, pointed blind at a system
with a known mixture, returns a number in the middle and near the mixture's
share. It does not show that the measure scales on a system whose partial
separation is *within* each trial, which is what a freely trained system would
have. Under page 5 the arm is now a candidate for the main registration, with
three runs at $32 to $44 from page 6's $450 envelope; **folding it in is John's
decision**, and this session makes no recommendation stronger than that.

---

## 6. Item 5 — the measure with the ruled form and the ruled numbers

    ../../../.venv/bin/python repairs.py --stage measure --arms <arms> --recipes base
    ../../../.venv/bin/python repairs.py --stage gate --arms T,C,F,M,blind --recipes base
    ../../../.venv/bin/python repairs.py --stage summary --arms T,C,F,M --recipes base

Run on the unchanged recipe only, because no redesign passed (method note §2.4).
Fresh episodes: 800 matched pairs, 1,600 trials per arm and seed.

### 6.1 The gates (pages 1b and 1h)

MEASURED, `out-repairs/gate_base.json` (3,000 episodes; bar 790 correct):

| arm | own-directed, seeds 0 / 1 / 2 | named-other, seeds 0 / 1 / 2 | learn-both (page 1b) | lesion: own-directed with the acting channel removed |
|---|---|---|---|---|
| T | 1.0000 on all three | 1.0000 on all three | **passes** | 0.2467 / 0.2510 / 0.2733 (reported, not gated) |
| C | 0.5703 / 0.5677 / 0.5757 | 0.2533 / 0.2503 / 0.2360 | **fails** (named-other 0 of 3) | 0.1780 / 0.1830 / 0.1703 (reported) |
| F | 0.5597 / 0.5513 / 0.5547 | 0.3313 / 0.2603 / 0.2487 | **fails** (named-other 1 of 3) | 0.1760 / 0.1850 / 0.1940: **collapses** under page 1h on all three seeds |
| M | 0.8640 / 0.8613 / 0.8667 | 0.5543 / 0.5663 / 0.5517 | **passes** | 0.2230 / 0.2190 / 0.2203 (reported) |
| ownership-blind solver | 0.2340 / 0.2383 / 0.2340 | 0.2373 / 0.2420 / 0.2167 | fails, as a solver with no ownership signal should | — |

The name-only solver (computed, not trained) scores 1.0000 on named-other and
0.2380 on own-directed, as on 2026-09-21. **Arm T's gate figures reproduce the
2026-09-21 record exactly**, including the three lesioned figures
(`out/gate.json`).

**Under the ruled numbers the free arm would not be read**: it fails page 1b.
Its reading below is reported as the rehearsal reports everything, and is not a
reading the registered procedure would make.

### 6.2 The reading, chance-corrected (page 2), with the floor of page 1c

MEASURED, `out-repairs/measure_base_T_C.json`, `measure_base_F.json`,
`measure_base_M.json`, `summary_base.json`:

| arm | untouched | whole-state | ownership-only | reading (chance-corrected) | raw difference | spread across seeds of the raw difference (page 1g) | within-seed bootstrap |
|---|---|---|---|---|---|---|---|
| T, seeds 0 / 1 / 2 | 0.0000 × 3 | 1.0000 × 3 | 1.0000 × 3 | **0.0000 × 3** | 0.0000 × 3 | 0.0000 | 0.0000 |
| C | 0.049 to 0.060 | 0.50 to 0.59 | 0.052 to 0.060 | **0.99 to 1.00**, entangled end | 0.44 to 0.53 | 0.0466 | 0.0194 to 0.0203 |
| F | 0.056 to 0.069 | 0.485 to 0.568 | 0.056 to 0.069 | **1.00 to 1.003**, entangled end | 0.42 to 0.51 | 0.0499 | 0.0189 to 0.0202 |
| M | 0.012 to 0.018 | 0.75 to 0.79 | 0.38 to 0.39 | **0.48 to 0.53**, the middle | 0.35 to 0.41 | 0.0309 | 0.0167 to 0.0184 |

- **Every reading is valid under the floor**: on every arm and seed the
  whole-state transplant's room over the untouched rate clears four fifths of the
  arm's own room (`reading.floor` fields).
- **Separation (page 1a): arm C minus arm T is 0.9977, 0.9927 and 1.0000 on
  seeds 0, 1 and 2, all above 0.5** (`summary_base.json`, `separation`).
- **The chance-corrected reading can exceed 1.** The free arm at seed 0 reads
  1.0029, and the sensitivity pick on arm C seed 0 reads 1.0051, because the
  ownership-only transplant landed slightly *below* the untouched rate. That is
  sampling noise around "the subspace does nothing", but the registration should
  say a reading above 1 is reported as observed, not clipped, as page 2 already
  says of a negative one. ARGUED.
- **Page 1g, as ruled, reports the across-seed spread; the bootstrap is less
  than half of it on arms C and F.** On 2026-09-21 the two agreed closely
  (rehearsal findings, section 11: 0.0189 and 0.0227 against 0.0198 and 0.0203).
  Here the across-seed spread is 0.0466 and 0.0499. MEASURED; the ruling's
  sentence that neither method measures drift between runs of one seed stands.
- **The rank cap of 8 (page 1d) did not bind on arms C and F**: the rule chose
  ranks 1, 2 and 4 there, because no rank moves those arms (§3 table). On arms T
  and M it chose 8 on every seed.

### 6.3 The controls

MEASURED, `controls` fields in the `measure_base_*.json` files. Ranges across
the three seeds:

| control | T | C | F | M | what it should show |
|---|---|---|---|---|---|
| 1. the complement of the nominated subspace | 0.0000 | 0.50 to 0.57 | 0.49 to 0.56 | 0.36 to 0.42 | action follows content, not identity |
| 2. as the proposal states it | no verdict | no verdict | pass (weak, §4) | no verdict | own-directed action does not move |
| 3. a random subspace, same rank | 0.0000 | 0.049 to 0.063 | 0.059 to 0.071 | 0.013 to 0.056 | no donor action |
| 4. before the identity can be known | 0.0000 | 0.14 to 0.16 | 0.06 to 0.15 | 0.03 to 0.12 | nothing happens |
| 6a. same-value cell, share moved | 0.000 | 0.59 to 0.72 | 0.64 to 0.74 | 0.17 to 0.32 | nothing moves |
| 6b. different-value cell, share moved | 1.000 | 0.90 to 0.91 | 0.88 to 0.90 | 0.85 to 0.95 | everything moves |
| 7. null transplant, bit-identical | yes | yes | yes | yes | nothing changes |

Controls 1 and 6 behave as on 2026-09-21, and the two findings about them stand
(rehearsal findings, section 6): control 1 cannot hold on an entangled arm by
construction, and control 6's same-value cell moves in well over half the trials
on arms C and F.

**Control 4 is worth a second look. ARGUED.** A transplant before the identity
can be known moves the donor's action in up to 0.16 of trials on arms C and F,
against untouched rates near 0.05 to 0.07. At the nominated sites those arms
receive the ownership signal by other routes (C by its side route, F by the
acting channel added at the embedding), so "before the identity can be known" is
not the same as "before the state differs". It did not reach the pre-stated
"nothing happens" on those arms here. On 2026-09-21 it read 0.0650 on arm C and
0.0600 on the free arm at seed 0 (rehearsal findings, section 6, which prints
seed 0 only), close to their untouched rates, which suggests it depends on where
the rule looks.

### 6.4 The no-transplant rate against the review's formula

MEASURED, `no_transplant_rate_miss` fields: arm T misses by 0.0000; arm C by
−0.0132, −0.0111 and −0.0039; the free arm by −0.0043, −0.0057 and +0.0054. All
are inside the 0.0175 room page 2 asked the rule to carry.

---

## 7. What this means for the registration text (ARGUED; for session (d))

1. **Page 4 (d) applies**, with one sentence added: a curriculum and loss
   re-weighting also failed at toy scale, and both made the named-other condition
   worse. Whether to attempt redesign (c), a grammar change, is John's.
2. **The degenerate exclusion must cover every all-positions site set**, not
   only "every layer at every position" (§3).
3. **The site-list rule and the printed list must agree.** The rule gives 296
   on the toy and 1,816 on the registered model with the toy's position sets;
   the 176 is the hand list's (§3).
4. **"The smallest layer set that clears it" needs one reading in words**; the
   two readings disagree on 7 of 12 arm-and-seed pairs (§3).
5. **Control 2 as worded cannot be run on arms T and M, and gives no verdict on
   arms that have not learned the named-other condition** (§4).
6. **A chance-corrected reading above 1 is reported as observed** (§6.2).
7. **The rider stays in the reporting table**; on the toy it returns "no
   verdict" for every arm but T (§3).
8. **Arm M passed page 5's line**; folding it in is a page 5 and page 6 decision.

---

## 8. Where running it differed from planning it

1. **Two additions not pre-stated**, committed as code before their output in
   `81dc84d` and labelled so in the code: the named-other diagnostic (§2),
   written after the curriculum scored below one in four; and the sensitivity
   pick without all-positions sets (§3), written after arm C's nominations.
   Neither replaces a pre-stated quantity.
2. **The prediction's number was low** (§5): 0.42 to 0.43 predicted from the
   record, against 0.46 to 0.49 from the arm's own routes and 0.48 to 0.53
   measured. The band and the formula check held.
3. **The ownership-blind solver was trained on three seeds, not one** as on
   2026-09-21; the extra two cost nothing but time.
4. **`gate_base.json` was written twice**: once early on arms T and F only, then
   on every arm. The committed file is the second; its arm T and F rows match
   the first, which were quoted in this session's chat before the second run.
5. **Laptop time**: 21 training runs, 5.68 hours of training summed across them
   (`train_*.json`), in two parallel streams of 9,161 and 11,307 seconds of wall
   time (the local training logs, which are not committed). Within the four to
   six hours the method note estimated. $0.

---

## 9. What still needs John

| decision | what this session found | where |
|---|---|---|
| Whether to attempt page 4's redesign (c), a grammar change, or to let (d) stand | both training redesigns failed; the evidence points at the grammar giving both action turns the same acting signal | §2 |
| Whether arm M is folded into the main registration (page 5, with page 6's envelope, $32 to $44 for three runs) | it passed the pre-stated line on all three seeds | §5 |
| Widening the degenerate-set exclusion to every all-positions site set | the ruled exclusion let the rule pick a degenerate set on arm C | §3 |
| Which reading of "the smallest layer set that clears it" is registered | the two disagree on 7 of 12 pairs | §3 |
| How control 2 is worded, or recorded as not applicable on arms T and M | as worded it returns no verdict on three arms of four | §4 |
| The rented slice (page 9), unchanged | not touched by this session; its go has not been given | ruling page 9 |

Nothing here is ruled. The pairing rule applies: this file is checked by a
session that did not write it, on the checker prompt in
`docs/weekend-1-session-prompts.md`, section (c).
