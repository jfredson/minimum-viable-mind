# Successor experiment, proposal version 2: reading how much of the act is organised around who is acting

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1d proposal v2",
session (d) of `docs/weekend-1-session-prompts.md`, in its own worktree
(branch `worktree-w1d-proposal-v2`). The file keeps the name the prompts file
gives it (dated 2026-09-26, the Saturday it was planned for); the work ran a
day early because the rulings it depends on were made on the evening of
2026-09-25. **Status: PROPOSAL, version 2. Nothing here is registered and
nothing here binds.** It is written from version 1
(`docs/successor-experiment-proposal-2026-09-21.md`, which is left unedited)
and goes to Gate C of `docs/outside-review-protocol.md` (a review attached to
a proposal before John rules on it), then, after his rulings, to Gate A (the
registration review, both tiers) as registration text. No money is spent and
no machine is rented by this document.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30): the plain word before the term of art, and no bare
identifier anywhere. Every finding quoted from a record is labelled
**MEASURED** (a command was run and its output is filed in the record cited)
or **ARGUED** (reasoning a reader can dispute). Every number carries the
committed file it was read from. Figures from the arms whose training does not
reproduce are quoted as a range and a direction, as
`docs/rulings/2026-09-23-range-and-direction-only.md` requires.*

## What this version rests on, and what was still pending when it was written

Version 2 carries the rulings John made on 2026-09-25 and the two
measurements made the same day. Three of its sources were not on the main
line when it was written, and two checks it depends on had not run. They are
named here, once, so that a reader knows which figures may still move.

| Source | Where it is | Standing when this was written |
|---|---|---|
| The Weekend 1 queue ruling: nine pages, ruled 2026-09-25 | `docs/rulings/2026-09-26-weekend-1-queue.md`, main line | Ruled. Its own check under the pairing rule is owed before sessions (c) and (d) rely on it; this session relied on it, and says so |
| The five rehearsal-repairs rulings of 2026-09-25 | `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`, branch `rulings-2026-09-25-repairs` (pull request 53, open) | Ruled; not yet merged |
| The rehearsal repairs findings, session (c) | `docs/2026-09-26-rehearsal-repairs.md`, branch `worktree-w1c-rehearsal-repairs` at commit `e0626b2` ("Rehearsal repairs: the findings"; pull request 52, open) | **Its check under the pairing rule was pending** when this was written and may adjust a figure. Every figure taken from it below is cited to that commit |
| The rented slice, second attempt: seconds per step | `docs/2026-09-25-rented-slice-attempt-2-findings.md`, the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`, and the compute ledger row, all on branch `worktree-mvm-w1f-rented-slice-attempt-2` at commit `7da1946` ("Rented slice, second attempt: seconds per step measured…"; pull request 51, draft) | **Its check was pending** too; same rule, every figure cited to that commit |
| The Amendment A3 closure block and the tier 2 dispositions | `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` and `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`, main line at `7b15c88` (the A3 registration commit) | Registered; what section 2 may cite about Amendment A3 is taken from there |
| The grammar attempt, redesign (c) for the named-other condition | branch `worktree-w1c-grammar-attempt` | **Pending: no findings and no output.** At 20:31 Pacific on 2026-09-25 the branch carried three commits beyond the main line — its method note, the repairs driver carried in unchanged, and the grammar setting and driver as code only, the last titled "code only, no output" (MEASURED: `git log --oneline main..worktree-w1c-grammar-attempt`, in the failure-mode pass filed with this version). Section 4.4 says what changes if it clears |

Where a figure below comes from one of the two pending sources, the sentence
says so. If a check moves a figure, this document is corrected by a dated
note beside the sentence, in the way the repository already handles a
superseded claim, and the registration text (a later version) carries the
checked figure.

---

## 0. The whole thing in seven sentences

The project's open question is one of degree: a small transformer that has
learned a causally load-bearing answer to "which agent am I" counts as a
centre at the bottom of the gradient, and what would separate it from a
centre in the fuller sense is how much of its act is organised around that
answer. Nobody has a measure of that. So the successor experiment builds
systems whose degree is fixed by how they are built — one where "which agent
am I" sits in a slot that can be swapped on its own, one where it is stirred
into everything, and, new in this version, one that is a mixture of the two
by item — and one ordinary freely trained system, and asks whether a
candidate measure can tell the built systems apart and place the mixture
between them. The measure is: transplant the part of the internal state that
says who is acting from one run into a matched run and see whether the
action follows the transplanted identity; compare that with transplanting
the whole internal state at the same places; the gap between the two, as a
share of the room the whole-state transplant had to move, is the reading. If
the measure separates the two built anchors at the ruled bar, the freely
trained system gets a reading and the project's current sentence "degree
unmeasured" is replaced by a number. If it does not separate them, that is a
result too, and the measure is not used. And one admission is written into
the registration whatever happens: a free-arm reading at the entangled
anchor cannot be told from the instrument's ceiling.

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
  moment it acts, that this turn is its own — a copy of its own previous state
  injected at its own turns. Registered as Amendment A1 on 2026-08-09. It is
  the only honest source of ownership in this design, because in a dialogue
  where the turns are interchangeable, nothing in the text itself can carry it
  (the red-team finding that made this necessary is ledger item RT-17, the
  finding that any learnable ownership cue in the tokens is a fingerprint).
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
- **The no-transplant rate.** The share of trials in which the model, with
  nothing transplanted, already gives the value the donor's identity would
  dictate. Version 1 called it the untouched rate or the floor. It is the
  quantity the chance-corrected form subtracts (section 6.3).
- **The chance-corrected form.** The reading with the no-transplant rate
  subtracted from both the top and the bottom of the fraction, ruled as the
  registered form on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`,
  page 2).
- **Arms.** The four trained systems being compared: the one built to keep the
  ownership answer separable (arm T, for tracker), the one built to entangle it
  (arm C, for the fuller centre end of the axis), the one built as a mixture of
  the two by item (arm M, for middle; section 5.3), and the ordinary freely
  trained one (arm F, for free).
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
likely to change his view of the programme — the matched-role swap experiment
in section 5 of `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`
— extended from two arms to four so the measure has a known case at both ends
of the axis and one in the middle.

