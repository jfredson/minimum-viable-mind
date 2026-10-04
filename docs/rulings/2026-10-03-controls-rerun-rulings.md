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
