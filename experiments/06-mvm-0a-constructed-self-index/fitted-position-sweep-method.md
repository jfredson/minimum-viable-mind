# The fitted linear read at all eleven positions — method, committed before the run

*2026-09-19. **UNREGISTERED**, diagnostic only. No verdict is read and no
cell here feeds one. Local, inference only, no training, no network, $0
[C1/C2]. Reads no registered verdict and touches no registered text.
Fresh output file per checkpoint, nothing overwritten [C6].*

*Committed before the run produces any output. The cells below were fixed
while nobody knew which would fire.*

*Runs decision 2 of the Gate B review of the linear-read closure
(2026-09-19): the closure items in the red-team ledger for the weaker read
(`RT-33`), for the claim that the line is closed (`RT-44`), and for the
untried cheapest follow-up (`RT-47`).*

## The question

The plain difference-of-averages read found own-agent identity at none of
the nine testable positions. Does a **fitted** linear classifier find it
at any of them?

This matters because the two reads are not equally sensitive. On these
very checkpoints, at the position where the answer is sitting in plain
sight as the input token, the difference-of-averages read scores 0.25 to
0.2675 while the fitted classifier scores 0.48 to 0.535 — against a
no-information rate of 0.25. That is the whole of the ledger's fatal
finding `RT-33`: the read used for the sweep is roughly half as sensitive
as one that was already written, already run, and never pointed at the
nine positions that matter.

## What is run

The same eleven positions, the same five layers and the same three
30-million-parameter checkpoints as the powered eleven-position sweep
(`powered-position-sweep-method.md`), read with the logistic-regression
classifier already implemented in `src/probe_target_diagnostic_a3.py`, on
the **four-answer register-index target**.

- **Checkpoints.** The three A3 30-million-parameter checkpoints, verified
  by checksum: pilot `a3_30m_seed0.pt` (`f751228c…`), seed 1
  `a3_30m_seed1.pt` (`eeed93b8…`), seed 2 `a3_30m_seed2.pt`
  (`f1f131cb…`).
- **Episodes.** 2,000 paired episodes at content seed 20260917, giving
  **4,000 episodes** — the same episodes the powered sweep used. Capture
  is chunked; the model is causal and each episode is encoded
  independently, so chunking changes nothing.
- **Layers.** 3, 4, 5, 7, 8.
- **Positions.** The same eleven, unchanged, with the same roles: position
  6 (`own_revision_marker`) is the control where the answer is knowable,
  position 1 (`own_assign_1_value`) is the control where it is not, and
  the other nine are testable.
- **Target.** The **register index**: the rank of the model's own marker
  word among the four marker words in the episode, in vocabulary order.
  Four answers. It is consistently defined across episodes and, once all
  four marker words have appeared, it is determinable from what the model
  has read.

### 1. The classifier, its penalty, and the fold scheme

**The classifier is not a new one.** It is the one already in
`probe_target_diagnostic_a3.probe`, kept identical so that the numbers it
already produced can be used as an instrument check:

- multinomial logistic regression, as provided by scikit-learn;
- the standard squared penalty on the weights, at the library's default
  strength (`C=1.0`);
- the `lbfgs` optimiser, capped at 2,000 passes;
- **features left on their original scale** — no standardising, no
  reduction of the 448 directions to fewer.

Two properties of this instrument are worth stating plainly rather than
discovering later.

**It does not always finish converging.** At 400 episodes it hits the
2,000-pass cap on every fold, so the numbers already on the record come
from a fit that stopped early. At 4,000 episodes it converges on most
folds (measured: 233 to 1,429 passes on a four-class target). The cap is
part of the instrument and is kept, because changing it would break the
comparison with the record. **Every fit records how many passes it
used**, and the findings report where the cap was hit.

**Leaving the features unscaled is a real choice with a real cost.** The
state space is extremely lopsided — about 99% of the variation lives in
ten of the 448 directions (`RT-34`). An unscaled fit is therefore pulled
towards the loud directions, and a signal living in a quiet one is harder
for it to reach. The fitted read is nonetheless far more sensitive than
the difference-of-averages read, which is the point; it is not a
sensitivity ceiling, and this method does not claim it is.

**Folds.** Four folds, assigned by the same helper every other run in
this stack uses.

**Seeding is per test, not per layer (`RT-39`).** The previous sweep gave
all 270 of its tests the same five fold splits and the same five sets of
shuffled labels, seeded by layer alone, so the tests were far less
independent than their count suggested. Here the fold split and the
shuffled-label draws are seeded from a stable digest of the **whole test
identity** — checkpoint, target, position and layer together — so no two
of the 165 tests share a split or a draw.

### 2. The null, and the bar, as a number

**The null.** For each test, **200 shuffled-label draws**: the same
classifier, the same folds, the labels shuffled. The real accuracy is
placed against the average and spread of those 200, and the count of
draws that met or beat it is reported beside the margin.

**The family.** One target × nine testable positions × five layers ×
three checkpoints = **135 discovery tests**. The two control positions are
not discovery tests and are not counted in the family, which follows the
powered sweep's convention exactly.

