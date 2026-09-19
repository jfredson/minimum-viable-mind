# Denoised own-agent direction — method, committed before the run

*2026-09-19. **UNREGISTERED** diagnostic. Local, inference only, no
training, no network, $0 [C1/C2]. Reads no registered verdict and touches
no registered text. Results go to a fresh file per checkpoint, nothing
overwritten [C6].*

*This file is committed before the diagnostic produces any output. The
whole value of it is that the outcome cells at the bottom were fixed
while nobody knew which one would fire. If the numbers turn out to want a
different rule, that is a finding for a later run, not an edit to this
file.*

## Where this came from

The research note on The Pain Axis paper (`docs/research-note-pain-axis-2026-09-19.md`),
item 2, "denoise before probing". The paper extracts its direction by
taking the difference between the average internal state under the target
condition and the average under a control condition, **after first
removing the directions that account for half the variation in the
control data**. Our five linear probes on the pilot checkpoint all landed
*below* their own permutation nulls (`blind-control-findings.md`), on a
checkpoint where ownership is measured to be load-bearing. One plausible
reason is that the residual stream at the probed positions is dominated
by variation that has nothing to do with ownership — position, content,
which token happens to sit there — and that this swamps a small ownership
signal when a probe is fitted to the raw states.

So: strip the loud, ownership-irrelevant directions out first, then look
for ownership in what is left.

This is a **known-answer test for the localization stack**. The existing
known-answer test (`known-answer-test-findings.md`) validates the plumbing
under the probe and, as that file says plainly, exercises neither the
deeper-layer capture path at revision positions nor the ablation path at
all. This one asks a sharper question: with the nuisance variation
removed, is own-agent identity linearly present at the positions the
registered pipeline probes?

**What a pass would and would not mean.** If the denoised direction
separates above its null, the stack was *insensitive* rather than the
signal *absent*, and the honest reading of the blind arm's not-flagged
result shifts. It would not show that what separates is a carried
self-index rather than the acting channel's input trace passed forward.
That is red-team objection R1 and nothing here answers it.

## What is measured

Per probed layer, per checkpoint: how well a direction built from the
average difference between own-agent conditions separates held-out
episodes by which agent the model is, **after projecting out the
principal components that account for half the variation in the control
condition**, scored against the same kind of permutation null the failed
probes were scored against.

### The checkpoints

The three A3 30-million-parameter checkpoints already in hand, verified by
checksum:

| name | file | checksum (md5) |
|---|---|---|
| pilot (seed 0) | `a3_30m_seed0.pt` | `f751228ce0e40bae5aba22c6d5aa6c60` |
| seed 1 | `a3_30m_seed1.pt` | `eeed93b80a7c8d81ba56d1ec6254af41` |
| seed 2 | `a3_30m_seed2.pt` | `f1f131cb78f27c57194bedd127fd4031` |

### The episodes and the positions

Identical to the blind-arm positive control, so the comparison against
those five failed probes is like for like: 200 paired episodes from
`localize_a3.paired_episodes` at content seed 20260917, giving 400
episodes; residual-stream states captured at the revision position, the
token that predicts the graded value, by `localize_a3.residuals_at`;
layers 3, 4, 5, 7 and 8. Four possible owning agents, so a classifier that
always guesses gets 0.25 and a separation score for one agent against the
rest has 0.5 as its no-information value.

Nothing about the episodes, the positions or the layers is changed. The
only thing that changes is what is done with the states after they are
captured.

### "Control condition", made concrete

The paper's control data are separate sentences that lack the property
being looked for. We have no such separate set at these positions, so the
control condition here is **the same states with the own-agent signal
taken out of them**: each episode's state minus the average state of the
episodes that share its owning agent. What is left is everything the
residual stream carries at that position *except* which agent the model
is — content, position, token identity, the ordinary machinery of the
episode. Those are the directions to remove.

