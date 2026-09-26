# Ruling 2026-09-26: the Gate C review of successor proposal version 2, RT-212 to RT-229

*Recorded 2026-09-26 (Pacific), in a Cowork planning session. Mixed authorship:
the findings are the Gate C tier 1 review's,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
(on main by pull request 56, commit `c17dbdc`), which reviewed
`docs/successor-experiment-proposal-2026-09-26-v2.md` at commit `e88c3c0`
(pull request 54, branch `worktree-w1d-proposal-v2`). Each ruling was put to
John in plain language with a recommendation, and he ruled "Agreed" on each.
The choices are his; none of the wording is his drafting. No compute was
launched and no money was spent under this ruling. Every number below is the
review's; the review has no numbered sections, so each ruling cites the
review's heading for that finding (for example "review, RT-212").*

*Written under the workspace plain-language rule. Nothing here edits registered
text or protocol text. Where an earlier ruling is refined, that is said at the
ruling that does it: this file refines `docs/rulings/2026-09-26-weekend-1-queue.md`
(pages 1b, 1e, 1h and 2) and `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`
(item 2), and widens item 10 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, and is read
with them.*

---

## What was ruled

### RT-212 (fatal). The free arm's ownership read never finds its label

*Review, RT-212. On arm F the read fitted at the action position scores at most
0.172 on held-out development episodes at any layer on any seed, against a
no-information level of 0.072; on arms T and M it fits at 1.0 or near it, and on
arm C at 0.96 or above from layer 1.*

1. **Version 3 registers a no-verdict rule.** The nomination's held-out fit
   accuracy on development episodes goes in the reporting table, and a read
   that misses a pre-stated floor returns no verdict on that arm. **The floor
   is absolute: four fifths on held-out development episodes**, the same
   convention as the site-set floor (queue ruling, page 1c). The
   label-permutation null (the fit a read reaches when the labels are shuffled)
   is reported beside it, not used as the bar. Reason recorded: a permutation
   null alone would likely certify arm F at 0.172, which recovers the label on
   about one episode in six; that is not an instrument worth transplanting.
   Version 3 must show, measured at toy scale, that the floor returns no
   verdict on the committed arm F reads and a reading on T, C and M.

2. **Arm F's toy reading is withdrawn from the record** under failure 2's own
   rule (the pre-stated target changes before registration, and the null
   already collected is withdrawn rather than reported). The toy record states
   arm F as **"no verdict, read failed its floor"**, not "fully entangled".
   Arm C's toy reading stays, read with RT-213.

3. **The review's route (b) runs as a $0 toy-scale investigation session on
   2026-09-26, in parallel with version 3, not as a blocker.** Route (b) is a
   label the own-directed loss forces on a free system; the candidate to try is
   "which earlier turns' values are the model's own", on the committed arm F
   seeds. If a read clears the floor before Gate A, it enters version 3 as a
   second registered read. If not, version 3 registers with item 1 alone and
   states that arm F may return no verdict at registered scale. Whether a
   registered "no verdict on the free arm" is worth the $161.90 is John's call
   once the investigation reports; his present view is yes.

### RT-213 (serious). Arm C fails the learn-both gate on every toy seed

*Review, RT-213. Arm C's named-other condition scores 760, 751 and 708 correct
of 3,000 against a bar of 790 (`gate_base.json`).*

1. **The constructed arms T, C and M are gated on the own-directed condition
   only; arm F keeps the learn-both gate.** Reason recorded: the anchors'
   ownership slot is built in by construction, their reading uses only the
   own-directed action, and the named-other gate tests whether a free system
   learned to represent ownership, which the anchors are not asked to prove.
   On the anchors' own terms the toy outcome is R1. This refines queue ruling
   page 1b as it applies to arms T, C and M; the bar itself is unchanged.

2. **Arm C's named-other failure is stated with its numbers** (760, 751, 708 of
   3,000 against 790) in sections 5.2, 10, 11, R-1 and R-3, with the cost of an
   arm C failure under the launch order.

3. **No extra arm C run in step 5a.** At $422 to $434 of $450 the envelope has
   no room, and under item 1 the failure no longer fires an R3. If John later
   wants the anchor's construction proven at registered scale before the second
   release, that run needs the ceiling revisited.

### RT-214 (serious). Control 3 fails on arm M seed 1

