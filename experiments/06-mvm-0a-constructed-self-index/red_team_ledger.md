# MVM-0a red-team ledger (pass 1, 2026-08-04)

*Adversarial pass on `pre-registration.md` draft v0.1. Fifteen findings:
three fatal, eleven serious, one procedural. All patches are written into
**draft v0.3**. RT-04 was adjudicated by John on 2026-08-04 (option (b) —
scope to Q5); the other fourteen dispositions are the drafter's
recommendation and remain open to John's review, per the house procedure.

Findings below quote v0.1's bin names (`H_center`, `H_bypass`,
`H_router`) because that is the vocabulary they were written against.
v0.3 renames those bins to `H_load-bearing`, `H_routed-around`, and
`H_generic-state` — a consequence of the RT-04 adjudication, not a
separate change.*

The pass's summary judgement, which the draft should absorb rather than
resist: the design's one structural virtue — a physically designated
ablation target — was doing more rhetorical work than engineering work.
Designation fixes *where* to cut, not *what was cut*.

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| RT-01 | Register may be a keyed memory array; bins can't tell | fatal | ADOPTED — swap/re-index/address probes + new bin |
| RT-02 | Self-identification bootstrap trilemma | fatal | ADOPTED — on-policy mandatory, no identity token, style canonicalization |
| RT-03 | "Residual path" unfalsifiable; decision deferred past registration | fatal | ADOPTED — no-register twin gate; architecture locked in registration |
| RT-04 | No report channel; H_description engineered out | serious→fatal for framing | **ADJUDICATED 2026-08-04 — option (b): scope to Q5, defer the contrast to MVM-0b** |
| RT-05 | T_syntax vacuous by construction; H_center collapses to one clause | serious | ADOPTED — cross-turn state control replaces it |
| RT-06 | Single training run; model is a draw, not a fixture | serious | ADOPTED — k ≥ 5 seeds, majority rule, seed-dependent bin |
| RT-07 | Register reliance is a trajectory; stopping point selects the verdict | serious | ADOPTED — checkpoint schedule, verdict read at budget exhaustion |
| RT-08 | Cue-detector gate: wrong time, wrong representation, no power | serious | ADOPTED — three runs, equivalence bound, positive control |
| RT-09 | H_bypass has no construction-failure guard | serious | ADOPTED — register-utilization gate before any bypass reading |
| RT-10 | Thresholds fitted to a same-model pilot | serious | ADOPTED — null-calibrated θ/δ on the registered model |
| RT-11 | Ownership not crossed with content; coherence solver passes | serious | ADOPTED — content-crossing as hard curriculum property + forced-revision eval |
| RT-12 | Q1 inference invalid; the instrument-testbed arm is missing | serious | ADOPTED — blind-localization arm added; Q1 claim deleted otherwise |
| RT-13 | Ablation operator for a recurrent state unspecified | serious | ADOPTED — operator set pre-registered + dynamics-matched control |
| RT-14 | `d` metric doesn't transfer: unbounded cull pool, chance floor | serious | ADOPTED — frozen items, cull ceiling, chance-corrected `d` |
| RT-15 | Ethics precondition is nominal (no owner/date) | worth-noting | ADOPTED — owner+date required in the registration; non-promotable tags |

## The three fatal findings, in full

### RT-01 — the register may be a keyed memory array

**Attack.** The draft never fixes whether there is one register or N (one
per agent). With N symmetric registers and the model owning index 0,
"self" is a slot address fixed by which index the loss queries. Ablating
register₀ destroys T_sr; ablating register₁ spares it. That crossed
dissociation *is* the H_center fingerprint, and a content-addressed
memory array containing no self-indexing produces it with certainty. The
system would behave identically if slot 0 were named "agent Q." With one
register, the self/other asymmetry is architectural rather than learned
and the matched-capacity control has no matched object.

**Why it bites.** Every gate in v0.1 passes. The paper reports
"self-indexing can be architecturally centralized." The mechanism is a
labeled dict.

**Patch (adopted).** Three probes a keyed slot and a center answer
differently: (1) **register swap** — exchange self and other register
contents; a keyed slot gives a tidy content relabel with all other
integration intact, a center gives global disruption; (2) **mid-episode
re-indexing** — change which agent the model is at turn k; keyed memory
follows the slot, a center pays a re-centering cost visible in non-self
integration too; (3) **address probe** — if the register decodes agent
identity at AUC ≥ 0.95 independent of episode content, it is an address.
New registered bin **self-index-not-established**, the direct analog of
Experiment 1's RT-09 "reflexivity not established" — a gate v0.1 dropped
while inheriting the objection.