**What Amendment A3 hands this experiment, in the words its closure block
registers** (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
the closure block dated 2026-09-25, and
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`). Its outcome:
*not testable — the registered comparison was undefined for every possible
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
nothing when moved is, on this rationale, not part of the act. The note's own
caution stands with it: these criteria license claims about degree of
participation, not a verdict on inside experience. The note's second and
third tests wait for resumption after May 2027; the second is named on the
weekend roadmap's extension list so it is not lost. **Nothing in this
paragraph is registered text, and no gate reads it.**

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
| **R2** | **metric does not separate** | Every arm carried passes the learn-both gate, but the measure cannot tell T and C apart at the bar. The measure is not used on arm F; the result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | One or more arms fail the learn-both gate after the one permitted re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. | Yes, if the gate was reached |
| **R4** | (none) | The programme hibernates with a registered design and a rehearsal only. **Since 2026-09-21 a missed kill date does not put the roadmap here by itself**: registration after 2026-10-18, or launch of the remaining registered runs after 2026-11-01, is still possible on a fresh ruling that names what comes off the back end to make room, and R4 is where the roadmap lands only if that ruling says it is not worth it (item 23 of the 2026-09-21 ruling; section 5 of `docs/december-result-roadmap-2026-09-20.md`). | No. Recorded as a schedule failure, not a scientific one |

**The admission that goes into the registration text whatever happens (ruled
2026-09-25, the queue ruling, page 5).** A free-arm reading at the entangled
anchor cannot be told from the instrument's ceiling. The chance-corrected form
reads 1 when the ownership-only transplant does nothing at all, and an
entangled system also reads near 1; a freely trained system reading near 1
therefore says either "as entangled as the built anchor" or "the nominated
subspace carried nothing here", and this measure cannot say which. The
rehearsal's free arm read at the entangled end on every seed (MEASURED:
1.00 to 1.003, `docs/2026-09-26-rehearsal-repairs.md` at commit `e0626b2`,
section 6.2; check pending), which is what makes the admission necessary
rather than decorative. Arm M (section 5.3) is the design's answer to it: a
known case in the middle of the scale, so that a free-arm reading can at
least be placed against three anchors rather than two. It does not remove the
admission, because arm M's known degree is a mixture by item, and a free arm's
partial separation, if it has any, would be within each trial (section 5.3).

**The honest prior, stated before the work rather than after it.** On the
existing record the most likely outcome is **R3**, and the most likely reason
is the named-other half of the task. Three seeds of the closed Amendment A3
design failed to learn a named-other query battery, landing at 0.2877, 0.3057
and 0.3195 against 0.3227 for a solver that cannot read the name the question
supplies; a fourth run with the battery's own loss term reached 0.3125 and
changed nothing (`control-learnability-pilot-findings.md`, the pilot findings
file; ledger items RT-52 to RT-69). This experiment moves the named-other
condition from a query at the end of the episode to an action at the model's
own turn. **At toy scale that has not been enough, and this is now on the
record rather than predicted** (ruled 2026-09-25: the queue ruling, page 4,
fallback (d), and item 1 of
`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`): the named-other
condition failed its bar on two of three toy arms, doubling the training
budget did not fix it (`docs/2026-09-21-successor-measure-rehearsal.md`,
section 8), and neither a curriculum nor loss re-weighting fixed it either
(MEASURED: 0 of 3 seeds under each, against 1 of 3 on the unchanged recipe,
`docs/2026-09-26-rehearsal-repairs.md` at `e0626b2`, section 2; check
pending). A grammar change, redesign (c), is being attempted on 2026-09-26
and was pending when this was written; section 4.4 says what changes if it
clears. Section 11 places a stop before the expensive wave so that an R3
costs the first release (about $44, section 12.3) rather than the whole plan.

**One reporting gap carried open from the Gate C review.** The review's
finding RT-182 (the no-verdict finding: the measure's own failure state has no
registered outcome term) is not closed by any ruling of 2026-09-25. This
version keeps the four terms above and reports an arm's *no verdict* in those
two words, as the rehearsal code does; what outcome a no verdict on arm C, M
or F maps to is decision 14 in section 15.

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

### 4.2 What "matched difficulty" means, concretely

Four things are matched, by construction in the generator and checked at the
rehearsal (MEASURED on the toy grammar: the four matched properties hold,
`docs/2026-09-21-successor-measure-rehearsal.md`, check P-1 and rehearsal item
R-1):

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
  function applies — ledger item RT-59, which turned out to need more than the
  one line it was first written as. It runs on every generator build.
- **The cue-detector gates.** Gates (i) and (ii) of the registered design (no
  surface cue in the curriculum text or the input tensors predicts which turns
  are the model's own) run unchanged on the new grammar. Gate (iii), the
  likelihood attack, runs in its act-withheld form as re-specified in Amendment
  A3 §3.4, because the policy at a revision position is perspectival and
  scoring another agent's turn under it with the acting channel present would
  read the model's ownership knowledge as a leak.

### 4.4 The named-other condition: what is on the record, and what is pending

**On the record (ruled 2026-09-25: the queue ruling, page 4, fallback (d);
the repairs rulings, item 1).** The registration text records that the
named-other condition failed its bar on two of three toy arms; that doubling
the training budget did not fix it; that a curriculum (the named-other
condition alone for the first 1,000 of 2,500 steps) and loss re-weighting
(the named-other loss four times the own-directed) did not fix it either and
both made it worse (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at
`e0626b2`, section 2, from `out-repairs/gate_curriculum.json` and
`out-repairs/gate_reweight.json`; check pending); and that the staggered first
run (section 11, step 5a) reads the learn-both result of one free-arm run
before the remaining runs are committed, which is what bounds the money.

**Stop condition S1 did not fire.** It asks whether the grammar is learnable at
tiny scale even in principle, and the separable arm learned both conditions to
1.0000 (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `e0626b2`, section
6.1, from `out-repairs/gate_base.json`). This is John's ruling, adopting the
rehearsal's adjudication (the queue ruling, page 4).

**The diagnosis, ARGUED and not ruled.** In this grammar the acting channel
fires on both action turns, so the two turns differ only in one word, and a
model that learns the own-directed route applies it at the named-other turn
too (the repairs findings, section 2, the paragraph headed "The reading").
That points at a grammar change rather than a training change.

**Pending: redesign (c), a grammar change, attempted on 2026-09-26** as its own
session at toy scale on the laptop at $0, with its pass line pre-stated before
the run: the named-other condition above the page 1b bar (section 8.1) on at
least two seeds of three on the free toy arm, with the own-directed condition
not degraded below its current level (the repairs rulings, item 1). When this
was written its branch carried nothing beyond the main line (the table at the
top of this document).

**What changes if it clears.** This version is amended before its Gate A: the
grammar in section 4.1 changes to the one that cleared, section 5.5's training
recipe with it, rehearsal items R-1 to R-6 are re-run on the new grammar and
their figures replace the ones cited here, the sentence on the record above is
rewritten to say what cleared and on how many seeds, and the honest prior in
section 3 is restated. **What changes if it does not.** Nothing: fallback (d)
is what registers, exactly as written above.

---

## 5. The four arms

All four train on the same grammar, at the same size (the registered 30M
configuration), on the same token budget, with the same launcher, watchdog and
network volume. What differs is the architecture, and only in the way the
ownership answer is allowed to exist.

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

What the rehearsal measured on its toy version: it reads **0.0000 on every
seed**, under the chance-corrected form and the ruled numbers, and its gate
and lesion figures reproduce the 2026-09-21 record exactly (MEASURED:
`docs/2026-09-26-rehearsal-repairs.md` at `e0626b2`, sections 6.1 and 6.2;
check pending). Its toy training reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

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
be high.** What the rehearsal measured on its toy version: it reads at the
entangled end, **0.99 to 1.00**, on every seed, with the ownership-only
transplant landing at the no-transplant rate (0.052 to 0.060 against a
whole-state 0.50 to 0.59), quoted as a range because this arm's training does
not reproduce (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `e0626b2`,
section 6.2; check pending).

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the rehearsal showing that its degree is
genuinely known by construction rather than merely intended, and that the
two-arm fallback is accepted in advance. This proposal keeps that exactly as
ruled; rehearsal items R-3 and R-6 in section 10 are the test, and at toy
scale both pass.

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable — but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. The registration text, if
the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker.

### 5.3 Arm M — a mixture of the two, by item (new in this version)

**Why it exists.** Section 3's admission: with anchors only at the two ends, a
free-arm reading at the entangled end cannot be told from a ceiling. John
ruled on 2026-09-25 that a fourth, partly separable arm would be attempted at
toy scale at $0, with its predicted reading stated before it ran, and folded
into the main registration only on a pre-stated pass: a chance-corrected
reading between 0.3 and 0.7 on all three seeds (the queue ruling, page 5,
option (iii)). It passed, and it is folded in (the repairs rulings, item 2).

**The construction** (the rehearsal's `experiments/rehearsal-successor-measure/src/arm_middle.py`,
method in `docs/rehearsal-repairs-method-2026-09-25.md`, section 5, both at
`e0626b2`): arm T's slot and head, and arm C's entangling and ordinary output
layer, in one network. Actions about some items go wholly through the
separable route and actions about the others go wholly through the entangled
route, so that about three fifths of actions are entangled (MEASURED on the
toy: 0.60375 of the 800 fresh episodes, 483 of 800, `out-repairs/measure_base_M.json`
at `e0626b2`, the field `entangled_share`; the findings' section 5 prints
this as 0.6033, a discrepancy this session flags for the pending check
rather than resolves). **The registration describes it as
what it is: a mixture by item, each action going wholly through the separable
or the entangled route, about three fifths entangled — not partial separation
within a trial** (the repairs rulings, item 2, in those words).

**The prediction, stated before it runs.** Write *p* for the entangled share,
and for each route write its whole-state and no-transplant accuracies. The
reading the measure should return, if the blind nomination catches the
separable route's slot and nothing of the entangled route, is the entangled
route's share of the total room the whole-state transplant moves:

    p × (whole_C − untouched_C) / [ (1 − p) × (whole_T − untouched_T) + p × (whole_C − untouched_C) ]

where the route accuracies are measured on the arm's own fresh episodes
(`docs/rehearsal-repairs-method-2026-09-25.md` at `e0626b2`, section 5, which
fixed this before the run). The registered prediction for arm M at the
registered size is the same in form: **between 0.3 and 0.7 on every seed, and
within 0.10 of that formula evaluated on the route accuracies measured on the
same fresh episodes.** The formula's value is computed and written down from
the measured routes before the blind reading is looked at.

**What the toy measured (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at
`e0626b2`, section 5, from `out-repairs/measure_base_M.json` and
`out-repairs/gate_base.json`; check pending).** The blind reading is **0.48 to
0.53** on the three seeds, quoted as a range because this arm has an
entangled route and is not expected to reproduce exactly; inside 0.3 to 0.7;
within 0.02 to 0.04 of the formula on its own routes (misses 0.021, 0.027 and
0.042). The number predicted from the record's arm C figures before the run,
0.42 to 0.43, was low, because arm M's entangled route learned better than
arm C does alone; the formula evaluated on the measured routes is the
prediction that held. Arm M passes the learn-both gate on both conditions on
all three seeds (own-directed 0.8613 to 0.8667, named-other 0.5517 to
0.5663). Its self-test passes all seven checks, including that perturbing the
slot never moves an entangled-route action (`out-repairs/self-tests.txt`).

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
envelope (section 12). **Arm M's seconds per step were not measured on the
rented machine**: the slice of 2026-09-25 timed arms T, C and F only
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `7da1946`, section
3). Its three runs therefore rest on ledger rows, not on rehearsal item R-11,
and section 12.4 says so.

### 5.4 Arm F — the freely trained system

The registered register-less configuration with the acting channel present —
the same architecture as the closed Amendment A3 runs — trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate and the ownership-lesion check in section 8.

What the rehearsal measured on its toy version, reported although the
registered procedure would not have read it: it **fails the learn-both gate**
(the named-other condition clears the bar on 1 seed of 3), and its reading is
at the entangled end, 1.00 to 1.003 (MEASURED: `docs/2026-09-26-rehearsal-repairs.md`
at `e0626b2`, sections 6.1 and 6.2; check pending). Under the ruled numbers
it would not be read at all. That is the honest prior of section 3, measured.

### 5.5 Seeds

**Three seeds per arm** (ruled 2026-09-25, the queue ruling, page 1f), giving
**twelve** registered runs across four arms. The registration says in terms
that the toy arithmetic implying one seed — the rehearsal's half-width
calculation, which the 2026-09-21 findings cautioned against carrying across
because the toy arms are far more repeatable than registered-size runs will
be (`docs/2026-09-21-successor-measure-rehearsal.md`, section 11) — was not
carried across. The training recipe is the rehearsal's unchanged recipe
unless the grammar attempt of section 4.4 clears.

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
nominated subspace*, and not *how many places you had to touch*. The
rehearsal's transplanting code proves the restriction as a tensor identity in
its self-test (rehearsal item R-8).

**One site set is not an intervention.** Copying the running state at every
position of a layer makes everything downstream of that layer the donor's own
computation, wherever ownership lives only in the running state; copying every
layer at every position is the donor's forward pass outright. Section 7.2
excludes every such site set by rule.

### 6.3 The number

For each arm, on fresh episodes:

- `accuracy_whole` — the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only` — the same share under the ownership-only
  transplant.
- `accuracy_untouched` — the same share with no transplant at all: the
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
different for every arm — the ceiling failure of Amendment A3 with the zero
replaced by a moving number (the Gate C review's finding RT-172, the
per-arm-ceiling finding, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`;
failure 1 of `docs/known-failure-modes.md`). The rehearsal confirmed it and
demonstrated the repair: on two made-up systems with the same true share
outside the subspace, 0.5, and different transplant strengths, version 1's
form read 0.4323 and 0.3222, and the chance-corrected form read 0.5018 and
0.5013 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`, section
5, from `out/denominator_simulated.json`). The top of the chance-corrected
scale is 1 on every arm.

**Readings outside 0 to 1 are reported as observed and never clipped** (the
repairs rulings, the paragraph after item 5). A negative reading means the
ownership-only transplant moved the action more than the whole-state one; a
reading above 1 means the ownership-only transplant landed below the
no-transplant rate. Both are sampling noise around "the subspace does
nothing" when small (the toy free arm read 1.0029 at one seed; the repairs
findings, section 6.2) and a warning about the instrument when large. The
rehearsal showed a negative value is reachable (rehearsal item R-4).

