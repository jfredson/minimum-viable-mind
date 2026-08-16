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
