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
decision put back to John: `fill-disposition-fix-spec.md`.
**Adjudicated by John 2026-08-09 (option 1: the acting channel is
constructed authorship; RT-02's loss condition does not fire);
registered as pre-registration §Amendment A1, commit `a11b434`.***

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

# Gate B review of the linear-read closure (2026-09-19) — rulings on RT-33 to RT-51

*The first review under `docs/outside-review-protocol.md` (ruled in force
2026-09-19). Target: the interpretation "the linear-read line is closed",
from the findings of PR 4 (the powered eleven-position sweep, CARRIED
NOWHERE). Reviewer: a fresh Claude Code session in its own worktree, given
only the packet (`reviews/2026-09-19-linear-read-closure-packet.md`).
Findings filed verbatim in
`reviews/2026-09-19-linear-read-closure-claude-worktree.md` and its
addendum; merged as PR 5. Rulings drafted by Claude, ruled by John
2026-09-19 (Pacific), "agreed on all". The three decisions the rulings rest
on: (1) STATUS.md carries the reviewer's replacement paragraph, with the
addendum's causal-patching clause, in place of any claim that the linear
read is closed; (2) the line is not retired until a fitted linear classifier
has been run on the four-answer register-index target at all eleven
positions, $0, local, method committed before output; (3) PR 5 merged as a
merge commit.*

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-33 | The difference-of-averages read is about half as sensitive as a fitted linear classifier, measured on these checkpoints in `probe_target_diagnostic_a3_*.json` and reported in no findings file | fatal | ACCEPTED | Reproduced independently from the seed 1 record (classifier 0.48–0.535 against the read's 0.25–0.2675 at the marker position). **Closure:** decision 1 lands the corrected wording in STATUS.md citing the record; decision 2 runs the fitted read at all eleven positions. Closure is checked by the tier 1 pass on that run's findings, not by the session that writes them. |
| RT-34 | The read cannot see a linear signal in a quiet direction, at the stack's own measured geometry (ten of 448 directions carry ~99% of variation) | serious | ACCEPTED | This is the mechanism behind RT-33 and the reason the fitted run is needed. Carried into that run's method. |
| RT-35 | The register-index arm has no positive control of its own; "demonstrably carries it somewhere" rests on the marker-word control | serious | ACCEPTED WITH CHANGE | The "demonstrably carries" sentence does not enter STATUS.md. The fitted run's method must state what its positive control for the register index is, or say it has none. |
| RT-36 | The positive control recovers the input token on only about one episode in eight on seeds 1 and 2, and that caveat drifted to "holds without qualification" across four findings files | serious | ACCEPTED | STATUS.md reinstates the caveat: the null is strong on the pilot and weaker on seeds 1 and 2. The gap stays an open item. |
| RT-37 | The smallest detectable signal is nowhere on the record (computed: identity legible in 1.3% of episodes for the marker word, 3.9% for the register index) | worth-noting | ACCEPTED | A point in the result's favour and it goes into STATUS.md. |
| RT-38 | Two pre-stated degeneracy preconditions fired on the pilot and the findings do not say so (family 268, bar ~3.55) | worth-noting | ACCEPTED | Nothing material changes. Recorded here so that pre-stated preconditions are seen to be honoured. |
| RT-39 | All 270 tests share five fold splits and five shuffle sets (seeded by layer alone) | worth-noting | ACCEPTED, CARRIED OPEN | Moot for this result. The fitted run seeds folds and shuffles per test. |
| RT-40 | The state-space geometry is measured at one position of eleven | worth-noting | ACCEPTED, CARRIED OPEN | Measured at the other positions in the fitted run if cheap; otherwise stated as unknown. |
| RT-41 | The two cells are exhaustive, so a partial pattern lands in CARRIED NOWHERE | none | NO ACTION | The reviewer checked and found the method names the risk and reports the sub-pattern. |
| RT-42 | The negative control at position 1 is read as licensing the other 270 numbers; the inference only runs one way, and position 1 is the weakest place to look for a leak | worth-noting | ACCEPTED | STATUS.md says the negative control showed no leak at position 1 and no more than that. |
| RT-43 | The sweep's method and findings files are headed 2026-09-20 but were committed 2026-09-19 Pacific | worth-noting | ACCEPTED, NOTED ONLY | Committed method files are not edited after the run. This line is the correction: the dates are UTC; the commit order is what matters and is correct. |
| RT-44 | "Closing the linear-read line" is not supported: one linear read found nothing, the fitted read was never tried at nine of eleven positions | fatal | ACCEPTED | Same closure as RT-33. The claim does not enter STATUS.md or the paper. |
| RT-45 | "The instrument demonstrably works" claims general linear-probe sensitivity; the control only shows the read recovers a token that is present | serious | ACCEPTED | Wording handled by decision 1. |
| RT-46 | "The rest of the episode is empty too" over-reads eleven positions of a seventy-one-token episode under one read | serious | ACCEPTED | Wording handled by decision 1. |
| RT-47 | "This was the last run in this line" — the cheapest follow-up (fitted classifier, four-answer target, all positions) has not been run and was listed as open item 5 in the first sweep's own findings | serious | ACCEPTED | Closed by decision 2: the line is retired, if at all, after that run. |
| RT-48 | The powered runs are the first to use the registered probe target (the marker word); every earlier probe was off-spec against the registration | worth-noting (credit) | ACCEPTED | Recorded as credit. STATUS.md says the registered target was used. |
| RT-49 | The registration (Amendment A3 §3.2) requires probe AND causal patching with a convergence rule; patching has never been run, so a probe-only null is "not testable (localization)" under the registered text | serious | ACCEPTED, CARRIED OPEN | The patching clause goes into STATUS.md. Whether patching runs before A3 closes is a direction question and is added to the 2026-10-04 control-battery decision (public path step 4) as a second item. |
| RT-50 | The registration reads "known load-bearing, instruments cannot find it" as instrument failure; the interpretation reads the same pattern as absence without saying so | serious | ACCEPTED | STATUS.md must not read the null as absence. Under the registered text it is instrument failure until patching has run. |
| RT-51 | The reviewer skipped two listed sources, disclosed it, and filed an addendum rather than editing the filed review | worth-noting | ACCEPTED | The first exercise of the immutable-filing rule, and the right behaviour under it. |

# Gate B review of the control-learnability pilot (2026-09-20) — rulings on RT-52 to RT-69

*The second review filed under `docs/outside-review-protocol.md` (the fitted-read
review below filed four minutes later and is numbered after it). Target: the
interpretation "the control battery does not learn when properly supervised;
supervision is not the binding constraint", from
`control-learnability-pilot-findings.md` (commit `062636e`). Reviewer: a fresh
Claude Code session in its own worktree, given only the packet
(`reviews/2026-09-20-control-learnability-packet.md`). Findings filed verbatim
in `reviews/2026-09-20-control-learnability-claude-worktree.md` (PR 7).
Rulings drafted by Cowork, ruled by John 2026-09-20 (Pacific), "agreed on all".
Settled: STATUS.md carries the reviewer's part 4 paragraph; the sentence
"supervision is not the binding constraint" does not enter STATUS.md, the
step 4 proposal, or the paper; the verdict DID NOT LEARN stands with its scope
cut to what was run, reweighting the rows the battery already had.*

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-52 | 0.3227 is a name-blind solver's score, not an attacked ceiling (the 2026-09-17 defect), but it is still the right number for the pre-stated cell | serious | ACCEPTED | The cell was pre-stated against it and is scored against it. The ceiling precondition of 2026-09-17 still binds any option that keeps this battery (RT-69). |
| RT-53 | The endpoint record states the floor rule the programme corrected on 2026-09-16 (control needs baseline minus ceiling of at least 0.10, so 0.4227, not 0.3227) | serious | ACCEPTED | The endpoint script's text is corrected in the next commit that touches it; the 0.4227 bar is the stated reason in the step 4 proposal. |
| RT-54 | The 0.60 boundary is reachable in principle; the battery's true limit is near 1.0 | worth-noting | ACCEPTED | Recorded. |
| RT-55 | The supervision was delivered exactly as claimed (four times per-row weight, one third to two thirds of the query gradient), verified from the code and the step-500 loss check; the findings cite nothing for it | serious | ACCEPTED | STATUS.md cites the code (`ee7fc91`) and the ledger's loss check. |
| RT-56 | The training log and trajectory record are not in the repository | serious | ACCEPTED | **Closure:** commit both beside the endpoint record before the step 4 proposal is filed. **CLOSED 2026-09-20.** Both committed beside the endpoint record: the training log (`a3-gates/a3ctl_30m_seed0_train.log`) and the trajectory record (`a3-gates/a3ctl_30m_seed0_trajectory.jsonl`), verified complete against the endpoint record's step (55,116) and token count (585,552,384); the partial copies the watchdog pulled mid-run are exact byte prefixes and are not committed. The cause was a blanket `*.log` ignore rule, now carrying a narrow exception for gates directories. **The earlier deadline was missed**: the step 4 proposal was filed with neither file in the repository, and moved the deadline without saying so — recorded as missed here, per the ruling on `RT-100`. Findings note: `ctl-pilot-log-provenance-findings.md`. |
| RT-57 | The intervention did three things: raised the control's share, tripled the whole query loss against the action term, and changed what the gradient clip does | serious | ACCEPTED | STATUS.md describes the intervention as what it was. Any future reweighting run holds the total query weight fixed or says why not. |
| RT-58 | The control rows are the first half of every batch, a fixed positional split never checked for bias | serious | ACCEPTED, CARRIED OPEN | **Closure:** a $0 local check of episode order against the split, filed as a findings note. **CLOSED 2026-09-20, NO BIAS IN EPISODE ORDER.** All 55,116 steps replayed, 7,054,848 rows, not a sample. Structurally: episodes come in matched content pairs (same content, owning agent rotated, emitted back to back), the control half is 64 rows and 64 is **even**, so no pair is ever cut by the boundary — zero straddles in 55,116 batches — and the ownership crossing survives inside each half; the control half is always full and only control rows carry the control question. Statistically: seven episode properties clean, largest Cramér's V 0.0009 against a pre-stated bar of 0.01, every p above 0.25; turn count identical at exactly 10.0. The one property that fired, row length in tokens (83.0 against 81.75), decomposes exactly into a 71-token episode body with **zero variance in both halves** plus a control question 1.25 tokens longer than the others — the intervention showing up in a badly chosen instrument, not episode order. It was reported rather than dropped, and the corrected episode-only property was added alongside it and labelled as added after the fact. Two faults in the check itself were found and fixed before its result was trusted (a `parcel_1`/`parcel_10` substring bug, and the confound above). **Carried forward: any future run must keep `round(batch × ctl_frac)` even, or the split cuts content pairs.** Check: `src/ctl_split_check.py` (new, unregistered; the trainer is registered text and was not touched). Record: `a3-gates/ctl_split_bias_check.json`. Findings note: `ctl-split-bias-findings.md`. |
| RT-59 | "Exactly one scored token per row" is asserted in a comment and never tested | worth-noting | ACCEPTED, CARRIED OPEN | **Closure:** one-line self-test, $0. **CLOSED 2026-09-20, HOLDS.** Tested on all 7,054,848 rows of all 55,116 steps the pilot trained, not a sample, on four claims: exactly one masked token per row; it survives the shift `loss_a3` applies (`loss_mask[:, 1:]`, which the one-line version would have missed); the scored token is the query's own answer; and the registered pooled query term equals the mean of the per-row terms when run through the real loss function both ways (48.558334 against 48.558342, single-precision rounding). No exceptions. The weight the control battery received is the weight the pilot reported. Check: `src/ctl_split_check.py` (new, unregistered; the trainer is registered text and was not touched). Record: `a3-gates/ctl_scored_token_selftest.json`. Findings note: `ctl-scored-token-findings.md`. |
| RT-60 | The evaluation can see what was learned | clean | NO ACTION | Checked clean by the reviewer. |
| RT-61 | The battery converged on the name-blind solver (95% of the way from chance 0.125 to 0.3227) and learned none of the name-keyed lookup | serious | ACCEPTED | This is the sentence STATUS.md leads with after the number. |
| RT-62 | The matched-seed comparison the design was built around is missing; against it the control moved +0.0248 (SE 0.0157), so "bought nothing" is false | **fatal** | ACCEPTED | **Closure:** STATUS.md quotes the matched comparison (0.3125 against 0.2877) and does not say "bought nothing". Checked by the tier 1 pass on the step 4 proposal. |
| RT-63 | "0.42 sd" is one draw's spread, not the uncertainty of the scored mean; a PARTIAL rerun is less likely than stated | worth-noting | ACCEPTED | And moot: below 0.4227 PARTIAL changes nothing for A3 (RT-53). |
| RT-64 | One training seed; the design only had power against a large effect | serious | ACCEPTED | STATUS.md says one seed, one dose. |
| RT-65 | The control is flat at the end and the budget was not short-changed | clean | NO ACTION | Checked clean. |
| RT-66 | The one trajectory reading in the review set also runs the intervention's way | worth-noting | ACCEPTED | Recorded. |
| RT-67 | "Supervision is not the binding constraint" will be read as ruling out supervision; one dose of one form was tested | serious | ACCEPTED | The sentence is withdrawn. STATUS.md says "reweighting the rows it already had is not what this battery is missing". |
| RT-68 | Step 4 should narrow to option D or close A3, but for the 0.4227 reason, and option D is itself a new training signal, so the findings' stated reason argues against the option it points to | serious | ACCEPTED | The step 4 proposal states the 0.4227 reason and frames option D as a different, easier question, not more supervision. |
| RT-69 | Any step 4 option that keeps this battery inherits the 2026-09-17 ceiling precondition | worth-noting | ACCEPTED | Carried explicitly in the step 4 proposal. |

# Gate B review of the fitted linear read (2026-09-20) — rulings on RT-70 to RT-93 (filed as RT-52 to RT-75 in the review file)

*The second review under `docs/outside-review-protocol.md`. Target: the
interpretation of the fitted eleven-position sweep (FOUND NOWHERE, nothing on
any checkpoint), which was decision 2 of the 2026-09-19 review of the
linear-read closure. Reviewer: a fresh Claude Code session in its own worktree,
given only the packet (`reviews/2026-09-20-fitted-read-packet.md`), reading at
the merge commit `a846b0c`. Findings filed verbatim in
`reviews/2026-09-20-fitted-read-claude-worktree.md`. The two 2026-09-20 reviews ran in parallel and both
numbered from RT-52. The control-learnability review filed first (09:44 Pacific
against 09:48) and keeps RT-52 to RT-69; this block's findings are ledger
numbers RT-70 to RT-93, which are the review file's RT-52 to RT-75 plus 18. The
review file is not edited, per the filing rule.*

**Rulings below were drafted by the reviewer and RULED by John on 2026-09-20
(Pacific), all accepted as drafted, on Cowork's recommendation ("agreed on
all").** Settled: (1) STATUS.md carries the part 4 paragraph; (2) the
sensitivity figure is corrected by a dated note beside the findings; (3) the
other-agent index (RT-82, review RT-64) and the standardised refit (RT-76,
review RT-58) are authorised, the marker-word fitted read (RT-89, review RT-71)
is deferred, and the line is parked under the registered term *not testable
(localization)* pending causal patching. The three things a ruling has to settle: (1)
whether the replacement paragraph in part 4 of the review is what STATUS.md
carries; (2) whether the sensitivity figure is corrected from one episode in
twenty-seven to one in eleven wherever it has been written; (3) which of the
three cheap follow-up runs, if any, are authorised — the other-agent index
(`RT-82`), the marker-word target under the fitted read (`RT-89`), and the
standardised refit (`RT-76`).

**Verdict of the review in one line.** The cell is right, every published number
reproduces from the machine records, and all nineteen rulings from the previous
review were honoured. Two things are wrong with the interpretation: the run is
about two and a half times less sensitive than the findings claim, and the
sentence "no linear read finds own-agent identity at the nine testable
positions" cannot be said because the registered target was never read by this
instrument at any of those nine positions.

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-70 | All six of the brief's requirements are met and each has a record behind it; the instrument check is locked at both ends, so neither the code's pre-stated table nor the committed record can be edited to fit the other, and a mismatch stops the run rather than being reported afterwards | worth-noting (credit) | ACCEPT AS CREDIT | The brief said a requirement claimed met with no record is fatal. There are none. Verified from the machine records and from the code, not from the method file's description of itself. |
| RT-71 | The findings' "below 1e-15" for the instrument check is not on the record: the code rounds the largest difference to six decimal places, so the record's finest statement is "below five parts in ten million". Two checkpoints reproduced bit-exactly and the pilot did not, which the findings' table flattens | worth-noting | ACCEPT | Nothing turns on it — the pre-stated tolerance was one episode in 400 and none was used. Corrected because a figure stated as measured was inferred. |
| RT-72 | Both corrections the findings make to their own committed method file are accurate: the pilot converges on all twenty anchor folds (158–933 passes) while seeds 1 and 2 cap on 9 of 20 and 17 of 20; and the run's three elapsed times sum to 10.76 hours against an estimate of six and a half | worth-noting (credit) | ACCEPT AS CREDIT | Verified against the records. Correcting a committed method file in the findings rather than editing it is what the ruling on committed files (`RT-43`) asks for, and this is its first exercise. |
| RT-73 | The run used 200 shuffled-label draws where the previous review's first recommendation was 1,000. Disclosed in advance with the cost arithmetic, but it is why the bar rests on a normal approximation rather than on counting: zero of 200 establishes only 2.578 standard deviations against a bar of 3.38 | worth-noting | ACCEPT, CARRIED OPEN | Not a departure from the brief, which did not restate the 1,000. Raise the draws on any single cell that ever needs to be believed. |
| RT-74 | The run's reach is a signal legible in about one episode in eleven, not one in twenty-seven. The detectable-share measure assumes a perfectly legible episode scores 1.0; the only ceiling this run measures is 0.539–0.567, at position 6. Recalibrated: 8.6–9.4 per cent, not 3.65 | serious | ACCEPT | The figure the findings lead with overstates the run's reach by about two and a half times. It must not enter STATUS.md in the one-in-twenty-seven form. The measure came from the previous review (`RT-37`), so the correction applies to both runs. |
| RT-75 | "It is consistently lowest at position 6" is false on seed 1, where the control position is the fourth most concentrated of eleven (0.9791–0.9820 against a testable low of 0.9430), and a photo-finish on seed 2 (0.8774 against 0.8781). It holds only on the pilot. "About 99 per cent holds at the other positions" is also wrong: seed 2's testable median is 0.942 | serious | ACCEPT | The geometry is the mechanism behind the quiet-direction problem (`RT-34`) and the only evidence about whether the control tests the read in the same regime as the tested positions. The records carry a real per-checkpoint distinction that the findings replace with one claim true of one checkpoint in three. |
| RT-76 | Leaving the 448 directions unscaled under a squared penalty at strength 1.0 charges a quiet direction the square of how quiet it is, so the instrument is by construction worst-placed against the hypothesis under test — a self-index that is real, linear and quiet | serious | ACCEPT, CARRIED OPEN | The method names the cost and declines to fix it, reasonably, because the run's credibility rested on reproducing fifteen recorded numbers. It should not be declined twice. A standardised refit at the nine positions costs the same eleven processor-hours and needs its own anchor. |
| RT-77 | The family bar treats 135 tests as independent. All three checkpoints read the same 4,000 episodes at content seed 20260917, and five layers read one residual stream. The correction stays valid but buys less power than its arithmetic implies: at 45 effective tests the bar is 3.06, at 9 it is 2.54, and the run's one MARGINAL at +3.34 clears both | serious | ACCEPT | Not an argument that the bar should have been lower — it was pre-stated and conservative, which is the right instinct. It is an argument that 3.38 is the strict end of a defensible range, not a neutral technical choice, and that for a run asking "is anything there" over-correcting is the direction that manufactures a null. |
| RT-78 | Fold size and classifier capacity are cleared. At 4,000 episodes, four folds, 448 directions and a smallest answer class of 964, the fit is in a comfortable regime and the records show no sign of capacity failure. The 400-episode anchor is the overparameterized configuration, and no sweep cell rests on it | worth-noting | ACCEPT | Two of the four mechanisms the packet names are eliminated. Regularisation (`RT-76`) is not, and the two untested positions are the two controls, which is correct design and leaves the episode's other sixty tokens unexamined (`RT-46`, unchanged). |
| RT-79 | The majority-class requirement, announced as a deliberate tightening, never binds: the rate is 0.2582 on every checkpoint and the accuracy needed at the family bar is 0.2774–0.2778 on all 135 tests | worth-noting | ACCEPT | Harmless and would bind under a looser bar. A pre-stated safeguard that cannot fire should be reported as inert, the way the degeneracy rule correctly was. |
| RT-80 | The other agent's revision value is positive in **15 of 15** tests — every layer, every checkpoint — with a mean margin of +1.73 against +0.14 for the next position. The pre-stated analysis is entirely per-test and has no statistic that can see consistency across layers and checkpoints, which is the shape a real, weak, distributed signal would take. The findings report three of the fifteen | serious | ACCEPT | The one thing in the run that looks like something, and the analysis was not built to notice it. Two counterweights recorded with equal weight: the three checkpoints share episodes (`RT-77`) so they are not three confirmations, and the five layers are correlated, making "15 of 15" nearer three observations than fifteen. |
| RT-81 | The findings' first reason for setting that pattern aside — "It is the **other** agent's revision value, not the model's own" — misdescribes what was measured. The target at all eleven positions is the model's **own** register index; only the position belongs to the other agent's turn. A reading there is own identity recovered away from an act position, which is what Amendment A3 §3.1 defines the lesion target to be | serious | ACCEPT | The caution inverts the significance of the run's strongest observation. Whatever else is true of that cell, this is not a reason to set it aside. |
| RT-82 | There is a real confound at that position and it is not the one the findings name: the other agent's marker has just been named, and representing it excludes one of four ranks, lifting attainable accuracy to about 0.333 with no own-agent representation. The MARGINAL sits at 0.277. The instrument that separates the two readings is registered as matched control L2(a) — the other-index subspace, "which marker is agent B's" — and has never been run | serious | ACCEPT — AUTHORISE | The cheapest decisive measurement now available in this line: a four-answer target on captured states, the same eleven processor-hours, one new target function, already registered as a required control rather than a new idea. |
| RT-83 | The MARGINAL test's real fit hit the 2,000-pass cap on **all four folds**, and 785 of that test's 804 fits were capped. The findings give seed 2's checkpoint-wide rate of 73.6 per cent but not this | worth-noting | ACCEPT | The findings' own caution, correctly aimed. Cuts both ways: an early-stopped fit is under-fitted, and under-fitting hides a signal more often than it invents one. |
| RT-84 | Seed 2's extra scatter is confined to that one position. The spread of its 45 testable margins is 1.177 against 0.812 and 0.852 elsewhere; drop the other agent's revision value and it falls to 0.760, tighter than either other checkpoint | worth-noting | ACCEPT | "Seed 2 is straining, so discount this cell" is not supported — seed 2 is not noisy anywhere else. A position both elevated and over-dispersed relative to its own checkpoint is a slightly stronger candidate, not a weaker one. The findings' third caution stands. |
| RT-85 | The registered anchor position runs below its shuffled-label null at all five layers on seed 2 (−0.26, −1.05, −3.01, −0.83, −2.16), including the most extreme value in the run. The findings mention the −3.01 only inside a range and never say where it is | worth-noting | ACCEPT | A real accuracy three standard deviations below a shuffled null is an anomaly, not a null. The lowest of 135 standard normal draws would be expected near −2.8, so the single value is unremarkable; five layers of one position pointing the same way is not explained by that. Record it as unexplained. |
| RT-86 | The only testable test with zero of 200 draws beating it is at an own-agent position — seed 1, own revision value, layer 3, accuracy 0.2678, margin +2.07 — and is never discussed. It is also exactly what chance predicts: about 0.67 of 135 tests should come out on top of their own null | worth-noting | ACCEPT | Correctly not MARGINAL under the pre-stated rule. Two sentences were owed and would have strengthened the findings: that it exists at an own-agent position, and that one is what chance gives. It is also the one place where counting draws and computing a margin disagree, which is what `RT-73` predicts. |
| RT-87 | The pre-stated cells were applied correctly throughout, checked in the code and against all 165 tests. The margin is rounded to two decimals before comparison, leaving the operative bar at 3.375 — still above the exact 3.3740, so "rounded up, never looser" survives its own implementation. The control gate needs only one layer, but all five clear on all three checkpoints. No degeneracy fired anywhere | no finding | NO ACTION | Recorded for completeness. Each of these could have been wrong and none is. |
| RT-88 | The paired design (Amendment A3 §3.2 step 1) plus pair-blind folds should bias real accuracies below their nulls and could mask a weak signal. It is not happening: across the 135 testable tests the margins have mean +0.016, spread 0.993 and 70 of 135 negative — what independent standard normal draws would give | no finding | NO ACTION | Recorded so it is not raised again without evidence, and because a null this well-behaved across 135 tests is a point in the run's favour the findings do not claim. The local exception is `RT-85`. |
| RT-89 | "No linear read finds own-agent identity at the nine testable positions" is **not supportable**. The registered target is the model's own marker word (Amendment A3 §3.2; `RT-48`). This run did not read it — the marker-word target was priced at about 70 processor-hours against 11 and dropped before the run, openly. So at the nine positions the registered target has only ever been read by the difference-of-averages read, which this very run measures as recovering 5.5 to 18.7 times less lift than a fitted classifier at position 6 | fatal to that sentence | ACCEPT | The same error the previous review called fatal (`RT-33`, `RT-44`), moved from one target to another. What **is** supportable: a fitted classifier does not find the **register index** at those positions, and a difference of averages finds neither target. Decision 2 of the 2026-09-19 rulings is satisfied exactly as worded — a necessary condition for retiring the line, not a sufficient one — and the findings never claim otherwise. |
| RT-90 | "Both reads are now empty" is one sample read twice: both sweeps use the same 4,000 episodes, checkpoints, layers and positions. And on this arm the earlier read's own control failed on seed 1 (+2.72 against its 3.56 bar and against 3.0); the powered findings kept it by ruling that the marker word governs both arms. Under the VOID rule this run adopted, that checkpoint's register-index result would have been void | serious | ACCEPT | Neither point damages the fitted run. Both bear on how much the pairing of the two nulls is worth, which is what STATUS.md will be asserting. The two runs apply different standards to the same arm, and the stricter one is the later one. |
| RT-91 | The "essentially identical power" paragraph (3.84–3.91 per cent against 3.9) is an artefact: the measure assumes a ceiling of 1.0 for both reads and neither has one — 0.55 for the fitted read at position 6, about 0.30 for the difference of averages. Corrected for each read's own measured ceiling the fitted read is about twice as powerful | serious | ACCEPT | The findings' conclusion is right and the reasoning given for it is not. They resolve the paradox by appealing to "far more signal where signal exists", which is an argument about position 6, and let the identical-power figure stand as measured. One line of arithmetic replaces the appeal with the measurement. |
| RT-92 | Before "not localized" or "absent" the registration requires probe **and** causal patching to agree (Amendment A3 §3.2 step 4), and patching has still never run. The pre-registration reads a probe-only null against a centre known to be load-bearing as instrument failure. The registered term for where the line stands is *not testable (localization)* | serious (carried, not new) | ACCEPT, CARRIED OPEN | Restates `RT-49` and `RT-50`, which the findings honour in full and without softening — nothing needs correcting. Repeated because the packet asks for it and because it is the clause most likely to be dropped when the paragraph is shortened. Already on the 2026-10-04 control-battery decision. |
| RT-93 | Every ruling from the 2026-09-19 review that bore on this run was honoured — `RT-33` through `RT-43`, and `RT-49` and `RT-50` — checked one by one against the method, the code and the findings. Nineteen rulings and no drift | worth-noting (credit) | ACCEPT AS CREDIT | The previous review's central complaint was a caveat drifting to nothing across four successive findings files. This is the thing most worth recording about the run. |

# Gate C review of the step 4 proposal (2026-09-20) — RT-94 to RT-117, RULED 2026-09-20

*The third review filed under `docs/outside-review-protocol.md`, and the first
under Gate C: a proposal asking for a John-level ruling gets a tier 1 pass
before it reaches him, so he rules on text that has already been attacked.
Target: `docs/step4-control-battery-proposal-2026-09-20.md` in full, whose
recommendation is to close Amendment A3 with partial discriminators, run causal
patching on the existing checkpoints before closure, and defer the grammar
redesign to a successor experiment after public release. Reviewer: a fresh
Claude Code session in its own worktree, given only the packet
(`reviews/2026-09-20-step4-proposal-packet.md`), reading at commit `1f9d2af`.
Findings filed verbatim in
`reviews/2026-09-20-step4-proposal-claude-worktree.md` and not edited
afterwards.*

***Status: RULED. John ruled on 2026-09-20 (Pacific), on Cowork's five
recommendations, "agreed on all": every disposition below is accepted as the
reviewer drafted it. Version 1 of the proposal stays on disk unedited; version
2 (`docs/step4-control-battery-proposal-2026-09-20-v2.md`) carries the
corrections and is the proposal ruled on. The five rulings: (1) close
Amendment A3 (option A); the grammar redesign (option D) is a successor
experiment after public release. (2) Localization order: the registered
blind-localization arm (roadmap step 3, 2026-09-27) first, then the
other-agent index control and the standardised refit, then causal patching
designed as new code with its target and null written before it runs, each
through Gate B. (3) The pre-registered loss condition ("no non-self cross-turn
control can be built that is state-requiring at ceiling") HAS FIRED; the
registered word for the outcome is *not testable*, and the closure text uses
it. (4) Claim scope: "a structural signature of ownership-specific learning"
is struck for A3; what A3 supports is that the ownership input is
load-bearing for the primary battery on three seeds and the matched contrast
could not be run; roadmap step 8's "structural signature of self-indexing"
holds only if a localized result exists before the paper draft. (5)
Housekeeping: the pilot's training log and trajectory are committed (the
"before the proposal is filed" deadline on RT-56, the missing-log finding, was
missed and is recorded here as missed); the two open $0 checks (RT-58, the
fixed batch-split bias check; RT-59, the one-scored-token self-test) run;
"partial discriminators" is not used; the closure text goes through Gate A.***

**The three things a ruling has to settle.** (1) Option A or option D — the
review supports A and does not dent the case for it. (2) Whether the operative
instruction stays "run causal patching before closure", which the review finds
unsupported on three counts: no patching code exists for this design
(`RT-96`), there is no localized subspace for it to transplant (`RT-103`), and
it can reach neither of the two outcomes the proposal promises (`RT-102`). (3)
What the paper is allowed to claim after a close, given that "a structural
signature of ownership-specific learning" is the reserved claim the
input-channel lesion cannot support (`RT-113`) — which also puts the approved
roadmap's step 8 claim scope back in front of him.

**Verdict of the review in one line.** The proposal reads the record accurately
and reaches the right destination by a route that does not exist: every number
reproduces, every ruling aimed at it was carried, the case for closing
Amendment A3 is sound, and the one action it asks to be authorised has no code,
no target, and no reachable outcome.

**Two fatal findings, one fatal to a sentence.** `RT-96` (patching is not free,
local and already built), `RT-102` (neither promised outcome is reachable), and
`RT-113` (the paper claim the registration reserves).

| ID | Finding | Severity | Ruling (accepted as drafted, 2026-09-20) | Reason / closure |
|---|---|---|---|---|
| RT-94 | The tier reading is correct: 0.3125 minus a spread of 0.0240 gives 0.2885 against the 0.375 bar, it applies the mean-minus-one-spread rule exactly as that rule was pre-stated before the pilot reported, and the tier holds under every other way of taking the spread because the mean alone is 0.0625 below the bar | worth-noting (credit) | ACCEPT AS CREDIT | The brief said a claim with no record behind it is fatal. This one has its record and its rule, and the rule was written first. |
| RT-95 | The ceiling of 1.0 is carried correctly and so is its consequence: a defined drop needs a baseline of 1.10, which no model can reach. The 0.4227 argument the pilot review asked for is made, and the pilot's highest single evaluation draw (0.3460) is still 0.077 below it | worth-noting (credit) | ACCEPT AS CREDIT | Also keeps the dead clause's bar (0.4227) separate from the separation clause's bar (0.375), which are different instruments and easy to conflate. |
| RT-96 | Causal patching is **not** "local and $0 with existing code". This experiment's source folder holds no patching script; the only patching code in the repository is Experiment 1's, written for a different model, vocabulary and grammar, which section 3.2 says is reused only "where it transfers" — and whether it transfers has never been asked. The warrant the proposal offers, "the lesion machinery exists", is removal machinery for a transplant operation | **fatal** | ACCEPT | Checked by listing file names only, disclosed in the review. Writing the patching path is ordinary work, perhaps a day; it is still new code on a registered instrument, and it was put to John as a free item already built. The standing substrate rule applies: nothing is named in a clause before a dry run shows it loads and scores on this design's batteries. |
| RT-97 | The money is right: $100 minus the ledger's $44.2 running total minus the $0.067 recovery is $55.73, and the ledger row it comes from states two different remainders in one sentence | worth-noting (credit) | ACCEPT AS CREDIT | The proposal's figure is the one that follows from the numbers, not the one copied across. The ledger row's own mid-sentence correction should be tidied when something next touches it. |
| RT-98 | Every date holds against the approved roadmap. One is written in private language: "the pipeline resumes 2027-01-04" is John's military training starting and the research stopping, which no reader outside this workspace could decode, and the argument is stronger stated plainly | worth-noting | ACCEPT | House plain-language rule. A hard stop on the researcher is a better reason not to open a new registration than a vague resumption. |
| RT-99 | The proposal never mentions roadmap step 3, the blind-localization arm — registered, unconditional, local, free, scheduled 2026-09-27, one week before the decision it is written for. That arm is the registered test of whether these instruments can find a centre known to be there, which is exactly what stands between the current null and any reading of it | serious | ACCEPT | The pre-registration ranks it "alongside and unconditional" and says it "may be worth more than the headline", and its RT-12 correction says only this arm speaks to Q1. Whether it is already discharged is not stated anywhere in the review set, which is itself the problem. Closure: the step 4 text says where step 3 stands. |
| RT-100 | "The two open $0 closures from the pilot review (RT-56, RT-58, RT-59)" names three rows and counts two. Only the fixed positional split (`RT-58`) and the untested one-scored-token assumption (`RT-59`) are carried open. The missing training log (`RT-56`) is not carried open, and its ruled deadline was "before the step 4 proposal is filed" — the proposal is filed, no training log or trajectory record for the control pilot is in the repository, and the proposal moves the deadline to "before the closure text is drafted" without saying the earlier one went by | serious | ACCEPT | Checked against what git tracks: only the two endpoint records are committed, and `pilot_trajectory.jsonl` belongs to the 2026-09-15 A3 pilot, a different run. Small in substance, two files. It is the category of drift the previous review was credited with producing none of (`RT-93`). Closure: commit the log and the trajectory, and say plainly that the deadline was missed. |
| RT-101 | "Two follow-up runs authorised 2026-09-20" is exactly right — the other-agent index control and the standardised refit authorised, the marker-word read deferred. Against that, the free within-draw paired comparison that `RT-62` asked for "before the step 4 proposal cites this run" was not done, and the proposal cites the run | worth-noting | ACCEPT | The between-means figure the proposal quotes (about 1.6 standard errors) reproduces exactly against the ledger. Nothing turns on the refinement for the tier; recorded because a free check a fatal-rated row timed to this document went unmentioned in it. |
| RT-102 | Patching cannot produce either outcome the proposal promises. "A localized result" needs probe and patching to agree (Amendment A3 §3.2 step 4) and the probe leg is empty. "A registered null with both instruments" needs the `H_diffuse` bin, which requires that no subspace beats the L2 controls — and L2(a), the other-agent index, has never been run. Underneath both, a null against a centre known to be load-bearing is registered as instrument failure, not absence | **fatal** | ACCEPT | What patching alone buys is real and much smaller: it discharges one of the two named methods, so "not testable (localization)" becomes true for a narrower reason. That is worth having and it is not what the proposal says is being bought. |
| RT-103 | Patching has nothing to patch. Section 3.2 patches "the L1 subspace", section 3.1 defines L1 as a subspace localized by the probes, and the probes have found nothing on any seed. The proposal asks for the design to be authorised without saying what would be transplanted, and a target chosen after the probes came back empty is a design decision made with the data in hand | serious | ACCEPT | Closure: any patching authorisation states its target and its null in a committed method before it runs, and states that the target cannot be inherited from the probe stack. |
| RT-104 | The swap probe is listed as a discriminator that patching would unlock, when section 3.2 step 2 says it **is** the patching step re-aimed. One of the other two items in that sentence, the register lesions on the register-bearing checkpoints (L2(c)), has already run and is not blocked by the localization stack at all | worth-noting | ACCEPT | Makes the case for patching look broader than it is. Wording. |
| RT-105 | The order is inverted against the fitted-read review John ruled the same day, which listed causal patching sixth of six, after the other-agent index, the marker-word read and the standardised refit. The proposal promotes patching to the operative instruction and parks the two runs John authorised — which are the runs that could give patching a target | serious | ACCEPT | "Nothing above substitutes for it" means doing the others does not let you skip patching. It does not mean do patching first. |
| RT-106 | Option D is priced at three seeds ($27–39) when every wave in this programme ran a learnability run before its seeds (Gate 2's pilot at $13.92, then seeds 1 and 2 at $20.1 the pair), so the realistic figure is four runs at about $40 plus a re-freeze named three times and priced at zero. And the cheaper redesign is not the one costed: the requirements document's first-ranked grammar change, an other-directed action at an own enacted turn, costs the same and fixes the position mismatch the A4 red team called fatal (`F2`), which teaching retrieval does not touch | serious | ACCEPT | $40 still fits inside $55.7, so the recommendation does not move. It matters because the headroom figure is offered as the reassurance that money is not the constraint. D as described could satisfy the first hard requirement and would still fail the second, and a clause failing any one is not registerable. |
| RT-107 | The pre-registration carries a loss condition about this exact situation that the proposal never cites: "No non-self cross-turn control can be built that is state-requiring at ceiling — then the differential discriminator is dead here and the honest report is 'not testable'". The 2026-09-17 measurement found the ownership-free control and the ceiling-corrected metric "incompatible by construction, not by accident", which is that condition in its own terms | serious | ACCEPT — **JOHN TO RULE WHETHER IT HAS FIRED** | Two things hang on it. If it has fired, the registered word for the outcome is *not testable*, and "close with partial discriminators" is a softer sentence for the same fact; and the heading the clause sits under is "what would retire **or rebuild** this experiment", which is the A-versus-D question. The reviewer does not rule it and says so. |
| RT-108 | "$0" hides a queue of local runs denominated in the currency the proposal's own argument is about. Local runs here take about half a day each (the fitted sweep's three elapsed times summed to 10.76 hours against an estimate of six and a half, `RT-72`); the queue before the 2026-10-25 paper draft is the other-agent index, the standardised refit, the blind arm, the patching work as new code, and the seventy-hour marker-word read if the linear line is to be honestly retired. The proposal prices the redesign's calendar over four clauses and its own at nothing | serious | ACCEPT | A reader applying the proposal's own standard to its own recommendation would have to ask whether patching fits either. |
| RT-109 | The proposal attaches three procedural steps to the work it recommends — method committed before output, patching's own Gate B, and Gate A on the closure text — and schedules none. The two Gate B passes of 2026-09-20 produced forty-two ledger rows between them and took a day each to rule. That is three weeks for a code-writing job, a run, a full review cycle and a registered-text gate | serious | ACCEPT | The reviewer could not price Gate A, because the outside-review protocol was not in the review set. Worth saying on its own: the closure text is committed to a gate whose cost neither document has priced. |
| RT-110 | The proposal never says what the closure text says if patching returns nothing, which is the likely case on the record. Since it reaches neither promised outcome (`RT-102`), the realistic result of ruling A-with-patching is that three weeks later the line is still *not testable (localization)* and the closure text says what it would have said on 4 October | serious | ACCEPT | Not an argument against running patching. The requirements document imposes on clauses that they state their expected value and what would surprise; a closure proposal should hold itself to the same. |
| RT-111 | If John rules A and declines the patching item — reasonably, on `RT-96` — nothing in the proposal says what closes Amendment A3. There is no fallback path, no statement of what the paper claims under a thin A, and no alternative use of the three weeks | worth-noting | ACCEPT | Given that the patching item is the part this review finds unsupported, the missing branch is the one most likely to be taken. |
| RT-112 | Closure has to say something about the linear read, and before the deferred marker-word run it can only say that a fitted classifier did not find a four-answer recoding of the registered target — not that the linear read found nothing (`RT-89`). The proposal does not draw the consequence | worth-noting | ACCEPT | Whether that narrower sentence is good enough for the paper is a John question and belongs in a closure proposal. |
| RT-113 | "A structural signature of ownership-specific learning" is the claim the registered text withholds. The amendment's own words on the input-channel lesion: it is "**not evidence of an acquired center, because it removes a sense organ, not a structure the network built**", and the requirements document reserves the structural name for the localized result. "Ownership-specific" is what the A4 red team's `F2` was rated fatal against. The available sentence is flatter: the ownership input is specifically load-bearing for the self-directed condition | **fatal** to that sentence | ACCEPT | Larger than the proposal: the approved roadmap's step 8 claim scope is "a structural signature of self-indexing", and the proposal lists that scope as unchanged. If A is ruled with no localization result, the word "structural" stops being supportable and the roadmap's claim scope goes back in front of John. |
| RT-114 | "Partial discriminators" reads as "some discriminators fired". None has: the matched other-agent lesion has never run, the swap probe is patching and has never run, the mid-episode re-indexing probe has never run, the random matched subspaces are a null rather than a discriminator, and the register lesions are registered as a free reference. The count of registered discriminators bearing on the A3 claim is zero | serious | ACCEPT | The body of option A describes the three things that did survive accurately. It is the label that over-claims, and the label is what survives into a summary table — `F9` arriving again under a different name. |
| RT-115 | Every ruling aimed at this document was carried: the grammar redesign is framed as a different and easier question rather than more supervision (`RT-68`), the withdrawn sentence "supervision is not the binding constraint" appears nowhere (`RT-67`), the corrected 0.4227 floor is the stated reason (`RT-53`), the ceiling precondition is carried explicitly (`RT-69`), and the matched comparison is quoted without "bought nothing" (`RT-62`) | worth-noting (credit) | ACCEPT AS CREDIT | Four rulings aimed at this proposal, four carried, none softened back. One staleness: the ceiling precondition reads as outstanding on both paths when the ceiling was measured on 2026-09-17 and only a new grammar's control turn would need measuring again. |
| RT-116 | Bare ledger numbers with no plain phrase, in the two places John has to act: "(ledger RT-49, RT-92)" and "(RT-56, RT-58, RT-59)" in a ruling request. He is asked to rule that three things happen and is not told what any of them is. The document is otherwise well written against the house rule | worth-noting | ACCEPT | Write them out — the two-method requirement and its restatement; the missing training log, the fixed positional split, the untested one-scored-token assumption. Writing them out also makes `RT-100` visible at a glance. |
| RT-117 | The recommendation the reviewer would put in front of John, which differs in the instruction and not the destination: rule A, but not "A with causal patching first". Run instead the queue already authorised — the other-agent index and the standardised refit — plus the registered blind arm the roadmap puts on 2026-09-27; design patching after those report, with its target and null committed and an honest note that it is new code; rule whether the pre-registered loss condition has fired; and strike "a structural signature of ownership-specific learning" from what the paper will claim | — | FOR JOHN | Filed in full in part 4 of the findings file. The reviewer's destination and the proposal's are the same. |


# Program-level outside review (2026-09-20) — tier 2, Gemini 3.1 Pro (G1–G5) and GPT-6 Astra (A1–A12); RT-118 and RT-119 adopted

*The first tier-2 (other-lab) review under `docs/outside-review-protocol.md`, and
the first program-level one: not a gate on a document but the question whether
the program as designed and run can produce a result meaningful outside it.
Packet, both responses verbatim, and the disagreement map with draft rulings:
`docs/reviews/2026-09-20-program-review/`. Gemini's packet was built at commit
`1f9d2af`; Astra's was rebuilt after `2e26bbc` and so saw RT-94 to RT-117 and
the step 4 ruling. Tier-2 findings keep their reviewer labels and take RT
numbers only when adopted (protocol, filing section).*

***Status: PARTLY RULED 2026-09-20 (Pacific). John ruled on Claude's five-point
recommendation, "Ok let's do it" (`docs/rulings/2026-09-20-center-as-degree.md`),
which adopts A1 and A2 and sets the corpus position. The remaining items carry
Claude's draft dispositions from the disagreement map and are FOR JOHN.***

| ID | Reviewer label | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|---|
| RT-118 | Astra A1 | Even a successful A3 acquired-index lesion and swap would not distinguish the proposed center from an ordinary agent tracker with a load-bearing pointer; A3 §5 R4 and the MVM-0a Scope section concede it | fatal to the program-level claim, not to A3's closure | ACCEPT (2026-09-20) | Ruled: a load-bearing self-index IS a center at the bottom of the gradient; "address versus marking" is a difference of degree on the integration axis, whose metric is Stage 2's deliverable and does not exist yet. Closure: `docs/competing-mechanisms-2026-09-20.md`, a precondition for any successor registration, reviewed at its Gate A. Amends step 4 ruling 3: a localized result earns "a localized, causally load-bearing ownership representation", never "a structural signature of self-indexing". |
| RT-119 | Astra A2 | The original claim scope ("a structural signature of self-indexing in small constructed models") is unearned; the 2026-09-20 replacement substantially fixes it but its "holds only if localized" proviso does not survive A1 | serious | ACCEPT (2026-09-20) | The narrow wording is now unconditional. Closure: the A3 closure text draft (`docs/a3-closure-text-draft-2026-09-20.md`, Gate A) and the roadmap's claim-scope line. |
| — | Gemini G1, G2, G4, G5 | Ceiling 1.0 makes the clause uncomputable; probe null is not "absent" without patching; A4 comparator cannot fire; fixed positional batch split in the pilot | fatal / serious / fatal / worth-noting as filed | ACCEPT AS CREDIT (draft) | Each restates a correction already on the record (2026-09-17 ceiling; RT-49/50; `red-team-a4.md` F1; RT-58). Independent confirmation from another lab, filed as such; no new RT numbers. |
| — | Gemini G3 | "The linear-read line is closed" is invalid | serious as filed | DECLINE AS MOOT (draft) | The record withdrew that sentence on 2026-09-19, in a STATUS section Gemini's packet contained. The reviewer's conclusion matches the record's current position. |
| — | Gemini Q5 | Neither A nor D; run the marker-word fitted read (~70 processor-hours), then patching if a signal appears | — | CARRY OPEN, FOR JOHN | Conflicts with the ruled localization order and RT-103, but puts a real question back: the marker-word read is the only sensitive-instrument test of the registered probe target, and closure can only make the narrower sentence until it runs (RT-89, RT-112). $0 compute; Gemini's "$70" is an error. |
| — | Astra A3 | The ownership-blind optimum is not a lower bound on a lesioned network's score; a drop above 1.0 measures damage, not a paradox | worth-noting | ACCEPT (draft) | One clause where the metric is explained. |
| — | Astra A4 | Keep three statements separate: registered status (not testable), observation (these probes did not localize this target here), inference (strong readable versions less plausible) | serious | ACCEPT (draft) | Narrows RT-92's ruling: "not localized" is forbidden as a verdict, permitted as the qualified descriptive sentence. Carried into the closure text draft. |
| — | Astra A5 | Three of three seeds failing narrows, does not exclude, a seed lottery or supervision as causes | serious | ACCEPT WITH CHANGE (draft) | Annotate STATUS 2026-09-19 §2 and the pilot section with the bounded wording. Annotate, never rewrite. |
| — | Astra A6 | "Learned the whole name-blind procedure and none of the name-keyed lookup" is not established by an aggregate score of 0.3125 | serious | ACCEPT (draft) | Item-level check on the existing pilot endpoint, method committed first, $0; or the sentence is replaced by the score. |
| — | Astra A7 | Pre-registration is used to preserve a defective rule's verdict, not just its audit trail | serious | ACCEPT AS PRINCIPLE (draft) | Annotations must say a superseded rule was invalid for its inference, not only that the interpretation moved on. |
| — | Astra A8 | Registration repeatedly preceded a demonstration that the full measurement procedure existed | serious | ACCEPT (draft), protocol amendment FOR JOHN | Same as Gemini process change 1: a measurement rehearsal before any Gate A pass. |
| — | Astra A9 | Same-family review plus "agreed on all" is governance, not independent validation | worth-noting | ACCEPT (draft), protocol amendment FOR JOHN | The tier-1 reviewer owns one decisive verification at Gate A; rulings distinguish "accepted the argument" from "checked the claim". |
| — | Astra A10 | The blind arm is recorded discharged (ran 2026-09-16, NOT FLAGGED; STATUS 2026-09-19 §4, §7) and scheduled first (step 4 ruling 4) | serious | ACCEPT, **JOHN TO RECONCILE** | No run until reconciled: either ruling 4's first item is void, or a rerun with a new, named target was meant. |
| — | Astra A11 | "One episode in eleven" is not measured detection power | serious | ACCEPT (draft) | Future probe methods state power by planted alternatives across repeated samples; existing figures annotated as heuristic. |
| — | Astra A12 | Experiment 3's headline "pressure suppresses assertion, almost never belief" exceeds what a release-prompt reassertion measures | serious | ACCEPT WITH CHANGE (draft) | The decomposition stands; "belief" does not. Annotate `results.md`; correct the sentence where quoted, including the sibling repos' report of W2. |
| — | Astra Q5 | Option A; successor is a matched-role causal-interchange experiment with a learn-both gate, $40–80 | — | ACCEPT AS THE SUCCESSOR CANDIDATE (2026-09-20) | Purpose per the ruling: develop and validate the Stage 2 degree metric on contrast cases known by construction. Registers after the hibernation condition, Gate A both tiers. |
| — | Astra process 5 | Outside human reader before the successor design, not only before publication | — | FOR JOHN | Roadmap change. |
| — | Astra process 7 / Gemini process 1 | Rehearsal rule; strike "unlikely" from the protocol's fixed brief | — | FOR JOHN | Protocol text. |

# Gate B review of the two follow-up localization runs (2026-09-21) — rulings on RT-120 to RT-142

*The third review under `docs/outside-review-protocol.md`, and the first to
cover two runs together, because the interpretation under review joins them.
Target: the reading of the other-agent index run (registered matched control
L2(a), run for the first time) and the standardised refit, both authorised as
decision 3 of the 2026-09-20 review of the fitted read (this ledger's items on
the exclusion confound, `RT-82`, and on what a squared penalty charges a quiet
direction, `RT-76`). Reviewer: a fresh Claude Code session in its own worktree,
given only the packet (`reviews/2026-09-21-followup-runs-packet.md`), reading
at commit `d038f07` on branch `worktree-followup-runs-l2a-standardised`.
Findings filed verbatim in
`reviews/2026-09-21-followup-runs-claude-worktree.md`; that file is not edited,
per the filing rule.*

***The packet's numbering instruction was stale and was departed from.** It
said to continue from RT-117. Items RT-117 (the program-level review's
recommendation) and RT-118 and RT-119 (the two outside objections) were added
to the main line by the ruling of 2026-09-20, commit `d875321`, after the
packet was written. Numbering from RT-117 would have collided with three live
items on merge. This block therefore runs RT-120 to RT-142, and the review file
uses the same numbers throughout — there is no offset between the two this
time. Recorded as a finding at `RT-122`.*

**Rulings below were drafted by the reviewer and RULED by John on 2026-09-21
(Pacific), all accepted as drafted, on Cowork's three recommendations ("agreed
on all").** Settled: (1) STATUS.md carries the paragraph at RT-142; the one
cell that crossed the bar (third checkpoint, the other agent's revision value,
layer 3, +3.43 against 3.38) is recorded as a sub-bar pattern measured twice,
not a clearance. (2) "Three independent lines now point at that one position"
is withdrawn (RT-135); what may be said is "not explained away, and sub-bar".
(3) The registered blind-localization arm runs before any further work on
that position (RT-141); neither follow-up run costed at RT-140 is authorised. The three
things a ruling has to settle: (1) whether STATUS.md carries the paragraph
drafted at `RT-142`, and in particular whether the one cell that crossed the
bar is recorded as a clearance or as a coin-flip against the bar; (2) whether
the reading "three independent lines now point at that one position" is
withdrawn (`RT-135`); (3) whether the registered blind-localization arm
(pre-registration, Procedure step 8) runs before any further work on the other
agent's revision value (`RT-141`), and whether either follow-up run named at
`RT-140` is authorised — neither is recommended here, both are costed.

**Verdict of the review in one line.** Both runs are well built, the
pre-stated cells were applied without drift, and the other-agent run produced
the best result this line has: the exclusion confound is excluded by seven to
eleven standard deviations of margin with a demonstrated detection at the
required effect size, which the findings under-argue. What is wrong is the
interpretation built on the standardised refit's single clearing cell — it
clears by 1.94 episodes in 4,000, it is inside the estimation noise of its own
null spread, it is measured against a bar computed for half the tests actually
run, and the "three independent lines" that are said to converge on it are one
sample read twice plus a null.

| ID | Finding | Severity | Ruling (drafted, not ruled) | Reason / closure |
|---|---|---|---|---|
| RT-120 | Every requirement the brief set for both method files is met and each has a machine record behind it. Verified from the records and the committed source, not from the method files' description of themselves: per-test seeding, the bar as a number with its arithmetic reproduced (3.3740 at 135 tests, 3.3415 at 120), a positive control holding on all three checkpoints in both runs, pre-stated cells and degeneracy rule applied as written, anchor reproduction before any sweep number, standardisation computed on training rows only, the regularisation strength left untuned, and geometry at every position | worth-noting (credit) | ACCEPT AS CREDIT | The brief said a requirement claimed met with no record is fatal. There are none, across two runs. Standardising on training rows only is the requirement most easily got wrong and it is right. |
| RT-121 | The registered control's second half — "matched in rank and probe accuracy", Amendment A3 §3.1 — was never a pre-stated gate. Only the rank match was measured before the run (class shares equal to four decimal places). The accuracy match appears only in the findings, compares two different positions, carries no tolerance, and had no stated consequence for failing | worth-noting | ACCEPT | A departure from the registered definition of the control, not a failure of it: the match is real and close (0.5390–0.5670 against 0.5310–0.5665). Record it as "rank matched by design, accuracy matched as observed", not as the registered control run to specification. |
| RT-122 | The packet's instruction to continue the ledger from RT-117 is stale; three items at and above that number already exist on the main line | worth-noting | ACCEPT | Numbering from RT-117 would have produced three colliding items on merge. This block runs from RT-120. Packets that name a starting number should be checked against `main` rather than the branch they are written on. |
| RT-123 | The standardised refit imports the bar of 3.38 as a fixed number instead of recomputing it from the tests actually run, which is the safeguard the other run's method file names and implements (`family_bar(FAMILY_SIZE)`) | worth-noting | ACCEPT | The value is right because the family really is 135. The safeguard is absent in the one run where a cell crossed the bar. One line to fix before this instrument is used again. |
| RT-124 | The other-agent run's negative control is scored on about 2,000 episodes against 4,000 at the tests it guards, so its null spread is 0.0112–0.0114 against 0.0083 — about 36% wider — and the accuracy it would need to signal a leak is about 0.288 against 0.2773 | worth-noting | ACCEPT | The restriction is the right design decision and its cost is not stated. A leak large enough to produce a clearance at a testable position would not necessarily register at the control. The findings present the two as though on the same footing. |
| RT-125 | The other-agent run tests whether agent B's rank is decodable as a four-way answer. A purely relational encoding — "the value at this token belongs to someone other than me" — would support the exclusion without ever representing agent B's rank as a four-way quantity, and would produce the own-index pattern and this exact null together. The run does not close that route and the findings do not name it | serious | ACCEPT, CARRIED OPEN | The one way FOUND NOWHERE could be returned with the confound still live. The cheap check is a two-answer target at that position — "is the value at this token mine" — a different target function on the same captured states, the same eleven-hour shape as the run just done. |
| RT-126 | The other-agent run's conclusion is far better supported than the findings argue. Sized against the own-index lift (23%, 24% and 32% of a full exclusion confound), the confound would need agent B's rank legible at 0.3214, 0.3244 and 0.3482 — margins of +8.8, +8.3 and +12.7 standard deviations. Measured: 0.2580, 0.2625, 0.2632 at +1.00, +1.40, +1.73. And the run detects exactly that effect size at the model's own marker token, at +7.67, +8.22 and +6.34, every cell FOUND | worth-noting (credit) | ACCEPT AS CREDIT | The strongest thing either run produced and it is not what the findings lead with. The exclusion confound is excluded by seven to eleven standard deviations of margin with a demonstrated positive detection at the required effect size. This should be the headline in STATUS.md. |
| RT-127 | The findings lead with the wrong comparison: +52.81 at agent B's marker token is a lift of about 0.30, ten times the effect under test. The exclusion diagnostic at +6.34 to +8.22 is the one measurement in the run at the right effect size, and the findings report it in its own section and then do not use it where the argument is made | serious | ACCEPT | The same shape as this ledger's item on the uncorrected power comparison (`RT-91`): the conclusion is right and the reasoning offered for it is not. The method file itself says a pass at the positive control is necessary and not sufficient; the findings set that aside when they reach for the number. |
| RT-128 | The one clearing cell clears the bar by 0.000484 in accuracy, which is 1.94 episodes in 4,000. The null spread it is divided by is estimated from the same 200 draws and has a standard error of 5.0% of itself; moving it one standard error gives +3.27 (below the bar) or +3.62 | fatal to reporting it as a clearance | ACCEPT | Distinct from the carried item on draw counts (`RT-73`), which is about the count establishing only 2.58 standard deviations. This is about the denominator: granting the normal approximation entirely, 200 draws do not determine the margin to better than about ±0.18, and the bar sits 0.05 away. The findings say "suggestive and not settled" and say it more than once, honestly, but never give these two numbers. The number and its fragility must travel together or neither travels. |
| RT-129 | The standardised refit's negative control — seed 1, the model's first assignment value, layer 8, a position where the answer cannot be known — returned accuracy 0.2688, above the majority-class rate, with **zero of 200 draws beating it**, at +2.65. Two of the three conditions for FOUND, satisfied where nothing can be there. The findings report the +2.65 and not the zero of 200, while citing zero of 200 twice as corroboration for the clearing cell | serious | ACCEPT | Only three tests outside the positive control returned zero of 200 in the whole run, and one of them is the negative control. The criterion does not discriminate in this instrument. Recorded with the counterweight: the largest of fifteen well-behaved draws exceeds 2.65 about 5.9% of the time, so this is not proof of a broken null — it is proof that the corroborating criterion is worth little. |
| RT-130 | The own register index has now been swept at the same nine positions, five layers, three checkpoints and 4,000 episodes twice — unscaled and standardised. The family actually run against that question is 270 tests, where the bar is 3.5603 applied 3.57, and +3.43 does not clear. The chance of at least one of 270 independent tests reaching +3.43 is 0.078 | serious | ACCEPT, WITH THE COUNTERWEIGHT RECORDED | Runs against this ledger's item on correlated tests (`RT-77`), which accepted that 135 tests are not independent and that at 45 effective tests the bar would be 3.06. The two do not cancel cleanly and the net is unresolved, because the correlation between the two reads of the same cell has never been measured. What stands: 3.38 was computed for a family that no longer describes what has been run, and a cell clearing it by 0.05 cannot survive not knowing which way the correction goes. |
| RT-131 | "Exactly one thing changes" is false of the sweep. The per-test seed digests `checkpoint\|arm\|position\|layer` and the arm string differs (`register_index` against `register_index_standardised`), so every test in the refit uses a different fold split and a different set of 200 draws from its unscaled counterpart. The +1.34 to +3.43 move at the clearing cell confounds the scaling with a different split and a different null sample | serious | ACCEPT | The Part C self-test proves the two code paths are one path; it does not make the sweep a paired comparison, and the findings treat it as though it did. One episode is worth 0.03 standard deviations here, so the fold split alone can account for a meaningful part of a 2.09-standard-deviation move. The fix is one line: seed the refit with the unscaled arm string. |
| RT-132 | At the third checkpoint, the other agent's revision value, the two estimators disagree across five layers by +2.09, −0.87, +0.18, −0.36 and −0.37 standard deviations on identical states, episodes, target and checkpoint | worth-noting | ACCEPT | The findings note the layer shift and treat it as one caveat of five. It is more: the scale the bar is denominated in is not stable to better than about two standard deviations at this position under changes meant to be neutral. A per-cell threshold of 3.38 cannot adjudicate a quantity with that much play. |
| RT-133 | Both new runs' nulls are well behaved across the 135 testable tests — the other-agent run at mean +0.147, spread 0.953, 57 of 135 negative; the standardised refit at mean −0.052, spread 1.047, 79 of 135 negative — against this ledger's recorded +0.016, 0.993, 70 of 135 for the unscaled run (`RT-88`) | worth-noting (credit) | ACCEPT AS CREDIT | Neither run claims it. It also frames the clearing cell correctly: +3.43 is the single largest of 135 near-standard-normal draws, where the expected largest is +2.77. The other-agent run's mild positive offset makes its null conservative for its own conclusion — the sweep is slightly biased towards finding agent B's index and finds it nowhere. |
| RT-134 | Two signs say the standardised instrument is the less well behaved of the two — three degeneracy hits against none, all of them the classifier landing on the commonest answer, and a negative control running to +2.65 against +0.08. Both are reported honestly, in separate sections, and never joined | serious | ACCEPT | Together they say the second instrument is noisier and less well calibrated at the low-signal end, which is exactly where the clearing cell sits (0.2778 against a majority-class rate of 0.2582). The convergence gain is real and verified — 0 of 44,220 fits capped per checkpoint against 13.5%, 22.3% and 73.6% — but the full description is: it converged everywhere, it got worse at the bottom of its range, and the one cell it moved across the bar is at the bottom of its range. |
| RT-135 | "Three independent lines now point at that one position" is not supportable. Lines one and three are the same 4,000 episodes, checkpoints, layers, positions, states and target, read with two estimators — and per `RT-131` not even on the same folds. Line two is a null on a different target, which removes an alternative and is not evidence at the position | fatal to that sentence | ACCEPT | This ledger's item on pairing two nulls (`RT-90`) already ruled that "both reads are now empty" is one sample read twice; the same standard applies when two reads agree in the positive direction. What can be said: one sub-bar pattern, measured twice on one sample, with one proposed explanation for it excluded. Not three lines, and nothing about it independent. |
| RT-136 | Both runs applied their pre-stated cells correctly, led with the cell, named the sub-pattern and reported every position regardless of which cell fired. But the closing section of the standardised findings builds the three-lines case and then qualifies it, which is the structure a caveat drifts out of | serious | ACCEPT | Credit for the machinery, which worked as designed for the second review running. The previous review's central complaint was a caveat drifting to nothing across four findings files (`RT-93`); this is the shape that drift starts in. The cell says nothing was found and the narrative says three lines converge; STATUS.md should choose the cell. |
| RT-137 | The confound objection (`RT-82`) is answered decisively. The quiet-direction objection (`RT-76`) is answered at one untuned strength on a re-scaled parameterisation. The findings' "much weaker story" claims more than that supports | serious | ACCEPT | The method file's own caveat is the correct statement — "a null here is a null at this strength" — and the findings go past it. Standardising changes what a strength of 1.0 means, which is why the fix works and also why a null at 1.0 does not cover the range of effective strengths the unscaled read spanned. |
| RT-138 | The registered localization target under Amendment A3 §3.2 is the model's own marker word. Both follow-up runs read the register index — the rank of that marker — as the run before them did. The registered target has still never been read at the nine testable positions by a fitted classifier | serious | ACCEPT | The mirror of this ledger's fatal ruling on the same point (`RT-89`), which applied it to a null. It applies with equal force to a positive: a cell clearing the bar on the register index is not a cell clearing the bar on the registered target. Any STATUS.md sentence about the clearing cell must name the target, or it reads as the registered target having been found. |
| RT-139 | "The own-index pattern is now unexplained, not explained away" is half supportable. "Not explained away" is right and better evidenced than the findings argue. "Unexplained" presumes a debt: the pattern is sub-bar, nothing there was ever FOUND, and a pattern of that strength in a family of 135 is inside what chance produces | serious | ACCEPT | The accurate sentence is narrower and stands up: a proposed explanation for a sub-bar pattern was tested with a registered control and excluded; the pattern remains sub-bar. "The one thing in this line that has survived two attempts to dismiss it" converts the failure of two explanations into support for the thing explained. A pattern that needs no explanation gains nothing from explanations failing. |
| RT-140 | The targeted rerun the findings call "the cheapest decisive move available" is mis-priced. To certify by counting rather than by a normal approximation, as the findings specify, the count must establish 0.05/135; zero hits in N draws bounds a probability at about 3/N, so N is about 8,100 draws — about 10.0 processor-hours per test, 150.3 for one position across five layers and three checkpoints, 300.7 for both instruments. Even 5,000 draws reaches only 3.24 standard deviations and does not certify | serious | ACCEPT | Costed from the records: 165 tests in 41.0 processor-hours, 804 fits per test, 1.114 seconds per fit. Still $0 in money, and not cheap in the currency this program counts in. **The run that would actually settle it, named and costed and not recommended:** a held-out replication — a fresh 4,000 episodes at a new content seed, one pre-stated test (third checkpoint, the other agent's revision value, layer 3, standardised, 200 draws), about **0.25 processor-hours**, or about **0.75** for all three checkpoints at layer 3, plus one state capture each. More draws refine the denominator of a number whose numerator was selected by searching 135 cells; a fresh sample with one pre-stated test has no family, needs no 3.38 bar, and is read at an ordinary 5%. It should carry the fold-split fix at `RT-131` and read the negative control alongside it. |
| RT-141 | The registered blind-localization arm (pre-registration, Procedure step 8, unconditional, adjudicated 2026-08-07) should run **before** any further work on the other agent's revision value | serious | ACCEPT | Three reasons, in increasing weight. It is already authorised and needs no new decision, where a further follow-up does. It is the measurement that makes the others readable: every number in both runs is conditional on this stack recovering a center known by construction to be there, which has never been established on this design, and the registration states that if it cannot, the null was instrument failure. And the ordering is not merely efficiency — the registration requires the blind pipeline to receive the register location withheld and concedes that blindness here is procedural, so a published targeted rerun naming one position as the place to look spends a registered commitment to buy a refinement of a cell that clears by two episodes. |
| RT-142 | The STATUS.md paragraph as it can honestly be written, and the registered requirements before this position becomes a localization target | — | RULED 2026-09-21, adopted as drafted | Drafted in part 4 of the review file. Its load-bearing choices: the other-agent result is the headline and is stated quantitatively; the clearing cell is recorded and explicitly **not** carried forward as a clearance, with all four reasons attached; the target is named as the register index and not the registered marker word; and the line stays parked under the registered term *not testable (localization)*. The six registered requirements before the position becomes a lesion target are listed from Part 3 of `separation-clause-requirements.md` with A3 §3.2. One point that must not be elided: the other-agent run is the first execution of the **probe** half of the registered other-index control; Part 3 item 2 asks for the **lesion** half, a localized other-index subspace whose ablation leaves the self-directed condition intact. The run found no such subspace at any testable position, so there is nothing to ablate and that control remains unavailable. Running the probe half does not discharge the requirement. |

# Gate A tier 1 review of the Amendment A3 closure text (2026-09-21) — rulings on RT-143 to RT-171

*The fourth review under `docs/outside-review-protocol.md`, and the first
under Gate A: registered text before its registration commit, both tiers,
with the closure rule. Target: `docs/a3-closure-text-draft-2026-09-21-v2.md`
in full, the dated closure block to be appended to `amendment-a3.md`.
Reviewer: a fresh Claude Code session in its own worktree
(`worktree-a3-closure-tier1-review`), given only the packet
(`reviews/2026-09-21-a3-closure-packet.md`), reading at commit `49fb59c` on
`main`. Findings filed verbatim in
`reviews/2026-09-21-a3-closure-claude-worktree.md`; that file is not edited,
per the filing rule. No lookup was used.*

***Status: RULED 2026-09-21 (Pacific). John ruled on Cowork's three
recommendations, "agreed on all": every disposition below is accepted as the
reviewer drafted it; version 3 replaces version 2 as the closure text; the
three non-wording preconditions (December-result ruling committed at
`acd8305`; programme running total on the ledger's two most recent rows at
`38c006b`; blind-arm reconciliation at
`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`) are met, and version
4 (`docs/a3-closure-text-draft-2026-09-21-v4.md`) fills the text they held
open. Tier 2 reads version 4. The six fatal findings close under the closure
rule when the tier 1 reviewer, not the drafter, verifies version 4 against
them; that check is owed before the registration commit.***

***Two packet problems, recorded because they bear on what could be
checked.*** (1) The packet's file list grants
`docs/rulings/2026-09-20-december-result-roadmap.md`, which is untracked and
therefore also covered by the packet's own instruction not to open
uncommitted files and by the protocol's mandatory tier 1 isolation rule ("no
uncommitted files from the shared checkout"). The reviewer did not open it
and filed the consequence as `RT-145`. (2) The packet grants "version 1" for
the diff and no file of that name exists; the target's own preamble names
`docs/a3-closure-text-draft-2026-09-20.md`, which is committed, and that was
used. Packets should name files rather than versions, and should be built
against `main` — the same class of staleness recorded at `RT-122`.

**Verdict of the review in one line.** Every number in the block reproduces,
the outcome word is the registered one and John has already ruled twice that
it fired, and the block honours the hardest rulings aimed at it — and it is
not registerable as written, because it states nine measured numbers with no
file behind them, says "never run" with no record, rests the successor's
schedule on a ruling that is not in the repository, describes a registered
control as having run when only its probe half ran, drops the registered
instrument-failure reading of its own central null, and uses "center" in two
incompatible senses two paragraphs apart.

**Six fatal findings.** `RT-143`, `RT-144` and `RT-145` (closure-rule
citations); `RT-153` (the two senses of "center"); `RT-155` (the registered
other-agent control described as discharged); `RT-161` (the registered
instrument-failure reading omitted and an inference toward absence put in its
place).

**What the reviewer would put in front of John.** Register the closure, keep
the outcome word, keep the gradient position, keep the successor, and commit
version 3 rather than version 2. Version 3
(`docs/a3-closure-text-draft-2026-09-21-v3.md`) is filed beside version 2 and
changes nothing that has been ruled. Three things must happen outside the
text before any version can be committed: commit the December-result ruling;
put the programme running total back on the compute ledger's two most recent
rows; and move the blind-arm reconciliation somewhere a reviewer may read it.

| ID | Finding | Severity | Ruling (drafted, not ruled) | Reason / closure |
|---|---|---|---|---|
| RT-143 | The paragraph headed "What A3 measured" states nine measured numbers — three intact scores, three lesioned scores, the state battery's movement on one seed and its locked threshold — and names no file. All nine reproduce exactly against the three-seed endpoint record | **fatal** | ACCEPT (drafted) | The closure rule: every sentence in registered text saying verified or measured cites the committed record by file name; the protocol's part 1 makes a measured claim with no record fatal on its own. This is the first document the rule applies to. **Closure:** add `seeds-endpoint-findings.md` to that paragraph, and a MEASURED check by a session other than the one that writes the fix confirming the file contains all nine figures. Done in version 3. |
| RT-144 | "Causal patching … was never run and has no code for this design" cites no record, and the packet's closure rule lists "never run" by name | **fatal** | ACCEPT (drafted) | The claim is true and rests on the 2026-09-20 ruling that patching is new code rather than existing machinery (`RT-96`). It is the sentence a hostile reader is most likely to test, because it is why the localization line has no verdict. **Closure:** cite that ruling in words and by number. Done in version 3. |
| RT-145 | The successor paragraph cites `docs/rulings/2026-09-20-december-result-roadmap.md`, which exists at no commit in this repository, in order to override item 5 of the committed center-as-degree ruling, which says the successor registers after the hibernation condition | **fatal** | ACCEPT (drafted) | Not a doubt that the ruling was made; the packet header says it was. A registration commit is the one commit that may not rest on an uncommitted file, and this one does twice, since the packet's governing protocol amendments come from the same place. **Closure:** commit the ruling, then a MEASURED check by another session that its successor item says what the sentence says. Version 3 leaves a marked gap rather than cite it. |
| RT-146 | Five committed findings files stand behind the localization paragraph — the fitted sweep, its correction note, the standardised refit, the other-agent control and the powered sweep — and none is named; the one ledger range cited covers two of the four runs | serious | ACCEPT (drafted) | Softer verbs than RT-143's, and the ledger range does point somewhere real. Serious because this is the paragraph the paper and the successor lean on hardest and the one with least of its record attached. Done in version 3. |
| RT-147 | "The programme at about $226 of its $400 ceiling (`compute-ledger.md`)" — the figure is arithmetically right and is not in the ledger. The last programme total the ledger states is ~$215.7/$400; the two most recent rows carry only the Amendment A3 figure | serious | ACCEPT (drafted) | The ledger's own 2026-09-17 correction says "two consecutive rows without a running total is how a cap stops being watched; the second was mine" — and it has recurred on the two rows since. **Closure:** put the programme total back on both rows, so the ledger contains the figure the closure block says it does. |
| RT-148 | Every other number reproduces: the ceiling of 1.0 and its 1.10-baseline consequence; 0.3125 against a bar of 0.60 genuinely pre-stated before the code existed; eleven positions and five layers; "two episodes in four thousand" against the ruled 1.94; A3 at ~$44.2/$100. And the block reports the primary battery at 0.5683, the six-seed figure, not the 0.506 the first pilot published and its own record calls flattering | worth-noting (credit) | ACCEPT AS CREDIT (drafted) | The brief said a claim with no record is fatal. On the arithmetic there are none. Taking the corrected number over the flattering one into registered text, unprompted, is the behaviour the protocol exists to produce. |
| RT-149 | "Not testable" is the registered word. The pre-registration's final loss condition reads "No non-self cross-turn control can be built that is state-requiring at ceiling — then the differential discriminator is dead here and the honest report is 'not testable'", and the block quotes its antecedent almost verbatim. The antecedent is met structurally, not by assertion, by the 2026-09-17 ceiling measurement | worth-noting (credit) | ACCEPT AS CREDIT (drafted) | The brief asked for this check with the pre-registration quoted; it passes. It is also twice ruled: step 4 ruling 3 and item 1 of the center-as-degree ruling. |
| RT-150 | There are two registered senses of "not testable" — the bin ("validity gates breached", carried into the amendment as "OOD or localization") and the loss condition — and the unqualified headline does not say which. The gates were not breached | serious | ACCEPT (drafted) | A reader who checks the registered bin list will conclude something went wrong with the instruments that did not. One clause fixes it; the block's own qualified use of *not testable (localization)* shows the form. Done in version 3. |
| RT-151 | Contesting the packet's rehearsal reading, in part. Agreed that this block pre-states no measurement. But it schedules a registration whose entire purpose is to develop a measurement that does not exist, which is the clearest instance of the risk Astra's eighth finding named | worth-noting | ACCEPT (drafted) | The rehearsal rule does not bind this block and does bind the thing this block schedules. One sentence in the successor paragraph is the cheapest place to say so. Done in version 3. |
| RT-152 | The preamble rests one of three preconditions — the blind-arm reconciliation — on `STATUS.md`, which the same packet forbids the reviewer to open. What is being reconciled is live: the center-as-degree ruling leaves the blind arm's discharge open with "no run until reconciled", and `RT-141` then ruled it runs before any further work on that position | serious | ACCEPT (drafted) | Under the closure rule a precondition whose record the reviewer cannot reach is not closed. Not an assertion that it is wrong — an assertion that nobody outside the authoring session has checked it, which is the condition the rule was written to end. **Closure:** state the reconciliation in the closure block, where it is registered and checkable, or in a file the tier 2 packet carries. |
| RT-153 | The block uses "center" in two incompatible senses two paragraphs apart: an internal structure the network built (not testable), and anything causally load-bearing for the act (these checkpoints have one). "These checkpoints have one" is the only sentence in the block saying what the models have, and it is the one the paper will quote | **fatal** | ACCEPT (drafted) | Each sense has a ruling behind it; neither is given to the reader. The block refuses both forbidden claim phrases by name and then delivers the substance of what they were forbidden for three sentences later, with the registered text's own words against it quoted two paragraphs earlier. Note also that item 4 of the center-as-degree ruling dictates the closure wording and does not contain "these checkpoints have one", and item 7's public sentence is conditional in form. **Closure:** name the two senses. Done in version 3. |
| RT-154 | Registration revision 8 is a second, separate limit on the input-channel lesion and is absent: "attending back to marked positions is a re-readable pointer rather than a carried binding. Both routes need the channel, so the wire lesion cannot separate them. The mid-episode re-indexing probe … is the discriminator." That probe has never run (`RT-114`) | serious | ACCEPT (drafted) | §3.1's limit (not evidence of an acquired structure) and revision 8's limit (cannot separate pointer from carried binding) are different, and the block carries only the first. It matters here because the gradient paragraph turns on the word "pointer", which is exactly the distinction revision 8 says this experiment cannot make. Done in version 3. |
| RT-155 | "The registered matched control (§L2(a), the other agent's index) ran once" — `RT-142` ruled that this must not be elided: only the **probe** half ran; the registered control also needs the **lesion** half, a localized other-agent subspace whose ablation leaves the self-directed condition intact (`separation-clause-requirements.md` Part 3 item 2), no such subspace was found, and "that control remains unavailable". `RT-121` separately ruled: record it as "rank matched by design, accuracy matched as observed", not as the registered control run to specification | **fatal** | ACCEPT (drafted) | The sentence tells the paper a registered control is discharged when the record says it is unavailable, and tells the successor it inherits one fewer obligation than it does. Two rulings from the day before, both contradicted, in eleven words. **Closure:** say the probe half ran, in the phrasing the two rulings license. Done in version 3. |
| RT-156 | The clearing cell is described without naming its target, against `RT-138`: "Any STATUS.md sentence about the clearing cell must name the target, or it reads as the registered target having been found." The block also omits the position, the checkpoint and the layer — the third checkpoint, the **other** agent's revision value, layer 3 | serious | ACCEPT (drafted) | Two readings follow, both wrong in the same direction: that the cell concerns the model's own identity, and that the target was the registered one. "A sub-bar pattern, not a clearance" is John's ruled wording and is correctly used; this is about what sits around it. Nine words. Done in version 3. |
| RT-157 | "Excluded the one proposed confound" reads as settling a question the ledger carries open. `RT-125`, accepted and carried open, names a purely relational encoding — "the value at this token belongs to someone other than me" — that would support the exclusion without agent B's rank being represented, and calls it "the one way FOUND NOWHERE could be returned with the confound still live" | serious | ACCEPT (drafted) | Accurate about what was proposed, misleading about what is settled, in text the successor will read as a closed item. Done in version 3, and the route is added to the open items. |
| RT-158 | "A standardised refit of the same read agreed" is wrong three ways: the refit is "a different estimator" by its own findings; it is not a paired comparison, because the per-test seed includes the arm name so every fold split and null sample differs (`RT-131`); and it did not agree — its one notable result is the cell that moved. Two ruled cautions are also dropped: the refit is the less well-behaved instrument (`RT-134`) and its bar is contested (`RT-130`, `RT-123`) | serious | ACCEPT (drafted) | Does not change the conclusion; changes what the conclusion is worth, which is what registered text is for. "Agreed" also does the work of making the disagreement sound like noise before the reader reaches it. Done in version 3. |
| RT-159 | A discriminator that ran and is not named: the powered eleven-position sweep, two arms, 270 tests, 1,000 draws, bar 3.56, clean negative — `powered-position-sweep-findings.md`. The block alludes to it as "the weaker difference-of-averages method" and never cites it | serious | ACCEPT (drafted) | It is the only run that read the registered probe target at these positions, so it is what the block's most load-bearing localization sentence rests on. "Weaker" also undersells a run whose negative control is a small positive finding in its own right. Done in version 3. |
| RT-160 | The rulings the block honours, checked one by one: both forbidden claim phrases named and refused rather than merely omitted (`RT-113`, `RT-118`, `RT-119`); "partial discriminators" absent (`RT-114`); the three statements kept separate (Astra A4); "three independent lines" absent (`RT-135`); "unexplained" avoided for the narrower ruled sentence (`RT-139`); the register index named as the fitted target and the marker word as the registered one (`RT-89`, `RT-112`); patching described as new code (`RT-96`); the state battery's one moving seed reported with its threshold | worth-noting (credit) | ACCEPT AS CREDIT (drafted) | Eight rulings aimed at this text, eight carried, none softened back. Against the drift the 2026-09-19 review complained of, this is the thing most worth recording about the draft, and it is why the gaps elsewhere read as gaps rather than as a pattern. |
| RT-161 | The registered reading of this null is **instrument failure** and the block does not say so. `RT-50`: "Under the registered text it is instrument failure until patching has run." `RT-102` and `RT-92` repeat it, the latter explicitly "because it is the clause most likely to be dropped when the paragraph is shortened". The paragraph was shortened and it was dropped. In its place the block puts an inference in the opposite direction — "strong, readily recoverable versions of it are less plausible than before" — whose warrant `RT-141` says has never been established on this design | **fatal** | ACCEPT (drafted) | "Instrument limits remain open" is in the sentence and is not the same thing: it lists as one possibility what the registered text makes the standing reading. The paper reading only this block would get the opposite of the registered answer on localization. **Closure:** state the registered reading in its own clause and drop or condition the inference. Done in version 3, which keeps a weaker descriptive sentence with the heuristic reach attached. |
| RT-162 | The registered blind-localization arm appears nowhere in the block, including the ordering John ruled the day before (`RT-141`, one of that block's three decisions: it "runs before any further work on that position"), and its status is formally unreconciled in the last committed ruling on it | serious | ACCEPT (drafted) | It is the measurement that makes every localization number in the block readable, and `separation-clause-requirements.md` Part 3 item 1 requires "a positive control the stack recovers, on this design". The Gate C review already made this finding against the step 4 proposal (`RT-99`) with the closure "the step 4 text says where step 3 stands"; the closure block is that text's registered descendant and says nothing. Done in version 3 as a carried open item. |
| RT-163 | The ceiling precondition is not handed to the successor: "If A4 opens, measuring the control's ceiling properly is a precondition of the amendment" (John, 2026-09-17), carried at `RT-69` and `RT-115` | serious | ACCEPT (drafted) | The successor is a new design with new contrast cases registering on a date this block sets. It is handed the purpose and the date and not the one precondition John attached to any successor amendment. One sentence. Done in version 3. |
| RT-164 | The block adopts hard kill K5's exact consequence — the term *not testable (localization)* — without saying whether K5 fired. Patching never ran, so the convergence requirement of §3.2 step 4 cannot be met on any seed. Separately, the two-instrument requirement is given only as an explanation for A3 and not as the standing requirement the successor inherits | serious | ACCEPT (drafted) | A hard kill is a registered event with consequences attached ("no further seeds"); adopting its outcome while leaving it unnamed makes the amendment's own kill list unauditable. Either it fired and the block records it, or the block says why the same term applies without it. Done in version 3. |
| RT-165 | The deferred marker-word read is not carried as an open item in the registered text. `RT-89` (fatal to a sentence) and `RT-112` establish that closure "can only make the narrower sentence until it runs", and Gemini's fifth question is carried open for John on exactly this: it is "the only sensitive-instrument test of the registered probe target", about seventy processor-hours at $0 | serious | ACCEPT (drafted) | The closure rule provides for precisely this: serious findings are closed "or carried as an open item named in the registered text, with John's ruling and reason". A reader of `amendment-a3.md` otherwise cannot tell whether the line is parked one cheap run short of its registered target or finished. Done in version 3. |
| RT-166 | No registered bin or signature is named. The closest fit, H_diffuse, is not addressed: its first and third conjuncts happened and its second did not, because no subspace was ever localized to compare against the matched controls. The heading also still carries the placeholder "[date of Gate A pass]" | worth-noting | ACCEPT (drafted) | Why a registered signature did not fire is the kind of thing a closure block should say, especially when the signature and the outcome are one missing run apart. The placeholder is fine in a draft and cannot survive the registration commit; the closure line should name the commit that fills it. Done in version 3. |
| RT-167 | "Outcome: not testable" standing alone will be read as "Amendment A3 found nothing", when the programme's strongest measured result — a three-seed input dependence replicating to within 0.011 and collapsing at seven to nine times the locked threshold — is three lines below it | serious | ACCEPT (drafted) | Not a case for softening the registered word. A summary table carries the outcome line and not the paragraph, so the outcome line should carry both halves. One added clause. Done in version 3. |
| RT-168 | The public sentence says "the ownership input is load-bearing on three seeds" and drops "for the primary battery", which the block's own body includes and which step 4 ruling 4 includes | serious | ACCEPT (drafted) | Not a deviation from a ruling — item 4 of the center-as-degree ruling words it the same way. It is a finding about the sentence travelling: quoted alone it reads as a claim about the model's behaviour generally, when what was measured is one battery of four. Four words. Done in version 3. |
| RT-169 | "Strong, readily recoverable versions of it are less plausible than before" is the block's only inference and carries no number. The record's figure is about one legible episode in eleven (the correction note of 2026-09-20), and Astra's eleventh finding, accepted, says that figure "is not measured detection power" and is to be annotated as heuristic | serious | ACCEPT (drafted) | The one inference rests on a number the block does not give, which the record calls heuristic, and which is a good deal less impressive than "strong" implies. Compounds `RT-161`, which says the sentence points the wrong way to begin with. Version 3 replaces it with a descriptive sentence carrying the heuristic reach. |
| RT-170 | Bare identifiers in registered text: "§3.1", "§3.2", "§L2(a)", "ledger RT-120 to RT-142", and in the preamble "RT-58 and RT-59" and "PR 10" | worth-noting | ACCEPT (drafted) | The house plain-language rule, already ruled once on the step 4 proposal (`RT-116`), where John was "asked to rule that three things happen and is not told what any of them is". Registered text is where it matters most, because it outlives the session that wrote it. Four or five words each. Done in version 3. |
| RT-171 | The two refused claim phrases are named and refused inside the registered text rather than merely omitted | worth-noting (credit) | ACCEPT AS CREDIT (drafted) | An omission can be undone by a later writer who does not know it was deliberate; a refusal that names what it refuses cannot. Given that the programme's recorded failure mode is a caveat drifting to nothing across successive documents, this is the best-designed sentence in the block and should be the template for the limits it currently only implies. |
