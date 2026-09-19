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

**Why the null was predicted rather than merely possible.** Two features of the design guaranteed that the register could at best become self-reference. First, the register's contents were never required by any objective: the loss was answer-only CE on end-of-episode queries, and the item analysis shows those queries decompose into unique-item lookup (solved by every run), general marker-keyed retrieval (a seed lottery won by two of five runs, register irrelevant), and revised-item recency (`register-lesion-findings.md`, thread 3). A solver never needed to know which agent it was to answer them, so nothing pressed the network to index the binding to a center, and a designated slot with no pressure on it fills with whatever is cheapest, here a bias. Second, the register was symmetric by design (N marker-keyed registers, shared init, no privileged own path, RT-01/RT-02), which was correct for excluding a keyed-slot confound but also meant "which register is mine" was itself something the network would have had to learn under pressure that did not exist.

**The one place a doing was load-bearing.** The record contains a pointer in the other direction. In the three runs that never learned general retrieval, the model's memory of its own first commitments collapsed from T_sr 0.96 to about 0.16 (eight-way chance 0.125) the moment the acting channel was zeroed at eval (`register-lesion-findings.md`, "The acting channel"). That is a mechanism the model could not drop without degrading the task, and it is an act, the motor-copy event, not a stored description. The binders barely used it (T_sr 0.98 without it) because the batteries let them answer by item lookup. So where authorship was load-bearing at 30M it was carried by a doing, and where the design offered a noun the network ignored it. That is exactly the shape ch05's distinction predicts, and it is why the redesign follows the doing.

**The J-space pointer.** ch05, "Where the Rivals Stand," records that the workspace structure Anthropic found "emerged in training" and that "post-training causes the J-space to acquire the Assistant's point of view" (the comparison note, "Their position," item on emergence, and "Divergence" item 2). A point of view was acquired because the post-training task needed one; nobody installed it. The same note names the discriminating experiment ch05 requests: remove the self-directed content alone and watch whether the composed act degrades or only the narration flattens. MVM-0a cannot run that contrast on a stock model, but it can build the small-model analogue: a task that cannot be done without a point of view, a system that acquires one under that pressure, and a lesion of the acquired structure scored on the task.

**What this section does not claim.** It does not claim the architecture failed, nor that a register could never become load-bearing under some other curriculum. It claims the narrower thing the files support: under this objective the register was never required, it became a bias, and the removal test read it correctly. Experiment 1 had already delivered the mirror image on a stock model, a locatable self-structure that was dialogue-state routing and a self-report that no intervention ever subtracted (`removal-test-findings.md`, "The registered verdict"). Between them the two experiments say: what we could find was not a center, and what we installed was not one either. The next design has to make the center something the task earns.

---

## 2. The design: an objective where self-indexing is load-bearing

### 2.1 The requirement, stated as a constraint on the loss

The objective must satisfy three conditions, each of which the old batteries violated:

1. **Perspective-dependence.** The correct output at a supervised position must depend on which agent the model is, so that a solver with no self-index cannot exceed a pre-stated shortcut ceiling.
2. **Ownership only from the act.** Under RT-17 (`red_team_ledger.md`, pass 2), in a token-only interface with exchangeable turns, ownership is unlearnable from statistics, so every learnable ownership signal is a fingerprint. The only clean grounding is causal authorship carried by the acting channel (A1). The redesign keeps the A1 enactment pipeline unchanged: own-turn values are drawn by the harness from the generator's own distribution, and the acting channel is the only authorship signal. What the model must acquire is the carrying of that signal across turns and its use at later positions where it is needed.
3. **The supervised position is an action, not a report.** The loss sits on what the model does next in the episode, on its own turn, not on a query asking it to describe who did what. A report-only solution is then not a solution: nothing in the objective rewards describing ownership, only acting on it.

Existing infrastructure this runs on, unchanged unless stated: `src/curriculum.py` (grammar, revision rule, paired content-crossing episodes), `src/encoding.py` (103-token closed vocab, register key stack), `src/model.py` (30M trunk, `act_proj`, twin configuration), `src/train.py` (batched enactment, `eval_heldout`, T_sr_rev split), `src/cue_detector.py` and `src/fingerprint_gate.py` (gates i to iii), `src/lesion_register.py` and `src/item_analysis.py` (lesion harness, per-item scoring at n=400), and the measured venue (RTX 5090 secure, $0.99/hr, twin-architecture runs at about 10.2 hours, `compute-ledger.md` wave 1 and 2 rows).

### 2.2 Three candidates

**Candidate A (primary): the perspectival revision rule, "act as yourself."**

The registered grammar already contains a revision mechanism: an agent later revises its own earlier assignment of a value to an item, and the revision must differ from that agent's earlier value (A1.1; RT-11). The candidate makes two changes.

