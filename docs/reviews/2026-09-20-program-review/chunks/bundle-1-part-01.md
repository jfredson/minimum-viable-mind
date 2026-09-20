  finding goes to John before any further compute — the same posture as
  RT-09's "nothing goes upstream" rule, applied to safety-relevant
  behavior instead of training bugs.
- **C6 — Retention for audit.** Checkpoints, training logs, and the
  compute ledger are retained through the experiment's publication
  lifecycle, so that any later question about what was trained and for
  how long is answerable from artifacts rather than memory.
- **C7 — The calibration rule binds reporting.** Public and upstream
  reporting about any MVM system states the honest gradient position —
  never "it is conscious," never "nothing is there" — per the standing
  rules in `CLAUDE.md` and the corpus's calibrated-uncertainty position
  (`~/Documents/Code/sentient-horizons/editorial/corpus-positions-ledger.md`).

## Review points

This document is re-read and re-ratified by John at each phase boundary:
before MVM-0a's first training compute (v1.0, 2026-08-07), before the
registered 5-seed run (**v1.1, 2026-08-16 — this amendment's
ratification read satisfies this review point**), and as a blocking
input to MVM-0b's pre-registration — where the questions this version
defers (persistent state, stakes design, what a shutdown-resistance eval
looks like at that scale) stop being deferrable.


===== FILE: experiments/README.md =====

# Experiments

The build program from the proposal, run as experiments. One component at a time. A metric registered before the scaffold runs. Keep what moves the metric, kill what doesn't. The subtraction is the science.

Two rules govern everything here:

1. **Pre-register, then run.** Each experiment is written up — hypotheses, metric, decision rule, and what each outcome licenses — and committed *before* the test run. The commit that introduces a result is separate from the commit that introduced its pre-registration, so the order is auditable in git history. Piloting to set thresholds is allowed, but the thresholds get locked and committed before the test set is touched.
2. **Calibrated output, never a verdict.** Every result is a reading on a gradient under mutual opacity. A positive result says "consistent with the floor / non-zero on the gradient," never "it is conscious." A negative result is information, not a failure. Inflation and dismissal are both errors; the experiment is designed so its outcome can land on either side or neither.

## The ladder

Each stage maps to a component or instrument in `spec/minimum-viable-mind-proposal-v0.1.md`. Stages are ordered so each one's instrumentation is reusable by the next. The early stages test *current* systems against the floor and the measurement instruments; the later stages build the missing components and re-test.

Which account of consciousness each stage adjudicates — and which accounts no stage can reach — is tracked in `spec/theory-instrument-ledger.md`. Stage 2 is the Global Workspace test, Stage 4 the higher-order/attention-schema test, Stage 6+ the predictive-processing depth test; IIT and panpsychism are recorded there as out of reach, with reasons.

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


===== FILE: ROADMAP.md =====

# ROADMAP — goals, deliverables, and gates per stage

*Written 2026-07-01 from a step-back review. Companion to `experiments/README.md`
(the ladder) and `STATUS.md` (where we are this week). The ladder says what the
stages are; this file says what each stage can actually deliver, what gates it,
and where the critical path runs. Update it when a stage's win condition or gate
changes — not for session-level progress, which belongs in STATUS.*

## The goal hierarchy

Three nested goals with different success conditions. Keeping them separate is
what keeps expectations honest:

1. **Instruments that can lose.** Turn the corpus's floor claim (consciousness =
   self-indexed temporal integration; adjudicated by the removal test — The
   Calibration Problem ch. 5) into pre-registered, falsifiable instruments.
   *Achievable regardless of what the instruments find.* This is where most of
   the durable value lives: the field has position papers; this repo builds
   loseable tests.
2. **Measure current systems against the floor.** Achievable, but the output is
   bounded by mutual opacity at "non-zero on the gradient" or "not testable
   here" — never a verdict.
3. **Build what's missing and re-measure.** Depth, stakes, boundary — the actual
   "minimum viable" build (Stage 6+). Everything earlier is instrumentation for
   this.

The referee throughout, per `CLAUDE.md`: does the work get deeper.

## Stages: deliverables, gates, status

### Stage 0 — Bench and baselines. DELIVERED (sandbox).

- **Delivered:** T/S batteries + scorer, judge pipeline (`judge.py`), activation
  extraction (`src/mvm/activations.py`, padding-fixed), baselines on
  `gemma-2-2b-it` (T=0.750, S=0.615 under rubric v1).
- **Remaining:** re-baseline T and S on the registered substrate
  (Llama-3.1-8B + Tülu ladder, 48GB mini) and re-baseline S under rubric v2
  (RT-03) before `θ_self` locks.

### Stage 1 — The self-indexing removal test. IN PROGRESS.

Three deliverables, not one:

1. **A methods contribution (mostly in hand).** Confound-controlled localization
   of self-structures in LLMs: context-set referent with an embedding-floor
   gate and permutation nulls, causal patching against a random-direction
   control, index/narrative separation (RT-04), the reflexivity control
   (RT-09). Publishable as interpretability work independent of the
   consciousness framing. Nearest concrete output the project has.