### 6.4 When the measure returns no verdict

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unequal
ceilings finding). This measure has a denominator, so it gets explicit
no-verdict rules, written before it runs:

1. **The floor (ruled, the queue ruling, page 1c; refined by the repairs
   rulings, item 4).** A site set is usable only if the whole-state transplant
   clears **four fifths of the arm's own own-directed accuracy on the same
   fresh episodes**, written on the chance-corrected scale:

       accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)

   The plain form, `accuracy_whole ≥ 0.8 × own_directed_accuracy`, is
   printed beside it everywhere, so a reader can see whether the two readings
   of the ruled sentence ever disagree; on the toy they never did (MEASURED: 0
   disagreements across all site sets, arms and seeds, the repairs findings at
   `e0626b2`, section 3). *Turning the ruled sentence into the first form is
   this design's choice and is marked ARGUED in the repairs method note.* If
   no site set clears the floor for an arm, that arm returns **no verdict** at
   nomination, and that is recorded rather than repaired. The floor keeps the
   denominator away from zero by construction: on an arm that has learned the
   task, `own_directed_accuracy − accuracy_untouched` is large, and the
   denominator is at least four fifths of it.
2. **The no-transplant sanity rule, replaced with the review's formula.**
   Version 1 said the no-transplant rate "should be near the one-in-eight
   guessing rate; if it is not, the pairing is broken and nothing is read".
   With distinct values that rule is pointed the wrong way round: a model that
   has learned nothing lands near one in eight and a model that has learned
   the task lands far below it (the Gate C review's finding RT-173; failure 3
   of `docs/known-failure-modes.md`). The registered rule is the review's
   formula: with *p* the arm's own-directed accuracy on the same fresh
   episodes, the no-transplant rate should be near

       (1 − p) / 7

   because an untransplanted model lands on the donor's answer only by erring
   onto exactly that one of the seven other slots. **The rule carries room
   for a miss of up to 0.0175** (the queue ruling, page 2), the largest miss
   the rehearsal measured against this formula (MEASURED: 0.0175 on the free
   arm at one seed, `docs/2026-09-21-successor-measure-rehearsal.md`, section
   5, from `out/denominator_floor.json`; on the repairs' fresh episodes every
   miss was inside 0.0132, the repairs findings at `e0626b2`, section 6.4).
   A measured no-transplant rate more than 0.0175 from the formula's value
   means the pairing is suspect, and nothing is read for that arm. The
   formula fires on the broken end and passes on the working end (the
   failure-mode pass filed with this version prints both).
3. **A reading outside 0 to 1** is reported as observed (section 6.3), not
   clipped and not suppressed.
4. **If a control that holds fails** (section 7.3 says which three hold), the
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

- **Training episodes** — what the arms are trained on.
- **Development episodes** — the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all. **The
  straight-line reads are fitted on development episodes, written to disk and
  reloaded**; they are never refitted on the episodes the reading is taken
  from (the rehearsal caught itself doing that and fixed it before any result
  was read: `docs/2026-09-21-successor-measure-rehearsal.md`, section 9, item 3).
- **Fresh episodes and confirmation seeds** — evaluated once, after the freeze.

**"Fresh" is disambiguated, as the rehearsal required** (its section 7, item
4). Version 1 asked for "marker and content combinations that appear in
neither of the other two sets", and that phrase has two readings. **The
registered reading is the weak one: unseen *combinations* of marker words,
items and values that the arm has each seen in training** — the rehearsal
grammar's pool named `fresh`, which draws from the training vocabulary with
its own seed (`experiments/rehearsal-successor-measure/src/grammar.py`, the
`POOLS` table). The strong reading — marker words the arm has never seen — is
**kept as a named diagnostic and is never the evaluation set**: under it the
separable arm's own accuracy fell to 0.7612, 0.6512 and 0.6512, the
whole-state transplant was capped there, and the reading went negative on two
seeds of three (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
section 7, item 4; the pool named `unseen-vocabulary` in the same grammar
file). The registration says which reading it means in these words.

### 7.2 Choosing the candidate ownership representation: one instrument

On development episodes only, for each arm, **identically**: one function,
which takes no argument that names an arm, called the same way for every arm
(the repairs' `experiments/rehearsal-successor-measure/src/repairs.py` at
`e0626b2` does this, and its nomination table shows one rule applied
throughout: the repairs findings, section 3). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy, the
same table).

