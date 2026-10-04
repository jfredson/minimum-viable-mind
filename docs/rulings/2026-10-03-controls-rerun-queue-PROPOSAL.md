# Proposal for John, 2026-10-03: three rulings after the controls re-run, one page each

*Written 2026-10-03 (Pacific) by a Claude Code session, at John's request.
**This is a proposal, not a ruling. Nothing in it is decided or registered,
and no registered text, ruling file, protocol text or proposal text is changed
by it.** Nothing was rented or spent to write it.*

*Written under the workspace plain-language rule. Findings are labelled
**MEASURED** (in an output file named beside them) or **ARGUED** (reasoning a
reader can dispute). Three documents are cited throughout and named here
once:*

- *"the re-run" is `docs/2026-10-03-controls-rerun.md`, on the main line at
  `821f154` (pull request 76), with its outputs under
  `experiments/rehearsal-successor-measure/out-controls-rerun/`;*
- *"the proposal" is `docs/successor-experiment-proposal-2026-09-26-v3.md`,
  version 3 of the successor experiment proposal;*
- *"this morning's rulings" is
  `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`.*

**Three things to know before relying on this packet.**

1. **The session that wrote it also ran the re-run**, and before that wrote
   the review, the earlier packet and the record of this morning's rulings.
2. **Neither the re-run nor this packet has been checked by a second
   session.** Page 2 rests on a diagnostic written after the re-run's output
   was seen. If the check of the re-run finds that diagnostic wrong, page 2's
   recommendation falls with it.
3. **Each page says what it would add to the work before the registration
   review**, because every one of these rulings creates something that has to
   be run once before it can be registered.

---

## The one-page index

"Agreed on all", or exceptions by page number, is enough.

| Page | Decision | Recommendation (John's to overturn) | Confidence |
|---|---|---|---|
| 1 | The other-agent control cannot be tested on any toy model | Keep it, as a reported control with no pre-stated pass line; say in the registration that it was never exercised at toy scale and that its no verdict is expected | moderate |
| 2 | The too-early-position control was defined on one twin only | Redefine it on both twins, and make it a control that holds again, as a known-answer test of the pairing | moderate to high, subject to the check |
| 3 | A piece transplanted at several positions is checked at one | Report its accuracy at the other positions; do not gate on it | moderate |

**What these rulings do not do.** They release no money and give no go. Each
amends a sentence of this morning's rulings, and the page says which.

---

## Page 1 — the other-agent control cannot be tested on any toy model

**The question in one sentence.** What does the registration say about a
control that has a pre-stated pass line and has never once been run?

**What the control is** (the proposal, section 7.3, item 2). Find, by the same
procedure, a representation of the *other*, named agent, and transplant it
from a twin that differs only in which agent is named. The model's
own-marker action should not move, or the "ownership" piece is really a
general "some agent" piece. Its pass line: the action moves in no more trials
than under a random piece, plus 0.05. This morning's rulings set the 0.05
(the proposal's decision 15).

**What the re-run found** (MEASURED: the re-run, section 5;
`out-controls-rerun/measure_F_seed0.json`, `control2`).

- By ruling it does not apply to the separable and mixed models, which hold
  the named agent outside the running state.
- It runs only on a model that learned the other-agent condition. Of the six
  remaining toy models, one did: the free model's seed 0 (994 of 3,000 against
  790).
- On that one, the read of the named agent's marker is right on at most 137
  of 180 held-out episodes, against 144 needed. So the procedure returns no
  verdict before any transplant is made. This would have happened under the
  proposal's earlier rule too.

**Why it cannot be left alone.** Item 5 of the ruling of 2026-09-21
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): "A
pre-stated quantity the rehearsal never exercised is a fatal finding on its
own." The 0.05 is such a quantity.

**The options.**

- **(a) Keep the control and its 0.05, and rule an exception to item 5.** Says
  what is true, and leaves a pass line in the registration that nobody has
  seen pass or fail.
