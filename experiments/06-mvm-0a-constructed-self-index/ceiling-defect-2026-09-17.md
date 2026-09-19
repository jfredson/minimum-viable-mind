# REGISTERED DEFECT — the control battery's ceiling was never verified

*2026-09-17. **Registered on John's instruction, before any further
analysis**, and independent of how the control-battery decision goes on
4 October. Local, $0. Nothing in the registered text is altered; §4 of the
amendment carries a dated notice pointing here.*

John's instruction, quoted: *"Register the ceiling defect now, before any
further analysis. Include the 0.5 vs 0.3227 documentation mismatch and the
fact that the solver ignores the supplied name."*

## The defect in one sentence

The registered text says both battery ceilings were **verified by the
attack sweep**. Only the primary battery's was. The control battery's
ceiling has never been attacked, and the single solver that produced it
ignores the one piece of information the control question supplies.

## What the registration claims

Amendment A3, §4 of the registration revisions, "The ceilings are measured,
not asserted":

> **Registered:** **0.2921** for the primary battery and **0.3227** for the
> control, measured on the registered grammar and **verified by the attack
> sweep, whose best ownership-blind attack reached 0.3036 on 12,000
> episodes — one standard error from the analytic value.**

The 0.3036 figure is an attack on the **primary** battery, compared against
the primary's 0.2921. It says nothing about the control. The sentence
attaches one verification to two numbers.

## Evidence, each checkable

**1. The attack sweep contains no control-battery code at all.** Searching
`src/shortcut_sweep.py` for the control battery's name returns **zero**
occurrences. The module attacks the primary battery only. So the clause
"verified by the attack sweep" is false as applied to the control, and the
0.3227 rests entirely on one reference solver in `curriculum_a3.py`.

**2. That solver ignores the name the question supplies.** The control
question names the agent it asks about, in the form *"where did
&lt;marker&gt; assign &lt;item&gt; to next?"*. The reference solver in
`measured_ceilings` never reads that marker. It forms all four agents'
successors on the queried item, strikes any already visible as a revision,
and guesses uniformly among the rest. Its score is therefore the score of
a solver that **cannot read names**, averaging 0.3227 over candidate sets
of size four, three and two.

**3. So 0.3227 is not a ceiling on this battery.** Every turn renders the
speaker's marker in plain text, so a solver that can do ordinary
name-keyed lookup retrieves the named agent's value and applies the
revision rule to it. Such a solver answers correctly every time. The
control battery's real ownership-blind ceiling is therefore **near 1.0 and
currently unmeasured**, not 0.3227.

That is coherent with the battery's purpose rather than a contradiction of
it. The control was designed to carry the same binding demand **without
self-reference**, so knowing which agent you are is irrelevant to
answering it. A solver blind to ownership should do well on it. What went
wrong is that the number recorded as its ceiling came from a solver blind
to something else entirely.

**4. The documentation mismatch, which predates the first dollar.** The
curriculum module's own description of the control battery states a
different figure:

> *"Two of the item's four values are struck by the two revisions a solver
> can invert, so its lookup ceiling is **0.5** — higher than T_act's, which
> **red-team pass 3 should weigh**, since the H_generic-binding bin turns
> on the difference between the two batteries' drops."*

So the registered number is 0.3227 and the module says 0.5. The comment
also names the exact risk and assigns it to a specific review. **Red-team
pass 3 ran and did not weigh it.** Neither figure has ever been checked
against an adversary.

## What follows, and what does not

**This does not change any result.** The control battery scored 0.2877,
0.3057 and 0.3195 on the three checkpoints. Against a floor requirement of
ceiling plus 0.10, it fails at 0.3227 and fails by more at 0.5 and fails
by far more at a true ceiling near 1.0. **Every reading makes the control
less learned, not more.** No verdict moves.

**It does change what the number means.** The metric divides the drop by
the distance from baseline to ceiling. For the control that denominator
was never a meaningful quantity, so the registered differential clause
rested on a yardstick nobody had checked. That is worth knowing whether or
not the clause was ever computable.

**It is a defect in a registered instrument, not in a result.** Recording
it is not a correction to a finding. It is a correction to the
registration's own claim about how one of its numbers was established.

## Consequences John has already set

**If A4 opens, measuring the control's ceiling properly is a precondition
of the amendment** (John, 2026-09-17). An amendment built on an unverified
denominator would inherit this defect.

**If A3 closes**, this belongs in the write-up as a limitation of a
comparison that was never actually available, alongside the fact that the
comparison could not be computed anyway.

**No ceiling is measured in this note.** Measuring it is the precondition
above, and John's instruction was to register the defect before further
analysis. Nothing here authorises spend, and nothing here changes
registered text.

## How this was found

Not by review of the registration, which had passed three red-team passes
with the mismatch sitting in the module's own docstring the whole time. It
surfaced from asking a narrower question, why the control battery failed
to learn, and reading the code that defines it. The original comment
predicted the exact failure mode and named the review that should have
caught it. The lesson worth keeping is that a warning written into the
code is not a warning anyone has read.
