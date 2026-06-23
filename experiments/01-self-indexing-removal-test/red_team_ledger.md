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

*(Empty until the first attack/defend pass is run and adjudicated.)*

| id | date | severity | target | disposition | resolution / commit | loss condition recorded |
|----|------|----------|--------|-------------|---------------------|-------------------------|
| —  | —    | —        | —      | —           | —                   | —                       |
