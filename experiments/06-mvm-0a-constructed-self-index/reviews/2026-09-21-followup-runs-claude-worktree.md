# Review — the two follow-up localization runs (Gate B, tier 1)

*Filed 2026-09-21 (Pacific) under `docs/outside-review-protocol.md`, to the
packet `reviews/2026-09-21-followup-runs-packet.md`. Reviewer: Claude, in a
worktree at commit `d038f07` on branch
`worktree-followup-runs-l2a-standardised`. Verbatim; not edited after filing.*

## What was opened

Only what the packet listed, and everything it listed:

- `reviews/2026-09-20-followup-runs-brief.md`
- `other-index-position-sweep-method.md`, `standardised-refit-method.md`
- `other-index-position-sweep-findings.md`, `standardised-refit-findings.md`
- `a3-gates/other_index_position_sweep_a3_*.json` (three checkpoint files and
  the summary), `a3-gates/standardised_position_sweep_a3_*.json` (same)
- `src/other_index_position_sweep_a3.py`,
  `src/standardised_position_sweep_a3.py`, `src/fitted_position_sweep_a3.py`
- `reviews/2026-09-20-fitted-read-claude-worktree.md`, the red-team ledger
  `red_team_ledger.md` (the block of rulings numbered RT-70 to RT-93),
  `fitted-position-sweep-findings.md` and its correction note
  `fitted-position-sweep-findings-CORRECTION-2026-09-20.md`
- `amendment-a3.md`, `pre-registration.md`,
  `separation-clause-requirements.md`

Two things I opened that the packet did not name, and why. **First**, the
version of the red-team ledger on `main`, through git rather than the working
tree — the packet tells me to continue the numbering from a specific item, and
I could not tell whether that number was free without looking. It was not; see
the stale-numbering finding below. It is the same listed file at a different
revision. **Second**, `git log` and `git worktree list`, to place the commits
the packet names. I opened no status file, nothing under `docs/`, no
transcript and no uncommitted file. I could not check the packet's phrase
"public path step 3" against its source, because that phrase does not appear
in the pre-registration and locating it would have meant opening `docs/`; the
pre-registration calls the same arm **Procedure step 8**, and that is the text
I reviewed against.

**No external lookup was used.** Every number below is computed in this
session from the committed record files and the committed source, or read from
the listed documents. The statistical formulas used (spreading an error rate
over a family of tests, the bound that zero hits in N draws places on a
probability, the expected largest of N draws) are standard and were evaluated
here rather than quoted.

Every finding is labelled **MEASURED** — checked against the records or the
code — or **ARGUED** — a reading that the records permit but do not compel.

**A note on the ledger numbering.** The packet says to continue from RT-117.
That instruction is stale: items RT-117, RT-118 and RT-119 already exist on
`main`, added by the ruling of 2026-09-20 on the program-level review and the
two outside objections (commit `d875321`). Numbering from RT-117 would collide
with three live items when this branch merges. **I have numbered from RT-120**
and recorded the departure as a finding.

---

## Part 1 — Feasibility

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-120 | Every requirement the brief set for both method files is met and each has a machine record behind it. Checked from the records and the source, not from the method files' description of themselves | worth-noting (credit) | MEASURED |
| RT-121 | The registered control's second half — "matched in probe accuracy" — was never a pre-stated gate. Only the rank match was measured before the run; the accuracy match was measured afterwards, at two different positions, with no tolerance and no stated consequence for failing | worth-noting | MEASURED |
| RT-122 | The packet's instruction to continue the ledger from RT-117 is stale. Three items at and above that number already exist on the main line | worth-noting | MEASURED |
| RT-123 | The standardised refit imports the bar of 3.38 as a fixed number instead of recomputing it from the tests actually run, which is the safeguard the other run's method file names and implements | worth-noting | MEASURED |
| RT-124 | The other-agent run's negative control is scored on half the episodes of the tests it guards, so its null is about 36% wider and it cannot catch a leak of the size those tests would report | worth-noting | MEASURED |

### RT-120 — the brief's requirements are met, with records (credit). MEASURED

The brief set eight requirements. I checked each against the committed code
and the committed records rather than against the method files' account of
themselves. All eight hold:

- **Seeding is per test.** `test_seed` in `src/fitted_position_sweep_a3.py`
  digests the whole test identity — checkpoint, arm, position and layer — so
  no two tests share a fold split or a set of shuffled draws, and the
  self-test asserts that the digests are distinct, stable, and differ by
  checkpoint.
- **The bar is a number**, 3.38, and the arithmetic behind it is right. The
  code spreads a 5% family-wise error over 135 tests one-sidedly, which needs
  3.3740, and applies it rounded up. I recomputed both values the code's
  self-test checks: 3.3740 at 135 tests and 3.3415 at 120, which round up to
  3.38 and 3.35 as claimed.
- **A positive control exists in both runs**, and both hold on all three
  checkpoints. In the other-agent run it is agent B's marker token
  (+32.93 to +52.81 standard deviations); in the standardised refit it is the
  model's own marker token (+32.61 to +40.41). No checkpoint is void.
- **Cells and the degeneracy rule were pre-stated** and are applied as
  written. The three degeneracy hits in the standardised refit are in the
  records exactly where the findings say they are.
- **Anchor reproduction happened before any sweep number.** Both runs
  re-ran the recorded fifteen-cell configuration and matched it; the records
  give the largest difference as 0.0 on all three checkpoints for the
  standardised refit, and the other-agent run's pilot difference is recorded
  as non-exact but below the rounding floor, which its findings describe
  correctly and more precisely than the summary file does.
