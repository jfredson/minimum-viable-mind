# The loop removal test: John's ruling on choice 9, the thresholds in margin (2026-11-23)

*Recorded 2026-11-23 by the session that wrote design version 0.16, straight after John answered. The choice is
section 10, choice 9, of the design (`docs/loop-removal-test-design-2026-11-20.md`, version 0.16, commit
22b84af). Authorship is mixed: the design recommended the option and John chose it.*

## How John was asked

John said "Yes, write 0.16", and version 0.16 was written. The session then put choice 9 to him in a question
form. The question was the author's summary of the choice. The session transcript is the primary record of
its wording, which is quoted here as the form showed it.

**The question:** "Choice 9 (loop removal test, margin scoring): every loss is now measured in units of C, how
much margin dropping to one pass costs the rule questions (4.19 nats on step 4b's data, steady to about
±14%). Two numbers decide the outcomes: δ (an excess below this counts as no excess) and the target gap the
test is sized to find. Which should they be?"

**His answer: "Shares of one pass (Recommended)".** The option read: "δ = 0.5 and target gap = 1.0, in units of
C: 'no excess' means less than half of what the extra passes supply; the test is sized for a gap as large as
what they supply. Follows the rebuilt practice set; anchored on a steady measure."

## What follows

- δ = 0.5 and the target gap of 1.0 are fixed, in units of C.
- C is fixed on the pilot at the step-4b rerun.
- Version 0.16's text already carries these values as the recommended option, so it needs no change beyond a
  note that the choice is ruled.
- The closure check of version 0.16 is next.