### RT-02 — the self-identification bootstrap trilemma

**Attack.** For the curriculum to be solvable the model must establish
which agent it is, and there are only three routes: **told** (an identity
token — identity supplied from outside, precisely the corpus's
"represents itself from outside"); **stylometry** (its own sampled text
is distributionally distinct from grammar-generated distractors —
self-recognition by fingerprint, fully explained by mimicry, which the
standing rules say to discount); or **teacher-forced** (its "own" turns
are designated turns in a static transcript it did not produce — third-
person tracking, not self-reference). All three yield H_center; none
supports the claim.

**Patch (adopted).** The only non-disqualifying grounding is *causal
authorship*. Therefore, registered rather than deferred: on-policy
training mandatory (commitments are the model's own sampled outputs); no
agent-identity token, header, or persistent positional convention;
style-canonicalization of all commitments at baseline and eval. **Loss
condition:** if T_sr collapses under canonicalization, the model was
doing stylometry and no H_center attaches; if identity must be supplied
by a label for the task to be learnable, the anti-router curriculum is
unbuildable in the required sense.

### RT-03 — the unloseability guard is a sentence, not a test

**Attack.** "The architecture must leave a residual path capable of
carrying the binding" has no test of "capable," and is trivially
satisfied by any transformer whose attention reaches prior turns. The
real determinant is whether *this* optimizer on *this* curriculum finds
the residual route — set by choices v0.1 defers to §Decisions, plus one
it never names: **whether attention spans the whole episode or is
windowed per turn.** Windowed ⇒ the register is the only cross-turn
channel ⇒ H_center guaranteed. So the registered prediction's truth value
is fixed by an unregistered decision made after registration.

**Patch (adopted).** A **no-register twin**: an identical model with the
register removed from initialization, same curriculum, budget, seeds. It
must reach held-out binding accuracy within a pre-committed margin — then
the residual path is *demonstrated* and H_center is loseable. If it does
not, the outcome is **void (architectural bottleneck)**, never H_center.
Cross-turn attention span, injection mechanism, and register width move
out of §Decisions and into the registration. No auxiliary loss on
register content and no hand-specified self-writing update rule — that
would be designing the answer in.

## The highest-value finding

### RT-12 — the missing arm is worth more than the headline

v0.1 claimed an H_center result would make Experiment 1's null "more
readable as absence than instrument failure (Q1)." That does not go
through: MVM-0a runs *no localization instrument at all* — that is its
advertised advantage — so a result obtained without running the
instrument cannot bear on whether the instrument works.

But the design is one step from answering Q1 properly. **Added as a
registered arm:** run Experiment 1's full localization pipeline (linear
probes, activation patching, SAEs where trainable) on MVM-0a **blind to
the register's location**, and ask whether the instruments recover a
center that is known-by-construction to exist and to be load-bearing,
and whether their ablation reproduces the designated-object damage
profile.

This is a ground-truth testbed for the entire program's interpretability
toolkit. **If the instruments fail to recover a center known to exist,
Experiment 1's null was instrument failure** — a bigger finding than
MVM-0a's own headline, and one v0.1 was structurally unable to notice.

## The finding John adjudicated

### RT-04 — the removal test's discriminating half is missing
**Resolved 2026-08-04: option (b).**

The corpus's operational test is a *contrast*: removal either degrades
the integrated act (center) or subtracts a report while processing
continues (description). v0.1 concedes it cannot produce judgeable
self-report and substitutes forced-choice self-identification — but that
is a task scored like T_sr, drawing on the same information. **There is
no reachable result in which the report is subtracted and processing is
intact.** H_description has been engineered out of the outcome space, so
an H_center label would carry a meaning derived from a contrast the
experiment never ran.

Two honest options were put to John, who chose **(b)**:

- **(a) Build a real report channel** — a separate head or turn type
  whose job is to *describe* current state rather than apply it, trained
  and verified to dissociate from T_sr at baseline, so "report
  subtracted, task intact" is an observable state of the world.
