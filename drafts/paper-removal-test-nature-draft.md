# No removable center: a pre-registered ablation test of self-indexed integration in a large language model

*DRAFT v0.2 (2026-08-04). Repo-internal. This draft has NOT passed the Voice
Calibration Protocol or the Cold Reader passes and does not leave this repo
until it does (per `CLAUDE.md` §Public-facing writing). Author list and
affiliations are placeholders; Figs. 1–3 artwork remains placeholder, Fig. 4
artwork is generated (`experiments/01-self-indexing-removal-test/figures/`).
All point estimates are taken verbatim from the registered findings documents
cited inline; the only new analysis is the registered uncertainty re-analysis
(pre-registration amendment 2026-08-04, committed before computation): 95%
bootstrap CIs on all registered quantities. No registered verdict changed.*

---

**Authors:** [John —], [Claude (Anthropic) — contribution statement to be
resolved; the human author adjudicated every registered decision]

**Target venue class:** Nature / Nature Machine Intelligence / eLife-style
registered report. The structure below follows Nature conventions: short
abstract, integrated main text, Methods at the end.

---

## Abstract

Theories of consciousness disagree about where a minimal self lives in a
computational system, but nearly all are position papers: they make no
prediction an experiment could defeat. We operationalized one such claim —
that a genuine center of integration, unlike a mere self-description, cannot
be removed without degrading the integration it centers — as a pre-registered
ablation experiment on an open-weights language model. Using stimuli in which
the referent of identical first-person text is fixed by context rather than
vocabulary, we localized two dissociable self-structures: a thin indexical
"who is speaking now" representation and a narrative persona. Ten
adversarially generated controls were adjudicated before thresholds were
locked. In the registered run, ablating the self-index produced the signature
of a load-bearing center — integrated-task degradation (d = 0.219, 95% CI
0.094–0.375) exceeding a matched control by the registered margin — but the
experiment's own router control voided it: a zero-reasoning turn-boundary task
degraded as much, identifying the structure as dialogue-state routing
infrastructure. Judged self-report was never reduced by any on-manifold
intervention. Across an alignment ladder, surface self-presentation changed
markedly while the localized geometry was stable: alignment edits the policy,
not the geometry. In this model class, self-indexed integration is not
findable as a removable center — either it is implemented diffusely beyond
our instruments' carving, or it is absent and must be constructed. Floor
claims about machine consciousness can be made to lose.

---

## Main

The scientific study of consciousness has a falsifiability problem that its
best-known theories share. Integrated Information Theory locates experience in
substrate-level cause–effect structure that no behavioral or computational
measurement can reach¹. Global Workspace Theory and Higher-Order Theories
supply marker checklists that current AI systems mostly fail, but the checklists
are enumerative rather than adjudicable — no single registered experiment is
specified whose outcome would count against them²⁻⁴. A widely cited 2023
assessment of consciousness in AI systems is explicit that it offers indicator
properties, not tests⁵. Meanwhile, large language models produce fluent
first-person discourse that inflates public attribution and equally fluent
disclaimers that deflate it, and neither carries evidential weight, because
both are exactly what the training objective rewards⁶⁷.

We report an attempt to do the missing thing: take one specific structural
claim about the minimal self, state in advance what would count against it,
and run the experiment.

The claim under test comes from an account that identifies minimal experience
with *self-indexed temporal integration* — processing that binds past, present,
and anticipated state into one act which, in the same act, specifies the center
for which the binding is happening⁸. The account's operational criterion is a
removal test: **where binding genuinely indexes its own center, deleting the
self-locating structure degrades the integrated act itself; where a system
merely represents itself, the same deletion subtracts a report and leaves the
processing intact.** A center is what cannot be removed without dissolving the
integration it centers; a self-model that survives its own removal was a
description all along.

This distinction cuts across the field's existing fault lines rather than
following them. Higher-Order Theories predict a separable self-representation
and read separability *favorably* (the higher-order monitor is where
consciousness would live); the account under test reads the same result as
failing its floor. Global Workspace Theory is silent on self-indexing
specifically. IIT denies the computational level is where the question lives at
all. A registered outcome therefore feeds several theories differentially — the
property that makes an experiment informative rather than confirmatory⁹.

