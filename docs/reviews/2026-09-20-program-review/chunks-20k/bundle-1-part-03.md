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

