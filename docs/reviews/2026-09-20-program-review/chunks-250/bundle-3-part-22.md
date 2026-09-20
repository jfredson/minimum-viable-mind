arithmetic would have replaced the appeal with the measurement.

### RT-74 — what the registration requires before "not localized" or "absent"

**Serious. Carried from the previous review rather than new. MEASURED.**
The packet asks what the registration still requires. The answer is
unchanged and the findings state it correctly and without softening,
which is to their credit.

Amendment A3 section 3.2 lists four numbered steps and the fourth is a
requirement:

> **Convergence requirement**, inherited: L1 counts as localized only
> when probe and patching agree on a confound-controlled design;
> otherwise the outcome is *not testable (localization)*, as Experiment 1
> registered.

The fifth adds that "the two-method requirement is met by probe plus
patching". The second method is causal patching: take the candidate
subspace out of an episode where the model is one agent, put it into the
matched episode where it is another, and see whether the action follows
the patched identity.

**Causal patching has still never been run.** The previous review checked
all six code files it was given and found no intervention of any kind; I
have checked the one code file I was given and it is the same — every
capture in it is read-only, the model is loaded, evaluated under a
no-gradient context, and deleted before scoring begins. Nothing in this
run changes a model's computation and then looks at what the model does.

So three statements are available and the third is the registered one:

- **"Not localized"** — not available. The registered condition for
  localization is agreement between two methods, and only one has run.
- **"Absent"** — not available, and further from available than before.
  The pre-registration's procedure step 8 reads the pattern the other way
  round: "if the instruments cannot recover a center that is known to be
  there, Experiment 1's null was instrument failure." Ownership is known
  to be load-bearing on these models. A probe-only null against a centre
  known to be doing work is registered as evidence about the instruments.
- **"Not testable (localization)"** — this is the registered phrase for
  where the line now stands, and it is where it stands.

The findings say all of this, cite the two ledger rows that established
it (`RT-49`, `RT-50`), and list patching first among the open items as
the binding one. Nothing needs correcting. It is repeated here because
the packet asks for it and because it is the clause most likely to be
dropped when the paragraph is shortened for the status file.

### RT-75 — the rulings were honoured

**Worth-noting, and it is credit. MEASURED.** The previous review
produced nineteen ledger rows and John ruled on all of them. I checked
each ruling that bore on this run against the method, the code and the
findings, and found none ignored:

the sensitivity finding (`RT-33`) is not merely cited but measured
directly on one target at one position, which is more than was asked; the
quiet-direction mechanism (`RT-34`) is carried into the method as a
stated cost rather than argued away; the missing register-index control
(`RT-35`) is answered by stating in advance that there is none and what
that costs; the legibility gap (`RT-36`) is quoted and explicitly not
resolved, with the findings refusing to offer their own flat control as
an explanation; the smallest detectable signal (`RT-37`) is reported per
test; the unreported degeneracy hits (`RT-38`) are answered by reporting
that none fired; the shared fold splits (`RT-39`) are fixed with per-test
seeding and the fix is verified by the code's own self-test; the
one-position geometry (`RT-40`) is measured at all 165 tests; the
exhaustive cells (`RT-41`) report their sub-pattern; the negative control
(`RT-42`) is read one way only, in the findings' own words; the
committed-file rule (`RT-43`) is honoured by putting two corrections in
the findings rather than editing the method; and the registered limits
(`RT-49`, `RT-50`) are carried in full.

That is nineteen rulings and no drift. Given that the previous review's
central complaint was a caveat drifting to nothing across four successive
findings files, this is the thing most worth recording about the run.

### The sentence for the status file

The packet asks for it, so here it is. It replaces whatever the status
file currently says about the linear read, and it is written to be
quotable in pieces, because it will be.

> A fitted linear classifier, run at eleven positions and five layers on
> all three 30-million-parameter checkpoints, does not find the model's
> register index anywhere except at the token where its own marker is the
> input. The controls held everywhere: the register index reads at 34 to
> 54 standard deviations at that token on every checkpoint, and the
> negative control shows no leak at the position where the answer is not
> yet knowable. One test reached three standard deviations without
> reaching the family-adjusted bar of 3.38, at the other agent's revision
> value on seed 2; the same position is the highest testable position on
> all three checkpoints and in all fifteen of its tests, and it is
> recorded as an open item rather than a result. This closes the fitted
> read on the register index. It does not close the linear read: the
> registered target is the model's own marker word, and no fitted read
> has ever been run on it at these nine positions — only the
> difference-of-averages read, which this run measures as recovering five
> to nineteen times less than a fitted classifier on the same target at
> the same position. Neither "not localized" nor "absent" may be said of
> any of this: Amendment A3 section 3.2 requires probe and causal
> patching to agree before anything counts as localized, patching has
> never been run, and the pre-registration reads a probe-only null
> against a centre known to be load-bearing as instrument failure. The
> registered term for where this stands is *not testable (localization)*.

**If it has to be shorter**, the three clauses that must survive are: the
registered target has never been read this way at these positions; the
run would have found a signal legible in about one episode in eleven, not
one in twenty-seven; and causal patching has never run, so nothing here
is absence.

**One sentence the status file should not carry**, in any form: that the
run would have found a signal in one episode in twenty-seven. It is the
figure the findings lead with and it is too generous by about two and a
half times (`RT-56`).

---

# The kill case

*Required whether or not the interpretation should stand.*

