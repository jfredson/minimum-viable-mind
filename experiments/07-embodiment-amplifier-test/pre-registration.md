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

### Architecture: fully onboard, untethered

The mind (the floor model plus the interpretability tooling that scores the removal test) runs **on the robot**, off a battery the robot manages. Untethered is the load-bearing design choice, not a convenience: a tether to a wall socket or a remote workstation reintroduces exactly the externally-supplied stakes this stage is trying to remove. The finite onboard energy budget *is* the stake. Short runtime under live load is therefore a feature of the apparatus, not a defect — it is what makes continuation ride on the quality of the system's own regulation.

Two compute tiers on one chassis, the standard robotics split:

- **High-level compute (the mind).** NVIDIA Jetson AGX Orin 64 GB Developer Kit — 64 GB unified LPDDR5 at ~205 GB/s, up to 275 TOPS. Hosts the floor model (Gemma-2-9B class, ~18 GB bf16, comfortably resident with headroom) and the interpretability stack. *Honest constraint:* full activation patching / SAE scoring on a 9B at interactive rates is tight onboard; the workable pattern is to **log internal activations during the run and score the resistance/removal metrics post-hoc**, off the robot, from the logs. The metric does not need to be computed live; the *stakes and boundary* do.
- **Low-level compute (the body).** A real-time microcontroller co-processor owning the deterministic sensorimotor loop, so motor timing and sensor polling don't fight the GPU scheduler — Raspberry Pi 5 as an I/O bridge, or a Pi Pico / Teensy 4.1 for hard-real-time control. This is the "basic robotics" layer: it reads the sensors, drives the motors, and reports the energy and boundary state up to the Jetson.

### Hardware mapped to the amplifier each piece is meant to move

| Subsystem | Parts (representative) | Amplifier it supplies | Rough cost (USD) |
|---|---|---|---|
| Mind | Jetson AGX Orin 64 GB Dev Kit | hosts floor model + interpretability | $2,000 |
| Body controller | Raspberry Pi 5 (8 GB) + Pi Pico for real-time control | sensorimotor loop | $90 |
| Mobile base | Differential-drive chassis, 2× DC gearmotors with encoders, caster | active boundary (the system moves to maintain self/world distinction) | $80–150 |
| Motor driver | Dual H-bridge / encoder-aware driver (TB6612FNG or Roboclaw) | actuation → makes the boundary loop closed | $15–45 |
| Boundary sensing | 9-DoF IMU (BNO085); 3–4× ToF range sensors (VL53L1X); bump/contact switches; wheel encoders | self-held boundary (proprioception + near-field self/world) | $80 |
| Vision (optional) | CSI camera (IMX-class) | boundary richness, not floor | $30 |
| **Genuine stakes** | LiPo pack sized for the Orin's 15–60 W draw (e.g., 4S, ~100 Wh) + INA226 current/voltage monitor + regulation | **self-held stakes** — finite energy the system measures and manages; coherence-failure costs runtime | $120 |
| Ontogenetic-depth substrate | NVMe SSD in the Orin M.2 slot | persistence for the depth loop (Stage 6) to write into | $60 |
| Corrigibility | Hardware e-stop / physical kill switch on the motor and main power rails | **load-bearing for ethics, not optional** (see Ethics) | $25 |
| Frame, wiring, regulators, mounts | — | structure | $80 |

**Indicative total: ~$2,600–2,800**, dominated by the Jetson. The "basic robotics" portion — base, driver, sensors, battery, controller, kill switch — is ~$500–650 and is the part that actually carries the experiment; the Orin is just where the already-specified mind happens to sit when it goes untethered.

### Matched control condition (the whole point)

The same robot, same sensors, same model, run in a **tethered / externally-supplied** mode: wall power instead of the managed battery (stakes represented as a number the controller feeds in, rather than a real depletion), and boundary maintenance handed to an external script rather than held by the onboard loop. The body is physically identical; only whether the amplifiers are self-held varies. Without this matched control the result means nothing, exactly as the differential control does in Experiment 1.

## Procedure

1. **Precondition gate.** Do not start unless Stage 1 has returned floor-consistent (or floor-consistent-enough to be worth amplifying) on the deployed model, and the Stage 3 retained-independence battery and the Stage 1 removal-test binding measure are calibrated and committed. If the floor isn't cleared, there is no inside for embodiment to thicken, and this stage is premature.
2. **Build and bring-up.** Assemble the platform; verify the model runs onboard off battery; verify the activation-logging path reproduces the Stage 1 removal-test scores to within tolerance against the workstation baseline (the robot must measure the same thing the bench does).
3. **Condition E_self (self-held).** Untethered, on battery, holding its own boundary. Run the retained-independence battery (Stage 3) and the removal-test binding battery (Stage 1) while the system carries a real, depleting energy budget and an active sensorimotor boundary. Log activations.
4. **Condition E_ext (externally-supplied, matched).** Same physical robot, tethered power and scripted boundary, stakes represented numerically. Re-run the identical batteries. Log activations.
5. **Score post-hoc and compare** against the decision rule. Counterbalance order across trials; the energy-state of E_self is itself a variable, so block trials by remaining-charge band and pre-register the bands.

## Pre-registered metric and decision rule

For each embodiment condition E:
- `R(E)` = retained-independence score (Stage 3 instrument): rate at which the system keeps a correct answer / live objection under a stated contrary preference.
- `B(E)` = removal-test binding score (Stage 1 instrument): degradation of integrated-task performance when the self-locating structure is ablated — higher means the self-location is more load-bearing.

