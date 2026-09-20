## What this changes downstream

The companion positive control, which John ruled yes on, is now **the only
remaining route to any sensitivity reading** on the localization stack.
Before this probe it was the better of two routes. It is now the only one.

The control-battery proposal due 2026-10-04 should carry this: whatever
else Amendment A4 decides, a register that saturates to a constant after
three turns is a design defect, and any future architecture claiming to
carry a self-index needs a check that the carrier still varies at the
point where it is read.


===== FILE: experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md =====

# The control battery's ceiling is 1.0, and the clause was never computable

*2026-09-17. Method committed before running at
`ceiling-measurement-method.md` (`2fba2ea`). No checkpoint loaded, no
inference, no spend. 4,000 episodes.*

## Verdict: A — STRUCTURALLY UNSATISFIABLE

**The registered differential clause could never have been computed. Not
by these models, not by any model, at any training budget, on any
architecture. It has been dead since registration.**

## The harness proved itself first

Both known-answer checks reproduced their registered values **exactly**,
to four decimal places, before any new number was reported:

| check | measured | registered |
|---|---|---|
| control, name-blind reference | 0.3227 | 0.3227 |
| primary battery reference | 0.2921 | 0.2921 |

So the harness reproduces the registration's own arithmetic. What follows
is not a different calculation quietly substituted.

## The measurement

| solver | score |
|---|---|
| name-keyed lookup | **1.0000** |
| registered name-blind reference | 0.3227 |
| learned attack | **1.0000** |
| **best of family** | **1.0000** |

Two independent solvers reach a perfect score. The hand-written one reads
the marker in the question, finds that marker's turn for the queried item,
and applies the shared revision rule. The learned one was given only
ownership-blind features and found the same structure by itself.

Neither touches the model's own slot or the acting channel. A scan of the
code, with docstrings and comments stripped, enforces that.

## Why this kills the clause

The floor rule defines a battery's drop only when
`baseline − ceiling ≥ 0.10`.

With a ceiling of 1.0, a defined drop needs a baseline of **1.10**.
Accuracy cannot exceed 1.0. So the control battery's drop is undefined for
**every possible model**, including a hypothetical one scoring a perfect
1.0, which would give a denominator of exactly zero.

The registered signature requires the primary battery's drop **minus the
control's**. One of its two terms can never exist.

## The reason is not what we thought, and the correction matters

Until today the record said A3 could not return a positive **because the
control battery never learned**. That conclusion was right and the reason
was wrong.

The control's failure to learn is **beside the point**. A perfectly
learning control would have made no difference whatever. The clause was
unsatisfiable the day it was registered, months before any checkpoint
existed.

**This also moots the proposal I wrote this morning.** Both routes I
offered, extra supervision and a scaffolded intermediate question, aimed
at making the control learn. Neither would have fixed anything. I was
proposing to spend $27 to $39 on a repair to the wrong component, and I
would have recommended it had this measurement not been run first. John's
instruction to measure the ceiling before opening an amendment is what
caught it.

## The structural point, which generalises past A3

This is not a slip in one number. It follows from two registered choices
that are individually reasonable and jointly incoherent.

1. The control battery is **designed to be answerable without ownership**.
   That is its entire purpose: same binding demand, no self-reference.
2. The metric divides by the distance from baseline to the **best score an
   ownership-blind solver reaches**.

Any control that is fully determined by the visible episode and does not
require ownership has an ownership-blind ceiling of 1.0 by construction.
Divide by the distance to 1.0 and you divide by zero or less.

**So the ceiling-corrected metric and the concept of an ownership-free
control are incompatible by construction**, not by accident. Any future
design pairing them inherits this, which is why it is worth reporting
upstream rather than filing as an A3 defect.

Worth stating fairly: the ceiling denominator was itself a registered
revision, adopted because dividing by chance manufactured a spurious
differential of 0.035 between the two batteries. That was a real problem
and the fix was a real fix. It simply traded a small artifact for an
unsatisfiable clause, and nobody noticed because the control never got
close enough to its floor for anyone to check the arithmetic.

## What this does not change

**The primary result is untouched.** Its ceiling is 0.2921, the models
score about 0.57, so its drop is well defined and enormous, between 7.5
and 8.6 times the locked threshold. Nothing here bears on it.

**No verdict is reopened.** Every finding that said the comparison was
uncomputable remains correct. Only the explanation changes.

**The other batteries are fine.** The state battery's ceiling is 0.0676
against a baseline of 1.0. The problem is specific to a control designed
to be ownership-free.

## What it means for 4 October

The question is no longer whether to make the control learn. **It is
whether the clause can be repaired at all, and if so whether repairing it
is a metric change rather than a training change.**

That is a different decision from the one the proposal framed, and it
should be re-framed before the date. I am not proposing the repair here,
because a metric change after seeing which way it cuts is exactly the move
this programme forbids, and because John decides whether the line
continues at all.

**No spend. No registered text altered.** This measurement is itself
unregistered, and says so.


===== FILE: experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md =====

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