The kill case is that this run answered the previous review's question
about the wrong target and then wrote its null as though it had answered
it about the right one. The ledger's fatal finding was that the sweep
used a read about half as sensitive as one already sitting in the
repository; the fix was to point the sensitive read at the nine positions
that matter, and the fix was carried out — beautifully, with an
instrument check locked at both ends, per-test seeding, geometry at every
position, pre-stated cells that were applied exactly as written, and two
public corrections to its own method file. Every number in it reproduces.
But the registered target is the model's own marker word, which this
stack's own previous review established and John accepted, and the
marker-word target was priced at seventy processor-hours and dropped
before the run began. So the instrument that was built to answer the
objection was aimed at the four-answer recoding, and at the nine
positions that matter the registered target has still only ever been read
by the instrument the ledger already called fatally insensitive — a gap
this very run re-measures and finds is not a factor of two but a factor
of five to nineteen. On top of that the null is softer than it reads: the
smallest signal the run could have caught is about one episode in eleven
rather than one in twenty-seven, because the measure assumes a perfect
read is possible and the only ceiling the run ever measures is 0.55; the
bar is set for 135 independent tests when all three checkpoints read the
same four thousand episodes; the fit leaves 448 directions unscaled under
a squared penalty that charges a quiet direction the square of how quiet
it is, which is precisely the hypothesis under test; and the one position
that looks like anything — positive in fifteen tests out of fifteen, at
the other agent's revision value — is set aside with a reason that
misdescribes what was measured, when the control that would settle it is
already registered as L2(a) and costs the same eleven processor-hours the
run just spent. None of that makes FOUND NOWHERE wrong. It makes it a
smaller result than the sentence it will be asked to support, and the
line should be retired, if at all, after two more cheap runs: the
marker-word target under this same fitted read, and the other-agent index
at these same eleven positions.

---

## What I would do next, in order

1. **Run the other-agent index at the eleven positions** (`RT-64`). Four
   answers, the same captured states, the same eleven processor-hours,
   one new target function. It is registered as matched control L2(a), it
   has never been run, and it decides whether the run's one interesting
   pattern is a self-index carried away from an act position or an
   exclusion artefact. Cheapest decisive measurement available.
2. **Run the marker-word target under the fitted read at the nine
   positions** (`RT-71`). Seventy processor-hours. Until this exists, no
   sentence about "the linear read" and the registered target can be
   written, and the line cannot honestly be retired.
3. **Refit standardised, at the nine positions, as a declared second
   instrument with its own anchor** (`RT-58`). Same cost as the run just
   done. It separates "not linearly present" from "not reachable under
   this penalty", which is the one thing the positive control cannot
   certify.
4. **Correct the sensitivity figure wherever it has been written**
   (`RT-56`). One episode in eleven, not one in twenty-seven, and say
   which ceiling the correction uses.
5. **Report consistency across layers and checkpoints, not only per-test
   clearance** (`RT-62`), in any future sweep of this shape. The analysis
   that found nothing had no way of seeing the one thing in its own data
   that looks like something.
6. **Causal patching** (`RT-74`). Already the binding open item and
   already on the 2026-10-04 control-battery decision. Nothing above
   substitutes for it.

## How the checks in this review were run

Every number above came from one of three places, and each is marked in
the text.

Read directly from the committed machine records under `a3-gates/`: all
165 tests on all three checkpoints — accuracies, null means, null
spreads, margins, draw counts, labels, majority-class rates, per-class
minimums, optimiser pass counts, degeneracy flags, geometry, and the
per-test detectable shares.

Recomputed by me from those records: the family bar arithmetic at 135,
270, 405, 45 and 9 tests; the evidence a zero-out-of-200 result can
establish; the detectable shares at both bars, which reproduce the
findings' table exactly; the recalibration of those shares against the
measured ceiling at position 6; the per-position means and sign counts
across layers and checkpoints; the spread of margins per checkpoint with
and without the other agent's revision value; the real-fit and null-fit
cap rates separately; and the mean, spread and sign balance of all 135
testable margins against what independent standard normal draws would
give.

Read from the code, not from its comments: the seeding function and its
self-test, the label logic and the order in which its conditions are
applied, the rounding of the margin before comparison, the one-layer
sufficiency of the control gate, the two-way lock on the anchor table,
and the absence of any intervention anywhere in the file.

I ran no model, loaded no checkpoint, and made no outside lookup.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-packet.md =====

# Review packet — the linear-read closure (Gate B, tier 1)

*Prepared 2026-09-19 (Pacific) under `docs/outside-review-protocol.md`,
ruled in force the same day. This is the first Gate B review under the
protocol: an interpretation that changes program direction, checked before
it enters STATUS.md's current-state section.*

## The interpretation under review

From the session that produced PR 4 (merged 2026-09-19):

> Combined with the anchor result, the linear-read line is closed on these
> checkpoints. But it is not evidence that these models have no self-index,
> and shouldn't be written up as though it were. Eleven positions out of a
> seventy-one-token episode, one statistic, linear, and a per-position read
> cannot see a distributed representation by construction. The honest
> statement is narrower and duller: a linear difference of averages, at the
> positions and layers we chose, does not find one. No registered result
> changes.

Headline as the session wrote it: "Powered eleven-position sweep returns
CARRIED NOWHERE on both arms: zero of 270 testable tests reach even 3 sd
(max +2.73) while positive controls hold at +159 sd and the negative control
shows no leak, closing the linear-read line."

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/`, at the commit that
