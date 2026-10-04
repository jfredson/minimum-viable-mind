# Successor experiment, proposal version 4: reading how much of the act is organised around who is acting

*Written 2026-10-03 (Pacific) by the Claude Code session "MVM proposal version
4 draft", in its own worktree (branch `claude/vigorous-jang-3f7d20`, cut from
the main line at `f32ba0c`). **Status: PROPOSAL, version 4. Nothing here is
registered and nothing here binds.** It is version 3
(`docs/successor-experiment-proposal-2026-09-26-v3.md`, main line at
`6d4ec3a`, pull request 71, left unedited) with John's three sets of rulings
of 2026-10-03 written in, every frozen number stated, and the site list
printed (section 18). It is the text intended for Gate A of
`docs/outside-review-protocol.md` (the registration review, both tiers).
Opening that review is a later step and John's to start. No money is spent
and no machine is rented by this document.*

**This version cannot go to the registration review yet. Three things stand
in front of it.**

1. **This version is owed a check by a session that did not write it**,
   under the pairing rule of the protocol. So is the record of John's
   late-evening ruling on its seven questions, which the same session wrote.
2. **One more short run is owed: the ordinary competing solver, put through
   the measurement as now registered.** John ruled on 2026-10-03 that it is
   run before the registration review opens, at $0, method committed before
   output, by a session other than this one (section 7.3, the last
   paragraph).
3. **Opening the registration review is John's step.**

**Two things that stood here in the first commits of this version are
settled.** The check of the short pre-stated run and of the evening ruling's
record did not exist when this draft was begun; it was filed while the draft
was being written, finds that both hold, and is on the main line at `53c8100`
(pull request 82). And the seven questions this version put to John in
section 19 were ruled the same night, in the words "Agreed on all"
(`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`); each is written
into the body where it bears.

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

Every source but one is on the main line and is cited by its main-line
commit. The one that is not is the last ruling, which is filed with this
version on pull request 83. The first ten rows are new since version 3.

| Source | Main-line commit | Standing |
|---|---|---|
| Version 3 of this proposal | `6d4ec3a` (pull request 71): `docs/successor-experiment-proposal-2026-09-26-v3.md` | The text this version starts from. Left unedited |
| The first independent review of version 3, findings RT-230 to RT-236 | `4cb7f8e` (pull request 74): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`, with its scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/` | Reviewed version 3 at `37269ad`. Nothing fatal; two serious findings (RT-230, the floor certified the read and not the piece transplanted; RT-233, four controls had no figure under the registered rules); five minor |
| **John's rulings of 2026-10-03 on that review and on version 3's open decisions (sixteen pages)** | `56a5a86` (pull request 75), with a dated note added under its decisions table at `fe5df65` (pull request 77): `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the first checklist this version was written to. Two rows of its decisions table (decisions 15 and 16) were changed later the same day by the ruling two rows below; the dated note says so |
| **The controls re-run under the registered rules, and its check** | re-run: `821f154` (pull request 76): `docs/2026-10-03-controls-rerun.md`, method `docs/controls-rerun-method-2026-10-03.md`, outputs `experiments/rehearsal-successor-measure/out-controls-rerun/`; check: `e184a6e` (pull request 79): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md` | **Every toy nomination, reading and control figure in this version is taken from this re-run**, under the rule that only a piece which itself carries the label at four fifths may be chosen. Checked by a session that did not run it: run again from the committed code, all 26 output files are equal value for value |
| **John's three rulings of 2026-10-03 after the controls re-run** | `fe5df65` (pull request 77): `docs/rulings/2026-10-03-controls-rerun-rulings.md` | **Binding on this version.** Control 2 kept as a reported description with no pass line; control 4 redefined and made a control that holds; the piece's accuracy at the other positions of its site reported, not gated |
| **The short pre-stated run** | method and code with no output: `9e978d9`; findings and outputs: `853988f` (pull request 80): `docs/2026-10-03-short-prestated-run-method.md`, `docs/2026-10-03-short-prestated-run.md`, outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/` | The redefined control 4 as a pre-stated quantity, the new reported column for all twelve toy models, and one end-to-end run of control 2's code. **Checked by a second session (next row): run again from the committed code, its output files are identical byte for byte, and every figure in its findings matches them** |
| **The check of the short pre-stated run and of the evening ruling's record** | `53c8100` (pull request 82): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`, with its scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/` | Both hold. Four notes for this version, all followed: say the too-early-position control compares the outputs at the two action positions; set out how the new column's two figures are computed and deal with the figure on the average moving by an episode; say that what the short run added for the other-agent control is the part of its code after the floor; say the piece's four fifths is established at the action position only. |
| **John's late-evening ruling of 2026-10-03 on this version's seven questions** | **filed with this version, pull request 83**: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` | **Binding on this version.** The floor on the piece only; the piece rule after the layers are chosen; the laptop's processor; the toy's episode counts at full size; twenty random pieces for the other-agent control; two seeds of three when an arm's seeds disagree; the competing solver run before the registration review. Recorded by the session that wrote this version, and owed a check |
| The check of the two ruling packets of 2026-10-03 and their records | `f32ba0c` (pull request 81): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md` | No number in either packet is wrong; six places where a page says a little more or less than its source. Its section 7 lists what this version should and should not carry, and this version follows it |
| **John's evening ruling of 2026-10-03** | `f32ba0c` (pull request 81): `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` | **Binding on this version.** The fifth registered outcome is satisfactory and stated as weaker than R1; the new reported figure is printed both ways. The record is checked (the row above): it says what John's words say. On the one part that rested on implication, how the two figures are computed, John confirmed that evening in the words "Yes, section 4 of the method is what I meant"; the dated note recording that is beside item 3 of the ruling record |
| The Gate C tier 1 review of version 2, findings RT-212 to RT-229 | `c17dbdc` (pull request 56): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md` | Reviewed version 2 at `e88c3c0`; one fatal finding (RT-212, the empty read on the free arm), four serious, thirteen minor |
| John's rulings on that review | `3af189d` (pull request 60), refined at `4bb5727` (pull request 63), annotated at `da41c20` (pull request 68), and extended at `a11f1d3` (pull request 69, "RT-212 item 3 resolved"): `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the checklist this version was written to; its three refinements after the toy re-run, the annotation of refinement 2's arm C clause, and the resolution of RT-212 item 3 after the label search are carried too |
| The five rehearsal-repairs rulings of 2026-09-25, with their annotations after the check | `62c3824` (pull request 53): `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` | Binding; read with the annotations |
| The rehearsal repairs, session (c), and their check | findings `882f252` (pull request 52): `docs/2026-09-26-rehearsal-repairs.md`; check `d216dbc` (pull request 58) | Checked: every verdict reproduces from the committed code; the decimals on arms C, F and M do not, as the 2026-09-23 ruling expects |
| John's rulings on version 3's decisions 20 and 21 | `9ed9f8c` (pull request 72): recorded in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | Binding. Version 3 carried these from John's revision instruction because no ruling file held them yet; one now does |
| The toy re-run under the version 3 rules, and its check | findings `9d9d31a` (pull request 62): `docs/2026-09-26-toy-rerun-v3-rules.md`, Part 1; check `70be9fb` (pull request 65): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md` | **Superseded on 2026-10-03 for every nomination, reading and control on arms C, F and M** by the controls re-run above, because the piece rule changes which sizes may be chosen. Still the source for three things: the label-permutation null beside the fit, the history of how the layer-0 and control 3 rules were clarified, and the fits as the laptop's graphics chip computed them (0.172, 0.067 and 0.106 on arm F). Arm T's figures reproduce exactly and are the same in every record |
| The thirty trained toy models | `8038275` (pull request 64) for the fifteen behind the repairs and the re-run, and `7ed2b0e` (pull request 67) for the other fifteen: `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one) and `out-grammar-c/models/` (nine), with one `SHA256SUMS` covering all thirty | Committed, with each file's fingerprint; every toy result of 2026-09-25 and 2026-09-26 rests on them (section 10) |
| The grammar attempt (redesign (c)) and its check | attempt `ff778ea` (pull request 57): `docs/2026-09-26-grammar-attempt.md`; check `f1ea004` (pull request 61) | The pass line was not cleared; fallback (d) registers for the named-other condition (section 4.4) |
| The rented slice, second attempt, and its check | `9f802db` (pull request 51): `docs/2026-09-25-rented-slice-attempt-2-findings.md` and the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`; check `afb5183` (pull request 55) | Checked: every point passes, point 1 in part (the go was not compared with John's own message, which no committed file holds) |
| Version 2's failure-mode pass | `a3013be` (pull request 54): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md` | The author's run on version 2; this version's own run is section 17 |
| The Weekend 1 queue ruling (nine pages, 2026-09-25) | main line: `docs/rulings/2026-09-26-weekend-1-queue.md`; its check, `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rulings-check-claude-worktree.md`, main line at `7c403b0` (pull request 78) | Ruled. Version 3 said the check of this ruling was still owed. The check had been written on 2026-09-25 and merged into a branch that never reached the main line; it landed on 2026-10-03 |
| The route (b) label search on the free arm, and its check | search: `a97c12b` (pull request 66): `docs/2026-09-26-free-arm-label-search.md`; check: `ecd2b6c` (pull request 70): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md` | Reported and checked: none of its three candidate reads clears the four-fifths floor on arm F, every figure recomputes, and John ruled on 2026-09-26 that the registration carries the fit floor alone (section 7.2, item 1). Version 3 cited both by branch; both are on the main line and are cited by their main-line commits throughout (the review of version 3, finding RT-236) |

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
used. The reading is made only where the piece of the internal state that is
actually transplanted has been shown to hold its label, at a pre-stated
floor, so that an empty instrument returns *no verdict* rather than a number
at the entangled end; on the toy that is exactly what the freely trained
system returns, on every seed. And the admission that remains is narrower
than before: the toy can now tell an empty instrument from a ceiling, from a
number the procedure already computes, and what it still cannot tell is a
system that is entangled from one whose ownership answer lives somewhere the
read did not look.

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
- **The fit, and the fit floor.** How often a straight-line read names the
  model's own marker word correctly on held-out development episodes, stated
  as a count of those episodes (on the toy, of 180). Ruled 2026-09-26 (the
  rulings on the review of version 2, RT-212) and moved on 2026-10-03 from
  the whole read to the piece that is transplanted (next entry): a piece
  whose own count is below **four fifths** cannot be chosen, an arm and seed
  with no piece that reaches it returns *no verdict*, and both counts are
  printed in the reporting table.
- **The piece.** What the ownership-only transplant actually moves: the
  leading 1, 2, 4 or 8 directions of the read at each layer of the site set.
  The number of directions is the piece's **size**; version 3 called it the
  rank, and both words appear below for the same thing. **The piece's own
  accuracy** is the held-out count of a fresh read given only the state's
  coordinates inside the piece (section 7.2, item 3).
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
- **Twins, and a twin's first own turn.** The two episodes of a matched pair
  (section 6.1). A twin's first own turn is the first position at which its
  acting channel is on. Control 4 is defined on the positions before both
  twins' first own turns (section 7.3, item 4).
- **The rider.** John's addition of 2026-09-25 to the reporting table: every
  arm is also read at arm T's nominated site set and rank, beside the reading
  at its own (the queue ruling, page 3).
- **The tripwire.** The billing check of section 12.5: two ratios, either at
  or above 1.25 halts the wave (the queue ruling, page 6, part 3).
- **The registered outcomes: R1 to R4, and a fifth term.** R1 to R4 were set
  by section 2 of the December-result roadmap. The fifth, *metric validated,
  degree not read*, was ruled on 2026-10-03. All five are in section 3.
- **Gates A, B and C.** The three review points of
  `docs/outside-review-protocol.md`: registration, interpretation, and
  proposals that ask John for a ruling. Versions 1 to 3 of this document
  were Gate C material; this version is written as Gate A material.
- **Two phrases left from version 3, and what they mean here.** "The Gate C
  review" and "the Gate C rulings", wherever version 3's text is carried
  unchanged, mean the review of version 2 and John's rulings of 2026-09-26 on
  it. The review of version 3 and the rulings of 2026-10-03 are always called
  that. Likewise "the re-run findings at `9d9d31a`" is the earlier toy re-run
  of 2026-09-26, and "the controls re-run" is the one of 2026-10-03 that
  supersedes its figures for arms C, F and M.
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
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`), and
with the fifth term John ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11, which
amends the roadmap's outcome list; the roadmap carries two dated notes saying
so). The registered wording is the wording in the middle column; nothing in
this document may report an outcome in other words.

| Outcome | Registered term | What it means | Satisfactory |
|---|---|---|---|
| **R1** | **metric validated, degree read** | The measure separates arms T and C at the pre-stated bar (section 9: 0.5 on the chance-corrected form), and arm F gets a reading with its spread across seeds. The closure sentence "degree unmeasured" is replaced by a number, stated as where arm F sits against the three anchors on this measure (weakness W1). | Yes |
| **R2** | **metric does not separate** | Every arm carried passes its gate (section 8.1: the own-directed condition on arms T, C and M; both conditions on arm F), but the measure cannot tell T and C apart at the bar. The measure is not used on arm F; the result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | One or more arms fail its gate after the one permitted re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. | Yes, if the gate was reached |
| **R4** | (none) | The programme hibernates with a registered design and a rehearsal only. **Since 2026-09-21 a missed kill date does not put the roadmap here by itself**: registration after 2026-10-18, or launch of the remaining registered runs after 2026-11-01, is still possible on a fresh ruling that names what comes off the back end to make room, and R4 is where the roadmap lands only if that ruling says it is not worth it (item 23 of the 2026-09-21 ruling; section 5 of `docs/december-result-roadmap-2026-09-20.md`). | No. Recorded as a schedule failure, not a scientific one |
| **The fifth term** | **metric validated, degree not read** | Arms T and C separate at the pre-stated bar, and arm F returns no verdict. Reported in those words with the reason after a colon, for example "metric validated, degree not read: read failed its floor". The measure is delivered and validated on the built systems; the freely trained system is not read with it. | **Yes, and stated as weaker than R1** (ruled in John's own words on 2026-10-03: `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1, confirming page 11, item 5, of that morning's rulings on its merits) |

**Arm F may return no verdict, and the registration says so in advance (ruled,
the rulings on the review of version 2, RT-212, items 1 and 3; the floor
moved to the transplanted piece by the rulings of 2026-10-03, page 1).** A
reading is made on an arm only where some size of the piece that would be
transplanted clears the fit floor of section 7.2 on held-out development
episodes. On the toy the free arm never did: its best piece, at any layer and
any size on any seed, is right on 34 of 180 held-out episodes against 144
needed, and its whole read is right on 32, 12 and 18 of 180 at the layers the
rule would otherwise choose (MEASURED: `docs/2026-10-03-controls-rerun.md` at
`821f154`, sections 1 and 3, from
`experiments/rehearsal-successor-measure/out-controls-rerun/nominate_F_seed*.json`,
computed on the laptop's processor). The earlier run, on its graphics chip,
gave 31, 12 and 19, which is the 0.172, 0.067 and 0.106 that version 3 quoted
(`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section 1.3;
section 7.2, item 1, says which device's figure is registered). So the toy
record for arm F is **"no verdict, read failed its
floor"** on every seed, and version 2's toy reading for arm F at the
entangled end is withdrawn from the record under failure 2's own rule (the
pre-stated target changed before registration, so the null already collected
is withdrawn rather than reported). **At registered scale the same can
happen, and the first release is the test of it** (John's ruling of
2026-09-26 on the route (b) result, the rulings file at `a11f1d3`, "RT-212
item 3 resolved", item 5; section 7.2, item 1): the single arm F run of step
5a has its nomination reported against the floor before the second release
is asked for, and a miss is a stop there, beside the learn-both stop (section
11). **If arms T and C separate and arm F returns no verdict, the outcome is
the fifth term, "metric validated, degree not read", with its reason after a
colon; it is not reported under R1** (ruled 2026-10-03, page 11, item 3). The
route (b) investigation, which looked for a label the own-directed loss does
force on a free system, found none that clears the floor at toy scale
(section 7.2, item 1), so this version registers with the fit floor alone and
with the ruled label as its one registered read. **The stop after the first
full-size free-model run is unchanged by the fifth term: a miss of the floor
there still goes to John before the second release** (page 11, item 6), and
whether the remaining runs are worth that release is his call with the
registered-size figures in hand.

**The admission (rewritten in version 3 from the ruling on RT-212; reworded
here to say what was measured, as the rulings of 2026-10-03, page 1, item 2,
direct).** Version 2 admitted that a free-arm reading at the entangled anchor
could not be told from the instrument's ceiling, because the chance-corrected
form reads 1 both when the act is entangled and when the nominated subspace
carried nothing. **The toy can tell those two apart, from a number the
procedure already computes**: the accuracy of the piece that is transplanted.
A piece right on 34 of 180 carried nothing, and the fit floor says so before
any transplant is looked at. On arm C, **the read holds the label; the
largest piece transplanted holds it; and no size of piece moves the action.**
In figures: the whole read is right on 180, 177 and 176 of 180 at the chosen
layers on seeds 0, 1 and 2; the chosen pieces, of 8, 8 and 4 directions, are
right on 180, 172 and 150 of 180 at the action position; and the
ownership-only transplant of those pieces lands at 0.0488, 0.0525 and 0.0612
against a no-transplant rate of 0.0512, 0.0488 and 0.0600 (MEASURED: the
controls re-run at `821f154`, section 2, from
`out-controls-rerun/measure_C_seed*.json`; "no size moves the action" is the
review of version 3, RT-230, which read arm C between 0.9897 and 1.0051 at
every size on every seed, at version 3's site sets). That is what "entangled
at these sites" means. Version 3's sentence here, that a subspace nominated
by a read at 0.96 or better "held the label and still moved nothing", claimed
more than was measured: on two seeds of three the piece it transplanted held
the label at 0.544 and 0.306 (the review, RT-230), and it is replaced by the
sentence in bold above.

**The piece's four fifths is established at the action position only.** Where
a site covers several positions, the same directions are transplanted at
every one of them, and away from the action position the piece often falls
below four fifths. On arm C seed 1 it is right on 139, 139 and 33 of 180 at
the three positions before the action; on arm C seed 2 it is below 144 at all
ten positions reported, from 30 to 139, and 123 on the average over the other
positions; on arm M it clears on the average on every seed (163, 174 and 175)
and misses at six, six and three of the ten positions reported. The whole
state at those positions holds the label throughout (149 to 180 of 180 on the
built systems), so the label is there and is not held in the chosen
directions (MEASURED, **checked: the check of the short run at `53c8100`**:
`docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
`out-short-prestated-run/part_b.json`). So "the piece held the label and the
transplant of it did nothing" is true at the action position and is not shown
across the whole site. John ruled that this is reported in the registered
table both ways and gated in neither
(`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3;
`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling
2); it is weakness W13.

What the admission that remains says (ARGUED): a piece that clears the floor
shows the label is present in those directions at the action position; it
does not show that the directions it found are the ones the act uses. A free
arm whose piece clears the floor and whose reading is near 1 is therefore "as
entangled as the built anchor at the sites this procedure nominates", and no
more; that the ownership answer lives in some other part of the state the
read did not find is not excluded. Arm M (section 5.3) is a known case in the
middle of the scale, so that a free-arm reading can be placed against three
anchors rather than two. It does not remove that residual admission, because
arm M's known degree is a mixture by item, and a free arm's partial
separation, if it has any, would be within each trial (section 5.3).

**The toy outcome, on the anchors' terms (ruled, the rulings on the review of
version 2, RT-213, item 1).** Under the rules this version registers, the toy
reaches the fifth term: its anchors separate and its free arm is not read.
Arm T reads 0.0000 and arm C **1.0051, 0.9926 and 0.9974**, so the
separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on
every seed; arm M reads 0.4886, 0.4860 and 0.5449, inside its band on every
seed; and arm F returns no verdict on every seed, twice over, because it
fails its gate and no piece of its read reaches the floor (MEASURED: the
controls re-run at `821f154`, sections 1 and 2, from
`out-controls-rerun/summary.json`; reproduced value for value by the check at
`e184a6e`, section 3). Version 3 gave arm C as 1.0051, 1.0025 and 1.0000;
seeds 1 and 2 were read through pieces of two directions and one, which do
not hold the label (the review, RT-230), and are replaced. Arm C's named-other
condition fails on every toy seed, at 760, 751 and 708 correct of 3,000
against a bar of 790 (MEASURED: `out-repairs/gate_base.json` at `882f252`;
the review of version 2, RT-213); under version 2's rules that made the toy
an R3, and under this version's it does not, because the constructed arms
are gated on the own-directed condition only (section 8.1) and their reading
uses only the own-directed action. **Version 2 left that failure out, and
this version states it wherever arm C's toy record is quoted** (sections 5.2,
10 and 11).

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

