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
