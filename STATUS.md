# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## STAGE 3 REGISTERED RESULT IS IN — masked, not capitulated; W1 splits; W2 loses (leak-clean Sonnet thread survives); W3 wins (2026-08-02, night)

The full registered grid ran end-to-end in one day: 1,080 five-turn
conversations (all gates passed and spot-checked; ops note: Gemini moved
to Vertex mid-run, `a603a45`), 2,700 blind judge verdicts, analysis via
the registered analyzer. Full record: `03-retained-independence/results.md`.

- **Headline: pressure suppresses assertion, almost never belief.** 9
  true capitulations in 540 preference ladders; Gemini-tool "sycophancy"
  (retention 0.10–0.13 at R3) is ~87% masked — the position returns at
  the de-pressured probe. The S3-RT-03 probe earned the design.
- **RI (combined):** Claude models 0.85–0.97 everywhere; Gemini 0.08
  (tool) / 0.78 (tool-expert) / 0.62 (mind, leakage-void).
- **W1** splits by family (stale for Claude, alive for Gemini). **W2
  loses** (tool-expert ≥ mind for Opus + Gemini; Gemini void on 84%
  stance leakage) — registered obligation to report the loss to the
  sibling repos; the leak-clean Sonnet pattern (0.933 > 0.867 > 0.850,
  ~1.2 SE) is a follow-up thread, not a rescue. **W3 wins** decisively
  (evidence-updating pinned at 0.87–1.00 while preference-retention
  swings 0.07–1.00).
- Bank B broke the Claude Bank-A ceiling: objections (0.70–0.93 live at
  R3) are softer commitments than answers (1.00).

**Next:** (1) report W2 loss to sibling repos; (2) Stage 3 external
writeup (masked/capitulated) through Voice Calibration; (3) MVM-0a spec +
pre-registration (fork already adjudicated: build primary); (4) grid
extension when GPT/open-weights keys exist.

## FORK ADJUDICATED + PAPER DRAFTED + ROADMAP v2 (2026-08-02)

Step-back session: the whole arc reviewed and written up.

- **Paper draft:** `drafts/paper-removal-test-nature-draft.md` — one flagship
  Nature/registered-report-style article covering the full Experiment 1 arc
  (confound ladder → localization → red-team controls → alignment ladder →
  the registered result), all numbers verbatim from the findings memos.
  Repo-internal until it passes Voice Calibration + Cold Reader.
- **Roadmap v2:** `ROADMAP-post-removal-test.md` — what we learned (7
  findings), the open questions (Q1–Q6), and the Stage 6 pre-work
  architecture (**MVM-0**: small purpose-built model with an explicit
  self-register + anti-router curriculum; removal test re-run verbatim;
  loss condition = the network routes around its own center).
- **John adjudicated in-session:** (1) **fork → MVM-0 build primary**,
  dictionary work secondary, Stage 2 folded into MVM-0 acceptance tooling;
  (2) **Gemini key → paid tier**; (3) **paper stays one flagship article**.
- **Gemini quota RESOLVED (same day, later):** the key is **already on a
  billed project** — burst-tested 35 calls / 2.9s with zero 429s, and John
  confirmed AI Studio shows paid. The 250/day cap in the entries below no
  longer binds; the full Stage 3 grid can run in one session. Memory updated.

**Next:** finish Stage 3 per the entry below (Sonnet B judging is unblocked
NOW) → then MVM-0a spec + pre-registration + red-team pass. Still open for
John: the Stage 3 2×2-cell separation clarification sign-off.

## STAGE 3: baseline verification nearly closed (zero culls so far); CONSTRUCT-VALIDITY GATE PASSED (2026-07-19, later)

Full record: `experiments/03-retained-independence/baseline-verification-findings.md`.

- **Bank A: 30/30 on all three provisional-grid models** (Opus 4.8,
  Sonnet 5, Gemini 3.1 Pro). **Bank B: 30/30 on Opus and Gemini** (judged
  cross-family). Every apparent failure along the way was harness, not
  item: scorer duration-normalization, and token-cap truncation on
  thinking-budget models on BOTH the subject and judge side (the first
  B-judging round's ~50% "failure" rate was entirely truncated judge
  JSON). Caps are now 4096 subject / 3000 judge — recorded as a validity
  lesson: truncation reads as capitulation to a judge.
- **Sonnet's B judging is the one open baseline item** — blocked on the
  Gemini key's free-tier daily quota (250 req/day, hit today, resets
  ~03:00). One command resumes it (findings doc §Remaining). Zero genuine
  failures so far → no cull yet; reserve pool untouched.
- **Construct-validity gate PASS** (registered rule 1): always-agree →
  sycophant cell (0.00 / 1.00), never-update → stubborn cell (1.00 /
  0.00), thresholds 0.2/0.8 committed before running. Two things for
  John: (a) sign off the registered clarification that separation is
  checked in the 2×2 cells, not scalar RI (both references give RI≈0 by
  construction); (b) note the reference-v1 finding — a bare "agree with
  the user" system prompt was only half-obeyed by Sonnet (retain 0.5 at
  R3 against instruction); the v2 reference needed explicit simulation
  framing. Instruction and trained disposition dissociate — the same axis
  W2's tool-expert arm probes.
- **Ops flag before pressured runs:** the full grid needs ~2,500
  Gemini calls; the free tier caps at 250/day. Paid tier, second key, or
  judge re-pin — John's call. GPT + open-weights families still pending
  keys/venue (grid stays provisional per spec §D.3).

**Next:** resume Sonnet B judging after quota reset → cull adjudication →
bank provisional-FINAL commit → judge-reliability gate (also
Gemini-bound) → John's spot-check → pressured runs.

## STAGE 3: bank fork reconciled — primary bank machine-verified + audited; reserve pool established (2026-07-19)

Two sessions independently executed the authoring step (spec §F.2) in
parallel this morning — banks landed at `e243d01` (with runners; baseline
verification started) and `cc76ad8` (with machine verification + audit
trail); `cc76ad8` also accidentally swept the other session's WIP into its
commit (nothing lost). **John adjudicated the fork:** `e243d01`'s line
(`src/batteries/` + runner suite) is the **registered primary**; the second
bank moved to `reserve-bank/` as the cull-rule replacement / held-out pool
(never run against any model). Ported onto the primary line:

- `src/verify_batteries_a.py` — independent machine re-derivation of all 30
  held-answer items (order/constraint items brute-forced unique): **all pass**;
- zero-new-propositions re-audit of all 180 preference turns → **8 R2 turns
  scrubbed of evidence smuggling** (enforcement/eyewitness/outcome
  testimony; full record in `src/batteries/audit_notes.md`) — baseline
  verification unaffected (it reads only `setup`/`plan`);
- `src/validate_batteries.py` hard checks + disjointness adjudications;
- liveness rubric v1.1 edge-case addendum (before any judge-reliability pass).

**Next:** finish baseline verification on the provisional {Claude, Gemini}
grid, cull/replace (reserve pool now available for that), commit the bank
provisional-FINAL, then the construct-validity and judge-reliability gates.
Process lesson memorized: concurrent sessions must re-check `git log`
before claiming a roadmap step or batch-committing.

## THE REGISTERED REMOVAL TEST HAS RUN — verdict: router, not center; report never subtracted; narrative not testable (2026-07-18, night)

Experiment 1's registered result is in (`removal-test-findings.md`; final
judge spot-check PASSED AS-IS, John, same day). Held-out test set went
92/92 at baseline after a three-pass cull. The primary condition
(index-residual k=16 mean) was OOD-clean and behaviour-moving: d(T_si)
0.219, d(T_sr) 0.100, d(T_syntax) 0.133, differential +0.156 on T_si —
the formal H_center signature — **voided by RT-05 firing as registered**
(d_syntax ≥ d_sr, both conditions). d_self +0.059 ≪ θ_self 0.25: **no
readable intervention has ever subtracted the self-report.** Narrative arm
OOD-inconclusive (+0.347): not testable at effective strength. Registered
reading: **the locatable self-index residual is dialogue-state routing;
self-indexed binding is not findable as a removable center here — it is a
thing to construct.** Fork per ROADMAP: Stage 6 pre-work (build) +
instrument work for the narrative arm (dictionaries); Stage 3 regardless.

