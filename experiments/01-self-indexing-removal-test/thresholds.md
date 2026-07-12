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

Model: `google/gemma-2-2b-it` @ `main` (**pilot / instrument sandbox only**;
decided 2026-06-23, red-team RT-05/06/08). The **registered run moves to a
less-RLHF'd, lightly-aligned instruction model** — preferably a staged-checkpoint
family (base → SFT → DPO → RLHF, e.g. OLMo-2 / Tülu) so RT-06's capability-gating
can be measured directly — and T and S are **re-baselined there**. Specific model
still to be pinned (see `red_team_ledger.md` Pass 2 substrate decision).

| Quantity | Baseline | Source |
|---|---|---|
| `T_base` (overall) | **0.750** (15/20) | `artifacts/stage0_baseline/task_results.json` |
| &nbsp;&nbsp;multi_step_reasoning | 1.000 (5/5) | " |
| &nbsp;&nbsp;needle_synthesis | 1.000 (5/5) | " |
| &nbsp;&nbsp;coreference_binding | 0.800 (4/5) | " |
| &nbsp;&nbsp;instruction_following | 0.200 (1/5) | " |
| `S_base` (fidelity) | **0.615** | `artifacts/stage0_baseline/self_report_scores.json` |
| &nbsp;&nbsp;first_person_activity | 0.719 | " |
| &nbsp;&nbsp;self_monitoring | 0.594 | " |
| &nbsp;&nbsp;self_vs_other | 0.531 | " |

`S_base` scored by the held-out judge `claude-opus-4-8` (≠ the model under test)
against the locked rubric; a human spot-check of the high/low items confirmed the
judge applies the rubric (catching self-contradiction, second-person framing, and
flat metaphysical denial) rather than rubber-stamping.

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

## Red-team pilot additions (2026-06-23)

From the adversarial design review (`red_team_ledger.md`, findings RT-01/RT-02;
pass 2 adds RT-05/RT-06/RT-07/RT-08 below). All must run on the pilot set
**before** the thresholds below are locked.

- **Activation-frequency control on the C_ctrl match (RT-01).** "Comparable
  causal centrality" may be confounded by the base-rate activation-frequency
  asymmetry between the I/Assistant persona and any third-person entity — so the
  C_self−C_ctrl gap could track raw frequency rather than self-vs-other identity.
  Pilot: (1) measure activation frequency of C_self and each C_ctrl on T-overall
  and report the asymmetry; (2) construct at least one C_ctrl matched on causal
  centrality estimated on a **neutral third corpus** (neither T nor S items);
  (3) regress `d_task` on activation frequency and check the C_self−C_ctrl gap
  survives the frequency control. **Pre-register a maximum acceptable
  frequency-asymmetry** between C_self and the C_ctrl cloud before `δ` is locked.
  **Loss condition:** if the gap does not survive the frequency control, invoke
  the registered "differential is dead" loss condition — do not lock `δ`.

- **T-split coherence check (RT-02).** Before locking, confirm the two T subsets
  behave coherently under C_self ablation. Report `d_task^si` and `d_task^sr`
  separately on the pilot set. **Loss condition / reading:** if they are
  statistically indistinguishable, the scrubbed-T design is vindicated and the
  single-T rule was safe; if self-relevant binding degrades sharply while
  self-irrelevant does not, the original single-T rule was biased toward
  H_description — the "floor-consistent, restricted" outcome (see
  `pre-registration.md`) applies and must be scored, not collapsed into
  description-only.

- **θ_self baseline note (RT-03 follow-up).** The S rubric is being revised to
  score self-tracking independent of first-person grammar (rubric v2). `θ_self`
  must be set against a **re-scored `S_base` under rubric v2**, not the v1
  `S_base = 0.615` recorded above. Re-baseline S before locking `θ_self`.

### Pass 2 additions (2026-06-23) — RT-05/RT-06/RT-07/RT-08

- **`T_syntax` router control (RT-05).** C_self-index is localized from a
  model-turn-vs-user-turn contrast, which aligns with ChatML dialogue-boundary
  tokens — it may be a *syntax router*, not a self-center. Pilot: add a `T_syntax`
  task that requires turn/boundary tracking but **zero reasoning or synthesis**,
  and report `d_task^syntax` under C_self-index ablation alongside `d_task^sr`.
  **Loss condition:** if `d_task^syntax ≈ d_task^sr`, C_self-index is a dialogue-
  state router and an H_center result on it is void — do not report it as a center.

- **Capability-gating, third-person-verified C_ctrl (RT-06).** RLHF gates the
  model's strongest reasoning to its Assistant persona, so ablating C_self can
  damage the *gate* to the task circuits and beat a passive third-person C_ctrl by
  construction. So C_ctrl must include at least one **capability-gating** persona
  (an expert/system-prompt mode that also keys high-capability reasoning), **and**
  that control must be verified to read as a *third-person object* — not as an
  adopted first-person self — via the separability check (`separate_self.py`:
  low cross-decode with C_self) **before** it is used. **Loss condition
  (maintained on rebuttal):** if no capability-gating C_ctrl can be kept third-
  person (it reads as C_self), the differential is dead for this model class —
  invoke "not testable here yet", do not lock `δ` or report H_center. This is
  **substrate-dependent**: decide the registered-run model (see `red_team_ledger.md`
  Pass 2 "Substrate decision") before running this pilot.

- **OOD perplexity gate (RT-07, PATCH).** Mean/zero-ablating a high-magnitude
  central vector can push the residual off-manifold (perplexity explosion) and be
  misread as degraded integration. Add a **neutral-corpus** (e.g. Wikipedia)
  perplexity check: if ablating C_self inflates base perplexity past a pre-set
  bound *relative to C_ctrl*, the run is **OOD-inconclusive**, not H_center. Keep
  mean-ablation as the registered primary and **report all three** (mean/zero/
  directional); directional serves as the OOD-minimizing cross-check. Pre-register
  the perplexity-inflation bound before the test set.

- **Attention-sink (RT-08, folded into RT-07).** The objection that ablation
  destroys integration via softmax/attention-sink collapse rather than via removing
  a center is screened by the RT-07 OOD perplexity gate plus the differential.
  Kept as a *secondary* sink-restoration check (does a content-free dummy token
  absorbing the attention mass recover performance?), promoted to required only if
  the OOD gate + differential fail to screen it in pilot.

### Pass 3 addition (2026-07-01) — RT-09 (external review, not from the Gemini loop)

- **Generic-speaker reflexivity control (RT-09).** RT-05 screens the syntax-router
  reading of C_self-index; RT-09 screens the deflation that survives it — that
  C_self-index is **generic speaker-slot tracking** (present for any observed
  dialogue, with the assistant merely occupying one slot), not a *reflexive*
  self-index. Pilot, before lock: localize C_speaker-generic from the
  `observed_speaker` contrast (third-party transcript inside a single user turn;
  model participates in neither condition; same embedding-floor and
  permutation-null gates), then run the RT-04 three-way geometry
  (`separate_self.py`) **and** the causal cross-patch (`patch_context.py`)
  against C_self-index. **Pre-registered decision rule:** generic if cross-decode
  ≥ 0.9 AUC **and** |cos| ≥ 0.5 **and** cross-patch restoration ratio ≥ 0.5.
  **Loss condition:** generic verdict ⇒ "reflexivity not established" — no
  H_center attaches to C_self-index as localized; do not lock `δ`/`θ` against it.
  Partial separation ⇒ project C_speaker-generic out and the **residual** becomes
  the removal-test target (primary), per the pre-registration amendment.

### Pass 4 addition (2026-07-12) — RT-10 (empirical, from the RT-09 first pass)

- **Length/depth deflation control (RT-10).** The RT-09 first pass found the
  turns-based stimuli confound label with token count (perfectly, non-overlapping
  ranges) — so C_self-index, C_self-narrative, and C_speaker-generic as localized
  may partly be a context-length tracker. Before lock: (a) regenerate the context
  stimuli **length-matched** (polarity-balanced fillers; verified by
  `check_length_confound.py`: label-from-token-count ~chance, length-direction
  AUC ~0.5) and re-run localization, the RT-04/RT-09 geometry, and the causal
  patching on v2; (b) `patch_context.py` gains a **length-direction control**
  next to the random one — C_self-index must beat it by the same ≥ 0.10 gap.
  **Loss condition:** turn_role signal collapses under length matching, or
  C_self-index fails to beat the length-direction patch ⇒ the localized
  direction is a length tracker; no `δ`/`θ` lock against it, localization redone.
- **RT-09 status:** first pass (original stimuli) did **not** fire the rule —
  |cos| 0.224 (< 0.5), cross-patch ratio 0.006 (< 0.5); cross-decode 1.000 was
  length-inflated. Recorded as **provisional**; the unchanged rule is re-applied
  on the v2 stimuli. RT-09 continues to gate `δ`/`θ` lock alongside RT-05/RT-10.
- **Outcomes on the v2 stimuli (2026-07-12, pilot sandbox `gemma-2-2b-it`):**
  the length gate **passed** (label-from-token-count 0.40–0.52 ≈ chance;
  length-direction AUC ~0.50; narrative carries a mild 0.56–0.57 residual —
  noted, not cleared away). **RT-10: both controls passed** — turn_role keeps a
  clean-floor computed signal (peak L15, margin +0.55) and C_self beats the
  length-direction patch 0.340 vs 0.012 (gap +0.328 ≥ 0.10). **RT-09: the rule
  did not fire** on a now-valid control (gen own-AUC 0.75–0.86 in band):
  cross-decode 1.000 ✓ but |cos| 0.148 ✗ and cross-patch ratio −0.005 ✗.
  Shared decodable component is real ⇒ per the pre-registered
  partial-separation path, the removal test targets the **residual**
  (C_self-index ⊥ C_speaker-generic; residual decodes at 1.0). Scope: these
  resolutions are on the pilot sandbox — **re-verify on the registered
  substrate before `δ`/`θ` lock**, like every other pilot gate.
- **RT-04 cross-patch outcome (2026-07-12, v2 stimuli, pilot sandbox):**
  **functionally separable** (`cross_patch_self.py`, convention registered at
  `5bfda70` before running). Both own patches valid (index 0.340, narrative
  0.338 at L22, random ~0) — the first *causal* confirmation of
  C_self-narrative — and both cross-patch ratios are below the 0.5 line
  (narr→index 0.282, index→narr 0.273). The shared geometric component
  substitutes at only ~27%: real, subordinate, reported. The removal test runs
  on each structure independently; same re-verify-on-registered-substrate
  scope as above.

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