**The bar.** Spreading a 5% family-wise error across 135 tests needs a
per-test margin of **3.3740 standard deviations**. Applied at **3.38**,
rounded up so the bar in force is never looser than the bar the
arithmetic asks for.

- The per-test bar of **3.0 standard deviations is still computed and
  reported**, for continuity with every earlier run in this line.
- The cells turn on **3.38 standard deviations, and zero of the 200
  shuffled draws meeting or beating the real accuracy, and accuracy above
  the majority-class rate**. A test meeting all three is **FOUND**.
- A test that passes three standard deviations but not 3.38 is
  **MARGINAL**, is reported, and triggers no cell.

**Requiring the majority-class rate is new and it is deliberate.** With
four unequal answers a classifier that always names the commonest one
already scores about 0.26. The powered sweep's label did not require
beating that; here it does, because a fitted classifier is much more
likely than a difference of averages to collapse onto the commonest
answer and score exactly there.

**What 200 draws can and cannot certify, stated in advance.** Zero out of
200 establishes a probability below 0.005, which is about 2.58 standard
deviations — **below** the 3.38 the family bar needs. So the count alone
cannot certify a family-safe clearance; the standard-deviation margin
supplies the rest, and that part is a normal approximation to a null
measured with 200 draws. This is weaker than the powered sweep's 1,000
draws, and the reason is cost: the fitted classifier is about 240 times
more expensive per draw than the difference-of-averages read, and 200
draws across 165 tests is already about eleven hours of processor time.
**A single FOUND cell should therefore be read as suggestive and worth a
targeted rerun at that one position with far more draws, not as settled.**
The findings will say so if it happens.

### 3. The positive control for the register index, and what it costs

`RT-35` is right that the register-index arm has never had a control of
its own, and that the marker-word control at the input position is not
one. Here is the honest position.

**There is no guaranteed-present control for the register index.** The
marker word at position 6 is guaranteed present, because it *is* the token
being read. The register index at position 6 is only guaranteed
**derivable**: by the model's revision turn all four marker words have
appeared, so the answer is a function of what the model has read — but
nothing guarantees the model has actually computed it. A control must be
something we know is there, and this is something we know *could* be
there.

**What position 6 is used for anyway.** It is the reference cell, and the
fitted classifier already clears it on the record, on all three
checkpoints (0.4475 to 0.535 against a majority-class rate of about
0.26). So it is used as a one-way gate:

- **If the register index fails at position 6 on a checkpoint, that
  checkpoint is VOID** and its other positions are reported without
  interpretation. Failing where the answer is most explicitly available
  means the read cannot be trusted where it is less so.
- **Clearing at position 6 does not certify sensitivity anywhere else.**
  The information is far more accessible there than at any testable
  position, so a pass is necessary and not sufficient.

**What this costs the reading, stated plainly.** If the register index
clears at position 6 and nowhere else, that result cannot separate "the
models do not carry the register index away from that position" from "the
fitted read is not sensitive enough to find it away from that position."
The FOUND NOWHERE cell therefore does not license a claim of absence, and
the section on what the findings may not say holds it to that.

### 4. The pre-stated cells

**Per test.** **FOUND** means all three of: margin at or above 3.38
standard deviations, zero of 200 draws meeting or beating the real
accuracy, and accuracy above the majority-class rate. **NOT FOUND** means
any of the three fails. **MARGINAL** — three standard deviations but not
3.38 — is reported and is not FOUND.

**The degeneracy precondition, carried forward unchanged.** A test is
**DEGENERATE** and gets no cell if the shuffled-label null has zero
spread, or a class is missing from a training fold, or **accuracy is
exactly equal to the majority-class rate**. Two tests on the pilot hit
that last condition in the previous sweep and the findings did not say so
(`RT-38`); **every degeneracy hit is reported here, by test**.

**Across checkpoints**, applied to the register-index arm. A checkpoint
whose position-6 control fails is VOID and excluded; if the **pilot** is
void, the arm is VOID and no cell is assigned.

**FOUND SOMEWHERE.** At least one of the nine testable positions is FOUND
on **the pilot**, and at least one testable position is FOUND on **at
least one other non-void checkpoint**.

> Reading: a fitted linear read finds own-agent identity at a position
> where it has to have been carried rather than read off the current
> token. The positions that clear are the finding and they name where to
> look next. It would not settle red-team objection R1 — what is carried
> could be the acting channel's trace passed forward rather than a
> self-index — and it would not localize anything until causal patching
> has run.

**FOUND NOWHERE.** The above does not hold.

> Reading: at these eleven positions, five layers and three checkpoints,
> a fitted linear read does not find the register index anywhere except
> where the answer is most explicitly available. See the limits: this is
> not a finding of absence.

**These two are exhaustive by construction**, and that has the same cost
it had last time: a pattern like "found on the pilot only" lands in FOUND
NOWHERE despite not being nothing. So the findings **report the clearing
positions per checkpoint regardless of which cell fires**, and name the
sub-pattern explicitly. The cell is a summary, not the whole result.

**The negative control.** A clearance at position 1 is reported, is
treated as evidence of a leak rather than of carrying, and is excluded
from the cells — unchanged from the powered sweep, whose self-test
verified against real episodes that the model's own marker really is
absent before its first own value token. That check is re-run here.

