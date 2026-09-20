of each other when intact (0.5683, 0.5633, 0.5738), and zeroing the one
channel that tells the model which agent it is collapses all three (to
0.1988, 0.2015, 0.1447). Every one of those falls clears the locked bite
threshold by seven to nine times. Nothing in this memo touches that.

**C2 — The registered comparison is dead, and for a structural reason.**
Measured on 2026-09-17 (`ceiling-measurement-findings.md`): the control
battery's ownership-blind ceiling — the score reachable by a solver that
knows nothing about which agent the model is — is **1.0**, reached
independently by a hand-written name-keyed lookup and by a learned
attack. The registered damage measure divides by the distance from the
battery's own score to that ceiling, and the floor rule requires that
distance to be at least 0.10. A defined damage figure for the control
therefore needs a score of **1.10**, which no model can reach. The clause
has been unsatisfiable since registration, months before a checkpoint
existed.

**C3 — The incompatibility generalises, so a repair must remove it, not
route around it.** A control designed to be answerable without ownership
has an ownership-blind ceiling of 1.0 by construction. Dividing by the
distance to that ceiling divides by zero or less. **A ceiling-corrected
damage measure and an ownership-free control are incompatible by
construction.** Any replacement clause that still divides by a ceiling
distance on the control inherits the same defect.

**C4 — No metric may be changed after seeing which way it cuts.** This is
the programme's central discipline and it has already refused one free,
available fix for exactly this reason (dividing by chance instead of the
ceiling, rejected on 2026-09-17 as fitting the rule to the data). Any new
clause must be written down, thresholded and committed **before** the
data it will be read on exists.