- **(b) Keep the control, and take the pass line out.** It is reported as a
  description: how often the own-marker action moves under the named agent's
  piece, beside how often under a random piece. No pre-stated number, so
  nothing is unexercised. The registration says it never ran at toy scale and
  that a no verdict is the expected result.
- **(c) Drop it.**
- **(d) Exercise it on a made-up case.** Build something on which the control
  can be seen to pass and to fail. Honest, in the protocol's own spirit, and
  the largest piece of new work: it needs a toy model that both learns the
  other-agent condition and carries the named agent readably, and four repair
  attempts have not produced one that learns it.

**Recommendation: (b).** *Confidence: moderate.* The control already cannot
veto a reading, so the pass line decides nothing; removing it costs only a
label of "pass" or "fail" beside a figure the reader can judge. It keeps the
question on the record for the full-size free model, which is the one model
that must learn both conditions before it is read at all. **Strongest
alternative: (d)**, if John holds that a control nobody has seen work is not
worth registering in any form. **What (b) gives up:** a pre-committed standard
for "the piece is specific to the model's own identity". A reader of the
result will have to judge the two figures without one.

**One $0 addition worth making under (b)** (ARGUED): run the control's code
path once on the free model's seed 0 with the floor switched off, labelled as
a test of the code and not a result, so that the registration is not the
first time that code runs end to end.

*Amends:* this morning's rulings, the table row for decision 15 (the 0.05
tolerance is withdrawn, not set). *Changes:* proposal version 4, section 7.3
(item 2), section 7.4 and section 15.

---

## Page 2 — the too-early-position control was defined on one twin only

**The question in one sentence.** Should this control be redefined so that it
tests what it was written to test, and if so, can it go back to being able to
withhold a reading?

**What the control is** (the proposal, section 7.3, item 4). Transplant the
whole state at positions before the model can know which agent it is. Nothing
should happen. Version 1 of the proposal made a failure withhold the reading.
Version 3 made it reported only, because on an earlier run it did not come
back at "nothing" on the entangled and free models, and gave as the reason
that those models "receive the ownership signal by other routes". This
morning's rulings agreed (the proposal's decision 16).

**What the re-run found** (MEASURED: the re-run, section 6). As written, the
control came back above the no-transplant rate by 0.065 to 0.10 on six of
twelve models: the mixed model on every seed, the entangled model's seed 2,
the free model's seeds 0 and 2. Those six are exactly the ones whose
transplant site reaches back to the model's first own turn.

