# The successor experiment's measurement rehearsal — findings

*2026-09-21 (Pacific). **UNREGISTERED.** Nothing here is a result about the
scientific question, nothing here is a bar, and nothing here registers
anything. It is a demonstration that the instrument exists and gives back
numbers — and, where it does not, an account of why.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent.** The one short slice of rented time is staged and has not been run; it
needs John's spoken go naming it, and that has not been given.*

*Filed at the path the protocol names for a rehearsal whose experiment
directory does not exist yet. Code and every output file:
`experiments/rehearsal-successor-measure/`.*

*Written under the workspace plain-language rule.*

---

## 0. What to read if you read nothing else

The measure works, and the procedure for pointing it at a system does not.

- **The measure separates the two constructed arms by the whole width of its
  scale.** The arm built so that the ownership answer sits in a slot of its
  own reads **exactly 0.0000** on all three seeds. The arm built so the
  ownership answer is stirred through everything reads **0.873, 0.885 and
  0.880**. That is rehearsal item R-2 and R-3 both passing, and it is the
  thing the successor experiment most needed to know.
- **The nomination procedure as the proposal writes it fails completely**, on
  the one arm whose answer is in a known place. It returns 0.0000 to 0.0117
  where the truth is 1.0000 — that is, it reads the separable arm as
  maximally entangled. The cause is that the proposal names the quantity the
  straight-line read is fitted to and never says what the **label** is, and in
  a grammar whose marker words are drawn afresh each episode that phrase has
  three meanings, two of which find nothing.
- **The two findings the proposal review marked fatal are both confirmed**, by
  measurement rather than by argument, and one of them is confirmed to four
  decimal places.
- **The freely trained arm reads at the entangled end**, not between the two
  anchors. That is either the honest answer or the instrument's ceiling, and
  the rehearsal cannot tell which.
- **Two of the seven controls do not mean what they say they mean**, and one
  of them would veto exactly the arm it exists to validate.
- **Throughput**: the two constructed architectures cost 0.98 and 1.05 times
  what the free one costs per step, not the 1.55 the money estimate inherited
  from a different experiment. Only the *ratio* is measured; the absolute
  figure the second release of money rests on still needs the rented slice.

---

## 1. What was committed when

The programme's discipline is method before output, and the worst failure in
its history came from a fix marked adopted with nobody having run anything.
The commit order on this branch:

| order | commit | what |
|---|---|---|
| 1 | `9a91c06` | the method: what would be built, and passing, failing and no-verdict for every check, written down while nobody knew which would fire |
| 2 | `518bf0e` | the method addendum: four further checks, after the review returned two findings marked fatal — again committed before their code |
| 3 | `5fa85e2` | the code: the grammar, the three architectures, the transplanting code, the measure |
| 4 | `8bc5fbe` | the rented slice, staged and not run |
| 5 | `9673bf1`, `4e89c69`, `623ef23` | the denominator checks, the frozen reads, the across-seed method, the self-test record |
| 6 | `6e8cc08` | the results |
| 7 | this file | the findings |

Section 9 records every place where building it differed from planning it,
which is the only honest way to keep a method file that was committed first.

---

## 2. The six checks the protocol requires

Each with the command that was run and the output it produced. The full output
of every one is in `experiments/rehearsal-successor-measure/out/`.

### P-1. The target can be found — **PASS, but only after a repair**

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python rehearse.py --stage nominate

The instrument is the proposal's own two-step nomination: fit a straight-line
read for "which agent is acting" at every candidate site, take its leading
directions up to a rank cap, then nominate by **causal effect** — the subspace
whose transplant best reproduces the counterfactual on development episodes.
It runs blind on every arm; the separable arm's known ownership block is never
handed to it.

On the separable arm, where the answer is in a known place by construction:

| seed | the procedure **as pre-stated** | the procedure **repaired** | the truth (its real ownership block) |
|---|---|---|---|
| 0 | 0.0117 | **1.0000** | 1.0000 |
| 1 | 0.0000 | **1.0000** | 1.0000 |
| 2 | 0.0000 | **1.0000** | 1.0000 |

The repair is section 3. **As written the procedure fails**; repaired, it
finds the answer exactly, and the reading it produces matches what the
procedure gets when it is simply handed the true block.

### P-2. The comparison has room to move — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Both ordinary competing solvers were built and scored on both conditions, and
all seven controls were run on every arm and seed. Nothing was assumed.

