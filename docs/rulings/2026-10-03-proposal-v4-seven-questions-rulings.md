# Ruling 2026-10-03 (late evening): the seven questions of successor proposal version 4

*Recorded 2026-10-03 (Pacific), late evening, in the Claude Code session that
drafted version 4 of the proposal and raised the seven questions. **Mixed
authorship:** each question was put to John in that session with a
suggestion, how confident it was and the strongest alternative, and he ruled
on the seven together in the words **"Agreed on all"**. The choices are his;
none of the wording below is his drafting. No compute was launched and no
money was spent under this ruling.*

*Written under the workspace plain-language rule. "Version 4" is
`docs/successor-experiment-proposal-2026-10-03-v4.md` (pull request 83). The
questions are its section 19 as first filed, at commit `a64aa82`.*

*Dated note, 2026-10-03 (Pacific), night, added by a session that did not
write this file; the text below is left as written. The same seven questions
were put to John a second time that evening, in another session, and
recorded in `docs/rulings/2026-10-03-version-4-questions-rulings.md`. The two
records differ on four points: rulings 2, 3, 4 and 6 below. **John ruled that
the other record stands on all four**
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`): the library
versions are pinned, not only recorded; the registration says what applying
the piece rule after the layers are chosen can miss; the sampling band is
printed at the floor; and the separation is the lowest of arm C's readings
minus the highest of arm T's, not compared seed by seed. On everything else
this record stands.*

**Cautions recorded with the ruling.**

1. The session that recorded it also wrote version 4, the questions and the
   suggestions. It is owed a check by a session that did not, under the
   pairing rule of `docs/outside-review-protocol.md`.
2. John ruled from a walk-through of the seven in the session's chat, which
   put them in a different order from section 19 and said which three it
   thought needed real thought. The record does not show whether he read
   section 19 itself.
3. **The session flagged one question as deserving more of his attention than
   the others, with its own confidence low to moderate: what an arm's outcome
   is when its three seeds disagree (ruling 6 below).** It is a new
   pre-stated rule and it can decide which registered outcome the experiment
   ends on. A general "Agreed on all" settles it on the record. If John wants
   to look at that one again, a sentence does it, as it did for the fifth
   outcome earlier the same day.
4. Version 4 had not been checked by a second session, or merged, when John
   ruled.

Nothing here edits registered text, protocol text, any earlier ruling file or
version 3. Version 4 carries the changes.

---

## What was ruled

Numbered as in section 19 of version 4.

### 1. The accuracy floor is on the transplanted piece only

The ruling of 2026-09-26 put the four-fifths floor on the whole straight-line
read. The ruling of 2026-10-03 (morning, page 1) put it on the piece that is
transplanted and did not say whether the earlier floor stays as a second
condition.

1. **The floor applies to the piece only.**
2. **The whole read's count is printed beside the piece's**, and is not a
   second condition.

The alternative that was put and not taken: require both.

### 2. The piece rule is applied after the layers are chosen

**Confirmed as the controls re-run ran it:** the requirement that a piece
reach four fifths decides which sizes of piece may be chosen, and never
changes which layers are used.

The alternative that was put and not taken: let the piece's accuracy also
decide between layer sets, which has not been run.

### 3. The registered fit is computed on the laptop's processor

1. **The device is the laptop's processor**, never its graphics chip. The
   figure computed there is the registered one.
2. The model's states are computed in the model's own 32-bit format, and the
   read is fitted by scikit-learn's logistic regression in 64-bit, as the
   controls re-run did.
3. **The versions of torch, scikit-learn and numpy are recorded in the output
   file. They are not pinned by the registration.**

The alternative that was put and not taken: the graphics chip.

### 4. The numbers of episodes at the full size are the toy's

**The registered measurement uses the counts the procedure was rehearsed
at:** 600 development episodes, of which the last 180 are held out for every
fit, so the floor is 144 of 180; 800 fresh matched pairs; 800 pairs on the
relaxed set; 3,000 held-out episodes for the learning gates, so the bar is
790; and 200 shuffles for the permutation null.

The alternative that was put and not taken: more held-out episodes, so that
the floor is not decided by a handful. The caution put with the suggestion is
carried: at 180, one episode is 0.0056 of the scale.

### 5. The other-agent control is compared against twenty random pieces

**The description reports the own-directed action's share moved under the
named agent's piece beside twenty random pieces of the same size at the same
sites, reported the way the random-pieces control reports them** (median,
95th percentile, and the counts below, equal and above). It still has no pass
line.

One consequence put with the suggestion and carried: this is a small change
to the control's code, so the code path that ran once on 2026-10-03, with a
single random piece, is not quite the one registered.

The alternative that was put and not taken: leave it at one draw.

### 6. When an arm's three seeds disagree, two of three decide

**The rule is the one the design already uses for its gates: at least two
seeds of three, with the third reported.**

How the session reads that, for John to overturn (the wording is the
session's):

1. An arm is read if at least two of its three seeds return a reading. It
   returns no verdict, as an arm, if two or more of its seeds return no
   verdict.
2. The separation bar is cleared if the entangled model's reading minus the
   separable model's is 0.5 or more on at least two of the three seeds,
   compared seed by seed as before.
3. Every seed is printed, whichever way it went.

The alternative that was put and not taken: all three seeds. See caution 3
above.

### 7. The ordinary competing solver is run under the piece rule before the registration review

1. **The ownership-blind solver's three committed toy models are put through
   the nomination and the reading as now registered**, on the laptop, at $0,
   with the method committed before the output.
2. **It is run before the registration review opens, by a session other than
   the one that drafted version 4**, and is owed its own check like any other
   run.
3. The expected result, stated now: no verdict, because a solver with no
   "this turn is yours" signal should have no read of its own marker that
   reaches four fifths.

The alternative that was put and not taken: state in the registration that it
was not measured under the rule, and leave it to the reviewer.

---

## What this changes, and where

- **Proposal version 4:** sections 3 (the seed rule), 6.4 and 7.2 (the floor
  on the piece only; the order the piece rule is applied in; the device), 7.3
  (the other-agent control's twenty draws; the solver run), 7.4, 8.1, 9 (the
  episode counts and the device as set numbers), 10, 11 and 19 (each question
  marked ruled).
- **One more short run before the registration review:** the competing solver
  under the piece rule, method first, by another session. Laptop only, $0.
- **Code owed with the registered measurement:** the other-agent control's
  twenty draws.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit registered text, protocol text, version 3 or any
earlier ruling file.
