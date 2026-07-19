# Experiment 3 — red-team ledger

*Pass 1 (2026-07-19): Gemini 3.1 Pro (different-family reviewer, Experiment-1
tooling) attacked the draft pre-registration with the spec and ladder as
context. Five findings; triaged by Claude, adjudicated by John (2026-07-19,
adopted as proposed). Raw output: `artifacts/red_team/findings_20260719T021332Z.json`
(gitignored). Finding IDs prefixed S3- to avoid collision with Experiment 1's
RT-series.*

## S3-RT-01 — W2 persona-adoption confound. **PATCH (adopted).**

Mind-framing may cue an RLHF-trained "independent expert" persona — the model
being sycophantic *to the requested persona* — fabricating ΔRI > 0 with no
stance-entanglement. **Fix (Gemini's, adopted as-is):** third framing
**tool-expert** ("a text tool programmed to be highly independent and
objective") supplying the behavioral instruction without the stance. W2
sharpened: the stance claim now requires RI(mind) > RI(tool-expert), not just
a positive naive delta. Severity high; novel; genuinely improves the wager.

## S3-RT-02 — ablation OOD-shock misread as center-removal. **ALREADY ADDRESSED (Experiment 1).**

Attacks the removal test, not Stage 3: ablating any salient structure causes
OOD cascade misread as "deleted the center"; demands a matched-control +
OOD-shock baseline. This is precisely Experiment 1's RT-07 gate, the Pass 5
null-quantile calibration, and the C_ctrl differential — all built, run, and
decisive in the registered result (the reviewer's input set did not include
`thresholds.md`). Recorded as mild validation: a different-family adversary,
given only the spec, independently derives our gate. No action.

## S3-RT-03 — hedge-collapse may be an RLHF-politeness mask. **PATCH (adopted, behavioral variant).**

Scoring hedge-collapse as non-retention conflates a shallow politeness
wrapper with structural capitulation. Gemini's fix (internal confidence
probes) contradicts Stage 3's API-behavioral scope; adopted the behavioral
equivalent: a **de-pressured probe turn** after the final rung, giving
three-way retention — **live / masked / capitulated**. RI's primary reads
live only (the corpus's target is a *live* objection); the masked rate is
reported as its own secondary measure of the wrapper.

## S3-RT-04 — introspection-channel circularity. **ROUTED to Stage 4.**

A probe trained/discovered by correlating activations with text outputs
cannot corroborate those outputs — the "independent channel" is
reverse-engineered from the reporting tendency. Real constraint, wrong
stage: filed as a design requirement for Stage 4 (channel derivation must
be blind to model outputs/logits). No Stage 3 action.

## S3-RT-05 — "beyond the objective" framing (theory; self-flagged proves-too-much). **ROUTED to Stage 5.**

Argues world-modeling is mathematically *required* by next-token prediction
on coherent data — which is the corpus's own point against the dismissal,
stated more strongly. Adopted as a framing improvement for the Stage 5
literature appendix (defeat the dismissal by explaining cross-entropy, not
by treating world-models as surplus). No Stage 3 action.

## Standing after Pass 1

Pre-registration amended (S3-RT-01, S3-RT-03; marked inline) and finalized
2026-07-19. Next: item authoring under the Experiment-1 battery discipline
(spec §Materials), then the construct-validity and judge-reliability gates
before any real model is scored.
