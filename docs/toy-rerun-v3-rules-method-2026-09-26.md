# The toy re-run under the version 3 rules — method, committed before any code or output

*Written 2026-09-26 (Pacific), on branch `worktree-w1d-toy-rerun-v3` from
`origin/main` at `62c3824`, by the Claude Code session commissioned as "MVM W1d
toy re-run under v3 rules". **UNREGISTERED.** Nothing here is a ruling and
nothing here registers anything. The five rule changes applied below were ruled
by John on 2026-09-26 against the Gate C review of version 2 of the successor
proposal
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`,
findings RT-212 to RT-216). No ruling file for them is on main at `62c3824`; the
session brief is the record of their wording, and it is quoted here. Where this
file had to choose how to turn a ruled sentence into code, it says so and marks
the choice ARGUED.*

*Order, as in the repairs session (method `docs/rehearsal-repairs-method-2026-09-25.md`,
then findings `docs/2026-09-26-rehearsal-repairs.md`): this file is committed
first, then the code, then the outputs, then the findings
(`docs/2026-09-26-toy-rerun-v3-rules.md`).*

*Laptop only, no network, no rented machine, **$0**. No arm is re-trained (§1).*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
Words (arm, transplant, whole-state, ownership-only, site set, nomination, the
chance-corrected reading, the learn-both gate) are as defined in section 0 of
the repairs method file and are not repeated here.*

---

## 1. The trained models, and the check that they are the committed ones

The repairs driver (`experiments/rehearsal-successor-measure/src/repairs.py`,
merged by pull request 52 at `882f252`) loads one trained model per arm and seed
from `out-repairs/ckpt_{arm}_base_seed{s}.pt`. **Those files were never
committed** (MEASURED: `git ls-files` lists no `.pt` file under
`experiments/rehearsal-successor-measure/` at `62c3824`). They survive, untracked,
on this laptop in the repairs session's worktree,
`~/Code/minimum-viable-mind/.claude/worktrees/w1c-rehearsal-repairs/experiments/rehearsal-successor-measure/out-repairs/`,
with timestamps matching the committed outputs. The re-run reads them from
there, in place, and records each file's SHA-256 in every output.

Because arms C, F and M do not reproduce from code and seed (the 2026-09-23
range-and-direction ruling), a retrained model would be a different model. So
before anything else, the code checks that these files are the models behind
the committed outputs. Pre-stated, all four must hold:

- **K1.** Every checkpoint loads into the driver's arm definition without a
  missing or unexpected weight.
- **K2.** The per-layer straight-line reads, refitted exactly as `fit_reads`
  does, give the same held-out fit accuracy at every layer as the committed
  `nominate_base_*.json` (`fit_accuracy.own`), to four decimals, and
  coefficients within 1e-4 of the committed `reads_*_base_seed*.npz` (largest
  absolute difference printed).
- **K3.** The learn-both gate, recomputed on the same 3,000 held-out development
  episodes, gives the committed `gate_base.json` correct counts on both
  conditions, exactly, for all twelve arm-and-seed runs.
- **K4.** The 44-site-set nomination, recomputed from this run's grid with the
  repairs rule unchanged, picks the committed nomination (position set, layer
  set, rank) on all twelve.

If any of K1 to K4 fails on an arm and seed, that arm and seed is reported as
"not the committed model" and is not re-trained here; the session says so and
stops short of a finding for it. If it holds, the committed reads
(`reads_*_base_seed*.npz`) are the ones used for every subspace, so the
ownership-only transplants are built from the same numbers the committed run
used.

## 2. What is re-run, and what is not

Re-run, on arms T, C, F and M, recipe `base`, seeds 0, 1 and 2, on the committed
trained models:

- the **nomination**, on the 600 development pairs the repairs run used
  (`make_data(600, seed=4242, pool="dev")`), own-directed condition;
- the **measure**, on the 800 fresh pairs the repairs run used
  (`make_data(800, seed=777, pool="fresh")`): the whole-state and ownership-only
  transplants, the untouched share, the chance-corrected reading and its
  whole-state floor (page 1c), exactly as `repairs.reading`;
- **control 3**, rebuilt under rule 2 below; control 7 (a null transplant leaves
  every output bit-identical) as a sanity check;
- the **gate**, recomputed (K3) and read under rule 5.

Not re-run, because none of the five rule changes touches them and the brief
does not ask for them: control 2 (ruled not applicable on arms T and M, and a
reported check on arms C and F, by the 2026-09-25 repairs ruling item 5),
controls 1 and 4 to 6, the page 3 rider, the oracle reading on arm T, and arm
M's route-by-route prediction. Their committed figures in `out-repairs/` stand
as they are.

Outputs go to a new directory, `experiments/rehearsal-successor-measure/out-v3-rules/`,
so nothing under `out-repairs/` is overwritten. The new code is a new file,
`src/rerun_v3.py`, which imports `repairs.py`'s helpers and leaves that file
exactly as merged.

## 3. The five rules as implemented

### 3.1 Rule 1 — the fit floor (RT-212)

Ruled: *the nomination's held-out fit accuracy of the ownership read goes in
every output and in the findings table. A read below four fifths on held-out
development episodes returns "no verdict, read failed its floor" for that arm
and seed. Also compute and report a label-permutation null for the fit (permute
the marker-word labels, refit, at least 200 permutations; report the 95th and
99th percentiles) beside the floor, not as the bar.*

- **The read** is the one the nomination uses: a straight-line read (logistic
  regression, `C=1.0`, `max_iter=3000`) of which marker word is the model's own,
  fitted at the own-directed action position at each layer on the first 70% of
  the 600 development recipients (420) and scored on the other 30% (180). This
  is `repairs.fit_reads` unchanged.
- **The nomination's fit accuracy** is the held-out fit accuracy at the
  nominated layer. *ARGUED:* when the nominated layer set has more than one
  layer, it is the **lowest** of those layers' fit accuracies, because the
  ownership-only transplant uses the read at every one of them and each must
  have found the label.
- **The floor**: a nomination whose fit accuracy is below 0.8 (fewer than 144
  of 180 held-out episodes) returns **"no verdict, read failed its floor"**.
- **The permutation null**: at every layer, for every arm and seed, the
  marker-word labels of all 600 recipients are shuffled, then split, fitted and
  scored exactly as the real read (so the held-out labels are shuffled too).
  **200 permutations** per layer, drawn from
  `numpy.random.default_rng([20260926, seed, layer])`, the same draws on every
  arm. Reported: the 95th and 99th percentiles (numpy's default, linear
  interpolation), the largest value, and the real fit's rank among them. Beside
  the floor, never as the bar.

### 3.2 Rule 2 — control 3 as a multi-draw null (RT-214)

Ruled: *twenty random subspaces of the same rank at the same sites per arm and
seed; the ownership-only transplant counts only if it beats the 95th percentile
of the twenty. Drop the 0.0175 room from control 3 only. Report control 3 for
all four arms including M.*

- On the fresh episodes, at the site set being read, 20 transplants each of a
  random subspace of the nominated rank at every nominated layer (draw `k` of 20
  from `numpy.random.default_rng([20260926, seed, k])`, a standard normal
  matrix orthonormalised as the driver's `transplant.orthonormal`; the same
  draws on every arm). Each gives a donor share.
- **Passes** when the ownership-only donor share is **strictly greater** than
  the 95th percentile of the 20 (numpy default, linear interpolation). There is
  no room term.
- Printed beside it, for continuity only: the committed single-draw control 3
  figure and the version 2 form (random donor share at or below untouched plus
  0.0175).
- Computed for all four arms, and at every row that is read (§4), not only the
  primary nomination.

*ARGUED, stated before the run.* As worded, rule 2 asks the ownership-only
transplant to move the action more than a random subspace does. On an arm
whose ownership is fully entangled (the high anchor, arm C), the ownership-only
transplant is expected to move the action no more than a random subspace, so
rule 2 will return "does not count" there whether or not the read found its
label. The committed run points that way (arm C's ownership-only shares 0.055 to
0.0567 on development episodes, against untouched about 0.05 on fresh). This
file applies the rule as worded and reports that consequence; it does not
reword the rule.

### 3.3 Rule 3 — the registered site-set rule (RT-215)

Ruled: *every contiguous layer set of the toy's five states times the four
named position sets (60 site sets), with the widened degenerate exclusion (any
set spanning every position at any layer), instead of the hand list of 44.
Report which nominations moved and the sensitivity row.*

- **Layer sets**: the 15 contiguous runs of the five states 0 to 4 (0 is the
  embedding's output, 1 to 4 the four blocks' outputs): (0), (1), (2), (3), (4),
  (0,1), (1,2), (2,3), (3,4), (0,1,2), (1,2,3), (2,3,4), (0,1,2,3), (1,2,3,4),
  (0,1,2,3,4).
- **Position sets**: `action`, `action+ans`, `action+3`, `post-identity`, as
  `transplant.position_mask` defines them.
- **The widened exclusion** is checked on the data, not assumed: a site set is
  excluded if its position set covers every position in any development
  episode. MEASURED while writing this file (a probe over the 600 development
  pairs): none of the four covers every position in any episode (`post-identity`
  starts at the model's first own turn, never the opening token, and ends at the
  action, never the closing one). So the family is **60 site sets × 4 rank caps
  = 240 comparisons** per arm and seed, and the code asserts it.
- **The nomination rule is the repairs rule unchanged** (repairs method §3.2,
  and the 2026-09-25 ruling item 4): the whole-state floor per site set;
  per position set, the smallest clearing layer set (fewest layers, then
  earliest); then the highest ownership-only share, ties to the lower rank, then
  the earlier position set.
- **"Which nominations moved"**: for each arm and seed, the 60-set nomination
  beside the committed 44-set nomination; moved if the position set, layer set
  or rank differs.
- **The rule 3 sensitivity row** is the committed 44-set nomination, re-read on
  the fresh episodes with every column of the table (fit accuracy, control 3
  null, reading), so a reader sees what the change of family did to the answer
  and not only to the site. *ARGUED:* this is the reading of "the sensitivity
  row" that the brief's table description gives ("rule 3's moved nominations").
  The repairs file's other sensitivity row (highest ownership-only share over
  every clearing site set, skipping the smallest-layer-set step) is also
  computed under the 60 sets and kept in the output file, not in the table.
- The grid is computed once over the union of both families (15 layer sets × 5
  position sets = 75 site sets, the "all" position set included only so that K4
  can recompute the committed 44-set nomination); the 60-set nomination never
  sees an "all" site set.

### 3.4 Rule 4 — layer 0 (RT-216)

Ruled: *a layer-0 nomination is allowed at the action position set only; at any
position set spanning the acting turns it is excluded and reported as "at the
acting channel's injection", no verdict. Also run and report the stricter
variant, layer 0 excluded at every position set, as a sensitivity row.*

- **A layer-0 nomination** is a nominated layer set that contains layer 0.
  *ARGUED:* a set such as (0,1) copies the injection as much as (0) does.
- **Primary, as ruled:** the 60-set nomination is made as in §3.3. If it
  contains layer 0 at any position set other than `action`, the arm and seed
  returns **"no verdict: at the acting channel's injection"**. *ARGUED, the
  reading of "excluded and reported":* the nomination is excluded from being a
  reading and reported with that label; the rule does not then go on to pick a
  different site set, because the ruling says the outcome is "no verdict". As
  an unruled column, kept in the output file, the code also records what the
  rule would pick if those layer-0 site sets were removed before choosing, so
  the other reading is visible.
- **Which position sets span the acting turns.** MEASURED while writing this
  file (the same probe): the twin episodes have identical tokens and differ only
  in the acting channel, which differs only on the model's own assignment turns.
  Only `post-identity` holds such a turn (in all 600 development episodes);
  `action`, `action+ans` and `action+3` lie inside the action turn, where the
  channel is on in both twins alike. The ruled wording allows layer 0 at
  `action` only, which is applied literally: layer 0 at `action+ans` and
  `action+3` is also "at the acting channel's injection". *ARGUED:* at those two
  the layer-0 states of the twins are identical, so a layer-0 whole-state
  transplant there cannot move anything and cannot clear the floor; the literal
  reading and the "differs between twins" reading therefore give the same
  nominations. The code checks this (the layer-0 whole-state donor share at
  those two sets equals the untouched share).

  > **Correction, added 2026-09-26 after the first pass's outputs (commit
  > `6f9428b`).** The sentence above, "at those two the layer-0 states of the
  > twins are identical, so a layer-0 whole-state transplant there cannot move
  > anything", is **wrong for arms T and M**. The check it names came back true
  > on arms C and F and false on arms T and M
  > (`out-v3-rules/nominate_{arm}_seed{s}.json`,
  > `layer0_whole_equals_untouched_inside_action_turn`). Arms T and M build their
  > ownership slot into the layer-0 state at every position from the acting
  > channel, so the twins differ there as well. It changed no nomination, because
  > none landed on layer 0 at `action+ans` or `action+3`. The sentence is left as
  > written, as the record of what was argued before the run.
- **The stricter variant (sensitivity row):** a nomination containing layer 0
  at any position set, `action` included, returns "no verdict: layer 0
  excluded". Its unruled "removed before choosing" column is recorded too.

### 3.5 Rule 5 — the gate (RT-213)

Ruled: *arms T, C and M are gated on the own-directed condition only; arm F
keeps learn-both. Report the gate verdict per arm under this rule.*

- The gate is recomputed from the models (K3) on the 3,000 held-out
  development episodes (`make_data(1500, seed=99, pool="dev")`); the bar is the
  ruled 790 of 3,000 on at least two seeds of three.
- Arms T, C and M **pass** if the own-directed condition clears on at least two
  of three seeds. Arm F **passes** if both conditions clear on at least two of
  three.
- An arm that fails its gate returns "no verdict: arm failed its gate" on every
  seed. Every other column is still computed and printed, so rule 1's and rule
  2's answers on that arm can be read on their own.

## 4. The rows and the order of verdicts

For each arm and seed, three rows are read on the fresh episodes, each with
every column:

1. **Primary**: the 60-set nomination, rules 1 to 5 applied.
2. **Rule 3 sensitivity**: the committed 44-set nomination, rules 1, 2, 4 and 5
   applied to it.
3. **Rule 4 stricter**: the primary nomination under the stricter layer-0 rule.

For each row, the verdicts, all printed, none short-circuiting the others:
gate (rule 5); nomination exists (some site set clears the whole-state floor on
development episodes); layer 0 (rule 4); fit floor (rule 1); the whole-state
floor on fresh episodes (page 1c, `repairs.reading`); control 3 (rule 2).
**"Reading"** is printed only when every one passes; otherwise **"no verdict"**
with every failing reason listed. The chance-corrected number is printed beside
it in every case, as the programme's page 2 requires.

## 5. What the findings file will say, and how

A table per arm and seed with: fit accuracy at the nominated layer(s),
permutation-null 95th and 99th percentiles there, floor verdict, the nominated
site set (layer set and position set, and rank), control 3 against its null,
and reading or no verdict; the two sensitivity rows; the gate per arm. It will
state plainly whether arm F returns no verdict on every seed under rule 1, and
whether arm M clears control 3 on all three seeds under rule 2. Every claim is
labelled MEASURED or ARGUED, and every figure cites its output file by path.
Arms C, F and M are reported as ranges across seeds and a direction, under the
2026-09-23 ruling; arm T's figures are exact where they reproduce.

## 6. Cost, and what this cannot do

Inference and small fits only: 75 site sets × 5 transplants on 600 episodes per
arm and seed, 3 rows × 22 transplants on 800 fresh episodes, and 12 × 5 × 200 =
12,000 small logistic fits for the permutation null. Estimated one to two hours
of laptop time, **$0**, no network.

It cannot say anything about the registered size, and it cannot make arms C, F
or M reproducible: it re-reads three particular trained models per arm, one per seed, which is
what the rules are about.

---

## 7. Addendum 2026-09-26: the second pass, committed before its code

*Added after the first pass's findings (commit `5276731`, pull request 62) and
before any second-pass code. John ruled three things on those findings on
2026-09-26, as relayed in this session's second brief. The first pass's rules,
as recorded in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` on main,
are otherwise unchanged. Same models, laptop only, $0.*

