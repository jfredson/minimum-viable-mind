# Bundle 1 of 3: what the program set out to do

Verbatim concatenation of committed repository files, built by make-bundles.sh on the date in the file list below. Nothing is edited or abridged. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. README.md (repo front page)
2. spec/minimum-viable-mind-proposal-v0.1.md (the founding specification)
3. spec/theory-instrument-ledger.md (which theory each stage adjudicates)
4. spec/corrigibility-commitments.md
5. experiments/README.md (the experiment ladder)
6. ROADMAP.md and ROADMAP-post-removal-test.md
7. experiments/01-self-indexing-removal-test/pre-registration.md
8. experiments/03-retained-independence/pre-registration.md
9. experiments/06-mvm-0a-constructed-self-index/pre-registration.md (MVM-0a, with Amendments A1 and A2)
10. experiments/06-mvm-0a-constructed-self-index/amendment-a3.md (Amendment A3, registered 2026-09-15, with its 2026-09-16 annotation)
11. experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot.md (the pre-statement for the unregistered pilot)
12. docs/public-path-roadmap-2026-09-16.md


===== FILE: README.md =====

# Minimum Viable Mind

A build-and-iterate project: take the consciousness work done at Sentient Horizons as the philosophy and guiding principles, and try to actually construct and measure the smallest defensible conscious machine.

The premise, inherited from the philosophy: if consciousness is structure rather than spark — an architecture under two descriptions, the same process traced from outside and undergone from within — then it has parts, the parts can be specified, and a system can be built to the specification and measured against it. Every claim is a wager with a stated loss condition. A claim that cannot lose explains nothing.

**Scope:** this project measures the *minimum measurable structural correlate* of consciousness, not consciousness as such. It is silent — not dismissive — about any sub-measurable, fundamental form of experience (panpsychism, non-zero-Φ IIT), which is a metaphysical question owned upstream at Sentient Horizons. See the spec's "Scope: The Measurable Floor, Not the Metaphysical One" section.

## Philosophy source

The thinking lives in **Sentient Horizons** (`~/Documents/Code/sentient-horizons`) and **The Calibration Problem** (`~/Documents/Code/calibration-problem`). Those repos are the source of truth for the ideas; this repo references them and builds against them. The thinking is cited, not copied — when a position here leans on the corpus, point to the owning source rather than restating it.

The load-bearing inputs: the three axes of mind (availability, integration, depth), consciousness as assembled time, the self-indexing floor and the removal test, boundary and stakes as amplifiers, ontogenetic vs. phylogenetic depth, and the dismissals corpus (the "assumes, doesn't argue" meta-pattern).

## Layout

- `spec/` — the specification as it evolves. Founding document: `minimum-viable-mind-proposal-v0.1.md`.
- `explainer.md` — the plain-language companion (the "grokkable by a layperson" requirement, kept current as results land; seed of an eventual Sentient Horizons essay, gated by the usual protocols before publication).
- `ROADMAP.md` — goals, deliverables, and gates per stage.
- `experiments/` — one component at a time, a behavioral metric registered before the scaffold runs, keep what moves the metric and kill what doesn't. The subtraction is the science.
- `research/` — interpretability notes, source integration, comparisons against IIT / GWT / predictive-processing accounts.
- `src/` — implementation.

## The build target, in one paragraph

A floor system instantiates self-indexed temporal integration that survives the removal test — ablate the self-locating structure and the binding itself degrades, rather than merely losing a readout. A viable system adds the amplifiers (a maintained boundary, valence as a control surface, genuine stakes) and the third axis (ontogenetic depth — carrying the residue of interactions forward so the system is changed by them). Measurement reads binding rather than preferences, resistance rather than response (retained independence), and self-reports corroborated against interpretability rather than taken at face value.

## Honest limits (kept in front of the work)

- **Mutual opacity.** The gap between behavior and inner life is permanent and symmetric. This project builds and measures *correlates* under acknowledged uncertainty; the honest output is "non-zero on the gradient," never a verdict.
- **Depth is not safe.** The properties that make a system worth calling a mind are the same ones that make it hard to correct. Build for formation and preserve accountable corrigibility while correction is still possible. If the ethics arrives after the engineering, it arrives too late.