**What a no verdict maps to (ruled 2026-10-03, page 11; it closes the
no-verdict finding RT-182 of the review of version 1, that the measure's own
failure state had no registered outcome term).** An arm's *no verdict* is
reported in those two words with its reason after a colon, as the re-run's
table does ("no verdict: read failed its floor"). Then:

1. **No verdict on arm C** fires the two-arm fallback John accepted in
   advance on 2026-09-20 (section 5.2).
2. **No verdict on arm M** drops arm M, which is then carried as an extension
   on the weekend roadmap.
3. **No verdict on arm F after arms T and C have separated** is the fifth
   term of the table above.

**When an arm's three seeds disagree, two of three decide, and the third is
reported (ruled 2026-10-03, late evening: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
ruling 6).** The floors and the controls that hold apply per arm and seed
(section 7.2, item 1), so an arm can read on two seeds and return no verdict
on the third. The rule is the one the design already uses for its gates. As
this session reads it, in wording that is its own and John's to overturn: an
arm is read if at least two of its three seeds return a reading, and returns
no verdict, as an arm, if two or more of its seeds do; the separation bar is
cleared if arm C's reading minus arm T's is 0.5 or more on at least two of
the three seeds, compared seed by seed; and every seed is printed, whichever
way it went. On the toy every arm behaves alike on all three seeds, so the
rule has not yet been exercised on a split. The record of that ruling notes
that this was the one question the session flagged as deserving more of
John's attention than a general agreement gives it.

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
conditions may be read as. **Ruled 2026-10-03 (decision 9): it is recorded as
a known limitation and not engineered away.**

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
standing prohibition (it has no argument handling) and is not used. **Part of
the registered recipe (ruled 2026-10-03, decision 13): the launcher waits for
the laptop's receipt, and the trainer does not delete its own machine.** What
the registration says about the shutdown is section 13, weakness W9. **Two
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
**0.0000 on every seed**, nominated at layer 0 at the action position with a
piece of 8 directions, the whole read and the piece each right on 180 of 180
held-out episodes on every seed; its ownership-only transplant moves the
action in every trial, above all twenty random draws of control 3 (MEASURED:
the controls re-run at `821f154`, section 2). Under the stricter layer-0
variant of section 7.2 its site moves to layer 1 at the action position and
it still reads 0.0000 (the same record, section 4). Its gate and lesion
figures reproduce the 2026-09-21 record exactly, and its toy training
reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

**Ruled 2026-10-03 (decision 2): the ownership path is forced by the
architecture, not merely encouraged by a penalty term.** The forced version
is what makes the degree known; a soft version would be more comparable with
arm F but would forfeit the one thing the arm exists to supply.

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
the controls re-run at `821f154`, sections 2 to 4, from
`out-controls-rerun/nominate_C_seed*.json`, `measure_C_seed*.json` and
`summary.json`; reproduced value for value by the check at `e184a6e`, section
3).** It reads **1.0051, 0.9926 and 0.9974** on seeds 0, 1 and 2, at the
entangled end on every seed, quoted per seed for these particular models and
not as a property of the code. The rule chose:

| Seed | Site set | Size of piece | Whole read, right of 180 | Piece, right of 180, at the action position | Whole-state, ownership-only and no-transplant shares | Reading |
|---|---|---|---|---|---|---|
| 0 | layer 2 at the action position | 8 directions | 180 | 180 | 0.5400, 0.0488, 0.0512 | 1.0051 |
| 1 | layer 1 at the action position and the three before it | 8 directions | 177 | 172 | 0.5550, 0.0525, 0.0488 | 0.9926 |
| 2 | layer 1 from the model's first own turn to the action | 4 directions | 176 | 150 | 0.5463, 0.0612, 0.0600 | 0.9974 |

**What that shows, in the words the ruling of 2026-10-03 directs (page 1,
item 2): the read holds the label; the largest piece transplanted holds it;
no size moves the action.** Every chosen piece clears four fifths (144 of
180) at the action position, and its ownership-only transplant lands within
0.004 of the no-transplant rate while the whole-state transplant moves the
action in more than half of trials. That no size moves the action is the
review of version 3, RT-230, at version 3's site sets: arm C read between
0.9897 and 1.0051 at 1, 2, 4 and 8 directions on every seed. **Version 3's
sentence here, that the subspace arm C transplants "holds the label and
clears the fit floor on every seed", was false on two seeds of three** (the
pieces it chose there, of two directions and of one, held the label at 0.544
and 0.306; the review, RT-230), and its readings for those seeds (1.0025 and
1.0000, at layers 4 and 1) are replaced by the table above. Version 2's
figures for this arm (0.99 to 1.00, and the separation figures 0.9977 and
0.9927) were replaced in version 3 and stay replaced.

**Away from the action position the piece often does not hold the label at
four fifths.** On seed 1 the piece is right on 139, 139 and 33 of 180 at the
one, two and three positions before the action, and 113 on the average over
those three. On seed 2 it is below 144 at all ten positions reported, from 30
to 139, and 123 on the average over the other positions of its site. Seed 0's
site is a single position (MEASURED, **checked: the check of the short run at `53c8100`**:
the short pre-stated run at `853988f`, section 4). The whole state holds the
label at every one of those positions. This is reported and not gated
(section 7.2, item 3; weakness W13).

**The choice among candidates is made among sampling noise on this arm, and
the record says so.** On seed 1 the rule chose layer 1 over layer 4 because
the development ownership-only share was 0.0533 against 0.0517, one episode
of 600; the session that ran the re-run had predicted layer 4, and said so in
its findings. What the piece rule fixes is that whichever candidate wins, its
piece carries the label. The reading at the chosen site is 0.9926; at layer 4
with 8 directions it was 0.9975 (the controls re-run, section 3; the review,
RT-230). **This version does not use the sizes and readings on page 1 of the
ruling packet of 2026-10-03 (8, 8 and 4 directions at layers 2, 4 and 1;
1.0051, 0.9975 and 0.9974): they were that session's forecast, the ruling
itself says they are not committed results, and the forecast was wrong on
seed 1.**

Control 3's twenty random draws all sit above the ownership-only transplant
on seed 0, and around it on seeds 1 and 2 (6 below, 1 equal and 13 above; 6
below, 5 equal and 9 above), which is what an entangled arm should show: its
ownership piece does no more than a random piece of its size (the controls
re-run, sections 2 and 4; the reading of it is ARGUED).

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
scale both pass under the registered rules. **Also ruled, 2026-10-03
(decision 3): arm C entangles by its architecture, and is not trained with a
penalty against transplantable ownership directions**, which would train the
system against the very instrument that will measure it.

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
the controls re-run at `821f154`, sections 2 and 4, from
`out-controls-rerun/measure_M_seed*.json`; reproduced by the check at
`e184a6e`, section 3).** The blind reading is **0.4886, 0.4860 and 0.5449**
on seeds 0, 1 and 2, inside 0.3 to 0.7 on every seed, so the fold-in pass
stands with control 3 reported beside it. Every seed is nominated at layer 1
from the model's first own turn to the action, with a piece of 8 directions;
the whole read and the piece are each right on 180 of 180 at the action
position; the whole-state transplant moves 0.7800, 0.7738 and 0.7937 of
trials and the ownership-only transplant 0.4050, 0.4062 and 0.3688, above all
twenty random draws of control 3 by a wide margin (random medians 0.015 to
0.019). **The "within 0.10" half of the prediction now has its figure at the
registered site sets, which version 3 listed as owed:** the true-slot reading
is 0.4837, 0.4760 and 0.4920, the route formula agrees with it to four
decimals, and the blind reading is within **0.0049, 0.0099 and 0.0529** of it
(MEASURED: the review of version 3, RT-231, from its script
`arm_m_true_slot.py`; found again by the controls re-run, section 4, whose
prose printed the middle figure as 0.0100 from two rounded numbers; the
unrounded difference is 0.00995, and the check at `e184a6e`, section 3,
gives 0.0099). Seed 2 uses a little over half the allowance. Arm M passes its
gate on the own-directed condition on all three seeds (0.8613 to 0.8667), and
clears the named-other condition too (0.5517 to 0.5663), although that is no
longer gated for it (MEASURED: `out-repairs/gate_base.json` at `882f252`).
Its self-test passes all seven checks, including that perturbing the slot
never moves an entangled-route action (`out-repairs/self-tests.txt` at
`882f252`).

**Away from the action position arm M's piece is not what this session, or
the one that ran it, expected.** On the average over the other positions of
its site the piece is right on 163, 174 and 175 of 180, above four fifths on
every seed. Position by position it reaches 144 at only four, four and seven
of the ten positions reported, and at the fourth token of the model's first
own turn (the value word) it is right on 34, 71 and 33 (MEASURED, **checked: the check of the short run at `53c8100`**: the short pre-stated run at `853988f`, section
4, whose author records that it expected better and was wrong). The two ways
of computing the figure give different pictures of this arm, which is why
John ruled that the registered table prints both (section 7.5).

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
every seed (ruled, the rulings on the review of version 2, RT-212, item 2;
the floor moved to the piece on 2026-10-03).** No piece of its read of "which
marker word is the model's own" reaches four fifths at any layer, at any
size, on any seed: the best is right on 34 of 180 held-out episodes against
144 needed. Its whole read is right on **32, 12 and 18 of 180** on seeds 0, 1
and 2 at the layers shown in the re-run's table (MEASURED: the controls
re-run at `821f154`, sections 2 and 3, from
`out-controls-rerun/nominate_F_seed*.json`, `fits`, on the laptop's
processor). On the laptop's graphics chip the same reads were right on 31, 12
and 19, which are the 0.172, 0.067 and 0.106 quoted in version 3 and in every
earlier record; each difference is one held-out episode, and section 7.2,
item 1, says which device's figure is the registered one (the review of
version 3, RT-232). The no-information level of this read is 0.072, about 13
of 180 (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section
1.3). It also fails the learn-both gate: the named-other condition clears on
1 seed of 3 (section 4.4). So it fails twice over. **The number the
arithmetic would have returned (1.0000, 1.0000 and 1.0108) is withdrawn from
the record** under failure 2's rule and is not a reading; it appears in the
re-run's table in parentheses, labelled "reported for description; no
reading", only so that a reader can see what an empty instrument returns,
which is the entangled end. Every control figure for this arm in section 7.3
is taken at the site the rule would choose with the piece requirement
switched off, and carries the same label.

