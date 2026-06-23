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
