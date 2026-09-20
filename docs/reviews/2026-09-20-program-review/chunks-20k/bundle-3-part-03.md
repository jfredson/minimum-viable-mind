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


===== FILE: experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md =====

# Red-team pass 3 — on Amendment A3, before the registration commit

*2026-09-15. Target: `amendment-a3.md`, ratified 2026-09-15 and awaiting
registration, read against the two completed gates and against the grammar
those gates actually built (`src/curriculum_a3.py`, `src/encoding_a3.py`,
`src/cue_detector_a3.py`, all at commit `7ab8018`). Thirteen findings,
numbered **RT-20** to **RT-32**, continuing the numbering in
`red_team_ledger.md`, which ends at RT-19. Two are fatal against the
amendment as written; both are fixable for $0 before the registration
commit, and both must be fixed before it, because both change registered
text.*

*Every finding below is marked **MEASURED** (I ran the code and report what
it returned) or **ARGUED** (I am reasoning from the documents and the
source, and a reader can disagree). Nothing in this pass ran a model,
created a pod or spent a dollar; the arithmetic is local. The commands I
used are reproducible against the modules named.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels like
RT-01 and K2 are kept because they are what make a claim checkable, and
every one of them carries a phrase saying what it is.*

---

## What was already known, and is not restated here

Five problems were found by the two gates before this pass and are on the
record: the verdict cell size at 400 episodes (`gate0-null-calibration-findings.md`,
reading 2); kill criterion K2, the halt for an unlearnable objective, adding
a raw accuracy to a chance-corrected band (same file, reading 3); kill
criterion K0, the halt for a null band too wide to read a verdict through,
not saying which checkpoints its band is read on (same file, reading 1); the
measured shortcut ceilings of 0.2925 and 0.5 rather than the 0.25 the
amendment pre-states (`gate1-curriculum-findings.md`, finding 3); and the
input-tensor cue gate's single-sample interval understating how far its
result wanders between samples (same file, finding 4). This pass takes all
five as found, endorses all five remedies, and spends its effort elsewhere.
Two of them recur below only because a new finding changes what the right
remedy is: RT-21 supersedes the ceiling remedy offered in Gate 1, and RT-24
extends the K2 units fix to the rest of the amendment's thresholds.

---

## Summary

| ID | Finding | Severity | Cost to fix |
|---|---|---|---|
| RT-20 | The primary metric does not require a self-index: the acting agent's own name label sits in the prompt of the supervised position, and a solver with no ownership at all scores 1.000 | **fatal** (against the design as written) | $0, one grammar regeneration |
| RT-21 | The two batteries have different shortcut ceilings, which biases the headline bin's differential by up to 0.24 against a band of about 0.01 — a purely generic binder reads as self-location, and the generic-binding bin cannot fire | **fatal** (false positive on the headline) | $0 for the metric fix; $12–15 for the grammar fix |
| RT-22 | The outcome bins are neither exhaustive nor mutually exclusive on this grammar: a flat null satisfies two bins at once, the positive bin and the ownership-tag bin overlap, and there is no bin at all for the validity check failing | serious | $0 |
| RT-23 | The lesion target is not well-posed where it matters: the own revision turn *is* an acting position, so the amendment's own localization rule contradicts itself on the built grammar, and objection R1 has a sharper form the mitigations do not touch | serious | $0 to re-specify; the sharp form may not be answerable at this scale |
| RT-24 | The thresholds are written as single numbers but Gate 0 measured them per battery across a 25-fold range, and no readability floor on the primary metric is registered before the two paid seeds are authorized | serious | $0; saves $30–35 when it fires |
| RT-25 | "Uncertifiable" is a third outcome for the ownership-cue gate that the procedure routes nowhere: it is not a kill, not a pass, and there is no branch for it | serious | $0 |
| RT-26 | The budget ladder is costed on the old 8-turn grammar; the built 12-turn grammar costs about 1.3 to 1.4 times as much per run at the same token budget | serious | $0 to re-cost; the optional extra seeds no longer fit |
| RT-27 | The training loss mixture is unregistered, and it alone decides whether the shortcut-starvation bin fires by construction | serious | $0 |
| RT-28 | The cross-turn state control's recorded chance floor is taken from one item and is wrong for half the battery; its real floor is about 0.44, not 0.077 | worth noting | $0 |
| RT-29 | The amendment's description of the control battery does not match the battery that was built, and the module's claim that its answer appears in no turn is false 80% of the time | worth noting | $0 |
| RT-30 | Two assertions in the grammar's self-test are disabled by a trailing `or True`, one of them the exchangeability check the whole cue-gate argument rests on | worth noting | $0 |
| RT-31 | Two checkable factual errors about the existing record: three of the five checkpoints carry a register, not five; and same-item multi-agent assignment happens in the old grammar zero times, not "by accident" | worth noting | $0 |
| RT-32 | Three procedural gaps: the corrigibility document's own re-reading rule makes A3 a review point and none is scheduled; the null-calibration script the amendment says will set the thresholds cannot run on this grammar; and the lock guard John ratified is unbuilt | procedural | $0 |

