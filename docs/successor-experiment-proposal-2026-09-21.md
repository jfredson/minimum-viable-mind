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
proposal … a go to draft, not a registration". Item 4 of the same ruling sets a
spend cap of $130; section 12 below reports that the roadmap's own items do not
fit inside it and proposes a number, which is what the standing rule ruled the
same day requires.*

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
   week 43.** One arm F run at the registered size launches first, about $12.
   Its learn-both result is read before the remaining eight launch. If it fails
   the gate, the one permitted re-run happens; if that fails too, the outcome is
   R3 and the remaining eight never launch. On the honest prior in section 3
   this is the most likely course, and it saves about $96 of the $108 wave.
   Cost: about a day of schedule, which week 43 has. Judgment call; decision 11.
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
  one permitted re-run fails it too. Outcome R3. About $32 spent.
- **S5.** Cumulative actual spend reaches the cap John rules. Work stops
  regardless of state; what is unrun is reported as unrun.
- **S6.** Either kill date passes (registration by 2026-10-18, runs launched by
  2026-11-01). Outcome R4, named in `STATUS.md` as a schedule failure.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.

---

## 12. Spend: the real arithmetic, the shortfall, and the number proposed

### 12.1 The cap in force does not fit its own contents

Section 6 of the December-result roadmap sets the successor cap at **$130**,
"covering rehearsal (up to $10), development runs (up to $10), nine registered
30M runs (about $110) and one re-run (about $12) with the balance as the
anomaly margin."

Those four items sum to **$142**. There is no balance. The plan is **$12 over
its own cap before any billing anomaly**, and the anomaly margin the sentence
promises does not exist. This is reported here rather than absorbed, under the
standing rule John made on 2026-09-20 in the same ruling that set the cap: when
the right next step costs more than the cap in force, the recommendation says
so and proposes the increase with the number; a cap is a gate for his ruling,
never a reason to route around a step, shrink it silently, or call it
impossible.

### 12.2 The itemised estimate

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| Rehearsal, week 40 | Tiny models, three architectures, transplanting code, the ten rehearsal items, throughput | Roadmap section 6; local where the Mac allows | $10 |
| Development runs, week 42 | Three arms, one seed each, at the 10-million size: pipeline, self-tests, throughput | The earlier 10-million run measured $1.94 for 2.86 machine-hours; three at about $2, plus margin | $10 |
| Nine registered runs at the registered size | Three arms × three seeds | The last measured pair of registered-size runs cost $20.08 for 20.28 machine-hours at $0.99/hr, so $10.04 each; the ledger's planning figure of $12 is carried instead, to cover arms T and C being slower per step | $108 |
| One permitted re-run | An arm that fails the learn-both gate gets one more try | One run at the planning figure | $12 |
| Transplanting and measurement on fresh episodes | The measurement itself, all arms, all controls | Planned local at $0, as every probe and lesion pass in this programme has run; carried as a contingency for one rented machine if the rehearsal's measured local runtime is too long | $12 |
| Billing-anomaly and idle-billing margin | The unexplained 3.5× billing row of 2026-08-08, waived and never explained, would turn one $10 run into about $35; idle billing has cost $10.30 across four occurrences | One anomalous run (+$23) | $23 |
| **Total** | | | **$175** |

**What the roadmap's list leaves out, and this one adds.** The roadmap has no
line for the measurement itself. Transplanting is new code run on nine
checkpoints with seven controls on fresh episodes, and while the programme's
probe work has always run locally at no cost, a nine-checkpoint transplanting
sweep is larger than anything it has run locally before. Carrying $12 against
it is honest; carrying nothing was not.

### 12.3 What $175 means against the programme ceiling

The programme envelope is $400, of which $215.70 is spent, leaving **$184.30**.
The closed Amendment A3 had its own $100 stop with about $55.70 unspent; that
remainder is already inside the $215.70 figure and must not be counted twice.

Everything else on the roadmap between now and the hibernation condition of
2027-01-04 is deferred and costs nothing: the seventy-hour marker-word read,
the blind-arm re-run, transplanting on the closed design's checkpoints, option
D, the frontier pilot, Stage 3 and the construction project. **So the successor
is the only remaining planned spend under the existing ceiling**, and a $175
cap fits inside it with $9.30 to spare. No raise of the $400 ceiling is
requested.

### 12.4 The recommendation, and the two alternatives named

**Proposed: raise the successor cap from $130 to $175**, itemised as above,
inside the unchanged $400 programme ceiling.

Two alternatives, so John rules on a choice rather than on a single number:

- **Hold $130.** The only plan that fits is two arms at three seeds — six
  registered runs at $72, plus $10, $10, $12 and $12, leaving a $14 margin,
  total $130. That is the two-arm fallback adopted **for budget reasons rather
  than because the rehearsal found arm C unbuildable**, and it is a different
  decision from the one John pre-approved. It buys the weaker design described
  in section 5.2 and should be recorded as such if chosen.
- **$211, at four seeds per arm.** If the rehearsal's paired-uncertainty method
  needs a fourth seed, twelve registered runs cost $144 and the total becomes
  $211, which exceeds the $184.30 remaining and would need a ruling on the
  $400 ceiling itself. Nothing suggests four seeds yet; the number is given now
  so that the possibility is not a surprise in week 41.

**What is not proposed:** shrinking the design quietly to fit $130, dropping the
anomaly margin, or leaving the measurement line at zero. Each would fit the
number and misreport the plan.

### 12.5 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used: this design
completes under $175 with three seeds on every arm carried. If measured spend
approaches $175 with runs missing, **the report is the shortfall, never a
second raise.**

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
makes that outcome cost about $32.

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
money, in one direction only.

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
   **Alternative:** adopt the roadmap's anomaly fallback from the start (two
   seeds on the constructed arms, three on the free arm), which saves $24 and
   weakens the two arms that are supposed to be the ground truth.

7. **Raise the successor cap from $130 to $175**, itemised in section 12,
   inside the unchanged $400 ceiling, which leaves $9.30. *Confidence: high
   that $130 cannot hold the roadmap's own contents; moderate on $175 as the
   right number.* **Alternatives:** hold $130 and take the two-arm design for
   budget reasons (section 12.4), or rule that the four-seed case at $211 comes
   back as a ceiling question if the rehearsal asks for it.

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
    learn-both result read, then the remaining eight. *Confidence: high.
    Judgment call.* **Alternative:** the roadmap's simultaneous launch of all
    nine, which is about a day faster and risks $96 on the most likely outcome
    in section 3.

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
- The spend record every number in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`.
