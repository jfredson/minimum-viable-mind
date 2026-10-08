*This is file 24 of 33 of one review packet, pasted into a single conversation. It contains record 16 part 2 of 3 (the measurement rehearsal on small stand-in models). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 16 of 25, part 2 of 3 - the measurement rehearsal on small stand-in models - `docs/2026-09-21-successor-measure-rehearsal.md` (complete file, 56,203 characters) =====
| item | what it had to show | state |
|---|---|---|
| **R-1** the grammar works and both conditions are learnable at tiny scale | both matched conditions above the one-in-four level; the four matched properties hold in the generated data | **FAIL on one half.** All four matched properties pass their checks. The own-directed condition clears its bar on every arm and seed. The named-other-directed condition clears it on one seed of three on the entangled arm and one of three on the free arm, and doubling the training budget moves it about a point. Section 8 — which also adjudicates the proposal's first stop condition, keyed to this item failing: **it does not fire**, because the separable arm reaches 1.0000 on both conditions on all three seeds |
| **R-2** the separable arm is constructible and its pointer is transplantable on its own | blind nomination finds it without being told where it is; the ownership-only transplant reproduces the counterfactual | **PASS on the arm, FAIL on the procedure as written.** The arm is constructible and its pointer is patchable on its own: the reading is exactly 0.0000 on all three seeds. The blind nomination finds it only under one of three readings of the read's label, and returns near zero under the other two. Section 3 |
| **R-3** the entangled arm is constructible and its degree is genuinely known by construction | no subspace reproduces the counterfactual while the whole-state transplant at the same sites does | **PASS.** Whole-state 0.540 to 0.575 against a best blind-nominated subspace of 0.066 to 0.069, on all three seeds. The two-arm fallback does not fire |
| **R-4** all four outcomes of the measure are reachable | near zero, high, negative, no verdict | **PASS.** 0.0000; 0.873 to 0.885; −0.1706 and −0.2755; and no verdict at the deliberately failing site set. The negative outcome needed its cause found before it could be produced at all — section 2, P-5 |
| **R-5** an ordinary competing solver is built and measured | a solver that cannot use ownership and a solver that uses only the name token, both scored on both conditions | **PASS.** 0.2237 and 0.2253; 0.2380 and 1.0000 |
| **R-6** the arithmetic is finite | the floor rule and the no-verdict rule exercised on cases chosen to break them | **PASS.** Sixteen made-up cases, 10,201 share pairs swept, no non-finite value, a floor of zero refused |
| **R-7** throughput is measured, per arm | seconds per step and projected wall-clock and money for each architecture at the registered size | **PARTIAL, and it is the one place the rehearsal reaches a question only a rented machine can answer.** The ratios between the three architectures are measured at 0.981, 1.049 and 1.000. The absolute seconds per step on rented hardware cannot be obtained on a laptop. Section 10 |
| **R-8** the transplanting code passes its known-answer tests | the null transplant changes nothing; a transplant moves the action to the donor's value; the ownership-only transplant is the whole-state one restricted to a subspace | **PASS.** The null transplant leaves every logit bit-identical on every arm and seed. The restriction property is proved as a tensor identity at full rank, with a largest logit difference of exactly zero. The transplant moves the separable arm's action from 0.0000 to 1.0000 |
| **R-9** the paired-uncertainty method is chosen and demonstrated | two candidates computed on the same data, and the seed count following from the method rather than from habit | **DEMONSTRATED; the choice is not made here.** Across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. They agree closely, which is the useful finding. The arithmetic for a half-width of 0.05 implies one seed at toy scale, which should not be carried across without a discount |
| **R-10** the separation bar is set | the observed separation between the two constructed arms and its spread, with the reasoning written out | **MEASURED, DELIBERATELY NOT SET.** 0.873 to 0.885 against exactly 0.0000, across-seed spread 0.019 and 0.000. Fixing the bar is John's; the measurement shows the choice is not a close one |
| **R-11** seconds per step is measured on the rented machine, for all three arms, and the shutdown path is exercised against the real vendor | seconds per training step for each architecture at the registered size, on the registered venue and rate, plus both halves of the shutdown handshake | **NOT RUN — it needs John's spoken go naming the run, and that has not been given.** Everything it asks for is staged and costed: `docs/successor-rented-slice-staging-2026-09-21.md`, with the plan the staging script writes in `out/rented-slice-plan.txt`. One slice is estimated at about **$0.75 to $1.00** with a hard cap of **$2.00** (staging note), inside the **$3** the proposal budgets for this item. Section 10 |

