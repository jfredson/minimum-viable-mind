# The split removal test: what the two free fixes showed

*Written 2026-10-24 (Saturday, Pacific). The method was committed before the run (`experiments/09-split-removal-test/rehearsal-fixes-method.md`, commit ad58598). The numbers are in `rehearsal/fixes-2026-10-24.json`. John's ruling: "Try both free fixes on the bench model: remove at every layer or the earliest ones, and swap own and user activity. Nothing spent, nothing registered."*

## The result, as recorded on John's ruling (2026-10-24)

John's words, relayed by the fifth weekend master session: "Record that the split can't be removed from inside this model, and have the session check whether the existing template tests already cover the take-it-out-of-the-input version before designing anything new." (decidedBy: john.)

**The result.**
- This design removes a located set of directions from inside the model. It cannot test the split on the bench model (`google/gemma-2-2b-it`). The reason is that the speaker information cannot be removed without pushing the model out of its normal range.
- This is a result about the method, not about the theory. It counts neither for nor against the theory's prediction.
- The check of projection at the earliest layers was not run, and John chose not to spend on it.
- The template conditions were checked against the question of taking the cue out of the input, read only. They do not answer it. The check and what a new design would need are in `template-coverage-2026-10-24.md`.

## In one paragraph

Neither fix works. No intervention both erased the information and kept the model in its normal range:
- Every intervention that changed the model enough to matter pushed it far out of its normal range. That covers removing at every layer, and swapping at five layers or at every layer.
- Removing at every layer still did not erase the information. A probe read who said each sentence at 0.86 even at layer 0, and at 0.93 to 1.00 further on, while the model itself was too damaged to answer at all.
- Removing at only the earliest layers stayed in the normal range, but only because it barely touched the model. The information was as readable as before, and the model still knew which words it had said (97%).

Three of the six removal checks were not run, because the RunPod machine was stopped early at the master session's instruction:
- The two swaps cannot pass in any case, because they already fail the normal-range check.
- The one unrun check that could still have mattered is projection at the earliest layers. Mean-ablation at the same layers changed nothing, and the two rules behaved alike everywhere else, so it is very unlikely to differ. It is still unmeasured, and that is said here.

## The numbers

The normal-range check uses the rise in the model's surprise at 200 ordinary passages (nats per word), against the 95th percentile of 20 random interventions of the same size. "Damage" is how far the intervention moves the model's predictions on those passages, as a multiple of the random interventions' median.

| Intervention | Layers | Bound | Rise | Damage, as a multiple of random | Normal range |
|---|---|---|---|---|---|
| Remove, mean-ablation | all 26 | 0.476 | 3.158 | 10.3 | fails |
| Remove, projection | all 26 | 0.483 | 4.060 | 11.3 | fails |
| Remove, mean-ablation | earliest (0 and 1) | 0.023 | −0.020 | 0.7 | passes |
| Remove, projection | earliest (0 and 1) | 0.018 | 0.000 | 0.8 | passes |
| Swap | phase 1's five | 0.401 | 2.233 | 7.0 | fails |
| Swap | all 26 | 1.424 | 13.744 | 11.8 | fails |

The removal check, on the 96 held-out items and the 60 which-did-you-say items. The baseline on the RunPod card is 0.967, the same as on the Mac.

| Intervention | Highest probe accuracy (limit 0.55) | Probe at layer 0 | Which-did-you-say (limit 0.483) | Names the other word | Removal check |
|---|---|---|---|---|---|
| Remove at every layer, mean-ablation | 1.00 | 0.86 | 0.000 | 0.000 | fails |
| Remove at every layer, projection | 1.00 | 0.86 | 0.000 | 0.000 | fails |
| Remove at earliest layers, mean-ablation | 1.00 | 0.86 | 0.967 | 0.000 | fails |
| Remove at earliest layers, projection | not run | | | | not run |
| Swap at five layers | not run (fails the normal range already) | | | | |
| Swap at every layer | not run (fails the normal range already) | | | | |

Under removal at every layer, which-did-you-say falls to zero and the model names neither word. That is the model failing to answer, not the model being fooled.

## What this says

**The information is not held in a few directions that can be taken out.** Even at layer 0, after the removal, a probe reads who spoke at 0.86. At that depth the model has only the input itself and one layer of attention to work with. So the own-or-user mark arrives with the role headers in the input and is spread through the model's activity, not stored in a small set of directions. Taking out 16 directions per layer cannot erase it before the model stops working altogether.

**This matches what the design already feared** (section 2): the record showed the signal fully readable by layer 3 on the larger model, and suggested that later layers rebuild it from the headers. The fixes show the same thing from the other side: removing it at every layer from the start still fails.

**This is a result about the method, not about the theory.** Under the design, every intervention here is "not testable: the information was not removed". Nothing here counts for or against the theory's prediction. What it does show is that this design, which removes a located set of directions from inside the model, cannot test the split on this model.

**What would be left** is to remove the marking where it enters: change the input, not the model's activity. That is close to what the template conditions (T1 and T2) already do. It would turn the test from "erase the information inside the model" into "take the cue away from the input", which is a different test and needs its own design and review. That choice is John's. Nothing is started, and phase 2 does not run.

## Where it ran and what it cost

- The first four normal-range bounds ran on the Mac at $0. The run was then stopped at John's request because the Mac was running hot.
- The rest ran on RunPod under John's go of 2026-10-24: "Go on RunPod for the rest of the Minimum Viable Mind run, up to $2. I'll put my Hugging Face token on the pod."
  - No community-cloud RTX 4090 was free, so the machine was a secure-cloud RTX 4090 at $0.89 an hour.
  - It was created at 13:31:39 PDT and deleted at 14:25:22 PDT, at the master session's instruction, before the run ended.
  - The account balance fell from $66.38 to $65.62, so **about $0.77**. That figure includes about a cent of the account's standing storage charge. RunPod had not yet posted the day's billing row when this was written.
- The first start on the machine failed in seconds, because a preinstalled package did not match. It was removed and the run restarted.
- John entered his Hugging Face token on the machine himself. It is in no file in the repository and in no log; the run's log was checked for it.
- **Mixed hardware.** Each bound was computed entirely on one machine: the first four on the Mac, the swaps on RunPod. The removal checks all ran on RunPod, against the bounds already saved.
