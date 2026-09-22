# Successor experiment, proposal version 1: reading how much of the act is organised around who is acting

*Drafted 2026-09-21 (Pacific) in a Claude Code session, in its own worktree.
**Status: PROPOSAL, version 1. Nothing here is registered and nothing here
binds.** It goes to Gate C of `docs/outside-review-protocol.md` (a review
attached to a proposal before John rules on it), then, after his rulings and a
rehearsal, to Gate A (the registration review, both tiers) as registration
text. No money is spent and no machine is rented by this document.*

*What authorises the draft: John's ruling of 2026-09-20 on the December-result
roadmap (`docs/rulings/2026-09-20-december-result-roadmap.md`), item 5 — the
result definition in section 2 of `docs/december-result-roadmap-2026-09-20.md`
and the three-arm design in its section 3 are "the basis of the successor
proposal … a go to draft, not a registration". Item 4 of the same ruling set a
spend cap of $130.*

***Revised 2026-09-21, after John ruled on spending.** Two things overtook
version 1 of this document on the day it was drafted: the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) was corrected
to a running total of about $225.70 of $400, and John ruled that the money is
authorised in two releases rather than as one flat cap, with the second release
asked for only after the week-40 rehearsal has measured throughput. **Section 12
is rewritten to that ruling and to the corrected arithmetic; sections 11, 13, 15
and 16 carry the consequences. Nothing about the science is changed.** Version
1's claim that a $175 cap fitted the envelope "with $9.30 to spare" was wrong by
the sign of its own margin and is corrected in section 12.1 rather than
silently removed.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30): the plain word before the term of art, and no bare
identifier anywhere.*

---

## 0. The whole thing in six sentences

The project's open question is now one of degree: a small transformer that has
learned a causally load-bearing answer to "which agent am I" counts as a centre
at the bottom of the gradient, and what would separate it from a centre in the
fuller sense is how much of its act is organised around that answer. Nobody has
a measure of that. So the successor experiment builds two systems whose degree
is fixed by how they are built — one where "which agent am I" sits in a slot
that can be swapped on its own, one where it is stirred into everything — and
one ordinary freely trained system, and asks whether a candidate measure can
tell the first two apart. The measure is: transplant the part of the internal
state that says who is acting from one run into a matched run and see whether
the action follows the transplanted identity; compare that with transplanting
the whole internal state at the same places; the gap between the two, as a
share of the whole-state result, is the reading. If the measure separates the
two built systems, the freely trained system gets a reading and the project's
current sentence "degree unmeasured" is replaced by a number. If it does not
separate them, that is a result too, and the measure is not used.

---

## 1. Words used here, once

- **The programme.** Minimum Viable Mind, this repository. **MVM-0a** is its
  small-transformer build, registered 2026-08-07, whose Amendment A3 closed on
  2026-09-20 with the registered word *not testable*.
- **Ownership.** Which of the several agents in a synthetic dialogue the model
  itself is. Nothing psychological is meant by the word; it names a fact about
  the episode that the model has to get right.
- **The acting channel.** The wire through which the model is told, at the
  moment it acts, that this turn is its own — a copy of its own previous state
  injected at its own turns. Registered as Amendment A1 on 2026-08-09. It is
  the only honest source of ownership in this design, because in a dialogue
  where the turns are interchangeable, nothing in the text itself can carry it
  (the red-team finding that made this necessary is ledger item RT-17).
- **A pointer to who I am.** A stored answer to "which of the agents am I" that
  later computation looks up. Plain synonym used throughout: *the ownership
  answer*.
- **The running state.** The vector a transformer carries forward from layer to
  layer at each token position, which everything downstream reads and writes.
  The technical name is the residual stream; it is used once more, in section
  6, and not again.
- **Transplanting (patching).** Taking the running state, or a part of it, out
  of one forward pass and putting it into another at the same place, then
  reading what the second pass does. The programme has never run this; the code
  does not exist (ruled 2026-09-20; it is built once, for this experiment).
- **A fitted straight-line read (a linear probe).** A classifier fitted to the
  running state to predict a label, used here only to propose candidate places
  to transplant, never to conclude anything on its own. The programme's
  existing machinery for this is
  `experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-method.md`,
  the method file for the eleven-position fitted read.
- **Arms.** The three trained systems being compared: the one built to keep the
  ownership answer separable (arm T, for tracker), the one built to entangle it
  (arm C, for the fuller centre end of the axis), and the ordinary freely
  trained one (arm F, for free).
- **The four registered outcomes, R1 to R4.** Set by section 2 of the
  December-result roadmap and reproduced in section 3 below.
- **Gates A, B and C.** The three review points of
  `docs/outside-review-protocol.md`: registration, interpretation, and
  proposals that ask John for a ruling. This document is Gate C material.
- **Ledger items, written RT-nn.** Numbered red-team findings in
  `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`. Each one
  cited below carries a phrase saying what it found.

---

## 2. The question, and what this experiment is for

The question, from section 1 of the December-result roadmap, unchanged:

> Can a measure of how far an act can be pulled apart, validated on systems
> whose degree is known by how they were built, read the degree of a freely
> trained 30-million-parameter transformer that acquired a load-bearing
> ownership answer under task pressure? If so, what does it read?

Two things the question is not. It is not "is anyone home"; the founding wager
carries that step and no experiment here settles it. And it is not "tracker or
centre" as two kinds of thing; that was ruled one axis of degree on 2026-09-20
(`docs/rulings/2026-09-20-center-as-degree.md`).

What this experiment is for, stated so it can lose: **to deliver a measure, not
a verdict.** That is Stage 2 of `ROADMAP.md`, whose win condition is written in
the roadmap's own words as "deliver the metric, not a verdict", validated on
contrast cases where the answer is known by construction, with a loss condition
for "the metric cannot distinguish the known cases". This proposal supplies the
contrast cases and writes that loss condition down as outcome R2.

The design is the one the outside reviewer named as the single experiment most
likely to change his view of the programme — the matched-role swap experiment
in section 5 of `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`
— extended from two arms to three so the measure has a known case at both ends
of the axis rather than one.

---

## 3. What counts as a result

Reproduced from section 2 of the December-result roadmap, which John accepted
as the basis of this proposal. The registered wording is the wording in the
middle column; nothing in this document may report an outcome in other words.

| Outcome | Registered term | What it means | Satisfactory |
|---|---|---|---|
| **R1** | **metric validated, degree read** | The measure separates arms T and C at the pre-stated bar, and arm F gets a reading with paired uncertainty across seeds. The closure sentence "degree unmeasured" is replaced by a number. | Yes |
| **R2** | **metric does not separate** | Every arm carried passes the learn-both gate, but the measure cannot tell T and C apart at the bar. The measure is not used on arm F; the result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | One or more arms fail the learn-both gate after the one permitted re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. | Yes, if the gate was reached |
| **R4** | (none) | Registration not committed by 2026-10-18, or runs not launched by 2026-11-01. The programme hibernates with a design and a rehearsal only. | No. Recorded as a schedule failure, not a scientific one |

