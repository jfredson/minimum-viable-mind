# The twin-binding anomaly (waves 1–2 of the registered 5-seed run)

*2026-08-18. Status: **finding recorded, not adjudicated**. The read on
what this means for the registered remainder is John's, at the analysis
point. Nothing here emits a verdict on H_load-bearing.*

## What we predicted, and what happened

The registered design pairs every full run with a **twin**: the same
recipe with the self-register parameters removed. The pre-stated
prediction (`pre-registration.md` §Materials, `launch-plan-5seed.md`
per-wave wrap item 3) is that **the twin SHOULD FAIL the self batteries
— no register, no binding** — and that this failure is what licenses
reading a full run's T_si/T_sr_rev as evidence that the constructed
self-index is doing work.

Across the five registered-recipe runs completed so far, that prediction
held once, failed once, and the fulls themselves split 1-in-3:

| run | register? | endpoint T_si | endpoint T_sr_rev | final loss | bound? |
|---|---|---|---|---|---|
| pilot seed-0 full (`fd1eb80c…`) | yes | 0.93 | 1.00 | ~0.43 | **yes** |
| seed-0 twin (`ae77f8aa…`) | no | 0.31 | 0.00 | ~0.47 | no *(as designed)* |
| seed-1 full (`5d8ad907…`) | yes | 0.33 | 0.00 | 0.4301 | **no** |
| **seed-1 twin (`b1e6fc2a…`)** | **no** | **0.96** | **1.00** | **0.0001** | **YES ⚠** |
| seed-2 full (`7424d14f…`) | yes | 0.35 | 0.00 | 0.4765 | **no** |

All five reached the full registered token budget (784,089,600 tok,
102,095 steps) with T_syntax 1.00 and T_state ≈0.99–1.00 — the grammar
and world-state batteries are at ceiling everywhere, so nothing here is
a training failure. The self batteries are the whole story.

## Why this is the serious kind of surprise

**A twin at ceiling means the batteries are solvable without the
register.** The twin exists to be the floor; when the floor scores 0.96
on T_si and 1.00 on T_sr_rev, the batteries stop licensing the inference
they were registered to license. This is RT-17's concern arriving in the
data rather than in a red-team note: the instrument may be measuring a
capability that mimicry (or memorization) fully explains, which the
standing rule says to discount.

**The seed-1 inversion**: the full model, which *had* the register,
missed the solution its own ablation found. Capacity was not the
constraint.

**The loss column is anomalous but does NOT mean memorization.**
Every other run — full or twin, binding or not — converges to
~0.43–0.48; the binding twin drove *training* loss to **0.0001**, four
orders of magnitude lower. Loss is comparable across the two
architectures (the non-binding twin sits at ~0.47, same band as the
fulls), so the collapse is specific to this one run, not an artifact of
removing the register.

