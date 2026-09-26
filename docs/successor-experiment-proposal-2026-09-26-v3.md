# Successor experiment, proposal version 3: reading how much of the act is organised around who is acting

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1d proposal v3",
in its own worktree (branch `worktree-w1d-proposal-v3`, cut from the main line
at `70be9fb`, the merge of the toy re-run's check). **Status: PROPOSAL, version
3. Nothing here is registered and nothing here binds.** It is written from
version 2 (`docs/successor-experiment-proposal-2026-09-26-v2.md`, main line at
`a3013be`, pull request 54, left unedited) and from John's rulings of
2026-09-26 on the Gate C tier 1 review of version 2
(`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, including its
"Refinements 2026-09-26, after the toy re-run"). It goes to Gate C tier 1 of
`docs/outside-review-protocol.md` (a review attached to a proposal before John
rules on it), then, after his rulings, to Gate A (the registration review, both
tiers) as registration text. No money is spent and no machine is rented by
this document.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30): the plain word before the term of art, and no bare
identifier anywhere. Every finding quoted from a record is labelled
**MEASURED** (a command was run and its output is filed in the record cited)
or **ARGUED** (reasoning a reader can dispute). Every number carries the
committed file it was read from. Figures from the arms whose training does not
reproduce are quoted with the caution
`docs/rulings/2026-09-23-range-and-direction-only.md` requires: they describe
the particular trained models on the record, not a property of the code.*

## What this version rests on

Every source version 2 named as pending has since merged to the main line, and
every source is cited here by its main-line merge commit. One source, the
route (b) label search, had reported but had not yet had its check when this
was written; it is named once so a reader knows which figures that check may
still move.

| Source | Main-line commit | Standing |
|---|---|---|
| The Gate C tier 1 review of version 2, findings RT-212 to RT-229 | `c17dbdc` (pull request 56): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md` | Reviewed version 2 at `e88c3c0`; one fatal finding (RT-212, the empty read on the free arm), four serious, thirteen minor |
| John's rulings on that review | `3af189d` (pull request 60), refined at `4bb5727` (pull request 63): `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the checklist this version was written to; its three refinements after the toy re-run are carried too |
| The five rehearsal-repairs rulings of 2026-09-25, with their annotations after the check | `62c3824` (pull request 53): `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` | Binding; read with the annotations |
| The rehearsal repairs, session (c), and their check | findings `882f252` (pull request 52): `docs/2026-09-26-rehearsal-repairs.md`; check `d216dbc` (pull request 58) | Checked: every verdict reproduces from the committed code; the decimals on arms C, F and M do not, as the 2026-09-23 ruling expects |
| The toy re-run under the version 3 rules, and its check | findings `9d9d31a` (pull request 62): `docs/2026-09-26-toy-rerun-v3-rules.md`, Part 1; check `70be9fb` (pull request 65): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md` | **Every toy figure in this version for arms C, F and M is taken from Part 1 of the re-run findings, under the rules this version registers**; the check recomputed every figure from the committed outputs and found no disagreement. Arm T's figures reproduce exactly and are the same in every record |
| The fifteen trained toy models | `8038275` (pull request 64): `experiments/rehearsal-successor-measure/out-repairs/models/` with `SHA256SUMS` | Committed, with each file's fingerprint; section 10 says what rests on them and what does not |
| The grammar attempt (redesign (c)) and its check | attempt `ff778ea` (pull request 57): `docs/2026-09-26-grammar-attempt.md`; check `f1ea004` (pull request 61) | The pass line was not cleared; fallback (d) registers for the named-other condition (section 4.4) |
| The rented slice, second attempt, and its check | `9f802db` (pull request 51): `docs/2026-09-25-rented-slice-attempt-2-findings.md` and the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`; check `afb5183` (pull request 55) | Checked: every point passes, point 1 in part (the go was not compared with John's own message, which no committed file holds) |
| Version 2's failure-mode pass | `a3013be` (pull request 54): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md` | The author's run on version 2; this version's own run is section 17 |
| The Weekend 1 queue ruling (nine pages, 2026-09-25) | main line: `docs/rulings/2026-09-26-weekend-1-queue.md` | Ruled. Its own check under the pairing rule was owed when version 2 was written and is still owed; this version relies on it as version 2 did, and says so |
| **The route (b) label search on the free arm** | branch `w1d-free-arm-label-search` at `26b737f` (pull request 66, open): `docs/2026-09-26-free-arm-label-search.md` | Reported: none of its three candidate reads clears the four-fifths floor on arm F, and John ruled on 2026-09-26 that this version registers with the fit floor alone (section 7.2, item 1). **Its check under the pairing rule was being run when this was written** and is cited by number once it lands; one of the search's figures is withheld until that check reconciles it (section 7.2, item 1) |

---

## 0. The whole thing in eight sentences

The project's open question is one of degree: a small transformer that has
learned a causally load-bearing answer to "which agent am I" counts as a
centre at the bottom of the gradient, and what would separate it from a
centre in the fuller sense is how much of its act is organised around that
answer. Nobody has a measure of that. So the successor experiment builds
systems whose degree is fixed by how they are built, one where "which agent
am I" sits in a slot that can be swapped on its own, one where it is stirred
into everything, and one that is a mixture of the two by item, and one
ordinary freely trained system, and asks whether a candidate measure can tell
the built systems apart and place the mixture between them. The measure is:
transplant the part of the internal state that says who is acting from one
run into a matched run and see whether the action follows the transplanted
identity; compare that with transplanting the whole internal state at the
same places; the gap between the two, as a share of the room the whole-state
transplant had to move, is the reading. If the measure separates the two
built anchors at the ruled bar, the freely trained system gets a reading and
the project's current sentence "degree unmeasured" is replaced by a number.
If it does not separate them, that is a result too, and the measure is not
used. New in this version: the reading is made only where the straight-line
read that nominates the ownership subspace has actually found its label, at a
pre-stated floor, so that an empty instrument returns *no verdict* rather
than a number at the entangled end; on the toy that is exactly what the
freely trained system returns, on every seed. And the admission that remains
is narrower than before: the toy can now tell an empty instrument from a
ceiling, from a number the procedure already computes, and what it still
cannot tell is a system that is entangled from one whose ownership answer
lives somewhere the read did not look.

---

## 1. Words used here, once

- **The programme.** Minimum Viable Mind, this repository. **MVM-0a** is its
  small-transformer build, registered 2026-08-07, whose Amendment A3 closed on
  2026-09-25 with the registered word *not testable*
  (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`, the closure
  block dated 2026-09-25).
- **Ownership.** Which of the several agents in a synthetic dialogue the model
  itself is. Nothing psychological is meant by the word; it names a fact about
  the episode that the model has to get right.
- **The acting channel.** The wire through which the model is told, at the
  moment it acts, that this turn is its own: a vector added to the model's
  input state at its own turns. Registered as Amendment A1 on 2026-08-09. It is
  the only honest source of ownership in this design, because in a dialogue
  where the turns are interchangeable, nothing in the text itself can carry it
  (the red-team finding that made this necessary is ledger item RT-17, the
  finding that any learnable ownership cue in the tokens is a fingerprint).
- **The injection, or layer 0.** The place the acting channel is added: the
  running state straight after the input embedding, before the first block.
  The transplant code counts it as layer 0. Section 7.2 removes layer-0 site
  sets from the candidate family wherever they span the turns the channel
  fires on.
- **The ownership answer.** A stored answer to "which of the agents am I" that
  later computation looks up.
- **The marker word.** The made-up name that stands for an agent in an episode.
  Marker words are drawn afresh every episode, so no name is permanently
  attached to any agent. **Which marker word is the model's own** is the label
  the ownership read is fitted against (ruled 2026-09-23,
  `docs/rulings/2026-09-23-nomination-label.md`).
- **The running state.** The vector a transformer carries forward from layer to
  layer at each token position, which everything downstream reads and writes.
  The technical name is the residual stream; it is used once more, in section
  6, and not again.
- **Transplanting (patching).** Taking the running state, or a part of it, out
  of one forward pass and putting it into another at the same place, then
  reading what the second pass does. The programme built this for the first
  time in the measurement rehearsal of 2026-09-21
  (`experiments/rehearsal-successor-measure/src/transplant.py`); nothing at
  the registered size has run it.
- **A fitted straight-line read (a linear probe).** A classifier fitted to the
  running state to predict a label, used here only to propose candidate places
  to transplant, never to conclude anything on its own.
- **The fit, and the fit floor.** How often the straight-line read names the
  model's own marker word correctly on held-out development episodes. New in
  this version (ruled, the Gate C rulings, RT-212): a read whose fit is below
  **four fifths** returns *no verdict* for that arm and seed, and the fit is
  printed in the reporting table.
- **The label-permutation null.** The fit the same read reaches when the labels
  are shuffled, from two hundred shuffles at toy scale, reported beside the
  fit as its 95th and 99th percentiles. It is reported, not used as the bar.
- **The no-transplant rate.** The share of trials in which the model, with
  nothing transplanted, already gives the value the donor's identity would
  dictate. It is the quantity the chance-corrected form subtracts (section
  6.3).
- **The chance-corrected form.** The reading with the no-transplant rate
  subtracted from both the top and the bottom of the fraction, ruled as the
  registered form on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`,
  page 2).
- **Arms.** The four trained systems being compared: the one built to keep the
  ownership answer separable (arm T, for tracker), the one built to entangle it
  (arm C, for the fuller centre end of the axis), the one built as a mixture of
  the two by item (arm M, for middle; section 5.3), and the ordinary freely
  trained one (arm F, for free).
- **The twenty-draw null (control 3).** Twenty random subspaces of the same
  rank at the same sites, each transplanted in place of the nominated one, so
  the reader can see whether the nominated directions do more than random
  directions of that size would. Reported, not gated (section 7.3).
- **The rider.** John's addition of 2026-09-25 to the reporting table: every
  arm is also read at arm T's nominated site set and rank, beside the reading
  at its own (the queue ruling, page 3).
- **The tripwire.** The billing check of section 12.5: two ratios, either at
  or above 1.25 halts the wave (the queue ruling, page 6, part 3).
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
likely to change his view of the programme, the matched-role swap experiment
in section 5 of `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`,
extended from two arms to four so the measure has a known case at both ends
of the axis and one in the middle.

**What Amendment A3 hands this experiment, in the words its closure block
registers** (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
the closure block dated 2026-09-25, and
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`). Its outcome:
*not testable: the registered comparison was undefined for every possible
model; separately, removing the ownership-input channel reduced
primary-battery accuracy on all three trained seeds.* Three things the
successor inherits and must carry, from the block's "Successor" paragraph:
measuring the control's ceiling properly is a precondition of any successor
amendment; nothing counts as localized or as absent until both instruments,
probe and causal patching, agree; and the rehearsal requirement applies to
the successor in full. The block also says what may not be said: that the
ownership structure is absent, or that Amendment A3's nulls make it less
likely. Nothing in this proposal reads Amendment A3's checkpoints, and
nothing here reopens its closure.

**Non-binding motivation, from the Wittgenstein note (ruled 2026-09-25, the
queue ruling, page 7).** The TimeAssembler note "Wittgenstein criteria for the
Stage 2 metric" (document id `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
Minimum Viable Mind project; a discussion note of 2026-09-22 that says of
itself "Nothing here is ruled or registered") proposes three tests. Its first
is the rationale this design already runs on, and John ruled that it goes
here, as motivation and not as a requirement: *an internal variable belongs
to the game only if intervening on it changes what the model does.* That is
why the measure is built on transplants rather than on how well a straight
line reads: a representation that a read recovers beautifully but that does
nothing when moved is, on this rationale, not part of the act. The fit floor
of this version is the other half of the same thought: a subspace nominated
by a read that never found its label is not a representation at all, and
transplanting it measures nothing. The note's own caution stands with it:
these criteria license claims about degree of participation, not a verdict on
inside experience. The note's second and third tests wait for resumption
after May 2027; the second is named on the weekend roadmap's extension list
so it is not lost. **Nothing in this paragraph is registered text, and no gate
reads it.**

---

## 3. What counts as a result

Reproduced from section 2 of the December-result roadmap, which John accepted
as the basis of this proposal, with R4 restated to the ruling of 2026-09-21
(item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`). The
registered wording is the wording in the middle column; nothing in this
document may report an outcome in other words.

| Outcome | Registered term | What it means | Satisfactory |
|---|---|---|---|
| **R1** | **metric validated, degree read** | The measure separates arms T and C at the pre-stated bar (section 9: 0.5 on the chance-corrected form), and arm F gets a reading with its spread across seeds. The closure sentence "degree unmeasured" is replaced by a number, stated as where arm F sits against the three anchors on this measure (weakness W1). | Yes |
| **R2** | **metric does not separate** | Every arm carried passes its gate (section 8.1: the own-directed condition on arms T, C and M; both conditions on arm F), but the measure cannot tell T and C apart at the bar. The measure is not used on arm F; the result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | One or more arms fail its gate after the one permitted re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. | Yes, if the gate was reached |
| **R4** | (none) | The programme hibernates with a registered design and a rehearsal only. **Since 2026-09-21 a missed kill date does not put the roadmap here by itself**: registration after 2026-10-18, or launch of the remaining registered runs after 2026-11-01, is still possible on a fresh ruling that names what comes off the back end to make room, and R4 is where the roadmap lands only if that ruling says it is not worth it (item 23 of the 2026-09-21 ruling; section 5 of `docs/december-result-roadmap-2026-09-20.md`). | No. Recorded as a schedule failure, not a scientific one |

**Arm F may return no verdict, and the registration says so in advance (ruled,
the Gate C rulings, RT-212, items 1 and 3).** A reading is made on an arm only
where the straight-line read that nominates its ownership subspace clears the
fit floor of section 7.2 on held-out development episodes. On the toy the
free arm's read never did: its best fit at any layer on any seed is 0.172,
against a floor of 0.8 and a no-information level of 0.072 (MEASURED:
`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section 1.3,
from `experiments/rehearsal-successor-measure/out-v3-rules/nominate_F_seed*.json`).
So the toy record for arm F is **"no verdict, read failed its floor"** on
every seed, and version 2's toy reading for arm F at the entangled end is
withdrawn from the record under failure 2's own rule (the pre-stated target
changed before registration, so the null already collected is withdrawn
rather than reported). **At registered scale the same can happen, and the
first release is the test of it** (John's ruling of 2026-09-26 on the route
(b) result, section 7.2, item 1): the single arm F run of step 5a has its
nomination fit reported against the floor before the second release is asked
for, and a miss is a stop there, beside the learn-both stop (section 11). If
arm F returns no verdict, R1 is not reached by a number at the entangled end:
arms T and C separated and arm F returned no verdict is reported in those
words, and what outcome it maps to is decision 14 in section 15. The route
(b) investigation, which looked for a label the own-directed loss does force
on a free system, found none that clears the floor at toy scale (section 7.2,
item 1), so this version registers with the fit floor alone and with the
ruled label as its one registered read. **Whether a registered "no verdict on
the free arm" is worth the second release is John's call; his present view is
that it is (the Gate C rulings, RT-212, item 3), and under the step 5a stop
that call is made with the registered-size fit in hand.**

**The admission, rewritten (it replaces version 2's, which was ruled on
2026-09-25, the queue ruling, page 5, and is narrowed here by the RT-212
ruling).** Version 2 admitted that a free-arm reading at the entangled anchor
could not be told from the instrument's ceiling, because the chance-corrected
form reads 1 both when the act is entangled and when the nominated subspace
carried nothing. **The toy can tell those two apart, from a number the
procedure already computes**: the fit of the read that nominated the
subspace. A subspace nominated by a read at 0.172 carried nothing, and the
fit floor says so before any transplant is looked at; a subspace nominated
by a read at 0.96 or better, which is what arm C's reads reach at their
nominated layers (1.000, 0.961 and 0.978; MEASURED: the re-run findings, Part
1, section 1.3), held the label and still moved nothing, which is what
"entangled at these sites" means. What the admission that remains says
(ARGUED): a read that clears the floor shows the label is present in the state
at those sites; it does not show that the directions it found are the ones
the act uses. A free arm whose read clears the floor and whose reading is
near 1 is therefore "as entangled as the built anchor at the sites this
procedure nominates", and no more; that the ownership answer lives in some
other part of the state the read did not find is not excluded. Arm M (section
5.3) is a known case in the middle of the scale, so that a free-arm reading
can be placed against three anchors rather than two. It does not remove that
residual admission, because arm M's known degree is a mixture by item, and a
free arm's partial separation, if it has any, would be within each trial
(section 5.3).

**The toy outcome, on the anchors' terms (ruled, the Gate C rulings, RT-213,
item 1).** Under the rules this version registers, the toy reaches R1 on its
anchors: arm T reads 0.0000 and arm C 1.0051, 1.0025 and 1.0000, so the
separation, arm C minus arm T, is 1.0051, 1.0025 and 1.0000 and clears 0.5 on
every seed; arm M reads 0.4886, 0.4860 and 0.5449, inside its band on every
seed; and arm F returns no verdict on every seed, twice over, because it fails
its gate and its read fails the floor (MEASURED: the re-run findings, Part 1,
sections 1.0 and 1.3, from `out-v3-rules/pass2_summary.json`; recomputed with
no disagreement by the check at `70be9fb`, section 3). Arm C's named-other
condition fails on every toy seed, at 760, 751 and 708 correct of 3,000
against a bar of 790 (MEASURED: `out-repairs/gate_base.json` at `882f252`;
the Gate C review, RT-213); under version 2's rules that made the toy an R3,
and under this version's it does not, because the constructed arms are gated
on the own-directed condition only (section 8.1) and their reading uses only
the own-directed action. **Version 2 left that failure out, and this version
states it wherever arm C's toy record is quoted** (sections 5.2, 10 and 11).

**The honest prior, stated before the work rather than after it.** On the
existing record the most likely outcome at registered scale is that **arm F
returns no verdict, or fails its gate**, and the most likely reason for either
is the named-other half of the task and the read that cannot find its label.
Three seeds of the closed Amendment A3 design failed to learn a named-other
query battery, landing at 0.2877, 0.3057 and 0.3195 against 0.3227 for a
solver that cannot read the name the question supplies; a fourth run with the
battery's own loss term reached 0.3125 and changed nothing
(`control-learnability-pilot-findings.md`, the pilot findings file; ledger
items RT-52 to RT-69). This experiment moves the named-other condition from a
query at the end of the episode to an action at the model's own turn. **At toy
scale that has not been enough, and every repair tried has now been tried and
failed** (section 4.4): the named-other condition failed its bar on two of
three toy arms; doubling the training budget did not fix it; a curriculum and
loss re-weighting did not fix it; and the grammar change, redesign (c), did
not fix it either, at 774, 730 and 759 correct of 3,000 on the free arm
against 790 needed on two seeds (MEASURED: `docs/2026-09-26-grammar-attempt.md`
at `ff778ea`, section 3; its check at `f1ea004` re-ran it and got 750, 809 and
739, so at most one seed of three clears on either run). Fallback (d)
registers. Section 11 places a stop before the expensive wave so that a
gate failure on arm F costs the first release (about $44, section 12.3)
rather than the whole plan; **a failure on arm C, the high anchor, is first
seen in step 5b, after the second release is drawn, and section 11 states
that cost.**

**One reporting gap carried open from the Gate C review of version 1.** The
finding RT-182 (the no-verdict finding: the measure's own failure state has
no registered outcome term) is not closed by any ruling of 2026-09-25 or
2026-09-26, although RT-212's ruling now makes a no verdict on arm F a
registered possibility. This version keeps the four terms above and reports
an arm's *no verdict* in those two words, with its reason after a colon as
the re-run's table does ("no verdict: gate failed; read failed its floor");
what outcome a no verdict on arm C, M or F maps to is decision 14 in
section 15.

---

## 4. The task: matched-role revisions

### 4.1 What the model does

The grammar extends the registered Amendment A3 grammar (`curriculum_a3.py`,
the episode generator committed 2026-09-15), which already has the pieces:
four agents, a closed vocabulary, ten turns, eight value slots, every revised
item assigned by all four agents before anyone revises it, and a revision rule
that is a deterministic function of the reviser's own earlier value (the
successor of that value, counted round the eight slots). The rehearsal's
shrunken version of it is `experiments/rehearsal-successor-measure/src/grammar.py`.