**What the after-the-fact diagnostic found** (MEASURED, **not pre-stated**:
`experiments/rehearsal-successor-measure/src/posthoc_control4.py`, output in
the re-run's section 6). The control takes its positions from the recipient:
everything before the recipient's first own turn. The donor twin is a
different agent, and in 0.5088 of pairs its first own turn comes earlier. At
those positions the donor already knows who it is. With the positions taken
before **both** twins' first own turns, the control returns exactly the
no-transplant rate on all twelve models.

**What that means** (ARGUED). The control was not showing ownership arriving
"by other routes". It was transplanting at positions where one twin's
identity was already known. Before both twins' first own turns, the two twins
have read the same words and neither has been told it is acting, so their
states should be identical and the transplant should change nothing at all.
That makes the redefined control a known-answer test, of the same kind as the
null transplant: it can only fail if the pairing is broken or if something in
the text gives identity away early. Both of those are things that should
withhold a reading.

**The options.**

- **(a) Redefine the positions on both twins, and make the control hold
  again.** Pass line: the share of trials landing on the donor's value equals
  the no-transplant share. This restores what version 1 intended.
- **(b) Redefine the positions, and keep it reported.** Fixes the definition
  and changes nothing else about this morning's ruling.
- **(c) Leave it as ruled this morning:** reported, positions on the
  recipient only. The registration would then carry a control that is known
  to measure something other than what its name says.

**Recommendation: (a).** *Confidence: moderate to high, subject to the check
of the re-run.* A control that can only fail when something is broken is
exactly the kind that should be able to stop a reading, and the toy shows it
passing on every model. **Strongest alternative: (b)**, on the ground that
the evidence is one diagnostic, written after the output was seen, by the
session that ran the re-run.

**What it adds before the registration review.** The redefined control is a
new pre-stated quantity, so it has to be run as such: method first, then
output. The diagnostic's figures cannot be quoted as that run. It is a few
minutes on the laptop, and the session that checks the re-run is the natural
place for it.

**One caution.** The stronger claim above, that the two twins' states are
identical before both first own turns, was not measured. What was measured is
that the transplant leaves the share unchanged. The pre-stated run should
compare the outputs themselves, as the null transplant does.

*Amends:* this morning's rulings, the table row for decision 16. *Changes:*
proposal version 4, sections 7.3 (item 4), 7.4, 7.5 and 15, and the "other
routes" sentence, which is withdrawn.

---

## Page 3 — a piece transplanted at several positions is checked at one

**The question in one sentence.** When the chosen site covers several
positions, must the transplanted piece carry the label at each of them?

**How it stands.** The registered read is fitted at the action position (the
proposal's decision 23, ruled 2026-09-26), and under this morning's page 1
the piece's accuracy is taken there too. When the chosen site is a span, the
same directions are transplanted at every position in the span.

**What is on the record** (MEASURED: the review, finding RT-230, first output
block). On the entangled model's seed 2, the one-direction piece was right on
0.306 at the action position and 0.161 to 0.194 at the other positions of its
span. On the mixed model, the 8-direction piece was right on 1.000 at the
action position and 0.839 to 0.983 elsewhere. The re-run chose a 4-direction
piece at a span on the entangled model's seed 2 and an 8-direction piece at a
four-position set on seed 1; **neither was measured at the other positions.**

**Why it is not obviously a defect** (ARGUED). The whole state at a model's
own earlier turns holds the label trivially, because its own marker word is
the input there. Directions fitted at the action position need not be the
ones that hold it at those turns. A piece that carries the label where the
model acts and less well elsewhere is still the piece the read found.

**The options.**

- **(a) Leave it:** accuracy at the action position only.
- **(b) Gate on it:** the piece must reach four fifths at every position of
  the site. A new rule nobody has run; it may return no verdict on the
  entangled model at span sites and push the rule toward single-position
  sites for a reason unrelated to degree.
- **(c) Report it:** print the piece's accuracy at the other positions beside
  its accuracy at the action position, with no pass line.

**Recommendation: (c).** *Confidence: moderate.* It puts in front of the
reader whether "the piece held the label and did nothing" is true across the
whole site or only where the model acts, which is the over-reading the review
warned of, without adding an unrehearsed gate about two weeks before the
registration deadline of 2026-10-18. **Strongest alternative: (b)**, if John wants the
floor to mean the same thing at every position.

**What it adds before the registration review.** One new column in the
reporting table, and one run that fills it for the twelve toy models. A few
minutes on the laptop, with the page 2 run.

*Amends:* this morning's rulings, page 1, by adding a reported figure; the
rule itself is unchanged. *Changes:* proposal version 4, sections 7.2 and 7.5.

---

## Appendix — where each number comes from

- Page 1: the re-run, section 5; `out-controls-rerun/measure_F_seed0.json`,
  field `control2` (the named read's counts by layer and size); the committed
  gate counts in `experiments/rehearsal-successor-measure/out-v3-rules/gate.json`.
- Page 2: the re-run, section 6, and the printed output of
  `src/posthoc_control4.py` there; `out-controls-rerun/table.md`, the control
  4 column.
- Page 3: the review
  (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`),
  finding RT-230, first output block; the re-run, section 3.