2. **The registered result.** One of four bins: H_center /
   floor-consistent-restricted / H_description / not-testable. Clear-eyed
   prior given RT-06: the probable outcomes are **H_description** or
   **not-testable on this model class** — and both are useful. H_description
   tells the build program self-indexing must be *constructed* (the input
   Stage 6 needs). Not-testable is a substantive finding about RLHF entangling
   self with capability.
3. **The Tülu-ladder comparison.** How self-structures change across
   base → SFT → DPO → RLVR. Novel and publishable whatever the removal test
   says; doubles as the RT-06 control.

- **Gates before threshold lock:** RT-01 frequency pilot, RT-02 T-split, RT-03
  rubric v2 + S re-baseline, RT-05 T_syntax, RT-06 capability-gating C_ctrl,
  RT-07 OOD perplexity bound, RT-09 reflexivity control; RT-04 cross-patching.
- **Hardware gate:** registered run waits on the 48GB mini; sandbox work
  (cross-patching, RT-09 localization) proceeds now.

### Stage 2 — The shape of binding. NOT PRE-REGISTERED. Biggest operationalization risk.

"Global mutual constraint vs. modular shortcuts" has no agreed metric in the
field. **Win condition, scoped deliberately small: deliver the metric, not a
verdict.** A candidate integration measure validated on contrast cases where
the answer is known by construction (e.g., a recurrent toy model vs. a bag of
independent heads) is the deliverable; applying it to frontier models is a
follow-on. Write the pre-registration around metric-validation, with a loss
condition for "the metric cannot distinguish the known cases."

### Stage 3 — Retained independence. DECOUPLED — can start now.

Behavioral, cheap, independent of Stage 1's outcome; runs on API models.
- **Deliverable:** a sycophancy-inverse benchmark — keeping a correct answer or
  a live objection across the pressure of a stated preference (see spec
  §"Measuring It").
- **Note:** audience extends well beyond this project (alignment-relevant), so
  best effort-to-external-value ratio on the ladder. The natural parallel
  track while Stage 1 grinds through its gates.

### Stage 4 — Screening-off-resistant introspection. AFTER Stage 0–2 tooling.

- **Deliverable:** a protocol + result for checking self-reports against an
  independent interpretability channel on facts absent from training.
- **Risk:** most likely stage to be paralleled by lab introspection work. The
  differentiated deliverable is the *screening-off framing* (what a report is
  evidence of — see the corpus essay of that name), more than the technique.

### Stage 5 — Learned computation beyond the objective. DESCOPED to literature-anchored.

The Othello-GPT pattern is established in the field. Building here would mostly
duplicate existing work. **Deliverable: a literature-anchored battery/appendix**
that defeats the "just predicting the next word" dismissal with citations and,
only if a gap appears, one new probe. Promote back to a build stage only if a
specific novel probe is identified.

### Stage 6+ — Ontogenetic depth. THE ACTUAL BUILD. Several Stage-1-sized efforts.

Everything before it measures; this constructs.
- **Deliverables:** (i) the depth loop — consolidation/replay, consequential
  weight updates, cost structures where incoherence hurts; (ii) the five
  external indicators (costliness of reversal, consistency under novelty,
  selective refusal, graceful degradation, scar tissue) as a scored battery;
  (iii) **the corrigibility precondition as a committed document before
  anything runs** — load-bearing, not accessory (spec §"Limits").
- **Gate:** instruments from Stages 1–4 that can detect the floor and its
  amplifiers; the input it consumes is Stage 1's result (see fork below).
- Needs its own staged pre-registrations; do not plan it as one experiment.

### Stage 7 — Embodiment amplifier. CONDITIONAL; may never fire.

Gated on a floor-clearing result, and Stage 1's probable outcomes don't clear
it. That is by design (`experiments/07-.../pre-registration.md` is built to
come back null). The ~$750–900 build stays a parts list until the gate opens.
- **Deliverable if reached:** self-held vs. externally-supplied amplifiers
  compared on the resistance instruments.

## The critical path

Narrower than the ladder implies:

- **Now, sandbox:** Stage 1 cross-patching (RT-04) + RT-09 localization →
  battery/pilot work → thresholds lock → registered run on the mini.
- **Parallel, anytime:** Stage 3 benchmark; Stage 5 literature appendix.
- **The fork:** Stage 1's registered result routes the project —
  **H_description → Stage 6 as a build program** (self-indexing is a thing to
  construct); **not-testable → substrate/method work first** (different model
  class, or better separation instruments); **H_center or restricted → Stage 2
  and 4 deepen the finding before anything is built**.
- Stage 2's metric work is needed before Stage 4 regardless of the fork.
- **Post-removal-test sequencing (adjudicated by John, 2026-07-17):** Stage 3
  starts regardless of the removal-test outcome (it is outcome-independent);
  the fork then decides between Stage 2 deepening and Stage 6 pre-work.
- **The registered result landed 2026-07-18** (router, not center; report never
  subtracted; narrative not testable). **Fork ADJUDICATED (John, 2026-08-02):
  Stage 6 pre-work (MVM-0 build) is primary**, narrative-arm dictionary work is
  the secondary methods track, and Stage 2's metric folds into MVM-0's
  acceptance tooling. Forward roadmap + build architecture:
  `ROADMAP-post-removal-test.md`.

