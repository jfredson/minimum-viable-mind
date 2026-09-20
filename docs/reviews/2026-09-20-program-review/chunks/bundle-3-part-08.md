
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
this particular draw of 4,000 episodes at a given position reproduces on
all three.

**The five layers read one residual stream.** Five reads of the same
running state at the same token are not five independent tests of
anything.

Spreading the error rate across 135 tests remains **valid** — the
correction controls the family-wise error whatever the dependence is.
What it does not do is control it *efficiently* under positive
dependence. The bar is set for a family that is larger than the effective
one, so it buys less power than the arithmetic implies:

| family assumed | bar it sets |
|---|---|
| 135 tests — as applied | 3.3740 |
| 45 tests — one set of positions and layers, shared episodes | 3.0588 |
| 9 tests — positions only, layers pooled | 2.5392 |

The run's one MARGINAL, at +3.34, clears both of the lower bars. I am
**not** arguing the bar should have been lower — it was pre-stated,
pre-committed, and choosing the conservative option before seeing the
data is the right instinct. I am arguing that for a run whose entire
question is "is anything there at all", over-correcting is the direction
that manufactures a null, and the findings present 3.38 as a neutral
technical choice rather than as the strict end of a defensible range.

### RT-60 — fold size and capacity are not the problem

**Worth-noting. MEASURED.** The packet names four candidate mechanisms.
Two of them clear.

At the sweep's own size the fit is comfortable: 4,000 episodes, four
folds, so 3,000 training rows against 448 directions and four answers,
with the smallest answer class holding 964 examples on every checkpoint.
That is not an overparameterized regime and I find no sign of capacity
failure in the records — the nulls are tight and well-behaved (spread
0.0067 to 0.0091 on every test), the real accuracies sit on top of their
nulls rather than scattering, and no test tripped the missing-class rule.

The 400-episode configuration *is* overparameterized — 300 training rows
against 448 directions — but it is used only to reproduce the recorded
anchor, and no sweep cell rests on it. The packet's framing asks about
"448 dimensions on 400 episodes"; that describes the anchor, not the
sweep, and the anchor is a reproduction check rather than a measurement.

So of the four mechanisms, fold size and capacity are cleared.
Regularisation is not (`RT-58`), and the two positions that were never
tested are the two controls, which is correct design: position 1 is where
the answer is provably not yet knowable and position 6 is where it is
explicit. That leaves the episode's other sixty tokens unexamined, which
is the previous review's point about eleven positions of seventy-one
(`RT-46`) and is unchanged by this run.

### RT-61 — the new requirement that never fires

**Worth-noting. MEASURED.** The method introduces a third condition for
FOUND — accuracy must beat the majority-class rate — and calls it out:
"Requiring the majority-class rate is new and it is deliberate." It never
does any work.

The majority-class rate is 0.2582 on all three checkpoints. The accuracy
needed to clear the family bar is between 0.2774 and 0.2778 on every one
of the 135 testable tests. So any test that clears the bar has already
beaten the majority-class rate by a comfortable margin, and the new
condition cannot suppress anything. The findings report it as one of
three conditions that had to be met, which reads as a tightening and is
not one.

This is worth-noting rather than serious because the requirement is
harmless and would bind under a looser bar. But a pre-stated safeguard
that cannot fire should be reported as inert, the same way the findings
correctly report that the degeneracy rule did not fire.

---

# 3. No verdict

*What the run measured, what it did not, and what the pre-stated cells
say a marginal means.*

| # | finding | severity | label |
|---|---|---|---|
| RT-62 | the run's one consistent pattern — the other agent's revision value, positive in 15 of 15 tests — is invisible to a purely per-test analysis and is under-reported | serious | MEASURED |
| RT-63 | the first reason given for setting that pattern aside misdescribes what was measured: the target at every position is the model's **own** index | serious | MEASURED |
| RT-64 | there is a real confound at that position and it is not the one named; the instrument that separates it is registered and has never been run | serious | ARGUED |
| RT-65 | the MARGINAL test's real fit hit the pass cap on all four folds, which the findings do not say | worth-noting | MEASURED |
| RT-66 | seed 2's extra scatter is confined to that one position; elsewhere it is as tight as the other checkpoints, which cuts against discounting the cell on "seed 2 is straining" | worth-noting | MEASURED |
| RT-67 | the registered anchor position runs below its null at all five layers on seed 2, reaching −3.01, and the findings mention it only inside a range | worth-noting | MEASURED |
| RT-68 | the only testable test with zero of 200 draws beating it is at an own-agent position and is never discussed; it is also exactly what chance predicts | worth-noting | MEASURED |
| RT-69 | the pre-stated cells were applied correctly throughout, checked in the code and against all 165 tests | no finding | MEASURED |
| RT-70 | I tested the obvious bias from splitting paired episodes across folds and it is not present | no finding | MEASURED |

