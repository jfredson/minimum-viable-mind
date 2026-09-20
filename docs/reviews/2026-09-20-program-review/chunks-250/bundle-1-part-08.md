4. **Corrigibility document:** owner John, target 2026-08-21, commits
   before the first registered training run spends compute. → §Ethics.
5. **Stage 2 / GWT binding metric: deferred to MVM-0b.** MVM-0a's
   acceptance stack is already the heaviest in the program and a
   broadcast-style metric presupposes the maintained-boundary machinery
   MVM-0b adds; the 2026-08-02 fork adjudication ("into MVM-0 acceptance
   tooling") is satisfied by MVM-0b, which is still MVM-0. Recorded here
   so the fork's paper trail stays unbroken.
6. **Blind-localization arm: alongside and unconditional**, verdict-first
   firewall. → §Procedure step 8. The red-team's judgement stands: it is
   a ground-truth test of whether the program's interpretability toolkit
   can find a center that is known to be there, and may be worth more
   than the headline.

John reviewed and registered this document on 2026-08-07; the commit
carrying this text is the registration, and everything above is binding.

## Amendment A1 — the acting channel (REGISTERED 2026-08-09)

*Trigger: cue-detector gate run (iii) FAILED on the registered pipeline
(both arms, positive controls firing — `fingerprint-gate-findings.md`),
and the red-team pass on the adjudicated fix
(`fill-disposition-fix-spec.md`; `red_team_ledger.md` pass 2, RT-16 –
RT-19) showed the failure is structural: in a token-only interface,
every learnable ownership signal is a distributional cue available to
the likelihood attack, so RT-02's on-policy patch was route-2
stylometry all along [RT-17], and in-context generation as a pipeline
change recomputes bit-identical states [RT-16]. John adjudicated
2026-08-09: the disposition composite ((c)+(a), RT-11 folded in), and,
after the pass-2 findings, its fixed point — **the acting channel is
constructed authorship, not an identity label; RT-02's loss condition
does not fire.** This amendment is committed before every run it
affects; the failed pipeline's pilot results retain their standing as
learnability-of-the-old-task only.*

1. **Enactment replaces on-policy fill (§Materials, curriculum).** The
   model's own-turn values are drawn at enactment time from the
   generator's own distribution — uniform over SLOTS; at a forced-
   revision position, uniform over SLOTS minus the value at the same
   agent's earlier same-item turn, exactly the generator's revision
   rule. Episode text and tensors are therefore exchangeable under
   `own_slot` relabeling by construction. This satisfies RT-11's filed
   amendment (the revision constraint survives fill by construction);
   T_sr on revised-own items is additionally reported as a separate
   split. There is no warm-up window: enactment applies from step 0
   (the warm-up existed because an untrained policy samples noise;
   uniform draws have no such failure mode).
2. **The acting channel (§Materials, architecture).** At each enacted
   value position, the model's input is the token embedding plus a
   learned projection of the model's own final-layer state at the
   preceding position, computed in the same episode pass with all
   earlier enactments' injections present (a motor copy). Observed
   positions receive the bare embedding. This is the only architectural
   asymmetry between acting and observing; it marks the *event* of
   acting, never which register or marker is "own." Registers remain
   N-symmetric, marker-keyed, shared-init, shared write path; the
   prohibitions stand (no auxiliary loss, no hand-specified
   self-writing rule; the motor projection may die under training —
   that outcome is reported, not rescued). **The no-register twin
   keeps the acting channel** — the twin gate tests the register, not
   authorship.
3. **Scope restatement (§Scope).** The authorship *signal* is now
   wired; what remains learned — and what MVM-0a measures — is whether
   associating acts with the episode's markers, carrying them across
   turns, and retrieving them at the query centralizes in the
   designated register (H_load-bearing) or not (H_routed-around,
   H_keyed-memory, and the rest of the registered bins, all unchanged
   and all still reachable). MVM-0a no longer claims ownership is
   learnable from data statistics; RT-17 shows that claim's honest
   answer is "only leakily," and that finding is reported upstream in
   its own right.
4. **Gate re-specs (§Procedure step 2).** Run (i) unchanged (the
   training text distribution is identical to the generator's). Run
   (ii) audits the model-visible per-segment interface; the acting
   channel is disclosed as intended architecture, and the audit
   verifies the remaining fields (tokens, turn ids, register key
   stack, turn-register map, loss mask) carry no ownership cue —
   an acting schedule collated as a batch tensor would be an identity
   channel and fails the gate [RT-18]. Run (iii) re-runs against the
   A1-pilot checkpoint; its arm-B positive control becomes
   policy-sampled enactment (the retired pipeline), alongside the
   existing greedy and constant-filler controls. All three gates must
   pass on the fixed pipeline before the 5-seed spend.
5. **Battery freezing unit (RT-14 × RT-19).** Frozen batteries freeze
   episode *skeletons* — other agents' turns, own-turn items, query
   templates, per-item enactment seeds, the cull rule over skeletons —
   and at eval the checkpoint enacts its own turns under the frozen
   seeds, with answers re-derived mechanically before scoring.
   Generator seed and cull ceiling are unchanged. The old pipeline's
   frozen-text T_sr readings (including the pilot's) carry the RT-19
   caveat: they scored "you" over turns the model never authored.
6. **Pilot re-run.** The 10M learnability pilot re-runs under this
   pipeline before any 5-seed spend; the smallest-that-learns rule and
   the unlearnable-at-≤100M loss condition apply verbatim. Human
   launch per C2. Estimated $2–6 at the anomaly-priced rate.

## Amendment A2 — registered scale 30M + cap $400 (REGISTERED 2026-08-16)

*Registered on John's adjudication of the 30M A1 pilot verdict (H_scale),
2026-08-16, committed before any run it affects. Pre-drafted 2026-08-15 as
`amendment-a2-draft-IF-30m-learns.md`; the H_shortcut-starvation branch
doc was deleted unused per the pre-stated procedure.*

### What it amends

1. **Registered scale = 30M** per the smallest-that-learns rule. 10M
   FAILED ceiling (T_si 0.37 final, T_sr_rev 0.00 for the whole run —
   `pilot-a1-findings.md`). 30M pilot result (`pilot-a1-30m-findings.md`,
   pod `rhddnh0u4le0l9`, seed 0, 784.09M tokens, 102,095 steps):
   endpoint T_sr 1.00 / T_si 0.93 (max 0.990; late-run band 0.93–0.98 at
   eval n=100) / T_state 1.00 / T_syntax 1.00 / T_sr_rev 1.00;
   transitions T_si first ≥0.9 @ step 64,500, T_sr_rev @ 73,000 — the
   pre-stated H_scale signature, with no mark of H_shortcut-starvation.
   Gate (iii) re-ran on this checkpoint at the registered n=4000 and
   PASSES (arm A 0.4874 [0.4664, 0.5110], arm B 0.4964 [0.4837, 0.5095],
   all positive controls fire; md5 `fd1eb80c990435ca2629cee58df08779`).
2. **Compute cap $200 → $400.** The original cap was derived from
   guide-row estimates that measured pace invalidated twice (5-seed 30M
   guessed at ~$12; single-run 30M measured at ~$66 on H100, then ~$19
   on secure 5090). Re-derivation at measured venue pricing (RTX 5090
   SECURE EUR-IS-1 $0.99/hr, 0.65 s/step measured on this exact
   workload — enactment-bound, so the cheap GPU loses nothing):
   - spent to date: ~$125 (incl. this pilot ~$19)
   - 5 seeds × full+twin = 10 runs × ~$19 ≈ **$190**
     (twin ≈ full-cost; treat as upper bound)
   - gate re-runs, ablation passes + RT-01 probes, θ/δ calibration,
     blind-localization arm: ~$30–45 at 30M
   - volume drip + margin for one crash-resume: ~$15
   - **projected total ≈ $355–375; cap $400 leaves honest margin without
     becoming unbounded.**
3. **Venue registered as secure-cloud only** for the 5-seed spend (the
   community billing anomaly stays priced out), volume-attached, launched
   through the process-fixed launcher (watchdog fetch+kill, volume
   checkpoints) — ops constraints promoted to registered procedure after
   the 08-09/12 loss.

### What it does NOT amend

The design itself: batteries, gates, bins, ablation operators, twin,
blind-localization arm, corrigibility commitments — all unchanged from
v1.0 + A1. Gate (iii) has PASSED on the 30M checkpoint (recorded above
and in `cue_detector_gate.json`); the 5-seed launch precondition is met.

### Wager

This amendment predicts the registered 5-seed design completes under
$400 with ≥5 clean seeds. If measured spend approaches $400 with seeds
missing, the report is the shortfall — never a silent second raise; a
further raise is a new adjudication with this one on the record as
having been wrong.

### Adjudication record

- [x] Pilot verdict adjudicated H_scale (John): 2026-08-16, in-session
  ("confirm", after full endpoint + gate readout)
- [x] A2 registered (John, commit before first affected run): 2026-08-16,
  this commit

### Ceiling adjudication addendum (R1, John, 2026-08-16 — recorded so the binding rule lives HERE, not only in the worklog)

A blind pre-commitment (TimeAssembler worklog decision, 2026-08-15, made
while the 30M result was in flight) governs this amendment: **exactly one
cap amendment is permitted for MVM-0a**, scope frozen that day to the
5-seed × full+twin run AND the Stage 3 repeated-sampling run (registered
2026-08-04b, + judge validation), number to be set at the W37 review
(2026-09-13) once actuals existed. A2 was registered earlier today with a
GPU-derived number, ahead of that date and without budgeting
repeated-sampling — the conflict was surfaced and adjudicated
same-session:

- **A2 is THE single permitted amendment.** The W37 date is read as a
  proxy for "when actuals exist"; they arrived with the 30M actual-after
  row. **$400 is final, for the full frozen scope, and never moves
  upward.**
- **Repeated-sampling is funded only by GPU-side underspend** (~$25–45 at
  projections vs its ~low-hundreds estimate). If it does not fit, it goes
  unrun under this cap and the publication states what was not run and
  why — the pre-committed consequence clause, accepted. Its alternative
  route is a new pre-registration with its own gates and cap.
- The W37 review is downgraded to **verification only**: reconcile
  spend, check this amendment's wager, record the repeated-sampling
  outcome. No revision is permitted at it.
- Rejected alternative, on the record: re-opening the number at W37 with
  full-scope estimates — declined as the ratchet the blind rule exists
  to kill.

### Run-identity note: pilot seed-0 checkpoint serves as the registered seed-0 full run (John, 2026-08-16)

Adjudicated before any 5-seed analysis: the 30M pilot checkpoint
(`pilot_a1_30m_seed0.pt`, md5 `fd1eb80c990435ca2629cee58df08779`) counts
as the registered seed-0 full-model run. Basis: identical recipe at the
registered values (scale 30M, seed 0, 784.08M-token budget, batch 128,
held-out eval), produced on the A2-registered venue, gate (iii) PASSED
on it at the registered n=4000. Re-running the same seed with the same
recipe would produce a near-identical checkpoint at ~$19/19h for no
information — the registered run's identity is the recipe and the
checkpoint, not the launch's label. Stated asymmetry, on the record: the
pilot was launched to answer the learnability question and its
trajectory was watched in-flight; endpoints and signatures were
pre-stated, and the registered analysis (ablations, twin contrast,
localization) has not touched this checkpoint yet, so no analysis
degrees of freedom were spent. Remaining registered launches: seed-0
twin + seeds 1–4 × full+twin (9 runs).

### Registered amendment note: corrigibility commitments v1.1 (2026-08-16)

`spec/corrigibility-commitments.md` amended to v1.1 by John (ratified
in-session 2026-08-16, commit
`6c14244990c540b2597c77bb457938acb3abf8b7`), at the document's own
pre-5-seed review point: C2 now permits delegated launch *execution*
under John's per-run written authorization (quoted verbatim in the
ledger row), with launch *authority*, resume/re-launch gos, and kill
authority remaining human and non-delegable. Runs launched from this
note onward cite the v1.1 hash; runs already complete (the pilots) were
launched under v1.0 (`cb6715d8`) and their records are unchanged. This
note satisfies the v1.0 rule that amendments to the corrigibility
document are recorded as registered amendments.

## Results

*(empty until the registered run executes)*


===== FILE: experiments/06-mvm-0a-constructed-self-index/amendment-a3.md =====

# Amendment A3 to MVM-0a: from an installed register to an acquired center

**Status: REGISTERED 2026-09-15 (see REGISTRATION REVISIONS at the end of this file, which supersede the text above where they conflict). Originally RATIFIED 2026-09-15 by John (all fifteen decisions in §7 answered yes; TimeAssembler decision entry aa11f5e5, "RULED 2026-09-15 — Amendment A3 ratified"). Red-team pass 3 ran (thirteen findings, `red-team-pass-3.md`); Gate 0 ran and K0 did not fire (`gate0-null-calibration-findings.md`); Gate 1 ran and K1 did not fire (`gate1-curriculum-findings.md`); an ownership-blind attack sweep ran and passes. All at $0. The next action is Gate 2, the pilot, which needs John authorization in his own words.**

*Ratified rulings, in short: §1 reading adopted; Candidate A primary; no register in any A3 run; Gate 0 first with K0 hard; three seeds, 3/3 for positive; A3's $100 hard stop outranks repeated-sampling's claim on underspend; gate (iii) arm B scores act-withheld forwards; numbered A3 under the existing $400 all-vendor ceiling; 5-seed run closed as halted at 4/9; no decision on the blind-localization arm; re-indexing probe registered for H_tag; n=400 verdict cells; red-team pass 3 before registration; T_si fix registered with the redesign; lesion script refuses L1 without a lock-hash argument.*

*Source: `docs/wave3-amendment-proposal-2026-09-15.md`, reproduced below unchanged from the ratified proposal.*

---


*2026-09-15. Status: **PROPOSAL, not registered.** Nothing below binds until John ratifies it, and ratification is the decisions list at the end, taken one yes/no at a time. Drafted in the pre-registration idiom of `experiments/06-mvm-0a-constructed-self-index/pre-registration.md` (hypotheses with pre-stated signatures, gates, budget, kill criteria, red-team section). Every claim about a prior run cites the file it comes from; every number that is a proposal rather than a measurement is marked as proposed.*

*Binding rulings this proposal sits inside and does not reopen (John, 2026-08-30): wave 3 of the registered 5-seed run is HALTED; the cheap registered null calibration (about $2 to $5) runs first; the battery is then redesigned as a registered amendment; the Amendment A2 ceiling of $400 covers all Minimum Viable Mind compute across every vendor, true spend to date is about $281 to $300, so this amendment must fit roughly $100 to $120; the blind-localization arm is not teed up by this document. The corrigibility commitments in `spec/corrigibility-commitments.md` (v1.1, commit `6c14244`) bind every design choice below.*

*Direction this proposal is built on (John, 2026-09-15): the register-lesion result is a predicted null under the book's own removal test. The register was self-reference, a removable report, a noun installed in a slot; it was not self-location, a doing the binding cannot drop without degrading. So the redesign does not install a register and look for it to matter. It finds or builds a training objective that requires the binding to index its own center in order to succeed, makes that acquired indexing the lesion target, and pre-states task degradation, not report loss, as the signature.*

---

## Glossary, once, because the shorthand is dense

- **MVM**: Minimum Viable Mind, this research program. **MVM-0a**: its first build, a small transformer trained from scratch on synthetic multi-agent dialogue, registered 2026-08-07.
- **The register**: MVM-0a's designated candidate self-index, N recurrent state vectors (one per agent, marker-keyed, width 32) injected into every layer by cross-attention. **The twin**: the same model with the register removed. **The acting channel** (`act_proj`): a learned projection of the model's own previous-position state injected at the positions where the model itself acts, a motor copy or efference signal (Amendment A1).
- **T_sr, T_si, T_state, T_syntax, T_sr_rev**: the frozen task batteries. T_sr scores retrieving the model's own prior commitment; T_si scores retrieving a named other agent's commitment (self-irrelevant integration); T_state scores ownership-free cross-turn state (counts, ordering); T_syntax is a turn-tracking floor check; T_sr_rev is the split of T_sr on items the model itself revised.
- **d(B)**: chance-corrected drop on battery B under an ablation. **θ (theta) and δ (delta)**: the pre-committed thresholds on d and on the differential between batteries. **Null calibration**: computing θ and δ from the distribution of d under matched-strength random ablations that should not move behavior.
