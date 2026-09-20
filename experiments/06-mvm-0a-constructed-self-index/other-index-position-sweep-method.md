# The other agent's index at the same positions — method, committed before the run

*2026-09-20. **UNREGISTERED** as a verdict-bearing run, diagnostic only.
No verdict is read and no cell here feeds one. Local, inference only, no
training, no network, $0 [C1/C2]. Reads no registered verdict and touches
no registered text. Fresh output file per checkpoint, nothing overwritten
[C6].*

*Committed before the run produces any output. The cells below, and the
prediction in the next section, were fixed while nobody knew which would
fire.*

*Runs the first of the two follow-up runs ruled on 2026-09-20 (the brief
`reviews/2026-09-20-followup-runs-brief.md`). It answers the red-team
ledger's item on the confound at the other agent's revision value
(`RT-82`, numbered `RT-64` in the review file), and it runs an instrument
that is already registered and has never been run: Amendment A3 section
3.1 lists it as matched control **L2(a)** — "the *other-index* subspace:
the same localization run for a named non-self agent ('which marker is
agent B's'), matched in rank and probe accuracy".*

## The question

The fitted linear read at eleven positions came back **found nowhere**,
with one pattern worth naming. At the other agent's revision value the
model's own register index — the rank of the model's own marker word
among the episode's four — read positive on fifteen tests out of fifteen,
reaching +2.33, +2.39 and +3.34 standard deviations at the best layer on
the three checkpoints, and reaching MARGINAL once on the third
checkpoint.

Two readings fit that, and they point in opposite directions.

- **The model carries a self-index away from its own act position.** That
  is close to what the registration defines the thing being looked for to
  be: Amendment A3 section 3.1 defines the target as a subspace carrying
  "which marker is mine" at positions *away from* act positions.
- **Or the state at that token represents which agent is speaking.** An
  agent is never its own other, so representing the speaker's rank
  removes one of four possibilities for the model's own rank. That lifts
  the best attainable accuracy on the own index from 0.25 to about 0.333
  with no own-agent representation involved at all. The MARGINAL sits at
  0.277, comfortably inside what the confound alone could produce.

This run separates them by pointing the identical read at the other
agent's index instead of the model's own.

## The prediction, stated before the run

Measured on the episode builder before this run, with no checkpoint
loaded — this is a fact about how the grammar lays turns out, not about
any model:

**Agent B's identity is a function of the tokens read at the other
agent's revision value in 100% of episodes, and at the other agent's
revision decision, one token earlier, in 0% of them.**

The reason is arithmetic in the grammar. For one contested item the four
agents hold four distinct values, and the revision rule — take the next
slot, wrapping — is a one-to-one map. So a revision turn's **value** is
unique to its agent given the assignment block that precedes it, and
reading it pins who is speaking. The "to" one token earlier pins nothing:
the item is known and the value is not.

That boundary is exactly where the own-index sweep changed character.
The other agent's revision decision showed nothing at all, averaging
−0.17 standard deviations across its fifteen tests; the other agent's
revision value one token later was positive on all fifteen. So:

- **If the exclusion reading is right**, this run finds the other agent's
  index at the other agent's revision value and not at the decision one
  token earlier.
- **If it finds the other agent's index at neither**, the exclusion
  reading is not supported, and the own-index pattern is left
  unexplained rather than explained away.
- **If it finds the other agent's index in both places**, the boundary is
  not where the grammar says it is and something in the instrument needs
  looking at before either reading is taken further.

Writing this down in advance is the point of the run. It is not a
hypothesis test with a cell of its own; the cells below are the only
things that fire.

## What is run

The same read, with one thing changed: the target.

- **Checkpoints.** The three A3 30-million-parameter checkpoints, verified
  by checksum: the pilot (`a3_30m_seed0.pt`), the second seed
  (`a3_30m_seed1.pt`) and the third (`a3_30m_seed2.pt`).
- **Episodes.** 2,000 paired episodes at content seed 20260917, giving
  **4,000 episodes** — the same episodes every run in this line has used.
- **Layers.** 3, 4, 5, 7, 8.
- **Positions.** The same eleven, unchanged, **plus one** — see below.
- **The read.** The classifier, its squared penalty and the library's
  default strength, the optimiser and its 2,000-pass cap, the fold
  helper, the per-test seeding, the 200-draw shuffled-label null and the
  family-adjusted bar are **imported from the code of the run this
  matches** (`src/fitted_position_sweep_a3.py`) rather than copied into
  the new file. "The same read" is therefore a fact about the code and
  not a claim about it.

### The target: the other agent's index

