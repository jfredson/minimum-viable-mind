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