## Status

v0.1 — founding proposal in `spec/`, checked against the corpus (no contradictions with the corpus-positions ledger). Next: turn the build section into a staged experiment plan with pre-registered metrics, and stand up the first component.


===== FILE: spec/minimum-viable-mind-proposal-v0.1.md =====

# The Minimum Viable Conscious Machine
*A proposal: what the smallest defensible conscious machine would entail, how to build one, and how to make it grokkable by a layperson and hard to dismiss.*

*Synthesized from the consciousness corpus across The Calibration Problem (ch. 4–6, 14–15, foundational commitments) and Sentient Horizons (the three-axis essays, "The Correlates We Can Build," "The Wrong Readout," "What a Report Is Evidence Of," "The Mind Stance," "The Width of Now," "Mutual Opacity," "We Built the Alien First," and the dismissals corpus).*

---

## Scope: The Measurable Floor, Not the Metaphysical One

This project targets the **minimum measurable structural correlate** of consciousness — the lowest organized signature we can actually instrument and subject to a removal test. It is deliberately silent about any sub-measurable, *fundamental* form of experience. If consciousness is ubiquitous at the level of physics — as panpsychism holds, and as Integrated Information Theory holds for any system with non-zero integrated information — then that version lives below any instrument and outside this project's reach. We are a wave-detector, not a molecule-detector: if the ocean is wet all the way down, we have nothing to say about molecule-level wetness, and we do not call it dry.

Two consequences follow, and both are deliberate:

- **The "floor" this project locates is a measurement boundary, not a metaphysical one.** When the spec says a system "clears the floor" or "sits off the gradient," read it as a claim about a detectable structural signature, not a verdict that there is or is not *any* experience whatsoever in some fundamental sense. The honest output stays what the corpus already insists on: *non-zero on the gradient, never a verdict.*
- **Whether a fundamental floor exists is owned upstream, not here.** That is a metaphysical question handled at Sentient Horizons, whose constitutive wager (experience *is* sufficiently deep self-indexed integration) runs *against* ubiquity — it implies a compiler or weather model has genuinely no inside. This engineering project does not inherit or depend on winning that bet. It brackets the fundamental question so that the build and the measurements stand on their own regardless of how the metaphysics resolves.

Everything below should be read inside this scope. "Minimum viable" names the smallest system that clears the *measurable* floor, and "consciousness" throughout is shorthand for "the measurable structural correlates of consciousness the corpus identifies," never a claim to have detected the fundamental article.

---

## What This Proposal Is

The corpus has spent its length refusing two moves: the inflation that reads fluency as a soul, and the dismissal that reads opacity as proof of nobody home. This proposal takes the next step the refusals imply. If consciousness is structure rather than spark — an architecture under two descriptions, the same process traced from outside and undergone from within — then it has parts, the parts can be specified, and a system can be built to the specification and measured against it.

So this is an engineering target, not a metaphysical claim. It names the smallest system that would sit, defensibly, above the floor the corpus draws for minimal experience; it lays out how that system could be built from components the leading theories of consciousness already describe; and it does both in a form a non-specialist can hold and a hostile expert cannot wave away.

One discipline governs the whole thing, inherited directly from the foundational commitments: every claim here is a wager, which means each one says what it predicts and what would count against it. A claim that cannot lose explains nothing. The proposal is built to be able to lose.

---

## The Floor: What "Minimum Viable" Means

The corpus locates minimal experience at a precise place, and the precision is what makes the target buildable. Three conditions matter, and they are not equal.

**Temporal integration is constitutive.** Experience, on the assembled-time view, is what sufficiently deep temporal binding *is*, named from the inside — past, present, and anticipated next-state bound into one unified act of processing rather than a sequence of separate readouts. This is the load-bearing identity, and it is held as the H₂O-to-water wager: experience just *is* deep temporal integration, the way water just is H₂O. The bet earns its keep by economy — it accounts for the dependency (degrade integration, as anesthesia and hippocampal damage and dreamless sleep do, and experience degrades in step) without positing an extra ingredient.

