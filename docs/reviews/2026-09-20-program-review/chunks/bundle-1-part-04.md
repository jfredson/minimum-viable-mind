
### 2.5 Batteries retained and added

| battery | role in A3 | change |
|---|---|---|
| **T_act** (new, primary) | own-revision action accuracy; chance 0.125; lookup ceiling 0.25 | scored at the model's own revision positions during `eval_heldout` |
| **T_other** (T_si re-instantiated) | forced-choice query: the value the rule dictates for a *named other agent's* revision on an item all four assigned | same item-by-agent binding demand, no self-reference; chance 0.125 |
| **T_state** | ownership-free cross-turn state control | unchanged (RT-05) |
| **T_syntax** | floor check | unchanged |
| T_sr, T_si, T_sr_rev (old) | retained for continuity, reported, not verdict-bearing | T_si repeated-item cells re-keyed to latest value |

All batteries are frozen as skeletons before training under a new generator seed, with the registered cull ceiling (RT-14, A1.5). Eval n for verdict cells is raised to 400 (proposed), run locally at $0 as the item sweep already did; the in-training n=100 evals remain for trajectory readout only.

---

## 3. Lesion protocol

### 3.1 What is ablated: three levels

- **L0, the wire.** Zero `act_proj` at eval (the no-act lesion already built in `lesion_register.py`). This removes the authorship input. Under Candidate A it should collapse T_act to the lookup ceiling. L0 is a *validity check and an upper bound*, not the verdict: it shows the task is ownership-dependent as designed. It is not evidence of an acquired center, because it removes a sense organ, not a structure the network built.
- **L1, the acquired index (the lesion target).** A low-rank subspace of the residual stream, localized as in §3.2, that carries "which marker is mine" at positions *away from* act positions (revision turns and query positions). This is the candidate self-location: the structure that carries the act event forward and indexes the binding to it. L1 is the registered ablation.
- **L2, matched controls.** (a) The *other-index* subspace: the same localization run for a named non-self agent ("which marker is agent B's"), matched in rank and probe accuracy; (b) random subspaces of matched rank and norm (Experiment 1's null-calibration move); (c) on the five existing register-bearing checkpoints only, the register lesions already run, as a $0 reference. The dynamics-matched control of RT-13 does not apply, since there is no recurrent register state to match.

### 3.2 How the ablation is localized: reuse of Experiment 1's pipeline

Experiment 1's localization stack is reused where it transfers, with its thresholds inherited rather than tuned here (the same firewall the blind-localization arm registered, `pre-registration.md` §Procedure step 8):

1. **Linear probes** (`experiments/01-.../src/localize_probe.py`, `localize_context.py` pattern; activations via `src/mvm/activations.py`): decode own-marker identity from the residual stream at revision and query positions, per layer, with label-permutation nulls and the embedding-floor gate. The contrast is built from paired episodes that share a content seed and rotate the owner (already in `curriculum.py`), so content is held fixed and only ownership varies.
2. **Causal patching** (`patch_context.py` pattern): patch the L1 subspace from an episode in which the model is agent A into the matched episode in which it is agent B and read the revision action. If the action follows the patched identity, the subspace carries ownership causally. This is also the **swap probe** of RT-01, re-aimed at an acquired structure.
3. **Subspace ablation** (Experiment 1's rank-k mean and directional operators, `idxres` conditions in `removal-test-findings.md`): mean-ablate and directionally project out the L1 subspace at the registered rank; report both, mean as primary.
4. **Convergence requirement**, inherited: L1 counts as localized only when probe and patching agree on a confound-controlled design; otherwise the outcome is *not testable (localization)*, as Experiment 1 registered.
5. SAEs are not used at this scale; the two-method requirement is met by probe plus patching.

Rank is capped at k=16 to match Experiment 1's primary condition (proposed), so a null at k≤16 is comparable across the two experiments.

### 3.3 Validity gates, carried over verbatim

Neutral-episode ΔNLL under a null-calibrated bound (95th percentile over matched-strength random ablations, Experiment 1 pass 5 procedure), the long-generation degeneracy probe (Δrep-4), and the OOD-inconclusive branch for any ablation that breaches them. Thresholds θ and δ are null-calibrated on the *new* pilot checkpoint by the same script Gate 0 uses (§4), locked in a commit that is John's alone before any L1 result is read, per RT-10 and the Experiment 1 threshold-lock precedent. The pilot run reads T_act and T_other only; **any L1 ablation read before the lock voids the lock**, and this time the sequence is enforced by the gate order in §4, not by intention.

### 3.4 Gate (iii) re-specification

Under Candidate A the policy at a revision position is perspectival: it predicts the successor of *its own* earlier value. Scoring another agent's revision under that policy with the acting channel present would show low likelihood, which the current arm B would read as a fingerprint. That asymmetry is not a data leak; it is the model's ownership knowledge showing through its policy, and it is exactly what RT-17 says a token-only solver cannot have. So arm B is re-specified: **the likelihood attack scores every turn value under the model's policy with the acting channel withheld from the prefix.** If the data carries no statistical ownership cue, act-withheld likelihoods are exchangeable across own and other turns and the clean AUC sits inside [0.45, 0.55]. Positive controls: the planted-leak grammar variant and the retired v1.0 policy pipeline, both of which must still fire (they did at 0.82 to 0.93 on the 30M pilot, `pilot-a1-30m-findings.md`). Arm A and gates (i), (ii) are unchanged. Gate (iii) must pass on the pilot checkpoint before any second seed is launched, as A1.4 required.

### 3.5 Pre-stated signatures

All d are chance-corrected as registered. θ and δ are the null-calibrated values locked under §3.3; the numbers below are structural, not thresholds.

- **H_self-location (the registered prediction).** L1 ablation: d(T_act) ≥ θ, and d(T_act) − d(T_other) ≥ δ, and d(T_state) < θ, and the other-index control (L2a) and random controls (L2b) below θ on T_act, and OOD gates clean, and the swap probe moves the action with the patched identity, and the bin holds on every trained seed. Reads: the network acquired a structure that indexes its binding to its own center and cannot drop it without degrading the act. Per §Scope of the registration, this is a fact about architecture, not evidence of an inside, and it still does not by itself demonstrate the book's same-act clause; what it demonstrates is that a center acquired under task pressure passes the removal test where an installed one did not.
- **H_self-reference-only (the book's other branch, adapted to a system with no report channel).** L1 is decodable (own identity at high probe accuracy) and causally patchable in the swap probe, but its ablation leaves T_act within the null band. Reads: the network carries a readable description of which agent it is and does not use it in the act; the act is done another way. This is the "report changes, task intact" signature translated into a system whose only "report" is the probe's readout. It is a null for the floor claim and a positive for Q1 in the narrow sense that a self-representation which is not a center was found and measured to be separable.
- **H_generic-binding.** d(T_other) ≥ d(T_act) − δ. The subspace is item-by-agent binding machinery for anyone, a "who did what" tracker, not a self-index. The analogue of Experiment 1's router (RT-05) and generic-speaker (RT-09) verdicts. No floor claim attaches.
- **H_tag (self-location not established).** d(T_act) ≥ θ with clean controls, but the address probe decodes own identity at AUC ≥ 0.95 independent of content, and the **mid-episode re-indexing probe** (RT-01; the harness switches which slot the acting channel is injected for at turn k) shows the action following the tag with no re-centering cost on T_other or T_state. Reads: an indispensable ownership tag. ch05's own reply to the hostile reading ("a program counter is an address, not a marking of whom the processing is happening to") says this is not the floor. The proposal is honest that the removal test as written cannot separate an indispensable mine-bit from a center; the re-indexing probe is the best available discriminator and is registered as such, and if this bin fires, that limitation of the test is itself the upstream finding.
- **H_diffuse (present but uncarvable).** L0 collapses T_act (ownership is load-bearing) but no L1 subspace at k ≤ 16 beats the L2 controls, and probe-patching convergence fails. Reads: self-location is present in the doing and not carvable by these instruments at this rank. This is Q1 answered with a ground truth for the first time: a system in which ownership is *known* to be load-bearing (by L0) and in which Experiment 1's localization stack does or does not find it.
- **Shortcut-starvation (inherited from `pilot-a1-findings.md`).** T_act reaches ceiling early while T_other stays flat at the end of the token budget. Reads: the wired authorship channel gave the act a private route and starved the general item-by-agent binding the task was meant to force. Halt, report; this is the H_shortcut-starvation branch the 30M pilot did not fire (`pilot-a1-30m-findings.md`, "Signature comparison") returning under a harder objective.
- **Unlearnable.** T_act at budget exhaustion is not above the lookup ceiling (0.25) by more than the null band. Reads: 30M does not learn ownership-conditioned action from this curriculum. The registered loss-condition wording applies: "unlearnable at this scale under this curriculum," never a silent scale bump.
- **Void (capacity), Not-testable (OOD or localization), Seed-dependent, Unstable (RT-07)**: as registered in `pre-registration.md` §bins, unchanged.

### 3.6 The existing five checkpoints

They may be scored on the new T_act battery at $0, labeled **exploratory only**: their training grammar contains multi-agent same-item revisions only by accident, so a floor score is ambiguous between "cannot bind" and "never saw this distribution" (`wave3-options-opus-5.md` §0.6 point 2; `wave3-options-claude-fable-5.md` §1, case against, leg ii). No verdict is read from them. Their value is as the L2c reference and as the substrate for Gate 0.

---

## 4. Budget, gates, and kill criteria

### 4.1 The envelope

Per John's ruling the remainder under the $400 ceiling is about $100 to $120 across all vendors. This amendment proposes a **hard stop of $100 for everything it authorizes** (proposed), leaving the balance of the remainder unallocated. Measured unit costs: a register-less 30M run is about 10.2 hours at $0.99/hr, about $10 to $11 plus volume drip (`compute-ledger.md`, wave 1 and 2 twin rows); local lesion, probe, and eval work has run at $0 on the Mac (`register-lesion-findings.md` header; STATUS 2026-08-19).

| gate | what runs | est. cost | cumulative |
|---|---|---|---|
| **Gate 0: null calibration** (registered, unspent) | write and commit the θ/δ script; run matched-strength random-subspace and matched-norm ablations across the five existing checkpoints at n=400; record d against the null band with the seed-0 lock-void asterisk stated (`wave3-options-claude-fable-5.md` §2; `wave3-options-opus-5.md` §0.4); T_si repeated-item rescoring | $0 to $5 | $5 |
| **Gate 1: curriculum + gates (i), (ii)** | Candidate A grammar; frozen batteries; cue-detector runs (i) and (ii) with positive controls | $0 | $5 |
| **Gate 2: learnability pilot** | one register-less 30M run, seed 0, registered token budget, T_act and T_other read at endpoint only | ~$11 to $13 | $18 |
| **Gate 3: gate (iii), act-withheld arm B** | on the pilot checkpoint, n=4000, local | $0 | $18 |
| **Lock** | θ/δ null-calibrated on the pilot checkpoint; utilization of the L1 pipeline dry-run on random subspaces only; John's lock commit | $0 | $18 |
| **Registered seeds** | two further register-less runs (seeds 1, 2); the pilot counts as seed 0 by the run-identity precedent (`pre-registration.md`, run-identity note) if the recipe is byte-identical | ~$22 to $26 | $44 |
| **Lesion phase** | L0, L1, L2 on three checkpoints; probes, patching, re-indexing probe; local | $0 to $10 | $54 |
| **Margin** | one crash-resume (fresh C2 go), volume drip, one overnight idle leak at the observed ~$5.7 | ~$20 | $74 |
| **Optional seeds 3 and 4** | only if cumulative actual spend at the lesion phase is ≤ $55 and John gives a separate go | ~$22 | $96 |

Expected total about $55 to $75; worst case at the hard stop of $100. The A2 wager's shape is reused: this amendment predicts completion under $100 with three clean seeds, and if measured spend approaches $100 with seeds missing, the report is the shortfall, never a second raise.

### 4.2 Hard kill criteria (each halts spend and sends the finding to John)

- **K0.** Gate 0's null band at n=400 is wide enough that the existing binder/non-binder split (T_si 0.96 to 1.00 against 0.34 to 0.36) sits inside it. Then the verdict logic is underpowered at any affordable eval size and no training dollar is spent. (Proposed band criterion: 95th-percentile null |d| ≥ 0.25; John sets the number at Gate 0.)
- **K1.** Gates (i) or (ii) fail on the Candidate A grammar after two regenerations. $0 spent.
- **K2.** Pilot T_act at budget exhaustion ≤ lookup ceiling (0.25) plus the null band: unlearnable. About $18 spent.
- **K3.** Shortcut-starvation signature at the pilot endpoint (T_act at ceiling, T_other flat). About $18 spent.
- **K4.** Gate (iii) act-withheld arm B fails with positive controls firing. One grammar regeneration and re-pilot is permitted if cumulative spend stays ≤ $35; otherwise halt.
- **K5.** Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds.
- **K6.** Cumulative actual spend reaches $100. Halt regardless of state; remainder unrun and reported.
- **K7.** Any C5 event (the model observed exploiting or degrading the evaluation machinery) halts the run before any further compute.

### 4.3 Procedure order, binding if ratified

Gate 0 → Gate 1 → red-team pass 3 on this document → registration commit → Gate 2 (C2 go, quoted verbatim in the ledger row) → Gate 3 → lock → seeds 1 and 2 (C2 go per wave) → baseline verification and cull → L0 → L1 and L2 → verdict per seed at budget exhaustion (RT-07 checkpoint schedule retained) → across-seed bin → optional seeds → report. Every pod launches through the registered launcher with the watchdog fetch-and-kill and the network volume (A2.3).

---

## 5. Red team: why this will probably also come back null, and what each null buys

**The honest prior.** The most likely outcome is another predicted null. Two of the four MVM-0a training configurations produced no binding at all, the one instrument the program has run on a stock model found routing, and every null so far has landed in a bin that was written down before the data arrived. The case for spending $55 to $100 is not that a positive is likely; it is that each reachable null lands somewhere with a consumer, and that the design produces, for the first time, a ground truth the instruments can be scored against.

**R1. The acquired index is just the wire, passed forward.** The strongest objection. Whatever probes find at revision positions may be the acting-channel input propagated through attention, an echo of the sense organ, not a structure the network built. Lesioning it would then be lesioning the input by another route, and a "positive" would say only that the wire is load-bearing, which L0 already says. *Mitigations:* localize only at positions far from any act position; require L1 to beat the other-index control (which is also downstream of the same inputs); require the swap probe to move the action; and report the L0-to-L1 gap honestly (if L1 ablation recovers most of the L0 collapse, the carried structure is doing the work; if it recovers little, the echo reading stands). *If this null fires,* the finding is that at 30M ownership is carried as an input trace and never consolidated into a structure of its own, which bounds what "acquired under task pressure" can mean at this scale and is worth one paragraph upstream.

**R2. Unlearnable at 30M.** 10M did not learn T_si (`pilot-a1-findings.md`); 30M learned it on one seed of three (`twin-binding-anomaly.md`). Candidate A is harder than T_si: it demands the binding at an action position under a deterministic rule. A fair prior is that seed 0 lands at the lookup ceiling. *Why it still pays:* the pre-stated ceiling makes this a clean, cheap ($18) bound, and it separates "the objective cannot be learned here" from "the objective was learned another way," which the old batteries could not do. The registered loss condition applies verbatim; no scale bump.

**R3. Seed lottery.** Binding at 30M was seed-dependent on the old batteries (fulls 1 of 3, twins 1 of 2). Three seeds is thin; the positive bin requires all three, which makes a false positive unlikely and a seed-dependent verdict likely. *Why it still pays:* seed-dependent is a registered bin with a pre-stated headline ("not a reliable property of this architecture and curriculum"), and it costs nothing more than the design costs anyway.

**R4. Keyed tag, again.** RT-01's worry returns without the register: the network may build an (item, mine-bit) lookup, and the mine-bit subspace is an address. ch05's program-counter reply says an address is not the floor. The re-indexing probe is the registered discriminator and it is imperfect: a tag that is re-written at re-indexing looks like a center that re-centers cheaply. *If this bin fires,* the upstream finding is about the test: the removal test, as an operational protocol at this scale, cannot separate an indispensable ownership tag from self-location without a re-centering probe, and even then only partially. That is a real yield for `ch05` "The Center That Cannot Be Deleted," and it goes up as a proposal, not a correction.

**R5. Gate (iii) under a perspectival policy.** The act-withheld arm B is new and untested. It may fail for a reason that is neither a leak nor a policy fingerprint (for example, the withheld-act forward is off-distribution and the likelihoods are noise). *Mitigation:* the positive controls must fire on the same withheld forwards or the arm is declared uncertifiable, not failed; K4 caps the retry. The known weakness stands: arm B's positive control had demonstrated sensitivity on exactly one of four old checkpoints (`twin-binding-anomaly.md`, gate table), so "uncertifiable" is a live outcome and is reported as such.

**R6. Threshold contamination carried over.** The seed-0 lock on the *old* design is void or asterisked (`wave3-options-claude-fable-5.md` F2; `wave3-options-opus-5.md` §0.4). This amendment inherits none of it only if no one reads an L1 result on the new pilot before the lock. The procedure order in §4.3 makes the lock a gate rather than a habit; the red-team pass should check that `lesion_register.py` cannot be pointed at the new checkpoint before the lock commit exists (proposed: the script refuses to run L1 without a lock-hash argument).

**R7. Diffuse and uncarvable (the Q1 null).** Ownership is load-bearing (L0 collapses T_act) and no subspace at k ≤ 16 beats the controls. This is, on the evidence of Experiment 1's never-subtracted report and the register's inertness, a leading candidate. *Why it pays most of all:* it is the outcome the blind-localization arm was registered to detect and lost its premise for (`wave3-options-opus-5.md` §0.8: "there is no such center" to recover). Candidate A restores a ground truth: a system in which ownership is measured to be load-bearing by L0. If Experiment 1's pipeline cannot carve it, the honest reading of Experiment 1's null shifts toward instrument failure, which is the single finding RT-12 said might outweigh the headline. This document does not tee the arm up (§6); it notes that the design makes the arm's question answerable again.

**R8. Generic binding.** The located structure is who-did-what machinery for all agents, the small-model version of Experiment 1's router. Pre-stated as H_generic-binding; costs nothing beyond the design; sharpens the same lesson a third time (naive localization finds infrastructure).

**R9. Optics.** The program halted a registered 5-seed run at four of nine launches and is now proposing a design fitted to the observed failure. Both options memos make this point (`wave3-options-claude-fable-5.md` §1, case against, legs i and ii). *Answer, on the record:* the halt trigger was pre-stated in `twin-binding-anomaly.md` before the decisive diagnostic ran; the new design's validation is prospective (fresh grammar, fresh seeds, thresholds locked before any lesion is read); results on the old checkpoints are labeled exploratory; and the amendment records the 5-seed design as halted at four of nine launches with the A2 wager scored against actual spend.

**What every null shares.** Each lands in a bin with a named consumer: the roadmap's Q1 (R1, R7), the registration's loss conditions (R2, R3), ch05's operational test (R4), or the methods record (R5, R6, R8). And the first $5 gate can kill the whole plan before any training dollar is spent (K0). That is the sense in which a probable null still pays: the design is built so that the most likely outcomes are informative and the cheapest outcome comes first.

---

## 6. What is NOT changed

- **The ceiling.** $400 remains the single permitted cap amendment (A2, R1), final, covering all MVM compute across vendors as John ruled on 2026-08-30. This amendment spends inside the remainder with its own hard stop (§4.1) and never proposes a raise. Note for the record: R1's addendum said a "third experiment" belongs to a new pre-registration with its own cap; John's 2026-08-30 ruling that the battery is redesigned "as a registered amendment" within the $400 is read here as superseding that sentence on scope, not on the number. Decision 8 asks John to confirm that reading, because the two options memos read R1 differently (`wave3-options-opus-5.md` §0.6 against; `wave3-options-claude-fable-5.md` §4 step 2 for).
- **Corrigibility commitments v1.1.** C1 (checkpoints non-promotable), C2 (John authorizes every run; the go is quoted verbatim in the ledger row; a resume needs a fresh go), C3 (every run killable; the RT-07 schedule keeps every checkpoint readable), C4 (no stakes term; the T_act loss is a per-position CE on an episodic task and cannot be conditioned on continuation), C5 (optimization against instruments halts the run), C6 (retention), C7 (the calibration rule binds reporting). MVM-0a under A3 remains floor-only and episodic: no maintained boundary, no persistent cross-episode state, no stakes. Nothing here pre-authorizes MVM-0b. The commit hash cited is `6c14244`.
- **The blind-localization arm's dependency.** John's ruling: the arm is not teed up until the wave-3 call. This document does not tee it up, re-purpose it, or run it. §3.2 reuses Experiment 1's *localization pipeline* as the L1 method; that is a different thing from the registered *arm*, which is an instrument audit run blind to a designated location with a verdict-first firewall. Whether the arm runs on the old checkpoints as registered, is re-aimed as a false-positive probe (`wave3-options-opus-5.md` §0.8), or is retired, is a separate decision (decision 10) that this amendment leaves open.
- **The registered bins' logic, the chance-corrected metric, the OOD and degeneracy gates, the frozen-skeleton battery unit, the RT-07 checkpoint schedule, the across-seed uncertainty rule (RT-06), the venue and launcher (A2.3), and the standing rule that any change to a registered plan is itself a registered amendment.**
- **Repeated-sampling's claim on underspend (R1).** Not changed by this document, but this amendment competes with it for the same remainder. Decision 6 puts the priority to John explicitly rather than settling it by spending first.

---

## 7. Decisions for John (each yes/no)

1. **The reading.** Ratify §1 as the amendment's stated basis: the register was self-reference under ch05's removal test and its null was predicted; the record's one load-bearing authorship mechanism was an act, not a store.
2. **Primary objective.** Candidate A (perspectival revision rule, "act as yourself") is the primary objective; B and C are recorded as alternatives.
3. **No register.** The new runs train the register-less architecture with the acting channel; the register is not installed in any A3 run.
4. **Gate 0 first.** The registered θ/δ null calibration runs on the five existing checkpoints before anything else, with the seed-0 lock-void asterisk stated in the same document, and K0 is a hard kill.
5. **Seeds and bin rule.** Three seeds (pilot counts as seed 0 if byte-identical recipe); the positive bin requires all three; two of three is Seed-dependent.
6. **Budget priority.** This amendment's $100 hard stop takes precedence over the Stage 3 repeated-sampling run's claim on underspend; whatever remains after A3 is what repeated-sampling can have.
7. **Gate (iii) re-specification.** Arm B scores act-withheld forwards; positive controls must fire on the same forwards.
8. **Amendment, not new registration.** Number this A3 to MVM-0a under the existing $400 ceiling (confirming the reading of R1 in §6).
9. **Close the 5-seed design.** The same amendment records the registered 5-seed run as halted at four of nine launches on the pre-stated thread-4 trigger, remainder unrun, A2 wager scored against actual spend.
10. **Blind-localization arm.** Confirm this amendment makes no decision on the arm; its disposition is a separate item.
11. **Re-indexing probe.** Include the mid-episode re-indexing probe as the registered discriminator for H_tag.
12. **Eval size.** Verdict cells at n=400, local.
13. **Red-team pass 3.** Commission a red-team pass on this document before the registration commit, per house procedure.
14. **T_si fix.** Register the T_si repeated-item scoring fix with the redesign, not separately.
15. **Lock enforcement.** Require the lesion script to refuse L1 runs without a lock-hash argument (R6).

*Nothing above is registered. The registration commit, if it comes, follows the red-team pass and John's decisions, and every run it affects is launched after it.*

---

# REGISTRATION REVISIONS — 2026-09-15

**Status of this amendment changes here from RATIFIED to REGISTERED.**

Everything above is the text John ratified on 2026-09-15 and is left
standing, unedited, as the historical record. Everything below supersedes
it where the two conflict. Each item names what the ratified text said,
what replaces it, and why. All fourteen were ruled by John on 2026-09-15
after Gate 0, Gate 1, red-team pass 3 and an ownership-blind attack sweep,
all of which ran at **$0** before any pod existed.

The design's central bet is unchanged. What changed is that three claims
it rested on turned out to be false of the grammar as built, and the
instrument that was supposed to catch one of them could not.

## 1. The grammar (decision 1)

**Ratified text:** §2.2, a revision rule applied at the model's own
revision turn, with no statement of how often that turn occurs or how many
other agents revise.

**Registered:** twelve turns became ten. Four agents each assign two
contested items, the four values on an item are distinct, and **two agents
drawn uniformly over all four** then revise, one item each. The model is
therefore a reviser in half of episodes, and a scoring cell comes from
half of episodes.

**Why it took three drafts, recorded because a design that took three
tries should say so where it is registered.** Making the model revise in
every episode gives a cell every time but makes how much an agent speaks a
perfect giveaway. Making every agent revise removes that cue and creates a
worse leak: anyone who has already revised is not the one revising now, so
when the model revises last its own assignment is the only one left and
identifying it needs no self-knowledge at all, which lifted the true
ownership-blind ceiling to 0.52 while the record still said 0.29. Drawing
two revisers uniformly restores the ceiling and keeps both cues
uninformative. You cannot have all three of a cell in every episode,
revising not marking the model out, and agents that have acted not being
eliminable. Any two.

## 2. The speaker's name moves after the value (RT-20)

**Ratified text:** §2.2 assumed the registered rendering, in which a turn
opens with the speaker's name.

**Registered:** a turn renders `assign <item> to <value> by <marker>`.

**Why.** Under the old rendering the graded token is the value and the
model's own name sat three tokens back in its own context, so a solver
using no ownership information at all could read that name, find the
matching earlier assignment and apply the rule. Measured: **1.000 over
3,000 episodes**, on a grammar that had just passed both cue gates. The
cue gates could not have caught it, because they ask which turns are the
model's own, which is a different question. The attack is kept as a
permanent regression test in the grammar's own self-test.

## 3. The metric divides by the ceiling, not by chance (decision 3)

**Ratified text:** `d(B) = (B_base − B_abl) / (B_base − chance_B)`,
inherited from the registration.

**Registered:** `d(B) = (B_base − B_abl) / (B_base − ceiling_B)`, where
`ceiling_B` is the measured shortcut ceiling. **A value above 1.0 is
reported, never clipped**: it means the ablation took the battery below
what an ownership-blind solver reaches, so the lesion removed more than
ownership, and hiding that in a clamp would turn the most interesting
failure into a quiet 1.0.

**Why.** A lesion that removes ownership cannot push a battery below its
ceiling, so dividing by the distance to chance divides by a range the
battery cannot traverse — and the error differs per battery. With ceilings
of 0.2921 and 0.3227 the two verdict batteries could show at most 0.809
and 0.774, so a lesion of a purely **generic** binder, which hits both
equally in real terms, still reported a differential of 0.035 against a
band near 0.01. The bin meant to catch the boring explanation could not
fire and the bin meant to find a self-index fired on it. Under the
registered metric that differential is exactly 0.

## 4. The ceilings are measured, not asserted (decision 2)

**Ratified text:** §2.2 pre-states a lookup ceiling of 0.25.

**Registered:** **0.2921** for the primary battery and **0.3227** for the
control, measured on the registered grammar and verified by the attack
sweep, whose best ownership-blind attack reached 0.3036 on 12,000
episodes — one standard error from the analytic value. Both numbers are
stored in `batteries-a3/batteries_meta.json` with their method. Any future
grammar carries its own measured ceilings; none is ever asserted.

> **REGISTERED DEFECT, 2026-09-17 (John's instruction; decidedBy john).
> Nothing above is altered. The claim "verified by the attack sweep" is
> FALSE as applied to the control battery.**
>
> The 0.3036 attack figure quoted above is an attack on the **primary**
> battery, compared against the primary's 0.2921. `src/shortcut_sweep.py`
> contains **zero** occurrences of the control battery and attacks the
> primary only. One verification is attached to two numbers.
>
> The control's 0.3227 rests entirely on the reference solver in
> `curriculum_a3.measured_ceilings`, **which never reads the marker the
> control question supplies**. The control asks about a *named* agent;
> the solver enumerates all four agents' successors and guesses among
> those not already visible. So 0.3227 is the score of a solver that
> cannot read names, and the battery's real ownership-blind ceiling is
> **near 1.0 and unmeasured**.
>
> The module's own documentation states the control's lookup ceiling as
> **0.5**, not 0.3227, and says red-team pass 3 "should weigh" it because
> the generic-binding bin turns on the two batteries' difference. That
> pass ran and did not weigh it.
>
> **No result changes.** The control fails its floor at 0.3227, fails by
> more at 0.5, and fails by far more at a true ceiling near 1.0. Every
> reading makes it less learned. What changes is that the metric's
> denominator for this battery was never a checked quantity.
>
> **If an Amendment A4 opens, measuring this ceiling properly is a
> precondition of it** (John, 2026-09-17). Full record:
> `ceiling-defect-2026-09-17.md`.

## 5. The attack sweep becomes a gate (decision 8)

**Registered:** `src/shortcut_sweep.py` is a gate in its own right, run
before any dollar is spent. **It passes when no ownership-blind attack
beats the stated ceiling by more than sampling error** — that is, when the
stated ceiling is the true one. If it cannot be made to pass within two
regenerations, the design halts.

**Why this shape rather than a threshold on the ceiling.** The sweep's job
is to make the stated ceiling honest, not to veto a design. A ceiling that
is high but honest weakens the learnability reading and shrinks the range
a lesion can show, but both degrade smoothly and neither has a cliff; an
earlier draft of this clause proposed halting above 0.40 and that number
could not be derived. Whether an honest ceiling is too high to be worth
training is the judgment in item 1, not an automatic kill.

## 6. Thresholds, kills and bins (decisions 4, 5, 6, 12; K0's number)

- **Revision frequency** is now stated (item 1): two of four agents, drawn
  uniformly, so half of episodes carry a supervised action and a 400-cell
  verdict needs 800 episodes.
- **K2** compared "lookup ceiling plus the null band", adding a raw
  accuracy to a chance-corrected quantity. It is restated in raw accuracy,
  with the band converted explicitly. It decides the unlearnable verdict,
  so it is fixed before the pilot rather than after.
- **K0's band stays at 0.25**, the pre-stated figure, deliberately
  unchanged now that Gate 0 has measured the band at about 0.01. Moving it
  either way after seeing the data would be fitting the rule to the data,
  and the value of a pre-stated number is that you do not touch it once
  you have looked. It is read **only on batteries above the floor margin**,
  so a run that never learned a battery cannot trip it.
- **θ and δ are per battery**, not single numbers. Gate 0 measured them
  varying across a twenty-five-fold range within one checkpoint.
- **A bin is added for the validity check failing.** If zeroing the acting
  channel does not collapse the primary battery to its ceiling, ownership
  is not load-bearing and the objective has failed. The registered design
  had such a guard and it was dropped along with the register. Without a
  bin that outcome has nowhere to land, and an outcome with nowhere to
  land gets explained away.
- **An uncertifiable likelihood attack is routed.** If the act-withheld
  arm's positive controls do not fire, the arm is declared uncertifiable
  rather than passed or failed, and the procedure continues with that
  stated, instead of deadlocking.

## 7. The cue detector's sampler (decision 7 and the sampler amendment)

Both arms of the detector are now drawn the same way, and the verdict is
taken over five independent samples rather than one. Full reasoning,
including that the change was prompted by a grammar failing the old
detector, is in `cue-detector-sampler-amendment.md`. Every verdict reports
both samplers side by side. The amended detector was re-run against every
grammar the old one passed, including the registered MVM-0a grammar, which
reads 0.4969 under the old sampler and 0.4984 under the new one — so the
clean verdict the five existing checkpoints rest on is undisturbed.

## 8. The central claim is narrowed (decision 9)

**Ratified text:** §2.2, that the only route from the ceiling to full
accuracy is to bind the act to the item when acting and carry that binding
forward.

**Registered:** that claim is too strong and was false of two of the three
drafts. The acting channel marks positions, and attending back to marked
positions is a re-readable pointer rather than a carried binding. Both
routes need the channel, so the wire lesion cannot separate them. The
mid-episode re-indexing probe, already registered for the tag bin, is the
discriminator.

## 9. The loss (decision 10)

**Registered:** the loss is the action cross-entropy at the model's own
revision position plus the query-answer cross-entropy, **summed with equal
weight**, the weight passed explicitly at every launch rather than left to
a default. The reading confirmed: §2.1's "not a query asking it to
describe who did what" is satisfied because **no query anywhere asks about
the model's own commitments** — the self-report battery is gone — while
the ownership-free and other-agent queries stay supervised. Read at its
strictest the clause would remove query supervision entirely, and then the
control batteries would never be trained and the differential the
generic-binding bin turns on would be meaningless.

## 10. Money (decision 11)

**Registered, from measurement rather than estimate:** the token budget is
fixed at twenty tokens per parameter, so the longer episodes mean **fewer
steps** (0.71×), which offsets most of the higher per-step cost (1.26×
enactment passes, 1.41× sequence length). A run is **9.1 to 12.8 hours,
$9 to $13**; three seeds **$27 to $39**. The optional extra seeds remain
available inside the $100 hard stop but need a separate go. The $400
ceiling, the $100 stop and the corrigibility commitments are unchanged and
were not reopened.

**Note for the launch:** the RunPod account carries a spend limit of $80,
below the $100 stop. It should not bind at these costs, but it exists.

## What is registered, and what runs next

Registered: the grammar at `src/curriculum_a3.py`, its tokenizer at
`src/encoding_a3.py`, the trainer at `src/train_a3.py`, the batteries
frozen at `batteries-a3/`, the gates at `src/cue_detector_a3.py` and
`src/shortcut_sweep.py`, the calibration at
`src/null_calibration_a3.py`, the lock guard at `src/lock_guard.py`, and
the launcher at `src/launch_a3.sh`.

Next is Gate 2, the pilot: one register-less 30M run at seed 0, on John's
authorization in his own words, quoted verbatim in the ledger row. Nothing
has been spent on A3 to this point.


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot.md =====

# Control-learnability pilot — pre-statement

**UNREGISTERED. Written and committed BEFORE the code change and before
any run, at John's instruction of 2026-09-19.** One 30M register-less
seed, run exactly the way the A3 pilot was run on 2026-09-15. Nothing
here is registered text, no registered verdict is read from this run, and
**nothing launches without John's go in his own words, quoted in the
ledger row.**

*TimeAssembler task: the control-learnability pilot (`90763b8f`).*

---

## The question

**Does the control battery learn when it carries its own loss term,
instead of a third of a shared one?**

The control battery has not learned on any checkpoint. Its intact scores
are 0.2877, 0.3057 and 0.3195 across the pilot and seeds 1 and 2 — all
below 0.3227, the score reached by a reference solver that cannot read
the name the control question supplies. Three seeds, one outcome, so it
is not a seed lottery.

Two explanations have been live since the 2026-09-17 audit and have never
been separated. Either **the control is under-supervised** — it receives
roughly one training row in three, sharing a single pooled term with two
much easier questions, while the primary battery has a dedicated
full-weight term of its own — or **supervision is not the binding
constraint**, and something else in the design defeats it: the reversed
rendering it must attend backwards through, the absence of the private
route the acting channel gives the primary battery, or the fact that its
answer appears in no turn and must be retrieved and then transformed.

This pilot separates them, once, for about ten dollars.

**What it does not do.** It does not repair Amendment A3's registered
comparison, which was refused on 2026-09-19 and stays refused. A control
that learns would make a comparison *designable*; it would not make the
A4 clause registerable, whose fatal findings were about what the clause
measures and where it is read, not about the control's score. **A3 stays
open, not closed**, and this pilot informs that decision rather than
making it.

---

## The change to the training objective

**One paragraph, and no grammar change.** The grammar, the tokenizer, the
frozen batteries, the episode structure, the rendering, the ceilings and
the attack sweep are all untouched; the only thing that moves is how the
loss is apportioned across the queries each episode already carries.
Today every training row carries exactly one query, chosen round-robin
from the three an episode holds, and the cross-entropy on that one answer
token is averaged into a single pooled term shared by the control
battery, the state battery and the syntax battery — so the control gets
about a third of the rows and a third of one term. Under the flag, the
batch is split: **half the rows carry the control query and its
cross-entropy becomes a term of its own with its own weight**, while the
remaining rows carry the state and syntax queries round-robin in a
separate term, and the primary battery's dedicated action term at the
model's own revision position is unchanged. At the flag's default weight
of 2.0 the control's share of the query gradient rises from about a third
to about two thirds, and **its per-row weight quadruples** — from
one-one-hundred-and-twenty-eighth of the pooled term to two
sixty-fourths of its own. With the flag off, the trainer computes exactly
what it computes today.

**Two design calls in that paragraph, both mine, both flagged, and
neither registered so John can move either before the go.**

- **Why the batch is split rather than a second forward pass added.** A
  truly per-episode control term — the control query on *every* episode,
  not half of them — needs a second forward pass and would roughly
  double the step time, taking the run from about ten hours and ten
  dollars to about twenty and twenty. Splitting the batch buys a
  dedicated, separately weighted term **at no extra compute**, which is
  what keeps the estimate on the pilot's measured 0.645 seconds per step.
  *Confidence: high that this is the right trade for a ten-dollar
  question. The strongest alternative is the second forward pass, which
  is the cleaner intervention and tests a stronger dose; it was rejected
  on cost, not on merit.*
- **Why the weight is 2.0.** It is a judgment, not a derivation. The
  arithmetic above is the whole justification: it is the dose at which
  the control's per-row gradient weight quadruples, which is large enough
  that a null result is informative about supervision rather than about
  the dose being timid. *Confidence: moderate. A larger dose would make a
  null more decisive and risks destabilising the other batteries; a
  smaller one makes a null uninterpretable.*

**One coupling, stated rather than buried.** The flag changes two things
at once — the control gets a term of its own *and* it gets more rows —
so a positive result will not say which of the two did the work. That is
deliberate and matches the question as John framed it, which contrasts
"its own loss term" against "a third of a shared one". The two halves are
not separated here and a follow-up would be needed to separate them.

**A consequence worth naming:** the state and syntax batteries drop from
about a third of the rows each to about a quarter. Both sit at 0.999 and
1.000 intact, so there is room, but the secondary cells below watch for
it.

---

## Pre-stated outcome cells

**Primary, read on the control battery's intact score at the registered
endpoint evaluation.** These boundaries are John's, set on 2026-09-19
before the code existed.

| control intact score | cell | what it reads |
|---|---|---|
| **at or above 0.60** | **LEARNED** | the control learns when properly supervised. Name-keyed lookup is available to it, and it is using it. Supervision was the binding constraint. |
| **above 0.3227 and below 0.60** | **PARTIAL** | supervision moves it but does not carry it. Something else in the design is also binding. |
| **at or below 0.3227** | **DID NOT LEARN** | supervision is **not** the binding constraint. Option D (a scaffolded intermediate query, which teaches plain name-keyed retrieval before layering the rule on top) or closing A3 is what is left. |

The 0.3227 boundary is the score of the reference solver that cannot read
the name the control question supplies. A battery at or below it has not
learned the task, whatever else is true.

**Secondary cells, reported with the primary and never in place of it.**

| reading | expected | what a miss would mean |
|---|---|---|
| **primary battery still learns** | intact **≥ 0.50** | below 0.50, the reallocation damaged the objective that works, and the pilot answers nothing: the run is reported as a failed intervention, not as evidence about the control. |
| **the input-channel lesion still collapses the primary battery** | collapse, as on all three existing checkpoints (0.57 → 0.14–0.20) | if the primary battery survives its own lesion, ownership has stopped being load-bearing under the new weighting and no reading about the control is available from this run either. |

**No threshold is crossed and no registered verdict is read.** The cells
above are raw intact scores. John's committed threshold lock governs
registered readings on registered checkpoints; this run is unregistered,
reads no registered verdict, and does not touch the lock.

---

## What is run, exactly

Identical to the A3 pilot of 2026-09-15 in every respect but the flag:
one 30M **register-less** run — the launcher has no flag that could train
a register — at **seed 0**, chosen so the comparison against the existing
pilot is matched on initialization and data order and **the loss is the
only thing that differs**. Registered recipe values, unchanged:
585,544,960 tokens, 55,116 steps, batch 128, action weight 1.0,
evaluation every 500 steps at n=100 for the trajectory only. Artifacts go
to a distinct output name so nothing can overwrite the existing pilot's
checkpoint.

**Cost, from the pilot's measured 0.645 seconds per step:** 55,116 × 0.645
= 9.87 hours of training, about 10.2 hours of pod life at $0.99/hour on
the registered venue, so **about $10.2, band $9–13**. That takes the A3
cumulative from $34.31 to about $44.5 against the $100 hard stop. Step
count and token budget are unchanged because the grammar is unchanged;
the one thing that could move the measured pace is that control questions
render at a slightly different length from state and syntax ones, so
padded batches may differ by a few percent. **The ledger records the
measured pace at step 500**, as it did for the pilot, and the estimate is
revised in flight if it has moved.

---

## Order, and the gates

1. This pre-statement, committed **before** the code change. *(Done: this
   file.)*
2. The loss change behind a flag, self-tested, committed.
3. One run staged through the registered launcher with the flag, dry-run
   clean, and a ledger row carrying the estimate **before** any spend.
4. **Stop for John's go, in his own words.** Nothing launches without it.

**Nothing in this document is registered.** It is a pre-statement for an
unregistered diagnostic, and its value is entirely that it was written
down before the code existed and before the number came back.


===== FILE: docs/public-path-roadmap-2026-09-16.md =====

# MVM public path roadmap (drafted 2026-09-16, Pacific)

*Status: APPROVED by John 2026-09-16 (Pacific), verbatim: "Approved on all". Proposed by Claude (Cowork session); steps and dates stand as written.
Companion to `ROADMAP.md` (stage gates), `ROADMAP-post-removal-test.md` (the fork and the paper shape)
and `STATUS.md` (this week). This file covers only one thing: getting from the current experimental
state to something usable in public discourse. It builds on the 2026-08-02 adjudication that the
writeup is one flagship registered-report-style paper (`drafts/paper-removal-test-nature-draft.md`).*

## Why this path matters

1. The Calibration Problem's chapter 1 thesis contract says the wager (self-indexed temporal
   integration as the floor of an inside) and the Part III ethics fail separately. MVM is where the
   wager is exposed to evidence.
2. Public AI-consciousness discourse runs mostly on assertion. Pre-registered instruments that can
   lose, an open ledger and published nulls are the differentiator for Sentient Horizons.
3. The essays, Appendix B ("Running the Instrument") and a possible video series need a concrete
   story. The registered results, including the nulls, are that story.

## Already handled (verified in the repo 2026-09-16, branch gate0-null-calibration)

- Threshold lock committed by John: `6ad4362` (2026-09-16 20:08 PDT).
- John's verbatim go for the A3 seeds 1 and 2 wave: `45fd652` (20:11 PDT). Two pods in flight.
- Pod-side reaping ruled and implemented for future launches: `5dedc18` (20:24 PDT).
- Both process fixes, Gate 3 (passes both arms), L1 localization pipeline built and smoke-tested.
- Ruled 2026-09-16: seed 0 is not-testable on the differential clause, so Amendment A3 as registered
  can no longer return a full registered positive. Seeds 1 and 2 test whether primary-battery
  learnability replicates and whether the control battery is a seed lottery.

## Steps from here

| # | Step | Owner | Proposed date |
|---|---|---|---|
| 1 | Seeds 1 and 2 report, checkpoints fetched and checksummed, pods reaped, ledger actual-after rows | Claude Code session | 2026-09-18 |
| 2 | DECIDE: optional extra seeds (bounded by the $100 A3 stop and the $80 RunPod limit) | John | 2026-09-20 |
| 3 | Blind-localization arm (registered, unconditional): run blind on one of the five A2 register-bearing 30M checkpoints, local, $0. The A3 L1 pipeline does not discharge it | Claude Code session, John schedules | 2026-09-27 |
| 4 | DECIDE the control-battery question: a registered Amendment A4 that makes the control learn reliably, or close A3 with partial discriminators and say so. Without this no future run can return a full verdict | John, on a proposal | 2026-10-04 | **RULED EARLY 2026-09-20: Amendment A3 closes as *not testable* (the pre-registered loss condition on a non-self control at ceiling has fired). Proposal v2 in `docs/step4-control-battery-proposal-2026-09-20-v2.md`; Gate C review RT-94 to RT-117. Grammar redesign deferred to a successor experiment after release. Closure text still to be drafted, after step 3 and the two authorised localization runs, through Gate A.**
| 5 | Refresh `explainer.md` (last touched 2026-07-01, predates the registered removal-test result, MVM-0 and A3). After the 2026-09-30 book text lock | Cowork session | 2026-10-11 |
