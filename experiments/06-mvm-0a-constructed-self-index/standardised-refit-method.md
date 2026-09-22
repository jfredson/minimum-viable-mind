# The standardised refit at the same positions — method, committed before the run

*2026-09-20. **UNREGISTERED**, diagnostic only. No verdict is read and no
cell here feeds one. Local, inference only, no training, no network, $0
[C1/C2]. Reads no registered verdict and touches no registered text.
Fresh output file per checkpoint, nothing overwritten [C6].*

*Committed before the run produces any output, and in the same commit as
the first of the two follow-up runs — so this method was fixed before that
run's numbers existed, and nothing here can have been shaped by them.*

*Runs the second of the two follow-up runs ruled on 2026-09-20 (the brief
`reviews/2026-09-20-followup-runs-brief.md`). It answers the red-team
ledger's item on what an unscaled fit charges a quiet direction
(`RT-58`).*

## The question

The fitted linear read that came back **found nowhere** left the 448
residual directions on the scale they arrived in, under the classifier
library's standard squared penalty.

That penalty is charged on the weight, not on what the weight does. A
direction carrying a small share of the variation has a correspondingly
small typical value, so producing a given contribution to the decision
needs a proportionally larger weight — and a squared penalty charges the
**square** of that factor. The stack's own geometry measurement, taken at
every position during that run, puts between 88% and 99.5% of the
variation in ten of the 448 directions. The remaining 438 share what is
left, and a signal resident in one of them is pushed towards zero far
harder than the same signal in a loud one.

So the instrument was, by construction, worst placed against exactly the
thing the run existed to test: a self-index that is real, linear and
quiet. The method file of that run named this and declined to fix it,
which was honest and, for a first run whose credibility rested on
reproducing fifteen recorded numbers, reasonable. It should not be
declined twice.

**Does a read that puts every direction on equal terms first find
anything the unscaled read could not?**

## What is run

The same sweep on the same target, with one thing changed.

- **Target.** The model's own **register index** — the rank of its own
  marker word among the episode's four, in vocabulary order. Four
  answers. Unchanged.
- **Checkpoints.** The three A3 30-million-parameter checkpoints,
  verified by checksum: the pilot (`a3_30m_seed0.pt`), the second seed
  (`a3_30m_seed1.pt`) and the third (`a3_30m_seed2.pt`).
- **Episodes.** 2,000 paired episodes at content seed 20260917, giving
  **4,000 episodes** — the same episodes.
- **Layers.** 3, 4, 5, 7, 8. **Positions.** The same eleven: the nine
  testable ones, the model's own marker token as the positive control,
  and the model's first assignment value as the negative control.
- **Everything not named below** — the fold helper, the per-test seeding,
  the 200-draw shuffled-label null, the family of 135 discovery tests,
  the bar of 3.38 standard deviations, the degeneracy preconditions, the
  labels and the cells — is **imported from the code of the run this
  refits** (`src/fitted_position_sweep_a3.py`) rather than copied, so
  that "the same sweep" is a fact about the code.

### The one change: standardising, per fold, on training rows only

Before each fit, every residual direction is centred and scaled to unit
spread. **The mean and the spread are computed on the training rows of
that fold and applied to both the training and the held-out rows.** The
held-out rows contribute to neither statistic, which is what keeps the
held-out accuracy an honest estimate rather than one that has already
seen the answer's neighbourhood.

**Zero-spread directions.** A direction with no spread on a training fold
carries no information in that fold, and its scale is undefined, so
dividing by it is not an option. Pre-stated rule: **it is set to zero on
both the training and the held-out rows**, and the count of such
directions is reported per test. The rule is exercised in the self-test
against a planted constant direction.

### The regularisation strength is not tuned, and that is the point

**It stays at the library's default of 1.0 — the value the unscaled run
used — and nothing chooses it.**

Standardising already changes what that strength means, which is the
whole fix: on unit-spread features the same penalty charges a quiet
direction the same as a loud one. Adding a tuned strength on top would
change two things at once and would make the instrument's sensitivity
depend on a number picked after looking at data.

**There is also nowhere honest to pick it from.** The positive control is
the one position where the signal is enormous and unrepresentative of
every position the question is actually asked at; tuning there would set
the strength on the wrong regime. The nine testable positions *are* the
result, so tuning on them would be choosing the instrument to suit the
answer. A separate held-out sample would be a different and larger run
than the one authorised.

So: exactly one thing changes, and this file says so before the run. The
cost is stated plainly — this run does not establish that 1.0 is the best
strength for a standardised fit, and a null here is a null at this
strength.

### Why this is a second instrument and not a correction

The run this refits reproduced fifteen recorded numbers exactly and is
demonstrably the instrument that produced the record. **This one is not,
and does not claim to be.** It is declared as a second instrument with its
own anchor. Its numbers are not corrections of the first run's and are not
to be substituted for them; where the two disagree, both stand, as two
reads with different biases.