**Agent B is the other reviser** — the one non-self agent that revises in
the episode, and whose turn supplies the two "other" positions in the
eleven. The episode builder's own bookkeeping already requires exactly
one, and an episode without one is dropped before any of this starts.

The target is **the rank of agent B's marker word among the episode's
four marker words, in vocabulary order**. Four answers, the same quantity
the own-index arm reads, read off a different agent.

**It is matched in rank, and that was measured before the run.** Across
4,000 episodes the other-agent index has the same class shares as the own
register index to four decimal places — 0.2582, 0.2410, 0.2547, 0.2460 —
so the majority-class rate a classifier gets for free is identical, and
the no-information rate is 0.25 for both. The two are **never equal**,
which is the exclusion that makes this the control that settles the
question.

**Why agent B is the other reviser and not some other non-self agent.**
The confound under test is about the agent whose turn the reading
position sits inside. Any other choice — the first agent to speak, a
fixed slot — would be a different agent from the one the confound names,
and would answer a question nobody asked.

### The one position added, and why

The eleven positions were chosen for the own-index target, and one of
them, the model's own marker token, was the positive control: the place
where the answer is the input token. **This target has no such position
among the eleven.** The other agent's revision decision and revision
value both sit *before* agent B's marker word in that turn, because a
turn renders as `assign {item} to {value} by {marker}` with the name
last.

Running without one would leave the run with no gate and, worse, no
measured ceiling — and the correction note of 2026-09-20
(`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`) requires
every detectable-signal figure to be calibrated against the read's own
measured ceiling rather than against a perfect score.

So **one position is added**: the marker token of agent B's revision
turn, two tokens after its value. It is the matched analogue of the
model's own marker token in the run this matches, and it is used for
nothing else:

- it is the **positive control**;
- it is **not a discovery test** and is **not counted in the family**;
- it is where the ceiling is measured.

This is a stated departure from the brief's "same eleven positions". It
adds a control, not a place to look for a result; the nine testable
positions are the same nine, so the two runs still compare cell for cell.

### The roles of the eleven, restated for this target

- **The nine testable positions are unchanged**, so every cell in this
  run has a counterpart in the run it matches.
- **The model's own marker token is no longer a control.** For the own
  index it was the place the answer sat in plain sight; for this target
  it says which rank is the model's, which is the one rank agent B's
  cannot be. It is reported as a diagnostic, is not a control, and is not
  in the family.
- **The negative control changes shape** — see the next section.

### The exclusion rule, stated in advance

The brief asks this run to pre-state its rule for positions where agent
B's marker has not yet appeared. Measured on the episode builder before
the run, with no checkpoint loaded:

| position | agent B's marker word has appeared | agent B's identity is determinable |
|---|---|---|
| the model's first assignment value | 50.00% | 0% |
| the model's second assignment value | 83.77% | 0% |
| the model's revision decision | 100% | 50% |
| the model's revision value | 100% | 50% |
| one after the model's revision value | 100% | 50% |
| the model's own marker token | 100% | 50% |
| the line break before the model's revision turn | 100% | 50% |
| the other agent's revision decision | 100% | **0%** |
| the other agent's revision value | 100% | **100%** |
| agent B's marker token *(the positive control)* | 100% | 100% |
| the appended question's answer marker | 100% | 100% |
| the appended question's answer token | 100% | 100% |

**The rule: no episode is dropped from any test in the family.** Every
position is read on all 4,000 episodes, exactly as the run this matches
reads them, so the two compare cell for cell and no position is scored on
a different sample from its counterpart. What differs between positions
is the **attainable ceiling**, and that is reported per position as the
two shares above rather than hidden by dropping rows. A null at a
position where the answer is determinable on half the episodes is read
against that half, and the findings say so.

**The one exception is the negative control, where the restriction is the
definition.** See below.

The second column is the one that matters and it is the sharper
measurement. A marker word having appeared somewhere is weak: by the
model's revision turn all four have appeared, so it distinguishes
nothing. Whether agent B's *identity* is pinned by what has been read is
the real ceiling, and it is not 1.0 everywhere.

### The controls

**The positive control** is agent B's marker token, where the answer is
the input token. A checkpoint that fails it is **VOID** and its other
positions are reported without interpretation: failing where the answer
is most explicitly available means the read cannot be trusted where it is
less so. **Clearing it does not certify sensitivity anywhere else** — the
information is far more accessible there than at any testable position,
so a pass is necessary and not sufficient. This is the same one-way gate
the matched run used, and it carries the same cost: if the other-agent
index clears at its marker token and nowhere else, that cannot separate
"the models do not carry it away from that token" from "this read cannot
find it away from that token".

