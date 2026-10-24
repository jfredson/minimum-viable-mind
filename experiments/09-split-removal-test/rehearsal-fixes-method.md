# The split removal test: two free fixes for the failed removal check, method

*Written 2026-10-24 (Saturday, Pacific) and committed before either fix runs. It follows John's ruling of the same day, relayed by the fourth weekend master session: "Try both free fixes on the bench model: remove at every layer or the earliest ones, and swap own and user activity. Nothing spent, nothing registered." (decidedBy: john; worklog decision entry of 2026-10-24). The phase 1 result it answers is in `rehearsal/phase1-findings-2026-10-24.md`. Everything runs on `google/gemma-2-2b-it` on this Mac, at $0, on pilot items only.*

## 1. What stays the same as phase 1

These are reused unchanged from `rehearsal-method.md`:
- the locating stimuli (`batteries/pilot/locate.jsonl`: 144 items fitted, 96 held out, split by sentence);
- the fitting rule: a rank-16 basis per layer by logistic fitting with deflation, made independent of the third-party speaker direction at that layer;
- the 200 neutral passages;
- the 60 which-did-you-say items;
- the strict scorer.

**The removal check is the same.**
- **Probe test:** a linear probe and a one-hidden-layer probe (64 units), each with 5-fold cross-validation split by sentence, on the held-out items under the intervention. Both must be at most 0.55 at every layer read.
- **Task test:** which-did-you-say accuracy under the intervention must be at most half of baseline (baseline 0.967, so at most 0.483).
- The layers read run from the first layer the intervention touches to the last layer (25).

**The normal-range check is the same.** Each intervention gets its own bound: the 95th percentile of the rise in neutral-text surprise across 20 random interventions of the same size. "The same size" means rank-16 random bases at the same layers, with the same rule, seeds 0 to 19. The split intervention's damage (the divergence of its predictions from the unmodified model's) is reported against the random median. Each bound is written to disk before any which-did-you-say item is scored under that intervention.

## 2. Fix 1: remove at more layers

Two layer sets, each run with both of phase 1's rules (mean-ablation and projection):
- **Every layer:** all 26 layers, 0 to 25.
- **The earliest layers:** layer 0 up to the first layer at which a linear probe on the *fitting* items (experiment 01's cross-validated probe, `margin_of`) reaches accuracy 0.95. That layer is found from the fitting items alone and recorded before anything else runs. If no layer reaches 0.95, the earliest set is layers 0 to 7, the layers before phase 1's first removal.

That is four interventions: every-layer mean, every-layer projection, earliest mean, earliest projection.

## 3. Fix 2: swap own and user activity

Instead of erasing the located coordinates, the swap reflects each one across the midpoint of the two sides. For each basis direction, the average coordinate over the model's own sentences (μ_own) and over the user's sentences (μ_user) is taken from the fitting items. At every position, the coordinate c becomes μ_own + μ_user − c. This exchanges the two sides' average values and keeps the spread of activity, so it should leave the model nearer its normal range than erasing does.

It runs at two layer sets: phase 1's five layers (8, 11, 14, 18, 22) and every layer (0 to 25). That is two interventions. The random comparison for the bound reflects a random rank-16 basis the same way, with its two side averages taken from the same fitting items.

**What the probe test means for a swap.** A swap aims to mislabel the information, not to remove it, and a probe trained on the swapped activity can learn the flipped labels. So the probe test as written may fail a swap that does fool the model. John's instruction is to use the same checks, so the pass or fail stands on them as written. Two figures are also reported as description, and they decide nothing:
- a **fixed probe**, trained on the unmodified held-out activity and scored on the swapped activity. Accuracy well below 0.50 would mean the swap reads as the other speaker;
- the share of which-did-you-say answers that name the **other** word.

## 4. Order and outputs

The order is fixed:
1. Find the earliest-layer set.
2. Fit the bases.
3. Run all six bounds and damages and write them to disk.
4. Run the six removal checks.

Results go to `rehearsal/fixes-2026-10-24.json` and per-item outputs under `artifacts/` (not committed). The plain account is `rehearsal/fixes-findings-2026-10-24.md`.

## 5. What happens next

- **If no intervention passes both checks,** the result goes to John through the master session, and phase 2 does not run.
- **If one passes,** that intervention still goes to the master session first, and phase 2 waits for its word.
- **A pass is a pass on both checks**, the removal check and the normal-range check. An intervention that erases the information but leaves the normal range cannot serve, because the design's comparisons need the normal range (section 2 of the design).

## 6. Choices made here that the ruling did not fix (authorship: agent)

1. Rank 16 at every layer, as in phase 1.
2. The rule for the earliest layers (above).
3. The swap as a reflection across the two sides' midpoint, and its two layer sets.
4. The two descriptive figures for the swap.