- *Every revised item is assigned by all N agents before any revision.* So at a revision turn on item X, the episode contains four earlier assignments of X, one per agent, with distinct values (the generator enforces distinctness on revised items). This is the "ownership is the only disambiguator" construction the findings file sketched (`register-lesion-findings.md`, "Wave-3 bearing," option (a)).
- *The revision rule becomes a deterministic function of the actor's own earlier value.* Proposed: the revised value is the successor of the actor's own earlier value on that item, modulo the slot count. Every agent obeys the same rule; the generator applies it to the other agents, and the enactment harness applies it to the model. The rule is perspective-invariant, but its application requires knowing which of the four earlier assignments was mine.

The supervised position is the model's own revision turn. The metric, **T_act**, is the fraction of own revision positions at which the model's distribution puts its argmax on the value the rule dictates for it. Chance is 1/8 (eight slots). A solver that does item lookup without ownership sees four candidate earlier values and can do no better than 1/4; this is the pre-stated **lookup ceiling of 0.25**. A coherence-clustering solver (RT-11) has nothing to cluster, because own earlier values are uniform draws. Stylometry is excluded by exchangeability (A1), and position is randomized by the grammar. The only route from 0.25 to 1.0 is to have bound the act event to the item at the time of acting and carried that binding forward to the revision turn. That carrying, and its use at the revision, is what "the binding indexes its own center" means at this scale.

Enactment stays exchangeable: the harness draws the model's first assignment uniformly, as now, and computes its revision by the same rule the generator uses for everyone. So the episode text and tensors remain invariant under relabeling of the model's slot, and gates (i) and (ii) apply as registered. The loss at the revision position is CE against the rule-dictated value; the loss at first-assignment positions is unchanged (none, they are draws). Gate (iii) needs one re-specification, given in §3.4.

*Why a report-only solution fails this objective.* There is no report position. A model that could describe "my earlier value on X was v" but did not use v at the revision would score at the lookup ceiling. Conversely, a model at ceiling on T_act has, by construction, used its own history in the act. If lesioning an acquired structure drops T_act while a matched other-agent structure's lesion does not, the structure was load-bearing for the act, which is the book's signature.

**Candidate B: stream continuation, "which stream am I."**

Interleave K independent episode streams in one context, each with its own running state (counts, ordering, the current T_state content). The model acts in exactly one stream, and its own turns are the only ones enacted with the acting channel. Its action at each own turn must continue its own stream's state (emit the next count, or the value the stream's rule dictates), where the other streams carry different states of the same form. A solver with no self-index can at best guess which stream is its own, with chance 1/K. This forces the model to track which of several streams it is, and to use that tracking in the act. It is attractive because the ownership-free T_state battery already exists and the state-continuation rule is a small change to it. It is not primary because interleaving multiplies episode length (cost scales with K), because the "which stream" index is a single bit set once per episode rather than an item-by-item binding, so a very cheap tag could solve it (the RT-01 keyed-slot worry in its purest form), and because the T_state generator would need a matching action-position supervision it does not yet have.

**Candidate C: continuation against a literal twin.**

As Candidate A, but the other agents' turns are sampled from the model's own policy into other slots (without acting-channel injection), so the confusers are not generator draws but the model itself. This is the strongest possible exclusion of stylometry: the twin is the model. It is not primary because A1's uniform draws already make every agent exchangeable with the model, so the gain is small; because it doubles forward passes per training step (the measured runs are enactment-bound, `pilot-a1-30m-findings.md`, "Run record"), which does not fit the budget; and because policy-sampled confusers reintroduce the gate (iii) hazard A1 was built to remove. It is recorded as the hardening to reach for if Candidate A's gate (iii) comes back with a fingerprint that the act-withheld arm (§3.4) cannot clear.

### 2.3 Why Candidate A is primary

It is the smallest change to the registered grammar that satisfies all three constraints in §2.1; it reuses the enactment pipeline, the frozen-skeleton battery unit (A1.5), and the chance-corrected metric verbatim; it has a pre-stated shortcut ceiling (0.25) that a lookup solver cannot exceed, so learnability and load-bearingness are separable in the data; it fixes the T_si repeated-item scoring defect in passing by giving revised items a single well-defined latest value (`register-lesion-findings.md`, thread 3; `wave3-options-opus-5.md` §0.6 point 1); and it supervises an action.

### 2.4 Architecture: no register

The register is not trained in the new runs. The trained architecture is the registered twin configuration (`model.py` with the register removed, acting channel present, full-episode causal attention, 30M), which is also the cheaper run (about 0.35 s/step against 0.53, `compute-ledger.md` wave 1 row). Removing the register is the direct consequence of §1: the center is to be acquired, not installed, and the lesion target is whatever the network builds to carry ownership across turns. The five existing checkpoints stay as $0 controls (§3.6).

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
