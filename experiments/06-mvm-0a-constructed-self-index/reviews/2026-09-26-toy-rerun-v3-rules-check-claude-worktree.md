# Check of the toy re-run under the version 3 rules — commit order, the models, the figures recomputed, and the rules read against the rulings

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1d toy re-run
check", on branch `worktree-w1d-toy-rerun-v3-check`, cut from `origin/main` at
`4bb5727` (the merge of the Gate C rulings' refinements, pull request 63).*

*This session did not write what it checks. The target is pull request 62,
"Toy re-run under the version 3 rules", written by the session "MVM W1d toy
re-run under v3 rules". Its branch is `worktree-w1d-toy-rerun-v3` at its tip,
commit `a71e833`. Its method is `docs/toy-rerun-v3-rules-method-2026-09-26.md`,
its findings `docs/2026-09-26-toy-rerun-v3-rules.md` (Part 1 the second pass,
Part 2 the first pass as first written at `5276731`), and its outputs
`experiments/rehearsal-successor-measure/out-v3-rules/`, all on that branch and
none on main. Every path below that starts `out-v3-rules/` means that folder at
`a71e833`. No file on that branch was modified.*

*The rulings it is checked against are
`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` as it now stands on
main: the rulings on the Gate C review's findings RT-212 to RT-229 (pull
request 60, merge `3af189d`) and the section "Refinements 2026-09-26, after the
toy re-run" (pull request 63, merge `4bb5727`). The trained models are checked
against the models commit, `235c385`, on branch `w1d-toy-models-committed`
(pull request 64, still open).*

*Three details of the brief did not match the repository, and this file uses
what the repository shows. The branch is `worktree-w1d-toy-rerun-v3`, not
`worktree-w1d-toy-rerun-v3-rules`. Its tip is `a71e833`; `caa6ec3` is the
commit that removed the branch's own copy of the models, three commits back.
And `235c385` is not on the rulings session's pull request. The refinements
were merged as pull request 63, and `235c385` is the models commit on pull
request 64, whose parent is `4bb5727`.*

*Every finding is labelled **MEASURED** (a command was run on the committed
files and its output is printed in the appendix) or **ARGUED** (reasoning a
reader can dispute), with the file it rests on. No model was loaded and nothing
was retrained: every figure is recomputed from the committed JSON outputs.
Laptop only, nothing rented, **$0**. Written under the workspace plain-language
rule.*

## Verdict

- **Commit order holds on both passes.** MEASURED, section 1. First pass:
  method, then code two minutes later, then outputs an hour after that, then
  findings. Second pass: method addendum, then code, then outputs, then
  findings, and again for the model-fingerprint check. **The second pass is,
  as it claims, arithmetic on the first pass's outputs.** Its new code loads no
  model and runs no transplant. It reads the committed JSON and applies the
  refined verdicts. No first-pass output changed after it was committed.
- **But the two rule choices of the second pass were made with their outcomes
  already on the record.** ARGUED, section 1.3. The first pass's findings
  printed exactly what the "remove and choose again" reading of the layer-0
  rule, and control 3 without a gate, would return. John's refinements chose
  both after that. The order of commits is clean. The honest description for
  version 3 is "clarified after the first pass, with its figures in hand", not
  "pre-stated".
- **The models are the models.** MEASURED, section 2. This check hashed the
  fifteen files stored at `235c385` itself, and they match that commit's
  fingerprint list, `models_sha256_check.json`, both passes' recorded
  fingerprints, and the findings' table: fifteen of fifteen. The branch's own
  short-lived copy (`a86783e`) holds the identical files. The findings'
  statement of what rests on these files is right in substance. It leaves out
  three small things: the training records and one set of diagnostic rows that
  also rest on them, and one 2026-09-25 result, the rented-machine timing run,
  which rests on another model.
- **Every figure the brief names reproduces exactly from the committed
  outputs.** MEASURED, section 3. Gate verdicts, fit accuracies and the floor
  on all twelve arm-and-seed pairs; **arm F no verdict on every seed** (fit 0.172,
  0.067, 0.106 at the nominated layer; best anywhere 0.172); all twelve
  nominations re-picked from the raw grid of transplant results; arm M 0.4886,
  0.4860, 0.5449, all inside 0.3 to 0.7; arm C 1.0051, 1.0025, 1.0000 against
  arm T's 0.0000, so separation 1.0051, 1.0025, 1.0000; control 3's median,
  95th percentile and below / equal / above counts on all twelve pairs; and the
  stricter layer-0 row. Nothing disagrees.
- **Four small errors in the findings, none moving a verdict.** MEASURED,
  section 3.8. Two of the four layer fits that differ between the laptop's
  processor and its graphics chip sit at a nominated layer, not one. The
  control 7 sanity check was run at the first pass's site sets, seven of which
  are no longer nominated. The log files listed among the outputs are not
  committed. And the list of what rests on the models misses the items above.
- **The five rules match the rulings they implement, with one wording
  difference that turns out not to matter.** MEASURED and ARGUED, section 4.
  The method quoted the session brief, because the ruling file reached main
  thirteen seconds before the method was committed on a branch cut earlier.
  Set against the ruling's words, rules 1, 2, 3 and 5 match. Rule 4 drops the
  ruling's list of which position sets "span the acting turns" (post-identity,
  and any set including the marked turns). In its place it reads "at the action
  position set only" literally, which also removes layer 0 at the two other
  position sets inside the action turn. MEASURED: under the narrower reading
  every one of the twelve nominations is the same.
- **The first pass's reading of "excluded" as "no verdict" was a fair
  reading of the sentence as written, but not the stronger reading of the
  ruling as a whole.** ARGUED, section 4.6. The sentence's subject is "a
  layer-0 nomination", which is "excluded ... and reported as ..., no
  verdict". Against that, every earlier use of "excluded" in these rulings
  means removed from the candidate list before choosing, and the same ruling's
  item 3 speaks of the stricter variant "moving" arm T's read to another layer,
  which only happens if the rule chooses again. The first pass handled the
  ambiguity well: it recorded the other reading as its own column, before the
  run, and put the choice to John.
- **The corrected sentence about layer 0 inside the action turn is right on
  arms T and M.** MEASURED and ARGUED from the code, section 5. Arms T and M
  append the ownership vector, a running count of the model's own earlier
  turns, to the layer-0 state at every position, so the twins differ there. A
  layer-0 whole-state copy at those two position sets moves the action on
  every T seed (1.000 against 0.000 untouched) and on every M seed (about 0.40
  against about 0.015). The correction's closing clause, that this "changed no
  nomination", is true, but for two different reasons. On arm M those sets
  miss the four-fifths floor. On arm T they clear it and tie with the action
  position, and the action position wins only on the tie-break order.
- **The refinements' own text has one wrong clause, for John.** MEASURED,
  section 6. Refinement item 2 says that under the "remove and choose again"
  reading "arms C and F still fall to the fit floor". Arm C does not. Its fit
  is 1.000, 0.961 and 0.978 at the re-chosen layers, and it gets a reading on
  every seed. Only arm F falls to the fit floor. The ruling file should carry
  an annotation. Nothing ruled depends on the clause.

---

## 0. Words used here, once

- **Arm**: one of four small trained models. **Arm T** is built so the answer
  to "whose value do I act on?" sits in one separate slot (separable, reads 0).
  **Arm C** mixes that answer into everything (entangled, reads near 1).
  **Arm F**, the free arm, is trained with no such construction. **Arm M**
  sends some actions through arm T's route and some through arm C's, so it
  should read in the middle.
- **Twins**: the donor and recipient episodes of a transplant. Their text is
  identical and they differ only in the acting channel, the input that marks
  which turns are the model's own.
- **Transplant**: copying part of the model's running internal state from the
  donor into the recipient and seeing whether the action follows the donor.
  **Whole-state** copies everything at the chosen places; **ownership-only**
  copies only the directions a straight-line read picked out as carrying
  "which agent is me".
- **The reading**: (whole-state share − ownership-only share) ÷ (whole-state
  share − untouched share). 0 is separable and 1 is entangled; it can sit a
  little above 1 when the ownership-only copy moves less than nothing at all.
- **Site set**: a choice of layers and token positions to transplant at.
  **Nomination**: the rule that picks one site set and a rank (how many
  directions) per arm and seed, from development episodes. Layer 0 is the
  state straight after the input embedding, where the acting channel is added.
- **Fit**: how often the straight-line read names the model's own marker
  word correctly on 180 held-out development episodes. The **fit floor** is
  four fifths (0.8).
- **Control 3**: twenty ownership-only-sized copies along random directions at
  the same site, to see whether the ownership directions do more than any
  directions of that size would.
- **First pass / second pass**: the re-run's two rounds. The first applied the
  five rules as ruled; the second applied John's three refinements to the
  first's outputs.

---

## 1. Commit order, and whether the second pass was arithmetic

### 1.1 The order

MEASURED, `git log --reverse --format='%h %ad %s' --date=iso --name-status origin/main..a71e833`
(files abbreviated):

