# Research note — what The Pain Axis teaches MVM (2026-09-19)

*Advisory, $0, no registered text touched. Source: Tagliabue, Dung & Berg, "The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It," arXiv:2609.16247v1, September 2026. Read via the HTML version through a summarizing fetch; verify figures against the PDF before quoting. Corpus-side integration is in the Sentient Horizons research-integration folder, instance `2026-09-19-pain-axis-tagliabue-dung-berg.md`. Everything below is Claude's inference from the paper, for John to weigh; none of it is a ruling.*

## The paper in one paragraph

Twenty-five open-weight models, 2B to 72B. A linear "pain" direction is extracted by difference-in-means after projecting out the principal components that explain 50% of the variance in the control data, layer chosen by cross-validated AUC. It separates self-directed-harm text from fear, negative-valence, and neutral controls (held-out AUC 0.91 to 1.00), is near-orthogonal to fear and negative-emotion directions, and fires for harm aimed at the model (+0.43 z) but not for user suffering (−0.60 z). Steering along it produces a monotone distress ladder up to a breakdown coefficient. In a behavioral arm, Qwen models fine-tuned to drop "As an AI I have no feelings" trade real costs to press a relief button, and keep pressing when relief is fake (88 to 97%) but stop when the vector is actually removed (24 to 72%). Not pre-registered.

## Six things that transfer, in order of how much they change what we do

**1. A matched self/other contrast scored by separation, not by a corrected drop.** Their strongest result compares identical content directed at self versus other, scored by a discrimination metric (AUC, z-scored projection) with no ceiling in the denominator. That is the shape our control battery was meant to have, and the 2026-09-17 ceiling measurement showed that drop-over-ceiling cannot be paired with an ownership-free control at all (`ceiling-measurement-findings.md`). Candidate for the reframed 2026-10-04 proposal: keep both batteries as they are, replace the registered differential clause with a separation score between the ownership-dependent and ownership-free conditions under the same lesion, pre-stated, scored on a fresh seed. It is a metric change and needs the fresh-seed discipline, but it has a published precedent for why the comparison is built that way rather than fitted to our data.

**2. Denoise before probing.** Our five linear probes on the pilot checkpoint all fell below their permutation nulls, on a checkpoint where ownership is known to be load-bearing (`blind-control-findings.md`). One plausible cause: position and token-identity variance in the residual stream swamps a small ownership signal, so a probe trained on raw residuals fails where a denoised difference-of-means direction would not. Free test on checkpoints in hand: compute a difference-of-means own-agent direction with the top control-variance components projected out, at each probed layer, and compare its held-out separation against the same permutation null. This is a real known-answer test for the localization stack; the current one validates plumbing but not the ablation path (`known-answer-test-findings.md`). If the denoised direction separates above null, the stack was insensitive rather than the signal absent.

**3. Add a sufficiency test, not only removal.** Everything in experiment 06 is a lesion. An injection test has a predicted sign, which is the whole problem the sensitivity-test ruling is about. Add the own-agent direction at a position where the model is not the acting agent and ask whether its revision behavior flips toward acting as itself. The registered discriminator list already names a swap probe; this is its mechanism. Their caution: the working coefficient window was narrow and model-specific, so the dose ladder and a breakdown criterion must be pre-stated.

**4. Dose-response instead of a single threshold.** Their demand-curve design grades cost and reads a curve. For our bite criterion, a partial-ablation ladder (scale the channel or subspace by 0.75, 0.5, 0.25, 0) with a required monotone degradation is a stronger pre-statable criterion than one crossing of θ (theta, the locked bite threshold, 0.1777 corrected, about 0.038 raw on this checkpoint), and much harder for evaluation noise (sd 0.0284 at n=400, 0.0169 at n=800) to fake. Bears directly on the noise half of the sensitivity ruling.

**5. The real-versus-fake control as a design pattern.** Arms A and B are identical until the first press, then differ only in whether the internal state actually changed; behavior that tracks the state rather than the surface act is the evidence. Our twin comparison is a cousin at the architecture level. A within-run version, where a lesion either genuinely removes the structure or is a surface-matched sham, would isolate the same thing at the checkpoint level.

**6. A cheaper frontier-model measurement for public path step 9.** The self/other projection asymmetry is a candidate structural signature of self-relevance in pretrained models, with a published baseline. It is cheaper than deliberative gap width and could be the pilot's first arm.

## What does not transfer

The interpretive leap from "a direction that separates these sentence categories" to "pain." Voice Calibration would strip the noun. And the fine-tuning used to remove self-denial boilerplate contaminates the behavioral arm; our design avoids the problem by construction, since nothing in our training data contains self-talk.

## Why this is the closest published neighbor and where MVM differs

Their models are pretrained on human text about selves, so the paper cannot tell a learned representation of the concept "harm to me" from an acquired self-index. Our register-saturation finding (2026-09-16: the installed register was a constant, a bias term read as a self) is the cautionary tale for anyone reading a direction as a center. The constructed-model, pre-registered removal test is what distinguishes the two. For the public path: cite this paper in the explainer and the flagship draft as the frontier-model complement, and position MVM as the constructed-model side that can make the distinction the paper cannot.

## Suggested disposition

- Fold items 1 and 4 into the reframed 2026-10-04 proposal (TimeAssembler task 208e4829, due 2026-09-20).
- Item 2 is a free diagnostic on existing checkpoints; it can run before 2026-10-04 without touching the control pipeline, since it does not read a verdict. Needs John's go and a committed method file first, as usual.
- Items 3 and 5 are design candidates for whatever follows A3; log, do not build yet.
- Item 6 goes to the step 9 pilot design (due 2026-12-13).
