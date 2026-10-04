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
