# Amendment A3 closure text (DRAFT for Gate A)

*Drafted 2026-09-20 (Pacific). This is registered text once it lands in
`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` as a dated
closure block, so it goes through Gate A (both tiers, closure rule) first.
It carries the step 4 ruling of 2026-09-20 (A3 closes as *not testable*)
and the later ruling of the same day (`docs/rulings/2026-09-20-center-as-degree.md`).
Preconditions before it can land, per the step 4 ruling: the pilot's
training log and trajectory committed; the two $0 checks RT-58 and RT-59
run; the blind-arm status reconciled (Astra A10).*

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
input; the registered probe target, the marker word, has been read only by
the weaker difference-of-averages method at those positions; causal
patching, which §3.2 requires alongside the probe, was never run and has no
code for this design. The registered term is *not testable
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
(`docs/competing-mechanisms-2026-09-20.md`). It registers after the
hibernation condition, through Gate A with both tiers.

**Money.** Amendment A3 closed at about $44 of its $100 hard stop; the
program at about $226 of its $400 ceiling (`compute-ledger.md`).
