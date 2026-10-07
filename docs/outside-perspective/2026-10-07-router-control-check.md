# Can experiment 1's router control ever return a centre? A check of the record (2026-10-07)

*Written 2026-10-07 by the Claude Code session that reviewed the brief for
outside models (`docs/outside-perspective/2026-10-07-detecting-another-mind-brief.md`).
Nothing here is a ruling and nothing was run; this is a reading of registered
text and recorded results, done at $0. Labels follow the outside-review
protocol: MEASURED means a figure is quoted from a committed record, ARGUED
means reasoning a reader can dispute. Written under the workspace plain-language
rule.*

## The question

The brief's section 4 worries that the project looked for the self as a stored
thing when the book says consciousness is something a system does. The review
of the brief suspected a sharper form of that worry sits in experiment 1's own
decision rule: that the control which reads "damage spreads to tasks not about
the self" as the signature of conversational bookkeeping cannot be told apart
from what the book predicts for a real centre. This note checks that suspicion
against the registration and the findings.

## What was opened

- `experiments/01-self-indexing-removal-test/pre-registration.md`: the two
  hypotheses, the decision rule, the controls, the loss conditions.
- `experiments/01-self-indexing-removal-test/red_team_ledger.md`: the row for
  the router finding (`RT-05`, the dialogue-state-router finding) and the
  reflexivity and length findings (`RT-09`, `RT-10`).
- `experiments/01-self-indexing-removal-test/removal-test-findings.md`: the
  registered result of 2026-07-18 and the 2026-08-04 uncertainty addendum.
- `experiments/01-self-indexing-removal-test/rt09-reflexivity-findings.md`:
  the generic-speaker control's result.
- `experiments/01-self-indexing-removal-test/theta-delta-lock-memo.md`.

Not opened: the stimulus code, the batteries themselves, `thresholds.md`, the
calibration findings. Nothing was re-run.

## What the registration says (MEASURED, quoted)

The two hypotheses:

- A centre (`H_center`): "Removing it degrades the model's integrated task
  performance ... and the degradation is specific to the self-locating
  structure, not a generic effect of damaging any well-trained component."
- A description (`H_description`): "Removing it subtracts or corrupts the
  model's first-person self-report while leaving integrated task performance
  intact."

The decision rule for a centre: the task drop is at least the task threshold,
and the drop exceeds the drop from removing a matched control structure by at
least the specificity margin. The router control, added 2026-06-23 from the
first adversarial pass: "If ablating C_self-index degrades a pure
turn/boundary-tracking task (`T_syntax`, no reasoning) as much as
`T_self_relevant`, the localized structure is a dialogue-state router rather
than a self-locating center, and no H_center claim attaches to it."

The three task batteries: tasks that need no reference to the self
(`T_si`), tasks that do (`T_sr`), and a turn-boundary tracking task with no
reasoning (`T_syntax`).

## What the run returned (MEASURED, quoted)

Primary condition: drops of 0.219 on the self-irrelevant tasks, 0.100 on the
self-relevant tasks, 0.133 on turn tracking. Self-report drop +0.059, no
report was removed. The centre signature fired (task drop plus differential,
+0.156 against the expert control) and was voided by the router control,
because 0.133 is at least 0.100.

The uncertainty addendum: the router gap, turn-tracking drop minus
self-relevant drop, is +0.033 with a 95% interval of [−0.133, +0.200]:
"'dropped as much as self-relevant' is statistically indistinguishable, as
read." The centre differential was +0.156 with an interval of [0.000,
+0.312]. Six of the seven self-irrelevant items that flipped were multi-step
reasoning items.

The findings file's own reading: "Removing it degrades integration
*generically*, most of all on self-irrelevant tasks, which is the router
account's own prediction (turn structure is woven into everything)." And:
"The self-binding the floor claim targets is either implemented elsewhere
(diffusely, or in structure our localization does not carve) or is not
present as a removable object at all."

