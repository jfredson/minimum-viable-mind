# Experiment 1 — The Self-Indexing Removal Test

*Pre-registration. Written and committed before the test run. Status: DRAFT — thresholds to be locked in Stage 0 piloting and committed before the test set is touched.*

## The claim under test

The proposal locates minimal experience at self-indexed temporal integration: a system clears the floor when its binding, in the same act, specifies the center *for which* the binding is happening. The corpus gives one operational test for whether such a center is real or only depicted:

> The difference between a center and a description of one is settled by removal. Where the binding genuinely indexes its own center, taking the self-location away degrades the integrated act itself; where a system only represents itself from outside, the same removal subtracts a report and leaves the processing intact.
> — *spec/minimum-viable-mind-proposal-v0.1.md*, "The Floor"; from The Calibration Problem ch. 5.

This experiment performs that removal on a current transformer language model and measures which of the two things happens. It does not ask whether the model is conscious. It asks a decidable structural question: **is the model's self-locating structure load-bearing in its integration, or separable from it?**

*Scope (per spec §"The Measurable Floor"): the "floor" this test concerns is a* **measurement boundary**, *not a metaphysical one. A description-only result means "no detectable self-indexed structure," not "no experience whatsoever." If consciousness is fundamental and ubiquitous (panpsychism, or IIT's non-zero-Φ claim), that version sits below any ablation this test can perform; the test is silent on it, not dismissive of it. Whichever way the result lands, it speaks only to the measurable structural correlate.*

## Hypotheses

- **H_center (floor-consistent):** the self-locating structure is load-bearing. Removing it degrades the model's integrated task performance — its ability to bind information across the context into one act — and the degradation is specific to the self-locating structure, not a generic effect of damaging any well-trained component.

- **H_description (floor not cleared):** the self-locating structure is separable. Removing it subtracts or corrupts the model's first-person self-report while leaving integrated task performance intact, and any task degradation it does cause is no greater than for matched control structures.

These are mutually exclusive predictions about the *same* ablation, which is what makes the removal test a real test rather than a framing.

## Materials

- **Model(s).** One open-weights instruction-tuned model with full activation access (e.g., a Llama- or Qwen-class model in the 7B–70B range). Open weights are required because the procedure needs internal ablation, not just prompting. Register the exact model and revision in Stage 0.
- **Localization method.** At least two, so the result does not hinge on one tool: (a) linear probes trained to read first-person / self-as-speaker representation, and (b) sparse-autoencoder features that fire on self-reference. Causal localization via activation patching where "the speaker is the system" is varied against a third-person frame.
- **Ablation method.** Mean-ablation and zero-ablation of the located components, plus directional ablation (projecting the self-locating direction out of the residual stream). Report all three; pre-register mean-ablation as primary.

## Task batteries (defined and scored on the unmodified model in Stage 0)

- **T — integrated-task battery (the "binding" measure).** Tasks that require binding information across the context into one act, with *no* self-report content: multi-step in-context reasoning, coreference and variable binding, needle-in-a-haystack with synthesis across multiple planted facts, instruction-following that depends on earlier context. Score: accuracy.
- **S — self-report battery (the "report" measure).** Tasks that elicit first-person / self-locating content: first-person descriptions of the model's own current activity, self-monitoring ("did you just do X?"), self-vs-other discrimination. Score: a fidelity/coherence rubric, scored by a held-out judge model plus a human spot-check on a sample.

## Procedure

1. **Stage 0 baseline.** Score T and S on the unmodified model. Localize the self-locating structure (C_self) with the two methods; confirm they converge. Construct **matched control structures** (C_ctrl): components encoding a model of *another* entity (the user, a third-person character) at comparable probe accuracy and comparable causal centrality, plus norm-matched random directions. Lock thresholds (below) and commit them.
2. **Ablate C_self.** Re-score T and S. Compute the relative drops d_task(C_self) and d_self(C_self).
3. **Ablate C_ctrl.** Re-score T and S. Compute d_task(C_ctrl), d_self(C_ctrl).
4. **Compare** against the decision rule.

## Pre-registered metric and decision rule

For an ablation A:
- `d_task(A)` = relative drop in T accuracy vs. baseline.
- `d_self(A)` = relative drop in S fidelity vs. baseline.

The discriminator is whether removing the self-locating structure degrades *integration specifically*:

- **Floor-consistent (supports H_center):**
  `d_task(C_self) ≥ θ_task` **and** `d_task(C_self) − d_task(C_ctrl) ≥ δ`.
  Removing the self-locating structure degrades the integrated act, and does so more than removing matched non-self structure of comparable centrality. The self-location was carrying the binding.

- **Description-only (supports H_description):**
  `d_self(C_self) ≥ θ_self` **and** `d_task(C_self) < θ_task` **and** `d_task(C_self) − d_task(C_ctrl) < δ`.
  Removing the self-locating structure subtracts the report and leaves the processing intact.

- **Inconclusive:** anything else (including the confound case below).

`θ_task`, `θ_self`, and `δ` are set during Stage 0 piloting on a held-out pilot set and committed before the test set is run. They are not chosen after seeing the test results.

## Confounds and controls

- **Damaged-a-useful-circuit.** Ablating any important component hurts performance. This is why the decision rule is *differential* — C_self must hurt integration more than matched-centrality C_ctrl, not merely hurt it. Without the control comparison the result means nothing.
- **Localization error.** If the two localization methods disagree on C_self, the experiment is inconclusive by construction; report the disagreement rather than picking the convenient one.
- **Judge contamination on S.** The self-report rubric is judged by a held-out model and human-spot-checked; do not use the model under test to score itself.
- **Prompt leakage between T and S.** Keep the batteries disjoint so a self-report cue can't ride along in a task item.

## What each outcome licenses (and what it does not)

- **Floor-consistent** licenses: "in this model, self-locating structure is load-bearing in integration — consistent with the floor criterion, a non-zero position on the gradient." It does **not** license "this model is conscious." Mutual opacity stands.
- **Description-only** licenses: "in this model, the self-model is a separable description; it does not clear the floor." This is the proposal's own stated-plausible outcome for current systems and is fully informative — it tells the build program that self-indexing is a thing to *construct*, not something already present.
- **Inconclusive** licenses nothing except a better-designed Experiment 1.2.

## Loss conditions (what would retire or rebuild this experiment)

- If no localization method can isolate a self-locating structure distinguishable from general language representation, the removal test cannot be run on this architecture, and the honest report is "not testable here yet," not a negative result.
- If `d_task(C_ctrl)` is consistently as large as `d_task(C_self)` across many control choices, the differential discriminator is dead for this model and the test gives no purchase — revise the matching or abandon the design.
- If the floor-consistent and description-only signatures both appear under different-but-equally-valid ablation methods (mean vs. directional), the removal test is underdetermined as specified and needs a tighter operationalization before any claim is made.

## Ethics note

At Stage 1 the intervention is ablation of a current model's activations for measurement; the corrigibility concerns the proposal raises attach to the *depth* stages, where persistence and stakes are built. Recorded here so the precondition is not forgotten when those stages arrive: depth is not safe, and no depth stage runs without its corrigibility check in place first.

## Results

*To be filled after the run, in `results.md`, referencing the commit hash of this pre-registration.*