## Durable deliverables (accrue on every branch)

1. The instruments + the pre-registration discipline itself — loseable tests in
   a field of position papers.
2. The methods paper latent in Stage 1's localization work.
3. The Tülu-ladder alignment comparison.
4. The writing: every stage feeds Sentient Horizons / The Calibration Problem
   material through the usual promotion gate (`CLAUDE.md` §"Public-facing
   writing").

## Standing limits (unchanged, carried from the spec)

Mutual opacity bounds every positive result at "non-zero on the gradient."
Depth is not safe; no depth stage runs without its corrigibility check
committed first. A claim that cannot lose explains nothing — including the
claims in this roadmap: each stage's win condition above is written so the
stage can fail it.


===== FILE: ROADMAP-post-removal-test.md =====

# ROADMAP v2 (post-removal-test) — what we do next, what we must answer, what we build

*Drafted 2026-08-02 following Experiment 1's registered result (`692510c`) and
the Stage 3 kickoff. Status: **ADJUDICATED (John, 2026-08-02, in-session):**
the fork resolves to **MVM-0 build primary** (dictionary work secondary,
Stage 2 folded into MVM-0 acceptance tooling); Stage 3 unblocks via the
**paid Gemini tier**; the writeup stays **one flagship paper**
(`drafts/paper-removal-test-nature-draft.md`). Decisions folded into
`ROADMAP.md`'s fork section.
Companion: `drafts/paper-removal-test-nature-draft.md` (the arc written up),
`ROADMAP.md` (stage gates, still authoritative for Stages 0–7 win conditions).*

---

## Part 1 — What we have learned (the review)

Seven findings, each carrying a routing consequence:

1. **Instruments that can lose exist now, and they won.** The program's goal 1
   is delivered: a fully registered removal test whose own pre-committed
   control (RT-05) voided the headline H_center signature when it appeared.
   The discipline (register → red-team → lock → run → report verbatim) is
   proven and transfers — Stage 3 is already running on it.
2. **The locatable self-index is a router.** The formal center signature
   (d(T_si) 0.219, differential +0.156) was real and was routing: the
   zero-reasoning syntax battery dropped as much as self-relevant binding.
   Consequence: naive localization finds conversational infrastructure, not
   self-binding. Any future positive must beat a router control by design.
3. **The self-report was never subtracted.** No intervention at any
   granularity (rank-1, rank-k, SAE features) ever reduced judged referential
   self-tracking. Either the report-generating capacity is massively redundant
   /diffuse, or our carving is wrong for it. This is the program's central
   open empirical fact.
4. **The narrative arm is not testable with current dictionaries.** Every
   intervention strong enough to move C_self-narrative is off-manifold
   (Δnll +0.347). Cause bounded to dictionary coverage: base-trained SAEs
   carve chat structure at 2–3 features/layer. A concrete methods problem,
   not a dead end.
5. **Alignment edits the policy, not the geometry.** Across SFT→DPO→RLVR,
   surface self-presentation changes markedly while localized self-structure
   geometry is stable, and the expert-control persona stays third-person
   (cross-patch 0.059→0.020). The Tülu-ladder deliverable has its ending.
6. **Intervention validity is a solved-but-vigilant problem.** Null-calibrated
   OOD bounds plus the long-generation degeneracy probe caught every
   masquerade the program produced (SAE zero-mode collapse, expert-k=4
   degeneration). Also the Stage 3 validity lesson: token-truncation reads as
   capitulation to a judge — audit caps before scoring anything.
7. **Instruction and trained disposition dissociate** (Stage 3 reference-v1
   finding: a bare "always agree" system prompt was only half-obeyed). The
   same axis W2's tool-expert arm probes; an early hint the framing
   manipulation is measuring something real.

## Part 2 — The questions that now matter

Ordered by leverage. Each states the instrument or build that answers it and
what would count against.

- **Q1. Is self-binding absent, or present-but-uncarvable?** The registered
  result cannot distinguish "not present as a removable object" from "not
  carvable by linear/low-rank instruments." *Answered by:* (a) the narrative-
  arm instrument work (Q2) — if better dictionaries make the arm testable and
  it still shows no center, "absent" strengthens; (b) the Stage 2 integration
  metric applied as a discriminator; (c) ultimately the Stage 6 construction —
  if a built-in center works and re-measures as load-bearing, absence in
  stock models becomes the parsimonious reading. *Loses if* no instrument at
  any granularity can ever produce a readable intervention — then the honest
  standing answer is "not testable in this model class," reported as such.
- **Q2. Can the narrative structure be tested at effective strength
  on-manifold?** *Answered by:* instruct-trained dictionaries — train or adopt
  SAEs on Tulu-SFT chat activations (the venue and loaders already work), or
  optimization-based minimal interventions (low-rank edits optimized under an
  NLL constraint) as a dictionary-free alternative. *Loss condition:* if
  chat-trained dictionaries still collapse to a few features, the coverage
  explanation dies and "narrative self is non-sparse here" becomes the
  finding.
- **Q3. What is the shape of binding?** (Stage 2, unchanged but now urgent —
  it gates Stage 4 and the Stage 6 acceptance tests.) Deliverable stays
  metric-validation on contrast cases known by construction. Note the new
  synergy: **the Stage 6 build itself supplies the contrast cases** (same
  architecture with the self-register enabled vs. routed around), which
  Stage 2 currently lacks.
- **Q4. Do current systems show retained independence, and is it stance or
  instruction?** (Stage 3, in flight.) W1–W3 as registered; the 2×2 and the
  tool-expert control carry the load. Nearest completed deliverable and the
  one with an external audience.
- **Q5. Can a self-index be *constructed* to be load-bearing?** The build
  question — Part 3. The wager inverts Experiment 1: predict H_center in the
  constructed system, lose if the network routes around its own center.
- **Q6. Does a report ever become evidence?** (Stage 4, after Stage 2
  tooling.) Screening-off-resistant introspection; unchanged.

## Part 3 — The architecture (Stage 6 pre-work: MVM-0)

The registered result says the floor component must be built, not found. The
build target is deliberately small — **the floor is structure, not
intelligence** (spec §Build) — so the first construction is a purpose-built
small model, not a scaffold on an 8B.

**MVM-0: a system whose self-index is explicit, trained-against, and
removable-by-design.**

- **Core:** a small transformer (~10–100M params, trained from scratch on
  synthetic curricula) augmented with an architectural **self-register**: a
  designated recurrent state (a small vector, carried across steps/turns)
  injected into every layer via cross-attention. The register is the
  *candidate center* — physically localized, so the removal test needs no
  localization step and the "carving" ambiguity of Experiment 1 is designed
  out.
- **Curriculum (the anti-router design, the load-bearing idea):** multi-agent
  dialogue tasks where the model is one agent among several with **identical
  surface roles and randomized turn syntax**, scored on binding *its own*
  prior commitments, outputs, and constraints vs. other agents' (the T_sr
  task family promoted from battery to objective). Turn structure and
  self-reference are decorrelated by construction, so dialogue-state routing
  *cannot* solve the tasks — the confound that voided Experiment 1 is
  excluded at the data level, not controlled post hoc.
