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