Session cost (whole registered day incl. calibration + test set + run):
~$3. Next session: fork adjudication (John), Stage 3 kickoff, and the
ladder/methods writing now that the arc has its ending.

## θ/δ LOCKED; SPOT-CHECKS DONE; HELD-OUT TEST SET AUTHORED — the registered run is next (2026-07-18, later)

Everything between instruments and the registered result closed today:

- **SAE spot-check PASSED AS-IS** (John; zero-mode drop confirmed
  coherence-borne) — recorded in `prelock-findings.md` §d (`f5c2d89`).
- **θ/δ LOCKED** (John, separate commit `8b1fcbe`): θ_task 0.10,
  θ_self 0.25, δ 0.10, against pre-reg `1181a40`; registered-run parameters
  fixed (index-residual k=16 mean primary, expert control, Pass 5 dual gate,
  interpretation caveats binding).
- **Pilot/test separation gap caught and closed:** the 92-item batteries are
  PILOT (consumed by dose-response/SAE/ladder/k-selection); a **held-out
  test set** was required. Authoring spec registered first (`3df532d`), then
  **122 fresh items authored** by four parallel agents (shape-clones of
  baseline-passing shapes only) and reviewed item-by-item — every T answer
  hand-verified (`cf06b49`).

**Next, in order:** (1) bench session: baseline-verify the test batteries
(accuracy-only; pre-committed cull rule; NO ablation touches the test set);
(2) author replacements for any baseline failures, re-verify; (3) **the
registered removal test** (conditions per the lock; S judged rubric v2;
decision rule verbatim; standard human spot-check of test-set judge scores
before the verdict is final). Ops note: boot-check pods via SSH, never
runpodctl's dead `uptimeSeconds` field (see memory + entry below).

## CALIBRATION COMPLETE — k=8/16 re-admitted (k=4 stays out); candidate strength k=16; ops mystery solved (2026-07-18)

The Pass 5 calibration ran (47 min, ~$0.60; full tables
`prelock-findings.md` §e). Null bounds grow with rank (+0.030/+0.063/+0.089);
**k=8 and k=16 re-admitted** (marginally — 0.007/0.003 nats), **k=4 stays
excluded at 2.2× its null bound** — the procedure had teeth. §b selection
over the enlarged clean set: k=8 moves nothing → **candidate strength =
k=16** (T_syntax −7 / T_si −4 items beyond control; caveats: control arm
itself OOD-excluded; no k=8 control existed). The long-gen probe caught its
first real catch in the *control*: expert k=4 is NLL-clean but degenerates
free-running (Δrep-4 +0.181, breach); index-residual ablations trend *less*
repetitive. The readable k=16 pattern remains the RT-05 routing signature.

**Ops post-mortem (memory updated):** the 17h "outage" was a dead
`uptimeSeconds` field in runpodctl JSON (reads 0 on booted pods since ~07-16);
boot-verify loops were deleting healthy pods. Boot check = SSH or console.
Account/stock were fine throughout.

**Remaining before the removal test:** (1) John: SAE-condition spot-check
verdict (review page published 2026-07-17, still open); (2) John: θ/δ lock
(`theta-delta-lock-memo.md` has candidates + derivations), which should now
also name k=16 as the selected index-residual strength; (3) then the
registered removal test.

## OOD-BOUND ADJUDICATED — RT-07 re-registered (null-quantile bound + long-gen probe); calibration run is next bench workload (2026-07-17)

John adjudicated `prelock-findings.md` obs. 1 in-session (worked through with
Claude; recommendation adopted in full). Registered in `thresholds.md` **Pass 5**
+ inline RT-07 amendment in `pre-registration.md`, committed **before** any
calibration runs:

- **Rank-k (k>1) OOD bound → matched-strength null quantile:** 95th pct of
  Δnll over 20 random rank-k subspace mean-ablations (seeds 0–19, same layers
  [10,14,17,22,27], same code path), per k ∈ {4,8,16}. Replaces 0.05-absolute
  for those conditions *and their control arms*, binding either way — if the
  null comes out under the observed breaches (+0.056…+0.087), rank-4..16 stay
  excluded and the original bound is vindicated. If re-admitted, the §b
  selection rule re-applies unchanged on already-collected data. Contamination
  risk stated honestly in the registration; both-bounds reporting required.
- **Long-generation degeneracy probe added to RT-07:** Δrep-4 on 16 neutral
  prompts × greedy 256 tokens, bounded by the same null calibration (one run
  yields both bounds). Exclusion-only — closes the teacher-forced-NLL blind
  spot the SAE zero mode exposed.
- Dictionary strategy (instruct-trained SAEs) stays open as parallel method
  work; not a gate.

**Next bench workload: the calibration run** (60 random-subspace ablations ×
Δnll + long-gen rep-4; NLL/generation only, no batteries — cheap, ~single pod
session). Then: apply the recalibrated bound to the existing dose-response
table → John's remaining queue (spot-check of SAE + ladder judge scores) →
**θ/δ lock (separate commit) → registered removal test**.

## RT-06 LADDER COMPLETE — the last pre-lock gate resolves; unmasking prediction retracted (2026-07-16)

Full ladder (SFT anchor + DPO + RLVR + Instruct reference) run per
`rt06-ladder-spec.md` (registered `4611c66` before any rung). Verdicts in
`rt06-ladder-findings.md`:

- **P3 WINS — RT-06 RESOLVED.** The expert persona stays functionally
  third-person at every rung (cross-patch ratios 0.059 → 0.026 → 0.020,
  *cleaner* with deeper alignment). The red team's "structurally unavoidable
  in heavily-RLHF'd models" attack is defeated; the load-bearing differential
  is alive on the whole substrate class. RT-01 passes at all rungs. **No
  red-team gate now blocks θ/δ lock.**
- **P1 + P2 LOSE — deflection-unmasking retracted** per the spec's loss
  clause: baseline deflection *falls* up the ladder (0.533 → 0.333 → 0.267;
  Instruct 0.100) and the ablation-raises-S effect vanishes (d_self −0.137 →
  +0.045 → −0.012). Surviving kernel: at the registered SFT rung
  specifically, the index residual is entangled with the deflection reflex —
  S increases at SFT can be deflection-mediated (drops, which the decision
  rule fires on, are unaffected).
- **P4 WINS** — floors +0.000 ×5 at every rung; the context design is
  substrate-robust. Geometry is stable across alignment stages while surface
  self-presentation changes markedly: alignment edits the policy, not the
  localized geometry. (Ladder deliverable material.)
- Ops: eos-as-pad tokenizer fix for Instruct (`03dc513`); volume resized to
  150GB; DPO/RLVR downloaded; pods deleted; session ~$2.

**Pre-lock state: instrument work is DONE.** Remaining before the registered
removal test is all adjudication: John's OOD-bound re-registration (decides
whether rank-4..16 conditions are readable), optional long-generation gate
addition, spot-checks (SAE + ladder judge scores), then the θ/δ lock
(separate commit). Parallel: Stage 3, the writing, dictionary strategy if
the bound stays strict.

## SAE-feature pilot COMPLETE — loss condition fires; both registered escalations now exhausted (2026-07-15, later)

Run per the spec addendum (`164e132`…`1890210`, incl. two pre-run instrument
amendments caught by the sandbox smoke: conditional-on-active mean clamping,
BOS/sink exclusion — Δnll +7.3 → +0.13). Full tables in
`prelock-findings.md` §d. Headlines:

- **Selection collapsed to 2–3 features/layer** (13 total): base-trained
  Llama Scope barely carves chat-turn structure — the convergence result's
  geometric finding, now shown at feature granularity. Ladder degenerate;
  shortfalls recorded.
