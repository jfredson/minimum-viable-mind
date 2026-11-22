# The loop removal test: John's rulings on choices 6, 7 and 8 (2026-11-21)

*Recorded 2026-11-21 by the session that wrote the design, straight after John answered. The choices are
section 10 of the design (`docs/loop-removal-test-design-2026-11-20.md`), version 0.12 (commit 4fb7e73).
The closure check of version 0.12
(`docs/reviews/2026-11-21-loop-removal-test-design-v0.12-closure-check-claude-code.md`) had found the
design ready for step 3 once choices 6 and 8 were ruled. Authorship is mixed: the design recommended each
option, and John chose it.*

## How John was asked

John said "Rule on them now". The session then put three questions to him in one question form. The
questions were the author's summaries of section 10, not its full text. The option John picked in each was
marked "(Recommended)". The session transcript is the primary record of the wording, and it is not in the
repository. The wording is quoted here as the form showed it.

## The rulings

1. **Choice 6, where the instruction sits: "Start (Recommended)".**
   - **The question:** where should the instruction "Answer with the single word or number only." go in
     each question? The form said that the start keeps the swap's dose equal between the two kinds of
     question. It said that the end helps the weakest rule kind (operator) survive: with three equal kinds,
     the practice set returns to John in about 9% of simulated runs at the start, against 0.2% at the end.
   - **The option's text:** "Before the rule. Protects the dose balance the test was built around; accepts
     a roughly 9% chance that the practice run comes back to you over operator survival."
2. **Choice 7, the working precision: "Accept 16-bit (Recommended)".**
   - **The option's text:** "Every condition runs at the same precision, so comparisons stay fair; every
     result sentence names 'at 16-bit'."
3. **Choice 8, the letter-code kind: "Drop, three equal (Recommended)".**
   - **The option's text:** "40/40/40 in the practice set; test half fits about 216-220 pairs, about 140-145
     confident. Costs: no spare kind, and sums and products all sit behind the lookup rule."

## What follows

- The instruction goes at the start of every scored item, donor and bites item. The neutral passages carry
  none.
- The test runs at 16-bit, and every outcome sentence says so.
- The letter-code rule kind is dropped. The pilot has 40 operator, 40 unit and 40 lookup pairs, and the test
  half uses the same shares.
- Step 3 can now be written: the battery specification, then the pilot, with the closure check's seven
  worth-noting points (RT-466 to RT-472) settled in the specification.
- The dose finding (RT-345) stays open until step 4b.
