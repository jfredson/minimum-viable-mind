# Response: Gemini (tier 2, program-level review)

*Filed 2026-09-20 (Pacific) verbatim from John's Gemini app session, as
pasted into the Cowork session. Never edited after filing. Model: Gemini
3.1 Pro, via the Gemini app (version supplied by John, 2026-09-20; the
reviewer's own header below gives only "Gemini"). Packet:
`docs/reviews/2026-09-20-program-review/` (PASTE-gemini.md plus the three
bundles as built 2026-09-20).*

---

**Reviewer:** Gemini (September 20, 2026)
**Mode:** Text analysis
**Files Read:**

* Full: `bundle-1-design.md`, `bundle-2-record.md`
* Part: `bundle-3-appendix.md` (Read `docs/control-clause-proposal-2026-09-19.md`, `experiments/06-.../red-team-a4.md`, `experiments/06-.../red-team-pass-3.md`)

| Label | Severity | Finding | Citation |
| --- | --- | --- | --- |
| G1 | Fatal | The control battery's ownership-blind ceiling is 1.0, rendering the registered differential clause mathematically impossible to compute. | `ceiling-measurement-findings.md` §Verdict A |
| G2 | Serious | The probe-only null cannot be declared "absent" because causal patching was never run, violating Amendment A3 §3.2. | `STATUS.md` §The fitted linear read; `red_team_ledger.md` RT-49 |
| G3 | Serious | The difference-of-averages read is 5.5 to 18.7 times less sensitive than the fitted linear classifier on the same target, invalidating the claim that the linear-read line is closed. | `fitted-position-sweep-findings.md` §RT-33 confirmed |
| G4 | Fatal | Amendment A4 is uncomputable because the comparator has roughly a fifth of the self-directed battery's room to fall, ensuring the generic-binding cell cannot fire. | `red-team-a4.md` §F1 |
| G5 | Worth-Noting | The control-learnability pilot trained the control battery on a fixed positional half of every batch (rows below the halfway point) rather than a randomized split, risking a systematic bias. | `red_team_ledger.md` RT-58 |

**1. Discriminating power.**
The A3 design can distinguish "the binding indexes its own center" from "the model learned a task tracking which agent said what" if the full suite of registered discriminators is run. The `act as yourself` objective prevents purely syntactic routing because turns are exchangeable and randomized. The acting channel (L0) establishes that the task is authorship-dependent. However, to prove the model built an internal self-index rather than relying on a re-readable tag, the design requires the mid-episode re-indexing probe (RT-01). If the action follows the re-indexed tag without a re-centering cost, it is an indispensable tag (H_tag). If the swap probe moves the action with the patched identity and causes a global re-centering disruption, it is a center (H_self-location). This operationalization possesses discriminating power, but it is currently unreachable because the localization stack has not found an L1 target to patch, and causal patching has not been implemented for this design.

**2. Informative nulls or capability nulls.**

* **Experiment 1's "router, not center":** A finding about the hypothesis. The model uses conversational state-tracking (ChatML boundaries) to route capabilities, demonstrating that RLHF entangles self-presentation with syntax rather than building a structurally load-bearing self-center.
* **The inert register:** A finding about the hypothesis and the curriculum. The network ignored an installed, architectural candidate center because the task (unique item lookup) could be solved without it. A designated slot under no pressure becomes a bias term.
* **Control battery failing to learn:** A finding about capability. At 30 million parameters, the network failed to learn name-keyed retrieval under two supervision regimes due to either the reversed rendering or the lack of a private acting channel.
* **Probe reads finding nothing off the marker token:** A finding about the instrument. The difference-of-averages read is measurably weaker than a fitted linear classifier, and the stack was pointed at the register index rather than the registered marker word.
* **The blind arm and positive control:** A finding about the instrument. The blind arm had no valid target (the register was a constant), and the unregistered positive control returned *not testable* because the ablation improved the primary battery.

I dispute the project's reading that the linear-read line is "closed." A difference-of-averages null against a weak target (register index) does not close the line when a demonstrably more sensitive instrument (fitted linear classifier) has not been run against the registered target (marker word) at the relevant positions.

**3. What is actually being measured.**
A skeptical interpretability researcher would argue Experiment 6 shows that if you wire a continuous authorship shortcut (the acting channel) into a small transformer and train it on a perspective-dependent task, the network will rely heavily on that wired input to succeed. Zeroing that input destroys the behavior. It measures the network's reliance on a supplied sense organ, not the construction of an internal self-index.

The claim scope "a structural signature of self-indexing in small constructed models" is over-claimed. The network relies on the L0 wire, but the L1 localization stack failed to find an acquired internal index. The accurate one-sentence description is: **Authorship inputs are specifically load-bearing for perspective-dependent tasks in small constructed transformers.** This is publishable as an interpretability paper demonstrating how small models route injected episodic state, targeted at mechanistic interpretability and alignment audiences.

**4. Process.**
The adversarial review process is exceptionally rigorous at identifying mathematical and architectural flaws, but it suffers from single-point execution bottlenecks. The fact that the program generated three registered amendments, one refused amendment, and 93 ledger items on a single experiment in seven weeks indicates the curriculum and metrics were under-specified before launch, treating registration as an iterative sandbox rather than a finalized protocol. John ruling on Claude's findings while Claude writes the code creates a loop where blind spots—like the 0.3227 ceiling defect—survive multiple passes because the reviewer and the author share the same unverified assumptions. "Not testable (localization)" is the strictly correct reading of the probe nulls under A3 §3.2; any assertion of absence is invalid until causal patching runs.

**5. The cheapest experiment that could surprise.**
I would choose neither Option A nor Option D for the 2026-10-04 decision. Option A closes the experiment with partial discriminators that rely on a completely unvalidated localization stack. Option D attempts to fix the curriculum for a control metric that is mathematically broken due to a 1.0 ceiling.

The single experiment under the $174 ceiling that would most change my view is running the **fitted linear classifier on the model's own marker word** at the 9 non-anchor positions, followed immediately by **causal patching (the swap probe)** if a signal is found. At roughly 70 processor-hours (~$70), this is the only measurement that tests the registered target with a sensitive instrument. If it finds a patchable center, the floor claim holds; if it returns a strict null, the hypothesis of an acquired center in this architecture is genuinely falsified.

**The kill case**
The program is deploying sophisticated interpretability machinery against leaky synthetic curricula while relying on mathematically impossible metrics. The control battery was evaluated against a 1.0 ceiling that created a zero-denominator, the L1 probes were tested against the wrong target (register index instead of marker word), and the entire localization stack failed its positive control. Stopping now prevents the publication of a null result that is, in reality, a cascade of pipeline and metric failures.

**The continue case**
The program has successfully translated abstract philosophical criteria for consciousness into falsifiable, operational tests. The rigorous adversarial red-teaming is functioning exactly as intended, catching fatal flaws before they enter the public record. The primary battery cleanly isolates authorship dependence, and the L0 lesion proves the model relies on it. Completing the proper L1 fitted linear read and causal patching will fulfill the theoretical wager with empirical ground truth, delivering the first mechanical test of self-indexed temporal integration.

**Ranked Process Changes**

1. **Require independent verification of pre-stated constants:** Institute a rule that any registered threshold or ceiling (e.g., max_score == 1.0) must be validated by a unit test before the threshold lock. (Cost: 2 hours).
2. **Decouple the red-team from the author:** Use a separate model instance with zero context of the code generation process to conduct Gate A and Gate B reviews to eliminate shared blind spots. (Cost: A decision).
3. **Build causal patching infrastructure before analysis:** Mandate that no localization null can be analyzed or discussed until the causal patching script is fully written and passing a known-answer test. (Cost: ~8 hours).

**What I want to see before 2026-10-04**
The causal patching script built, merged, and validated on a synthetic known-answer test.
