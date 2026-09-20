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