## The anchor, in three parts

The brief requires this run to pre-state its own anchor and to make clear
that failing to reproduce the *unscaled* numbers is not a failure. It has
three parts, and the first two are checked in the run itself, before any
sweep number is computed.

### Part A — the shared check, which can fail the run

The **unscaled** fit is re-run on the recorded 400-episode configuration
— the same 200 paired episodes, the original capture path, folds seeded by
layer as the original seeded them — and compared with the fifteen numbers
already on the record:

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot (seed 0) | 0.5025 | 0.5125 | 0.5225 | 0.5250 | 0.5175 |
| seed 1 | 0.4800 | 0.5250 | 0.5350 | 0.5275 | 0.5150 |
| seed 2 | 0.4600 | 0.4700 | 0.4950 | 0.4475 | 0.4825 |

**Every cell must match to within 0.0025**, one episode in 400. This
proves that the capture path, the episode draw, the fold helper and the
classifier configuration are all unchanged — that this run differs from
the recorded one **by the scaling and by nothing else**. A miss on any
cell makes the run a **FAILED INSTRUMENT**: it reports the differences and
nothing else.

The table is written into the code as a pre-stated claim **and** checked
against the committed record files, so neither can be quietly edited to
fit the other.

### Part B — this instrument's own declared anchor, which can also fail the run

The **standardised** fit is run on the same states, the same target and
the same folds, and reported in full beside Part A.

**It will not return the numbers in the table above, and that is not a
failure.** A standardised fit is a different estimator; landing somewhere
else is what it is for. It is therefore not compared with them.

What it must do is work where the answer is available. Pre-stated
requirement: **every one of the fifteen cells must reach an accuracy of at
least 0.35** at the model's own marker token, where the answer is the
input token, against a majority-class rate of 0.2582.

The floor is chosen from two numbers that were already on the record
before this run: the unscaled fit's **worst** recorded cell there is
0.4475, and the majority-class rate is 0.2582. A floor of 0.35 sits well
below the first, so a standardised read that is merely somewhat worse
than the unscaled one passes; and well above the second, so a read that
has collapsed onto naming the commonest answer fails. It catches a broken
implementation without being a lottery. Falling below it on any cell makes
the run a **FAILED INSTRUMENT**.

### Part C — in the self-test, not the run

**With the standardising step replaced by a do-nothing transform, the
standardised code path must reproduce the unscaled path's number exactly
— accuracy and optimiser pass counts, cell for cell.**

This is the strongest available proof that the scaling is the only thing
that changed: the two code paths are the same path. It is asserted in the
self-test, so it is checked every time the file is run and not only once.

The self-test also checks the change is real in the direction claimed: a
signal planted **only** in a direction ten thousand times quieter than the
loudest must be reachable after standardising and not before. If
standardising did nothing, that assertion would fail.

## The pre-stated cells

Unchanged from the run this refits, and imported from its code rather
than restated.

**Per test.** **FOUND** means all three of: margin at or above **3.38
standard deviations**, zero of 200 shuffled-label draws meeting or beating
the real accuracy, and accuracy above the majority-class rate. **NOT
FOUND** means any of the three fails. **MARGINAL** — three standard
deviations but not 3.38 — is reported and is not FOUND.

**The family.** Nine testable positions × five layers × three checkpoints
= **135 discovery tests**. The two control positions are not discovery
tests and are not counted. Spreading a 5% family-wise error over 135
tests, one-sided, needs 3.3740 standard deviations, applied at 3.38 —
rounded up, so the bar in force is never looser than the arithmetic asks
for. The per-test bar of 3.0 is still computed and reported, for
continuity.

**What 200 draws can and cannot certify, stated in advance.** Zero out of
200 establishes a probability below 0.005, about 2.58 standard deviations
— **below** the 3.38 the family bar needs. The count alone cannot certify
a family-safe clearance; the margin supplies the rest under a normal
approximation to a null measured with 200 draws. **A single FOUND cell is
suggestive and wants a targeted rerun at that position with far more
draws, not settled.** The findings will say so if it happens.

**The degeneracy precondition.** A test is **DEGENERATE** and gets no cell
if the shuffled-label null has zero spread, or a class is missing from a
training fold, or accuracy is exactly equal to the majority-class rate.
Every hit is reported, by test.

**The positive control** is the model's own marker token. A checkpoint
that fails it is **VOID**; if the **pilot** is void, the arm is VOID and
no cell is assigned. Clearing it does not certify sensitivity anywhere
else: the information is far more accessible there than at any testable
position, so a pass is necessary and not sufficient. The same cost
follows as before — if the index clears there and nowhere else, that
cannot separate "the models do not carry it away from that token" from
"this read cannot find it away from that token".

**The negative control** is the model's first assignment value, where the
model's own marker has not yet appeared anywhere and the answer is not
knowable. A clearance is treated as evidence of a leak rather than of
carrying, and is excluded from the cells.