### RT-62 — one position is positive in fifteen tests out of fifteen, and nothing in the analysis can see it

**Serious. MEASURED.** The findings do name the other agent's revision
value as the highest testable position on all three checkpoints, and give
its three best-layer margins: +2.33, +2.39, +3.34. They do not report the
number that makes it interesting. Averaging each position's margin across
its five layers, and counting how many of its fifteen tests came out
positive:

| position | pilot | seed 1 | seed 2 | mean of 15 | positive |
|---|---|---|---|---|---|
| `other_revision_value` | +1.49 | +1.37 | +2.33 | **+1.73** | **15 / 15** |
| `query_answer_value` | −0.27 | +0.42 | +0.27 | +0.14 | 9 / 15 |
| `own_revision_value` | −0.09 | +1.23 | −0.75 | +0.13 | 8 / 15 |
| `own_revision_by` | −0.16 | +0.60 | −0.14 | +0.10 | 8 / 15 |
| `query_answer_decision` | −0.15 | +0.47 | −0.68 | −0.12 | 7 / 15 |
| `other_revision_decision` | +0.09 | −0.41 | −0.18 | −0.17 | 7 / 15 |
| `own_assign_2_value` | −1.01 | +0.19 | −0.54 | −0.45 | 5 / 15 |
| `before_own_revision_turn` | −0.53 | −0.37 | −0.84 | −0.58 | 1 / 15 |
| `own_revision_decision` | −0.17 | −0.26 | −1.46 | −0.63 | 4 / 15 |

Every one of its fifteen tests is positive: +1.91, +0.57, +2.33, +1.32,
+1.30 on the pilot; +1.25, +2.39, +1.24, +0.85, +1.11 on seed 1; +1.34,
+3.34, +1.75, +2.54, +2.70 on seed 2. Its mean margin is more than twelve
times the next position's. Nothing else in the run is remotely like this.

**The pre-stated analysis cannot see it**, and that is the finding. Every
cell in the method turns on a single test clearing a single bar. There is
no statistic anywhere in the method, the code or the findings that asks
whether a position is consistently elevated across layers and
checkpoints — and consistency across layers and checkpoints is the shape
a real, weak, distributed signal would take, as against the shape a
single lucky test would take. The method's own honesty note anticipates
the opposite case (a single FOUND cell being over-read) and says nothing
about this one.

**Two things that cut the other way, and I want them on the record with
equal weight.** First, the three checkpoints read the same 4,000 episodes
(`RT-59`), so a property of this episode draw at this position would
reproduce on all three and would look exactly like this. The three
checkpoints are not three independent confirmations. Second, the five
layers within a checkpoint are heavily correlated, so "fifteen of
fifteen" is nearer three observations than fifteen. Treating each
checkpoint as one observation, "some position among nine ranks top on all
three" happens by chance about one time in eighty — suggestive, not
decisive, and that calculation still assumes an independence across
checkpoints that the shared episodes deny.

So this is not a finding. It is the one thing in the run that looks like
something, the analysis was not built to notice it, and the findings
report a third of it.

### RT-63 — the target is the model's own index at every position, including that one

**Serious. MEASURED.** The findings give three cautions against reading
anything into the MARGINAL. The first is:

> It is the **other** agent's revision value, not the model's own. If
> something is readable there it is not obviously own-agent identity.

**The target read at that position is the model's own register index** —
the rank of the model's own marker word among the four in the episode.
That is the target at all eleven positions; the run has one target and
the method says so repeatedly. Only the *position* belongs to the other
agent's turn.

So a reading there is own-agent identity recovered at a token that is not
the model's own act. That is not a reason to discount it. It is, almost
word for word, what the registration defines the thing being looked for
to be. Amendment A3 section 3.1 defines the lesion target as a subspace
"that carries *'which marker is mine'* at positions *away from* act
positions (revision turns and query positions)". A position inside the
other agent's revision turn is about as far from the model's own act
position as this episode goes.

The caution inverts the significance of the run's own strongest
observation. Whatever else is true of that cell, "it is the other agent's
turn, so it would not be own-agent identity" is not a reason to set it
aside — it is a reason it would matter.

### RT-64 — the confound that is actually there, and the control that would settle it

**Serious. ARGUED.** Having said the findings' reason is wrong, I owe a
better one, and there is one.

The register index is the rank of the model's own marker among the four
markers present in the episode. At the other agent's revision value, the
other agent's marker has just been named in the running text. A
representation of *that* marker partially determines the model's own rank
by exclusion: it removes one of four possibilities, which lifts the best
attainable accuracy from 0.25 to about 0.333 with no own-agent
representation involved at all. The MARGINAL sits at 0.277. The confound
is comfortably large enough to produce it.

