# Denoised own-agent direction — result

*2026-09-19. **UNREGISTERED** diagnostic. Method and code committed
before any output at `db24540`; this file reports what came back. Local,
inference only, no training, no network, $0. Three checkpoints verified
by checksum. Reads no registered verdict and touches no registered text.*

## The cell

**DOES NOT SEPARATE.** On all three checkpoints, at every probed layer,
in both arms.

**Zero of the fifteen denoised tests cleared its permutation null by
three standard deviations.** The largest margin anywhere in the family
was 1.54 standard deviations, on the pilot at layer 5. The family was
named in advance at fifteen tests with roughly a two per cent chance of
one clearing on its own; nothing cleared, so that allowance was never
called on.

Per the method file and John's instruction of 2026-09-19: **the blind-arm
positive control is not rerun.** The trigger was a separation above the
null on any checkpoint and there is none. That is said plainly here and
nothing downstream is touched.

## What came back

Separation is the chance that an episode of a given owning agent projects
higher than an episode of another, averaged over the four agents. No
information is 0.5. The margin is in standard deviations of that layer's
own 200-draw label-permutation null, and the bar is three.

### Pilot, seed 0 (`a3_30m_seed0.pt`, `f751228c…`)

| layer | denoised separation | margin | undenoised separation | margin |
|---|---|---|---|---|
| 3 | 0.5204 | +0.85 sd | 0.5014 | −0.02 sd |
| 4 | 0.4980 | −0.19 sd | 0.4846 | −0.90 sd |
| **5** | **0.5387** | **+1.54 sd** | 0.5373 | +1.60 sd |
| 7 | 0.5152 | +0.52 sd | 0.5121 | +0.39 sd |
| 8 | 0.4918 | −0.58 sd | 0.4848 | −0.88 sd |

### Seed 1 (`a3_30m_seed1.pt`, `eeed93b8…`)

| layer | denoised separation | margin | undenoised separation | margin |
|---|---|---|---|---|
| 3 | 0.5061 | +0.21 sd | 0.4942 | −0.37 sd |
| 4 | 0.5004 | −0.20 sd | 0.5110 | +0.33 sd |
| 5 | 0.5027 | +0.10 sd | 0.4917 | −0.46 sd |
| 7 | 0.4947 | −0.29 sd | 0.5005 | −0.05 sd |
| 8 | 0.5150 | +0.69 sd | 0.5034 | +0.11 sd |

### Seed 2 (`a3_30m_seed2.pt`, `f1f131cb…`)

| layer | denoised separation | margin | undenoised separation | margin |
|---|---|---|---|---|
| 3 | 0.5053 | +0.11 sd | 0.5062 | +0.21 sd |
| 4 | 0.5025 | −0.07 sd | 0.4860 | −0.85 sd |
| 5 | 0.4760 | −1.26 sd | 0.4813 | −1.08 sd |
| 7 | 0.5168 | +0.94 sd | 0.5214 | +0.85 sd |
| 8 | 0.5214 | +0.87 sd | 0.5161 | +0.68 sd |

Every one of the thirty numbers sits between 0.476 and 0.539 against a
no-information value of 0.5. The nulls are healthy — the preconditions
stated in advance were satisfied everywhere and no layer was reported
degenerate — so the comparisons mean something, and what they mean is
that nothing separated.

Denoising nudged the separation up in ten of the fifteen layers and down
in five, by amounts far too small to call. The contrast arm was added to
answer "is the denoising why", and the honest answer is that the question
never arose, because neither arm found anything.

## The finding underneath the null result, which is the useful part

**The residual stream at these positions is nearly ten-dimensional.**
Removing the principal components accounting for half the variation in
the control condition took **three components out of 448** on fourteen of
the fifteen layers, and four on the remaining one. Going further:

| checkpoint | variation in the largest 1 direction | in the largest 3 | in the largest 10 |
|---|---|---|---|
| pilot, layer 3 | 23.3% | 50.4% | 98.8% |
| pilot, layer 8 | 34.4% | 57.5% | 99.0% |
| seed 1, all layers | 18.9% | 51.5% | 99.6% |
| seed 2, layer 3 | 18.5% | 49.8% | 98.2% |
| seed 2, layer 8 | 24.1% | 53.2% | 98.4% |

(Descriptive, computed after the run, carrying no cell.)

