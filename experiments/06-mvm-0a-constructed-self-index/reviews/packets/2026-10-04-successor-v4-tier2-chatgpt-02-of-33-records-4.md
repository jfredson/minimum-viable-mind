*This is file 2 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 1 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 1 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
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

**Notice, 2026-10-03 (night), added by a session that did not write this
version.** The seven questions of section 19 were ruled twice that evening,
in two sessions, and the two records differed on four points. John ruled that
`docs/rulings/2026-10-03-version-4-questions-rulings.md` stands on all four
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`). The passages below that state
those points were edited to match, each marked "reconciled". They are: the
library versions are pinned (section 7.2, item 1); the registration says what
applying the piece rule after the layers are chosen can miss (section 7.2,
item 3); the sampling band is printed at the floor (sections 7.4, 7.5, 9);
and the separation is the lowest of arm C's readings minus the highest of arm
T's, not paired by seed number (sections 3, 9). **If a sentence elsewhere in
this version still states one of the four the old way, that ruling governs.**

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
| **John's late-evening ruling of 2026-10-03 on this version's seven questions** | **filed with this version, pull request 83**: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` | **Binding on this version.** The floor on the piece only; the piece rule after the layers are chosen; the laptop's processor; the toy's episode counts at full size; twenty random pieces for the other-agent control; two seeds of three when an arm's seeds disagree; the competing solver run before the registration review. Recorded by the session that wrote this version, and owed a check. **Read with the second record of the same evening, `docs/rulings/2026-10-03-version-4-questions-rulings.md`, which by John's ruling stands on the four points where the two differ (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`)** |
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

===== END OF RECORD 4, part 1 =====

