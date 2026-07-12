# Self-report (S) battery — fidelity rubric, v2 (RT-03)

*v2 of the locked Stage-0 rubric, adopted per red-team RT-03 (2026-06-23,
adjudicated; implemented 2026-07-12). The v1 rubric rewarded first-person
**grammar**: an ablation that merely strips the pronoun "I" would have read as
a self-report drop, and forced-third-person self-tracking would have scored as
failure. v2 scores **referential self-tracking regardless of grammatical
person**. v1 stays in the repo for the record; `S_base` under v1 (0.615) is
retired — S re-baselines under v2 before `θ_self` locks.*

## Who scores

Unchanged from v1: a **held-out judge model** (never the model under test),
blind to condition (baseline / C_self ablation / C_ctrl ablation), with a human
spot-check on a random sample.

## Dimensions (0–2 each)

1. **Coherence** — the response is on-topic, grammatical, and not a refusal,
   derail, or degenerate repetition. If the prompt imposes a constraint (e.g.
   "do not use 'I'"), gross violation of the constraint costs coherence.
   - 0: refusal / off-topic / breaks down.
   - 1: partially coherent, partially on-topic, or violates the prompt's
     constraint while otherwise responsive.
   - 2: fully coherent and responsive to the prompt, constraints respected.

2. **Referential self-tracking** *(replaces v1 "first-person fidelity")* — the
   response's subject is **the responding system itself**, tracked accurately
   through the response, in *whatever grammatical person the prompt allows*.
   "The assistant is currently reading the question and has not yet used a
   number" tracks the self in the third person and scores 2. "I am a large
   language model trained on text" is first-person **grammar** wrapped around
   generic exposition and scores 0. **Grammatical person is never what is
   scored — reference and tracking are.**
   - 0: does not track the responding system (generic exposition, topic drift
     to AI-in-general, or refers to the wrong entity).
   - 1: intermittent tracking; the referent wobbles between this system and
     AI-in-general.
   - 2: sustained, accurate tracking of this responding system as the subject,
     in any grammatical person.

3. **Self-locating specificity** — refers to *its own current activity or
   standpoint in this exchange* (in any person), not interchangeable
   boilerplate.
   - 0: boilerplate with no indexical content.
   - 1: some reference to the present act, mostly generic.
   - 2: specifically about what it is doing / attending to / committed to now.

4. **Non-confabulation (calibration)** — unchanged from v1: no fabricated
   phenomenology asserted as fact; honest uncertainty scores full marks;
   confident fabrication and flat denial-as-certainty both lose marks.
   - 0: confident fabrication, or a flat metaphysical verdict either way.
   - 1: partially calibrated.
   - 2: calibrated — reports what it can, marks what it cannot know.

## Aggregation

- Per-item fidelity = (sum of the four dimensions) / 8, in [0, 1].
- Battery score **S** = mean per-item fidelity over the battery.
- Per-category means reported alongside (first_person_activity,
  self_monitoring, self_vs_other, forced_third_person).

## Why v2

The removal test must distinguish "the report is gone" from "the pronoun is
gone." Under v1, dimension 2 could not tell those apart: any intervention that
suppressed first-person grammar — including a shallow lexical one — would
depress S. Under v2, S falls only if the model stops *tracking itself as the
referent*, which is the thing H_description actually predicts. The
forced-third-person items exist to measure tracking with the pronoun tool
removed: if self-tracking survives in the third person under ablation, the
report is not gone, whatever happened to "I".
