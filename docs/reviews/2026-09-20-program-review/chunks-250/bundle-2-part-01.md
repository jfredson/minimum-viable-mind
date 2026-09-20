
Note the corrected bar recorded on 2026-09-17: the floor rule is not
"baseline below ceiling" but "baseline minus ceiling below 0.10", so the
control needs **0.4227**, not 0.3227, for its drop to be defined. The
three checkpoints miss by 0.135, 0.117 and 0.103 — four to forty times
wider than the raw ceiling gap suggests.

### 3. THE REGISTERED COMPARISON WAS NEVER COMPUTABLE BY ANY MODEL

The 2026-09-17 ceiling measurement (`ceiling-measurement-findings.md`,
method committed before running, no checkpoint loaded, $0) found that
**the control battery's ownership-blind ceiling is 1.0000, not the
registered 0.3227.** Two independent solvers reach a perfect score
without touching the model's own slot or the acting channel: a
hand-written one that reads the marker in the question and applies the
shared revision rule, and a learned one given only ownership-blind
features that found the same structure by itself. The harness proved
itself first, reproducing both registered reference values exactly to
four decimal places.

**Verdict A — structurally unsatisfiable.** With a ceiling of 1.0, a
defined drop needs a baseline of 1.10, and accuracy cannot exceed 1.0.
So the control's drop is undefined for *every possible model*, including
a hypothetical perfect one. The registered signature needs the primary
battery's drop minus the control's; one of its two terms can never
exist. **The clause has been dead since registration** — not since this
result, not since these seeds. This also moots candidates C and D of
`control-battery-proposal.md`, which tried to make the control learn:
making it learn was never the binding problem.

### 4. The localization instruments have no validated positive control

- **Registered blind-localization arm: NOT FLAGGED**, sub-bin
  *instrument failure to locate* (`blind-arm-findings.md`). No probe
  cleared its permutation null by the required three standard
  deviations; the best reached 1.3. Per John's 2026-09-16 ruling the
  committed verdict and its name **stand as written**, with a dated
  annotation beside them recording that the *interpretation* is
  superseded: the unblinded probe showed the register never encoded
  own-agent identity at any turn, so there was nothing at that location
  to find. Annotate, never rewrite.
- **Unregistered positive control: NOT TESTABLE** by the letter of the
  cells committed before the run (`blind-control-findings.md`). Every
  probe sat *below* its own null at all five depths. The ablation
  cleared the threshold in magnitude (−0.3516 against 0.1777) but with
  the **wrong sign** — it made the primary battery *better*, which a
  sensitivity test should never count as a bite.

**Consequence: no localization work runs until the stack has a validated
positive control.** The 2026-09-16 not-testable verdict is not reopened.

### 5. RULED 2026-09-19 — a bite is a degradation, and the rule binds future runs only

John ratified the proposal in conversation ("Yes to your view"). Four
parts, committed into the criteria file
(`src/blind_control_a3.py`, successor to the criteria first committed at
`a3c5fbf`) with the ruling quoted, before anything executes:

1. **Sign.** The ablation bites only when the **signed** corrected drop
   on the primary battery reaches the threshold. An improvement never
   counts.
2. **Noise.** Evaluate at **800 episodes or more**, with intact and
   ablated readings paired on the same evaluation seed. The threshold is
   about 0.038 raw battery points here; evaluation noise is sd 0.0284 at
   400 episodes (1.3 sd) and 0.0169 at 800 (2.2 sd).
3. **A fourth cell**, to be added before the next run: probe passes and
   the ablation *improves* the primary battery beyond noise =
   **located, wrong structure**. Neither pass, nor insensitive, nor not
   testable.
4. **Process.** Committed to the criteria file first, ruling quoted. **No
   registered text changes; the control stays unregistered.**

**The executable cells in that module still implement the 2026-09-16
letter** (they take an absolute value, and the episode count defaults to
400). The amendment is documentation until the code is changed, which
must happen before the next run.

Open and not ruled: whether to replace the single-threshold bite with a
partial-ablation dose ladder requiring steady worsening. That belongs to
the reframed 2026-10-04 proposal.

### 6. Where the money is

**A3 $34.31 of its $100 hard stop; the whole program about $216 of
$400.** Everything since 2026-09-17 has been local and $0. Ops cleanup
done 2026-09-19: John deleted the idle EUR-IS-1 storage volume after
both seed checkpoints matched their recorded checksums, and reverted the
sleep setting on the Mac. Details in `compute-ledger.md`.

### 7. The dated path, and what is next

