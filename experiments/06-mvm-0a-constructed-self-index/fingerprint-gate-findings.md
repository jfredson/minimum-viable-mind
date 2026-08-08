# Gate run (iii) findings — FAIL: the model's rollouts carry an ownership fingerprint (2026-08-08)

*RT-08's third run, built and run against the pilot checkpoint
(`artifacts/pilot-10m-seed0/`, md5 `d63a85a…`) the day the checkpoint
existed. **The gate FAILED on both arms, with both positive controls
firing** — the detector has standing, and the cue is real. This is the
outcome RT-02 predicted ("the route most likely to survive"), and it
blocks the 5-seed spend under the registered rule: any cue-detector
failure regenerates the design element that leaks. Numbers below are
the pre-committed n = 4000 record (`cue_detector_gate.json`); the
n = 300 shakeout agreed (A 0.668 [0.590, 0.749], B 0.885
[0.857, 0.912]) — the verdict never depended on n.*

## Result (n = 4000, seed 20260808)

| arm | clean AUC [95% CI] | bound | positive control | verdict |
|---|---|---|---|---|
| A — committed family (runs i/ii detector) on model-filled text | **0.7076** [0.6872, 0.7279] | [0.45, 0.55] | 0.9361 (constant filler) ✓ | **FAIL** |
| B — likelihood attack (turn values scored under the model's own policy) | **0.8731** [0.8650, 0.8807] | [0.45, 0.55] | 0.9054 (greedy fill) ✓ | **FAIL** |

Both CIs exclude the equivalence bound entirely — the verdict does not
depend on n.

## The cue, diagnosed

**The model has a favorite bay.** Its fill-position policy is far from
the generator's uniform: over 800 fresh episodes, own-turn values hit
`bay_D` 41.6% and `bay_F` 19.6% (uniform = 12.5%), own-value entropy
1.73 nats vs 2.08 uniform, while other agents' generator-drawn turns
stay flat. Mechanism: **the training loss only ever touched answer
tokens**, so the fill-position distribution was never trained toward
anything — it is an incidental byproduct of the trunk, and it is
biased. A solver can tag high-policy-likelihood turns as "probably
mine" and shortcut ownership tracking with no self-index — the exact
mimicry-adjacent channel the standing rules say to discount.

## The deeper finding: RT-02 and RT-08 squeeze the design from both sides

In the current fill-then-train pipeline, the model consumes a completed
episode cold; the generation-time computation is discarded. So the ONLY
thing that marks own turns as own is their sampling distribution.
That leaves two branches, both bad:

- the policy differs from the generator → the ownership cue leaks
  (this failure);
- the policy is made indistinguishable from the generator → own turns
  carry no signal at all, and "you" has nothing to be learned FROM in a
  fill-then-train pipeline (symmetrizing the source destroys the task).

Which means the two red-team constraints — authorship-grounded identity
[RT-02] and no distributional cue [RT-08] — are jointly satisfiable
only if identity is carried by something OTHER than token statistics.
The candidate that does this is architectural: **in-context generation**
— the model's own turns generated inside the same forward pass whose
register state persists across the episode, so "own" is grounded in
computational continuity (the register state at generation time is part
of the same computation the training loss reads), not in the
distribution of the emitted tokens. The gate is, in effect, forcing the
design from *identity as statistical signature* toward *identity as
continuity of state* — which is considerably closer to what the corpus
means by a self-index (`calibration-problem` ch. 5) than the fill
pipeline was.

## Disposition candidates (John adjudicates; red-team pass on the chosen fix before re-registration)

1. **(a) Calibrated fill** — keep fill-then-train but reshape the fill
   distribution to the generator's marginal (temperature, or explicit
   marginal calibration). Kills arm A's cue cheaply; arm B survives if
   context-conditional sharpness remains. A measurement, not a
   guarantee — re-gate after.
2. **(c) In-context generation** — own turns generated within the
   training forward, register state continuous (the fix the §above
   argues for). Architecturally honest; does not by itself remove the
   text-level cue, so it composes with (a). Larger code change; touches
   §Materials, so it is a registered amendment.
3. **(b) Symmetrize the source** (model generates all agents' turns) —
   rejected in analysis: it removes the own/other contrast entirely in
   a fill-then-train pipeline and the task becomes unlearnable; noted
   because *why* it fails is the deeper finding above.
4. Fold in the already-filed **RT-11 amendment** (revision contrast must
   survive fill — `pilot-findings.md` caveat 2) in the same amendment
   cycle, one red-team pass over both.

**Whatever is chosen: re-run gates (i)–(iii) on the fixed pipeline
before any 5-seed spend.** The pilot's learnability result stands (the
model learns the task as posed), but the task-as-posed leaks, so the
5-seed run on the current pipeline would measure a solver with a
shortcut available — exactly what the anti-router design exists to
exclude.

## Scoreboard for the gates-before-model discipline

Four real catches, zero GPU dollars wasted on a confounded design:
the RT-11×RT-02 patch interaction (run i), the sampler position
asymmetry (run i, harness-side), the stale T_state answers after fill
(build), and now the policy fingerprint (run iii) — the one that would
have silently underwritten a false H_load-bearing headline.