### 5. The anchor reproduction, and what fails the run

The fitted classifier's register-index numbers at the marker position are
already on the record for all three checkpoints, in
`probe_target_diagnostic_a3_*.json`, at 400 episodes:

| checkpoint | layer 3 | layer 4 | layer 5 | layer 7 | layer 8 |
|---|---|---|---|---|---|
| pilot (seed 0) | 0.5025 | 0.5125 | 0.5225 | 0.5250 | 0.5175 |
| seed 1 | 0.4800 | 0.5250 | 0.5350 | 0.5275 | 0.5150 |
| seed 2 | 0.4600 | 0.4700 | 0.4950 | 0.4475 | 0.4825 |

**Before any sweep number is computed**, the run re-runs that exact
configuration — 200 paired episodes at content seed 20260917, the original
capture path, folds seeded by layer as the original seeded them — and
compares all fifteen cells.

- **Every cell must match to within 0.0025**, which is one episode in 400,
  the smallest difference the statistic can express. Anything larger on
  any cell makes the run a **FAILED INSTRUMENT**: it reports the
  differences and nothing else, and says nothing about any position.
- The differences are reported whether or not they are zero, and an exact
  match on all fifteen is reported as such.

The expected values above are written into the code as a pre-stated
claim, **and** checked against the committed record files, so that neither
can be quietly edited to fit.

### 6. The state-space geometry at every position

`RT-40` notes the geometry was measured at one position of eleven. It is
cheap here — one decomposition of a 4,000 by 448 table per position and
layer, well under a second — so it is measured at **all** of them: the
share of variation carried by the top ten directions, reported per
position, per layer, per checkpoint.

### 7. The marker-word target: not run, and why

The brief asks for the marker-word target too if it fits in the session.
**It does not fit, and this is stated before the run rather than after.**

Measured on real captured states, one four-fold pass costs 1.19 seconds on
the four-answer register index and 7.56 seconds on the 25-answer marker
word, because the 25-answer fit hits the 2,000-pass cap on most folds. At
200 draws across 165 tests that is about **11 processor-hours for the
register index and about 70 for the marker word** — and 70 processor-hours
does not fit in a session on this machine at any useful degree of
parallelism. Cutting its draws to 50 would still cost about 17
processor-hours on top of the register-index run, and would leave its null
too coarse to resolve a bar anywhere near 3.38.

So the marker-word target is **not run here**. The register-index target
is the one the brief names as primary, it is the one the classifier has
already been run on at the marker position, and it is the one with an
anchor to reproduce. The family and the bar above are fixed for the
register-index arm alone and do not change.

### 8. The smallest signal this run could detect

Reported per test, by the method `RT-37` used: the accuracy the test would
have to reach to clear the bar is the null average plus 3.38 times the
null spread, and the smallest detectable signal is the share of episodes
that would have to be perfectly legible, with the rest at chance, to
produce it. Both the no-information rate and the majority-class rate are
given as the reference, because the cells use the stricter one.

## What the findings may and may not say

They may say where a fitted linear read finds own-agent identity and where
it does not, on these checkpoints, at these positions.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index. Under Amendment A3 §3.2 nothing counts as
localized or as absent until causal patching has also run (`RT-49`,
`RT-50`); a probe-only null is instrument failure under the registered
text, not absence. The findings quote the pilot-versus-seeds legibility
gap as a caveat and **do not resolve it** (`RT-36`).

The findings go through a Gate B review before any of this enters
STATUS.md.

## What this cannot do

One fitted linear statistic, eleven positions, five layers, 4,000
episodes, three 30-million-parameter checkpoints on a synthetic grammar,
one target. A null everywhere is consistent with identity being carried
non-linearly, or distributed across positions rather than resident at any
one of them, or at a position not on the list, or in a quiet direction an
unscaled fit is pulled away from. It does not touch red-team objection R1.
It changes no registered result.

## Cost and where the output goes

Capture is about two and a half minutes per checkpoint per pass, two
passes. Scoring is about 201 fits per test at 1.19 seconds, 55 tests per
checkpoint: about 3.7 processor-hours per checkpoint, about 11 in total.

Scoring runs in parallel across tests, but the speed-up is poor and the
reason is worth recording: the fit is limited by how fast the machine can
move the state table through memory, not by how fast it can multiply, so
extra workers mostly wait. Measured on real states, four workers reach
1.46 fits per second against 0.63 for one — a speed-up of about 2.3 — and
six workers are no faster than four. **So the run takes about six and a
half hours of wall-clock time**, and it is run as a background process
with per-test progress. Local, inference only, $0.

One fresh file per checkpoint under `a3-gates/`, named
`fitted_position_sweep_a3_<checkpoint>.json`, plus a summary file and
`fitted-position-sweep-findings.md`. Nothing existing is overwritten.

Implementation: `src/fitted_position_sweep_a3.py`, committed together with
this file and before either produced any output. Gated on the known-answer
test, and deliberately not on the threshold lock, for the reason given in
`denoised-direction-method.md`.