**Confidence: moderate, and this is a judgment call rather than a
standard one.** The strongest alternative is to use the pair structure
instead: the episodes come in pairs that share a content seed with the
owning agent rotated, so the average of a pair carries the content with
ownership averaged away, and the principal components of those pair
averages are another honest reading of "control variance". I chose the
within-agent version because it uses every episode rather than half the
degrees of freedom, and because it does not depend on every pair
surviving the filter that keeps only episodes where the model actually
revises. If a later session prefers the pair-average reading, it is a
different measurement and gets its own method file; it is not a knob to
turn on this one after seeing the result.

### The denoising step

On the training part of each split, and only there:

1. Centre the states within own-agent class, as above, to get the control
   condition.
2. Take the principal components of that control condition, ordered by
   how much variation each accounts for, and keep the **smallest number
   of them whose variation adds up to at least half** of the total. Call
   that set the nuisance directions. The count is recorded for every
   layer and checkpoint, because a layer where half the variation sits in
   one direction is telling a different story from one where it takes
   forty.
3. Project the nuisance directions out of every state, training and
   held-out alike, using the components fitted on the training part.

### The direction

On the denoised training states, the average state for each of the four
owning agents. One direction per agent: that agent's average minus the
average of the other three. This is the difference of means, in the only
form that makes sense with four conditions rather than two. Each direction
is scaled to unit length.

### The score

Held-out states are projected onto the four directions.

**The headline number is the separation score**: for each owning agent,
how well that agent's projection separates its own episodes from the
other three, expressed as the area under the receiver operating
characteristic curve — the probability that a randomly chosen episode of
that agent projects higher than a randomly chosen episode of another. No
information gives 0.5, perfect separation gives 1.0. Averaged across the
four agents. This is the paper's metric and it has no ceiling problem.

**Reported beside it, carrying no outcome cell**: the held-out accuracy of
assigning each episode to whichever agent's average it lands nearest, in
the denoised space. This is on the same scale as the five probe
accuracies in `blind-control-findings.md` (chance 0.25) and exists so the
two tables can be read against each other directly.

Splitting is four-fold cross-validation, the same as the probes used.
Everything above — the class averages used for centring, the nuisance
components, the directions, the nearest-average reference points — is
fitted on the training folds only and applied to the held-out fold. This
is the part that is easy to get wrong and that would quietly invent a
result: if the nuisance components or the direction see the held-out
episodes, the separation is not held out and means nothing.

### The null

The same construction the probes used: 200 draws, each one shuffling the
own-agent labels and running the **entire** procedure again — centring,
principal components, directions, scoring, cross-validation — on the
shuffled labels. The comparison is the real score against the mean and
spread of those 200.

**The bar is clearance by three standard deviations of the null**, the
same bar the probes had to clear and the same bar the blind-arm control
uses. It is not moved for this diagnostic.

### The contrast arm, which is mine to add and is not in item 2

The same difference-of-means direction, the same splits, the same
statistic and the same null, **without the denoising step**. Item 2's
claim is specifically that denoising is what would rescue the signal.
Without this arm a pass would show that some linear read works and would
say nothing about whether projecting out the nuisance directions is why.
It costs one more pass over states already in memory.

## Preconditions, stated in advance

Carried over from the lesson of the register probe, where a degenerate
null was discovered after the fact rather than before.

- If the permutation null for a layer has **zero spread**, the
  three-standard-deviation comparison compares a number to itself. That
  layer is reported DEGENERATE and gets no cell.
- If the real separation score is **exactly 0.5**, the no-information
  value, that layer is reported DEGENERATE and gets no cell.
- If the nuisance directions account for the full rank of the training
  states, so that projecting them out leaves nothing, that layer is
  reported DEGENERATE and gets no cell.

## The family of tests, named before it is run

Five layers on each of three checkpoints is **fifteen tests**, plus
fifteen more in the contrast arm. At a three-standard-deviation bar, one
test in roughly seven hundred clears by chance, so fifteen tests clear by
chance about two per cent of the time. That is small but it is not
nothing, and one marginal clearance out of fifteen is much weaker evidence
than five clearances. The findings will report **how many of the fifteen
cleared and by what margins**, not only whether any did. The bar itself is
not adjusted: it is kept at three standard deviations so the comparison
against the five failed probes is like for like, and the count is reported
instead.

## Outcome cells, fixed here

