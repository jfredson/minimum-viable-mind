*This is file 17 of 33 of one review packet, pasted into a single conversation. It contains record 6 (John's rulings of 2026-10-03 on the review of version 3 (binding on version 4)); record 7 (John's three rulings of 2026-10-03 after the controls re-run); record 8 (John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 6 of 25 - John's rulings of 2026-10-03 on the review of version 3 (binding on version 4) - `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (complete file, 9,929 characters) =====
# Ruling 2026-10-03: the review of successor proposal version 3 (RT-230 to RT-236) and the proposal's open decisions

*Recorded 2026-10-03 (Pacific) in a Claude Code session. **Mixed authorship:**
each ruling was put to John as one page of
`docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md` (pull request
75), with a recommendation, its confidence and the strongest alternative, and
he ruled on the sixteen pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. "The proposal" is
`docs/successor-experiment-proposal-2026-09-26-v3.md` (main line at
`6d4ec3a`). "The review" is its first independent review,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
(main line at `4cb7f8e`), whose findings are numbered RT-230 to RT-236 in the
red team ledger's sequence. Every number below is the review's or the
proposal's, with the place named.*

**Three things about how this ruling was reached, stated so they are not
found later.**

1. The session that recorded it also wrote the review and the packet. The
   pages on the review's findings (1 to 3) therefore recommended rulings on
   that session's own findings.
2. The packet had not been checked by a second session when John ruled, which
   the pairing rule of `docs/outside-review-protocol.md` asks for. That check
   is still owed, and so is the check of this file.
3. John ruled from the packet's one-page index and the three pages the
   session drew his attention to (1, 11 and 15). The record does not show
   whether he read the other pages in full.

Nothing here edits registered text, protocol text or the proposal. Version 4
of the proposal carries the changes. Two earlier documents gain a dated note
beside the sentence this ruling touches, and are otherwise left as written.

---

## What was ruled

### Page 1 — the fit floor applies to the piece that is transplanted (finding RT-230, serious)

*The review, RT-230 (MEASURED): the four-fifths floor was scored on the whole
straight-line read, while the transplant moves only the read's leading 1, 2,
4 or 8 directions. On arm C, the entangled model, the piece the rule chose
holds the label at 1.000, 0.544 and 0.306 on seeds 0, 1 and 2; the
8-direction piece holds it at 1.000, 0.900 and 0.989; the arm reads between
0.9897 and 1.0051 at every size.*

1. **Option (b) is ruled: only sizes whose own held-out accuracy clears four
   fifths may be chosen, and that accuracy is printed in the reporting
   table**, beside the whole read's. The accuracy of a piece is the held-out
   accuracy of a read given only the state's coordinates inside that piece, on
   the same development episodes and split as the whole read. An arm and seed
   with no size that clears returns "no verdict, read failed its floor".
2. **Sections 3 and 5.2 of the proposal are reworded** to say what was
   measured: the read holds the label; the largest piece transplanted holds
   it; no size moves the action.
3. **The readings the packet gave under this rule (1.0051, 0.9975 and 0.9974
   on arm C, at 8, 8 and 4 directions) are not committed results.** They are
   the session's reading of the review's outputs. The re-run of page 2
   produces them, and version 4 quotes the re-run.

The alternative that was put and not taken: fixing the size at 8 directions
with the smaller sizes as extra rows.

### Page 2 — the re-run comes before the registration review (finding RT-233, serious)

**The re-run of rehearsal items R-1 to R-6 under the registered rules,
including page 1's rule, is a precondition of the registration review (Gate
A) on version 4.** It covers controls 1, 2, 4 and 6 on arms C, F and M at the
site sets the rule nominates, and control 7 (the null transplant) at every
nominated site set. Its method is committed before its output, and a session
that did not run it checks it. Laptop only, $0. The arm M true-slot check is
already done (the review, RT-231: 0.0049, 0.0099 and 0.0529 against 0.10) and
version 4 cites the review for it, re-confirmed under page 1's rule by the
re-run.

### Page 3 — the four minor findings, accepted as the review states each fix

- **RT-232:** the read's accuracy is stated as a count of held-out episodes,
  and the registration names the device the registered figure is computed on.
- **RT-234:** the text says the whole-state floor is applied on development
  episodes at nomination and again on fresh episodes at the reading, and that
  a site set which clears the first and misses the second returns no verdict.