The change is that the model now acts in **two matched roles at the same kind
of position**:

- **Own-directed revision.** The model's turn arrives; the correct output is
  the successor of **the model's own** earlier value on that item.
- **Named-other-directed revision.** The model's turn arrives carrying a
  marker word; the correct output is the successor of **the named agent's**
  earlier value on the same item.

Both are actions on the model's own turn, supervised the same way, scored the
same way. This is the whole point of the redesign: in the closed Amendment A3
design the ownership condition was an action and its comparison condition was a
question asked at the end, so the two were never at the same kind of position,
which is the defect the outside review called out and the internal requirements
document had already ranked first for repair.

**The grammar is as version 2 had it.** The grammar change attempted on
2026-09-25 (redesign (c), section 4.4) did not clear its pass line, so nothing
in this section changes; in particular the acting channel fires on both action
turns, as before.

### 4.2 What "matched difficulty" means, concretely

Four things are matched, by construction in the generator and checked at the
rehearsal (MEASURED on the toy grammar: the four matched properties hold,
`docs/2026-09-21-successor-measure-rehearsal.md`, check P-1 and rehearsal item
R-1; re-checked on 3,000 matched pairs under the grammar attempt's setting
too, `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 2):

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
item RT-17). So one condition reads its answer's owner and the other has to
have carried it. That asymmetry *is* the experiment; removing it would mean
putting the model's own name in the text, which would reintroduce the very
leak the acting channel was built to avoid. It is recorded here, will be
recorded in the registration text, and bounds what a difference between the two
conditions may be read as. Decision 9 in section 15 puts it to John.

**Distinctness, and the one place it is relaxed.** Within an item the four
agents' values are distinct, drawn without replacement (MEASURED on the
rehearsal grammar: `experiments/rehearsal-successor-measure/src/grammar.py`,
the function `_content`, draws the four values with `replace=False`, and the
matched-property check counts four distinct candidate values on every item).
Sections 4.2, 6.1 and 8.1 lean on that. Control 6 in section 7.3 needs its
negation for one of its two cells, so control 6 runs on a **separately
generated relaxed set** in which one item per episode has two agents sharing
a value (the same file's `collide` option), labelled as such wherever it
appears. The relaxed set is never used for the reading, the gates or any
other control. Section 7.3 gives the trial counts that set produces.

### 4.3 Carried-forward rules that apply to the new generator

- **The even-split rule.** Any batch fraction that splits rows by condition must
  give an even number of rows, or the split cuts the generator's matched content
  pairs. Measured and recorded 2026-09-20 as ledger item RT-58 (the batch-split
  bias check). The rehearsal grammar carries it (`grammar.py`, the function
  `_check_even_split`).
- **The one-scored-token self-test.** The check that exactly one token per
  supervised position is scored, and that the check survives the shift the loss
  function applies: ledger item RT-59, which turned out to need more than the
  one line it was first written as. It runs on every generator build.
- **The cue-detector gates.** Gates (i) and (ii) of the registered design (no
  surface cue in the curriculum text or the input tensors predicts which turns
  are the model's own) run unchanged on the new grammar. Gate (iii), the
  likelihood attack, runs in its act-withheld form as re-specified in Amendment
  A3 §3.4, because the policy at a revision position is perspectival and
  scoring another agent's turn under it with the acting channel present would
  read the model's ownership knowledge as a leak.

### 4.4 The named-other condition: fallback (d) registers

**What registers (ruled 2026-09-25: the queue ruling, page 4, fallback (d);
the repairs rulings, item 1, whose "if it does not, (d) is what registers" is
now the case).** The registration text records, in these words:

- that the named-other condition **failed its bar on two of three toy arms**
  (on the committed models: arm F clears it on 1 seed of 3, at 994, 781 and
  746 correct of 3,000 against 790; arm C on 0 seeds of 3, at 760, 751 and
  708; arms T and M on 3 of 3; MEASURED: `out-repairs/gate_base.json` at
  `882f252`, reproduced field for field by the re-run's `out-v3-rules/gate.json`
  at `9d9d31a`);
- that **doubling the training budget did not fix it**
  (`docs/2026-09-21-successor-measure-rehearsal.md`, section 8);
- that **both training changes did not fix it**: a curriculum (the named-other
  condition alone for the first 1,000 of 2,500 steps) and loss re-weighting
  (the named-other loss four times the own-directed) cleared on 0 of 3 seeds
  each, against 1 of 3 on the unchanged recipe, and both made it worse
  (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `882f252`, section 2,
  from `out-repairs/gate_curriculum.json` and `out-repairs/gate_reweight.json`;
  the check at `d216dbc` re-ran both from clean and got 0 of 3 each again);
- that **the grammar change did not fix it**: redesign (c), which turns the
  acting channel off on the seven tokens of the named-other action turn so
  that the two action turns no longer receive the same "this turn is yours"
  signal, ran on 2026-09-25 with its pass line committed before the run (790
  or more of 3,000 on at least two free-arm seeds of three, with the
  own-directed condition not degraded below 0.5513). It got **774, 730 and
  759**, 0 seeds of 3; the own-directed half held at a mean of 0.5654
  (MEASURED: `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 3,
  from `out-grammar-c/passline.json`). Its check re-ran the attempt from the
  committed code and got **750, 809 and 739**, 1 seed of 3, and the same
  verdict (MEASURED: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`
  at `f1ea004`, "Verdict"). **The check's note is carried into the record:
  a count of seeds clearing is a property of one training run, not of the
  code**, so the record says "at most one seed of three clears on either
  run", which is also what both earlier runs of the unchanged grammar gave;
- and that **the staggered first run bounds the money** (section 11, step 5a):
  the learn-both result of one free-arm run is read before the remaining
  runs are committed.

**Stop condition S1 did not fire.** It asks whether the grammar is learnable at
tiny scale even in principle, and the separable arm learned both conditions to
1.0000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, arm T on every
seed). This is John's ruling, adopting the rehearsal's adjudication (the queue
ruling, page 4).

**The diagnosis, ARGUED and not ruled.** In this grammar the acting channel
fires on both action turns, so the two turns differ only in one word, and a
model that learns the own-directed route applies it at the named-other turn
too (the repairs findings, section 2, the paragraph headed "The reading").
The grammar attempt tested exactly that diagnosis by removing the shared
signal, and found the free arm still gives its own value at the named-other
turn only about one time in twenty and splits the rest across the other
agents' values, the same pattern as before the change (the grammar attempt at
`ff778ea`, section 3, from `out-grammar-c/diagnose_named_other.json`). Its
own reading, marked ARGUED there and here: the model already tells the two
turns apart and fails at a different step, matching the named marker word to
that agent's assignment. The check agrees the pattern is measured and the
step is not (the grammar check at `f1ea004`, section 4). Nothing in this
version acts on that reading.

**What the grammar attempt's failure does not show.** It does not show that no
grammar change could work, only that the smallest one, which removes the
shared acting signal, did not; and the toy arms may be too small to learn a
condition the registered size will learn, which is page 4's standing argument
against every toy redesign (the grammar attempt, section 7; ARGUED).

---

## 5. The four arms

All four train on the same grammar, at the same size (the registered 30M
configuration), on the same token budget, with the same launcher, watchdog and
network volume. **The launcher, named (ruled, the Gate C rulings, RT-228):**
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered launcher that carries the argument guard of ledger item
RT-198 and the hang fix of 2026-09-25, and that the rented slice's second
attempt ran (`docs/2026-09-25-rented-slice-attempt-2-findings.md` at
`9f802db`). The registered launcher `launch_a3.sh` is registered text under a
standing prohibition (it has no argument handling) and is not used. **Two
things are owed as code before step 4 of section 11, and this document does
not do them:** a training entry point on the rented machine for arms T, C and
M, which does not exist yet, and the tripwire of section 12.5. Arm M's code
(`experiments/rehearsal-successor-measure/src/arm_middle.py`) has run only on
this laptop; that is listed as untested beside the handshake's machine half
in weakness W9. What differs between the arms is the architecture, and only
in the way the ownership answer is allowed to exist.

### 5.1 Arm T: the ownership answer kept separable, by construction

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

What the toy measured, under the rules this version registers: it reads
**0.0000 on every seed**, nominated at layer 0 at the action position, rank 8,
with its read fitting at 1.000 on every seed; its ownership-only transplant
moves the action in every trial, above all twenty random draws of control 3
(MEASURED: the re-run findings at `9d9d31a`, Part 1, section 1.3). Under the
stricter layer-0 variant of section 7.2 its site moves to layer 1 at the
action position and it still reads 0.0000 (the same table). Its gate and
lesion figures reproduce the 2026-09-21 record exactly, and its toy training
reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

Judgment call (decision 2): the ownership path is architecturally forced, not
merely encouraged by a penalty term. The forced version is what makes the
degree known; a soft version would be more comparable with arm F but would
forfeit the one thing the arm exists to supply.

### 5.2 Arm C: the ownership answer entangled, by construction

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

**What the toy measured, under the rules this version registers (MEASURED:
the re-run findings at `9d9d31a`, Part 1, section 1.3, from
`out-v3-rules/measure_C_seed*.json`, row `unruled_layer0_injection_removed`,
and `pass2_summary.json`; recomputed by the check at `70be9fb`, section
3.5).** It reads **1.0051, 1.0025 and 1.0000** on seeds 0, 1 and 2, at the
entangled end on every seed, quoted per seed for these particular models and
not as a property of the code. Its reads fit at **1.000, 0.961 and 0.978** at
the nominated layers (2, 4 and 1, at the action position on seeds 0 and 1 and
at the post-identity position set on seed 2, ranks 8, 2 and 1), so the
subspace it transplants holds the label and clears the fit floor on every
seed; the ownership-only transplant then lands at or below the no-transplant
rate (0.0488, 0.0475 and 0.0600 against 0.0512, 0.0488 and 0.0600) while the
whole-state transplant moves the action in 0.5400, 0.5575 and 0.5463 of
trials. Control 3's twenty random draws sit above the ownership-only
transplant on seeds 0 and 1 (0 of 20 below on seed 0; 0 below and 1 equal on
seed 1) and around it on seed 2 (3 below, 9 equal, 8 above), which is what an
entangled arm should show: its ownership subspace does no more than a random
subspace of its size (the re-run findings, Part 1, section 1.4; ARGUED there).
**Version 2's figures for this arm (0.99 to 1.00, and the separation figures
0.9977 and 0.9927) came from the repairs' 44-set family before the
site-set rule was run and, on two seeds, from all-positions site sets the
rule excludes (the Gate C review, RT-221); they are replaced, not kept.**

**Arm C fails the named-other condition on every toy seed, and this version
says so wherever its toy record is quoted (ruled, the Gate C rulings, RT-213,
item 2).** Its named-other accuracy is 760, 751 and 708 correct of 3,000
against a bar of 790, so it clears on 0 seeds of 3, while its own-directed
condition clears on 3 of 3 (MEASURED: `out-repairs/gate_base.json` at
`882f252`, fields `runs.C/base/*.other_correct`; the Gate C review, RT-213).
Under version 2's learn-both gate that would have made the toy an R3 by way
of the high anchor. Under this version arm C is gated on the own-directed
condition only (section 8.1), with the reason recorded there, so its toy
record is a pass on the gate and a reading on every seed. **What that failure
costs under the launch order** is in section 11: a constructed arm that fails
its gate at registered scale is first seen in step 5b, after the second
release is drawn, and John ruled against an extra arm C run in step 5a on the
envelope's arithmetic (the Gate C rulings, RT-213, item 3).

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the rehearsal showing that its degree is
genuinely known by construction rather than merely intended, and that the
two-arm fallback is accepted in advance. This proposal keeps that exactly as
ruled; rehearsal items R-3 and R-6 in section 10 are the test, and at toy
scale both pass under the registered rules.

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable, but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. The registration text, if
the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker.

### 5.3 Arm M: a mixture of the two, by item

**Why it exists.** Section 3's admission, in its version 2 form: with anchors
only at the two ends, a free-arm reading at the entangled end cannot be told
from a ceiling. John ruled on 2026-09-25 that a fourth, partly separable arm
would be attempted at toy scale at $0, with its predicted reading stated
before it ran, and folded into the main registration only on a pre-stated
pass: a chance-corrected reading between 0.3 and 0.7 on all three seeds (the
queue ruling, page 5, option (iii)). It passed on the repairs run, and it was
folded in (the repairs rulings, item 2).

**Version 2's arm M pass was read without control 3 applied (ruled, the Gate C
rulings, RT-214, item 3).** Under version 2's own rules, which made control 3
a control that holds with a fixed 0.0175 room, arm M seed 1 got no reading
(its random subspace moved 0.0563 of trials against a limit of 0.0350; the
Gate C review, RT-214), so the "on all three seeds" pass John folded arm M in
on was not met by the design as then written. Control 3 is now a reported
twenty-draw null (section 7.3), and under it arm M reads on every seed; the
re-run was the check the RT-214 ruling asked for before this version was
filed, and its result is below.

**The construction** (`experiments/rehearsal-successor-measure/src/arm_middle.py`,
method in `docs/rehearsal-repairs-method-2026-09-25.md`, section 5, both at
`882f252`): arm T's slot and head, and arm C's entangling and ordinary output
layer, in one network. Actions about some items go wholly through the
separable route and actions about the others go wholly through the entangled
route, so that about three fifths of actions are entangled: 0.60375 of the 800
fresh measurement trials, 483 of 800 (MEASURED: `out-repairs/measure_base_M.json`
at `882f252`, the field `fourth_arm.entangled_share`). The repairs findings
print 0.6033, which is the same share on the held-out gate episodes, 1,810 of
3,000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, the field
`own_by_route.entangled_share`); both are right, on different episodes (the
Gate C review, RT-219). **The registration
describes it as what it is: a mixture by item, each action going wholly
through the separable or the entangled route, about three fifths entangled,
not partial separation within a trial** (the repairs rulings, item 2, in those
words).

**The prediction, and what it is (ruled, the Gate C rulings, RT-223).** Write
*p* for the entangled share, and for each route write its whole-state and
no-transplant accuracies. The reading the measure should return, if the blind
nomination catches the separable route's slot and nothing of the entangled
route, is the entangled route's share of the total room the whole-state
transplant moves:

    p × (whole_C − untouched_C) / [ (1 − p) × (whole_T − untouched_T) + p × (whole_C − untouched_C) ]

**That formula is the true-slot reading of section 7.2, item 6, written in
route accuracies: one check, not two.** By algebra, a transplant that carries
the separable route fully and the entangled route not at all gives exactly
this number in the chance-corrected form, and on the repairs run the formula
and the true-slot reading agree to four decimals on every seed (0.4895,
0.4572 and 0.4904; MEASURED: the Gate C review, RT-223, from
`out-repairs/measure_base_M.json` at `882f252`). So what the comparison
shows is that the blind nomination finds about what the true slot gives on
the same episodes, a check of the nomination against the construction, and
not a prediction made in advance of the run. The registered prediction for
arm M at the registered size is: **between 0.3 and 0.7 on every seed, and
within 0.10 of the true-slot reading on the same fresh episodes.** The
true-slot reading is computed and written down before the blind reading is
looked at.

**What the toy measured, under the rules this version registers (MEASURED:
the re-run findings at `9d9d31a`, Part 1, sections 1.0 and 1.3, from
`out-v3-rules/measure_M_seed*.json` and `pass2_summary.json`; recomputed by
the check at `70be9fb`, section 3.4).** The blind reading is **0.4886, 0.4860
and 0.5449** on seeds 0, 1 and 2, inside 0.3 to 0.7 on every seed, so the
fold-in pass stands with control 3 reported beside it. Every seed is
nominated at layer 1 at the post-identity position set, rank 8, with its read
fitting at 1.000; the whole-state transplant moves 0.7800, 0.7738 and 0.7937
of trials and the ownership-only transplant 0.4050, 0.4062 and 0.3688, above
all twenty random draws of control 3 by a wide margin (random medians 0.015 to
0.019). **One figure for arm M has no re-run counterpart:** the re-run did not
recompute the route split or the true-slot reading at the re-chosen site sets,
so the toy demonstration of the "within 0.10" half of the prediction rests on
the repairs run at its own site sets, where the blind reading missed the
true-slot reading by 0.021, 0.027 and 0.042 (the Gate C review, RT-223, from
the same file). That check at the registered site sets is owed with the R-1
to R-6 re-run before Gate A (section 10). Arm M passes its gate on the
own-directed condition on all three seeds (0.8613 to 0.8667), and clears the
named-other condition too (0.5517 to 0.5663), although that is no longer
gated for it (MEASURED: `out-repairs/gate_base.json` at `882f252`). Its
self-test passes all seven checks, including that perturbing the slot never
moves an entangled-route action (`out-repairs/self-tests.txt` at `882f252`).
**Version 2's figures for this arm (0.48 to 0.53) came from the pre-rule
family and are replaced.**

**What this buys, and what it does not (ARGUED, from the findings' own
words).** It shows the measure, pointed blind at a system with a known
mixture, returns a number in the middle and near the mixture's share. It does
not show that the measure scales on a system whose partial separation is
*within* each trial, which is what a freely trained system would have. Page
5's strongest argument against applies in full and is carried as weakness
W10: its degree is a design intention, and it differs from both anchors in
more than degree.

**What it costs.** Three registered runs, priced at **$32 to $44** from the
compute ledger's per-run rows (the queue ruling, pages 5 and 6; the
derivation, from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and
2026-08-12 rows, is on page 5 of
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`), from the $450
envelope (section 12). Of that, the $1.94 development run at the 10-million
size is now paid from the first release's development line and launched in
step 4 with the other three arms (ruled, the Gate C rulings, RT-229; section
12.3), and section 12.4 carries only the three registered runs. **Arm M's
seconds per step were not measured on the rented machine**: the slice of
2026-09-25 timed arms T, C and F only
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section
3). Its three runs therefore rest on ledger rows, not on rehearsal item R-11,
and section 12.4 says so.

### 5.4 Arm F: the freely trained system

The registered register-less configuration with the acting channel present,
the same architecture as the closed Amendment A3 runs, trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate, the ownership-lesion check in section 8, and the fit floor of section
7.2.

**What the toy record states for it: "no verdict, read failed its floor", on
every seed (ruled, the Gate C rulings, RT-212, item 2).** Its read of "which
marker word is the model's own" fits at **0.172, 0.067 and 0.106** at the
nominated layer on seeds 0, 1 and 2, against a floor of 0.8; its best fit at
any layer on any seed is 0.172, and the no-information level of this read is
0.072 (MEASURED: the re-run findings at `9d9d31a`, Part 1, section 1.3, from
`out-v3-rules/nominate_F_seed*.json`; the same fits are in the repairs'
`out-repairs/nominate_base_F.json` at `882f252` and, from the 2026-09-21
rehearsal, in `out/nominate.json` on the main line, so this has been in a
committed record since before the label was ruled, the Gate C review,
RT-212). It also fails the learn-both gate: the named-other condition clears
on 1 seed of 3 (section 4.4). So it fails twice over, and the re-run's table
prints it as "no verdict: gate failed; read failed its floor". **The number
the arithmetic would have returned (1.0000, 1.0000 and 1.0108) is withdrawn
from the record** under failure 2's rule and is not a reading; it appears in
the re-run's table in parentheses only so that a reader can see what an empty
instrument returns, which is the entangled end. Version 2's "1.00 to 1.003" is
replaced by the sentence above.

**What the free arm does instead of representing the label (ARGUED, the Gate
C review, RT-212, from `grammar.py` and the gate file).** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver, and it collapses when the acting channel is removed
(0.1760 to 0.1940), so its ownership answer is load-bearing; but an
own-directed action can be solved by attending to the value tokens on the
turns the acting channel marked, with no need to know which marker word those
turns carry. That is why the route (b) investigation of section 7.2 looks for
a label the own-directed loss does force on a free system.

### 5.5 Seeds

**Three seeds per arm** (ruled 2026-09-25, the queue ruling, page 1f), giving
**twelve** registered runs across four arms. The registration says in terms
that the toy arithmetic implying one seed, the rehearsal's half-width
calculation, which the 2026-09-21 findings cautioned against carrying across
because the toy arms are far more repeatable than registered-size runs will
be (`docs/2026-09-21-successor-measure-rehearsal.md`, section 11), was not
carried across. The training recipe is the rehearsal's unchanged recipe; the
grammar attempt of section 4.4 did not clear, so nothing changes it.

---

## 6. The measure

### 6.1 The pairing

Episodes are generated in matched pairs that share a content seed and rotate
which agent the model is, machinery the registered generator already has. In
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
nominated subspace*, and not *how many places you had to touch*. The
rehearsal's transplanting code proves the restriction as a tensor identity in
its self-test (rehearsal item R-8).

**Two kinds of site set are not an intervention on what the network built.**
Copying the running state at every position of a layer makes everything
downstream of that layer the donor's own computation, wherever ownership lives
only in the running state; copying every layer at every position is the
donor's forward pass outright. And copying layer 0, the state the acting
channel is added to, at positions spanning the turns the channel fires on, is
a transplant of the acting channel's own input rather than of anything the
network computed from it (the Gate C review, RT-216). Section 7.2 removes both
kinds from the candidate family by rule.

### 6.3 The number

For each arm, on fresh episodes:

- `accuracy_whole`: the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only`: the same share under the ownership-only
  transplant.
- `accuracy_untouched`: the same share with no transplant at all: the
  no-transplant rate. Section 6.4 says what it must be near.

**The reading is the chance-corrected form** (ruled 2026-09-25, the queue
ruling, page 2):

    degree = (accuracy_whole − accuracy_ownership_only) / (accuracy_whole − accuracy_untouched)

**with the raw difference and both accuracies always reported beside it**, and
the no-transplant rate with them. Zero means fully separable: transplanting
the ownership answer alone does everything transplanting the whole state
does. One means the ownership-only transplant did nothing at all: the act
resists being pulled apart at these sites. The separation bar (section 9, 1a)
and the floor (1c) are written on this scale.

**Why this form and not version 1's.** Version 1 divided by `accuracy_whole`
alone. A no-transplant rate that sits under both terms does not cancel in
that ratio, so the largest value version 1's reading could return was
different for every arm: the ceiling failure of Amendment A3 with the zero
replaced by a moving number (the Gate C review of version 1, finding RT-172,
the per-arm-ceiling finding, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`;
failure 1 of `docs/known-failure-modes.md`). The rehearsal confirmed it and
demonstrated the repair: on two made-up systems with the same true share
outside the subspace, 0.5, and different transplant strengths, version 1's
form read 0.4323 and 0.3222, and the chance-corrected form read 0.5018 and
0.5013 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`, section
5, from `out/denominator_simulated.json`). The top of the chance-corrected
scale is 1 on every arm; section 17, failure 1, prints it for all twelve
toy arm-and-seed pairs under this version's rules.

**Readings outside 0 to 1 are reported as observed and never clipped** (the
repairs rulings, the paragraph after item 5). A negative reading means the
ownership-only transplant moved the action more than the whole-state one; a
reading above 1 means the ownership-only transplant landed below the
no-transplant rate. Both are sampling noise around "the subspace does
nothing" when small (arm C reads 1.0051 at one toy seed; the re-run findings,
Part 1, section 1.3) and a warning about the instrument when large. The
rehearsal showed a negative value is reachable (rehearsal item R-4).

### 6.4 When the measure returns no verdict

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unequal
ceilings finding). This measure has a denominator, so it gets explicit
no-verdict rules, written before it runs:

1. **The whole-state floor (ruled, the queue ruling, page 1c; refined by the
   repairs rulings, item 4).** A site set is usable only if the whole-state
   transplant clears **four fifths of the arm's own own-directed accuracy on
   the same fresh episodes**, written on the chance-corrected scale:

       accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)

   The plain form, `accuracy_whole ≥ 0.8 × own_directed_accuracy`, is
   printed beside it everywhere, so a reader can see whether the two readings
   of the ruled sentence ever disagree; on the toy they never did (MEASURED: 0
   disagreements across all site sets, arms and seeds, the repairs findings at
   `882f252`, section 3; the re-run records both forms on every row,
   `out-v3-rules/measure_*_seed*.json`, `reading.floor`). *Turning the ruled
   sentence into the first form is this design's choice and is marked ARGUED
   in the repairs method note.* If no site set clears the floor for an arm,
   that arm returns **no verdict** at nomination, and that is recorded rather
   than repaired. The floor keeps the denominator away from zero by
   construction: on an arm that has learned the task,
   `own_directed_accuracy − accuracy_untouched` is large, and the denominator
   is at least four fifths of it.
2. **The fit floor (new; ruled, the Gate C rulings, RT-212, item 1).** The
   straight-line read that nominates the ownership subspace must fit at
   **four fifths or better on held-out development episodes** at the nominated
   layer, the same convention as the whole-state floor. A read that misses it
   returns **"no verdict, read failed its floor"** for that arm and seed, and
   the transplant arithmetic is not reported as a reading. The fit is printed
   in the reporting table, with the label-permutation null beside it as a
   reference and not as the bar. Section 7.2, item 1, gives the rule in full
   and its toy demonstration.
3. **The no-transplant sanity rule, with the review's formula and the
   allowance as re-worded (ruled, the Gate C rulings, RT-222).** Version 1
   said the no-transplant rate "should be near the one-in-eight guessing
   rate; if it is not, the pairing is broken and nothing is read". With
   distinct values that rule is pointed the wrong way round: a model that has
   learned nothing lands near one in eight and a model that has learned the
   task lands far below it (the Gate C review of version 1, finding RT-173;
   failure 3 of `docs/known-failure-modes.md`). The registered rule is the
   review's formula: with *p* the arm's own-directed accuracy on the same fresh
   episodes, the no-transplant rate should be near

       (1 − p) / 7

   because an untransplanted model lands on the donor's answer only by erring
   onto exactly that one of the seven other slots. **The rule carries room
   for a miss of at most the largest measured miss, rounded up to 0.018.**
   The largest miss the rehearsal measured against this formula was 0.017536,
   on the free arm at one seed (MEASURED:
   `docs/2026-09-21-successor-measure-rehearsal.md`, section 5, from
   `out/denominator_floor.json`); version 2 wrote the allowance as 0.0175,
   which that very case fails (the Gate C review, RT-222). On the repairs'
   fresh episodes every miss was inside 0.0132 (the repairs findings at
   `882f252`, section 6.4). A measured no-transplant rate more than 0.018 from
   the formula's value means the pairing is suspect, and nothing is read for
   that arm. **The detection margin at the bar is printed in the reporting
   table**: if a pairing is broken so that the donor's answer is unrelated to
   the recipient, an untouched model hits it one time in eight, and at an
   own-directed accuracy of 0.2633 (the learn-both bar) the formula gives
   0.1052, so the rule flags the broken pairing by 0.0198, a margin of only
   0.0018 over the allowance; at 0.56, the toy free arm's level, the margin
   is 0.0441 (MEASURED: section 17, failure 3). The mechanism is not changed
   this weekend.
4. **A reading outside 0 to 1** is reported as observed (section 6.3), not
   clipped and not suppressed.
5. **If a control that holds fails** (section 7.3 says which two hold), the
   reading is not made for that arm.

**The only subtraction anywhere in this design is of the measured
no-transplant rate, in the chance-corrected form of section 6.3, and nothing
wider.** No ownership-blind ceiling is estimated, subtracted or divided by
anywhere. (This sentence replaces version 1's "No normalisation by an
ownership-blind ceiling anywhere", as the queue ruling's page 2 directs: the
outside review's one-line warning still stands, and the programme has already
paid for the lesson once; what has changed is that the no-transplant rate is
a measured quantity of the pairing, not a ceiling, and subtracting it is what
gives every arm the same top of scale.)

---

## 7. The measurement procedure

### 7.1 Data split, and what "fresh" means

Three disjoint sets, generated from separate seeds and committed before use:

- **Training episodes**: what the arms are trained on.
- **Development episodes**: the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all. **The
  straight-line reads are fitted on development episodes, written to disk and
  reloaded**; they are never refitted on the episodes the reading is taken
  from (the rehearsal caught itself doing that and fixed it before any result
  was read: `docs/2026-09-21-successor-measure-rehearsal.md`, section 9, item 3).
  The fit of section 7.2, item 1, is scored on a held-out part of the
  development episodes (on the toy, the last 180 of 600), never on the fresh
  episodes.
- **Fresh episodes and confirmation seeds**: evaluated once, after the freeze.

**"Fresh" is disambiguated, as the rehearsal required** (its section 7, item
4). Version 1 asked for "marker and content combinations that appear in
neither of the other two sets", and that phrase has two readings. **The
registered reading is the weak one: unseen *combinations* of marker words,
items and values that the arm has each seen in training**, the rehearsal
grammar's pool named `fresh`, which draws from the training vocabulary with
its own seed (`experiments/rehearsal-successor-measure/src/grammar.py`, the
`POOLS` table). The strong reading, marker words the arm has never seen, is
**kept as a named diagnostic and is never the evaluation set**: under it the
separable arm's own accuracy fell to 0.7612, 0.6512 and 0.6512, the
whole-state transplant was capped there, and the reading went negative on two
seeds of three (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
section 7, item 4; the pool named `unseen-vocabulary` in the same grammar
file). The registration says which reading it means in these words.

### 7.2 Choosing the candidate ownership representation: one instrument

On development episodes only, for each arm, **identically**: one function,
which takes no argument that names an arm, called the same way for every arm
(the repairs' `experiments/rehearsal-successor-measure/src/repairs.py` and the
re-run's `src/rerun_v3.py`, both at `9d9d31a`, do this, and their nomination
tables show one rule applied throughout). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy: arm C
is nominated at layers 2, 4 and 1 on its three seeds, the re-run findings,
Part 1, section 1.3).

1. **The label, its route to the states, and the fit floor.** The
   straight-line read is fitted against **which marker word is the model's
   own**. *The route by which that quantity reaches the model's states, in one
   sentence:* the marker word is the input token at every turn the model's own
   assignments are spoken on, so it is carried by the token into the running
   state; and on an arm whose slot is built from it (arms T and M) or which
   multiplies it into content (arm C), the read recovers it at 0.96 or better
   from the first block onward. **What version 2's route sentence went on to
   claim, that which marker word is the model's own is forced by the loss at
   the own-directed action, is false for a freely trained system and is
   struck** (the Gate C review, RT-212): an own-directed action can be solved
   by attending to the value tokens on the turns the acting channel marked,
   without knowing which marker word those turns carry, and the toy free arm
   does exactly that (section 5.4). Ruled 2026-09-23
   (`docs/rulings/2026-09-23-nomination-label.md`; fixed in code as well as in
   text: the repairs code's `READ_LABEL = "marker-word"`, and the successor's
   measurement code when written, per the queue ruling, page 3). The label
   was ruled on the separable arm alone, which is the one arm whose slot is
   made of the label by construction (that ruling's section 4), and it is the
   only one of the three readings of "which agent is acting" that recovers a
   degree known independently of the instrument; the other two, the agent's
   slot and the marker's rank, put an arm whose degree is zero by construction
   at the entangled end of the scale.

   **The fit floor (ruled, the Gate C rulings, RT-212, item 1).** The read's
   accuracy on held-out development episodes at the nominated layer is
   printed in the reporting table for every arm and seed. **A read below four
   fifths returns "no verdict, read failed its floor" for that arm and seed.**
   The floor is absolute, the same convention as the whole-state floor. The
   label-permutation null, the fit the read reaches when the labels are
   shuffled (two hundred shuffles at toy scale; its 95th and 99th percentiles),
   is reported beside it and is not the bar. The reason recorded in the
   ruling: a permutation null alone would likely certify a read at 0.172,
   which recovers the label on about one episode in six, and that is not an
   instrument worth transplanting. The floor is applied per seed, as the
   re-run applied it; the check at `70be9fb`, section 4.1, notes that the
   ruling's "on that arm" leaves per-seed against per-arm open, and that on
   the toy it is moot because every arm passes or fails on all three seeds
   alike (decision 21).

   **The toy demonstration the ruling required (MEASURED: the re-run findings
   at `9d9d31a`, Part 1, section 1.3; the check at `70be9fb`, section 3.2).**
   The floor returns no verdict on the committed arm F reads and a reading on
   arms T, C and M: arm F fits at 0.172, 0.067 and 0.106 at its nominated
   layers (best anywhere 0.172); arm T at 1.000 on every seed; arm C at 1.000,
   0.961 and 0.978; arm M at 1.000 on every seed; the permutation null's 95th
   percentile sits at 0.111 to 0.128 across all twelve pairs. The lowest fit
   among the reads that clear is 0.961. **One clause of the rulings file's
   refinement item 2 is wrong on this point and is owed an annotation**: it
   says that under the layer-0 removal "arms C and F still fall to the fit
   floor"; arm C does not, and only arm F falls to the floor (the check at
   `70be9fb`, section 6). Nothing ruled depends on the clause.

   **The route (b) investigation, and what it found (the Gate C rulings,
   RT-212, item 3; the result ruled 2026-09-26).** Route (b) asked for a label
   the own-directed loss does force on a free system, which a straight-line
   read can recover on arm F at four fifths. The free-arm label search
   (`docs/2026-09-26-free-arm-label-search.md`, branch
   `w1d-free-arm-label-search` at `26b737f`, pull request 66; laptop only, $0,
   nothing retrained, on the committed arm F models) tried three candidates
   under the registered site-set rule at toy scale, with a floor of 0.80 on
   held-out fit and a 200-shuffle label-permutation null at each site.
   **None clears the four-fifths floor on arm F, at any site set, on any
   seed.** The best is 0.789, from candidate 1 (which earlier turns are the
   model's own), and that from position spans that start at one of the
   model's own turns, so that where the span starts gives part of the answer
   away; anchored at the action position the three candidates reach 0.733,
   0.383 and 0.478. All three sit well above their shuffle null, so they are
   carried by the free arm, just not at the floor (MEASURED: the search's
   findings at `26b737f`, sections 1 and 2; **its check under the pairing rule
   was being run when this was written and is cited by number when it
   lands**). **John's ruling of 2026-09-26: this version registers with the
   fit floor alone; the ruled label, which marker word is the model's own,
   stays the one registered read; and the three candidates enter the toy
   record as exploratory fits, not as registered reads.** One of the search's
   figures is withheld here: its fit for the ruled label on arm F over the 60
   site sets differs from the 0.172 the Gate C review and the re-run report,
   and it is not quoted until the search's check reconciles the two; the 0.172
   quoted throughout this version is the re-run's. What follows from the
   ruling for the launch order: the single arm F run of step 5a has its
   nomination fit reported against the floor before the second release is
   asked for, and a miss is a stop there (section 11, step 5a).

2. **Candidate sites: the rule, the printed list, and what is removed from the
   family.** The site list is registered as the rule that generates it
   (ruled, the queue ruling, page 1e), and the registration prints the list
   the rule produces for the registered 12-layer architecture beside the rule,
   with the count of comparisons it implies, so the family correction is
   pre-stated. **The rule has now been run at toy scale exactly as registered
   (ruled, the Gate C rulings, RT-215; MEASURED: the re-run findings at
   `9d9d31a`, Part 1), so every toy nomination, reading and control figure in
   this version comes from the family the rule generates**, which meets the
   review's objection that version 2's figures came from a hand-listed
   44-set family the rule never produced (the Gate C review, RT-215). The
   rule:
   - **Positions**, grouped into the position sets the rehearsal used and
     registered here by name (`experiments/rehearsal-successor-measure/src/rehearse.py`,
     `CANDIDATE_POSITIONS`; positions in `src/transplant.py`): the action
     position alone (`action`); **the action position and the answer-marker
     token just before it** (`action+ans`; version 2 described this set
     backwards, the Gate C review, RT-224); the action position and the three
     positions before it (`action+3`); every position from the model's first
     own turn to the action (`post-identity`). (The rehearsal's fifth set,
     every position, is excluded by the rule below.) *That this grouping is
     what the ruled position clause means is this design's reading, marked
     ARGUED and put to John as decision 19.*
   - **Layers**: every contiguous set of the model's running states, counting
     the state after the input embedding as one (layer 0) and each of the
     twelve blocks' outputs as one more: 13 states, 91 contiguous sets.
   - **The all-positions exclusion** (ruled, the repairs rulings, item 3):
     **any site set whose positions are all positions is excluded**, at any
     layer. The reason is section 6.2's: copying all positions at a layer
     hands the donor's whole forward pass downstream. On the four named
     position sets no site set spans every position in any episode (MEASURED:
     the re-run's `out-v3-rules/nominate_*_seed*.json`, field
     `family.share_of_episodes_where_position_set_spans_every_position`; the
     check at `70be9fb`, section 4.3), so on this family the exclusion removes
     nothing further.
   - **The layer-0 exclusion, as removal from the family (ruled, the Gate C
     rulings, RT-216, item 1, as clarified by refinement item 2).** Layer 0 is
     the state the acting channel is added to. **Every site set whose layers
     include layer 0 is removed from the candidate family before nomination
     at every position set other than `action`**, and the rule chooses again
     from what remains, in the way the all-positions exclusion works. Layer 0
     stays a candidate at the action position set only, where the constructed
     anchors' slot sits by construction. The reason: at position sets
     spanning the turns the channel fires on, the twins differ at layer 0 only
     by the channel's own input, so a whole-state transplant there is a
     transplant of the acting channel and not of anything the network built,
     and the subspace compared against it was, on arms C and F, a read fitted
     at 0.072 (the Gate C review, RT-216). **This reading of the ruling, that
     "excluded" means removed from the family and chosen again, was clarified
     after the re-run of 2026-09-26, with the re-run's figures in hand, and is
     not called pre-stated here**: the re-run's first pass read "excluded" as
     "reported as no verdict", recorded the removal reading as its own column
     before it ran, and put the choice to John, who ruled the removal reading
     on the same day (the re-run findings, Part 2; the check at `70be9fb`,
     sections 1.3 and 4.6). Under it, six of the nine toy nominations on arms
     C, F and M that the first pass had left at the injection move off layer
     0, every one to a single later layer (the re-run findings, Part 1,
     section 1.5). *Two readings of which position sets "span the acting
     turns" exist, and they give the same twelve toy nominations:* the ruling's
     first sentence keeps layer 0 at `action` only, which the re-run applied;
     its parenthesis names `post-identity` and any set including the marked
     turns, which on this grammar is `post-identity` alone (MEASURED: the check
     at `70be9fb`, section 4.4, by a script printed in its appendix C and not
     committed as a file). This version
     registers the reading as run, layer 0 kept at `action` only, and puts the
     narrower one to John as decision 20. On the separable arms layer 0 inside
     the action turn does move the action (arm T's whole-state share there is
     1.000 against 0.000 untouched; arm M's about 0.40, short of its floor),
     so it is the rule's position-set order, `action` first, that decides the
     tie on arm T and not any property of the states (the check at `70be9fb`,
     section 5). Version 2's argument that those states are identical in the
     twins was wrong for arms T and M and is not repeated.
   - **The count.** With every contiguous layer set at the four position sets,
     the family is 60 site sets on the toy and 364 on the registered model;
     with the layer-0 sets removed at the three position sets other than
     `action`, **45 site sets and 180 comparisons on the toy, and 325 site
     sets and 1,300 comparisons on the registered model** at four rank caps.
     The narrower reading of decision 20 gives 55 and 220 on the toy, 351 and
     1,404 on the registered model; the stricter variant below gives 40 and
     160, and 312 and 1,248 (MEASURED by this session: section 17, failure
     3, prints the command and its output). The ruled figures before the
     all-positions widening, 296 and 1,816, and version 2's 60 and 364, are
     superseded by these; the repairs rulings' annotation 4 records the first
     supersession. The list and the rule have to agree, and the registration
     prints both.
   - **The stricter variant, as a sensitivity row (ruled, the Gate C rulings,
     RT-216, item 3).** Every layer-0 site set removed at every position set,
     `action` included, then choose again. Reported beside the primary
     reading for every arm and seed, so John can switch to it with figures in
     hand before Gate A. On the toy it differs from the primary row only on
     arm T, whose site moves from layer 0 to layer 1 at the action position,
     rank 8, with fit 1.000 and reading 0.0000 on every seed; on arms C, F
     and M the primary nominations contain no layer 0, so the row is the same
     pick with the same numbers (MEASURED: the re-run findings, Part 1,
     section 1.3; the check at `70be9fb`, section 3.7). The reason recorded
     for not ruling it blind: it may move arm T's anchor read off the layer
     its slot was built at, which on the toy is exactly what it does.
3. **Candidate directions.** At each site, fit the straight-line read for the
   label above and take its leading directions, at each of the rank caps
   **1, 2, 4 and 8**; **the registered cap is 8** and the search family
   reports all four (ruled, the queue ruling, page 1d).
4. **The layer set for the whole-state transplant: "the smallest that clears
   the floor", in one reading** (ruled, the repairs rulings, item 4). For each
   position set, the layer set with the fewest layers that clears the
   four-fifths floor of section 6.4, ties going to the earliest layers; a
   position set with no clearing layer set drops out. The other reading, the
   highest ownership-only share over every clearing site set, is computed and
   printed beside it as a sensitivity row, **and that repairs-style row is the
   sensitivity row this version means** (the check at `70be9fb`, section 4.3,
   asked for the row to be named). On the repairs run's 44-set family the two
   readings picked different site sets on **8 of 12 arm-and-seed pairs, and
   the ownership-only shares they reached differed on 7 of 12**, by 0.02 or
   less (MEASURED: the Gate C review, RT-218, which resolved version 2's two
   counts; the repairs rulings' annotation 3, which adds that the check's
   re-run gave 6 of 12, so about half the pairs, by about 0.02, is what both
   runs support). On the re-run's 60-set family, no primary nomination is a
   multi-layer set, and the sensitivity reading picks a multi-layer set on five
   of twelve pairs (MEASURED: the re-run findings at `9d9d31a`, Part 2, first
   pass, section 5). The ruling's condition, that a nomination moving to a
   multi-layer set the hand list never tried be reported, did not fire.
5. **Nominate by causal effect, not by how well the read fits.** Over the
   surviving (position set, its smallest clearing layer set) pairs and the
   four rank caps, the nominated configuration is the one with the highest
   *development-set ownership-only transplant accuracy*; ties go to the lower
   rank, then the earlier position set. This is the main lesson of the closed
   design: a representation that a straight-line read recovers beautifully can
   do nothing when you intervene on it. The fit floor of item 1 is applied to
   the nominated configuration afterwards, not used to choose it, so the
   nomination stays blind to how well the read fits and the floor stays a
   no-verdict rule rather than a tie-break.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference; on arm M that reference is the formula
   of section 5.3 written in route accuracies, one check and not two (the Gate
   C rulings, RT-223). Judgment call; decision 1.
7. **The rider, in the reporting table** (ruled: John's addition, the queue
   ruling, page 3; kept in the table by the repairs rulings). For every arm
   and seed, the reading is also taken at **arm T's** nominated site set and
   rank for the same seed, using that arm's own read fitted at those sites,
   and reported beside the reading at the arm's own nomination, so a reader
   can see whether what differs between arms is their degree or where the
   procedure looked. **Where the whole-state transplant at arm T's site set
   misses the floor, the rider returns "no verdict", and the report says
   which of two things that means.** On the toy it returned no verdict for
   arms C, F and M on every seed, for two different reasons (ruled, the Gate C
   rulings, RT-225): on arms C and F, at layer 0 at the action position,
   nothing about ownership has yet reached those arms' running states, and
   the whole-state transplant lands on the no-transplant rate (0.0512 to
   0.0600 on arm C, 0.0563 to 0.0688 on arm F); on arm M, which carries arm
   T's slot, the whole-state transplant there moves the action in about 0.41
   of trials against about 0.01 untouched, and the no verdict is **a miss of
   the four-fifths floor**, not nothing reaching the state (MEASURED: the
   repairs findings at `882f252`, section 3, "The rider"; the Gate C review,
   RT-225; the repairs rulings' annotation 5). Arm T's site set is layer 0 at
   the action position on every seed under the registered rule, the same site
   the repairs run nominated, so these rider figures stand under the rule.

### 7.3 Controls

Every one of these is run on every arm. **Two of them hold**, and a failure
means the reading is not made for that arm: control 7 (the null transplant)
and control 1 on arm T only. **The rest are reported** beside the reading,
each with its pre-stated expectation, and cannot veto it. Version 2 made
control 3 hold as well; this version does not, for the reason under item 3.

**What was and was not re-run under the registered rules.** The re-run of
2026-09-26 re-ran control 3 (as the twenty-draw null) and control 7 at the
re-chosen site sets for every arm and seed. It did not re-run controls 1, 2, 4
and 6 at those site sets. For arm T, whose nomination is unchanged and whose
training reproduces exactly, the repairs run's figures for those controls
stand. **For arms C, F and M, version 2's figures for controls 1, 2, 4 and 6
were taken at site sets the rule no longer nominates and are not carried into
this version**; each is stated below as an expectation with its rationale,
and the figures are owed from the R-1 to R-6 re-run before Gate A (section
10).

1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.018 room of section 6.4 (on the toy:
   0.0000 on every seed, the repairs findings at `882f252`, section 6.3). *On
   arms C, M and F it is reported and cannot veto.* On an entangled arm the
   complement carries the ownership signal by construction, since in a system
   where ownership multiplies content at every layer there is no
   ownership-free complement to transplant, so on such an arm the complement
   is expected to reproduce the counterfactual almost as well as the whole
   state does; the 2026-09-21 rehearsal saw 0.5375 against a whole-state
   0.5400 on its entangled arm (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 6). As version 1 wrote it, this control would have vetoed the
   reading on exactly the arm the control battery exists to validate, and on
   arm F it would have vetoed whatever the free arm turned out to be, which is
   the thing being measured. Its value on arms C, M and F is a description of
   how much of the identity-driven difference lives outside the nominated
   subspace, which is the reading itself seen from the other side.
2. **Another agent's representation: not applicable on arms T and M; a
   reported check on arms C and F** (ruled, the repairs rulings, item 5).
   Nominate, by the identical procedure with the named agent's marker word as
   the label, a representation of the named agent who is not acting, and
   transplant it from a twin that differs only in which agent is named; the
   own-directed action should not move. *Pre-stated pass line*: the
   own-directed action changes in no more trials than under a random subspace
   of the same rank at the same sites, plus 0.05 (the rehearsal's tolerance;
   registering that number is decision 15). *Run only once the arm has learned
   the named-other condition* (passes the section 8.1 bar on that condition),
   because it returns no verdict on an arm that has not; on the toy that is
   every arm C and arm F seed but one. *Not applicable on arms T and M*, which
   hold the named agent outside the running state by construction, so no
   transplant into the state can move that action: on the toy, 0 of 44 site
   sets cleared the floor on arm T although it scores 1.0000 on the
   named-other condition (MEASURED: the repairs findings at `882f252`, section
   4; arm M's count there is from the pre-rule family and is not carried). Its
   mechanism is not reworded in this version. This is the successor's own
   obligation, not the closed design's control run on 2026-09-21 (the Gate C
   review of version 1, finding RT-181, on version 1's wording).
3. **Matched random subspaces: the twenty-draw null. Reported, not gated
   (ruled, the Gate C rulings, RT-214, items 1 and 2, as refined on 2026-09-26
   by refinement item 1).** Twenty random subspaces of the same rank and the
   same norm at the same sites are each transplanted in place of the
   nominated subspace, on every arm and seed. The reporting table prints the
   median and 95th percentile of the twenty random donor shares, the
   ownership-only transplant's own donor share, and how many of the twenty
   draws fall below, equal and above it. The fixed 0.0175 room of version 2 is
   dropped from this control. **The reason it is reported and not gated, as
   recorded in the refinement: a gate on this control cannot pass a separable
   arm and an entangled arm in the same direction.** An entangled arm's
   ownership-only transplant is meant to move nothing, so it can never beat
   random subspaces; on the re-run's first pass, which gated on it, arm C seed
   0's read fit at 1.000 and was blocked only by this control (the re-run
   findings, Part 2, first pass, sections 6.2 and 7). Its job of catching a
   leaky site set is done by the whole-state floor and the no-transplant rule.
   **This reporting rule was clarified after the re-run of 2026-09-26, with
   the first pass's figures in hand, and is not called pre-stated here**; the
   re-run's method had argued before any output that the gate as worded would
   return "does not count" on an entangled arm whether or not the read found
   its label (the check at `70be9fb`, section 1.3). *What the toy shows
   (MEASURED: the re-run findings at `9d9d31a`, Part 1, sections 1.3 and 1.4):*
   on arms T and M the ownership-only transplant sits above all twenty draws
   on every seed (arm M about 0.37 to 0.41 against random medians of 0.015 to
   0.019); on arm C it sits below all twenty on seeds 0 and 1 and in the
   middle on seed 2; on arm F it sits in the middle of the draws on every
   seed, which is consistent with a read that holds nothing, though arm F's
   verdict comes from its fit and not from this control. Version 2's arm M
   pass was read without this control applied (section 5.3).
4. **A position where the answer is not yet knowable. Reported.** Transplanting
   before the identity can be known is expected to do nothing. Version 1 made
   this hold; the rehearsal repairs found it reaching well above the
   no-transplant rate on arms C and F at their then-nominated sites, because
   those arms receive the ownership signal by other routes at those sites, so
   "before the identity can be known" is not "before the state differs"
   (MEASURED and ARGUED: the repairs findings at `882f252`, section 6.3; the
   figures there are at pre-rule site sets and are not carried). *Changing it
   from a control that holds to a reported one is this design's call, not a
   ruling*, and is decision 16.
5. **Fresh marker and content combinations**, per section 7.1. By construction.
6. **Who is acting, versus which value. Reported, on the relaxed set.** The
   discriminating control. Trials are split into pairs whose donor identity
   dictates *the same* value as the recipient's and pairs where it dictates a
   *different* value. A transplant that has moved who is acting changes the
   action in the second group and not the first; a transplant that has
   smuggled a value across changes the action in both. **The first cell is
   empty by construction on the distinctness-preserving grammar** (0 of
   4,000 trials: MEASURED, `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 5, from `out/denominator_control6.json`; the Gate C review of
   version 1, finding RT-173; failure 3 of `docs/known-failure-modes.md`), so
   control 6 runs on the **separately generated relaxed set** of section 4.2,
   in which one item per episode has two agents sharing a value. On that set
   both cells have trials: 81 same-value and 719 different-value trials of 800
   per arm and seed on the toy, on all four arms (MEASURED: the `controls`
   fields of `out-repairs/measure_base_*.json` at `882f252`; section 17,
   failure 3, prints them). Both cells are pre-stated and both are reported,
   with the one-in-four reference for a solver that cannot tell which agent it
   is restated for the relaxed set, where it rises (on the toy, from 0.2467 to
   0.3095 on exactly the trials the relaxation adds; the 2026-09-21 rehearsal,
   section 5). Pre-stated expectation: the separable arm moves nothing in the
   same-value cell and everything in the different-value cell (on the toy,
   0.000 and 1.000, the same file); an entangled arm is expected to move the
   same-value cell too, as the repairs run found on arms C and M at their
   then-nominated sites, and that is reported as the caveat it is (weakness
   W11): on those arms the whole-state transplant carries something besides
   identity.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read. On the
   toy it holds on all twelve arm-and-seed pairs, at the first pass's site
   sets; the re-run's second pass, which was arithmetic on the first pass's
   outputs, did not re-run it at the seven site sets that changed (the check at
   `70be9fb`, section 3.8, which calls this a citation gap and not a doubt,
   since copying a model's own state into itself is a no-op at any site). It
   is re-run at the registered site sets before any registered reading.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text, as the one registered
  read; the three route (b) candidates recorded as exploratory fits and not
  frozen as reads;
- **the fit floor (four fifths, on held-out development episodes) and the
  permutation null beside it**;
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture, its two exclusions (all positions; layer 0 away
  from the action position set, as removal from the family), and the count of
  comparisons;
- the stricter layer-0 variant, as the sensitivity row;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its rank, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it", with the repairs-style sensitivity
  row named;
- the transplanting operation, as code, with its self-tests;
- all seven controls, which two hold, **the twenty-draw null of control 3 and
  its reported statistics**, the pre-stated cells, the relaxed set for control
  6 and its generating seed;
- the whole-state floor rule (four fifths, on the chance-corrected scale) and
  the no-verdict rules of section 6.4, including the no-transplant formula,
  its 0.018 room and the detection margin printed at the bar;
- the separation bar between R1 and R2 (0.5);
- the gates of section 8: the own-directed bar on arms T, C and M, the
  learn-both bar on arm F, and the ownership-lesion rule with its two-of-three
  clause;
- the uncertainty method (section 9, 1g) and the seed count (three);
- the reporting table's columns (section 7.5), including the rider;
- the predictions: arm T near zero; arm C high; arm M between 0.3 and 0.7 and
  within 0.10 of its true-slot reading on the same fresh episodes; arm F
  unknown and not predicted, and possibly no verdict.

Nothing on that list may be changed afterwards. If something on it turns out
to be wrong, the registered output is reported as it stands and the correction
is a separate, dated note beside it, the programme's existing practice, and
the process correction the outside review asked for: an immutable registration
is not an immutable scientific conclusion, but the two are kept visibly apart.

### 7.5 The reporting table

One row per arm and seed, with these columns, in this order, so that every
number a no-verdict rule or a caveat depends on is beside the reading it
bears on:

1. the nominated site set (layers, position set, rank);
2. **the read's held-out fit at the nominated layer, and the permutation
   null's 95th and 99th percentiles beside it** (RT-212);
3. whether the fit floor passes;
4. the whole-state, ownership-only and no-transplant accuracies on fresh
   episodes, the raw difference, and whether the whole-state floor clears in
   both forms;
5. the no-transplant miss against the formula of section 6.4, **and the
   detection margin at the bar** (RT-222);
6. **control 3's twenty-draw null: median and 95th percentile of the random
   donor shares, the ownership-only share, and the counts below, equal and
   above** (RT-214);
7. the reading on the chance-corrected form, or the no verdict with its
   reason;
8. **the stricter layer-0 row**: the same columns with every layer-0 site set
   removed (RT-216);
9. the repairs-style sensitivity row for the whole-state layer set;
10. the rider: the reading at arm T's site set, or its no verdict with which
    of the two reasons applies;
11. the true-slot reference on arms T and M;
12. controls 1, 2, 4 and 6, each with its pre-stated expectation, and control
    7's pass;
13. the ownership-lesion result;
14. and, across the three seeds of each arm, the across-seed spread of the raw
    difference with the within-seed bootstrap beside it (section 9, 1g).

---

## 8. The gates every arm passes before it is read

### 8.1 The gate on learning: own-directed only on the constructed arms, both conditions on arm F

**The constructed arms T, C and M are gated on the own-directed condition
only; arm F keeps the learn-both gate (ruled, the Gate C rulings, RT-213,
item 1, refining the queue ruling's page 1b as it applies to arms T, C and M;
the bar itself is unchanged).** The reason recorded: the anchors' ownership
slot is built in by construction, their reading uses only the own-directed
action, and the named-other gate tests whether a free system learned to
represent ownership, which the anchors are not asked to prove. Arm F is not
read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, on every arm, with
  its spread across seeds. Not combined into one number, not normalised by
  anything. The named-other condition is reported on arms T, C and M although
  it does not gate them.
- **The threshold, per condition (ruled, the queue ruling, page 1b):** the
  condition's accuracy is above the one-in-four level at the 0.05 level under
  a one-sided binomial test, **on at least two seeds of three**. The ruling
  writes the bar as "above 0.2630"; on 3,000 held-out episodes that is 790 or
  more correct, a share of 0.2633 (MEASURED: the bar's derivation is printed
  in `docs/rehearsal-repairs-method-2026-09-25.md` at `882f252`, and
  `out-repairs/gate_base.json` carries it as the field `bar`; this session
  re-derived it by an exact binomial tail, section 17, failure 3); at the
  registered episode count it is the same rule, recomputed and printed.
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal, one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, `out-repairs/gate_base.json` at `882f252`).
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.
- **What is already on the record about this gate (MEASURED: the re-run
  findings at `9d9d31a`, Part 1, section 1.2, whose gate counts equal
  `out-repairs/gate_base.json` field for field):** arm T clears both
  conditions on 3 seeds of 3; arm C clears the own-directed condition on 3 of 3
  and the named-other on 0 of 3 (760, 751 and 708 of 3,000), and passes its
  gate; arm M clears both on 3 of 3 and passes; arm F clears the own-directed
  on 3 of 3 and the named-other on 1 of 3 (994, 781 and 746), and **fails**.
  No training change fixed the free arm's failure (section 4.4).

### 8.2 The ownership-lesion check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation, the lesion
the existing code already performs. **The pre-stated shape (ruled, the queue
ruling, page 1h; refined by the Gate C rulings, RT-220):**

- **own-directed accuracy falls below the section 8.1 bar**: that is the
  collapse, and it gates;
- **arm F is read if at least two of three seeds collapse, with the third
  reported** (the RT-220 ruling). A separate collapse bar below the learn-both
  bar was considered and not taken, because it adds a second pre-stated
  number nobody has rehearsed. What the two-of-three clause is for: because
  the collapse line *is* the learn-both bar, it sits just above the level a
  fully collapsed arm is expected to reach, and an arm whose lesion drops it
  to exactly one in four is read as "not collapsed" 4.85% of the time per
  seed (MEASURED: section 17, failure 3, the exact binomial tail at 790 of
  3,000). One seed of three misreading that way must not stop arm F being
  read;
- named-other-directed accuracy is **reported and not gated**; the pre-stated
  expectation that it holds is a description, because the rehearsal found
  that shape is architecture-specific (`docs/2026-09-21-successor-measure-rehearsal.md`,
  section 8);
- the ownership-free state and syntax batteries **must hold**.

**What this check does and does not establish, in the closed design's own
registered words: it removes a sense organ, not a structure the network
built.** It is a precondition for reading arm F, since it shows the ownership
answer is load-bearing for the act, which is what makes arm F worth
measuring; it is not evidence of a centre and is never reported as such.

Arms T, C and M do not take this check as a gate: their dependence on
ownership is architectural. Their lesion results are computed and reported as
a description of the constructed systems. **On the toy, described honestly
(ruled, the Gate C rulings, RT-220):** arm T collapses on two of three seeds,
at 0.2467 and 0.2510, and its seed 2 reads 0.2733 against the bar of 0.2633,
so under the rule it did not collapse there; arms C and M collapse on all
three (0.1703 to 0.1830 and 0.2190 to 0.2230); arm F, the arm this gate is
for, collapses on all three, at 0.1760 to 0.1940 (MEASURED:
`out-repairs/gate_base.json` at `882f252`, fields `lesioned_own` and
`lesion_collapses_own`; section 17, failure 3, prints them). Version 2's "all
three collapse" was wrong for arm T seed 2 and is replaced.

---

## 9. The numbers, now set

Every number version 1 deliberately left blank is filled from John's rulings
of 2026-09-25 and 2026-09-26, each citing the ruling that set it. **None was
invented here.** The registration text freezes them in this form.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form, per seed | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a. **Under this version's rules the toy cleared it on every seed, at 1.0051, 1.0025 and 1.0000** (MEASURED: the re-run findings at `9d9d31a`, Part 1, section 1.0, from `out-v3-rules/pass2_summary.json`, `separation`). Version 2's 0.9977 and 0.9927 came from the pre-widening family, at site sets the rule excludes, and are superseded (the Gate C rulings, RT-221) |
| Gate on learning (R3) | above one in four at the 0.05 level, one-sided binomial, on at least two seeds of three: **0.2633 on 3,000 held-out episodes** (790 or more correct), or the same rule at the registered count; **on the own-directed condition only for arms T, C and M, on both conditions for arm F**; the ownership-blind and name-only solvers reported beside it as references | the queue ruling, page 1b; the Gate C rulings, RT-213, item 1 |
| Fit floor on the nominating read | **four fifths on held-out development episodes**, at the nominated layer, per arm and seed; the permutation null reported beside it and not used as the bar | the Gate C rulings, RT-212, item 1 |
| Whole-state floor (whether a site set is usable) | **four fifths of the arm's own own-directed accuracy** on the same fresh episodes, on the chance-corrected scale; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded; every layer-0 site set removed at position sets other than `action` | the queue ruling, page 1c; the repairs rulings, items 3 and 4; the Gate C rulings, RT-216, item 1, as clarified by refinement item 2 |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the queue ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model: **325 site sets and 1,300 comparisons** after the layer-0 removal (45 and 180 on the toy); the count is the rule's output, not hand arithmetic | the queue ruling, page 1e; the repairs rulings, item 3; the Gate C rulings, RT-215 and RT-216 |
| Control 3 | **a twenty-draw null, reported and not gated**: median, 95th percentile, and the ownership-only share's place among the draws | the Gate C rulings, RT-214, items 1 and 2, as refined on 2026-09-26, refinement item 1 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the queue ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so | the queue ruling, page 1g; on the repairs run the two disagreed by more than two to one on arms C and F (the repairs findings at `882f252`, section 6.2; figures at pre-rule site sets, not carried) |
| Ownership-lesion collapse threshold (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed, **on at least two seeds of three, the third reported**; the named-other clause reported and not gated; the ownership-free batteries must hold; gates arm F only | the queue ruling, page 1h; the Gate C rulings, RT-220 |
| The no-transplant allowance | **at most the largest measured miss, rounded up to 0.018**; the detection margin at the bar printed in the reporting table | the queue ruling, page 2; the Gate C rulings, RT-222 |
| The form of the reading | **the chance-corrected form** of section 6.3 | the queue ruling, page 2 |
| The label | **which marker word is the model's own**, the one registered read; the route (b) candidates recorded as exploratory fits only | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3; the Gate C rulings, RT-212, item 3; John's ruling of 2026-09-26 on the route (b) result (section 7.2, item 1) |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`; checked at `afb5183`, point 5. **Arm M was not timed.** Whether fifty steps meets item R-11's five hundred is decision 17 |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of its true-slot reading on the same fresh episodes (the formula of section 5.3, which is that reading written in route accuracies) | the queue ruling, page 5 (the band); the repairs method note at `882f252`, section 5 (the formula and the 0.10); the Gate C rulings, RT-223 |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). It ran in three parts, all at toy scale on the laptop
except one item: the rehearsal of 2026-09-21
(`docs/2026-09-21-successor-measure-rehearsal.md`, code in
`experiments/rehearsal-successor-measure/`, re-run from code on 2026-09-22
with the separable arm reproducing exactly and the other two not); the
repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at `882f252`,
code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`, checked at `d216dbc`); and the re-run of 2026-09-26 under this
version's rules (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, code
`src/rerun_v3.py`, outputs `out-v3-rules/`, checked at `70be9fb`). The one
part that spent money is item R-11. Total spent on the rehearsal so far:
about $0.57, the sum of the compute ledger's three slice rows, of the
rehearsal line's $10 (item 10 of the 2026-09-21 ruling; section 12.3).

**The models every toy result rests on.** The fifteen trained toy models
behind the repairs and the re-run (arms T, C, F and M and the ownership-blind
solver, three seeds each) are committed at
`experiments/rehearsal-successor-measure/out-repairs/models/` with their
`SHA256SUMS` list and a `README.md` (main line at `8038275`, pull request 64),
because they cannot be rebuilt from code and seed (the repairs check at
`d216dbc` retrained from clean and got different nominations) and an
uncommitted record the reader cannot open is the form of ledger item RT-145.
The re-run's fingerprint check compared three recorded hashes per file with
that list and found all fifteen agree, and its check hashed the stored files
themselves and found the same (MEASURED: `out-v3-rules/models_sha256_check.json`,
`all_agree: true`; the check at `70be9fb`, section 2.1). **What rests on
them:** every base-recipe result of the repairs (`gate_base.json`,
`nominate_base_*.json`, `measure_base_*.json`, `summary_base.json`, the
training records `train_*_base_seed*.json` and the `F/base/*` rows of
`diagnose_named_other.json`), the whole of `out-v3-rules/`, and every toy
figure in sections 3, 5, 7, 8 and 9 of this version. **What rests on models
not committed at the time of writing, named so nothing is stepped over:** the
two training-redesign results of section 4.4 (the curriculum and the loss
re-weighting, 0 of 3 seeds each), which rest on six further free-arm models
still untracked in the repairs worktree; the grammar attempt of section 4.4
(774, 730 and 759), which rests on its own nine models, untracked in its
worktree; the grammar check's and the repairs check's re-run figures, which
rest on models those sessions trained and did not commit; and the rented
slice's seconds per step (section 9), whose timing model exists on the record
only as a checksum (the check at `70be9fb`, section 2.2). None of those
figures is a reading of the measure; each is a gate count or a timing, quoted
as such. Whether those fifteen further files get the same treatment is put to
John as decision 22.

**A pre-stated quantity the rehearsal never exercised is a fatal finding on
its own** (item 5 of the 2026-09-21 ruling). Each item below therefore says
what exercised it.

- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  The four matched properties hold (P-1). The own-directed condition learns on
  every arm. **The named-other condition does not clear the bar on the free
  arm on a majority of seeds, under any of three training recipes or under
  the grammar change, and does not clear it on arm C on any seed** (760, 751
  and 708 of 3,000; section 4.4 and section 5.2). Stop condition S1 is ruled
  not to have fired; fallback (d) registers; the constructed arms are gated on
  the own-directed condition only. *Exercised; the finding is the honest
  prior, measured.*
- **R-2. Arm T is constructible and its ownership slot is transplantable on
  its own, and so is arm M's separable route.** The blind nomination finds
  arm T's slot without being told where it is, on every seed, and reads
  0.0000 under the registered rule and under the stricter variant; on arm M
  the blind subspace's ownership-only transplant moves 0.37 to 0.41 of trials
  against random medians of 0.015 to 0.019 (the re-run findings at `9d9d31a`,
  Part 1, sections 1.3 and 1.4). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction, and arm M's mixture reads between the anchors in its
  pre-stated band.** No nominated subspace reproduces the counterfactual on
  arm C while the whole state does: its reads fit at 0.961 or better and its
  ownership-only transplant lands at or below the no-transplant rate, so it
  reads 1.0051, 1.0025 and 1.0000; arm M reads 0.4886, 0.4860 and 0.5449
  against a band of 0.3 to 0.7 (section 5.3). **Arm C fails the named-other
  condition on every seed and passes its gate on the own-directed condition**
  (section 5.2). *Exercised under the registered rules; the two-arm fallback
  does not fire.* The check of arm M's reading against its true-slot reading
  at the registered site sets is owed with the re-run of R-1 to R-6 before
  Gate A (section 5.3).
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1; and arm T seed 0 on the grammar attempt's unseen pool, at
  −0.1870), above one (arm C at 1.0051), and no verdict (arm F on every seed,
  by the gate and by the fit floor; control 2 on the arms that have not
  learned the named-other condition). *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised.*
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the whole-state floor (the smallest toy denominator under
  the registered rule is 0.4263, arm F seed 0; section 17, failure 1); the
  no-transplant formula was checked against nine arm-and-seed pairs on
  2026-09-21 and twelve on 2026-09-25; two made-up systems of equal true share
  and unequal transplant strength read the same under the registered form
  (section 6.3). *Exercised.*
- **R-7. Throughput, per arm, projected to dollars.** Done from item R-11's
  measured ratios on the lifetime-priced cost of a registered-size run
  (section 12.4). *Exercised for arms T, C and F; arm M's runs are priced from
  ledger rows.*
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant leaves every logit bit-identical on every arm and seed; the
  ownership-only transplant is proved a restriction of the whole-state one;
  a transplant on arm T moves the action to the donor's value. *Exercised*
  (with the citation gap of section 7.3, item 7, that the null transplant was
  run at the first pass's site sets).
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 1.0025 and 1.0000 under
  the registered rules on 2026-09-26. *Exercised.*
- **R-11. Seconds per step on the rented machine, all three arms, and the
  shutdown path against the real vendor.** Measured on 2026-09-25 on the
  second attempt at the rented slice, after a first attempt that hung and was
  stopped with neither measurement taken (`docs/2026-09-25-rented-slice-findings.md`,
  main line). Throughput: **PASS**, three figures with their spread, fetched
  home (section 9), checked character for character against the launcher's
  log (the check at `afb5183`, point 5). The shutdown handshake: **the laptop
  half passed against the real vendor, copy, checksum, receipt written,
  delete, confirmed gone, and the machine half was not exercised**, because
  the laptop deletes the machine in the same second it writes the receipt, so
  the machine's own "receipt found" can never be observed on the normal path
  (MEASURED and ARGUED: `docs/2026-09-25-rented-slice-attempt-2-findings.md`
  at `9f802db`, section 4; the check at `afb5183`, points 7 and 8). None of
  the slice's six pre-stated handshake lines fits, and the findings do not
  force one. **Two things this leaves open, put to John in section 15**: fifty
  timed steps were run where the item says five hundred (decision 17), and
  the machine half of the handshake is still untested (decision 18). Cost:
  about $0.57 across three rows against the item's $3 (section 12.3).

**What happens next.** This version goes to its Gate C tier 1 review, with
the route (b) search's check cited by number once it lands; John rules on
section 15; rehearsal items R-1 to R-6 are re-run once more on the registered rules
to refresh the control figures of section 7.3 and the arm M true-slot check
of section 5.3 at the registered site sets; the registration text (version 4,
with every frozen number and the printed site list) goes to Gate A, both
tiers; the registration commits when both tiers are answered and he rules.
There is no target date; the only date is the kill date of 2026-10-18
(section 11).

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. Gate C tier 1 on this version → John's rulings on section 15 → the route
   (b) search's check read against section 7.2, item 1, and its figures
   annotated if the check moves one.
2. Registration text (version 4) with every frozen number and the printed site
   list → **Gate A, both tiers** → registration commit. **No target date.
   Kill date 2026-10-18**, past which committing it takes a fresh ruling
   naming what comes off the back end (item 23 of the 2026-09-21 ruling).
3. Implementation frozen; unit tests; the even-split rule and the
   one-scored-token self-test run on the built generator; the training entry
   point for arms T, C and M on the rented machine written and named in the
   registration (section 5); the tripwire of section 12.5 written into the
   launch preconditions beside the sleep guard and the argument guard (the
   queue ruling, page 6, "Changes").
4. Development runs at the 10-million size, **four arms, one seed each,
   including arm M, from the first release's development line (ruled, the
   Gate C rulings, RT-229)**. **This is a pipeline and throughput check, not a
   learnability verdict**: the 10-million size failed to learn the earlier
   design's task, so a null here means nothing about the registered size, and
   the registration says so in advance. It is also the first time arm M's code
   runs on the rented machine (weakness W9).
5. **The staggered launch, in two steps, as ruled 2026-09-21** (item 12 of
   that ruling; steps 5a and 5b of the roadmap chain).
   - **5a. One arm F run at the registered size launches first**, on John's go
     naming it, inside the first release (section 12.3). Three things come
     back before anything else launches: whether it passes the learn-both
     gate; what the machine actually bills (the tripwire, section 12.5); and,
     **new (John's ruling of 2026-09-26 on the route (b) result, section 7.2,
     item 1), the nomination fit of that run's ownership read on development
     episodes, reported against the four-fifths floor**. If it fails the
     gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches. **If the read misses the fit floor, that is a
     stop before the second release draws, beside the learn-both stop**: it
     goes to John as a registered-size "no verdict, read failed its floor" on
     one seed, and whether the remaining runs are worth the second release is
     his call with that figure in hand (section 3). The fit is computed on the
     laptop from the fetched checkpoint, as the toy nominations were, and
     draws no rented time (ARGUED: a 30-million-parameter model's activations
     on development episodes fit on the laptop; if that turns out not to be
     so, the cost goes into the first release's rehearsal line and is said).
   - **5b. The remaining eleven registered runs**, two more of arm F, three
     each of arms T, C and M, launch only after 5a's learn-both result is
     read and its billing found normal, the second release is asked for and
     ruled, and John gives the go. **Kill date 2026-11-01 binds this step, not
     5a** (item 23 of the 2026-09-21 ruling): past it, launching takes a fresh
     ruling naming what comes off the back end.
   - **What a constructed arm's failure costs under this order, stated (ruled,
     the Gate C rulings, RT-213, items 2 and 3).** Step 5a tests arm F only.
     Arm C, the high anchor, is first trained at the registered size in step
     5b, after the second release, about $119 on the ruled split plus arm M's
     runs (section 12.4), has been drawn. On the toy, arm C is the arm that
     fails the named-other condition on every seed; under this version's gate
     that failure would not fire an R3 (section 8.1), but a failure of arm C's
     *own-directed* condition at registered scale, or an arm C whose
     construction did not hold (weakness W3), is seen only after both releases
     are drawn, and an R3 or a two-arm fallback caused that way costs the
     whole successor, about $194 to $206, not the first release's $44. John
     ruled against an extra arm C run inside step 5a: at $422 to $434 of $450
     the envelope has no room, and if he later wants the anchor's construction
     proven at registered scale before the second release, that run needs the
     ceiling revisited.
6. Nomination on development episodes as arm F checkpoints arrive, with the
   fit floor applied and printed; frozen and committed; transplants on fresh
   episodes, all arms. The measure computed on arms T, C and M: that is the
   validation result.
7. **Gate B** on the validation. John rules: read arm F, or close on R2 or R3.
8. If R1: arm F read on the frozen procedure, confirmation seeds; findings;
   Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
   state the chain is in.

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). **Ruled on 2026-09-25 not to have fired** (the
  queue ruling, page 4): the separable arm learned both conditions to 1.0000
  and the transplanting code passes. The named-other failure on the free arm,
  and now on arm C too, is fallback (d), on the record in section 4.4, not S1.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded. At toy
  scale R-3 passed under the registered rules.
- **S3.** The rehearsal fails item R-4 or R-6. The measure is not registered.
  At toy scale both passed.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the
  whole first release, which since item 19 of the 2026-09-21 ruling includes
  the re-run (section 12.3). (Version 1 stated this outcome's cost two ways;
  the Gate C review of version 1, finding RT-178, caught it, and item 19
  removed the gap.)
- **S4a (new, John's ruling of 2026-09-26).** The staggered first registered
  run passes the learn-both gate but its ownership read misses the fit floor
  on development episodes. Not an outcome on its own: a stop before the second
  release draws, with the registered-size fit reported to John against the
  floor and its permutation null, and nothing else launches until he rules.
  About $44 spent at most, as for S4.
- **S5.** Cumulative actual spend reaches the release John has authorised,
  about $44 for the first release (section 12.3), until and unless he rules on
  the second. Work stops regardless of state; what is unrun is reported as
  unrun, and nothing launches against a release that has not been ruled.
- **S6.** A kill date passes: registration not committed by 2026-10-18, or
  the remaining runs of step 5b not launched by 2026-11-01. **Launching or
  registering past the date needs a fresh ruling that names what comes off the
  back end to make room** (item 23 of the 2026-09-21 ruling); nothing is
  written off automatically and nothing slips past unremarked. R4 is where
  the roadmap lands only if that ruling says it is not worth it. There is no
  2026-10-11 target: version 1 carried one, and item 23 leaves the schedule
  with the two kill dates and nothing else.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**:
  missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over (item 15 of the 2026-09-21 ruling; section
  12.7). Control 2's *not applicable* on arms T and M is not an instance of
  this: it is a ruled disposition with the reason on the record (section 7.3).
  Nor is a *no verdict* under the fit floor: that is a registered outcome of
  the procedure with its reason printed.
- **S9.** **The tripwire trips**: either billing ratio of section 12.5 at or
  above 1.25 on any machine of a wave, or a check that cannot run. **The wave
  halts, not trims** (section 12.5), and it goes to John with the ledger row
  beside the estimate.

---

## 12. Spend: rebuilt from the compute ledger, and the two releases as ruled

*Every dollar figure in this section is read from
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` (the
programme's system of record for money), from the dated note beside the
spending proposal that recomputed the second release, or from a ruling that
quotes the ledger; the row or note is named beside each figure. Nothing here
is a request, and nothing here releases money: John's process does that, run
by run, with his own words quoted in the ledger row before anything is
created.*

### 12.1 Where the money stands

| | | Source |
|---|---|---|
| Programme ceiling | **$450**, raised from $400 on 2026-09-25 | the compute ledger's ceiling note of 2026-09-25 at the top of the file, recording the queue ruling's page 6 ("The envelope") |
| Spent across the programme, as of the last row on the main line | **about $228.15** | the ledger's second 2026-09-25 row (line 95), the rented slice's second attempt, "After this run"; on the main line since `9f802db` |
| Amendment A3 against its $100 stop | **about $46.75** | the same row |
| The rehearsal line of the first release, spent | about $0.02 (2026-09-21), about $0.50 (first attempt), about $0.05 (second attempt); **about $9.43 of $10 remains** | the same row; the check at `afb5183`, point 3, confirms the $0.0525 against the two balance readings and the vendor's posted billing row |
| Headroom before the successor's two releases | **about $221.85** | $450 minus about $228.15, arithmetic on the two rows above; not a figure the ledger states |

Version 2 carried these figures from an unmerged branch; they are now on the
main line, unchanged. No ledger row has been written since.

### 12.2 What is ruled, and what this section is built to

- **The flat $130 cap of 2026-09-20 is superseded** by the two releases of
  the 2026-09-21 ruling (items 10, 11 and 19 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, with
  its correction note of 2026-09-22: about $44 and about $131). That sentence
  is the closure of the Gate C review of version 1's finding RT-176 (the
  $175-against-$130 finding), and a dated annotation goes beside item 4 of the
  2026-09-20 ruling (the queue ruling, page 6, part 1).
- **The envelope is $450** (the queue ruling, page 6, part 2, recorded in the
  compute ledger's ceiling note of 2026-09-25). What it was ruled to buy, on
  the ledger rows the packet cited: the base plan of about $175 on top of
  about $227.63 spent, plus one extension of $32 to $44 (arm M) or about $36,
  with $3 to $15 left. It does not hold two extensions. The measured figures
  below leave more room than that arithmetic did.
- **The first release's development line covers four arms, not three (ruled,
  the Gate C rulings, RT-229).** This widens item 10 of the 2026-09-21 ruling,
  which covered three; the reason recorded is that arm M's code has never run
  on the rented machine, so its development run belongs in step 4 with the
  others, before the second release. Version 2 had costed that run twice, once
  in each release (the Gate C review, RT-229); this version costs it once, here.
- **The second release is asked for only after seconds per step were
  measured on the rented machine** (item 11 of the 2026-09-21 ruling). They
  were, on 2026-09-25 (section 9). The ruling changed the ceiling, not that
  gate.
- **The staggered launch** (item 12), **halt not trim** (item 13), **funding
  per wave** (item 14) and **a check that cannot run is a trip** (item 15) all
  stand; sections 11, 12.5, 12.6 and 12.7.
- **The pre-authorisation scheme** of `docs/preauthorised-spending-proposal-2026-09-21.md`
  **is not adopted** (the queue ruling, page 6, part 3). Only its tripwire is.

### 12.3 The first release: about $44, ruled 2026-09-21, with a four-arm development line

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| The rehearsal | Tiny models, the transplanting code, rehearsal items R-1 to R-11, including the rented slice | item 10 of the 2026-09-21 ruling: up to $10. Spent so far: about $0.57, the sum of the ledger's three slice rows (about $0.02 on the 2026-09-21 row, about $0.50 and about $0.05 on the two 2026-09-25 rows), leaving about $9.43 by the last row's own running line | up to **$10** |
| Development runs | **Four arms, one seed each**, at the 10-million size: pipeline, self-tests, throughput, and arm M's first run on the rented machine | item 10: up to $10 for three arms, **widened to four by the RT-229 ruling**. The ledger's reconciliation of 2026-08-12 trues the earlier 10-million run up to $1.943 (lines 393 and 400), so four such runs are about $7.77 of the $10 line (MEASURED: section 17, candidate 7) | up to **$10** |
| One free-arm run at the registered size | Step 5a of section 11 | item 10: about $12. The lifetime-priced cost of a registered-size run is $10.04 (the ledger's 2026-09-17 row, line 88: 20.28 pod-hours at $0.99 for two runs, computed from measured pod lifetimes and not balance-confirmed, as the row itself says; the Gate C rulings, RT-226) | about **$12** |
| The one permitted re-run | If step 5a fails the learn-both gate | **item 19: folded into the first release**, at the same planning figure | about **$12** |
| **First release, total** | | | **about $44** |

This is the release John has authorised; nothing beyond it is launchable
without the second. Stop conditions S4 and S5 in section 11 are stated
against it.

### 12.4 The second release: from the measured seconds per step, then arm M's three runs

**What the second release is bound to, and now has.** Item 11 bound it to
rehearsal item R-11's measured seconds per step for arms T, C and F on the
registered venue. Those were measured on 2026-09-25 (section 9), and the
dated note beside the spending proposal recomputed the release from them
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
at `9f802db`; checked at `afb5183`, point 6, where the script's re-run is
byte-identical to its committed output). The method, in the note's own words,
is MEASURED arithmetic on an ARGUED method: the measured seconds cannot be
turned straight into hours for a run (a timed step holds 1,792 tokens where a
registered step held about 10,624, and a real run also generates its data,
evaluates and saves), so the note does what version 1's spending arithmetic
did, with the measurement in place of the inference: **the lifetime-priced
cost of a registered-size run, $10.04 (the ledger's 2026-09-17 row), times
each arm's measured ratio.** Every figure below is the note's, printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
into `second-release-arithmetic.txt` beside it.

| Per run | Version 1's planning figure | From the measurement |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** (ratio 1.044) |
| Arm C | $12 | **$10.84** (ratio 1.080) |
| Arm M | (none: arm M is new in version 2) | **not measured**; priced from ledger rows below |

| Item | Version 1 (provisional) | From the measurement (the note's table) |
|---|---|---|
| The remaining eight registered runs of arms T, C and F (two F, three T, three C) | $96 | **$84.06** |
| One permitted re-run, priced at the dearest arm (C) | $12 | **$10.84** |
| Transplanting and measurement on fresh episodes | $12 | $12.00, unchanged: not a throughput line |
| Billing-anomaly and idle-billing margin | $23 | $23.00, unchanged: not a throughput line |
| **Second release, before arm M** | **$143** | **$129.90** |
| **Both releases, before arm M** (the note's first release of about $32) | $175 | **$161.90** |

**How this reads against the ruled split.** The note's table keeps the
permitted re-run inside the second release and pairs it with a first release
of about $32, which was the split on 2026-09-21 when the note's method was
written. Item 19 later moved the re-run into the first release (section
12.3), so the same money as ruled is **about $44 plus $119.06** (the second
release without its re-run line: $84.06 + $12 + $23), about $163.06. The
$1.16 between the two totals is the re-run at the $12 planning figure in the
ruled first release against $10.84 on the measured method; it is a matter of
which release the re-run sits in and at which price, not of how much money
there is. **$161.90 is the figure this section carries for both releases
before arm M**, as the note computed it.

**Then arm M's three registered runs.** Arm M's ruled allocation is **$32 to
$44** (the queue ruling, page 5, and page 6's envelope; the repairs rulings,
item 2), from the ledger's per-run rows rather than from item R-11, because
arm M was not timed on the rented machine. That range is: three runs at what
the last three clean runs billed (about $29.70 to $30.12), or $36 at the
planning figure, or up to about $41.76 if each billed as the 2026-09-15 pilot
did with its idle time, **plus about $1.94 for one development run at the
10-million size** (page 5 of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`,
from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and 2026-08-12 rows).
**The $1.94 comes out of this section (ruled, the Gate C rulings, RT-229):**
it is paid from the first release's four-arm development line and launched in
step 4, so this section carries the three registered runs only, **about $30
to $42**. The ruled $32 to $44 stands as the allocation John ruled; moving its
development run between releases changes which release pays and when, not
how much money there is. Arm M's runs are in the second release (the repairs
rulings, "What this changes": section 12.4).

**The whole successor, and the programme after it.** Arithmetic on the
figures above; no ledger row states these totals.

| | |
|---|---|
| Both releases before arm M | about $161.90 |
| Arm M's three runs | about $30 to $42 (the ruled $32 to $44 less its $1.94 development run, now in the first release) |
| **The successor, all in** | **about $192 to $204** on the note's split; about $193 to $205 on the ruled split |
| Spent before it | about $228.15 |
| **Programme after the successor** | **about $422 to $434 of $450**, stated as a range: the repairs rulings' annotation 2 gives it in these words on the note's split with arm M at $32 to $44 (MEASURED: section 17, candidate 7, prints $422.05 and $434.05); on the ruled split with the $1.94 moved into the first release it is about $421 to $433 |
| **Left** | **about $16 to $28** on the note's split; about $17 to $29 on the ruled split with the $1.94 moved; **$14.79 at the least**, on the ruled split with arm M at its ruled top of $44 (the Gate C review, RT-217) |

**The second release is asked for on these figures or not at all**, and the
request carries the measured figures beside the provisional ones so the
movement is visible. Two things that could still move it, stated so they
cannot arrive quietly: the first free-arm run of step 5a gives arm F's own
run cost, and the eight later runs of arms T, C and F are to be repriced from
it before the second release is drawn (the note's "what this does not
settle", item 2); and arm M's per-run cost is a ledger inference until a run
of it exists. Arm M is priced at arm F's per-run figures although it carries
both arm T's slot and arm C's entangling, whose measured ratios are 1.044 and
1.080; at arm C's ratio the lower end of its three runs would be about $32.52,
which the range still covers (the Gate C review, "The arithmetic of both
releases"; ARGUED there).

### 12.5 The tripwire: 1.25, halt not trim, with the in-flight clause

**Adopted on 2026-09-25** (the queue ruling, page 6, part 3), from sections
5.3 and 5.4 of `docs/preauthorised-spending-proposal-2026-09-21.md`, whose
pre-authorisation scheme is not adopted. Two ratios are measured, because the
authoritative one is slow and the fast one is rough:

- **Ratio A, authoritative: billed hours divided by machine-existence hours**,
  per machine, from the vendor's own billing rows: the quantity rule 4 of the
  compute ledger already reconciles at phase boundaries, and the one the
  2026-08-08 anomaly was recorded in (8.47 billed against 2.42 existed; the
  figures are at the ledger's 2026-09-21 row, line 93, and its note at line
  423, both describing the 2026-08-07/08 row, which itself carries neither
  number; the Gate C rulings, RT-226).
- **Ratio B, fast: account-balance drawdown per elapsed hour, divided by the
  posted hourly rate times the number of machines running**, from the balance
  query the ledger already uses, available within minutes of launch.

Both are measured against the posted rate read from the machine's creation
record, not remembered. **Either ratio at or above 1.25 is a trip.** When it
trips:

1. **Halt, not trim.** No further machine is created. The wave stops; nothing
   else launches (item 13 of the 2026-09-21 ruling replaced the roadmap's seed
   fallback with this, on the arithmetic that a trimmed plan at the anomalous
   rate still spends about $326, more than the programme has).
2. **A machine already in flight is left to finish only if** its projected
   total is inside its estimate times the measured ratio and the funded balance
   covers it, the spending proposal's own clause (its section 5.4, item 2):
   killing a running machine forfeits its checkpoint, but if the projected
   drawdown would exhaust the funded balance before the checkpoint and its
   finished-marker are written, the machine is deleted and the run written
   off. That is arithmetic, not taste.
3. **The ledger row is written first**, with the measured ratio, both hours and
   the balance reading, before anything else happens.
4. **John is told the number**, and every later launch needs his own words.
5. **A check that cannot run is a trip** (item 15 of the 2026-09-21 ruling;
   section 12.7).

The tripwire is written into the launch preconditions beside the sleep guard
and the argument guard (the queue ruling, page 6, "Changes"); that is code
work owed before step 4 of section 11, and not done by this document. **It
does not exist as code yet, so by failure 6's own standard it is untested
until it has met the real billing rows** (the Gate C review, failure 6). It
runs in flight, hourly, on ratio B from the first hour of the first machine;
before the second machine of any wave is created; and at each wave boundary
on ratio A, reconciled to the ledger.

### 12.6 The account is funded per wave, not per release

Unchanged from version 1 and from item 14 of the 2026-09-21 ruling: the rented
account is prepaid with automatic reload off, and **topped up to the estimate
for the wave about to launch plus $20, and no further**, so that no anomaly of
any size can cost more than that, because there is nothing else in the account
to spend. This is the only control in the programme's history that held when
everything else failed (2026-08-12). The vendor balance stood at $75.8645 on
2026-09-26T01:54Z (the ledger's second 2026-09-25 row, line 95; the check at
`afb5183` read $75.864512286 at 01:54:04Z), which is above what step 5a's
estimate plus $20 would call for; the rule caps what is topped up, not what
is already there.

### 12.7 A check that cannot be run counts as a trip, not a skip

Item 15 of the 2026-09-21 ruling, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate, a stop condition or a tripwire check cannot
be evaluated (the data is missing, the code will not run on the artifact, the
measurement was never taken, the balance query returns an error), **the check
counts as failed and its consequence fires.** It is never recorded as not
applicable and stepped over, and it is never deferred past the launch it was
supposed to gate. Written into section 11 as stop condition S8 and into the
tripwire as its fifth line.

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used. **Version 1's
wager, that the rehearsal measures a per-run cost at or below the $12
planning figure, survives on the 2026-09-25 measurement: the dearest timed
arm is $10.84** (the note at `9f802db`). **The wager this version makes, on
the ruled split and against the full range (ruled, the Gate C rulings,
RT-217):** the twelve registered runs, with arm M's three priced from ledger
rows at the top of their ruled range, complete inside the $450 envelope with
three seeds on every arm carried and **at least $10 left**. On the ruled
split, $44 plus $119.06, with arm M at its ruled top of $44, the plan leaves
$14.79, and with arm M's three runs at $41.76 and the $1.94 moved into the
first release it leaves $17.03; both meet the floor (MEASURED: section 17,
candidate 7). Version 2's $16 floor was already lost at the top of the range
on the ruled split (the Gate C review, RT-217), which is why the floor is
now $10. If measured spend approaches the second release's ruled figure with
runs missing, **the report is the shortfall, never a second raise.**

---

## 13. What this cannot claim, and its weakest points

The Gate C brief asks what a result will be read as claiming beyond what it
measures. Answering it before the reviewer does.

**W1. The constructed arms differ in more than their degree.** They differ in
architecture, in parameter count within the size band, in how they route
information. Anything that separates them is confounded with degree. What the
arms establish is that the measure moves in the right direction between a
system built to be separable, one built as a mixture and one built to be
entangled; they do **not** establish that the measure responds to integration
and to nothing else. Consequently arm F's reading is "where arm F sits against
three constructed anchors on this measure", and never "arm F's integration is
*d*". The public sentence in section 8 of the December-result roadmap already
carries this hedge, and the recommendation is that the hedge is not loosened
at any later point. This is the deepest weakness in the design and it is not
removable by anything affordable.

**W2. The reading is relative to the site set, and the arms cannot be read
at the same site set.** A different frozen site set could give a different
number. Mitigated by one pre-stated rule applied identically to every arm, and
by saying in the registered text that the reading is the degree *at the sites
this procedure nominates*. The rider makes the second half of this weakness
visible rather than hidden: at arm T's site set, arms C, F and M return no
verdict on the toy, for two different reasons (section 7.2, item 7), so what
differs between arms is first of all where the procedure has to look.

**W3. Arm C's degree was an intention until the rehearsal showed otherwise,
and the toy is not the registered model.** At toy scale no nominated
subspace carries the counterfactual on arm C, although its reads find the
label at 0.96 or better (section 5.2). A network built with ownership
multiplied into every layer could still, at 30 million parameters, learn to
concentrate it in a low-rank direction, in which case arm C's anchor
collapses into a second copy of arm T. The registered-size nomination is the
test, and its failure fires the two-arm fallback rather than a repair; under
the launch order that failure is seen only after both releases are drawn
(section 11, step 5b).

**W4. The whole-state transplant may fail for arm C at the registered size.**
If ownership in arm C is spread across layers the site-set rule does not
cover, no site set clears the floor and arm C returns no verdict: honest, but
it leaves the experiment with no high anchor by another route. The rule of
section 7.2 covers every contiguous layer set precisely to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is that arm F fails its gate or returns no
verdict, and both are now measured at toy scale, not predicted.** Sections
3, 4.4 and 5.4. The staggered launch makes a gate failure on arm F cost the
first release, about $44, instead of the whole wave, and since John's ruling
of 2026-09-26 on the route (b) result the same is true of a read that misses
the fit floor: the first release's single arm F run is the test of both, and
either miss is a stop before the second release draws (section 11, step 5a).
The route (b) search found no label the free system carries at the floor at
toy scale (section 7.2, item 1), so the registered read is the ruled one and
the honest expectation is that this stop may fire. John's present view is that
a registered "no verdict on the free arm" is worth the second release (the
Gate C rulings, RT-212, item 3); the stop lets him make that call with the
registered-size fit in hand.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text; decision 9.

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. **On the toy, before this version's
rule, six of the nine nominations on arms C, F and M sat at the injection:
layer 0 at the post-identity position set, which spans exactly the turns the
channel fires on** (MEASURED: the Gate C review, RT-216; the re-run findings
at `9d9d31a`, Part 2, first pass, section 6.2). Version 2's claim that the
other arms' nominated sites were downstream of the injection was false and is
struck (ruled, the Gate C rulings, RT-216, item 2). What now mitigates the
weakness: layer-0 site sets are removed from the candidate family at every
position set spanning the acting turns (section 7.2), and the rule chooses
again; under that rule every toy nomination on arms C, F and M sits at layer
1 or later; the stricter variant, layer 0 removed everywhere, is reported as
a sensitivity row so that the one remaining layer-0 nomination, arm T's at
the action position, can be compared with its layer-1 alternative (0.0000 on
both). The rider, control 2 on the arms it can run on, and the honest gap
between the lesion result and the transplant result do the rest. What the
rule does not do: it does not show that a layer-1 nomination is anything
other than the channel's trace one block on; that is what the fit floor and
control 3's distribution are reported for.

**W8. The per-run cost is measured for three arms and inferred for the
fourth, and the measurement is fifty steps, not five hundred.** Section 12.4
prices arms T, C and F from the 2026-09-25 measurement and arm M from ledger
rows. Item R-11 as written asks for five hundred timed steps per arm; the plan
John authorised timed fifty, and the spread was tight (each arm's slowest
step within 3% of its median; the check at `afb5183` recomputed arm C's at
2.9%), so the ratios are unlikely to move much with a longer window; that is
argued, not measured (the slice findings at `9f802db`, section 3). Decision 17.

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor, and arm M's code has never run on the rented machine.** The
laptop half has (section 10, R-11). On the normal finishing path the laptop
deletes the machine the moment it writes the receipt, so the machine's own
"receipt found" is close to unobservable by construction; the watcher is a
backstop for a laptop that never answers, not a tested primary. Twelve
registered runs inherit that. **Beside it (ruled, the Gate C rulings,
RT-228): arm M's code, `experiments/rehearsal-successor-measure/src/arm_middle.py`,
has run only on this laptop; the rented slice timed arms T, C and F only, and
no training entry point for arms T, C or M exists on the rented machine yet.**
By failure 6's discipline both are untested until they have met the far end;
step 4 of section 11 is where arm M first does. Decision 18 puts the two ways
forward on the handshake to John.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. Control 6 says the whole-state transplant carries more than identity
on the entangled arms.** On the relaxed set, at the site sets the repairs run
nominated, the same-value cell moved on arms C and M where a transplant that
moved only who is acting would move nothing (section 7.3, item 6; the figures
there were taken before the registered site rule and are owed again from the
R-1 to R-6 re-run). On those arms the reading cannot be read as purely a
statement about where the ownership answer lives. It is reported as the
caveat it is, on every arm, in the reporting table.

**W12. The fit floor tells an empty instrument from a ceiling; it does not
tell an entangled act from an ownership answer the read did not find.**
Section 3's residual admission. A read that clears the floor shows the label
is in the state at those sites; a reading near 1 with such a read shows the
directions the read found do nothing on their own; that the act's ownership
answer is carried by directions the read did not find, at sites the rule did
not nominate, is not excluded by anything in this design. The rider, the
sensitivity rows and control 3's distribution make that visible; they do not
remove it.

---

## 14. What this does not change

- **The programme ceiling of $450**, ruled 2026-09-25 and recorded in the
  compute ledger's ceiling note of that date. This document asks for no
  change to it and proposes none.
- **The corrigibility commitments** (`spec/corrigibility-commitments.md`,
  version 1.1): John authorises every run and his go is quoted word for word in
  the ledger row; every run is killable; no stakes term; checkpoints are not
  promotable; optimisation against the instruments halts the run. All four
  arms are episodic and floor-only: no state kept across episodes, no
  maintained boundary, no stakes. Nothing here pre-authorises a larger build.
- **The claim rule.** Nothing produced by this experiment is reported as a
  conscious machine, and every positive is bounded at "non-zero on the
  gradient", per the standing limits in `ROADMAP.md`.
- **The closure of Amendment A3.** It closed as *not testable* on 2026-09-25
  and this experiment does not reopen it. The closed design's checkpoints are
  not transplanted: their grammar has no matched comparison condition and
  their target was never localised.
- **The outside-review protocol's gates, its closure rule, the pairing rule
  and the failure-mode pass.** This document passes through them; it does not
  amend them. Its failure-mode pass is section 17.
- **The grammar of section 4.** The grammar attempt did not clear, so the
  grammar, the training recipe and rehearsal items R-1 to R-6 stand as
  version 2 had them.
- **The dates.** Registration by 2026-10-18 and the remaining runs of step 5b
  launched by 2026-11-01, each a kill date in the sense of item 23 of the
  2026-09-21 ruling (a fresh ruling to go past, never a quiet drift); wrap-up
  starting 2026-12-21; the hibernation condition complete by 2027-01-04. No
  2026-10-11 target.

---

## 15. Decisions for John

Each with how confident the recommendation is, whether it is ordinary practice
or a judgment call, and the strongest alternative, so nothing is inherited by
default. Version 2's nineteen are kept under their numbers; the ones ruled
since are marked so and carry the ruling; three new ones follow.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references; on arm M the true-slot reading and the formula of
   section 5.3 are one check (the Gate C rulings, RT-223).

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Confidence: high. Judgment call. Not yet ruled.* **Alternative:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for: a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Confidence: moderate, raised by the toy result of section 5.2, where its
   reads find the label at 0.96 or better and the subspace still does
   nothing. Judgment call. Not yet ruled.* **Alternative:** train arm C with a
   penalty that punishes any linearly transplantable ownership direction,
   which trains the system against the very instrument that will measure it.
   Recommended against.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Confidence: high. Standard practice for intervention comparisons.
   Not yet ruled.* **Alternative:** transplant the whole forward state at every
   layer as the denominator, which always succeeds and turns the measure into a
   report on how the sites were chosen.

5. **The registered reading is the chance-corrected form, with the raw
   difference and both accuracies reported alongside, always, plus the floors
   and the no-verdict rules.** *Ruled 2026-09-25 (the queue ruling, page 2);
   the fit floor added 2026-09-26 (the Gate C rulings, RT-212).*

6. **Three seeds per arm.** *Ruled 2026-09-25 (page 1f).*

7. **The money goes in two releases.** *Ruled 2026-09-21 (items 10, 11 and 19)
   and 2026-09-25 (the queue ruling, page 6); the development line widened to
   four arms 2026-09-26 (the Gate C rulings, RT-229); section 12 is built to
   them.* The one number John should see before it can surprise him: the
   programme after the successor is about $422 to $434 of $450, and on the
   ruled split with arm M at its ruled top the plan leaves $14.79, against the
   wager's $10 floor (section 12.8).

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. *Confidence: high.
   Standard practice. Not yet ruled.* **Alternative:** number it as a further
   amendment, which keeps one budget instrument and one ledger but attaches
   new work to a closed registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Confidence: high. Judgment call. Not yet ruled.*
   **Alternative:** add a condition in which the model's own name appears as a
   token, which would match the conditions exactly and would put an ownership
   cue into the text. Ruled against here; John's call. *The grammar attempt of
   section 4.4 did not clear, so this decision is put with the grammar as
   version 2 had it.*

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Its shape is ruled (page 1h),
    and its two-of-three clause (the Gate C rulings, RT-220); the standing as
    a precondition and not a finding is version 1's recommendation and not
    yet ruled. Confidence: high. Standard practice, and the closed design's
    own registered wording.*

11. **The registered wave launches staggered**: step 5a, then 5b. *Ruled
    2026-09-21 (item 12), with item 23 settling which step the second kill
    date binds; the fit-floor stop added to step 5a by John's ruling of
    2026-09-26 on the route (b) result.*

12. **This proposal goes to Gate C tier 1 before John rules on the open items
    above**, per the protocol. *Confidence: high. Standard practice here.*

13. **The successor's registration names a launcher that waits for the
    receipt, and makes "the trainer does not delete its own machine" part of
    the registered recipe.** *Confidence: moderate. Judgment call. The launcher
    file is now named (section 5; the Gate C rulings, RT-228); the rest is not
    yet ruled, and now with the vendor result in hand*: the laptop half of the
    handshake works against the real vendor and the machine half was never
    given the chance (section 10, R-11). **Alternative:** leave the shutdown
    policy in unregistered operations scripts, where a later edit can quietly
    remove it. (Version 1's account of what one failure cost merged two events;
    the Gate C review of version 1, finding RT-186, corrected it, and the
    sentence is not repeated here.)

14. **What a no verdict maps to** (the Gate C review of version 1, finding
    RT-182, still open; sharpened by the RT-212 ruling, under which a no
    verdict on arm F is a registered possibility). Recommendation: a no verdict
    on arm C fires the two-arm fallback already ruled in advance; a no verdict
    on arm M drops arm M and carries it as extension E0 on the weekend
    roadmap; a no verdict on arm F after arms T and C have separated is
    reported in the words *metric validated, degree not read*, as a fifth
    registered term, with the reason after a colon ("read failed its floor").
    *Confidence: moderate. Judgment call.* **Alternative:** keep four terms and
    report an arm F no verdict under R1 with a sentence, which is the
    over-reading the finding warns against.

15. **Control 2's pre-stated tolerance on arms C and F: 0.05** over the random
    subspace, the rehearsal's number (section 7.3, item 2). *Confidence: low on
    the number, which was a rehearsal-only tolerance chosen before any figure
    existed; high that a pre-stated number is needed. Judgment call.*
    **Alternative:** the 0.018 room of the no-transplant rule, one number for
    every "no more than the null" check in the design, which is tidier and may
    be too tight for a control that moves an action rather than reads one.

16. **Control 4 is reported, not a control that holds** (section 7.3, item
    4). *Confidence: moderate. Judgment call, this design's own.* On the
    repairs run it did not reach "nothing happens" on arms C and F at their
    nominated sites, for a reason the findings give; as version 1 wrote it, it
    would veto the reading on those arms. **Alternative:** keep it as a control
    that holds and anchor it at a position the nominated sites cannot reach,
    which the rule of section 7.2 does not guarantee exists.

17. **Whether fifty timed steps meets item R-11's five hundred.** The plan
    John authorised ran fifty after five warm-up steps; the item says five
    hundred after fifty. Recommendation: accept fifty for the second release's
    arithmetic, and take the five-hundred-step window from the first
    registered-size run of step 5a rather than from a new rental, repricing
    the eight later runs from it before the second release is drawn.
    *Confidence: moderate. Judgment call.* **Alternative:** hold R-11 to its
    letter and rent a longer timing before asking for the second release,
    about another dollar and another go.

18. **The handshake's machine half.** Two ways to test it, from the slice
    findings' section 9 (at `9f802db`): (a) make the laptop wait, after
    writing the receipt, up to twice the watcher's polling interval before
    deleting, and have the watcher write its "receipt found" somewhere the
    laptop fetches, standard practice for a two-party shutdown, moderate
    confidence that it lets a pass be observed; (b) leave the design as it is
    and register that on the normal path the laptop is the reap and the
    watcher is the backstop, which is what can honestly be said today and
    costs nothing more to rent. Recommendation: (b) for the registration text,
    with (a) as the fix if a later wave shows the laptop failing to answer.
    *Confidence: moderate. Judgment call.*

19. **The position sets of section 7.2 are the rehearsal's four, by name**,
    with the second described as the action position and the answer-marker
    token just before it. The ruled position clause does not say how
    positions are grouped (the repairs findings, section 3); registering the
    rehearsal's grouping is the only one that has been exercised, now under
    the registered rule. *Confidence: moderate. Judgment call.* **Alternative:**
    register the ruled clause literally, the action position and each position
    between the source assignment and the action, one set each, which has not
    been run and would change the count.

20. **Which reading of the layer-0 exclusion is registered (new).** The
    RT-216 ruling's first sentence keeps layer 0 at the action position set
    only; its parenthesis names the position sets spanning the acting turns,
    which on this grammar is `post-identity` alone. The two readings differ on
    `action+ans` and `action+3`, and on the toy they give the same twelve
    nominations (the check at `70be9fb`, section 4.4). Recommendation: register
    the reading as run, layer 0 kept at `action` only (45 site sets on the toy,
    325 on the registered model), because it is the one the re-run exercised
    and it is the stricter of the two where they differ. *Confidence:
    moderate. Judgment call.* **Alternative:** the narrower reading, layer 0
    removed at `post-identity` only (55 and 351), which follows the ruling's
    parenthesis and keeps two more site sets that on the separable arms do
    move the action (section 7.2, item 2).

21. **The fit floor is applied per arm and seed, not per arm (new).** The
    RT-212 ruling says a read that misses the floor "returns no verdict on
    that arm"; the re-run applied it per seed, and the check calls that an
    interpretation, moot on the toy because every arm passes or fails on all
    three seeds alike (the check at `70be9fb`, section 4.1). Recommendation:
    per arm and seed, because every other quantity in the reporting table is
    per seed and the across-seed spread is the registered uncertainty.
    *Confidence: moderate. Judgment call.* **Alternative:** per arm, with the
    arm returning no verdict if fewer than two seeds of three clear, which
    matches the shape of the learn-both and lesion rules and would let one
    seed's reading stand beside two no verdicts.

22. **Whether the fifteen further toy models get the same treatment as the
    fifteen committed (new).** The six free-arm models behind the two training
    redesigns, and the nine behind the grammar attempt, are still untracked in
    their worktrees (section 10); the re-run findings and the models' own
    README both name the gap. Recommendation: commit them with a fingerprint
    list, about 75 MB, because the sentence "every toy result of the weekend
    has its models on the record" is otherwise false in a way the RT-145 form
    describes. *Confidence: moderate. Judgment call; the money is $0 and the
    cost is repository size.* **Alternative:** leave them, since none of the
    results resting on them is a reading of the measure, and say so in the
    registration, which section 10 already does.

*Nothing above is registered. The registration commit, if it comes, follows
the Gate C pass, John's decisions, and Gate A, and every run it affects is
launched after it.*

---

## 16. Where the pieces are

- This proposal: `docs/successor-experiment-proposal-2026-09-26-v3.md`.
- Version 2, unedited: `docs/successor-experiment-proposal-2026-09-26-v2.md`
  (main line at `a3013be`, pull request 54). Version 1, unedited:
  `docs/successor-experiment-proposal-2026-09-21.md`.
- The Gate C tier 1 review of version 2, whose one fatal finding and four
  serious findings this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
  (RT-212 to RT-229; main line at `c17dbdc`, pull request 56), with its
  scripts in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.
- The rulings this version is built to:
  `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` (main line at
  `3af189d`, pull request 60; its refinements at `4bb5727`, pull request 63);
  `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` (five decisions and
  five annotations; main line at `62c3824`, pull request 53);
  `docs/rulings/2026-09-26-weekend-1-queue.md` (nine pages, 2026-09-25);
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (the
  releases, the staggered launch, halt not trim, item 23 on the dates);
  `docs/rulings/2026-09-23-nomination-label.md` and
  `docs/rulings/2026-09-23-range-and-direction-only.md`;
  `docs/rulings/2026-09-20-center-as-degree.md` and
  `docs/rulings/2026-09-20-december-result-roadmap.md`. John's ruling of
  2026-09-26 on the route (b) result is carried in section 7.2, item 1, from
  his message; it has no ruling file of its own at the time of writing.
- The three rehearsals: `docs/2026-09-21-successor-measure-rehearsal.md`
  (main line); `docs/2026-09-26-rehearsal-repairs.md` (main line at
  `882f252`, pull request 52; checked at `d216dbc`, pull request 58); and
  `docs/2026-09-26-toy-rerun-v3-rules.md` (main line at `9d9d31a`, pull
  request 62; checked at `70be9fb`, pull request 65), with their method notes
  `docs/successor-measure-rehearsal-method-2026-09-21.md`, its denominator
  addendum, `docs/rehearsal-repairs-method-2026-09-25.md` and
  `docs/toy-rerun-v3-rules-method-2026-09-26.md`; code and outputs under
  `experiments/rehearsal-successor-measure/` (`out/`, `out-repairs/`,
  `out-v3-rules/`).
- The fifteen trained toy models:
  `experiments/rehearsal-successor-measure/out-repairs/models/`, with
  `SHA256SUMS` and `README.md` (main line at `8038275`, pull request 64).
- The grammar attempt: `docs/2026-09-26-grammar-attempt.md` (main line at
  `ff778ea`, pull request 57; its method note
  `docs/grammar-attempt-method-2026-09-25.md`; outputs `out-grammar-c/`),
  checked at `f1ea004` (pull request 61):
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`.
- The route (b) label search: `docs/2026-09-26-free-arm-label-search.md`
  (branch `w1d-free-arm-label-search` at `26b737f`, pull request 66, open;
  its check cited here once it lands).
- The rented slice: `docs/2026-09-25-rented-slice-findings.md` (first attempt,
  main line) and `docs/2026-09-25-rented-slice-attempt-2-findings.md` with
  the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  (main line at `9f802db`, pull request 51; checked at `afb5183`, pull request
  55).
- Amendment A3's closure, registered: `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
  the closure block of 2026-09-25, and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
- The roadmap it implements: `docs/december-result-roadmap-2026-09-20.md`,
  sections 2, 4 and 5 as amended 2026-09-21; the weekend schedule laid over
  it, `docs/weekend-roadmap-2026-09-24.md`.
- The spend record every figure in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, with its
  ceiling note of 2026-09-25 and its rows of 2026-09-21 and 2026-09-25 (lines
  93 to 95).
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate C now and Gate A later, with the list it is run against,
  `docs/known-failure-modes.md`; this version's own run of that list is
  section 17.
- The Wittgenstein note cited in section 2 as non-binding motivation: the
  TimeAssembler document `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
  Minimum Viable Mind project; not a file in this repository.

---

## 17. The author's failure-mode pass, entry by entry

The outside-review protocol's failure-mode pass belongs to the Gate A tier 1
reviewer, and "an author's run never stands in for the reviewer's"
(`docs/outside-review-protocol.md`, "The failure-mode pass"). This is the
author's run, made so that the reviewer's hour is not spent on a defect
already known, and it is kept in this document rather than filed beside it so
that a reader of the proposal sees it without opening a second file. The list
(`docs/known-failure-modes.md`) has six numbered entries on the main line at
`70be9fb`, and a seventh candidate, drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 9,
item 2, and run by the Gate C review of version 2; all seven were run here
with this session's own commands, on the committed outputs on the main line
(`experiments/rehearsal-successor-measure/out-v3-rules/` at `9d9d31a` and
`out-repairs/` at `882f252`; paths below are relative to that directory).
Every command was run from this worktree with the repository's own Python
environment, shown as `.venv/bin/python`; nothing was rented, created or
spent, and no registered, ruling or protocol text was edited.

**1. A comparison whose denominator was zero. Does not fire. MEASURED.** Part
one asks whether the ceilings typed in trace to committed measurements. The
no-transplant rate is measured on every arm and seed
(`measure_*_seed*.json`, `reading.accuracy_untouched`), not assumed. Part two
asks for the denominator and the top of the scale when the target is absent,
for every arm and seed at the site set this version's rule nominates:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-v3-rules/'
print('arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form)')
for a in 'TCFM':
  for s in '012':
    r=json.load(open(f'{O}measure_{a}_seed{s}.json'))['rows']['unruled_layer0_injection_removed']['reading']
    u,w,o=r['accuracy_untouched'],r['accuracy_whole'],r['arm_own_accuracy']
    print(f'{a}/{s}       {u:.4f}    {w:.4f}  {o:.4f} |  {w-u:.4f}       {0.8*(o-u):.4f}    |  {(w-u)/(w-u):.4f}')
"
arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form)
T/0       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000
T/1       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000
T/2       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000
C/0       0.0512    0.5400  0.5487 |  0.4888       0.3980    |  1.0000
C/1       0.0488    0.5575  0.5813 |  0.5088       0.4260    |  1.0000
C/2       0.0600    0.5463  0.5525 |  0.4863       0.3940    |  1.0000
F/0       0.0587    0.4850  0.5587 |  0.4263       0.4000    |  1.0000
F/1       0.0563    0.5675  0.5663 |  0.5112       0.4080    |  1.0000
F/2       0.0688    0.5300  0.5563 |  0.4613       0.3900    |  1.0000
M/0       0.0125    0.7800  0.8712 |  0.7675       0.6870    |  1.0000
M/1       0.0175    0.7738  0.8800 |  0.7563       0.6900    |  1.0000
M/2       0.0138    0.7937  0.8712 |  0.7800       0.6860    |  1.0000
```

The smallest denominator is 0.4263 (arm F seed 0), and every denominator
clears what the floor needs. The top of the scale is 1.0000 on every arm
under the registered form. The repair of the per-arm-ceiling finding (RT-172)
holds on the re-run's data as it held on the repairs'. One thing to watch,
ARGUED: on arm F the denominator clears the floor by only 0.026 to 0.103.

**2. A probe target that cannot be recovered in principle. Fires on the free
arm, and is now caught by a registered rule. MEASURED.** Part one, the
route-sentence search, with this design's own wording in the pattern:

```
$ grep -n -iE 'route by which|carried by the token|forced by the loss|is the input token' docs/successor-experiment-proposal-2026-09-26-v3.md
1031:   own**. *The route by which that quantity reaches the model's states, in one
1032:   sentence:* the marker word is the input token at every turn the model's own
1033:   assignments are spoken on, so it is carried by the token into the running
1037:   claim, that which marker word is the model's own is forced by the loss at
```

(The same four lines match again inside this section, where the command's
output is quoted; those are not route sentences.)

A route sentence exists (section 7.2, item 1), and the fourth match is the
sentence striking version 2's loss clause, not a route. Part two, the two
runs on the same instrument with the same bar: the committed fit accuracies,
per layer, serve as the positive control (arms T, C and M) and the target run
(arm F):

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-v3-rules/'
p=json.load(open(O+'pass2_summary.json'))
for a in 'TCFM':
  for s in '012':
    n=json.load(open(f'{O}nominate_{a}_seed{s}.json'))
    print(f'{a}/{s} fits per layer', {l:round(v,3) for l,v in n['fit_accuracy'].items()})
print('arm_F:', {s:(round(v['fit_accuracy'],3), v['fit_floor_passes'], v['reasons']) for s,v in p['arm_F'].items()})
print('arm_M_pass:', p['arm_M_pass']['met_on_every_seed'], [round(x,4) for x in p['arm_M_pass']['readings']])
print('separation:', {s:round(v['C_minus_T'],4) for s,v in p['separation'].items()})
"
T/0 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
T/1 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
T/2 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
C/0 fits per layer {'0': 0.072, '1': 0.994, '2': 1.0, '3': 1.0, '4': 1.0}
C/1 fits per layer {'0': 0.072, '1': 0.983, '2': 0.967, '3': 0.983, '4': 0.961}
C/2 fits per layer {'0': 0.072, '1': 0.978, '2': 0.983, '3': 1.0, '4': 1.0}
F/0 fits per layer {'0': 0.072, '1': 0.172, '2': 0.144, '3': 0.106, '4': 0.067}
F/1 fits per layer {'0': 0.072, '1': 0.067, '2': 0.117, '3': 0.144, '4': 0.117}
F/2 fits per layer {'0': 0.072, '1': 0.106, '2': 0.139, '3': 0.111, '4': 0.111}
M/0 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 0.989, '4': 0.989}
M/1 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
M/2 fits per layer {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
arm_F: {'0': (0.172, False, ['arm failed its gate', 'read failed its floor']), '1': (0.067, False, ['arm failed its gate', 'read failed its floor']), '2': (0.106, False, ['arm failed its gate', 'read failed its floor'])}
arm_M_pass: True [0.4886, 0.486, 0.5449]
separation: {'0': 1.0051, '1': 1.0025, '2': 1.0}
```

The middle limb of failure 2, "the second run clears the bar and the first
does not", is exactly the toy's state: the read clears on arms T, M and C
(1.0, and 0.961 or above at the nominated layers) and returns nothing on arm F
(at most 0.172). **This is the Gate C review's RT-212, and it still fires on
the free arm.** What has changed is the design's response: the fit floor of
section 7.2 turns the firing into a registered *no verdict* on arm F on every
seed, and the withdrawn number is not reported as a reading. The route (b)
search for a target the free system does carry found none at the floor
(section 7.2, item 1), so the failure is caught rather than repaired, and the
registration says so.

**3. A cell that is empty by construction. Does not fire on the reading; its
test's third part is now inside the allowance. MEASURED.** Part one, the
cells: control 6's two cells on the relaxed set, on every arm and seed:

```
$ .venv/bin/python -c "
import json,glob
R='experiments/rehearsal-successor-measure/out-repairs/'
for f in sorted(glob.glob(R+'measure_base_*.json')):
    d=json.load(open(f))['arms']
    for k in sorted(d):
        c=d[k]['controls']; print(' ',k, 'same-value trials', c['6a same-value cell: trials'], 'different-value trials', c['6b different-value cell: trials'])
"
  F/base/0 same-value trials 81 different-value trials 719
  F/base/1 same-value trials 81 different-value trials 719
  F/base/2 same-value trials 81 different-value trials 719
  M/base/0 same-value trials 81 different-value trials 719
  M/base/1 same-value trials 81 different-value trials 719
  M/base/2 same-value trials 81 different-value trials 719
  C/base/0 same-value trials 81 different-value trials 719
  C/base/1 same-value trials 81 different-value trials 719
  C/base/2 same-value trials 81 different-value trials 719
  T/base/0 same-value trials 81 different-value trials 719
  T/base/1 same-value trials 81 different-value trials 719
  T/base/2 same-value trials 81 different-value trials 719
```

Both cells have trials on every arm and seed, so the RT-173 repair holds.
Control 2's cell on arms T and M has zero clearing site sets by construction,
which the repairs rulings' item 5 records as not applicable, with its reason.
Part two, the generator property that empties a cell, is section 4.2's
distinctness, read and named there. Part three, thresholds at both ends, for
every threshold this version attaches to a count:

```
$ .venv/bin/python -c "
from fractions import Fraction as Fr
from math import comb
n=3000
def tail(k): return Fr(sum(comb(n,i)*3**(n-i) for i in range(k,n+1)), 4**n)
k=min(k for k in range(760,820) if tail(k)<=Fr(1,20))
print('learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05:', k, 'share %.4f'%(k/n), 'tail %.4f'%float(tail(k)))
print('a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability %.4f per seed'%float(tail(k)))
for p in (0.2633, 0.56):
    f=(1-p)/7; print(f'no-transplant rule at own-directed {p}: formula {f:.4f}, broken-pairing rate 0.1250, miss {0.125-f:.4f}, flagged by the 0.018 room: {0.125-f>0.018}, margin {0.125-f-0.018:.4f}')
print('largest measured miss 2026-09-21: %.6f; inside 0.018: %s'%(0.07625-(1-0.589)/7, 0.07625-(1-0.589)/7<=0.018))
"
learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05: 790 share 0.2633 tail 0.0485
a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability 0.0485 per seed
no-transplant rule at own-directed 0.2633: formula 0.1052, broken-pairing rate 0.1250, miss 0.0198, flagged by the 0.018 room: True, margin 0.0018
no-transplant rule at own-directed 0.56: formula 0.0629, broken-pairing rate 0.1250, miss 0.0621, flagged by the 0.018 room: True, margin 0.0441
largest measured miss 2026-09-21: 0.017536; inside 0.018: True
```

The bar reproduces at 790 of 3,000. The no-transplant rule fires on the
broken end and passes on the working end, and the case the allowance was set
from is now inside it (RT-222 closed); at the bar it detects a broken pairing
by 0.0018, which is printed in the reporting table. The lesion collapse line
misreads a fully collapsed arm 4.85% of the time per seed, which is what the
two-of-three clause of section 8.2 is for (RT-220 closed). The fit floor sits
at 0.8 against a permutation null whose 95th percentile is 0.111 to 0.128 on
every pair, so it has room on both ends. The lesion figures themselves:

```
$ .venv/bin/python -c "
import json
g=json.load(open('experiments/rehearsal-successor-measure/out-repairs/gate_base.json'))['runs']
for k in sorted(g):
    if k[0] in 'TCFM': print(k, 'lesioned own-directed %.4f'%g[k]['lesioned_own'], 'collapses:', g[k]['lesion_collapses_own'])
"
C/base/0 lesioned own-directed 0.1780 collapses: True
C/base/1 lesioned own-directed 0.1830 collapses: True
C/base/2 lesioned own-directed 0.1703 collapses: True
F/base/0 lesioned own-directed 0.1760 collapses: True
F/base/1 lesioned own-directed 0.1850 collapses: True
F/base/2 lesioned own-directed 0.1940 collapses: True
M/base/0 lesioned own-directed 0.2230 collapses: True
M/base/1 lesioned own-directed 0.2190 collapses: True
M/base/2 lesioned own-directed 0.2203 collapses: True
T/base/0 lesioned own-directed 0.2467 collapses: True
T/base/1 lesioned own-directed 0.2510 collapses: True
T/base/2 lesioned own-directed 0.2733 collapses: False
```

And the site-set family this version registers, counted by the rule and its
two variants rather than by hand:

```
$ .venv/bin/python -c "
def contiguous(n): return [tuple(range(a,b+1)) for a in range(n) for b in range(a,n)]
P4=['action','action+ans','action+3','post-identity']
for name,n in (('toy (embedding + 4 blocks)',5),('registered (embedding + 12 blocks)',13)):
    L=contiguous(n); fam=[(l,p) for l in L for p in P4]
    reg=[(l,p) for l,p in fam if not (0 in l and p!='action')]
    narrow=[(l,p) for l,p in fam if not (0 in l and p=='post-identity')]
    strict=[(l,p) for l,p in fam if 0 not in l]
    print(f'{name}: {len(L)} contiguous layer sets x 4 position sets = {len(fam)} site sets')
    print(f'   registered rule (layer 0 kept at the action position set only): {len(reg)} site sets, {4*len(reg)} comparisons at four rank caps')
    print(f'   narrower reading (layer 0 removed at post-identity only):       {len(narrow)} site sets, {4*len(narrow)} comparisons')
    print(f'   stricter variant (layer 0 removed everywhere):                  {len(strict)} site sets, {4*len(strict)} comparisons')
"
toy (embedding + 4 blocks): 15 contiguous layer sets x 4 position sets = 60 site sets
   registered rule (layer 0 kept at the action position set only): 45 site sets, 180 comparisons at four rank caps
   narrower reading (layer 0 removed at post-identity only):       55 site sets, 220 comparisons
   stricter variant (layer 0 removed everywhere):                  40 site sets, 160 comparisons
registered (embedding + 12 blocks): 91 contiguous layer sets x 4 position sets = 364 site sets
   registered rule (layer 0 kept at the action position set only): 325 site sets, 1300 comparisons at four rank caps
   narrower reading (layer 0 removed at post-identity only):       351 site sets, 1404 comparisons
   stricter variant (layer 0 removed everywhere):                  312 site sets, 1248 comparisons
```

**4. A claim of measurement with no record, or a record that does not
reproduce. Fires on one class of figure, said so in the text. MEASURED.** Part
one, the two sweeps, run on this document's sections 0 to 16 (the text
before this section, cut at its heading, because this section's own output
blocks match the patterns and would count themselves):

```
$ awk '/^## 17\. /{exit} {print}' docs/successor-experiment-proposal-2026-09-26-v3.md > "$T/v3-through16.md"
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T/v3-through16.md"
573
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T/v3-through16.md"
195
$ grep -c MEASURED "$T/v3-through16.md"; grep -c ARGUED "$T/v3-through16.md"; wc -l < "$T/v3-through16.md"
56
15
2552
```

Part two was run by reading, for every MEASURED claim this version takes
from the re-run, the repairs, the 2026-09-21 rehearsal, the grammar attempt,
the slice and the ledger, against the file named beside it; the commands in
failures 1 to 3 and candidate 7 are the ones that can be shown. **Where it
fires, and what the text does about it:** every toy figure for arms C, F and
M that version 2 quoted from the repairs' 44-set family does not reproduce
under the registered rule, and this version replaces each with the re-run's
figure or, for the controls the re-run did not re-run (controls 1, 2, 4 and
6, the true-slot check on arm M, and the uncertainty row), drops the figure
and says it is owed (sections 5.3, 7.3, 9 and W11). The figures that rest on
models not committed at the time of writing are named in section 10. The
repository's own two checkers, run on the whole document. A first run, before
this section existed, found four references to files not in the repository
and six figures absent from the file cited; one reference was a script name
printed in a check's appendix rather than a file, and three figures were arm
M's gate-episode share and its counts (0.6033, 1,810 of 3,000) cited to the
fresh-episode file; both sentences were reworded (section 7.2, item 2;
section 5.3). The run on the file as it stands:

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-09-26-v3.md
[CONFIDENT] 3 reference(s) name a file that is not in the repository
  (every one is the route (b) search's findings file, on pull request 66 and not yet merged, cited by branch and commit at each place)
[CONFIDENT] 3 exact figure(s) absent from the one file their sentence cites
  (every one is the section number 1.3, in "Part 1, section 1.3", read as a figure)
$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-09-26-v3.md
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source: 2 found
  ($44, cited to the 2026-09-21 ruling that set the first release, which is the figure's source; the ledger carries it because the ruling did)
```

That the checkers see so little of this document is a statement about the
checkers, not about the rest being clean.

**5. A command that creates something while documented as creating nothing.
Does not fire on anything this document runs; one gap stated. MEASURED.** The
proposal runs nothing that touches a vendor. The list's own test:

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  ... (every line ok)
registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A
      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing
all checks pass. nothing was created and nothing was spent.
```

The gap is the one RT-228 named and section 5 now states: the launcher is
named (`launch_a3_fetch_first.sh`, which carries the guard), the registered
`launch_a3.sh` is not used, and the successor's training entry point for arms
T, C and M on the rented machine does not exist yet.

**6. A remote step tested only against stand-ins. The launcher's check passes;
the design has three such steps, each stated. MEASURED.**

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)
launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
```

On the design: the handshake's machine half has been tested only against
stand-ins (W9, decision 18); arm M's code has never run on the rented machine
(W9, step 4 of section 11); the tripwire does not exist as code yet (section
12.5). All three are said in the text, and none is counted as tested.

**Candidate 7. An outcome line a plan states in advance that the design
cannot produce on the path it expects. Does not fire on the four lines it
fired on in version 2; one line is conditional and says so. MEASURED.** The
drafted test: for each pre-stated line, name the code path that prints each
signal it needs, and show that path can run in the order the line requires.
Run on the committed outputs:

- **Arm M's pass line** ("between 0.3 and 0.7 on every seed"): produced,
  with control 3 reported and not gated
  (`pass2_summary.json`, `arm_M_pass.met_on_every_seed: true`, readings
  0.4886, 0.4860 and 0.5449; failure 2's output above). RT-214 closed.
- **The lesion description**: now "arm T collapses on two of three seeds",
  which is what the path produced (failure 3's output above). RT-220 closed.
- **The rider**: can produce a reading on arms C, F and M on 0 of 9 toy pairs
  on the path it expects, and the text says so with the two reasons (section
  7.2, item 7). Accepted as the report.
- **The $10 wager** (section 12.8), and the money lines of section 12:

```
$ .venv/bin/python -c "
spent=228.15; first=44.0; second_no_rerun=84.06+12+23; note_both=161.90
print('ruled split: first release %.2f + second release without its re-run line %.2f = %.2f'%(first,second_no_rerun,first+second_no_rerun))
for lo,hi,label in ((29.70,41.76,'arm M three runs only, 1.94 in the first release'),(32,44,'arm M as ruled, 32 to 44, 1.94 inside')):
    for m in (lo,hi):
        left=450-spent-(first+second_no_rerun)-m
        print(f'  {label}: arm M {m:.2f}: programme after {spent+first+second_no_rerun+m:.2f}, left {left:.2f}, meets the 10 floor: {left>=10}')
for m in (32,44):
    print(f'note split (161.90 + arm M {m}): programme after {spent+note_both+m:.2f}, left {450-spent-note_both-m:.2f}')
print('first release development line, four arms at 1.943 each: %.2f of the 10 line'%(4*1.943))
"
ruled split: first release 44.00 + second release without its re-run line 119.06 = 163.06
  arm M three runs only, 1.94 in the first release: arm M 29.70: programme after 420.91, left 29.09, meets the 10 floor: True
  arm M three runs only, 1.94 in the first release: arm M 41.76: programme after 432.97, left 17.03, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 32.00: programme after 423.21, left 26.79, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 44.00: programme after 435.21, left 14.79, meets the 10 floor: True
note split (161.90 + arm M 32): programme after 422.05, left 27.95
note split (161.90 + arm M 44): programme after 434.05, left 15.95
first release development line, four arms at 1.943 each: 7.77 of the 10 line
```

  The wager meets its floor on every split and at both ends of the range.
  RT-217 and RT-229 closed.
- **R1's precondition** (every arm carried passes its gate): produced on the
  toy under section 8.1's gates for arms T, C and M; arm F fails, and the
  line for arm F is now conditional in the text ("arm F may return no
  verdict", section 3), with the stop of step 5a as the path that produces
  the signal before the second release. RT-213 closed on the anchors' terms;
  on arm F the candidate does not fire because the text no longer states a
  line the path cannot produce.

Whether the candidate is a new species or an instance of failure 3 is John's
ruling, still open; on this version it catches nothing failure 3's test does
not.

**What this pass leaves open, in one place.** The controls the re-run did not
re-run at the registered site sets (section 7.3), the true-slot check on arm
M at those sites (section 5.3), the route (b) search's check (section 7.2,
item 1), and the reviewer's own pass, which is still owed, as the protocol
says.

---

## 18. Change log from version 2, keyed to the Gate C review's findings

Every change from version 2 is listed by the finding that caused it, with the
section it lands in. Findings are the Gate C tier 1 review of version 2
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
at `c17dbdc`) and the rulings on them
(`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` at `3af189d` and
`4bb5727`). "Ruled" means the ruling file; "refined" means its section
"Refinements 2026-09-26, after the toy re-run".

- **RT-212 (fatal: the free arm's ownership read never finds its label).**
  Ruled, items 1 to 3. The fit floor of four fifths on held-out development
  episodes registered as a no-verdict rule, with the label-permutation null
  reported beside it (sections 1, 6.4 item 2, 7.2 item 1, 7.4, 7.5, 9); its
  toy demonstration, no verdict on arm F at 0.172, 0.067 and 0.106 and a
  reading on T, C and M (section 7.2, item 1); arm F's toy reading withdrawn
  and stated as "no verdict, read failed its floor" on every seed (sections
  3, 5.4, 10 R-4); section 3's admission rewritten to say the toy can tell an
  empty instrument from a ceiling, with the residual admission stated and
  carried as W12; version 2's loss clause in the route sentence struck
  (section 7.2, item 1); the route (b) investigation reported, none of three
  candidates at the floor, and John's ruling of 2026-09-26 that this version
  registers with the fit floor alone, the ruled label as the one registered
  read, the three candidates as exploratory fits (section 7.2, item 1;
  sections 3, 7.4, 9); the fit-floor stop added to step 5a beside the
  learn-both stop, as S4a (section 11; W5); the search's figure for the ruled
  label withheld until its check reconciles it with 0.172 (section 7.2, item
  1).
- **RT-213 (serious: arm C fails the learn-both gate on every toy seed).**
  Ruled, items 1 to 3. Arms T, C and M gated on the own-directed condition
  only, arm F on both, with the reason recorded (sections 3, 8.1, 9); arm C's
  named-other failure stated with its numbers, 760, 751 and 708 of 3,000
  against 790, wherever its toy record is quoted (sections 3, 4.4, 5.2, 8.1,
  10 R-1 and R-3); the toy outcome on the anchors' terms, R1 (section 3);
  the cost of a constructed arm's failure under the launch order stated, and
  no extra arm C run in step 5a (section 11, step 5b; W3).
- **RT-214 (serious: control 3 fails on arm M seed 1).** Ruled, items 1 to 3,
  refined by refinement item 1. Control 3 is a twenty-draw null, reported and
  not gated on every arm, with its distribution and the ownership-only
  transplant's place in it in the reporting table (sections 1, 7.3 item 3,
  7.4, 7.5, 9); the reporting rule described as clarified after the re-run of
  2026-09-26, not as pre-stated (section 7.3, item 3); version 2's arm M pass
  stated as read without control 3 applied (section 5.3); the fixed 0.0175
  room dropped from this control.
- **RT-215 (serious: the site-set rule was never run).** Ruled. The rule run
  at toy scale as one combined re-run with the fit floor and the null, and
  every toy figure for arms C, F and M taken from it (sections "What this
  version rests on", 3, 5.2, 5.3, 5.4, 7.2 item 2, 9, 10); the sensitivity
  row named as the repairs-style row (section 7.2, item 4); the condition on
  multi-layer nominations reported as not fired (section 7.2, item 4).
- **RT-216 (serious: most nominations sat at the injection).** Ruled, items 1
  to 3, refined by refinement item 2. Layer-0 site sets removed from the
  candidate family at every position set other than `action`, as removal and
  choose again, written into section 7.2, item 2, with the removal reading
  described as clarified after the re-run and not as pre-stated; the counts
  under the rule, 45 and 180 on the toy, 325 and 1,300 on the registered
  model, with the two variants beside them (section 7.2, item 2; section 9);
  the stricter variant, layer 0 removed everywhere, as a sensitivity row
  (sections 7.2 item 2, 7.4, 7.5); W7's last sentence struck and replaced
  by the measured fact, six of nine nominations at the injection before the
  rule (section 13); version 2's argument about identical twin states inside
  the action turn not repeated, and the tie-break on arm T stated (section
  7.2, item 2); which reading of "spanning the acting turns" is registered put
  to John as decision 20; the refinements' wrong clause about arm C falling to
  the fit floor named as owed an annotation (section 7.2, item 1).
- **RT-217 (minor: the $16 wager).** Ruled. The wager stated on the ruled
  split against the full range, with a $10 floor, and the worst case, $14.79,
  printed (sections 12.4, 12.8, 15 item 7; section 17, candidate 7).
- **RT-218 (minor: 7 of 12 and 8 of 12).** Ruled. "8 of 12 by site set, 7 of
  12 by share", the word "discrepancy" dropped, and the check's 6 of 12 noted
  (section 7.2, item 4).
- **RT-219 (minor: 0.6033 and 0.60375).** Ruled. 0.60375 kept, with the
  gate-episode share explained and cited to its own file (section 5.3).
- **RT-220 (minor: the lesion description).** Ruled. Arm T collapses on two of
  three seeds, seed 2 at 0.2733 against 0.2633; arm F read if at least two of
  three seeds collapse, the third reported; the 4.85% misread rate printed
  (sections 8.2, 9; section 17, failure 3).
- **RT-221 (minor: the separation figures).** Ruled. 1.0051, 1.0025 and
  1.0000 from the re-run; version 2's 0.9977 and 0.9927 labelled as from the
  pre-widening family (sections 3, 5.2, 9, 10 R-10).
- **RT-222 (minor: the 0.0175 allowance).** Ruled. "At most the largest
  measured miss, rounded up to 0.018", with the detection margin at the bar
  printed in the reporting table (sections 6.4 item 3, 7.3 item 1, 7.4, 7.5,
  9, 15 item 15).
- **RT-223 (minor: arm M's formula and true-slot reading are one check).**
  Ruled. Said so (sections 5.3, 7.2 item 6, 9, 15 item 1); the check at the
  registered site sets listed as owed (sections 5.3, 10 R-3).
- **RT-224 (minor: a position set described backwards).** Ruled. "The action
  position and the answer-marker token just before it" (sections 7.2 item 2,
  15 item 19).
- **RT-225 (minor: the rider's cause on arm M).** Ruled. One clause: on arm M
  the rider's no verdict is a miss of the four-fifths floor with about 0.41
  moved, not nothing reaching the state (sections 7.2 item 7, 13 W2).
- **RT-226 (minor: two ledger citations).** Ruled. The 8.47 against 2.42
  figures cited to the ledger's lines 93 and 423; $10.04 called the
  lifetime-priced cost (sections 10 R-7, 12.3, 12.4, 12.5).
- **RT-227 (minor: 34 references to unmerged files).** Ruled. Every merged
  source cited by its main-line merge commit: 52 at `882f252`, 51 at
  `9f802db`, 53 at `62c3824`, 54 at `a3013be`, 55 at `afb5183`, 56 at
  `c17dbdc`, 57 at `ff778ea`, 58 at `d216dbc`, 60 at `3af189d`, 61 at
  `f1ea004`, 62 at `9d9d31a`, 63 at `4bb5727`, 64 at `8038275`, 65 at
  `70be9fb`; pull request 66 cited by branch and commit until it merges
  (throughout; section 16); every arm C, F and M figure re-derived from the
  combined re-run (RT-215).
- **RT-228 (minor: "the same launcher" names no file).** Ruled. The launcher
  named, the registered one excluded, the missing training entry point and the
  tripwire listed as code owed (section 5); arm M's code on the rented machine
  listed as untested beside the handshake's machine half (W9; section 11,
  step 4; section 17, failure 6).
- **RT-229 (minor: arm M's development run costed twice).** Ruled. The first
  release's development line covers four arms, widening item 10 of the
  2026-09-21 ruling; the $1.94 out of section 12.4; arm M's development run
  in step 4 (sections 5.3, 11, 12.2, 12.3, 12.4).
- **From the refinements' item 3 and the check of the re-run (not a numbered
  finding).** The fifteen committed models named as what every toy result
  rests on, with what rests on models not yet committed listed (section 10;
  decision 22); the check's four small errors in the re-run findings carried
  where they bear (section 7.3, item 7, on control 7's site sets); the
  check's note that the second pass's two rule choices were made with the
  first pass's figures in hand carried into sections 7.2 and 7.3.
- **From the grammar attempt and its check (the repairs rulings, item 1).**
  Fallback (d) registers: the attempt's failure recorded with its numbers and
  the check's re-run, the note that seed counts are one-run properties, the
  grammar left as version 2 had it (sections 3, 4.1, 4.4, 5.5, 14, 15 item
  9).
- **Not changed.** Sections 2, 4.1 to 4.3, 6.1, 6.2, 7.1, 12.6 and 12.7
  carry version 2's text with only the citations updated; version 1's
  decisions 2, 3, 4, 8, 12 and 13 stand as put.

---

## What this version does not do

It edits nothing: not version 2, not any ruling, registered text or protocol
text, and not the re-run's or the label search's findings. It issues no go,
releases no money, launches nothing and rents nothing. It does not close the
Gate C review of version 1's finding RT-182 or rule on any of the open
decisions in section 15. It does not fill in the route (b) search's check,
which is cited by number once it lands. Under the pairing rule of
`docs/outside-review-protocol.md` it is checked by a session that did not
write it, the Gate C tier 1 reviewer, before anything relies on it.