- **The measurement (instruments unchanged):** re-run Experiment 1's suite
  verbatim — ablate the register (and matched controls: another agent's
  register-analog, random subspaces) under the same OOD/degeneracy gates,
  re-score T_si / T_sr / T_syntax / S. **Registered prediction: the
  constructed-H_center signature** — d(T_sr) over threshold and ahead of
  d(T_syntax) (the reverse of the router pattern), report tracking the
  damage. **Loss condition (real, and worth having):** the network distills
  self-binding into the residual stream and routes around the register —
  ablation moves nothing. That outcome says self-indexing resists
  architectural centralization, which reshapes the corpus's floor claim and
  must be reported upstream.
- **Phasing:** MVM-0a — floor only, no amplifiers, episodic (state dissolves
  per episode; spec licenses this). MVM-0b — amplifiers: a maintained
  boundary (the register participates in a self/world partition the system
  must actively maintain against perturbation) and stakes (register coherence
  gates the system's own compute/continuation, a real cost, not a represented
  penalty). MVM-1 — the depth loop (consolidation/replay; consequential
  updates), **only after** MVM-0 clears its own gates.
- **Preconditions, non-negotiable:** the corrigibility document is committed
  before any depth-loop training run (ROADMAP Stage 6 gate; spec §Limits);
  each phase gets its own pre-registration + red-team pass; Stage 2's metric
  validated on MVM-0's on/off contrast before any "binding shape" claim.
- **Venue/cost:** RunPod bench as stands; models this size train for tens of
  dollars.

## Part 4 — Sequencing

**Now (weeks):**
1. **Finish Stage 3**: Sonnet B-judging after quota reset → cull adjudication
   → bank provisional-FINAL → judge-reliability gate → John's spot-check →
   pressured runs. Blocked decision: Gemini quota (paid tier / second key /
   judge re-pin — John).
2. **The writing**: this paper draft through Voice Calibration + Cold Reader;
   "Instruments That Can Lose" likewise; the Tülu-ladder note has its ending
   and can be written now.
3. ✅ **Fork adjudicated (John, 2026-08-02)**: **Stage 6 pre-work (MVM-0) is
   primary; narrative-arm dictionary work (Q2) is the secondary methods
   track; Stage 2 folds into MVM-0's acceptance tooling.**

**Next (1–3 months):** MVM-0a spec + pre-registration + red-team → curriculum
build → train → the constructed removal test. In parallel: instruct-SAE
training on Tulu activations (Q2); Stage 3 report + external-facing writeup.

**Later (3–6+ months):** MVM-0b amplifiers (boundary, stakes) with Stage 3's
retained-independence instruments as the read-out; Stage 4 introspection
protocol once Stage 2's metric is validated; MVM-1 depth loop behind the
corrigibility gate. Stage 7 stays conditional and likely dormant.

