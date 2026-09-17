# Known-answer test of the localization pipeline — PASS

*2026-09-16. Ruled by John, criteria committed before any output at
`79bd815`. Unregistered and labelled so. Local, $0, inference only.*

## Verdict

**PASS**, at ceiling and by a wide margin.

| quantity | value |
|---|---|
| probe accuracy | 1.0000 |
| null mean | 0.1306 |
| null standard deviation | 0.0264 |
| margin | 32.91 sd |
| chance, eight slots | 0.1250 |
| majority-class rate | 0.1762 |
| episodes probed | 193 |

The pre-stated bar was 0.95 with a non-degenerate null and clearance by
three standard deviations. The null is healthy, the accuracy is perfect,
and the margin is roughly eleven times the bar.

The denominator is 193 rather than 400 because the ownership action is
scored only where the model actually revises, which is by design: making
the model revise every episode is what would let an ownership-blind
solver work out which agent it is.

## What passes, and what that licenses

Residual capture, position indexing, probe fitting and label-permutation
null construction all work. A value present at the probed position is
recovered perfectly.

Per John's pre-stated reading, that means **tonight's failure to find
ownership structure is about the localization stack at this scale, not
about the code.**

## What the test did not exercise, stated plainly

The verdict above is the pre-stated one and is not being reinterpreted.
This section adds scope, not a bin.

The test probes **layer 0** at the **acting-channel position**. The blind
control probed **layers 3, 5, 7 and 8** at **revision positions**, and
then took a subspace and ablated it. So the known-answer test validates
the machinery those two runs share, and leaves three things unexercised:

1. The position choice used in the blind runs. Reading revision positions
   is the A3 pipeline's registered choice and nothing here tests it.
2. The deeper-layer capture path, though it is the same code with a
   different index.
3. **The ablation path entirely** — the subspace construction and the
   ablation hook. Nothing in this test touches them.

So the honest statement is that the plumbing under the probe is sound.
A bug living specifically in the ablation path would not have been caught
here, and the ablation result has separately been shown to carry no
information anyway.

## The diagnostic, which matters for how the pass is described

Pre-stated with no bin attached: the same probe with the acting channel
**zeroed**.

| arm | accuracy | margin |
|---|---|---|
| acting channel live | 1.0000 | 32.91 sd |
| acting channel zeroed | 1.0000 | 31.30 sd |

Identical. The target decodes perfectly either way, so the decodability
comes from the value token's own embedding sitting at that position, not
from the acting channel.

This is exactly the case the pre-stated note anticipated: *"If the target
decodes either way, the pass shows the plumbing works and says nothing
about the acting channel specifically."* The pass is a plumbing check and
should be described as one. It is not evidence that the pipeline can read
what the acting channel contributes.

## The gate

John's ruling: no A3 L1 localization read on any seed until this passes.
It passes, so the gate lifts. Verified mechanically: `require_known_answer_pass`
now accepts, and the threshold lock still refuses an L1 read independently
when no lock is supplied. Both checks remain in force and the gate is
checked before the lock.

The gate lifting is permission, not instruction. No L1 read has been run
on any seed, the seeds are still training, and John authorises runs.

The L0 direct lesion was never gated and proceeds as registered.