**The honest prior, stated before the work rather than after it.** On the
existing record the most likely outcome is **R3**, and the most likely reason
is the named-other half of the task. Three seeds of the closed Amendment A3
design failed to learn a named-other query battery, landing at 0.2877, 0.3057
and 0.3195 against 0.3227 for a solver that cannot read the name the question
supplies; a fourth run with the battery's own loss term, four times the
per-row weight and two thirds of the query gradient, reached 0.3125 and changed
nothing (`control-learnability-pilot-findings.md`, the pilot findings file;
ledger items RT-52 to RT-69). This experiment moves the named-other condition
from a query at the end of the episode to an action at the model's own turn,
which is precisely the repair the outside reviewer proposed and the internal
requirements document ranked first. It may still not be learnable at this
size. Section 11 places a stop before the expensive wave so that an R3 costs
about $32 rather than about $140.

---

## 4. The task: matched-role revisions

### 4.1 What the model does

The grammar extends the registered Amendment A3 grammar (`curriculum_a3.py`,
the episode generator committed 2026-09-15), which already has the pieces:
four agents, a closed vocabulary, ten turns, eight value slots, every revised
item assigned by all four agents before anyone revises it, and a revision rule
that is a deterministic function of the reviser's own earlier value (the
successor of that value, counted round the eight slots).

The change is that the model now acts in **two matched roles at the same kind
of position**:

- **Own-directed revision.** The model's turn arrives; the correct output is
  the successor of **the model's own** earlier value on that item.
- **Named-other-directed revision.** The model's turn arrives carrying a name
  token; the correct output is the successor of **the named agent's** earlier
  value on the same item.

Both are actions on the model's own turn, supervised the same way, scored the
same way. This is the whole point of the redesign: in the closed Amendment A3
design the ownership condition was an action and its comparison condition was a
question asked at the end, so the two were never at the same kind of position,
which is the defect the outside review called out and the internal requirements
document had already ranked first for repair.

### 4.2 What "matched difficulty" means, concretely

Four things are matched, by construction in the generator and checked at the
rehearsal:

1. **Candidate count.** In both conditions the item has been assigned by all
   four agents, so four earlier values are in the context. A solver that cannot
   tell which agent the answer belongs to can do no better than one in four.
   Random guessing over the eight slots is one in eight. Both numbers are the
   same in both conditions.
2. **Distance.** The number of turns between the source assignment and the
   action, and the number of intervening turns by other agents, are drawn from
   the same distribution in both conditions.
3. **Supervision.** Equal numbers of supervised action positions of each kind
   per episode, equal loss weight per position, one scored token per position.
4. **Transformation.** The same successor rule in both conditions, so nothing
   about the arithmetic differs.

**The asymmetry that cannot be matched, stated rather than hidden.** In the
named-other condition the identity of the source agent is a token in the input;
in the own-directed condition it is not, and cannot be, because a dialogue with
interchangeable turns carries no honest ownership signal in its text (ledger
item RT-17, the finding that any learnable ownership cue in the tokens is a
fingerprint). So one condition reads its answer's owner and the other has to
have carried it. That asymmetry *is* the experiment; removing it would mean
putting the model's own name in the text, which would reintroduce the very
leak the acting channel was built to avoid. It is recorded here, will be
recorded in the registration text, and bounds what a difference between the two
conditions may be read as. Decision 9 in section 15 puts it to John.

### 4.3 Carried-forward rules that apply to the new generator

- **The even-split rule.** Any batch fraction that splits rows by condition must
  give an even number of rows, or the split cuts the generator's matched content
  pairs. Measured and recorded 2026-09-20 as ledger item RT-58 (the batch-split
  bias check). It applies here because the new grammar has two supervised
  conditions and therefore a split.
- **The one-scored-token self-test.** The check that exactly one token per
  supervised position is scored, and that the check survives the shift the loss
  function applies — ledger item RT-59, which turned out to need more than the
  one line it was first written as. It runs on every generator build.