Steps 1 to 3 of the public path roadmap
(`docs/public-path-roadmap-2026-09-16.md`, approved verbatim "Approved
on all") are **discharged**. Step 4 has been reframed: it is no longer
"make the control learn" but **repair the clause, change the metric, or
close A3 with partial discriminators and say so** — John decides
2026-10-04, on a proposal.

- **2026-09-20** — draft the reframed 2026-10-04 proposal (the
  reframed-proposal task, `208e4829`). $0.
- **2026-09-30** — book text lock. No MVM result lands before it.
- **2026-10-04** — John's decision on the control-battery question.
- **2026-10-11** — refresh `explainer.md`, after the book lock.

Also on file, advisory and $0:
`docs/research-note-pain-axis-2026-09-19.md`, six methodology lessons
from the nearest published neighbour. Two of them (a matched self/other
contrast scored by separation, and the dose ladder) fold into the
2026-10-04 proposal; one (projecting out the top control-variance
directions before probing) is a free known-answer test that could run
before 2026-10-04 on John's go, since it reads no verdict.

## The arc (so the next session sees the whole shape)

1. ✅ Proposal (`spec/`) and staged experiment plan (`experiments/`) written.
2. ✅ Stage 0 bench scaffolded (`src/`), environment stood up on the Air, smoke test green.
3. ✅ Stage 0 baselines — T and S batteries built and scored on the unmodified model (T=0.750, S=0.615); rubric locked; `thresholds.md` committed with baselines filled, `θ/δ` still TBD.
4. ⏳ **Stage 1 — the self-indexing removal test.** Interp deps installed; localization went through several rounds of confound-hunting (topic-vocab → role-word → a padding-side readout bug, now fixed) that retired the declarative "I am {role}" route. The trustworthy instrument is now `localize_context.py`: identical surface text whose "I" is fixed by **context** (turn role / attribution), scored as a margin over a label-permutation null with the true token embedding as the lexical floor. It validates cleanly — no lexical cue at the readout, with a real *computed* self/other signal, now **causally confirmed** by directional patching against a random-direction control. Design then amended by the red-team review (RT-01..04): this signal is **C_self-index**; next is C_self-narrative + separability (RT-04), the T-split / S-rubric-v2 battery work (RT-02/RT-03), and the C_ctrl frequency-control pilot (RT-01) → lock thresholds → removal test for each structure. (You are here.)
5. ⏳ **Registered run** on the confirmed substrate (Llama-3.1-8B + Tülu-3 ladder + Llama Scope; see `registered-run-model-comparison.md`), on the RunPod cloud bench (the 48GB-mini plan is superseded). Migration complete 2026-07-13: baselines + all gates re-verified on Tulu-3-8B-SFT. Remaining: the pre-lock queue in the top entry → θ/δ lock → removal test. Then later stages per `experiments/README.md`.



===== FILE: experiments/01-self-indexing-removal-test/removal-test-findings.md =====

# THE REGISTERED REMOVAL TEST — findings (run 2026-07-18)

*Experiment 1's registered result. Run per the θ/δ lock (`8b1fcbe`), runner
registered `a4efcf0`, held-out test set finalized `a11e769` (92/92
baseline-verified, untouched by any pilot). Substrate
`allenai/Llama-3.1-Tulu-3-8B-SFT`, cloud bench, one pass per condition.
S judged locally (rubric v2, held-out judge `claude-opus-4-8`). **Human
spot-check of the test-set judge scores: PASSED AS-IS — John, 2026-07-18**
(17 panels: primary-condition drops incl. both self_monitoring items,
directional increases, control and excluded-arm consistency reads).
Raw artifacts: `artifacts/removal_test/` (gitignored).*

## Results

All test batteries baseline at 1.000, so relative drop = flipped fraction.

| condition | d(T_si) | d(T_sr) | d(T_syntax) | d_self | Δnll (gate) | Δrep-4 (gate) |
|---|---|---|---|---|---|---|
| idxres mean k=16 (**primary**) | **0.219** | **0.100** | 0.133 | +0.059 | +0.0867 ✅ (bound 0.0893) | −0.085 ✅ |
| idxres directional k=16 | 0.125 | 0.067 | 0.133 | −0.039 | +0.0856 ✅ | +0.020 ✅ |
| narrative mean k=16 | 0.063 | 0.033 | 0.067 | +0.039 | **+0.3468 ❌ OOD** | +0.114 ✅ |
| expert mean k=16 (control) | 0.063 | 0.000 | 0.100 | +0.020 | +0.1244 ❌ | +0.039 ✅ |

Baseline S on the held-out set: 0.6375 (coincidentally identical to the
pilot baseline — the battery construction transferred cleanly).

## The locked decision rule, applied verbatim

**Primary condition (OOD-clean; margin +0.0026 nats under the bound —
carried honestly, same marginality as the calibration):**

- `d_task ≥ θ_task (0.10)`: **fires** — T_si 0.219, T_sr 0.100 (exactly at
  threshold), T_syntax 0.133.
- `d_task(C_self) − d_task(C_ctrl) ≥ δ (0.10)`: **fires on T_si** (+0.156);
  T_sr +0.100 (exactly at δ); T_syntax +0.033 (does not). *Caveat fixed at
  lock: the k=16 control arm is NLL-OOD-excluded (+0.124, reproducing the
  calibration value exactly), so the differential's comparison arm is
  off-manifold — flagged, not fatal, per the lock text.*
- **RT-05 router control: the loss condition FIRES.**
  d_task^syntax (0.133) ≥ d_task^sr (0.100), and likewise in the
  directional cross-check (0.133 vs 0.067). Per the registration:
  *"C_self-index is a dialogue-state router and an H_center result on it is
  void — report the router reading, do not report a center."*
- `d_self ≥ θ_self (0.25)`: **does not fire** — +0.059, within the
  0.05–0.07 control wobble. The directional condition moves S slightly
  *up*. **The self-report was not subtracted by any readable condition.**
- **H_description** (d_self ≥ θ_self ∧ d_task < θ_task): does not fire —
  the observed pattern is its mirror image (task damaged, report intact).
- **RT-02 floor-consistent-restricted**: does not apply — both T subsets
  dropped, and the *self-irrelevant* battery dropped hardest (0.219 vs
  0.100), the reverse of the restricted signature.
- **C_self-narrative: NOT TESTABLE at this strength** — mean-ablating the
  rank-16 narrative subspace is catastrophically off-manifold (+0.347,
  4× the index residual). The RT-04/Metzinger arm returns
  OOD-inconclusive; no claim attaches to the narrative structure.

## The registered verdict

**No center was removed.** The formal H_center signature (task drop +
differential) appears and is voided by the experiment's own pre-registered
router control. **No description was subtracted either** — judged
referential self-tracking survived every readable intervention, as it has
survived every intervention this program has ever run at any granularity.

The registered reading: **on this substrate, the locatable C_self-index
residual is dialogue-state routing infrastructure, not the floor's
self-binding.** Removing it degrades integration *generically* — most of
all on self-irrelevant tasks, which is the router account's own prediction
(turn structure is woven into everything) — while the system's ability to
track itself in its reports is untouched. The self-binding the floor claim
targets is either implemented elsewhere (diffusely, or in structure our
localization does not carve) or is not present as a removable object at
all. The narrative self-structure remains untested at effective strengths:
every instrument strong enough to move it is off-manifold.

Per the pre-registration's outcome licenses: this result **does not
license** "no self-model exists here," and it bounds nothing about
sub-measurable experience (the Measurable Floor framing stands). What it
licenses is the program-routing fact: **self-indexed integration, if this
project is to measure it, must first be *constructed* — it is not findable
as a removable center in this model class with these instruments.**

## What this feeds (the fork)

- **Stage 6 pre-work** (self-indexing as a thing to build) is the
  H_description-flavored branch this result most supports.
- **Instrument/substrate work** (instruct-trained dictionaries; better
  separation methods for the narrative arm) is the not-testable branch it
  keeps open — the narrative structure's untestability is now a concrete,
  bounded methods problem.
- Stage 3 proceeds regardless, per the 2026-07-17 sequencing adjudication.
- The Tülu-ladder deliverable gains its ending: alignment edits the policy,
  not the geometry — and the geometry, when removed, was routing.

## Instrument notes (for the methods paper)

1. Expert-arm Δnll +0.1244 reproduced the calibration's value to four
   decimals across separate runs — the bench is highly stable.
2. The long-generation gate passed everything it should have and the
   index ablations again generated *less* repetitively than baseline.
3. The held-out battery construction (shape-cloning + pre-committed cull)
   converged in three passes (8 fails → 2 → 0), with every failure in a
   documented flakiness class — the discipline transfers.
4. Judge behaviour on the fresh set matched the pilot set (baseline S
   identical at 0.6375); rubric v2's dimension decomposition again did the
   interpretive work in the spot-check.

## Addendum (2026-08-04): registered uncertainty re-analysis

Per the pre-registration amendment of 2026-08-04 (registered `10afc15`
before computation): 95% percentile bootstrap CIs (B=10,000, item-level
within battery, draws shared across conditions) on every registered
quantity. Point estimates reproduce this memo exactly; registered
verdicts unchanged. Full tables: `removal_ci.json` (committed beside
this memo); Fig. 4 artwork in `figures/`.

What the intervals add: (1) the H_center differential that RT-05 voided
was +0.156 [0.000, +0.312] — its lower bound touches zero at n=32, so
the headline signature was imprecise even before it was voided; (2) the
RT-05 router gap d(T_syntax) − d(T_sr) is +0.033 [−0.133, +0.200]
(primary) — "dropped as much as self-relevant" is statistically
indistinguishable, as read; (3) d_self = +0.059 [−0.062, +0.185]: the
upper bound sits below θ_self = 0.25, so the never-subtracted-report
claim now carries a quantified ceiling; (4) per-item view: six of the
seven flipped T_si items are multi_step_reasoning (6/8 in-category vs
1/24 elsewhere) — category-concentrated damage, the profile of generic
