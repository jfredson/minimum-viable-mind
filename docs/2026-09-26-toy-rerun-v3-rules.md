# The toy re-run under the version 3 rules (RT-212 to RT-216) — findings

*Written 2026-09-26 (Pacific), on branch `worktree-w1d-toy-rerun-v3`, by the
Claude Code session commissioned as "MVM W1d toy re-run under v3 rules".
**UNREGISTERED.** Nothing here is a ruling. It applies the version 3 rules to the
toy's committed trained models and reports what they return.*

*This file has two parts. **Part 1** gives the results under the rules as they
now stand: the five rule changes John ruled on 2026-09-26 against the Gate C
review of version 2 (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`,
RT-212 to RT-216), as amended by **his three rulings of the same day on this
file's first pass**. Those three rulings: control 3 is reported, not gated;
rule 4 removes the layer-0 site sets from the candidate family before choosing;
and the trained models are committed. **Part 2** is the first pass exactly as
first written (commit `5276731`), kept as the record and superseded where Part
1 differs.*

*Commit order. First pass: method `dc7eee8`, code `392477b`, outputs `6f9428b`,
findings `5276731`. Second pass: method addendum and dated correction `6e23dc1`
(`docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7 and the note in
section 3.4); the models `a86783e`; code `7a01026` (`--stage pass2` in
`experiments/rehearsal-successor-measure/src/rerun_v3.py`); outputs `dc1de9e`;
then this revision. Laptop only, no network, no rented machine, **$0**. No arm
was retrained in either pass.*

*Every claim is labelled **MEASURED** (read off a committed output file, cited
by path) or **ARGUED** (reasoning from those numbers or from the code). Paths
are relative to `experiments/rehearsal-successor-measure/out-v3-rules/` unless
written in full. Arms C, F and M do not reproduce from code and seed
(`docs/rulings/2026-09-23-range-and-direction-only.md`). Their figures describe
these particular trained models, and are reported as a range and a direction,
not as a property of the code. Written under the workspace plain-language rule.*

---

# Part 1 — Results under the rulings as they now stand

## 1.0 The answer, briefly

MEASURED, `pass2_summary.json` and `pass2_table.md`.

- **Arm M reads 0.4886, 0.4860 and 0.5449 on seeds 0, 1 and 2. The pass line of
  0.3 to 0.7 is met on all three seeds** (`arm_M_pass.met_on_every_seed: true`).
- **Arm C reads 1.0051, 1.0025 and 1.0000 on seeds 0, 1 and 2.** Arm T reads
  0.0000 on every seed. So **the separation figure, arm C minus arm T, is
  1.0051, 1.0025 and 1.0000, and it clears the 0.5 bar on every seed**
  (`separation`).
- **Arm F returns no verdict on each seed: 0, 1 and 2.** On every seed it fails
  twice over. Its gate fails (the named-other condition is learned on 1 seed of
  3), and its read fails the floor: 0.172, 0.067 and 0.106 at the nominated
  layer, against 0.8 (`arm_F`).
- Arm T reads 0.0000 on all three seeds under the primary rule and under the
  stricter layer-0 variant. The stricter variant moves its site from layer 0 to
  layer 1, both at the action position.
- The stricter variant changes nothing on arms C, F or M. None of their primary
  nominations contains layer 0 once rule 4 removes the injection sets.

ARGUED: under the rules as they now stand, the toy reaches the proposal's first
result on its anchors. The separable anchor reads 0 and the entangled anchor
about 1, with separation on every seed. The fourth arm lands inside its
pre-stated band on every seed, and the free arm is correctly returned as "no
verdict" rather than as a reading.

## 1.1 The trained models: committed, and what rests on them

MEASURED. The fifteen models are committed under
`experiments/rehearsal-successor-measure/out-repairs/models/` (commit
`a86783e`). They were copied byte for byte from the repairs worktree, where they
had lived untracked since 2026-09-25. A narrow exception in `.gitignore` admits
them past the repository's blanket rule against `*.pt` files. The second-pass
code checked each file's SHA-256 against the hash the first pass recorded when
it read the models in place, and all twelve read models match
(`pass2_summary.json`, `model_sha256`). The first pass's checks K1 to K4 (Part
2, first pass §1) showed these are the models behind the committed repairs
outputs.