| commit | time (2026-09-26, Pacific) | what it adds |
|---|---|---|
| `dc7eee8` | 07:34:45 | first-pass method, `docs/toy-rerun-v3-rules-method-2026-09-26.md` |
| `392477b` | 07:36:46 | first-pass code, `src/rerun_v3.py` |
| `6f9428b` | 08:39:11 | first-pass outputs, 39 files in `out-v3-rules/` |
| `5276731` | 08:41:18 | first-pass findings |
| `6e23dc1` | 09:38:46 | second-pass method addendum (section 7) and the dated correction in section 3.4 |
| `a86783e` | 09:39:33 | the fifteen models, on this branch |
| `7a01026` | 09:40:17 | second-pass code (`--stage pass2`) |
| `dc1de9e` | 09:41:03 | second-pass outputs, `pass2_summary.json`, `pass2_table.md` |
| `f24d77a` | 09:43:04 | second-pass findings |
| `29e9751` | 09:57:01 | method note: the models are not committed here |
| `caa6ec3` | 09:57:12 | the fifteen models removed from the branch again |
| `8471a50` | 09:57:46 | code for the fingerprint check (`--stage sums`) |
| `ed81fd3` | 09:58:02 | its output, `models_sha256_check.json` |
| `a71e833` | 09:59:07 | findings revised to cite the models at `235c385` |

Method before code, code before output, output before findings, on the first
pass, the second pass, and the fingerprint-check round. The findings' own
statement of this order (findings, preamble) matches the log exactly.

Two timing notes, both MEASURED. The rulings file reached main at 07:34:32
(`3af189d`), thirteen seconds before the method was committed on a branch cut
from `62c3824`, so the method's sentence "No ruling file for them is on main
at `62c3824`" is true, and its rule wording comes from the session brief
(section 4 compares it with the ruling). The refinements were committed at
09:38:12 on their own branch (`c9a0389`) and merged at 09:39:32 (`4bb5727`), so
the second pass's method addendum (09:38:46) followed John's rulings and did
not follow their merge. That is the right way round.

### 1.2 What the second pass's code changed

MEASURED, `git diff 392477b 7a01026` and `git diff 7a01026 8471a50` on
`src/rerun_v3.py` (124 and 48 lines added, 4 and 4 removed):

- **One line reachable by the first pass's stages changed:** the models'
  folder, from the repairs worktree's untracked copy to
  `out-repairs/models/`. The first-pass stages were not re-run after it.
  `git diff --stat 6f9428b a71e833 -- out-v3-rules/` shows only three files
  added (`pass2_summary.json`, `pass2_table.md`, `models_sha256_check.json`)
  and no first-pass file changed.
- **`stage_pass2`** loads no model. It hashes each model file and stops if a
  fingerprint differs from the first pass's record. It then reads
  `nominate_*`, `null_*`, `measure_*` and `gate.json`, asserts that each
  measure row read the site set the nomination names, and applies the
  second-pass verdicts: gate, nomination exists, fit floor, whole-state floor
  on fresh episodes. Control 3 is reported beside them as median, 95th
  percentile, and draws below, equal and above. The layer-0 "injection" reason
  is gone because the primary site set now comes from the first pass's
  "removed before choosing" column.
- **`stage_sums`** reads no model either. It compares three fingerprint
  records per file against the models commit's `SHA256SUMS`.

ARGUED: the only verdict-moving changes are the two the refinements ruled
(control 3 no longer gates; the primary site set is the removed-before-choosing
pick). Both act on numbers the first pass had already computed on fresh
episodes (`measure_*`, rows `unruled_layer0_injection_removed` and
`unruled_every_layer0_removed`). Section 3 recomputes every verdict
independently of this code and gets the same answer.

### 1.3 A caveat on what "pre-stated" can mean here

ARGUED. The commit order is clean, but the second pass's two rule choices were
not made blind. The first pass's findings (Part 2, sections 6.2 and 7) printed
what the "remove and choose again" reading returns (arm M inside its band on
all three seeds) and what control 3 does to arm C (blocks its one clean seed).
John then chose both. Two things weigh against calling that tuning:

- Both problems were **stated before the first pass ran**. The method argued
  in section 3.2 that control 3, as worded, "will return 'does not count'"
  on an entangled arm "whether or not the read found its label". Section 3.4
  committed to recording the removed-before-choosing column. Both are in
  `dc7eee8`, before any output.
- The reason recorded for refinement item 1 is a design reason (a one-way
  control cannot pass a separable and an entangled arm alike), not a result.

Version 3 should still describe these as clarifications made after the toy
re-run with its figures in hand. It should not call them pre-stated.

---

## 2. The models

### 2.1 The fingerprints

MEASURED, `check_models.py` (appendix A, output in appendix D). For each of the
fifteen `.pt` files at
`235c385:experiments/rehearsal-successor-measure/out-repairs/models/`, this
check computed the SHA-256 of the stored file itself (`git cat-file blob`, piped
through `hashlib.sha256`) and compared it with:

1. that commit's `SHA256SUMS`: 15 of 15 equal;
2. `out-v3-rules/models_sha256_check.json`, all three recorded fields
   (`models_commit_list`, `second_pass_read`, `first_pass_read`): 15 of 15
   equal (the first-pass field is empty for the three blind-arm files, which
   the first pass did not read), `all_agree: true`, `entries_in_list: 15`, no
   file in the list the session did not read;
3. the first pass's `checkpoint_sha256` in every `nominate_{arm}_seed{s}.json`
   and `measure_{arm}_seed{s}.json`: 12 of 12 equal;
4. `pass2_summary.json`, `model_sha256`: 15 of 15 equal;
5. the table in findings section 1.1: 15 of 15 equal.

The branch's own copy at `a86783e` has the same fifteen stored files (the same
git file identifiers) as `235c385`. So the second pass, which ran against the
branch copy, read byte-for-byte the files now in pull request 64.

That the first pass read the models behind the committed repairs outputs rests
on its checks K1 to K4 (`summary.json`, `checks`; findings Part 2, section 1).
This check did not re-run them, since that needs the models loaded. It
confirmed only that the re-run's gate counts (`out-v3-rules/gate.json`, `runs`)
equal `out-repairs/gate_base.json` on main: 12 of 12 pairs, both conditions
(appendix G).

ARGUED, for whoever merges: `235c385` is on an open pull request (64). Until it
merges, a reader of main cannot open the models the re-run cites.

### 2.2 What rests on them

The findings (section 1.1) say every base-recipe result of the repairs rests on
these fifteen files: `gate_base.json`, `nominate_base_*`, `measure_base_*`,
`reads_*_base_*.npz`, `summary_base.json` and the repairs findings. So does all
of `out-v3-rules/`. They list as resting elsewhere: the two arm F training
redesigns (six models), the grammar attempt (nine models, pull request 57), and
the repairs check (pull request 58, retrained from clean).

MEASURED, listing `out-repairs/` and `out/` on main and the commits since
2026-09-24 that touch `experiments/`:

- **Right:** the exceptions named are real. `gate_curriculum.json`,
  `gate_reweight.json` and the `F/curriculum/*` and `F/reweight/*` rows of
  `diagnose_named_other.json` come from the six redesign models. The grammar
  attempt's `train_{C,F,T}_base_seed{0,1,2}.json` in `out-grammar-c/` show nine
  models. The repairs check committed only its review file, so its figures
  rest on models of its own that were never committed.
- **Missing from "rests on these files"** (minor): the training records
  `out-repairs/train_{T,C,F,M,blind}_base_seed*.json`, and the `F/base/*` rows
  of `diagnose_named_other.json`. Both describe these same fifteen models.
- **Missing from "does not rest on these files"** (minor): the second rented-machine
  run of 2026-09-25 (pull request 51, `9f802db`). It trained its own toy model on the
  rented machine and committed only its checksum
  (`out/rented-slice-2026-09-25-attempt-2/model-md5.txt`). Its result is a
  timing figure (seconds per step), not a measure reading. ARGUED: that is
  why it was probably left out, but it is a committed 2026-09-25 result on a
  model that is not on the record.
- **Not assessed:** the route (b) label search on arm F exists only as a local
  branch (`w1d-free-arm-label-search`, outputs committed at 10:09, after these
  findings) and is not on the remote.

---

## 3. The figures, recomputed from the committed outputs

MEASURED, `recompute.py` (appendix B, output in appendix E). It reads only
`out-v3-rules/` at `a71e833`. It recomputes each quantity from the rawest
committed number available, and it shares no code with `rerun_v3.py`. It
re-applies the repairs driver's four-fifths floor to every one of the 300 grid
entries per arm and seed. It re-picks each nomination from the grid by the
ruled rule, re-derives the null percentiles from the 200 stored shuffled fits,
recomputes the reading from its three shares, and recomputes control 3's
statistics from the twenty stored random shares. It then compares all of this
with `pass2_summary.json`. **No disagreement was found anywhere** (`PROBLEMS:
none`).

### 3.1 The gate