**The negative control** is the model's first assignment value,
**restricted to the episodes in which agent B's marker word has not yet
appeared anywhere** — half of them, measured above, so about 2,000
episodes. Nothing about agent B is in context there: the marker has not
been seen and no revision has happened, so the identity is not
determinable by any route. A clearance there is evidence of a leak rather
than of carrying, and is excluded from the cells. This is the only test in
the run whose rows are restricted, and the restriction is what makes it a
control.

The unrestricted first assignment value is also reported, with no role.

### Seeding, the null and the bar

**Seeding is per test.** The fold split and the shuffled-label draws are
seeded from a digest of the whole test identity — checkpoint, target,
position and layer together — so no two tests share a split or a set of
draws. The target name differs from the matched run's, so no test here
shares a split with any test there either.

**The null.** For each test, 200 shuffled-label draws: the same
classifier, the same folds, the labels shuffled. The real accuracy is
placed against the average and spread of those 200, and the count of
draws that met or beat it is reported beside the margin.

**The family.** Nine testable positions × five layers × three checkpoints
= **135 discovery tests**, the same family as the run this matches. The
positive control, the negative control and the two diagnostic positions
are not discovery tests and are not counted.

**The bar is recomputed, not assumed.** Spreading a 5% family-wise error
over 135 tests, one-sided, needs a per-test margin of **3.3740 standard
deviations**, applied at **3.38** — rounded up, so the bar in force is
never looser than the bar the arithmetic asks for. The code computes this
from the number of tests actually run rather than carrying a constant, and
the self-test checks that the rule reproduces 3.38 on 135 tests and 3.35
on 120.

- The per-test bar of **3.0 standard deviations is still computed and
  reported**, for continuity with every earlier run in this line.
- The cells turn on **3.38 standard deviations, and zero of the 200
  shuffled draws meeting or beating the real accuracy, and accuracy above
  the majority-class rate**. A test meeting all three is **FOUND**.
- A test that passes three standard deviations but not 3.38 is
  **MARGINAL**, is reported, and triggers no cell.

**What 200 draws can and cannot certify, stated in advance.** Zero out of
200 establishes a probability below 0.005, which is about 2.58 standard
deviations — **below** the 3.38 the family bar needs. The count alone
therefore cannot certify a family-safe clearance; the standard-deviation
margin supplies the rest, and that part is a normal approximation to a
null measured with 200 draws. **A single FOUND cell should be read as
suggestive and worth a targeted rerun at that one position with far more
draws, not as settled.** The findings will say so if it happens.

## The pre-stated cells

**Per test.** **FOUND** means all three of: margin at or above 3.38
standard deviations, zero of 200 draws meeting or beating the real
accuracy, and accuracy above the majority-class rate. **NOT FOUND** means
any of the three fails. **MARGINAL** — three standard deviations but not
3.38 — is reported and is not FOUND.

**The degeneracy precondition.** A test is **DEGENERATE** and gets no cell
if the shuffled-label null has zero spread, or a class is missing from a
training fold, or accuracy is exactly equal to the majority-class rate.
Every degeneracy hit is reported, by test.

**Across checkpoints.** A checkpoint whose positive control fails is VOID
and excluded; if the **pilot** is void, the arm is VOID and no cell is
assigned.

**FOUND SOMEWHERE.** At least one of the nine testable positions is FOUND
on **the pilot**, and at least one testable position is FOUND on **at
least one other non-void checkpoint**.

> Reading: a fitted linear read finds the other agent's index at a
> testable position. **Where** is the finding. A clearance at the other
> agent's revision value supports the exclusion reading of the own-index
> MARGINAL and closes that position; a clearance only elsewhere does not.

**FOUND NOWHERE.** The above does not hold.

> Reading: at these positions, five layers and three checkpoints, a
> fitted linear read does not find the other agent's index anywhere
> except where its marker is the input token. This does not support the
> exclusion reading, and it is **not** a finding of absence.

**These two are exhaustive by construction**, which costs the same thing
it cost last time: a pattern like "found on the pilot only" lands in
FOUND NOWHERE despite not being nothing. So the findings **report the
clearing positions per checkpoint regardless of which cell fires**, and
name the sub-pattern explicitly. The cell is a summary, not the whole
result.

## The instrument check

This run changes the target and nothing else, so **its instrument check is
the matched run's**: the fifteen fitted-classifier register-index
accuracies at the model's own marker token, 400 episodes, already on the
record in the committed per-checkpoint files from the earlier probe-target
diagnostic.

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot (seed 0) | 0.5025 | 0.5125 | 0.5225 | 0.5250 | 0.5175 |
| seed 1 | 0.4800 | 0.5250 | 0.5350 | 0.5275 | 0.5150 |
| seed 2 | 0.4600 | 0.4700 | 0.4950 | 0.4475 | 0.4825 |

