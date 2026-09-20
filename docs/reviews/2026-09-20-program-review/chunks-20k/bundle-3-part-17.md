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
merged PR 4. Read in this order.

Method files (each committed before its run):
- `denoised-direction-method.md`
- `position-sweep-method.md`
- `powered-target-test-method.md`
- `powered-position-sweep-method.md`

Findings files:
- `denoised-direction-findings.md`
- `position-sweep-findings.md` (the sweep found invalid on all three
  checkpoints; the reason was the target)
- `powered-target-test-findings.md` (the anchor result, NOT CARRIED)
- `powered-position-sweep-findings.md` (CARRIED NOWHERE, the result under
  review)

Code the findings were produced by:
- `src/denoised_direction_a3.py`, `src/position_sweep_a3.py`,
  `src/powered_target_test_a3.py`, `src/powered_position_sweep_a3.py`,
  `src/probe_target_diagnostic_a3.py`, `src/marker_legibility_a3.py`

Records: the JSON outputs under `a3-gates/` named `powered_*`,
`probe_target_diagnostic_*` and `denoised_direction_*`.

Registered text the interpretation is read against: `amendment-a3.md` and
`pre-registration.md`.

Do not open: STATUS.md, the compute ledger, any chat transcript, any
uncommitted file, or `docs/`. Say at the top of the findings file what was
opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the method files pre-state or
   threshold (the family bar, the 1,000-draw null, the positive and negative
   controls, the anchor reproduction): can it be measured at all with the
   stated instrument, and can the control condition actually reach the
   stated threshold? Cite the committed record that shows so, or say that
   none exists. A "verified" or "measured" claim with no record behind it
   is a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way "carried nowhere" could be
   returned by a model that does carry own-agent identity linearly at these
   positions (a probe that cannot see it, a target still ill-posed, a null
   that is too wide, an exclusion of positions that removed the ones that
   matter).
3. **No verdict.** Every way the sweep could have failed to return a verdict
   and been read as one anyway.
4. **Over-reading.** What "the linear-read line is closed" will be read as
   claiming in STATUS.md, in the paper, and in public, beyond what was
   measured. Say whether the session's narrower statement above is the
   right wording for STATUS.md, and if not, write the sentence that is.

Label every finding MEASURED (you ran a check and report its output) or
ARGUED (reasoning a reader can dispute). Continue the ledger numbering from
RT-32. Plain language throughout. Lookup allowed and flagged. Do not soften
findings to be polite.

## Filing

Findings to `reviews/2026-09-19-linear-read-closure-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this review enters STATUS.md until John rules on it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-claude-worktree.md =====

# Outside review — the linear-read closure (Gate B, tier 1)

*Filed 2026-09-19 under the outside-review protocol, against the review
packet `2026-09-19-linear-read-closure-packet.md`. Verbatim on filing and
not edited afterwards. Nothing here is a ruling; rulings are John's and go
in the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read at the commit that merged pull request 4 (`eaff1d5`), in a fresh
worktree checked out at that commit. Exactly the packet's list and nothing
else:

- The four method files: the denoised-direction method
  (`denoised-direction-method.md`), the position-sweep method
  (`position-sweep-method.md`), the powered-target-test method
  (`powered-target-test-method.md`), the powered-position-sweep method
  (`powered-position-sweep-method.md`).
- The four findings files with the matching names ending
  `-findings.md`.
- The six code files named in the packet, under `src/`:
  `denoised_direction_a3.py`, `position_sweep_a3.py`,
  `powered_target_test_a3.py`, `powered_position_sweep_a3.py`,
  `probe_target_diagnostic_a3.py`, `marker_legibility_a3.py`.
- The fifteen records under `a3-gates/` whose names begin `powered_`,
  `probe_target_diagnostic_` or `denoised_direction_`.
- Git metadata only — commit dates, messages and the list of files each
  commit touched — used to check the "committed before the run" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the compute
ledger (`compute-ledger.md`), the `docs/` folder including the research
note the denoising idea came from, the registered texts
(`amendment-a3.md` and `pre-registration.md`), the red-team ledger
(`red_team_ledger.md`), any chat transcript, any uncommitted file, and the
model checkpoint files themselves.

Two consequences of that, stated so they are not mistaken for omissions.
**First**, the packet says the interpretation is read against the
registered texts, and those are on the do-not-open list, so I cannot check
the interpretation against them. Nothing below turns on registered text.
**Second**, I could not read the red-team ledger to see the last number
used, so I have numbered findings from **RT-33**, reading "continue from
RT-32" as meaning RT-32 is taken. If that is off by one, the numbers
renumber trivially.

No outside lookup was used. Every number below either comes from a
committed record or from a check I ran myself, and each is labelled.

**Verdict in one line.** The CARRIED NOWHERE result is sound, correctly
computed and honestly reported — I reproduced every published number from
the records. The sentence built on top of it is not. The stack's own
committed records contain a measurement showing that the read used
throughout the sweep is roughly half as accurate as an ordinary fitted
linear read on the same states, and that measurement appears in none of
the four findings files.

---

# 1. Feasibility

*For every quantity the method files pre-state or threshold: can it be
measured at all, can the control actually reach the threshold, and is
there a committed record behind it?*

| # | pre-stated quantity | can it be measured? | record behind it | severity |
|---|---|---|---|---|
| F1 | the family bar of 3.56 standard deviations | yes | recorded in all three sweep files; arithmetic reproduces | none |
| F2 | the per-test bar of 3.0 standard deviations, reported for continuity | yes | recorded per test | none |
| F3 | the 1,000-draw null | yes | every one of the 330 tests records 1,000 draws and a count | none |
| F4 | the positive control reaching the bar | yes, by a wide margin | +159, +21, +29 standard deviations, no draw beating it | none |
| F5 | the negative control | yes | 30 tests, −2.19 to +0.76, none clears | none |
| F6 | reproducing the earlier anchor result | yes | all 60 shared tests bit-identical | none |
| F7 | the scorer agreeing with the original | yes | differences of exactly 0.0, recorded in every file | none |
| F8 | checkpoints verified by checksum | yes | the three checksums in the records match the ones the method files fixed in advance | none |