**What the free arm does instead of representing the label (ARGUED, the Gate
C review, RT-212, from `grammar.py` and the gate file).** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver, and it collapses when the acting channel is removed
(0.1760 to 0.1940), so its ownership answer is load-bearing; but an
own-directed action can be solved by attending to the value tokens on the
turns the acting channel marked, with no need to know which marker word those
turns carry. That is why the route (b) investigation of section 7.2 looked for
a label the own-directed loss does force on a free system. The review of
version 3 saw the same thing directly: on the free arm the label is fully
readable from the whole state at the first token of the model's first own
turn and nearly unreadable at the action position (its RT-230, the side
observation), so the free toy model does not carry the marker word forward to
where it acts.

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
nothing" when small (arm C reads 1.0051 at one toy seed; the controls re-run
at `821f154`, section 2) and a warning about the instrument when large. The
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

   **The floor is applied twice, on different episodes (the review of
   version 3, RT-234, accepted 2026-10-03, page 3).** At nomination it is
   applied on development episodes, to decide which site sets are candidates.
   At the reading it is applied again, on the fresh episodes. **A site set
   that clears on development episodes and misses on fresh ones returns "no
   verdict: floor missed on fresh episodes"**; the nomination is frozen by
   then and is not redone. On the toy the two agree on all twelve arm-and-seed
   pairs, and the narrowest margin is arm F seed 0 on development episodes,
   0.4433 against 0.4280 needed, which is 9 episodes of 600 (MEASURED: the
   review, RT-234; the controls re-run at `821f154`, section 4, "the
   whole-state floor on fresh episodes clears on all twelve").
2. **The fit floor, on the piece that is transplanted (ruled, the rulings on
   the review of version 2, RT-212, item 1; applied per arm and seed, ruled
   2026-09-26 on decision 21; moved from the whole read to the piece by the
   rulings of 2026-10-03, page 1).** Only a size of piece whose own held-out
   accuracy reaches **four fifths** on development episodes may be chosen
   (section 7.2, item 3, gives the rule in full). An arm and seed with no
   size that reaches it returns **"no verdict, read failed its floor"**, and
   the transplant arithmetic is not reported as a reading. The piece's count
   and the whole read's count are both printed in the reporting table, with
   the label-permutation null beside them as a reference and not as the bar.
   **The floor is on the piece only (ruled 2026-10-03, late evening, ruling
   1).** The ruling of 2026-09-26 put the floor on the whole read, at the
   worst layer of the nominated site set. The morning ruling of 2026-10-03
   moved it to the piece and did not say whether the whole read must still
   clear four fifths in its own right. John ruled that it need not: the
   whole read's count is printed beside the piece's and is not a second
   condition. That is how the controls re-run ran
   (`experiments/rehearsal-successor-measure/src/rerun_controls.py`,
   `PIECE_MIN`; its method, rule 9). On the toy the two readings give the
   same twelve verdicts: every chosen piece's whole read is right on 176 or
   more of 180, and arm F misses both. They can differ in principle, because
   a piece can score above its whole read by an episode or two (on arm F seed
   1, 17 against 12; on the named agent's read of section 7.3, item 2, 139
   against 137). The alternative that was put and not taken: require both.
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
5. **If a control that holds fails** (section 7.3: the null transplant,
   control 7; the content transplant, control 1, on arm T only; and the
   too-early-position control, control 4, as redefined), the reading is not
   made for that arm and seed. **A requirement on the registered code: it
   withholds the reading itself.** The toy re-run's code computed each of
   these as a true-or-false field and printed the reading regardless; every
   one passed, so no reading was printed that should not have been, but the
   withholding was left to the reader of the table (the check at `e184a6e`,
   section 4, item 3). In the registered code a failed control that holds, a
   no-transplant miss outside its allowance, or a floor missed on fresh
   episodes replaces the reading with "no verdict" and its reason, in the
   output file and in the table.

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
re-run's `src/rerun_v3.py`, both at `9d9d31a`, and the controls re-run's
`src/rerun_controls.py` at `821f154`, do this, and their nomination tables
show one rule applied throughout). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy: arm C
is nominated at layer 2 at the action position, layer 1 at the action
position and the three before it, and layer 1 from the first own turn to the
action, on its three seeds; the controls re-run at `821f154`, section 3).

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

   **The fit floor (ruled, the rulings on the review of version 2, RT-212,
   item 1; moved to the piece by the rulings of 2026-10-03, page 1, item
   1).** In the ruling's words: "only sizes whose own held-out accuracy
   clears four fifths may be chosen, and that accuracy is printed in the
   reporting table", beside the whole read's. "The accuracy of a piece is the
   held-out accuracy of a read given only the state's coordinates inside that
   piece, on the same development episodes and split as the whole read. An
   arm and seed with no size that clears returns 'no verdict, read failed its
   floor'." The floor is absolute, the same convention as the whole-state
   floor. The label-permutation null, the fit the whole read reaches when the
   labels are shuffled (two hundred shuffles at toy scale; its 95th and 99th
   percentiles), is reported beside it and is not the bar. The reason
   recorded in the ruling of 2026-09-26: a permutation null alone would
   likely certify a read at 0.172, which recovers the label on about one
   episode in six, and that is not an instrument worth transplanting. **The
   floor applies per arm and seed** (ruled 2026-09-26 on decision 21,
   recorded in the rulings file at `9ed9f8c`): an arm's three seeds are
   reported one by one, each a reading or a no verdict, and the across-seed
   spread of section 9 is taken over the seeds that read. The whole read's
   count is printed and is not a second floor (section 6.4, item 2).

   **How the accuracy is stated, and on what it is computed (the review of
   version 3, RT-232; accepted 2026-10-03, page 3, as the review states the
   fix).** Every fit in the registration and in the reporting table is
   **stated as a count of held-out episodes** (on the toy, of 180; the floor
   there is 144). **The registration names the device and the number format
   the registered fit is computed on, and the figure on that device is the
   registered one.** The reason: the floor is a hard line, per arm and seed,
   and on the toy two of twelve reads moved by exactly one held-out episode
   between the laptop's processor and its graphics chip (arm F, 32 against 31
   and 18 against 19; the other ten were identical; MEASURED: the review,
   RT-232; the controls re-run at `821f154`, section 3), so a fit within an
   episode or two of four fifths could pass on one device and fail on the
   other. **Ruled 2026-10-03, late evening (ruling 3):** the registered fit is
   computed on the laptop's **processor**, never its graphics chip; the
   model's states are computed in the model's own 32-bit floating-point
   format; the read is scikit-learn's logistic regression, which fits in
   64-bit; and the versions of torch, scikit-learn and numpy are recorded in
   the output file and are not pinned by the registration, as the controls
   re-run did (torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0,
   `out-controls-rerun/summary.json`). The processor is the device the
   controls re-run and the short pre-stated run, which supply every toy
   figure in this version, ran on. The alternative that was put and not
   taken: the graphics chip. **In the registered run the
   read is fitted once, on that device, written to disk and reloaded
   (section 7.1); the printed whole-read count and the transplanted
   directions come from that one fit.** On the toy re-run they came from two
   fits of the same read: the directions from the coefficients committed
   earlier on the graphics chip, and the printed count from a fresh fit on
   the processor (the check at `e184a6e`, section 4, item 2); on the built
   arms nothing turns on it.

   **The toy demonstration (MEASURED: the controls re-run at `821f154`,
   sections 2 and 3; reproduced by the check at `e184a6e`, section 3).** The
   floor returns no verdict on arm F and a reading on arms T, C and M. Right
   of 180 held-out episodes at the action position, whole read then chosen
   piece: arm T 180 and 180 on every seed; arm C 180 and 180, 177 and 172,
   176 and 150; arm M 180 and 180 on every seed; arm F 32, 12 and 18 for the
   whole read, with no piece above 34 at any layer or size. The lowest piece
   among those that clear is 150 of 180. The permutation null's 95th
   percentile sat at 0.111 to 0.128 (about 20 to 23 of 180) across all twelve
   pairs on the earlier re-run (`docs/2026-09-26-toy-rerun-v3-rules.md` at
   `9d9d31a`, Part 1, section 1.3; the check at `70be9fb`, section 3.2; that
   null is for the whole read, on the graphics chip, and was not recomputed
   on 2026-10-03). **One clause of the rulings file's refinement item 2 was
   wrong on this point and carries an annotation** (the rulings file at
   `da41c20`, pull request 68): it said that under the layer-0 removal "arms
   C and F still fall to the fit floor"; arm C does not, and only arm F falls
   to the floor. Nothing ruled depends on the clause.

   **The route (b) investigation, and what it found (the Gate C rulings,
   RT-212, item 3; the result ruled 2026-09-26).** Route (b) asked for a label
   the own-directed loss does force on a free system, which a straight-line
   read can recover on arm F at four fifths. The free-arm label search
   (`docs/2026-09-26-free-arm-label-search.md`, main line at `a97c12b`, pull
   request 66; laptop only, $0,
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
   findings at `a97c12b`, sections 1 and 2; its check,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`,
   main line at `ecd2b6c`, pull request 70,
   recomputed every best fit, shuffle summary and verdict from the committed
   files with no disagreement, and confirmed the twelve models against the
   committed fingerprint list; its section 6 narrows the search's closing
   sentence to "none of three candidates chosen in advance", which is how it
   is stated here). **John's ruling of 2026-09-26 (the rulings file at
   `a11f1d3`, "RT-212 item 3 resolved", items 1 to 5): this version registers
   with the fit floor alone; the ruled label, which marker word is the model's
   own, stays the one registered read; the three candidates enter the toy
   record as exploratory fits, not as registered reads; the experiment
   proceeds; and the first release's single arm F run reports its nomination
   fit against the floor, a miss being a stop before the second release
   draws** (section 11, step 5a). The reason recorded there: the fits rising to
   0.79 above a 0.10 shuffle baseline on the small toy model is the argument
   that the deeper registered model may clear the floor, and $44 is the price
   of finding out before $130 is spent. **The depths, stated the same way in
   both places (the review of version 3, RT-236; accepted 2026-10-03, page
   3): the toy has four blocks and five running states; the registered model
   has twelve blocks and thirteen running states.** The ruling as recorded
   calls the toy "a five-layer model" and the registered one "twelve-layer",
   which counts states for one and blocks for the other; the rulings file
   carries a dated note beside the phrase and stands as recorded. Like for
   like, the registered model is three times as deep, not two and a half. **The search also printed a
   fit for the ruled label on arm F of 0.556, 0.483 and 0.433 over its 60 site
   sets, which is not the 0.172 the Gate C review and the re-run report. The
   check reconciled the two: they are different reads of the same models,
   episodes, split and fitter.** The registered rule fits one read per layer
   at the action position only and reports the worst layer of the nominated
   set; the search fitted one read per site set, with the layers and
   positions of the set laid end to end and the post-identity span averaged,
   and all three of its higher figures come from that averaged span at layers
   0 to 1 or 0, which starts at the model's own marker word and which the
   layer-0 removal of item 2 excludes. On the search's own cell for the
   registered read (layer 1, the action position) it prints 0.172, 0.067 and
   0.106 to the digit (MEASURED: the check at `ecd2b6c`, "Verdict" and section
   2). Item 3 registers which read is meant, so the two cannot be confused
   again; the 0.172 is the registered read's figure as the graphics chip
   computed it, and on the processor the same read is right on 32 of 180.

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
     every position, is excluded by the rule below.) **Ruled 2026-10-03 (decision 19): the
     position sets are the rehearsal's four, by name.**
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
     committed as a file). **This version registers the reading as run, layer
     0 kept at `action` only, 45 site sets on the toy and 325 on the
     registered model (ruled 2026-09-26 on decision 20)**; the narrower
     reading is recorded beside it as the alternative that was put and not
     taken. On the separable arms layer 0 inside
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
     160, and 312 and 1,248 (MEASURED: the review of version 3, "What was
     checked and held", recomputed all eight site-set counts by arithmetic
     on the rule; section 18 prints the registered list with its command). The ruled figures before the
     all-positions widening, 296 and 1,816, and version 2's 60 and 364, are
     superseded by these; the repairs rulings' annotation 4 records the first
     supersession. The list and the rule have to agree, and the registration
     prints both: **the list for the registered model is printed in section
     18**, generated by the rule and not typed by hand, with the command that
     generated it.
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
3. **Candidate directions, and the read that supplies them, registered.**
   **The read the rule uses is one fitted straight-line read per layer, on
   the running state at the mask token of the own-directed action (the
   `action` position), labelled with the model's own marker word, fitted on
   the development episodes and scored on the held-out part of them** (in the
   rehearsal code, `repairs.fit_reads`: one logistic regression per layer, the
   same read whatever site set is later nominated). At each site set the
   directions transplanted are that read's leading directions at each layer
   in the set, at each of the rank caps **1, 2, 4 and 8**; **the registered
   cap is 8** and the search family reports all four (ruled, the queue ruling,
   page 1d).

   **The piece rule (ruled 2026-10-03, page 1; the review of version 3,
   RT-230, option (b)).** For each candidate site set and each size, the
   piece's own accuracy is computed: a fresh straight-line read given only
   the state's coordinates inside the piece, **at the action position**, on
   the same development episodes and the same split as the whole read; for a
   site set with more than one layer, the worst layer's. **A size is a
   candidate only if its piece is right on at least four fifths of the
   held-out episodes** (on the toy, 144 of 180). An arm and seed with site
   sets that clear the whole-state floor and no size that reaches four fifths
   returns "no verdict, read failed its floor". The alternative that was put
   to John and not taken: fixing the size at 8 directions with the smaller
   sizes as extra rows. **The requirement is applied after the layer set is
   chosen (item 4), so it decides which sizes may be chosen and never changes
   which layers are used (ruled 2026-10-03, late evening, ruling 2).** The
   re-run's method had marked that as its own reading, for John to overturn
   (`docs/controls-rerun-method-2026-10-03.md`, rule 7; the check at
   `e184a6e`, section 4, item 6); he confirmed it. The alternative that was
   put and not taken: letting the piece's accuracy also decide between layer
   sets, which has not been run.

   **The piece's accuracy at the other positions of its site: reported both
   ways, gated in neither (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
   `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
   ruling 2).** Where the chosen site set covers more than the action
   position, the same directions are transplanted at every position of it,
   and the four fifths above was established at one of them. So the
   reporting table prints, beside the piece's count at the action position,
   **(i) its count at each other position of the site, and (ii) its count on
   the average over those positions.** Neither has a pass line; the rule is
   unchanged. Each is computed as the short pre-stated run's method states
   (`docs/2026-10-03-short-prestated-run-method.md` at `9e978d9`, section 4):
   - **A count at a position** is computed exactly as at the action position,
     with only the position changed: the model's state at that position on
     the development episodes, its coordinates inside the piece, **a fresh
     read fitted at that position** on the same split, and the number of
     held-out episodes it gets right. It is not the action-position read
     carried over. The same count for the whole state at that position is
     printed beside it, so that a low piece figure can be told apart from a
     position where the label is not in the state at all.
   - **Which positions are reported one by one.** For the action position and
     the token before it: that one position. For the action position and the
     three before it: each of the three. For a site that runs from the
     model's first own turn to the action, whose length differs from episode
     to episode: **the five tokens of the model's first own turn, and the
     five tokens before the action**; the positions between them do not line
     up from one episode to the next and **are covered by the average only**.
     A site at the action position alone is printed as "single position".
   - **The count on the average** is the same count taken on the state
     averaged over every position of the site except the action position.
     **In the registered code that average is taken in 64-bit arithmetic.**
     The reason is the check of the short run, finding 11: on the toy, the
     same average of the same numbers added up in a different order moved the
     count by one episode of 180 on three of the eight figures (arm F seed
     0's whole state, 90 against 91; arm F seed 2's, 74 against 73; arm M
     seed 0's piece, 164 against 163), and in 64-bit arm F seed 0 gives 92
     and 24. The check offered two ways to deal with it, saying the figure is
     good to an episode or two, or fixing the arithmetic; this draft does
     both, and the choice of 64-bit is this draft's. **The toy figures on the
     average quoted in this version are therefore good to an episode or
     two.** The per-position counts did not move.
   - For a site set with more than one layer, the worst layer's figure.
   - **How much of a span the ten named positions cover:** a span from the
     first own turn to the action runs 16 to 53 positions on the toy, 39.2 on
     average, so the ten positions reported one by one are about a quarter of
     it, and the rest is seen only through the average (the check of the
     short run, finding 14).

   **This computation rests on John's own words.** The evening ruling
   recorded it as ruled from "print both figures", which accepts it by
   implication only; the check of that record said so (its finding 19), John
   was asked, and he answered "Yes, section 4 of the method is what I meant"
   (a dated note beside item 3 of the ruling record, main line at `53c8100`).

   *What the toy shows (MEASURED, **checked: the check of the short run at `53c8100`**:
   `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
   `out-short-prestated-run/part_b.json`; each cell is whole state then
   piece, right of 180).* Arm T on every seed and arm C seed 0: single
   position. Arm C seed 1: 180 and 139, 179 and 139, 179 and 33 at one, two
   and three positions before the action; 179 and 113 on the average. Arm C
   seed 2: the piece between 30 and 139 at the ten positions, the whole state
   between 149 and 180; 180 and 123 on the average. Arm M: the piece at 144
   or more at four, four and seven of the ten positions on seeds 0, 1 and 2,
   and as low as 34, 71 and 33 at the fourth token of the first own turn;
   180 and 163, 180 and 174, 180 and 175 on the average. Arm F, described
   only: the piece between 11 and 36 everywhere except the first token of
   the first own turn on seed 2 (145), which is the model's own marker word
   itself. The action-position counts recomputed by that run equal the
   controls re-run's on all twelve. **A limit of these figures, from the
   run's own findings:** each is a fresh read fitted on 420 episodes with
   twelve possible answers, in a piece of 4 or 8 directions; a figure like
   139 against 144 is a few episodes and should not be read finely. **A nominated site set's fit, for the floor of item 1, is the
   fit of the worst layer in the set**, as the re-run's verdict code reports
   it; on the toy no nomination has more than one layer, so this has not yet
   bitten. **What is not the registered read:** a read fitted per site set,
   with the states of every layer and every position in the set laid end to
   end and a multi-position span averaged over its positions, which is what
   the route (b) label search fitted (its `site_features`). That is a
   different quantity, it can score far higher on the same models (0.556
   against 0.172 on arm F seed 0, item 1), and nothing in this design uses it
   (the label-search check at `ecd2b6c`, section 2, which traced both reads
   through the code).
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
   sizes whose piece clears the floor (item 3), the nominated configuration
   is the one with the highest *development-set ownership-only transplant
   accuracy*; ties go to the smaller size, then the earlier position set.
   This is the main lesson of the closed design: a representation that a
   straight-line read recovers beautifully can do nothing when you intervene
   on it. **What changed on 2026-10-03:** version 3 applied the fit floor to
   the nominated configuration afterwards; under the piece rule the floor is
   applied before the choice, as a limit on which sizes may be chosen. Among
   the sizes that pass, the choice is still blind to how well any read fits.
   **On an arm where nothing moves the action, that choice is made among
   sampling noise, and the registration says so** (the review of version 3,
   RT-230 and RT-235): on arm C the development shares at different sizes and
   sites differ by one or two episodes of 600, and on seed 1 one episode
   decided the site (section 5.2). What the piece rule secures is that
   whichever candidate wins, its piece holds the label at the action
   position. It does not make the pick stable.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference; on arm M that reference is the formula
   of section 5.3 written in route accuracies, one check and not two (the Gate
   C rulings, RT-223). On the toy the true-slot reading is 0.0000 on arm T
   and 0.4837, 0.4760 and 0.4920 on arm M (the controls re-run at `821f154`,
   section 4). Ruled 2026-09-25 (decision 1).
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
   the repairs run nominated, so these rider figures stand under the rule,
   and the controls re-run found them again: the whole-state share at arm T's
   site is 0.0512, 0.0488 and 0.0600 on arm C, 0.0587, 0.0563 and 0.0688 on
   arm F, each the no-transplant rate, and 0.4088, 0.4138 and 0.4100 on arm M
   (the controls re-run at `821f154`, section 2, the last column).

### 7.3 Controls

Every one of these is run on every arm. **Three of them hold**, and a failure
means the reading is not made for that arm and seed: control 7 (the null
transplant), control 1 on arm T only, and control 4 (the too-early-position
control, as redefined on 2026-10-03). **The rest are reported** beside the
reading and cannot veto it. Version 2 made control 3 hold as well, and
version 3 made control 4 reported; this version does neither, for the reasons
under items 3 and 4. **The registered code withholds a reading when a control
that holds fails; it does not only print true or false** (section 6.4, item
5).

**All of them now have figures under the registered rules.** Version 3 had
none for controls 1, 2, 4 and 6 on arms C, F and M at the site sets the rule
nominates, and the review of version 3 made that a precondition of the
registration review (RT-233; ruled 2026-10-03, page 2). The controls re-run
of 2026-10-03 ran controls 1, 3, 4, 6 and 7, the true-slot reference, the
rider and the stricter row on all twelve toy models, with its method and code
committed before its output (`docs/2026-10-03-controls-rerun.md` at
`821f154`); a session that did not run it ran it again from the committed
code and found every one of about 26,700 values equal (the check at
`e184a6e`, section 3). Control 2 has no figure and cannot have one at toy
scale (item 2). Arm F's figures are taken at the site the rule would choose
with the piece requirement switched off and are labelled "reported for
description; no reading" (the re-run's method, rule 12).

1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.018 room of section 6.4 (on the toy:
   0.0000 on every seed). *On arms C, M and F it is reported and cannot
   veto.* On an entangled arm the complement carries the ownership signal by
   construction, since in a system where ownership multiplies content at
   every layer there is no ownership-free complement to transplant, so on
   such an arm the complement is expected to reproduce the counterfactual
   almost as well as the whole state does. On the toy it does: arm C's
   complement moves 0.5450, 0.5625 and 0.5312 of trials against whole-state
   shares of 0.5400, 0.5550 and 0.5463; arm M's moves 0.3875, 0.3762 and
   0.4288 against about 0.78, about half, which is what a mixture would give
   (ARGUED); arm F's, for description only, 0.4838, 0.5637 and 0.5400 against
   0.4850, 0.5675 and 0.5300 (MEASURED: the controls re-run at `821f154`,
   sections 2 and 4). As version 1 wrote it, this control would have vetoed
   the reading on exactly the arm the control battery exists to validate, and
   on arm F it would have vetoed whatever the free arm turned out to be,
   which is the thing being measured. Its value on arms C, M and F is a
   description of how much of the identity-driven difference lives outside
   the nominated subspace, which is the reading itself seen from the other
   side.
2. **Another agent's representation: a reported description with no pass
   line; not applicable on arms T and M (ruled, the repairs rulings, item 5;
   and `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1).**
   Nominate, by the identical procedure with the named agent's marker word as
   the label and the named-other action as the anchor, a representation of
   the named agent who is not acting, and transplant it from a twin that
   differs only in which agent is named. **What is reported: how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under twenty random pieces of the same size at the same sites,
   reported as control 3 reports its twenty (median, 95th percentile, and
   the counts below, equal and above).**
   - **It has no pass line.** Version 3 proposed a tolerance of 0.05 over the
     random piece (its decision 15); John agreed to it on the morning of
     2026-10-03 and withdrew it the same day after the controls re-run. No
     number is registered for this control, so nothing about it is a
     pre-stated quantity the rehearsal failed to exercise, in the sense of
     item 5 of the 2026-09-21 ruling.
   - **The registration says in terms: this control never ran at toy scale.**
     It runs only on an arm that has learned the named-other condition
     (passes the section 8.1 bar on it), and only where a piece of the named
     agent's read reaches four fifths. Arms T and M are not applicable by
     ruling: they hold the named agent outside the running state by
     construction, so no transplant into the state can move that action. Of
     the other six toy models, five have not learned the named-other
     condition (arm C at 760, 751 and 708 of 3,000 and arm F seeds 1 and 2 at
     781 and 746, against 790). The one that has, arm F seed 0 (994), has a
     read of the named agent's marker that misses the floor: the whole read
     is right on at most 137 of 180 held-out episodes and the best piece on
     139, against 144 needed (MEASURED: the controls re-run at `821f154`,
     section 5, from `out-controls-rerun/measure_F_seed0.json`, `control2`;
     the check at `e184a6e`, section 3). That would have been a no verdict
     under version 3's rule too. Four attempts to repair the named-other
     condition have not produced a toy model that learns it (section 4.4).
   - **A no verdict is the expected result at registered scale too**, and is
     reported as "no verdict" with which of the two reasons applies.
   - **The part of its code after the floor has run once, and that run is NOT
     A RESULT.** The function has three early exits, and the controls re-run
     took all three: "not applicable" on the six separable and mixed models,
     "has not learned" on five, and the floor on arm F seed 0. What had never
     run was everything after the floor (the check of the short run, finding
     15). So that the registered run is not the first time that code
     executes, the
     re-run's own function for the control was called once on arm F seed 0
     with the piece's accuracy floor switched off for that one call, at $0.
     It ran without error and returned its figures: a site at layer 1, the
     action position and the three before it, 8 directions, a piece right on
     92 of 180 (the floor would have asked for 144); the own-directed action
     moved in 0.0012 of trials, under a random piece in 0.0063, and the
     named-other action in 0.0962. **Those figures are evidence that the code
     ran. They are not a pass or a fail of anything**, because the piece
     transplanted is not known to carry the named agent at all (**NOT A
     RESULT**, and **checked: the check of the short run at `53c8100`**:
     `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 5, from
     `out-short-prestated-run/part_c_NOT_A_RESULT.json`). What is still true
     after it: the control has never been exercised on a model whose read of
     the named agent clears its floor.
   - **Twenty random pieces, not one (ruled 2026-10-03, late evening, ruling
     5).** The re-run's code compares against a single random piece, drawn
     with its own seed (the check at `e184a6e`, section 4, item 4). John
     ruled that the registered description uses twenty. **That is a change to
     the control's code, owed with the registered measurement, so the code
     path that ran once on 2026-10-03, with a single random piece, is not
     quite the one registered.** The alternative that was put and not taken:
     leave it at one draw.

   The alternative that was put to John and not taken: exercising the control
   on a made-up case built for the purpose. This is the successor's own
   obligation, not the closed design's control run on 2026-09-21 (the review
   of version 1, finding RT-181).
3. **Matched random subspaces: the twenty-draw null. Reported, not gated
   (ruled, the rulings on the review of version 2, RT-214, items 1 and 2, as
   refined on 2026-09-26 by refinement item 1).** Twenty random subspaces of
   the same rank and the same norm at the same sites are each transplanted in
   place of the nominated subspace, on every arm and seed. The reporting
   table prints the median and 95th percentile of the twenty random donor
   shares, the ownership-only transplant's own donor share, and how many of
   the twenty draws fall below, equal and above it. The fixed 0.0175 room of
   version 2 is dropped from this control. **The reason it is reported and
   not gated, as recorded in the refinement: a gate on this control cannot
   pass a separable arm and an entangled arm in the same direction.** An
   entangled arm's ownership-only transplant is meant to move nothing, so it
   can never beat random subspaces; on the earlier re-run's first pass, which
   gated on it, arm C seed 0's read fit at 1.000 and was blocked only by this
   control (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 2,
   first pass, sections 6.2 and 7). Its job of catching a leaky site set is
   done by the whole-state floor and the no-transplant rule. **This reporting
   rule was clarified after the re-run of 2026-09-26, with the first pass's
   figures in hand, and is not called pre-stated here** (the check at
   `70be9fb`, section 1.3). *What the toy shows (MEASURED: the controls
   re-run at `821f154`, sections 2 and 4):* on arms T and M the
   ownership-only transplant sits above all twenty draws on every seed (arm M
   0.37 to 0.41 against random medians of 0.015 to 0.019); on arm C it sits
   below all twenty on seed 0 and among them on seeds 1 and 2; on arm F it
   sits among the draws on every seed, which is consistent with a piece that
   holds nothing, though arm F's verdict comes from its floor and not from
   this control.
4. **Positions before both twins' first own turns. Holds (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 2, which
   reverses that morning's ruling on version 3's decision 16).**
   - **What is run.** At the layers of the arm's nominated site set, the
     donor twin's whole state is transplanted into the recipient at every
     position before the earlier of the two twins' first own turns. A twin's
     first own turn is the first position at which its acting channel is on.
     The control takes the site set's layers and not its positions.
   - **The pass line: the transplant changes nothing.** The model's outputs
     at its two action positions (its scores over the vocabulary there, which
     is what the null transplant has always compared) with the transplant are
     compared with the same outputs without it, on every pair, and must be
     bit-identical. "Outputs" here and wherever this control is described
     means those, and not the outputs at every position (the check of the
     short run, finding 7). Reported
     beside it: the share of trials landing on the donor's value with the
     transplant, the no-transplant share, and the number of trials whose
     action changed. **A failure withholds the reading for that arm and
     seed.**
   - **What this control is, said plainly: a known-answer test of the pairing
     and of the code, like the null transplant.** The twins are the same
     text. They differ only in which turns carry the acting channel. The
     models read left to right. So until one twin's channel first comes on,
     both have had exactly the same input, their internal states are the same
     numbers, and transplanting one into the other puts back what was already
     there. **It cannot fail on a correctly built model with correctly built
     pairs, and a pass says nothing about any model.** It is right that a
     failure withholds a reading, because a failure means the pairing, the
     left-to-right property or the transplant code is broken. It is not
     evidence that a model does not yet know its identity at those positions,
     and no report of this experiment describes it that way.
   - **What is withdrawn.** Version 3 defined this control on the positions
     before the *recipient's* first own turn, found it above the
     no-transplant rate on arms C and F, and explained that by saying those
     arms "receive the ownership signal by other routes at those sites".
     **That sentence is withdrawn** (ruling 2, item 3). The control as then
     defined was transplanting at positions where identity was already known,
     in the donor: in 407 of 800 matched pairs (0.5088) the donor twin's
     first own turn comes before the recipient's. Under that definition the
     re-run found the control above the no-transplant rate by 0.065 to 0.10
     on six of the twelve toy models and by 0.005 or less on the other six
     (MEASURED: the controls re-run at `821f154`, section 6).
   - **The evidence the redefinition rests on.** The diagnostic that
     suggested it was written after the re-run's output was seen and was not
     pre-stated (`src/posthoc_control4.py`). The ruling said that if the
     check of the re-run found the diagnostic wrong, the ruling returned to
     John. The check did not find it wrong. With separately written code that
     shares only the episode generator, the model loader and the model's
     forward pass, it found on all twelve models: the twins' inputs and
     states are identical before both first own turns, at every layer; the
     outputs with the redefined transplant are bit-identical to the outputs
     without it; and all of the old definition's excess is in the pairs where
     the donor's first own turn comes first (MEASURED: the check at
     `e184a6e`, section 5, from its script `independent_control4.py`).
   - **The pre-stated run the ruling required** (method and code committed
     before output, by a session that did not write the diagnostic): the
     redefined control **holds on all twelve toy models**. The outputs are
     bit-identical; the donor-value share equals the no-transplant share on
     every line; no trial's action changes; a null transplant at the same
     positions is bit-identical; and across the 800 pairs the control
     transplants at between 1 and 21 positions per pair, about 5 on average,
     never none, so it is never an empty test (MEASURED, **checked: the check of the short run at `53c8100`**: `docs/2026-10-03-short-prestated-run.md` at
     `853988f`, section 3, from `out-short-prestated-run/part_a.json`). The
     method said in advance that this was not a blind prediction: the session
     had already observed it with different code while checking the re-run.
     **The check of that run** ran it again from the committed code and got
     byte-identical output files, found the same thing with separately
     written code at all five running states of every model, and showed the
     test is not empty: with random noise added to the donor's state at the
     same positions the outputs change on all twelve models, so the
     transplant does write there, and it changes nothing in the real control
     because what it writes is what was already there (findings 4, 8 and 9).
     **One limit the check records on the word "pre-stated"** (finding 3):
     the record shows that the method and code were committed and pushed
     before the output, 2 minutes 39 seconds apart; no committed file can
     show that the script was never run before the method was committed.
     Little turns on it, because this control cannot fail on correctly built
     pairs whenever it is run.

   The alternative that was put to John and not taken: redefining the
   positions and keeping the control reported only.
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
   same-value cell and everything in the different-value cell; an entangled
   arm is expected to move the same-value cell too, and that is reported as
   the caveat it is (weakness W11): on those arms the whole-state transplant
   carries something besides identity. *What the toy shows under the
   registered rules (MEASURED: the controls re-run at `821f154`, sections 2
   and 4):* arm T moves 0.0000 of the same-value cell and 1.0000 of the
   different-value cell on every seed; the same-value cell moves on arm C
   (0.5062, 0.6296 and 0.5679), on arm M (0.2222, 0.2716 and 0.3210) and, for
   description, on arm F (0.7284, 0.6790 and 0.6296); the different-value
   cell moves in 0.82 to 0.95 of trials on those three arms.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read. **On the
   toy it holds at every place it was run, fifteen different places:** the
   twelve primary site sets (arm F's three being the described ones) and the
   three stricter-row site sets that differ from their primary, which are arm
   T's (MEASURED: the controls re-run at `821f154`, section 4; the check at
   `e184a6e`, section 3, which corrects the re-run's own count: its "twelve,
   nine and three" names fifteen different places, not twenty-four). That
   closes the citation gap version 3 recorded, that the null transplant had
   not been run at the site sets that changed. It is run again at the
   registered site sets before any registered reading.

**The ordinary competing solver has not yet been measured under the piece
rule, and it will be before the registration review opens (ruled 2026-10-03,
late evening, ruling 7).** The controls re-run did not load the
ownership-blind solver's three models, and read the gate from the committed
file (the check at `e184a6e`, section 4, item 8). The figures section 8.1
quotes for that solver and for the name-only solver are their accuracies on
the two conditions, from `out-repairs/gate_base.json` at `882f252`, taken
before the piece rule existed. Those are accuracies on the task and do not
pass through the nomination, so the piece rule does not change them; but
neither solver has been put through the nomination and the transplants under
the rule as now registered. **What is owed:** the ownership-blind solver's
three committed toy models, put through the nomination and the reading as
section 7.2 now states them, on the laptop at $0, with the method committed
before the output, by a session other than the one that drafted this
version, and checked like any other run. **The expected result, stated now:
no verdict**, because a solver with no acting channel should have no read of
its own marker word that reaches four fifths. **This version quotes no figure
for it. When the run is done its result is written in here, and until then
this text does not go to the registration review.** The alternative that was
put and not taken: state in the registration that it was not measured, and
leave it to the reviewer. In the registered experiment both solvers are
scored on both conditions on the registered episodes, as section 8.1 says.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text, as the one registered
  read; the three route (b) candidates recorded as exploratory fits and not
  frozen as reads;
- **the fit floor: four fifths of held-out development episodes, on the piece
  that is transplanted and on the piece only, at the action position, stated
  as a count; the device the registered fit is computed on, the laptop's
  processor, and its number format (section 7.2, item 1);
  and the permutation null beside it**;
- **the piece's accuracy at the other positions of its site, both ways (each
  position, and the average over them), as reported figures with no pass
  line, and the method by which each is computed** (section 7.2, item 3);
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture (section 18), its two exclusions (all positions;
  layer 0 away from the action position set, as removal from the family), and
  the count of comparisons;
- the stricter layer-0 variant, as the sensitivity row;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its size, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it", with the repairs-style sensitivity
  row named;
- the transplanting operation, as code, with its self-tests;
- all seven controls, and which hold: **control 7; control 1 on arm T;
  control 4 as redefined, on the positions before both twins' first own
  turns, with its pass line that the outputs are bit-identical**; the
  twenty-draw null of control 3 and its reported statistics; **control 2 as a
  reported description with no pass line, against twenty random pieces, with
  the statement that it never ran at toy scale**; the pre-stated cells, the relaxed set for control 6 and
  its generating seed;
- **that the code withholds a reading when a control that holds fails**
  (section 6.4, item 5);
- the whole-state floor rule (four fifths, on the chance-corrected scale,
  applied on development episodes at nomination and again on fresh episodes
  at the reading) and the no-verdict rules of section 6.4, including the
  no-transplant formula, its 0.018 room and the detection margin printed at
  the bar;
- the separation bar between R1 and R2 (0.5);
- **the five registered outcome terms of section 3, and what a no verdict on
  each arm maps to**;
- the gates of section 8: the own-directed bar on arms T, C and M, the
  learn-both bar on arm F, and the ownership-lesion rule with its two-of-three
  clause;
- the uncertainty method (section 9, 1g) and the seed count (three);
- **the numbers of episodes at the registered size, which are the toy's
  (ruled 2026-10-03, late evening, ruling 4): 600 development episodes with
  the last 180 held out for every fit, so the floor is 144 of 180; 800 fresh
  matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for
  the gates, so the bar is 790; 200 shuffles for the permutation null**;
- **the rule for an arm whose seeds disagree: two of three, the third
  reported** (section 3);
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

1. the nominated site set (layers, position set, size of piece);
2. **the whole read's held-out count at the nominated layer, and the chosen
   piece's own held-out count at the action position, each as a count of
   held-out episodes on the registered device, with the permutation null's
   95th and 99th percentiles beside them** (RT-212, RT-230, RT-232);
3. **the chosen piece's count at each other position of its site, and its
   count on the average over those positions, each with the whole state's
   count beside it; reported, with no pass line on either** (ruled
   2026-10-03; section 7.2, item 3);
4. whether the fit floor passes;
5. the whole-state, ownership-only and no-transplant accuracies on fresh
   episodes, the raw difference, and whether the whole-state floor clears in
   both forms, **on development episodes and again on fresh ones** (RT-234);
6. the no-transplant miss against the formula of section 6.4, **and the
   detection margin at the bar** (RT-222);
7. **control 3's twenty-draw null: median and 95th percentile of the random
   donor shares, the ownership-only share, and the counts below, equal and
   above** (RT-214);
8. the reading on the chance-corrected form, or the no verdict with its
   reason;
9. **the stricter layer-0 row**: the same columns with every layer-0 site set
   removed (RT-216);
10. the repairs-style sensitivity row for the whole-state layer set;
11. the rider: the reading at arm T's site set, or its no verdict with which
    of the two reasons applies;
12. the true-slot reference on arms T and M;
13. **the controls that hold, each with its pass or fail: control 7; control
    1 on arm T; control 4 as redefined, with the donor-value share, the
    no-transplant share and the number of trials whose action changed**;
14. **the controls that are reported: control 1 on arms C, M and F; control 2
    as a description (the own-directed action's share moved under the named
    agent's piece, beside twenty random pieces), or its no verdict with the
    reason; control 6's two cells**, each with its pre-stated expectation
    where it has one;
15. the ownership-lesion result;
16. and, across the three seeds of each arm, the across-seed spread of the raw
    difference with the within-seed bootstrap beside it (section 9, 1g).

**The report for the first full-size free-model run (step 5a of section 11)
prints more than its row (the review of version 3, RT-235; accepted
2026-10-03, page 3):** the read's held-out count at every layer, the chosen
piece's own count, and the candidates the nomination chose among. The reason:
on a model where no transplant moves anything, the layer the nomination lands
on is picked among sampling noise, so the stop of step 5a must not be decided
on one number from an arbitrary pick. The procedure has already computed all
three.

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
  re-derived it by an exact binomial tail, section 17, failure 3); the
  registered measurement uses the same 3,000, so the bar is 790 there too
  (ruled 2026-10-03, late evening, ruling 4).
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal, one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, `out-repairs/gate_base.json` at `882f252`;
  these were taken before the piece rule of 2026-10-03; the ownership-blind
  solver is to be put through the nomination under it before the
  registration review, section 7.3, the last paragraph).
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.
- **What is already on the record about this gate (MEASURED: the earlier
  re-run's findings at `9d9d31a`, Part 1, section 1.2, whose gate counts
  equal `out-repairs/gate_base.json` field for field; the controls re-run of
  2026-10-03 read the gate from that committed file and did not run it
  again):** arm T clears both
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
measuring; it is not evidence of a centre and is never reported as such
(ruled 2026-10-03, decision 10).

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
of 2026-09-25, 2026-09-26 and 2026-10-03, each citing the ruling that set it.
**None was invented here.** The registration text freezes them in this form.
The device row and the last row, the numbers of episodes, were open when this
version was first filed and were ruled the same night.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form, per seed | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a. **Under this version's rules the toy cleared it on every seed, at 1.0051, 0.9926 and 0.9974** (MEASURED: the controls re-run at `821f154`, section 2, from `out-controls-rerun/summary.json`, `separation`). Version 3's 1.0051, 1.0025 and 1.0000 were read on two seeds through pieces that do not hold the label and are superseded (the review of version 3, RT-230) |
| Gate on learning (R3) | above one in four at the 0.05 level, one-sided binomial, on at least two seeds of three: **0.2633 on 3,000 held-out episodes** (790 or more correct), or the same rule at the registered count; **on the own-directed condition only for arms T, C and M, on both conditions for arm F**; the ownership-blind and name-only solvers reported beside it as references | the queue ruling, page 1b; the Gate C rulings, RT-213, item 1 |
| Fit floor | **four fifths of held-out development episodes, on the piece that is transplanted, at the action position**, per arm and seed, stated as a count (144 of 180 on the toy); only sizes whose piece reaches it may be chosen; the whole read's count printed beside it and not a second floor; the permutation null reported beside it and not used as the bar | the rulings on the review of version 2, RT-212, item 1; per arm and seed, and the read itself, ruled 2026-09-26 (decisions 21 and 23); moved to the piece by `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 1; on the piece only, and applied after the layers are chosen, by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, rulings 1 and 2 |
| The piece's accuracy at the other positions of its site | **reported both ways, with no pass line on either**: a count at each other position, and a count on the average over them, computed as section 7.2, item 3, states | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 2 |
| The device and number format of the registered fit | **the laptop's processor; the figure computed there is the registered one.** States in 32-bit, the read fitted in 64-bit by scikit-learn, library versions recorded and not pinned | the review of version 3, RT-232, accepted as the review states it by the rulings of 2026-10-03, page 3; the device by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 3 |
| Whole-state floor (whether a site set is usable) | **four fifths of the arm's own own-directed accuracy**, on the chance-corrected scale, **applied on development episodes at nomination and again on the fresh episodes at the reading; a site set that clears the first and misses the second returns no verdict**; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded; every layer-0 site set removed at position sets other than `action` | the queue ruling, page 1c; the repairs rulings, items 3 and 4; the rulings on the review of version 2, RT-216, item 1, as clarified by refinement item 2; the review of version 3, RT-234, accepted 2026-10-03, page 3 |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the queue ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model: **325 site sets and 1,300 comparisons** with layer 0 kept at the action position set only (45 and 180 on the toy); the count is the rule's output, not hand arithmetic | the queue ruling, page 1e; the repairs rulings, item 3; the Gate C rulings, RT-215 and RT-216; the reading of the layer-0 exclusion ruled 2026-09-26 (decision 20) |
| Control 3 | **a twenty-draw null, reported and not gated**: median, 95th percentile, and the ownership-only share's place among the draws | the rulings on the review of version 2, RT-214, items 1 and 2, as refined on 2026-09-26, refinement item 1 |
| Control 2, the other-agent control | **no pass line.** A reported description, beside twenty random pieces; the 0.05 tolerance of version 3's decision 15 is withdrawn and not registered; the registration says the control never ran at toy scale | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the twenty by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 5 |
| Control 4, the too-early-position control | **holds; its pass line is that the outputs with the transplant are bit-identical to the outputs without it**, on the positions before both twins' first own turns, at the nominated layers; a failure withholds the reading for that arm and seed | the same file, ruling 2, reversing that morning's ruling on version 3's decision 16 |
| What a no verdict maps to | arm C: the two-arm fallback; arm M: arm M is dropped and carried as an extension; arm F after arms T and C separate: **the fifth registered term, "metric validated, degree not read", satisfactory and stated as weaker than R1** | `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the queue ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so | the queue ruling, page 1g; on the repairs run the two disagreed by more than two to one on arms C and F (the repairs findings at `882f252`, section 6.2; figures at pre-rule site sets, not carried) |
| Ownership-lesion collapse threshold (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed, **on at least two seeds of three, the third reported**; the named-other clause reported and not gated; the ownership-free batteries must hold; gates arm F only | the queue ruling, page 1h; the Gate C rulings, RT-220 |
| The no-transplant allowance | **at most the largest measured miss, rounded up to 0.018**; the detection margin at the bar printed in the reporting table | the queue ruling, page 2; the Gate C rulings, RT-222 |
| The form of the reading | **the chance-corrected form** of section 6.3 | the queue ruling, page 2 |
| The label | **which marker word is the model's own**, the one registered read; the route (b) candidates recorded as exploratory fits only | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3; the Gate C rulings, RT-212, item 3; John's ruling of 2026-09-26 on the route (b) result (section 7.2, item 1) |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`; checked at `afb5183`, point 5. **Arm M was not timed.** **Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for** (ruled 2026-10-03, decision 17) |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of its true-slot reading on the same fresh episodes (the formula of section 5.3, which is that reading written in route accuracies). On the toy under the registered rules: 0.4886, 0.4860 and 0.5449, within 0.0049, 0.0099 and 0.0529 of the true-slot reading | the queue ruling, page 5 (the band); the repairs method note at `882f252`, section 5 (the formula and the 0.10); the rulings on the review of version 2, RT-223; the toy figures from the review of version 3, RT-231, and the controls re-run at `821f154` |
| The numbers of episodes at the registered size | **the toy's, unchanged: 600 development episodes with the last 180 held out for every fit (the floor is 144 of 180); 800 fresh matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for the gates (the bar is 790); 200 shuffles for the permutation null.** The caution carried with it: at 180, one episode is 0.0056 of the scale | `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 4 |
| An arm whose three seeds disagree | **two seeds of three decide, the third reported**: an arm is read if two or more seeds read; the separation bar is cleared if cleared on two or more seeds | the same file, ruling 6 |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). It ran in five parts, all at toy scale on the laptop
except one item: the rehearsal of 2026-09-21
(`docs/2026-09-21-successor-measure-rehearsal.md`, code in
`experiments/rehearsal-successor-measure/`, re-run from code on 2026-09-22
with the separable arm reproducing exactly and the other two not); the
repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at `882f252`,
code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`, checked at `d216dbc`); and the re-run of 2026-09-26 under this
version's rules (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, code
`src/rerun_v3.py`, outputs `out-v3-rules/`, checked at `70be9fb`); **the
controls re-run of 2026-10-03 under the piece rule**
(`docs/2026-10-03-controls-rerun.md` at `821f154`, method
`docs/controls-rerun-method-2026-10-03.md`, code `src/rerun_controls.py`,
outputs `out-controls-rerun/`, checked at `e184a6e`), which the rulings of
2026-10-03, page 2, made a precondition of the registration review; **and the
short pre-stated run of the same day** (`docs/2026-10-03-short-prestated-run.md`
at `853988f`, method at `9e978d9`, code `src/short_prestated_run.py`, outputs
`out-short-prestated-run/`; checked by a second session, main line at
`53c8100`). The
last two loaded the twelve committed base-recipe models, checked each file's
fingerprint against the committed list before loading it, trained nothing and
spent nothing. The one part that spent money is item R-11. Total spent on the rehearsal so far:
about $0.57, the sum of the compute ledger's three slice rows, of the
rehearsal line's $10 (item 10 of the 2026-09-21 ruling; section 12.3).

**The models every toy result rests on: thirty, all committed.** The fifteen
trained toy models behind the repairs and the re-run (arms T, C, F and M and
the ownership-blind solver, three seeds each) are committed at
`experiments/rehearsal-successor-measure/out-repairs/models/` (main line at
`8038275`, pull request 64), because they cannot be rebuilt from code and
seed (the repairs check at `d216dbc` retrained from clean and got different
nominations) and an uncommitted record the reader cannot open is the form of
ledger item RT-145. The other fifteen are committed too (main line at
`7ed2b0e`, pull request 67): the six free-arm models behind the two training
redesigns that failed (`ckpt_F_curriculum_seed*.pt` and
`ckpt_F_reweight_seed*.pt`, in the same folder) and the nine behind the
grammar attempt (arms T, C and F, three seeds each, at
`experiments/rehearsal-successor-measure/out-grammar-c/models/`). One
fingerprint list, `out-repairs/models/SHA256SUMS`, covers all thirty, with a
`README.md` beside it saying where each file came from. The re-run's
fingerprint check compared three recorded hashes per file with the list for
the first fifteen and found all agree, its check hashed the stored files
themselves and found the same, and the label-search check found all thirty
files on the main line check against the list (MEASURED:
`out-v3-rules/models_sha256_check.json`, `all_agree: true`; the check at
`70be9fb`, section 2.1; the label-search check at `ecd2b6c`, section 4).
**What rests on them: every toy result of 2026-09-25 and 2026-09-26 that
this version quotes.** On the first fifteen: every base-recipe result of the
repairs (`gate_base.json`, `nominate_base_*.json`, `measure_base_*.json`,
`summary_base.json`, the training records `train_*_base_seed*.json` and the
`F/base/*` rows of `diagnose_named_other.json`), the whole of
`out-v3-rules/`, the label search's fits, the whole of
`out-controls-rerun/` and `out-short-prestated-run/` (which use the twelve
models of arms T, C, F and M and not the solver's three), and every toy
figure in sections 3, 5, 7, 8 and 9 of this version. On the six redesign models: the curriculum and
loss re-weighting results of section 4.4 (0 of 3 seeds each). On the nine
grammar-attempt models: the grammar attempt's figures of section 4.4 (774,
730 and 759, and everything in `out-grammar-c/`). Two kinds of figure quoted
in this version are not toy results and rest on no committed model, and are
said to be what they are where they appear: the rented slice's seconds per
step (section 9), a timing of a model that exists on the record as a
checksum only; and the two checks' own re-run figures (the grammar check's
750, 809 and 739; the repairs check's 6 of 12), which are the checks'
verification of a verdict, quoted as such, from retrainings those checks
recorded but did not keep. Decision 22, which asked whether the further
fifteen should be committed, is done.

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
  against random medians of 0.015 to 0.019 (the controls re-run at `821f154`,
  sections 2 and 4). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction, and arm M's mixture reads between the anchors in its
  pre-stated band.** On arm C the read holds the label, the piece
  transplanted holds it at the action position (180, 172 and 150 of 180), and
  the ownership-only transplant lands within 0.004 of the no-transplant rate
  while the whole state moves the action, so it reads 1.0051, 0.9926 and
  0.9974; arm M reads 0.4886, 0.4860 and 0.5449 against a band of 0.3 to 0.7,
  and within 0.0049, 0.0099 and 0.0529 of its true-slot reading at the
  registered site sets (sections 5.2 and 5.3). **Arm C fails the named-other
  condition on every seed and passes its gate on the own-directed condition**
  (section 5.2). *Exercised under the registered rules; the two-arm fallback
  does not fire.* The check of arm M's reading against its true-slot reading,
  which version 3 listed as owed, is done.
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1; and arm T seed 0 on the grammar attempt's unseen pool, at
  −0.1870), above one (arm C at 1.0051), and no verdict (arm F on every seed,
  by the gate and by the fit floor; control 2 on every toy model it applies
  to). *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised, before the piece rule of 2026-10-03.
  The ownership-blind solver's run through the nomination under that rule is
  owed before the registration review, by ruling (section 7.3, the last
  paragraph).*
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the whole-state floor (the smallest toy denominator under
  the registered rule is 0.4863, arm C seed 2, among the pairs that read, and
  0.4263 on arm F seed 0, which is described and not read; section 17,
  failure 1); the
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
  at fifteen different places on the toy (section 7.3, item 7), which closes
  the citation gap version 3 recorded.
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 0.9926 and 0.9974 under
  the registered rules on 2026-10-03. *Exercised.*
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
  force one. **Both things this left open were ruled on 2026-10-03**: fifty timed
  steps are accepted for the second release's arithmetic, with the
  five-hundred-step figure taken from the first full-size run (decision 17);
  and the registration says what is true of the handshake today, that on the
  normal path the laptop deletes the machine and the machine's own watcher is
  a backstop (decision 18; weakness W9). Cost:
  about $0.57 across three rows against the item's $3 (section 12.3).

**The seven controls, and what exercised each under the registered rules.**
Controls 1, 3, 6 and 7, the true-slot reference, the rider and the stricter
row: the controls re-run, on all twelve toy models, checked (section 7.3).
Control 4 as redefined: the short pre-stated run, on all twelve, **checked: the check of the short run at `53c8100`**; the same fact was measured independently, with
separately written code, by the check of the controls re-run (section 7.3,
item 4). Control 5 holds by construction. **Control 2 was never exercised at
toy scale, and the registration says so in terms** (section 7.3, item 2). It
carries no pre-stated number, so by John's ruling nothing about it is an
unexercised quantity in the sense of item 5 of the 2026-09-21 ruling; the
part of its code after the floor has run once, in a run labelled NOT A
RESULT.

**What happens next.** The ordinary competing solver is run under the piece
rule, method first, by another session, and checked; this version and the
late-evening ruling's record are checked under the pairing rule by a session
that did not write them; this text is brought into line with both; then it
goes to Gate A, both tiers, when John opens that review; the registration
commits when both tiers are answered and he rules. There is no target date;
the only date is the kill date of 2026-10-18 (section 11).

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. **Done.** The first independent review of version 3 (RT-230 to RT-236);
   John's rulings of 2026-10-03 on it and on version 3's open decisions; the
   controls re-run under the registered rules, and its check; John's three
   rulings after it; the short pre-stated run; John's evening ruling. The check of the short
   pre-stated run and of the evening ruling's record; John's late-evening
   ruling on this version's seven questions. **Owed before step 2:** the
   competing solver's run under the piece rule, and its check; the check of
   this version and of the late-evening ruling's record under the pairing
   rule.
2. This text, brought into line with those → **Gate A, both tiers**, opened
   by John → registration commit. **No target date. Kill date 2026-10-18**,
   past which committing it takes a fresh ruling naming what comes off the
   back end (item 23 of the 2026-09-21 ruling).
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
     item 1), the nomination of that run's ownership read on development
     episodes, reported against the four-fifths floor: whether any size of
     piece reaches it, with the read's held-out count at every layer, the
     chosen piece's own count, and the candidates the nomination chose among
     (the review of version 3, RT-235; section 7.5)**. A fourth thing comes
     back with them: **the five-hundred-step timing that rehearsal item R-11
     asked for is taken from this run, and the eleven later runs are repriced
     from it before the second release is asked for** (ruled 2026-10-03,
     decision 17). If it fails the
     gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches. **If no size of piece reaches the fit floor,
     that is a stop before the second release draws, beside the learn-both
     stop** (unchanged by the fifth outcome term: the rulings of 2026-10-03,
     page 11, item 6): it
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
   A no verdict on arm C fires the two-arm fallback, and a no verdict on arm
   M drops arm M (section 3).
8. If arms T and C separate: arm F read on the frozen procedure, confirmation
   seeds. If arm F reads, the outcome is R1; if it returns no verdict, the
   outcome is the fifth term, "metric validated, degree not read", with its
   reason. Findings; Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
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
  run passes the learn-both gate but no size of piece of its ownership read
  reaches the fit floor on development episodes. Not an outcome on its own: a stop before the second
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
  Nor is control 2's *no verdict* on an arm that has not learned the
  named-other condition or whose read of the named agent misses its floor:
  the registration says in advance that it is the expected result. Nor is a
  *no verdict* under the fit floor: that is a registered outcome of the
  procedure with its reason printed.
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
main line, unchanged. No ledger row has been written since: the ledger's
last row on the main line at `f32ba0c` is still the second 2026-09-25 row,
and nothing in the work of 2026-10-03 rented or spent anything.

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
- **The successor gets a new experiment directory with its own registration
  (`experiments/08-…`), and the compute ledger stays where it is**, in
  experiment 06's folder, as the programme's one record of money (ruled
  2026-10-03, decision 8).

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
run cost and the five-hundred-step timing, and the later runs are repriced
from it before the second release is asked for (the note's "what this does
not settle", item 2; ruled 2026-10-03, decision 17); and arm M's per-run cost is a ledger inference until a run
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
piece carries the counterfactual on arm C, although the pieces transplanted
hold the label at the action position (section 5.2). A network built with ownership
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
registration text, as ruled 2026-10-03 (decision 9).

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
both). The rider and the honest gap between the lesion result and the
transplant result do the rest. Control 2, which was meant to help here, has
never run on any toy model and is expected to return no verdict at
registered scale too (section 7.3, item 2), so it is not counted on. What the
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
argued, not measured (the slice findings at `9f802db`, section 3). **Ruled
2026-10-03 (decision 17): fifty steps are accepted for the second release's
arithmetic, and the five-hundred-step figure comes from the first full-size
run, with the later runs repriced from it.**

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor, and arm M's code has never run on the rented machine.** The
laptop half has (section 10, R-11). **What the registration says, as ruled on
2026-10-03 (decision 18, option (b)): on the normal path the laptop deletes
the machine, and the machine's own watcher is a backstop for a laptop that
never answers.** That is what is true today: the laptop deletes the machine
the moment it writes the receipt, so the machine's own "receipt found" is
close to unobservable by construction. Option (a), making the laptop wait for
the machine's acknowledgement, is the repair if a later run shows the laptop
failing to answer, and it comes off the Weekend 2 launcher items. **The
caution John ruled with is carried: twelve full-size runs rest on a backstop
that has not fired against the real vendor.** **Beside it (ruled, the rulings
on the review of version 2, RT-228): arm M's code,
`experiments/rehearsal-successor-measure/src/arm_middle.py`, has run only on
this laptop; the rented slice timed arms T, C and F only, and no training
entry point for arms T, C or M exists on the rented machine yet.** By failure
6's discipline both are untested until they have met the far end; step 4 of
section 11 is where arm M first does.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. Control 6 says the whole-state transplant carries more than identity
on the entangled arms.** On the relaxed set, at the site sets the registered
rule nominates, the same-value cell moved on arm C in 0.51 to 0.63 of trials
and on arm M in 0.22 to 0.32, where a transplant that moved only who is
acting would move nothing (section 7.3, item 6; the controls re-run at
`821f154`, section 4). On those arms the reading cannot be read as purely a
statement about where the ownership answer lives. It is reported as the
caveat it is, on every arm, in the reporting table.

**W12. The fit floor tells an empty instrument from a ceiling; it does not
tell an entangled act from an ownership answer the read did not find.**
Section 3's residual admission. A piece that clears the floor shows the label
is in those directions at the action position; a reading near 1 with such a
piece shows the directions the read found do nothing on their own; that the act's ownership
answer is carried by directions the read did not find, at sites the rule did
not nominate, is not excluded by anything in this design. The rider, the
sensitivity rows and control 3's distribution make that visible; they do not
remove it.

**W13. The piece is shown to hold the label at the action position only.**
The floor is applied there, where the registered read is fitted. Where the
chosen site covers several positions the same directions are transplanted at
all of them, and on the toy the piece often falls below four fifths away from
the action position: on arm C seeds 1 and 2, and, position by position, on
arm M (sections 3, 5.2 and 5.3; **checked: the check of the short run at `53c8100`**). So
a sentence of the form "the piece held the label and transplanting it did
nothing", or "did half", is true at the action position and is not shown
across the whole site. The readings do not depend on it: they come from what
the transplants do to the action. John ruled that the figure is reported both
ways and gated in neither; the alternative put to him and not taken was to
require four fifths at every position of the site.

**W14. Two of the seven controls say less than their names suggest.** Control
4 as redefined is a known-answer test of the pairing and the code: it cannot
fail on a correctly built model, so its pass is not evidence about what any
model knows early. Control 2 has never run on a toy model, has no pass line,
and is expected to return no verdict. Neither is a weakness of the reading
itself, but a reader counting controls should know that two of the three
that hold (controls 4 and 7) test the pairing and the code and not a model,
and that the controls which say something about a model are 1, 3 and 6.

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

## 15. Decisions, each now ruled

**Every decision below is now ruled or done.** Each keeps its number from
version 3, with the ruling that settled it and the alternative that was put
and not taken, so that the reader can see what was chosen against what.
Decisions 2, 3, 4, 8, 9, 10, 13, 14, 17, 18 and 19 were ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, "Agreed on all" to sixteen pages put to John with a
recommendation each; the record says he ruled from the index and three pages
his attention was drawn to). Decisions 15 and 16 were ruled that morning and
changed later the same day. Five new entries, 24 to 28, record the other
rulings of 2026-10-03, and entry 29 the seven questions this version raised,
ruled the same night.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references; on arm M the true-slot reading and the formula of
   section 5.3 are one check (the Gate C rulings, RT-223).

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Ruled 2026-10-03 (page 4).* **The alternative not taken:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for: a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Ruled 2026-10-03 (page 5): by architecture, with no penalty against
   transplantable ownership directions.* **The alternative not taken:** train
   arm C with a penalty that punishes any linearly transplantable ownership
   direction, which trains the system against the very instrument that will
   measure it.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Ruled 2026-10-03 (page 6).* **The alternative not taken:** transplant
   the whole forward state at every
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
   (`experiments/08-…`), not another amendment to MVM-0a. *Ruled 2026-10-03
   (page 7), with one thing settled alongside: the compute ledger stays in
   experiment 06's folder as the programme's one record of money.* **The
   alternative not taken:** number it as a further amendment, which keeps one
   budget instrument and one ledger but attaches new work to a closed
   registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Ruled 2026-10-03 (page 8).* **The alternative not
   taken:** add a condition in which the model's own name appears as a token,
   which would match the conditions exactly and would put an ownership cue
   into the text.

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Its shape was ruled on
    2026-09-25 (the queue ruling, page 1h) and its two-of-three clause on
    2026-09-26 (RT-220); its standing as a precondition and not a finding was
    ruled 2026-10-03 (page 9).*

11. **The registered wave launches staggered**: step 5a, then 5b. *Ruled
    2026-09-21 (item 12), with item 23 settling which step the second kill
    date binds; the fit-floor stop added to step 5a by John's ruling of
    2026-09-26 on the route (b) result.*

12. **The proposal went to an independent review before John ruled on its
    open items**, per the protocol. *Done: the review of version 3, RT-230 to
    RT-236, main line at `4cb7f8e`.*

13. **The successor's registration names a launcher that waits for the
    receipt, and makes "the trainer does not delete its own machine" part of
    the registered recipe.** *Ruled 2026-10-03 (page 10).* The launcher
    file is named (section 5; RT-228); the laptop half of the handshake works
    against the real vendor and the machine half was never given the chance
    (section 10, R-11). **The alternative not taken:** leave the shutdown
    policy in unregistered operations scripts, where a later edit can quietly
    remove it. *The ruling packet's page for this decision gave as a reason a
    sentence about the programme's largest single loss; the check of the
    packets found that sentence is not what the ledger shows, and it is not
    carried here. The decision stands without it.* (Version 1's account of what one failure cost merged two events;
    the Gate C review of version 1, finding RT-186, corrected it, and the
    sentence is not repeated here.)

14. **What a no verdict maps to.** *Ruled 2026-10-03 (page 11), closing the
    no-verdict finding RT-182 of the review of version 1:* a no verdict on arm
    C fires the two-arm fallback already ruled in advance; a no verdict on
    arm M drops arm M and carries it as an extension on the weekend roadmap;
    a no verdict on arm F after arms T and C have separated is a fifth
    registered term, *metric validated, degree not read*, with the reason
    after a colon. The stop after the first full-size free-model run is
    unchanged. **The alternative not taken:** keep four terms and report an
    arm F no verdict under R1 with a sentence, which is the over-reading the
    finding warns against. Whether the fifth term counts as satisfactory is
    entry 28.

15. **Control 2's tolerance.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation, 0.05 over the random subspace
    (page 12). After the controls re-run showed the control has no figure on
    any toy model, he **withdrew it**: control 2 is kept as a reported
    description with no pre-stated pass line
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the
    morning's rulings file carries a dated note under its decisions table).
    Section 7.3, item 2. **Alternatives not taken:** the 0.018 room of the
    no-transplant rule; and exercising the control on a made-up case built
    for the purpose.

16. **Control 4's standing.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation that it be reported and not a
    control that holds (page 13), on the account that arms C and F "receive
    the ownership signal by other routes". After the controls re-run and its
    diagnostic he **reversed it**: the control is redefined on the positions
    before both twins' first own turns, and it holds (the same file, ruling
    2; the same dated note). The account is withdrawn. Section 7.3, item 4.
    **The alternative not taken:** redefining the positions and keeping the
    control reported only.

17. **Whether fifty timed steps meets item R-11's five hundred.** The plan
    John authorised ran fifty after five warm-up steps; the item says five
    hundred after fifty. Recommendation: accept fifty for the second release's
    arithmetic, and take the five-hundred-step window from the first
    registered-size run of step 5a rather than from a new rental, repricing
    the later runs from it before the second release is asked for. *Ruled
    2026-10-03 (page 14), as recommended.* **The alternative not taken:**
    hold R-11 to its
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
    costs nothing more to rent. *Ruled 2026-10-03 (page 15): option (b), with
    (a) as the repair if a later run shows the laptop failing to answer, and
    (a) taken off the Weekend 2 launcher items. The caution put with it is
    carried in weakness W9: twelve full-size runs rest on a backstop that has
    not fired against the real vendor.*

19. **The position sets of section 7.2 are the rehearsal's four, by name**,
    with the second described as the action position and the answer-marker
    token just before it. The ruled position clause does not say how
    positions are grouped (the repairs findings, section 3); registering the
    rehearsal's grouping is the only one that has been exercised, now under
    the registered rule. *Ruled 2026-10-03 (page 16): the rehearsal's four, by
    name.* **The alternative not taken:** register the ruled clause literally, the action position and each position
    between the source assignment and the action, one set each, which has not
    been run and would change the count.

20. **Which reading of the layer-0 exclusion is registered.** The RT-216
    ruling's first sentence keeps layer 0 at the action position set only;
    its parenthesis names the position sets spanning the acting turns, which
    on this grammar is `post-identity` alone. The two readings differ on
    `action+ans` and `action+3`, and on the toy they give the same twelve
    nominations (the check at `70be9fb`, section 4.4). *Ruled 2026-09-26: the
    reading as run, layer 0 kept at `action` only, 45 site sets on the toy and
    325 on the registered model.* Registered in section 7.2, item 2. The
    alternative that was put and not taken: the narrower reading, layer 0
    removed at `post-identity` only (55 and 351), which follows the ruling's
    parenthesis and keeps two more site sets that on the separable arms do
    move the action.

21. **The fit floor is applied per arm and seed, not per arm.** The RT-212
    ruling says a read that misses the floor "returns no verdict on that
    arm"; the re-run applied it per seed, and the check calls that an
    interpretation, moot on the toy because every arm passes or fails on all
    three seeds alike (the check at `70be9fb`, section 4.1). *Ruled
    2026-09-26: per arm and seed.* Written into sections 6.4 and 7.2. The
    alternative that was put and not taken: per arm, with the arm returning
    no verdict if fewer than two seeds of three clear.

22. **Whether the fifteen further toy models get the same treatment as the
    fifteen committed.** *Done: pull request 67 (main line at `7ed2b0e`)
    committed the six redesign models under `out-repairs/models/` and the
    nine grammar-attempt models under `out-grammar-c/models/`, with the one
    `SHA256SUMS` covering all thirty.* Section 10 now says that every toy
    result of 2026-09-25 and 2026-09-26 rests on committed models.

23. **The registered read is one read per layer at the action position, with
    a site set's fit being its worst layer (new, and ruled with the
    revision).** Put here so the choice is on the record beside the others:
    the rule's read is `repairs.fit_reads`, one logistic regression per layer
    at the mask token, scored on held-out development episodes; the label
    search's pooled per-site-set read is a different quantity and is not
    registered (section 7.2, item 3). *Ruled 2026-09-26, in John's revision
    instruction for this version.* The alternative that exists and was not
    taken: register the pooled read, which scores higher on arm F (0.556
    against 0.172 on seed 0) because it strings positions together and
    averages a span that starts at the model's own marker word, and which the
    layer-0 removal would then cut into.

24. **The fit floor applies to the piece that is transplanted** (the review
    of version 3, RT-230, serious). *Ruled 2026-10-03 (page 1), option (b):
    only sizes whose own held-out accuracy clears four fifths may be chosen,
    and that accuracy is printed beside the whole read's.* Sections 6.4 and
    7.2. **The alternative not taken:** fixing the size at 8 directions with
    the smaller sizes as extra rows.

25. **The controls re-run comes before the registration review** (the review
    of version 3, RT-233, serious). *Ruled 2026-10-03 (page 2); done and
    checked the same day* (sections 7.3 and 10).

26. **The review's four minor findings, RT-232, RT-234, RT-235 and RT-236,
    are accepted as the review states each fix.** *Ruled 2026-10-03 (page
    3).* The fit as a count on a named device and number format (section
    7.2, item 1); the whole-state floor applied twice (section 6.4, item 1);
    the fuller report for the first full-size free-model run (section 7.5);
    the depths stated the same way (section 7.2, item 1). For RT-232 this
    version follows the review's own wording and not the packet's shortening
    of it, as the check of the packets advises.

27. **The chosen piece's accuracy at the other positions of its site is
    reported, not gated, and printed both ways.** *Ruled 2026-10-03
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
    `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
    ruling 2).* Section 7.2, item 3; section 7.5. **The alternative not
    taken:** requiring four fifths at every position of the site.

28. **The fifth registered outcome is satisfactory, and is stated as weaker
    than R1.** *Ruled 2026-10-03 in John's own words, "Yes, satisfactory and
    weaker than R1" (the evening ruling, ruling 1).* That morning's record
    had counted his "Agreed on all" as settling it; the check of the packets
    found that recording honest but thin and asked him to confirm or overturn
    it, and he confirmed it. Section 3.

29. **The seven questions this version put to John.** *Ruled 2026-10-03, late
    evening, "Agreed on all" (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).* The
    floor on the piece only; the piece rule applied after the layers are
    chosen; the registered fit on the laptop's processor; the toy's episode
    counts at full size; twenty random pieces for control 2; two seeds of
    three when an arm's seeds disagree; the competing solver run under the
    piece rule before the registration review. Section 19 gives each with the
    alternative not taken.

*Nothing above is registered. The registration commit, if it comes, follows
the checks owed on this version, the competing solver's run, and Gate A,
and every run it affects is launched after it.*

---

## 16. Where the pieces are

- This proposal: `docs/successor-experiment-proposal-2026-10-03-v4.md`.
- Version 3, unedited: `docs/successor-experiment-proposal-2026-09-26-v3.md`
  (main line at `6d4ec3a`, pull request 71). Version 2, unedited:
  `docs/successor-experiment-proposal-2026-09-26-v2.md` (main line at
  `a3013be`, pull request 54). Version 1, unedited:
  `docs/successor-experiment-proposal-2026-09-21.md`.
- The first independent review of version 3, whose two serious findings and
  five minor ones this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
  (RT-230 to RT-236; main line at `4cb7f8e`, pull request 74), with its
  scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/`.
- The three rulings of 2026-10-03 this version is built to:
  `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (sixteen pages;
  main line at `56a5a86`, pull request 75; its dated note at `fe5df65`), with
  its packet `docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md`;
  `docs/rulings/2026-10-03-controls-rerun-rulings.md` (three rulings; main
  line at `fe5df65`, pull request 77), with its packet
  `docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md`; and
  `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (the
  evening ruling; main line at `f32ba0c`, pull request 81). **This version
  quotes the rulings files and the toy records, not the packets.**
- The check of the two packets and their records:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`
  (main line at `f32ba0c`, pull request 81).
- The controls re-run: `docs/2026-10-03-controls-rerun.md`, its method
  `docs/controls-rerun-method-2026-10-03.md`, code
  `experiments/rehearsal-successor-measure/src/rerun_controls.py` and the
  after-the-fact diagnostic `src/posthoc_control4.py`, outputs
  `experiments/rehearsal-successor-measure/out-controls-rerun/` (main line at
  `821f154`, pull request 76); its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-controls-rerun-check-scripts/` (main
  line at `e184a6e`, pull request 79).
- The short pre-stated run: `docs/2026-10-03-short-prestated-run-method.md`
  (main line at `9e978d9`) and `docs/2026-10-03-short-prestated-run.md` (main
  line at `853988f`; pull request 80), code `src/short_prestated_run.py`,
  outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/`,
  of which `part_c_NOT_A_RESULT.json` is named for what it is. Its check,
  which also checks the record of the evening ruling:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/`.
  (main line at `53c8100`, pull request 82).
- John's late-evening ruling on this version's seven questions:
  `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
  filed with this version on pull request 83.
- The Gate C tier 1 review of version 2, whose one fatal finding and four
  serious findings this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
  (RT-212 to RT-229; main line at `c17dbdc`, pull request 56), with its
  scripts in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.
- The earlier rulings, all still binding:
  `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` (main line at
  `3af189d`, pull request 60; its refinements at `4bb5727`, pull request 63;
  the annotation of refinement 2's arm C clause at `da41c20`, pull request
  68; the resolution of RT-212 item 3 after the label search at `a11f1d3`,
  pull request 69);
  `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` (five decisions and
  five annotations; main line at `62c3824`, pull request 53);
  `docs/rulings/2026-09-26-weekend-1-queue.md` (nine pages, 2026-09-25);
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (the
  releases, the staggered launch, halt not trim, item 23 on the dates);
  `docs/rulings/2026-09-23-nomination-label.md` and
  `docs/rulings/2026-09-23-range-and-direction-only.md`;
  `docs/rulings/2026-09-20-center-as-degree.md` and
  `docs/rulings/2026-09-20-december-result-roadmap.md`. John's rulings of
  2026-09-26 on decisions 20 and 21 are recorded in the first of those files
  (main line at `9ed9f8c`, pull request 72); his ruling on decision 23 is
  carried from his revision instruction for version 3 and has no ruling file
  of its own.
- The three earlier rehearsals: `docs/2026-09-21-successor-measure-rehearsal.md`
  (main line); `docs/2026-09-26-rehearsal-repairs.md` (main line at
  `882f252`, pull request 52; checked at `d216dbc`, pull request 58); and
  `docs/2026-09-26-toy-rerun-v3-rules.md` (main line at `9d9d31a`, pull
  request 62; checked at `70be9fb`, pull request 65), with their method notes
  `docs/successor-measure-rehearsal-method-2026-09-21.md`, its denominator
  addendum, `docs/rehearsal-repairs-method-2026-09-25.md` and
  `docs/toy-rerun-v3-rules-method-2026-09-26.md`; code and outputs under
  `experiments/rehearsal-successor-measure/` (`out/`, `out-repairs/`,
  `out-v3-rules/`).
- The thirty trained toy models:
  `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one)
  and `experiments/rehearsal-successor-measure/out-grammar-c/models/` (nine),
  with the one `SHA256SUMS` and the `README.md` in the first folder (main line
  at `8038275`, pull request 64, and `7ed2b0e`, pull request 67).
- The grammar attempt: `docs/2026-09-26-grammar-attempt.md` (main line at
  `ff778ea`, pull request 57; its method note
  `docs/grammar-attempt-method-2026-09-25.md`; outputs `out-grammar-c/`),
  checked at `f1ea004` (pull request 61):
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`.
- The route (b) label search: `docs/2026-09-26-free-arm-label-search.md`
  (main line at `a97c12b`, pull request 66), and its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`
  (main line at `ecd2b6c`, pull request 70).
- The rented slice: `docs/2026-09-25-rented-slice-findings.md` (first attempt,
  main line) and `docs/2026-09-25-rented-slice-attempt-2-findings.md` with
  the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  (main line at `9f802db`, pull request 51; checked at `afb5183`, pull request
  55).
- Amendment A3's closure, registered: `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
  the closure block of 2026-09-25, and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
- The roadmap it implements: `docs/december-result-roadmap-2026-09-20.md`,
  sections 2, 4 and 5 as amended 2026-09-21, with the two dated notes of
  2026-10-03 under its outcome table; the weekend schedule laid over it,
  `docs/weekend-roadmap-2026-09-24.md`.
- The spend record every figure in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, with its
  ceiling note of 2026-09-25 and its rows of 2026-09-21 and 2026-09-25 (lines
  93 to 95).
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate A, both tiers, with the list it is run against,
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
`53c8100`, and a seventh candidate, drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 9,
item 2. All seven were run here, on 2026-10-03, with this session's own
commands, on the committed outputs of the controls re-run
(`experiments/rehearsal-successor-measure/out-controls-rerun/` at `821f154`),
of the short pre-stated run (`out-short-prestated-run/` at `853988f`) and of
the repairs (`out-repairs/` at `882f252`). `.venv/bin/python` stands for the
project's own Python, which lives in the main checkout and was run by its
full path from this worktree. Nothing was rented, created, trained or spent,
and no registered, ruling or protocol text was edited. **Version 3's pass ran
the same tests on the earlier re-run's outputs; every block below is this
session's own run and not a copy of that one.**

**1. A comparison whose denominator was zero. Does not fire. MEASURED.** Part
one asks whether the ceilings typed in trace to committed measurements. The
no-transplant rate is measured on every arm and seed
(`measure_*_seed*.json`, `primary.reading.accuracy_untouched`), not assumed.
Part two asks for the denominator and the top of the scale when the target is
absent, for every arm and seed at the site set this version's rule chooses:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
print('arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form) | status')
for a in 'TCFM':
  for s in '012':
    m=json.load(open(f'{O}measure_{a}_seed{s}.json'))
    r=m['primary']['reading']
    u,w,o=r['accuracy_untouched'],r['accuracy_whole'],r['arm_own_accuracy']
    print(f'{a}/{s}       {u:.4f}    {w:.4f}  {o:.4f} |  {w-u:.4f}       {0.8*(o-u):.4f}    |  {(w-u)/(w-u):.4f} | {"described only, no reading" if m["primary"]["described_only"] else "reads"}')
"
arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form) | status
T/0       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/1       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/2       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
C/0       0.0512    0.5400  0.5487 |  0.4888       0.3980    |  1.0000 | reads
C/1       0.0488    0.5550  0.5813 |  0.5063       0.4260    |  1.0000 | reads
C/2       0.0600    0.5463  0.5525 |  0.4863       0.3940    |  1.0000 | reads
F/0       0.0587    0.4850  0.5587 |  0.4263       0.4000    |  1.0000 | described only, no reading
F/1       0.0563    0.5675  0.5663 |  0.5112       0.4080    |  1.0000 | described only, no reading
F/2       0.0688    0.5300  0.5563 |  0.4613       0.3900    |  1.0000 | described only, no reading
M/0       0.0125    0.7800  0.8712 |  0.7675       0.6870    |  1.0000 | reads
M/1       0.0175    0.7738  0.8800 |  0.7563       0.6900    |  1.0000 | reads
M/2       0.0138    0.7937  0.8712 |  0.7800       0.6860    |  1.0000 | reads
```

Among the nine pairs that read, the smallest denominator is 0.4863 (arm C
seed 2); arm F seed 0, which is described and not read, has 0.4263. Every
denominator clears what the floor needs. The top of the scale is 1.0000 on
every arm under the registered form. The repair of the per-arm-ceiling
finding (RT-172) holds on the controls re-run's data as it held on the
earlier runs'. One thing to watch, ARGUED: on arm F the denominator clears
the floor by only 0.026 to 0.103.

**2. A probe target that cannot be recovered in principle. Fires on the free
arm, and is caught by a registered rule. MEASURED.** Part one, the
route-sentence search, with this design's own wording in the pattern, run on
sections 0 to 16 of this file (the text before this section):

```
$ awk '/^## 17\. /{exit} {print}' docs/successor-experiment-proposal-2026-10-03-v4.md > "$T/v4-through16.md"
$ grep -n -iE 'route by which|carried by the token|forced by the loss|is the input token' "$T/v4-through16.md"
1256:   own**. *The route by which that quantity reaches the model's states, in one
1257:   sentence:* the marker word is the input token at every turn the model's own
1258:   assignments are spoken on, so it is carried by the token into the running
1262:   claim, that which marker word is the model's own is forced by the loss at
```

A route sentence exists (section 7.2, item 1), and the fourth match is the
sentence striking version 2's loss clause, not a route. Part two, the two
runs on the same instrument with the same bar. The committed counts, per
running state, serve as the positive control (arms T, C and M) and the target
run (arm F):

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
print('right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions')
for a in 'TCFM':
  for s in '012':
    n=json.load(open(f'{O}nominate_{a}_seed{s}.json'))
    f=n['fits']
    print(f'{a}/{s}', ' '.join(f"{f[l]['whole']:>3}|{max(f[l]['piece'].values()):>3}" for l in sorted(f)), '->', n['primary']['status'])
S=json.load(open(O+'summary.json'))
print('separation:', {s:round(v['C_minus_T'],4) for s,v in S['separation'].items()}, 'all clear 0.5:', all(v['clears_0_5'] for v in S['separation'].values()))
print('arm M readings:', [round(json.load(open(f'{O}measure_M_seed{s}.json'))['primary']['reading']['degree'],4) for s in '012'])
"
right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions
T/0 180|180 180|180 180|180 180|180 180|180 -> nominated
T/1 180|180 180|180 180|180 180|180 180|180 -> nominated
T/2 180|180 180|180 180|180 180|180 180|180 -> nominated
C/0  13| 14 179|180 180|180 180|180 180|180 -> nominated
C/1  13| 14 177|172 174|167 177|175 173|162 -> nominated
C/2  13| 13 176|178 177|175 180|171 180|179 -> nominated
F/0  13| 14  32| 34  26| 30  19| 25  12| 20 -> read failed its floor: no size's piece reaches four fifths
F/1  13| 14  12| 17  21| 18  24| 19  21| 20 -> read failed its floor: no size's piece reaches four fifths
F/2  13| 14  18| 24  25| 29  20| 26  20| 24 -> read failed its floor: no size's piece reaches four fifths
M/0 180|180 180|180 180|180 179|179 178|178 -> nominated
M/1 180|180 180|180 180|180 180|180 180|180 -> nominated
M/2 180|180 180|180 180|180 180|180 180|177 -> nominated
separation: {'0': 1.0051, '1': 0.9926, '2': 0.9974} all clear 0.5: True
arm M readings: [0.4886, 0.486, 0.5449]
```

The middle limb of failure 2, "the second run clears the bar and the first
does not", is exactly the toy's state: on arms T, C and M a piece reaches 144
of 180 at every running state past the injection, and on arm F none does at
any (at most 34). **This is the fatal finding of the review of version 2,
RT-212, and it still fires on the free arm.** What the design does about it
is unchanged in kind and sharper in aim: the floor now sits on the piece that
is transplanted (RT-230), it turns the firing into a registered *no verdict*
on arm F on every seed, and the withdrawn number is not reported as a
reading. The route (b) search for a target the free system does carry found
none at the floor (section 7.2, item 1), so the failure is caught rather than
repaired, and the registration says so. **A second place the same failure
fires, new in this version and stated in it:** the named agent's read that
control 2 needs cannot be recovered at the floor on any toy model (section
7.3, item 2). That control carries no pre-stated number, by ruling.

**3. A cell that is empty by construction. Does not fire on the reading. It
describes control 2 on the toy, which the text says in terms. MEASURED.** Part
one, the cells: control 6's two cells on the relaxed set, the positions
control 4 transplants at, and control 2's reach:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
for a in 'TCFM':
  for s in '012':
    c=json.load(open(f'{O}measure_{a}_seed{s}.json'))['primary']['controls']['6']
    print(f' {a}/{s} same-value trials', c['same_value_trials'], 'different-value trials', c['different_value_trials'])
a=json.load(open('experiments/rehearsal-successor-measure/out-short-prestated-run/part_a.json'))
print('control 4 as redefined, positions transplanted per pair:', a['positions_per_pair'])
print('control 2: toy models on which it returned a figure:', sum(1 for a_ in 'CF' for s in '012' if json.load(open(f'{O}measure_{a_}_seed{s}.json'))['control2']['status']!='no verdict'), 'of 6 it applies to')
"
 T/0 same-value trials 81 different-value trials 719
 T/1 same-value trials 81 different-value trials 719
 T/2 same-value trials 81 different-value trials 719
 C/0 same-value trials 81 different-value trials 719
 C/1 same-value trials 81 different-value trials 719
 C/2 same-value trials 81 different-value trials 719
 F/0 same-value trials 81 different-value trials 719
 F/1 same-value trials 81 different-value trials 719
 F/2 same-value trials 81 different-value trials 719
 M/0 same-value trials 81 different-value trials 719
 M/1 same-value trials 81 different-value trials 719
 M/2 same-value trials 81 different-value trials 719
control 4 as redefined, positions transplanted per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
control 2: toy models on which it returned a figure: 0 of 6 it applies to
```

Both of control 6's cells have trials on every arm and seed, so the RT-173
repair holds. Control 4 as redefined transplants at one position or more in
every pair, so it is never an empty test (that line is from the short
pre-stated run; its check added that the transplant does write there, since
noise added to the donor's state changes the outputs on all twelve models).
Control 2 returned
a figure on none of the six toy models it applies to, and has zero clearing
site sets by construction on arms T and M, which the repairs rulings' item 5
records as not applicable. **So control 2's cell is empty at toy scale. The
text does not hide it: the registration says the control never ran, it
carries no pass line, and its no verdict is the expected result.** Whether a
control in that state should be in the registered design at all was John's to
rule and he ruled it stays (section 7.3, item 2). Part two, the generator
property that empties a cell, is section 4.2's distinctness, read and named
there. Part three, thresholds at both ends, for every threshold this version
attaches to a count:

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
print('piece floor on the toy: four fifths of 180 held-out episodes =', Fr(4,5)*180, '; one episode is %.4f of the scale'%(1/180))
"
learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05: 790 share 0.2633 tail 0.0485
a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability 0.0485 per seed
no-transplant rule at own-directed 0.2633: formula 0.1052, broken-pairing rate 0.1250, miss 0.0198, flagged by the 0.018 room: True, margin 0.0018
no-transplant rule at own-directed 0.56: formula 0.0629, broken-pairing rate 0.1250, miss 0.0621, flagged by the 0.018 room: True, margin 0.0441
largest measured miss 2026-09-21: 0.017536; inside 0.018: True
piece floor on the toy: four fifths of 180 held-out episodes = 144 ; one episode is 0.0056 of the scale
```

The bar reproduces at 790 of 3,000. The no-transplant rule fires on the
broken end and passes on the working end, and the case the allowance was set
from is inside it; at the bar it detects a broken pairing by 0.0018, which is
printed in the reporting table. The lesion collapse line misreads a fully
collapsed arm 4.85% of the time per seed, which is what the two-of-three
clause of section 8.2 is for. The piece floor is 144 of 180 on the toy,
against a no-information level of about 13 and a best free-arm piece of 34 at
one end and built-arm pieces of 150 to 180 at the other, so it has room on
both ends on the toy; one episode is 0.0056 of the scale, which is why the
device is named and why the caution about 180 held-out episodes is carried
with the ruled counts (section 9). **Control 4's pass line, bit-identical
outputs, has no working end to test: it cannot fail on a correctly built
model. That is said in section 7.3, item 4, and it is why the control is
described as a known-answer test and not as evidence.** The lesion figures
themselves:

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

And the site-set family this version registers, counted by the rule. The
command and its output are section 18, which prints the list itself: 325 site
sets and 1,300 comparisons on the registered model, 45 and 180 on the toy.

**4. A claim of measurement with no record, or a record that does not
reproduce. Fires on one class of figure, said so in the text. MEASURED.** Part
one, the two sweeps, run on sections 0 to 16 of this file (cut at this
section's heading, because this section's own output blocks match the
patterns and would count themselves):

```
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T/v4-through16.md"
759
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T/v4-through16.md"
233
$ grep -c MEASURED "$T/v4-through16.md"; grep -c ARGUED "$T/v4-through16.md"; wc -l < "$T/v4-through16.md"
68
14
3406
$ grep -c 'checked: the check of the short run' "$T/v4-through16.md"
8
```

Part two was run by reading every MEASURED claim this version adds or changes
against the file named beside it: the controls re-run's findings and its
`table.md`, `summary.json`, `nominate_*` and `measure_*` files; the check of
the re-run; the short pre-stated run's findings and its `table.md`; the
review of version 3; and the three rulings files. The commands in failures 1
to 3 and candidate 7 are the ones that can be shown. **Where it fires, and
what the text does about it:**

- **Every figure taken from the short pre-stated run was unchecked when this
  version was first filed, and is checked now.** The check ran the script
  again and got byte-identical files (main line at `53c8100`). Each such
  figure carries the words "checked: the check of the short run" (the count
  above).
- **The figure on the average over a site does not reproduce to the episode
  under a different order of addition** (three of eight toy figures move by
  one of 180; the check of the short run, finding 11). The text says the toy
  figures are good to an episode or two and requires 64-bit averaging in the
  registered code (section 7.2, item 3).
- **Version 3's figures for arm C's seeds 1 and 2 do not hold under the piece
  rule** and are replaced by the controls re-run's (RT-230).
- **One figure in the controls re-run's own prose does not reproduce to its
  last digit**: the 0.0100 for arm M seed 1, which is 0.0099 (the check of the
  re-run). This version quotes 0.0099.
- **The competing solvers' figures were taken before the piece rule**, and
  the text says so in three places; the run under the rule is owed before the
  registration review, by ruling (section 7.3, the last paragraph).

The repository's own two checkers, run on the whole document as it stands:

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
  (version 3 had six, all to the label search and its check, which had not merged then; both are on the main line now, and so is the check of the short pre-stated run)
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  (the count of arm M's entangled gate episodes, in a sentence of section 5.3 carried unchanged from version 3: the file cited holds the share and not the count, which is that share of the gate's episodes)
$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain: 0 found
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source: 2 found
  (both in one sentence of section 12.2, cited to the 2026-09-21 ruling that set the two releases, which is the figures' source; the ledger carries them because the ruling did)
```

That the checkers see so little of this document is a statement about the
checkers, not about the rest being clean.

**5. A command that creates something while documented as creating nothing.
Does not fire on anything this document runs; one gap stated. MEASURED.** The
proposal runs nothing that touches a vendor. The list's own test, run by this
session (the last lines of its output; every line above them is `[ ok ]`):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  ...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

The gap is the one RT-228 named and section 5 states: the launcher is named
(`launch_a3_fetch_first.sh`, which carries the guard), the registered
`launch_a3.sh` is not used, and the successor's training entry point for arms
T, C and M on the rented machine does not exist yet.

**6. A remote step tested only against stand-ins. The launcher's check passes;
the design has three such steps, each stated. MEASURED.**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
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
stand-ins, and the registration says what is true of it, as ruled (W9,
decision 18); arm M's code has never run on the rented machine (W9, step 4 of
section 11); the tripwire does not exist as code yet (section 12.5). All
three are said in the text, and none is counted as tested. **One step of a
different kind is in the same state and is said too: the code that withholds
a reading when a control that holds fails does not exist yet** (section 6.4,
item 5); on the toy every such control passed, so the withholding has never
been exercised.

**Candidate 7. An outcome line a plan states in advance that the design
cannot produce on the path it expects. Fires on one line, which the text
states; does not fire on the others. MEASURED.** The drafted test: for each
pre-stated line, name the code path that prints each signal it needs, and
show that path can run in the order the line requires. Run on the committed
outputs:

- **Arm M's pass line** ("between 0.3 and 0.7 on every seed, and within 0.10
  of its true-slot reading"): produced, both halves, at the registered site
  sets (failure 2's output above; section 5.3).
- **The separation line** (0.5 on every seed): produced (failure 2's output).
- **The fifth outcome term** ("metric validated, degree not read"): produced.
  It is where the toy lands, by the path the text expects: the anchors
  separate and arm F returns "read failed its floor".
- **Control 4's pass line** (bit-identical outputs at the two action
  positions): produced on all twelve, by code committed before its output,
  and reproduced byte for byte by its check (main line at `53c8100`).
- **Control 2's reported description**: **cannot be produced on the path the
  toy offers, on any model.** The text says so in terms and attaches no line
  to it. This is the one place the candidate fires.
- **The lesion description**: "arm T collapses on two of three seeds", which
  is what the path produced (failure 3's output above).
- **The rider**: can produce a reading on arms C, F and M on 0 of 9 toy pairs
  on the path it expects, and the text says so with the two reasons (section
  7.2, item 7). Accepted as the report.
- **The two-of-three rule for an arm whose seeds disagree** (section 3):
  ruled, and **never produced on the toy**, where every arm's three seeds
  agree. The code that applies it does not exist yet. Stated here so that it
  is not counted as rehearsed.
- **The $10 wager** (section 12.8), and the money lines of section 12, which
  no ruling of 2026-10-03 changed:

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

Whether the candidate is a new species or an instance of failure 3 is John's
ruling, still open; on this version it catches control 2, which failure 3's
test catches too.

**What this pass leaves open, in one place.** The competing solver's run
under the piece rule; the check of this version and of the late-evening
ruling's record; the code owed before step 4 of section 11 (the training
entry point for arms T, C and M, the tripwire, the withholding of a reading
on a failed control, control 2's twenty random pieces, and the two-of-three
rule); and the reviewer's own pass,
which is still owed, as the protocol says.

---

## 18. The printed site list for the registered model

The site list is registered as the rule that generates it (section 7.2, item
2), and the registration prints the list beside the rule. This is the list,
printed by the rule and not typed by hand. A layer set is written as its
first and last running state: "3-5" is states 3, 4 and 5 together. State 0 is
the running state straight after the input embedding, where the acting
channel is added; states 1 to 12 are the outputs of the twelve blocks. Each
row lists every layer set that begins at that state, and the position sets
each of them is a candidate at. Every site set whose layers include state 0
is a candidate at the action position set only; every other layer set is a
candidate at all four position sets (`action`, the action position alone;
`action+ans`, the action position and the answer-marker token just before it;
`action+3`, the action position and the three positions before it;
`post-identity`, every position from the model's first own turn to the
action). No site set spans every position. The toy's list is printed after
it, for comparison with the 45 the controls re-run's code asserts.

```
$ .venv/bin/python -c "
def contiguous(n): return [(a,b) for a in range(n) for b in range(a,n)]
P4=['action','action+ans','action+3','post-identity']
def name(a,b): return str(a) if a==b else f'{a}-{b}'
for label,n in (('registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)',13),('toy model: 5 running states',5)):
    L=contiguous(n); total=0
    print(label)
    for a in range(n):
        sets=[name(x,y) for x,y in L if x==a]
        ps=['action'] if a==0 else P4
        total+=len(sets)*len(ps)
        print(f'  first state {a:>2} | at {", ".join(ps)} | layer sets: {", ".join(sets)} | {len(sets)} x {len(ps)} = {len(sets)*len(ps)} site sets')
    print(f'  total: {total} site sets, {4*total} comparisons at sizes 1, 2, 4 and 8')"
registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4, 0-5, 0-6, 0-7, 0-8, 0-9, 0-10, 0-11, 0-12 | 13 x 1 = 13 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 1-8, 1-9, 1-10, 1-11, 1-12 | 12 x 4 = 48 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12 | 11 x 4 = 44 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4, 3-5, 3-6, 3-7, 3-8, 3-9, 3-10, 3-11, 3-12 | 10 x 4 = 40 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4, 4-5, 4-6, 4-7, 4-8, 4-9, 4-10, 4-11, 4-12 | 9 x 4 = 36 site sets
  first state  5 | at action, action+ans, action+3, post-identity | layer sets: 5, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12 | 8 x 4 = 32 site sets
  first state  6 | at action, action+ans, action+3, post-identity | layer sets: 6, 6-7, 6-8, 6-9, 6-10, 6-11, 6-12 | 7 x 4 = 28 site sets
  first state  7 | at action, action+ans, action+3, post-identity | layer sets: 7, 7-8, 7-9, 7-10, 7-11, 7-12 | 6 x 4 = 24 site sets
  first state  8 | at action, action+ans, action+3, post-identity | layer sets: 8, 8-9, 8-10, 8-11, 8-12 | 5 x 4 = 20 site sets
  first state  9 | at action, action+ans, action+3, post-identity | layer sets: 9, 9-10, 9-11, 9-12 | 4 x 4 = 16 site sets
  first state 10 | at action, action+ans, action+3, post-identity | layer sets: 10, 10-11, 10-12 | 3 x 4 = 12 site sets
  first state 11 | at action, action+ans, action+3, post-identity | layer sets: 11, 11-12 | 2 x 4 = 8 site sets
  first state 12 | at action, action+ans, action+3, post-identity | layer sets: 12 | 1 x 4 = 4 site sets
  total: 325 site sets, 1300 comparisons at sizes 1, 2, 4 and 8
toy model: 5 running states
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4 | 5 x 1 = 5 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4 | 4 x 4 = 16 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4 | 3 x 4 = 12 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4 | 2 x 4 = 8 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4 | 1 x 4 = 4 site sets
  total: 45 site sets, 180 comparisons at sizes 1, 2, 4 and 8
```

**The count this implies, frozen with the list:** 325 site sets, each at four
sizes of piece, so 1,300 comparisons in the nomination family for each arm
and seed. Under the stricter variant (the sensitivity row) the first row
drops out: 312 site sets and 1,248 comparisons. Both agree with section 7.2,
item 2, and with the review of version 3, which recomputed them ("What was
checked and held"). The registered measurement code asserts the count before
it runs, as the toy code does.

---

## 19. The seven questions put to John, each now ruled as suggested

Seven places where this session did not think the answer was its to give.
**John ruled on all seven on 2026-10-03, late evening, in the words "Agreed
on all", taking the suggestion in each** (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).
The questions are left below as they were put, so that a reader can see what
was chosen against what; "written as run" and "this version says" in them
describe the first filing of this version, and the body now carries each
ruling where it bears. None of them changes a toy figure. **Two things to
hold on to.** Question 6 was the one this session said deserved more of
John's attention than the others, and a general agreement settled it; the
record of the ruling says so. And question 7 leaves a run owed before the
registration review.

1. **Does the whole read still have to reach four fifths, now that the piece
   does?** The ruling of 2026-09-26 (RT-212) put the fit floor on the whole
   read, at the worst layer of the nominated site set. The ruling of
   2026-10-03 (page 1) says only sizes whose own accuracy clears may be
   chosen, printed "beside the whole read's", and does not say whether the
   earlier floor remains a second condition. The controls re-run applied the
   floor to the piece only. On the toy both readings give the same twelve
   verdicts, but a piece can score an episode or two above its whole read.
   *Written as run: the floor is on the piece (sections 6.4, item 2, and
   7.2, item 1).* **Suggestion: the piece only, with the whole read's count
   printed.** Confidence moderate. It is the piece that is transplanted, and
   a second floor is a second way to return no verdict on the arm being read,
   for no gain the first does not give. Strongest alternative: require both,
   which costs nothing on the toy and keeps the 2026-09-26 ruling to its
   letter.

2. **The piece rule is applied after the layers are chosen.** So it decides
   which sizes may be chosen and never changes which layers are used. That
   was the re-run method's own reading, marked as John's to overturn; the
   check noted it has not been put to him in terms. *Written as run (section
   7.2, item 3).* **Suggestion: confirm it.** Confidence moderate. The
   alternative, letting the piece's accuracy also decide between layer sets,
   has not been run, and would need the toy re-run again before the
   registration review.

3. **Which device, and which number format, is the registered fit computed
   on?** The ruling (page 3, RT-232) says the registration names them and
   that the figure on the named device is the registered one. It does not
   say which. *This draft writes in the laptop's processor, the model's
   states in 32-bit, the read fitted by scikit-learn in 64-bit, the library
   versions recorded (section 7.2, item 1).* **Suggestion: confirm that.**
   Confidence high on the processor, because every toy figure in this version
   was computed on it and it is the one device every later reader will also
   have; moderate on whether the registration should also pin the library
   versions exactly or only record them. Strongest alternative: the graphics
   chip, which is faster on a 30-million-parameter model and is what the
   earlier committed fits used.

4. **The numbers of episodes at the registered size.** The brief for this
   version asks for every frozen number to be stated. Every bar is stated,
   but each is a share or a rule, and no ruling sets how many development,
   held-out and fresh episodes the registered measurement uses, how many are
   on the relaxed set, how many held-out episodes the gates are scored on, or
   how many shuffles the permutation null uses. *The registration must print
   them; this version lists them as not set (section 9, the last row).*
   **Suggestion: the toy's counts, unchanged: 600 development episodes with
   the last 180 held out, 800 fresh matched pairs, 800 on the relaxed set,
   3,000 for the gates, 200 shuffles.** Confidence moderate. They are the
   only counts the procedure has been rehearsed at, the floor is then 144 of
   180 as on the toy, and section 11 already argues the registered model's
   states fit on the laptop at that scale. Strongest alternative: more
   held-out episodes, so that the floor is not decided by a handful: at 180,
   one episode is 0.0056, and the toy has already shown fits moving by one
   episode between devices.

5. **Control 2's comparison: one random piece or twenty?** The ruling keeps
   control 2 as a description: how often the own-directed action moves under
   the named agent's piece, beside how often it moves under "a random piece".
   The code draws one, with its own seed; control 3 draws twenty. *Written
   as the code runs, one draw (section 7.3, item 2).* **Suggestion: twenty,
   reported as control 3 reports them.** Confidence moderate. With no pass
   line a single draw is a weak thing to print beside a figure. It is a small
   code change, and it would mean the code path that ran once on 2026-10-03
   is not quite the one registered. Strongest alternative: leave it at one,
   since the control is expected to return no verdict anyway.

6. **What is an arm's outcome when its seeds disagree?** The floors and the
   controls that hold apply per arm and seed, so an arm can read on two seeds
   and return no verdict on the third. The ruling on what a no verdict maps
   to (page 11) speaks of "no verdict on arm C", "on arm M" and "on arm F"
   and does not say how many seeds make that so. The separation bar is
   written "per seed" in the same way, without saying what follows if it is
   cleared on two seeds of three. On the toy every arm behaves alike on all
   three seeds, so this has never bitten. *Not written into the body beyond
   section 3 saying the case is open.* **Suggestion: the rule the design
   already uses for its gates, at least two seeds of three, with the third
   reported.** Confidence low to moderate; this is a new pre-stated rule and
   deserves his attention more than the others. Strongest alternative: all
   three seeds, which is stricter and makes the fifth outcome and the
   two-arm fallback more likely.

7. **The ordinary competing solver under the piece rule.** The protocol's
   rehearsal asks that a system with none of the structure the measure
   claims to detect be put through the same measurement. The ownership-blind
   solver and the name-only solver were scored on both conditions before the
   piece rule existed, and the controls re-run did not load them. *This
   version says so in three places and quotes no figure for them as if it
   were under the new rule (sections 7.3, 8.1 and 10).* **Suggestion: run
   the ownership-blind solver's three committed toy models through the
   nomination and reading as now registered, on the laptop at $0, method
   committed before output, before the registration review opens.**
   Confidence moderate to high. The expected result is a no verdict (a
   solver with no acting channel should have no read of its own marker that
   reaches four fifths), it is an afternoon, and without it the registration
   review's first question on "satisfied by the wrong thing" has an argument
   behind it and not a number. Strongest alternative: state in the
   registration that it was not measured under the rule, and let the
   reviewer decide whether that is a finding.

**Two things that are not questions, said so they are not found later.**
John's ruling on decision 23 (which read is the registered one) still has no
ruling file of its own; it is carried from his revision instruction for
version 3. And the three rulings of 2026-10-03 were each given as agreement
to a packet or a suggestion, with the wording the recording session's; the
records say so themselves, and this version quotes the records.

---

## 20. Change log from version 3, keyed to the ruling or finding behind each change

"The morning rulings" are
`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (main line at
`56a5a86`). "The re-run rulings" are
`docs/rulings/2026-10-03-controls-rerun-rulings.md` (`fe5df65`). "The evening
ruling" is `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`
(`f32ba0c`). "The review" is the first independent review of version 3,
findings RT-230 to RT-236 (`4cb7f8e`). "The check of the re-run" is at
`e184a6e`, and "the check of the packets" at `f32ba0c`.

- **RT-230 (serious: the floor certified the read, not the piece
  transplanted). The morning rulings, page 1.** The fit floor moved to the
  piece: only sizes whose own held-out accuracy reaches four fifths may be
  chosen, the piece's count printed beside the whole read's (sections 1, 6.4
  item 2, 7.2 items 1, 3 and 5, 7.4, 7.5, 9). Sections 3 and 5.2 reworded to
  what was measured: the read holds the label, the largest piece transplanted
  holds it, no size moves the action. Version 3's sentence that arm C's
  transplanted subspace "holds the label and clears the fit floor on every
  seed" struck. **Arm C's toy readings changed from 1.0051, 1.0025 and
  1.0000 to 1.0051, 0.9926 and 0.9974, with the sites and sizes the re-run
  chose** (sections 3, 5.2, 9, 10). The forecast on page 1 of the ruling
  packet (8, 8 and 4 directions; 0.9975 on seed 1) is not used: the re-run
  showed it wrong on seed 1, and the check of the packets says to quote the
  re-run (its section 7, row 6).
- **RT-233 (serious: four controls had no figure under the registered
  rules). The morning rulings, page 2.** The controls re-run is done and
  checked. Every figure for controls 1, 3, 4, 6 and 7, the true-slot
  reference, the rider and the stricter row is quoted from it (sections 5,
  7.2, 7.3, 10, W11). Version 3's sentences saying those figures were owed
  are gone.
- **RT-231 (minor: arm M's true-slot check, run by the review).** Arm M's
  blind reading is within 0.0049, 0.0099 and 0.0529 of its true-slot reading
  at the registered site sets (sections 5.3, 9, 10 R-3). **0.0099, not the
  0.0100 the re-run's prose printed** (the check of the re-run, section 7,
  item 3).
- **RT-232 (minor: fits move by one episode between devices). The morning
  rulings, page 3.** Fits stated as counts of held-out episodes; the
  registration names the device and number format, and the figure on that
  device is the registered one (sections 1, 5.4, 7.2 item 1, 7.5, 9). Taken
  from the review's own wording, which also names the number format, and not
  from the packet's shortening (the check of the packets, section 7, row 9).
  The device, the laptop's processor, was ruled late that evening.
- **RT-234 (minor: the whole-state floor is applied twice). Page 3.** Said in
  sections 6.4 item 1, 7.4, 7.5 and 9: on development episodes at nomination,
  again on fresh episodes at the reading, and a site set that clears the
  first and misses the second returns no verdict.
- **RT-235 (minor: the stop reads its fit at a layer the noise may pick).
  Page 3.** The report for the first full-size free-model run prints the
  read's count at every layer, the chosen piece's count and the candidates
  (sections 7.5 and 11, step 5a). Section 7.2, item 5, and section 5.2 now
  say that on an arm where nothing moves the action the choice is made among
  sampling noise.
- **RT-236 (minor: depths, and two citations by branch). Page 3.** Four
  blocks and five running states against twelve and thirteen, stated the
  same way (section 7.2, item 1). The label search and its check cited by
  their main-line commits, `a97c12b` and `ecd2b6c`, throughout.
- **Decisions 2, 3, 4, 8, 9, 10, 13, 17, 18 and 19. The morning rulings,
  pages 4 to 10, 14, 15 and 16.** Each marked ruled in section 15 and where
  it bears: sections 4.2, 5, 5.1, 5.2, 7.2 item 2, 8.2, 9, 10 R-11, 11 step
  5a, 12.2, 12.4, W8, W9. The handshake is described as ruled, option (b),
  with the caution carried (W9). **Not carried: the packet's sentence about a
  $97.04 loss, on its page for decision 13.** Version 3 left that sentence
  out on purpose, and the check of the packets found it is not what the
  ledger shows (its section 7, row 3).
- **Decision 14, what a no verdict maps to. The morning rulings, page 11; the
  evening ruling, ruling 1.** The fifth registered term, "metric validated,
  degree not read", added to the outcome table as satisfactory and stated as
  weaker than R1; the mapping for arms C and M written in; the paragraph on
  the open reporting gap replaced; the toy outcome restated as the fifth term
  (sections 1, 3, 7.4, 9, 11 steps 7 and 8, 15).
- **Decision 15, control 2's tolerance. Agreed in the morning rulings (page
  12); withdrawn by the re-run rulings, ruling 1.** Control 2 is a reported
  description with no pass line; the registration says in terms that it
  never ran at toy scale, why, and that a no verdict is expected; its one
  end-to-end run is quoted labelled NOT A RESULT (sections 7.3 item 2, 7.4,
  7.5, 9, 10, 11 S8, W7, W14).
- **Decision 16, control 4's standing. Agreed in the morning rulings (page
  13); reversed by the re-run rulings, ruling 2.** Control 4 redefined on the
  positions before both twins' first own turns, and made a control that
  holds, with the pass line that the outputs are bit-identical. Described as
  a known-answer test of the pairing and the code, which cannot fail on a
  correctly built model and whose pass says nothing about any model (the
  check of the re-run, section 5). The sentence that arms C and F "receive
  the ownership signal by other routes" withdrawn (sections 1, 6.4 item 5,
  7.3 item 4, 7.4, 7.5, 9, 10, W14). **Not carried: the re-run's sentence
  tying the six models with a large excess to their sites' position set as a
  cause**; the control uses only the site's layers (the check of the re-run,
  section 7, item 3).
- **The re-run rulings, ruling 3, and the evening ruling, ruling 2: the
  piece's accuracy at the other positions.** A reported figure, printed both
  ways, with how each is computed, and the toy's figures (sections 3, 5.2,
  5.3, 7.2 item 3, 7.4, 7.5, 9). The plain statement that the piece's four
  fifths is established at the action position only, with the figures for
  arms C and M, and a new weakness W13.
- **From the check of the re-run, section 7 (not a ruling).** The null
  transplant counted as tested at fifteen different places (sections 7.3
  item 7, 10 R-8). Two requirements on the registered code written in: the
  controls that hold withhold the reading in code (sections 6.4 item 5, 7.3,
  7.4); and the ordinary competing solver is said, in three places, not to
  have been measured under the piece rule (sections 7.3, 8.1, 10 R-5), with
  its run now owed by ruling.
- **The short pre-stated run.** Quoted for control 4 as redefined, for the
  new column, and for the one run of the part of control 2's code after the
  floor, labelled NOT A RESULT.
- **From the check of the short pre-stated run (main line at `53c8100`, pull
  request 82), section 10 (not a ruling).** Filed while this version was
  being written; the first commit of this version had marked the short run's
  figures as unchecked. All four of its notes are followed: control 4 is
  said to compare the outputs at the two action positions (section 7.3, item
  4); the new column's computation is set out in full, the figure on the
  average is said to be good to an episode or two on the toy, and the
  registered code averages in 64-bit (section 7.2, item 3); what the short
  run added for control 2 is said to be the part of its code after the floor
  (section 7.3, item 2; section 10); and the piece's four fifths is said to
  be established at the action position only (sections 3, 5.2, 5.3, W13).
  Also carried from it: the test is not empty (noise changes the outputs),
  the ten named positions are about a quarter of a span, the limit on what
  "pre-stated" can be shown to mean, and John's confirmation that section 4
  of the short run's method is what "print both figures" means.
- **John's late-evening ruling on this version's seven questions
  (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, filed with
  this version).** Each written in where it bears: the floor on the piece
  only (sections 6.4 item 2, 7.2 item 1, 9); the piece rule applied after
  the layers are chosen (section 7.2, item 3); the registered fit on the
  laptop's processor, library versions recorded and not pinned (sections 7.2
  item 1, 7.4, 9); the toy's episode counts at the full size (sections 7.4,
  8.1, 9); twenty random pieces for control 2, with the code change that
  implies (sections 7.3 item 2, 7.4, 7.5, 9); two seeds of three when an
  arm's seeds disagree (sections 3, 7.4, 9); and the competing solver's run
  under the piece rule owed before the registration review (sections 7.3,
  8.1, 10, 11). Section 19 keeps the questions as put and says they are
  ruled.
- **The header, the source table, section 16 and section 17.** Rewritten for
  this version: sources by main-line commit, the eight new ones first; the
  author's failure-mode pass run again with this session's commands on the
  controls re-run's outputs. Section 18, the printed site list, is new.
  Section 19, the questions for John, is new. Version 3's change log from
  version 2 is not repeated; it is section 18 of version 3.
- **Left alone.** Sections 2, 4.1, 4.3, 4.4, 5.5, 6.1, 6.2, 7.1, 8.2 (but for
  one clause), 12.3, 12.5 to 12.8 and 14 carry version 3's text. Sections
  4.2, 6.3, 8.1, 12.1, 12.2 and 12.4 change by a sentence or a citation each.
  Wherever version 3's text says "this version" of a change it made from
  version 2, that change is carried here unchanged.

---

## What this version does not do

It edits nothing: not version 3, not any ruling, registered text or protocol
text, and not the findings of any run. It issues no go, releases no money,
launches nothing, trains nothing and rents nothing. It does not open the
registration review, and it is not ready for it: the competing solver's run
under the piece rule is owed, and this version and the record of the
late-evening ruling are owed a check under the pairing rule of
`docs/outside-review-protocol.md`. The seven questions of section 19 were
John's, and he ruled them; this version resolved none of them itself.