- **Standardisation is computed on training rows only.** The `standardise`
  function takes the mean and spread of the training fold and applies them to
  both sides; the held-out rows contribute to neither. This is the one
  requirement most easily got wrong, and it is right.
- **The regularisation strength was not chosen by looking at sweep
  results.** It stays at the library default of 1.0, and the method file
  argues in advance — correctly — that there is nowhere honest to tune it.
- **Geometry is reported at every position**, per layer, per checkpoint.

The detectable-signal figure is calibrated against each read's own measured
ceiling and not against a perfect score, as the correction note of 2026-09-20
requires. Both runs land at about one episode in eleven, which matches the
corrected figure for the run they follow.

The brief said a requirement claimed met with no record is fatal. There are
none.

### RT-121 — the registered control's accuracy match was checked after the fact. MEASURED

Amendment A3 section 3.1 registers the other-index control as "the same
localization run for a named non-self agent … **matched in rank and probe
accuracy**". The method file measures and pre-states only the rank match: the
four class shares agree to four decimal places (0.2582, 0.2410, 0.2547,
0.2460), so the free accuracy a classifier gets is identical. That half is
done properly and before the run.

The accuracy half appears only in the findings, after the numbers existed. It
is a real measurement and it does show a close match — the model's own index
reads 0.5390 to 0.5670 where its own marker is the input token, and agent B's
index reads 0.5310 to 0.5665 where agent B's marker is the input token — but
three things follow from its being retrospective. It compares **two different
positions**, one per target, which is the only comparison available but is not
the like-for-like the registered phrase suggests. It had **no pre-stated
tolerance**, so no width of gap would have counted as a failure. And nothing
said what would happen if it failed, whereas every other gate in the run
carries a stated consequence.

This is a departure from the registered definition of the control, not a
failure of it. The run is still the first execution of that control and the
match is close. It should be recorded as "rank matched by design, accuracy
matched as observed" rather than as the registered control run to
specification.

### RT-122 — the packet's ledger numbering is stale. MEASURED

The packet says "Continue the ledger numbering from RT-117." On the main line
the ledger already carries RT-117 (the recommendation from the program-level
review of 2026-09-20), and RT-118 and RT-119 (the two outside objections ruled
the same day). On this branch the ledger stops at RT-93, which is why the
packet's author saw a gap. Numbering this review from RT-117 would have
produced three colliding items on merge. I have numbered from RT-120.

### RT-123 — the standardised refit imports the bar rather than recomputing it. MEASURED

The other-agent run computes its bar from the family it actually runs:
`FAMILY_SD_EXACT, FAMILY_SD_BAR = family_bar(FAMILY_SIZE)`, where the family
size is derived from the list of testable positions. Its method file presents
this as a safeguard — "the code computes this from the number of tests
actually run rather than carrying a constant".

The standardised refit does not do this. It imports `FAMILY_SD_BAR` from the
run it refits as a fixed 3.38. Nothing is wrong with the value, because the
family really is 135 tests. But the safeguard is absent in the run where a
cell actually crossed the bar, which is the run where it would have mattered
had the position list ever changed. Cheap to fix and worth fixing before this
instrument is used again.

### RT-124 — the restricted negative control is scored on half the sample. MEASURED

The other-agent run's negative control is the model's first assignment value
restricted to the episodes where agent B's marker has not yet appeared — about
2,000 of the 4,000. That restriction is the right design decision and the
method file defends it well.

Its cost is not stated. At 2,000 rows the null spread is 0.0112 to 0.0114
against 0.0083 at the testable positions, about 36% wider. So the accuracy the
negative control would need to signal a leak is roughly 0.288, against 0.2773
at the tests it guards. **A leak large enough to produce a clearance at a
testable position would not necessarily register at the negative control.**
The control is not wrong; it is about a third less sensitive than the thing it
is protecting, and the findings present it as though the two were on the same
footing.

---

## Part 2 — Satisfied by the wrong thing

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-125 | The other-agent run tests whether agent B's rank is decodable as a four-way answer. A purely relational encoding — "the rank at this token is not mine" — would produce the own-index pattern and this exact null together. That route is open and the run does not close it | serious | ARGUED |
| RT-126 | The other-agent run's conclusion is far better supported than the findings argue. Sized against the own-index lift, the confound would need agent B's rank to read at +8.3 to +12.7 standard deviations; it reads +1.00 to +1.73, and the run demonstrably detects an effect of exactly that size elsewhere | worth-noting (credit) | MEASURED |
| RT-127 | The findings lead with the wrong comparison. The +52.81 positive control is not the number that carries the argument; the exclusion diagnostic at +6.34 to +8.22 is, and it is the one measurement in the run at the right effect size | serious | MEASURED |
| RT-128 | The one clearing cell clears by 1.94 episodes in 4,000. A one-standard-error change in the null spread it is divided by — 5.0% of that spread, from the same 200 draws — puts it at +3.27, below the bar. The clearance is inside the estimation noise of its own denominator | fatal to reporting it as a clearance | MEASURED |
| RT-129 | The standardised refit's negative control also returned zero of 200 draws beating it, and also beat the majority-class rate, at a position where the answer cannot be known. Two of the three conditions for FOUND were met where nothing can be there. The findings cite "zero of 200" as corroboration for the clearing cell and never report that the negative control produced it too | serious | MEASURED |
| RT-130 | The own index has now been swept over the same 135 cells twice. Against the 270 tests actually run the bar is 3.5603, applied 3.57, and +3.43 does not clear it | serious | MEASURED |
| RT-131 | "Exactly one thing changes" is false of the sweep. The fold splits and the 200 null draws also differ between the two reads, because the arm name feeds the seed. The move from +1.34 to +3.43 at that cell confounds the scaling with a different fold split and a different null sample | serious | MEASURED |
| RT-132 | At the position in question on the third checkpoint, the two estimators disagree by −0.87 to +2.09 standard deviations across five layers on identical states. A quantity that moves that far under a change of estimator cannot carry a bar set at 3.38 | worth-noting | MEASURED |
| RT-133 | Both new runs' nulls are well behaved across the 135 testable tests, matching the earlier run's record. This is a point in both runs' favour that neither claims | worth-noting (credit) | MEASURED |
| RT-134 | Two separate signs say the standardised instrument is the less well behaved of the two — three degeneracy hits against none, and a negative control running to +2.65 against +0.08. Both are reported; they are never joined, and together they bear directly on the one cell that cleared | serious | MEASURED |