- **(b) Drop the corpus framing** — rename the bins, register the weaker
  claim the design actually supports, and state that MVM-0a does not
  instantiate the removal test.

The pass explicitly rejected v0.1's option of dropping the S arm while
keeping Experiment 1's vocabulary. Option (b) as adopted avoids that: the
S arm is retired **and** the bins are renamed (H_load-bearing /
H_generic-state / H_routed-around), so nothing borrows a meaning the
experiment cannot earn.

**Reasoning recorded at adjudication.** Building a report head was
rejected because its wiring would decide the answer — a head reading the
register dies with it by construction; a head reading the residual stream
reports on something other than the candidate center. And Experiment 1's
never-subtracted report was a finding *because* that channel was not
built by us; one we design ourselves is an artifact of our own wiring.
The reframe: "it is a mere self-description" was the live alternative for
a **stock** model where we did not know what was there. For a
deliberately constructed candidate center the live alternatives are
load-bearing, routed-around, or keyed slot — which is what the renamed
bins say. The cost, recorded in §Scope: a positive result is not a
demonstration that the corpus's floor was built, because the floor's
same-act clause is untested by retrieval through a consulted register.

## Remaining findings

**RT-05** (T_syntax vacuous): the curriculum randomizes turn markers *so
that* syntax carries no self-information, so `d(T_syntax) ≈ 0` is
near-certain and the differential clause is automatically satisfied
whenever `d(T_sr) ≥ θ`. Replaced with a **cross-turn state control**
(running counts, last-mentioned entity, event ordering) — state-requiring
but ownership-free, the actual competitor for register capacity — gated
on being demonstrably state-requiring (it must fail on a matched model
with cross-turn state removed).

**RT-06** (single run): the model is a draw, not a fixture, and
centralization-vs-distribution is textbook seed-sensitive. k ≥ 5 seeds,
verdict requires a pre-committed majority, across-seed spread is the
primary uncertainty. New bin **seed-dependent**. The cost excuse
Experiment 1 had does not exist here — these models train for tens of
dollars.

**RT-07** (trajectory): the register is the shortest path and is
plausibly used early then abandoned, so a saturating stopping criterion
leaves free choice among checkpoints. Ablation battery runs on a fixed
checkpoint schedule; verdict read at budget exhaustion; bin flipping
across the final three checkpoints returns **unstable**. Note the pass's
observation that "used then abandoned" may be the most interesting
finding available here, and v0.1 could never have seen it.

**RT-08** (cue detector): three holes — it runs pre-training so it cannot
see the on-policy fingerprint cue; it scans text while the model consumes
**tensors** (turn-type embeddings, segment ids, loss-mask-correlated
padding); and "near chance" with unspecified classifier capacity accepts
underpowered nulls, the exact error RT-10 caught empirically in
Experiment 1. Patch: three runs (text, input tensors, post-training
rollouts), a pre-committed equivalence bound (AUC CI within [0.45,
0.55]), and a positive control on a deliberately leaky variant.

**RT-09** (bypass unguarded): a dead injection gate, bad init, or
LayerNorm swamping the register produces "all d below θ with clean
gates" — and v0.1 attaches an *upstream reporting obligation* to that
outcome. A training bug would propagate into the philosophy repos as a
correction. **Register-utilization gate** required before any H_bypass
reading: attention mass above a floor, causal path patching showing the
register is live for something, non-negligible gradient flow through the
write path. Failing any → **construction failure (register unused)**,
nothing goes upstream.

**RT-10** (threshold fitting): Experiment 1's pilot was a *different
model* (gemma-2-2b-it) by design; here the pilot is the same architecture
on the same curriculum, so `d(T_sr)` on the pilot **is** the registered
quantity up to a seed. θ and δ must be null-calibrated on the registered
model — the move Experiment 1 already made for its OOD bound. Any pilot
*ablation* result read before threshold lock voids the lock.

**RT-11** (ownership vs content): the curriculum decorrelates ownership
from turn syntax and nothing else, so "mine" may be recoverable by
coherence clustering with no ownership representation anywhere. Hard
curriculum property: the same commitment content must appear self-owned
in some episodes and other-owned in others, balanced. Plus a
forced-revision eval (the model's own commitment inconsistent with its
prior behavior) that a coherence solver fails and an ownership tracker
passes.

