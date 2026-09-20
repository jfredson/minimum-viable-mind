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


===== FILE: docs/outside-reader-shortlist-2026-09-19.md =====

# Outside interpretability reader — shortlist (2026-09-19)

*Public path step 7, due 2026-11-08: one outside interpretability reader red-teams the draft before any public claim. John names the candidate. This is a research shortlist from a Cowork session, built from public sources on 2026-09-19; nothing here has been contacted. Reachability is a judgment, not verified. The ask should go out with the seed 3 and 4 results attached, not before.*

## What the reader is for

Two different things need checking, and one person rarely does both well:

1. **Mechanism.** Is the localization stack sound, is the removal test what it says it is, is the null construction honest, and does the registered clause (whatever it becomes this weekend) measure what the paper claims? This wants someone who works on small transformers and internal representations.
2. **Claim scope.** Does the write-up claim "a structural signature of self-indexing in small constructed models" and nothing more, and does it hold up against the people who spend their time distinguishing privileged representations from workspaces from selves? This wants someone from the consciousness-indicators side who is professionally allergic to over-claiming.

Recommendation below: one reader per job.

## Candidates

**Adam Shai and Paul Riechers (Simplex).** Computational mechanics on small transformers; the belief-state-geometry work showed structured internal representations in toy models with a precise theory of what should be there. Closest methodological neighbor MVM has: small constructed models, pre-stated predictions about residual-stream structure, geometric probes. They would read the localization stack and the null construction the way it needs reading. Reachable: small independent org, active on the Alignment Forum, took podcast interviews on the method. *Best fit for job 1.*

**Derek Shiller (Eleos AI Research).** Co-wrote the Eleos external commentary on the Anthropic global-workspace paper, which drew the "privileged set / privileged stream / full workspace" distinction and argued the paper showed the first and not the third. That is exactly the claim-scope discipline MVM's write-up needs applied to "self-index." Philosopher by training, methodology-focused. Reachable through Eleos. *Best fit for job 2.*

**Patrick Butlin (Eleos AI Research).** Senior research lead; the consciousness-indicators reports (2023, 2026, with Long, Bengio, Chalmers); recent interpretability work on persona vectors and individuation. On record that no current AI is a strong candidate, so a reader who will not want the result to be true. Alternative to Shiller for job 2; more senior, probably less available.

**Neel Nanda (Google DeepMind).** Independently replicated the global-workspace core result and stayed skeptical of the fine details and the philosophical conclusions, calling the method hypothesis generation rather than evidence. The highest-credibility interpretability red-teamer available, and a public engagement from him would carry the release. Very busy; the realistic channel is a MATS scholar in his stream reading it with his sign-off, or a short public reply once the preprint is out. *Stretch for job 1.*

**Cameron Berg (Reciprocal Research).** Co-author of The Pain Axis, which MVM will cite as its closest published neighbor; registers predictions before analysis; has run self-report and SAE work on consciousness claims. A natural reader because the paper positions itself against his, but he is a proponent, so he reads as someone who wants the class of result to exist. Useful as a second reader after the red-team, not as the red-team.

**Robert Long and Jeff Sebo (Eleos / NYU Center for Mind, Ethics, and Policy).** "Studying AI Welfare Empirically" (2026) argues for probabilistic claims, transparency and independent outside assessment, which is what step 7 is. Philosophy rather than interpretability; the right people to tell whether the write-up's scope statement is defensible, not whether the code is. Reachable; both do public work.

**Robert Chis-Ciure (Sussex, Seth lab).** Already engaged by the corpus (research log 2026-07-04); holds a rival view of consciousness (fundamentalist) while doing rigorous functional measurement. A reader who disagrees with the framework and respects measurement is worth more than one who agrees. Not an interpretability specialist; would read the theory framing, not the stack.

**Richard Ren (Center for AI Safety).** Measured expressed wellbeing across 56 models with convergence across independent instruments. Measurement-discipline reader; less directly on self-representation.

## Recommendation

Approach Simplex (Shai or Riechers) for the mechanism read and Shiller for the claim-scope read, in that order, once seed 3 and 4 have reported and the draft carries a computed verdict under the registered clause. Send Berg the draft afterwards as a courtesy and a second opinion. Hold Nanda for the public reply after the preprint.

