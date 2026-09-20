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
- **RT-nn**: a numbered red-team finding in `red_team_ledger.md`. **C1 to C7**: the seven corrigibility commitments. **A1, A2**: the registered amendments of 2026-08-09 and 2026-08-16. **R1**: the ceiling adjudication addendum of 2026-08-16.
- **Gate (i), (ii), (iii)**: the three cue-detector runs (curriculum text, input tensors, post-training rollouts) that certify no surface cue predicts which turns are the model's own. **Arm A / arm B** of gate (iii): a text classifier on enacted text, and a likelihood attack scoring turn values under the model's own policy. **AUC**: area under the receiver operating curve, 0.5 is chance.
- **OOD**: out of distribution. **NLL**: negative log-likelihood. **CE**: cross-entropy loss. **CI**: confidence interval. **SAE**: sparse autoencoder.
- **Experiment 1**: the self-indexing removal test on a stock 8B instruction-tuned model (`experiments/01-self-indexing-removal-test/`). **Q1** and **Q5**: the roadmap questions "is self-binding absent or present-but-uncarvable?" and "can a self-index be constructed to be load-bearing?" (`ROADMAP-post-removal-test.md` Part 2).
- **J-space**: the "Jacobian lens" workspace reported by Anthropic in July 2026, a sparse set of verbalizable directions that behave as a global workspace and that post-training causes to acquire the Assistant's point of view (`calibration-problem/explorations/comparisons/2026-07-08-anthropic-jspace-global-workspace.md`).
- **ch05**: `calibration-problem/ch05-consciousness-as-assembled-time.md`, cited by section title.

---

## 1. What the register-lesion result means under the removal test

> **ANNOTATION, 2026-09-16 (John's ruling; decidedBy john). Nothing in
> this section is edited and no registered text is changed — no grammar,
> battery, bin, kill criterion or spending cap is touched. What follows is
> a dated note beside §1, recording that its central reading is
> withdrawn.**
>
> John's ruling: *"the reading that the register-lesion null showed
> 'self-reference, not self-location' is withdrawn. A constant vector was
> neither, and the lesion null is uninformative about the removal test."*
>
> **The original wording, quoted so the withdrawal is checkable.** The
> direction this proposal was built on, at the head of this document:
> *"The register was self-reference, a removable report, a noun installed
> in a slot; it was not self-location, a doing the binding cannot drop
> without degrading."* And in §1 below: *"By the book's own criterion the
> register 'was a description all along,' and in fact something weaker
> than a description, since nothing downstream even read it. It was a noun
> installed in a slot."*
>
> **What was measured on 2026-09-16.** The register in every trained
> register-bearing checkpoint is a **constant**. Its writer emits the same
> vector whatever it is given, from the first write, at the floating-point
> floor: across-episode spread 7.6 × 10⁻⁸ on seed-0 full, 2.8 × 10⁻⁸ on
> seed-1 full, 5.9 × 10⁻⁸ on seed-2 full. A probe at the register's known
> location recovers no own-agent identity at any turn. An untrained model
> at the same configuration does not behave this way, so the constancy is
> trained in rather than architectural.
> (`register-saturation-findings.md`, `register-direct-probe-findings.md`)
>
> **Why that withdraws the reading.** ch05's removal test separates a
> description that can be lopped off from a center that cannot be deleted.
> Both branches presuppose that the thing removed **carries something**. A
> constant carries nothing. It is not a report the system holds about
> itself, because it is identical whoever the system is and whatever
> happened; and it is plainly not a structural feature the act indexes
> itself to. It is a bias term. So it was neither branch, and the lesion
> that removed it was not an instance of the removal test at all. **The
> null is uninformative about that test**, rather than being the test's
> predicted negative result.
>
> **What in §1 survives, and is in fact strengthened.** The paragraph
> "Why the null was predicted rather than merely possible" stands, and its
> own words now read as a literal description of the measurement: the
> register's contents "were never required by any objective", so "a
> designated slot with no pressure on it fills with whatever is cheapest,
> **here a bias**." That was written as an inference. It is now measured.
> What does not survive is the step from there to calling the result
> self-reference under ch05, because a bias is not a description of
> anything.
>
> **A3's design and the pilot result do not depend on the withdrawn
> reading.** Stating that plainly, since it is the question an annotation
> like this one raises:
>
> - A3 is **register-less by construction** (§2.4). It removes nothing
>   that this annotation concerns, and its launcher has no flag that could
>   enable a register.
> - A3's objective was chosen because it **requires ownership to
>   succeed** — the perspectival revision rule — not because the register
>   was judged to be self-reference. The argument for that objective is
>   pressure on the network, and it is unaffected by what the old register
>   turned out to hold.
> - The pilot result is a direct measurement that stands alone: zeroing
>   the acting channel takes the primary battery from **0.506 to 0.182**
>   while the ownership-free batteries hold at 0.999 and 1.000, and across
>   120 content-blind ablations the worst reached 0.2758 against 1.515 for
>   the authorship lesion.
> - §1's closing paragraph, "The one place a doing was load-bearing", also
>   stands. The acting-channel collapse from 0.96 to about 0.16 is a
>   separate measurement on separate runs and owes nothing to the register
>   reading.
>
> **What the withdrawal does cost.** §1 was ratified as "the amendment's
> stated basis" (§Ratification item 1). Its motivating story — an
> installed noun failing the removal test, so build a doing instead — is
> weaker than it read: the installed noun was never even a noun. The
> redesign's justification now rests on the pressure argument and the
> pilot measurement rather than on a clean ch05 verdict about the
> register. That is a smaller claim honestly held, and it is the one the
> evidence supports.

**What was measured.** The pilot seed-0 full model, the only register-bearing run that passed the self batteries, kept every battery score under every lesion of its register: with the cross-attention injection removed entirely, T_si went 0.93 to 0.94 on the registered eval seed and 1.00 to 0.99 on a disjoint replicate, T_sr_rev stayed 1.00, and T_sr, T_state, T_syntax stayed at or above 0.99 (`register-lesion-findings.md`, thread 4 table). The pathway was not dead: removing the injection shifts logits by mean absolute 0.22 and the cross-attention residual norms are large (18 to 275 per block against 3 to 14 for the trunk read). But deranging which register's content is read moves the logits by mean absolute 0.014, so the four registers carry nearly identical content. The findings file's own phrase: "numerically active and informationally inert, a learned bias channel, not an agent-indexed store." Wave 2 had already produced a register-less twin that passed the same batteries at ceiling (T_si 0.96, T_sr_rev 1.00, `twin-binding-anomaly.md`), so no observed binding anywhere in the 30M record is register-dependent.

**What the book's test says about that.** ch05, "The Center That Cannot Be Deleted," draws the line the whole framework rests on: self-reference is "a report the system carries about itself"; self-location is "a structural feature of the binding itself, the act specifying its own center." The test that separates them is removal: "Where binding genuinely indexes its own center, taking the self-location away does not merely silence a report, it degrades the integrated act itself. ... Where a system only represents itself from outside, the same removal subtracts a description and the processing carries on intact. A center is what cannot be deleted without dissolving the integration it centers. A self-model that can be lopped off while the computation proceeds was a description all along."

Read through that sentence, the register lesion is not a surprise. Removal left the processing intact. By the book's own criterion the register "was a description all along," and in fact something weaker than a description, since nothing downstream even read it. It was a noun installed in a slot. The registration anticipated this in §Scope: "the register could be a thing consulted rather than the thing the binding is indexed to," and it recorded that "no result here closes that gap." The gap did not close; it was measured to be the whole distance.