1. **The label, and its route to the states.** The straight-line read is
   fitted against **which marker word is the model's own**. *The route by
   which that quantity reaches the model's states, in one sentence:* the
   marker word is the input token at every turn the model's own assignments
   are spoken on, so it is carried by the token into the running state, and
   which of the four marker words is the model's own is forced by the loss at
   the own-directed action, where the correct output depends on it and the
   acting channel is the only thing that tells the two apart. That is a route
   an agent's slot in the episode's list, or the marker's rank in dictionary
   order, does not have: nothing the model is shown or trained on requires
   either. Ruled 2026-09-23 (
   `docs/rulings/2026-09-23-nomination-label.md`; fixed in code as well as in
   text: the repairs code's `READ_LABEL = "marker-word"`, and the successor's
   measurement code when written, per the queue ruling, page 3). It is the
   only one of the three readings of "which agent is acting" that recovers a
   degree known independently of the instrument, and it recovers it exactly on
   all three seeds of the separable arm (MEASURED: that ruling's table). The
   other two readings — the agent's slot and the marker's rank — put an arm
   whose degree is zero by construction at the entangled end of the scale.
2. **Candidate sites: the rule, and the printed list.** The site list is
   registered as the rule that generates it (ruled, the queue ruling, page
   1e), and the registration prints the list the rule produces for the
   registered 12-layer architecture beside the rule, with the count of
   comparisons it implies, so the family correction is pre-stated. The rule:
   - **Positions**, grouped into the position sets the rehearsal used and
     registered here by name (`experiments/rehearsal-successor-measure/src/rehearse.py`,
     `CANDIDATE_POSITIONS`): the action position alone; the action position
     and the answer position after it; the action position and the three
     positions before it; every position from the model's first own turn to
     the action. (The rehearsal's fifth set, every position, is excluded by
     the rule below.) *That this grouping is what the ruled position clause
     means is this design's reading, marked ARGUED and put to John as
     decision 19; the repairs findings say the ruled clause does not itself
     say how positions are grouped.*
   - **Layers**: every contiguous set of the model's running states, counting
     the state after the input embedding as one and each of the twelve blocks'
     outputs as one more — 13 states, 91 contiguous sets.
   - **The exclusion, widened** (ruled, the repairs rulings, item 3): **any
     site set whose positions are all positions is excluded**, at any layer,
     not only every layer at every position. The reason is section 6.2's:
     copying all positions at a layer hands the donor's whole forward pass
     downstream. The narrower exclusion let the rule nominate such a set on
     arm C at two seeds of three (MEASURED: the repairs findings at
     `e0626b2`, section 3).
   - **The count.** The ruled figures before the widening were 296 on the toy
     and 1,816 on the registered model with the toy's five position sets (the
     repairs rulings, item 3; the packet's 176 was hand arithmetic and is
     superseded). With the all-positions sets removed, the rule gives **60 site
     sets and 240 comparisons on the toy, and 364 site sets and 1,456
     comparisons on the registered model** at four rank caps (MEASURED by this
     session; the command and its output are in the failure-mode pass filed
     with this version,
     `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md`).
     The list and the rule have to agree, and the registration prints both.
3. **Candidate directions.** At each site, fit the straight-line read for the
   label above and take its leading directions, at each of the rank caps
   **1, 2, 4 and 8**; **the registered cap is 8** and the search family
   reports all four (ruled, the queue ruling, page 1d).
4. **The layer set for the whole-state transplant: "the smallest that clears
   the floor", in one reading** (ruled, the repairs rulings, item 4). For each
   position set, the layer set with the fewest layers that clears the
   four-fifths floor of section 6.4, ties going to the earliest layers; a
   position set with no clearing layer set drops out. The other reading —
   the highest ownership-only share over every clearing site set — is
   computed and printed beside it as a sensitivity row. On the toy the two
   readings picked different site sets on **7 of 12** arm-and-seed pairs by
   the findings' text and the repairs rulings' item 4, and on **8 of 12** by
   this session's count from the same nomination files, which is also what
   the findings' own table lists; the ownership-only shares they reached were
   within 0.02 on every pair on either count (MEASURED: the repairs findings
   at `e0626b2`, section 3, and this session's recount in the failure-mode
   pass filed with this version). The discrepancy is flagged for the pending
   check of those findings; it does not change which reading is registered.
5. **Nominate by causal effect, not by how well the read fits.** Over the
   surviving (position set, its smallest clearing layer set) pairs and the
   four rank caps, the nominated configuration is the one with the highest
   *development-set ownership-only transplant accuracy*; ties go to the lower
   rank, then the earlier position set. This is the main lesson of the closed
   design: a representation that a straight-line read recovers beautifully can
   do nothing when you intervene on it.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference (on the toy: arm M's true-slot reading
   was 0.4572 to 0.4904 against its blind 0.48 to 0.53, the repairs findings,
   section 5). Judgment call; decision 1.
7. **The rider, in the reporting table** (ruled: John's addition, the queue
   ruling, page 3; kept in the table by the repairs rulings). For every arm
   and seed, the reading is also taken at **arm T's** nominated site set and
   rank for the same seed, using that arm's own read fitted at those sites,
   and reported beside the reading at the arm's own nomination, so a reader
   can see whether what differs between arms is their degree or where the
   procedure looked. **Where the whole-state transplant moves nothing at arm
   T's site set, the rider returns "no verdict", and that is itself the
   report.** On the toy it returned no verdict for arms C, F and M on every
   seed: at the first layer, at the action position, nothing about ownership
   has yet reached those arms' running states (MEASURED: the repairs findings
   at `e0626b2`, section 3, "The rider"). So the first thing the rider shows
   is that the arms cannot be read at the same place at all.

### 7.3 Controls

Every one of these is run on every arm. **Three of them hold** — a failure
means the reading is not made for that arm: control 7 (the null transplant),
control 3 (the matched random subspace), and control 1 on arm T only. **The
rest are reported** beside the reading, each with its pre-stated expectation,
and cannot veto it. This is the change the rehearsal required; version 1
made all seven hold.

1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.0175 room of section 6.4 (on the toy:
   0.0000 on every seed). *On arms C, M and F it is reported and cannot veto.*
   On an entangled arm the complement carries the ownership signal by
   construction — in a system where ownership multiplies content at every
   layer there is no ownership-free complement to transplant — so on such an
   arm the complement reproduces the counterfactual almost as well as the
   whole state does. On the toy entangled arm it reached 0.5375 against a
   whole-state 0.5400 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 6). In the repairs it reached 0.50 to 0.57 on arm C, 0.49 to 0.56
   on arm F and 0.36 to 0.42 on arm M (MEASURED: `docs/2026-09-26-rehearsal-repairs.md`
   at `e0626b2`, section 6.3). As version 1 wrote it, this control would have
   vetoed the reading on exactly the arm the control battery exists to
   validate, and on arm F it would have vetoed whatever the free arm turned
   out to be, which is the thing being measured. Its value on arms C, M and F
   is a description of how much of the identity-driven difference lives
   outside the nominated subspace, which is the reading itself seen from the
   other side.
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
   because it returns no verdict on an arm that has not. *Not applicable on
   arms T and M*, which hold the named agent outside the running state by
   construction, so no transplant into the state can move that action: on the
   toy, 0 of 44 site sets cleared the floor on arm T although it scores 1.0000
   on the named-other condition, and 0 of 44 on arm M (MEASURED: the repairs
   findings at `e0626b2`, section 4). Its mechanism is not reworded in this
   version. This is the successor's own obligation, not the closed design's
   control run on 2026-09-21 (the review's finding RT-181 on version 1's
   wording).
3. **Matched random subspace. Holds.** A random subspace of the same rank and
   the same norm at the same sites should not produce the donor's action above
   the no-transplant rate plus the 0.0175 room (on the toy: 0.0000 on arm T,
   0.049 to 0.071 on arms C and F against no-transplant rates of 0.049 to
   0.069, the repairs findings, section 6.3).
4. **A position where the answer is not yet knowable. Reported.** Transplanting
   before the identity can be known is expected to do nothing. Version 1 made
   this hold; the rehearsal found it reaching 0.14 to 0.16 on arm C and 0.06
   to 0.15 on arm F at their nominated sites, against no-transplant rates
   near 0.05 to 0.07,
   because those arms receive the ownership signal by other routes at those
   sites, so "before the identity can be known" is not "before the state
   differs" (MEASURED and ARGUED: the repairs findings at `e0626b2`, section
   6.3). *Changing it from a control that holds to a reported one is this
   session's call, not a ruling*, and is decision 16.
