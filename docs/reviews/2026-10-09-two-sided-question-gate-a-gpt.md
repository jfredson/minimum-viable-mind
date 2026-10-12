Model: gpt-6-astra (provider version 1787853604, as the API reports it)
Date: 2026-10-09 (UTC 2026-10-09T18:01:44Z to 2026-10-09T18:06:16Z)
Mode: documents shown (the packet `docs/reviews/packets/2026-10-09-two-sided-question-gate-a-tier2-packet.md`, with the reply labels set to A; SHA-256 of the exact message 3598235869d7fd6c088b626eaff554a9e29301bc7c31777907c5750b39ac9268), by API, one message, no system prompt, no tools, no web access, reasoning effort high; output limit 12000 tokens
Usage: {"input_tokens": 42780, "output_tokens": 11393, "reasoning_tokens": 6214, "status": "completed", "response_id": "resp_0240bab56b859211006ac92c09a1b087d08b48096d183f82a5"}

*Filed word for word by `docs/reviews/2026-10-09-two-sided-question-gate-a-scripts/tier2_packet_and_run.py`; nothing below the rule is edited. Sent by API rather than by John through the app, which is a departure from the protocol's tier 2 wording; see the pass's covering note, `docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`.*

---

**Recommendation: do not write section 2 into the spec as shown.** The change of research target is defensible. The claims that motivate it, the conclusions it promises, and the rules that would bind later experiments are not yet aligned.

I reviewed only the supplied packet. Scripted API delivery does not materially change this document review, but I cannot inspect repository state, verify hashes, or run closure checks. **Every finding below is ARGUED.** None is a MEASURED closure.

Below, **P** means `docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md`; line references use the proposal’s original numbering.

## 1. Feasibility

| Finding | Severity | Quantity or threshold | Assessment and supporting record |
|---|---|---|---|
| **A1** | **fatal** | Presence ratings tracking fluency “no better than chance” — P, lines 153–169 | No rating instrument, fluency measure, chance model, or rehearsal is supplied. The inside review reports that none exists. This meets the explicit fatal condition in `docs/outside-review-protocol.md`. |
| **A2** | **fatal** | “Degree measured” and placement “on the axes at a degree” — P, lines 171–174 and 188–199 | No instrument converts these battery readings into axis degrees. No rehearsal or committed measurement supports that promised output. As binding reporting language, “degree measured” triggers the protocol’s unsupported-measurement rule. |
| **A3** | **serious** | The “smallest” configuration that “passes the battery”; “decidable within a family” — P, lines 140–151 | Parameter count is measurable. The claimed minimum is not yet defined: there is no system-level pass rule, bounded candidate set, treatment of training variability, or stopping rule. The battery draft supplies row-loss rules, not a procedure that returns this minimum. |

### A1 — The observer threshold is not merely awaiting participants

The missing pieces are the measurement itself. “Chance” could mean zero correlation, shuffled model labels, random rankings, or a classifier’s baseline accuracy. Those are different quantities. Nothing specifies which one binds.

There is also a statistical error waiting behind the missing instrument. Failure to detect a relationship does not establish that ratings track fluency no better than chance. A small study, a restricted range of highly fluent models, or unreliable ratings could all return that result even when fluency matters substantially. A future loss condition would need a specified effect size, adequate sensitivity, and a rule for distinguishing evidence of a negligible association from an inconclusive result.

The record already supplies the immediate repair: ruling 10 in `docs/rulings/2026-10-07-two-sided-question-rulings.md` defers this to a later **design question**, not a run. State that ruling and remove the threshold. No human-study rehearsal is owed now if no human-study measurement is being registered now.

### A2 — A row score is not yet a degree of Integration or Depth

`docs/filtered-battery-proposal-2026-10-07.md` on branch `felt-features-table-2026-10-09` describes contrasts, gaps, and row dispositions. It does not establish how a particular gap becomes a position on an axis, whether different rows share a scale, or whether increasing a score means increasing the proposed property.

The book summary itself calls the signatures diagnostic heuristics, not validated independent measurements: `~/Code/calibration-problem/editorial/argument-summary-2026-10-07.md`, chapter 4. The founding-wager proposal explicitly says the degree metric does not exist: `docs/founding-wager-proposal-2026-09-20.md`.

The fatal rating concerns the binding promise **“degree measured,”** not the absence of completed future research. Replace it with what the proposed instruments could actually return:

> Named construction contrasts, row-level scores and uncertainty; no validated axis degree yet.

Also remove the unconditional **“non-zero.”** An honest output rule must permit zero, failure, and an unmeasured quantity. “Never a verdict” does not cancel an unsupported positive placement.

### A3 — Counting parameters does not make a minimum decidable

Restricting the search to one construction family avoids an absolute claim across all architectures. It does not, by itself, make the search finite or settle what counts as success.

A family can contain indefinitely many sizes, configurations, histories, and training seeds. Even at a fixed size, a failed training run does not establish that no passing configuration exists. A larger passing model does not establish that every smaller model fails.

A workable registration can instead specify:

- a finite size grid and candidate-selection procedure;
- a fixed battery and system-level pass rule;
- a rule for combining training seeds and uncertainty;
- a maximum search budget;
- outcomes of “smallest tested passing size,” “none passed within the registered search,” and “inconclusive.”

Those are decidable outputs of a finite experiment. “The smallest configuration in the family” is a stronger claim.

### Remaining quantity audit

The other named properties are reversal cost, consistency across linked-but-undisclosed situations, selective refusal with a history, history-dependent change, and stakes not supplied by the prompt. **Section 2 supplies no numeric thresholds or complete instruments for them.**

The supplied battery draft marks the relevant discriminating work as design-only or dependent on future constructions. Consequently, **no supplied record demonstrates reachable control ceilings or thresholds for those discriminators**. Experiment D’s reported retention values are not measurements of reversal cost, and the draft correctly acknowledges that.

That absence need not be another fatal finding if these remain explicitly identified research aims, with instruments and rehearsals deferred to their own registrations. Section 2 must not simultaneously defer the instruments and promise measured degrees.

The historical removal-test numbers do have a record: `experiments/01-self-indexing-removal-test/removal-test-findings.md`. The principal problem there is interpretation, addressed under A12 and A14, not missing numerical provenance.

## 2. Satisfied by the wrong thing

| Finding | Severity | Failure route | Required restriction |
|---|---|---|---|
| **A4** | **serious** | “Weights and transcript” are treated as proof that named cheaper mechanisms exhaust a frontier model’s computation — P, lines 140–165. | Distinguish a system’s state sources from the algorithms those states implement. Call frontier readings reference observations, not independently established mechanism labels. |
| **A5** | **serious** | A matched construction contrast can detect an ordinary learning, reset, or control effect while being described as evidence of a richer feature — P, lines 140–151. | Test ordinary adaptive competitors and limit the conclusion to the causal contrast actually isolated. Matching is not elimination of alternative mechanisms. |
| **A6** | **serious** | Moving the same memory across the declared system boundary can change its classification from “cheaper route” to “history became structure” — P, lines 142–150. | Fix the system boundary and say which causal property, rather than storage location, distinguishes the routes. |
| **A7** | **serious** | Observers can identify construction arms through fluency, competence, latency, style, or failure patterns rather than the intended feature — P, lines 153–165. | Construction labels are not sufficient ground truth for calibrated perception. Require independent checks of the manipulation and competing visible cues. |
| **A8** | **worth-noting** | Repeated battery, family, and threshold selection can fit the evaluation despite an unpublished item bank — P, lines 140–151. | Separate development from final confirmation and record every search that selected the reported system. |

### A4 — An inventory of inputs is not an inventory of mechanisms

The battery draft’s section 0 argues that a frontier model’s replies depend on trained weights and the transcript, then identifies those with policy, imitation, persona, lookup, and routing. Section 2 imports the conclusion by calling frontier readings **known** cheaper-route reference profiles.

The inference does not follow. Fixed weights can implement a board model, workspace-like computation, error correction, or other structured algorithms. Calling the whole computation a “trained response policy” does not distinguish those mechanisms from imitation. The supplied book summary itself reports workspace-like representations emerging in a trained model. No external source is needed to expose the inconsistency.

A frozen system’s lack of lasting updates between encounters can support a narrow conclusion about **encounter-specific persistence**, assuming the interface’s state model is correct. It does not establish the absence of every relevant within-pass structure.

If “cheaper route” is defined to mean anything weights and a record can implement, the classification is true by definition. It is then not a negative control establishing that the proposed structural feature is absent. The spec should choose and state the narrower claim.

### A5 — “We changed the construction and the score changed” is not enough

Consider an ordinary adaptive controller with:

- a learned table of commitments;
- a resource penalty for changing entries;
- an update rule that responds differently to evidence and commands;
- a reset that erases some recent learning.