*The eleventh row was added after the fact, and the reason is worth stating so
nobody reads it as a gap that was nearly missed. The proposal grew item R-11
four seconds after this rehearsal's method file was committed, on the branch
this work was not on, so the rehearsal was planned against a list of ten and
this table was first written with ten rows. The rehearsal staged and costed
exactly what the eleventh item asks for anyway, without having seen it. Nothing
was missed but the numbering — and a table that claims to cover every item has
to cover every item, because the protocol makes a pre-stated quantity with no
rehearsal line against it a fatal finding on its own.*

---

## 3. The finding that matters most: the nomination step is underspecified

> **Added 2026-09-23 by a later session — the label has since been ruled, and
> this section is otherwise untouched.** John has ruled that the straight-line
> read is fitted against **which marker word is the model's own**, the third of
> the three readings below and the only one that returns this arm's known
> 0.0000. He first chose the marker's rank — the reading this section annotates
> as the programme's own convention — was shown the measured degrees in the
> second table below, and changed his answer. The ruling is
> `docs/rulings/2026-09-23-nomination-label.md`; authorship is mixed, the
> session put the options and the measurement and he chose. **Item 4 of this
> section is not answered by that ruling and stays open**: the winning reading
> still varies across the nine arm-and-seed pairs, so fixing the label does not
> make the procedure one instrument. Nothing below is rewritten — this is a
> dated record of what was measured on 2026-09-21, and it stands as written,
> including where it calls the label an open question.

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

| reading of the label | how well it fits, seeds 0 / 1 / 2 | ownership-only transplant, best over every site set and rank cap, seeds 0 / 1 / 2 |
|---|---|---|
| the agent's slot | 0.256 / 0.256 / 0.256 (chance is 0.25) | **0.0117 / 0.0000 / 0.0000** |
| the marker's rank — *the programme's own convention* | 0.706 / 0.694 / 0.700 | **0.0050 / 0.0183 / 0.0117** |
| which marker word | 1.000 / 1.000 / 1.000 | **1.0000 / 1.0000 / 1.0000**, at rank 8 and above |

Every cell above is read out of `out/nominate.json`. An earlier draft of this
table printed the two failing rows as a flat **0.0000**; neither is 0.0000 on
every seed, and the marker-rank row is not 0.0000 on any seed. The correction
does not move the finding — 0.005 to 0.018 is far below the 0.2500 a solver
that cannot tell whose value it needs reaches by luck, so "no causal effect" is
still the fair plain reading — but a cell in this table has to carry what was
measured, and these two did not.

**What the measure itself would print, which is the sentence this turns on.**
The table above reports the transplant accuracies and leaves the arithmetic to
the reader. Doing the arithmetic means putting each label's best configuration
through `measure.py`, at the rehearsal's own working floor of 0.30, with the
whole-state accuracy and the no-transplant rate the record gives for this arm
(1.0000 and 0.0000 on all three seeds, so both candidate forms of the reading
agree exactly):

