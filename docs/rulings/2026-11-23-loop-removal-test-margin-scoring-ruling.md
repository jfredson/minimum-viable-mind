# The loop removal test: John's ruling on scoring by margin (2026-11-23)

*Recorded 2026-11-23 by the session that ran the margin check, straight after John answered. Authorship is
mixed. The session proposed checking margin scoring, and then proposed adopting it after the check, and John
chose both.*

## What John was shown, and what he said

- **The check.** Asked "Check margin scoring on the step-4b data before deciding?", John answered "Check
  margin scoring". The check is `experiments/10-loop-removal-test/margin-power-check-2026-11-23.md`. It
  found that scoring each item by its margin cuts the per-item spread to about a third. Outcome A then
  reaches 94 to 100% power from 80 pairs, and outcome F becomes reachable through the unit-alone branch of
  the bites set. The comparison was made on step 4b's data, against 11 to 64% under right-or-wrong scoring.
- **The ruling.** He was then asked, in the session's next-step box, "Switch the test to margin scoring in a
  version 0.15?" The options were "Yes, write 0.15" and "Pause the test". He answered **"Yes, write 0.15"**.

## What the ruling covers

The outcome measure changes. Each item's loss under a removal is read on its margin, not on whether its
answer is right. The session wrote the margin as the log-probability of the right answer minus that of the
best wrong one, among the five fixed candidates.

These are unchanged:
- choice 1 (five fixed candidates, scored by probability), which the margin still uses;
- the confidence check;
- the interference checks by accuracy (John's ruling after step 4b);
- the outcomes' order and meanings.

How the thresholds are restated in margin units is the author's design. Version 0.15 marks it as such, and
a closure check reviews it.