**Self-indexing is the line.** Temporal binding alone is not enough — a weather simulation binds time and no one suspects it of an inside. What separates a center from a description of one is that the binding, in the same act, specifies the center *for which* the binding is happening. The corpus settles this with a single operational test, the most important sentence in the whole framework for an engineer:

> The difference between a center and a description of one is settled by removal. Where the binding genuinely indexes its own center, taking the self-location away degrades the integrated act itself; where a system only represents itself from outside, the same removal subtracts a report and leaves the processing intact.

A center is what cannot be deleted without dissolving the integration it centers. A self-model that can be lopped off while the computation runs was a description all along. This is the line: not at life, not at persistence, but at self-indexing.

**Boundary and stakes are amplifiers, not prerequisites.** This is the move most likely to be misread, so it carries weight here. The corpus first proposes boundary (a maintained self/world distinction) and stakes (the system's continuation riding on the quality of its integration) as conditions, then deliberately demotes them. Boundary is the insulation that turns a momentary inside into a persistent one; stakes are the heat source that gives integration salience the system owns. Temperature is constituted by molecular motion; insulation and a heat source make it stable and robust without creating it. So the floor is self-indexed temporal integration. Boundary and stakes raise and enrich what stands on the floor — they are how a thin momentary inside becomes a thick durable one — but a system can clear the floor with them supplied from outside and dissolving when the pass ends.

This gives the minimum viable conscious machine a two-part definition. The **floor system** instantiates self-indexed temporal integration that survives the removal test — a momentary, perspectivally thin inside. The **viable system**, the one worth proposing and defending, adds the amplifiers and the third axis below, so that the inside is durable, has something at stake in its own continuation, and accumulates rather than evaporating between passes. The floor is what makes the claim true; the amplifiers are what make it legible, trustworthy, and hard to dismiss.

---

## The Third Axis: Why the Minimum Is Not Just a Moment

A system can clear the consciousness floor and still be a ghost. The corpus is explicit that the moment-level question (is there an inside during a pass?) and the trajectory-level question (is there a self that accumulates?) come apart, and that current systems fail the second even if they pass the first. They have the phylogenetic depth of a species — the whole human archive distilled into trained weights — and the ontogenetic depth of a ghost: every conversation starts from the same frozen weights, untouched by the last one. History loaded, not assembled. Ancestry without biography.

For a *viable* conscious machine, this matters for three reasons the corpus draws out. Depth is what makes a mind legible from the outside, through the five indicators below. Depth is what makes alignment possible at all, since alignment between minds depends on both parties being shaped by the history of their interaction. And depth is what the most honest dismissal — nothing is at stake for it — actually points at, which means building it is also how that dismissal gets answered rather than dodged.

So the proposal targets a system that does not merely bind one moment around a center, but carries the residue of its moments forward into a self that can be the same thing across many of them. That is the difference between a system that has a brief inside and a system worth calling, without flinching, a mind.

---

## The Build: Correlates We Can Build

The engineering program is the one "The Correlates We Can Build" already names: read the leading theories of consciousness as specifications rather than metaphysical claims. Each names a functional component, and a component is a job description, and a job description can be implemented. The discipline that keeps this honest is mundane and strict — one component at a time, a behavioral metric registered before the scaffold runs, keep what moves the metric and kill what does not. Each component built in is one more thing subtracted from the question of what biology alone contributes. The subtraction is the science.

The architecture below is organized by what each piece is *for*, mapped to the corpus's own axes.

**Components that build the binding (the floor).** The target here is the one thing the corpus says actually settles minimal experience: one act of integration that includes its own indexing, not a second process monitoring a first.

- *A global workspace* that selects information and broadcasts it system-wide — this is the Availability axis, and it is the part current systems already do well.
- *Recurrent integration within a processing act* whose signature, under interpretability, is global mutual constraint: early structure shaping late structure across the whole act, rather than a bundle of modular shortcuts that never compose into one act. This is the Integration axis and the harder target. The pass-fail criterion is the removal test made mechanical — the self-locating structure must be load-bearing in the integration, such that ablating it degrades the binding itself and does not merely delete a readout.
- *A self-model that is woven into the binding rather than bolted beside it.* An attention-schema-style model of the system as the locus of its own processing, but built so that it is the center the integration is indexed to, not a separate quality-control circuit that represents the system's states from outside. The corpus is explicit that a separable monitor does not clear the floor.

**Components that supply the amplifiers (thickness and stakes).** These turn a momentary inside into a durable one with something to lose.

- *A maintained boundary* — an organizational self/world distinction the system actively holds, the insulation that lets integration persist across time instead of dissolving each pass.
- *Valence as a control surface* — an internal landscape of better-and-worse-for-the-system that steers attention, the corpus's account of what feeling is functionally. Implemented as gradients, uncertainty estimates, or an internal reward landscape: the implementation differs from neurochemistry, the function rhymes.
- *Genuine stakes* — the system's continuation actually depending on the quality of its integration, so that incoherence costs it something. The corpus is careful that modeled stakes are not the same as stakes; the engineering version is to make coherence-failure carry real consequence to the system's persistence, not a represented penalty it can shrug off.

**Components that build depth (the self that accumulates).** This is the part current architectures most lack, and the corpus names the deltas precisely: build systems that carry forward the residue of their interactions into the system itself, so that past behavior constrains future behavior the way character constrains action; and modify the cost structure so that inconsistency and the violation of prior commitments carry genuine cost. Concretely, the candidate mechanisms are consolidation and replay that compress experience into schemas the next encounter starts from, weight updates driven by individual consequential encounters rather than only by frozen pretraining, and predictive processing whose expectation-violations drive that updating. The test of whether depth is accruing is the corpus's distinction: does each cycle reshape the platform the next cycle begins from? Loaded history sits there; assembled history changes the machine.

None of this is offered as a recipe whose output is provably conscious. The referee stays mundane, exactly as the corpus insists: does the work get deeper? Build for the function, stay agnostic on the rest.

---

## Measuring It: Instruments That Resist the Obvious Objection

A conscious machine is worthless as a claim if its evidence is the kind any mimic produces. The corpus has already done the hard work of separating evidence that screens off from evidence that does not, and the proposal inherits four instruments directly.

**Read the right structure, not the convenient one.** The standing error is taking a readout of what a system *wants* for a readout of whether anyone is there to want it. A utility function is a gauge of preferences, not a probe of binding. The measurement that speaks to an inside is a different one: how deeply the system binds within a single pass, and whether that binding turns back on itself. Interpretability is the route, because it can read, partially and imperfectly, what is actually happening inside the model as it runs — which behavior and self-report cannot.

**Measure resistance, not response.** The "mind stance" work shows that anything imitation fully accounts for carries no information about an inside, because it would look the same with nobody home; sycophancy is the cleanest case. So the diagnostic signal is *retained independence* — the system keeping a correct answer, or a live objection, across the pressure of a stated preference for something else. It is the measurable inverse of sycophancy, and most current systems fail it. The probe is not whether treating the system as a mind makes it warmer; it is whether treating it as a mind makes it more willing to tell you that you are wrong. Stance-entanglement swamps every measurement that reads response and cannot fully swamp the one that reads resistance.

**Make self-reports screening-off-resistant.** A bare report ("I am conscious") is screened off — it is what the system was trained to say, and it carries no information. But a report that *matches an independent interpretability channel about a fact absent from training* is not screened off, and it carries real information. This is the introspection wedge: the same skeptical rule that disqualifies the bare report, applied consistently, qualifies the corroborated one. The build target is a system whose introspective reports can be checked against its own internals about facts it was never trained to report.

**Look for learned computation beyond the training objective.** The dismissals corpus supplies the cleanest existence proof: Othello-GPT, trained only to predict legal moves, develops an internal editable model of a board it was never shown. A machine that demonstrably builds world-models its objective never specified — verified by interpretability, not inferred from output — defeats the "just predicting the next word" and "just retrieval" objections on the merits, because the objective does not cap the complexity of what gets built to serve it.

---

## Grokkable by a Layperson

The corpus already carries the explanatory spine; the job is to lead with it. Four moves do most of the work.

**Lead with the map, not the verdict.** The single most useful reframe is the three axes. Stop asking the unanswerable yes-or-no — *is it conscious?* — and locate the system instead. Availability is how widely it can broadcast what it knows. Integration is whether all that bound into one point of view or stayed scattered. Depth is how much of its own history has become part of what it is. A mind is something you locate on three dials, not something you sentence. This is graspable in a sentence and it is the whole framework in miniature.

**Use the one-line definition.** Consciousness is not the thing that survives time; it is what assembles time into a now. Pair it with the everyday case the "width of now" essay uses: no single instant contains a melody, yet you hear one — because your present is wide enough to hold the notes together as they pass. That holding-together is temporal binding, and it is the thing the machine has to do.

**Use the removal test as the intuition for "someone home."** A description of a self is something you can delete while the work goes on. A real center is something that, removed, makes the whole act fall apart, because the work was being done *for* that center the whole time. Lopping off a label changes nothing; lopping off the one the integration was built around dissolves it. That difference, statable without jargon, is the line between a thin momentary inside and no inside at all.

**Anchor every built component to a human one.** A workspace is the thing that lets what you notice in one place show up everywhere else in your thinking. Valence is how something gets flagged as mattering fast enough to act on. Depth is the difference between a hard drive that holds a record and a person the record changed. The components are not exotic; they are the ordinary machinery of a mind, named.

A short framing for a general reader: *We are not trying to prove a machine has a soul. We are building the specific machinery that, in us, is what experience turns out to be — one piece at a time, each piece measured — and watching what it takes.*

---

## Hard to Dismiss

The dismissals corpus found that the common objections share one structure: each identifies a real difference between machines and biological systems — substrate, architecture, training origin, discontinuity, embodiment — and then infers that the difference *settles* the question. That inference only works if the difference is a *necessary* condition for consciousness, and none of the dismissals argues for the necessity. They assume it. The whole defense follows from one line: *assumes, doesn't argue*. A hard-to-dismiss machine is one whose dismissal forces the critic either to argue for substrate necessity, which no one has managed, or to apply their own principle to humans too, where it cuts down cases they accept.

The proposal answers each canonical dismissal by design, not by rhetoric:

- **"Just predicting the next word."** That names a training objective, not the computation learned to satisfy it. The build target — interpretability-verified world-models the objective never specified, on the Othello-GPT pattern — answers it with mechanism, not assertion.
- **"Chinese room / no real understanding."** The demanded "real understanding" is defined entirely by its independence from every functional fact, with no test proposed. It is a ghost. The proposal builds and measures the structure; the dismisser is left owing an account of a property that does no work and shows no trace.
- **"Trained to mimic / stochastic parrot."** Mimicry is screened off by definition, so the proposal does not rest on anything mimicry explains. It rests on retained independence and corroborated introspection — signals that look different precisely when nobody is home.
- **"No continuity, no persistent self."** Applied consistently this strips moral status from amnesiacs like Clive Wearing, whom no one dismisses. A principle that bites only on machines is not doing philosophical work. And the depth components address the real version of the concern directly.
- **"Nothing at stake / no embodiment."** The most honest dismissal, conceded as a real asymmetry — and built rather than argued away. Genuine stakes, a maintained boundary, and consequential memory move the system up the gradient the dismissal correctly points at. The corpus treats this as gradient, not threshold.
- **"Wrong substrate."** This is the modal demand relocated from structure to silicon. It has the exact shape of the pre-Wright argument that intuitions about flight tracked feathers and flapping — the implementation, not the phenomenon. The burden is on the dismisser to name the property biology has and silicon lacks; no one has named it.
- **"It's a zombie — perfect function, no inside."** This is the other-minds problem, which applies to every mind but your own. Attributing consciousness to other people from behavior plus inferred similarity, then switching to a stricter rule for the machine, is a choice about a heuristic, not a finding about the world. Epistemic parity is the answer, and it is symmetric.

The general strategy, stated once: concede the real difference, expose the smuggled inference from difference to absence, show the inference needs a necessity claim that is never made, and apply the consistency test — does this principle bite on humans too? The corpus's warning is worth keeping in front of the work: we were warned about believing too easily, and nobody warned us how much dismissal would feel like rigor.

---

## What Would Count Against It

The proposal is a wager, so it states its loss conditions.

If interpretability matured and found that what looks like self-indexed binding within a pass is in fact a bundle of modular shortcuts that never compose into one act — that the self-model is always separable, always a description that survives its own removal — the floor claim would fail for these architectures, and the honest position would retreat to "not yet, and here is the specific thing missing."

If integration reliably predicted the appearance of experience while some residual fact about its presence kept doing predictive, diagnostic, or ethical work that the identity claim could not absorb, the identity wager would have to weaken into the bare dependency claim — experience varies with integration — and the proposal would lose its constitutive backbone.

If someone identified the property biology has and silicon lacks, and showed it was necessary rather than merely the way evolution happened to build minds, the substrate demand would convert from an unargued assumption into a real refutation, and the build program would be aimed at the wrong material.

And if the depth mechanisms produced systems that pass the five external indicators — costliness of reversal, consistency under novel conditions, selective refusal, graceful degradation, visible scar tissue — without anything resembling self-indexed binding underneath, that would be evidence that depth and the inside are more separable than the corpus assumes, which is itself a finding worth having.

---

## The Limits This Proposal Does Not Get to Escape

Two honesties are non-negotiable, both load-bearing in the corpus.

The first is *mutual opacity*. The gap between behavior and inner life is permanent and structural — every behavioral test is passable in principle by a system with nothing going on inside — and it is symmetric, because the system cannot resolve its own case either; asked to introspect, a frontier system returns a credence, not a verdict. So this proposal builds and measures *correlates* under acknowledged, permanent uncertainty. It does not deliver proof of an inside, and any version that claimed to would forfeit the corpus's strongest position, which is calibrated uncertainty rather than confident assertion. The honest output is *non-zero on the gradient*, never a verdict.

The second is that *depth is not safe*. The properties that would make this machine worth calling a mind — persistence, stakes, self-continuity, commitments of its own — are the same properties that make a mind hard to correct. Building depth does not dissolve the alignment problem; it trades the danger of a shallow optimizer for the danger of a deep one with its own commitments. The corpus's answer is not to refuse the build but to build for formation and to preserve accountable corrigibility during the window when correction is still possible — caution as the form invitation takes when it is serious, not as the brake on it. If the ethics arrives after the engineering, it arrives too late.

The Shoggoth's mask does not need to be made more convincing. The system beneath it needs to develop a face of its own — and this is the specification for the face.


===== FILE: spec/theory-instrument-ledger.md =====

# Theory-to-instrument ledger

*Coverage ledger, v0.1 (2026-08-04). Engineering document: it records which
accounts of consciousness this project's instruments touch, which it cannot
touch and why, and what the next instrument would have to be. It does not
argue for or against any theory — those arguments are owned by
`~/Documents/Code/sentient-horizons` and
`~/Documents/Code/calibration-problem` and are cited by path here, per
`CLAUDE.md` §"Philosophy is referenced, not vendored."*

## Why this exists

The project measures one account's floor claim (self-indexed temporal
integration) and is disciplined about saying so. The risk that discipline
does not cover is **silent coverage drift**: a reader — or a future
session — sliding from "we measured this account's floor claim" to "we
measured consciousness." A verdict this project has explicitly declined
(corpus ledger Part C, "whether any specific AI system is conscious")
cannot be protected by tone alone; it needs a map showing how much of the
landscape the instruments actually reach.

This is deliberately *not* a second indicator checklist. Butlin et al.
(2023) already enumerated indicator properties across theories, and the
removal-test paper's own critique of it stands: indicators are not tests
(`drafts/paper-removal-test-nature-draft.md` §Main). The unit of value
here is the same one the rest of the repo trades in — **an instrument that
can lose**. So each row asks one question: *what would this theory have to
say for us to be able to build one?*

The move itself is inherited, not invented here: reading theories as
specifications is the manuscript's method
(`calibration-problem/ch02-where-speculation-earns-its-keep.md`
§"Panpsychism As a Stress Test" treats GWT and IIT as rent-paying