**Before any sweep number is computed**, the run re-runs that exact
configuration and compares all fifteen cells. **Every cell must match to
within 0.0025**, which is one episode in 400, the smallest difference the
statistic can express. Anything larger on any cell makes the run a
**FAILED INSTRUMENT**: it reports the differences and nothing else, and
says nothing about any position. The differences are reported whether or
not they are zero.

The expected values above are written into the code as a pre-stated claim
**and** checked against the committed record files, so that neither can be
quietly edited to fit the other.

**The capture path is checked too.** Adding a twelfth position means
teaching the capture step about it, and a capture step that quietly moved
the other eleven would invalidate the comparison the whole run exists to
make. The self-test therefore runs the capture twice on a small,
randomly-initialised model — no checkpoint is read — once through the
matched run's unmodified capture and once through this run's, and
requires the eleven to come back **element for element identical** and the
same episodes to be kept.

## The smallest signal this run could detect, against the measured ceiling

Reported per test: the accuracy the test would have to reach to clear the
bar is the null average plus 3.38 times the null spread, and the smallest
detectable signal is the share of episodes that would have to be legible,
with the rest at chance, to produce it.

**That share is calibrated against this read's own measured ceiling at the
positive control, not against a perfect score.** The correction note of
2026-09-20 makes this mandatory, and it is not a small adjustment: on the
matched run it moved the headline from a signal legible in about one
episode in twenty-seven to about one in eleven. Both the no-information
rate and the majority-class rate are given as the reference, because the
cells use the stricter one.

## The state-space geometry at every position

Measured at all of them, as in the matched run: the share of variation
carried by the top ten of 448 directions, reported per position, per
layer, per checkpoint.

## What the findings may and may not say

They may say where a fitted linear read finds the other agent's index and
where it does not, on these checkpoints, at these positions; and whether
that pattern supports or fails to support the exclusion reading of the
own-index result.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index.

- Under **Amendment A3 section 3.2** nothing counts as localized or as
  absent until causal patching has also run. Patching has never been run
  (the ledger's item on it, `RT-49`, and the item on what a probe-only
  null means, `RT-50`), so under the registered text a probe-only null is
  **instrument failure, not absence**. **The registered term for the
  line's state is *not testable (localization)*** until causal patching
  runs, and the findings use that term and no other.
- The features are left unscaled, so this read is pulled towards the ten
  loud directions and a signal living in a quiet one is harder for it to
  reach (the ledger's items on the lopsided state space, `RT-34`, and on
  what a squared penalty charges a quiet direction, `RT-58`). The second
  of the two follow-up runs addresses exactly that, and this one does
  not.
- The pilot-versus-seeds legibility gap on the difference-of-averages
  control is carried as an open caveat and is not resolved here.
- It does not touch red-team objection **R1** and changes no registered
  result.

## What this cannot do

One fitted linear statistic, twelve positions, five layers, 4,000
episodes, three 30-million-parameter checkpoints on a synthetic grammar,
one target. A null everywhere is consistent with the other agent's index
being carried non-linearly, or distributed across positions rather than
resident at any one of them, or at a position not on the list, or in a
quiet direction an unscaled fit is pulled away from.

And a clearance is not a mechanism. Finding the other agent's index at
the other agent's revision value would show the state there carries who
is speaking; it would not show that the own-index reading at the same
token is *caused* by that, only that a confound large enough to produce
it is demonstrably present. Settling causation needs patching.

## Cost and where the output goes

Local, inference only, no training, no network, $0 [C1/C2], on three
existing checkpoints. Sixty-five tests per checkpoint against the matched
run's fifty-five — the twelfth position adds five, the restricted
negative control adds five more on about half the episodes — so roughly
**twelve to thirteen processor-hours** against the matched run's eleven.
It is run as a background process with per-test progress. The matched run
took 10.8 hours of wall-clock time at four workers, and its method
under-estimated that; this one is expected to take longer than that
rather than less, and the findings will report the actual.

One fresh file per checkpoint under `a3-gates/`, named
`other_index_position_sweep_a3_<checkpoint>.json`, plus a summary file and
`other-index-position-sweep-findings.md`. Nothing existing is
overwritten.

Implementation: `src/other_index_position_sweep_a3.py`, committed together
with this file and before either produced any output. Gated on the
known-answer test, and deliberately not on the threshold lock, for the
reason given in the denoised-direction method file.

These findings go through a Gate B review before any of this enters
`STATUS.md`.
