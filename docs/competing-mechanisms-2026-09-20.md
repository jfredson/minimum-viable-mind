# Competing mechanisms: what an ordinary tracker is, what a center adds, and how the difference is read

*Drafted 2026-09-20 (Pacific) as the closure of ledger item RT-118 (Astra
A1, program-level review). Status: DRAFT. Under the 2026-09-20 ruling
`docs/rulings/2026-09-20-center-as-degree.md` this page is a precondition
for any successor pre-registration and is reviewed at Gate A alongside it.
One page by design; anything longer belongs in the book.*

## Mechanism T: an ownership tracker

A system that solves the "act as yourself" task by keeping (a) a table of
agent, item and value assignments updated from the dialogue and (b) a
pointer to which agent it is, acquired from the marked events and consulted
when an action is computed. Under the instruments this program has:

- Removing the pointer degrades own-agent actions (L0 and any localized L1
  lesion both fire).
- Swapping the pointer moves the action to the donor agent's values (the
  swap probe fires).
- Another agent's representation is separately encoded and its lesion does
  not move own-agent actions (the matched other-agent control holds).
- Re-indexing mid-episode is followed after a switching cost that depends
  on implementation, not on whether anyone is home (Amendment A3 §5 R4).

Every observation Amendment A3 registered is produced by mechanism T.

## Mechanism C: a center

A system in which the pointer is the thing the act is organized around:
the ownership signal does not sit in a slot that a retrieval step consults,
but constrains the whole pass, so that early structure (whose turn, what I
committed to) shapes late structure (what I now say) across the act, and
the act cannot be decomposed into a table lookup plus a pointer read
without losing accuracy. This is the spec's "global mutual constraint
rather than a bundle of modular shortcuts" (`spec/minimum-viable-mind-proposal-v0.1.md`,
"The Build"), and ROADMAP.md's Stage 2.

## The ruling that makes these one axis, not two kinds

Per the 2026-09-20 ruling: mechanism T with a causally load-bearing pointer
already is a center, at the bottom of the gradient. Mechanism C is not a
different kind of thing; it is T with more of the act organized around the
pointer. The difference between them is a degree on the integration axis.
So the question the successor asks is not "T or C?" but "how far along the
T-to-C axis is this system, and can the instruments read that?"

## What observation separates degrees

The observation is decomposability. For a system at the T end, there
exists a factoring of the computation into (table, pointer, lookup) such
that patching the pointer alone, with the table held fixed, reproduces the
full counterfactual action; the pointer is separable from the binding. As a
system moves toward C, no such factoring exists: patching the pointer
alone produces an action that is neither the donor's nor the original's,
because the ownership signal was entangled with the content representation
throughout the pass, and reproducing the counterfactual needs the joint
state patched. The degree metric is, to first approximation, the accuracy
lost when the counterfactual is produced by pointer patching alone versus
joint patching, normalized by the joint-patching accuracy. Zero means fully
separable (pure T); the metric rises as the act resists decomposition.

This is a candidate, not a validated metric. ROADMAP.md scopes Stage 2's
deliverable as "deliver the metric, not a verdict", validated on contrast
cases where the answer is known by construction. The successor supplies
the contrast cases: a model trained with an explicit table-and-pointer
architecture (T by construction) and a model trained without one on the
same matched-role task, and the metric must separate them before it is
read on anything else. If it cannot separate the known cases, that is the
registered loss condition and the metric is not used.

## What this page does not claim

Nothing here says where any existing checkpoint sits on the axis; the
metric does not exist yet. Nothing here says that a high reading is
evidence of experience beyond what the founding wager already commits to:
a high reading is a system further along the one axis the wager names.
And nothing here settles whether the axis has a threshold at which "thin
inside" becomes "worth calling a mind"; the spec locates that in the
amplifiers and depth, not in the floor.
