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
| RT-56 | The training log and trajectory record are not in the repository | serious | ACCEPTED | **Closure:** commit both beside the endpoint record before the step 4 proposal is filed. |
| RT-57 | The intervention did three things: raised the control's share, tripled the whole query loss against the action term, and changed what the gradient clip does | serious | ACCEPTED | STATUS.md describes the intervention as what it was. Any future reweighting run holds the total query weight fixed or says why not. |
| RT-58 | The control rows are the first half of every batch, a fixed positional split never checked for bias | serious | ACCEPTED, CARRIED OPEN | **Closure:** a $0 local check of episode order against the split, filed as a findings note. |
| RT-59 | "Exactly one scored token per row" is asserted in a comment and never tested | worth-noting | ACCEPTED, CARRIED OPEN | **Closure:** one-line self-test, $0. |
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

**Rulings below are DRAFTED BY THE REVIEWER AND NOT YET RULED.** Nothing here
has been put to John and nothing enters STATUS.md until he rules. The three
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
| RT-142 | The STATUS.md paragraph as it can honestly be written, and the registered requirements before this position becomes a localization target | — | DRAFTED, AWAITING JOHN | Drafted in part 4 of the review file. Its load-bearing choices: the other-agent result is the headline and is stated quantitatively; the clearing cell is recorded and explicitly **not** carried forward as a clearance, with all four reasons attached; the target is named as the register index and not the registered marker word; and the line stays parked under the registered term *not testable (localization)*. The six registered requirements before the position becomes a lesion target are listed from Part 3 of `separation-clause-requirements.md` with A3 §3.2. One point that must not be elided: the other-agent run is the first execution of the **probe** half of the registered other-index control; Part 3 item 2 asks for the **lesion** half, a localized other-index subspace whose ablation leaves the self-directed condition intact. The run found no such subspace at any testable position, so there is nothing to ablate and that control remains unavailable. Running the probe half does not discharge the requirement. |