That would also explain why the effect is strongest at the other agent's
turn rather than the model's own, and why the other agent's revision
*decision* — one token earlier, before the value — shows nothing (mean
−0.17 across fifteen tests). I have not tested it: doing so needs the
position and target definitions, which are not in the packet.

**The instrument that separates these two readings is registered and has
never been run.** Amendment A3 section 3.1 lists, as matched control
L2(a):

> The *other-index* subspace: the same localization run for a named
> non-self agent ("which marker is agent B's"), matched in rank and probe
> accuracy.

Run the identical fitted read at the identical positions against the
*other* agent's index. If the other agent's index reads strongly at the
other agent's revision value and the model's own index reads weakly, the
MARGINAL is the exclusion confound and the position is closed. If the own
index survives once the other index is accounted for, it is the first
thing in this sequence that looks like a self-index away from an act
position. It is a four-answer target on captured states, so it costs the
same eleven processor-hours as the run just completed, and the code needs
a new target function and nothing else.

This is the cheapest decisive measurement now available in this line, and
it is already registered as a required control rather than being a new
idea.

### RT-65 — the MARGINAL was fitted by an optimiser that stopped early on every fold

**Worth-noting. MEASURED.** The findings caution that seed 2 strains the
instrument, giving the checkpoint-wide cap rate of 73.6 per cent. The
sharper fact is in the record and is not reported: for the MARGINAL test
itself — seed 2, the other agent's revision value, layer 4 — the real fit
used the full 2,000 passes on **all four folds**, and 785 of that test's
804 fits hit the cap.

So the single number the findings single out for discussion comes from a
fit that stopped early everywhere, not merely from a checkpoint where
that often happens. That is their own caution, correctly aimed, and it is
the version that should have been written.

It also cuts both ways, which is why it is worth-noting rather than
serious: an early-stopped fit is an under-fitted one, and under-fitting
more often hides a signal than invents one. Raising the cap is the
obvious check and the findings already list it as an open item, correctly
noting it would be a different instrument needing its own anchor.

### RT-66 — seed 2 is not generally unstable; it is unstable at one position

**Worth-noting. MEASURED.** The findings' framing is that seed 2 is the
straining checkpoint and its numbers deserve the most caution. The spread
of the 45 testable margins supports that at first glance — 1.177 on seed
2 against 0.812 on the pilot and 0.852 on seed 1.

Remove the other agent's revision value and seed 2's spread falls to
**0.760**, which is tighter than either of the other two checkpoints. The
excess scatter is not a property of seed 2. It is that one position.

That matters for how the MARGINAL is read. "Seed 2's numbers are noisy,
so discount this one" is not supported: seed 2's numbers are not noisy
anywhere except at the position in question, and a position that is
elevated *and* over-dispersed relative to its own checkpoint's behaviour
is a slightly stronger candidate than the findings allow, not a weaker
one. This is the second of the findings' three cautions, and like the
first it points the other way once the record is checked.

Their third caution — that one position rising on three checkpoints while
never reaching the bar is unremarkable in a family of 135 — stands, with
the qualification in `RT-62` that the family is not 135 independent
tests.

### RT-67 — the registered position reads below chance at every layer on seed 2

**Worth-noting. MEASURED.** The model's own revision decision is the
position the registration names, and the previous review's tables track
it as "the registered anchor". On seed 2 its five margins are **−0.26,
−1.05, −3.01, −0.83 and −2.16** — every layer below its own
shuffled-label null, two of them beyond two standard deviations, and one
of them the most extreme value anywhere in the run.

The findings mention the −3.01 once, inside the phrase "the full range of
margins is … −3.01 to +3.34 on seed 2", and never say where it is or that
it sits in a run of five negatives at the registered position.

A real accuracy three standard deviations *below* a shuffled-label null
is not a null result; it is an anomaly. It may be nothing — with 135
tests the lowest of 135 standard normal draws would be expected near
−2.8, so −3.01 alone is unremarkable. What is not explained by that is
all five layers of one position pointing the same way. The honest
sentence is that it is unexplained, and the findings should have written
one.

### RT-68 — the one test no shuffled draw matched is at an own-agent position

**Worth-noting. MEASURED.** Exactly one testable test in the whole run
had **zero of 200** shuffled draws meet or beat its real accuracy: seed
1, the model's own revision value, layer 3, accuracy 0.2678, margin
+2.07. Every other zero-draw result in the run is at the positive
control.

The findings print it in the table as "0.2678 +2.07 (0)" and never
mention it. Under the pre-stated rule it is correctly not MARGINAL — it
does not reach 3.0 standard deviations — and I am not arguing the rule
was misapplied.

Two sentences were owed. The first is that it exists and is at an
own-agent position, which is the position class the registration cares
about. The second is that it is exactly what chance predicts: with 201
values in play, about 0.67 of 135 tests should come out on top of their
own null, so seeing one is unremarkable and seeing none would have been
mildly surprising. Saying both would have cost a line and would have
strengthened the findings, not weakened them.

