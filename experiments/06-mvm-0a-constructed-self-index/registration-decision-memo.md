# MVM-0a registration — decision memo (DRAFT, prepared 2026-08-07)

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
fraction improves") winnable with GWT landing in MVM-0b — it does not need
it in MVM-0a. Record the deferral in v0.4 so the fork adjudication's
paper trail stays unbroken.

## Decision 6 — blind-localization arm [RT-12]: alongside or follow-on

**Recommendation: alongside — registered now, in this pre-registration, as
an unconditional arm.** The decisive argument is selection-proofing: if the
arm is a follow-on, the decision to run it is made *after* the headline is
known, and "we ran the instrument-audit because the headline disappointed"
is a story a skeptical reader gets to tell. Registering it unconditionally
now — it runs on the same trained seeds regardless of bin — removes that
degree of freedom for ~$5 of analysis compute (probes, patching, and SAEs
are minutes-scale at d ≤ 448). Sequencing firewall inside the arm: the
headline verdict is computed and committed **before** the localization
pipeline runs, and the pipeline (Experiment 1's, mechanically re-run)
receives a config with the register location withheld. State the honest
limit in the registration: with one researcher, blindness is **procedural,
not epistemic** — the analyst knows the architecture; what is blind is the
pipeline's inputs, and every threshold it uses is inherited from Experiment
1, not tuned here. The red team's judgement stands in the draft and this
memo endorses it: if the instruments cannot recover a center known-by-
construction to be there and load-bearing, **Experiment 1's null was
instrument failure** — a result worth more than the headline either way it
goes.

---

## Adjudication checklist (for the v0.4 commit)

| # | decision | proposed value |
|---|---|---|
| 1 | scale + budget | ladder 10M→30M→100M, pre-committed smallest-that-learns rule; 20 tok/param; cap $200; unlearnable-at-scale loss condition verbatim |
| 2a | registers | N (one per agent), marker-keyed, symmetric machinery |
| 2b | register width | 32 |
| 2c | injection | cross-attention, every layer |
| 2d | attention span | full-episode causal |
| 3 | N agents / turns | keep 4 / 8 (gate-certified values) |
| 4 | corrigibility doc | John, 2026-08-21, blocks first training run |
| 5 | GWT metric | defer to MVM-0b, recorded in v0.4 |
| 6 | blind-localization | alongside, unconditional, verdict-first firewall |

After adjudication: write values into pre-registration.md v0.4, John's
review, then the registration commit makes it binding (house procedure,
step 2). The cue-detector gate run (ii) on input tensors becomes buildable
the moment 2a–2d are fixed, since the tensor layout (register keying,
marker embeddings, loss masks) is what it inspects.