**RT-13** (ablation operator): the register is a recurrent state with a
trajectory; "mean-ablate" replaces a time-varying signal with a constant
and removes cross-turn *dynamics*, not merely self-content — which looks
exactly like H_center. Operator set pre-registered (mean over which
index, zero, noise) plus a **dynamics-matched control**: random state of
matched norm *and* matched temporal autocorrelation. If that restores
T_sr, the register's content was not carrying the binding.

**RT-14** (metric transfer): (a) items come from a generator, so culling
to ceiling can run unbounded and selects the subset this model solves by
whatever shallow heuristic it found — a researcher degree of freedom
applied after the model exists. Freeze items before training, pre-commit
a cull ceiling, halt if exceeded. (b) Forced-choice batteries have a
chance floor: `d` maxes at `1 − 1/N`. Use chance-corrected
`d = (B_base − B_abl)/(B_base − 1/N)` and report N everywhere.

**RT-15** (ethics nominal): a precondition with no owner is a note, not a
gate — and MVM-0a is not a discardable prototype, it is precisely
MVM-0b's substrate, one config change away. Name an owner and date for
the corrigibility document *in the registration*; tag MVM-0a checkpoints
non-promotable; require any run adding a maintained boundary or
compute-gating stakes to cite the corrigibility document's commit hash in
its own pre-registration.

---

# Pass 2 (2026-08-09) — on the gate-(iii) fix

*Target: the adjudicated disposition for the gate-(iii) failure — (c)
in-context generation composed with (a) calibrated fill, RT-11 folded
in (John, 2026-08-09). Full analysis, the resulting design, and the
decision put back to John: `fill-disposition-fix-spec.md`. Dispositions
below are the drafter's recommendation; nothing is registered until
John adjudicates the fix-spec §Decision and the amendment lands.*

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| RT-16 | Naive in-context generation is a computational no-op | fatal (vs fix as stated) | RECOMMENDED — fix must be architectural, not pipeline; see spec §Design |
| RT-17 | Trilemma closes: exchangeable ⇒ unlearnable; (a)-only cannot win | fatal (vs (a) alone); upgrades RT-02 | RECOMMENDED — acting channel (efference copy) + uniform draws; RT-17 reported upstream regardless |
| RT-18 | An acting mask collated into the batch is an identity tensor | serious | PATCHED in spec — acting schedule is harness control flow; run (ii) re-specified |
| RT-19 | Frozen-text T_sr has no acts in it; latent in old pipeline too | serious | PATCHED in spec — freeze skeletons, enact at eval under frozen seeds; pilot T_sr caveat noted |

### RT-16 — naive in-context generation is a no-op

The forward is deterministic given tokens; a fresh forward over a
filled episode recomputes exactly the generation-time states, and
`model_fill_batched` already conditions pass-k samples on pass-(k−1)
fills. Sharing the KV/register cache changes wall-clock, not
information — implemented as stated, (c) re-fails gate (iii)
identically. Continuity of state must be *made*, not cached.

### RT-17 — the trilemma closes

If episodes reach the model as tokens only, machinery is symmetric,
and own turns are exchangeable with generator turns (what arm B
demands, since the attacker holds the policy), the input distribution
is invariant under own_slot relabeling and no function of the inputs
identifies ownership above chance: unlearnable. Contrapositive: every
learnable ownership signal in a token-only interface is arm B's
statistic. On-policy fill's "causal authorship" was route-2 stylometry
all along; gate (iii) found the theory gap, not a bug. (a)-only
therefore either fails the gate or starves T_sr — a registered-quality
wager, falsifiable for ~$6. Upstream obligation attaches to RT-17
itself: own-ness is not learnable from exchangeable data through a
pure token interface.

### RT-18 — the acting mask is an identity tensor if collated

Patch: sampling events are execution, not data; the model-visible
interface carries tokens, turn ids, marker keys, and motor-copy
injections only. Run (ii) audits that interface with the acting
channel disclosed; arm B's positive control becomes policy-sampled
enactment (the old pipeline).

### RT-19 — eval-time authorship

Frozen batteries freeze own turns as unauthored generator text
(`parse_battery_item` never reconstructs own_slot) — "you" over turns
the model never enacted, latent in the old design and undefined under
the new one. Patch: freeze episode skeletons + per-item draw seeds;
the checkpoint enacts its own turns at eval; answers re-derived
mechanically. Cull ceiling and pre-commitments unchanged.