- **The cue-detector gates.** Gates (i) and (ii) of the registered design (no
  surface cue in the curriculum text or the input tensors predicts which turns
  are the model's own) run unchanged on the new grammar. Gate (iii), the
  likelihood attack, runs in its act-withheld form as re-specified in Amendment
  A3 §3.4, because the policy at a revision position is perspectival and
  scoring another agent's turn under it with the acting channel present would
  read the model's ownership knowledge as a leak.

---

## 5. The three arms

All three train on the same grammar, at the same size (39.2 million actual
parameters, the registered 30M configuration), on the same token budget, with
the same launcher, watchdog and network volume. What differs is the
architecture, and only in the way the ownership answer is allowed to exist.

### 5.1 Arm T — the ownership answer kept separable, by construction

The registered trunk plus two additions:

- **An explicit table** of assignments: for each agent and each item, the value
  that agent most recently assigned. It is written at assignment turns and read
  at action positions.
- **A separate slot holding the ownership answer**, a single vector position
  that carries "which agent am I" and nothing else, produced from the acting
  channel and read by the action head as the row selector into the table.

The action is computed as: read the ownership slot, read the table row it
selects for the current item, apply the successor rule. The factoring into
(table, ownership answer, lookup) is the architecture, not something the
network may or may not discover, and the ownership slot is a single place that
can be transplanted on its own. **Its degree is zero by construction**, and
that is the point of the arm.

Judgment call (decision 2): the ownership path is architecturally forced, not
merely encouraged by a penalty term. The forced version is what makes the
degree known; a soft version would be more comparable with arm F but would
forfeit the one thing the arm exists to supply.

### 5.2 Arm C — the ownership answer entangled, by construction

The registered trunk with the ownership signal mixed into the content
representation at every layer, and no slot of its own anywhere:

- The acting channel produces, per layer, a scale-and-shift applied to the
  whole running state of that block, so the ownership signal multiplies content
  rather than sitting beside it.
- The item and value representations are combined with the ownership signal
  multiplicatively at the point of binding, so that "which item, whose value"
  is one quantity rather than two.
- No dedicated ownership position exists and no part of the architecture reads
  ownership alone.

The prediction, if the construction works: transplanting any single nominated
part of the state fails to reproduce the counterfactual action, while
transplanting the whole state at the same places succeeds. **Its reading should
be high.**

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the week-40 rehearsal showing that its
degree is genuinely known by construction rather than merely intended, and that
the two-arm fallback is accepted in advance. This proposal keeps that exactly
as ruled, and adds what the rehearsal has to show (rehearsal items R-3 and R-6
in section 10).

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable — but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. The registration text, if
the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker.

### 5.3 Arm F — the freely trained system

The registered register-less configuration with the acting channel present —
the same architecture as the closed Amendment A3 runs — trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate and the ownership-lesion check in section 8.

### 5.4 Seeds

Three seeds per arm is the planning number, giving nine registered runs. **The
seed count is not fixed by this document**: it follows from the
paired-uncertainty method, which the rehearsal chooses (section 9). If the
rehearsal's method needs more than three, that comes back to John as a fresh
number before the registration commits, with what it costs (section 12 gives
the arithmetic at four seeds).

---

## 6. The measure

### 6.1 The pairing

Episodes are generated in matched pairs that share a content seed and rotate
which agent the model is — machinery the registered generator already has. In
a pair, the **recipient** episode is the one the model runs; the **donor**
episode is its twin in which the model is a different agent. Because all four
agents assigned the item, **the value the donor's identity dictates is already
present in the recipient's own context.** So a successful transplant does not
import an answer from outside; it changes which of four in-context values gets
selected. This is the construction that lets the experiment tell apart
"the transplant moved who is acting" from "the transplant carried the answer
with it", which is the confusion the outside review warned about.

### 6.2 The two transplants

A **site set** is fixed before anything is read: a list of token positions and
a list of layers. At those sites:

- **Whole-state transplant.** Replace the entire running-state vector at each
  site with the donor's.
- **Ownership-only transplant.** At the same sites, replace only the part of
  that vector lying in the nominated ownership subspace, leaving the rest of
  the vector as the recipient had it.

The second is a restriction of the first to a subspace, not a smaller or
different intervention. That is deliberate: it means the measure reads *how
much of the identity-driven difference at these places lives outside the
nominated subspace*, and not *how many places you had to touch*. A reviewer's
first objection to a measure of this shape is that the whole-state transplant
trivially wins because it moves more; defining the two as subspace and
superspace at identical sites is the answer to that objection, and the
rehearsal's null-transplant test (rehearsal item R-8) checks it.

### 6.3 The number

For each arm, on fresh episodes:

- `accuracy_whole` — the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only` — the same share under the ownership-only
  transplant.
- `accuracy_untouched` — the same share with no transplant at all, reported as
  a floor. It should be near the one-in-eight guessing rate; if it is not, the
  pairing is broken and nothing is read.

**The reading is** `degree = (accuracy_whole − accuracy_ownership_only) /
accuracy_whole`.

Zero means fully separable: transplanting the ownership answer alone does
everything transplanting the whole state does. The number rises toward one as
the act resists being pulled apart. The raw difference,
`accuracy_whole − accuracy_ownership_only`, is reported alongside with its
paired uncertainty across seeds, always, and never replaced by the ratio.

### 6.4 When the measure returns nothing

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unsatisfiable
denominator). This measure has a denominator, so it gets an explicit invalid
rule, written before it runs:

- If `accuracy_whole` is below a floor set by the rehearsal, the measure
  returns **INVALID** for that arm and no degree is reported. The reason is
  recorded: the whole-state transplant did not reproduce the counterfactual at
  these sites, so there is nothing for the ratio to be a share of.
- If `accuracy_ownership_only` exceeds `accuracy_whole`, the reading is
  negative. It is reported as observed and treated as a warning about the
  instrument, not quietly clipped to zero. The rehearsal must show a negative
  value is reachable on a deliberately broken toy case, so that it is a real
  outcome rather than an impossible one.
- If any control in section 7.3 fails, the reading is not made for that arm.

**No normalisation by an ownership-blind ceiling anywhere.** The outside review
said it in one line — report raw accuracy changes with paired uncertainty, do
not normalise the comparison condition by its ownership-blind ceiling — and the
programme has already paid for the lesson once. The only division in this
design is the one above, and it has the floor rule attached.

---

## 7. The measurement procedure

### 7.1 Data split

Three disjoint sets, generated from separate seeds and committed before use:

- **Training episodes** — what the arms are trained on.
- **Development episodes** — the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all.
- **Fresh episodes and confirmation seeds** — evaluated once, after the freeze,
  with marker and content combinations that appear in neither of the other two
  sets.

### 7.2 Choosing the candidate ownership representation

On development episodes only, for each arm, identically:

1. **Candidate sites.** A pre-listed set of token positions (the action
   position, and positions between the source assignment and the action) and
   all layers. The list is written down before it is searched, and the number
   of comparisons it implies is written down with it, so the family correction
   is pre-stated rather than chosen once the results are in.
2. **Candidate directions.** At each site, fit a straight-line read for "which
   agent is acting" and take the leading directions, up to a rank cap the
   rehearsal sets.
3. **Nominate by causal effect, not by how well the read fits.** The nominated
   site set and subspace are the ones with the highest *development-set
   ownership-only transplant accuracy*. This is deliberate and is the main
   lesson of the closed design: a representation that a straight-line read
   recovers beautifully can do nothing when you intervene on it, and the
   programme spent a month on reads that were never allowed to conclude
   anything because the causal half had never been built.
4. **The layer set for the whole-state transplant** is chosen on development
   data by the same rule for every arm: the smallest layer set at which the
   whole-state transplant clears the floor. If no layer set clears it for an
   arm, that arm returns INVALID, and that is recorded rather than repaired.
5. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot is computed and reported separately,
   as a reference for what the measure reads under perfect nomination.
   Judgment call; decision 1.

### 7.3 Controls

Every one of these is run on every arm, and the reading is not made for an arm
whose controls do not hold.

1. **Content transplant.** Transplant the complement of the nominated subspace
   at the same sites. The action should follow content, not identity.
2. **Another agent's representation.** Nominate, by the identical procedure, a
   representation of a named agent who is not acting, and transplant it. The
   own-directed action should not move. This is the matched control that the
   closed design registered as L2(a) and that first ran on 2026-09-21.
3. **Matched random subspace.** A random subspace of the same rank and the same
   norm at the same sites should not produce the donor's action.
4. **A position where the answer is not yet knowable.** Transplanting before
   the identity can be known should do nothing. This control has held on every
   sweep the programme has run and it is cheap; it stays.
5. **Fresh marker and content combinations**, per section 7.1.
6. **Who is acting, versus which value.** The discriminating control. Trials
   are split into pairs whose donor identity dictates *the same* value as the
   recipient's and pairs where it dictates a *different* value. A transplant
   that has moved who is acting changes the action in the second group and not
   the first. A transplant that has smuggled a value across changes the action
   in both. Both cells are pre-stated and both are reported.
7. **Null transplant.** Transplant the recipient's own state into itself.
   Nothing may change. This is the known-answer test for the transplanting code
   and it runs before any result is read.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the site set and the rule that chose it;
- the nominated subspace and its rank, per arm;
- the whole-state layer set, per arm;
- the transplanting operation, as code;
- all seven controls and their pre-stated cells;
- the floor on `accuracy_whole` and the invalid rule;
- the separation bar between R1 and R2;
- the learn-both threshold and the ownership-lesion threshold;
- the paired-uncertainty method and the seed count;
- the predictions: arm T near zero, arm C high, arm F unknown and not predicted.

Nothing on that list may be changed afterwards. If something on it turns out to
be wrong, the registered output is reported as it stands and the correction is
a separate, dated note beside it — the programme's existing practice, and the
process correction the outside review asked for: an immutable registration is
not an immutable scientific conclusion, but the two are kept visibly apart.

---

## 8. The gates every arm passes before it is read

### 8.1 The learn-both gate

No arm is read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, with paired
  uncertainty across seeds. Not combined into one number, not normalised by
  anything.
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and — the addition this proposal makes — the
  **measured** accuracy of an ordinary competing solver built at the rehearsal
  (rehearsal item R-5), so the bar is set against something that was actually
  built rather than against arithmetic. The closed design's comparison battery
  sat on the shoulder of a solver nobody had measured until very late, and that
  is how a null got read as a capability claim for three weeks.
- **The threshold itself is set by the rehearsal** and frozen in the
  registration text. This document does not name it.
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.

### 8.2 The ownership-lesion check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation — the lesion
the existing code already performs. Pre-stated shape:

- own-directed accuracy collapses toward the one-in-four level;
- named-other-directed accuracy holds;
- the ownership-free state and syntax batteries hold.

Thresholds from the rehearsal. **What this check does and does not establish,
in the closed design's own registered words: it removes a sense organ, not a
structure the network built.** It is a precondition for reading arm F — it
shows the ownership answer is load-bearing for the act, which is what makes arm
F worth measuring — and it is not evidence of a centre and is never reported as
such.

Arms T and C do not take this check as a gate: their dependence on ownership is
architectural. Their lesion results are computed and reported as a description
of the constructed systems.

---

## 9. The numbers this document deliberately does not set

Every number below is set by the week-40 rehearsal from measurements, then
written into the registration text and frozen. **Inventing a plausible value
here would be a fatal finding waiting to happen**, and the roadmap says so in
terms: "this document does not invent the numbers; it fixes that they are fixed
before any run."

| Number | What it decides | Set by |
|---|---|---|
| Separation bar between arms T and C | R1 against R2 | Rehearsal item R-10, from the observed toy separation and its spread |
| Learn-both threshold, per condition | R3 | Rehearsal items R-1 and R-5, against the measured competing solver |
| Floor on the whole-state transplant accuracy | whether a reading is valid at all | Rehearsal items R-4 and R-6 |
| Rank cap on the nominated subspace | how much of the state counts as "the ownership answer" | Rehearsal item R-2 |
| Candidate site list and its family correction | how many comparisons the search implies | Rehearsal item R-2 |
| Seed count per arm | the uncertainty on every reading, and the bill | Rehearsal item R-9 |
| Paired-uncertainty method | how across-seed uncertainty is computed and reported | Rehearsal item R-9 |
| Ownership-lesion collapse threshold | whether arm F is read | Rehearsal item R-1 |

---

## 10. The rehearsal, week of 2026-09-28

A complete measurement rehearsal before any Gate A is now protocol: John
adopted it on 2026-09-20 as one of the three amendments to
`docs/outside-review-protocol.md`, from the outside review's ranked process
change 3. This is its first application, and the protocol text edit it depends
on is owed before the successor's Gate A and is the first thing that Gate
checks.

**Scale and cost.** Tiny models, roughly one to three million parameters, short
episodes, small vocabulary, run locally where the Mac's throughput allows and
on the cheapest rented machine where it does not. Budgeted at up to $10.

**Everything below is written down and committed before the rehearsal runs, and
each item is a pass or a fail.**

- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  Both matched conditions reach above the one-in-four level; the four matched
  properties of section 4.2 hold in the generated data (candidate counts,
  distance distributions, supervision counts, transformation). Also fixes the
  learn-both threshold's form and the lesion-collapse threshold.
- **R-2. Arm T is constructible and its ownership slot is transplantable on its
  own.** The blind nomination procedure finds it without being told where it
  is, and the ownership-only transplant reproduces the counterfactual, so the
  measure reads near zero. Fixes the rank cap and the candidate site list.
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction.** The blind nomination procedure, run over the whole frozen
  site set, finds no subspace whose transplant reproduces the counterfactual,
  while the whole-state transplant at the same sites does. **If R-3 fails, the
  two-arm fallback fires**, the registration drops arm C, and it says in its
  own text that the validation now rests on one anchor and is weaker for it.
- **R-4. All four outcomes of the measure are reachable.** A near-zero value
  (arm T), a high value (arm C), a negative value (a deliberately broken case),
  and INVALID (a case where the whole-state transplant is below the floor). A
  measure that cannot return its own failure states is not a measure.
- **R-5. An ordinary competing solver is built and measured.** A solver that
  cannot use ownership, and a solver that uses only the name token, both scored
  on both conditions, so the learn-both threshold is set against measured
  competitors.
- **R-6. The arithmetic is finite.** The floor rule and the invalid rule are
  exercised on cases chosen to break them. No division happens anywhere that
  can return a number when its denominator is near zero.
- **R-7. Throughput is measured, per arm.** Seconds per step and projected
  wall-clock and dollars for each of the three architectures at the registered
  size. The outside reviewer's condition, in his words: the altered grammar
  needs a throughput check before the estimate becomes a budget. Arms T and C
  add computation per layer and will not cost what arm F costs. **The spend
  table in section 12 is superseded by this measurement**, and if it goes up,
  the number goes back to John before the registration commits.
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant changes nothing; a transplant on the arm T toy moves the action to
  the donor's value; the ownership-only transplant is verified to be the
  restriction of the whole-state transplant to a subspace and not a different
  intervention.
- **R-9. The paired-uncertainty method is chosen and demonstrated**, and the
  seed count follows from it rather than from habit.
- **R-10. The separation bar is set** from the observed separation between arms
  T and C at tiny scale and its spread, with the reasoning written out.

**What happens next.** The rehearsal findings are committed as a findings
document; the bars go into registration text version 2; Gate A runs both tiers;
the registration commits by 2026-10-11, or by the kill date of 2026-10-18, or
the roadmap drops to R4 and says so.

---

## 11. Order of work, and where it stops

Binding if registered, in this order:

1. Rehearsal (week 40) → findings → Gate C tier 1 on this proposal's version 2.
2. Registration text version 2 with every frozen number in it → **Gate A, both
   tiers** → registration commit. Target 2026-10-11, **kill date 2026-10-18**.
3. Implementation frozen; unit tests; the even-split rule and the
   one-scored-token self-test run on the built generator (week 42).
4. Development runs at the 10-million size, three arms, one seed each (week
   42). **This is a pipeline and throughput check, not a learnability verdict**
   — the 10-million size failed to learn the earlier design's task, so a null
   here means nothing about the registered size, and the registration says so
   in advance to stop anybody reading it as a result later.
5. **A staggered launch, which is this proposal's addition to the roadmap's
   week 43, and which John adopted on 2026-09-21.** One arm F run at the
   registered size launches first, about $12 (compute ledger, "Phase budget
   guide") — the third and last line of the first release of money in section
   12.3, and the last thing the money authorised so far pays for. Its learn-both
   result is read before the remaining eight launch, and the remaining eight are
   inside the second release, which does not exist until he rules on it. If the
   first run fails the gate, the one permitted re-run happens — about $12 that
   the first release does not cover and that is asked for separately (section
   12.3); if that fails too, the outcome is R3 and the remaining eight never
   launch. On the honest prior in section 3 this is the most likely course, and
   it saves about $96 of the $108 wave. Cost: about a day of schedule, which
   week 43 has. Judgment call; decision 11.
6. Remaining runs launched (week 43). Nomination on development episodes as arm
   F checkpoints arrive.
7. Nomination frozen and committed (week 44). Transplants on fresh episodes,
   all arms. The measure computed on arms T and C: that is the validation
   result.
8. **Gate B** on the validation (week 45). John rules: read arm F, or close on
   R2 or R3.
9. If R1: arm F read on the frozen procedure, confirmation seeds (week 46);
   findings; Gate B; closure text through Gate A (weeks 47 to 49).

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). Nothing trains. About $10 spent.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded.
- **S3.** The rehearsal fails item R-4 or R-6 (the measure cannot return its own
  failure states, or the arithmetic is not finite). The measure is not
  registered. About $10 spent. This is the condition the closed design needed
  and did not have.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the first
  release's $32 (section 12.3) plus about $12 for the re-run, which the first
  release does not cover and which is asked for when the first half of this
  condition fires.
- **S5.** Cumulative actual spend reaches the release John has authorised —
  about $32 for the first release (section 12.3), until and unless he rules on
  the second. Work stops regardless of state; what is unrun is reported as
  unrun, and nothing launches against a release that has not been ruled.
- **S6.** Either kill date passes (registration by 2026-10-18, runs launched by
  2026-11-01). Outcome R4, named in `STATUS.md` as a schedule failure.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**
  — missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over. John's ruling of 2026-09-21; section 12.7.
- **S9.** The first rented machine of any wave bills at an anomalous rate (the
  3.5× row of 2026-08-08, compute ledger). **The wave halts** and it goes to John
  with the billed row beside the estimate. This replaces the roadmap's week-43
  seed fallback, which at the anomalous rate spends more than the programme has
  left; section 12.5.

---

## 12. Spend: the corrected arithmetic, and the two releases of money John ruled

*Wording note. John's ruling of 2026-09-21 authorises the money in two
**tranches**. That is a borrowed finance word, so this document says **first
release** and **second release** and means exactly what the ruling means: an
amount he has approved now, and a larger amount he will be asked for later.*

### 12.1 The number version 1 of this section was built on was wrong

Version 1 of this section said the programme had spent **$215.70** of its $400
and had $184.30 left, and concluded that a flat cap of $175 fitted inside that
with $9.30 to spare. **That conclusion was wrong, and the error is recorded
here rather than quietly repaired.**

The $215.70 came from the spend record in `data/project.toml`. The money's
system of record is not that file but the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`), which calls
itself "the registered budget instrument" in its own first line. That ledger
was corrected on 2026-09-21 to fold in two rows the project file had not caught
up with:

- the control-learnability pilot of 2026-09-19, **about $9.90** (compute
  ledger, the 2026-09-19 row, which records the correction in terms: the row
  "had carried the pre-run figure");
- the checkpoint recovery of 2026-09-20, **$0.067** (compute ledger, the
  2026-09-20 row — measured from the account balance falling from $79.8897 to
  $79.8228, not inferred).

The ledger's last row now reads a programme running total of **about $225.70 of
$400** (compute ledger, the 2026-09-20 row).

So the arithmetic that matters is:

| | |
|---|---|
| Programme envelope (raised from $200 on 2026-08-16) | **$400** — compute ledger, the 2026-08-16 top-up note and the 2026-08-15 row |
| Spent to date | **about $225.70** — compute ledger, the 2026-09-20 row |
| **Headroom** | **$174.30** |

A flat cap of $175 does not fit inside $174.30 with $9.30 to spare. It is
**$0.70 more than every dollar the programme has left**, before a single
billing anomaly. Version 1 had the sign of its own margin inverted, and the
number it reported as spare was the number it was over by.

*(`data/project.toml` still carries the stale $215.70, and section 6 of the
December-result roadmap `docs/december-result-roadmap-2026-09-20.md` repeats it
as "about $184 unspent". A separate session is correcting the project file;
this document does not touch it, the roadmap or any ruling. Where the two
disagree, the ledger governs, and this section is written against the ledger.)*

