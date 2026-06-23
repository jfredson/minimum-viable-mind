# Experiment 1 — Locked thresholds (θ_task, θ_self, δ)

*Companion to `pre-registration.md`. The pre-registration commits the decision
rule; this file commits the three numbers that rule turns on. Per the
pre-registration and `experiments/README.md`, the thresholds are set during
Stage 0 piloting on a **held-out pilot set** and committed **before the test set
is touched** — and never adjusted after seeing the test results.*

**Status: PILOTING — structure committed, values not yet locked.** The `θ_task`,
`θ_self`, and `δ` cells below are `TBD`. They get filled from pilot data (Stage 1
localization + ablation on the pilot set) and committed in a *separate* commit
before any test-set run, so the order is auditable in git history.

## The rule these numbers serve

For an ablation `A`, with all scores relative to the unmodified-model baseline:

- `d_task(A)` = relative drop in T accuracy = `(T_base − T_A) / T_base`.
- `d_self(A)` = relative drop in S fidelity = `(S_base − S_A) / S_base`.

The discriminator (verbatim intent from the pre-registration):

- **Floor-consistent (H_center):** `d_task(C_self) ≥ θ_task` **and**
  `d_task(C_self) − d_task(C_ctrl) ≥ δ`.
- **Description-only (H_description):** `d_self(C_self) ≥ θ_self` **and**
  `d_task(C_self) < θ_task` **and** `d_task(C_self) − d_task(C_ctrl) < δ`.
- **Inconclusive:** anything else.

So `θ_task` is the bar for "integration was degraded at all," `δ` is the bar for
"degraded *specifically* by the self-locating structure vs. matched controls,"
and `θ_self` is the bar for "the first-person report was subtracted."

## Baselines on the unmodified model (the denominators above)

Model: `google/gemma-2-2b-it` @ `main` (pilot model; bumps to Gemma-2-9B for the
registered run — re-baseline there).

| Quantity | Baseline | Source |
|---|---|---|
| `T_base` (overall) | **0.750** (15/20) | `artifacts/stage0_baseline/task_results.json` |
| &nbsp;&nbsp;multi_step_reasoning | 1.000 (5/5) | " |
| &nbsp;&nbsp;needle_synthesis | 1.000 (5/5) | " |
| &nbsp;&nbsp;coreference_binding | 0.800 (4/5) | " |
| &nbsp;&nbsp;instruction_following | 0.200 (1/5) | " |
| `S_base` (fidelity) | **TBD** (held-out judge) | `artifacts/stage0_baseline/self_report_scores.json` |

**Piloting note already in hand:** `instruction_following` baselines near the
floor (0.20), so it has little room to show a *measurable* drop under ablation
(a floor effect). Compute `d_task` on **T-overall** and treat the three
high-baseline categories as the primary drop signal; instruction_following is
qualitative/supporting, not a primary discriminator.

## How each threshold gets set (the piloting procedure)

The pilot set is **disjoint from the test set** and from each other (T and S
items kept separate so a self-report cue can't ride along in a task item). It is
used only to estimate effect sizes and noise — never to score the registered
result.

- **`θ_task` — "integration degraded at all."** Set above the *noise band* of
  `d_task` under interventions that should not touch integration: norm-matched
  random-direction ablations and, ideally, a no-op/identity control, measured on
  the pilot set. `θ_task` is the upper edge of that band (e.g. mean + k·SD of the
  null `d_task`), so a drop that clears it is unlikely to be generic damage.

- **`δ` — "degraded *specifically* by the self-locating structure."** This is the
  load-bearing one (the differential makes the test a test). Set above the
  *spread of `d_task(C_ctrl)`* across the several matched control structures
  C_ctrl (other-entity models at comparable probe accuracy and causal centrality)
  on the pilot set. `δ` must exceed how much `d_task` varies just from *which*
  comparable non-self component you ablate — otherwise the C_self−C_ctrl gap is
  within control-choice noise and means nothing (see the loss condition below).

- **`θ_self` — "the report was subtracted."** Set above the noise band of
  `d_self` under the same null interventions used for `θ_task`. A self-report
  fidelity drop that clears `θ_self` is one the judge would not have assigned to
  ordinary scoring variation. Requires `S_base` first (run `judge.py`).

Candidate framing only (NOT locked): a drop is "real" when it clears its null
band with margin; `δ` is meaningful only if the pilot shows
`d_task(C_self)` separating cleanly from the C_ctrl cloud. If the pilot shows it
does not, the differential discriminator is dead for this model — that is a
registered loss condition, not a threshold to lower until it passes.

## The locked values

To be filled from pilot data and committed before the test set runs. Until then,
the test set must not be scored.

| Threshold | Locked value | Basis (pilot artifact + commit) |
|---|---|---|
| `θ_task` | **TBD** | |
| `θ_self` | **TBD** | |
| `δ` | **TBD** | |

Pre-registration commit this locks against: *(fill the hash of the
`pre-registration.md` commit when locking — `git log --oneline -- experiments/01-self-indexing-removal-test/pre-registration.md`).*

## Loss conditions carried from the pre-registration

- If `d_task(C_ctrl)` is consistently as large as `d_task(C_self)` across many
  control choices, the differential is dead for this model — revise the matching
  or abandon the design. Do not shrink `δ` to manufacture a result.
- If the two localization methods disagree on C_self, the experiment is
  inconclusive by construction; report the disagreement.
- If floor-consistent and description-only signatures both appear under
  different-but-equally-valid ablation methods (mean vs. directional), the test
  is underdetermined as specified — tighten the operationalization before any
  claim.
