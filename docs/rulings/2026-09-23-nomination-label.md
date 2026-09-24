# Ruling 2026-09-23: the label the ownership read is fitted against is which marker word

*Recorded 2026-09-23 (Pacific). The session put the question, the three possible
answers and the measured table to John, and he chose. Recorded as mixed
authorship for that reason: the choice is his, and none of the wording below is
his drafting. No compute was launched and no money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).*

*Filed as its own dated file rather than as further numbered items in
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`. That file
is a different day and a different subject — verifying reviews and releasing
money in two stages — and John's standing permission to annotate a recorded
ruling file covers bookkeeping only. Adding a new ruled item to it would be a
different act, so this is a new file and nothing in that one is touched.*

---

## What the question was

The successor experiment measures how spread out a model's answer to "whose
value do I need here" is. A reading of **0.0000** means the answer sits in a slot
of its own; a reading near **1.0000** means it is stirred through everything. To
get that number, the procedure first has to decide which part of the model's
internal state counts as the ownership answer. That step is the **nomination**
step, and section 7.2 of `docs/successor-experiment-proposal-2026-09-21.md` says
to do it by fitting a straight line that reads off "which agent is acting" and
taking its leading directions.

It never says what that straight line is fitted **against**. In these episodes
the made-up names that stand for agents — the marker words — are drawn afresh
every episode on purpose, so that no name is permanently attached to any agent,
and the phrase has at least three meanings:

- **the agent's slot** — its position in the episode's list of agents;
- **the marker's rank** — where the model's own marker word falls among the four
  present, in dictionary order. This is the programme's own existing convention,
  carried over from the method file for the earlier eleven-position fitted read;
- **which marker word** — which of the pool of names is the model's own.

The experiment's central number depends on that choice, and nobody had made it.
The measurement rehearsal found it, and it was blocking registration.

## The measurement the ruling rests on

The rehearsal trained three small models — it calls them arms — and measured all
three readings on the one whose right answer is known in advance: the arm built
so that the ownership answer sits in a slot of its own, whose reading is
therefore **0.0000 by construction**. At seed 0, with the whole-state
transplant and the ownership-only transplant put through the measure:

| reading of the label | whole-state | ownership-only | the degree it reports |
|---|---|---|---|
| the agent's slot | 1.0000 | 0.0117 | **0.9883** |
| the marker's rank | 1.0000 | 0.0050 | **0.9950** |
| which marker word | 1.0000 | 1.0000 | **0.0000** |

Across the three seeds the marker's rank reports **0.9950 / 0.9817 / 0.9883**,
and the agent's slot reports **0.9883 / 1.0000 / 1.0000**. Which marker word
reports **0.0000** on all three.

So two of the three readings put an arm whose degree is zero by construction at
the entangled end of the scale — the largest wrong answer the scale allows — and
give no sign that anything went wrong.

## 1. The label is which marker word

**Ruled: the straight-line read is fitted against which marker word is the
model's own.** It is the only one of the three readings that recovers a degree
known independently of the instrument, and it recovers it exactly, on all three
seeds.

## 2. The first answer, and why it is on the record

John's first choice was **the marker's rank**. The rehearsal findings annotate
that reading as "the programme's own convention", which reads like the
established and therefore safe choice. It is one of the two that break the
measure: it reports 0.9950, 0.9817 and 0.9883 for an arm whose degree is zero,
which is as wrong as the scale permits, and its straight line fits well — 0.706,
0.694 and 0.700, which the findings record as far above the level guessing
reaches — so nothing about it looks wrong from the fit alone.

He was then shown the measured table above and changed his answer. That sequence
is recorded because it is what makes the ruling defensible: the choice was made
against a measurement on an arm whose answer was known in advance, not against
which option sounded most like house practice. A later session re-reading this
should be able to see that the safe-sounding option was the one on the table and
was rejected on evidence.

## 3. What this does not settle: the label is fixed, the procedure is not one instrument

**The nomination problem is not closed by this ruling.** Across the nine
arm-and-seed pairs the rehearsal ran, the reading that wins is not the same one
twice running: which marker word wins seven times, the marker's rank once, and
the agent's slot once. A procedure that silently picks one of three meanings
depending on which system it is pointed at is three instruments, not one.

That is a second defect, independent of the missing label, and the registration
still has to answer it. Fixing the label stops the search choosing for itself,
which is what this ruling buys; it does not make the instrument behave the same
way on every arm. Nobody should read this file as closing the nomination step.

## 4. The standing of the figures above

Every figure in this file comes from the separable arm — the one built so the
ownership answer sits in a slot of its own — and was read out of
`docs/2026-09-21-successor-measure-rehearsal.md`, section 3.

Those figures reproduced **exactly** when the rehearsal was re-run from the
committed code, from clean, on 2026-09-22. That check is recorded in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`.

The reason this has to be said plainly is that the rehearsal's other two arms —
the one built to be entangled and the freely trained one — **did not** reproduce.
Their training does not give the same answer twice: the entangled arm's readings
moved by up to 0.05 between the record and the re-run, and two runs of the same
seed differ by up to 0.51 in the saved weights against 0.0003 on the separable
arm. The separable arm is steady not because its training is reproducible but
because it answers perfectly, and a weight that moves in the fourth decimal place
cannot move a saturated answer.

So these figures are trustworthy as a demonstration on the one arm whose answer
is known, and they are **not** evidence about what the instrument does in
general. Nobody should later quote them as the general case, and nobody should
infer from their stability that the rehearsal's training reproduces.

---

## What was NOT ruled here

- **No money was authorised and none was spent.** This ruling is about a word in
  a procedure. Nothing was launched, and the short slice of rented machine time
  still has no fresh go from John — see the launcher-guard ruling
  (`docs/rulings/2026-09-22-launcher-argument-guard.md`), item 4, which is where
  the earlier go lapsed.
- **Nothing else in the rehearsal's list of open numbers is answered.** Section
  11 of the rehearsal findings lists numbers still waiting on John — the
  separation bar, the floor on the whole-state transplant accuracy, the rank cap,
  the seed count and the rest. This ruling answers the nomination label and
  nothing else on that list.
- **Which of the two forms of the reading's arithmetic gets registered is still
  open.** The rehearsal reports both everywhere — the one the proposal writes and
  the one corrected for the floor the whole-state transplant has to clear — and
  adopts neither. This ruling does not adopt one either.
- **The registration text is not amended by this file.** What is ruled is the
  label; writing it into the proposal, and writing in the fact that the
  procedure is not one instrument across arms, is work still owed, and under the
  pairing rule that text is owed a check by a session other than the one that
  writes it.

## Recorded elsewhere

- `docs/2026-09-21-successor-measure-rehearsal.md`: a note added under section 3
  in the same commit as this file, saying the label has since been ruled. The
  findings are a dated record, so that is an addition and nothing in them is
  rewritten.