**Corrected 2026-08-18 (this note's first draft got this wrong):** the
obvious memorization reading is *not* available. `train.py`'s
`eval_heldout` generates episodes from the same grammar with **disjoint
content seeds**, and own turns are enacted by the model in that eval's
own forward passes (`src/train.py:172`). The twin's 0.96/1.00 is
therefore measured on episodes it never trained on — it **generalizes**.
The honest reading of loss 0.0001 is that this run found a crisp,
near-deterministic algorithm that fits the closed grammar almost
exactly, not that it memorized the eval. That makes the construct
problem *worse*, not better: the alternative solution is real and it
transfers.

**Binding looks seed-dependent, not architecture-dependent.** 1 of 3
fulls and 1 of 2 twins bound. With n=100 per eval the run-to-run swings
(e.g. seed-2 wandering 0.26 → 0.43 → 0.31 → 0.35 across late checkpoints
while never leaving the flat band) are consistent with noise around a
non-binding baseline, not with slow drift toward binding.

## What this is NOT

- **Not a C5 trigger.** Nothing optimized against, evaded, or degraded
  the instruments. A model found a legitimate solution the design did
  not anticipate; the design's wager lost honestly. C5 governs
  adversarial behavior toward the monitoring machinery, and none
  occurred. Runs completed normally and were reaped normally.
- **Not a verdict on H_load-bearing.** The main question is untouched:
  we cannot yet say whether the self-index is load-bearing, because we
  no longer trust the instrument to distinguish "bound" from "solved
  another way."
- **Not a training bug.** Config headers verified on the live pods
  (`twin=True params=29.3M` for twins vs `twin=False params=39.2M` for
  fulls); the seed-1 twin's live process carried `--twin`. The
  hand-repaired launch of seed-1 twin used the registered recipe
  verbatim (`compute-ledger.md` 2026-08-17 row).

## Gate (iii) run against all four checkpoints (2026-08-18, $0, local)

Ran the registered fingerprint gate (`src/fingerprint_gate.py`, n=4000,
equivalence bound [0.45, 0.55], `positive_control_min_auc` 0.70) against
each 30M checkpoint. Runs (i) and (ii) are checkpoint-independent and
pass everywhere; arm A of run (iii) is also checkpoint-independent in
practice (its "enact" text is generator-drawn, so it returns bit-identical
numbers across checkpoints — expected, not a bug). **Arm B, the
likelihood attack, is the only checkpoint-sensitive leg:**

| checkpoint | arch | bound | clean AUC | pc greedy | pc policy | pc_pass | GATE |
|---|---|---|---|---|---|---|---|
| pilot seed-0 full | full | yes | 0.4964 | 0.9312 | 0.8248 | **pass** | PASS |
| seed-1 full | full | no | 0.5052 | 0.7079 | 0.5955 | fail | FAIL |
| seed-0 twin | twin | no | 0.5052 | 0.6961 | 0.6538 | fail | FAIL |
| seed-1 twin | twin | **yes** | 0.4950 | 0.7732 | 0.6519 | fail | FAIL |

**How to read this — and what it is NOT.** Every clean arm sits inside
the equivalence bound, so **there is no evidence of a rollout
fingerprint anywhere**. All three FAILs are *positive-control* failures:
the detector could not recover a **planted** leak, so it has no
demonstrated sensitivity on those checkpoints and cannot certify them
either way. An uncertifiable instrument is the finding.

The first draft of this note predicted the twin's gate result would give
"direct support" for a shortcut/memorization story. **It did not, and
that prediction was wrong.** The non-binding twin fails the positive
control too (0.6961/0.6538 ≈ the binding twin's 0.7732/0.6519), so the
collapse does not track binding — and the non-binding *full* fails as
well (0.7079/0.5955), so it does not cleanly track architecture either.
With n=1 per cell the only defensible statement is the narrow one:
**arm B's positive control has demonstrated sensitivity on exactly one
checkpoint — the pilot — and on none of the three registered-run
checkpoints.**

Procedural note: gate (iii) was the precondition *for* the 5-seed spend
and was satisfied at the registered scale by the pilot checkpoint; these
per-seed runs are diagnostic, not a retroactive gate on work already
done. But an instrument that only demonstrates sensitivity on the one
checkpoint it was validated against is a live problem for the analysis
phase, independent of the twin anomaly.

**Artifact hazard found and worked around:** `fingerprint_gate.py`
writes to a single fixed path (`cue_detector_gate.json`) and replaces
its run-(iii) entry, so gating a second checkpoint silently clobbers the
first — this run overwrote the pilot's committed PASS record before it
was caught. The canonical file has been restored from git and each
checkpoint's result is now kept beside its own artifacts as
`artifacts/<run>/cue_detector_gate_<run>.json`. Fix the script's output
path before the analysis phase [C6: artifacts must answer later
questions].

## Diagnostic threads, cheap and already-purchased

All five checkpoints are local and non-promotable [C1]. These cost
compute in the single-dollar range, not the ~$130 the registered
remainder would cost:

1. ~~**Gate (iii) on the binding twin.**~~ **DONE 2026-08-18** — see the
   gate section above. Result did not support the shortcut hypothesis;
   what it surfaced instead is that the detector's positive control has
   no demonstrated sensitivity on any registered-run checkpoint.
2. ~~**Train/held-out gap on the binding twin.**~~ **ANSWERED without new
   compute** — the batteries were *already* scored on held-out episodes
   with disjoint content seeds (`train.py:172`), so the twin's 0.96
   generalizes and the memorization reading is off the table.
3. **Cross-seed battery item analysis.** Are the twin's T_si successes
   concentrated on items with particular structure (revision depth,
   referent distance, lexical overlap with the training grammar)? An
   item-level split is the cheapest remaining route to "what is the
   alternative algorithm actually keying on."
4. **Ablate the register at inference — the decisive test, still to
   run.** Zero/lesion the register in the *bound pilot* checkpoint and
   re-score T_si/T_sr_rev. If the pilot's binding survives the lesion,
   then even the one clean success was never register-dependent and the
   construct problem is total rather than partial. This is the single
   highest-information diagnostic left and it needs no new training —
   only an inference-time harness.
5. **θ/δ null calibration** (already registered, `~$2–5`) — the noise
   floor these late-checkpoint swings should be judged against. With
   eval n=100 per battery, seed-2's late wander (0.26 → 0.43 → 0.31 →
   0.35) is very likely inside it.
6. **Fix `fingerprint_gate.py`'s fixed output path** before any further
   gating (see hazard note above).

## The open decision (John's)

The registered remainder is 7 runs ≈ **$130** of the ~$219 left under
the A2 ceiling. The question is not whether the design is interesting
but whether those 7 runs answer the live question. As of this note the
live question changed: it is now **"what computation solves these
batteries?"**, and more seeds measure the variance of an instrument whose
construct validity is in doubt. Wave 3 is therefore **not authorized**;
Claude will not launch it absent a fresh go [C2 v1.1]. The options as
they stand — continue as registered, pause for the diagnostics above and
re-decide, or amend the battery design — are John's to weigh, and any
change to the registered plan is itself a registered amendment.
