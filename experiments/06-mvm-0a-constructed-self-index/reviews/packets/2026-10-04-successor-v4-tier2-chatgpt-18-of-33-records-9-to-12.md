*This is file 18 of 33 of one review packet, pasted into a single conversation. It contains record 9 (first record of John's ruling on version 4's seven questions); record 10 (second record of the same ruling, which stands where the two differ); record 11 (John's ruling on which of the two records stands); record 12 (John's ruling on the two questions raised by the check of version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 9 of 25 - first record of John's ruling on version 4's seven questions - `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` (complete file, 7,864 characters) =====
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
===== END OF RECORD 9 =====

===== RECORD 10 of 25 - second record of the same ruling, which stands where the two differ - `docs/rulings/2026-10-03-version-4-questions-rulings.md` (complete file, 8,617 characters) =====
# Ruling 2026-10-03 (late evening): the seven questions version 4 of the proposal asks

*Recorded 2026-10-03 (Pacific), late evening, in a Claude Code session.
**Mixed authorship:** each question was put to John as one page of
`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md` (pull request 84),
with a recommendation, its confidence and the strongest alternative, and he
ruled on the seven pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. The questions are those of
section 19 of version 4 of the successor experiment proposal,
`docs/successor-experiment-proposal-2026-10-03-v4.md`, read at `a64aa82` on
pull request 83, which was open and unmerged when John ruled.*

*Dated note, 2026-10-03 (Pacific), night; the text below is left as written.
The same seven questions were put to John in the session that drafted version
4, and recorded there as
`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`. The two
records differ on four points (rulings 2, 3, 4 and 6). **John ruled that this
record stands on all four**
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`).*

**Cautions recorded with the ruling.**

1. The session that recorded it wrote the packet, and before that the review
   of version 3, two earlier packets and the controls re-run. Rulings 1, 2
   and 3 close gaps in rulings that session drafted; ruling 2 confirms a
   reading that session chose.
2. The packet had not been checked by a second session when John ruled, and
   version 4 had not been checked either. Both checks, and the check of this
   file, are owed.
3. **Ruling 6, part 2, was this session's own proposal and is in no earlier
   document.** John agreed to it from the packet's index and its summary in
   conversation, where it was one of three pages drawn to his attention.

---

## What was ruled

### 1. The fit floor is on the piece only

Only sizes of piece that themselves reach four fifths on held-out development
episodes may be chosen. **The whole read is not a second condition.** Its
count is printed beside the piece's in the reporting table. This narrows item
1 of the ruling on RT-212 (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`),
which put the floor on the whole read; that file gains a dated note.

The alternative that was put and not taken: requiring both.

### 2. The piece rule is applied after the layers are chosen

For each group of positions the rule first takes the fewest layers at which
the whole-state transplant clears its floor; only then are sizes whose piece
misses four fifths excluded. The piece rule never changes which layers are
used. **The registration says in a sentence what this can miss:** a model
whose label is readable only at layers later than the earliest ones at which
the transplant works returns "no verdict, read failed its floor". The report
for the first full-size free-model run already prints the accuracy at every
layer and the candidates the rule chose among, so such a miss is visible when
John rules at that stop.

The alternative that was put and not taken: letting the piece rule take part
in choosing the layers, which would need the toy re-run again.

### 3. The registered accuracy is computed on the laptop's processor, with the library versions pinned

The device is the laptop's processor. The model's states are 32-bit; the read
is fitted by scikit-learn in 64-bit. **The library versions are pinned in a
committed file named in the registration**, in the way
`.venv-lock-2026-08-28.txt` does for the project's environment. The figure
computed that way is the registered one. If the processor proves impractical
at full size, that is a fresh question for John, not a switch.

### 4. The episode counts are the toy's, and the sampling band is printed at the floor

600 development episodes with the last 180 held out; 800 fresh matched pairs;
800 on the relaxed set; 3,000 for the gates; 200 shuffles for the permutation
baseline. **Beside every count taken against the four-fifths floor, the
reporting table prints the band that sampling alone would put around it.**
Recorded with the ruling: at 180 held-out episodes one episode is 0.0056, and
a piece whose true accuracy is exactly four fifths passes about half the
time. A miss at the first full-size free-model run goes to John with that
band beside it.

The alternative that was put and not taken: more held-out episodes for the
read, which would need the toy fits run once at the new count.