### RT-125 — the relational route is open. ARGUED

The confound under test says: the state at the other agent's revision value
represents who is speaking; an agent is never its own other; so one rank of
four is ruled out and the attainable accuracy on the model's own index rises
from 0.25 towards 0.333, with no self-representation involved.

The run's logic is that if the model can rule out agent B's rank, then agent
B's rank must be decodable, so pointing the same read at agent B's rank tests
the confound directly. That is sound for an **absolute** encoding — a
representation of "agent B's marker is the third of the four".

It is not sound for a **relational** one. A state that carries "the value
being read here belongs to someone other than me", attached to the current
token, supports the exclusion without ever representing agent B's rank as a
four-way quantity. A four-way linear decoder aimed at agent B's rank would
read nothing from such a state, while a decoder aimed at the model's own rank
would gain exactly the exclusion the confound describes. The observed pattern
— own index elevated at that token, agent B's index flat — is what a purely
relational encoding predicts.

I cannot tell from the records whether that is what is happening, and neither
can the run. This is the one route by which the run could return FOUND NOWHERE
with the confound still live, and the findings do not name it. The cheap check
is a two-answer target at that position — "is the value at this token mine or
not" — which is a different target function on the same captured states and
the same eleven-hour shape as the run just done.

### RT-126 — the conclusion is better supported than the argument given (credit). MEASURED

The findings argue their case qualitatively: agent B's index reads +1.00,
+1.40 and +1.73 at the position in question, against an instrument that finds
the same target at +52.81 where agent B's marker is the input token.

The quantitative version is much stronger, and it is available from the
records. The confound has to explain a specific amount of lift. The own index
at that position reads at best 0.2688, 0.2700 and 0.2770 on the three
checkpoints, against chance at 0.25 and a full exclusion confound at 0.3333 —
so the observed lift is 23%, 24% and 32% of what a full confound would give.
For the confound to explain it, agent B's rank would have to be legible in
that share of episodes, which against each read's own measured ceiling means
an accuracy of 0.3214, 0.3244 and 0.3482 — that is, margins of **+8.8, +8.3
and +12.7 standard deviations**.

Measured: 0.2580, 0.2625 and 0.2632, at **+1.00, +1.40 and +1.73**.

And the run proves it can see an effect of exactly that size. At the model's
own marker token, where the exclusion arithmetic is directly available, agent
B's index reads 0.3030, 0.3205 and 0.3010 at **+7.67, +8.22 and +6.34**, every
cell FOUND. That is the same lift the confound would need, detected
comfortably, by the same instrument, on the same states, in the same run.

**The exclusion confound is excluded by something between seven and eleven
standard deviations of margin, with a demonstrated positive detection at the
required effect size.** That is a much better result than "found nowhere", and
it is the strongest thing either run produced. It should be what STATUS.md
says, and it is not what the findings lead with.

### RT-127 — the wrong number is doing the work. MEASURED