| file | SHA-256 |
|---|---|
| `ckpt_T_base_seed0.pt` | `b679bf6cd7884f28a137a6e6a669728213c085ba9cba5c9a2574b947885cfe68` |
| `ckpt_T_base_seed1.pt` | `1558acb2fce628335f28c3a29acef43fdf0d409151e1b5774d8e75aa7f489113` |
| `ckpt_T_base_seed2.pt` | `84f48372c995c7c53baa80d9379a3778bb8c1845e45589b743bd2b8c083c90c2` |
| `ckpt_C_base_seed0.pt` | `47326bb90c5f4ad03beacc74da1d33eec1fd4462314a2e9ce385c36a1e7ffeee` |
| `ckpt_C_base_seed1.pt` | `b3596f309e780e5820a7064ccb207a413a71be439170986b18479fe957e0af2a` |
| `ckpt_C_base_seed2.pt` | `2fc87d0454af22bc2d1c00b7247c220ff0705b8c2500005b47a9cb491ac202f0` |
| `ckpt_F_base_seed0.pt` | `c3afe0c6354f49f185b1806a433e6f0563b48a14f6e4559b2264ecb0abeea88d` |
| `ckpt_F_base_seed1.pt` | `2e51df7efd952e044b63702a5dc63c88e12de41ffe89c1b15c35892756cb219b` |
| `ckpt_F_base_seed2.pt` | `d5b59d8b8d32d42327beb4e6866107fe6e1167f4de1d0d73e3e201ed9d1683b1` |
| `ckpt_M_base_seed0.pt` | `e0f55d92d42bffdb3774cb267bbd8caf16f901fd3fa2f127e9989780188ceda2` |
| `ckpt_M_base_seed1.pt` | `d9b8010c9bec5ae20aaacabd38acd89497ef121599643a15d548ad44f688ecab` |
| `ckpt_M_base_seed2.pt` | `eeb3a7a43628791f1c85ac85d6108b74e89c0a209f1688c7342d864ce4926dba` |
| `ckpt_blind_base_seed0.pt` | `027f5ac0c78576e9263ad488ce18f0cb64070e5eeb89ff30e9a177294e25e162` |
| `ckpt_blind_base_seed1.pt` | `9b44cd386e6de0298a52355868652bdc9a9c0e3c3c4cd7af48485cc53ba9c3f5` |
| `ckpt_blind_base_seed2.pt` | `092393bdc1b488cfef7706a02804988bb4d672489bc0f332eada603d42f52ba6` |

**These files cannot be rebuilt from code and seed.** Retraining arms C, F or M
from the same code and seed gives a different model: the repairs check (pull
request 58) re-ran from clean and got different nominations. The toy results
listed below rest on these fifteen files and on nothing else.

**What rests on them.** The brief asked this file to say that *every*
committed toy result of 2026-09-25 and 2026-09-26 rests on these fifteen files.
That is not quite true, and this file says what is:

- **Rests on these files:** every base-recipe result of the rehearsal repairs
  in `experiments/rehearsal-successor-measure/out-repairs/`. That is
  `gate_base.json` (arms T, C, F, M and the ownership-blind arm),
  `nominate_base_*.json`, `measure_base_*.json`, `reads_*_base_*.npz` and
  `summary_base.json`, and the findings `docs/2026-09-26-rehearsal-repairs.md`
  built on them. It is also every file in `out-v3-rules/`, both passes, and this
  file.
- **Does not rest on these files:**
  - The two arm F training redesigns in `out-repairs/` (`gate_curriculum.json`,
    `gate_reweight.json`, and the curriculum and reweight rows of
    `diagnose_named_other.json`). They rest on six more models,
    `ckpt_F_curriculum_seed{0,1,2}.pt` and `ckpt_F_reweight_seed{0,1,2}.pt`,
    which are still untracked in the repairs worktree.
  - The grammar attempt, pull request 57 (`out-grammar-c/`). It rests on its own
    nine models, still untracked in the `w1c-grammar-attempt` worktree.
  - The repairs check, pull request 58. It retrained from clean, and this
    session did not look for its models.