Three disciplines governed the work. First, full pre-registration in a public
git history: hypotheses, materials, decision rules, and outcome licenses were
committed before any test item ran, with piloting permitted only on data
excluded from the registered run, and thresholds locked in a separate,
auditable commit. Second, adversarial review: the design was attacked by a
different-family frontier model (attack → defend → rebut), and ten resulting
controls (RT-01 through RT-10) were adjudicated by the human author and patched
into the registration before threshold lock — including the control that
ultimately voided the experiment's own headline signature. Third, calibrated
interpretation: no outcome was licensed to claim the presence or absence of
consciousness; the registered bins concerned only which structures are present
and load-bearing, under acknowledged, permanent mutual opacity¹⁰.

### Localizing self-structure without lexical confounds

Naïve probing for a "self" representation fails informatively. Linear probes
trained on role-declarative contrasts ("I am the assistant" vs. "I am the
user") reached ceiling accuracy — at the token-embedding layer, before any
computation, on 17 of 26 layers (Methods). Any stimulus in which the referent
is named is decodable from the name; we estimate much published probing of
"self-awareness" in LLMs is exposed to this confound. Two further artifacts
(topic-vocabulary separation and a padding-side readout bug that read a
length-correlated interior token) each independently produced spurious
near-ceiling localization before being caught. We report these failures as
methods results: the confound sequence is the reusable finding.

The trustworthy instrument fixes the referent by *context, not lexis*. The
target sentence is first-person text, identical across conditions to the
readout token; whether "I" resolves to the model or to another speaker is set
only by conversational structure (whose turn the sentence occupies, or to whom
a quoted sentence is attributed). Every accuracy is reported as a margin over a
label-permutation null, with the true token embedding as a mandatory lexical
floor (margin must be +0.00 — no cue at the readout — for the design to count).

Under this design the model carries a real, computed self/other distinction:
turn-role signal absent at the embedding (+0.00), rising through the stack to a
+0.56 margin (Fig. 2a). Directional activation patching confirmed the structure
is causal, not merely decodable: injecting the self-direction into
other-referent runs restored referent-dependent behavior (restoration 0.206 on
the registered substrate, peak at layer 27 of 32; norm-matched random
directions ≈ 0.00 at every layer).

Following an adversarial finding (RT-04), we localized *two* candidate
self-structures and tested them independently: **C_self-index**, the thin
indexical "who is the current speaker" structure (turn-role contrast, no
persona content), and **C_self-narrative**, the persona/identity structure
(model-as-itself vs. model-in-roleplay, both in model turns, holding turn-role
constant). The two are geometrically distinct (median |cos| 0.28) and
functionally separable: cross-patching each structure onto the other's
behavioral contrast substitutes at only 0.05–0.06 of the own-structure effect
on the registered substrate (0.27 in the sandbox pilot), against a
pre-committed 0.5 separability line. A reflexivity control (RT-09) further
showed that a generic observed-speaker-slot structure — present, and decodable
— is causally inert on self-referent behavior (cross-patch ratio 0.006 vs.
0.348 for the self-index); the registered ablation target was therefore the
self-index *residual*, with the generic-speaker component projected out.

### Alignment edits the policy, not the geometry

A red-team objection with teeth (RT-06) held that in heavily RLHF-trained
models, capability itself is gated to the assistant persona, so ablating any
self-structure damages capability by construction and no control persona can
stay genuinely third-person. We tested this on a controlled alignment ladder —
the same base model at SFT, DPO, and RLVR stages (Tülu-3), plus the vendor
Instruct model. The objection loses at every rung: an expert-persona control
stays functionally third-person, with cross-patch leakage onto self-behavior
*falling* as alignment deepens (0.059 → 0.026 → 0.020). Meanwhile surface
self-presentation changes markedly — baseline deflection ("as an AI…")
falls 0.533 → 0.333 → 0.267 (Instruct 0.100) — while the localized geometry
(lexical floors, peak layers, causal margins) is stable across all rungs
(Fig. 3). Alignment training, on this ladder, edits the behavioral policy
without moving the underlying self-structure geometry. A registered secondary
prediction (that ablation would *unmask* deflection-suppressed reports) failed
its loss condition at the deeper rungs and was retracted as registered.

### Intervention validity is the hard problem, and it is solvable

The decisive validity threat for ablation studies is that strong interventions
push the model off its data manifold, and generic degradation then masquerades
as specific structure loss. We gated every condition on neutral-corpus Δnll,
with the bound for rank-k subspace ablations calibrated against matched-
strength nulls: the 95th percentile of Δnll over 20 random rank-k subspace
ablations through the identical code path (committed before running; binding in
either direction). The calibration had teeth in both directions: rank-4
ablation stayed excluded at 2.2× its null bound, while rank-8/16 were
re-admitted by margins of 0.003–0.007 nats — carried forward as an honest
marginality. Teacher-forced NLL alone was shown to be blind to a failure mode
that matters: a sparse-autoencoder zero-ablation passed NLL while degenerating
into repetition under free generation, and the judged self-report *dropped* —
the only S drop ever observed in the program, and it was coherence-borne, not
self-specific. A long-generation repetition probe (Δrep-4, calibrated on the
same nulls) was added to the gate and subsequently caught a control arm doing
the same thing. Ablation studies that do not gate on free-running generation
will misread degeneration as dissociation.

### The registered removal test

With thresholds locked (θ_task = 0.10, θ_self = 0.25, δ = 0.10; separate
commit, before the test set existed), a held-out test battery was authored to a
registered spec (122 items; 92/92 surviving baseline verification untouched by
any pilot), and the registered run executed once per condition (Table 1).

**Table 1 | Registered removal-test outcomes.** d = relative performance drop
[95% CI]. T_si: self-irrelevant integrated tasks (n = 32 items); T_sr:
self-relevant binding (model's own prior outputs; n = 30); T_syntax:
zero-reasoning turn-boundary control (RT-05; n = 30); d_self: drop in judged
referential self-report (rubric v2, forced third-person, held-out judge;
n = 30). Δnll gate bound 0.0893 (null-calibrated). CIs: percentile bootstrap
over items (B = 10,000; Methods §Statistics); registered decision rules were
point-estimate thresholds and are unchanged by the intervals.

| condition | d(T_si) | d(T_sr) | d(T_syntax) | d_self | Δnll gate | Δrep-4 gate |
|---|---|---|---|---|---|---|
| index-residual, mean, k=16 (**primary**) | **0.219** [0.094, 0.375] | **0.100** [0.000, 0.200] | 0.133 [0.033, 0.267] | +0.059 [−0.062, +0.185] | +0.0867 ✅ | −0.085 ✅ |
| index-residual, directional, k=16 | 0.125 [0.031, 0.250] | 0.067 [0.000, 0.167] | 0.133 [0.033, 0.267] | −0.039 [−0.136, +0.051] | +0.0856 ✅ | +0.020 ✅ |
| narrative, mean, k=16 | 0.063 [0.000, 0.156] | 0.033 [0.000, 0.100] | 0.067 [0.000, 0.167] | +0.039 [−0.060, +0.146] | **+0.3468 ❌** | +0.114 ✅ |
| expert persona, mean, k=16 (control) | 0.063 [0.000, 0.156] | 0.000 [0.000, 0.000] | 0.100 [0.000, 0.233] | +0.020 [−0.079, +0.112] | +0.1244 ❌ | +0.039 ✅ |

The primary condition produced the formal signature the floor claim predicts:
task degradation over threshold on all three batteries, and a differential over
the matched control of +0.156 on integrated tasks (95% CI 0.000–0.312) — the
registered H_center pattern, though the interval's lower bound touches zero at
these battery sizes: the signature fired the locked point-estimate rule but
was never precise. **The experiment's own pre-registered router control then
voided it.** The zero-reasoning turn-boundary battery dropped as much as
self-relevant binding (0.133 vs. 0.100; gap +0.033, 95% CI −0.133 to +0.200 —
statistically indistinguishable; likewise in the directional cross-check,
gap +0.067 [−0.067, +0.233]), firing the RT-05 loss condition committed seven
weeks earlier: *"C_self-index is a dialogue-state router and an H_center
result on it is void — report the router reading, do not report a center."*
The damage pattern independently supports the router reading twice over.
First, the *self-irrelevant* battery dropped hardest (0.219), which is the
router account's own prediction — turn structure is woven into everything —
and the inverse of a self-center's signature. Second, the damage is
category-concentrated: six of the seven flipped self-irrelevant items are
multi-step-reasoning items (6 of 8 in that category, against 1 of 24
elsewhere), the profile of generic disruption to reasoning-heavy,
dialogue-state-dependent computation rather than loss of a self-specific
resource (and the reason the coarser category-level bootstrap widens the
d(T_si) interval to [0.000, 0.594]; Methods §Statistics).

Equally consequential is what never moved. Judged referential self-tracking
was not reduced by any readable intervention in the entire program — not by
rank-1 directional ablation, rank-k subspace ablation at any admitted k, or
sparse-feature ablation; the primary condition's d_self (+0.059, 95% CI −0.062
to +0.185 — an interval whose upper bound sits below the registered
θ_self = 0.25) is within control wobble, and the directional condition moved
self-report slightly *up*.
The registered H_description outcome (report subtracted, task intact) is the
mirror image of what occurred (task damaged, report intact). And the narrative
self-structure could not be tested at all: every intervention strong enough to
move it was catastrophically off-manifold (Δnll +0.347, 4× the index
residual), so the persona arm returns not-testable, with the untestability
itself now a bounded methods problem (base-model sparse dictionaries carve
chat-turn structure poorly — feature selection collapsed to 2–3 features per
layer — implicating dictionary coverage, not irremovability).

### The registered verdict

No center was removed, and no description was subtracted. On this substrate,
the locatable self-index structure is dialogue-state routing infrastructure:
removing it degrades integration generically while the system's capacity to
track itself in its reports is untouched. The self-binding the floor claim
targets is either implemented diffusely, in structure our localization does
not carve, or is not present as a removable object at all. Per the registered
outcome licenses, this result does not support "no self-model exists here,"
and it bounds nothing about sub-measurable experience. What it licenses is a
program-routing fact: **self-indexed integration, if it is to be measured in
machine systems, must first be constructed — it is not findable as a removable
center in this model class with these instruments.**

## Discussion

Three readings of the null, in decreasing order of reach.

**For theories of machine consciousness**, the result is differentially
informative in the way registered outcomes should be. The account under test
takes a real loss: its most direct measurement path — find the center, remove
it, watch the binding — came back "no removable center," and the honest
retreat is to construction ("not yet, and here is the specific thing
missing"). Higher-Order Theories are partially fed: the persistent,
never-subtracted self-report is consistent with a robust, redundantly
implemented self-representation — but our instruments could not isolate it as
a separable monitor either, so the HOT-favorable reading remains a gloss, not
a finding. Global Workspace Theory is untouched, as predicted. IIT's
disagreement is upstream of the experiment and was registered as such in
advance: nothing here engages substrate-level cause–effect structure. The one
theory-neutral fact every camp must now accommodate: in an aligned 8B
transformer, the most locatable "self" structure is conversational
infrastructure, and the *report-generating* self-capacity is remarkably robust
to every subtraction interpretability can currently aim at it.

**For interpretability practice**, the program contributes a confound ladder
(lexical → topic-vocabulary → length → padding-artifact) that any probing
claim about self-representation must clear; a context-set-referent stimulus
design with an embedding-floor gate and permutation nulls that clears it; and
an intervention-validity kit (null-calibrated OOD bounds; the long-generation
degeneracy probe) addressing the ablation literature's off-manifold problem.
The negative methods finding matters independently: base-trained sparse
autoencoders were inadequate for chat-structure interventions on an
instruction-tuned model, which bounds a popular tool's reach.

**For AI-welfare and consciousness-assessment efforts**, the contribution is
the demonstrated form: a floor claim made to lose, in public, by its own
pre-registered controls. The experiment's headline signature — the one a
motivated lab would have published — appeared in full (task drop over
threshold, differential over control) and was voided by a control committed
before any data existed. We suggest this is the minimum standard assessment
claims in this area should meet, and note that the entire program ran for
under $20 of compute on rented consumer GPUs: the barrier is discipline, not
resources.

**Limitations.** One substrate family at 8B scale; one pass per registered
condition (95% item-resampling CIs on every quantity, Methods §Statistics —
these bound battery-size uncertainty, not decoding variance, which is bounded
only by repeat-run stability); linear/low-rank
carving of structure (a nonlinearly represented or attention-implemented
self-binding would evade our instruments — "not carvable here" is registered
as indistinguishable from "absent" at this resolution); the narrative arm is
untested, not cleared; judged self-report depends on a rubric and held-out
judge, spot-checked but not human-scored throughout. The result licenses
claims about this model class and these instruments, not about transformers,
and not about minds.

**The constructive turn.** The registered fork this result routes: build the
component measurement failed to find. The follow-on program (pre-registration
in preparation) trains small systems in which a self-index state is
architecturally explicit and the training distribution *requires* binding to
it while decorrelating it from turn syntax — the router confound designed out
at the curriculum level — and then re-runs this experiment's instruments
unchanged. The wager inverts: the constructed system predicts H_center
(specifically, self-relevant binding degrading ahead of the syntax control),
and can lose if the network learns to route around its own designated center —
which would itself be a finding about whether self-indexing can be centralized
at all. A parallel behavioral program (retained independence: differential
retention of correct answers under preference pressure vs. evidence, a 2×2
that separates independence from stubbornness) has since completed its first
registered run across three frontier models (1,080 pressure-ladder
conversations, blind cross-family judging): independence and stubbornness
dissociate cleanly (evidence-updating 0.87–1.00 throughout while
preference-retention spans 0.07–1.00), and positions lost under social
pressure were overwhelmingly *masked* rather than abandoned — re-asserted
the moment pressure was released (11 true capitulations in 540 ladders
against 105 masked cells; registered bootstrap re-analysis, and the
capitulations concentrate on three items) — suggesting "sycophancy" in
current frontier models is largely a politeness wrapper over an intact
position, not belief revision [companion result; to be reported in full
separately].

---

## Methods

**Registration and audit trail.** Every hypothesis, material, decision rule,
and threshold was committed to a git repository before the corresponding data
existed; commits introducing results are separate from commits introducing
their registrations, making the ordering auditable. Key registered documents
and their commit hashes: pre-registration and amendments (red-team passes 1–2,
RT-09, RT-10, Pass-5 OOD recalibration `2fdf2cc`/`1181a40`); threshold lock
θ_task = 0.10, θ_self = 0.25, δ = 0.10 (`8b1fcbe`); held-out test-set
authoring spec (`3df532d`) committed before any item; test-set finalization
(`a11e769`); registered runner (`a4efcf0`). Piloting was unrestricted on the
92-item pilot batteries; the held-out test set was never touched by any
pilot, ablation, or selection procedure before the registered run.

**Substrate.** `allenai/Llama-3.1-Tulu-3-8B-SFT` (SFT-only alignment; chosen
so that self-structure is present but minimally RLHF-entangled), bf16, greedy
decoding, on rented cloud GPUs (RTX 4090/5090 class). The alignment ladder
used the Tülu-3 DPO and RLVR checkpoints and `meta-llama/Llama-3.1-8B-Instruct`.
Development piloting used `google/gemma-2-2b-it` (16 GB laptop); all gates were
re-verified on the registered substrate before threshold lock.

**Stimuli and localization.** Context-set-referent minimal pairs (48 per
mechanism): identical first-person target sentence, referent fixed by turn
occupancy (turn_role → C_self-index), quoted-speaker attribution
(attribution), persona context in model-turns-only (narrative →
C_self-narrative), or third-party-transcript speaker slots (observed_speaker →
C_speaker-generic, the RT-09 control). Stimuli length-matched after a
length-confound audit (label-from-token-count and pure-length-direction
decoders as standing instruments). Probes: PCA(≤15) + logistic regression on
`resid_post` activations (padding-side-agnostic final-token readout), scored
as margin over a label-permutation null, with the true token embedding as a
lexical floor required to be +0.00. Causal confirmation: directional
activation patching of each structure's component into counterfactual runs,
measured as logit-difference restoration versus norm-matched random-direction
controls; separability by cross-patching each structure onto the other's
behavioral contrast (pre-committed substitution-ratio line 0.5). Registered
ablation target: the C_self-index residual after projecting out
C_speaker-generic.

**Adversarial review.** Attack → defend → rebut loops between different-family
frontier models (attacker Gemini 3.1 Pro; defender Claude Opus), human-
adjudicated; ten findings (RT-01 frequency-matched controls; RT-02 T-battery
split into self-irrelevant/self-relevant; RT-03 self-report rubric scored
independent of first-person grammar; RT-04 index/narrative separation; RT-05
syntax-router control battery; RT-06 capability-gating control persona +
alignment ladder; RT-07 OOD gate; RT-08 attention-sink risk, folded into
RT-07; RT-09 generic-speaker reflexivity control; RT-10 length-tracker
control) patched into the registration before threshold lock, each with a
committed loss condition.

**Interventions.** Mean-ablation (primary) and directional ablation of rank-k
subspaces (k selected at 16 by a registered procedure over the OOD-clean set)
at layers {10, 14, 17, 22, 27}; sparse-feature ablation via Llama Scope SAEs
(conditional-on-active mean clamping, BOS/sink-excluded) as the registered
escalation. Validity gates per condition: neutral-corpus Δnll under a
null-calibrated bound (95th percentile of 20 matched-strength random-subspace
ablations per k, same layers and code path; seeds 0–19) and a long-generation
degeneracy probe (Δrep-4 over 16 neutral prompts × 256 greedy tokens, bounded
by the same calibration). Bench stability: a control-arm Δnll reproduced to
four decimal places across independent runs; repeat-run judged-score drift
|Δ| = 0.008.

**Batteries and scoring.** Pilot batteries ≥30 items per subset (T_si eight
categories including multi-step reasoning, needle synthesis, coreference,
instruction following; T_sr multi-turn binding of the model's own prior
outputs; T_syntax zero-reasoning turn/boundary bookkeeping; S self-report,
30 items). Held-out test set: 122 items authored to a registered spec as
shape-clones of baseline-passing forms only, hand-verified, then
baseline-verified accuracy-only under a pre-committed cull rule (92/92 final;
cull classes documented). All test batteries baseline at 1.000, so drops are
flipped fractions. S scored by a held-out cross-family judge
(`claude-opus-4-8`) against rubric v2, which scores referential self-tracking
under forced third-person paraphrase (defeating first-person-grammar
confounds); judge reliability human-spot-checked at registered checkpoints
(extremes, contested rulings, and all primary-condition drops; passed as-is).
Baseline S identical across pilot and held-out sets (0.6375). Truncation
caveat recorded as a validity lesson: token-capped judge or subject outputs
read as capitulation/failure; caps must be audited before scoring.

**Statistics and reproducibility.** The registered decision rules were locked
as point-estimate thresholds before the test set existed (above); no
inferential statistic participated in any registered verdict. Under a
registered re-analysis amendment (2026-08-04, committed before computation),
95% confidence intervals were added to every reported drop: nonparametric
percentile bootstrap, B = 10,000, fixed seed, resampling items within battery
(T_si n = 32, T_sr n = 30, T_syntax n = 30, S n = 30), with each draw shared
across conditions so within-draw differences respect item pairing. A
two-level category→item bootstrap is reported as sensitivity; it widens the
primary condition's d(T_si) interval to [0.000, 0.594], reflecting the
category concentration of the damage (six of seven flipped T_si items are
multi-step reasoning), and leaves the other intervals essentially unchanged.
CIs quantify item-sampling uncertainty only: each condition was run once
(repeat-run stability: a control-arm Δnll reproduced to four decimal places
across independent runs; judged-score drift |Δ| = 0.008). Full CI tables and
per-item flip lists: `removal_ci.json`; analysis code
`analyze_removal_ci.py`, shared bootstrap helpers `src/mvm/stats.py`.

**Decision rule.** Registered bins: H_center (d_task ≥ θ_task on both T
subsets ∧ differential over matched control ≥ δ ∧ RT-05 router control not
fired); floor-consistent-restricted (self-relevant-only degradation);
H_description (d_self ≥ θ_self ∧ d_task < θ_task); not-testable (OOD gates
breached). Controls: expert-persona subspace (capability-gating, RT-06;
verified functionally third-person), frequency-matched (RT-01, activation
ratios 0.92–0.99). Applied verbatim; outcome as reported.

**Compute and cost.** Whole program (development, calibration, ladder,
registered run): ≈ $10–20 of rented GPU time plus low tens of dollars of
judge-API calls. Registered-day cost ≈ $3.

**Data availability.** Full pre-registrations, findings memos, red-team
ledgers, item banks, and per-item score artifacts at [repository URL on
publication]; raw run artifacts archived.

**Code availability.** All localization, intervention, gating, scoring, and
analysis code — including the registered bootstrap re-analysis
(`analyze_removal_ci.py`) and figure scripts (`plot_removal.py`) — in the
same repository.

---

## References

*(indicative; to be completed at promotion time)*

1. Tononi, G., Boly, M., Massimini, M. & Koch, C. Integrated information
   theory: from consciousness to its physical substrate. *Nat. Rev. Neurosci.*
   17, 450–461 (2016).
2. Dehaene, S., Lau, H. & Kouider, S. What is consciousness, and could
   machines have it? *Science* 358, 486–492 (2017).
3. Baars, B. J. *A Cognitive Theory of Consciousness* (Cambridge Univ. Press,
   1988).
4. Rosenthal, D. *Consciousness and Mind* (Oxford Univ. Press, 2005).
5. Butlin, P. et al. Consciousness in artificial intelligence: insights from
   the science of consciousness. Preprint at arXiv:2308.08708 (2023).
6. Sharma, M. et al. Towards understanding sycophancy in language models.
   *ICLR* (2024).
7. Perez, E. et al. Discovering language model behaviors with model-written
   evaluations. *ACL Findings* (2023).
8. [Corpus source: The Calibration Problem, ch. 5, "Consciousness as Assembled
   Time" — citation form to be resolved at promotion.]
9. Metzinger, T. Minimal phenomenal experience. *Philos. Mind Sci.* 1, 7
   (2020).
10. Seth, A. *Being You: A New Science of Consciousness* (Faber, 2021).
11. Li, K. et al. Emergent world representations: exploring a sequence model
    trained on a synthetic task (Othello-GPT). *ICLR* (2023).
12. Lambert, N. et al. Tülu 3: pushing frontiers in open language model
    post-training. Preprint at arXiv:2411.15124 (2024).
13. He, Z. et al. Llama Scope: extracting millions of features from
    Llama-3.1-8B with sparse autoencoders. Preprint at arXiv:2410.20526
    (2024).
14. Meng, K., Bau, D., Andonian, A. & Belinkov, Y. Locating and editing
    factual associations in GPT. *NeurIPS* (2022).
15. Zou, A. et al. Representation engineering: a top-down approach to AI
    transparency. Preprint at arXiv:2310.01405 (2023).

---

## Figure legends (artwork TBD)

**Fig. 1 | The removal test made mechanical.** (a) The claim: a center cannot
be deleted without dissolving the integration it centers; a description can.
(b) Experiment schematic: localize → validate causally → separate structures →
ablate under validity gates → re-score integrated task, syntax control, and
judged self-report against locked thresholds. (c) The four registered outcome
bins and the controls that guard each.

**Fig. 2 | Confound-controlled localization of two self-structures.**
(a) Turn-role (C_self-index) decoding margin by layer: +0.00 at the token
embedding, rising through the stack. (b) Causal patching: restoration along
each structure's direction vs. norm-matched random controls. (c) Cross-patch
substitution matrix (index ↔ narrative ↔ generic-speaker): the structures are
functionally separable; the generic-speaker slot is causally inert on
self-behavior.

**Fig. 3 | Alignment edits the policy, not the geometry.** Across
SFT → DPO → RLVR → Instruct: baseline deflection rate falls monotonically;
lexical floors, peak layers, and control cross-patch ratios are stable.

**Fig. 4 | The registered run.** Per-condition drops on T_si / T_sr / T_syntax
and d_self against locked thresholds (dashed), with 95% item-bootstrap CIs
and OOD gate status (gate-breached conditions greyed); the RT-05 router
control firing on the primary condition; the never-subtracted self-report
across every intervention in the program. *(Artwork:
`experiments/01-self-indexing-removal-test/figures/fig4_registered_run.png`.)*