Ten directions out of 448 carry about ninety-nine per cent of everything
that varies at the probed position once ownership is taken out. The
states are not a high-dimensional space with a small ownership signal
buried in it. They are an almost flat, roughly ten-dimensional object.

That changes what the null result can be read as. The method file said in
advance that small component counts make **"the nuisance was not actually
removed"** a live reading, and it is: removing three directions leaves
seven still carrying nearly half the variation. But the numbers point at
something stronger than an under-removal. There is no room in this
geometry for the picture item 2 proposed — a loud nuisance subspace
sitting on top of a quiet ownership subspace — because there is barely
any subspace. Removing the loud directions and removing the signal would
be close to the same operation. Denoising cannot rescue a signal from
variation it is not separable from.

**This is a limitation of the recipe on these checkpoints, not a
refutation of the paper's method.** Their models are 2 to 72 billion
parameters with residual streams of thousands of dimensions carrying
years of text. Ours is 30 million parameters trained on a synthetic
grammar. The denoising step needs a nuisance subspace distinguishable
from the target subspace, and at this scale there is not one.

## The five failed probes look different under this statistic

The original blind-arm probes were not merely at their nulls; **all five
sat below them** (`blind-control-findings.md`), which is systematic and
was flagged as such. This diagnostic's secondary number, the accuracy of
assigning each episode to the nearest agent average in the denoised
space, is on the same scale as those probe accuracies — no information is
0.25 — and on the pilot it reads:

| layer | 2026-09-16 probe accuracy (null) | denoised nearest-average accuracy (null) |
|---|---|---|
| 3 | 0.2350 (0.2532) | 0.2900 (0.2510) |
| 4 | 0.2400 (0.2529) | 0.2575 (0.2508) |
| 5 | 0.2275 (0.2530) | 0.2675 (0.2523) |
| 7 | 0.2475 (0.2543) | 0.2650 (0.2511) |
| 8 | 0.2250 (0.2502) | 0.2625 (0.2490) |

All five probes were below their nulls; all five nearest-average
accuracies are above theirs. **The systematic below-null pattern is not
reproduced by a difference-of-averages read of the same states.** That
suggests the below-null pattern was a property of fitting a regularised
classifier to these states, not a property of the states themselves — a
classifier that finds nothing can score below a shuffled-label classifier
when the shuffling happens to regularise it.

Two cautions, both real. The spread of the null was not recorded for this
secondary number, because it carries no outcome cell, so "above the null
mean" is the whole of what can be claimed from that column — not "above
by any particular margin". And on seeds 1 and 2 the same column is mixed,
sitting both above and below its nulls. The pattern is worth noticing and
is not worth more than noticing.

## What this does and does not establish

**Does.** Own-agent identity is not linearly decodable at the registered
probe positions on any A3 checkpoint in hand, by a difference of
averages, with or without the denoising step, at a bar of three standard
deviations over a permutation null. The specific rescue item 2 proposed —
that nuisance variance was swamping a small ownership signal — is not
what happened, and the geometry says why.

**Does not.** It does not show that no self-structure exists in these
models. It tests one position (the revision position), five layers, a
linear read, and 400 episodes. Ownership is *measured* to be load-bearing
on the pilot: zeroing the acting channel takes the ownership battery from
0.506 to 0.182. Something carries that, and this diagnostic did not find
it. The gap between "the action depends on ownership" and "ownership is
not linearly legible where we look" is the live problem, and it is now
better described than it was this morning.

**Where that leaves the localization stack.** The reading that the stack
is insensitive rather than the signal absent is *not* supported by this
test — that was the SEPARATES cell and it did not fire. But nor is it
ruled out: a ten-dimensional state space at the probed position is a
reason to doubt the probe *position*, not only the probe. The natural
next question is whether ownership is legible anywhere — other positions,
other layers, a non-linear read — and that is a different experiment with
its own method file, not a rerun of this one with the knobs moved.

## Record

- Outputs: `a3-gates/denoised_direction_a3_a3_30m_seed0.json`,
  `…seed1.json`, `…seed2.json`, and
  `a3-gates/denoised_direction_a3_summary.json`. Fresh files, nothing
  overwritten.
- Method committed before output: `denoised-direction-method.md`.
- Implementation: `src/denoised_direction_a3.py`.
- Runtime about 47 seconds per checkpoint on a laptop. No spend.
- Gated on the known-answer test, which passes. Not gated on the
  threshold lock, and the method file says why.