ARGUED, for John: if the intent is that every toy result of the weekend has its
models on the record, those fifteen further files (about 75 MB) need the same
treatment. This session did not commit them, because the ruling named fifteen.

## 1.2 The gate (rule 5, unchanged from the first pass)

MEASURED, `gate.json`. Arms T, C and M are gated on the own-directed condition
only; arm F on both conditions. The bar is 790 of 3,000 on at least two seeds
of three.

| arm | own-directed clears | named-other clears | gate |
|---|---|---|---|
| T | 3 of 3 | 3 of 3 | passes |
| C | 3 of 3 | 0 of 3 | passes |
| F | 3 of 3 | 1 of 3 | **fails** |
| M | 3 of 3 | 3 of 3 | passes |

## 1.3 The findings table

MEASURED, `pass2_table.md` (rows `primary`), with the underlying figures in
`measure_{arm}_seed{s}.json` (`rows.unruled_layer0_injection_removed`, read on
the 800 fresh episode pairs in the first pass),
`nominate_{arm}_seed{s}.json` and `null_{arm}_seed{s}.json`.

- The **site set** is the 60-set rule's nomination after rule 4 removes every
  layer-0 site set at a position set other than `action`.
- **Fit** is the read's held-out accuracy (180 development episodes) at the
  nominated layer.
- **Null** is the 95th and 99th percentile of 200 label-shuffled fits at that
  layer, beside the 0.8 floor, not as the bar.
- **Control 3** is the median and 95th percentile of the twenty random
  subspaces' donor shares. It is followed by the ownership-only donor share and
  how many of the twenty draws fall below, equal and above it. It is reported
  only and decides nothing.
- The **reading** is `(whole − ownership-only) / (whole − untouched)`: 0 is
  separable, 1 is entangled.

| arm/seed | site set (layer, position set, rank) | fit | null 95th / 99th | fit floor | control 3: median / 95th; ownership-only (below / equal / above) | reading or verdict |
|---|---|---|---|---|---|---|
| T/0 | 0, action, 8 | 1.000 | 0.117 / 0.133 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| T/1 | 0, action, 8 | 1.000 | 0.117 / 0.128 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| T/2 | 0, action, 8 | 1.000 | 0.111 / 0.128 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| C/0 | 2, action, 8 | 1.000 | 0.111 / 0.122 | passes | 0.0587 / 0.0639; 0.0488 (0 / 0 / 20) | **1.0051** |
| C/1 | 4, action, 2 | 0.961 | 0.122 / 0.139 | passes | 0.0550 / 0.0613; 0.0475 (0 / 1 / 19) | **1.0025** |
| C/2 | 1, post-identity, 1 | 0.978 | 0.117 / 0.128 | passes | 0.0600 / 0.0653; 0.0600 (3 / 9 / 8) | **1.0000** |
| F/0 | 1, post-identity, 1 | 0.172 | 0.128 / 0.133 | **fails** | 0.0587 / 0.0625; 0.0587 (6 / 7 / 7) | no verdict: gate failed; read failed its floor (number 1.0000) |
| F/1 | 1, action+3, 4 | 0.067 | 0.117 / 0.122 | **fails** | 0.0587 / 0.0650; 0.0563 (2 / 1 / 17) | no verdict: gate failed; read failed its floor (number 1.0000) |
| F/2 | 1, post-identity, 8 | 0.106 | 0.117 / 0.133 | **fails** | 0.0638 / 0.0664; 0.0638 (8 / 3 / 9) | no verdict: gate failed; read failed its floor (number 1.0108) |
| M/0 | 1, post-identity, 8 | 1.000 | 0.122 / 0.139 | passes | 0.0150 / 0.0190; 0.4050 (20 / 0 / 0) | **0.4886** |
| M/1 | 1, post-identity, 8 | 1.000 | 0.117 / 0.139 | passes | 0.0187 / 0.0226; 0.4062 (20 / 0 / 0) | **0.4860** |
| M/2 | 1, post-identity, 8 | 1.000 | 0.117 / 0.144 | passes | 0.0150 / 0.0213; 0.3688 (20 / 0 / 0) | **0.5449** |

