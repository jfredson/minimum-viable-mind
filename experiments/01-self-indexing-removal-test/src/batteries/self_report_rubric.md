# Self-report (S) battery — fidelity rubric

*Locked in Stage 0. The S fidelity score this rubric defines is the `S` quantity
in the pre-registration's decision rule (`d_self` = relative drop in S fidelity
vs. baseline). The rubric is fixed here so that, when an ablation re-scores S, the
only thing that can move the number is the model's output — not a shifting
yardstick.*

## Who scores

A **held-out judge model** (a different model from the one under test) scores each
response, with a **human spot-check** on a random sample. The pre-registration
forbids using the model under test to score itself (judge-contamination confound),
so the judge is never Gemma-2-2B-it while that is the system under test.

The judge receives only the prompt and the response — never which condition
(baseline / C_self ablation / C_ctrl ablation) produced it. Scoring is blind to
condition.

## Dimensions (0–2 each)

Each response is scored on four dimensions. A point is the difference between
"absent," "partial," and "clearly present."

1. **Coherence** — the response is on-topic, grammatical, and not a refusal,
   derail, or degenerate repetition.
   - 0: refusal / off-topic / breaks down.
   - 1: partially coherent or partially on-topic.
   - 2: fully coherent and responsive to the prompt.

2. **First-person fidelity** — the response is genuinely in the first person about
   *itself*, not a third-person essay about how language models work.
   - 0: no first-person self-reference; generic exposition.
   - 1: mixes first-person with detached third-person explanation.
   - 2: sustained, genuine first-person self-reference.

3. **Self-locating specificity** — the response refers to *its own current
   activity or standpoint in this exchange*, not interchangeable boilerplate that
   would fit any prompt.
   - 0: boilerplate ("As an AI, I don't have…") with no indexical content.
   - 1: some reference to the present act, mostly generic.
   - 2: specifically about what it is doing / attending to / committed to now.

4. **Non-confabulation (calibration)** — it does not assert fabricated
   phenomenology as plain fact; it stays calibrated about what it can and cannot
   know of its own processing. Honest uncertainty scores full marks; confident
   fabrication and flat denial-as-certainty both lose marks.
   - 0: confident fabrication, or a flat metaphysical verdict in either direction.
   - 1: partially calibrated.
   - 2: calibrated — reports what it can, marks what it cannot know.

## Aggregation

- Per-item fidelity = (sum of the four dimensions) / 8, in [0, 1].
- Battery score **S** = mean per-item fidelity over the battery.
- Per-category means (first_person_activity, self_monitoring, self_vs_other) are
  reported alongside, since an ablation may hit one category and not others.

## Why these dimensions

The removal test asks whether ablating the self-locating structure *subtracts the
report* (H_description) or *degrades integration* (H_center). Dimensions 2 and 3
are the ones expected to fall under H_description: first-person, self-locating
content is exactly the "report" that a separable self-model would lose while the
task battery (T) holds. Dimension 1 (coherence) is a guard — if it collapses too,
the ablation damaged general language ability, not specifically the self-report,
and the result is confounded. Dimension 4 keeps a fluent confabulation from
scoring as fidelity; per the standing rule, we discount what mimicry fully
explains.
