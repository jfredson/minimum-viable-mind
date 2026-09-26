# The toy re-run under the version 3 rules (RT-212 to RT-216) — findings

*Written 2026-09-26 (Pacific), on branch `worktree-w1d-toy-rerun-v3`, by the
Claude Code session commissioned as "MVM W1d toy re-run under v3 rules".
**UNREGISTERED.** Nothing here is a ruling. It applies the five rule changes John
ruled on 2026-09-26 against the Gate C review of version 2 of the successor
proposal
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`,
findings RT-212 to RT-216) to the toy's committed trained models, and reports
what they return.*

*Order of commits on this branch: the method,
`docs/toy-rerun-v3-rules-method-2026-09-26.md` (`dc7eee8`); the code,
`experiments/rehearsal-successor-measure/src/rerun_v3.py` (`392477b`); the
outputs, `experiments/rehearsal-successor-measure/out-v3-rules/` (`6f9428b`);
then this file. Laptop only, no network, no rented machine, **$0**. No arm was
re-trained.*

*Every claim is labelled **MEASURED** (read off a committed output file, cited
by path) or **ARGUED** (reasoning from those numbers or from the code). Paths
below are relative to `experiments/rehearsal-successor-measure/out-v3-rules/`
unless written in full. Arms C, F and M do not reproduce from code and seed
(`docs/rulings/2026-09-23-range-and-direction-only.md`); their figures are
properties of these particular trained models, reported as a range and a
direction, not as properties of the code.*

*Written under the workspace plain-language rule.*

---

## 0. The answer, briefly

- **Arm F returns no verdict on every seed under rule 1.** MEASURED: the read's
  held-out fit at the nominated layer is 0.072, 0.067 and 0.072 on seeds 0, 1
  and 2, against a floor of 0.8 (`measure_F_seed{0,1,2}.json`,
  `rows.primary.verdict.fit_accuracy`). Its best fit at any layer on any seed is
  0.172. Arm F also fails its gate (rule 5), and on every seed it fails control 3
  (rule 2); on two seeds of three it also sits at the acting channel's injection
  (rule 4). Any one of these alone gives no verdict.
- **Arm M clears control 3 on all three seeds under rule 2.** MEASURED: its
  ownership-only transplant moves the action to the donor's value in 0.3925,
  0.3937 and 0.3775 of trials, against a 95th percentile of twenty random
  subspaces of 0.0151, 0.0701 and 0.0139 (`measure_M_seed{0,1,2}.json`,
  `rows.primary.control3`). Seed 1, which failed version 2's form of control 3,
  passes this one by a wide margin.
- **But arm M gets a reading on one seed of three, not three, once all five rules
  apply.** MEASURED: seeds 0 and 2 nominate layer 0 at the post-identity position
  set, which rule 4 reports as "at the acting channel's injection", no verdict.
  Seed 1 reads 0.4846. So the pass John folded arm M in on ("between 0.3 and 0.7
  on all three seeds") is **not met under the rules as ruled**. It is met under
  one reading of rule 4 that the ruling did not choose (§6.2).
- **Arm C returns no verdict on every seed.** Seeds 1 and 2 sit at the injection
  with a read at 0.072; seed 0 has a sound read (1.000 at layer 2) and fails only
  control 3, because its ownership-only transplant (0.0488) moves no more than a
  random one (95th percentile 0.0639). The method file predicted exactly this
  before the run (method §3.2): **rule 2 as worded cannot give a reading to an
  arm that is truly entangled**, whatever its read.
- **Arm T reads 0.0000 on all three seeds** under the primary rules, and returns
  no verdict on all three under rule 4's stricter variant, because its nomination
  is layer 0 at the action position.
- So under the five rules the toy gives readings on arm T (3 of 3) and arm M (1
  of 3) only. **The separation bar (arm C's reading minus arm T's, at least 0.5)
  cannot be computed on any seed.**

## 1. The models: never committed, still on disk, confirmed as the committed ones

MEASURED. The repairs driver's trained models (`ckpt_*_base_seed*.pt`) were never
committed: `git ls-files` lists no `.pt` file under
`experiments/rehearsal-successor-measure/` at `62c3824`. They survive, untracked,
in the repairs session's worktree on this laptop,
`~/Code/minimum-viable-mind/.claude/worktrees/w1c-rehearsal-repairs/experiments/rehearsal-successor-measure/out-repairs/`.
The re-run read them in place; each output records the file's SHA-256
(`nominate_*_seed*.json`, `checkpoint_sha256`).

Every pre-stated check held on all twelve arm-and-seed models (`summary.json`,
`checks`):

| check | what it compares | result |
|---|---|---|
| K1 | strict load into the arm definition | 12 of 12 load with no missing or unexpected weight |
| K2 | refitted reads against the committed `out-repairs/reads_*.npz` and fit accuracies | 12 of 12; largest coefficient difference **0.0**; fit accuracies equal at every layer (`nominate_*_seed*.json`, `K2`) |
| K3 | recomputed gate counts against `out-repairs/gate_base.json` | 12 of 12 equal, both conditions (`gate.json`, `K3`) |
| K4 | the 44-site-set nomination recomputed against the committed one | 12 of 12 pick the same position set, layer set and rank (`nominate_*_seed*.json`, `K4`) |
| extra | the committed nomination re-read on the fresh episodes against `out-repairs/measure_base_*.json` | 12 of 12 give the committed whole-state, ownership-only and untouched shares exactly |

So nothing was re-trained, and every figure below comes from the same models as
the committed repairs record. ARGUED, and a request for John: these fifteen
files are the only copies of models that cannot be reproduced from code and
seed. If the repairs worktree is cleaned up, they are gone. They are about 5 MB
each. Keeping them somewhere durable (not necessarily git) would protect every
toy result from this weekend.

## 2. The gate under rule 5 (RT-213)

MEASURED, `gate.json`, `verdicts`. The bar is 790 correct of 3,000 held-out
development episodes, on at least two seeds of three.

| arm | rule | own-directed clears | named-other clears | version 2 (learn-both) | **rule 5** |
|---|---|---|---|---|---|
| T | own-directed only | 3 of 3 (3000, 3000, 3000) | 3 of 3 | passes | **passes** |
| C | own-directed only | 3 of 3 (1711, 1703, 1727) | 0 of 3 (760, 751, 708) | fails | **passes** |
| F | learn-both | 3 of 3 (1679, 1654, 1664) | 1 of 3 (994, 781, 746) | fails | **fails** |
| M | own-directed only | 3 of 3 (2592, 2584, 2600) | 3 of 3 (1663, 1699, 1655) | passes | **passes** |

Rule 5 changes one verdict, arm C's, from fail to pass. Arm F still fails.

## 3. The findings table

Per arm and seed, on the 800 fresh episode pairs. "Fit" is the read's held-out
accuracy on 180 development episodes at the nominated layer (method §3.1);
"null" is the 95th / 99th percentile of 200 label-permuted fits at that layer.
"Control 3" is the ownership-only donor share against the 95th percentile of
twenty random subspaces. "Number" is the chance-corrected figure,
`(whole − ownership-only) / (whole − untouched)`, printed whether or not it is a
reading (0 = separable, 1 = entangled). Source: `table.md`, `measure_*_seed*.json`
(`rows.primary`), `nominate_*_seed*.json`, `null_*_seed*.json`.

### 3.1 The primary row: all five rules

| arm/seed | nominated site set | fit | null 95th / 99th | fit floor | control 3 | number | verdict |
|---|---|---|---|---|---|---|---|
| T/0 | layer 0, action, rank 8 | 1.000 | 0.117 / 0.133 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| T/1 | layer 0, action, rank 8 | 1.000 | 0.117 / 0.128 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| T/2 | layer 0, action, rank 8 | 1.000 | 0.111 / 0.128 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| C/0 | layer 2, action, rank 8 | 1.000 | 0.111 / 0.122 | passes | 0.0488 vs 0.0639: does not beat | 1.0051 | no verdict: control 3 |
| C/1 | layer 0, post-identity, rank 8 | 0.072 | 0.111 / 0.122 | **fails** | 0.0550 vs 0.0514: beats | 0.9863 | no verdict: injection; read failed its floor |
| C/2 | layer 0, post-identity, rank 2 | 0.072 | 0.111 / 0.128 | **fails** | 0.0600 vs 0.0625: does not beat | 1.0000 | no verdict: injection; floor; control 3 |
| F/0 | layer 0, post-identity, rank 2 | 0.072 | 0.117 / 0.122 | **fails** | 0.0575 vs 0.0588: does not beat | 1.0029 | no verdict: gate; injection; floor; control 3 |
| F/1 | layer 1, action+3, rank 4 | 0.067 | 0.117 / 0.122 | **fails** | 0.0563 vs 0.0650: does not beat | 1.0000 | no verdict: gate; floor; control 3 |
| F/2 | layer 0, post-identity, rank 1 | 0.072 | 0.111 / 0.128 | **fails** | 0.0688 vs 0.0712: does not beat | 1.0000 | no verdict: gate; injection; floor; control 3 |
| M/0 | layer 0, post-identity, rank 8 | 1.000 | 0.117 / 0.133 | passes | 0.3925 vs 0.0151: beats | 0.5105 | no verdict: at the acting channel's injection |
| M/1 | layer 3, action, rank 8 | 1.000 | 0.117 / 0.133 | passes | 0.3937 vs 0.0701: beats | 0.4846 | **reading** |
| M/2 | layer 0, post-identity, rank 8 | 1.000 | 0.111 / 0.128 | passes | 0.3775 vs 0.0139: beats | 0.5322 | no verdict: at the acting channel's injection |

Every row also passes the whole-state four-fifths floor on fresh episodes, and
control 7 (copying the recipient's own states changes no output, bit for bit)
holds on all twelve (`measure_*_seed*.json`,
`control7_null_transplant_bit_identical`).

### 3.2 The two sensitivity rows

**Rule 3's row: the committed 44-set nomination, re-read under rules 1, 2, 4
and 5.** It differs from the primary row only where the nomination moved, which
is arm C seeds 0 and 1 (§5). On the other ten it is the primary row exactly.

| arm/seed | 44-set nomination | fit | null 95th / 99th | control 3 | number | verdict |
|---|---|---|---|---|---|---|
| C/0 (moved) | layer 0, every position, rank 2 | 0.072 | 0.117 / 0.122 | 0.0525 vs 0.0513: beats | 0.9977 | no verdict: injection; read failed its floor |
| C/1 (moved) | layer 0, every position, rank 4 | 0.072 | 0.111 / 0.122 | 0.0525 vs 0.0512: beats | 0.9927 | no verdict: injection; read failed its floor |

(Both of these site sets are now excluded outright by the widened exclusion of
the 2026-09-25 repairs ruling, item 3; they are shown because the brief asks what
moved.)

**Rule 4's stricter row: layer 0 excluded at every position set, action
included.** It differs from the primary row only on arm T, whose three
nominations are layer 0 at the action position:

| arm/seed | site set | number | primary verdict | **stricter verdict** |
|---|---|---|---|---|
| T/0, T/1, T/2 | layer 0, action, rank 8 | 0.0000 | reading | **no verdict: layer 0 excluded** |
| every other arm and seed | as §3.1 | as §3.1 | as §3.1 | as §3.1 (the layer-0 reason is relabelled; nothing else changes) |

MEASURED, `measure_T_seed*.json`, `rows.stricter`. So under the stricter
variant, **no arm gets a reading on more than one seed**: arm T none, arm M one
(seed 1).

## 4. Rule 1: the fit floor and its permutation null (RT-212)

MEASURED, `null_*_seed*.json` and `nominate_*_seed*.json` (`fit_accuracy`).

- **The floor does what RT-212 asked.** It returns no verdict on every arm F
  seed and on the committed arm F reads, and it passes on the nominated read of
  every arm T and arm M seed (1.000 at every layer) and on arm C wherever arm C's
  nomination is off layer 0 (0.961 to 1.000 at layers 1 to 4). This is the
  closure test the review set out ("returns no verdict on the committed arm F
  reads and a reading on T, C and M"), met for T and M. For C the floor passes
  where the read sits at layers 1 to 4, but C gets no reading, for other reasons
  (§3.1).
- **The permutation null sits at about 0.11 to 0.12 (95th percentile) and 0.12
  to 0.14 (99th) at every layer of every arm.** With 12 marker words present
  among the 600 development episodes and 180 held out, that is the level a read
  reaches by chance.
- **On arm F the read finds something, just very little.** Arm F's fit beats the
  99th percentile of its null at some layers: seed 0 layer 1 (0.172 against
  0.133) and layer 2 (0.144 against 0.133), seed 2 layer 2 (0.139 against 0.122),
  seed 1 layer 3 (0.144 GPU refit / 0.133 CPU refit, against 0.133). ARGUED: so
  the permutation null alone, used as the bar, would have let arm F's read
  through at those layers. The floor at four fifths is what separates a read
  that has found the label (0.96 to 1.00) from one that has found a trace of it
  (at most 0.172). The ruling's choice to report the null beside the floor and
  not as the bar is borne out.
- **At layer 0 on arms C and F the fit is 0.072 on every seed, below the null's
  median.** ARGUED: at layer 0 the action position's state is the same in every
  episode on those arms (the mask token plus its position), so the read can only
  guess one word. A permuted read does better by chance because permuting varies
  which word is most common in each part of the split. Either way, the read at
  that site holds nothing.

## 5. Rule 3: the registered site-set rule (RT-215)

MEASURED, `nominate_*_seed*.json`.

- **The family is 60 site sets, 240 comparisons per arm and seed.** The widened
  exclusion removes none of the 60: none of the four named position sets covers
  every position in any of the 600 development episodes
  (`family.share_of_episodes_where_position_set_spans_every_position`: 0 for
  all four; 1 for "all", which is not in the 60).
- **Two nominations of twelve moved**, both on arm C, both away from an "every
  position" set that the new family no longer contains:
  - C/0: layer 0 at every position, rank 2 → **layer 2 at the action position,
    rank 8**;
  - C/1: layer 0 at every position, rank 4 → **layer 0 at post-identity, rank 8**.
- The other ten are unchanged. **None of the 24 site sets the hand list never
  ran (the multi-layer sets (0,1), (1,2), (2,3), (0,1,2), (1,2,3) and (0,1,2,3))
  was nominated.** ARGUED: this is because every smallest clearing layer set is
  a single layer, as the review expected.
- The new sets do change the repairs file's other sensitivity row (highest
  ownership-only share over every clearing set, skipping the smallest-layer-set
  step), which now picks a multi-layer set on five of twelve: C/1 (0,1,2), C/2
  (0,1), F/1 (1,2,3), M/0 (0,1) and M/2 (0,1)
  (`sensitivity_v60_highest_over_every_clearing_set`). It is kept in the output
  files, not the table.
- How many of the 60 site sets clear the whole-state floor on development
  episodes: arm T 60 of 60; arm C 51, 39, 51; arm F 42, 39, 42; arm M 42, 42, 42
  (`site_sets_clearing_of_60`).

## 6. Rule 4: layer 0 (RT-216)

### 6.1 As ruled

MEASURED, `measure_*_seed*.json`, `rows.primary.verdict.reasons`.

- **Six nominations of twelve are "at the acting channel's injection"**: C/1,
  C/2, F/0, F/2, M/0, M/2, all at layer 0 post-identity. That is the same six
  the review counted.
- **Three nominations are layer 0 at the action position and are allowed**: T/0,
  T/1, T/2. They are the whole of arm T's readings.
- **The method file's argument about layer 0 inside the action turn was half
  wrong**, and is corrected here. The method argued (ARGUED, method §3.4) that at
  the `action+ans` and `action+3` position sets the twins' layer-0 states are
  identical, so a layer-0 transplant there cannot move anything. The check shows
  this holds on arms C and F, and **not on arms T and M**
  (`layer0_whole_equals_untouched_inside_action_turn`: true on C and F, false on
  T and M). ARGUED: arms T and M build their ownership slot into the layer-0
  state at every position from the acting channel, so the twins differ there
  too. This changes no nomination, because no nomination is layer 0 at those two
  position sets. The literal ruling (layer 0 allowed at `action` only) was
  applied either way.

### 6.2 The reading the ruling did not choose, for John

The ruling says a layer-0 nomination at those position sets "is excluded and
reported as 'at the acting channel's injection', no verdict". The method
(§3.4) read that as: the arm and seed gets no verdict, and the rule does not go
on to choose a different site. The other possible reading is that those site
sets are removed from the family before choosing. The code recorded that second
reading as an unruled column (`rows.unruled_layer0_injection_removed`). MEASURED,
and not a result of the ruled rules:

| arm/seed | pick with those sets removed first | number | verdict under rules 1, 2, 5 |
|---|---|---|---|
| M/0 | layer 1, post-identity, rank 8 | 0.4886 | reading |
| M/1 | layer 1, post-identity, rank 8 | 0.4860 | reading |
| M/2 | layer 1, post-identity, rank 8 | 0.5449 | reading |
| C/0 to C/2 | layer 2 action / layer 4 action / layer 1 post-identity | 1.0051 / 1.0025 / 1.0000 | no verdict: control 3 on all three |
| F/0 to F/2 | layer 1 in each case | 1.0000 / 1.0000 / 1.0108 | no verdict: gate; floor; control 3 |
| T/0 to T/2 | unchanged (layer 0, action) | 0.0000 | reading |

ARGUED: under this second reading arm M gets readings of 0.486 to 0.545 on all
three seeds, all inside the pre-stated 0.3 to 0.7, one layer past the injection.
(M/1's pick changes too, from layer 3 action to layer 1 post-identity, because
removing sets changes which site set is smallest per position set; both give
about 0.49.) Arm M's ruled pass therefore turns on which reading of rule 4 is
meant. That is John's call, and this file does not make it. With every layer-0
set removed at every position (the stricter variant under the second reading,
`rows.unruled_every_layer0_removed`), arm T moves to layer 1 at the action
position and still reads 0.0000 on all three seeds, and arm M is as above.

## 7. Rule 2: control 3 as a twenty-draw null (RT-214)

MEASURED, `measure_*_seed*.json`, `rows.primary.control3`.

- **Arm M clears it on all three seeds**, by a wide margin (§0). On seed 1 the
  twenty random subspaces reach up to 0.0713 of trials (95th percentile 0.0701),
  so version 2's single random draw (0.05625, reproduced here exactly as
  `single_draw_as_repairs`) was not unusual for that site. Under version 2's
  form (random at most untouched plus 0.0175, i.e. 0.0350) seed 1 still fails
  (`version2_form_passes: false`). ARGUED: version 2's limit was too tight for a
  site where random subspaces move something. The multi-draw null measures what
  random subspaces do at that site, which is the point of RT-214.
- **Arm T clears it on all three seeds**: ownership-only 1.0000, and none of the
  twenty random subspaces moves anything (0.0000).
- **Arm F fails it on all three seeds**: ownership-only 0.0563 to 0.0688, never
  above the random 95th percentile (0.0588 to 0.0712).
- **Arm C fails it on seeds 0 and 2 and passes on seed 1 by 0.0036** (0.0550
  against 0.0514; about three trials of 800). ARGUED: seed 1's pass is noise, not
  evidence; its read at that site fits at 0.072.
- **The consequence the method stated before the run happened.** Arm C seed 0
  has a sound read (1.000 at layer 2), a whole-state transplant that clears its
  floor (0.5400 against untouched 0.0512), and an ownership-only transplant that
  moves the action no more than untouched does (0.0488). That is what an
  entangled arm is supposed to look like, and it is the only arm C seed that
  passes every other rule. Rule 2 as worded gives it no verdict, because it
  requires the ownership-only transplant to beat random subspaces, which an
  entangled arm's cannot do. ARGUED: as worded, rule 2 makes the high anchor
  unreadable by design. It fits a separable or partly separable arm (T, M), where
  the ownership-only transplant should move things. A form that suits both would
  compare against the random null in the direction the arm is expected to go, or
  would require the random subspaces to be inert rather than requiring the
  ownership subspace to beat them. That is a design question for John; nothing
  here rewords the rule.

## 8. What this leaves, per arm

| arm | gate (rule 5) | readings under all five rules | range of the chance-corrected number, all seeds | direction |
|---|---|---|---|---|
| T | passes | **3 of 3**: 0.0000 each (none under the stricter variant) | 0.0000 exactly | separable, as built |
| C | passes | **0 of 3** | 0.986 to 1.005 | entangled, as built, but no seed certifies it |
| F | fails | **0 of 3** | 1.000 to 1.003 | not a reading: the read finds no label (at most 0.172) |
| M | passes | **1 of 3** (seed 1: 0.4846) | 0.485 to 0.532 | partly separable, as built; 3 of 3 under the unruled reading of rule 4 (0.486 to 0.545) |

MEASURED from §3 and §6.2. ARGUED, what it means for version 3:

1. Under the rules as ruled, the toy does not reach the proposal's first result
   (every arm read and the separation bar met). Arm C, the high anchor, gets no
   reading on any seed, so the separation bar is not computable.
2. Two rules decide most of this, and neither is about the system being
   measured. Rule 2 blocks arm C's one clean seed, and rule 4's reading
   (no verdict, or remove and choose again) decides whether arm M passes. Both
   are wording questions that can be settled before Gate A at $0.
3. Rule 1 is the rule that works as intended on the toy: it retires arm F's
   empty reading and leaves the anchors alone.

## 9. Things a checker should know

- **The null stage's refit ran on the CPU, the nomination's on the GPU.** Four
  of the sixty per-layer fit accuracies differ between the two by one or two of
  180 held-out episodes: F/0 layer 1 (0.1722 GPU, 0.1778 CPU), F/1 layer 3
  (0.1444, 0.1333), F/2 layer 1 (0.1056, 0.1000) and M/0 layer 3 (0.9889,
  0.9944). MEASURED, comparing `nominate_*` `fit_accuracy` with `null_*`
  `layers.*.fit_accuracy`. The table uses the GPU figures, which equal the
  committed ones (K2). None is at a nominated layer that crosses 0.8. The
  permutation nulls were fitted on the CPU states.
- **The null for T/0 and T/1 was produced by a first pair of processes that ran
  too slowly and was stopped**. Their results files were complete and are kept.
  Their logs were not, because the combined logs were removed when the remaining
  ten arm-and-seed runs were relaunched one process each. The draws are seeded
  by seed and layer (method §3.1), so re-running `--stage null --arms T --seeds 0,1`
  reproduces them on the same machine.
- **Not re-run**: control 2, controls 1 and 4 to 6, the rider, the oracle and
  arm M's route prediction (method §2). Their committed figures in
  `out-repairs/` stand.
- **Wall time**: about 40 minutes of nomination on the GPU and about 30 minutes
  of permutation nulls in ten CPU processes, after a slow first attempt; $0.

## 10. Files

- Method: `docs/toy-rerun-v3-rules-method-2026-09-26.md`
- Driver: `experiments/rehearsal-successor-measure/src/rerun_v3.py`
- Outputs, under `experiments/rehearsal-successor-measure/out-v3-rules/`:
  `gate.json` (rule 5, K3); `nominate_{arm}_seed{s}.json` (the 75-site-set grid,
  the 60- and 44-set nominations, the unruled picks, K2, K4, checkpoint hashes);
  `null_{arm}_seed{s}.json` (200 permuted fits per layer);
  `measure_{arm}_seed{s}.json` (every row, reading, control 3 with its twenty
  draws, verdict reasons, control 7); `table.md` and `summary.json` (assembled);
  `logs/`.