5. **Fresh marker and content combinations**, per section 7.1. By construction.
6. **Who is acting, versus which value. Reported, on the relaxed set.** The
   discriminating control. Trials are split into pairs whose donor identity
   dictates *the same* value as the recipient's and pairs where it dictates a
   *different* value. A transplant that has moved who is acting changes the
   action in the second group and not the first; a transplant that has
   smuggled a value across changes the action in both. **The first cell is
   empty by construction on the distinctness-preserving grammar** (0 of
   4,000 trials: MEASURED, `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 5, from `out/denominator_control6.json`; the Gate C review's
   finding RT-173; failure 3 of `docs/known-failure-modes.md`), so control 6
   runs on the **separately generated relaxed set** of section 4.2, in which
   one item per episode has two agents sharing a value. On that set both
   cells have trials: 81 same-value and 719 different-value trials of 800 per
   arm and seed on the toy (MEASURED: `out-repairs/measure_base_M.json` at
   `e0626b2`, the fields `6a same-value cell: trials` and `6b different-value
   cell: trials`; the count across all four arms is printed in the
   failure-mode pass filed with this version). Both cells are pre-stated and
   both are reported, with the one-in-four reference for a solver that cannot
   tell which agent it is restated for the relaxed set, where it rises (on
   the toy, from 0.2467 to 0.3095 on exactly the trials the relaxation adds;
   the 2026-09-21 rehearsal, section 5). Pre-stated expectation: the
   separable arm moves nothing in the same-value cell and everything in the
   different-value cell (on the toy, 0.000 and 1.000); an entangled arm moves
   the same-value cell too (0.59 to 0.72 on arm C, 0.17 to 0.32 on arm M), and
   that is reported as the caveat it is: on those arms the whole-state
   transplant carries something besides identity.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text;
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture, its exclusion, and the count of comparisons;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its rank, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it";
- the transplanting operation, as code, with its self-tests;
- all seven controls, which three hold, their pre-stated cells, the relaxed
  set for control 6 and its generating seed;
- the floor rule (four fifths, on the chance-corrected scale) and the
  no-verdict rules of section 6.4, including the no-transplant formula and
  its 0.0175 room;
- the separation bar between R1 and R2 (0.5);
- the learn-both threshold and the ownership-lesion threshold (section 8);
- the uncertainty method (section 9, 1g) and the seed count (three);
- the reporting table's columns, including the rider;
- the predictions: arm T near zero; arm C high; arm M between 0.3 and 0.7 and
  within 0.10 of the formula of section 5.3 evaluated on its measured routes;
  arm F unknown and not predicted.

Nothing on that list may be changed afterwards. If something on it turns out
to be wrong, the registered output is reported as it stands and the correction
is a separate, dated note beside it — the programme's existing practice, and
the process correction the outside review asked for: an immutable registration
is not an immutable scientific conclusion, but the two are kept visibly apart.

---

## 8. The gates every arm passes before it is read

### 8.1 The learn-both gate

No arm is read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, with its spread
  across seeds. Not combined into one number, not normalised by anything.
- **The threshold, per condition (ruled, the queue ruling, page 1b):** the
  condition's accuracy is above the one-in-four level at the 0.05 level under
  a one-sided binomial test, **on at least two seeds of three**. The ruling
  writes the bar as "above 0.2630"; on 3,000 held-out episodes that is 790 or
  more correct, a share of 0.2633 (MEASURED: the bar's derivation is printed
  in `docs/rehearsal-repairs-method-2026-09-25.md` at `e0626b2`, and
  `out-repairs/gate_base.json` carries it as the field `bar`; this session
  re-derived it, and the derivation is in the failure-mode pass filed with
  this version); at the registered episode count it is the same rule,
  recomputed and printed.
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal — one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, the repairs findings, section 6.1).
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.
- **What is already on the record about this gate** is section 4.4: at toy
  scale the free arm fails it on the named-other condition, and no training
  change fixed that.

### 8.2 The ownership-lesion check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation — the lesion
the existing code already performs. **The pre-stated shape (ruled, the queue
ruling, page 1h):**

- **own-directed accuracy falls below the section 8.1 bar** — that is the
  collapse, and it gates;
- named-other-directed accuracy is **reported and not gated**; the pre-stated
  expectation that it holds is a description, because the rehearsal found
  that shape is architecture-specific (`docs/2026-09-21-successor-measure-rehearsal.md`,
  section 8);
- the ownership-free state and syntax batteries **must hold**.

**What this check does and does not establish, in the closed design's own
registered words: it removes a sense organ, not a structure the network
built.** It is a precondition for reading arm F — it shows the ownership
answer is load-bearing for the act, which is what makes arm F worth measuring
— and it is not evidence of a centre and is never reported as such.

Arms T, C and M do not take this check as a gate: their dependence on
ownership is architectural. Their lesion results are computed and reported as
a description of the constructed systems (on the toy: all three collapse,
the repairs findings, section 6.1).

---

## 9. The numbers, now set

Every number version 1 deliberately left blank is now filled from John's
rulings of 2026-09-25, each citing the ruling that set it. **None was
invented here.** The registration text freezes them in this form.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form, per seed | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a. The toy cleared it on every seed, at 0.9977, 0.9927 and 1.0000 (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `e0626b2`, section 6.2, from `out-repairs/summary_base.json`) |
| Learn-both threshold, per condition (R3) | above one in four at the 0.05 level, one-sided binomial, on at least two seeds of three: **0.2630 on 3,000 held-out episodes**, or the same rule at the registered count; the ownership-blind and name-only solvers reported beside it as references | the same ruling, page 1b |
| Floor on the whole-state transplant (whether a reading is valid) | **four fifths of the arm's own own-directed accuracy** on the same fresh episodes, on the chance-corrected scale; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded | the same ruling, page 1c; the two refinements are items 3 and 4 of `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the same ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model; the count is the rule's output, not hand arithmetic | the same ruling, page 1e; the repairs rulings, item 3 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the same ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so | the same ruling, page 1g; on the toy the two disagreed by more than two to one on arms C and F (0.0466 and 0.0499 across seeds against 0.019 to 0.020 within), the repairs findings, section 6.2 |
| Ownership-lesion collapse threshold (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed; the named-other clause reported and not gated; the ownership-free batteries must hold; gates arm F only | the same ruling, page 1h |
| The form of the reading | **the chance-corrected form** of section 6.3 | the same ruling, page 2 |
| The label | **which marker word is the model's own** | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3 |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `7da1946`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json` (check pending). **Arm M was not timed.** Whether fifty steps meets item R-11's five hundred is decision 17 |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of the formula of section 5.3 on its measured route accuracies | the queue ruling, page 5 (the band); the repairs method note at `e0626b2`, section 5 (the formula and the 0.10) |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). It ran in two parts, both at toy scale on the laptop:
the rehearsal of 2026-09-21 (`docs/2026-09-21-successor-measure-rehearsal.md`,
code in `experiments/rehearsal-successor-measure/`, re-run from code on
2026-09-22 with the separable arm reproducing exactly and the other two not)
and the repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at
`e0626b2`, code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`; check pending). The one part that spent money is item R-11.
Total spent on the rehearsal so far: about $0.57, the sum of the compute
ledger's three slice rows, of the rehearsal line's $10 (item 10 of the
2026-09-21 ruling; section 12.3).

**A pre-stated quantity the rehearsal never exercised is a fatal finding on
its own** (item 5 of the 2026-09-21 ruling). Each item below therefore says
what exercised it.

- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  The four matched properties hold (P-1). The own-directed condition learns on
  every arm. **The named-other condition does not clear the bar on the free
  arm on a majority of seeds, under any of three training recipes** (section
  4.4). Stop condition S1 is ruled not to have fired; fallback (d) is on the
  record; the grammar attempt is pending. *Exercised; the finding is the
  honest prior, measured.*
- **R-2. Arm T is constructible and its ownership slot is transplantable on
  its own — and so is arm M's separable route.** The blind nomination finds
  arm T's slot without being told where it is, on every seed, and reads
  0.0000; on arm M the blind subspace catches 0.92 to 0.96 of the separable
  route's effect (the repairs findings, sections 3 and 5). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction — and arm M's mixture reads between the anchors in its
  pre-stated band.** No nominated subspace reproduces the counterfactual on
  arm C while the whole state does (ownership-only at the no-transplant rate);
  arm M reads 0.48 to 0.53 against a band of 0.3 to 0.7 and a formula it
  matched within 0.04 (section 5.3). *Exercised; the two-arm fallback does
  not fire.*
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1), above one (the free arm at one seed), and no verdict (arm C's
  first layer alone in the 2026-09-21 sweep; control 2 on three arms).
  *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised.*
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the floor; the no-transplant formula was checked against
  nine arm-and-seed pairs on 2026-09-21 and twelve on 2026-09-25; two
  made-up systems of equal true share and unequal transplant strength read
  the same under the registered form (section 6.3). *Exercised.*
- **R-7. Throughput, per arm, projected to dollars.** Done from item R-11's
  measured ratios on the measured cost of a registered-size run (section
  12.4). *Exercised for arms T, C and F; arm M's runs are priced from ledger
  rows.*
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant leaves every logit bit-identical on every arm and seed; the
  ownership-only transplant is proved a restriction of the whole-state one;
  a transplant on arm T moves the action to the donor's value. *Exercised.*
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21 and 0.99 to 1.00 on 2026-09-25. *Exercised.*
- **R-11. Seconds per step on the rented machine, all three arms — and the
  shutdown path against the real vendor.** Measured on 2026-09-25 on the
  second attempt at the rented slice, after a first attempt that hung and was
  stopped with neither measurement taken (`docs/2026-09-25-rented-slice-findings.md`,
  main line). Throughput: **PASS**, three figures with their spread, fetched
  home (section 9). The shutdown handshake: **the laptop half passed against
  the real vendor — copy, checksum, receipt written, delete, confirmed gone —
  and the machine half was not exercised**, because the laptop deletes the
  machine in the same second it writes the receipt, so the machine's own
  "receipt found" can never be observed on the normal path (MEASURED and
  ARGUED: `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `7da1946`,
  section 4; check pending). None of the slice's six pre-stated handshake
  lines fits, and the findings do not force one. **Two things this leaves
  open, put to John in section 15**: fifty timed steps were run where the
  item says five hundred (decision 17), and the machine half of the handshake
  is still untested (decision 18). Cost: about $0.57 across three rows against
  the item's $3 (section 12.3).

