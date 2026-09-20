shape.

**Pre-stated cells and the degeneracy rule.** Both fixed in the method
file and both implemented as written. FOUND requires three things
together: margin at or above the bar, zero of 200 draws matching or
beating the real accuracy, and accuracy above the majority-class rate.
The degeneracy rule suppresses a label if the null has no spread, a class
is missing from a training fold, or accuracy lands exactly on the
majority-class rate. The code's self-test plants a signal and confirms
FOUND, plants noise and confirms no label, raises the bar out of reach
and confirms the same planted signal is demoted to MARGINAL, and starves
a class to confirm the degeneracy rule fires and suppresses the label. I
read all of it.

**The anchor reproduction.** This is the strongest piece of engineering
in the stack and it deserves saying. The fifteen recorded numbers are
written into the code as a pre-stated claim, **and** the code refuses to
run at all unless those fifteen values match the committed record files
to nine decimal places. So the code cannot be edited to fit the record,
and the record cannot be edited to fit the code, and a mismatch stops the
run rather than being reported at the end. Then the run re-executes the
original 400-episode configuration and compares. Every one of the fifteen
reproduced.

**Geometry at every position.** Measured at all 165 tests, not just the
anchor, which is what the ruling on the one-position geometry (`RT-40`)
asked for. The numbers are in the records. What the findings *say* about
them is wrong in one place, which is a separate finding below (`RT-57`).

### RT-53 — a number in the findings that the record does not carry

**Worth-noting. MEASURED.** The findings report the instrument check as
reproducing "to floating-point round-off — the largest difference on any
cell was below 1e-15". The record does not support that figure. The code
rounds the largest difference to six decimal places before writing it, so
every record says `0.0`, and the finest statement the record can make is
"below five parts in ten million".

The record does carry one detail the findings lose. On the pilot the
field recording an exact match across every layer is **false** while the
largest difference still prints as `0.0` — which means the pilot's worst
difference is greater than zero and smaller than the rounding could show.
On seeds 1 and 2 that same field is **true**, so those two are bit-exact.
So the three checkpoints did not behave identically: two reproduced
exactly and one reproduced to within summation order. The findings' table
prints "below 1e-15" against all three, which flattens that.

Nothing turns on it. The pre-stated tolerance was one episode in 400 and
the run used none of it. But "below 1e-15" is stated as a measurement and
it is an inference, and this review is required to mark that distinction.

### RT-54 — the two corrections are real corrections, and both check out

**Worth-noting, and it is credit. MEASURED.** The findings carry two
corrections to the committed method file rather than editing it, which is
what the ruling on not editing committed method files (`RT-43`) requires.
I verified both against the record.

The first says the method file was wrong to claim the classifier hits its
2,000-pass cap on every fold at 400 episodes. Correct: on the pilot's
twenty anchor folds the optimiser used between 158 and 933 passes and
capped on none of them; on seed 1 it capped on 9 of 20 and on seed 2 on
17 of 20. Those are exactly the numbers the correction gives.

The second says the six-and-a-half-hour estimate was low and the run took
10.8 hours. The three records give 2.93, 3.36 and 4.47 hours, which sum
to 10.76. Correct, and the explanation offered — that the slowest
checkpoint is the one whose fits converge least — holds: the cap rates
run 13.5, 22.3 and 73.6 per cent in the same order as the times.

A findings file that corrects its own method file twice, in public,
against numbers anyone can check, is behaving the way this protocol is
supposed to make things behave.

### RT-55 — a fifth of the draws the previous review asked for

**Worth-noting. MEASURED.** The previous review's first recommendation
was to run the fitted classifier "4,000 episodes, 1,000 draws, three
checkpoints". The run used **200** draws. The brief did not restate the
1,000, so this is not a departure from the brief, and the method file
declares the shortfall in advance, gives the cost arithmetic, and states
the consequence plainly: zero out of 200 establishes only about 2.58
standard deviations' worth of evidence, which is below the 3.38 the
family bar needs, so the margin has to supply the rest under a normal
approximation to a null measured with only 200 draws.

That disclosure is correct and I recomputed it: zero of 200 gives a
probability below one in 201, which is 2.578 standard deviations. I
record this in feasibility rather than burying it because it is the
reason the whole result rests on an approximation rather than on
counting, and because it is the cheapest thing to fix if any single cell
ever needs to be believed.