The +52.81 figure at agent B's marker token corresponds to an accuracy of
0.5553 — a lift of about 0.30 over chance. The effect the run needs to rule
out is a lift of about 0.03 to 0.07. A control ten times larger than the
effect under test certifies very little about sensitivity at that effect size,
which the method file itself says in advance ("clearing it does not certify
sensitivity anywhere else … a pass is necessary and not sufficient") and which
the findings then set aside when they reach for the number.

The exclusion diagnostic is the right control and the run already has it: an
effect of the exact size in question, detected at +6.34 to +8.22. The findings
do report it, in its own section, and correctly call it the place where the
mechanism "can be watched directly". They then do not use it where the
argument is made.

This is the same shape as the earlier ruling on the identical-power paragraph
(the ledger's item on the uncorrected power comparison, `RT-91`): the
conclusion is right and the reasoning offered for it is not. One paragraph of
arithmetic replaces an appeal to an irrelevant control with the measurement
that settles it.

### RT-128 — the clearing cell clears by two episodes. MEASURED

The record for the cell:

| quantity | value |
|---|---|
| accuracy | 0.2778 |
| null average | 0.2496 |
| null spread | 0.0082 |
| margin | +3.43 standard deviations |
| accuracy needed at the 3.38 bar | 0.277316 |
| **excess over the bar** | **0.000484, which is 1.94 episodes in 4,000** |

One episode is worth 0.0305 standard deviations at this position. **The cell
clears the bar by about two correct held-out predictions out of four
thousand.**

Worse, the denominator is itself estimated from the same 200 draws. The
standard error of a spread estimated from 200 draws is 5.0% of it, or 0.000411
here. Moving the null spread by one standard error in either direction:

| null spread | margin | result |
|---|---|---|
| 0.007789 (−1 standard error) | +3.62 | clears |
| 0.008200 (as measured) | +3.44 | clears |
| 0.008611 (+1 standard error) | +3.27 | **does not clear** |

**The bar-crossing sits inside the estimation noise of the quantity it is
divided by.** This is not the same point as the findings' "200 draws cannot
certify it", which is about the *count* of draws establishing only about 2.58
standard deviations. That point is correct and is carried from the earlier
ruling on draw counts (`RT-73`). The point here is about the *spread*: even
granting the normal approximation entirely, the margin is not determined to
better than about ±0.18 standard deviations by 200 draws, and the bar sits
0.05 away.

The findings say the cell is "suggestive and not settled" and say so more than
once, which is honest. They do not say it clears by two episodes, and they do
not say that a one-standard-error wobble in the null spread reverses it.
Anyone reading "+3.43 against a 3.38 bar, zero of 200 draws beating it" will
take it for a clearance with a small margin. It is a coin-flip against the
bar. **Fatal to reporting it as a clearance**; the number and its fragility
must travel together or neither should travel.

### RT-129 — the negative control also returned zero of 200. MEASURED

Across the standardised refit, exactly three tests outside the positive
control returned zero of 200 shuffled draws meeting or beating the real
accuracy:

| checkpoint | position | layer | margin | what is there |
|---|---|---|---|---|
| seed 2 | the other agent's revision value | 3 | +3.43 | the clearing cell |
| seed 2 | the other agent's revision value | 4 | +2.47 | same position |
| seed 1 | the model's first assignment value | 8 | +2.65 | **the negative control** |

The third is the negative control — the position chosen precisely because the
model's own marker has not appeared and the answer is not knowable by any
route. At that position the instrument produced accuracy 0.2688, above the
majority-class rate of 0.2582, with **zero of 200 draws beating it**. Two of
the three conditions for FOUND were satisfied where, by construction, nothing
can be found. It failed only the margin.

The findings report the +2.65 and call it "a caution about how well calibrated
this second instrument is", which is the right instinct. They do not report
that it came with zero of 200 draws. That omission matters because "zero of
200 shuffled draws met or beat it" is offered twice as part of what makes the
clearing cell notable — in the headline box and in the three-lines summary.
**The same criterion was met at a position where the answer cannot exist.**
Its evidential weight in this run is close to zero, and the findings' own
records show why.

For fairness: one negative-control test at +2.65 out of fifteen is not by
itself proof of a broken null. Under a well-behaved null the largest of
fifteen draws exceeds 2.65 about 5.9% of the time, and the expected largest of
fifteen is +1.97. So this is an unremarkable-to-mildly-surprising event taken
alone. The point is not that the null is broken; it is that the corroborating
criterion the findings lean on does not discriminate.

### RT-130 — the family is 270, not 135. MEASURED

The bar of 3.38 spreads a 5% family-wise error over 135 tests. That was the
right bar for the unscaled sweep. It is not the right bar now.

The model's own register index has now been swept at the **same nine testable
positions, the same five layers, the same three checkpoints, the same 4,000
episodes** twice: once unscaled and once standardised. Both are discovery
sweeps looking for the same thing in the same states. The family actually run
against that question is 270 tests.

| family | exact bar | applied | does +3.43 clear? |
|---|---|---|---|
| 135 tests (one sweep) | 3.3740 | 3.38 | yes, by 0.05 |
| 270 tests (both sweeps) | 3.5603 | 3.57 | **no, by 0.14** |

The probability that at least one of 270 independent tests reaches +3.43 or
beyond is 0.078. The findings quote 5% for 135 tests and call the cell "the
outcome the bar was designed to permit by chance about one time in twenty".
Against the tests actually run it is closer to one time in thirteen.

**The honest complication**, which I record because it cuts the other way. The
ledger has already accepted that the 135 tests are not independent (`RT-77`,
the ruling on treating correlated tests as independent): three checkpoints
read one draw of episodes and five layers read one running state, and at 45
effective tests the bar would be 3.06, at 9 effective tests 2.54. That ruling
pushes the bar down; this finding pushes it up. **The two do not cancel
cleanly and I cannot say where the net lands**, because the correlation
between the unscaled and standardised reads of the same cell has never been
measured and is the missing quantity. What can be said is that 3.38 was
computed for a family that no longer describes what has been run, and that a
cell clearing it by 0.05 cannot survive the uncertainty in which direction the
correction goes.

### RT-131 — the fold splits and the null draws also changed. MEASURED

The standardised refit's central claim about itself is that exactly one thing
changed. Its Part C self-test supports a version of that: with the
standardising step replaced by a do-nothing transform, the standardised code
path reproduces the unscaled path's accuracies and optimiser pass counts
exactly. That proves the two code paths are one path.

It does not make the sweep comparison a paired one. The per-test seed is a
digest of `checkpoint | arm | position | layer`, and the arm string differs:
`register_index` in the unscaled run, `register_index_standardised` in the
refit. **So every test in the standardised sweep uses a different fold split
and a different set of 200 shuffled draws from its unscaled counterpart.**

The consequence lands exactly on the cell that matters. At the third
checkpoint, the other agent's revision value, layer 3, the unscaled read gives
+1.34 and the standardised read gives +3.43. The findings attribute that move
to the scaling. It is the sum of three changes: the scaling, a different
train/held-out split, and a different null sample. Given that one episode is
worth 0.03 standard deviations here and the null spread is itself uncertain to
5%, the fold split alone can account for a meaningful part of a 2.09-standard-
deviation move.

The fix is one line and costs nothing: run the standardised sweep with the
unscaled run's arm string in the seed digest, so the two reads share fold
splits and null draws and the difference between them is the estimator alone.
Until that is done, the refit is not a controlled comparison with the run it
refits, whatever the self-test shows about the code path.

### RT-132 — the two estimators disagree by two standard deviations on identical states. MEASURED

At the third checkpoint, the other agent's revision value, all five layers,
unscaled against standardised:

| layer | unscaled | standardised | difference |
|---|---|---|---|
| 3 | +1.34 | **+3.43** | +2.09 |
| 4 | +3.34 | +2.47 | −0.87 |
| 5 | +1.75 | +1.93 | +0.18 |
| 7 | +2.54 | +2.18 | −0.36 |
| 8 | +2.70 | +2.33 | −0.37 |

These are the same states, the same episodes, the same target and the same
checkpoint. The measurement moves by up to 2.09 standard deviations under a
change of estimator (and of fold split, per the previous finding). The
findings note the layer shift — "the position is consistent across reads; the
layer is not" — and treat it as one caveat among five.

It is more than that. **The scale the bar is denominated in is not stable to
better than about two standard deviations at this position under changes that
are supposed to be neutral.** A bar of 3.38 cannot adjudicate a quantity with
that much play in it. Whatever is happening at this position across layers, it
is not something a per-cell threshold can resolve.

### RT-133 — both nulls are well behaved (credit). MEASURED

The earlier ruling on the paired design (`RT-88`) recorded, for the unscaled
run, that the 135 testable margins have mean +0.016, spread 0.993 and 70 of
135 negative — what independent standard normal draws would give. I ran the
same check on both new runs:

| run | mean | spread | negative | largest |
|---|---|---|---|---|
| unscaled own index (recorded, `RT-88`) | +0.016 | 0.993 | 70 of 135 | +3.34 |
| other-agent index (this review) | +0.147 | 0.953 | 57 of 135 | +2.79 |
| standardised own index (this review) | −0.052 | 1.047 | 79 of 135 | +3.43 |

Both new nulls behave. The standardised refit's testable margins are almost
exactly standard normal, which is a real point in the run's favour and one it
does not claim. It also frames the clearing cell correctly: **+3.43 is the
single largest of 135 well-behaved draws, where the expected largest is
+2.77.** Above expectation, and not far above it.

The other-agent run carries a mild positive offset of +0.147 across the sweep.
The findings notice this qualitatively ("agent B's index carries a mild
positive offset across this sweep generally") and use it correctly, to argue
that the +0.46 mean at the position in question is below that run's own
baseline. Quantified, the offset is small and it makes the run's null
*conservative* for its own conclusion: the sweep is slightly biased towards
finding agent B's index, and still finds it nowhere.

### RT-134 — two signs of a worse-behaved instrument, never joined. MEASURED

The standardised refit reports two departures from the run it refits, in
separate sections:

- **Three degeneracy hits against none.** All three are the classifier landing
  exactly on the majority-class rate. The findings state plainly that
  "standardising makes the classifier collapse onto naming the commonest
  answer more often", and call it "a real property of the second instrument".
- **A negative control running to +2.65 against +0.08.** At a position where
  the answer is not knowable, the standardised read produced a margin more
  than thirty times the unscaled read's, with zero of 200 draws beating it
  (see the finding above).

Each is reported honestly. Neither is connected to the other, and neither is
connected to the clearing cell. Together they say the same thing: **the second
instrument is noisier and less well calibrated at the low-signal end than the
first.** That is precisely the end of the range the clearing cell sits in, at
an accuracy of 0.2778 against a majority-class rate of 0.2582.

The findings' summary of the run is "standardising did not broadly raise
sensitivity … but made every fit converge". The convergence gain is real and
well evidenced — not one fit in 165 tests hit the pass cap, against 13.5%,
22.3% and 73.6% unscaled, which I verified from the records (0 of 44,220 fits
per checkpoint). But the full description is: it converged everywhere, and it
became less well behaved at the bottom of its range, and the one cell it moved
across the bar is at the bottom of its range.

---

## Part 3 — No verdict

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-135 | "Three independent lines now point at that one position" is not supportable. Two of the three are the same sample read twice with two estimators, which the ledger has already ruled is one observation; the third is a null on a different target, which removes an alternative and is not evidence for the position | fatal to that sentence | MEASURED |
| RT-136 | Both runs applied their pre-stated cells correctly and put FOUND NOWHERE first, which is the design working. But the closing section of the standardised findings builds an argument that functions as a result while the cell says there is none, and the two point in different directions | serious | MEASURED |
| RT-137 | The runs answered the confound objection decisively and the quiet-direction objection only partly. A null at one untuned strength on a re-scaled parameterisation narrows "the penalty was hiding it"; "a much weaker story" claims more than one strength can show | serious | ARGUED |
| RT-138 | The registered localization target is the model's own marker word. Both runs read the register index instead. The one clearing cell is therefore a clearing cell on a target the registration does not name, and the mirror of the earlier fatal ruling applies to a positive as much as to a null | serious | MEASURED |

### RT-135 — the three lines are not three, and not independent. MEASURED

The interpretation under review says: "Three independent lines now point at
that one position, and none is strong enough alone." The three are given as
the unscaled own-index read ranking the position first of nine; the
other-agent index being absent there; and the standardised read clearing the
bar there.

**Lines one and three are one observation.** They are the same 4,000 episodes
at the same content seed, the same three checkpoints, the same five layers,
the same nine positions, the same captured states and the same target. The
only difference is the estimator — and per the fold-split finding above, also
the fold split and the null sample, which makes them less comparable, not more
independent. The ledger has already ruled on exactly this move: the item on
pairing two nulls (`RT-90`) holds that "both reads are now empty" is "one
sample read twice". The same standard applies when the two reads agree in the
positive direction. Two estimators on one sample are one observation with an
uncertainty attached, and the earlier finding that the position ranks first of
nine by mean margin is a statement about the *same numbers* the standardised
read then re-measured.

**Line two is not evidence for the position.** The other-agent null removes a
proposed alternative explanation. Removing an alternative raises what is left
only in proportion to how much of the space that alternative occupied, and it
adds no new positive evidence at the position. It is also, on its own terms, a
*null* — and this program's registered reading of a probe-only null is
instrument failure rather than absence, a standard the runs apply rigorously
to their own cells and not to this inference.

What can honestly be said: **one sub-bar pattern, measured twice with two
estimators on one sample, with one proposed explanation for it excluded.**
That is a reason to look again at that position. It is not three lines and
nothing about it is independent.

### RT-136 — the cell and the narrative point different ways. MEASURED

Credit first, because it is the larger part. Both findings files lead with the
pre-stated cell, both say FOUND NOWHERE before anything else, both name the
sub-pattern as the method files required, and both report every position
regardless of which cell fired. The exhaustive-cells cost — that "found on the
pilot only" lands in FOUND NOWHERE despite not being nothing — was disclosed
in advance and honoured. The standardised findings state in their own headline
section that "the pilot found nothing, so the cell is FOUND NOWHERE whatever
else happened". That is the machinery working as designed, and it is the
second review in a row where the pre-stated analysis was applied without
drift.

The difficulty is the closing section, "What this means, read together with
the first follow-up run". It assembles the three lines, states that they point
at one position, and then lists five reasons it is not a finding. Every one of
the five reasons is accurate. But the structure — build the case, then
qualify — leaves a reader with a case, and the qualifications are the kind
that get compressed out when a paragraph is shortened for a status file. The
previous review's central complaint was a caveat drifting to nothing across
four successive findings files (the ruling recorded at `RT-93`). This is the
shape that drift starts in.

The cell says nothing was found. The narrative says three lines converge. Both
are in the same document and STATUS.md will have to choose. It should choose
the cell.

### RT-137 — one strength is not the whole objection. ARGUED

The two objections the runs were sent to answer:

**The confound at the other agent's revision value (`RT-82`) is answered, and
decisively** — see the credit finding above. This is a clean discharge of a
ledger item and the run deserves the credit.

**The quiet-direction objection (`RT-76`) is answered in part.** The objection
is that leaving 448 directions unscaled under a squared penalty charges a
quiet direction the square of how quiet it is, so the instrument was worst
placed against a signal that is real, linear and quiet. Standardising removes
that specific bias, and the method file's argument for leaving the strength at
1.0 is right: there is nowhere honest to tune it, and tuning would change two
things at once.

But the consequence is that the refit tests one point in a two-dimensional
space — scaling, and strength — and the two interact. On unit-spread features
a penalty of 1.0 means something different from what it meant on raw features;
the method file says this, correctly, as the reason the fix works. The same
fact means a null at 1.0 on standardised features does not cover the range of
effective strengths the unscaled read spanned. The findings' claim that "the
signal was there all along but the unscaled penalty could not reach it" is
"now a much weaker story" is stronger than one untuned strength supports. The
method file's own caveat — "a null here is a null at this strength" — is the
correct statement and the findings should not have gone past it.

### RT-138 — the registered target was not read. MEASURED

The ledger's ruling on the registered target (`RT-89`) was called fatal to a
sentence in the previous findings: the registered localization target under
Amendment A3 section 3.2 is the model's **own marker word**, and the fitted
sweep read the **register index** — the rank of that marker among the
episode's four — instead, because the marker-word target was priced at about
seventy processor-hours against eleven and dropped before the run, openly.

Neither follow-up run changes this. The standardised refit reads the register
index. The other-agent run reads the rank of agent B's marker. **The registered
target has still never been read at the nine testable positions by a fitted
classifier.**

The earlier ruling applied this to a null: "no linear read finds own-agent
identity at the nine testable positions" was not supportable. The mirror
applies with equal force to a positive. **A cell clearing the bar on the
register index is not a cell clearing the bar on the registered target.** The
register index is a four-answer summary of the marker word; a signal in one
is suggestive about the other and is not the other. Any sentence that enters
STATUS.md about the clearing cell must name the target it was measured on, or
it will read as the registered target having been found, which it has not
been.

---

## Part 4 — Over-reading

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-139 | "The own-index pattern is now unexplained, not explained away" is half supportable. "Not explained away" is right and well evidenced. "Unexplained" presumes something requiring explanation; the pattern is sub-bar and a sub-bar pattern in a family of 135 needs no explanation yet | serious | ARGUED |
| RT-140 | The targeted rerun the findings call "the cheapest decisive move available" is mis-priced by roughly an order of magnitude. To do what the findings say it must do — certify by counting rather than by a normal approximation — needs about 8,100 draws, which is about 150 processor-hours for one instrument and 300 for both | serious | MEASURED |
| RT-141 | The registered blind arm should run before any further work on this position, and not only for efficiency: a published, targeted rerun that names one position as the place to look is an input to a pipeline the registration requires to receive the location withheld | serious | ARGUED |
| RT-142 | The STATUS.md paragraph, as it can honestly be written | — | — |

### RT-139 — "unexplained, not explained away". ARGUED

**"Not explained away" is supportable**, and more strongly than the findings
argue. The confound proposed in the ledger's item on the exclusion arithmetic
(`RT-82`) has been tested with a registered control and excluded by seven to
eleven standard deviations of margin, with a demonstrated detection at the
required effect size. That is a real result and it should be recorded as one.

**"Unexplained" is not supportable as written**, because it presumes there is
something that requires an explanation. What exists at that position is a
sub-bar pattern: under the unscaled read the position was positive in fifteen
tests of fifteen and reached MARGINAL once, and nothing there was ever FOUND.
Fifteen of fifteen positive is a genuine consistency observation — it is what
the earlier ruling on cross-layer consistency (`RT-80`) accepted, while
recording that the three checkpoints share episodes and the five layers are
correlated, making "fifteen of fifteen" nearer three observations than
fifteen. A pattern of that strength in a family of 135 tests is inside what
chance produces. It does not need a reason, and offering one and then
withdrawing it does not create a debt.

The accurate sentence is narrower and stands up: **a proposed explanation for
a sub-bar pattern was tested with a registered control and excluded; the
pattern remains sub-bar.** Saying the pattern is "now unexplained" gives it a
standing it has not earned, and "it is the one thing in this line that has
survived two attempts to dismiss it" — the phrasing in the open items —
converts the failure of two explanations into support for the thing being
explained. It is not. A pattern that needs no explanation cannot gain credit
from explanations failing.

### RT-140 — the recommended next move is mis-priced. MEASURED

The findings recommend "a targeted rerun at that one position with far more
draws" and call it "the cheapest decisive move available", specifying "far
more than 200 draws — enough that the count alone can certify a family-safe
clearance rather than leaning on a normal approximation".

That specification has a price, and it is not small. Certifying by counting
means the count alone must establish the per-test error rate the family bar
needs, which is 0.05 divided by 135, or 3.70 in ten thousand. Zero hits in N
draws bounds a probability at about 3/N, so N must be about **8,100 draws**.

From the records, the standardised run's 165 tests took 41.0 processor-hours
of fitting, a mean of 895 seconds per test, and each test is 804 fits (four
folds times one real fit plus 200 draws) — 1.114 seconds per fit.

| draws per test | per test | one position, 5 layers × 3 checkpoints | both instruments |
|---|---|---|---|
| 200 (as run) | 0.25 h | 3.7 h | 7.5 h |
| 1,000 | 1.24 h | 18.6 h | 37.2 h |
| 5,000 | 6.19 h | 92.8 h | 185.6 h |
| **8,100 (certifies by counting)** | **10.0 h** | **150.3 h** | **300.7 h** |

Even 5,000 draws does not certify by counting — zero of 5,000 bounds the
probability at 6 in ten thousand, about 3.24 standard deviations, still below
3.38. So the run as the findings specify it is a 150-to-300 processor-hour
job, against the 11-hour runs it follows, and against the "cheapest decisive
move" framing. It is still $0 in money, being local inference on existing
checkpoints, but it is not cheap in the currency this program has been
counting in, and the open item should say so.

**The run that would actually settle it, named and costed as the brief asks.**
A **held-out replication**: draw a fresh set of 4,000 episodes at a new content
seed, capture states at the one position, and run **one pre-stated test** —
the third checkpoint, the other agent's revision value, layer 3, standardised,
200 draws. One test, pre-registered, on a sample the cell has never seen.

- **Cost: about 0.25 processor-hours** of fitting for the single test, or about
  **0.75 processor-hours** for all three checkpoints at layer 3, plus one state
  capture per checkpoint. $0, local, inference only.
- **Why it settles what more draws cannot.** The clearing cell's problem is not
  mainly the precision of its null; it is that it is the largest of 135 tests
  chosen after the fact, on a sample already read twice. More draws refine the
  denominator of a number whose numerator was selected by searching. A fresh
  sample with one pre-stated test has no family, needs no bar of 3.38, and is
  read at an ordinary 5%. If the position is real, a pre-stated test on fresh
  episodes is the direct evidence; if it is the largest of 135 draws, it will
  regress.
- It should carry the fold-split fix from the earlier finding, and should read
  the negative control alongside it, which the findings' third open item
  already asks for.

I am not recommending that this be run. The brief asks for it to be named and
costed and that is what the above is.

### RT-141 — the blind arm should run first. ARGUED

**Before.** Three reasons, in increasing order of weight.

*It is already authorised.* The blind-localization arm is registered as
unconditional (pre-registration, Procedure step 8, adjudicated 2026-08-07): it
"runs on the same trained seeds regardless of which bin the headline reaches",
and registering it unconditionally was itself the device for removing the
"instrument audit run only because the headline disappointed" degree of
freedom. It needs no new decision. A further follow-up on this position does.

*It is the measurement that makes the others readable.* The arm asks whether
the localization stack recovers a center "known-by-construction to exist and
to be load-bearing", and the registration states the consequence plainly: if
the instruments cannot recover a center that is known to be there, the null
was instrument failure. Every number in both follow-up runs — the nulls, the
+3.43, the seven-to-eleven-standard-deviation exclusion of the confound — is
conditional on this stack being able to find something when something is
there. That has never been established on this design. Spending another
150 hours refining the precision of a cell measured by an instrument of
unknown sensitivity is the wrong order of operations.

*And the ordering is not merely a matter of efficiency.* The registration
requires the blind pipeline to "receive a config with the register location
withheld", and concedes that with one researcher "blindness is procedural, not
epistemic — what is blind is the pipeline's inputs". A targeted rerun at the
other agent's revision value, filed in findings and recorded in the ledger,
publishes the conclusion that this is the position to look at. Each such
document makes it harder to run a later arm whose inputs are honestly blind to
where the answer is thought to be. **Running the follow-up first spends a
registered commitment to buy a refinement of a cell that clears by two
episodes.** The order should be: the blind arm, then whatever the blind arm
says is worth doing about this position.

### RT-142 — the STATUS.md paragraph

What STATUS.md may say about the other agent's revision value, written to be
readable by someone who has not followed this line:

> **Two follow-up reads, 2026-09-21 (both local, no money spent).** The first
> pointed the existing read at a different question — which of the four marker
> words belongs to the other agent who revises — and found it nowhere except
> where that agent's own name is the word being read. This settles the
> objection raised on 2026-09-20, that the model's own index looked positive
> at the other agent's revision value only because knowing who is speaking
> rules out one of the four possible answers. For that to explain what was
> seen, the other agent's rank would have to be readable at that token at
> about 0.32 to 0.35; it reads 0.258 to 0.263, and the same read detects an
> effect of exactly the required size at a different token in the same run.
> The objection is excluded. That is the solid result of the pair.
>
> The second read put all 448 directions of the state on an equal footing
> before fitting, which the earlier read did not, to test whether the earlier
> read's penalty had been hiding a faint signal. It had not: the spread of
> results is unchanged to two decimal places and the pre-stated outcome is
> again *found nowhere*. Every fit converged, where the earlier read's third
> checkpoint mostly ran out of steps, which is a real improvement in the
> instrument. One cell of 135 crossed the family-adjusted bar — third
> checkpoint, the other agent's revision value, layer 3, at 3.43 against a bar
> of 3.38. **It is not carried forward as a clearance.** It clears by two
> correct predictions out of 4,000; a one-standard-error change in the spread
> it is measured against, which is 5% of that spread and comes from the same
> 200 draws, puts it below the bar; the same states have now been swept twice
> for this target, and against the 270 tests actually run the bar is 3.56; and
> the same run's negative control, at a token where the answer cannot be
> known, also returned zero of 200 draws beating it.
>
> So: one proposed explanation excluded, and a sub-bar pattern at one position
> that is now measured twice and still sub-bar. Nothing is localized. Under
> the registration nothing counts as localized or absent until causal patching
> has also run, and it has not; the registered term for where this line stands
> is still **not testable (localization)**. Both reads measured the register
> index — the rank of the marker word — and not the model's own marker word,
> which is the registered target and has still never been read at these
> positions.

**What the registration requires before the other agent's revision value
becomes a localization target.** Under Part 3 of
`separation-clause-requirements.md`, read with Amendment A3 section 3.2, the
position is not a lesion target until all of the following exist on this
design:

1. **Probe and patching agreeing.** Section 3.2 step 4 makes convergence the
   condition: the subspace counts as localized only when probe and causal
   patching agree on a confound-controlled design, and otherwise the outcome
   is *not testable (localization)*. Patching has never run. The two-method
   requirement is met by probe plus patching and by nothing else (step 5).
2. **A positive control the stack recovers on this design**, not a synthetic
   one — Part 3, item 1.
3. **The denoised difference-of-means direction run against the same
   permutation null**, so that "insensitive stack" and "no signal" are
   separated — Part 3, item 1.
4. **The discriminators the comparison does not carry** — Part 3, item 2: the
   swap probe moving the action with the patched identity; the other-index
   control *as a lesion*, a subspace localized for a named non-self agent,
   matched in rank and probe accuracy, that does not hurt the self-directed
   condition; and the mid-episode re-indexing probe for the tag bin.
5. **A random baseline matched in rank, norm and layer** — Part 3, item 3.
6. **The full bin set** — Part 3, item 4.

One point on item 4 that the findings should not be allowed to elide. The
other-agent run is the first execution of the *probe* half of the registered
other-index control. Part 3 asks for the *lesion* half — a localized
other-index subspace whose ablation leaves the self-directed condition intact.
The run found no such subspace at any testable position, so there is nothing
to ablate and that control remains unavailable. **Running the probe half does
not discharge the requirement.**

---

## The kill case

If one thing sinks this pair, it is this. The standardised refit's one clearing
cell — the only positive result either run produced, and the thing the
interpretation is built around — clears the bar by 1.94 episodes out of 4,000,
against a null spread estimated from 200 draws whose own standard error is 5%
of itself, which is enough to move the margin from +3.43 to +3.27 and below the
bar; it was reached with a different fold split and a different null sample
from the unscaled read it is compared against, so the +1.34 to +3.43 move it
rests on is not attributable to the scaling; it is the largest of 135 tests on
a sample that has now been swept twice for the same target, against which the
bar is 3.56 and not 3.38; the same run's negative control, at a token where the
answer provably cannot be known, satisfied two of the three conditions for
FOUND including the zero-of-200-draws criterion the findings cite as
corroboration; the target it was measured on is not the registered localization
target; and the pilot, the most legible checkpoint by every earlier measure,
shows +1.54. Strip the cell out and what remains is what the pre-stated cells
already said twice: **found nowhere**, plus one genuinely good result — the
exclusion confound excluded by seven to eleven standard deviations with a
demonstrated detection at the required effect size — which the findings
under-argue while over-arguing the cell. The interpretation's claim that "three
independent lines now point at that one position" is the failure mode this
review exists to catch: two of the lines are one sample read twice, which the
ledger has already ruled is one observation, and the third is a null that
removes an alternative rather than evidence that points anywhere. Nothing here
should enter STATUS.md as a convergence.

---

*Findings are numbered RT-120 to RT-142 and continue in `red_team_ledger.md`.
The packet's instruction to continue from RT-117 is stale; see RT-122.*