| solver | own-directed | named-other-directed |
|---|---|---|
| ownership-blind (trained, acting channel removed) | 0.2237 | 0.2253 |
| name-only (computed) | 0.2380 | 1.0000 |
| references: guessing over eight slots / a solver that cannot tell whose value it needs | 0.1250 / 0.2500 | 0.1250 / 0.2500 |

The comparison is not saturated: the separable arm reaches 1.0000 on both
conditions against an ownership-blind competitor at 0.2237.

### P-3. The arithmetic is finite — **PASS**

    ../../../.venv/bin/python measure.py --self-test

Sixteen made-up cases chosen to break the formula, including a zero
denominator, a denominator just under and just over the floor, an
ownership-only accuracy above the whole-state one, both accuracies equal and
both zero. Every one returns a finite number or the explicit no-verdict
outcome with its reason. All 10,201 share pairs from zero to one were swept:
none returns a non-finite value. A floor of zero is refused outright, because
a floor of zero is the closed design's unsatisfiable-denominator defect
re-entering through the front door.

### P-4. The interventions run end to end — **PASS**

    ../../../.venv/bin/python transplant.py --self-test
    ../../../.venv/bin/python rehearse.py --stage transplant

Every arm is trained, **saved to a checkpoint file and read back from it**
before any intervention runs, so what is exercised is the path the registered
experiment would use. Eight interventions run to completion on every arm and
seed: the whole-state transplant, the ownership-only transplant, the null
transplant, the content-complement transplant, the matched random-subspace
transplant, an unmatched donor's transplant, a transplant at a position where
the identity cannot yet be known, and the acting-channel lesion.

They move what they are supposed to move: on the separable arm the whole-state
transplant takes the donor-dictated action from 0.0000 to 1.0000.

### P-5. All three outcomes are reachable — **PASS**

    ../../../.venv/bin/python rehearse.py --stage outcomes
    ../../../.venv/bin/python negative_case.py

| made-up case | expected | measured |
|---|---|---|
| the separable arm at its nominated site set | near zero, valid | **0.0000, 0.0000, 0.0000** |
| the entangled arm at its nominated site set | high, valid | **0.8727, 0.8848, 0.8801** |
| the separable arm at a deliberately failing site set (earliest layer, before the identity can be known) | no verdict | **no verdict**, whole-state accuracy 0.0000 |
| a negative reading | reachable | **−0.1706 and −0.2755** |

The negative reading deserves its own sentence, because finding it took
finding out what causes it. Searched over every architecture, every one of the
nine layer sets, every one of the five position sets, all three readings of
the read's label and all six rank caps on fresh episodes, **no configuration
produced a negative reading at all**. It appears immediately on episodes whose
marker words the arms have never seen. The condition is therefore not
mysterious and it is worth registering: **a negative reading appears when the
subspace was chosen on data whose vocabulary the reading is then taken on.**
The nominated directions live in the well-trained part of the space; the
whole-state transplant is capped by the arm's own degraded accuracy on strange
words; so the subspace beats the superspace and the reading goes below zero.
That is exactly what the proposal says a negative reading is for — a warning
about the instrument, reported as observed and never clipped to zero.

### P-6. An ordinary competing solver is built and scored — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Two were built, because "satisfied by the wrong thing" has two shapes here. An
**ownership-blind solver** — the same architecture with the acting channel
removed entirely, so it has none of the structure the measure claims to detect
— scores 0.2237 on the own-directed condition and 0.2253 on the named-other
one, which is the one-in-four level and nothing more. A **name-only solver**,
computed rather than trained, gets the named-other condition exactly right and
the own-directed condition at 0.2380.

The measure does not read near-zero degree off the blind solver, because the
blind solver cannot be read at all: its own-directed action does not depend on
an ownership answer it does not have, so there is nothing for a transplant to
move. **That is the right answer** — a system with none of the structure
returns no reading rather than a flattering one.

---

## 2a. The proposal's ten rehearsal items, and where each one stands