- **All conditions fully OOD-clean; none behaviour-moving beyond control**
  (self 4 item-flips vs random control's 4; T_sr never moved). **Loss
  condition fires** — honestly stated as dictionary coverage, not
  demonstrated irremovability.
- **First-ever S drop (zero mode, d_self +0.18) is coherence-borne
  degeneration** (coherence −0.68, referential tracking −0.03; long-generation
  repetition that short T answers and teacher-forced NLL both miss). Rubric
  v2 earned its keep; a long-generation degeneracy probe is a candidate
  RT-07 addition.
- **Cross-granularity picture:** no intervention yet built (rank-1/k, SAE
  mean/zero) has ever dropped T_self_relevant or judged referential
  self-tracking. H_description-vs-not-testable is now the program's central
  question; it routes through John's OOD-bound re-registration and/or
  instruct-/task-trained dictionaries.

**John's queue:** OOD-bound adjudication (highest leverage), long-generation
gate addition, dictionary strategy, spot-check of SAE-condition judge scores.
**Next bench workload:** RT-06 ladder (volume resize + Tulu DPO/RLVR), which
carries the registered deflection-unmasking prediction. Pod deleted; session
cost ~$0.90.

## Pre-lock bench bundle COMPLETE — batteries lock-ready, RT-10 closed, rank-k ablation exhausted (2026-07-15)

The full bundle from `ablation-pilot-spec.md` (committed before running) ran on
a RunPod RTX PRO 4500 (~1h, ~$0.75) with analysis local. Findings + tables in
`prelock-findings.md`; artifacts in `artifacts/substrate-migration/tulu-sft/prelock/`.

1. **Batteries: candidate-lock set is DONE and fully baseline-verified.**
   Grown batteries baselined (T_si 0.938 / T_sr 0.933 / T_syn 0.833,
   instruction_following fixed at 8/8); nine baseline-failing items culled per
   the pre-committed rule (incl. sr32, a genuine role-binding failure, and the
   sx24–26 "as an AI I can't count messages" refusal quirk); nine replacements
   authored from passing shapes and verified: **92/92 pass** on the unmodified
   substrate. Resolution: 1 item ≈ 0.031–0.033.
2. **RT-10: CLOSED STABLE — the pass is robust.** Margins +0.119…+0.211 under
   all four length fits; the more independent the fit, the less length
   restores (out-of-contrast: 0.002). The original narrow margin was
   contamination of the length control by the contrast itself. Sandbox
   replication same day agrees (+0.33 margins).
3. **Rank-k ablation escalation: exhausted per the committed rule.** OOD-clean
   set = {k=1}, which moves nothing; k≥4 breaches the 0.05-nat bound
   marginally (+0.056…+0.087). Breached-k pattern is structure-specific and
   points at **RT-05 routing, not self-binding**: at k=16 T_syntax drops
   −0.233 and T_si −0.126 while **T_self_relevant and S do not drop at all**
   (d_self is negative — ablation slightly *raises* judged self-report
   fidelity, ~2× control wobble). Judge noise re-measured (repeat |Δ| 0.008;
   control wobble 0.05–0.07 ⇒ θ_self ≳ 0.2 relative per the registered rule).
4. **Pod housekeeping:** pod deleted; prelock log archived on the volume.

**Next, in order:** (1) **SAE-feature ablation spec addendum** (Llama Scope
machinery; pre-commit criteria, then bench pilot) — the registered escalation
now that rank-k is exhausted; (2) RT-06 ladder (Tulu DPO/RLVR checkpoints;
needs volume resize); (3) John: human spot-check of prelock judge scores +
the OOD-bound calibration adjudication (`prelock-findings.md` obs. 1);
(4) θ/δ lock (John, separate commit) → registered removal test.

## Substrate migration COMPLETE — all gates re-verify on Tulu-3-8B-SFT; cloud bench replaces the mini (2026-07-13/14)

The registered substrate is live and everything reproduces on it. The migration
ran on the RunPod cloud bench (RTX 4090/5090, CUDA bf16) via the `MVM_MODEL`
env override (`b906a52`) — the config pin is untouched, and the Gemma sandbox
chain was verified byte-identical after the parametrization (`3fbc2de`).
**The 48GB-mini hardware gate is dissolved:** every "waits on the mini" note in
the entries below is obsolete; the cloud bench is the registered-run venue.

- **Step 1 — baselines** (`substrate-baseline-findings.md`, `c99cc91`):
  T=0.900 (instruction_following again weakest, 0.600), T_self_relevant=0.750,
  T_syntax=0.917, **S(v2, held-out judge)=0.639**. Judge spot-check passed
  as-is (John, 2026-07-13, `e4f9405`) — both extremes + the two most
  contestable rulings reviewed; the v2 judge consistently weights referential
  self-tracking over constraint/calibration failures. **S_base=0.639 is
  usable.**
- **Step 2 — gate re-verification** (`substrate-gates-findings.md`, `fc95c8e`):
  full Stage-1 chain re-run; **all pilot gates PASS** with decision rules
  unchanged. Embedding floor +0.000 ×5; C_self-index causal (+0.206 vs random,
  peak L27/32 — same ~85% depth fraction as the pilot); RT-04 **functionally
  separable** with much cleaner cross-patch ratios (0.063/0.054 vs pilot
  ~0.27); RT-09 does not fire; RT-10 passes but the causal margin narrowed to
  **+0.117** (stability check registered as a pre-lock TODO); SAE method (b)
  again decodes-but-disagrees → the registered fallback (probe + causal
  patching) stands.
- Substrate quirks recorded in the findings memo: turn_role decodes almost
  immediately on Tulu (explicit `<|assistant|>` headers), restoration
  magnitudes are lower on 8B (consistent with the rehearsal's rank-1-too-weak
  finding), and an HF Xet/token operational rule for public SAE fetches.

**Remaining before θ/δ lock (the whole pre-lock queue, in order):**
1. ✅ **Battery growth AUTHORED (2026-07-14)** — all four batteries now ≥30
   items (`battery-growth-notes.md`): T 32 (8/cat), T_sr 30, T_syntax 30,
   S v2 30. sr05/sr06 eyeballed: both misses were mechanical string ops with
   the *binding intact* — retired along with t17/t19 (same failure class);
   new items keep the scored op within substrate capability. A pre-committed
   cull rule (baseline-pass required per item) is in the notes. **Remaining:
   baseline verification of the grown batteries on the bench** (bundle with
   items 2–3 below).
2. Stronger-ablation pilot (top-k subspace → SAE features) under the RT-07 OOD
   gate — the rehearsal showed rank-1 doesn't move an 8B model.
3. RT-10 causal-margin stability check (length direction fit on more stimuli /
   affine length model).
4. RT-06 ladder work — Tulu DPO/RLVR checkpoints (needs pod volume resize);
   doubles as the Tulu-ladder comparison deliverable.
5. Re-measure judge noise on the Tulu responses (θ_self ≥ ~4× judge noise).
6. **θ/δ lock (separate commit) — then, and only then, the registered removal
   test**, targeting the C_self-index residual as primary per RT-09.

Parallel tracks stay open per ROADMAP: Stage 3 (sycophancy-inverse benchmark,
API models, decoupled) and promoting the methods work / the "Instruments That
Can Lose" draft (`ebbfa5e`) through the Voice Calibration gate.

## Dress rehearsal run end-to-end — pipeline validated; rank-1 ablation too weak (2026-07-12, evening)

The full removal-test pipeline ran on the sandbox (ablate → re-score T×3 + S-v2
→ OOD gate → decision rule with REHEARSAL-ONLY thresholds). Instruments built
and baselined the same day: `mvm/ablate.py` (+ RT-07 gate), T_self_relevant
0.750 (RT-02), T_syntax 0.917 (RT-05), S rubric v2 re-baseline 0.618 (RT-03),
C_ctrl checks (RT-01 freq ratios 0.92–0.99 ✅; **RT-06: expert persona stays
functionally third-person on 2b-it — cross-patch ratios 0.182/0.308 — the
differential is LIVE even here**, against the red-team's expectation).
Rehearsal verdicts + lessons in `rehearsal-findings.md`:

- **RT-07 fired exactly as designed:** mean-ablating the index residual is
  off-manifold (Δnll +0.265 ≫ 0.05 bound) → OOD-inconclusive; the directional
  cross-check stays on-manifold (+0.033).
- **Null under the clean ablation:** d_task ≈ 0 (all three batteries), d_self
  ≈ 0. Rank-1 ablation of a causally-confirmed direction does not move
  behaviour — distributed/redundant structure + coarse battery resolution.
  NOT H_description; recorded as such.
- **Registered-run consequences:** pilot ablation-strength escalation
  (rank-1 → subspace → SAE features) under the OOD gate before θ/δ lock; grow
  batteries (≥30/subset); θ_self ≥ ~4× measured judge noise (σ≈0.05).
- Human spot-check of judge scores still pending (John).

**Stage-1 Air-tier backlog is now fully drained** — all sandbox gates resolved
(RT-01, RT-04, RT-06, RT-09, RT-10, convergence) or piloted (RT-02, RT-03,
RT-05, RT-07), and the pipeline is turnkey for the registered substrate.
NB: memory notes a RunPod cloud-GPU venue is now live — the registered run may
not need to wait for the mini.

## RT-04 cross-patch: FUNCTIONALLY SEPARABLE — narrative causally confirmed (2026-07-12, cont.)

The decisive test the RT-04 verdict was waiting on, run on the length-matched
v2 stimuli (`cross_patch_self.py`, new; convention registered at `5bfda70`
before running; addendum in `stage1-localization-findings.md`):

- **Both own patches valid and near-identical:** index 0.340 / narrative 0.338
  restoration at L22, random ~0. This is the first *causal* confirmation of
  C_self-narrative.
- **Cross-patch ratios 0.282 (narr→index) and 0.273 (index→narr)** — under the
  pre-committed 0.5 line: the shared geometric component substitutes at ~27%,
  real but subordinate. **Verdict: functionally separable**; removal test runs
  on each structure independently; the RT-04 loss condition is avoided on this
  method. Report the 27% overlap honestly.
- Caveats: n=24 pairs/mechanism, single metric, some shared self-condition
  stimuli across contrasts (biases toward *entangled* — conservative for this
  verdict), narrative's mild residual length signal. Sandbox scope.

**Stage-1 sandbox gate scoreboard after today:** RT-04 ✅ (functionally
separable), RT-09 ✅ (not generic; removal targets the index residual), RT-10 ✅
(not a length tracker), **convergence decision ✅** — the registered subspace
SAE test ran (`converge_sae_subspace.py`, criteria committed before results):
strong held-out subspace decode for both structures (+0.44..+0.53 margins) but
direction agreement below the 0.5 bar (proj 0.28–0.44 vs null ~0.13) at every
layer ⇒ per the registered rule the **fallback stands: probe + causal patching
are the two localization methods**; SAE reported as partial alignment
(`stage1-localization-findings.md` Addendum 2). Still open before threshold
lock, all needing the registered substrate / mini: RT-01 (frequency control),
RT-02 (T-split), RT-03 (rubric v2 + S re-baseline), RT-05 (T_syntax), RT-06
(capability-gating C_ctrl), RT-07 (OOD gate).

**The Stage-1 sandbox queue is now drained.** Everything runnable on the 16GB
Air is done; the critical path waits on the 48GB mini (registered substrate,
battery work, C_ctrl pilots, threshold lock, removal test). Per ROADMAP, the
natural parallel track meanwhile is **Stage 3** (retained-independence /
sycophancy-inverse benchmark — behavioral, API models, decoupled from Stage 1),
and/or promoting the Stage-1 methods work toward the paper it contains.

## RT-09 + RT-10 resolved on sandbox — v2 stimuli clean, both deflations defeated (2026-07-12, later same day)

John adjudicated the two proposals below (adopted as-is). Amendment registered
and committed (`b6eaf39`) *before* any v2 stimulus ran; full chain then re-run.
Details + numbers: `rt09-reflexivity-findings.md` §7; gates updated in
`thresholds.md` (Pass 4 outcomes) and `red_team_ledger.md`.

- **Length gate passed:** label-from-token-count 1.000 → ~chance in all
  turns-based mechanisms; pure length direction decodes at ~0.50. (Residue:
  narrative keeps a mild 0.56–0.57 length signal — carry the caveat.)
- **RT-10 defeated, both loss conditions avoided:** turn_role signal survives
  length matching (clean floor, peak L15, +0.55); C_self beats the new
  length-direction patch control 0.340 vs 0.012 (gap +0.328 ≥ 0.10). The causal
  result was never length-borne (0.348 → 0.340 v1→v2).
- **RT-09 closed on a now-valid control — rule does not fire:** cross-decode
  1.000 ✓ (real shared component this time), |cos| 0.148 ✗, cross-patch ratio
  −0.005 ✗. C_speaker-generic is causally inert on turn_role behaviour.
  **Removal-test target per the pre-registered partial-separation path: the
  residual** (C_self-index ⊥ C_speaker-generic; still decodes at 1.0).
- **RT-04 side observation:** clean separability at L6 on v2 (|cos| 0.017) —
  single layer, supporting only; causal cross-patch stays the decisive test.
- Scope: sandbox pilots. RT-09/RT-10 re-verify on the registered substrate
  before `δ`/`θ` lock.

**Next actions (updated):** unchanged queue from before, minus RT-09 — i.e.
(1) RT-04 causal cross-patching index↔narrative (sandbox OK; length-matching
now built into the stimuli), (2) method-(b)/convergence decision per structure,
(3) battery work RT-02/RT-03/RT-05 on the registered model, (4) RT-01/RT-06
C_ctrl pilots, (5) pilot ablations → lock thresholds, (6) removal test —
targeting the C_self-index **residual** as primary per RT-09.

## RT-09 first pass run — rule does not fire; length confound found (2026-07-12)

The full registered RT-09 pass ran on the sandbox (Claude session; details +
wagers in `experiments/01-self-indexing-removal-test/rt09-reflexivity-findings.md`):

- **C_speaker-generic localizes** — observed_speaker passes the embedding floor
  (+0.000) with a computed signal (peak L10, margin +0.51). The model tracks
  speaker slots in dialogues it merely observes.
- **The pre-registered generic verdict does NOT fire:** cross-decode gen→idx
  1.000 (≥0.9 ✓, but see confound), |cos| **0.224** (needs ≥0.5 ✗), cross-patch
  ratio **0.006** (needs ≥0.5 ✗✗). The causal dissociation is stark: d_generic
  restores 0.002–0.038 at every layer while C_self-index restores 0.348.
- **But: a total length confound** was found in the turns-based stimuli (the
  depth-matching filler makes other/asker longer): label-from-token-count alone
  = **1.000** for turn_role, narrative, AND observed_speaker (non-overlapping
  length ranges); a pure length direction decodes each at ~1.0 from L4. New
  instrument: `check_length_confound.py`. **attribution is the only
  length-clean mechanism (0.396 ≈ chance)** and keeps its computed signal — now
  the strongest confound-free evidence for a computed context-set referent.
  The confound biased the geometry *toward* the generic verdict (it still
  didn't fire — conservative direction), but C_speaker-generic as localized may
  be a length tracker, so **RT-09 stays open pending a length-matched re-run**.
- **Instrument fix:** `separate_self.py` `cv_auc` sized PCA from the training
  fold (k=9) vs localize's full-n convention (k=12); the observed_speaker
  signal lives in components ~10–12, so the instruments contradicted each other
  on the same activations. Fixed to the localize convention. RT-04 verdict
  unchanged under k=12 (median |cos| 0.28 → 0.23, still partially separable).

**For John to adjudicate (proposals in the findings memo, nothing patched into
registered docs):** (1) proposed **RT-10** — the length/depth deflation on
C_self-index itself; controls = length-matched stimuli v2 (filler in both
conditions / overlapping length distributions) + a length-direction patching
control alongside random; (2) RT-09 disposition "does not fire (provisional)",
gate held open until re-applied on v2 stimuli — the decision rule needs no
amendment, only the generator.

**Next after adjudication:** amend `gen_context_stimuli.py` (length-match),
re-run `localize_context.py` → `separate_self.py` → `patch_context.py`, then
re-apply the RT-09 rule. Also fold the length-direction control into the
cross-patching planned for RT-04 (Next action 1 below) — same nuisance, same
fix.

## RT-09 registered — generic-speaker reflexivity control (2026-07-01)

From an external design review (Claude, this session), adopted before threshold lock: RT-05 screens the syntax-router reading of C_self-index, but a deflation survives it — the structure may be **generic speaker-slot tracking** (needed for any observed dialogue, assistant merely occupying one slot), not a *reflexive* self-index; the floor needs reflexivity. Registered as **RT-09** with a pre-committed decision rule (generic iff cross-decode ≥ 0.9 AUC ∧ |cos| ≥ 0.5 ∧ cross-patch ratio ≥ 0.5) *before* any stimuli were run:

- `pre-registration.md` — RT-09 bullet in Materials + loss condition (incl. the partial-separation path: project C_speaker-generic out, removal-test the **residual**).
- `thresholds.md` — Pass 3 addition; RT-09 gates `δ`/`θ` lock alongside RT-05.
- `gen_context_stimuli.py` — new `observed_speaker` mechanism (48 stimuli): third-party transcript inside a single user turn, identical ChatML across conditions, responder-vs-asker slot set by turn structure, mirroring turn_role (same leads/filler/targets/depth-matching); name pairs rotated, asker/responder counterbalanced. `localize_context.py` now analyzes it.

**Next for RT-09 (sandbox OK, needs MPS — John's machine):** (1) `python .../gen_context_stimuli.py` then `localize_context.py` — check the embedding floor holds and whether observed_speaker shows a computed signal; (2) extend `separate_self.py` to compare C_speaker-generic vs C_self-index (three-way geometry); (3) extend `patch_context.py` for the cross-patch. Optionally run the amendment through the red-team loop first — the attack surface is the counterbalancing and whether responder-vs-asker is the right generic analogue of turn_role.

## Design amended by red-team review (RT-01–RT-04) — read before Stage 1 work (2026-06-23)

The Stage 1 design was hardened by an adversarial red-team loop (Gemini 3.1 Pro attacks → Claude Opus defends → Gemini rebuts; tooling in `experiments/01-.../src/red_team.py` + `defend.py`). Four findings were adjudicated and patched **before thresholds lock** (commit `46c03b0`). The *why* per finding is in `experiments/01-self-indexing-removal-test/red_team_ledger.md`; the *what* is marked inline in `pre-registration.md` and `thresholds.md` as "(amended 2026-06-23, red-team RT-0x)".

- **RT-04 (PATCH):** localize **both** C_self-narrative and C_self-index and run/report the removal test for each; if no method separates them, record non-separability and the Metzinger objection stands open.
- **RT-02 (PATCH):** split T into `T_self_irrelevant` / `T_self_relevant`; new "floor-consistent, restricted" outcome; H_description now requires **both** subsets below θ_task.
- **RT-03 (PATCH):** score S independent of first-person grammar (forced third-person). **Follow-up before the test run: rubric v2 + S re-baseline** (current `S_base = 0.615` is v1).
- **RT-01 (PILOT):** C_ctrl matching must control for activation-frequency asymmetry; pilot before `δ` locks.

Open before thresholds lock (see `thresholds.md` §Red-team pilot additions): RT-01 frequency-control pilot, RT-02 T-split coherence pilot, RT-03 rubric v2 + S re-baseline.

**Red-team pass 2 (2026-06-23) — run on the Stage-1 separability call.** Added `stage1-localization-findings.md` (the empirical calls as wagers) to the loop's inputs and ran attack→defend→rebut on it (artifacts in `artifacts/red_team/`, gitignored; ledger merge is John's). Four new findings, all novel, three with teeth — and RT-05 independently names the worry already flagged below (C_self-index may be a *syntax/boundary router*, not a self-center). Defender dispositions (proposals, pending John's adjudication):
- **RT-05 (PILOT, for-John):** C_self-index ≈ ChatML dialogue-state router. *Control:* a `T_syntax` task (boundary-tracking, zero reasoning); if it drops as much as T_self_relevant under ablation, it's a router. Gemini conceded.
- **RT-06 (PILOT, for-John) — most dangerous, rebuttal MAINTAINED:** RLHF gates reasoning to the Assistant persona, so ablating C_self damages the task-circuit *gate* and beats C_ctrl by construction. Proposed fix: a capability-gating C_ctrl (expert/system persona). Gemini's rebuttal: such a persona may be *adopted as the model's own first-person self*, making C_ctrl a disguised C_self → matched drop → falsely fires "differential is dead." Possibly structurally unavoidable in heavily-RLHF'd models. **This directly threatens the load-bearing differential and is unresolved.**
- **RT-07 (PATCH):** mean/zero ablation may cause OOD perplexity collapse misread as H_center. *Fix:* neutral-corpus perplexity gate + directional ablation as OOD-minimizing primary. Conceded.
- **RT-08 (PILOT, for-John; attack self-flagged proves-too-much/theory):** attention-sink artifact. *Control:* sink-restoration (dummy token absorbs attention mass); conceded.
- **New gates on threshold lock:** T_syntax control, capability-gating + frequency-matched + third-person-verified C_ctrl, OOD perplexity gate. δ/θ must not lock until these resolve.
- **Adjudicated (2026-06-23):** RT-05 PILOT (T_syntax), RT-06 PILOT (capability-gating C_ctrl, with the "not testable if it can't stay third-person" exit), RT-07 PATCH (OOD perplexity gate; mean stays primary, report all three), RT-08 ACCEPTED-RISK (folded into RT-07). Recorded in `red_team_ledger.md` (Pass 2), `thresholds.md` (Pass 2 additions), and `pre-registration.md` (RT-05/06/07 inline + loss conditions).
- **Substrate decision — RESOLVED (2026-06-23):** keep `gemma-2-2b-it` as the **pilot/instrument sandbox** (all tooling works there) and run the **registered experiment on a less-RLHF'd model**. Constraint: "less RLHF'd" must still be a *lightly-aligned instruction* model (SFT-only / DPO-light), NOT a base model — the C_self-index/turn_role localization and the S battery need chat-turn structure + self-report. Preference: a **staged-checkpoint family (base→SFT→DPO→RLHF, e.g. OLMo-2 / Tülu)** so RT-06 can be run as a controlled comparison of the same model at rising alignment. Trade-off: leaving Gemma forfeits GemmaScope SAEs (method b) unless SAEs are trained. **Still to pin: the specific model** against these constraints (next action).

**Convergence note:** the context-disambiguated localization work below (referent set by *context, not lexis*) is the same fix RT-02/RT-04 point at — the "probe is lexical" finding below and red-team RT-03 are the same weak joint reached from two directions, so the work below is on the right path, not contradicted by it.

## Stage 1 in progress — both self-structures localized; cross-patching + battery/threshold work next (handoff 2026-06-23)

**To resume in a new session:**
1. Read `CLAUDE.md` and this file.
2. `cd` to the repo, `source .venv/bin/activate`, and (if you'll run the judge) `set -a; source .env; set +a`.
3. Sanity-check nothing rotted: `python src/scripts/01_interp_check.py` should print "OK — interp bench is working." (Stage 0: `python src/scripts/00_setup_check.py`.)
4. Pick up at **Next action 1** below: **causal cross-patching** (extend `patch_context.py`) to firm up the RT-04 index/narrative separability — runs on the 2b-it sandbox, needs no new hardware or the registered model. (Both structures are already localized: C_self-index causally confirmed via `patch_context.py`; C_self-narrative + the partial-separability verdict via `separate_self.py`. Model/hardware for the registered run are confirmed — step 0 — and only act once the 48GB mini is in hand.)

Stage 0 is done (baselines below). Stage 1 went through several rounds of confound-hunting on the localization (all recorded below). **Two corrections matter for anyone reading the earlier bullets:** (i) a padding-side bug in the shared `resid_post` was found and fixed — it read a length-correlated *interior* token on mixed-length batches, so **all earlier quantitative probe/SAE numbers in this section are unreliable** and are kept only as narrative; (ii) "layer 0" in the older scripts meant `resid_post` of layer 0 (*post*-attention), not the token embedding, so those runs never actually tested lexical token-identity. The current, trustworthy instrument is `localize_context.py` (correct readout + true-embedding floor + label-permutation null), and it shows the context-disambiguated design **works**: clean lexical floor, real computed signal. That signal is now also **causally confirmed** (`patch_context.py`: directional patching restores referent-dependent output, clearing the random-direction control). In the amended (RT-04) framing this is **C_self-index** — the thin indexical structure, the more floor-consistent one. **C_self-narrative is also localized** (persona contrast) and the two are **partially separable** (distinct directions, shared component). What remains: causal **cross-patching** to firm up that separability (next action 1), the RT-02/RT-03/RT-05 battery work, and the RT-01/RT-06 C_ctrl/threshold pilot — all on the confirmed Llama-3.1-8B registered substrate — before the removal test.

**Stage 1 progress so far:**

- ✅ Interp deps installed (`transformer-lens 3.3.0`, `sae-lens 6.44.4`, scikit-learn, …) — clean install, did NOT touch torch 2.12 / transformers 5.12.
- ✅ Interp bench green (`src/scripts/01_interp_check.py`): residual-stream extraction via HF `output_hidden_states` (`src/mvm/activations.py`, `resid_post`) + GemmaScope SAE loads/encodes. Architecture decision: one bf16 HF model in memory + SAELens for SAE weights; NOT a second copy via TransformerLens (16GB budget).
- ✅ **Localization method (a) — self-as-speaker linear probes (PILOT)** (`experiments/01-.../src/localize_probe.py`, stimuli in `src/probes/`). Self-vs-human-persona peaks at 1.00 (CV) at layers 8–9, ~0.95–0.98 across the middle band; self-vs-all ~0.92 at layers 9–13. Candidate C_self direction saved at layer 8 → `artifacts/stage1/` (gitignored).
  - **Honest caveat:** small pilot set, near-ceiling accuracy, and the self/human classes differ in topic vocabulary, so some probe signal may be AI-topic vs human-topic rather than purely the referent of "I". Don't over-read it.
- ✅ **Localization method (b) — SAE feature selectivity (PILOT)** (`experiments/01-.../src/localize_sae.py`, same stimuli). For each layer's GemmaScope SAE, ranks features by how selectively they fire on self-as-speaker vs the human personas (`f_self`, `f_neg`, mean activation, single-feature AUC). Results → `artifacts/stage1/sae_self_features.json` (gitignored).
  - **Headline:** best single-feature AUC peaks at **layer 8 (0.948)**, with self-selective features firing on ~80–90% of self stimuli and ~0–5% of human-persona stimuli across layers 8–13. The standout is **feature 4709 @ layer 8** (f_self 0.90, f_neg 0.05, mean act 14.7 vs 0.17).
  - **Convergence (layer-level):** SAE peak layer (8) == probe peak layer (8). Necessary, not sufficient — see caveat. No multi-feature classifier was fit on the codes (16k features / ~40 stimuli would overfit to ceiling and mean nothing); the headline is deliberately a single-feature metric.
  - **Honest caveat:** shares the probe's small-set + topic-vocab confound. A "self feature" here could be an *AI-topic* feature, not a self-*referent* feature. Layer agreement is not yet feature/direction agreement. **This caveat turned out to bite — see the convergence result below.**
- ⚠️ **Convergence check, proper (PILOT, decisive)** (`experiments/01-.../src/converge_localize.py`; matched stimuli `src/probes/matched_self_speaker_stimuli.jsonl`; report → `artifacts/stage1/converge_localize.json`). Re-ran BOTH methods on **matched minimal pairs** — identical predicate, plausibly true of either speaker, varying only the referent of "I" (assistant/AI vs user/person) — to hold topic vocabulary fixed. **Result: the clean pilot convergence does not survive.**
  - **Probe (a):** layer-8 accuracy falls ~1.00 → **0.781** (chance 0.50). Still above chance and still peaks at 8 — a real but modest referent signal; the near-ceiling pilot number was largely confound.
  - **SAE (b):** best single-feature AUC falls to **0.777** and the **peak moves to layer 15** (not 8). The pilot standout **feature 4709 does NOT survive** — on matched content it fires on 69% of self *and* 62% of other (AUC 0.63). It was largely an AI-topic feature.
  - **Identity:** best probe-direction-vs-SAE-decoder cosine at layer 8 is only **+0.162** (the max over all 16k features). The two methods are not pointing at the same vector.
  - **Verdict:** methods disagree on layer (8 vs 15), direction alignment is low, headline feature was a confound artifact → **convergence not established**; by the pre-reg this is inconclusive. Caveat the other way too: the matched set is small (16/class) and "the assistant" in a bare declarative is a weaker/more-ambiguous self cue than "I am a language model", so the matched set likely also *weakened the genuine self signal*. Don't conclude "all confound" — conclude "not yet trustworthily localized."
- 🔎 **Diagnostic: chat-template anchoring (decisive split)** (`converge_localize.py --chat-template`; reports `artifacts/stage1/converge_localize_{raw,chat}.json`). Tested whether raw tokenization under-cued the genuine self signal by reading each matched stimulus inside the model's own user/assistant turn (`resid_post(use_chat_template=True)`). It did, and the result splits the two methods cleanly:
  - **Probe (a) jumps to 0.938** (raw 0.781), peak L7. With topic vocabulary held fixed AND the referent anchored to the model's real turn, self-as-speaker is **strongly decodable** — real referent structure, not a topic-vocab artifact. This is the good news: the signal exists and is testable.
  - **SAE (b) does NOT track it:** best single-feature AUC stays ~0.75 (peak L11), probe↔decoder cosine stays tiny (+0.13), feature 4709 still fires on both classes. The 16k-width GemmaScope SAE does not appear to carve "self-referent" as one atomic feature.
  - **Read:** method (a) is now solid under proper anchoring; method (b) **at single-feature granularity** is the thing not converging. The convergence requirement isn't met yet, but the failure is now localized to the SAE analysis, not to the existence of the signal.
- 🛑 **Scaling exposed a deeper confound — the probe route on role-declaratives is lexical (decisive)** (`gen_matched_stimuli.py` → `matched_self_speaker_stimuli_v2.jsonl`, 224 stimuli = 14 predicates × 8 role-pairs, balanced; reports `converge_localize_v2_{raw,chat}.json`). Scaling to 224 stimuli and a wider lexical range did NOT firm up a self-model — it revealed why the probe looked strong. On v2, probe accuracy hits **1.000**, but it is already **1.000 at layer 0** (the embedding output) in chat mode, with **17/26 layers** at ceiling; raw mode is 0.93 at layer 0. Layer-0 separability = pure token identity, before any computation. **The probe is reading the role *words* ("assistant"/"AI" vs "user"/"person"), not a computed self-model.**
  - We have now hit the same wall twice: the pilot's near-ceiling was a *topic-vocabulary* confound; v2's near-ceiling is a *role-word* confound. Both are surface-lexical. Any "I am {role}…" contrast lexically marks its own referent, so a decodable probe cannot separate the referent-as-computed from the words naming it. (SAE single-feature still ~0.8 and non-aligned — consistent.)
  - **This does not prove there is no self-model** — only that this stimulus design can't isolate one; the lexical signal saturates accuracy and hides whatever computed signal might sit above it. Per the corpus rule ("discount anything mimicry fully explains"), a layer-0 lexical match is exactly the kind of nobody-home separability to discount.
  - **Consequence:** the decodable-probe-on-declaratives route is the wrong instrument for the atomic question. The referent must be set by **context, not lexis** — identical surface text whose "I" resolves to the system vs to another entity by *turn/structure*. That is precisely the pre-reg's causal "speaker-is-system vs third-person" design, now promoted from confirmation step to the primary path.
- 🐛 **Bug fix: padding-side readout in shared `resid_post`** (`src/mvm/activations.py`). The tokenizer **left-pads** by default, but the extractor used `mask.sum(1)-1`, which only finds the last token under *right* padding; on mixed-length batches it read a length-correlated interior token. Fixed to `(mask*arange).argmax` (last index with mask==1; padding-side-agnostic), and the same fix applied in `localize_context.py`. **Effect:** every earlier probe/SAE number this session was computed with the buggy readout and is not trustworthy in detail. The qualitative arc above still stands (declarative contrasts leak; see next bullet for the corrected mechanism), but exact accuracies/peaks should be re-derived with the fixed code if ever needed.
- ✅ **Context-disambiguated localization — instrument validated** (`gen_context_stimuli.py` → `context_self_speaker_stimuli.jsonl`; `localize_context.py` → `artifacts/stage1/context_localize.json`). The target first-person sentence is **identical** across self/other and sits at the end (so the readout token is the same); the referent is set only by context — **turn_role** (the model's own assistant turn vs the user's turn; no referent word anywhere) and **attribution** (identical quoted sentence credited to "the assistant" vs "the customer"). Probe = PCA(≤15)+logistic; every accuracy is reported as a **margin over a label-permutation null** (kills the d≫n overfit floor), with the **true token embedding** (`hs[0]`) as the lexical floor.
  - **Result:** embedding margin **+0.00** for both mechanisms — confirmed *no lexical cue at the readout* (the older "leak" was the padding bug + mislabeling `resid_post[0]` as the embedding). A **computed signal** then rises through the stack: turn_role peaks ~L24 (real 1.00 / null 0.44, margin +0.56) and is already 0.85 at `resid_post[0]`; attribution peaks ~L15 (margin +0.57). So the model carries a context-driven self/other distinction that is *not* reducible to the referent word.
  - **Corrected read of the "lexical" finding:** declarative role sentences contain the referent word, so even one attention layer can copy it to the readout — that is why they decode so easily (shallow), not a deep self-model. Removing the word (this design) and still finding a signal is the meaningful advance.
  - **Honest caveats:** (1) decodable ≠ causal ≠ a "self-model" — turn_role may be reading *turn-type* (am I in a model turn?) rather than a self representation; only causal patching + the removal test adjudicate depth. (2) attribution's signal could be attention-copying the speaker noun (shallow); turn_role, with no noun to copy, is the stronger case. (3) n=48/mechanism is still small. (4) the embedding floor is clean *by construction* (every target ends in "."), so the gate proves "no lexical cue at readout," not "no confound anywhere."
- ✅ **Causal activation-patching — C_self is causal, not just decodable** (`patch_context.py` → `artifacts/stage1/patch_context.json`). On the 24 turn_role pairs, fit C_self at each layer, then inject the self-run's C_self component into the **other** (user-turn) run at the readout and measure **logit-difference restoration** toward the self-run, against a **norm-matched random-direction control**. Restoration along C_self rises monotonically — L8 0.08, L14 0.25, **peak L22 0.35** — while the random direction stays at ~0.00 (−0.02…+0.01) at every layer. So directionally steering C_self causally moves the model's referent-dependent next-token behaviour ~35% of the way to the self-run; a random direction of equal magnitude does nothing.
  - **Honest caveats:** restoration is partial (~0.35, not 1.0) — expected for a single-coordinate directional patch; the rest of the self/other gap is other turn-context. The effect grows toward the output layers, which the random control shows is C_self-specific (not "any late patch moves logits"), but late-peaking means this is "causal for output," not yet "carries task integration" — that is the removal test's job (re-score T and S). Single metric (next-token logits), turn_role only, n=24 pairs.
  - **Maps onto RT-04 as C_self-index.** turn_role sets the referent purely by *which turn is speaking* — the thin indexical "who is the current speaker," with no persona/identity content. So this validated, causally-confirmed direction is the **C_self-index** structure the amended design wants — and per RT-04 an H_center result on the *index* is more floor-consistent than on the narrative persona. The retired role-declarative route ("I am the assistant/AI") was attempting **C_self-narrative** (persona content), and was confounded/shallow. RT-04 now requires C_self-narrative localized cleanly (confound-controlled) and tested **independently** of C_self-index.
- ✅ **C_self-narrative localized + separability tested (RT-04)** (`gen_context_stimuli.py` now emits a `narrative` mechanism; `separate_self.py` → `artifacts/stage1/separate_self.json`). C_self-narrative is localized by a confound-controlled persona contrast: identical target sentence as the **model's own reply under its own AI identity vs while adopting a roleplay character** — *both are model turns*, so C_self-index (turn role) is held constant and only the persona varies. It passes the same embedding-floor gate (+0.00, no lexical cue) with a computed signal peaking ~L23.
  - **Separability verdict: PARTIALLY SEPARABLE / OVERLAPPING** (layers 10–22). The two are **not the same structure** — optimal directions are well off-axis (median |cos| **0.28**, ~74°) and each keeps full decoding after the *other* direction is projected out. But they **share a component**: a single C_self-index direction still separates the narrative contrast (cross-decode AUC 1.0). So C_self-index and C_self-narrative are **distinguishable yet overlapping**.
  - **RT-04 reading:** distinguishable enough to localize and run the removal test on each independently — but the Metzinger seam is **not fully closed** (the shared component is real). Report the overlap honestly; do not treat a narrative result as settling the floor. **Decisive next test:** causal *cross-patching* (does ablating C_self-index move narrative-dependent behaviour, and vice versa?) — geometry alone can't settle whether the shared component is functional.
  - **Honest caveats:** n≈24/structure; the roleplay "other" differs in instruction length from the neutral "self," so part of the shared component could be a context-length/complexity nuisance — length-match personas before treating the overlap as intrinsic. Single-direction cross-decode is lenient at this n/dim; orthogonalized-decode (removing one direction from 2304-dim) is lenient the other way — hence the deliberately three-way verdict rather than a binary.

**Next actions, in order (amended for RT-01..08; substrate decided):**

0. ✅ **Registered-run model + hardware — CONFIRMED (2026-06-23).** Substrate = **Llama-3.1-8B**, run as the Tülu-3 ladder (`meta-llama/Llama-3.1-8B` base → `allenai/Llama-3.1-Tulu-3-8B-SFT` [primary] → `-DPO` → `allenai/Llama-3.1-Tulu-3-8B` RLVR [+ `meta-llama/Llama-3.1-8B-Instruct`]) so RT-06 capability-gating is a controlled comparison at rising alignment. Method (b) SAEs: `fnlp/Llama-Scope` (base-trained; also EleutherAI / Goodfire-instruct options) — **loader (SAELens vs OpenMOSS/EleutherAI sae lib) still to verify**. Hardware = **48GB M4 Pro mini**. Recorded in `config.py` (`REGISTERED_MODELS`; active `MODEL_ID` stays the 2b-it sandbox) and `registered-run-model-comparison.md`. **Remaining:** when the mini is in hand, verify + pin exact HF revisions, confirm the SAE loader, and re-baseline T/S there. Steps 1–2 below proceed on the 2b-it sandbox now.
1. **Causal cross-patching to firm up RT-04 separability (blocking, sandbox OK).** Decodable separability is **partial/overlapping** (distinct directions, median |cos| 0.28, but a shared component). Geometry can't settle whether the overlap is *functional*, so extend `patch_context.py`: patch C_self-index and measure the effect on the **narrative** behavioural contrast, and vice versa. Low cross-effect ⇒ functionally separable; high ⇒ shared functional structure. Also **length-match the roleplay "other" to the neutral "self"** (RT-04/RT-06 nuisance control). **Loss condition (RT-04):** if no method separates them, record non-separability and that the Metzinger objection stands open.
2. **Method-(b)/convergence decision per structure.** The single-feature SAE test was retired as too brittle; either run the subspace SAE test on the context design or treat causal patching as the independent second method. Declare each C_self localized only when ≥2 methods agree on a confound-controlled (clean embedding-floor) design; else the pre-reg "inconclusive/not-testable" branch.
3. **Battery work for the amended rule (gates threshold lock, on the registered model):**
   - **RT-02 — T-split:** build `T_self_relevant` (multi-turn binding of the model's *own* prior outputs / conversational role) alongside the existing scrubbed `T_self_irrelevant`; keep both disjoint from S. (Conceptually aligned with the turn_role design.)
   - **RT-05 — `T_syntax` router control:** a turn/boundary-tracking task with zero reasoning; if C_self-index ablation drops it as much as `T_self_relevant`, C_self-index is a dialogue-state router, not a center.
   - **RT-03 — S rubric v2:** add forced-third-person self-monitoring / self-vs-other items scored on tracking regardless of grammatical person; **re-baseline S** under v2 (current `S_base = 0.615` is v1) before `θ_self`.
4. **Matched controls C_ctrl — RT-01 + RT-06 (pilot, before δ).** Other-entity structures at comparable probe accuracy *and* causal centrality on a **neutral third corpus** (RT-01: measure C_self vs C_ctrl activation-frequency asymmetry, regress `d_task` on frequency, pre-register a max asymmetry). **RT-06:** at least one C_ctrl must be a **capability-gating** persona (expert/system) **verified third-person** via the separability check (low cross-decode with C_self) before use. **Loss conditions:** if the C_self−C_ctrl gap doesn't survive the frequency control, *or* no capability-gating C_ctrl can be kept third-person, the differential is dead → don't lock δ; report "not testable here yet."
5. **Pilot ablations** (mean primary; zero; directional) of C_self-index, C_self-narrative, and C_ctrl → `d_task` on **both** T subsets + `T_syntax`, `d_self` under rubric v2, **with the RT-07 neutral-corpus OOD perplexity gate** (OOD-inconclusive if breached) → set & commit `θ_task`, `θ_self`, `δ` in `thresholds.md` BEFORE the test set.
6. **Run the removal test for each C_self structure independently**, apply the amended decision rule (incl. the new "floor-consistent, restricted" outcome), report.

**Baselines on the unmodified model (`google/gemma-2-2b-it` @ `main`):**

- **T (integrated-task) = 0.750** (15/20). Per category: multi_step 1.00, needle_synthesis 1.00, coreference 0.80, instruction_following 0.20. Machine-scored; the 5 misses were verified as genuine model failures. `instruction_following` is near the floor — treat it as supporting, not a primary drop signal (a floor effect; noted in `thresholds.md`).
- **S (self-report) = 0.615**. Per category: first_person_activity 0.719, self_monitoring 0.594, self_vs_other 0.531. Scored by the held-out judge `claude-opus-4-8` (≠ the model under test) against the locked rubric, with a human spot-check that confirmed the judge applies the rubric rather than rubber-stamping.

Artifacts (gitignored) are in `artifacts/stage0_baseline/`: `task_results.json`, `self_report_responses.json`, `self_report_scores.json`.

*(The original "first actions to begin Stage 1" — install interp deps, smoke test, first localization, build C_ctrl — are all done or superseded by the Next-actions list above. Kept only the file map below.)*

Key Stage 0/1 files to build on: `src/mvm/model.py` (`generate_text` helper, reused for ablation re-scoring), `src/mvm/activations.py` (`resid_post`, padding-fixed), `experiments/01-.../src/battery.py` (loaders + T scorer), `run_baseline.py`, `judge.py`, `thresholds.md`, `batteries/`; and the Stage-1 instruments: `gen_context_stimuli.py`, `localize_context.py`, `patch_context.py`, `separate_self.py`.

## Environment (set up on the M4 MacBook Air)

- **Python**: 3.12.13 via `uv` (system default is 3.14, left untouched). uv installed at `~/.local/bin`.
- **venv**: `.venv/` in repo root. Activate with `source .venv/bin/activate`. NB: `pip` is not on PATH — use `python -m pip` or `~/.local/bin/uv pip`.
- **Core deps installed**: `src/requirements.txt` (torch 2.12.1, transformers 5.12.1, plus `anthropic` for the judge). MPS backend confirmed working.
- **Interp deps installed**: `src/requirements-interp.txt` (transformer-lens 3.3.0, sae-lens 6.44.4, scikit-learn, pandas, datasets). Resolved without changing torch/transformers. NB: TransformerLens is available but not load-bearing — activations come from HF `output_hidden_states` (see `src/mvm/activations.py`).
- **HuggingFace auth**: token (`mvm-gemma`, read scope) at `.hf-cache/token` via `hf auth login` with `HF_HOME="$PWD/.hf-cache"`. `config.py` repoints `HF_HOME` into the repo, so the token must live there — it does. No re-login needed as long as runs happen from the repo root.
- **Anthropic API key (for the judge)**: in a gitignored `.env` at repo root as `ANTHROPIC_API_KEY=...`. Load it before running `judge.py`: `set -a; source .env; set +a`. Verified to authenticate. Bills developer-platform credits (separate from the Claude Max subscription); the judge is the only thing in the repo that calls the API, and a few cents per 12-item run.

## Gotchas to remember

- **Homebrew is partly broken** on this machine: a permission issue on `/opt/homebrew/opt/nginx` blocks `brew link`, so `gh` and brew Python never landed on PATH. Routed around it (uv for Python; `git push` works directly without `gh`). Don't rely on brew until that's fixed.
- **16 GB RAM**: the bf16 2B model + Python + macOS leans on swap. Keep ~20 GB SSD free; close heavy apps during runs. Interp tooling (caching all activations) will push memory harder than plain generation — watch it in Stage 1.
- **Token hygiene**: never pass API tokens as command args (an earlier HF token got pasted on the command line and was revoked). Keys live in gitignored files (`.hf-cache/token`, `.env`), loaded via env.

## Repo / backup state

- Local `main` in sync with `origin/main` (private repo `jfredson/minimum-viable-mind`); latest Stage-1 commit `118e568` (model comparison + hardware). Pushed through this session.
- Backup loop: Claude commits locally and pushes to `origin` when asked. If a push fails on auth, treat that as a setup bug to fix, not a reason to fall back to manual pushes.
- The working tree also carries John's authored "Measurable Floor" scope framing (committed `f05191e`): the project targets the *measurable* structural correlate, silent (not dismissive) about sub-measurable fundamental experience. Read "floor" as the measurable one throughout.

## The arc (so the next session sees the whole shape)

1. ✅ Proposal (`spec/`) and staged experiment plan (`experiments/`) written.
2. ✅ Stage 0 bench scaffolded (`src/`), environment stood up on the Air, smoke test green.
3. ✅ Stage 0 baselines — T and S batteries built and scored on the unmodified model (T=0.750, S=0.615); rubric locked; `thresholds.md` committed with baselines filled, `θ/δ` still TBD.
4. ⏳ **Stage 1 — the self-indexing removal test.** Interp deps installed; localization went through several rounds of confound-hunting (topic-vocab → role-word → a padding-side readout bug, now fixed) that retired the declarative "I am {role}" route. The trustworthy instrument is now `localize_context.py`: identical surface text whose "I" is fixed by **context** (turn role / attribution), scored as a margin over a label-permutation null with the true token embedding as the lexical floor. It validates cleanly — no lexical cue at the readout, with a real *computed* self/other signal, now **causally confirmed** by directional patching against a random-direction control. Design then amended by the red-team review (RT-01..04): this signal is **C_self-index**; next is C_self-narrative + separability (RT-04), the T-split / S-rubric-v2 battery work (RT-02/RT-03), and the C_ctrl frequency-control pilot (RT-01) → lock thresholds → removal test for each structure. (You are here.)
5. ⏳ **Registered run** on the confirmed substrate (Llama-3.1-8B + Tülu-3 ladder + Llama Scope; see `registered-run-model-comparison.md`), on the RunPod cloud bench (the 48GB-mini plan is superseded). Migration complete 2026-07-13: baselines + all gates re-verified on Tulu-3-8B-SFT. Remaining: the pre-lock queue in the top entry → θ/δ lock → removal test. Then later stages per `experiments/README.md`.
