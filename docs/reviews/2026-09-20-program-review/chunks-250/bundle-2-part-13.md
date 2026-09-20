   reproduce that checkpoint's endpoint means, intact and lesioned, for
   every battery, to the rounding (F19).

### H4 — The outcome table must partition the outcomes and keep ruled names (from F9, F10, F13, F21)

- Every combination of the clause's conditions lands in a named cell,
  including: the separation condition holding while a comparator or
  control condition fails; an improvement of the primary inside the
  band; two seeds of three; a seed returning not-testable while the
  others pass. The A3 bins "seed-dependent" and "unstable" are carried
  (F13, F21).
- Cell names are not reused from the registered A3 bins unless the cell
  carries the same discriminators. A positive under an input-channel
  lesion is named for what it measures, on the order of "the ownership
  input is specifically load-bearing for the self-directed condition";
  H_self-location stays reserved for the localized result (F9).
- A cell John has ruled keeps its ruled meaning. The 2026-09-19 "located,
  wrong structure" cell means the ablation improves the primary battery
  beyond noise; a comparator-falls-more outcome gets its own name (F10).
- Three fresh seeds, three of three for a positive, as A3 registered.

### H5 — The validity gates must exist and have been run (from F17)

The neutral-episode likelihood bound and the long-generation degeneracy
probe have no A3 implementation and have never been applied to the
input-channel lesion on any seed. Before a clause names them, they are
implemented for the design's grammar and run on the seen seeds under
every lesion the clause will read, and the result is reported. A gate
whose first application is on the verdict seeds is either a surprise
kill or a sentence.

### H6 — Reporting rules registered with the clause (from F11, F12)

- Seen seeds are reported under their own heading, labelled seen and
  verdict-free, never in the same table as fresh seeds.
- The write-up states which cells were reachable on the checkpoint read,
  not only which fired.
- Any dose ladder on an input scaling is reported as an input-scaling
  curve, with the statement that a smooth reduction of one signal is
  monotone by construction.

---

## Part 2 — What the pilot must show for H1 to be satisfiable

The pilot is one unregistered seed. What it can decide is whether the
control battery, given its own loss term, reaches a level at which a
comparison has room to move. The numbers below are stated before the
pilot reports and are read against the pilot's intact scores measured
the way the endpoint reads are: at least 800 episodes, at least six
independent evaluation seeds, mean and spread reported. Where a
threshold is compared against a mean, use the mean minus one spread, so
that a lucky draw does not clear a bar.

### The fixed points these numbers rest on

| quantity | value | source |
|---|---|---|
| primary battery intact, seen seeds | 0.5683, 0.5633, 0.5738 | the endpoint findings, `seeds-endpoint-findings.md` |
| primary under the input-channel lesion | 0.1988, 0.2015, 0.1447 | same |
| primary's chance floor / ownership-blind ceiling | 0.125 / 0.2921 | `batteries-a3/batteries_meta.json` |
| control intact, seen seeds | 0.2877, 0.3057, 0.3195 | the endpoint findings |
| control under the input-channel lesion, seen seeds | 0.2283, 0.2342, 0.2617 | the endpoint records, `a3-gates/endpoint_*.json` |
| control's chance floor / name-blind reference / true ownership-blind ceiling | 0.125 / 0.3227 / 1.0 | `ceiling-measurement-findings.md` |
| evaluation noise at 800 episodes, primary / control | sd 0.0169 / 0.0233 | `a3-gates/eval_noise_a3.json` |
| random-damage band on the primary, 95th percentile | 0.1777 corrected, about 0.049 raw | John's lock, `null-calibration/theta_delta.lock.json` |

From these: the primary's room (intact minus chance) is about **0.44**;
its fall under the input-channel lesion is about **0.37 to 0.43**; a
random-damage spread of the mean drop is of order **0.02 to 0.025 raw**
(a standard deviation runs about half the 95th percentile), so a
difference of two drops is inside the null when it is below about
**0.05 raw**.

### Tier A — a raw-difference clause is registerable

The statistic compares raw drops. For the boring cell to be reachable,
a lesion removing the same fraction of each battery's room must give a
difference inside the null even at full removal, so the two rooms must
differ by no more than the band:

> **control intact ≥ primary intact − 0.05**, with both measured on the
> pilot checkpoint. At a primary of 0.57 that is **control ≥ 0.52**.

Under Tier A the statistic needs no denominator that can shrink, the
design's original intent (matched contrast, no ceiling anywhere) is
met, and H1 is satisfied outright.

### Tier B — a relative-drop clause is registerable, with a floor

The statistic compares each battery's drop as a fraction of its own
room. This restores reachability at lower control scores but puts a
room back in a denominator, the shape of the defect that killed the A3
clause, so the room must be large enough that the fraction is not
noise:

> **control room ≥ 0.25**, that is **control intact ≥ 0.375**; and
> **control intact ≥ name-blind reference + 2 sd = 0.3227 + 0.047 ≈ 0.37**,
> so that "learned" means "beats a solver that cannot read the name",
> not "landed near it".