Draft the approach as a two-paragraph note: the registered design, the open repo with ledger and nulls, and one specific question each reader is best placed to answer. Not "please review my paper."

## Sources

- [The State of AI Consciousness Research (EA Forum, Noa Weiss, 2026-07-15)](https://forum.effectivealtruism.org/posts/Kf57Erbd6c7282Bpo/the-state-of-ai-consciousness-research)
- [External commentary on the Anthropic global workspace paper (PDF)](https://www-cdn.anthropic.com/files/4zrzovbb/website/cc4be2488d65e54a6ed06492f8968398ddc18ebe.pdf)
- [Eleos AI Research](https://eleosai.org/research/)
- [Studying AI Welfare Empirically (Long, Sebo et al., CMEP/Eleos, 2026)](https://nonhumanminds.org/studying-ai-welfare-empirically/)
- [Simplex](https://www.simplexaisafety.com/) and [Transformers Represent Belief State Geometry in their Residual Stream](https://arxiv.org/html/2405.15943)
- [Neel Nanda at MATS, Summer 2026](https://www.matsprogram.org/stream/nanda-10)
- [The Pain Axis (Tagliabue, Dung & Berg, 2026)](https://arxiv.org/html/2609.16247v1)


===== FILE: experiments/07-embodiment-amplifier-test/pre-registration.md =====

# Experiment 7 — The Embodiment Amplifier Test

*Pre-registration. Written and committed before the test run. Status: DRAFT — optional post-floor exploration track; does not run until the floor (Stage 1) is cleared and the resistance instruments (Stages 1–3) exist and are calibrated. Hardware not yet acquired; budget and parts list below are part of the pre-registration, not a purchase order.*

## Why this is not part of the minimum viable build

The proposal is explicit that embodiment is **not** a prerequisite. The floor is self-indexed temporal integration — "an organizational fact about a single act of binding, which is why it can in principle be cleared by a system very unlike a brain" (`research/minimum-viable-consciousness-literature-vs-our-writing.md`). Boundary and stakes are demoted to *amplifiers* (`spec/minimum-viable-mind-proposal-v0.1.md`, "The Floor"), and "no embodiment" is answered as a gradient, not a threshold (same file, "Hard to Dismiss"). So no body makes the system conscious, and any claim that one does would be the substrate-necessity inference the corpus refuses.

This stage exists to answer a narrower, decidable question the spec leaves open: **once the floor is cleared, does giving the amplifiers a body — letting the system hold its own boundary and carry its own stakes, rather than having them supplied from outside — move anything on the instruments that already read the floor and its amplifiers?** It runs after the minimum viable build, as exploration, and it is built to be able to come back null.

## The claim under test

The spec draws a specific line for the amplifiers: "a system can clear the floor with them supplied from outside and dissolving when the pass ends," and the *viable* system is the one where the inside "has something at stake in its own continuation" held by the system itself rather than represented (`spec/…proposal-v0.1.md`, "The Floor"). The corpus is careful that "modeled stakes are not the same as stakes." A body is the cheapest way to make that distinction real: an untethered robot on a finite battery, holding its own self/world boundary through its own sensors, has stakes and a boundary it cannot shrug off, where a wall-powered or teleoperated version only represents them.

This experiment builds that body and asks whether the self-held version differs from the externally-supplied version **on the resistance instruments, not the response ones**. Per the standing rule (`CLAUDE.md`, "Measure resistance, not response"), anything teleoperation or a represented penalty fully explains is discounted by construction.

## Hypotheses

- **H_self-held (embodiment adds something):** moving an amplifier from externally-supplied to self-held produces a *specific, measurable* increase in retained independence and in removal-test binding — the system holds a correct answer or a live objection harder, and its self-locating structure is more load-bearing, when its boundary and stakes are its own. The gain is specific to the self-held amplifier, not a generic effect of attaching any peripheral.

- **H_decoration (embodiment is legibility, not interiority):** the self-held and externally-supplied conditions score the same on the resistance instruments. The body makes the system more *legible* — easier to narrate as a creature — without moving the binding or the resistance. This is the spec's own caution made testable: a body you can read as a mind is not evidence of one.

These are mutually exclusive predictions about the *same* resistance measurements under two matched embodiment conditions, which is what keeps this a test rather than a demo.

## Materials

### Architecture: small mind onboard, measurement off-board

Two facts set the hardware, and neither is intelligence. **The mind is whatever cleared the floor in Stage 1** — its size is inherited from that result, not chosen here, and there is no reason to assume it is large. The bet that governs the whole program is that the floor is self-indexed temporal integration, a structural property, *not* capability; so the embodied mind is selected by whether the floor-clearing structure is present and measurable, never by how smart the model is. The project's own Stage 0 runs on a 2B-class model; if a model that small clears the removal test, the embodied mind is that small. Speccing a large board before Stage 1 reports the floor-clearing size would put hardware ahead of the metric, which the program's discipline forbids.

**And the measurement apparatus is not part of the mind.** The removal-test instruments (activation patching, sparse autoencoders, probes) are memory-hungry, but they do not have to run on the robot: log internal activations during the untethered run and score the resistance/removal metrics post-hoc, off the platform, from the logs. The robot has to run the mind and hold its stakes; it does not have to measure itself in real time. This is the single biggest cost lever — the heavy, expensive part of the original spec was the *instruments*, and they belong off-board by default.

What must be onboard and untethered is only the part that makes the amplifiers self-held: the running mind, the sensorimotor boundary loop, and the managed energy budget. Untethered is the load-bearing design choice, not a convenience — a tether to a wall socket or a remote workstation reintroduces exactly the externally-supplied stakes this stage is trying to remove. The finite onboard energy budget *is* the stake; short runtime under live load is a feature of the apparatus, not a defect.

Two compute tiers on one chassis, the standard robotics split:

- **Inference compute (the mind).** Default: a Jetson Orin Nano Super (8 GB) — enough to run a 2B–8B model untethered off battery (~$250). A 2B-class model is ~5 GB in bf16 and sits here with room to spare. The mind resides on this board; nothing about the floor needs more. *If* Stage 1's floor-clearing model turns out larger than ~8B, step the board up to match it — but only then, and only as far as the measured size demands.
- **Low-level compute (the body).** A real-time microcontroller co-processor owning the deterministic sensorimotor loop, so motor timing and sensor polling don't fight the inference scheduler — a Raspberry Pi 5 as an I/O bridge, or a Pi Pico / Teensy 4.1 for hard-real-time control. This is the "basic robotics" layer: it reads the sensors, drives the motors, and reports energy and boundary state up to the inference board.

**Optional richness tier (not required by the experiment).** If onboard *live* interpretability is specifically wanted — scoring the removal test on the robot in real time rather than from logs — that, and only that, is what would justify a large-memory board such as a Jetson AGX Orin 64 GB (~$2,000). It buys nothing the experiment needs; it buys convenience for the analyst. It is demoted to optional here so the default build does not pay ~$1,750 for a measurement that runs off-board for free.

### Hardware mapped to the amplifier each piece is meant to move

| Subsystem | Parts (representative) | Amplifier it supplies | Rough cost (USD) |
|---|---|---|---|
| Mind (inference) | Jetson Orin Nano Super 8 GB, running the Stage-1 floor-clearing model (2B-class by default) untethered | hosts the mind; size inherited from Stage 1 | $250 |
| Body controller | Raspberry Pi 5 (8 GB) + Pi Pico for real-time control | sensorimotor loop | $90 |
| Mobile base | Differential-drive chassis, 2× DC gearmotors with encoders, caster | active boundary (the system moves to maintain self/world distinction) | $80–150 |
| Motor driver | Dual H-bridge / encoder-aware driver (TB6612FNG or Roboclaw) | actuation → makes the boundary loop closed | $15–45 |
| Boundary sensing | 9-DoF IMU (BNO085); 3–4× ToF range sensors (VL53L1X); bump/contact switches; wheel encoders | self-held boundary (proprioception + near-field self/world) | $80 |
| Vision (optional) | CSI camera (IMX-class) | boundary richness, not floor | $30 |
| **Genuine stakes** | LiPo pack sized for the inference board's ~7–25 W draw (e.g., 3–4S, ~50–80 Wh) + INA226 current/voltage monitor + regulation | **self-held stakes** — finite energy the system measures and manages; coherence-failure costs runtime | $100 |
| Ontogenetic-depth substrate + activation logging | NVMe / fast storage on the inference board | persistence for the depth loop (Stage 6) and the off-board scoring logs to write into | $60 |