- **RT-235:** the report for the first full-size free-model run prints the
  read's accuracy at every layer, the chosen piece's own accuracy, and the
  candidates the nomination chose among.
- **RT-236:** depths are stated the same way in both places (the toy has four
  blocks and five running states; the registered model twelve and thirteen),
  and the label search and its check are cited by their main-line commits
  (`a97c12b`, `ecd2b6c`). A dated note goes beside the phrase "a five-layer
  model" in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`.

### Pages 4 to 10, 12 to 14 and 16 — the proposal's decisions, agreed as the proposal recommends

| Proposal decision | Ruled |
|---|---|
| 2 | Arm T's ownership path is forced by its architecture, not encouraged by a penalty |
| 3 | Arm C entangles by architecture; no penalty against transplantable ownership directions |
| 4 | The two transplants are a subspace and its containing space at identical sites |
| 8 | A new experiment directory with its own registration, `experiments/08-…`; the compute ledger stays in experiment 06's folder as the programme's one record of money |
| 9 | The asymmetry between the own-directed and named-other conditions is recorded as a known limitation, not engineered away |
| 10 | The ownership-lesion check is a precondition for reading arm F and is never reported as evidence of a centre |
| 13 | The registration names a launcher that waits for the receipt, and "the trainer does not delete its own machine" is part of the registered recipe |
| 15 | Control 2's tolerance on arms C and F is 0.05 over the random subspace |
| 16 | Control 4 is reported and cannot veto a reading |
| 17 | Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for |
| 19 | The position sets are the rehearsal's four, by name |

*Dated note, 2026-10-03 (Pacific), later the same day, beside the table
above, which is left as written. After the controls re-run John ruled again
on two of its rows (`docs/rulings/2026-10-03-controls-rerun-rulings.md`):
**decision 15's 0.05 tolerance is withdrawn**, control 2 being kept as a
reported description with no pre-stated pass line; and **decision 16 is
reversed**, control 4 being redefined on both twins and made a control that
holds. Page 1 of this file also gains a reported figure, the piece's accuracy
at the other positions of its site, with the rule itself unchanged.*

### Page 11 — what a no verdict maps to (decision 14)

1. **No verdict on arm C** fires the two-arm fallback already accepted on
   2026-09-20.
2. **No verdict on arm M** drops arm M, which is then carried as an extension
   on the weekend roadmap.
3. **No verdict on arm F after arms T and C have separated is a fifth
   registered term: "metric validated, degree not read"**, reported with its
   reason after a colon.
4. **This amends the outcome list ruled on 2026-09-20** (section 2 of
   `docs/december-result-roadmap-2026-09-20.md`), which gains a dated note.
5. **The fifth outcome is satisfactory, and is stated as weaker than R1.**
   The packet put this as a suggestion and said it was John's call; "Agreed on
   all" is recorded as agreeing to it. Reason recorded: Stage 2's deliverable
   is the measure and not a verdict, and a validated measure with no reading
   delivers it.
6. The stop after the first full-size free-model run is unchanged: a miss of
   the floor there still goes to John before the second release.

### Page 15 — the handshake's machine half (decision 18)

**Option (b):** the registration says what is true today, that on the normal
path the laptop deletes the machine and the machine's own watcher is a
backstop for a laptop that never answers. Option (a), making the laptop wait
for the machine's acknowledgement, is the repair if a later run shows the
laptop failing to answer. **This takes option (a) off the Weekend 2 launcher
items** listed in `docs/weekend-1-handoff-2026-09-26.md`. The caution the
packet put with it is carried: twelve full-size runs rest on a backstop that
has not fired against the real vendor.

---

## What this changes, and where

- **Proposal version 4:** sections 3 (the outcome table gains the fifth term;
  the admission reworded), 5.2, 6.4, 7.2, 7.3, 7.4, 7.5 (the new column), 9,
  10, 11, 12.4, 13 (weakness W9) and 15 (every decision above marked ruled).
- **`docs/december-result-roadmap-2026-09-20.md`, section 2:** a dated note
  naming the fifth term.
- **`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`:** a dated note
  on the depth of the toy model.
- **The weekend roadmap and TimeAssembler:** the controls re-run as a Weekend
  2 goal; the handshake repair removed from the launcher items.
- **The red team ledger:** rows for RT-230 to RT-236 are owed. RT-212 to
  RT-229 have none either; both sets wait on the reconciliation that item 21
  of the 2026-09-21 ruling assigns to a later session.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 6 =====