Why 0.25: the standard error of a mean of 400 paired 0/1 differences is
about 0.023 raw; over a room of 0.25 that is a relative error of about
0.09, against about 0.05 for the primary. Below a room of 0.25 the
comparator's relative drop is noisier than the effect it is meant to
detect. The two conditions coincide near **0.375**, which is also
within rounding of the level the corrected A3 floor rule already
required (0.4227) for the old drop to be defined at all; a control that
cannot clear the old floor does not clear the new one either.

Under Tier B the clause must additionally register the room floor as a
not-testable condition on every fresh seed, because a fresh seed whose
control lands below it has no defined comparator.

### Tier C — no separation clause

> **control intact < 0.375** on the pilot.

The control does not learn enough for any comparison to move. The
result is reported as the matched contrast remaining unmet, and the
next design question is the grammar, not the clause.

### Conditions on the primary, which the extra loss term can move

Adding a control loss changes the mixture the primary was learned
under. Whatever tier the control reaches, the primary must still be a
battery a lesion can be read on:

> **primary intact ≥ 0.49** (its ownership-blind ceiling of 0.2921 plus
> 0.20, four times the random-damage band), and its fall under the
> input-channel lesion must still clear the locked band. If the control
> loss starves the primary toward its ceiling, that is the
> shortcut-starvation outcome A3 pre-stated, and no clause is built on
> it.

### What the pilot does not decide

- One seed reaching a tier licenses a design, not a registration. The
  tier is confirmed or not on the redesign's fresh seeds, and a fresh
  seed landing in a lower tier is not-testable under that clause.
- The pilot says nothing about H2. A control that learns the appended
  question to 0.55 is still read at the appended question.
- The pilot's control score under the input-channel lesion will be in
  its endpoint record, as the seen seeds' are. It may be quoted to
  pre-state the expected value of a future statistic (H1, corollary 2).
  It is not evidence for a cell.

---

## Part 3 — What still needs a localized lesion

Everything above makes a comparison clause honest. None of it makes the
comparison answer the programme's question. Two distinct claims are in
play and the requirements for each differ.

### Claim 1 — the ownership input is specifically load-bearing

This is what a separation clause under the input-channel lesion can
say, once H1 and H2 hold. It is a stronger statement than the seen
result, because it controls content and rule on a comparator that can
move. It is still a statement about an input, and the registered text
already concedes that the wire lesion cannot separate a carried binding
from a re-readable pointer (Amendment A3, registration revision 8). No
comparator fixes that, because the two accounts predict the same
behaviour under input removal.

### Claim 2 — the network built a structure that indexes its binding to its own center

This is the registered H_self-location and it needs, in addition to a
comparison that can move:

1. **A localized lesion target**, a low-rank subspace at positions away
   from the model's own act positions, found by probe and patching that
   agree (Amendment A3 §3.2). The stack has found nothing on any seed,
   and the known-answer test validates the plumbing but not the
   ablation path. Before any clause is read on a localized lesion:
   - a positive control the stack recovers, on this design, not a
     synthetic one;
   - the denoised difference-of-means direction from the Pain Axis note
     (item 2 of `docs/research-note-pain-axis-2026-09-19.md`) run
     against the same permutation null, so that "insensitive stack" and
     "no signal" are separated before money is spent.
2. **The discriminators the comparison does not carry** (F3): the swap
   probe moving the action with the patched identity; the other-index
   control, a subspace localized for a named non-self agent, matched in
   rank and probe accuracy, that does not hurt the self-directed
   condition; and the mid-episode re-indexing probe for the tag bin.
   Without these, an act-marker echo or a mine-bit tag passes any
   separation clause.
3. **A random baseline matched to the lesion** in rank, norm and layer,
   which the Gate 0 machinery does produce for a subspace lesion (H2,
   option 2 is met by construction here).
4. **The full bin set**: H_tag, H_self-reference-only, H_diffuse and the
   validity-check-failed bin, as A3 registered them, with the separation
   statistic replacing only the differential conjunct inside them.

### The order this implies

1. Read the pilot against Part 2. If Tier C, stop here and say so.
2. If Tier A or B, redesign the grammar for H2 (an other-directed action
   at an own enacted turn), re-run the gates and the attack sweep with a
   name-reading attacker, measure the new ceilings, and re-freeze.
3. Write the clause to H3 to H6, with substrates dry-run before they are
   named and the scoring script's known-answer test passed on a seen
   checkpoint.
4. Register Claim 1's cell under its own name. Read it on fresh seeds.
5. Register Claim 2 only when Part 3's items 1 and 2 exist on the
   design. Until then, the localized-lesion application of the clause
   is a stated future amendment, not a registered one.

---

*Authorship: this document is Claude's, written to John's brief of
2026-09-19. Nothing in it is a ruling and nothing in it is clause text.
The tiers in Part 2 are pre-stated numbers; the choice of 0.05 for the
raw band and 0.25 for the relative-room floor are judgment calls from
the measured noise, stated so that they can be argued before the pilot
reports rather than after.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md =====

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