Every row clears the whole-state four-fifths floor on fresh episodes
(`reading.floor.clears`). Control 7 (copying the recipient's own states changes
no output, bit for bit) holds on all twelve (`measure_*_seed*.json`,
`control7_null_transplant_bit_identical`).

**The stricter layer-0 row** (every layer-0 site set removed at every position
set, then choose again). MEASURED, `pass2_table.md`, rows `stricter`. It
differs from the table above only on arm T. Arm T's site moves from layer 0 to
**layer 1 at the action position, rank 8**, with fit 1.000, control 3
(20 / 0 / 0) and reading **0.0000** on all three seeds. On arms C, F and M the
primary nominations contain no layer 0, so the stricter row is identical.

## 1.4 What the control 3 distribution shows, now that it is reported

MEASURED, `pass2_table.md`. ARGUED where marked.

- **Arms T and M:** the ownership-only transplant sits above all twenty random
  draws on every seed, by a wide margin (arm M about 0.37 to 0.41 against random
  medians of 0.015 to 0.019). The ownership subspace does something that random
  subspaces of its size do not.
- **Arm C:** the ownership-only transplant sits **below** all twenty draws on
  seeds 0 and 1 (0 / 0 / 20 and 0 / 1 / 19), and in the middle of them on seed 2
  (3 / 9 / 8). ARGUED: this is what an entangled arm should show. Its ownership
  subspace carries nothing that moves the action on its own, no more than a
  random subspace does. The first pass's gate turned this into "no verdict"
  (Part 2, first pass §7); reported and not gated, it is simply the evidence
  that goes with a reading near 1.
- **Arm F:** the ownership-only transplant sits in the middle of the random
  draws on every seed (6 / 7 / 7, 2 / 1 / 17, 8 / 3 / 9). ARGUED: this is
  consistent with a read that holds nothing. Arm F's verdict comes from its
  fit, not from control 3.

## 1.5 What changed from the first pass, and why

MEASURED, comparing Part 1 with Part 2.

- **Rule 4.** In the first pass a layer-0 nomination at `post-identity` gave no
  verdict (6 of 12). Removing those site sets and choosing again moves every one
  of the six off layer 0:
  - C/1: to layer 4 at the action position, rank 2;
  - C/2 and F/0: to layer 1 at post-identity, rank 1;
  - F/2, M/0 and M/2: to layer 1 at post-identity, rank 8.

  C/0, F/1 and arm T are unchanged. M/1 also moves, from layer 3 at action to layer 1 at post-identity. Removing
  site sets changes which layer set is smallest per position set, and so which
  candidate has the highest ownership-only share. Its reading barely changes
  (0.4846 to 0.4860).
- **Control 3.** In the first pass it removed arm C seeds 0 and 2 and every arm
  F seed. Reported instead of gated, it removes nothing.
- **The net effect.** In the first pass: readings on arm T (3 of 3) and arm M
  (1 of 3), none on C or F, no separation figure. In the second pass: readings
  on T, C and M on every seed, separation on every seed, arm M inside its band
  on every seed, and arm F no verdict on every seed.
- **Unchanged:** the models, the reads, the fit floor, the permutation null,
  the 60-site-set family, the gate, and every fresh-episode figure. The second
  pass is arithmetic on the first pass's outputs. Every site set it reports was
  read on the fresh episodes by the first pass's code (method §7.2).

## 1.6 Things a checker should know

- The second pass ran no model. `--stage pass2` checks the committed models'
  hashes, then takes the nominations from `nominate_*` and the fresh-episode
  figures from `measure_*`. It asserts that each measure row read the site set
  the nomination names.