Exhaustive and disjoint, read across the whole diagnostic.

**SEPARATES.** At least one layer on at least one checkpoint clears its
null by three standard deviations in the **denoised** arm, and the same
layer's undenoised arm does not clear, or clears by a smaller margin.

> Reading: the ownership signal is linearly present at the probed
> positions and the nuisance variation was hiding it. The localization
> stack was insensitive rather than the signal absent, and the honest
> reading of the blind arm's not-flagged result shifts toward instrument
> failure — which RT-12 named as possibly outweighing the headline.

**SEPARATES, BUT NOT BECAUSE OF THE DENOISING.** At least one layer on at
least one checkpoint clears in the denoised arm, and the same layer's
undenoised arm also clears by a margin no smaller.

> Reading: a linear read of own-agent identity exists at these positions
> and the five probes missed it for some other reason — the probe's
> regularisation, its loss, or the difference between fitting a classifier
> and taking a difference of averages. Projecting out the nuisance
> directions is not what did it. This is a real finding about the
> localization stack and a different one from the cell above.

**DOES NOT SEPARATE.** No layer on any checkpoint clears in the denoised
arm.

> Reading: own-agent identity is not linearly decodable at the probed
> positions on any checkpoint in hand, even after the loudest
> ownership-irrelevant directions are removed. The five probes falling
> below their nulls is not explained by nuisance variance swamping a small
> signal. This does not show the signal is absent from the model — only
> that this position, this layer set and a linear read do not find it.

**DEGENERATE THROUGHOUT.** Every layer on every checkpoint trips a
precondition. No cell is assigned and the diagnostic is reported as having
failed to run rather than as having answered.

A result fitting none of these is reported as fitting none. No cell is
added after the fact.

## What this triggers, stated before the answer is known

Per John's instruction of 2026-09-19: if the denoised direction separates
above its null on **any** checkpoint — that is, either of the first two
cells above — the blind-arm positive control is rerun under the signed
rule of 2026-09-19 on the pilot and on seeds 1 and 2, at 800 paired
episodes, and every cell is reported in `blind-control-findings.md` as a
dated addition. The 2026-09-16 verdict is not edited. If it does not
separate on any checkpoint, that is said plainly and nothing is rerun.

## What gates this and what does not

The diagnostic calls the known-answer gate
(`lock_guard.require_known_answer_pass`), which passes, because this is a
read of the localization stack and John's ruling of 2026-09-16 gates those
on the known-answer test passing.

It deliberately does **not** require the threshold lock. The lock exists
so that no ablation result is read against a bite threshold that was
chosen after seeing it. Nothing here ablates anything and no number here
is compared to that threshold or to any registered band. Requiring a lock
that has no bearing on the measurement would be theatre, and saying so is
better than quietly adding a gate that looks like rigour.

## Cost and where the output goes

Inference on three 30-million-parameter checkpoints on a laptop, one
forward pass per checkpoint to capture states, then linear algebra on
matrices of a few hundred rows. Minutes, no spend, no network.

One fresh file per checkpoint under `a3-gates/`, named
`denoised_direction_a3_<checkpoint>.json`, plus
`denoised-direction-findings.md`. Nothing existing is overwritten.

Implementation: `src/denoised_direction_a3.py`, committed together with
this file and before either produced any output.

## A limitation of this recipe, found while building it and not after

"Keep removing components until the variation removed reaches half" stops
at the first component that crosses the line. If the
ownership-irrelevant variation sits in two directions of similar size,
the first can cross the line on its own and the second is left standing —
still louder than any ownership signal, and still able to swamp it. The
synthetic check in the implementation demonstrates exactly this and keeps
it as a named case rather than tuning it away.

This is a property of the rule item 2 prescribes, taken from the paper,
not a mistake in carrying it out, and the threshold is deliberately left
at half rather than raised to whatever would have worked. The defence is
reporting: **the number of components removed is recorded for every layer
and checkpoint**, so a layer where half the variation was reached in one
or two components can be recognised on the record instead of guessed at.
If the diagnostic does not separate and the component counts are small,
"the nuisance was not actually removed" is a live reading of that result
and the findings must say so.
