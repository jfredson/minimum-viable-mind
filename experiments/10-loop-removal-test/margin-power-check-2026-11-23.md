# The loop removal test: does scoring by margin give the test its power?

*Written 2026-11-23, on John's "Check margin scoring". This is a free check on the Mac, using step 4b's
recorded data: the old pilot, `step4b-run-2026-11-23/`. The script is `src/margin_power_check.py`, and its
output is `step4b-rerun-code-test-2026-11-23/margin-power-check.json`. It is a check of an idea, not a design,
and it is owed a look by a session that did not write it.*

## The question

Testing the rerun's code showed that, with each item scored as right or wrong, the test is underpowered.
Outcome A is read only about half the time at the test half's size, and outcome F almost never. The idea is
to score each item by its **margin** instead. The margin is how far, in log-probability, the right answer is
ahead of the best wrong one. It is a continuous number, so it should carry much less noise per item.

## How the two scales are compared

The design's thresholds are a gap of 0.20 and δ of 0.10. They are set on the normalised accuracy scale, so
they cannot simply be carried over to margins as numbers. Instead, they are carried over **as shares of
what one pass costs**:
- **The prompt-rule cell.** On the 72 pairs that survive the new baseline checks, the cell's one-pass cost
  is 0.174 in normalised accuracy and 4.19 nats in margin. So every margin loss is divided by 24.1. After
  that, a gap of 0.20 is the same share of what the passes supply on either scale.
- **The bites items** get their own ratio.

The step-4b simulation's own code then runs on the converted spreads. Everything else is the same, including
the renames, both methods, and the shared-fact share of 0 and 0.3.

## What it found

**The spread per item falls to about a third.** The removal's per-item loss has these spreads, in the common
units:

| | Swap, prompt-rule | Swap, routine | Average, prompt-rule | Average, routine |
|---|---|---|---|---|
| Right or wrong | 0.45 | 0.47 | 0.50 | 0.58 |
| Margin | 0.17 | 0.15 | 0.15 | 0.13 |

**Outcome A becomes well powered.** These are the chances that a true gap of 0.20, spread evenly, is read as A
under both methods, after every rename. Each was run 600 times.

| Test-half pairs | 80 | 140 | 200 | 260 |
|---|---|---|---|---|
| Right or wrong (no shared facts) | 14% | 36% | 52% | 64% |
| Margin (no shared facts) | **96%** | **100%** | **100%** | **100%** |
| Right or wrong (shared-fact share 0.3) | 11% | 25% | 39% | 49% |
| Margin (shared-fact share 0.3) | **94%** | **98%** | **99%** | **100%** |

**The scenario with the gap on the operator and unit pairs only is 0% on both scales.** That is not a lack of
power. In the old pilot's surviving pairs, no operator pairing survived, so only two rule kinds remain:
lookup and unit. A gap carried by unit alone is then exactly what the "Depends on one kind" rule is built to
rename. With three rule kinds surviving, it would not be. That cannot be measured until the simplified
operator kind is run.

**Outcome F becomes reachable,** with the bites set's branch choice in margin units:

| Target | Both kinds, right or wrong | Unit alone, right or wrong | Both kinds, margin | Unit alone, margin |
|---|---|---|---|---|
| One-pass condition | 69% | 42% | 100% | 100% |
| "Bites" | 91% | 85% | 100% | 100% |
| "Does not bite" at no true loss | 4% | 20% | 25% | **95%** |
| The branch qualifies | no | no | no | **yes** |

With margins, the unit-alone branch qualifies. Both kinds still fall short on "does not bite", because of
the old two-step operator kind's noise. The simplified kind may differ.

## Caveats

- **Margins have long tails.** In converted units, the swap's margin loss on prompt-rule items runs from 0.15
  (5th percentile) to 0.69 (95th). The simulation draws from normal distributions. The real tails would
  widen intervals somewhat.
- **The comparisons were matched on damage in the user's turn,** which step 4b showed was measured badly. The
  comparisons' own losses here are therefore not final.
- **It is the old pilot.** The operator kind and the prose's rendering have changed since.
- **The conversion is the author's choice.** It makes a gap of 0.20 the same share of the one-pass cost on
  both scales. A different anchor would give different numbers, though not a threefold change in the spread.

## What it means

Scoring by margin looks like it fixes both power problems: outcome A, and outcome F through the unit-alone
branch. It is a large change all the same. Every outcome would be read on the margin, not on whether the
model gets the answer right. The thresholds (δ, the gap, the bites conditions) would need restating in
margin units, and the design and its reviews would go another round. The rerun is better made after that
change, so that it measures what the test will actually use.