| item | what it had to show | state |
|---|---|---|
| **R-1** the grammar works and both conditions are learnable at tiny scale | both matched conditions above the one-in-four level; the four matched properties hold in the generated data | **FAIL on one half.** All four matched properties pass their checks. The own-directed condition clears its bar on every arm and seed. The named-other-directed condition clears it on one seed of three on the entangled arm and one of three on the free arm, and doubling the training budget moves it about a point. Section 8 |
| **R-2** the separable arm is constructible and its pointer is transplantable on its own | blind nomination finds it without being told where it is; the ownership-only transplant reproduces the counterfactual | **PASS on the arm, FAIL on the procedure as written.** The arm is constructible and its pointer is patchable on its own: the reading is exactly 0.0000 on all three seeds. The blind nomination finds it only under one of three readings of the read's label, and returns near zero under the other two. Section 3 |
| **R-3** the entangled arm is constructible and its degree is genuinely known by construction | no subspace reproduces the counterfactual while the whole-state transplant at the same sites does | **PASS.** Whole-state 0.540 to 0.575 against a best blind-nominated subspace of 0.066 to 0.069, on all three seeds. The two-arm fallback does not fire |
| **R-4** all four outcomes of the measure are reachable | near zero, high, negative, no verdict | **PASS.** 0.0000; 0.873 to 0.885; −0.1706 and −0.2755; and no verdict at the deliberately failing site set. The negative outcome needed its cause found before it could be produced at all — section 2, P-5 |
| **R-5** an ordinary competing solver is built and measured | a solver that cannot use ownership and a solver that uses only the name token, both scored on both conditions | **PASS.** 0.2237 and 0.2253; 0.2380 and 1.0000 |
| **R-6** the arithmetic is finite | the floor rule and the no-verdict rule exercised on cases chosen to break them | **PASS.** Sixteen made-up cases, 10,201 share pairs swept, no non-finite value, a floor of zero refused |
| **R-7** throughput is measured, per arm | seconds per step and projected wall-clock and money for each architecture at the registered size | **PARTIAL, and it is the one place the rehearsal reaches a question only a rented machine can answer.** The ratios between the three architectures are measured at 0.981, 1.049 and 1.000. The absolute seconds per step on rented hardware cannot be obtained on a laptop. Section 10 |
| **R-8** the transplanting code passes its known-answer tests | the null transplant changes nothing; a transplant moves the action to the donor's value; the ownership-only transplant is the whole-state one restricted to a subspace | **PASS.** The null transplant leaves every logit bit-identical on every arm and seed. The restriction property is proved as a tensor identity at full rank, with a largest logit difference of exactly zero. The transplant moves the separable arm's action from 0.0000 to 1.0000 |
| **R-9** the paired-uncertainty method is chosen and demonstrated | two candidates computed on the same data, and the seed count following from the method rather than from habit | **DEMONSTRATED; the choice is not made here.** Across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. They agree closely, which is the useful finding. The arithmetic for a half-width of 0.05 implies one seed at toy scale, which should not be carried across without a discount |
| **R-10** the separation bar is set | the observed separation between the two constructed arms and its spread, with the reasoning written out | **MEASURED, DELIBERATELY NOT SET.** 0.873 to 0.885 against exactly 0.0000, across-seed spread 0.019 and 0.000. Fixing the bar is John's; the measurement shows the choice is not a close one |

---

## 3. The finding that matters most: the nomination step is underspecified

Section 7.2 of the proposal says: *fit a straight-line read for "which agent is
acting"*. It never says what the label is. In a grammar whose marker words are
drawn afresh every episode — which both the registered generator and this
stand-in do, on purpose, so that no marker word is attached to any agent —
that phrase has at least three meanings:

- **the agent's slot** in the episode's list of agents. This is arbitrary per
  episode: nothing in the episode defines it, so no state can carry it. It is
  also the natural reading of the proposal's sentence, and it is the one the
  method file pre-stated.
- **the rank of the model's own marker word** among the four present, in
  vocabulary order. This is the programme's own existing convention, from the
  method file for the eleven-position fitted read.
- **which marker word is the model's own**, out of the pool.

How well each fits, at the action position, and what each finds when its
directions are transplanted into the arm whose answer is in a known place:

| reading of the label | how well it fits | ownership-only transplant, best over every rank |
|---|---|---|
| the agent's slot | 0.256 (chance is 0.25) | **0.0000** |
| the marker's rank — *the programme's own convention* | 0.706 | **0.0000** |
| which marker word | 1.000 | **1.0000** at rank 8 and above |

Three things follow, and all three belong in the registration text.