*Review, RT-214. Arm M seed 1's random subspace moves 0.0563 of trials against
a limit of 0.0350, so under version 2's rules arm M gets no reading on that
seed.*

1. **Control 3 becomes a multi-draw null:** many random subspaces of the same
   rank at the same sites (twenty at toy scale), and the reading counts only if
   the ownership-only transplant beats the 95th percentile of the random draws.
   The fixed 0.0175 room in control 3 is dropped.

2. **Control 3 is re-run on all four arms under that null at toy scale before
   version 3 is filed**, and reported for all four in the reporting table. If
   arm M clears on all three seeds, the fold-in ruling (repairs ruling, item 2)
   stands and is annotated with the checked figures; if not, the fold-in
   returns to John as a fresh ruling.

3. **Version 3 states that version 2's arm M pass was read without control 3
   applied.**

### RT-215 (serious). The registered site-set rule was never run

*Review, RT-215. The toy ran 44 hand-listed site sets; the registered rule
(every contiguous layer set times four position sets) gives 60 on the toy, 24
of which never ran, and 8 of the sets that ran are excluded by it.*

The registered site-set rule is **run at toy scale before version 3 is filed**,
as **one combined re-run** with the RT-212 fit floor and the RT-214 null, so
every toy number in version 3 comes from one run under the rules being
registered. If any nomination moves to a multi-layer set the hand list never
tried, version 3 reports it and the sensitivity row from the new run. The
ruling-file annotation the review asks for is done (repairs ruling,
annotation 4, pull request 53).

### RT-216 (serious). Most nominations sit where the acting channel is injected

*Review, RT-216. Layer 0 is the state the acting channel is added to; six of
the nine nominations on arms C, F and M are layer 0 at the "post-identity"
position set, which spans the turns where the channel fires.*

1. **Layer 0 stays a candidate at the action position set only**, where the
   constructed anchors' slot sits by construction. A layer-0 nomination at any
   position set spanning the acting turns (post-identity, and any set including
   the marked turns) is excluded by rule, written into section 7.2, and
   reported as **"at the acting channel's injection", no verdict**. This refines
   queue ruling page 1e.

2. **W7's last sentence is struck** and replaced by the measured fact: on the
   toy, six of nine nominations on arms C, F and M sat at the injection.

3. **The combined re-run also reports the stricter variant, layer 0 excluded
   everywhere, as a sensitivity row**, so John can switch to it with figures in
   hand before Gate A. Reason for not ruling the stricter variant blind: it may
   move arm T's anchor read off the layer its slot was built at.

### RT-217 (minor). The $16 wager

*Review, RT-217. On the ruled split the top of arm M's range leaves $14.79.*

The wager is stated on the ruled split against the full range, and **its floor
is lowered to $10**.

### RT-220 (minor). The lesion description, and when arm F is read

*Review, RT-220. Arm T seed 2's lesioned own-directed accuracy is 0.2733
against the bar of 0.2633.*

The toy lesion is described honestly: arm T collapses on two of three seeds;
seed 2 reads 0.2733 against 0.2633. **Registered: arm F is read if at least two
of three seeds collapse, with the third reported.** A separate collapse bar
below the learn-both bar was considered and not taken, because it adds a second
pre-stated number nobody has rehearsed. This refines queue ruling page 1h.

### RT-222 (minor). The 0.0175 allowance

*Review, RT-222. The allowance was set from a miss of 0.017536, which fails it;
near the learn-both bar it detects a broken pairing by 0.0023.*

The allowance is written as **"at most the largest measured miss, rounded up to
0.018"**, and the detection margin at the bar is printed in the reporting table.
The mechanism is not changed this weekend. This refines the wording of queue
ruling page 2's "room for the miss of up to 0.0175".

### RT-229 (minor). Which release pays for arm M's development run

*Review, RT-229. Arm M's development run appears in the first release's
development line and again as $1.94 in the second release.*

The first release's development line covers four arms. **This widens item 10 of
the 2026-09-21 ruling on staged spending, which covered three.** The $1.94 comes out of section 12.4. Reason: arm M's code has
never run on the rented machine (RT-228), so its development run belongs in
step 4 with the others, before the second release.

### RT-218, RT-219, RT-221, RT-223 to RT-228 (minor). Accepted as the review states each fix

- **RT-218** (review, RT-218): section 7.2 item 4 says "8 of 12 by site set,
  7 of 12 by share" and drops the word "discrepancy".
