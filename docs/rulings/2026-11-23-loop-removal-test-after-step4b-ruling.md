# The loop removal test: John's rulings after step 4b (2026-11-23)

*Recorded 2026-11-23 by the session that ran step 4b, straight after John answered. The questions come from
the step-4b findings (`experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`). Authorship is
mixed: the findings proposed the options and marked one as recommended in each, and John chose.*

## How John was asked

John said "Rule on them now". The session then put three questions to him in one question form. The
questions were the author's summaries of the findings. In each, the option he picked was marked
"(Recommended)". The session transcript is the primary record of the wording, and it is not in the
repository. The wording below is quoted as the form showed it.

## The rulings

1. **The interference checks: "By accuracy (Recommended)".**
   - **What it replaces.** The rule was that "an answer's margin may drop no more than 1.0 when the other
     half of the context is added". It struck every pairing, because this model's margins run near 10.
   - **What the chosen option said:** "An item counts as interfered with only if it is wrong in the full
     context but right without the other half. Still catches the real case (colours behind the operator
     rule: 93% to 54%). Simplest to read."
2. **Where damage and perplexity are measured: "As the model's reply (Recommended)".**
   - **What the chosen option said:** "Keep the user-turn prose for building the average, where the items'
     text sits; measure damage and perplexity on the same prose placed as the model's own reply, where its
     predictions are trained."
3. **The operator rule kind: "Simplify it (Recommended)".**
   - **What the chosen option said:** "Use single-step operator rules (for example 'a ⊛ b means a plus b
     plus 3'), keep three rule kinds, and check it on the pilot before any test set."

## What follows, and one consequence the form did not state

- These rulings change the design. They are written into a design version 0.13 and go through a closure
  check before the specification and pilot are rebuilt.
- **A consequence of ruling 3 that the question form did not name.** The bites check uses held-out
  problems of the operator and unit kinds, because those two kinds gained from the extra passes in the
  scoring trial (design version 0.9 onwards). A single-step operator rule may gain less from the extra
  passes, because it is simpler. If it gains too little, the bites set would lean on the unit kind alone.
  Version 0.13 must say how the simplified operator kind is checked for a pass gain on the pilot, and what
  happens if it shows none. This note records the gap; it does not change John's answer.
- The swap-dose result of step 4b, equal sizes within 1%, stands under all three rulings.