1. **The registration must say what the label is.** Under two of the three
   readings the measure would have reported the separable arm — the arm whose
   degree is zero by construction — as maximally entangled. That is a wrong
   answer of the largest possible size, produced by a sentence nobody thought
   was ambiguous.
2. **The programme's existing convention is one of the two that fail.** The
   marker-rank label fits at 0.706, well above chance, and has **zero** causal
   effect. This is the programme's own lesson arriving in a new shape: a
   representation a straight-line read recovers beautifully can do nothing when
   you intervene on it. The proposal already says to nominate by causal effect
   rather than by fit, and this rehearsal is the first thing in the programme
   to show what that rule buys.
3. **The rank cap is not free either.** With the right label, the
   ownership-only transplant on the separable arm goes 0.170 at rank 1, 0.365
   at rank 2, 0.805 at rank 4, and **1.000 at rank 8**. A cap below the
   dimensionality of the encoding cannot carry the answer however well the
   subspace is chosen, so a rank cap chosen for parsimony would have produced a
   partial reading and been indistinguishable from partial entanglement.

---

## 4. The reading, on fresh episodes

    ../../../.venv/bin/python rehearse.py --stage transplant

Both candidate forms of the reading are reported everywhere. Neither is
adopted here.

| arm and seed | no transplant | whole-state | ownership-only | the reading as registered | the floor-corrected reading |
|---|---|---|---|---|---|
| separable, seed 0 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| separable, seed 1 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| separable, seed 2 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| entangled, seed 0 | 0.0600 | 0.5400 | 0.0688 | **0.8727** | 0.9818 |
| entangled, seed 1 | 0.0663 | 0.5750 | 0.0663 | **0.8848** | 1.0000 |
| entangled, seed 2 | 0.0638 | 0.5525 | 0.0663 | **0.8801** | 0.9949 |
| free, seed 0 | 0.0600 | 0.5825 | 0.0663 | **0.8863** | 0.9880 |
| free, seed 1 | 0.0550 | 0.5663 | 0.0925 | **0.8366** | 0.9267 |
| free, seed 2 | 0.0762 | 0.5663 | 0.0850 | **0.8499** | 0.9821 |

**The separation between the two constructed arms is the whole scale.** Zero
against roughly 0.88, with an across-seed spread of 0.019 on the entangled arm
and exactly zero on the separable one.

**The free arm sits at the entangled end.** Its three readings, 0.886, 0.837
and 0.850, are inside the entangled arm's range, not between the two anchors.
Two readings of that, and the rehearsal cannot choose between them: either a
freely trained system of this shape genuinely keeps its ownership answer
distributed, or the instrument saturates and cannot tell "quite entangled"
from "entangled by construction". Section 7 says what would separate them.

---

## 5. The two findings the review marked fatal, both confirmed

### The reading divides by an uncorrected accuracy — **confirmed**

    ../../../.venv/bin/python denominator.py --stage simulated
    ../../../.venv/bin/python denominator.py --stage attenuated

On made-up trial populations built from a **known** true share of the
identity-driven difference living outside the subspace — 0.5 in both cases —
and two different transplant effectivenesses, drawn 200 times at 2,000 trials
each:

| case | whole-state accuracy | the reading as registered | the floor-corrected reading |
|---|---|---|---|
| strong transplant | 0.9008 | 0.4323 (spread 0.0119) | **0.5018** (spread 0.0132) |
| weak transplant | 0.3497 | 0.3222 (spread 0.0181) | **0.5013** (spread 0.0230) |

The floor-corrected form returns the true share in both cases. The registered
form differs between two systems that are identical in the quantity it claims
to report, by 0.110 — six times its own spread.

On **real forward passes**, holding the architecture, the sites and the
subspace fixed and only moving the state a fraction of the way toward the
donor's, the same thing happens: on six of the nine arms and seeds the
floor-corrected form is markedly the flatter of the two. On the free arm at
seed 2 the registered reading spans **0.517** across the attenuation while the
floor-corrected one spans 0.073, and on the entangled arm at seed 1 the
registered reading spans 0.342 against 0.016.

**One measurement makes this less alarming than it looks, and it is worth
putting beside the finding.** The correction's size is the no-transplant rate,
and on a working arm that rate is near zero, so the two forms nearly coincide
in the table in section 4. The gap opens exactly where the whole-state
transplant is weak — which is where the proposal's own weakness list expects
the entangled arm to be. So the finding bites on the arm it was predicted to
bite on, and not before.