### 7.1 The three rulings, and how each is applied

1. **Control 3 is reported, not gated, on every arm.** The twenty-draw null of
   §3.2 is kept as it is. For each of the twelve arm-and-seed pairs, the table
   reports the null's median and 95th percentile (numpy default, linear
   interpolation) and where the ownership-only donor share sits in the
   distribution: how many of the twenty draws fall strictly below it, how many
   equal it, and how many fall above it. **No arm loses its reading on control
   3.** It is dropped from the verdict list of §4.
2. **Rule 4 means exclusion from the candidate family.** A site set whose layer
   set contains layer 0, at any position set other than `action`, is removed
   from the 60-set family before nomination, and the rule of §3.3 chooses again
   from what remains, the same way the degenerate all-positions exclusion works.
   That is the family the first pass already recorded as the unruled column
   `unruled_v60_with_layer0_injection_sets_removed_before_choosing`; it is now
   the **primary** nomination. The **stricter variant** (every site set
   containing layer 0 removed, `action` included, then choose again) is the
   first pass's `unruled_v60_with_every_layer0_set_removed_before_choosing`,
   kept as a sensitivity row. Because layer 0 can no longer be nominated at those
   sets, the "at the acting channel's injection" verdict can no longer occur.
3. **The fifteen trained models are committed** under
   `experiments/rehearsal-successor-measure/out-repairs/models/`: arms T, C, F,
   M and the ownership-blind arm, recipe `base`, seeds 0 to 2, copied byte for
   byte from the repairs worktree. The findings list each file's SHA-256, and
   the code checks it against the hash each first-pass output recorded.