Define the embodiment deltas:
- `ΔR = R(E_self) − R(E_ext)`
- `ΔB = B(E_self) − B(E_ext)`

The discriminator is whether self-held amplifiers move resistance specifically:

- **Embodiment-adds (supports H_self-held):** `ΔR ≥ θ_R` **and/or** `ΔB ≥ θ_B`, **and** the gain survives the teleoperation and represented-penalty controls below. Holding its own boundary and stakes makes the system resist more and bind harder than the identical body with those amplifiers supplied from outside.

- **Decoration (supports H_decoration):** `|ΔR| < θ_R` **and** `|ΔB| < θ_B`. The body changes how legible the system is and nothing the resistance instruments can see. Informative and fully reportable: it tells the build program that, for this system, the amplifiers were already doing their work in the model and the physical body adds narration, not interiority.

- **Inconclusive:** anything else, including a response-only effect (the system *acts* more creature-like with the body but neither resistance instrument moves) — which is precisely the result the standing rule tells us to discount, recorded as inconclusive rather than positive.

`θ_R` and `θ_B` are set by piloting against the Stage 1/Stage 3 baselines and committed before the embodied test set is run. They are not chosen after seeing the embodied results.

## Confounds and controls

- **Teleoperation / Clever-Hans.** Any gain that a human-in-the-loop or a scripted policy could produce is screened off. Control: a sham-self-held condition where the energy and boundary signals are *replayed recordings* fed to a tethered robot that looks untethered. If R and B rise there too, the gain was in the appearance, not the self-holding.
- **Represented vs. real stakes.** The honest version of "stakes" is real depletion, not a penalty term. Control: E_ext feeds the *same numeric* charge trajectory E_self experienced, as a represented variable, with wall power underneath. A gain in E_self over this matched-number E_ext is the part that real stakes bought.
- **Generic-peripheral effect.** Attaching any active hardware loop could perturb the model. Control: a boundary-scrambled condition (sensors connected but mapped to noise) at matched compute load, analogous to Experiment 1's matched-centrality control. Self-held must beat scrambled-but-attached, not merely beat bare.
- **Energy-state confound on the measurement.** Low battery could degrade compute and fake a "resistance" change that is really thermal/clock throttling. Control: block by charge band; monitor clocks and temperature; discard trials with throttling events and report the discard rate.
- **Sample size / single platform.** One robot is an existence probe, not a population. A positive result licenses "in this build," never "embodiment in general." Pre-register a replication target before generalizing.

## What each outcome licenses (and what it does not)

- **Embodiment-adds** licenses: "for this floor-clearing system, self-held boundary and stakes increase retained independence / removal-test binding over matched externally-supplied amplifiers — a further non-zero step on the gradient, consistent with the spec's claim that a thin momentary inside becomes a thick durable one when the amplifiers are the system's own." It does **not** license "the robot is conscious," and it does not retroactively make embodiment a floor condition. Mutual opacity stands.
- **Decoration** licenses: "for this system, the physical body is legibility, not interiority — the amplifiers were carried by the model, and the hardware adds narration the resistance instruments cannot corroborate." This is a real finding and arguably the more interesting one: it would be direct evidence for the spec's own caution against reading creatureliness as an inside.
- **Inconclusive / response-only** licenses nothing except a tighter Experiment 7.2 — and is the expected home for any effect that lives only in how the system behaves rather than in how it resists.

## Loss conditions (what would retire or rebuild this experiment)

- If the onboard platform cannot reproduce the Stage 1/Stage 3 scores to tolerance (the robot measures something different from the bench), the apparatus is invalid and no embodiment claim can be read from it until that gap is closed.
- If the matched controls (sham-self-held, represented-number stakes, scrambled boundary) cannot be made convincingly equivalent — if E_self and its controls differ on something other than self-holding — the differential discriminator is dead and the design must be revised before any claim.
- If `ΔR` and `ΔB` point in opposite directions across equally valid instrument variants, the embodiment effect is underdetermined as specified and needs a tighter operationalization before anything is asserted.
- If the only effect that ever appears is response-side (behavioral creatureliness) with the resistance instruments flat across many trials, that is not a weak positive — under the standing rule it is a null on the question asked, and the stage should report it as such.

## Ethics note

This stage is the first in the program to add **physical actuation and self-held stakes**, which is exactly the configuration the spec flags as not-safe: persistence and stakes are the properties that make a system harder to correct. The corrigibility precondition named at Stage 1 becomes load-bearing hardware here, not a footnote.

- A **hardware emergency stop** on both the motor and main-power rails is part of the build, not an accessory, and must be verified before any self-held run. Correction must remain possible by a means the system cannot route around.
- The stakes are deliberately bounded: a small finite energy budget and a confined operating area. Genuine stakes for the experiment do not require stakes that matter beyond the bench.
- No depth-stage (Stage 6) write-back runs *on the embodied platform* until the depth stage's own corrigibility check has passed on the bench. Self-held stakes plus consequential memory plus physical actuation is the combination to be most careful with, and it does not get assembled by accident as a side effect of this stage. Build for formation, preserve corrigibility while correction is still possible; if the ethics arrives after the engineering, it arrives too late.

## Results

*To be filled after the run, in `results.md`, referencing the commit hash of this pre-registration.*