- **RT-219** (review, RT-219): no change beyond dropping "discrepancy"; 0.60375
  (483 of 800 fresh trials) stays; the findings' sentence is corrected at its
  check.
- **RT-221** (review, RT-221): quote the separation figures the rule produces
  and label the old ones (0.9977, 0.9927) as coming from the pre-widening
  family; arm C's range in section 5.2 follows.
- **RT-223** (review, RT-223): say that arm M's formula is the true-slot reading
  written in route accuracies, one check, not two.
- **RT-224** (review, RT-224): the position set is "the action position and the
  answer-marker token just before it".
- **RT-225** (review, RT-225): one clause saying the rider's no verdict on arm M
  is a miss of the four-fifths floor (the whole-state transplant moves about
  0.41), not nothing reaching the state.
- **RT-226** (review, RT-226): the 8.47 against 2.42 citation points at the
  ledger lines that carry it; the $10.04 is called "the lifetime-priced cost".
- **RT-227** (review, RT-227): version 3 cites main-line merge commits (pull
  request 52 is `882f252`, 51 is `9f802db`, 53 is `62c3824`) and re-derives
  every arm C, F and M figure from the combined re-run (RT-215).
- **RT-228** (review, RT-228): the launcher file is named in the registration,
  and arm M's code on the rented machine is listed as untested beside the
  handshake's machine half (W9).

## What this changes, and where

Version 3 of the successor proposal:

- **Section 3** (what counts as a result): arm F may return no verdict (RT-212);
  the toy outcome on the anchors' terms (RT-213).
- **Section 5** (opening sentence): the launcher named (RT-228).
- **Sections 5.2, 5.3, 5.4**: arm C's named-other failure with its numbers and
  figures from the combined re-run (RT-213, RT-221); arm M's formula as one
  check (RT-223); arm F's toy reading stated as "no verdict, read failed its
  floor" (RT-212).
- **Section 6.4**: the allowance as "at most the largest measured miss, rounded
  up to 0.018" (RT-222).
- **Section 7.2**: the fit floor and its toy demonstration (RT-212); the rule as
  run (RT-215); the layer-0 exclusion off the action position (RT-216); the
  8 of 12 wording (RT-218); the position-set wording (RT-224); the rider's
  cause on arm M (RT-225); a second registered read if the investigation clears
  (RT-212).
- **Section 7.3**: control 3 as a multi-draw null, reported for all four arms,
  with version 2's arm M pass stated as read without it (RT-214).
- **Section 7.4**: the floor and the null frozen with the rest.
- **Section 8.1**: arms T, C and M gated on the own-directed condition only
  (RT-213).
- **Section 8.2**: the lesion description and the two-of-three rule (RT-220).
- **Section 9**: separation figures from the combined re-run (RT-221, RT-227).
- **Sections 10 and 11**: arm C's failure in R-1 and R-3 and its cost under the
  launch order (RT-213); arm M's development run in step 4 (RT-229).
- **Sections 12.3, 12.4, 12.5, 12.8**: the four-arm development line and the
  $1.94 out of 12.4 (RT-229); the ledger citations (RT-226); the wager on the
  ruled split with a $10 floor (RT-217).
- **Section 13**: W7's last sentence struck and replaced (RT-216); arm M's code
  on the rented machine listed as untested beside W9 (RT-228).
- **Section 16 and every citation**: main-line merge commits (RT-227).
- **The reporting table**: fit accuracy and the permutation null (RT-212),
  control 3 for all four arms (RT-214), the layer-0-excluded sensitivity row
  (RT-216), the detection margin at the bar (RT-222).

Before version 3 is filed: one combined toy re-run under the registered site
rule, the fit floor and the multi-draw null (RT-212, RT-214, RT-215, RT-216).
In parallel on 2026-09-26: the $0 route (b) investigation on arm F (RT-212).

## What this file does not do

It edits nothing: not the proposal (version 3 carries the changes), not the
queue ruling, the repairs ruling or the 2026-09-21 ruling (refined here, and
annotated beside where needed), not the ledger or any protocol text. It issues no go. If
the combined re-run or the route (b) investigation moves a number above, the
ruling is re-read against the new figure and this file is annotated, not
rewritten; RT-214's fold-in returns to John as a fresh ruling if arm M fails
the new null on any seed.