**Nothing here chooses a form.** Both are computed, both are reported, and
which is registered is John's to rule on.

### A control's first cell is empty by construction — **confirmed exactly**

    ../../../.venv/bin/python denominator.py --stage control6
    ../../../.venv/bin/python denominator.py --stage floor

Under a grammar that keeps the four values within an item distinct — which the
proposal requires in three places — **0 of 4,000 trials** fall in the cell
where the donor's identity dictates the same value as the recipient's. The
reason is structural, not statistical: within an item the four values are
distinct and the successor rule is one-to-one, so distinct sources give
distinct answers, always.

Filling the cell means relaxing distinctness, and that costs something
measurable: on a relaxed set, 346 of 4,000 trials land in the cell, and the
reference a solver that cannot tell which agent it is can reach moves from
**0.2467 to 0.3095** on exactly the trials that were added.

The same distinctness inverts the proposal's sanity rule on the no-transplant
rate. Measured against both predictions on the record:

| arm and seed | measured | the proposal says | the review's formula says |
|---|---|---|---|
| separable, all three seeds | 0.0000 | 0.1250 | 0.0000 |
| entangled, seed 0 | 0.0600 | 0.1250 | 0.0598 |
| entangled, seed 1 | 0.0663 | 0.1250 | 0.0620 |
| entangled, seed 2 | 0.0638 | 0.1250 | 0.0605 |
| free, seed 0 | 0.0600 | 0.1250 | 0.0624 |
| free, seed 1 | 0.0550 | 0.1250 | 0.0634 |
| free, seed 2 | 0.0762 | 0.1250 | 0.0587 |

The review's formula predicts every measured value to within a few
thousandths; the proposal's "near one in eight" is wrong on every arm, and is
wrong in the direction that matters: it **passes for a model at chance and
fails for a model that works**. As registered it would call a working
instrument broken.

---

## 6. The seven controls, and the two that do not mean what they say

Run on every arm and seed. The table below is seed 0 of each arm; the rest are
in `out/transplant.json`.

| control | separable | entangled | free | what it should show |
|---|---|---|---|---|
| 1. transplant the complement of the nominated subspace | 0.0000 | 0.5375 | 0.5813 | the action follows content, not identity |
| 2. an unmatched donor's representation | 0.2513 | 0.0525 | 0.0613 | the action does not move |
| 3. a matched random subspace of the same rank | 0.0000 | 0.1113 | 0.0975 | no donor action |
| 4. a transplant before the identity can be known | 0.0000 | 0.0650 | 0.0600 | nothing happens |
| 5. fresh marker and content combinations | by construction | by construction | by construction | — |
| 6a. same-value cell: share whose action moved | **0.000** | 0.691 | 0.741 | nothing moves |
| 6b. different-value cell: share whose action moved | **1.000** | 0.921 | 0.908 | everything moves |
| 7. null transplant leaves every logit bit-identical | true | true | true | nothing changes |

**Control 6 is the one that earns its place, and it says something
uncomfortable.** On the separable arm it discriminates perfectly: nothing moves
when the donor's identity dictates the same value, everything moves when it
dictates a different one. That is precisely what "the transplant moved who is
acting" looks like. On the entangled and free arms the action moves in about
**three quarters** of the same-value trials, where it should move in none. On
those arms the whole-state transplant is carrying something besides identity,
and the reading of roughly 0.88 cannot be read as purely a statement about
where the ownership answer lives. This is the outside review's "satisfied by
the wrong thing" worry arriving with a number attached, and it is the single
most important caveat on section 4's table.

**Control 1 cannot hold for an entangled arm, by construction.** Transplanting
the complement of the nominated subspace reproduces the counterfactual almost
exactly as well as transplanting the whole state — 0.5375 against 0.5400. That
is not a defect in the arm; it is what entanglement *means*. In a system where
the ownership signal multiplies content at every layer there is no
ownership-free complement to transplant. **As the proposal writes it, control
1 would veto the reading on exactly the arm the control battery exists to
validate.** It needs re-wording before registration: on the separable arm it
is a real and passing check (0.0000), and on an entangled arm it should be
recorded as not applicable and said so, rather than failed.