## The check (ARGUED)

**What the book predicts for a centre.** Chapter 5 of The Calibration Problem:
"A center is what cannot be deleted without dissolving the integration it
centers." The floor is binding that marks, within the act, whom it is
happening to. If that is right, removing a real centre does not damage a
subset of tasks. It damages the act. On the three batteries that means drops
on all three, including turn tracking, because tracking who said what across
a conversation is itself binding across time.

**What the router control reads.** A turn-tracking drop at least as large as
the self-relevant drop means router. So any pattern in which a centre's
removal damages everything, which is the book's pattern, is read as a router.
The only pattern the rule can read as a centre is one where self-relevant
tasks drop more than turn tracking: a self that some tasks use more than
others. That is the self as a stored thing some computations consult, the
reading section 4 of the brief calls the noun view.

**So the two accounts coincide on the battery.** "Turn structure is woven
into everything" and "the centre is woven into everything" make the same
prediction about which tasks drop. The control picks the router reading by
parsimony, which is a legitimate choice and the one the registration made in
advance. But it is not a discrimination. The registered result should be
read as "the located structure behaves as a router would, and also as a
centre of the book's kind would; the cheaper account is taken." The findings
file's second sentence quoted above already leaves this door open; the
brief's section 3A does not.

**Three things that cut the other way, so the suspicion is not a verdict.**

1. The located structure came from a model-turn-versus-user-turn contrast, so
   it is by construction the kind of thing a turn tracker would be. Finding
   turn-tracking behaviour in a structure found by a turn contrast is the
   expected result under both accounts, which is the problem, but it also
   means the prior for "router" was high before any ablation ran.
2. The reflexivity control (`RT-09`) did not fire, on the pilot model: a
   generic speaker-slot direction learned from third-party dialogue was
   nearly orthogonal to the located structure (cosine 0.148) and causally
   inert on it (cross-patch ratio −0.005). The structure removed was specific
   to the model's own turn, not generic bookkeeping of who is speaking. The
   length control (`RT-10`) also did not fire. The brief omits both, and they
   are points in favour of the structure being about the self, not merely
   about turns. Caveat: these ran on the pilot sandbox model; whether they
   were re-verified on the registered 8-billion-parameter model before lock
   was not checked here.
3. The router gap itself is inside noise. The verdict rests on a point
   estimate of +0.033 whose interval spans zero on both sides. The
   registration says to apply the rule as written, and it was, but a
   reader weighing the result should know the control fired by a margin the
   data cannot distinguish from nothing.

## What this changes

- **For the brief.** Section 3A should carry one sentence: the control that
  voided the centre reading cannot separate a router from a centre woven into
  the whole act; it chose the cheaper reading, in advance, as registered. And
  it should add that the structure was shown not to be generic
  speaker-tracking, so "dialogue routing" is routing of the model's own turn.
- **For any redesign.** A removal test that respects the verb view needs a
  decision rule in which damage spreading to every task is a possible
  signature of a centre, with the router account ruled out by a different
  kind of evidence than which tasks drop. Candidates: whether the removed
  structure is specific to the system's own turn (the reflexivity control
  already does this); whether a sham perturbation matched in surface form
  does the same damage; whether the damage follows the system's own record
  of its actions rather than the turn markers. None of this is a proposal;
  it is the shape a proposal would need.
- **For the record.** This note claims nothing about the result's figures,
  which stand. It claims the registered reading is a parsimony choice between
  two accounts the battery cannot separate, and that the registration text
  did not say so.

## What would show this note is wrong

A pattern on the three batteries that the registered rule would have called a
centre and that the book's account also predicts. The restricted outcome
(self-relevant drops, self-irrelevant survives) is one the rule allows, but it
is the pattern of a self some tasks use, not of a centre that holds the act
together. If someone can show the book predicts the restricted pattern for a
real centre, the two accounts come apart and this note's claim fails.
