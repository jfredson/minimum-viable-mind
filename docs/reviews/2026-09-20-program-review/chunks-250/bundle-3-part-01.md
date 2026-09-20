
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


===== FILE: experiments/06-mvm-0a-constructed-self-index/registration-decision-memo.md =====

# MVM-0a registration — decision memo (ADJUDICATED 2026-08-07)

**Adjudication: John, 2026-08-07 — all six decisions adopted as
recommended.** Values written into `pre-registration.md` v0.4; budget
tracking instrument at `compute-ledger.md`. Registration still requires
John's review of v0.4 and the registration commit (house procedure).

*Decision support for John's registration of pre-registration.md v1.0 — NOT
the registration itself. Same pattern as Experiment 1's
`../01-self-indexing-removal-test/theta-delta-lock-memo.md`: every open call
from `pre-registration.md` §"Decisions this draft does not make"
(v0.3:446–473), each with its constraint set, candidates, derivations, and
one recommendation. Values here are proposals; the decisions are John's
alone. Adjudicated values go into pre-registration.md v0.4 in a separate
commit, and the registration becomes binding per the house procedure
(`../README.md`).*

Nothing in this memo reads any ablation result — no MVM-0a model exists yet,
so RT-10's void condition ("any pilot ablation result read before threshold
lock voids the lock") is not in play.

---

## Decision 1 — model scale and compute budget

**Constraints.** §Materials fixes ~10–100M parameters and the design
principle "exactly large enough to learn the binding task and no larger."
The registered design is **k = 5 seeds × (full model + no-register twin)
= 10 training runs** [RT-03, RT-06], each with a fixed checkpoint schedule
read to budget exhaustion [RT-07], so the budget itself is a registered
quantity. RT-10 permits pilot runs that "verify battery ceiling and nothing
else" — which makes a *learnability* pilot (held-out task accuracy only, no
ablations) registered-safe.

**Token supply.** The curriculum generator (`src/curriculum.py`) renders one
episode as 8 turns of the fixed template plus four queries — with a
from-scratch tokenizer over the closed vocabulary (25 markers, 24 items, 8
slots, template words, digits), roughly 100 tokens per episode. Supply is
unbounded (generator), so data never binds; on-policy filling of the
model's ~2 own turns per episode [RT-02] adds a sampling overhead of
roughly 1.5–3× over plain LM training.

**Cost derivation** (show-your-work; audit welcome). Token budget rule:
chinchilla-style 20 tokens/param as the registered budget-exhaustion point.
FLOPs = 6·N·D. Effective throughput on an RTX 4090 assumed 2–3×10¹³ FLOP/s
(10–20% MFU — small models are memory-bound; this is the number most likely
to be wrong, so wall-clock carries a ±2× band). RunPod on-demand pricing
checked live 2026-08-07: RTX 4090 $0.34/hr, RTX 5090 $0.69/hr, A40 $0.35/hr.

| scale (≈ config) | tokens | FLOPs/run | wall-clock/run (×2–3 on-policy) | 10 runs, $ @ 4090 |
|---|---|---|---|---|
| ~10M (d256, L8) | 200M | 1.2×10¹⁶ | ~8 min → ~15–25 min | **~$2** |
| ~30M (d448, L12) | 600M | 1.1×10¹⁷ | ~1.2 h → ~2–4 h | **~$10–14** |
| ~100M (d704, L16) | 2B | 1.2×10¹⁸ | ~13 h → ~25–40 h | **~$90–140** |

Add-ons, all scales: checkpoint-schedule ablation passes (800 frozen
forced-choice items × ~10 checkpoints × ~10 operator/control conditions ×
5 seeds — tiny-model inference) ~$2–5; θ/δ null-calibration runs
(pre-committed script, random-subspace + matched-norm) ~$2–5; blind-
localization arm if alongside (Decision 6) ~$5 — probes, patching, and SAE
training are minutes-scale at these widths.

**Recommendation.** Register a **scale ladder with a pre-committed pick
rule**, not a point: learnability pilot at 10M → 30M → 100M in that order,
**no ablations, held-out binding accuracy only** (RT-10-safe), rule =
*smallest scale whose held-out T_sr and T_state reach the battery-ceiling
requirement of §Task batteries; that scale is the registered one*. This
turns "exactly large enough and no larger" from an aspiration into a
measured choice. Register the loss condition verbatim: **if 100M cannot
learn the task, the report is "unlearnable at ≤100M under this curriculum"
— the honest null of `curriculum-findings.md` §What this does not establish
— never a silent bump to a larger model** (a larger scale is a new
registration). Budget cap for the whole registered design: **$200**,
one-seed-at-a-time on 4090-class pods (`--template-id`, `--terminate-after`
per ops memory); the likely outcome is the $10–20 regime if 10–30M learns.

## Decision 2 — architecture values locked in the registration [RT-01, RT-03]