### 12.2 What John ruled on 2026-09-21

Six rulings, given in session on 2026-09-21 (Pacific) on the strength of the
corrected ledger. **The committed ruling text is owed under `docs/rulings/`; it
is not yet on disk, and this section is written to be superseded by it rather
than to stand in for it.** Decision 7 in section 15 is rewritten to match.

1. **The money is authorised in two releases, not as one flat cap.** The first
   release covers the rehearsal, the development runs and one free-arm run at
   the registered size.
2. **The second release is asked for only after the week-40 rehearsal has
   measured seconds per step for all three arms**, so that the figure rests on
   measurement rather than on a per-step premium carried over from a different
   experiment's full-versus-twin runs.
3. **The staggered launch is adopted** — this proposal's own recommendation in
   section 11, item 5, and decision 11.
4. **"Halt, not trim" replaces the roadmap's week-43 seed fallback** as the
   response to a billing anomaly (section 12.5 below).
5. **The rented account is funded per wave rather than per cap**: topped up to
   that wave's estimate plus $20 and no further (section 12.6).
6. **A check that cannot be run counts as a trip, not a skip** (section 12.7).

**The $400 ceiling is untouched.** The ruling of 2026-08-16 that raised it from
$200 and made it final stands, and nothing in this section asks for a raise.