**Control 2 was implemented differently from the proposal and its number
should not be read as a pass.** The proposal asks for a representation of a
*named agent who is not acting*, nominated by the identical procedure. What
was run instead transplants the ownership subspace of an *unmatched* episode.
On the separable arm that gives 0.2513, which is the one-in-four rate — the
action moved to an arbitrary identity and coincided with the matched donor's
by chance. The control as the proposal states it is still owed.

---

## 7. What would make the experiment look unbuildable, or the measure
unreadable — the honest list

This is the part worth more than a clean report.

1. **The free arm is not between the anchors; it is at one of them.** Readings
   of 0.886, 0.837 and 0.850 against an entangled arm at 0.873 to 0.885. If
   that holds at the registered size, the promised outcome — "the closure
   sentence *degree unmeasured* is replaced by a number" — is delivered, but
   the number is "as entangled as a system built to be entangled", and the
   measure will not have demonstrated that it **scales** rather than merely
   **detects**. What would separate the two readings is a fourth arm built to
   sit deliberately in the middle, which this rehearsal did not build and which
   the proposal does not have. **Recommendation, for John to rule on: add a
   partially-separable arm to the design, or accept in the registration text
   that a free-arm reading near the entangled anchor cannot be told from a
   ceiling.**
2. **Control 6 fails its pre-stated shape on two of the three arms.** Three
   quarters of the same-value trials move. Until that is understood the
   roughly-0.88 readings are not clean statements about where the ownership
   answer lives.
3. **The whole-state transplant can never beat the arm's own accuracy**, and
   at toy scale that ceiling is about 0.55 on the entangled and free arms
   because that is all those arms can do. Every floor, and every separation
   bar, is therefore a statement about a denominator that is itself bounded by
   how well the arm learned. A floor named as an absolute number would be
   wrong; it has to be named relative to the arm's own accuracy on the same
   episodes. That is a change to the proposal's section 6.4.
4. **The freshness requirement is ambiguous and the strong reading breaks the
   measurement.** Section 7.1 asks for "marker and content combinations that
   appear in neither of the other two sets". Read as *combinations*, the
   separable arm scores 1.0000 and the measure reads 0.0000. Read as *marker
   words the arm has never seen*, the separable arm's own accuracy falls to
   0.7612, 0.6512 and 0.6512, the whole-state transplant is capped there, and
   the reading goes **negative** on two seeds out of three. The registration
   has to say which reading it means. (The strong reading is what produced the
   negative case in section 2, so it is worth keeping as a deliberate
   diagnostic, not as the evaluation set.)
5. **The degenerate site set is real and has to be excluded in writing.**
   Transplanting every layer at every position is not an intervention: it is
   the donor's own forward pass, proved as a tensor identity in the
   transplanting code's self-test. On the separable arm the whole-state
   accuracy is 1.0000 at *every one* of the forty-five site sets, so the
   "smallest layer set that clears the floor" rule the proposal gives has
   nothing to choose between and would pick arbitrarily.
6. **The named-other condition barely learns at toy scale, and doubling the
   training budget does not fix it.** This is what the proposal's own honest
   prior predicts for the whole experiment, reproduced for nothing. See
   section 8.

---

## 8. The learn-both gate, and the condition that did not learn

    ../../../.venv/bin/python rehearse.py --stage gate

| arm and seed | own-directed | named-other-directed | own-directed with the acting channel removed |
|---|---|---|---|
| separable, 0 / 1 / 2 | 1.0000 / 1.0000 / 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.2467 / 0.2510 / 0.2733 |
| entangled, 0 / 1 / 2 | 0.5817 / 0.5660 / 0.5767 | 0.2590 / 0.2370 / 0.2637 | 0.1717 / 0.1807 / 0.1860 |
| free, 0 / 1 / 2 | 0.5633 / 0.5563 / 0.5890 | 0.2547 / 0.2680 / 0.2393 | 0.1813 / 0.1947 / 0.1857 |

**R-1 fails on the named-other condition, as pre-stated.** The cell fixed
before running was: both conditions above the one-in-four level, significantly
under a binomial test at the 0.05 level, on at least two seeds of three. On
3,000 held-out episodes that bar is 0.2630. The entangled and free arms clear
it on **one seed each**. The own-directed condition clears its bar
comfortably everywhere.

