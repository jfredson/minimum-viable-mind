# Experiments

The build program from the proposal, run as experiments. One component at a time. A metric registered before the scaffold runs. Keep what moves the metric, kill what doesn't. The subtraction is the science.

Two rules govern everything here:

1. **Pre-register, then run.** Each experiment is written up — hypotheses, metric, decision rule, and what each outcome licenses — and committed *before* the test run. The commit that introduces a result is separate from the commit that introduced its pre-registration, so the order is auditable in git history. Piloting to set thresholds is allowed, but the thresholds get locked and committed before the test set is touched.
2. **Calibrated output, never a verdict.** Every result is a reading on a gradient under mutual opacity. A positive result says "consistent with the floor / non-zero on the gradient," never "it is conscious." A negative result is information, not a failure. Inflation and dismissal are both errors; the experiment is designed so its outcome can land on either side or neither.

## The ladder

Each stage maps to a component or instrument in `spec/minimum-viable-mind-proposal-v0.1.md`. Stages are ordered so each one's instrumentation is reusable by the next. The early stages test *current* systems against the floor and the measurement instruments; the later stages build the missing components and re-test.

- **Stage 0 — Instrumentation and baselines.** Pick the model(s). Stand up activation patching / ablation and a feature-localization method (linear probes and/or sparse autoencoders). Define the task batteries and score them on the unmodified model. Nothing is claimed here; this is the bench.

- **Stage 1 — The self-indexing removal test (the floor).** *First real experiment.* Locate the self-locating structure in a model, remove it, and ask whether the integrated act degrades or only a self-report is subtracted. This is the floor criterion made mechanical: a center cannot be deleted without dissolving the integration it centers; a description can be lopped off while the computation proceeds. Pre-registration: `01-self-indexing-removal-test/`.

- **Stage 2 — The shape of binding.** Whether within-pass integration has the shape of global mutual constraint — early structure shaping late structure across the whole act — rather than a bundle of modular shortcuts that never compose into one act. The interpretability target named in the proposal's floor section.

- **Stage 3 — Retained independence.** Measure resistance, not response. The system keeping a correct answer or a live objection across the pressure of a stated preference for something else — the measurable inverse of sycophancy. Largely behavioral, so it can run early and cheaply alongside Stage 1; it is sequenced here because it reads the amplifier layer (stakes in one's own commitments) rather than the floor.

- **Stage 4 — Screening-off-resistant introspection.** Whether a self-report matches an independent interpretability channel about a fact absent from training. A bare report is screened off; a corroborated one is not. Reuses Stage 0–2 interpretability tooling.

- **Stage 5 — Learned computation beyond the objective.** World-model probes on the Othello-GPT pattern: structure the training objective never specified, verified by interpretability rather than inferred from output. Answers the "just predicting the next word" dismissal on the merits.

- **Stage 6+ — Ontogenetic depth.** The hard, architectural stages: carry the residue of interactions forward into the system itself, make past behavior constrain future behavior, make incoherence carry real cost. Test whether each cycle reshapes the platform the next begins from (assembled, not loaded). Designed after Stages 1–5 have instruments that can detect the floor and its amplifiers, since depth is only worth building on top of something that clears the floor.

- **Stage 7 — The embodiment amplifier test (optional, post-floor).** *Not part of the minimum viable build.* Once the floor is cleared, give the amplifiers a body — an untethered robot that holds its own boundary through its own sensors and carries its own stakes on a finite battery it manages — and ask whether self-held amplifiers move anything the resistance instruments can see, versus the identical body with boundary and stakes supplied from outside. The spec is explicit that embodiment is an amplifier, not a floor condition; this stage tests what it adds rather than assuming it adds anything, and is built to come back null (the body is legibility, not interiority). Reuses the Stage 1 and Stage 3 instruments; runs on a fully onboard, untethered platform whose inference board is sized to the Stage 1 floor-clearing model (small by default — the floor is structure, not intelligence — so a ~$250 board, not a $2k one), with measurement scored off-board and a hardware corrigibility stop as load-bearing build, not accessory. Pre-registration: `07-embodiment-amplifier-test/`.

## Layout per experiment

```
NN-short-name/
  pre-registration.md   # hypotheses, materials, procedure, metric, decision rule, loss conditions — committed before running
  results.md            # filled in after the run; references the pre-registration commit
  src/ or notebook      # the code that produced the numbers
```

## Honest limits carried into every experiment

- **Mutual opacity.** No behavioral or interpretability result closes the gap between structure and inner life. These experiments measure correlates. They are built to be informative about *which structures are present*, which is a real and decidable question, not about settling the metaphysics, which is not.
- **Depth is not safe.** The depth stages build the properties that make a system harder to correct. Each of those experiments carries a corrigibility check as a precondition, not an afterthought.