It can exhibit persistence, selective refusal, costly reversal, and traces of consequential history without any separately demonstrated self-centred integration. Its consequential version can differ from training on a transcript simply because resetting state changes later computation.

This is an **unrun counterexample design**, not a claim that such a controller has passed the proposed battery. It identifies the ordinary competing solver the rehearsal should attempt.

Some of those properties may be exactly what the project now intends to call Depth. That is permissible. But then the result is about those operational properties; it does not establish an additional structure merely by calling them “real features.”

The battery’s non-token consequence is especially vulnerable here. A reset can leave a behavioural mark through ordinary information loss or a changed optimization trajectory. Exposure matching does not remove those alternatives.

The same limit applies to the inside review’s RT-288. Holding another route constant does not establish that it is irrelevant: it may interact with the manipulated route. A pair identifies a particular intervention effect, not the inability of an entire alternative class to produce the behaviour.

### A6 — The boundary can decide the answer before the experiment

The battery draft’s fresh-instance test supplies the fresh system with everything outside the weights. That makes the placement of information crucial.

Imagine two implementations of the same learned response function. One stores an encounter-specific vector in model weights. The other stores the vector in a memory module read by otherwise fixed weights. A fresh-instance comparison can classify them differently because the copying rule treats those storage locations differently, despite equivalent behaviour and equivalent causal use of history.

A distinction between these implementations may be scientifically useful. But “inside weights” is not automatically “assembled history,” and “outside weights” is not automatically a mere description.

Each construction registration should define the whole tested system—including memory, update machinery, and any reset controller—and identify the additional causal property at issue. Otherwise the experiment can win by putting an ordinary store on the favoured side of a boundary. It can also make “smallest” misleading by counting model parameters while leaving substantial machinery outside the count.

### A7 — Known construction is ground truth for what was built, not for what observers detected

This is not an objection that demands ground truth about consciousness. The project has properly withdrawn that claim.

It is an objection about the proposed observer measurement. Knowing which arm received a memory mechanism does not show that a participant’s rating tracked memory rather than that arm’s longer answers, improved task success, distinctive hesitation, or characteristic errors. Blinding participants to battery scores does not blind them to these cues.

A future design must distinguish at least:

1. whether the intended mechanism was installed and used;
2. whether it changed the proposed indicator;
3. whether observers detected that indicator rather than competing differences.

A positive result could then be reported as observer sensitivity to a specified manipulation or feature. “Detections of presence track structure rather than fluency” requires more than successful arm classification.

### A8 — A hidden bank does not cover the whole search

The battery draft already provides unpublished held-out items and repeated seeds. Those are useful safeguards.

The residual risk is selection over architectures, histories, row definitions, and pass thresholds. A “smallest passing system” search is particularly exposed: repeated inspection can select a lucky model or redefine success around what was found. The binding requirement should be final confirmation under a frozen rule, using data not used to choose that system or rule. This can be small and budget-aware; it need not be an expensive extra study.

## 3. No verdict

| Finding | Severity | How the process loses its answer | Needed repair |
|---|---|---|---|
| **A9** | **serious** | Rows can be discarded after failing, while “passes the battery” remains undefined; the battery can become easier after the evidence arrives — P, lines 148–151 and 188–199. | Freeze the battery version and success rule for each claim. Separate candidate failure, instrument failure, and battery revision. Write the actual replacement loss paragraph. |
| **A10** | **serious** | The resulting spec would contain incompatible instructions about its target and admissible instruments, and depends on an unreviewed founding section — P, lines 101–110, 116–151 and 179–199. | Give explicit precedence and supersession rules; resolve the founding-wager dependency and the corroborated-report exception before commitment. |
| **A3, continued** | **serious** | An unbounded minimum search need never return a negative verdict, even when every affordable run fails. | Register a finite search and an honest “none found within this search” outcome. |

### A9 — A failed indicator must not silently cease to be a requirement

The battery draft says a row moves to DISCARD when matched constructions read the same. That may be the correct response when an indicator proves non-discriminating. But it creates a problem for section 2’s system-level definition.

Suppose a candidate clears four rows and fails five. If those five are then removed, does it now “pass the battery”? Without a frozen version and aggregation rule, the text permits that reading. The same system can move from failure to success without changing and without new confirmatory evidence.

There are three different outcomes to keep separate:

- **Candidate failure:** a valid instrument did not detect the required property in this candidate.
- **Instrument failure:** the test could not distinguish the registered controls.
- **Theory or battery failure:** the proposed indicator did not behave as predicted.

They do not license the same public conclusion or the same next step. A later battery revision should not retroactively turn an earlier candidate into a registered success.

The supplied battery has useful loss conditions, but section 2 neither incorporates them by a fixed reference nor writes its own replacement paragraph. The text at P, lines 188–199 describes a proposed suspension and an upstream request; it is not the exact operative paragraph that reviewers are being asked to approve. That is an unresolved specification, not merely an editorial inconvenience.

### A10 — Later registrations could select whichever rule suits them

The contradictions identified by the inside review are real:

- `spec/minimum-viable-mind-proposal-v0.1.md` says the project targets a measurable floor; the addition says it does not measure that floor.
- The existing Build section uses removal as its pass-fail criterion; the addition calls it a definition rather than an instrument.
- “Minimum viable” acquires a second definition without withdrawing the first.
- The new “only” rule requires matched constructions, while the battery permits a corroborated report under a known internal intervention.
- The insertion presupposes `docs/founding-wager-proposal-2026-09-20.md`, which has not passed this review process.

These conflicts can prevent a verdict, but they can also allow convenient verdict selection: one later registration cites the new rule, another cites the unchanged old one.

The repair need not erase the project’s history or rewrite John’s prose without permission. Dated supersession notes can preserve the earlier text while unambiguously saying what no longer binds. The final assembled spec, including the exact loss paragraph, is what should receive the closure check.

## 4. Over-reading

| Finding | Severity | What will be claimed beyond the evidence | Correct scope |
|---|---|---|---|
| **A11** | **serious** | Because experience is accessible only conditionally on an identity claim, the proposed underlying structure cannot yield new empirical information — P, lines 116–127. | Unsettled identity does not imply unmeasurable structure. State a present instrument limitation, not a general impossibility. |
| **A12** | **serious** | Damage on all three batteries means the router control necessarily rejects a real centre — P, lines 120–127 and 181–186. | Shared positive drops do not entail the inequality that triggers the router control. The record supports underdetermination of the observed result, not the stated impossibility argument. |
| **A13** | **serious** | The old depth-versus-binding loss condition has no empirical input once the experience floor is no longer measured — P, lines 188–199. | The old condition concerns observable architecture as well as its interpretation. Retain the structural counterexample or explain specifically why it cannot be tested. |
| **A14** | **worth-noting** | The later reinterpretation will be read as the experiment’s original registered finding, with “every task” suggesting uniform damage. | Preserve the original verdict, distinguish the dated reinterpretation, and report the concentration and uncertainty of the damage. |

### A11 — The identity claim does not already contain the measurements

Even if experience and some structure are identical, that premise does not tell us which systems instantiate the structure, how it works, or what interventions change it. Those remain empirical questions.

Conversely, if rival metaphysical accounts predict the same structural measurements, an experiment may fail to distinguish those accounts while still teaching us about the structure. The founding-wager proposal itself relies on this distinction when it says a reader rejecting the wager can retain the structural findings.

The sentence saying no instrument can return anything the identity does not already say therefore overreaches. It also conflicts with the supplied book summary’s proposed interventions and discussion of measured workspace-like structure.

A defensible replacement would be:

> The project currently lacks a validated method for separating the proposed self-locating structure from indispensable bookkeeping. It therefore redirects its measurements to specified construction contrasts. Any interpretation in terms of experience remains conditional on the founding wager.

That preserves the refounding without turning a failed instrument into an impossibility theorem.

### A12 — “All tasks are damaged” does not mean “turn tracking is damaged at least as much”

This is the main logical gap not isolated by the inside review.

`docs/outside-perspective/2026-10-07-router-control-check.md` argues:

1. removing a real centre damages all three batteries;
2. the router rule fires when turn-tracking damage is at least self-relevant damage;
3. therefore a real centre’s removal is classified as routing.

Step 3 does not follow. The first premise says nothing about the relative sizes of the drops.

For illustration only, consider these **hypothetical, unmeasured** drops:

- self-irrelevant: 0.20;
- self-relevant: 0.30;
- turn tracking: 0.10.

All three batteries deteriorate. Yet the router condition, `0.10 ≥ 0.30`, is false. With suitable specificity comparisons and valid intervention gates, this pattern could reach the quoted centre decision rule. It is not the restricted pattern in which self-irrelevant performance survives.