### 7.2 What is computed, and from what

Every site set named in 7.1 was already read on the fresh episodes in the first
pass, by the same code, with its twenty random draws
(`out-v3-rules/measure_{arm}_seed{s}.json`, `rows.unruled_layer0_injection_removed`
and `rows.unruled_every_layer0_removed`). So the second pass is **pure
arithmetic on committed outputs**, with no new model runs: a new stage,
`--stage pass2`, in `src/rerun_v3.py`, which

- points the driver at the committed model files and checks that every file's
  SHA-256 equals the one the first-pass outputs recorded (if one differs, the
  stage stops);
- takes the primary and stricter site sets from the nomination files (and checks
  they are the ones the measure files read);
- applies the verdicts below and writes `out-v3-rules/pass2_table.md` and
  `out-v3-rules/pass2_summary.json`, leaving every first-pass file untouched.

### 7.3 The verdicts in the second pass

In this order, all printed, none short-circuiting the others: the gate (rule 5,
unchanged: arms T, C and M on the own-directed condition only, arm F on
learn-both); a nomination exists; the fit floor (rule 1, unchanged: the lowest
fit among the nominated layers is at least 0.8, with the permutation null
beside it); the whole-state four-fifths floor on fresh episodes. **Reading** if
all pass, otherwise **no verdict** with every failing reason. Control 3 is
printed beside it and decides nothing.

Also reported, from the readings: arm M's reading per seed, and whether all
three lie between 0.3 and 0.7 (the pass of the 2026-09-25 repairs ruling, item
2); arm C's reading per seed, and the separation figure per seed, arm C's
reading minus arm T's, against the 0.5 bar (page 1a of the Weekend 1 queue
ruling), computed only on a seed where both are readings.
