# Free-arm label search at toy scale — method, committed before the code

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1d free-arm label
search", on branch `w1d-free-arm-label-search`, cut from main at `62c3824`.
**UNREGISTERED.** Nothing here is a ruling or registers anything. It answers
route (b) of John's ruling on the fatal review finding RT-212 (the ownership read
on the free arm never finds its label; review file
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`).*

*Order of commits, as the programme's discipline requires: this file, then the
code (`experiments/rehearsal-successor-measure/src/label_search.py`), then its
output (`experiments/rehearsal-successor-measure/out-label-search/`), then the
findings (`docs/2026-09-26-free-arm-label-search.md`). Laptop only, no network,
no rented machine, **$0**. Nothing is retrained. No file under
`experiments/rehearsal-successor-measure/src/` that exists on main is changed.*

---

## 1. The question

Route (b) of the RT-212 ruling asks for a quantity that the own-directed loss
actually forces a freely trained system to carry, and that a fitted straight-line
read can recover on arm F (the freely trained arm) at toy scale.

The ruled label, "which marker word is the model's own"
(`docs/rulings/2026-09-23-nomination-label.md`), is not forced. The own-directed
action (`<act> revise <self> <item> <ans> <mask>`, `grammar.py`) asks for the
successor of the model's own earlier value on one item. The text never names the
model; only the acting channel (a learned vector added at every token of the
model's own turns, `arms.py`, `_embed`) says which turns are its own. So the
action can be solved by finding the acting-marked assignment turn for the asked
item and copying its value, without ever knowing the marker word written at the
start of that turn. On the committed arm F seeds that read fits at no better than
0.172 (review, RT-212).

## 2. The candidates, in the order they will run

All labels are facts about the episode, computed from the generator's own
records (`grammar.render`), never fed to any arm. "Turn k" means the k-th of the
eight assignment turns in text order (0 to 7).

**Candidate 1 — which two assignment turns are the model's own.** The review's
wording ("which earlier turns' values are the model's own") made precise. Every
agent makes exactly two assignment turns, one per item, so the label is an
unordered pair of turn numbers out of eight. The read is one straight-line map
from the state to eight scores, one per turn number, fitted as a softmax over
the eight with each training episode entered twice, once for each of its two own
turns. The prediction is the two highest-scoring turns; it is right only if that
pair is exactly the model's pair. Guessing blind scores about 1 in 28.

**Candidate 2 — which assignment turn holds the model's own value on the asked
item.** Only the one turn the own-directed action needs: `source_turn[OWN]` in
`grammar.render`, a number from 0 to 7. An ordinary eight-way read.

**Candidate 3 — the model's own value on the asked item.** `values[model,
own_item]`, one of the eight value words. An ordinary eight-way read. *Stated in
advance as a weakness:* the correct answer is the successor of this value, a
fixed one-to-one relabelling, so at the action position in the last layers this
read is close to reading the arm's own output. It is the quantity the loss forces
most directly, and for that reason it is the least informative about ownership
as distinct from content. It runs last.

**Stop rule.** Candidate 1 runs on every arm. Candidate 2 runs only if candidate
1 fails the floor on arm F (section 5); candidate 3 only if candidates 1 and 2
both fail. Nothing beyond candidate 3 runs, whatever the result. Every candidate
that runs is fitted on arm F first and then on arms T, C and M for comparison.

**Reference row, not a candidate.** The ruled label ("which marker word is the
model's own", `repairs.READ_LABEL`) is fitted at the same site sets on every arm,
so the candidates sit beside the label they would replace.

## 3. Where the read is fitted: the registered site-set rule

The rule the review ran in RT-215 (proposal version 2, section 7.2 item 2): every
contiguous set of the model's running states, times four named position sets.
The toy has five running states (layer 0 = the input embedding with the acting
channel added; layers 1 to 4 = after each block), so 15 contiguous layer sets,
and 60 site sets in all. Position sets, from `transplant.position_mask`, anchored
at the own-directed action:

- `action` — the `<mask>` position only;
- `action+ans` — that and the `<ans>` token just before it (the review's RT-224
  records that the proposal describes this one backwards);
- `action+3` — the `<self> <item> <ans> <mask>` tokens;
- `post-identity` — every position from the model's first own turn up to the
  action.

**The features a read sees at a site set** (ARGUED; the rule says where, not how
to pool). For the three fixed-length position sets, the running state at each
position in the set, at each layer in the layer set, laid end to end (at most 4
positions × 5 layers × 160 numbers). For `post-identity`, whose length varies by
episode, the average over its positions at each layer, laid end to end across
layers.

**Two structural cautions, stated before any output.**

1. *`post-identity` leaks the identity through its own extent.* Where it starts is
   the model's first own turn, which is one of the two turns candidate 1 asks for
   and is strongly tied to candidate 2. Any average over it carries where it
   starts. A read there can succeed because of how the site set was cut, not
   because of anything the network built.
2. *Layer 0 is the acting channel itself* (review, RT-216). At the action-anchored
   positions this does not matter (the acting channel fires there in every
   episode alike, so nothing at those positions at layer 0 tells episodes apart
   by who the model is). Inside `post-identity` it does: the channel marks exactly
   the model's own turns.

So each candidate's verdict is taken twice (section 5): over all 60 site sets,
and over the 45 **fixed-extent** site sets (the three action-anchored position
sets), whose extent does not depend on who the model is. **The stop rule uses the
fixed-extent verdict**, because a clearance that can come from how the site set
was cut would be no evidence that the free system carries the quantity.

## 4. The fitter, the data, the null

- **Checkpoints.** The committed rehearsal-repair runs for recipe `base`, seeds
  0, 1 and 2, arms F, T, C and M (`ckpt_<arm>_base_seed<n>.pt`). They are not in
  git (`.gitignore`); the copies used are the ones the repairs session wrote, in
  its worktree `.claude/worktrees/w1c-rehearsal-repairs/.../out-repairs/`. Their
  SHA-256 hashes go in the output. **Identity check, run first:** re-fitting the
  ruled label at the action position, layer by layer, must reproduce the
  committed `fit_accuracy.own` figures in `out-repairs/nominate_base_*.json` to
  within 1e-9 on all twelve arm-and-seed pairs. If any differs, the session
  stops and reports that, and fits nothing else.
- **Episodes.** Exactly the repairs' development set: `training.make_data(600,
  seed=4242, pool="dev")`, the 600 recipient episodes, first 70% (420) to fit,
  last 30% (180) held out to score. The same split the 0.172 figure comes from.
- **The read.** `sklearn` `LogisticRegression(max_iter=3000, C=1.0)`, no feature
  scaling: the fitter `repairs.fit_reads` uses, unchanged.
- **Fit accuracy.** The share of the 180 held-out episodes the read gets right.
- **Label-permutation null.** The training labels are shuffled across the 420
  training episodes (for candidate 1, whole pairs are shuffled together), the read
  is refitted, and it is scored against the true held-out labels. **100
  shuffles per site set per seed on arm F; 20 on arms T, C and M and for the
  reference row** (their fits are expected far from the null; the numbers are
  fixed here so they cannot be chosen after). Reported per site set: the null's
  mean, 95th and 99th percentiles and maximum, and where the real fit falls.
- **Chance-corrected fit**, reported beside and deciding nothing:
  `(fit − null mean) / (1 − null mean)`.
- Each arm's own-directed accuracy on the 3,000 gate episodes
  (`out-repairs/gate_base.json`) is printed beside, as context.

## 5. The floor, and what counts as clearing it

The four-fifths floor John ruled (Weekend 1 queue ruling, page 1c) is written
for the whole-state transplant. The session brief applies it to fit accuracy;
this file does the same, on the plain scale: **0.80**.

- A site set **clears on a seed** when its held-out fit is at least 0.80 **and**
  above every one of that site set's shuffled fits.
- A candidate **clears the floor on an arm** when at least one site set clears on
  **all three** seeds of that arm.
- Reported for each candidate and arm: cleared over all 60 site sets (yes/no,
  and which), cleared over the 45 fixed-extent site sets (yes/no, and which),
  and the weaker count of seeds on which *some* site set clears.
- **Stop rule decision** (section 2): a candidate "fails the floor on arm F"
  when it does not clear over the 45 fixed-extent site sets.

## 6. What this cannot say

A read fitting on arm F shows the quantity is linearly recoverable there, not
that the arm uses it, and not that transplanting along it would carry ownership.
Whether any candidate should become the registered label is John's ruling; the
findings make no recommendation about it.

---

## Amendment 1 (2026-09-26, after the identity check and before any candidate was fitted)

**What happened.** The identity check of section 4, run as committed (code at
`883bc81`) with the forward pass on the laptop's processor, **failed**. Arms T and C
and arm M seeds 1 and 2 matched exactly. Arm F seeds 0, 1 and 2 and arm M seed 0
differed by one or two of the 180 held-out episodes (largest gaps 0.0056, 0.0111,
0.0056 and 0.0056). As section 4 required, nothing else was fitted.

**Why (MEASURED).** The committed runs computed their forward passes on the laptop's
graphics processor (`"device": "mps"` in every `out-repairs/train_*.json`). Re-running
exactly `repairs.fit_reads` with the forward pass there (a scratch diagnostic, not
committed as output) reproduced the committed figures on **all twelve** arm-and-seed
pairs with a largest gap of 0. The weights are the committed ones. The CPU gaps are
floating-point differences between the two processors, which flip one or two
near-tied held-out predictions. They show up on arm F, where the read sits near
chance and many predictions are near ties.

**The change.** Every forward pass in this search runs on `mps`, as the committed
runs did. The fitting stays on the processor, unchanged. The identity check is run
again on `mps` and must pass on all twelve pairs, to within 1e-9, before anything
else is fitted. Nothing else in sections 1 to 6 changes. The failed processor-run
check stays on record in the findings.

---

## Amendment 2 (2026-09-26, ruled by John during the run; candidate 1 arm F seed 1 stopped part-way)

**Why.** The null of section 4 (100 shuffles at every one of the 60 site sets on
arm F) made each arm F seed take 5,493 seconds (about 92 minutes) for candidate 1.
Other jobs were loading the laptop at the same time (load average near 105 for
part of it). The null only matters at the best site, where the result is read.
John ruled the change below. Candidate 1 arm F seed 0 had finished under the old
plan. Its file is kept, renamed
`superseded_fit_own-turn-pair_F_seed0_every-site-100-shuffles.json`, and is not
used for any verdict. Seed 1 was stopped part-way and wrote nothing.

**The change.** For every candidate, the reference row and every arm:

- The straight-line read is still fitted, and scored on the held-out episodes, at
  **all 60 site sets**, exactly as before.
- The label-permutation null runs **only at the single best-fitting site set** of
  each arm and seed: the one with the highest held-out fit, ties going to the
  earlier site set in the rule's order. There it is **200 shuffles**, on every
  arm alike, replacing the 100 (arm F) and 20 (other arms).
- **Clearing on a seed** (section 5) now means: held-out fit at least 0.80 and
  above every one of the 200 shuffles at that arm and seed's best site set. For
  the best site set itself this is the old test. For any other site set it
  borrows the best site set's null. That rests on one observation, made before
  this amendment on the superseded arm F seed 0 file: across all 60 site sets the
  null's 95th percentile ran only from 0.056 to 0.067, and no single shuffle
  anywhere exceeded 0.10.
- Sections 2, 3 and 5 are otherwise unchanged. The stop rule still uses the 45
  fixed-extent site sets, and the verdict is still taken across all three seeds.
- Every seed is refitted from scratch under this rule, seed 0 included. The fits
  are deterministic, so seed 0's 60 fits come out the same as in the superseded
  file (checked when the findings are written).