**What happens next.** This version goes to its Gate C tier 1 review; if the
grammar attempt clears, it is amended and items R-1 to R-6 re-run before Gate
A; John rules on section 15; the registration text (version 3, with every
frozen number and the printed site list) goes to Gate A, both tiers; the
registration commits when both tiers are answered and he rules. There is no
target date; the only date is the kill date of 2026-10-18 (section 11).

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. Gate C tier 1 on this version → John's rulings on section 15 → the grammar
   attempt's outcome folded in or not (section 4.4).
2. Registration text (version 3) with every frozen number and the printed site
   list → **Gate A, both tiers** → registration commit. **No target date.
   Kill date 2026-10-18**, past which committing it takes a fresh ruling
   naming what comes off the back end (item 23 of the 2026-09-21 ruling).
3. Implementation frozen; unit tests; the even-split rule and the
   one-scored-token self-test run on the built generator; the tripwire of
   section 12.5 written into the launch preconditions beside the sleep guard
   and the argument guard (the queue ruling, page 6, "Changes").
4. Development runs at the 10-million size, four arms, one seed each. **This
   is a pipeline and throughput check, not a learnability verdict** — the
   10-million size failed to learn the earlier design's task, so a null here
   means nothing about the registered size, and the registration says so in
   advance.
5. **The staggered launch, in two steps, as ruled 2026-09-21** (item 12 of
   that ruling; steps 5a and 5b of the roadmap chain).
   - **5a. One arm F run at the registered size launches first**, on John's go
     naming it, inside the first release (section 12.3). Two things come back
     before anything else launches: whether it passes the learn-both gate, and
     what the machine actually bills (the tripwire, section 12.5). If it fails
     the gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches.
   - **5b. The remaining eleven registered runs** — two more of arm F, three
     each of arms T, C and M — launch only after 5a's learn-both result is
     read and its billing found normal, the second release is asked for and
     ruled, and John gives the go. **Kill date 2026-11-01 binds this step, not
     5a** (item 23 of the 2026-09-21 ruling): past it, launching takes a fresh
     ruling naming what comes off the back end.
6. Nomination on development episodes as arm F checkpoints arrive; frozen and
   committed; transplants on fresh episodes, all arms. The measure computed on
   arms T, C and M: that is the validation result.
7. **Gate B** on the validation. John rules: read arm F, or close on R2 or R3.
8. If R1: arm F read on the frozen procedure, confirmation seeds; findings;
   Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
   state the chain is in.

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). **Ruled on 2026-09-25 not to have fired** (the
  queue ruling, page 4): the separable arm learned both conditions to 1.0000
  and the transplanting code passes. The named-other failure on the free arm
  is fallback (d), on the record in section 4.4, not S1.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded. At toy
  scale R-3 passed.
- **S3.** The rehearsal fails item R-4 or R-6. The measure is not registered.
  At toy scale both passed.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the
  whole first release, which since item 19 of the 2026-09-21 ruling includes
  the re-run (section 12.3). (Version 1 stated this outcome's cost two ways;
  the review's finding RT-178 caught it, and item 19 removed the gap.)
- **S5.** Cumulative actual spend reaches the release John has authorised —
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
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**
  — missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over (item 15 of the 2026-09-21 ruling; section
  12.7). Control 2's *not applicable* on arms T and M is not an instance of
  this: it is a ruled disposition with the reason on the record (section 7.3).
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
| Spent across the programme, as of the last row on the main line | **about $228.1** | the ledger's 2026-09-25 row for the rented slice's first attempt, "After this run" |
| Spent, as of the second attempt's row | **about $228.15** | the ledger's second 2026-09-25 row, on branch `worktree-mvm-w1f-rented-slice-attempt-2` at `7da1946` (check pending) |
| Amendment A3 against its $100 stop | **about $46.75** | the same branch row |
| The rehearsal line of the first release, spent | about $0.02 (2026-09-21), about $0.50 (first attempt), about $0.05 (second attempt); **about $9.43 of $10 remains** | the same branch row |
| Headroom before the successor's two releases | **about $221.85** | $450 minus about $228.15, arithmetic on the two rows above; not a figure the ledger states |

Version 1 was written against a $400 ceiling and a running total of about
$225.70, and two dated notes at its end carried it to about $227.60 — all
three figures the compute ledger's on their day (its 2026-08-16 top-up note,
its 2026-09-20 row and its 2026-09-21 correction). The rows above supersede
them.

### 12.2 What is ruled, and what this section is built to

- **The flat $130 cap of 2026-09-20 is superseded** by the two releases of
  the 2026-09-21 ruling (items 10, 11 and 19 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, with
  its correction note of 2026-09-22: about $44 and about $131). That sentence
  is the closure of the review's finding RT-176 (the $175-against-$130
  finding), and a dated annotation goes beside item 4 of the 2026-09-20 ruling
  (the queue ruling, page 6, part 1).