From `gate.json`, `runs`, against 790 of 3,000 on at least two seeds of three
(queue ruling page 1b; RT-213 item 1, own-directed only on T, C and M):

| arm | own-directed correct | named-other correct | rule | gate |
|---|---|---|---|---|
| T | 3000, 3000, 3000 | 3000, 3000, 3000 | own-directed only | passes |
| C | 1711, 1703, 1727 | 760, 751, 708 | own-directed only | passes |
| F | 1679, 1654, 1664 | 994, 781, 746 | learn-both | **fails** (named-other 1 of 3) |
| M | 2592, 2584, 2600 | 1663, 1699, 1655 | own-directed only | passes |

### 3.2 Fit and the fit floor, per arm and seed

At the second pass's nominated layer, from `nominate_*` `fit_accuracy`, with
the null percentiles recomputed from `null_*` `layers.*.null`:

| arm/seed | layer | fit | null 95th / 99th | floor 0.8 |
|---|---|---|---|---|
| T/0, T/1, T/2 | 0 | 1.000, 1.000, 1.000 | 0.117/0.133, 0.117/0.128, 0.111/0.128 | passes |
| C/0 | 2 | 1.000 | 0.111 / 0.122 | passes |
| C/1 | 4 | 0.961 | 0.122 / 0.139 | passes |
| C/2 | 1 | 0.978 | 0.117 / 0.128 | passes |
| F/0 | 1 | 0.172 | 0.128 / 0.133 | **fails** |
| F/1 | 1 | 0.067 | 0.117 / 0.122 | **fails** |
| F/2 | 1 | 0.106 | 0.117 / 0.133 | **fails** |
| M/0, M/1, M/2 | 1 | 1.000, 1.000, 1.000 | 0.122/0.139, 0.117/0.139, 0.117/0.144 | passes |

**Arm F is no verdict on every seed under the four-fifths floor.** Its best fit
at any layer on any seed is 0.172 (`nominate_F_seed0.json`, layer 1). It also
fails its gate. The lowest fit among the nominated reads on arms T, C and M is
0.961. So RT-212 item 1's closing test ("the floor returns no verdict on the
committed arm F reads and a reading on T, C and M") is met in the second pass.
It was met only for T and M in the first pass.

### 3.3 The nominations

Re-picked from the 300 grid entries per pair (15 contiguous layer sets × 5
position sets × 4 ranks), family = the 60 site sets on the four named position
sets, with every site set whose layers include 0 removed at any position set
other than `action`, then the repairs rule (smallest clearing layer set per
position set; highest ownership-only share; ties to the lower rank, then the
earlier position set):

| arm/seed | first pass (60 sets, no removal) | second pass (primary) | stricter (every layer-0 set removed) |
|---|---|---|---|
| T/0–2 | 0, action, 8 | 0, action, 8 | **1**, action, 8 |
| C/0 | 2, action, 8 | 2, action, 8 | same |
| C/1 | 0, post-identity, 8 | 4, action, 2 | same |
| C/2 | 0, post-identity, 2 | 1, post-identity, 1 | same |
| F/0 | 0, post-identity, 2 | 1, post-identity, 1 | same |
| F/1 | 1, action+3, 4 | 1, action+3, 4 | same |
| F/2 | 0, post-identity, 1 | 1, post-identity, 8 | same |
| M/0 | 0, post-identity, 8 | 1, post-identity, 8 | same |
| M/1 | 3, action, 8 | 1, post-identity, 8 | same |
| M/2 | 0, post-identity, 8 | 1, post-identity, 8 | same |

All 36 picks equal the recorded ones (`nomination_v60`,
`unruled_v60_with_layer0_injection_sets_removed_before_choosing`,
`unruled_v60_with_every_layer0_set_removed_before_choosing`), and each measure
row read the site set its nomination names. The recorded floor verdict equals
the recomputed one on all 3,600 grid entries. The site sets clearing the floor,
of 60: T 60, 60, 60; C 51, 39, 51; F 42, 39, 42; M 42, 42, 42, as the first
pass printed.

### 3.4 Arm M

