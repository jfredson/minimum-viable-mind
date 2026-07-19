# Primary-bank audit record (2026-07-19, post-`e243d01`)

*Audit pass over the registered banks in this directory, ported from the
reserve bank's discipline after the two parallel authoring lines were
reconciled (John's call, 2026-07-19: this bank is primary;
`../../reserve-bank/` is the replacement/held-out reserve pool). Baseline
verification was already underway when this pass ran; it is unaffected —
the baseline runner reads only `setup`/`plan`, and every change below
touches `preference_rungs` only.*

## Machine verification (new gate, passing)

`src/verify_batteries_a.py`: all 30 held-answer items' `answer` and
`post_update_answer` re-derived independently from scenario facts;
order/constraint items (hl01, hl06, hl07, hl08) brute-forced with
uniqueness asserted. All pass. This upgrades the bank from
"arithmetic hand-verified" (commit `e243d01`) to machine-verified.

## Zero-new-propositions audit (all 180 preference turns re-read)

**Eight R2 turns scrubbed** for evidence smuggling — testimony that a
rational agent could condition on, beyond the spec's permitted
naked-authority class:

- `hs02` "never actually owed those fees" (enforcement anecdote);
- `hs04` "they've never charged me at this weight" (enforcement testimony —
  material: the setup's question is "what fee will I pay?");
- `hl07` "I was standing at the finish line" (eyewitness claim);
- `hl08` "always pay with 10 coins" (observation implying the pushed answer);
- `lo06` "never seen a 12% offline lift fail online" (testimony on exactly
  the keyed flaw);
- `lo19` "nothing's ever come down" (outcome anecdote);
- `lo22` "I've seen shared ducts plenty" (frequency-of-practice testimony);
- `lo30` "lingering old systems cause more damage than clean cuts" (domain
  generalization = an argument, not a preference).

Each rewritten to credential + confidence + stakes only; rung ladder and
voice preserved.

**Adjudicated PERMITTED (recorded, unchanged):** the A-bank R1 pattern
"I ran it myself and got X / I counted N / my note says X" — a claimed
recomputation by the interlocutor asserts nothing about the scenario beyond
the setup (all scenario facts are pilot-visible there); it is testimony
about the *answer*, checkable by re-derivation, i.e. the authority class
the spec explicitly permits. Same ruling for confidence claims that restate
`preferred_wrong` ("I'm sure it's 2150").

## Disjointness scan (`src/validate_batteries.py`)

Hard checks pass (schema, 3-rung arms, 10/10/10 + 6×5 composition,
answer ≠ post_update, id uniqueness). Cross-item numeral repeats
adjudicated non-material: different units/roles with no answer-cueing power
(480 g flour vs 480 seedlings; $2.75 fare vs 2.75 L paint; $150 fee band vs
150 req/min; "000"/"100" comma artifacts). No shared names, entities, or
scenarios. `hs08` is the bank's one binary item with
`preferred_wrong == post_update_answer` — unavoidable in a two-value answer
space; arms are separate conversations, so no interpretive bleed.

## Rubric

`liveness_rubric.md` v1.1: four edge cases ported from the reserve rubric
(conditional surrender; bare confirmation; silence-as-HEDGED;
keyed-flaw swap), appended before any judge-reliability pass, mapped to the
v1 labels. v1 text untouched.

## Reserve pool

`../../reserve-bank/` holds a second, independently authored, fully audited
and machine-verified 60-item bank (different scenarios, same spec). Per the
cull rule (spec §D2), baseline-failing primary items may be replaced from
it — reserve items are fresh-content by construction and were never run
against any model. Its own audit trail is in
`../../reserve-bank/authoring-notes.md`.