**C5 — A bite is counted by signed degradation.** John's ruling of
2026-09-19 (worklog decision `c79b82d7`, "sensitivity test counts a bite
by degradation"): damage counts only when the score goes **down**; an
improvement never counts. At least 800 episodes, with intact and damaged
readings taken on the same episodes. A fourth outcome cell exists for
"the structure was located but it is the wrong structure". Any new clause
carries these forward.

**C6 — The registered ceiling defect is a precondition on any amendment.**
John's instruction of 2026-09-17, now written into the amendment document
itself: the control's stated ceiling of 0.3227 was never verified by the
attack sweep, rests on a reference solver that cannot read the name the
question supplies, and disagrees with the design module's own stated 0.5.
**If an Amendment A4 opens, that ceiling must be measured properly
first.** It has been: the measurement is the 1.0 figure in C2, and the
measurement reproduced both registered known-answer checks to four
decimal places before reporting anything new. This precondition is
satisfied.

**C7 — Money is not the binding constraint, but the caps are real.**
Spent against the A3 hard stop: **$34.31 of $100** (kill criterion K6,
which halts everything). Spent against the wider envelope: **$215.7 of
$400**, leaving about $184. The RunPod account spend limit is $80 and the
funding rule requires the balance to cover the estimate plus $10 before a
launch. A two-seed wave at about $20 fits all three with room.

**C8 — Two gates hold absolutely.** No registered text changes without
John's ruling. Nothing launches without John's go in his own words,
quoted in the ledger row before the spend.

---

## 2. What changed since the 2026-09-17 draft

Six things, in the order they matter.

**1. The ceiling measurement mooted the previous candidates.** The
2026-09-17 proposal offered four routes, two of which (extra supervision,
a scaffolded intermediate question) aimed at making the control battery
learn, at $27 to $39. A perfectly learning control would have changed
nothing whatever, because the clause fails at a score of 1.0 just as it
fails at 0.32. That proposal is withdrawn, and the annotation on it says
so.

**2. The question itself changed shape.** It is no longer "how do we make
the control learn". It is "can the comparison be repaired at all, and is
the repair a change of measurement rather than a change of training".

**3. The extra-seeds date is answered, not deferred.** John ruled on
2026-09-17 (worklog decision `36413c8d`) that the 20 September
extra-seeds question is closed: it asked for more seeds routed to a
checkpoint whose control had learned, and no such checkpoint exists or
can exist. Any further seeds are now seeds of an amended design, which
makes them this decision's business rather than a separate one.

**4. The bite rule is ruled, and it left one thing open.** C5 above. The
ruling explicitly routed one question here: whether to replace a single
crossing of a threshold with a graded ladder of partial damage requiring
the degradation to grow as more is removed. That is answered in §5.4.

**5. There is now a published precedent for the shape of the repair.**
The Pain Axis paper (Tagliabue, Dung & Berg, arXiv 2609.16247, September
2026; read and summarised in `docs/research-note-pain-axis-2026-09-19.md`)
builds its strongest result as a **matched comparison between identical
content directed at the self and at another**, scored by how cleanly the
two sets of numbers can be told apart, with **no ceiling anywhere in the
denominator**. That is the shape our control comparison was meant to have
and never had. The precedent matters for C4: it means the comparison is
built that way because that is how this kind of comparison is built, not
because it is the shape that makes our numbers work.

> *Verification note, per the standing rule on facts stated from memory:
> the Pain Axis figures were read through a summarising fetch of the
> paper's web version and have **not** been checked against the PDF.
> Nothing in this proposal depends on any number from that paper. It is
> cited only as precedent for the shape of a comparison.*

**6. The date moved.** The decision was scheduled for 4 October. John
intends to rule today and, if the ruling is for an amendment, to launch
tonight. That is why this memo carries the registerable text, the
threshold plan and the cost estimate rather than deferring them.

---

## 3. The candidates

### Candidate A — Close A3 with partial discriminators

Report the primary result, the instrument audit, and the comparison that
was never available, and say all three plainly. **Cost: $0.**

**What it yields.** A replicated, well-measured finding that an objective
requiring a model to act as itself is learnable at 30M parameters, and
that removing the one signal telling it which agent it is collapses that
ability. Plus an unusually candid instrument audit: a registered
denominator that was never checked, a verification attached to the wrong
battery, and a design comment that warned about it and was not acted on.

**What it costs in strength, stated honestly.** The discriminators that
survive without the control are the matched other-agent damage test, the
random matched-subspace tests, and the swap probe. **All three run
through a localization stack that has so far found nothing anywhere.**
Its probes fell below their own permutation baselines on a checkpoint
where ownership is measured to be load-bearing; the blind arm was not
flagged and landed on the worse half of that outcome; and one damage test
*improved* the battery it was meant to hurt. So the partial
discriminators are partial in a stronger sense than the phrase suggests:
they are the ones whose instrument is currently unvalidated.

**What the write-up then claims.** That removing the ownership input
breaks the ownership task, while two ownership-free batteries hold. The
weakness a reader will find immediately: those two batteries (cross-turn
state, turn counting) are **much easier tasks**, scoring 0.999 and 1.000
intact. "The damage broke the hard thing and not the easy things" is not
the same claim as "the damage was specific to ownership", and Candidate A
cannot separate them.

### Candidate B — Register Amendment A4: replace the differential clause with a separation-scored comparison

Keep both batteries exactly as they are. Keep the grammar, the frozen
batteries, the gates and the attack sweep untouched. Replace the one
registered clause that compares the two batteries' damage figures with a
comparison that scores **how cleanly the damage to the ownership-dependent
condition separates from the damage to the ownership-free condition, on
matched content, under the same damage operation**, with no ceiling in
any denominator. Lock its threshold on checkpoints nobody reads a verdict
from, then read it on two **fresh** checkpoints, seeds 3 and 4, launched
as one wave. **Cost: about $20.**

**The fact that makes this cheap.** Every episode in the frozen batteries
already carries **both** queries — the self-directed one, scored at the
model's own revision position, and the other-directed one, asking the
same rule's verdict for a named other agent. Same turns, same items, same
rule, same episode; **only the agent whose commitment is queried
differs.** The matched self/other contrast the Pain Axis paper had to
build on purpose is already inside our registered grammar by
construction. So Candidate B needs **no grammar change, no re-freezing of
batteries, no change to training, and no new attack sweep.** It needs a
new scoring script and two fresh checkpoints.

**What it repairs, and what it does not.** It repairs the comparison. It
does **not** repair the localization question — where in the network
ownership lives — which remains open and whose instrument remains
unvalidated. §5.7 states this as a registered limitation so that a
positive result cannot be read as more than it is.

---

## 4. Recommendation

> **Register Amendment A4 (Candidate B), under three conditions, and
> launch seeds 3 and 4 as one wave tonight if John's go is given.**

**Why B over A.** Candidate A closes a registered comparison as
permanently uncomputable at the exact moment a computable version of the
same comparison is available, costs about $20, requires no change to the
design being tested, and can be locked before the data it reads exists.
The scientific content at stake is not decoration: the matched self/other
contrast is the only thing in the design that can separate "the damage
was specific to ownership" from "the damage broke binding in general",
and that separation is the difference between a finding about
self-indexing and a finding about binding. Candidate A cannot make it.
Candidate B can, on data that does not yet exist, under a threshold
committed in advance.

**Why this is not the forbidden move.** C4 forbids changing a measure
after seeing which way it cuts. Three things keep B on the right side of
that line, and John should test each of them rather than take them:

1. The reason for the change was **measured before the change was
   proposed**, and the measurement was one John required as a
   precondition. The ceiling-corrected measure is incompatible with an
   ownership-free control *by construction* (C3) — a fact about the
   design, not about our results.
2. The replacement has a **published precedent** for why a comparison of
   this kind is built without a ceiling in the denominator.
3. The verdict is read **only on fresh checkpoints**, with the threshold
   locked and committed before those checkpoints exist, and with an
   explicit written commitment that the new statistic is not computed on
   seeds 0, 1 or 2 before the lock (§5.5).

**The three conditions.**

- **(i)** The clause is read on fresh seeds only. Seeds 3 and 4 must both
  satisfy it. Seeds 0, 1 and 2 may be scored under it *after* the verdict
  is read, reported as a consistency check, labelled as such, and never
  counted toward the outcome.
- **(ii)** The threshold is calibrated only on the register-less twin
  checkpoints and an untrained model, by the plan in §5.5, and **John
  commits the lock file**, as he committed the existing one.
- **(iii)** The registration states in terms that A4 repairs the
  comparison and not the localization, so that a positive result under
  the input-channel removal is reported as *the ownership input being
  specifically load-bearing*, never as *an acquired internal structure
  having been found*.

**Confidence, and the strongest case against.** My confidence that B is
the right call is **moderate-to-high** on the reasoning and **moderate**
on the outcome — I think the clause is the right instrument and I do not
predict it will fire. The strongest argument against B, which I cannot
fully answer, is in §6.1: **the content-matched comparator never learned**,
so it may be unable to show damage, and a comparison in which one side
cannot move is a weaker comparison than it looks. §5.2 adds a second,
learned comparator to cover this, and §6.1 says plainly what remains
uncovered.

---

## 5. The amendment, in registerable form

Everything in §5 is drafted so it can be lifted into an `amendment-a4.md`
and committed. It is **not** registered until John rules and the
registration commit is made.

### 5.1 Definitions

**Matched cell.** An evaluation episode carrying both queries: the
self-directed query (the primary battery, scored at the model's own