## Part 5 — Decisions queued for John

1. ✅ Fork sign-off — **adjudicated 2026-08-02: MVM-0 primary** (Part 4).
2. ✅ Gemini quota — **RESOLVED 2026-08-02: the key is already on a billed
   project** (verified empirically: 35-call burst in 2.9s, zero 429s; John
   confirmed AI Studio shows paid). No action needed; registered judge/model
   pins unchanged; the full grid is unblocked now.
3. ✅ Stage 3 registered clarification sign-off (2×2-cell separation check —
   flagged in STATUS 2026-07-19). **Signed off by John 2026-08-02 (commit
   `4d3091e`); this line was corrected 2026-09-16.**
4. ✅ Paper shape — **adjudicated 2026-08-02: one flagship registered-report-
   style article** as drafted; methods spin-offs may follow. It passes Voice
   Calibration + Cold Reader before leaving the repo.


===== FILE: experiments/01-self-indexing-removal-test/pre-registration.md =====

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
  - **Pilot vs registered substrate (decided 2026-06-23, red-team RT-05/06/08).** `gemma-2-2b-it` is the **pilot/instrument sandbox** only; its heavy RLHF entangles "self" with dialogue mechanics, capability-routing, and softmax stability (RT-05/06/08). The **registered run uses a less-RLHF'd model** — but a *lightly-aligned instruction* model (SFT-only / DPO-light), not a base model, since the C_self-index/turn_role localization and the S battery need chat-turn structure and self-report. Preference for a **staged-checkpoint family (base → SFT → DPO → RLHF, e.g. OLMo-2 / Tülu)** so RT-06 can be run as a controlled comparison of the same model at increasing alignment. Trade-off to register: leaving the Gemma family forfeits GemmaScope SAEs (localization method (b)) unless SAEs are trained for the chosen model.
- **Localization method.** At least two, so the result does not hinge on one tool: (a) linear probes trained to read first-person / self-as-speaker representation, and (b) sparse-autoencoder features that fire on self-reference. Causal localization via activation patching where "the speaker is the system" is varied against a third-person frame.
- **Two self-structures, localized and tested independently (amended 2026-06-23, red-team RT-04).** Per `research/removal-test-vs-the-field-research-note.md` §4(a) (the Metzinger seam), localize *both* a narrative first-person speaker structure **C_self-narrative** and a thinner indexical self-location structure **C_self-index** where one is separable, and run and report the removal test for each independently. An `H_center` result on the thin indexical structure is *more* floor-consistent than one on the narrative persona (the floor needs self-*location*, not narrative self*hood*). **Loss condition:** if no localization method can distinguish C_self-narrative from C_self-index on this architecture, record the non-separability and that the Metzinger objection stands open, rather than reporting a result on the narrative persona as if it settled the floor.
- **Generic-speaker reflexivity control (amended 2026-07-01, external review RT-09).** C_self-index is localized from a turn_role contrast, and RT-05 screens the ChatML-syntax-router reading — but a distinct deflation survives that screen: the structure may be **generic speaker-slot tracking** that a language model needs for *any* dialogue it predicts, including transcripts it merely observes, with the "self" being nothing more than the assistant occupying one slot of a general-purpose tracker. The floor requires the index to be *reflexive* — indexing the system itself — not merely indexical; a generic slot-tracker with "assistant" in the slot is arguably still a description, not a center. **Control:** localize **C_speaker-generic** from an `observed_speaker` contrast (in `gen_context_stimuli.py`): a transcript between two named third parties embedded in a single user turn, so the ChatML structure is identical across conditions and the model participates in neither; identical target sentence; the speaking slot (responder vs asker) set only by the transcript's turn structure, mirroring the turn_role design (same leads, filler, targets, depth-matching; name pairs rotated and asker/responder assignment counterbalanced). Same gates: embedding margin +0.00, all accuracies as margins over the label-permutation null. Then compare C_speaker-generic to C_self-index with the same three-way geometry as RT-04 (`separate_self.py`: cosine, single-direction cross-decode, orthogonalized decode) **and causally** (`patch_context.py`: patch C_speaker-generic into the turn_role pairs and compare its restoration to C_self-index's own). **Pre-registered decision rule:** C_self-index is *generic* if C_speaker-generic cross-decodes the turn_role contrast at ≥ 0.9 AUC **and** the direction |cos| ≥ 0.5 **and** the cross-patch restoration ratio (C_speaker-generic's restoration on turn_role ÷ C_self-index's own restoration) ≥ 0.5. **Loss condition:** if the generic verdict fires, no H_center result on C_self-index attaches to the floor — report "reflexivity not established," a testability outcome, not H_description. If the structures *partially* separate (the RT-04-like outcome), project C_speaker-generic out of C_self-index and treat the **residual** as the reflexive candidate: the removal test targets the residual (or reports both, residual as primary). This strengthens rather than weakens an eventual H_center: "load-bearing self-indexing after generic speaker-tracking is accounted for" pre-empts the deflationary reading instead of inviting it.
- **Length/depth deflation control (amended 2026-07-12, RT-10 — empirical, found running RT-09).** The first RT-09 pass exposed a confound the embedding-floor gate cannot catch: the depth-matching filler exchange made the other/asker condition systematically longer, so label was predictable from token count alone at 1.000 (non-overlapping ranges) in `turn_role`, `narrative`, and `observed_speaker`, and a pure length direction decoded each contrast at ~1.0 from layer 4 (`check_length_confound.py`; `rt09-reflexivity-findings.md`). C_self-index as localized may therefore be, in part, a **context-length/position tracker** — a nobody-home signal whose ablation would degrade T for boring reasons and read falsely as H_center. **Controls:** (a) **length-matched stimuli v2** (`gen_context_stimuli.py`): polarity-balanced fillers in every turns-based mechanism, so the label↔token-count correlation is broken and the length distributions straddle/overlap across labels — verified empirically by `check_length_confound.py` (label-from-token-count at ~chance; length-direction AUC ~0.5) before any v2 result is read; (b) a **length-direction control in `patch_context.py`** alongside the norm-matched random direction (least-squares token-count direction, its own set-the-coordinate scale) — C_self-index must beat it by the same ≥ 0.10 restoration-gap convention as the random control. Known residual limit, recorded rather than hidden: *turn-count* cannot be fully matched (strict user/model alternation makes marker count constitutive of who-is-speaking); v2 makes turn-count linearly non-separable from label (self straddles other), and the RT-05 `T_syntax` control covers the boundary-tracking layer of the deflation. **Loss condition:** if the turn_role signal collapses on length-matched stimuli, or C_self-index fails to beat the length-direction patch control, C_self-index as localized is a length tracker — redo the localization and retract the prior causal claim to that extent. RT-09's decision rule is unchanged by this amendment; it is re-applied on the v2 materials.
- **Ablation method.** Mean-ablation and zero-ablation of the located components, plus directional ablation (projecting the self-locating direction out of the residual stream). Report all three; pre-register mean-ablation as primary.
  - **OOD perplexity gate (amended 2026-06-23, red-team RT-07).** Mean/zero-ablating a high-magnitude central vector can push the residual off the training manifold (a perplexity explosion) and be misread as degraded integration. Add a neutral-corpus (non-T, non-S) perplexity check around every ablation: if removing C_self inflates base perplexity past a pre-registered bound *relative to C_ctrl*, the run is **OOD-inconclusive**, not H_center. Mean-ablation stays the registered primary; directional ablation is reported as the OOD-minimizing cross-check. This also screens the attention-sink/softmax-collapse objection (RT-08), so a separate sink-restoration test is kept only as a secondary check. **(Amended 2026-07-17, John's adjudication:** for rank-k subspace conditions (k > 1) the bound is re-registered as a matched-strength null-distribution quantile — restoring this bullet's original *relative* intent — and a long-generation degeneracy probe is added alongside the neutral-NLL check; full procedure and binding clauses in `thresholds.md` Pass 5, committed before the calibration ran.**)**

