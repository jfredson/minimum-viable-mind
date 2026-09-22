# Amendment A3 closure text, version 2 (DRAFT for Gate A)

*2026-09-21 (Pacific). Version 1 (`a3-closure-text-draft-2026-09-20.md`,
unedited) predates two things that are now on the record and is
superseded by this file: the two follow-up localization reads and their
Gate B rulings of 2026-09-21 (ledger RT-120 to RT-142), and the
December-result ruling of 2026-09-20, under which the successor registers
in 2026 rather than after hibernation. This is registered text once it
lands in `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`
as a dated closure block, so it goes through Gate A (both tiers, closure
rule) first. Preconditions per the step 4 ruling, all met as of
2026-09-21: the pilot's training log and trajectory committed (PR 10); the
two $0 checks RT-58 and RT-59 closed clean (PR 10); the blind-arm status
reconciled (Astra A10, no re-run; STATUS.md 2026-09-21).*

---

## Closure of Amendment A3, [date of Gate A pass]

**Outcome: not testable.** The pre-registered loss condition fired: no
non-self cross-turn control can be built that is state-requiring at
ceiling. The control battery's ownership-blind ceiling is 1.0
(`ceiling-measurement-findings.md`, 2026-09-17), so the registered
differential clause had no computable value for any model from the day it
was registered. An unregistered pilot giving the control its own loss term
did not make it usable (0.3125 against a pre-stated bar of 0.60;
`control-learnability-pilot-findings.md`). The clause is not repaired; a
successor grammar is a new registration.

**What A3 measured.** On three seeds trained from scratch, the primary
battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the
ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the
syntax battery was unchanged and the state battery moved on one seed
(0.0769 on seed 2, below its 0.1172 threshold). The ownership input is
load-bearing for the primary battery. The matched contrast against a
non-self control could not be run.

**What A3 did not measure.** Whether the network built an internal center
around the ownership input is not testable with these instruments. The
input-channel lesion removes a sense organ, not a structure the network
built (§3.1). A fitted linear classifier at eleven positions and five
layers found the register index nowhere except where its marker is the
input, and a standardised refit of the same read agreed; the registered
matched control (§L2(a), the other agent's index) ran once and excluded the
one proposed confound; one cell of the refit crossed the family bar by two
episodes in four thousand and is recorded as a sub-bar pattern, not a
clearance (ledger RT-120 to RT-142, ruled 2026-09-21). The registered probe
target, the marker word, has been read only by the weaker
difference-of-averages method at those positions; causal patching, which
§3.2 requires alongside the probe, was never run and has no code for this
design. The registered term is *not testable
(localization)*. This is a status, not a finding of absence: these probes
did not localize this target at these positions, and strong, readily
recoverable versions of it are less plausible than before; other
implementations and instrument limits remain open.

**Where this sits on the project's gradient.** Under the ruling of
2026-09-20, a causally load-bearing ownership pointer is a center at the
bottom of the gradient. These checkpoints have one. Their degree on the
integration axis, how much of the act is organized around that pointer
rather than consulting it, is unmeasured, because the metric for that
axis (Stage 2) does not yet exist. The sentence this experiment supports
in public is: the ownership input is load-bearing on three seeds; whether
an internal center formed around it is not testable here; its degree is
unmeasured. No result of A3 is described as "a structural signature of
self-indexing" or "a structural signature of ownership-specific learning".

**Successor.** A matched-role causal-interchange experiment with a
learn-both eligibility gate, whose purpose is to develop and validate the
Stage 2 degree metric on contrast cases known by construction
(`docs/competing-mechanisms-2026-09-20.md`). It registers in 2026, through
Gate A with both tiers, registration commit target 2026-10-11
(`docs/rulings/2026-09-20-december-result-roadmap.md`, which amends item 5
of the center-as-degree ruling).

**Money.** Amendment A3 closed at about $44 of its $100 hard stop; the
program at about $226 of its $400 ceiling (`compute-ledger.md`).