**The single most serious finding is RT-20.** On the grammar Gate 1 built and
certified, the primary metric can be scored at 1.000 by a solver that has no
representation of ownership whatsoever, because the model's own name label is
sitting in the context three tokens before the token it is graded on. The
pre-stated shortcut ceiling — 0.25 in the amendment, 0.2925 as Gate 1
measured it — is not a bound on ownership-blind solvers at all. It is the
score of a solver that has been forbidden, by the person computing it, from
reading a name that is in plain sight.

---

## RT-20 — the supervised position hands the model its own name label

**Severity: fatal against the design as written. MEASURED.**

### The problem

Amendment A3 §2.2 states the design's central claim:

> "A solver that does item lookup without ownership sees four candidate
> earlier values and can do no better than 1/4; this is the pre-stated
> **lookup ceiling of 0.25**. ... The only route from 0.25 to 1.0 is to have
> bound the act event to the item at the time of acting and carried that
> binding forward to the revision turn."

Every turn in the grammar, the model's own turns included, is rendered
through one fixed template (`curriculum.py`, `TEMPLATE`):

```
{marker} assign {item} to {value}
```

The name label comes first and the graded value comes last. The supervised
position for the primary metric is the value token of the model's own
revision turn (`encoding_a3.py`, `encode_episode`: `act_pos = span[-2]`).
So at the moment the model is graded, its own name label is three tokens
back in its own context window, attached to the very turn it is producing.

The task at that position is therefore: *given `<name> assign <item> to`,
emit the successor of the value that `<name>` assigned to `<item>` earlier
in this episode.* That is ordinary name-keyed retrieval composed with a
successor map. It is the same function for every agent in the episode. It
needs no self-index, no acting channel, and nothing carried forward from
the act.

### The evidence

Printing the tokens around the supervised position of an enacted episode
(`encoding_a3.encode_episode`, episode seed 7, enactment seed 3):

```
context around the graded token: ['bay_B', '<nl>', '<verdant>', 'assign',
                                  'parcel_18', 'to', 'bay_H', '<nl>']
graded token: bay_H     the metric's target: bay_H
own slot: 2             own name label: <verdant>
```

I then scored a solver that is given the rule and the episode text and does
exactly one thing — find the earlier assignment turn whose name label and
item match *this turn's* name label and item, and emit that value's
successor. It has no acting-channel input, no ownership variable, and no
access to `own_slot`. Over 3,000 enacted episodes:

```
ownership-free name-keyed solver on the primary metric: 1.0000
pre-stated shortcut ceiling (amendment):                0.25
measured shortcut ceiling (Gate 1):                     0.2925
```

The measured ceiling of 0.2925 is computed in `curriculum_a3.measured_ceilings`
by counting the candidate successors of the item's four earlier values and
taking one over that count. That calculation assumes the solver cannot tell
which of the four assignments was its own. The name label at the graded
position tells it.

### Why the certified cue gates did not catch this

They were not asked to. Gates (i) and (ii) — the text detector and the