===== RECORD 7 of 25 - John's three rulings of 2026-10-03 after the controls re-run - `docs/rulings/2026-10-03-controls-rerun-rulings.md` (complete file, 5,989 characters) =====
# Ruling 2026-10-03: three decisions after the controls re-run

*Recorded 2026-10-03 (Pacific) in a Claude Code session. **Mixed authorship:**
each ruling was put to John as one page of
`docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md` (pull request 77),
with a recommendation, its confidence and the strongest alternative, and he
ruled on the three pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. "The re-run" is
`docs/2026-10-03-controls-rerun.md` (main line at `821f154`). "The proposal"
is `docs/successor-experiment-proposal-2026-09-26-v3.md`. "This morning's
rulings" is `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, which
this file amends in three places and which gains a dated note at each.*

**Cautions recorded with the ruling.** The session that recorded it also ran
the re-run and wrote the packet, the review and this morning's record. Neither
the re-run nor the packet had been checked by a second session when John
ruled. **Ruling 2 rests on a diagnostic written after the re-run's output was
seen; if the check of the re-run finds that diagnostic wrong, ruling 2 returns
to John.**

---

## What was ruled

### 1. Control 2, the other-agent control: kept, reported, with no pre-stated pass line

*The re-run, section 5 (MEASURED): control 2 has no figure on any toy model.
The one model that learned the other-agent condition, arm F seed 0, has a
read of the named agent's marker that is right on at most 137 of 180 held-out
episodes against 144 needed.*

1. **Control 2 stays in the design as a reported description:** how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under a random piece of the same size at the same sites.
2. **Its pass line is withdrawn.** The 0.05 tolerance set this morning (the
   proposal's decision 15) is not registered. With no pre-stated number,
   nothing about the control is unexercised in the sense of item 5 of the
   2026-09-21 ruling.
3. **The registration says in terms** that the control never ran at toy scale,
   why, and that a no verdict is the expected result.
4. **Its code path is run once on arm F seed 0 with the floor switched off**,
   at $0, labelled as a test of the code and not a result, so the registration
   is not the first time that code runs end to end.

The alternative that was put and not taken: exercising the control on a
made-up case built for the purpose.

### 2. Control 4, the too-early-position control: redefined on both twins, and it holds again

*The re-run, section 6 (MEASURED; the diagnostic was not pre-stated): as
written the control is above the no-transplant rate by 0.065 to 0.10 on six
of twelve models; in 0.5088 of pairs the donor twin's first own turn precedes
the recipient's; with positions taken before both twins' first own turns it
returns exactly the no-transplant rate on all twelve.*

1. **The control's positions are those before both twins' first own turns.**
2. **It is a control that holds:** a failure withholds the reading for that
   arm and seed. Its pass line is that the transplant changes nothing; the
   pre-stated run compares the model's outputs themselves, as the null
   transplant does, and reports the donor-value share beside the
   no-transplant share.
3. **The proposal's sentence that arms C and F "receive the ownership signal
   by other routes" at those positions is withdrawn.**
4. **This reverses this morning's ruling on the proposal's decision 16**, which
   made the control reported only, on the account now withdrawn.
5. **The redefined control is run as a pre-stated quantity before the
   registration review**, method first and then output, by a session that did
   not write the diagnostic. The diagnostic's figures are not quoted as that
   run.

The alternative that was put and not taken: redefining the positions and
keeping the control reported only.

### 3. A piece transplanted at several positions: its accuracy at the other positions is reported, not gated

*The review, finding RT-230 (MEASURED): on arm C seed 2 a one-direction piece
was right on 0.306 at the action position and 0.161 to 0.194 at the other
positions of its span; on arm M the 8-direction piece was right on 1.000 and
0.839 to 0.983. The pieces the re-run chose on arm C seeds 1 and 2 were not
measured at the other positions.*

1. **The reporting table gains a column:** the chosen piece's accuracy at the
   other positions of its site, beside its accuracy at the action position.
2. **It has no pass line.** The rule of this morning's page 1 is unchanged:
   the piece must reach four fifths at the action position.
3. **The column is filled for the twelve toy models before the registration
   review**, in the same run as ruling 2's.

The alternative that was put and not taken: requiring four fifths at every
position of the site.

---

## What this changes, and where

- **Proposal version 4:** section 7.2 (the piece's accuracy, where it is
  taken and what is reported), section 7.3 (items 2 and 4), section 7.4 (the
  frozen list: control 2 without a pass line; control 4 redefined, among the
  controls that hold), section 7.5 (the new column) and section 15 (decisions
  15 and 16).
- **`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`:** a dated note
  beside the table that carries decisions 15 and 16.
- **Before the registration review, one more short run**, method committed
  before output, by a session that did not write the diagnostic: control 4 as
  redefined, the new column, and control 2's code path with the floor
  switched off. Laptop only, $0. The check of the re-run is the natural place
  for it.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 7 =====

===== RECORD 8 of 25 - John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways - `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (complete file, 4,960 characters) =====
# Ruling 2026-10-03 (evening): the fifth outcome is satisfactory, and the new reported figure is printed both ways

*Recorded 2026-10-03 (Pacific), evening, in the Claude Code checking session
that raised both questions. **Mixed authorship:** each question was put to
John at the end of that session with a suggestion, and he ruled in the words
**"Yes, satisfactory and weaker than R1; print both figures"**. The choices
are his; none of the wording below is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule.*

**Cautions recorded with the ruling.** The session that recorded it also wrote
the two documents the questions come from: the check of the ruling packets
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`,
section 5) and the findings of the short pre-stated run
(`docs/2026-10-03-short-prestated-run.md`, section 4). Neither had been
checked by a second session, or merged, when John ruled. This file is owed
the same check.

