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