### 5. The other-agent control is compared with twenty random pieces

Control 2 reports how often the own-directed action moves under the named
agent's piece, beside twenty random pieces of the same size at the same sites:
their middle value, their 95th percentile, and where the real figure sits
among them. No pass line, as ruled earlier that day. **The code changes
accordingly, and the code test of 2026-10-03 is run once more on the changed
code**, labelled a test of the code and not a result.

### 6. What a model's outcome is when its seeds disagree

**Part 1.** A model returns a reading if **at least two of its three seeds**
return one; the third is reported. This is the rule the design already uses
for its gate on learning and for the channel-removal check.

**Part 2.** **The separation between the two built anchors is the lowest
reading among arm C's seeds that read, minus the highest among arm T's seeds
that read. It must be at least 0.5.** Seeds are not paired by number.
Recorded reason: seed 0 of one model has no relation to seed 0 of another,
and a pairing by number is not defined when the two models read on different
numbers of seeds. On the toy this is 0.9926 (arm C reads 1.0051, 0.9926 and
0.9974; arm T reads 0.0000 on every seed;
`experiments/rehearsal-successor-measure/out-controls-rerun/summary.json`).

**What follows.** "Metric validated" means arms T and C each read on at least
two seeds and the separation so defined is at least 0.5. "Degree read" means
arm F reads on at least two seeds. If arm F reads on one seed only, the
outcome is "metric validated, degree not read", and that seed's figure is
printed as a description.

The queue ruling's page 1a set the bar at 0.5 as "the minimum gap between the
entangled arm's reading and the separable arm's reading" and did not say how
the gap is taken across seeds; the proposal's "per seed" was the proposal's.
This ruling says how. That file gains a dated note.

The alternatives that were put and not taken: all three seeds; and keeping
the gap paired by seed number.

### 7. The ordinary competing solver is run under the rules as now registered

The three committed ownership-blind toy models
(`experiments/rehearsal-successor-measure/out-repairs/models/ckpt_blind_base_seed{0,1,2}.pt`)
are put through the nomination and reading as registered, on the laptop, $0,
method committed before output, and checked by a session that did not run it,
**before the registration review**. The method states, as the running
session's reading, what "the model's own turn" and its twin pairing mean for
a solver with no acting channel. The expected result is no verdict on every
seed; a reading on any seed goes to John before anything else moves.

The alternative that was put and not taken: saying in the registration that
it was not measured.

---

## What this changes, and where

- **Proposal version 4:** section 3 (the outcome wording of ruling 6);
  section 7.2 (rulings 1 to 3); section 7.3, item 2 (ruling 5); section 7.5
  (the band of ruling 4); section 9 (the counts filled; the separation as
  defined); sections 7.3, 8.1 and 10 (the solver's figures once ruling 7's
  run exists); section 19 (the seven questions marked ruled). It is that
  version's author, or a session John names, who writes them in.
- **Dated notes** in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`
  (RT-212, item 1) and `docs/rulings/2026-09-26-weekend-1-queue.md` (page 1a).
- **Before the registration review, at $0:** the competing-solver run and its
  check (ruling 7); the changed control 2 code and its code test (ruling 5).
- **STATUS.md and data/project.toml are not touched by the commit that lands
  this file**, because pull request 83 was open and edits both; whichever
  session next updates them carries this ruling in.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 10 =====

===== RECORD 11 of 25 - John's ruling on which of the two records stands - `docs/rulings/2026-10-03-seven-questions-reconciliation.md` (complete file, 3,795 characters) =====
# Ruling 2026-10-03 (night): which of two records stands on the seven questions of proposal version 4

*Recorded 2026-10-03 (Pacific), night, in a Claude Code session. **Authorship:
John's.** The question was put to him with the four differences laid out and a
recommendation; he ruled in the words **"Your record stands on all four, do
the clean-up"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What happened

On the evening of 2026-10-03 the seven questions in section 19 of version 4
of the successor experiment proposal were put to John twice, in two sessions,
within minutes of each other, and he answered "Agreed on all" in both.

- **Record A:** `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
  by the session that drafted version 4 (pull request 83). It records
  agreement to version 4's own suggestions.
- **Record B:** `docs/rulings/2026-10-03-version-4-questions-rulings.md`, by
  the session that wrote a seven-page packet on the same questions
  (`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`, pull request
  84). It records agreement to that packet's recommendations.