| seed | reading of the label | whole-state | ownership-only | the degree the measure prints |
|---|---|---|---|---|
| 0 | the agent's slot | 1.0000 | 0.0117 | **0.9883** |
| 0 | the marker's rank | 1.0000 | 0.0050 | **0.9950** |
| 0 | which marker word | 1.0000 | 1.0000 | 0.0000 |
| 1 | the agent's slot | 1.0000 | 0.0000 | **1.0000** |
| 1 | the marker's rank | 1.0000 | 0.0183 | **0.9817** |
| 1 | which marker word | 1.0000 | 1.0000 | 0.0000 |
| 2 | the agent's slot | 1.0000 | 0.0000 | **1.0000** |
| 2 | the marker's rank | 1.0000 | 0.0117 | **0.9883** |
| 2 | which marker word | 1.0000 | 1.0000 | 0.0000 |

**Under the two failing readings of one unwritten word, the instrument reports
a degree of 0.982 to 1.000 for an arm whose degree is 0.0000 by construction.**
That is a wrong answer of the largest size the scale allows, on the one arm
where the right answer is known in advance. It is not a near miss and it is not
a matter of precision: the instrument would put the separable arm at the
entangled end of its own scale and give no sign that anything had gone wrong.

Four things follow, and all four belong in the registration text.

1. **The registration must say what the label is.** Under two of the three
   readings the measure would have reported the separable arm — the arm whose
   degree is zero by construction — as maximally entangled. That is a wrong
   answer of the largest possible size, produced by a sentence nobody thought
   was ambiguous.
2. **The programme's existing convention is one of the two that fail.** The
   marker-rank label fits at 0.706, 0.694 and 0.700 across the three seeds,
   well above chance, and its best transplant reaches 0.0050, 0.0183 and
   0.0117 — no useful causal effect at all. This is the programme's own lesson
   arriving in a new shape: a representation a straight-line read recovers
   beautifully can do nothing when you intervene on it. The proposal already
   says to nominate by causal effect rather than by fit, and this rehearsal is
   the first thing in the programme to show what that rule buys.
3. **The rank cap is not free either.** With the right label, at the site set
   the nomination picks on all three seeds (the first layer, at the position
   where the action is taken), the ownership-only transplant on the separable
   arm averages **0.153 at rank 1, 0.355 at rank 2, 0.832 at rank 4 and 1.000
   at rank 8**. Per seed, from `out/nominate.json`: 0.1517 / 0.1417 / 0.1667 at
   rank 1, 0.3350 / 0.3950 / 0.3350 at rank 2, 0.7783 / 0.8467 / 0.8717 at rank
   4, and exactly 1.0000 on every seed at rank 8. A cap below the
   dimensionality of the encoding cannot carry the answer however well the
   subspace is chosen, so a rank cap chosen for parsimony would have produced a
   partial reading and been indistinguishable from partial entanglement.
   *(An earlier draft of this paragraph gave the curve as 0.170, 0.365 and
   0.805. Those three figures are in no committed output file, and no arm,
   label, site set or way of averaging reproduces them: across the nine search
   grids of 810 rows each, the closest rank curve of any arm, label and site set
   misses them by 0.055 in total. They are
   withdrawn, and the measured curve above replaces them.)*
4. **Even repaired, the procedure is not one instrument.** The label that wins
   is not the same label twice running. Across the nine arm-and-seed pairs the
   winning reading is which-marker-word seven times, the marker's rank once
   (the entangled arm at seed 2) and the agent's slot once (the free arm at
   seed 0). The margins in those two cases are tiny: on the entangled arm at
   seed 2 the three labels reach 0.0683, 0.0650 and 0.0633, and on the free arm
   at seed 0 they reach 0.0700, 0.0683 and 0.0667 — so no reading reported
   anywhere in this file moves. But an instrument that silently picks one of three
   meanings per run is three instruments, and which one it is depends on the
   data it is pointed at. That is a second reason, independent of the first,
   why the registration has to fix the label rather than leave the search to
   choose it.

---

## 4. The reading, on fresh episodes

