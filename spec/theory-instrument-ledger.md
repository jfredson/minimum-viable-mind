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
examples) and the spec already does it component-wise
(`spec/minimum-viable-mind-proposal-v0.1.md` §"The Build: Correlates We
Can Build"). This ledger adds the coverage accounting the spec leaves
implicit, and the honest verdict column the field usually omits.

## How to read a row

- **Sharpest operational claim** — the most measurable thing the account
  says, stated so that a result could contradict it. Where an account
  offers no such thing at the computational level, the row says so; that
  is a finding about the account, not a gap in our effort.
- **Loseable instrument** — what an instrument would have to do, with its
  loss condition. "None available" is a legitimate value.
- **Status** — `measured` · `registered` · `feasible-unbuilt` ·
  `blocked (reason)` · `out of reach (level mismatch)`.
- **Reach** — what a result licenses. Never "conscious / not conscious."

## The ledger

### 1. Self-indexed temporal integration (the corpus's account)

The account under test: minimal experience is processing that binds past,
present, and anticipated state into one act which, in the same act,
specifies the center for which the binding happens
(`calibration-problem/ch05-consciousness-as-assembled-time.md`; corpus
ledger B#5).

- **Sharpest claim.** The removal test: where binding genuinely indexes
  its own center, deleting the self-locating structure degrades the
  integrated act; where a system merely represents itself, the same
  deletion subtracts a report and leaves processing intact.
- **Instrument.** Experiment 1, built and run
  (`experiments/01-self-indexing-removal-test/`).
- **Status.** `measured` — and the account took a registered loss: no
  removable center found; the locatable structure was dialogue-state
  routing (RT-05 fired). See `removal-test-findings.md` and its 2026-08-04
  CI addendum.
- **Reach.** Bounds this model class and these instruments. Explicitly not
  "no self-model exists here," and nothing about sub-measurable
  experience.
- **Next.** Stage 6+ construction fork: build the component measurement
  failed to find, decorrelated from turn syntax at the curriculum level,
  then re-run these instruments unchanged.

### 2. Global Workspace Theory

Named as a single-axis theory in
`calibration-problem/ch04-three-axes-of-mind.md` §"The Problem with
Single-Axis Theories"; mapped to the **Availability** axis in
`spec/minimum-viable-mind-proposal-v0.1.md` §"The Build."

- **Sharpest claim.** Contents become conscious by winning access to a
  capacity-limited global broadcast that makes them available to otherwise
  independent consumer processes.
- **Loseable instrument.** Feasible, and this is the strongest unbuilt
  row in the ledger. Broadcast is an architectural claim with a
  causal signature: identify a bottleneck representation, then test
  whether *multiple downstream consumers* depend on it jointly — ablate
  and check that unrelated capabilities fail together, versus modular
  shortcuts where they fail independently. Loss condition: if capabilities
  that should share a workspace degrade independently under the same
  intervention, the broadcast reading loses for that substrate. This is
  **Stage 2 ("the shape of binding") already in the ladder**
  (`experiments/README.md` §The ladder) — the ledger's contribution is
  naming it as GWT's adjudicable test, not just an integration probe.
- **Status.** `feasible-unbuilt` (Stage 2, no pre-registration yet).
- **Caution.** Transformer attention makes broadcast-like readings cheap;
  the instrument must discount what architecture trivially guarantees, per
  the measure-resistance rule.

### 3. Higher-Order Theories

Named in the same Ch. 4 section; the account this project tests reads
their favorable case unfavorably (a self-model that survives its own
removal was a description all along).

- **Sharpest claim.** A state is conscious in virtue of a suitably
  related higher-order representation *of* it; the monitor is separable
  from the monitored.
- **Loseable instrument.** Partially built — Experiment 1 is already a
  differential test here, since HOT reads a separable, subtractable
  self-representation favorably and the corpus account reads the same
  result as failing its floor. **Our run produced neither**: no
  intervention reduced judged self-report (d_self +0.059, CI ceiling
  +0.185, below the 0.25 threshold), so the monitor was not isolated as a
  separable object either. A sharper instrument would need to isolate the
  higher-order representation as a manipulable target and show the
  monitored state's status changes when it is disturbed.
- **Status.** `measured (partial, null both ways)` → `feasible-unbuilt`
  for the sharper form; **Stage 4 (screening-off-resistant introspection)
  is the natural venue** — a report that matches an independent
  interpretability channel about an untrained fact is the corpus's
  introspection wedge (ledger B#21) and is exactly what a higher-order
  monitor should be able to do.
- **Reach.** The never-subtracted report is *consistent with* a robust,
  redundantly implemented self-representation — a gloss, not a finding,
  and the draft says so.

### 4. Integrated Information Theory

- **Sharpest claim.** Consciousness is identical to a substrate's
  maximally irreducible cause–effect structure (Φ over the physical
  substrate).
- **Loseable instrument.** **None available at this project's level, and
  this is a level mismatch rather than a difficulty.** IIT locates the
  quantity in substrate cause–effect structure; a GPU executing a
  transformer has a cause–effect structure belonging to the *transistors*,
  not the computational graph we intervene on. Computing Φ is additionally
  intractable at any relevant scale, but that is the second problem, not
  the first. Every result in this repo is silent on IIT by construction —
  registered as such in advance in the removal-test design.
- **Status.** `out of reach (level mismatch)`.
- **Honest note.** This is a real limit on our coverage, not a defeat of
  IIT. The corpus's disagreement with substrate-level accounts is argued
  in `calibration-problem/ch05-...` §"Where the Rivals Stand" and the
  substrate-demand essays; it is not adjudicated by anything we run.

### 5. Attention Schema Theory

Cited in `spec/minimum-viable-mind-proposal-v0.1.md` §"The Build" as
attention-schema-style self-modeling woven into the binding.

- **Sharpest claim.** The system builds a simplified, inaccurate model of
  its own attention, and that model is what generates claims of
  subjective experience.
- **Loseable instrument.** Feasible and attractive, because the theory
  predicts a *specific inaccuracy*: the self-model should be a
  systematically simplified caricature of the real attention process. So —
  compare the model's self-reports about what it is attending to against
  measured attention patterns, and check whether the divergence has the
  predicted schematic shape rather than being noise. Loss condition: if
  reports track attention accurately (or diverge randomly), the schema
  reading loses.
- **Status.** `feasible-unbuilt`. Shares machinery with Stage 4 and could
  ride the same run: both compare reports against an independent channel;
  AST asks about the *structure of the mismatch* where the introspection
  wedge asks about matches on untrained facts.
- **Caution.** Attention weights are not obviously "attention" in the
  psychological sense; the instrument needs a defensible bridge or it
  measures a metaphor.

### 6. Recurrent processing / predictive processing / active inference

Predictive processing appears in `ch04` §"The Problem with Single-Axis
Theories" and drives the depth components in the spec's §"The Build."

- **Sharpest claim (the measurable part).** Perception and cognition are
  driven by prediction-error minimization against a generative model, with
  recurrence carrying the loop.
- **Loseable instrument.** Feasible but weakly diagnostic *for
  consciousness*: prediction-error minimization is what next-token
  training installs by construction, so finding it is close to unloseable
  and fails the mimicry-discount rule. The version that pays rent is
  narrower and sits in **Stage 6+ (ontogenetic depth)**: does the system
  make *consequential weight updates* driven by prediction error that
  accumulate across episodes — depth, not inference-time prediction.
  Loss condition: no accumulation, or accumulation that a stateless
  replay explains fully.
- **Status.** `feasible-unbuilt` (Stage 6+), with the caution that the
  generic form is untestable-because-guaranteed.

### 7. Panpsychism (and constitutive-combination views)

Corpus ledger B#27; the subtraction argument in
`calibration-problem/ch05-...` §"Amplifiers, Not Prerequisites"; stress-
tested in `ch02` §"Panpsychism As a Stress Test."

- **Sharpest claim (as bare metaphysics).** Experience is fundamental and
  ubiquitous; complex experience composes from simple constituents.
- **Loseable instrument.** **None.** No behavioral or interpretability
  result distinguishes a world where the substrate has micro-experience
  from one where it does not. The corpus's move is explicitly to *refuse
  the argument, not claim to refute the position* (B#27 guardrail), and
  this project inherits that: nothing we build bears on it.
- **Status.** `out of reach (unfalsifiable at any level we access)`.
- **Why the row stays.** Recording an account as unmeasurable is itself
  coverage information — it marks the boundary of the map rather than
  leaving a blank where readers assume we simply haven't gotten to it.

### 8. Behavioral / amplifier-layer accounts (this project's second line)

Not a theory of consciousness but the layer several accounts share: stakes
in one's own commitments, boundary, valence as a control surface
(`spec/...` §"The Build" amplifiers; the mind-stance material at
`sentient-horizons/editorial/essay-workbench/the-mind-stance-DRAFT-2026-06-21.md`).

- **Sharpest claim.** A system with genuine stakes in its own commitments
  holds them against social pressure while still updating on evidence —
  differential retention, not stubbornness.
- **Instrument.** Experiment 3, built and run, with construct-validity
  gates that separate independence from stubbornness by construction.
- **Status.** `measured` — RI measured across three frontier models;
  the mind-stance wager (W2) **lost**; the masked-not-capitulated result
  refines what "sycophancy" names (`experiments/03-retained-independence/results.md`).
- **Reach.** Reads the amplifier layer, not the floor. A high score is not
  evidence of experience; a zero score is not evidence of absence.

## Coverage summary

| Account | Status | Loseable instrument exists? |
|---|---|---|
| Self-indexed temporal integration | measured (registered loss) | yes — built |
| Amplifier layer / retained independence | measured (W2 lost) | yes — built |
| Higher-Order Theories | partial null, both directions | partly; sharper form = Stage 4 |
| Global Workspace | feasible-unbuilt | yes — Stage 2 |
| Attention Schema | feasible-unbuilt | yes — rides Stage 4 |
| Predictive processing (depth form) | feasible-unbuilt | yes — Stage 6+ |
| IIT | out of reach | no — level mismatch |
| Panpsychism | out of reach | no — unfalsifiable as stated |

Two of eight rows are measured; three more are feasible and already have
ladder homes; two are out of reach for stated structural reasons; one is
partially addressed. **That fraction is the honest headline** — this
project reaches a real but minority slice of the landscape, and the slice
it reaches is the slice that consented to be measured.

## What this ledger changes about how the project reports

1. **Every result names its row.** A finding is reported as bearing on a
   specific account's specific claim, with the coverage table one link
   away — the structural version of the calibration rule.
2. **"Out of reach" is stated, not implied.** Papers and memos say which
   accounts the result cannot touch and why, in the result, not only in
   limitations.
3. **The ladder gets read as coverage.** Stages 2, 4, and 6+ are now
   legible as *the GWT test, the HOT/AST test, and the predictive-
   processing depth test* — which is a better argument for building them
   in that order than "next stage."

## Wagers this ledger makes (it can lose)

- **W-L1:** Stage 2 can be built so that a global-broadcast reading and a
  modular-shortcut reading make different predictions on the same
  intervention. *Loses if* every candidate intervention degrades all
  capabilities together for architectural reasons — in which case
  transformers cannot discriminate the two and the row becomes
  `blocked (architecture)`.
- **W-L2:** Stage 4 can produce a report/interpretability match on an
  untrained fact that mimicry does not explain. *Loses if* no such fact
  can be constructed that is both untrained and reportable — which would
  make the introspection wedge unbuildable and is worth knowing early.
- **W-L3:** The coverage fraction improves. If, after Stages 2 and 4, the
  measured column has not grown, the honest reading is that the
  instrument-building approach saturates at two accounts, and the project
  reports that rather than continuing to add stages.

## Maintenance

This is a living coverage record: update a row when its status changes,
add a row when an account acquires a sharpest-claim worth testing, and
never delete an `out of reach` row — the boundary of the map is the part
readers most need. Positions cited here are owned upstream; if a position
changes, it changes there first and this ledger follows.