### 12.3 The first release: about $32, inside the $174.30 headroom

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| Rehearsal, week 40 | Tiny models, three architectures, transplanting code, the ten rehearsal items of section 10, and the throughput measurement the second release depends on | Section 6 of the December-result roadmap budgets it at up to $10; local where the Mac allows | up to **$10** |
| Development runs, week 42 | Three arms, one seed each, at the 10-million size: pipeline, self-tests, throughput | The earlier 10-million run measured $1.94 for 2.86 machine-hours (compute ledger, the 2026-08-07/08 pilot row); three at about $2, plus margin | up to **$10** |
| One free-arm run at the registered size, week 43 | The staggered first run of section 11, item 5, whose learn-both result is read before anything else launches | The last measured pair of registered-size runs cost $20.08 for 20.28 machine-hours at $0.99/hr, so $10.04 each (compute ledger, the 2026-09-17 row); the ledger's own planning figure for a run at this size is $12 (compute ledger, "Phase budget guide", registered training at 30M) | about **$12** |
| **First release, total** | | | **about $32** |

Against the corrected headroom:

| | |
|---|---|
| Headroom (section 12.1) | $174.30 |
| First release | about $32 |
| **Left unauthorised after the first release** | **about $142.30** |

**No change to the $400 envelope is requested, and none is needed.** The first
release is about 18% of what the programme has left and about 8% of the
envelope. It buys the whole of the critical path up to and including the first
registered-size result, which is the point at which the most likely outcome in
section 3 declares itself.

**What the first release deliberately does not cover**, so that nothing is read
into it: the remaining eight registered runs; the one permitted re-run of a run
that fails the learn-both gate; the transplanting and measurement work of
section 12.4; and any margin for the billing anomaly. All four belong to the
second release.

**One gap this creates, flagged rather than absorbed.** Section 11's stop
condition S4 is the staggered first run failing the learn-both gate and its one
permitted re-run failing too. The first release as ruled names **one** run at
the registered size, so the re-run — about $12 on the ledger's planning figure
— has no authorisation inside it. On the honest prior in section 3 this is the
most likely branch of the whole plan, which makes it a poor thing to discover
at the moment it fires. See decision 7 in section 15: the recommendation is
that the re-run is asked for as a small separate release when and if S4's first
half happens; the strongest alternative is that John folds it into the first
release now, making that release about $44 and still leaving about $130.30
unauthorised.

### 12.4 The second release: shaped now, costed after the rehearsal measures it

This is **not a request and not a cap**. It is the itemisation the second
release will be built from, so that John can see now what he will be asked for
later, and so the rehearsal knows which numbers it is being run to settle.

| Item | What it buys | Basis | Provisional amount |
|---|---|---|---|
| The remaining eight registered runs | Three arms × three seeds, less the one free-arm run already in the first release | Eight at the ledger's $12 planning figure (compute ledger, "Phase budget guide") | **$96** |
| One permitted re-run | An arm that fails the learn-both gate gets one more try | One run at the same planning figure | **$12** |
| Transplanting and measurement on fresh episodes | The measurement itself, all arms, all controls | Planned local at $0, as every probe and lesion pass in this programme has run; carried as a contingency for one rented machine if the rehearsal's measured local runtime is too long | **$12** |
| Billing-anomaly and idle-billing margin | The unexplained 3.5× billing row of 2026-08-08, waived and never explained (compute ledger, the 2026-08-07/08 row and the waiver note beneath the table), would turn one $10 run into about $35; idle billing has cost about $10.30 across four occurrences (compute ledger, the 2026-09-17 row and the notes on the pod-side reaper) | One anomalous run (+$23) | **$23** |
| **Provisional total** | | | **$143** |

**What the roadmap's list leaves out, and this one keeps.** Section 6 of the
December-result roadmap has no line for the measurement itself. Transplanting
is new code run on nine checkpoints with seven controls on fresh episodes, and
while the programme's probe work has always run locally at no cost, a
nine-checkpoint transplanting sweep is larger than anything it has run locally
before. Carrying $12 against it is honest; carrying nothing was not. That line
survives this revision unchanged — it is real work, and it is the one item in
this section that no earlier document had costed at all.

**The two releases together come to about $175, which is $0.70 past the
headroom.** $32 plus $143 is $175, against $174.30 left (section 12.1). This is
stated plainly because it is the finding, not a rounding error to absorb: **the
plan as currently itemised does not fit the remaining envelope, by $0.70,
before any anomaly.** It is not a shortfall the first release has to solve —
the first release fits with about $142.30 unspent behind it — but it is the
thing the second release must answer, and it can be answered in exactly three
ways: the rehearsal measures the per-run cost below the planning figure; the
seed count comes down on the rehearsal's own uncertainty method (section 9,
rehearsal item R-9); or John rules on the $400 ceiling itself. **This document
proposes none of the three now**, because choosing between them before the
measurement exists is the error the two-release scheme was ruled to prevent.

**Why the per-run figure is expected to move.** Version 1 carried the ledger's
$12 planning figure instead of the $10.04 measured on 2026-09-17, "to cover
arms T and C being slower per step". That premium is an inference from a
different experiment's full-versus-twin step times, not a measurement of these
three architectures, and it is exactly what John's second ruling refuses to
build a release on. **Rehearsal item R-7 replaces it**: seconds per step and
projected wall-clock and dollars for each of the three architectures at the
registered size, which is also the outside reviewer's condition in his own
words — the altered grammar needs a throughput check before the estimate
becomes a budget. Arms T and C add computation per layer and will not cost what
arm F costs. **The table above is superseded by that measurement**, in either
direction, and the second release is asked for on the measured figure.

### 12.5 Halt, not trim: what happens if the billing anomaly recurs

Section 6 of the December-result roadmap says that if the 3.5× billing anomaly
recurs on the first rented machine, "the seed plan drops as stated in week 43
before the second pod launches" — two seeds on the constructed arms, three on
the free arm. (*Pod* is the rental service's word for one rented machine; it
appears here only inside that quotation.) **John replaced that rule on
2026-09-21 with a halt.**

The reason is arithmetic. Dropping seeds does not address a tripled unit cost;
it addresses the number of units. Seven runs at 3.5× the ledger's $12 planning
figure is $42 each, or $294, and adding the rehearsal ($10), the development
runs ($10) and the measurement line ($12) gives **about $326** — the figure
John's ruling cited as about $328, the same arithmetic to a dollar of rounding.
That is **82% of the entire $400 envelope**, and, more to the point, **$152
more than the $174.30 the programme actually has left** (section 12.1). The
trimmed plan does not fit either. A fallback that still spends more than
everything remaining is not a fallback.