> **Added 2026-09-23 by a later session — what may be quoted from this table
> has since been ruled, and this section is otherwise untouched.** Re-running
> the whole rehearsal from the committed code, from clean, on 2026-09-22
> reproduced the separable arm's rows exactly and reproduced **none** of the
> entangled or free arm's figures: those two arms' readings moved by up to
> 0.0506 and 0.0440. John has ruled that from those two arms the registration
> may quote **a range and a direction only** — about 0.83 to 0.89, at the
> entangled end, one seed of three clearing the learn-both bar — and **no
> decimal as a property of the code**, so no "degree d" sentence for them. The
> ruling is `docs/rulings/2026-09-23-range-and-direction-only.md`; authorship is
> mixed — the session put the question and three options, he chose one. It
> settles nothing else: neither form of the reading's arithmetic is adopted, and
> the uncertainty method, the seed count and the separation bar in section 11 all
> stay open — with the seed-count row now known to rest on a spread that does not
> measure this variation at all. Nothing below is rewritten; this is a dated
> record of what was measured on 2026-09-21 and it stands as written.

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
donor's, the same thing happens on most arms but not on all of them. Counted
out of `out/denominator_attenuated.json`, arm by arm and seed by seed, with the
span each form covers across the four attenuations:

| arm and seed | the reading as registered | the floor-corrected reading | which is flatter |
|---|---|---|---|
| entangled, seed 0 | 0.0405 | 0.0221 | floor-corrected |
| entangled, seed 1 | 0.3424 | 0.0164 | floor-corrected |
| entangled, seed 2 | 0.0087 | 0.0023 | floor-corrected |
| free, seed 0 | 0.3291 | 0.0085 | floor-corrected |
| free, seed 1 | 0.0680 | 0.0710 | **the registered one** |
| free, seed 2 | 0.5169 | 0.0732 | floor-corrected |
| separable, seed 0 | 0.0067 | 0.0067 | dead heat |
| separable, seed 1 | 0.0631 | 0.0631 | dead heat |
| separable, seed 2 | 0.0066 | 0.0066 | dead heat |

**Five of the nine, not six.** Three are dead heats, and they are dead heats
for a reason worth stating rather than glossing: on the separable arm the
no-transplant rate is exactly zero, so the two forms are the same arithmetic on
that arm and cannot disagree. The biggest gaps are the free arm at seed 2,
where the registered reading spans **0.5169** across the attenuation while the
floor-corrected one spans 0.0732, and the entangled arm at seed 1, where the
registered reading spans 0.3424 against 0.0164.

**And this check fails its own pre-stated cell on one arm and seed, which was
not reported.** The method addendum's cell for it is written per arm, and its
fail line is exactly "the registered form is the flatter one"
(`docs/successor-measure-rehearsal-method-addendum-denominator-2026-09-21.md`,
check D-2). On the free arm at seed 1 the registered form is the flatter one,
0.0680 against 0.0710. **That is a fail, and it is recorded here as a fail.**
The gap is small and the overall picture is unchanged — five arms and seeds
favour the correction, three cannot distinguish the two forms, and the two
largest gaps in the table are both enormous and both in the correction's favour
— but a pre-stated line that fires has to be reported when it fires, and an
earlier draft of this file reported no fail anywhere for this check.

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

The proposal's "near one in eight" is wrong on every arm, and is wrong in the
direction that matters: it **passes for a model at chance and fails for a model
that works**. As registered it would call a working instrument broken. The
review's formula is far better — but **not, as an earlier draft of this file
said, right to within a few thousandths everywhere.** The misses, out of
`out/denominator_floor.json`: the separable arm's three seeds are exact at
0.0000; the entangled arm's three are out by 0.0002, 0.0042 and 0.0033; the
free arm's are out by 0.0024, **0.0084** at seed 1 and **0.0175** at seed 2.
So seven of the nine are within about four thousandths or better and two are
not, and the worst miss — 0.0762 measured against 0.0587 predicted — is nearly
two hundredths, which is about **a third of the value being predicted**. The
finding stands and the formula is the right one to register in place of "near
one in eight"; the claim about how closely it predicts does not, and a rule
registered against it needs room for a miss of that size.

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

===== END OF RECORD 16, part 2 =====