Readings, recomputed from `measure_M_seed{0,1,2}.json`, row
`unruled_layer0_injection_removed`: **0.4886, 0.4860, 0.5449**, every one
inside **0.3 to 0.7** (the repairs ruling's item 2 pass line). Gate passes, fit
1.000, whole-state floor cleared on fresh episodes. `pass2_summary.json`
agrees (`arm_M_pass.met_on_every_seed: true`).

### 3.5 Arm C and the separation figure

Arm C, same row: **1.0051, 1.0025, 1.0000**, each a reading (gate passes, fit
passes, whole-state floor cleared). Arm T: 0.0000 on every seed. Separation (C
minus T): **1.0051, 1.0025, 1.0000**, each clearing 0.5 (queue ruling page 1a).
`pass2_summary.json` `separation` agrees.

### 3.6 Control 3, all twelve pairs

Recomputed from the twenty stored `random_donor_shares` and the
`ownership_only` share at the primary site set (numpy median; 95th percentile
by numpy's default, linear interpolation):

| arm/seed | random median | random 95th | ownership-only | draws below / equal / above it |
|---|---|---|---|---|
| T/0 | 0.0000 | 0.0000 | 1.0000 | 20 / 0 / 0 |
| T/1 | 0.0000 | 0.0000 | 1.0000 | 20 / 0 / 0 |
| T/2 | 0.0000 | 0.0000 | 1.0000 | 20 / 0 / 0 |
| C/0 | 0.0587 | 0.0639 | 0.0488 | 0 / 0 / 20 |
| C/1 | 0.0550 | 0.0613 | 0.0475 | 0 / 1 / 19 |
| C/2 | 0.0600 | 0.0653 | 0.0600 | 3 / 9 / 8 |
| F/0 | 0.0587 | 0.0625 | 0.0587 | 6 / 7 / 7 |
| F/1 | 0.0587 | 0.0650 | 0.0563 | 2 / 1 / 17 |
| F/2 | 0.0638 | 0.0664 | 0.0638 | 8 / 3 / 9 |
| M/0 | 0.0150 | 0.0190 | 0.4050 | 20 / 0 / 0 |
| M/1 | 0.0187 | 0.0226 | 0.4062 | 20 / 0 / 0 |
| M/2 | 0.0150 | 0.0213 | 0.3688 | 20 / 0 / 0 |

Every cell equals the findings' table (section 1.3) and `pass2_summary.json`.
ARGUED: the many ties (C/2 has nine draws equal to the ownership-only share)
are expected, since every share is a whole number of trials out of 800.

### 3.7 The stricter layer-0 row

Recomputed from row `unruled_every_layer0_removed`: identical to the primary
row except on arm T, whose site moves from layer 0 to **layer 1 at the action
position, rank 8**, with fit 1.000, control 3 at 20 / 0 / 0 and reading
**0.0000** on all three seeds. On arms C, F and M the primary picks hold no
layer 0, so the row is the same pick with the same numbers. This matches
findings section 1.3.

### 3.8 Errors found in the findings (none moves a verdict)

1. **"One of those four is now a nominated layer, F/2 layer 1"** (findings
   section 1.6). MEASURED: the four layer fits where the processor's refit and
   the graphics chip's refit disagree are F/0 layer 1 (0.1722 against 0.1778),
   F/1 layer 3, F/2 layer 1 (0.1056 against 0.1000) and M/0 layer 3. **F/0
   layer 1 is also a second-pass nominated layer.** So two of the four are
   nominated, not one. Both are far below 0.8 either way.
2. **"Control 7 ... holds on all twelve"** (findings section 1.3), cited to
   `measure_*_seed*.json`. MEASURED from `rerun_v3.py` lines 451–457: control
   7 was run only at the first pass's primary site set. Seven of the twelve
   second-pass site sets differ from those (C/1, C/2, F/0, F/2, M/0, M/1,
   M/2). ARGUED: copying a model's own states back into itself should be a
   no-op at any site, so this is a citation gap rather than a doubt. The
   sentence should say where control 7 was run.
3. **The log files listed as outputs are not committed** (findings sections
   1.7 and Part 2 section 10: `out-v3-rules/logs/pass2.log`, `sums.log`,
   `logs/`). MEASURED: `git ls-tree -r a71e833` has no `out-v3-rules/logs/`
   path, and `.gitignore` excludes `*.log` outside `a3-gates/` directories.
4. **The list of what rests on the models** is incomplete in the small ways
   set out in section 2.2.

---

## 4. The five rules against the rulings

The method's rules (section 3) quote the session brief, not the ruling file
(section 1.1 above). Each is set against the ruling's own words here, with the
second pass's reading (method section 7.1) against the refinements.

### 4.1 Rule 1, the fit floor — ruling RT-212, items 1 and 2

| ruling (words) | method | match |
|---|---|---|
| "The nomination's held-out fit accuracy on development episodes goes in the reporting table" | "goes in every output and in the findings table" | yes |
| "a read that misses a pre-stated floor returns no verdict on that arm. The floor is absolute: four fifths on held-out development episodes" | "A read below four fifths on held-out development episodes returns 'no verdict, read failed its floor' for that arm and seed" | yes; "for that arm and seed" is the method's, see below |
| "The label-permutation null ... is reported beside it, not used as the bar" | "report a label-permutation null ... beside the floor, not as the bar", 200 shuffles, 95th and 99th percentiles | yes; the count and percentiles are the brief's additions, not contrary to the ruling |
| item 2: "no verdict, read failed its floor" | the same label | yes, word for word |

ARGUED: applying the floor per seed where the ruling says "on that arm" is an
interpretation. It is moot here, because each arm passes or fails on all three
seeds alike. Taking the lowest fit across a multi-layer nomination (method
section 3.1, marked ARGUED) is also moot: no nomination in either pass has
more than one layer.

### 4.2 Rule 2, control 3 — ruling RT-214, items 1 and 2, and refinement 1

| ruling (words) | method | match |
|---|---|---|
| "many random subspaces of the same rank at the same sites (twenty at toy scale)" | "twenty random subspaces of the same rank at the same sites per arm and seed" | yes |
| "the reading counts only if the ownership-only transplant beats the 95th percentile of the random draws" | "the ownership-only transplant counts only if it beats the 95th percentile of the twenty"; code: strictly greater | yes in effect: the code withholds the reading. "Beats" as strictly greater is the plain sense |
| "The fixed 0.0175 room in control 3 is dropped" | "Drop the 0.0175 room from control 3 only" | yes |
| item 2: "re-run on all four arms ... and reported for all four" | "Report control 3 for all four arms including M" | yes |
| refinement 1: "reported, not gated, on every arm ... its distribution and the ownership-only transplant's place in it go in the reporting table" | method 7.1 item 1: median, 95th percentile, draws below / equal / above; "decides nothing" | yes |

### 4.3 Rule 3, the site-set rule — ruling RT-215 and the repairs ruling, item 3

| ruling (words) | method | match |
|---|---|---|
| "every contiguous layer set times four position sets ... gives 60 on the toy" | "every contiguous layer set of the toy's five states times the four named position sets (60 site sets)" | yes; MEASURED 60 in every `nominate_*` (`family.site_sets`) |
| repairs item 3: "any site set that spans every position at any layer is excluded" | "the widened degenerate exclusion (any set spanning every position at any layer)", checked on the data | yes; MEASURED none of the four spans every position in any episode (`family.share_of_episodes_where_position_set_spans_every_position`) |
| "If any nomination moves to a multi-layer set the hand list never tried, version 3 reports it and the sensitivity row from the new run" | "Report which nominations moved and the sensitivity row" | the condition did not fire. MEASURED: no nomination in either pass is multi-layer |

ARGUED: the ruling's "the sensitivity row" most naturally means the repairs'
own sensitivity row (the highest ownership-only share over every clearing
set). The method instead put the old 44-set nomination re-read in the table,
and reported the repairs-style row in prose (first pass section 5: a
multi-layer pick on five of twelve). Since the condition did not fire, this
leaves nothing undone. Version 3 should name which row it means.

### 4.4 Rule 4, layer 0 — ruling RT-216, items 1 and 3, and refinement 2

The ruling, item 1, in full: "Layer 0 stays a candidate at the action position
set only, where the constructed anchors' slot sits by construction. A layer-0
nomination at any position set spanning the acting turns (post-identity, and
any set including the marked turns) is excluded by rule, written into section
7.2, and reported as 'at the acting channel's injection', no verdict."

The method's quote: "a layer-0 nomination is allowed at the action position set
only; at any position set spanning the acting turns it is excluded and reported
as 'at the acting channel's injection', no verdict."

- **What was dropped:** the parenthesis naming the sets that span the acting
  turns ("post-identity, and any set including the marked turns"), and the
  reason clause. MEASURED by the method's own probe: only post-identity holds
  one of the model's own assignment turns. So the ruling's two sentences
  disagree about `action+ans` and `action+3`. The first sentence removes
  layer 0 there ("action position set only"); the second names only
  post-identity.
- **What the method did:** it applied the first sentence literally, so both
  passes removed layer 0 at every position set other than `action`, and said
  so (method section 3.4, marked ARGUED). Refinement 2 speaks of "position
  sets spanning the acting turns", and the second pass kept the literal
  reading (method 7.1 item 2: "at any position set other than `action`").
- **Does it matter?** MEASURED, `alt.py` (appendix C, output in appendix F):
  with layer 0 removed at post-identity only, all twelve second-pass
  nominations are the same, and so are all twelve first-pass nominations.
  Section 5 gives the reason per arm.

Item 3 ("the stricter variant, layer 0 excluded everywhere, as a sensitivity
row") matches the method's stricter row, and the second pass's form of it
(remove, then choose again) matches refinement 2's reading.

### 4.5 Rule 5, the gate — ruling RT-213, item 1

| ruling (words) | method | match |
|---|---|---|
| "The constructed arms T, C and M are gated on the own-directed condition only; arm F keeps the learn-both gate" | "arms T, C and M are gated on the own-directed condition only; arm F keeps learn-both" | yes, word for word apart from "the ... gate" |
| "the bar itself is unchanged" | 790 of 3,000 on at least two seeds of three | yes; queue ruling page 1b gives "at least two seeds of three", and RT-213 quotes the bar as 790 |

### 4.6 Was "excluded" as "no verdict" a fair reading of the ruling as then written?

ARGUED. **Yes as a reading of the sentence; no as the best reading of the
ruling.**

For the first pass's reading:

- The sentence's subject is "a layer-0 nomination", not a site set. A
  nomination only exists after the rule has chosen, and the sentence goes on
  to say what is reported for it: "'at the acting channel's injection', no
  verdict". Read on its own, that describes a verdict on an arm and seed. It
  does not describe a candidate removed from the list.
- The first pass did not hide the choice. The method committed, before any
  output, to recording the other reading as its own column (method section
  3.4). The findings put both readings side by side and said the choice was
  John's (Part 2, section 6.2).

Against it:

- Everywhere else in these rulings, "excluded" is said of site sets and means
  removed from the list before choosing: page 1c's "excluded by name", page
  1e's "the degenerate all-sites set excluded", and repairs item 3's "any site
  set that spans every position at any layer is excluded". Refinement 2 appeals
  to exactly this ("as the degenerate all-positions exclusion works").
- The same ruling's item 3 gives as its reason for not ruling the stricter
  variant blind that "it may move arm T's anchor read off the layer its slot
  was built at". A read only moves off a layer if the rule chooses again.
  Under the first pass's reading, the stricter variant leaves arm T with no
  verdict, not moved. The first pass did not cite this sentence.

So refinement 2's word "clarified" is fair. The ruling already leaned toward
"remove and choose again", and the first pass's reading was a defensible
literal one that it correctly surfaced rather than settled.

---

## 5. The corrected sentence on layer 0 inside the action turn

The method's original sentence (section 3.4): at `action+ans` and `action+3`
"the layer-0 states of the twins are identical, so a layer-0 whole-state
transplant there cannot move anything and cannot clear the floor". The dated
correction (added in `6e23dc1`) says this "is wrong for arms T and M", that the
check came back true on C and F and false on T and M, that "Arms T and M build
their ownership slot into the layer-0 state at every position from the acting
channel, so the twins differ there as well", and that it "changed no
nomination, because none landed on layer 0 at `action+ans` or `action+3`".

**The check.** MEASURED, `nominate_*` field
`layer0_whole_equals_untouched_inside_action_turn`: true at both position sets
on every C and F seed, false at both on every T and M seed. As the correction
says.

**The mechanism.** MEASURED from the code on main. In `src/arms.py`,
`_own_vec` (lines 156–164) builds the ownership vector at every position from a
running count, over the assignment turns, of where the acting channel fired.
For arm T, `running` (lines 190–194) appends that vector to the layer-0 state
at every position. In `src/arm_middle.py`, `forward` (lines 106–115) does the
same for arm M (line 114, `torch.cat([x, own_vec], dim=-1)`, before the layer-0 hook).
Inside the action turn that running count reflects the model's own earlier
turns, which is exactly where the twins differ. On arm C the ownership vector
enters layer 0 only at the value positions (`_embed`, lines 166–175) and later
through the blocks; arm F has no such term. So at the action turn, arm C's and
arm F's layer-0 states hold only the token, the position and the acting-channel
vector, which are the same in both twins. **The correction is right on arms T
and M, and its explanation is right.** ARGUED, one refinement of wording: the
twins differ at layer 0 through the running count of earlier turns, not
through the acting channel at those positions, where it is on in both twins
alike.

**Its size.** MEASURED, `alt.py` (appendix F), layer 0 at `action+ans` and at
`action+3` (identical figures at the two):

- arm T: whole-state share 1.000 against 0.000 untouched on every seed; it
  clears the floor at every rank; ownership-only 1.000 at rank 8;
- arm M: whole-state share 0.397, 0.398, 0.393 against 0.015, 0.017, 0.012
  untouched; the floor needs about 0.67 to 0.70; **it does not clear**.

**"It changed no nomination."** True, and more strongly than the correction
says. Under the literal rule the sets were never candidates, so nothing could
land on them. And even under the narrower reading that keeps them (section
4.4), no nomination changes. The reasons differ by arm:

- **arm M:** layer 0 inside the action turn misses the four-fifths floor, so
  it is never a candidate;
- **arm T:** layer 0 at `action+ans` and `action+3` clears the floor with an
  ownership-only share of 1.000 at rank 8, tying layer 0 at `action`. The
  `action` position set wins **only on the tie-break order** (the earlier
  position set in the repairs driver's list).

ARGUED: the original sentence's premise failed, but the conclusion it
protected (the literal and the narrower readings give the same nominations)
holds on this toy. On arm T it holds by a tie-break, not by construction.
Version 3's section 7.2 should not repeat the original argument. It should say
that on the separable arms layer 0 inside the action turn does move the
action, and that the rule's position-set order decides the tie on arm T.

---

## 6. For John: one clause of the refinements to annotate

Refinement 2 reads: "Under that reading arm M reads on all three seeds (0.486
to 0.545 on the re-run's first pass; re-run findings, section 6.2), so the
fold-in pass stands; **arms C and F still fall to the fit floor**."

MEASURED (section 3.2): under that reading arm C's fit is **1.000, 0.961 and
0.978** at its re-chosen layers (2, 4 and 1), all above 0.8. Arm C gets a
reading on every seed. In the first pass's column for that reading, arm C was
stopped by **control 3**, not the fit floor (findings Part 2, section 6.2:
"no verdict: control 3 on all three"). Only arm F falls to the fit floor, on
every seed.

ARGUED: the clause is probably carried over from the first pass's ruled
reading, where C/1 and C/2 did fail the fit floor at layer 0 post-identity (fit
0.072). No ruled choice depends on it: refinement 1 already removes control 3
as a gate, and Part 1 of the findings reports arm C correctly. But the rulings
file is the record version 3 will cite. It should carry a dated annotation
beside refinement 2, in the way the repairs ruling was annotated after its
check: under the remove-and-choose-again reading arm C passes the fit floor on
all three seeds and reads 1.0051, 1.0025 and 1.0000; only arm F falls to the
fit floor.

---

## 7. What was opened, and what was not

- **Opened:** `git log` and `git diff` of every commit on pull request 62; the
  method and findings at `a71e833` and the first-pass findings at `5276731`;
  `src/rerun_v3.py` at `a71e833`; all 42 files of `out-v3-rules/` at
  `a71e833`; the ruling file on main at `4bb5727`; the queue ruling and the
  repairs ruling on main; the fifteen model files, `SHA256SUMS` and `README.md`
  at `235c385`; the fifteen at `a86783e`; `src/arms.py`, `src/arm_middle.py`,
  `src/transplant.py` and `src/repairs.py` on main; `out-repairs/` and `out/`
  listings on main.
- **Not done:** no model was loaded, so checks K1, K2 and K4 (strict load,
  refitted reads, the 44-set nomination) and every fresh-episode share are
  taken from the committed files, not re-derived. No permutation fit was
  re-run. The first pass's Part 2 claims beyond those the brief named (for
  example the old 44-set rule-3 sensitivity figures 0.9977 and 0.9927, and arm
  F's layers that beat the 99th percentile of its null) were not re-checked.
- **Not written:** nothing on branch `worktree-w1d-toy-rerun-v3` or
  `w1d-toy-models-committed` was touched. This file is the only change on
  this branch.
- **The repository's own checks on this file.** MEASURED,
  `scripts/check_citations.py --scope nocopies --only <this file>`: 30
  references to files not on main. Every one is a file on pull request 62's
  branch (the method, the findings, `rerun_v3.py`, `out-v3-rules/`), the models
  path on pull request 64, the uncommitted `logs/` that section 3.8 reports,
  or one of this check's three scripts (`check_models.py`, `recompute.py`,
  `alt.py`), which are printed in the appendix and not committed. 0 figures
  absent from the file their sentence cites. `scripts/check_single_source.py
  --only <this file>`: 0 confident findings, 0 unsourced figures.

---

## Appendix

*Scripts were run from this worktree with the repository's Python
environment (`~/Code/minimum-viable-mind/.venv/bin/python`, numpy 2.5.0) on
a copy of `a71e833`'s files extracted with `git archive`. Output is verbatim.*

### A. `check_models.py` (section 2.1)

```python
import hashlib, json, subprocess, os
T = "/Users/john/.claude/jobs/faa2f7d5/tmp"
O = T + "/b/experiments/rehearsal-successor-measure/out-v3-rules"
def tree(c):
    out = subprocess.check_output(["git", "ls-tree", c, "experiments/rehearsal-successor-measure/out-repairs/models/"], text=True)
    return {l.split("\t")[1].split("/")[-1]: l.split()[2] for l in out.splitlines()}
t235, ta86 = tree("235c385"), tree("a86783e")
pts = sorted(k for k in t235 if k.endswith(".pt"))
print("pt files at 235c385:", len(pts), "| a86783e same blob ids:", all(t235[k] == ta86.get(k) for k in pts), len(ta86))
sums = dict((l.split()[1], l.split()[0]) for l in open(T + "/SHA256SUMS") if l.strip())
blob = {k: hashlib.sha256(subprocess.check_output(["git", "cat-file", "blob", t235[k]])).hexdigest() for k in pts}
print("blob sha256 == SHA256SUMS:", all(blob[k] == sums[k] for k in pts), len(sums))
chk = json.load(open(O + "/models_sha256_check.json"))
p2 = json.load(open(O + "/pass2_summary.json"))["model_sha256"]
print("check all_agree:", chk["all_agree"], "entries:", chk["entries_in_list"], "extra:", chk["files_in_list_not_read_here"])
bad = []
for k in pts:
    r = chk["files"][k]
    arm, seed = k.split("_")[1], k.split("seed")[1][0]
    first = None
    if arm != "blind":
        first = json.load(open(f"{O}/nominate_{arm}_seed{seed}.json"))["checkpoint_sha256"]
        ms = json.load(open(f"{O}/measure_{arm}_seed{seed}.json"))
        mh = ms.get("checkpoint_sha256")
        if mh and mh != blob[k]: bad.append((k, "measure"))
    for name, v in [("chk.list", r["models_commit_list"]), ("chk.second", r["second_pass_read"]), ("chk.first", r["first_pass_read"]), ("nominate", first), ("pass2", p2[f"{arm}/{seed}"])]:
        if v is not None and v != blob[k]: bad.append((k, name))
print("mismatches vs blob hashes:", bad)
# findings table
f = open(T + "/b/docs/2026-09-26-toy-rerun-v3-rules.md").read()
print("findings table hashes all match:", all(f"`{k}` | `{blob[k]}`" in f for k in pts))
```

### B. `recompute.py` (section 3)

```python
"""Independent recompute of the toy re-run's verdicts from committed outputs
(branch worktree-w1d-toy-rerun-v3 at a71e833). No model is loaded."""
import json, numpy as np
O = "/Users/john/.claude/jobs/faa2f7d5/tmp/b/experiments/rehearsal-successor-measure/out-v3-rules/"
L = lambda f: json.load(open(O + f))
ARMS, SEEDS = "TCFM", (0, 1, 2)
POS = ["action", "action+ans", "action+3", "post-identity", "all"]  # repairs tie order
FOUR = POS[:4]
CONTIG = [tuple(range(a, b + 1)) for a in range(5) for b in range(a, 5)]
BAR, FLOOR, FIT = 790, 0.8, 0.8
problems = []
def chk(cond, msg):
    if not cond: problems.append(msg)

# ---- gate
g = L("gate.json")
print("GATE")
for a in ARMS:
    own = sum(g["runs"][f"{a}/{s}"]["own_correct"] >= BAR for s in SEEDS)
    oth = sum(g["runs"][f"{a}/{s}"]["other_correct"] >= BAR for s in SEEDS)
    passes = (own >= 2 and oth >= 2) if a == "F" else own >= 2
    chk(passes == g["verdicts"][a]["passes"], f"gate {a}")
    print(f"  {a}: own {own}/3 other {oth}/3 -> {'passes' if passes else 'FAILS'}",
          [ (g['runs'][f'{a}/{s}']['own_correct'], g['runs'][f'{a}/{s}']['other_correct']) for s in SEEDS])
gate_pass = {a: g["verdicts"][a]["passes"] for a in ARMS}

def floor(w, u, acc):
    need = FLOOR * (acc - u)
    return (w - u >= need) and need > 0

def pick(grid, allowed):
    clearing = [x for x in grid if allowed(tuple(x["layers"]), x["positions"])]
    clearing = [x for x in clearing if x["_clears"]]
    if not clearing: return None
    small = {}
    for x in clearing:
        k = (len(x["layers"]), tuple(x["layers"]))
        small[x["positions"]] = min(small.get(x["positions"], k), k)
    c = [x for x in clearing if (len(x["layers"]), tuple(x["layers"])) == small[x["positions"]]]
    b = min(c, key=lambda x: (-x["accuracy_ownership_only"], x["rank"], POS.index(x["positions"])))
    return dict(layers=list(b["layers"]), positions=b["positions"], rank=b["rank"])

spec = lambda x: None if x is None else dict(layers=list(x["layers"]), positions=x["positions"], rank=x["rank"])
fam60 = {(l, p) for l in CONTIG for p in FOUR}
res = {}
cpu_gpu = []
print("\nPER ARM/SEED")
for a in ARMS:
    for s in SEEDS:
        n, nl, m = L(f"nominate_{a}_seed{s}.json"), L(f"null_{a}_seed{s}.json"), L(f"measure_{a}_seed{s}.json")
        u, acc = n["untouched"], n["arm_accuracy"]
        for x in n["grid"]:
            x["_clears"] = floor(x["accuracy_whole"], u, acc)
            chk(x["_clears"] == x["floor"]["clears"], f"{a}/{s} grid floor")
        chk(len(n["grid"]) == 300, "grid size")
        in60 = lambda l, p: (l, p) in fam60
        first = pick(n["grid"], in60)
        prim = pick(n["grid"], lambda l, p: in60(l, p) and not (0 in l and p != "action"))
        strict = pick(n["grid"], lambda l, p: in60(l, p) and 0 not in l)
        chk(first == spec(n["nomination_v60"]), f"{a}/{s} first-pass v60 pick")
        chk(prim == spec(n["unruled_v60_with_layer0_injection_sets_removed_before_choosing"]), f"{a}/{s} primary pick")
        chk(strict == spec(n["unruled_v60_with_every_layer0_set_removed_before_choosing"]), f"{a}/{s} stricter pick")
        chk(prim == m["rows"]["unruled_layer0_injection_removed"]["site_set"], f"{a}/{s} measure row site")
        chk(strict == m["rows"]["unruled_every_layer0_removed"]["site_set"], f"{a}/{s} measure strict site")
        clear60 = len({(tuple(x["layers"]), x["positions"]) for x in n["grid"] if x["_clears"] and in60(tuple(x["layers"]), x["positions"])})
        # CPU vs GPU fits
        for l in range(5):
            gf, cf = n["fit_accuracy"][str(l)], nl["layers"][str(l)]["fit_accuracy"]
            if abs(gf - cf) > 1e-9: cpu_gpu.append((f"{a}/{s}", l, round(gf, 4), round(cf, 4)))
            nul = np.array(nl["layers"][str(l)]["null"])
            chk(len(nul) == 200, "null count")
            chk(abs(np.percentile(nul, 95) - nl["layers"][str(l)]["null_p95"]) < 1e-12, f"{a}/{s} p95 l{l}")
            chk(abs(np.percentile(nul, 99) - nl["layers"][str(l)]["null_p99"]) < 1e-12, f"{a}/{s} p99 l{l}")
        out = {}
        for kind, row in (("primary", "unruled_layer0_injection_removed"), ("stricter", "unruled_every_layer0_removed"), ("first", "primary")):
            sp = {"primary": prim, "stricter": strict, "first": first}[kind]
            r = m["rows"][row]
            rd = r["reading"]
            w, o, uu, ac = rd["accuracy_whole"], rd["accuracy_ownership_only"], rd["accuracy_untouched"], rd["arm_own_accuracy"]
            fl = floor(w, uu, ac)
            deg = (w - o) / (w - uu) if fl else None
            chk(deg is None or abs(deg - rd["degree"]) < 1e-12, f"{a}/{s} {kind} degree")
            fits = {l: n["fit_accuracy"][str(l)] for l in sp["layers"]}
            wl = min(sp["layers"], key=lambda l: (fits[l], l))
            fit = fits[wl]
            rnd = np.array(r["control3"]["random_donor_shares"])
            chk(len(rnd) == 20, "20 draws")
            c3 = dict(median=np.median(rnd), p95=np.percentile(rnd, 95), own=o,
                      below=int((rnd < o).sum()), eq=int((rnd == o).sum()), above=int((rnd > o).sum()))
            reasons = []
            if not gate_pass[a]: reasons.append("gate")
            if fit < FIT: reasons.append("fit floor")
            if not fl: reasons.append("whole-state floor (fresh)")
            if kind == "first":
                if 0 in sp["layers"] and sp["positions"] != "action": reasons.append("injection")
                if not (o > c3["p95"]): reasons.append("control 3")
            out[kind] = dict(site=sp, fit=fit, fit_layer=wl, p95n=nl["layers"][str(wl)]["null_p95"],
                             p99n=nl["layers"][str(wl)]["null_p99"], deg=deg, c3=c3,
                             verdict="reading" if not reasons else "no verdict: " + ", ".join(reasons))
        out["clear60"] = clear60
        out["l0noop"] = n["layer0_whole_equals_untouched_inside_action_turn"]
        out["c7"] = m["control7_null_transplant_bit_identical"]
        res[f"{a}/{s}"] = out

def fmt(k, r):
    s = r["site"]; c = r["c3"]
    return (f"  {k}: L{tuple(s['layers'])} {s['positions']} r{s['rank']} | fit {r['fit']:.3f} (l{r['fit_layer']}) "
            f"null {r['p95n']:.3f}/{r['p99n']:.3f} | c3 med {c['median']:.4f} p95 {c['p95']:.4f} own {c['own']:.4f} "
            f"({c['below']}/{c['eq']}/{c['above']}) | deg {'-' if r['deg'] is None else f'{r['deg']:.4f}'} | {r['verdict']}")
for kind in ("primary", "stricter", "first"):
    print(f"\n[{kind}]")
    for k, v in res.items(): print(fmt(k, v[kind]))
print("\nclearing of 60:", {k: v["clear60"] for k, v in res.items()})
print("layer0 whole==untouched inside action turn:", {k: v["l0noop"] for k, v in res.items()})
print("control7 (first-pass primary site):", {k: v["c7"] for k, v in res.items()})
print("CPU vs GPU fit differences:", cpu_gpu)
nominated_layers = {k: v["primary"]["site"]["layers"] for k, v in res.items()}
print("  of those, at a Part 1 nominated layer:", [d for d in cpu_gpu if d[1] in nominated_layers[d[0]]])

M = [res[f"M/{s}"]["primary"]["deg"] for s in SEEDS]
print("\narm M readings", [round(x, 4) for x in M], "all in [0.3,0.7]:", all(0.3 <= x <= 0.7 for x in M))
for s in SEEDS:
    c, t = res[f"C/{s}"]["primary"], res[f"T/{s}"]["primary"]
    print(f"seed {s}: C {c['deg']:.4f} ({c['verdict']}), T {t['deg']:.4f} ({t['verdict']}), C-T {c['deg']-t['deg']:.4f} clears 0.5: {c['deg']-t['deg'] >= 0.5}")
print("arm F:", [(res[f'F/{s}']['primary']['fit'], res[f'F/{s}']['primary']['verdict']) for s in SEEDS])
print("arm F best fit any layer any seed:", max(L(f"nominate_F_seed{s}.json")["fit_accuracy"][str(l)] for s in SEEDS for l in range(5)))
print("arms T,C,M min fit at Part-1 nominated layer:", min(res[f"{a}/{s}"]["primary"]["fit"] for a in "TCM" for s in SEEDS))

# pass2_summary agreement
p2 = L("pass2_summary.json")
for k, v in res.items():
    for kind in ("primary", "stricter"):
        e = p2["arms"][k][kind]
        chk(e["site_set"] == v[kind]["site"], f"p2 site {k} {kind}")
        chk(e["verdict"]["status"] == v[kind]["verdict"].split(":")[0], f"p2 status {k} {kind}: {e['verdict']['status']} vs {v[kind]['verdict']}")
        c = e["control3"]
        chk((c["draws_below"], c["draws_equal"], c["draws_above"]) == (v[kind]["c3"]["below"], v[kind]["c3"]["eq"], v[kind]["c3"]["above"]), f"p2 c3 {k} {kind}")
        chk(abs(c["p95"] - v[kind]["c3"]["p95"]) < 1e-12 and abs(c["median"] - v[kind]["c3"]["median"]) < 1e-12, f"p2 c3 num {k}")
print("pass2 arm_M_pass:", p2["arm_M_pass"]); print("pass2 separation:", p2["separation"])
print("\nPROBLEMS:", problems or "none")
```

### C. `alt.py` (sections 4.4 and 5)

```python
"""Would the narrower reading of 'spanning the acting turns' (post-identity
only) have picked differently from the literal 'action only' reading?"""
import json
O = "/Users/john/.claude/jobs/faa2f7d5/tmp/b/experiments/rehearsal-successor-measure/out-v3-rules/"
L = lambda f: json.load(open(O + f))
POS = ["action", "action+ans", "action+3", "post-identity", "all"]
FOUR = POS[:4]
CONTIG = [tuple(range(a, b + 1)) for a in range(5) for b in range(a, 5)]
fam60 = {(l, p) for l in CONTIG for p in FOUR}

def floor(w, u, acc):
    need = 0.8 * (acc - u)
    return (w - u >= need) and need > 0

def pick(grid, allowed):
    c = [x for x in grid if allowed(tuple(x["layers"]), x["positions"]) and x["_c"]]
    if not c: return None
    sm = {}
    for x in c:
        k = (len(x["layers"]), tuple(x["layers"]))
        sm[x["positions"]] = min(sm.get(x["positions"], k), k)
    c = [x for x in c if (len(x["layers"]), tuple(x["layers"])) == sm[x["positions"]]]
    b = min(c, key=lambda x: (-x["accuracy_ownership_only"], x["rank"], POS.index(x["positions"])))
    return (tuple(b["layers"]), b["positions"], b["rank"], round(b["accuracy_ownership_only"], 4))

for a in "TCFM":
    for s in (0, 1, 2):
        n = L(f"nominate_{a}_seed{s}.json"); u, acc = n["untouched"], n["arm_accuracy"]
        for x in n["grid"]: x["_c"] = floor(x["accuracy_whole"], u, acc)
        lit = pick(n["grid"], lambda l, p: (l, p) in fam60 and not (0 in l and p != "action"))
        nar = pick(n["grid"], lambda l, p: (l, p) in fam60 and not (0 in l and p == "post-identity"))
        first_lit = pick(n["grid"], lambda l, p: (l, p) in fam60)
        print(a, s, "literal", lit, "| narrow", nar, "SAME" if lit == nar else "DIFFERS", "| first-pass pick", first_lit)
        if a in "TM":
            for p in ("action+ans", "action+3"):
                rows = [(x["rank"], round(x["accuracy_whole"], 4), round(x["accuracy_ownership_only"], 4), x["_c"])
                        for x in n["grid"] if x["layers"] == [0] and x["positions"] == p]
                print(f"    layer0 {p}: (rank, whole, own, clears) {rows}; untouched {u:.4f}, arm acc {acc:.4f}")
```

### D. Output of `check_models.py`

```
pt files at 235c385: 15 | a86783e same blob ids: True 15
blob sha256 == SHA256SUMS: True 15
check all_agree: True entries: 15 extra: []
mismatches vs blob hashes: []
findings table hashes all match: True
```

### E. Output of `recompute.py`

```
GATE
  T: own 3/3 other 3/3 -> passes [(3000, 3000), (3000, 3000), (3000, 3000)]
  C: own 3/3 other 0/3 -> passes [(1711, 760), (1703, 751), (1727, 708)]
  F: own 3/3 other 1/3 -> FAILS [(1679, 994), (1654, 781), (1664, 746)]
  M: own 3/3 other 3/3 -> passes [(2592, 1663), (2584, 1699), (2600, 1655)]

PER ARM/SEED

[primary]
  T/0: L(0,) action r8 | fit 1.000 (l0) null 0.117/0.133 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/1: L(0,) action r8 | fit 1.000 (l0) null 0.117/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/2: L(0,) action r8 | fit 1.000 (l0) null 0.111/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  C/0: L(2,) action r8 | fit 1.000 (l2) null 0.111/0.122 | c3 med 0.0587 p95 0.0639 own 0.0488 (0/0/20) | deg 1.0051 | reading
  C/1: L(4,) action r2 | fit 0.961 (l4) null 0.122/0.139 | c3 med 0.0550 p95 0.0613 own 0.0475 (0/1/19) | deg 1.0025 | reading
  C/2: L(1,) post-identity r1 | fit 0.978 (l1) null 0.117/0.128 | c3 med 0.0600 p95 0.0653 own 0.0600 (3/9/8) | deg 1.0000 | reading
  F/0: L(1,) post-identity r1 | fit 0.172 (l1) null 0.128/0.133 | c3 med 0.0587 p95 0.0625 own 0.0587 (6/7/7) | deg 1.0000 | no verdict: gate, fit floor
  F/1: L(1,) action+3 r4 | fit 0.067 (l1) null 0.117/0.122 | c3 med 0.0587 p95 0.0650 own 0.0563 (2/1/17) | deg 1.0000 | no verdict: gate, fit floor
  F/2: L(1,) post-identity r8 | fit 0.106 (l1) null 0.117/0.133 | c3 med 0.0638 p95 0.0664 own 0.0638 (8/3/9) | deg 1.0108 | no verdict: gate, fit floor
  M/0: L(1,) post-identity r8 | fit 1.000 (l1) null 0.122/0.139 | c3 med 0.0150 p95 0.0190 own 0.4050 (20/0/0) | deg 0.4886 | reading
  M/1: L(1,) post-identity r8 | fit 1.000 (l1) null 0.117/0.139 | c3 med 0.0187 p95 0.0226 own 0.4062 (20/0/0) | deg 0.4860 | reading
  M/2: L(1,) post-identity r8 | fit 1.000 (l1) null 0.117/0.144 | c3 med 0.0150 p95 0.0213 own 0.3688 (20/0/0) | deg 0.5449 | reading

[stricter]
  T/0: L(1,) action r8 | fit 1.000 (l1) null 0.117/0.133 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/1: L(1,) action r8 | fit 1.000 (l1) null 0.117/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/2: L(1,) action r8 | fit 1.000 (l1) null 0.117/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  C/0: L(2,) action r8 | fit 1.000 (l2) null 0.111/0.122 | c3 med 0.0587 p95 0.0639 own 0.0488 (0/0/20) | deg 1.0051 | reading
  C/1: L(4,) action r2 | fit 0.961 (l4) null 0.122/0.139 | c3 med 0.0550 p95 0.0613 own 0.0475 (0/1/19) | deg 1.0025 | reading
  C/2: L(1,) post-identity r1 | fit 0.978 (l1) null 0.117/0.128 | c3 med 0.0600 p95 0.0653 own 0.0600 (3/9/8) | deg 1.0000 | reading
  F/0: L(1,) post-identity r1 | fit 0.172 (l1) null 0.128/0.133 | c3 med 0.0587 p95 0.0625 own 0.0587 (6/7/7) | deg 1.0000 | no verdict: gate, fit floor
  F/1: L(1,) action+3 r4 | fit 0.067 (l1) null 0.117/0.122 | c3 med 0.0587 p95 0.0650 own 0.0563 (2/1/17) | deg 1.0000 | no verdict: gate, fit floor
  F/2: L(1,) post-identity r8 | fit 0.106 (l1) null 0.117/0.133 | c3 med 0.0638 p95 0.0664 own 0.0638 (8/3/9) | deg 1.0108 | no verdict: gate, fit floor
  M/0: L(1,) post-identity r8 | fit 1.000 (l1) null 0.122/0.139 | c3 med 0.0150 p95 0.0190 own 0.4050 (20/0/0) | deg 0.4886 | reading
  M/1: L(1,) post-identity r8 | fit 1.000 (l1) null 0.117/0.139 | c3 med 0.0187 p95 0.0226 own 0.4062 (20/0/0) | deg 0.4860 | reading
  M/2: L(1,) post-identity r8 | fit 1.000 (l1) null 0.117/0.144 | c3 med 0.0150 p95 0.0213 own 0.3688 (20/0/0) | deg 0.5449 | reading

[first]
  T/0: L(0,) action r8 | fit 1.000 (l0) null 0.117/0.133 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/1: L(0,) action r8 | fit 1.000 (l0) null 0.117/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  T/2: L(0,) action r8 | fit 1.000 (l0) null 0.111/0.128 | c3 med 0.0000 p95 0.0000 own 1.0000 (20/0/0) | deg 0.0000 | reading
  C/0: L(2,) action r8 | fit 1.000 (l2) null 0.111/0.122 | c3 med 0.0587 p95 0.0639 own 0.0488 (0/0/20) | deg 1.0051 | no verdict: control 3
  C/1: L(0,) post-identity r8 | fit 0.072 (l0) null 0.111/0.122 | c3 med 0.0494 p95 0.0514 own 0.0550 (20/0/0) | deg 0.9863 | no verdict: fit floor, injection
  C/2: L(0,) post-identity r2 | fit 0.072 (l0) null 0.111/0.128 | c3 med 0.0600 p95 0.0625 own 0.0600 (6/7/7) | deg 1.0000 | no verdict: fit floor, injection, control 3
  F/0: L(0,) post-identity r2 | fit 0.072 (l0) null 0.117/0.122 | c3 med 0.0587 p95 0.0588 own 0.0575 (2/3/15) | deg 1.0029 | no verdict: gate, fit floor, injection, control 3
  F/1: L(1,) action+3 r4 | fit 0.067 (l1) null 0.117/0.122 | c3 med 0.0587 p95 0.0650 own 0.0563 (2/1/17) | deg 1.0000 | no verdict: gate, fit floor, control 3
  F/2: L(0,) post-identity r1 | fit 0.072 (l0) null 0.111/0.128 | c3 med 0.0694 p95 0.0712 own 0.0688 (2/8/10) | deg 1.0000 | no verdict: gate, fit floor, injection, control 3
  M/0: L(0,) post-identity r8 | fit 1.000 (l0) null 0.117/0.133 | c3 med 0.0125 p95 0.0151 own 0.3925 (20/0/0) | deg 0.5105 | no verdict: injection
  M/1: L(3,) action r8 | fit 1.000 (l3) null 0.117/0.133 | c3 med 0.0531 p95 0.0701 own 0.3937 (20/0/0) | deg 0.4846 | reading
  M/2: L(0,) post-identity r8 | fit 1.000 (l0) null 0.111/0.128 | c3 med 0.0112 p95 0.0139 own 0.3775 (20/0/0) | deg 0.5322 | no verdict: injection

clearing of 60: {'T/0': 60, 'T/1': 60, 'T/2': 60, 'C/0': 51, 'C/1': 39, 'C/2': 51, 'F/0': 42, 'F/1': 39, 'F/2': 42, 'M/0': 42, 'M/1': 42, 'M/2': 42}
layer0 whole==untouched inside action turn: {'T/0': {'action+3': False, 'action+ans': False}, 'T/1': {'action+3': False, 'action+ans': False}, 'T/2': {'action+3': False, 'action+ans': False}, 'C/0': {'action+3': True, 'action+ans': True}, 'C/1': {'action+3': True, 'action+ans': True}, 'C/2': {'action+3': True, 'action+ans': True}, 'F/0': {'action+3': True, 'action+ans': True}, 'F/1': {'action+3': True, 'action+ans': True}, 'F/2': {'action+3': True, 'action+ans': True}, 'M/0': {'action+3': False, 'action+ans': False}, 'M/1': {'action+3': False, 'action+ans': False}, 'M/2': {'action+3': False, 'action+ans': False}}
control7 (first-pass primary site): {'T/0': True, 'T/1': True, 'T/2': True, 'C/0': True, 'C/1': True, 'C/2': True, 'F/0': True, 'F/1': True, 'F/2': True, 'M/0': True, 'M/1': True, 'M/2': True}
CPU vs GPU fit differences: [('F/0', 1, 0.1722, 0.1778), ('F/1', 3, 0.1444, 0.1333), ('F/2', 1, 0.1056, 0.1), ('M/0', 3, 0.9889, 0.9944)]
  of those, at a Part 1 nominated layer: [('F/0', 1, 0.1722, 0.1778), ('F/2', 1, 0.1056, 0.1)]

arm M readings [0.4886, 0.486, 0.5449] all in [0.3,0.7]: True
seed 0: C 1.0051 (reading), T 0.0000 (reading), C-T 1.0051 clears 0.5: True
seed 1: C 1.0025 (reading), T 0.0000 (reading), C-T 1.0025 clears 0.5: True
seed 2: C 1.0000 (reading), T 0.0000 (reading), C-T 1.0000 clears 0.5: True
arm F: [(0.17222222222222222, 'no verdict: gate, fit floor'), (0.06666666666666667, 'no verdict: gate, fit floor'), (0.10555555555555556, 'no verdict: gate, fit floor')]
arm F best fit any layer any seed: 0.17222222222222222
arms T,C,M min fit at Part-1 nominated layer: 0.9611111111111111
pass2 arm_M_pass: {'band': [0.3, 0.7], 'met_on_every_seed': True, 'readings': [0.4885993485342019, 0.4859504132231405, 0.5448717948717948]}
pass2 separation: {'0': {'C': 1.0051150895140666, 'C_minus_T': 1.0051150895140666, 'T': 0.0, 'clears_0_5': True}, '1': {'C': 1.0024570024570023, 'C_minus_T': 1.0024570024570023, 'T': 0.0, 'clears_0_5': True}, '2': {'C': 1.0, 'C_minus_T': 1.0, 'T': 0.0, 'clears_0_5': True}}

PROBLEMS: none
```

### F. Output of `alt.py`

```
T 0 literal ((0,), 'action', 8, 1.0) | narrow ((0,), 'action', 8, 1.0) SAME | first-pass pick ((0,), 'action', 8, 1.0)
    layer0 action+ans: (rank, whole, own, clears) [(1, 1.0, 0.1517, True), (2, 1.0, 0.335, True), (4, 1.0, 0.7783, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
    layer0 action+3: (rank, whole, own, clears) [(1, 1.0, 0.1517, True), (2, 1.0, 0.335, True), (4, 1.0, 0.7783, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
T 1 literal ((0,), 'action', 8, 1.0) | narrow ((0,), 'action', 8, 1.0) SAME | first-pass pick ((0,), 'action', 8, 1.0)
    layer0 action+ans: (rank, whole, own, clears) [(1, 1.0, 0.1417, True), (2, 1.0, 0.395, True), (4, 1.0, 0.8467, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
    layer0 action+3: (rank, whole, own, clears) [(1, 1.0, 0.1417, True), (2, 1.0, 0.395, True), (4, 1.0, 0.8467, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
T 2 literal ((0,), 'action', 8, 1.0) | narrow ((0,), 'action', 8, 1.0) SAME | first-pass pick ((0,), 'action', 8, 1.0)
    layer0 action+ans: (rank, whole, own, clears) [(1, 1.0, 0.1667, True), (2, 1.0, 0.335, True), (4, 1.0, 0.8717, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
    layer0 action+3: (rank, whole, own, clears) [(1, 1.0, 0.1667, True), (2, 1.0, 0.335, True), (4, 1.0, 0.8717, True), (8, 1.0, 1.0, True)]; untouched 0.0000, arm acc 1.0000
C 0 literal ((2,), 'action', 8, 0.055) | narrow ((2,), 'action', 8, 0.055) SAME | first-pass pick ((2,), 'action', 8, 0.055)
C 1 literal ((4,), 'action', 2, 0.0533) | narrow ((4,), 'action', 2, 0.0533) SAME | first-pass pick ((0,), 'post-identity', 8, 0.0567)
C 2 literal ((1,), 'post-identity', 1, 0.0533) | narrow ((1,), 'post-identity', 1, 0.0533) SAME | first-pass pick ((0,), 'post-identity', 2, 0.055)
F 0 literal ((1,), 'post-identity', 1, 0.0633) | narrow ((1,), 'post-identity', 1, 0.0633) SAME | first-pass pick ((0,), 'post-identity', 2, 0.0633)
F 1 literal ((1,), 'action+3', 4, 0.05) | narrow ((1,), 'action+3', 4, 0.05) SAME | first-pass pick ((1,), 'action+3', 4, 0.05)
F 2 literal ((1,), 'post-identity', 8, 0.0733) | narrow ((1,), 'post-identity', 8, 0.0733) SAME | first-pass pick ((0,), 'post-identity', 1, 0.07)
M 0 literal ((1,), 'post-identity', 8, 0.3867) | narrow ((1,), 'post-identity', 8, 0.3867) SAME | first-pass pick ((0,), 'post-identity', 8, 0.3683)
    layer0 action+ans: (rank, whole, own, clears) [(1, 0.3967, 0.0283, False), (2, 0.3967, 0.0633, False), (4, 0.3967, 0.1867, False), (8, 0.3967, 0.3683, False)]; untouched 0.0150, arm acc 0.8583
    layer0 action+3: (rank, whole, own, clears) [(1, 0.3967, 0.0283, False), (2, 0.3967, 0.0633, False), (4, 0.3967, 0.1867, False), (8, 0.3967, 0.3683, False)]; untouched 0.0150, arm acc 0.8583
M 1 literal ((1,), 'post-identity', 8, 0.395) | narrow ((1,), 'post-identity', 8, 0.395) SAME | first-pass pick ((3,), 'action', 8, 0.3783)
    layer0 action+ans: (rank, whole, own, clears) [(1, 0.3983, 0.0583, False), (2, 0.3983, 0.12, False), (4, 0.3983, 0.2567, False), (8, 0.3983, 0.355, False)]; untouched 0.0167, arm acc 0.8717
    layer0 action+3: (rank, whole, own, clears) [(1, 0.3983, 0.0583, False), (2, 0.3983, 0.12, False), (4, 0.3983, 0.2567, False), (8, 0.3983, 0.355, False)]; untouched 0.0167, arm acc 0.8717
M 2 literal ((1,), 'post-identity', 8, 0.3683) | narrow ((1,), 'post-identity', 8, 0.3683) SAME | first-pass pick ((0,), 'post-identity', 8, 0.37)
    layer0 action+ans: (rank, whole, own, clears) [(1, 0.3933, 0.04, False), (2, 0.3933, 0.105, False), (4, 0.3933, 0.2267, False), (8, 0.3933, 0.37, False)]; untouched 0.0117, arm acc 0.8867
    layer0 action+3: (rank, whole, own, clears) [(1, 0.3933, 0.04, False), (2, 0.3933, 0.105, False), (4, 0.3933, 0.2267, False), (8, 0.3933, 0.37, False)]; untouched 0.0117, arm acc 0.8867
```

### G. The gate counts against the repairs record (section 2.1)

```
$ .venv/bin/python -c "<compare out-v3-rules/gate.json runs with out-repairs/gate_base.json runs>"
pairs compared 12 mismatches []
```
