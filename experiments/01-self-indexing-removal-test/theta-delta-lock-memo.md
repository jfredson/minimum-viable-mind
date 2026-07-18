# θ/δ lock — decision memo (DRAFT, prepared 2026-07-17)

*Decision support for John's lock commit — NOT the lock itself. This memo
consolidates every registered input the three thresholds must respect, with
derivations and candidate values. The lock happens in a separate commit that
fills the TBD table in `thresholds.md`, per the pre-registration. Values here
are proposals; the decision is John's alone.*

## What locks, and what each number must respect

Per `thresholds.md` §"How each threshold gets set" (registered 2026-06-23) and
everything measured since:

### θ_task — "integration degraded at all"

- **Resolution floor:** post-cull batteries are 32/30/30 items with baseline
  1.000 on all three (92/92, `prelock-findings.md` §a) — so relative drop =
  raw fraction of flipped items; one item = 0.031 (T_si) / 0.033 (T_sr,
  T_syntax).
- **Null band:** under interventions that should not move behaviour, observed
  battery movement is 0–2 items (idxres k=1: ±1–2; expert k=4: 0–1; SAE
  random control: 4 flips vs self's 4 — matched, i.e. control-band). Upper
  edge of the null band ≈ 2 items ≈ 0.067.
- **Candidate: θ_task = 0.10** (≥ 3 flipped items on a 30-item battery, ≥ 4
  on T_si). Clears the null band's upper edge with a full item of margin and
  matches the pre-committed §b selection-rule granularity ("≥ 3 items beyond
  control"), keeping the pilot's strength selection and the registered rule
  consistent with each other.

### θ_self — "the report was subtracted"

- **Registered rule:** θ_self ≥ ~4× judge noise.
- **Noise, measured** (`prelock-findings.md` §c): repeat-pass battery |Δ|
  0.008; bootstrap SE 0.040; **binding number = control-arm d_self wobble
  0.05–0.07 relative** (consistent with rehearsal σ≈0.05) ⇒ θ_self ≳ 0.2.
- **Candidate: θ_self = 0.25** (≈ 4–5× the wobble band's midpoint). Against
  S_base = 0.6375 that means judged S must fall below ≈ 0.478 — deeper than
  the zero-mode coherence collapse (0.525) reached, which is the right side
  of that line given the §d lesson that coherence-borne degeneration can
  masquerade as a self-report drop (now separately gated by the rep-4 probe).
- **Caveats the lock rationale must carry** (registered): (i) S on this
  substrate is partly an inverse measure of deflection boilerplate — at the
  SFT rung, ablation-driven S *increases* can be deflection-mediated (ladder
  P2 surviving kernel); the rule fires only on drops, so validity holds, but
  small increases must not be over-read. (ii) Any qualifying S drop must be
  checked against the coherence dimension before H_description is scored —
  a drop carried by coherence alone is the degeneration signature, not
  description-loss (rubric v2 dimension decomposition + long-gen gate).

### δ — "degraded specifically by the self-structure"

- **What it must exceed:** the spread of d_task(C_ctrl) across matched
  controls. Measured: expert k=4 moved 0–1 items (−0.015 Δnll, essentially
  inert); expert k=16 moved ≤ 2 items on any battery (0.067); SAE expert
  m=32 moved zero items. Control spread ≈ 0–0.067.
- **Candidate: δ = 0.10.** Same magnitude as θ_task: the C_self−C_ctrl gap
  must be worth ≥ 3 items beyond whatever the matched control did. Registered
  loss condition stands: if the gap doesn't clear δ across control choices,
  the differential is dead — δ does not shrink to rescue it.

## Dependencies and order

1. **The calibration run** (Pass 5, in flight) decides which interventions
   are *readable*, not what the thresholds *are* — the numbers above are
   derivable today. But locking after it reports keeps the lock commit able
   to name the admitted intervention set explicitly, which the removal-test
   run order needs anyway. **Recommended order: calibration → this lock →
   removal test.**
2. **Spot-checks:** ladder scores PASSED AS-IS (2026-07-17, recorded).
   SAE-condition scores — **still open**, awaiting John's explicit verdict.
3. The lock commit should cite: this memo, `prelock-findings.md` §a/§c,
   `rt06-ladder-findings.md` (P2 kernel caveat), and the Pass 5 amendment,
   and fill the pre-registration commit hash per the TBD table's
   instruction.

## What the removal test then runs (for the lock commit's completeness)

Primary target: **C_self-index residual** (⊥ C_speaker-generic, per RT-09),
mean ablation primary, directional cross-check, at the strength the §b rule
selects from the OOD-clean set under the recalibrated bound; C_self-narrative
tested independently (RT-04, functionally separable); C_ctrl-expert arm at
matched strength (RT-06, validated at every rung); RT-07 gate = neutral-NLL
bound + long-generation rep-4, both null-calibrated; decision rule verbatim
from `thresholds.md` §"The rule these numbers serve", including the
floor-consistent-restricted outcome (RT-02) and the RT-05 router reading if
T_syntax co-drops.