It is also the one place in the run where counting the draws and
computing the margin disagree about which side of "interesting" a test
falls on, which is the disagreement `RT-55` predicts when a bar of 3.38
is resolved by 200 draws.

### RT-69 — the cells were applied correctly

**No finding. Recorded for completeness. MEASURED.** I checked the label
logic in the code against the method file and then against all 165 tests
in the records.

FOUND requires margin at or above 3.38, zero of 200 draws matching or
beating the real accuracy, accuracy above the majority-class rate, and no
degeneracy. MARGINAL is three standard deviations without the family bar,
is reported, and triggers no cell. The MARGINAL in this run clears 3.0 at
+3.34, fails 3.38, and correctly triggers nothing. The two cells are
exhaustive, the sub-pattern is reported as the earlier ruling on
exhaustive cells (`RT-41`) requires, and the code's self-test exercises
all three sub-patterns including the two that did not occur.

Two details I checked because they could have been wrong and were not.
The rounding of the margin before comparison leaves the operative bar at
3.375, still above the exact 3.3740 (`RT-52`). And a checkpoint's control
is treated as holding if **any** single layer clears at position 6 — a
weak test as written — but all five layers clear on all three
checkpoints, at +34 to +54 standard deviations, so nothing turns on it.

The degeneracy rule fired nowhere, on any of the 165 tests. I confirmed
this from the records rather than from the summary: no null with zero
spread, no missing class, no accuracy landing exactly on the
majority-class rate.

### RT-70 — a bias I expected to find and did not

**No finding. Recorded because it should not be raised again without
evidence. MEASURED.** Amendment A3 section 3.2 specifies that the probe
contrast is "built from paired episodes that share a content seed and
rotate the owner … so content is held fixed and only ownership varies",
and the run uses those pairs. The folds are cut at random over the
flattened list and are not pair-aware, so a held-out episode's partner —
same content, different owner, therefore usually a different register
index — normally sits in the training set. A classifier that leant on
content would then be actively misled on the real labels while suffering
no such handicap on the shuffled ones, which would push real accuracies
**below** their nulls and could mask a weak signal.

It is not happening at any scale worth worrying about. Across the 135
testable tests the margins have a mean of +0.016, a spread of 0.993, and
70 of 135 fall below zero — which is what 135 independent standard normal
draws would look like, to three figures. Whatever the unpaired folds are
doing, they are not producing a global negative bias.

I record it because it is the first thing a sceptical reader will think
of, because the shape of the null across 135 tests being this well-behaved
is a genuine point in the run's favour that the findings do not claim,
and because the local exception to it is the five negative layers at the
registered position on seed 2 (`RT-67`).

---

# 4. Over-reading

*The sentence for the status file, whether the broad claim is now
supportable, and what the registration still requires.*

| # | finding | severity | label |
|---|---|---|---|
| RT-71 | "no linear read finds own-agent identity at the nine testable positions" is not supportable: the registered target was never read by this instrument at any of those nine positions | fatal to that sentence | MEASURED |
| RT-72 | "both reads are now empty" is one sample read twice, and on this target the earlier read's own control failed on seed 1 under the rule this run adopted | serious | MEASURED |
| RT-73 | the "essentially identical power" paragraph compares two reads through a measure that assumes a perfect score neither can reach; the conclusion drawn from it is right and the reasoning given for it is not | serious | MEASURED |
| RT-74 | what the registration still requires before "not localized" or "absent": causal patching, which has still never run | serious (carried, not new) | MEASURED |
| RT-75 | every ruling the run was required to honour, it honoured | worth-noting (credit) | MEASURED |

### RT-71 — the registered target has still never been read at the nine positions by this instrument

**Fatal to the sentence the packet asks about. MEASURED.** The packet
asks whether "no linear read finds own-agent identity at the nine
testable positions" is now supportable. **It is not**, and the reason is
not a matter of degree.

The previous review's addendum established, from the registered text,
what this programme is supposed to be looking for. Amendment A3 section
3.2 specifies linear probes that "decode **own-marker identity** from the
residual stream at revision and query positions". Section 3.1 defines the
target as a subspace carrying "which marker is mine". The addendum's
finding on this (`RT-48`) states it plainly and John accepted it: the
registered target is the model's own marker word, and the powered runs
were the first in the whole line to use it.

**This run did not read it.** The method declares before the run, with
the arithmetic, that the marker-word target does not fit: about 70
processor-hours against about 11, because the 25-answer fit hits the pass
cap on most folds. So the marker-word target was not run, and this is
stated openly in the method, in the code, in the machine records and
three times in the findings. Nobody hid anything.

But the consequence has not been drawn. Assemble what has actually been
measured at the nine testable positions:

