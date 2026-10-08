*This is file 27 of 33 of one review packet, pasted into a single conversation. It contains record 17 part 3 of 3 (the repairs to the rehearsal); record 18 part 1 of 2 (the toy re-run under version 3's rules). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 17 of 25, part 3 of 3 - the repairs to the rehearsal - `docs/2026-09-26-rehearsal-repairs.md` (complete file, 33,735 characters) =====
1. **Page 4 (d) applies**, with one sentence added: a curriculum and loss
   re-weighting also failed at toy scale, and both made the named-other condition
   worse. Whether to attempt redesign (c), a grammar change, is John's.
2. **The degenerate exclusion must cover every all-positions site set**, not
   only "every layer at every position" (§3).
3. **The site-list rule and the printed list must agree.** The rule gives 296
   on the toy and 1,816 on the registered model with the toy's position sets;
   the 176 is the hand list's (§3).
4. **"The smallest layer set that clears it" needs one reading in words**; the
   two readings disagree on 7 of 12 arm-and-seed pairs (§3).
5. **Control 2 as worded cannot be run on arms T and M, and gives no verdict on
   arms that have not learned the named-other condition** (§4).
6. **A chance-corrected reading above 1 is reported as observed** (§6.2).
7. **The rider stays in the reporting table**; on the toy it returns "no
   verdict" for every arm but T (§3).
8. **Arm M passed page 5's line**; folding it in is a page 5 and page 6 decision.

---

## 8. Where running it differed from planning it

1. **Two additions not pre-stated**, committed as code before their output in
   `81dc84d` and labelled so in the code: the named-other diagnostic (§2),
   written after the curriculum scored below one in four; and the sensitivity
   pick without all-positions sets (§3), written after arm C's nominations.
   Neither replaces a pre-stated quantity.
2. **The prediction's number was low** (§5): 0.42 to 0.43 predicted from the
   record, against 0.46 to 0.49 from the arm's own routes and 0.48 to 0.53
   measured. The band and the formula check held.
3. **The ownership-blind solver was trained on three seeds, not one** as on
   2026-09-21; the extra two cost nothing but time.
4. **`gate_base.json` was written twice**: once early on arms T and F only, then
   on every arm. The committed file is the second; its arm T and F rows match
   the first, which were quoted in this session's chat before the second run.
5. **Laptop time**: 21 training runs, 5.68 hours of training summed across them
   (`train_*.json`), in two parallel streams of 9,161 and 11,307 seconds of wall
   time (the local training logs, which are not committed). Within the four to
   six hours the method note estimated. $0.

---

## 9. What still needs John

| decision | what this session found | where |
|---|---|---|
| Whether to attempt page 4's redesign (c), a grammar change, or to let (d) stand | both training redesigns failed; the evidence points at the grammar giving both action turns the same acting signal | §2 |
| Whether arm M is folded into the main registration (page 5, with page 6's envelope, $32 to $44 for three runs) | it passed the pre-stated line on all three seeds | §5 |
| Widening the degenerate-set exclusion to every all-positions site set | the ruled exclusion let the rule pick a degenerate set on arm C | §3 |
| Which reading of "the smallest layer set that clears it" is registered | the two disagree on 7 of 12 pairs | §3 |
| How control 2 is worded, or recorded as not applicable on arms T and M | as worded it returns no verdict on three arms of four | §4 |
| The rented slice (page 9), unchanged | not touched by this session; its go has not been given | ruling page 9 |

Nothing here is ruled. The pairing rule applies: this file is checked by a
session that did not write it, on the checker prompt in
`docs/weekend-1-session-prompts.md`, section (c).
===== END OF RECORD 17, part 3 =====

===== RECORD 18 of 25, part 1 of 2 - the toy re-run under version 3's rules - `docs/2026-09-26-toy-rerun-v3-rules.md` (complete file, 39,408 characters) =====
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
and the trained models are committed. John later changed the third: the models
are committed by the rulings session at commit `235c385`, not on this branch
(§1.1). **Part 2** is the first pass exactly as
first written (commit `5276731`), kept as the record and superseded where Part
1 differs.*

*Commit order. First pass: method `dc7eee8`, code `392477b`, outputs `6f9428b`,
findings `5276731`. Second pass: method addendum and dated correction `6e23dc1`
(`docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7 and the note in
section 3.4); the models `a86783e`; code `7a01026` (`--stage pass2` in
`experiments/rehearsal-successor-measure/src/rerun_v3.py`); outputs `dc1de9e`;
findings `f24d77a`. Then, after John's change to step 3: method note `29e9751`;
the models removed from this branch again `caa6ec3` (history not rewritten; the
pull request's net change carries no model files); code `8471a50`
(`--stage sums`); output `ed81fd3`; then this revision. Laptop only, no network, no rented machine, **$0**. No arm
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

**Where the models are.** The fifteen models are committed by the rulings
session, not by this branch: **commit `235c385`** on branch
`w1d-toy-models-committed`, at
**`experiments/rehearsal-successor-measure/out-repairs/models/`**, with a
`SHA256SUMS` list and a `README.md`. The commit was made under item 3 of
"Refinements 2026-09-26, after the toy re-run" in
`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, and its pull request
was being opened as this was written. This branch had briefly committed its own
copy at the same path (`a86783e`). By John's change it removed that copy again
in a new commit (`caa6ec3`) rather than rewriting pushed history. The pull
request's net change therefore carries no model files, and does not collide
with `235c385`.

**The two records agree.** MEASURED, `models_sha256_check.json`
(`all_agree: true`), written by `--stage sums` in
`experiments/rehearsal-successor-measure/src/rerun_v3.py` from `235c385`'s
`SHA256SUMS`. For every model this session read, three hashes are compared:

- the hash the first pass recorded when it read the file in place in the repairs
  worktree (`nominate_*_seed*.json`, `checkpoint_sha256`; the first pass did not
  read the three blind-arm models);
- the hash the second pass recorded when it read the copy
  (`pass2_summary.json`, `model_sha256`);
- the line for that file in `235c385`'s `SHA256SUMS`.

All fifteen agree. The list has fifteen entries and no file this session did
not read. The first pass's checks K1 to K4 (Part 2, first pass §1) showed that
these are the models behind the committed repairs outputs.

| file | SHA-256 (this session's reads = `235c385` `SHA256SUMS`) |
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
treatment. The `235c385` README lists the same gaps under "Not here".

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

- The second pass ran no model. `--stage pass2` checks the models' hashes (it
  ran while this branch still held its own copy, which `--stage sums` later
  showed is byte-identical to `235c385`'s), then takes the nominations from `nominate_*` and the fresh-episode
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

- Method addendum: `docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7,
  with the dated change to item 3; the dated correction in section 3.4.
- Models: commit `235c385` (branch `w1d-toy-models-committed`),
  `experiments/rehearsal-successor-measure/out-repairs/models/`, with its
  `SHA256SUMS` and `README.md`; hashes in §1.1. Not on this branch.
- Code: `experiments/rehearsal-successor-measure/src/rerun_v3.py`, `stage_pass2`
  and `stage_sums`.
- Outputs: `out-v3-rules/pass2_table.md`, `out-v3-rules/pass2_summary.json`,
  `out-v3-rules/models_sha256_check.json`, `out-v3-rules/logs/pass2.log`,
  `out-v3-rules/logs/sums.log`. Every first-pass output is unchanged.

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

===== END OF RECORD 18, part 1 =====