- **The envelope is $450** (the queue ruling, page 6, part 2, recorded in the
  compute ledger's ceiling note of 2026-09-25). What it was
  ruled to buy, on the ledger rows the packet cited: the base plan of about
  $175 on top of about $227.63 spent, plus one extension of $32 to $44 (arm
  M) or about $36, with $3 to $15 left. It does not hold two extensions. The
  measured figures below leave more room than that arithmetic did.
- **The second release is asked for only after seconds per step were
  measured on the rented machine** (item 11 of the 2026-09-21 ruling). They
  were, on 2026-09-25 (section 9). The ruling changed the ceiling, not that
  gate.
- **The staggered launch** (item 12), **halt not trim** (item 13), **funding
  per wave** (item 14) and **a check that cannot run is a trip** (item 15) all
  stand; sections 11, 12.5, 12.6 and 12.7.
- **The pre-authorisation scheme** of `docs/preauthorised-spending-proposal-2026-09-21.md`
  **is not adopted** (the queue ruling, page 6, part 3). Only its tripwire is.

### 12.3 The first release: about $44, ruled 2026-09-21

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| The rehearsal | Tiny models, the transplanting code, rehearsal items R-1 to R-11, including the rented slice | item 10 of the 2026-09-21 ruling: up to $10. Spent so far: about $0.57, the sum of the ledger's three slice rows (about $0.02 on the 2026-09-21 row, about $0.50 and about $0.05 on the two 2026-09-25 rows, the second at `7da1946`), leaving about $9.43 by that branch row's own running line | up to **$10** |
| Development runs | Four arms, one seed each, at the 10-million size: pipeline, self-tests, throughput | item 10: up to $10. The ledger's reconciliation of 2026-08-12 trues the earlier 10-million run up to $1.943 | up to **$10** |
| One free-arm run at the registered size | Step 5a of section 11 | item 10: about $12. The measured cost of a registered-size run is $10.04 (the ledger's 2026-09-17 row: $20.08 for two runs) | about **$12** |
| The one permitted re-run | If step 5a fails the learn-both gate | **item 19: folded into the first release**, at the same planning figure | about **$12** |
| **First release, total** | | | **about $44** |

This is the release John has authorised; nothing beyond it is launchable
without the second. Stop conditions S4 and S5 in section 11 are stated
against it.

### 12.4 The second release: from the measured seconds per step, then arm M

**What the second release is bound to, and now has.** Item 11 bound it to
rehearsal item R-11's measured seconds per step for arms T, C and F on the
registered venue. Those were measured on 2026-09-25 (section 9), and the
dated note beside the spending proposal recomputed the release from them
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
at `7da1946`; check pending). The method, in the note's own words, is
MEASURED arithmetic on an ARGUED method: the measured seconds cannot be
turned straight into hours for a run (a timed step holds 1,792 tokens where a
registered step held about 10,624, and a real run also generates its data,
evaluates and saves), so the note does what version 1's spending arithmetic
did, with the measurement in place of the inference — **the measured cost of
a registered-size run, $10.04 (the ledger's 2026-09-17 row), times each arm's
measured ratio.** Every figure below is the note's, printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
into `second-release-arithmetic.txt` beside it.

| Per run | Version 1's planning figure | From the measurement |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** (ratio 1.044) |
| Arm C | $12 | **$10.84** (ratio 1.080) |
| Arm M | — | **not measured**; priced from ledger rows below |

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

**Then arm M's three registered runs: $32 to $44** (the queue ruling, page 5,
and page 6's envelope; the repairs rulings, item 2), from the ledger's per-run
rows rather than from item R-11, because arm M was not timed on the rented
machine. The range is: three runs at what the last three clean runs billed
(about $29.70 to $30.12), or $36 at the planning figure, or up to about $41.76
if each billed as the 2026-09-15 pilot did with its idle time, plus about
$1.94 for one development run at the 10-million size (page 5 of
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`, from the ledger's
2026-09-19, 2026-09-17, 2026-09-15 and 2026-08-12 rows). Arm M's runs are in
the second release (the repairs rulings, "What this changes": section 12.4).

**The whole successor, and the programme after it.** Arithmetic on the
figures above; no ledger row states these totals.

| | |
|---|---|
| Both releases before arm M | about $161.90 |
| Arm M's three runs | $32 to $44 |
| **The successor, all in** | **about $194 to $206** |
| Spent before it | about $228.15 |
| **Programme after the successor** | **about $422 to $434 of $450** |
| **Left** | **about $16 to $28** |

The repairs ruling's own sentence — arm M's runs "with the two releases
recomputed from the measured seconds per step ($161.90) leaves the programme
at about $434 of $450" — is the top of that range. **The second release is
asked for on these figures or not at all**, and the request carries the
measured figures beside the provisional ones so the movement is visible. Two
things that could still move it, stated so they cannot arrive quietly: the
first free-arm run of step 5a gives arm F's own run cost, and the eight later
runs of arms T, C and F are to be repriced from it before the second release
is drawn (the note's "what this does not settle", item 2); and arm M's per-run
cost is a ledger inference until a run of it exists.

### 12.5 The tripwire: 1.25, halt not trim, with the in-flight clause

**Adopted on 2026-09-25** (the queue ruling, page 6, part 3), from sections
5.3 and 5.4 of `docs/preauthorised-spending-proposal-2026-09-21.md`, whose
pre-authorisation scheme is not adopted. Two ratios are measured, because the
authoritative one is slow and the fast one is rough:

- **Ratio A, authoritative: billed hours divided by machine-existence hours**,
  per machine, from the vendor's own billing rows — the quantity rule 4 of the
  compute ledger already reconciles at phase boundaries, and the one the
  2026-08-08 anomaly was recorded in (8.47 billed against 2.42 existed, the
  ledger's 2026-08-07/08 row).
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
   covers it — the spending proposal's own clause (its section 5.4, item 2):
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
work owed before step 5a, and not done by this document. It runs in flight,
hourly, on ratio B from the first hour of the first machine; before the
second machine of any wave is created; and at each wave boundary on ratio A,
reconciled to the ledger.

### 12.6 The account is funded per wave, not per release

Unchanged from version 1 and from item 14 of the 2026-09-21 ruling: the rented
account is prepaid with automatic reload off, and **topped up to the estimate
for the wave about to launch plus $20, and no further**, so that no anomaly of
any size can cost more than that, because there is nothing else in the account
to spend. This is the only control in the programme's history that held when
everything else failed (2026-08-12). The vendor balance stood at $75.8645 on
2026-09-26T01:54Z (the ledger's second 2026-09-25 row at `7da1946`), which is
above what step 5a's estimate plus $20 would call for; the rule caps what is
topped up, not what is already there.

### 12.7 A check that cannot be run counts as a trip, not a skip

Item 15 of the 2026-09-21 ruling, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate, a stop condition or a tripwire check cannot
be evaluated — the data is missing, the code will not run on the artifact, the
measurement was never taken, the balance query returns an error — **the check
counts as failed and its consequence fires.** It is never recorded as not
applicable and stepped over, and it is never deferred past the launch it was
supposed to gate. Written into section 11 as stop condition S8 and into the
tripwire as its fifth line.

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used. **Version 1's
wager — that the rehearsal measures a per-run cost at or below the $12
planning figure — survives on the 2026-09-25 measurement: the dearest timed
arm is $10.84** (the note at `7da1946`). The wager this version makes: **the
twelve registered runs, with arm M's three priced from ledger rows, complete
inside the $450 envelope with three seeds on every arm carried and at least
$16 left.** If measured spend approaches the second release's ruled figure
with runs missing, **the report is the shortfall, never a second raise.**

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

**W2. The reading is relative to the site set — and the arms cannot be read
at the same site set.** A different frozen site set could give a different
number. Mitigated by one pre-stated rule applied identically to every arm, and
by saying in the registered text that the reading is the degree *at the sites
this procedure nominates*. The rider makes the second half of this weakness
visible rather than hidden: at arm T's site set, arms C, F and M return no
verdict on the toy (section 7.2, item 7), so what differs between arms is
first of all where the procedure has to look.

**W3. Arm C's degree was an intention until the rehearsal showed otherwise —
and the toy is not the registered model.** At toy scale no nominated
subspace carries the counterfactual on arm C (section 5.2). A network built
with ownership multiplied into every layer could still, at 30 million
parameters, learn to concentrate it in a low-rank direction, in which case
arm C's anchor collapses into a second copy of arm T. The registered-size
nomination is the test, and its failure fires the two-arm fallback rather
than a repair.

**W4. The whole-state transplant may fail for arm C at the registered size.**
If ownership in arm C is spread across layers the site-set rule does not
cover, no site set clears the floor and arm C returns no verdict — honest, but
it leaves the experiment with no high anchor by another route. The rule of
section 7.2 covers every contiguous layer set precisely to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is R3, and it is now measured at toy scale, not
predicted.** Section 4.4. The staggered launch makes that outcome cost the
first release, about $44, instead of the whole wave.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text; decision 9.

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. Mitigated by nominating at positions away
from the acting positions, by control 2 on the arms it can run on, and by
reporting the gap between the lesion result and the transplant result
honestly. The rider sharpens it: at the first layer at the action position,
which is where arm T's slot sits, the other arms show nothing, so their
nominated sites are downstream of the acting channel's injection and not at
it.

**W8. The per-run cost is measured for three arms and inferred for the
fourth, and the measurement is fifty steps, not five hundred.** Section 12.4
prices arms T, C and F from the 2026-09-25 measurement and arm M from ledger
rows. Item R-11 as written asks for five hundred timed steps per arm; the plan
John authorised timed fifty, and the spread was tight (each arm's slowest
step within 3% of its median), so the ratios are unlikely to move much with a
longer window — that is argued, not measured (the slice findings at
`7da1946`, section 3). Decision 17.

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor.** The laptop half has (section 10, R-11). On the normal
finishing path the laptop deletes the machine the moment it writes the
receipt, so the machine's own "receipt found" is close to unobservable by
construction; the watcher is a backstop for a laptop that never answers, not
a tested primary. Twelve registered runs inherit that. Decision 18 puts the
two ways forward to John.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. Control 6 says the whole-state transplant carries more than identity
on the entangled arms.** On the relaxed set, the same-value cell moves in
0.59 to 0.72 of trials on arm C and 0.17 to 0.32 on arm M, where a transplant
that moved only who is acting would move none (section 7.3). On those arms
the reading cannot be read as purely a statement about where the ownership
answer lives. It is reported as the caveat it is, on every arm, in the
reporting table.

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
  amend them. Its failure-mode pass is filed beside it (section 16).
- **The dates.** Registration by 2026-10-18 and the remaining runs of step 5b
  launched by 2026-11-01, each a kill date in the sense of item 23 of the
  2026-09-21 ruling (a fresh ruling to go past, never a quiet drift); wrap-up
  starting 2026-12-21; the hibernation condition complete by 2027-01-04. No
  2026-10-11 target.

---

## 15. Decisions for John

Each with how confident the recommendation is, whether it is ordinary practice
or a judgment call, and the strongest alternative, so nothing is inherited by
default. Version 1's thirteen are kept under their numbers; the ones ruled
since are marked so and carry the ruling; six new ones follow.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references.

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Confidence: high. Judgment call. Not yet ruled.* **Alternative:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for — a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Confidence: moderate, raised by the toy result of section 5.2. Judgment
   call. Not yet ruled.* **Alternative:** train arm C with a penalty that
   punishes any linearly transplantable ownership direction, which trains the
   system against the very instrument that will measure it. Recommended
   against.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Confidence: high. Standard practice for intervention comparisons.
   Not yet ruled.* **Alternative:** transplant the whole forward state at every
   layer as the denominator, which always succeeds and turns the measure into a
   report on how the sites were chosen.

5. **The registered reading is the chance-corrected form, with the raw
   difference and both accuracies reported alongside, always, plus the floor
   and the no-verdict rules.** *Ruled 2026-09-25 (the queue ruling, page 2).*

6. **Three seeds per arm.** *Ruled 2026-09-25 (page 1f).*

7. **The money goes in two releases.** *Ruled 2026-09-21 (items 10, 11 and 19)
   and 2026-09-25 (the queue ruling, page 6); section 12 is built to them.*
   The one number John should see before it can surprise him: the whole
   successor is about $194 to $206 and the programme after it about $422 to
   $434 of $450, leaving about $16 to $28 (section 12.4).

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. *Confidence: high.
   Standard practice. Not yet ruled.* **Alternative:** number it as a further
   amendment, which keeps one budget instrument and one ledger but attaches
   new work to a closed registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Confidence: high. Judgment call. Not yet ruled.*
   **Alternative:** add a condition in which the model's own name appears as a
   token, which would match the conditions exactly and would put an ownership
   cue into the text. Ruled against here; John's call. *If the grammar attempt
   of section 4.4 clears, this decision is re-put with the new grammar beside
   it.*

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Its shape is ruled (page 1h);
    the standing as a precondition and not a finding is version 1's
    recommendation and not yet ruled. Confidence: high. Standard practice, and
    the closed design's own registered wording.*

11. **The registered wave launches staggered**: step 5a, then 5b. *Ruled
    2026-09-21 (item 12), with item 23 settling which step the second kill
    date binds.*

12. **This proposal goes to Gate C tier 1 before John rules on the open items
    above**, per the protocol. *Confidence: high. Standard practice here.*

13. **The successor's registration names a launcher that waits for the
    receipt, and makes "the trainer does not delete its own machine" part of
    the registered recipe.** *Confidence: moderate. Judgment call. Not yet
    ruled, and now with the vendor result in hand*: the laptop half of the
    handshake works against the real vendor and the machine half was never
    given the chance (section 10, R-11). **Alternative:** leave the shutdown
    policy in unregistered operations scripts, where a later edit can quietly
    remove it. (Version 1's account of what one failure cost merged two events;
    the review's finding RT-186 corrected it, and the sentence is not repeated
    here.)

14. **What a no verdict maps to** (the review's finding RT-182, still open).
    Recommendation: a no verdict on arm C fires the two-arm fallback already
    ruled in advance; a no verdict on arm M drops arm M and carries it as
    extension E0 on the weekend roadmap; a no verdict on arm F after arms T and
    C have separated is reported in the words *metric validated, degree not
    read*, as a fifth registered term. *Confidence: moderate. Judgment call.*
    **Alternative:** keep four terms and report an arm F no verdict under R1
    with a sentence, which is the over-reading the finding warns against.

15. **Control 2's pre-stated tolerance on arms C and F: 0.05** over the random
    subspace, the rehearsal's number (section 7.3, item 2). *Confidence: low on
    the number, which was a rehearsal-only tolerance chosen before any figure
    existed; high that a pre-stated number is needed. Judgment call.*
    **Alternative:** the 0.0175 room of the no-transplant rule, one number for
    every "no more than the null" check in the design, which is tidier and may
    be too tight for a control that moves an action rather than reads one.

16. **Control 4 is reported, not a control that holds** (section 7.3, item
    4). *Confidence: moderate. Judgment call, this session's own.* On the toy
    it did not reach "nothing happens" on arms C and F at their nominated
    sites, for a reason the findings give; as version 1 wrote it, it would veto
    the reading on those arms. **Alternative:** keep it as a control that
    holds and anchor it at a position the nominated sites cannot reach,
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
    findings' section 9 (at `7da1946`): (a) make the laptop wait, after
    writing the receipt, up to twice the watcher's polling interval before
    deleting, and have the watcher write its "receipt found" somewhere the
    laptop fetches — standard practice for a two-party shutdown, moderate
    confidence that it lets a pass be observed; (b) leave the design as it is
    and register that on the normal path the laptop is the reap and the
    watcher is the backstop, which is what can honestly be said today and
    costs nothing more to rent. Recommendation: (b) for the registration text,
    with (a) as the fix if a later wave shows the laptop failing to answer.
    *Confidence: moderate. Judgment call.*

19. **The position sets of section 7.2 are the rehearsal's four, by name.**
    The ruled position clause does not say how positions are grouped
    (the repairs findings, section 3); registering the rehearsal's grouping
    is the only one that has been exercised. *Confidence: moderate. Judgment
    call.* **Alternative:** register the ruled clause literally — the action
    position and each position between the source assignment and the action,
    one set each — which has not been run and would change the count.

*Nothing above is registered. The registration commit, if it comes, follows
the Gate C pass, John's decisions, the grammar attempt's outcome and Gate A,
and every run it affects is launched after it.*

---

## 16. Where the pieces are

- This proposal: `docs/successor-experiment-proposal-2026-09-26-v2.md`.
- Version 1, unedited: `docs/successor-experiment-proposal-2026-09-21.md`.
- The failure-mode pass this version was run through, filed with it:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md`.
  It is the author's run of the list; the Gate A tier 1 reviewer's own pass
  is still owed, as the protocol says.
- The Gate C review of version 1, whose two fatal findings this version
  repairs: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
  (RT-172 to RT-188).
- The rulings this version is built to: `docs/rulings/2026-09-26-weekend-1-queue.md`
  (nine pages, 2026-09-25); `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`
  (five decisions, on branch `rulings-2026-09-25-repairs`);
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (the
  releases, the staggered launch, halt not trim, item 23 on the dates);
  `docs/rulings/2026-09-23-nomination-label.md` and
  `docs/rulings/2026-09-23-range-and-direction-only.md`;
  `docs/rulings/2026-09-20-center-as-degree.md` and
  `docs/rulings/2026-09-20-december-result-roadmap.md`.
- The two rehearsals: `docs/2026-09-21-successor-measure-rehearsal.md` (main
  line) and `docs/2026-09-26-rehearsal-repairs.md` (branch
  `worktree-w1c-rehearsal-repairs` at `e0626b2`, check pending), with their
  method notes `docs/successor-measure-rehearsal-method-2026-09-21.md`, its
  denominator addendum, and `docs/rehearsal-repairs-method-2026-09-25.md`;
  code and outputs under `experiments/rehearsal-successor-measure/`.
- The rented slice: `docs/2026-09-25-rented-slice-findings.md` (first attempt,
  main line) and `docs/2026-09-25-rented-slice-attempt-2-findings.md` with
  the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  (branch `worktree-mvm-w1f-rented-slice-attempt-2` at `7da1946`, check
  pending).
- Amendment A3's closure, registered: `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
  the closure block of 2026-09-25, and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
- The roadmap it implements: `docs/december-result-roadmap-2026-09-20.md`,
  sections 2, 4 and 5 as amended 2026-09-21; the weekend schedule laid over
  it, `docs/weekend-roadmap-2026-09-24.md`.
- The spend record every figure in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, with its
  ceiling note of 2026-09-25 and its rows of 2026-09-21 and 2026-09-25 (the
  second of those on the branch named above).
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate C now and Gate A later, with the list it is run against,
  `docs/known-failure-modes.md`.
- The Wittgenstein note cited in section 2 as non-binding motivation: the
  TimeAssembler document `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
  Minimum Viable Mind project; not a file in this repository.

---

## What this version does not do

It edits nothing: not version 1, not any ruling, registered text or protocol
text. It issues no go, releases no money, launches nothing and rents nothing.
It does not close the review's finding RT-182 or rule on any of the open
decisions in section 15. Under the pairing rule of
`docs/outside-review-protocol.md` it is checked by a session that did not
write it — the Gate C tier 1 reviewer of `docs/weekend-1-session-prompts.md`,
section (d) — before anything relies on it.