---

# 2. Satisfied by the wrong thing

*Every way FOUND NOWHERE could be returned by a model that does carry a
linear register-index signal at these positions.*

| # | finding | severity | label |
|---|---|---|---|
| RT-56 | the run's real reach is a signal in about one episode in eleven, not one in twenty-seven; the measure assumes a perfect read is possible and this read's own measured ceiling is 0.55 | serious | MEASURED |
| RT-57 | the claim that the state space is least concentrated at the control position is false on seed 1 and a photo-finish on seed 2, so the control sits in a different regime from the tested positions on one checkpoint and the same one on another | serious | MEASURED |
| RT-58 | leaving the 448 directions unscaled under a squared penalty charges a quiet direction the square of how quiet it is, so the read is worst-placed against precisely the hypothesis under test | serious | ARGUED from measured geometry |
| RT-59 | the bar treats 135 tests as independent when all three checkpoints read the same 4,000 episodes and five layers read one residual stream; the correction stays valid but buys less power than its arithmetic implies | serious | MEASURED |
| RT-60 | fold size and classifier capacity are cleared: at 4,000 episodes the fit is in a comfortable regime and I find no sign of capacity failure | worth-noting | MEASURED |
| RT-61 | the majority-class requirement, announced as a deliberate tightening, never binds on any test in the run | worth-noting | MEASURED |

### RT-56 — the run would have found a signal in one episode in eleven, not one in twenty-seven

**Serious. MEASURED for the arithmetic, ARGUED for the calibration.**
This is the most consequential thing in the review, because it is the
number the findings lead with when they say how much the null is worth.

The findings say: "the run would have found a register index legible in
about one episode in twenty-seven, and found none." The measure behind
that (`RT-37`) works like this: take the accuracy a test would need to
clear the bar, and ask what share of episodes would have to be **perfectly
legible**, with the rest at chance, to produce it. At a needed accuracy of
0.2774 against a chance rate of 0.25, that share is 3.65 per cent, which
is one episode in twenty-seven. I recomputed every figure in that table
and all of them are exactly right: 3.05 to 4.08 per cent on the pilot,
3.03 to 4.05 on seed 1, 3.22 to 4.03 on seed 2, and the 3.84, 3.86 and
3.91 at the previous sweep's bar. The arithmetic is not in question.

**The assumption inside it is.** "Perfectly legible" means the classifier
scores 1.0 on those episodes. This read does not score 1.0 on anything —
including at the one position in the whole run where the answer is
available and the control clears at more than thirty standard deviations.
There, it scores **0.539 to 0.567**. That is the only ceiling this run
ever measures, and it is a little over half.

Redo the arithmetic with the measured ceiling in place of the assumed
one, so that a legible share produces accuracy `0.25 + share × (ceiling −
0.25)`:

| checkpoint | ceiling measured at position 6 | share as the findings compute it | share against the measured ceiling |
|---|---|---|---|
| pilot | 0.5670 | 3.65% — one in 27 | **8.6%–8.8% — one in 11** |
| seed 1 | 0.5575 | 3.65% — one in 27 | **8.9%–9.0% — one in 11** |
| seed 2 | 0.5485 | 3.71% — one in 27 | **9.3%–9.4% — one in 11** |

**So the run overstates its own reach by about two and a half times.** It
can see a register index legible in roughly one episode in eleven. It
cannot see one legible in one episode in twenty.

Three things to be fair about. The calibration is ARGUED: position 6 is a
derivable target, not a guaranteed-present one, so 0.55 may be the
model's limit rather than the read's — and if the model represents the
index perfectly there, then 0.55 is genuinely the read's ceiling and the
correction is right. Either way it is the best-supported ceiling
available, and 1.0 is not supported by anything. Second, the correction
does not change the cell: one episode in eleven is still a real amount of
signal to have missed. Third, the findings did not invent this measure —
it came out of the previous review, where the same implicit ceiling of
1.0 sat unexamined. The correction belongs to both runs.

### RT-57 — the control does not sit where the findings say it sits

**Serious. MEASURED.** The findings write, under geometry:

> It is consistently lowest at position 6, the one place the answer is
> present — 0.8579 on the pilot at layer 5, against 0.9899 at the highest
> position.

The share of variation carried by the top ten of 448 directions, at
position 6 against the nine testable positions, from the records:

| checkpoint | position 6 | the nine testable positions | is position 6 lowest? |
|---|---|---|---|
| pilot | 0.8524 – 0.8651 | 0.9486 – 0.9907 | **yes, clearly** |
| seed 1 | 0.9791 – 0.9820 | 0.9430 – 0.9953 | **no** — four testable positions are lower |
| seed 2 | 0.8774 – 0.8815 | 0.8781 – 0.9806 | by 0.0007, a photo-finish |

On seed 1 the control position is the fourth *most* concentrated of the
eleven, above the other agent's revision value (0.9430), the model's own
revision value (0.9559), the query answer value (0.9565) and its second
assignment (0.9647). The claim is false there. The specific comparison
the findings quote — 0.8579 against 0.9899 — is a pilot-only, layer-5
comparison and it is accurate as far as it goes; the word doing the
damage is "consistently".

The same paragraph adds that "the stack's earlier figure of about 99 per
cent in ten directions holds at the other positions". Across the 135
testable tests the range is 0.878 to 0.9953, with per-checkpoint medians
of 0.974, 0.984 and **0.942**. Ninety-four per cent is not about
ninety-nine, and on seed 2 seven of the nine testable positions sit below
0.95.

**Why this is serious rather than pedantic.** The geometry is the whole
mechanism behind the quiet-direction problem (`RT-34`), and it is also
the only evidence available about whether the positive control tests the
read in the same regime as the tested positions. On the pilot it plainly
does not — the control lives in a far less concentrated space than
anywhere the question is actually asked, which makes a pass there weak
evidence about the nine. On seed 1 it plainly does, which makes the pass
there better evidence. That is a real and useful distinction between
checkpoints, it is sitting in the records, and the findings replace it
with a single claim that is true of one checkpoint in three.

### RT-58 — an unscaled fit charges a quiet direction the square of how quiet it is

**Serious. ARGUED, from the geometry measured in this run.** The method
file names this and declines to fix it, which is honest. It is still the
single most likely way a real signal would have been returned as FOUND
NOWHERE, so it belongs here in full.

The classifier is a logistic regression with the library's default
squared penalty at strength 1.0, on features left at their original
scale. The penalty is charged on the weight, not on the weight's effect.
A direction carrying a small share of the variation has a
correspondingly small typical value, so producing a given contribution to
the decision needs a proportionally larger weight — and a squared penalty
charges the **square** of that factor. With the top ten of 448 directions
carrying between 88 and 99.5 per cent of the variation depending on
position and checkpoint, the remaining 438 directions share what is left,
and a signal resident in one of them is pushed toward zero far harder
than the same signal in a loud one.

So the instrument is, by construction, worst-placed against exactly the
hypothesis the run exists to test: a self-index that is real, linear and
quiet. The method's defence is that the fitted read is nonetheless far
more sensitive than the difference-of-averages read it replaces, and that
is true and measured. But "more sensitive than the thing the ledger
called fatally insensitive" is a floor, not a ceiling, and the findings
say so.

The fix is cheap and it is a different instrument: standardise the
features, or fit in a whitened basis, and the quiet directions compete on
equal terms. That would break the comparison with the record and would
need its own anchor, which is precisely the trade the method chose to
avoid — reasonably, for a first run whose credibility rested on
reproducing fifteen recorded numbers. It should not be avoided twice. A
standardised refit at the nine positions costs the same eleven
processor-hours and would separate "not linearly present" from "not
reachable by this penalty".

### RT-59 — 135 tests, far fewer independent ones

**Serious. MEASURED for the dependence, ARGUED for what it costs.** The
family bar is computed as if there were 135 independent discovery tests.
They are strongly dependent, in two ways that are both visible in the
method and the code.

**The three checkpoints read the same episodes.** One content seed
(20260917), one call to the episode builder, 2,000 pairs giving 4,000
episodes, and all 4,000 kept on all three checkpoints — the records show
the same count everywhere. So the three checkpoints are three models
reading one sample, not three samples. Anything that is a property of
