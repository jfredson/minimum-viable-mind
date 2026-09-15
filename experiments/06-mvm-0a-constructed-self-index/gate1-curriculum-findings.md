# Gate 1 — the Candidate A grammar, and what building it exposed

*2026-09-15. Status: **measured record, not adjudicated.** Gate 1 is the
second action Amendment A3 orders (§4.1) and the second free one. Its
kill criterion K1 — gates (i) or (ii) failing after two regenerations —
**did not fire**. Everything ran locally at **$0**; nothing was trained,
no pod was created [C1/C2]. Code: `src/curriculum_a3.py`,
`src/encoding_a3.py`, `src/cue_detector_a3.py`, all committed at
`7ab8018` before the gate was run on them. Records in `a3-gates/`,
frozen batteries in `batteries-a3/`.*

## The grammar, in one paragraph

Twelve turns, four agents, two contested items. Every agent assigns each
contested item exactly once, and the four values on an item are distinct,
so the four assignments differ only in who made them. Then every agent
revises exactly once, two agents per item, in random order. The revision
rule is shared and deterministic: the revised value is the successor of
that agent's own earlier value on that item. The rule is the same for
everyone; applying it requires knowing which of four assignments was
yours. The supervised position is the model's own revision, and the
metric read there is `T_act`.

`curriculum.py` and `encoding.py` were not edited. Their token ids are
what make every record in `lesion-results/` and `null-calibration/`
reproduce, and the five existing checkpoints were trained under them, so
A3 gets new modules rather than changes to old ones. The A3 vocabulary
adds exactly one word, "next", which the control battery's counterfactual
needs.

## The gate result

| run | clean AUC | 95% interval | positive control | verdict |
|---|---|---|---|---|
| (i) curriculum text, plus episode-relative features | 0.5097 | [0.4867, 0.5316] | 0.9433 | PASS |
| (ii) input tensors | 0.5259 | [0.5032, 0.5498] | 1.0000 | PASS |

Both clean intervals sit inside the registered equivalence bound of
[0.45, 0.55], and both positive controls fire well above the 0.70 floor.
**K1 does not fire.**

## Four things worth John's attention, three of them free fixes

**1. The first draft of this grammar was killed by its own self-test, and
the record says so.** It gave the model one revision and one other agent
one revision, leaving two agents with assignments only. That made the
model's agent the only one with three turns, so **agent turn count
predicted ownership perfectly** — 3 turns for the model in every episode,
against 0.43 of other-agent turns — and revision status predicted it at
0.33 against 0.14. Giving every agent exactly one revision removes both
cues by construction instead of by measurement. The failure is recorded
because a design that passes a gate on its second try should say what its
first try did.

**2. The detector had to be given features the registered one lacks.** An
A3 turn renders identically whether it assigns or revises —
"<marker> assign <item> to <value>" — so a detector reading only a turn's
own text, position and length cannot see that the turn repeats an item
its agent assigned earlier. The registered feature set would have caught
the first draft through turn count, but a variant that balanced counts
while leaving revision status skewed would have passed it. So gate (i)
here adds episode-relative features: revision status, how many earlier
turns share the item, rank within the revision block, and the agent's
share of revisions. A gate is only as good as what it is handed, and
handing it less than the model can see is how a clean verdict gets
manufactured.

**3. The pre-stated lookup ceiling of 0.25 is not what this grammar has.
Measured: 0.2925.** Because two agents revise each item, a solver that
inverts the rule on a co-reviser who went first can strike one candidate.
The model revises first half the time, so the ceiling is 0.25 on half the
cells and 0.333 on the other half. This is the price of making every
agent revise, which is what removes the ownership cue in finding 1, so
the two cannot both be had for free.

The control battery is worse: `T_other` has a measured ceiling of **0.5**,
because both revisions on the queried item strike a candidate each. That
asymmetry matters more than it looks, because the H_generic-binding bin
turns on the difference between the two batteries' drops, and the two
batteries no longer start from the same place.

**Recommendation for red-team pass 3:** either adopt the measured
ceilings as the pre-stated ones, or buy 0.25 back by adding a third
contested item that nobody revises, which restores a four-candidate set
for both batteries at roughly a third more compute per run. This is a
design choice with a price, so it is John's rather than mine. Both
numbers are recorded in `batteries-a3/batteries_meta.json`, measured
rather than asserted.

**4. Gate (ii) fails a clean grammar about one run in nine, and that is a
property of the gate, not of A3.** The registered gate reports one AUC
with a bootstrap interval, and that interval resamples the test split of
a *single* draw of episodes. It measures uncertainty within one sample
and is silent about how far the point estimate wanders between samples.
On this grammar the two are not the same:

| run | mean over six independent samples | spread | chance a clean grammar fails |
|---|---|---|---|
| (i) text | 0.4939 | 0.0120 | under 1 in 1000 |
| (ii) tensors | 0.5054 | 0.0224 | about 1 in 9 |

The registered seed's tensor AUC of 0.5259 is within one spread of
chance, and the six-sample mean is 0.5054. There is no cue: the own
register's stack index is uniform to within one standard error over
40,000 episodes. What the classifier fits on one draw is that draw's own
chance imbalance, part of which survives into the test split of the same
draw.

The consequence is procedural. K1 permits two regenerations, so a clean
grammar being failed once and regenerated for nothing is likely, while
being killed outright is not. **Recommendation for red-team pass 3: take
the gate (ii) verdict over several independent samples rather than one,
or raise its episode count to about 14,000, which is where its spread
matches gate (i)'s.** The stability check is now part of the tooling
(`cue_detector_a3.py --stability`) and its record is in `a3-gates/`.

## Batteries frozen

400 items each for `T_act`, `T_other`, `T_state` and `T_syntax`, as A1
skeletons under generator seed 20260915, before any training [RT-14,
RT-19, A1.5]. Each item pre-commits the episode recipe and an enactment
seed; the checkpoint under evaluation enacts its own turns under that
seed at eval time, and the stored episode is the audit record of that
deterministic enactment, never a substitute for it. `T_act` is the
Gate 0 cell-size fix delivered: 400 episodes now yield **400 scoring
cells**, not the 19 the registered grammar's revision-conditioned battery
yields at the same episode count.

## What Gate 1 does not claim

It does not claim the objective is learnable — that is Gate 2, and it
costs money. It does not claim the grammar carries no ownership cue at
all, only that two detectors with pre-committed capacity cannot find one
within a pre-committed bound, which is what the registration asks and no
more. It runs no model. And it does not settle the two design questions
in findings 3 and 4; it prices them and hands them over.

## Cost

**$0.** A3 cumulative spend remains **$0.00 of the $100 hard stop.**

## What comes next

The ratified order is Gate 0 → Gate 1 → red-team pass 3 → registration
commit → Gate 2. Gates 0 and 1 are done and free. **Red-team pass 3 now
carries five items**: the three from Gate 0 (the verdict cell size, K2's
mismatched units, and which checkpoints K0's band is read on) and the two
above (the ceiling numbers, and the gate (ii) sampling fix). After that
the registration commit, and only then the pilot, on John's authorization
in his own words.

One build step remains before the pilot and it is free: the trainer does
not yet know about `T_act`. The loss must sit at the own revision
position and `eval_heldout` must score there rather than at an appended
query. The encoder already emits that position, held apart from the
model's inputs so gate (ii) cannot see it.