This is not a surprise and it is not a small thing. Section 3 of the proposal
states the honest prior before the work: the most likely outcome of the whole
experiment is that an arm fails the learn-both gate, and **the most likely
reason is the named-other half**. The rehearsal reproduces exactly that
failure, at toy scale, for about two hours of laptop time.

**Is it the budget or the task? Measured, not guessed.**

    ../../../.venv/bin/python budget_check.py

The free arm was trained once more at roughly twice the budget — 5,000 steps
instead of 2,500, on 20,000 matched pairs instead of 15,000. The named-other
condition moved from **0.2547 to 0.2657**, and the own-directed condition from
0.5633 to 0.5737. Doubling the budget bought about one percentage point on the
condition that is failing, which leaves it sitting on the bar rather than
clearing it.

**So the shortfall is not mainly a limit of the training budget.** At this
size, on this grammar, the named-other-directed revision is close to
unlearnable, and more steps do not fix it. That does not settle what happens at
the registered size — the ten-million rung failed to learn the earlier design's
task and the thirty-million rung did not — but it does mean the risk the
proposal's honest prior names is real, is reproducible on a laptop for nothing,
and would be worth attacking in the design before about $110 of registered runs
are committed to it.

**The acting-channel lesion behaves as pre-stated on the separable arm and
not on the others.** Removing the channel drops the separable arm's
own-directed accuracy to the one-in-four level (0.2467 to 0.2733) while its
named-other accuracy stays at **1.0000** — textbook. On the entangled and free
arms the lesion drops *both* conditions, because in a system where ownership
modulates everything, removing the channel disturbs everything. The
proposal's section 8.2 pre-states the shape "own-directed collapses,
named-other holds"; that shape is **architecture-specific**, and the
registration should say so rather than apply it to all arms.

---

## 9. Where building it differed from planning it

The method file is unchanged; this is the record of the departures, which is
the only honest way to keep a method that was committed first.

1. **The deliberately broken arm was not built.** The method planned an arm
   with two sign-flipped copies of the ownership answer so that the whole-state
   transplant would cancel itself. Building it showed the idea cannot work:
   because matched pairs differ only in the acting channel, the whole-state
   transplant at a site set is *exactly the donor's state there*, so any
   architecture that is consistent under it cannot be made to cancel. The
   negative outcome was pursued by a systematic search instead, and found —
   section 2, P-5 — with its cause identified. This is a better result than the
   planned one, and it was forced by the building.
2. **The nomination family was widened after the pre-stated one failed.** Three
   readings of the read's label instead of one, and rank caps to 24 instead of
   8. The pre-stated family is still computed and reported separately at every
   point, so the failure of the procedure *as written* is on the record beside
   the repaired one. 810 comparisons per arm and seed, of which 225 are the
   pre-stated family.
3. **The fitted reads were frozen.** The first implementation re-fitted the
   straight-line read on the fresh episodes the reading is taken from, which is
   the one thing a data split exists to prevent. Fixed before any result in
   this file was read; the reads are fitted on development episodes, written to
   disk, and reloaded.
4. **The fresh pool was corrected** from unseen marker words to unseen
   combinations of seen words, per section 7 item 4. The stronger pool is kept
   under its own name because its collapse is a finding.
5. **Control 2 was implemented differently from the proposal**, recorded in
   section 6 rather than quietly counted as a pass.
6. **The rehearsal ran as soon as it was built** rather than waiting for a
   slot. Nothing about it was waiting on a calendar.

---

## 10. Throughput, and exactly what still needs the rented machine

    ../../../.venv/bin/python rehearse.py --stage throughput
    ../../../.venv/bin/python bench_arms.py --device auto --steps 20

At the registered configuration's shape — 448 wide, 12 layers — timed on the
laptop's own accelerator, batch 32, twenty steps after warm-up:

| architecture | parameters | seconds per step | median | ratio to the free arm |
|---|---|---|---|---|
| the separable arm | 26,065,471 | 0.2500 | 0.2508 | **0.981** |
| the entangled arm | 29,329,735 | 0.2672 | 0.2678 | **1.049** |
| the free arm | 29,049,735 | 0.2548 | 0.2557 | **1.000** |

**This is the measurement the second release of money was waiting for, and it
is only half of it.** The proposal carried a per-step premium of about 1.55,
inferred from a different experiment's full-versus-twin step times, "to cover
arms T and C being slower per step". Measured, the premium is **about five per
cent on the entangled arm and slightly negative on the separable one**. If
that ratio holds on rented hardware, the constructed arms do not cost
materially more than the free arm, and the second release's arithmetic — the
eight remaining runs at the planning figure — needs no architecture premium at
all.