This does **not** show that the book predicts those numbers, or that the removal test is a valid centre detector. It shows that the cited qualitative prediction does not exclude them. An inability to derive a discriminating prediction is different from proving that the registered control must reject every centre-consistent result.

The actual result remains ambiguous: its router gap was +0.033 with a 95% interval spanning zero, and both proposed accounts can accommodate broad damage. Report that limited conclusion. Do not use this note as proof that the instrument could never return the other answer.

### A13 — The proposed suspension removes more than an unavailable consciousness verdict

The existing loss condition in `spec/minimum-viable-mind-proposal-v0.1.md` concerns a system passing the depth indicators **“without anything resembling self-indexed binding underneath.”** That is not simply a requirement to prove phenomenal absence.

A constructed system could provide evidence against the assumed link between the indicators and the proposed binding architecture. Whether that evidence succeeds depends on a defensible structural definition and inspection—not necessarily on an independent consciousness meter.

The new paragraph instead suspends the condition until the book says whether the profile is possible without the floor. That risks letting the theory decide, after a profile appears, whether it is allowed to count as a counterexample.

If the structural absence claim is presently untestable, say exactly why. But preserve a standing loss such as:

> If the registered indicators are reproduced by constructions independently shown to lack the proposed binding organization, those indicators do not support the claimed connection to that organization.

A difficulty measuring the floor does not justify withdrawing every empirical bridge between depth indicators and binding.

### A14 — Preserve the distinction between result and reassessment

`experiments/01-self-indexing-removal-test/removal-test-findings.md` records the original registered verdict. The October reinterpretation changes what is inferred from those figures. It should be presented as a dated reassessment, not rewritten into the July registration’s successful execution.

The rulings already require disclosure that the founding wager was adopted after the earlier experiments. Carry that discipline into the binding text and later reporting.

Also replace “damage spread across every task” with “positive point-estimate drops on all three batteries,” accompanied where relevant by the uncertainty and concentration of failures. Six of seven flipped self-irrelevant items were multi-step reasoning items. That matters to what kind of disruption the intervention produced.

### Reporting guardrail for the paper, STATUS.md, and public material

I have not seen the current paper, STATUS.md, or site, so these are risks the new text creates, not findings about those documents.

A defensible headline result would look like:

> Within the registered family and tested size grid, construction X produced contrast Y against comparator Z. It was the smallest tested configuration meeting the frozen rule. This identifies a specified construction effect, not a validated degree of mind, an exclusion of all cheaper mechanisms, or a verdict about experience.

Observer findings should separately name the cues and manipulations tested. Do not compress the two studies into “we built the minimum mind and people detected it.”

## Kill case

The strongest case against this refounding is that it risks rebuilding the original identification problem under new labels. Frontier systems become “cheaper routes” by definition; constructed systems become ground truth because the intended feature was installed; ordinary learning and reset effects can supply the behavioural contrast; failed indicators can be discarded; and the original depth-versus-binding counterexample is suspended. The resulting programme could repeatedly obtain the expected construction differences without independently establishing that it measures the book’s axes or what makes a mind feel present. That would still be legitimate instrument and adaptive-systems research, but the spec would advertise more than it had earned. The refounding survives this kill case only if it fixes operational properties independently of preferred implementations, tests ordinary competing solvers, freezes success and failure rules, and reports the resulting contrasts without automatic “non-zero” or “degree measured” language.

## Differences from the inside reviewer

- **RT-289: serious → fatal as written.** The binding phrase “degree measured” has neither an instrument nor a supporting record. The protocol explicitly makes an unsupported measurement claim fatal. Recasting it as an unvalidated future aim removes that basis.
- **RT-286: retain serious, but reject the claimed necessary collision with the capacity loss condition.** A smallest passing size does not, by definition, make the within-construction size effect larger than the between-construction effect. Both rules can coexist. The missing pass rule and unjustified minimum remain serious.
- **RT-283: retain fatal.** Lack of authorization to run does not stop its pre-stated threshold from binding a future design if committed unchanged.
- **RT-288: retain serious, but strengthen the closure.** Matching other routes does not exclude them or their interactions. The conclusion must remain limited to specified tested constructions and interventions.

I would not otherwise change the inside findings’ severity. The largest additional issues here are A11–A13: the move from uncertain identity to structural unmeasurability, the missing inequality in the router argument, and the excessive scope of the suspended loss condition.