Neither session knew of the other's record until both were filed. The two
agree on questions 1, 5 and 7 and on the main answer to 2, 4 and 6. They
differ on four points.

## What was ruled: record B stands on all four

| Question | Record A | Record B, which stands |
|---|---|---|
| 3, the device | the library versions are recorded and **not pinned** | the library versions are **pinned in a committed file named in the registration** |
| 2, the order of the piece rule | confirmed as run | confirmed as run, **and the registration says in a sentence what it can miss**: a model whose label is readable only at layers later than the earliest ones at which the transplant works returns no verdict |
| 4, the episode counts | the toy's counts | the toy's counts, **and beside every count taken against the four-fifths floor the reporting table prints the band that sampling alone would put around it** |
| 6, seeds that disagree | two of three; the separation "cleared if cleared on two or more seeds", compared seed by seed | two of three; **the separation is the lowest reading among arm C's seeds that read minus the highest among arm T's seeds that read, at least 0.5, with seeds not paired by number**; "metric validated" means both anchors read on at least two seeds and that separation clears; "degree read" means arm F reads on at least two seeds |

On everything else the two records say the same thing and both stand.

## What this changes, and where

- **Record A** gains a dated note at its head pointing here. Its text is
  otherwise left as written.
- **Record B** gains a dated note at its head saying a second record exists
  and that this file settles the differences.
- **Version 4 of the proposal** is edited at the passages that state these
  four points (its header table, sections 3, 7.2, 7.4, 7.5, 9 and 20), and
  carries a short notice at its head naming this ruling. **Those edits were
  made by the session that recorded this ruling, not by version 4's author,
  and version 4 is long: a sentence elsewhere in it may still state one of
  the four points the old way. Where it does, this ruling governs.** The
  check version 4 is owed should look for such sentences.

## Cautions

The session that recorded this wrote record B and the packet behind it, and
recommended that record B stand. John's ruling is in his own words, quoted
above. This file and the edits to version 4 are owed a check by a session
that wrote neither.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit registered text or protocol text.
===== END OF RECORD 11 =====

===== RECORD 12 of 25 - John's ruling on the two questions raised by the check of version 4 - `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` (complete file, 2,870 characters) =====
# Ruling 2026-10-03 (night): the two questions raised by the check of proposal version 4

*Recorded 2026-10-03 (Pacific), night, by the Claude Code coordination
session. **Authorship: mixed.** The check of version 4 (pull request 86,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md`,
section 6) proposed each answer. The coordination session put both questions
to John once, with those suggestions, and he ruled in the words **"Agreed on
both suggestions"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **The other-agent control's code is changed to draw twenty random pieces,
   and its code test is run again on the changed code, before the
   registration review.** This is how the second record of the seven-question
   ruling has it (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 5). The first record had it done with the registered measurement
   (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). Doing
   it before the review satisfies both records. The reconciliation
   (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`) did not list
   this difference. Version 4 follows the first record at lines 1834 to 1836
   and 3866 to 3868. The registration text follows this ruling.

2. **The rule that separates the two built models stays as ruled.** That rule
   is the lowest reading among the entangled model's seeds that return a
   reading, minus the highest among the separable model's, at 0.5 or more,
   with seeds not paired by number. It forgives a seed that returns no
   verdict. It does not forgive a seed that returns an odd reading. The
   registration says so in one sentence. The less strict alternative, which
   would take the middle reading of each model's three seeds, was not taken.

## For John to know, not ruled here

The check found six places where the two records of the seven-question ruling
differ without the reconciliation listing them (section 3.3 of the check). One
of them is question 1 above. On the other five, the second record simply says
more and nothing conflicts. Under the reconciliation's own rule that both
records stand, they stand as written in the second record, and the
registration text carries them.

## What this changes

- The registration text: both rulings above, the five fuller points from the
  second record, and the thirty wording fixes in section 4 of the check.
- Before the registration review: the other-agent control's code with twenty
  random pieces, and its code test re-run. The competing-solver session
  (branch `w2b-job1-competing-solver-run`) already has this change in its
  plan. Its check confirms the change was made.
- Nothing edits version 4, an earlier ruling file, STATUS.md or
  `data/project.toml` here.
===== END OF RECORD 12 =====

