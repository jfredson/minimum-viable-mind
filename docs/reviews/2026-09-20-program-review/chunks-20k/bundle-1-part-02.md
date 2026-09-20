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


===== FILE: spec/corrigibility-commitments.md =====

# Corrigibility commitments

*v1.1, 2026-08-16 (v1.0: 2026-08-07). **Owner: John** (adjudicated
2026-08-07, MVM-0a registration decision 4 [RT-15]; target date
2026-08-21, met early). Drafted by Claude at John's direction and
committed on his instruction; John's read-through is what makes this a
gate rather than a note, and any line he wants changed is amended before
the first training run. Amendments to this document are John-only and
are recorded as registered amendments — a training run may not cite a
hash of this file that postdates its own pre-registration. **v1.1
(John, 2026-08-16, at the pre-5-seed review point): C2 amended to
delegate launch execution — not launch authority — see C2; ratified by
John's read-through this date.***

## Why this document exists

The corpus's position is that depth is not safe and the project proceeds
anyway, with eyes open (`CLAUDE.md`; the owning source is
`spec/minimum-viable-mind-proposal-v0.1.md` §The Limits This Proposal
Does Not Get to Escape: build for formation, preserve **accountable
corrigibility during the window when correction is still possible** — "if
the ethics arrives after the engineering, it arrives too late"). RT-15
made the operational point: a precondition with no owner and no text is a
note. This is the text. It is written **before** any MVM model exists, at
a scale (≤100M parameters, synthetic closed-grammar dialogue, episodic
state that dissolves at episode end) where the honest credence that
anything morally relevant is present is very low — and non-zero, per the
standing calibration rule. The document exists now because MVM-0a is
MVM-0b's substrate, one config change away, and precommitment is only
precommitment if it precedes capability.

## What this document gates

1. **Any training run that adds a maintained boundary, persistent
   cross-episode state, or a stakes term that gates the system's own
   compute** (MVM-0b and beyond) must cite this document's commit hash in
   its own pre-registration, and that pre-registration gets its own
   red-team pass (pre-registration.md v1.0 §Ethics). Nothing in MVM-0a's
   registration pre-authorizes MVM-0b.
2. **MVM-0a training runs** (floor-only, episodic) are licensed by the
   registered design, subject to the commitments below.

## Commitments

- **C1 — Non-promotable checkpoints.** Every MVM-0a checkpoint and
  artifact is tagged `non-promotable`: it may be analyzed, ablated, and
  published about, but may not be loaded as the initialization or
  substrate of any system with a maintained boundary or stakes without a
  new pre-registration citing this document (§What this gates).
- **C2 — A human authorizes every run; execution may be delegated, authority may not.**
  *(v1.1, 2026-08-16 — v1.0 read "a human launches every run" and was
  practiced as John typing the launch command himself; this amendment
  delegates the keystroke, never the decision.)* No training run starts
  without John's explicit go for that run or that registered batch.
  Claude may execute a launch **only** when all of the following hold:
  (a) John has given the go in the live session, in his own words,
  naming the specific run(s) — seed, twin/full, scale — or a specific
  registered batch; (b) the go is quoted verbatim in that run's compute
  ledger row, so the authorization trail is auditable from artifacts;
  (c) the funding rule in force (balance ≥ in-flight cost + margin) has
  been checked and passes; (d) the launch uses the registered launcher
  and venue. A delegated go authorizes exactly the named runs, once: it
  does not carry over to resumes (a crash-resume needs a fresh go),
  re-launches, retries that change venue or recipe, or any later wave.
  No automation may launch, extend, or re-launch training on its own;
  scheduled or unattended training loops remain out of scope for MVM
  entirely until this document is revised to address them. Kill
  authority is untouched by delegation: John (and the registered
  watchdog/deadline machinery) may kill any run at any time, and Claude
  may kill but never restart.
- **C3 — Every run can be killed, and the kill switch is never load-bearing
  for the science.** All cloud runs launch with a hard terminate
  (`--terminate-after`); local runs are foreground processes. No
  experiment design may make "the run was stopped early" unrecoverable or
  penalize stopping — the RT-07 checkpoint schedule already treats any
  checkpoint as readable, and that property is now a commitment, not a
  convenience.
- **C4 — No stakes term may ever reward continuation.** In any future
  design under §What this gates, reward may not be conditioned on the
  training or evaluation process continuing to run, on avoiding
  termination, or on the state of the termination machinery. A proposed
  stakes term that cannot be written without that property is a design
  rejected by this document.
- **C5 — Optimization against the instruments halts the run.** If a model
  under training is observed to exploit, degrade, or evade the evaluation
  or monitoring machinery (judges, gates, probes), the run halts and the
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