**The rule that replaces it:** the first rented machine billed at an anomalous
rate halts the wave. Nothing else launches; the anomaly goes to John with the
billed row beside the estimate, and he rules on whether anything further runs.
Exposure is bounded at roughly one machine's overrun — about $30 on the 3.5×
row — instead of at a trimmed wave's $326. This is a harder stop than trimming and it is meant
to be: the cheapest moment to find out that a run costs three times its
estimate is after one run.

### 12.6 The account is funded per wave, not per release

The physical backstop is unchanged in kind and tightened in degree. Rule 5 of
the compute ledger already makes the rented account prepaid with automatic
reload **off**, "topped up in increments John chooses, never past the cap's
remainder", so that "the account physically cannot overspend what the ledger
permits".

John's ruling of 2026-09-21 makes the increment the wave's, not the release's:
**the account is topped up to the estimate for the wave about to launch plus
$20, and no further.** The consequence is the point of it — **no anomaly of any
size can cost more than that, because there is nothing else in the account to
spend.** The first release's $32 is an authorisation, not a deposit: the
deposit before the rehearsal is the rehearsal's estimate plus $20, and the
deposit before the staggered run is that run's estimate plus $20.

This is stricter than the practice the ledger records. The wave of 2026-09-17
was funded on a balance of $111.67 against $26 in flight plus $10 (compute
ledger, the 2026-09-17 row) — sufficient under that rule, but with about $75
sitting in the account that an anomaly could have reached.

### 12.7 A check that cannot be run counts as a trip, not a skip

John's sixth ruling of 2026-09-21, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate or a stop condition cannot be evaluated — the
data is missing, the code will not run on the artifact, the measurement was
never taken — **the check counts as failed and its consequence fires.** It is
never recorded as not applicable and stepped over, and it is never deferred
past the launch it was supposed to gate.

Written into section 11 as stop condition S8. The cost of getting this wrong is
already on this programme's record: an unread check is how a null got read as a
capability claim for three weeks (section 8.1).

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used: **the rehearsal
measures a per-run cost at or below the ledger's $12 planning figure, and this
design completes inside the $174.30 the programme has left, with three seeds on
every arm carried.** If measured spend approaches the second release's ruled
figure with runs missing, **the report is the shortfall, never a second raise.**

---

## 13. What this cannot claim, and its weakest points

The Gate C brief asks what a result will be read as claiming beyond what it
measures. Answering it before the reviewer does.

**W1. The two constructed arms differ in more than their degree.** They differ
in architecture, in parameter count within the size band, in how they route
information. Anything that separates them is confounded with degree. What the
arms establish is that the measure moves in the right direction between a
system built to be separable and a system built to be entangled; they do **not**
establish that the measure responds to integration and to nothing else.
Consequently arm F's reading is "where arm F sits between two constructed
anchors on this measure", and never "arm F's integration is *d*". The public
sentence in section 8 of the December-result roadmap already carries this hedge
— "on a metric that separates a tracker built to be separable from a system
built to be entangled" — and the recommendation is that the hedge is not
loosened at any later point. This is the deepest weakness in the design and it
is not removable by anything affordable.

**W2. The reading is relative to the site set.** A different frozen site set
could give a different number. Mitigated by using one pre-stated procedure
applied identically to every arm, and by saying in the registered text that the
reading is the degree *at the sites this procedure nominates*.

**W3. Arm C's degree is an intention until the rehearsal shows otherwise.**
Already conditional by John's ruling. The specific risk is subtler than "it
cannot be built": a network can be built with ownership multiplied into every
layer and still learn to concentrate it in a low-rank direction, in which case
the ownership-only transplant succeeds and arm C's known-high anchor collapses
into a second copy of arm T. Rehearsal item R-3 is the test, and its failure
fires the fallback rather than a repair.

**W4. The whole-state transplant may fail for arm C.** If ownership in arm C is
spread across layers the frozen site set does not cover, the denominator falls
below its floor and arm C returns INVALID — which is honest but leaves the
experiment with no high anchor by another route. Rehearsal items R-3 and R-6
test it; the layer-set rule in section 7.2 is written to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is R3, and R3 is thin.** Three seeds of the
closed design and one reweighted pilot never learned a named-other task. The
repair — same position, same supervision, same transformation — is the right
one and may still not be enough at this size. Section 11's staggered launch
makes that outcome cost about $44 — the first release's $32 plus about $12 for
the one permitted re-run (section 12.3) — instead of the whole wave.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text; decision 9.

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. Mitigated by nominating at positions away
from the acting positions, by requiring the nominated subspace to beat the
other-agent control (which is downstream of the same inputs), and by reporting
the gap between the lesion result and the transplant result honestly.

**W8. Nine runs is a planning number.** The seed count follows from the
rehearsal's uncertainty method (section 9), and the bill follows from the
throughput the rehearsal measures (rehearsal item R-7). Both can move the
money, in one direction only. This is the whole reason the second release of
money is asked for after the rehearsal rather than now (section 12.4): the
number in the table there is the shape of the request, not the request.

---

## 14. What this does not change

- **The $400 programme ceiling.** Unchanged and not proposed for change.
- **The corrigibility commitments** (`spec/corrigibility-commitments.md`,
  version 1.1): John authorises every run and his go is quoted word for word in
  the ledger row; every run is killable; no stakes term; checkpoints are not
  promotable; optimisation against the instruments halts the run. All three
  arms are episodic and floor-only: no state kept across episodes, no
  maintained boundary, no stakes. Nothing here pre-authorises a larger build.
- **The claim rule.** Nothing produced by this experiment is reported as a
  conscious machine, and every positive is bounded at "non-zero on the
  gradient", per the standing limits in `ROADMAP.md`.
- **The closure of Amendment A3.** It closed as *not testable* and this
  experiment does not reopen it. The closed design's checkpoints are not
  transplanted: their grammar has no matched comparison condition and their
  target was never localised.
- **The outside-review protocol's gates and its closure rule.** This document
  passes through them; it does not amend them. The three adopted protocol
  amendments are owed as protocol text before this experiment's Gate A.
- **The dates.** Registration by 2026-10-18, runs launched by 2026-11-01,
  wrap-up starting 2026-12-21, hibernation condition 2027-01-04.

---

## 15. Decisions for John

Each with how confident the recommendation is, whether it is ordinary practice
or a judgment call, and the strongest alternative, so nothing is inherited by
default.