**FOUND SOMEWHERE.** At least one of the nine testable positions is FOUND
on **the pilot**, and at least one testable position is FOUND on **at
least one other non-void checkpoint**.

> Reading: a standardised linear read finds the register index at a
> position where it has to have been carried rather than read off the
> current token, and **the unscaled read did not**. The positions that
> clear are the finding and they name where to look next. It would not
> settle red-team objection R1, and it would localize nothing until
> causal patching has run.

**FOUND NOWHERE.** The above does not hold.

> Reading: at these eleven positions, five layers and three checkpoints, a
> standardised linear read does not find the register index anywhere
> except where the answer is most explicitly available. Together with the
> unscaled run, that separates "not reachable under that penalty" from
> "not linearly present here" — which is the one thing the positive
> control cannot certify on its own. It is still **not** a finding of
> absence.

**These two are exhaustive by construction**, so a pattern like "found on
the pilot only" lands in FOUND NOWHERE despite not being nothing. The
findings **report the clearing positions per checkpoint regardless of
which cell fires**, and name the sub-pattern explicitly.

## The smallest signal this run could detect, against the measured ceiling

Reported per test: the accuracy the test would have to reach to clear the
bar is the null average plus 3.38 times the null spread, and the smallest
detectable signal is the share of episodes that would have to be legible,
with the rest at chance, to produce it.

**That share is calibrated against this instrument's own measured ceiling
at the positive control** — not against a perfect score, and **not against
the unscaled read's ceiling**. The correction note of 2026-09-20
(`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`) makes this
mandatory, and it is not a small adjustment: on the unscaled run it moved
the headline from a signal legible in about one episode in twenty-seven to
about one in eleven. Both the no-information rate and the majority-class
rate are given as the reference.

Comparing this run's reach with the unscaled run's is the point of the
exercise, and the comparison is only meaningful when each is calibrated
against its own ceiling. The findings will present them that way.

## The state-space geometry at every position

Measured at all of them, as in the run this refits: the share of variation
carried by the top ten of 448 directions, per position, per layer, per
checkpoint. It is the mechanism this run exists to neutralise, so it is
reported beside the cells rather than in a footnote.

## What the findings may and may not say

They may say where a standardised linear read finds the register index
and where it does not, on these checkpoints, at these positions; and how
that compares with the unscaled read at the same cells.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index.

- Under **Amendment A3 section 3.2** nothing counts as localized or as
  absent until causal patching has also run. Patching has never been run
  (the ledger's item on it, `RT-49`, and the item on what a probe-only
  null means, `RT-50`), so under the registered text a probe-only null is
  **instrument failure, not absence**. **The registered term for the
  line's state is *not testable (localization)*** until causal patching
  runs, and the findings use that term and no other.
- Standardising removes the penalty's bias against quiet directions. It
  does **not** make the read unbiased, and it is still one linear
  statistic at one strength.
- One target was read. The marker-word target under this same read
  remains unrun, at about seventy processor-hours.
- The pilot-versus-seeds legibility gap on the difference-of-averages
  control is carried as an open caveat and is not resolved here.
- It does not touch red-team objection **R1** and changes no registered
  result.

## What this cannot do

One fitted linear statistic at one regularisation strength, eleven
positions, five layers, 4,000 episodes, three 30-million-parameter
checkpoints on a synthetic grammar, one target. A null everywhere remains
consistent with identity being carried non-linearly, or distributed
across positions rather than resident at any one of them, or at a
position not on the list.

What it **can** do, and the reason it is worth eleven processor-hours, is
narrow one specific alternative: if the standardised read also finds
nothing, "the signal was there but this penalty could not reach it" stops
being an available explanation of the unscaled null.

## Cost and where the output goes

Local, inference only, no training, no network, $0 [C1/C2], on three
existing checkpoints. Fifty-five tests per checkpoint, the same count as
the run it refits, at about **eleven processor-hours**. The standardising
step itself is negligible beside the fit; how long the optimiser takes on
standardised features is not known in advance and may run either way, so
the wall-clock estimate is held loosely. The run this refits took 10.8
hours at four workers against a projected six and a half, and that
under-estimate is not repeated here: **expect twelve hours or more**, and
the findings will report the actual.

It is run as a background process with per-test progress, and it runs
**after** the other-agent index run, as the brief orders.

One fresh file per checkpoint under `a3-gates/`, named
`standardised_position_sweep_a3_<checkpoint>.json`, plus a summary file
and `standardised-refit-findings.md`. Nothing existing is overwritten.

Implementation: `src/standardised_position_sweep_a3.py`, committed
together with this file and before either produced any output. Gated on
the known-answer test, and deliberately not on the threshold lock, for the
reason given in the denoised-direction method file.

These findings go through a Gate B review before any of this enters
`STATUS.md`.
