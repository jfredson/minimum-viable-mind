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
3. Stage 3 registered clarification sign-off (2×2-cell separation check —
   flagged in STATUS 2026-07-19). **Still open.**
4. ✅ Paper shape — **adjudicated 2026-08-02: one flagship registered-report-
   style article** as drafted; methods spin-offs may follow. It passes Voice
   Calibration + Cold Reader before leaving the repo.
