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