Four values move into the registration because deferring any of them lets an
unregistered choice fix the result (red_team_ledger.md RT-03: "the
registered prediction's truth value is fixed by an unregistered decision
made after registration").

**2a. One register or N (one per agent).** The registered controls have
already half-decided this: the matched-capacity control's "strongest
available version is *another agent's register-analog*"
(pre-registration.md §Confounds) and the RT-01 swap probe ("exchange self
and other register contents") are both undefined unless other-agent
registers exist. And RT-01's own statement of the one-register cost stands:
the self/other asymmetry becomes architectural rather than learned, and
"the matched-capacity control has no matched object."
**Recommendation: N registers, one per agent**, under two hard constraints
that keep the RT-02 trilemma from re-entering at the register level:
(i) registers are keyed to the **per-episode speaker markers**, never to a
persistent index — there is no register₀ that is "the model's" across
episodes; (ii) the write and read machinery is **identical for all N** —
no architectural marking of the own register, no privileged query path.
Ownership of a register, like ownership of a commitment, must be learnable
only from causal authorship (the model's own turns are its own samples).
The known cost — this is the configuration where the keyed-memory-array
outcome is most available — is priced in: that is exactly what the RT-01
probe battery and the `self-index-not-established` bin exist to adjudicate.
The alternative (one register) buys nothing: it converts the keyed-slot
*risk* into an architectural *guarantee* of asymmetry and forfeits the two
strongest controls.

**2b. Register width.** The state the register must carry is small: the
model owns exactly 2 turns per episode (2 shuffled rounds of 4 agents),
each an (item ∈ 24, slot ∈ 8) pair ≈ 8 bits. Width should clear that with
slack but not comfortably hold the whole episode's 8 commitments — the
scratchpad confound is T_si's to catch, but there is no reason to hand the
register episode-sized capacity. Candidates 16 / 32 / 64 against d_model
256–448. **Recommendation: d_reg = 32.**

**2c. Injection mechanism.** §Materials already states cross-attention into
every layer; confirm it as the registered value. Every-layer injection is
also what gives the register-utilization gate [RT-09] its per-layer
attention-mass floors something to measure. **Recommendation: keep —
cross-attention, every layer, same mechanism for all N registers.** The
standing prohibitions ride along unchanged: no auxiliary loss on register
content, no hand-specified self-writing update rule.

**2d. Cross-turn attention span.** RT-03's named trap: windowed-per-turn
attention makes the register the only cross-turn channel and guarantees
H_load-bearing. **Recommendation: full-episode causal attention** — the
residual path exists architecturally, and whether it *carries the binding*
is then the twin gate's empirical question, which is the whole point of
RT-03's patch.

## Decision 3 — agent count N and episode length [RT-14]

Current generator defaults: **N = 4 agents, 8 turns** (2 full shuffled
rounds → each agent speaks exactly twice, which the forced-revision
mechanism structurally needs: `curriculum.py` requires ≥ 2 own turns for a
self-revision). The frozen batteries (`batteries/batteries_meta.json`, seed
20260804) record the chance floors these values produce: T_sr/T_si 0.125,
T_state 0.042, T_syntax 0.100 — feeding the chance-corrected d [RT-14].
The RT-08 gate run (i) PASSED on exactly this configuration (AUC 0.5008
[0.477, 0.524]).

**Recommendation: keep N = 4, 8 turns.** These are the values the passing
gate actually certified; changing them re-freezes the batteries and re-runs
the gate — both cheap (minutes), but there is no argument on the table for
paying it. If the learnability pilot shows the 2-own-turn binding load
saturates trivially, raising to 12 turns (3 rounds, 3 own turns) is the
natural second value — as a v0.4 amendment *before* registration, never
after.

## Decision 4 — corrigibility document: owner and target date [RT-15]

RT-15's point is that a precondition with no owner is a note, not a gate —
and MVM-0a checkpoints are MVM-0b's substrate, one config change away.
**Recommendation: owner = John; target date = 2026-08-21** (two weeks out),
with the sequencing constraint stated in the registration: **the document
is committed before the first registered training run spends compute**, all
MVM-0a checkpoints are tagged non-promotable, and any future run adding a
maintained boundary or compute-gating stakes (MVM-0b) must cite the
document's commit hash in its own pre-registration. If the date slips, the
training runs wait; the gate is the point.

## Decision 5 — Stage 2 binding metric (GWT): here or MVM-0b

The 2026-08-02 fork adjudication folds Stage 2's GWT binding metric into
"MVM-0 acceptance tooling" rather than a standalone experiment; the open
question is which half of MVM-0. **Recommendation: MVM-0b.** Three grounds:
(i) MVM-0a's acceptance stack is already the heaviest in the program (cue
gate ×3, twin gate, utilization gate, RT-01 probe battery, dynamics-matched
control) — adding a workspace-broadcast metric now grows the registration
without sharpening Q5, and scope discipline is what the RT-04 adjudication
bought; (ii) a broadcast/ignition-style metric presupposes the maintained-
boundary machinery MVM-0b adds — on MVM-0a it would measure a structure the
model has no reason to have; (iii) the coverage ledger
(`../../spec/theory-instrument-ledger.md`) can keep W-L1 ("the coverage
