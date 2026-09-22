# Rehearsal method, addendum: the denominator and the empty control cell

*2026-09-21 (Pacific). **UNREGISTERED.** An addendum to
`docs/successor-measure-rehearsal-method-2026-09-21.md`, written and committed
**before** the code it describes, for the same reason the first method file
was. The first file is left exactly as written; this one adds four checks to
it and changes none of the ten it already carries.*

*Written under the workspace plain-language rule.*

---

## 1. Why this addendum exists

A review attached to the successor proposal before John rules on it — the
protocol's proposal gate — returned two findings marked fatal, and both of
them are in the part of the design this rehearsal is in the middle of
building. The instruction that came with them is the right one and is followed
here: **do not implement the formula as written, and do not quietly substitute
another one either. Make the choice something the rehearsal answers.**

That is what a rehearsal is for. A rehearsal that discovers the registered
measure cannot mean what its own sentence says is doing exactly its job, and
finding it now costs nothing, where finding it after registration costs the
whole line.

### Finding one — the reading divides by an uncorrected accuracy

Section 6.3 of the proposal registers

    degree = (accuracy_whole - accuracy_ownership_only) / accuracy_whole

and separately says `accuracy_untouched` — the share of trials that land on
the donor's value with **no transplant at all** — should sit near the
one-in-eight guessing rate. It never subtracts that floor from either term.
A floor under both terms does not cancel in a ratio.

The review's arithmetic, which this rehearsal reproduces rather than trusts:
a system reading 0.9 whole-state and 0.5125 ownership-only returns 0.431; a
system reading 0.35 and 0.2375 returns 0.321. By the document's own account
both have exactly half of the identity-driven difference living outside the
nominated subspace, so both should read the same number. Subtracting the floor
from both terms returns 0.500 for both.

Why that is worse than an arithmetic slip: the separation bar between the two
constructed arms is fixed at toy scale and then applied to registered models
whose transplant accuracies will not match the toy's. The proposal's own
weakness list already predicts that the entangled arm has the weakest
whole-state transplant — which squeezes the top of the scale on exactly the
arm that is supposed to be the known-high anchor, and leans the whole design
toward "the measure does not separate" for a reason that is about arithmetic
rather than about the systems. It is the closed Amendment A3 denominator
failure in a new shape: not a zero this time, but a denominator whose
behaviour was never measured on the condition it will be applied to.

### Finding two — a control's first cell is empty by construction

Control 6 of section 7.3, the one that tells "the transplant moved who is
acting" apart from "the transplant carried the answer with it", splits trials
into a cell where the donor's identity dictates **the same** value as the
recipient's and a cell where it dictates a **different** one. But the
generator draws four **distinct** values per contested item and asserts it,
and the successor rule is a one-to-one map, so two agents can never dictate
the same answer. The first cell has no trials in it at all. The proposal
requires that distinctness in three other places, so it contradicts itself
independently of any code.

The same distinctness inverts the sanity rule attached to
`accuracy_untouched`: with distinct values a model that is right about its own
answer essentially never lands on the donor's, so the untouched rate is about
`(1 - accuracy) / 7`, not one in eight. That rule passes for a model at chance
and fails for a model that works — a registered rule that would call a working
instrument broken.

---

## 2. The four checks this addendum adds, with their cells fixed first

Nothing below chooses a form for the registration text. Each check produces a
measurement and hands it over; which form is registered is John's to rule on,
on the evidence these checks produce.

### D-1. The two forms, on made-up trial populations with a known true share

Command: `denominator.py --stage simulated`

A trial population is generated from three numbers that are **known because
they were used to build it**:

- `b` — the base rate at which a trial lands on the donor's value for reasons
  that have nothing to do with the transplant;
- `p` — how effective the whole-state transplant is at these sites;
- `s` — **the true share of the identity-driven difference living outside the
  nominated subspace**, which is the quantity the measure claims to report.

Trials are drawn, not computed from a closed form, so the check measures the
estimator including its spread. Two cases are built with **the same `s` and
different `p`**, which is the shape the review asked for.

- **Pass** — the floor-corrected form,
  `(whole - ownership_only) / (whole - untouched)`, returns the true `s` in
  both cases within the spread across repeated draws, **and** the registered
  form returns materially different numbers in the two cases. That confirms
  the finding.
- **Fail** — the registered form is also invariant across the two cases. Then
  the finding is wrong and the record says so.
- **No verdict** — the two forms cannot be separated because the spread across
  draws swamps the gap. Then the check is run with more trials until it can,
  and how many trials that took is itself reported, because the registered
  experiment has to afford them.

### D-2. The same question on real forward passes

Command: `denominator.py --stage attenuated`

The simulated check has the weakness that it is a simulation. So the same
question is asked of the trained arms, by **attenuating the transplant**: at
identical sites, with the identical subspace, the state is moved a fraction
`a` of the way toward the donor's rather than all the way, for
`a` in 1.00, 0.75, 0.50, 0.25. The architecture, the sites and the subspace do
not change, so **the true share outside the subspace does not change**; only
how effective the transplant is does.

- **Pass** — across `a`, the floor-corrected form is flatter than the
  registered form, and the record carries both curves.
- **Fail** — the registered form is the flatter one.
- **No verdict** — attenuation does not move `accuracy_whole` enough to tell
  the two apart on this arm. Reported per arm.

**Both forms are computed and reported everywhere. Neither is adopted here.**

### D-3. The untouched floor, measured rather than assumed

Command: `denominator.py --stage floor`

`accuracy_untouched` is measured on every arm and seed, and compared with the
two predictions on the record: the proposal's "near one in eight", and the
review's `(1 - accuracy) / 7`.

- **Pass** — the measurement is reported beside both predictions, and the
  sanity rule of section 6.3 is judged against it in plain words.
- **Fail** — not reachable; this check is a measurement, and failing to take
  it counts as a trip under stop condition S8 rather than a skip.

### D-4. Whether control 6's first cell can be populated at all

Command: `denominator.py --stage control6`

Two things are measured.

1. **On the distinctness-preserving grammar** — the one the rehearsal has
   already built, and the one the proposal requires — the number of trials in
   the same-value cell is counted.
   - **Pass** — the count is exactly **zero**, confirming that the cell is
     empty by construction and not by bad luck, with the structural reason
     stated: within an item the four values are distinct and the successor
     rule is one-to-one, so distinct sources give distinct answers.
   - **Fail** — the count is not zero, which would mean the structural
     argument is wrong and the finding needs re-examining.
2. **On a grammar that relaxes distinctness for a designated subset of
   trials** — the cost of populating the cell is measured: how many trials it
   yields, and what it does to the reference a blind solver can reach on those
   trials. The expectation, written down first: where two of the four agents
   share a value, a solver that cannot tell which agent it is lands on the
   right value **one time in two** rather than one in four on those trials, so
   populating the cell moves the comparison's reference on exactly the trials
   it populates.
   - **Pass** — both numbers are measured and reported, so the trade is
     visible rather than argued.

---

## 3. What this addendum does not do

- It does not change the measure in `measure.py` from what section 6.3
  registers. That function keeps computing the registered form, and the
  floor-corrected form is added **beside** it, with both reported everywhere.
- It does not name a floor, a separation bar or a corrected-form constant.
- It does not change the grammar the other rehearsal items run on. The
  relaxed-distinctness set exists only for check D-4 and for control 6, is
  generated separately, and is labelled wherever it appears.
- It does not touch registered text, the compute ledger, `data/project.toml`
  or any ruling, and it spends nothing.