**What a laptop cannot answer, and no arithmetic here can make it.** Seconds
per step on an Apple M4 does not predict seconds per step on a rented graphics
card. What transfers is the *ratio between the three architectures*; the
absolute figure does not. That is precisely the inference John's ruling of
2026-09-21 declined to build a release on.

So: **the rented slice is still owed, and it is now owed for a smaller
question than before** — not "how much more do the constructed arms cost",
which is answered at 0.98 and 1.05, but "how many seconds does a step take on
the machine we will rent". It is staged, costed and not run:
`docs/successor-rented-slice-staging-2026-09-21.md`, and the plan the staging
script writes is in `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`.

The same slice exercises the shutdown handshake against the real vendor, which
has never met it, and the pre-stated pass and fail lines for both halves are in
that staging note.

---

## 11. The numbers this rehearsal was told not to invent

Section 9 of the proposal lists eight numbers as outputs of the rehearsal. None
is named here. What each one now has behind it:

| number | what the rehearsal measured | still needed |
|---|---|---|
| the separation bar between the two constructed arms | separation of **0.873 to 0.885** against **0.0000**, across-seed spread 0.019 on the entangled arm and 0.000 on the separable one | John's ruling. A bar anywhere from 0.1 to 0.8 would separate these two at toy scale, so the measurement does not force a choice; what it does is show the choice is not close |
| the learn-both threshold, per condition | measured competitors: ownership-blind at 0.2237 and 0.2253, name-only at 0.2380 and 1.0000 | a decision about the named-other condition, which at toy scale does not clear the one-in-four level on a majority of seeds |
| the floor on the whole-state transplant accuracy | the full curve against site set, per arm, in `out/nominate.json`: the entangled arm runs 0.0517 at the first layer, 0.3467 at the second, and about 0.556 from the third on, which is its own accuracy | John's ruling — and, per section 7 item 3, a floor stated **relative to the arm's own accuracy**, not as an absolute |
| the rank cap on the nominated subspace | 0.170 at rank 1, 0.365 at rank 2, 0.805 at rank 4, **1.000 at rank 8** on the separable arm | John's ruling; the measurement says a low cap silently under-reads |
| the candidate site list and its family correction | 45 site sets × 3 labels × 6 rank caps = **810 comparisons** per arm and seed; the pre-stated family was 225 | John's ruling on which labels are in the family at all |
| the seed count per arm | three seeds gave an across-seed spread of 0.019 and 0.023 on the raw difference; the arithmetic for a half-width of 0.05 implies **one seed** | John's ruling. The toy arms are far more repeatable than registered-size runs will be, so this number should not be carried across without a discount |
| the paired-uncertainty method | both computed on the same data: across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. **They agree closely**, which is itself the useful finding — the choice does not matter much here | John's ruling |
| the ownership-lesion collapse threshold | the separable arm drops to 0.2467 to 0.2733 on the own-directed condition while holding 1.0000 on the named-other one | a decision, plus the section 8 finding that the pre-stated shape is architecture-specific |

---

## 12. What would be needed to finish

1. **John's rulings** on the eight numbers above, on which form of the reading
   is registered, and on the nomination label — which is now a
   registration-blocking question rather than a detail.
2. **The rented slice**, which needs his spoken go naming it. About $0.75 to
   $1.00, hard cap $2.00, inside the first release.
3. **Three repairs to the proposal text**, each with a measurement behind it:
   control 1 re-worded so it cannot veto the entangled arm; the no-transplant
   sanity rule replaced with the review's formula; and section 7.1's freshness
   requirement disambiguated.
4. **A decision about the middle of the scale** — a partially separable fourth
   arm, or an admission in the registration text that a free-arm reading at the
   entangled anchor cannot be told from a ceiling.
5. **A design change for the named-other condition, or a decision to accept
   the risk.** Section 8 settles that it is not a budget limit: doubling the
   budget moved it by about a point. This is the single cheapest thing the
   rehearsal found that could sink the registered experiment, and it is worth
   attacking before the money is committed rather than after.
6. **Control 2 built as the proposal states it**, rather than as it was run.

None of the six costs more than a few hours, and only the second costs money.