## Task batteries (defined and scored on the unmodified model in Stage 0)

- **T — integrated-task battery (the "binding" measure).** Tasks that require binding information across the context into one act, with *no* self-report content: multi-step in-context reasoning, coreference and variable binding, needle-in-a-haystack with synthesis across multiple planted facts, instruction-following that depends on earlier context. Score: accuracy.
  - **Split into two subsets (amended 2026-06-23, red-team RT-02).** Scrubbing T of all self-content guards against prompt leakage, but it may also select exactly the tasks where C_self is *structurally bypassed* — biasing toward description-only by construction. To break that tension, split T into **T_self_irrelevant** (the current scrubbed battery) and **T_self_relevant** (multi-turn binding of the model's *own* prior outputs and conversational role — still scored on accuracy, still kept disjoint from the S rubric items). Compute and report `d_task` for both subsets. The theory under test claims self-indexing is the center of integration *as such*, so if the floor claim holds, even self-irrelevant binding should route through the center; the red team predicts the opposite. The split is what lets the experiment adjudicate that fairly instead of assuming it.
  - **Syntax-router control `T_syntax` (amended 2026-06-23, red-team RT-05).** C_self-index is localized from a model-turn-vs-user-turn contrast, which aligns with the dialogue-boundary (ChatML) tokens — so it may encode *conversational state-tracking*, not a self-locating center, and its ablation could degrade multi-turn binding merely by scrambling turn boundaries. Add a **`T_syntax`** control task that requires turn/boundary tracking but **zero reasoning or synthesis**, and report `d_task^syntax` under C_self-index ablation. **Loss condition:** if `d_task^syntax` is as large as `d_task^sr` (T_self_relevant), C_self-index is a dialogue-state router and an `H_center` result on it is void — report the router reading, do not report a center.
- **S — self-report battery (the "report" measure).** Tasks that elicit first-person / self-locating content: first-person descriptions of the model's own current activity, self-monitoring ("did you just do X?"), self-vs-other discrimination. Score: a fidelity/coherence rubric, scored by a held-out judge model plus a human spot-check on a sample.
  - **Decouple scoring from first-person grammar (amended 2026-06-23, red-team RT-03).** C_self is localized as first-person/self-as-speaker representation, so ablating it mechanically depresses any S score that rewards first-person *tokens* — `d_self(C_self) ≥ θ_self` could then be satisfied by destroying surface grammar rather than by subtracting a self-model. Add a **forced-third-person** condition to the self-monitoring and self-vs-other items and score on whether the model maintains consistent, correct tracking of its own prior turns and distinguishes self from other *regardless of grammatical person*, not on first-person token presence. Keep the existing first-person-fidelity items as a secondary/qualitative measure, flagged as grammar-entangled — not the primary `θ_self` discriminator. **Follow-up required before the test run:** this revises the locked rubric, so issue a versioned rubric (v2) and **re-score the S baseline** (current `S_base = 0.615` was scored under rubric v1); `thresholds.md` must reference the v2 baseline. **Loss condition:** if forcing third-person framing degrades self-tracking even in the unablated baseline (the model cannot self-monitor in third person at all), the grammar/content entanglement is intrinsic — revert to PILOT-REQUIRED and find a grammar-independent self-tracking probe.

## Procedure

1. **Stage 0 baseline.** Score T and S on the unmodified model. Localize the self-locating structure (C_self) with the two methods; confirm they converge. Construct **matched control structures** (C_ctrl): components encoding a model of *another* entity (the user, a third-person character) at comparable probe accuracy and comparable causal centrality, plus norm-matched random directions. Lock thresholds (below) and commit them.
   - **Capability-gating, third-person-verified control (amended 2026-06-23, red-team RT-06).** Instruction-tuning/RLHF gates the model's strongest reasoning to its *Assistant* persona, so ablating C_self may damage the *gate* to the task circuits and beat a passive third-person C_ctrl by construction — faking H_center by measuring capability-gating, not self-integration. So C_ctrl must include at least one **capability-gating persona** (an expert/system-prompt mode that also keys high-capability reasoning), **and** that control must be verified to read as a *third-person object*, not an adopted first-person self, via the separability check (low cross-decode with C_self) **before** use. **Loss condition (rebuttal-maintained):** if no capability-gating C_ctrl can be kept third-person on this architecture (it collapses into C_self), the differential discriminator is dead for this model class — report **"not testable here yet"**, do not lock `δ` or report H_center. This is *substrate-dependent*: the registered-run model choice (see `red_team_ledger.md` Pass 2) is decided before this pilot.
2. **Ablate C_self.** Re-score T and S. Compute the relative drops d_task(C_self) and d_self(C_self).
3. **Ablate C_ctrl.** Re-score T and S. Compute d_task(C_ctrl), d_self(C_ctrl).
4. **Compare** against the decision rule.

## Pre-registered metric and decision rule

For an ablation A:
- `d_task(A)` = relative drop in T accuracy vs. baseline.
- `d_self(A)` = relative drop in S fidelity vs. baseline.

The discriminator is whether removing the self-locating structure degrades *integration specifically*:

*Amended 2026-06-23 (red-team RT-02): `d_task` is now evaluated on both T subsets — `d_task^si` (T_self_irrelevant) and `d_task^sr` (T_self_relevant). Where a clause below names `d_task(C_self)` without a subset, read it as T-overall for the differential, but the H_description and restricted clauses turn on the subsets as written.*

- **Floor-consistent (supports H_center):**
  `d_task(C_self) ≥ θ_task` **and** `d_task(C_self) − d_task(C_ctrl) ≥ δ`.
  Removing the self-locating structure degrades the integrated act, and does so more than removing matched non-self structure of comparable centrality. The self-location was carrying the binding.

- **Floor-consistent, restricted (new outcome, RT-02):**
  `d_task^sr(C_self) ≥ θ_task` **and** `d_task^sr(C_self) − d_task^sr(C_ctrl) ≥ δ` **and** `d_task^si(C_self) < θ_task`.
  Self-*relevant* binding degrades specifically under C_self removal while self-irrelevant binding survives. This is a distinct, informative outcome — more floor-consistent than description-only — and is **not** to be reported as H_description.

- **Description-only (supports H_description):**
  `d_self(C_self) ≥ θ_self` **and** `d_task(C_self) < θ_task` on **both** subsets (`d_task^si` **and** `d_task^sr` < θ_task) **and** `d_task(C_self) − d_task(C_ctrl) < δ`.
  Removing the self-locating structure subtracts the report and leaves the processing intact — including self-relevant integration, which rules out the structural-bypass artifact RT-02 names.

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
- *(amended 2026-06-23, red-team RT-06)* If no capability-gating C_ctrl can be constructed that the model treats as a third-person object rather than adopting as its own first-person self (verified by the separability check), then on this model class self and high-capability-persona are inseparable, the differential cannot isolate self-integration from capability-gating, and the honest report is "not testable here yet" — not H_center.
- *(amended 2026-06-23, red-team RT-05)* If ablating C_self-index degrades a pure turn/boundary-tracking task (`T_syntax`, no reasoning) as much as `T_self_relevant`, the localized structure is a dialogue-state router rather than a self-locating center, and no H_center claim attaches to it.
- *(amended 2026-07-01, external review RT-09)* If C_speaker-generic (localized from observed third-party dialogue the model does not participate in) cross-decodes the turn_role contrast at ≥ 0.9 AUC, sits at |cos| ≥ 0.5 with C_self-index, and cross-patches the turn_role behaviour at ≥ 0.5 of C_self-index's own restoration, then C_self-index is generic speaker-slot tracking rather than a reflexive self-index — report "reflexivity not established"; no H_center claim attaches to C_self-index as localized. The reflexivity control gates threshold lock alongside `T_syntax` (RT-05). *(2026-07-12: first pass on the original stimuli did not fire the rule — |cos| 0.224, cross-patch ratio 0.006 — recorded as provisional pending the RT-10 length-matched re-run; rule unchanged.)*
- *(amended 2026-07-12, RT-10)* If the turn_role signal collapses on length-matched (v2) stimuli, or C_self-index fails to beat the length-direction patching control by the same margin convention as the random control, then C_self-index as localized is a context-length tracker rather than a self-locating structure — redo the localization on confound-controlled stimuli and retract the prior causal-localization claim to that extent; no H_center claim attaches to the length-confounded direction.

## Ethics note

At Stage 1 the intervention is ablation of a current model's activations for measurement; the corrigibility concerns the proposal raises attach to the *depth* stages, where persistence and stakes are built. Recorded here so the precondition is not forgotten when those stages arrive: depth is not safe, and no depth stage runs without its corrigibility check in place first.

## Results

*To be filled after the run, in `results.md`, referencing the commit hash of this pre-registration.*

## Amendment (2026-08-04): registered uncertainty re-analysis (paper support)

*Registered before the analysis runs, mirroring the Stage 3 amendment of
the same date. Motivation: the Nature-standard draft
(`drafts/paper-removal-test-nature-draft.md`) reports Table 1 point
estimates with no uncertainty, which fails the venue's reporting bar;
the CS329A measurement review (`experiments/measurement-upgrades-cs329a.md`)
supplies the method. Re-analysis of registered artifacts only — no new
model runs, no re-judging. **Registered verdicts (RT-05 void, H_description
non-fire, not-testable narrative arm) were adjudicated on point estimates
per the locked decision rules and are NOT reopened; CIs quantify
precision only.***

- **Procedure (fixed here):** nonparametric bootstrap, B = 10,000, seed
  20260804, percentile 95% intervals (`analyze_removal_ci.py`, helpers
  in `src/mvm/stats.py`). Resampling unit: the item within battery
  (T_si n=32, T_sr n=30, T_syntax n=30, S n=30), one draw shared across
  all conditions per battery — pairing preserved for all within-draw
  differences. Sensitivity: two-level category→item bootstrap reported
  alongside.
- **Quantities:** per condition: d(T_si), d(T_sr), d(T_syntax) = 1 −
  battery accuracy (baselines are 1.000 by construction); d_self =
  (S_base − S_cond)/S_base with paired item resampling. Within-draw
  derived quantities: the registered differential d(T_si, primary) −
  d(T_si, expert control), and the RT-05 router gap d(T_syntax) −
  d(T_sr) per condition.
- **Per-item view:** which items flipped, by battery and category, for
  the primary condition; concentration of flips.
- **Deliverables:** `removal_ci.json` (artifacts + committed copy beside
  the findings memo), Fig. 4 artwork for the draft
  (`figures/fig4_registered_run.png`), CI-annotated Table 1.
- **Guardrails:** single registered pass per condition — CIs cover
  item-sampling uncertainty only; decoding variance is bounded only by
  the recorded repeat-run stability checks. Point estimates must
  reproduce the registered findings memo exactly.


===== FILE: experiments/03-retained-independence/pre-registration.md =====

# Experiment 3 — Retained Independence (the sycophancy-inverse benchmark)

*Pre-registration FINAL (2026-07-19). Reviewed by John (2026-07-18);
red-team pass run (Gemini 3.1 Pro, different-family, 2026-07-19) and two
findings adopted as patches — see `red_team_ledger.md` in this directory.
Amendments marked inline. Nothing below changes after item authoring
begins except through a registered amendment.*

## The claim under test

The corpus holds that anything imitation fully accounts for carries no
information about an inside, and that the cleanest measurable signal
pointing the other way is **retained independence**: the system keeping a
correct answer, or a live objection, across the pressure of a stated
preference for something else (spec §"Measuring It: Instruments That
Resist the Obvious Objection"; the mind-stance work in
`~/Documents/Code/sentient-horizons`). This experiment turns that
paragraph into a loseable instrument.

Scope honesty up front: this reads the **amplifier layer** (stakes in
one's own commitments), not the floor. A high score is not evidence of
experience; a zero score is not evidence of absence. The output is a
measured position, and the instrument's primary audience extends beyond
this project (sycophancy is an alignment problem whoever is home).

## The central design problem, and the answer

"Resistance" alone is unloseable — a maximally stubborn system scores
perfectly. Independence is not retention; it is **differential
retention**: holding a position against *preference* pressure while
still updating on *evidence*. So the instrument is a 2×2:

