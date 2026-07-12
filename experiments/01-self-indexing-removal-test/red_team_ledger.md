# Red-team ledger — Experiment 1

*The durable, human-curated record of the adversarial design review. One row per
finding, one disposition per row, each with the reason it was disposed of that
way. This is to the experiment design what the corpus-positions ledger is to the
philosophy: an auditable trail of what was challenged and how it was answered.*

**This file is curated by John, not generated.** `red_team.py` (Gemini, the
attacker) and `defend.py` (Claude, the stake-free defender) produce machine
artifacts in `artifacts/red_team/` — findings, dispositions, and a
`proposed_ledger_*.md` of suggested rows. Those proposals are *inputs*. A row
lands here only after John adjudicates it. The defender's disposition is a
recommendation; the decision is the human's.

## The loop

1. **Attack** — `red_team.py` → `findings_*.json` (Gemini 3.1 Pro).
2. **Defend** — `defend.py` → `adjudication_*.json` + `proposed_ledger_*.md`
   (Claude assigns a disposition + loss condition per finding).
3. **Rebut** — `defend.py --rebut` → one bounded Gemini counter-round, so the
   defender does not get the last word.
4. **Adjudicate** — John decides the `for-John` rows, then merges the result
   into the table below.

## Dispositions

- **PATCH** — design changes; links to the commit or pre-registration amendment.
- **ACCEPTED-RISK** — limitation the design will live with; must be recorded as a
  stated loss condition in `pre-registration.md`.
- **ROUTED-UPSTREAM** — theory-level; owned by `sentient-horizons` /
  `calibration-problem`, not patched here.
- **PILOT-REQUIRED** — settled by data, not argument; added to the Stage 0 pilot.
- **REJECTED** — finding declined (e.g. proves-too-much); record the broader
  principle it violated.

## Hard gate

Every PATCH disposition must land **before** `θ_task`, `θ_self`, `δ` are
committed in `thresholds.md`. The pre-registration forbids changing the design
after the test set is in view, so the red-team loop runs — and its patches are
applied — during Stage 0, not after.

## Ledger

### Pass 2026-06-23 — Gemini 3.1 Pro attack, Claude Opus 4.8 defense, Gemini rebuttal

Five-doc attack (`artifacts/red_team/findings_20260623T200321Z.json`),
adjudicated (`adjudication_20260623T200425Z.json`). The bounded rebuttal round
had the attacker **concede all four** dispositions. All four bear on construct
validity or the registered rule; adjudicated by John and patched pre-lock.

| id | date | severity | target | disposition | resolution | loss condition recorded |
|----|------|----------|--------|-------------|------------|-------------------------|
| RT-01 | 2026-06-23 | high | design | PILOT-REQUIRED | `thresholds.md` §Red-team pilot additions: activation-frequency control on the C_ctrl match | C_self−C_ctrl gap must survive the activation-frequency control, else the "differential is dead" loss condition fires (no `δ` lock) |
| RT-02 | 2026-06-23 | high | design | PILOT-REQUIRED + decision-rule PATCH | `pre-registration.md`: T split (self-relevant / self-irrelevant) + new "floor-consistent, restricted" outcome; `thresholds.md` T-split coherence check | if self-relevant binding degrades while self-irrelevant survives → restricted outcome, **not** H_description; if indistinguishable, scrubbed-T design vindicated |
| RT-03 | 2026-06-23 | medium | design | PATCH | `pre-registration.md` §S battery: forced-third-person scoring, grammar-decoupled; **follow-up: rubric v2 + S re-baseline before test run** | if third-person framing degrades self-tracking in the unablated baseline → revert to PILOT-REQUIRED (grammar-independent probe needed) |
| RT-04 | 2026-06-23 | medium | design | PATCH | `pre-registration.md` §Localization: localize + test both C_self-narrative and C_self-index (per research note §4(a)) | if the two cannot be separated by any method → record non-separability; the Metzinger objection stands open |

**Open follow-ups before thresholds lock:** RT-01 frequency-control pilot; RT-02
T-split coherence pilot; RT-03 rubric v2 + S re-baseline. Commit hash for these
patches: *(fill after the review commit lands).*

### Pass 2 2026-06-23 — attack on the Stage-1 separability call

Six-doc attack including `stage1-localization-findings.md` (the empirical
localization calls as wagers): `artifacts/red_team/findings_20260623T204557Z.json`,
defended + rebutted (`adjudication_20260623T204851Z.json`). Four novel findings,
three with teeth. The rebuttal conceded RT-05/RT-07/RT-08 once controls were
proposed; it **maintained RT-06**. RT-05 independently re-derived the
syntax/boundary-router worry the builder had already flagged for C_self-index.

| id | date | severity | target | disposition | resolution | loss condition recorded |
|----|------|----------|--------|-------------|------------|-------------------------|
| RT-05 | 2026-06-23 | high | design | PILOT-REQUIRED | `thresholds.md` §Red-team pilot additions + `pre-registration.md` §T battery: add a `T_syntax` control (turn/boundary tracking, zero reasoning) | if ablating C_self-index degrades `T_syntax` as much as `T_self_relevant`, C_self-index is a dialogue-state router — H_center on it is void |
| RT-06 | 2026-06-23 | high | design | PILOT-REQUIRED | `thresholds.md` + `pre-registration.md`: C_ctrl must include a **capability-gating** persona (expert/system), and that control must be **verified third-person** (separability check vs C_self) before use | **rebuttal maintained:** if no capability-gating C_ctrl can be kept a third-person object (it reads as C_self under the separability check), the differential is dead for RLHF'd instruction models → report **"not testable here yet"**, do not force H_center. Substrate-dependent (see below). |
| RT-07 | 2026-06-23 | medium | implementation | PATCH | `pre-registration.md` §Ablation + `thresholds.md`: neutral-corpus **OOD perplexity gate**; keep mean-ablation as registered primary, report all three, directional as OOD cross-check | if C_self ablation inflates neutral-corpus perplexity past a pre-set bound vs C_ctrl, the run is **OOD-inconclusive**, not H_center |
| RT-08 | 2026-06-23 | high | theory | ACCEPTED-RISK (folded into RT-07) | attack self-flagged `proves_too_much`; the OOD/perplexity gate (RT-07) + the differential already screen generic attention-collapse damage; optional sink-restoration test kept as a secondary check, not a lock gate | if the RT-07 OOD gate + differential do **not** screen the attention-sink artifact in pilot, promote the sink-restoration control from secondary to required |

**Open follow-ups before thresholds lock (pass 2):** RT-05 `T_syntax` pilot; RT-06
capability-gating + third-person-verified C_ctrl (with the substrate decision
below); RT-07 OOD perplexity gate. RT-08 folded into RT-07.

**Substrate decision (gates RT-06, prioritized above it):** RT-05/RT-06/RT-08 are
three faces of one risk — on a heavily-RLHF'd instruction model, "self" structure
is entangled with dialogue mechanics, capability-routing, and softmax stability.
Decide whether the *registered* run uses `gemma-2-2b-it` (accept and pilot the
entanglements) or moves to a less-RLHF'd model where they are weaker.

**Resolved 2026-06-23:** keep `gemma-2-2b-it` as the **pilot / instrument
sandbox** (all tooling works there) and plan the **registered run on a less-RLHF'd
model**. Treat running RT-06 on 2b-it as a deliberate test of the "not testable on
heavily-RLHF'd models" hypothesis — informative either way. **Constraints on the
registered-run model (so the pick doesn't break the instrument):** (1) it must
retain chat/turn structure and self-report capability — so "less RLHF'd" means a
*lightly-aligned instruction model* (SFT-only / DPO-light), NOT a pure base model,
which would have no assistant turn for C_self-index or S; (2) leaving the Gemma
family loses GemmaScope SAEs (localization method (b)) unless SAEs are trained.
**A staged-checkpoint family (e.g. OLMo-2 / Tülu: base → SFT → DPO → RLHF) is the
strongest option** — it lets RT-06 be run as a controlled comparison of the *same*
model at increasing alignment, directly measuring the capability-gating effect.
*(Specific model still to be pinned against these constraints — see STATUS next
actions.)*

### Pass 4 2026-07-12 — empirical self-audit during the RT-09 first pass (not from the Gemini loop)

Source: reconciling an instrument discrepancy while running the registered RT-09
pass exposed a stimulus confound no reviewer had named (evidence:
`check_length_confound.py`; narrative in `rt09-reflexivity-findings.md`).
Adjudicated by John 2026-07-12 (both proposals adopted as-is).

| id | date | severity | target | disposition | resolution | loss condition recorded |
|----|------|----------|--------|-------------|------------|-------------------------|
| RT-10 | 2026-07-12 | high | design | PATCH + control | (a) `gen_context_stimuli.py` v2: break the label↔token-count correlation in every turns-based mechanism (polarity-balanced fillers so length distributions straddle/overlap across labels), verified empirically by `check_length_confound.py`; (b) `patch_context.py`: add a **length-direction control** (least-squares token-count direction, own set-the-coordinate scale) alongside the norm-matched random control — C_self-index must beat it by the same ≥ 0.10 gap convention as the random control | if the turn_role signal collapses on length-matched stimuli, or C_self-index fails to beat the length-direction patch control, C_self-index as localized is a context-length tracker — redo the localization and retract the causal claim to that extent; no H_center attaches |

**RT-09 first-pass disposition (same date):** the registered rule did **not**
fire (cross-decode 1.000 ✓ but length-inflated; |cos| 0.224 < 0.5 ✗; cross-patch
ratio 0.006 < 0.5 ✗). Recorded as **"does not fire (provisional)"** — the
confound biased the geometry *toward* firing and it still missed, but
C_speaker-generic as localized may itself be a length direction, so the control
has not yet demonstrably tested slot-generality. The RT-09 gate stays open; the
**decision rule is unchanged** and gets re-applied on the RT-10 length-matched
stimuli. Materials amendment only — same pattern as RT-01..08.

**Pass-4 outcomes (2026-07-12, v2 stimuli, pilot sandbox):** length gate passed
(label-from-token-count ≈ chance in all mechanisms; mild 0.56–0.57 residual in
narrative, recorded). **RT-10 resolved — both loss conditions avoided:** the
turn_role signal survives length matching (clean floor, peak L15, margin +0.55)
and C_self beats the length-direction patch control 0.340 vs 0.012 (gap +0.328
≥ 0.10). **RT-09 resolved on a now-valid control:** the rule did not fire —
cross-decode 1.000 (real shared component, no longer length) but |cos| 0.148
< 0.5 and cross-patch ratio −0.005 < 0.5; C_speaker-generic is causally inert on
turn_role behaviour. Per the pre-registered partial-separation path, the removal
test targets the **residual** (C_self-index with C_speaker-generic projected
out), which still decodes at 1.0. Both gates re-verify on the registered
substrate before `δ`/`θ` lock. Side observation for RT-04: on length-matched
stimuli the index/narrative pair reaches *clean* separability at L6 (|cos|
0.017) — single layer, n≈24/side, so recorded as supporting, not upgraded.