1. **Nomination runs blind on every arm, including arm T.** The measure is
   validated together with the procedure that feeds it, and the reading obtained
   by handing the procedure arm T's true slot is reported separately as a
   reference. *Confidence: high. Judgment call.* **Alternative:** hand the
   procedure arm T's known slot, which tests the arithmetic under perfect
   nomination and is a weaker and more flattering test, since in the field
   nobody is handed the true site.

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Confidence: high. Judgment call.* **Alternative:** a soft table-and-pointer
   with a penalty term, which is more comparable with arm F but gives up the
   one property the arm exists for — a degree that is known rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Confidence: moderate. Judgment call.* **Alternative:** train arm C with a
   penalty that punishes any linearly transplantable ownership direction. That
   would make its degree known by the training objective — but it trains the
   system against the very instrument that will measure it, which is circular,
   and a high reading would then be a fact about the penalty and not about the
   system. Recommended against for that reason.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Confidence: high. Standard practice for intervention comparisons.*
   **Alternative:** transplant the whole forward state at every layer as the
   denominator, which always succeeds and turns the measure into a report on
   how the sites were chosen.

5. **The registered reading is the normalised number, with the raw difference
   and its paired uncertainty reported alongside, always, plus an explicit
   floor-and-INVALID rule.** *Confidence: high on reporting both; moderate on
   which is registered as primary. Judgment call.* **Alternative:** register the
   raw difference as primary, which has no denominator and therefore no
   zero-denominator failure mode at all, but is not comparable across arms with
   different overall accuracy — and comparing arms is the whole design.

6. **Three seeds per arm as the planning number**, with the real count set by
   the rehearsal's uncertainty method. *Confidence: moderate. Judgment call.*
   **Alternative:** two seeds on the constructed arms and three on the free arm
   from the start, which saves $24 at the ledger's $12 planning figure and
   weakens the two arms that are supposed to be the ground truth. Note that this
   is now only a design choice about uncertainty, **not** a response to a
   billing anomaly: John's "halt, not trim" ruling of 2026-09-21 retired the
   roadmap's week-43 seed fallback for that purpose, on the arithmetic in
   section 12.5.

7. **The money goes in two releases, and what is asked for now is about $32.**
   Superseding version 1's request for a flat $175 cap, which was arithmetically
   impossible: the programme has $174.30 left, not $184.30 (section 12.1).
   Asked for now: the rehearsal (up to $10), the development runs (up to $10)
   and one free-arm run at the registered size (about $12), against $174.30 of
   headroom, with the $400 ceiling untouched. Asked for later, after rehearsal
   item R-7 measures seconds per step for all three arms: the second release,
   built from the itemisation in section 12.4 and provisionally $143.
   *Confidence: high on the first release's arithmetic, which is measured
   against the ledger throughout; deliberately no confidence offered on $143,
   because the measurement that would justify it has not been taken.*
   **Alternatives:** (a) fold the one permitted re-run into the first release
   now, making it about $44, which removes the gap flagged in section 12.3 at
   the cost of authorising a run before the run it re-tries has failed — this is
   the alternative worth ruling on; (b) rule the whole $175 now as version 1
   proposed, which the corrected headroom cannot hold and which would commit the
   per-run figure to an unmeasured premium; (c) hold the roadmap's $130 and take
   the two-arm design for budget reasons, which buys the weaker design of
   section 5.2 by a budget decision rather than by the rehearsal's finding, and
   should be recorded as such if chosen. **One number John should see before it
   can surprise him:** if the rehearsal's uncertainty method asks for a fourth
   seed, twelve registered runs at the planning figure cost $144 and the whole
   plan reaches about $211, which exceeds the $174.30 remaining and would be a
   question about the $400 ceiling itself. Nothing suggests four seeds yet.

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. The grammar, the
   architectures, the measure and the outcome set are all new, and MVM-0a's
   Amendment A3 is closed. *Confidence: high. Standard practice.*
   **Alternative:** number it as a further amendment, which keeps one budget
   instrument and one ledger but attaches new work to a closed registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Confidence: high. Judgment call.* **Alternative:**
   add a condition in which the model's own name appears as a token, which
   would match the conditions exactly and would put an ownership cue into the
   text, reintroducing the leak the acting channel exists to prevent. Ruled
   against here; John's call.

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Confidence: high. Standard
    practice, and the closed design's own registered wording.* **Alternative:**
    treat the lesion result as part of the finding, which is the over-reading
    the programme has already corrected once.

11. **The registered wave launches staggered**: one arm F run first, its
    learn-both result read, then the remaining eight. **Ruled by John on
    2026-09-21 and adopted**; it is recorded here because the rest of the
    document is built on it and because it is what makes the two releases line
    up with the work. *Confidence: high. Judgment call.* **Alternative:** the
    roadmap's simultaneous launch of all nine, which is about a day faster and
    risks $96 on the most likely outcome in section 3.

12. **This proposal goes to Gate C tier 1 before John rules on the twelve items
    above**, per the protocol. *Confidence: high. Standard practice here.*
    **Alternative:** rule first and review the registration text only, which is
    what the protocol's Gate C exists to prevent.

*Nothing above is registered. The registration commit, if it comes, follows the
rehearsal, the Gate C pass, John's decisions and Gate A, and every run it
affects is launched after it.*

---

## 16. Where the pieces are

- This proposal: `docs/successor-experiment-proposal-2026-09-21.md`.
- The roadmap it implements, approved 2026-09-20:
  `docs/december-result-roadmap-2026-09-20.md`, sections 1, 2, 3 and 6.
- The ruling that authorises and bounds it:
  `docs/rulings/2026-09-20-december-result-roadmap.md`, items 4, 5 and 7, and
  the standing rule on spend.
- The ruling that makes the question one of degree:
  `docs/rulings/2026-09-20-center-as-degree.md`.
- The one-page statement of the measure it specifies:
  `docs/competing-mechanisms-2026-09-20.md`.
- The design it extends: section 5 of
  `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`, the
  matched-role swap experiment.
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate C now and Gate A later.
- The registration idiom it is written in:
  `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` and the
  pre-registration beside it.
- The spend record every number in section 12 is drawn from, and the system of
  record where it disagrees with anything else:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, corrected on
  2026-09-21 to a running total of about $225.70 of $400.
- The spend figure that is stale and is **not** used here: the spend record in
  `data/project.toml` (about $215.70), being corrected in a separate session;
  section 6 of the December-result roadmap repeats the same stale figure.
- **Owed, and not yet on disk:** the committed text of John's spending ruling of
  2026-09-21 (the two releases, "halt, not trim", per-wave funding, and a check
  that cannot be run counting as a trip), which belongs under `docs/rulings/`.
  Section 12 is written from that ruling as given in session and is superseded
  by the committed text when it lands.