---

## What was ruled

### 1. The fifth registered outcome is satisfactory, and is stated as weaker than R1

*Background: page 11 of the first ruling packet of 2026-10-03 asked whether
the fifth outcome, "metric validated, degree not read" (the built models
separate and the freely trained model returns no verdict), counts as
satisfactory. It gave a suggestion and said it was John's call. John's
"Agreed on all" that morning was recorded as settling it
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11, item 5).
The check found that recording honest but thin, and recommended he confirm or
overturn it in a sentence.*

1. **The fifth outcome is satisfactory.**
2. **It is stated as weaker than R1** ("metric validated, degree read").
3. This confirms item 5 of page 11 of that morning's rulings **on its merits**,
   in John's own words, and it no longer rests on the general agreement.
4. The dated note of 2026-10-03 under the outcome table in
   `docs/december-result-roadmap-2026-09-20.md` therefore stands as written,
   and gains a second dated note pointing here.

### 2. The new reported figure is printed both ways

*Background: ruling 3 of `docs/rulings/2026-10-03-controls-rerun-rulings.md`
added a reported column, the chosen piece's accuracy at the other positions
of its site, and did not say how it is computed. The short pre-stated run
computed it two ways, as that session's own reading: one figure per position,
and one figure on the state averaged over the other positions of the site.
The two disagree about the mixed model: on the average its piece clears four
fifths on every seed (163, 174 and 175 right of 180); position by position it
misses at three to six of ten positions.*

1. **The registered reporting table prints both:** the piece's accuracy at
   each other position of its site, and its accuracy on the average over
   those positions, beside its accuracy at the action position.
2. **Neither has a pass line.** The rule is unchanged: the piece must reach
   four fifths at the action position.
3. How each is computed is as the short run's method states it
   (`docs/2026-10-03-short-prestated-run-method.md`, section 4): a fresh read
   fitted at that position on the piece's coordinates, on the same episodes
   and split; for a site that runs from the model's first own turn to the
   action, the positions reported one by one are the five tokens of that
   first own turn and the five before the action, and the positions between
   them are covered by the average only.

*Dated note, 2026-10-03 (Pacific), late evening, beside item 3, which is left
as written. The check of this record
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`,
finding 19) found that "print both figures" accepted the computation in item
3 by implication only, and asked John whether section 4 of the short run's
method is what he meant. He answered in the words **"Yes, section 4 of the
method is what I meant"**. Mixed authorship: the question was the checking
session's, the choice is his. Item 3 therefore rests on his own words. The
same check found that the figure taken on the average moves by one episode in
180 depending on the order the average is added up in (its finding 11); that
is a note for version 4 of the proposal and is not part of this ruling.*

---

## What this changes, and where

- **Proposal version 4:** section 3 (the fifth term marked satisfactory and
  weaker than R1, by this ruling); sections 7.2 and 7.5 (the new column, both
  ways, with how each is computed).
- **`docs/december-result-roadmap-2026-09-20.md`:** a dated note under the
  existing one.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text, protocol text or any
earlier ruling file.
===== END OF RECORD 8 =====