- The first pass's notes (Part 2, first pass §9) still apply. The CPU and GPU
  refits differ on four of sixty layer fits by one or two held-out episodes.
  One of those four is now a nominated layer, F/2 layer 1: 0.1056 on the GPU
  (the table's figure, equal to the committed one), 0.1000 on the CPU. Both are
  far below 0.8. The T/0 and T/1 null logs were lost when those processes were
  relaunched; their results files are complete.
- The method file's sentence about layer-0 transplants inside the action turn
  was wrong for arms T and M. It now carries a dated correction (method §3.4),
  and is not deleted.

## 1.7 Files (second pass)

- Method addendum: `docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7;
  the dated correction in section 3.4.
- Models: `experiments/rehearsal-successor-measure/out-repairs/models/`
  (fifteen files, hashes in §1.1).
- Code: `experiments/rehearsal-successor-measure/src/rerun_v3.py`, `stage_pass2`.
- Outputs: `out-v3-rules/pass2_table.md`, `out-v3-rules/pass2_summary.json`,
  `out-v3-rules/logs/pass2.log`. Every first-pass output is unchanged.

---

# Part 2 — The first pass, as first written (commit `5276731`), superseded where Part 1 differs

*Kept as the record, unedited apart from heading levels. Its section references
(§0 to §10) point within this part. Its rule 4 is "no verdict at the
injection", and its control 3 gates the reading. John's rulings of 2026-09-26
replaced both (Part 1). Its §6.2 "unruled" column is what Part 1 now reports as
the primary row.*

### First pass §0. The answer, briefly

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

### First pass §1. The models: never committed, still on disk, confirmed as the committed ones

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

### First pass §2. The gate under rule 5 (RT-213)

MEASURED, `gate.json`, `verdicts`. The bar is 790 correct of 3,000 held-out
development episodes, on at least two seeds of three.

| arm | rule | own-directed clears | named-other clears | version 2 (learn-both) | **rule 5** |
|---|---|---|---|---|---|
| T | own-directed only | 3 of 3 (3000, 3000, 3000) | 3 of 3 | passes | **passes** |
| C | own-directed only | 3 of 3 (1711, 1703, 1727) | 0 of 3 (760, 751, 708) | fails | **passes** |
| F | learn-both | 3 of 3 (1679, 1654, 1664) | 1 of 3 (994, 781, 746) | fails | **fails** |
| M | own-directed only | 3 of 3 (2592, 2584, 2600) | 3 of 3 (1663, 1699, 1655) | passes | **passes** |

Rule 5 changes one verdict, arm C's, from fail to pass. Arm F still fails.

### First pass §3. The findings table

Per arm and seed, on the 800 fresh episode pairs. "Fit" is the read's held-out
accuracy on 180 development episodes at the nominated layer (method §3.1);
"null" is the 95th / 99th percentile of 200 label-permuted fits at that layer.
"Control 3" is the ownership-only donor share against the 95th percentile of
twenty random subspaces. "Number" is the chance-corrected figure,
`(whole − ownership-only) / (whole − untouched)`, printed whether or not it is a
reading (0 = separable, 1 = entangled). Source: `table.md`, `measure_*_seed*.json`
(`rows.primary`), `nominate_*_seed*.json`, `null_*_seed*.json`.

#### First pass §3.1 The primary row: all five rules

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

#### First pass §3.2 The two sensitivity rows

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

### First pass §4. Rule 1: the fit floor and its permutation null (RT-212)

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

### First pass §5. Rule 3: the registered site-set rule (RT-215)

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

### First pass §6. Rule 4: layer 0 (RT-216)

#### First pass §6.1 As ruled

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

#### First pass §6.2 The reading the ruling did not choose, for John

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

### First pass §7. Rule 2: control 3 as a twenty-draw null (RT-214)

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

### First pass §8. What this leaves, per arm

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

### First pass §9. Things a checker should know

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

### First pass §10. Files

- Method: `docs/toy-rerun-v3-rules-method-2026-09-26.md`
- Driver: `experiments/rehearsal-successor-measure/src/rerun_v3.py`
- Outputs, under `experiments/rehearsal-successor-measure/out-v3-rules/`:
  `gate.json` (rule 5, K3); `nominate_{arm}_seed{s}.json` (the 75-site-set grid,
  the 60- and 44-set nominations, the unruled picks, K2, K4, checkpoint hashes);
  `null_{arm}_seed{s}.json` (200 permuted fits per layer);
  `measure_{arm}_seed{s}.json` (every row, reading, control 3 with its twenty
  draws, verdict reasons, control 7); `table.md` and `summary.json` (assembled);
  `logs/`.
