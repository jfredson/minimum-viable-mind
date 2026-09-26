# Check of the free-arm label search — commit order, the 0.556 against the 0.172, the figures recomputed, the models, the processor, and the closing paragraph

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1d label search
check", on branch `check-free-arm-label-search`, cut from `origin/main` at
`da41c20` (the annotation of the Gate C rulings' refinement 2, pull request 68).*

*This session did not write what it checks. The target is pull request 66, "the
free-arm label search at toy scale", written by the session "MVM W1d free-arm
label search". Its branch is `w1d-free-arm-label-search` at its tip, commit
`26b737f`, cut from main at `62c3824`. Its method is
`docs/2026-09-26-free-arm-label-search-method.md` with two dated amendments, its
findings `docs/2026-09-26-free-arm-label-search.md`, its code
`experiments/rehearsal-successor-measure/src/label_search.py` and
`label_search_report.py`, and its outputs
`experiments/rehearsal-successor-measure/out-label-search/`, all on that branch
and none on main. Every path below that starts `out-label-search/` means that
folder at `26b737f`. No file on that branch was modified. This check read the
branch through `git archive 26b737f` into a scratch folder.*

*It runs under route (b) of John's ruling on the Gate C review's fatal finding
RT-212 (the ownership read on the free arm never finds its label),
`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, item 3. The models
are checked against the fingerprint list committed on main under
`experiments/rehearsal-successor-measure/out-repairs/models/SHA256SUMS`
(pull requests 64 and 67).*

*Every finding is labelled **MEASURED** (a command was run and its output is in
the appendix) or **ARGUED** (reasoning a reader can dispute), with the file it
rests on. Nothing was retrained. Two runs loaded the twelve committed models, to
repeat the identity check on the graphics processor and on the processor
(section 5). Everything else is recomputed from the committed JSON outputs.
Laptop only, nothing rented, **$0**. Written under the workspace plain-language
rule.*

## Verdict

- **Commit order holds.** MEASURED, section 1. Method, then code, then
  amendment 1, then its code change, then amendment 2, then its code change,
  then the outputs in the stop rule's order, then the findings. The recorded
  run times fit inside the gaps between each code commit and the output commit
  after it (ARGUED from the timings). Two small things are worth knowing. The
  graphics-processor identity check that amendment 1 cites was first run as an
  uncommitted scratch diagnostic *before* the amendment was written. And the
  committed identity-check output, `verify.json`, went in with amendment 2's
  method commit rather than an output commit. Both are disclosed. Neither lets
  an output steer the rule that scores it.
- **The 0.556 and the 0.172 are two different reads, and the registered rule
  produces the 0.172.** ARGUED from the code, MEASURED on the figures,
  section 2. The two agree on everything underneath: the same models, episodes,
  420/180 split, fitter, scoring, and graphics processor. PR 66's own
  cell for the registered read (layer 1, the action position) is 0.172 / 0.067 /
  0.106 to the digit. They differ in what the read is fed. The registered rule
  fits one read per layer at the `<mask>` position only (`repairs.fit_reads`),
  whatever site set is nominated, and reports the worst layer of the nominated
  set (`rerun_v3.pass2_verdict`). PR 66 fits one read per *site set*: layers
  laid end to end, several positions laid end to end, and the post-identity
  span *averaged*. All three 0.556 / 0.483 / 0.433 figures come from that
  averaged span, at layers 0–1 or 0. That span starts at the model's own
  marker word, and RT-216 removes layer 0 from it. So RT-212's wording ("at
  most 0.172 … at any layer") is right for the read the rule registers. On
  arm F at the toy re-run's own nominated site set (F/0: layer 1,
  post-identity), the registered read gives 0.172 where PR 66's pooled read
  gives 0.511.
- **No candidate clears on any seed; the figures reproduce.** MEASURED,
  section 3. Every best fit, action-anchored best, shuffle summary and verdict
  in the findings' section 4 and section 6 tables recomputes exactly from the
  committed `fit_*.json`. The "clears" flag stored in every file agrees with
  the four-fifths floor plus the best-site shuffles. No arm F site set reaches
  0.80 for any label. Candidate 1 (which two turns are the model's own) goes
  above 0.78 only at two site sets, both on seed 2 and both over the
  post-identity span: 0.789 at layers 0–1 and 0.783 at layer 1. Its
  action-anchored bests are 0.733 / 0.383 / 0.478.
- **The models are the committed models.** MEASURED, section 4. The twelve
  fingerprints recorded in `verify.json` and in every `fit_*.json` equal the
  twelve `base` entries in the committed `SHA256SUMS`. All thirty files under
  `out-repairs/models/` on main also check against that list.
- **Amendment 1 reproduces, and one committed figure elsewhere was made on the
  processor.** MEASURED, section 5. Run on the graphics processor with the
  models from git, the identity check matches all twelve arm-and-seed pairs
  with a largest gap of 0. Run on the processor, it fails on exactly the four
  pairs and by exactly the gaps `verify_cpu_failed.json` records. Elsewhere,
  the toy re-run's committed permutation baselines
  (`out-v3-rules/null_*.json`, pull request 62) were fitted on the processor.
  Their per-layer fits carry the processor's values on the same four pairs
  (F/0 layer 1: 0.1778, not 0.1722). The toy re-run's findings already
  disclose this. It moves no verdict: those baselines are reported beside the
  floor, not used as the bar. No other committed output records the
  processor.
- **The closing plain-language paragraph is mostly MEASURED, but not all of it
  as written.** Section 6. Three things need fixing. "No read the free system
  is forced to carry clears the floor" is wider than what was measured: three
  candidates, chosen in advance. "Near chance at arm F's fixed-extent sites"
  is not what the files show. The ruled label reaches 0.206 and 0.211 there on
  seeds 0 and 2, and on those seeds 18 and 17 action-anchored site sets beat
  every one of the 200 shuffles. And "never passes 0.48" should be "never
  passes 0.49" (the seed-1 best is 0.4833). None of this changes a verdict.

## 0. Words used here, once

- **Arm F** is the freely trained toy model. **Arms T, C and M** are the
  constructed comparison arms.
- **Registered read** means the straight-line read the site-set rule of
  proposal version 2, section 7.2, uses to pick its transplant directions. In
  code it is `repairs.fit_reads`: one logistic regression per layer, on the
  running state at the own-directed action's `<mask>` position, labelled with
  the model's own marker word.
- **Pooled read** means PR 66's read: one logistic regression per site set, on
  the states of every layer in the set and every position in the set, laid end
  to end, with the post-identity span averaged over its positions first
  (`label_search.per_layer_features`, `site_features`).
- **Action-anchored** (PR 66's "fixed-extent") site sets are the 45 whose
  positions are `action`, `action+ans` or `action+3`. Their extent does not
  depend on who the model is.
- **Shuffles** are the label-permutation baseline: refit with the training
  labels shuffled, scored on the true held-out labels, 200 times at each arm
  and seed's best site set (amendment 2).

## 1. Commit order

### 1.1 The order

MEASURED, `git log --reverse 62c3824..26b737f` and `git show --stat` on each
commit (appendix A).

| # | commit | time (−07:00) | what | files |
|---|---|---|---|---|
| 1 | `583b3f2` | 07:34:15 | method | method file only |
| 2 | `883bc81` | 07:36:16 | code | `label_search.py` added |
| 3 | `88ab899` | 07:38:16 | amendment 1 (forward pass on the graphics processor) | method file only |
| 4 | `53240d4` | 07:38:40 | its code change; the failed processor-run check | `label_search.py`; `verify_cpu_failed.json` |
| 5 | `6c82c81` | 09:56:06 | amendment 2 (shuffles at the best site only) | method file; `verify.json`; the superseded candidate 1 arm F seed 0 file |
| 6 | `609260b` | 09:56:48 | its code change; the report script | `label_search.py`; `label_search_report.py` added |
| 7 | `fd7f5fa` | 10:09:33 | candidate 1 outputs, four arms, and its verdict | 12 `fit_` files, `verdict_own-turn-pair.json` |
| 8 | `63f1ead` | 10:11:24 | candidate 2 outputs and verdict | 12 + 1 |
| 9 | `54ee9b0` | 10:19:24 | candidate 3 and the ruled label's reference row | 24 + 2 |
| 10 | `26b737f` | 10:22:33 | findings | findings file only |

- **Method before code, code before output, output before findings: yes.**
- **Each amendment before the fits it governs: yes.** Amendment 1 (commit 3)
  precedes every graphics-processor output (commits 5 and 7 to 9). Amendment 2
  (commit 5) precedes its code (commit 6) and every output made under it
  (commits 7 to 9).
- **No file on main under `src/` was changed.** Only the two new files were
  added. MEASURED, the `--stat` output.
- **The candidates ran in the stop rule's order.** Candidate 1, then 2, then 3,
  each with its verdict file committed before the next candidate's outputs.

### 1.2 Were the committed fits run after the code that made them?

ARGUED, from the `seconds` field of every `fit_*.json` (appendix C, "seconds
per label and arm"). The label search reads its code from the file on disk, so
commit order alone does not prove that a run used the committed code. The
timings are consistent with it:

- candidate 1, all four arms: 737 seconds (12.3 minutes). Code commit 6 at
  09:56:48, output commit at 10:09:33, a gap of 12.7 minutes;
- candidate 2: 91 seconds, against a gap of 1.9 minutes;
- candidate 3 and the reference row: 277 + 166 = 443 seconds (7.4 minutes),
  against a gap of 8.0 minutes.

Run back to back, each batch fits into its gap with under a minute to spare.
This is consistent with, not proof of, the claimed order.

### 1.3 Two things a reader should know

- **Amendment 1 cites a result obtained before it was written.** Its "Why"
  paragraph reports a scratch diagnostic that reproduced all twelve pairs on
  the graphics processor, "not committed as output". So the amendment was
  written knowing the graphics-processor check would pass. ARGUED: this is
  harmless. The amendment changes where the forward pass runs, to the
  processor the committed models were measured on (`"device": "mps"` in every
  `out-repairs/train_*.json`), not anything a candidate's fit depends on. No
  candidate was fitted before it. Section 5 repeats that check independently.
- **`verify.json` was committed with the method amendment, not in an output
  commit.** It is output of commit 4's code, committed in commit 5, so it
  still comes after its code. MEASURED: the verify stage is identical
  between `53240d4` and `26b737f` (the `53240d4..609260b` diff touches only
  `stage_fit`), and section 5's rerun at `26b737f` reproduces it.

## 2. The discrepancy: 0.556 / 0.483 / 0.433 against "never above 0.172"

### 2.1 What is the same

MEASURED unless marked.

| | Gate C review (RT-212) and toy re-run (PR 62) | PR 66 reference row |
|---|---|---|
| models | the repairs' `base` runs, arm F seeds 0–2 | the same files: section 4 |
| label | `repairs.read_labels(recip, "own")`, the marker word | the same call (`label_search.labels`, "marker-word") |
| episodes | `make_data(600, seed=4242, pool="dev")` | the same |
| split | first 420 fit, last 180 held out (`int(0.7 * n)`) | the same (`TRAIN_SHARE = 0.7`) |
| fitter | `LogisticRegression(max_iter=3000, C=1.0)`, no scaling | the same |
| scoring | plain accuracy on the 180 held out | the same (`clf.score`) |
| processor for the fits | graphics processor (`nominate_*`, committed runs) | graphics processor (amendment 1) |

The proof that these really are the same: PR 66's own cell for "layer 1,
`action`" on the reference row is **0.172 / 0.067 / 0.106**. Its per-layer
`action` fits are **0.0722, 0.1722, 0.1444, 0.1056, 0.0667** on seed 0, equal
to the committed `fit_accuracy.own` (appendix C). So scoring, split and
processor explain none of the gap.

### 2.2 What differs

MEASURED on the figures (appendix B and C), ARGUED on the reading of the code.

1. **Site family.** The registered read is fitted **per layer, at one
   position**. The nominated site set decides where the transplant happens
   and which layers' reads supply its directions (`repairs.nominate`, which
   takes `reads[l]["coef"]` for each `l` in the set). It does not change what
   the read is fitted on. PR 66 fits **one read per site set**. For a layer
   set it lays the layers end to end (up to 5 × 160 numbers). For `action+ans`
   and `action+3` it lays 2 or 4 positions end to end.
2. **Position averaging.** For `post-identity`, PR 66 averages the states over
   every position from the model's first own turn to the action. The
   registered read never sees those positions.
3. **Where the three figures come from.** 0.556 is layers 0–1,
   post-identity; 0.483 is layers 0–1, post-identity; 0.433 is layer 0,
   post-identity. **All three are pooled reads over the averaged span, and
   all three contain layer 0.** The span's first token is the model's own
   marker word, which is the label itself entering at the input. And layer 0
   is where the acting channel marks exactly the model's own turns. PR 66's
   method named this leak in advance (section 3, caution 1), and its findings
   say it (section 5, item 4).
4. **RT-216 removes all three.** Layer 0 is a candidate only at the `action`
   position set. With layer 0 removed elsewhere, the pooled read's best is
   0.533 / 0.456 / 0.406 (layers 1–2 or layer 1, still post-identity). That
   reproduces the findings' section 2.2 to the digit.
5. **Multi-position concatenation alone moves it a little.** Restricted to
   action-anchored site sets, the pooled read reaches 0.206 (layer 2,
   `action+3`), 0.144 (layer 3, `action`) and 0.211 (layers 0–1,
   `action+ans`). 0.206 and 0.211 are above 0.172 because several positions
   are laid end to end. Seed 1's 0.144 is itself a single-layer `action` read.
6. **Held-out split, scoring and processor:** no difference (section 2.1).

### 2.3 Which figure the registered nomination rule produces

ARGUED from the code and the rulings, MEASURED on the figures.

- The rule as run in the toy re-run (`rerun_v3.pass2_verdict`) takes the
  nominated site set, looks up the per-layer `action` read at each of its
  layers, and reports the **worst** of them against the 0.80 floor. For arm F
  that gave **0.172 / 0.067 / 0.106** (toy re-run, table in Part 1). The
  nominations were F/0 layer 1 post-identity, F/1 layer 1 `action+3`, and F/2
  layer 1 post-identity. At F/0's nominated site set the registered read gives
  0.172 and PR 66's pooled read gives **0.511**. Same named site set,
  different read.
- The ruling on RT-212 describes "the read fitted at the action position",
  "at most 0.172 … at any layer on any seed". PR 66's per-layer `action`
  fits confirm that. The best single-layer `action` fit on arm F is 0.1722
  (seed 0, layer 1), 0.1444 (seed 1, layer 3) and 0.1389 (seed 2, layer 2).
- **So RT-212's wording rests on the right figure.** No registered route
  produces 0.556. It would take a pooled read over a span that begins at the
  model's own marker word, at layer 0, which RT-216 has already excluded.
- **One ambiguity for version 3 to close (ARGUED).** Proposal version 2,
  section 7.2, item 3 says "At each site, fit the straight-line read for the
  label above". "At each site" can be read as PR 66 read it (fit on the site
  set's positions) or as the code does it (at the action, per layer, for the
  layers in the site set). The code, the rulings and every committed figure
  use the second. PR 66's findings table puts the pooled 0.556 in a column
  headed "best fit, all 60 site sets" beside the registered 0.172 without
  saying they are different reads. Version 3 should say in a sentence which
  read the site set feeds. Otherwise the next reader will meet the same
  apparent contradiction.

## 3. The figures, recomputed from the committed outputs

MEASURED, `recompute.py` and `extra.py` (appendix B and C), on every
`out-label-search/fit_*.json` and `verdict_*.json`.

### 3.1 Best fit per candidate per seed on arm F, the shuffles at the best site, and the verdict

| label | best fit, seeds 0 / 1 / 2 (site set) | best action-anchored fit | shuffle mean / 95th / highest at the best site | shuffles at or above the best fit | site sets clearing | verdict file |
|---|---|---|---|---|---|---|
| candidate 1, which two turns are the model's own | 0.733 (0–1 action+3) / 0.483 (0–1 post-identity) / 0.789 (0–1 post-identity) | 0.733 / 0.383 / 0.478 | 0.037 / 0.061 / 0.100; 0.035 / 0.061 / 0.083; 0.036 / 0.061 / 0.078 | 0, 0, 0 of 200 | 0, 0, 0 | fails on F |
| candidate 2, which turn holds the own value | 0.450 / 0.450 / 0.456 (all layer 0 post-identity) | 0.356 / 0.311 / 0.417 | 0.128 / 0.183 / 0.233; 0.129 / 0.184 / 0.239; 0.129 / 0.183 / 0.233 | 0, 0, 0 | 0, 0, 0 | fails on F |
| candidate 3, the own value | 0.611 (4 action+ans) / 0.611 (1–2 action) / 0.633 (0–3 action+ans) | the same | 0.125 / 0.167 / 0.189; 0.130 / 0.178 / 0.239; 0.122 / 0.172 / 0.200 | 0, 0, 0 | 0, 0, 0 | fails on F |
| reference, the ruled label | 0.556 / 0.483 / 0.433 (post-identity) | 0.206 / 0.144 / 0.211 | 0.082 / 0.122 / 0.144; 0.083 / 0.117 / 0.156; 0.079 / 0.117 / 0.156 | 0, 0, 0 | 0, 0, 0 | fails on F |

- **Against the four-fifths floor:** no arm F site set reaches 0.80 for any
  label on any seed (appendix C, "any arm F site ≥ 0.8": none). So no
  candidate clears on any seed, under the method's stricter test (0.80 *and*
  above every shuffle) or under the ruling's (0.80 alone). Each
  `verdict_*.json` has `clears_over_all_60: false`,
  `clears_over_fixed_extent_45: false` and `seeds_with_some_clearing_site: 0`
  for arm F.
- **The stored "clears" flag agrees** with a fresh test of fit ≥ 0.80 and fit
  above the stored shuffles' maximum, on all 240 arm-and-seed files (an
  assertion in `recompute.py`). The best site recorded in each file is the
  first maximum in rule order.
- **Arms T, C and M** also match the findings' section 4 table on every cell.
  The reference row clears on T (60 of 60), M (60 of 60) and C (57, 56 and 57
  of 60 by seed; 56 on all three seeds, 42 of them action-anchored, per
  `verdict_marker-word.json`). The highest shuffle anywhere a site cleared is
  0.267.

### 3.2 Candidate 1's fits above 0.78 come only from spans starting at the model's own turn

MEASURED (appendix B, last block):

- seed 0: no site set above 0.78. Best 0.7333, at layers 0–1, `action+3`;
- seed 1: none. Best 0.4833 (post-identity), best action-anchored 0.3833;
- seed 2: exactly two, **0.7889 at layers 0–1 post-identity and 0.7833 at
  layer 1 post-identity**. Best action-anchored 0.4778 (layer 2,
  `action+ans`).

So the action-anchored figures are **0.733 / 0.383 / 0.478**, as the brief
says and as the findings print. Every fit above 0.78 sits on the
post-identity span. That span begins at the model's first own turn, which is
one of the two turns candidate 1 asks for. That is the leak the method
flagged before any output (method, section 3, caution 1). ARGUED: seed 0's
0.733 is the one strong action-anchored figure. It includes layer 0 at
`action+3`, which RT-216 excludes. At layer 1 alone the same positions give
0.722. It is one seed of three, and the other two stay at or below 0.48.

### 3.3 Smaller checks of the findings' text

MEASURED unless marked.

- **Section 2.2's layer-0-excluded figures** (candidate 1: 0.722 / 0.394 /
  0.783; candidate 2: 0.444 / 0.406 / 0.450; candidate 3: 0.611 / 0.611 /
  0.633; reference: 0.533 / 0.456 / 0.406) recompute exactly, at the site sets
  it names.
- **Amendment 2's correction** (the superseded file's shuffle 95th percentile
  runs 0.050 to 0.067, not 0.056 to 0.067; highest single shuffle 0.100):
  confirmed. The superseded seed 0 file's 60 fits equal the refit's, largest
  difference 0.
- **Section 5, item 1:** layer 4 alone gives 0.478 / 0.228 / 0.600, and
  layer 0 alone at action-anchored sites gives 0.028 to 0.039. Both read off
  the table correctly.
- **Section 2.1, item 2** says a seed took "2 to 211 seconds" after the
  change. The `seconds` fields run from 2 (reference, arm M) to 211
  (candidate 1, F/0). Confirmed.

## 4. The models

MEASURED, `shasum -a 256 -c SHA256SUMS` and `shacmp.py` (appendix D).

- `verify.json` records one fingerprint per arm and seed, and every
  `fit_*.json` records the same one for its model. It is one fingerprint per
  model across all 48 fit files. Each of the twelve equals the
  `ckpt_<arm>_base_seed<n>.pt` line in
  `experiments/rehearsal-successor-measure/out-repairs/models/SHA256SUMS` on
  main: **12 of 12**.
- The label search loaded the models from the repairs worktree
  (`.claude/worktrees/w1c-rehearsal-repairs/.../out-repairs/`). They were not
  yet in git when its method was written. The fingerprints show they are
  byte-identical to the files committed since by pull request 64.
- On main, all thirty entries in `SHA256SUMS` check OK against the files: the
  fifteen of pull request 64 and the fifteen of pull request 67.

## 5. Amendment 1: the graphics processor, the processor, and figures elsewhere

### 5.1 The twelve identity checks reproduce on the graphics processor

MEASURED (appendix E). PR 66's `label_search.py --stage verify --device mps`
at `26b737f` was run from a scratch copy of the branch. Its models were the
files committed on main under `out-repairs/models/`. **All twelve arm-and-seed
pairs match the committed `fit_accuracy.own` with a largest gap of 0.** F/0
reads 0.0722, 0.1722, 0.1444, 0.1056 and 0.0667 at layers 0 to 4.

### 5.2 The failure on the processor reproduces too

MEASURED (appendix E). The same stage with `--device cpu` **fails on exactly
the four pairs** `verify_cpu_failed.json` records, by exactly its gaps: F/0
0.0056, F/1 0.0111, F/2 0.0056, M/0 0.0056. The eight other pairs match. The
differing layer fits are F/0 layer 1 0.1778 (graphics processor 0.1722), F/1
layer 3 0.1333 (0.1444), F/2 layer 1 0.1000 (0.1056) and M/0 layer 3 0.9944
(0.9889). The committed failed check and the rerun used the same models (same
fingerprints). So the amendment's explanation holds: arithmetic on the two
processors differs slightly and flips one or two near-tied held-out
predictions. The weights are not to blame.

### 5.3 Committed figures elsewhere produced on the processor

MEASURED, `nullcheck.py` (appendix F) and a sweep of every committed JSON for
a `"device"` field.

- Of the committed JSON files that record where they ran, 43 say `mps` and one
  says `cuda` (the rented slice). **None says `cpu`.** The files that record
  it are in `out-repairs/`, `out-grammar-c/`, `out/`, `lesion-results/` and
  `null-calibration/`.
- **The toy re-run's permutation baselines were fitted on the processor**, and
  their files do not record it. In `out-v3-rules/null_*.json` (pull request
  62), the per-layer `fit_accuracy` differs from the graphics-processor
  `nominate_*.json` on the same four pairs and layers as above. The values are
  the processor's: 0.1778, 0.1333, 0.1000 and 0.9944. That means the baseline
  percentiles printed beside the floor in the toy re-run's table were also
  fitted on processor states. That table is `pass2_table.md` and the findings'
  Part 1 table, for example F/0's "0.128 / 0.133". So is the "0.144 GPU refit
  / 0.133 CPU refit" remark in its section on the null.
- **Already disclosed:** the toy re-run's findings, first pass §9, say "The
  null stage's refit ran on the CPU, the nomination's on the GPU … The
  permutation nulls were fitted on the CPU states". Its check (pull request 65)
  recomputed those differences. ARGUED: this moves no verdict. The ruling on
  RT-212 makes the baseline a figure reported beside the floor, not the bar.
  And every fit and verdict in that table uses the graphics-processor
  figures. The one record gap is that `null_*.json` does not say where it ran.
- No other committed output was found to have been made on the processor. The
  sweep covers the files that record a device and the toy re-run's baselines.
  It cannot rule out an older output that records nothing.

## 6. The closing plain-language paragraph (findings, section 7)

Sentence by sentence, against the committed files.

| sentence | status |
|---|---|
| "No." | ARGUED. It answers route (b)'s question: is there a label the own-directed loss forces, readable at four fifths on arm F? For the three candidates, the answer is MEASURED no. |
| "The free system carries three things that its own-directed task forces on it" | **ARGUED, not MEASURED.** "Carries" is measured: every best fit beats all 200 shuffles. "Forces" is the method's argument (section 1). For candidate 1 it is weakest: the action needs only one of the two own turns, which is why the method added candidate 2 as "only the one turn the own-directed action needs". |
| "A straight-line read recovers each one far above chance on arm F" | MEASURED. The lowest arm F best fit is 0.450, against a highest shuffle of 0.239 for that label. |
| "but none of them gets to four fifths at any site on any seed" | MEASURED. The highest is 0.789. |
| "It reaches 0.73 in the tokens of the action turn at the first two layers on one seed" | MEASURED (0.733, layers 0–1, `action+3`, seed 0). Worth adding that layer 0 there is excluded under RT-216; layer 1 alone gives 0.722. |
| "and 0.79 averaged over the post-identity span on another … the method had already said a fit there proves little" | MEASURED (0.789, seed 2), and the method did say it before any output. |
| "On the third seed it never passes 0.48" | **Slightly wrong as written.** The seed 1 best is 0.4833, which passes 0.48. "Never passes 0.49" or "reaches at most 0.48" is right. |
| "The model's own value on the asked item reaches 0.61 to 0.63 at the action, a little above how often the arm answers correctly" | MEASURED against 0.551 to 0.560. The best sites are `action` or `action+ans`, so "at the action or the token before it" is more exact. |
| "The ruled label reads perfectly on arms T and M and nearly so on arm C" | MEASURED. Every site set on T and M is at 1.000 or within 0.044 of it. C reaches 1.000 at its best site on every seed, so "nearly" undersells it slightly but is not wrong. |
| "and is near chance at arm F's fixed-extent sites" | **Not MEASURED as written.** The best action-anchored fits are 0.206 / 0.144 / 0.211. Blind guessing gives 0.083 and the shuffle mean is 0.08. On seeds 0 and 2, 18 and 17 action-anchored site sets beat every one of the 200 shuffles. "Far below the floor, though above the shuffled-label level on two seeds" is what the files show. (ARGUED: the best of 45 site sets is flattered by being the best of many, so the gap over the shuffles is an upper bound. It is still not "near chance".) |
| "At toy scale, then, no read the free system is forced to carry clears the floor on arm F, on any of the 60 site sets." | **Wider than what was measured.** Three reads were tried, chosen in advance under a stop rule that forbade a fourth. "None of the three candidates the method allowed clears the floor on arm F, at any of the 60 site sets" is MEASURED, and is how the findings' own section 1 puts it. "No read … forced to carry" claims every such label. |

ARGUED: none of the three corrections moves a verdict. The last one matters
most, because this paragraph is what John reads to decide whether "no verdict
on the free arm" is worth registering (RT-212 ruling, item 3). As written, it
reads as a general impossibility at toy scale. What was shown is that the
three labels the method named do not clear.

## 7. What was opened, and what was not

- Opened: every commit on `62c3824..26b737f`; the method, both amendments and
  the findings in full; `label_search.py` at `26b737f` and its diffs at
  `53240d4..609260b`; every `out-label-search/` JSON; `repairs.fit_reads`,
  `repairs.nominate` and `rerun_v3.verdicts` / `pass2_verdict` on main; the
  toy re-run findings' Part 1 table and first pass §9; the RT-212 and RT-216
  rulings with refinement 2; proposal version 2 section 7.2;
  `out-v3-rules/null_*.json` and `nominate_*.json`; `SHA256SUMS` and the
  thirty model files.
- Ran: the verify stage twice (graphics processor, then processor). No
  candidate fit was rerun. ARGUED: the fits are
  deterministic given the features, and section 5.1 shows the features
  reproduce, but the 60-site fits themselves were only recomputed from the
  committed numbers, not refitted.
- Not checked: `label_search_report.py`'s rendering beyond the cells compared
  in section 3; the gate figures in the findings' context table (read from the
  repairs' `gate_base.json`, already checked by pull request 65).

## Appendix

Scripts ran with the repository's `.venv` Python from the scratch folder
`$CLAUDE_JOB_DIR/tmp/`. Their inputs were `pr66/` (`git archive 26b737f`,
unpacked) and this worktree at `da41c20`. The scripts are reproduced so the
figures can be checked without the scratch folder.

### A. Commit order

```
$ git log --format='%h %ad %s' --date=iso-strict --reverse origin/main..origin/w1d-free-arm-label-search
583b3f2 2026-09-26T07:34:15-07:00 Method for the free-arm label search (RT-212 route b), before any code
883bc81 2026-09-26T07:36:16-07:00 Free-arm label search driver, before any output
88ab899 2026-09-26T07:38:16-07:00 Method amendment 1: forward passes on mps, after the identity check failed on the processor
53240d4 2026-09-26T07:38:40-07:00 Label search: forward passes on mps (method amendment 1); keep the failed processor-run identity check
6c82c81 2026-09-26T09:56:06-07:00 Method amendment 2 (ruled by John): null of 200 shuffles at each arm and seed's best site only
609260b 2026-09-26T09:56:48-07:00 Label search: fit all 60 site sets, null of 200 shuffles at the best one (amendment 2); report tables
fd7f5fa 2026-09-26T10:09:33-07:00 Label search output: candidate 1 (which two turns are the model's own) on arms F, T, C, M
63f1ead 2026-09-26T10:11:24-07:00 Label search output: candidate 2 (which turn holds the model's own value on the asked item) on arms F, T, C, M
54ee9b0 2026-09-26T10:19:24-07:00 Label search output: candidate 3 (the model's own value on the asked item) and the ruled label's reference row
26b737f 2026-09-26T10:22:33-07:00 Findings: free-arm label search at toy scale (RT-212 route b)
$ git merge-base origin/main origin/w1d-free-arm-label-search
62c38244d0154e5e21f359e0c676e7430269d772
```

Files per commit (`git show --stat`): `583b3f2` method only; `883bc81`
`src/label_search.py` only; `88ab899` method only; `53240d4`
`out-label-search/verify_cpu_failed.json`, `src/label_search.py`; `6c82c81`
method, `out-label-search/superseded_fit_own-turn-pair_F_seed0_every-site-100-shuffles.json`,
`out-label-search/verify.json`; `609260b` `src/label_search.py`,
`src/label_search_report.py`; `fd7f5fa` twelve `fit_own-turn-pair_*` and
`verdict_own-turn-pair.json`; `63f1ead` twelve `fit_own-source-turn_*` and its
verdict; `54ee9b0` twelve `fit_marker-word_*`, twelve `fit_own-value_*` and
both verdicts; `26b737f` findings only.

### B. `recompute.py` (sections 3, 4, 5) and its output

```python
import json, os, glob
import numpy as np
os.chdir("/Users/john/.claude/jobs/22692952/tmp")
O = "pr66/experiments/rehearsal-successor-measure/out-label-search"
FIX = ("action", "action+ans", "action+3")
labs = ["own-turn-pair", "own-source-turn", "own-value", "marker-word"]
def lf(L): return f"{L[0]}" if len(L)==1 else f"{L[0]}-{L[-1]}"
for lab in labs:
    print("=====", lab)
    for arm in "FTCM":
        for s in (0,1,2):
            d = json.load(open(f"{O}/fit_{lab}_{arm}_seed{s}.json"))
            sites = d["sites"]
            fits = [x["fit"] for x in sites]
            bi = int(np.argmax(fits)); b = sites[bi]
            fx = max((x for x in sites if x["positions"] in FIX), key=lambda x: x["fit"])
            nv = np.array(d["null"]["values"])
            clears = [x for x in sites if x["fit"] >= 0.8 and x["fit"] > nv.max()]
            flag = [x for x in sites if x["clears"]]
            assert len(clears) == len(flag)
            assert b["layers"] == d["best_site"]["layers"] and b["positions"] == d["best_site"]["positions"]
            print(...)  # one line per arm and seed, as below
    v = json.load(open(f"{O}/verdict_{lab}.json"))
    print("verdict F:", ...)
# candidate 1 on F: fits above 0.78; the superseded file against the refit;
# fingerprints per model across all fit files; verify.json and verify_cpu_failed.json
```

```
===== own-turn-pair
F/0 best 0.733 @ 0-1 action+3      fixed 0.733 @ 0-1 action+3   null n=200 mean 0.037 p95 0.061 max 0.100 ge_best 0 clear 0 above_all_shuffles 57
F/1 best 0.483 @ 0-1 post-identity fixed 0.383 @ 1 action+3   null n=200 mean 0.035 p95 0.061 max 0.083 ge_best 0 clear 0 above_all_shuffles 56
F/2 best 0.789 @ 0-1 post-identity fixed 0.478 @ 2 action+ans null n=200 mean 0.036 p95 0.061 max 0.078 ge_best 0 clear 0 above_all_shuffles 57
T/0 best 0.289 @ 0-4 post-identity fixed 0.067 @ 0 action     null n=200 mean 0.034 p95 0.061 max 0.078 ge_best 0 clear 0 above_all_shuffles 15
T/1 best 0.294 @ 3 post-identity fixed 0.067 @ 0 action     null n=200 mean 0.035 p95 0.056 max 0.078 ge_best 0 clear 0 above_all_shuffles 15
T/2 best 0.283 @ 0-4 post-identity fixed 0.067 @ 0 action     null n=200 mean 0.033 p95 0.056 max 0.083 ge_best 0 clear 0 above_all_shuffles 15
C/0 best 0.411 @ 0-1 post-identity fixed 0.406 @ 1-2 action+ans null n=200 mean 0.036 p95 0.061 max 0.078 ge_best 0 clear 0 above_all_shuffles 57
C/1 best 0.522 @ 0-1 post-identity fixed 0.389 @ 0-1 action+3   null n=200 mean 0.038 p95 0.061 max 0.100 ge_best 0 clear 0 above_all_shuffles 31
C/2 best 0.428 @ 0-1 post-identity fixed 0.211 @ 0-1 action+3   null n=200 mean 0.035 p95 0.061 max 0.078 ge_best 0 clear 0 above_all_shuffles 34
M/0 best 0.311 @ 0-1 post-identity fixed 0.083 @ 2 action+3   null n=200 mean 0.036 p95 0.061 max 0.078 ge_best 0 clear 0 above_all_shuffles 16
M/1 best 0.372 @ 0-1 post-identity fixed 0.150 @ 0-1 action+ans null n=200 mean 0.036 p95 0.061 max 0.089 ge_best 0 clear 0 above_all_shuffles 21
M/2 best 0.411 @ 0-1 post-identity fixed 0.244 @ 0-1 action+3   null n=200 mean 0.037 p95 0.067 max 0.083 ge_best 0 clear 0 above_all_shuffles 49
verdict F: {'clears_over_all_60': False, 'clears_over_fixed_extent_45': False, 'seeds_with_some_clearing_site': 0} fails_F True
===== own-source-turn
F/0 best 0.450 @ 0 post-identity fixed 0.356 @ 0-2 action+3   null n=200 mean 0.128 p95 0.183 max 0.233 ge_best 0 clear 0 above_all_shuffles 49
F/1 best 0.450 @ 0 post-identity fixed 0.311 @ 0-1 action+3   null n=200 mean 0.129 p95 0.184 max 0.239 ge_best 0 clear 0 above_all_shuffles 26
F/2 best 0.456 @ 0 post-identity fixed 0.417 @ 0-1 action+ans null n=200 mean 0.129 p95 0.183 max 0.233 ge_best 0 clear 0 above_all_shuffles 57
T/0 best 0.411 @ 0 post-identity fixed 0.228 @ 0-4 action+3   null n=200 mean 0.124 p95 0.167 max 0.217 ge_best 0 clear 0 above_all_shuffles 18
T/1 best 0.400 @ 0-1 post-identity fixed 0.194 @ 2-4 action+3   null n=200 mean 0.129 p95 0.172 max 0.200 ge_best 0 clear 0 above_all_shuffles 15
T/2 best 0.400 @ 0-2 post-identity fixed 0.200 @ 0-1 action+3   null n=200 mean 0.124 p95 0.183 max 0.228 ge_best 0 clear 0 above_all_shuffles 15
C/0 best 0.433 @ 0 post-identity fixed 0.383 @ 0-1 action+ans null n=200 mean 0.127 p95 0.183 max 0.244 ge_best 0 clear 0 above_all_shuffles 57
C/1 best 0.456 @ 0 post-identity fixed 0.294 @ 0-1 action+3   null n=200 mean 0.128 p95 0.184 max 0.217 ge_best 0 clear 0 above_all_shuffles 30
C/2 best 0.439 @ 0 post-identity fixed 0.306 @ 1 action+3   null n=200 mean 0.128 p95 0.183 max 0.244 ge_best 0 clear 0 above_all_shuffles 19
M/0 best 0.417 @ 0 post-identity fixed 0.211 @ 1 action+ans null n=200 mean 0.124 p95 0.172 max 0.194 ge_best 0 clear 0 above_all_shuffles 12
M/1 best 0.367 @ 0 post-identity fixed 0.222 @ 1 action+3   null n=200 mean 0.124 p95 0.172 max 0.194 ge_best 0 clear 0 above_all_shuffles 21
M/2 best 0.378 @ 0 post-identity fixed 0.278 @ 0-1 action+ans null n=200 mean 0.123 p95 0.178 max 0.189 ge_best 0 clear 0 above_all_shuffles 39
verdict F: {'clears_over_all_60': False, 'clears_over_fixed_extent_45': False, 'seeds_with_some_clearing_site': 0} fails_F True
===== own-value
F/0 best 0.611 @ 4 action+ans    fixed 0.611 @ 4 action+ans null n=200 mean 0.125 p95 0.167 max 0.189 ge_best 0 clear 0 above_all_shuffles 57
F/1 best 0.611 @ 1-2 action        fixed 0.611 @ 1-2 action     null n=200 mean 0.130 p95 0.178 max 0.239 ge_best 0 clear 0 above_all_shuffles 57
F/2 best 0.633 @ 0-3 action+ans    fixed 0.633 @ 0-3 action+ans null n=200 mean 0.122 p95 0.172 max 0.200 ge_best 0 clear 0 above_all_shuffles 57
T/0 best 0.344 @ 0-3 post-identity fixed 0.206 @ 0-3 action+3   null n=200 mean 0.128 p95 0.172 max 0.189 ge_best 0 clear 0 above_all_shuffles 25
T/1 best 0.361 @ 1-3 post-identity fixed 0.250 @ 4 action+3   null n=200 mean 0.128 p95 0.172 max 0.206 ge_best 0 clear 0 above_all_shuffles 40
T/2 best 0.350 @ 2-3 post-identity fixed 0.211 @ 2-4 action+ans null n=200 mean 0.126 p95 0.172 max 0.200 ge_best 0 clear 0 above_all_shuffles 21
C/0 best 0.578 @ 2-3 action+3      fixed 0.578 @ 2-3 action+3   null n=200 mean 0.129 p95 0.178 max 0.250 ge_best 0 clear 0 above_all_shuffles 57
C/1 best 0.600 @ 3-4 action        fixed 0.600 @ 3-4 action     null n=200 mean 0.128 p95 0.178 max 0.261 ge_best 0 clear 0 above_all_shuffles 50
C/2 best 0.578 @ 1-4 action+3      fixed 0.578 @ 1-4 action+3   null n=200 mean 0.124 p95 0.172 max 0.211 ge_best 0 clear 0 above_all_shuffles 57
M/0 best 0.478 @ 0-4 action+3      fixed 0.478 @ 0-4 action+3   null n=200 mean 0.125 p95 0.172 max 0.211 ge_best 0 clear 0 above_all_shuffles 51
M/1 best 0.394 @ 3-4 action+3      fixed 0.394 @ 3-4 action+3   null n=200 mean 0.127 p95 0.178 max 0.206 ge_best 0 clear 0 above_all_shuffles 49
M/2 best 0.467 @ 0-3 action        fixed 0.467 @ 0-3 action     null n=200 mean 0.126 p95 0.167 max 0.183 ge_best 0 clear 0 above_all_shuffles 57
verdict F: {'clears_over_all_60': False, 'clears_over_fixed_extent_45': False, 'seeds_with_some_clearing_site': 0} fails_F True
===== marker-word
F/0 best 0.556 @ 0-1 post-identity fixed 0.206 @ 2 action+3   null n=200 mean 0.082 p95 0.122 max 0.144 ge_best 0 clear 0 above_all_shuffles 33 | L1 action 0.172
F/1 best 0.483 @ 0-1 post-identity fixed 0.144 @ 3 action     null n=200 mean 0.083 p95 0.117 max 0.156 ge_best 0 clear 0 above_all_shuffles 15 | L1 action 0.067
F/2 best 0.433 @ 0 post-identity fixed 0.211 @ 0-1 action+ans null n=200 mean 0.079 p95 0.117 max 0.156 ge_best 0 clear 0 above_all_shuffles 32 | L1 action 0.106
T/0 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.085 p95 0.211 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
T/1 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.086 p95 0.217 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
T/2 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.086 p95 0.211 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
C/0 best 1.000 @ 0-1 action+ans    fixed 1.000 @ 0-1 action+ans null n=200 mean 0.082 p95 0.128 max 0.156 ge_best 0 clear 57 above_all_shuffles 57 | L1 action 0.994
C/1 best 1.000 @ 0-1 action+ans    fixed 1.000 @ 0-1 action+ans null n=200 mean 0.085 p95 0.128 max 0.150 ge_best 0 clear 56 above_all_shuffles 57 | L1 action 0.983
C/2 best 1.000 @ 0-1 action+ans    fixed 1.000 @ 0-1 action+ans null n=200 mean 0.083 p95 0.122 max 0.161 ge_best 0 clear 57 above_all_shuffles 57 | L1 action 0.978
M/0 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.085 p95 0.211 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
M/1 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.085 p95 0.211 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
M/2 best 1.000 @ 0 action        fixed 1.000 @ 0 action     null n=200 mean 0.085 p95 0.211 max 0.267 ge_best 0 clear 60 above_all_shuffles 60 | L1 action 1.000
verdict F: {'clears_over_all_60': False, 'clears_over_fixed_extent_45': False, 'seeds_with_some_clearing_site': 0} fails_F True
===== cand1 F fits > 0.78, and fixed-extent maxima
0 [] max non-post-identity 0.7333 max any 0.7333
1 [] max non-post-identity 0.3833 max any 0.4833
2 [('0-1', 'post-identity', 0.7889), ('1', 'post-identity', 0.7833)] max non-post-identity 0.4778 max any 0.7889
superseded vs refit largest gap 0.0
superseded p95 range 0.05 0.06694444444444443 max shuffle 0.1 n shuffles 100
verify all_match True {'C/0': 0.0, 'C/1': 0.0, 'C/2': 0.0, 'F/0': 0.0, 'F/1': 0.0, 'F/2': 0.0, 'M/0': 0.0, 'M/1': 0.0, 'M/2': 0.0, 'T/0': 0.0, 'T/1': 0.0, 'T/2': 0.0}
cpu all_match False {'F/0': 0.0056, 'F/1': 0.0111, 'F/2': 0.0056, 'M/0': 0.0056}
cpu sha same as mps: True
```

(The fingerprint-per-model lines, one fingerprint for each of the twelve
models across all its fit files, are in appendix D.)

### C. `extra.py` (sections 1.2, 2.2, 3.3, 6) and its output

```python
# as recompute.py for paths; then:
# 1. arm F best per seed with layer 0 allowed only at 'action' (RT-216)
# 2. sum of the 'seconds' field per label and arm
# 3. ruled label on arm F: top three action-anchored fits, the best site's
#    shuffle mean and maximum, the per-layer 'action' fits, and how many
#    action-anchored site sets beat every shuffle
# 4. any arm F site set at 0.8 or above, any label
```

```
== RT-216 exclusion (layer 0 allowed only at 'action'), arm F best per seed
own-turn-pair 0.722 (1 action+3) | 0.394 (1 post-identity) | 0.783 (1 post-identity)
own-source-turn 0.444 (1 post-identity) | 0.406 (1 post-identity) | 0.450 (1 post-identity)
own-value 0.611 (4 action+ans) | 0.611 (1-2 action) | 0.633 (1-3 action+ans)
marker-word 0.533 (1-2 post-identity) | 0.456 (1 post-identity) | 0.406 (1 post-identity)
== seconds per label and arm (sum over seeds)
own-turn-pair ['F 309', 'T 85', 'C 157', 'M 185'] total 737s = 12.3 min
own-source-turn ['F 29', 'T 26', 'C 15', 'M 21'] total 91s = 1.5 min
own-value ['F 95', 'T 40', 'C 60', 'M 83'] total 277s = 4.6 min
marker-word ['F 77', 'T 8', 'C 76', 'M 5'] total 166s = 2.8 min
== ruled label arm F: fixed-extent best vs its seed's best-site null; per-layer action fits
0 [('2', 'action+3', 0.2056), ('0-1', 'action+ans', 0.2), ('1', 'action+ans', 0.2)] null mean 0.082 max 0.144 per-layer action L0..L4 [0.0722, 0.1722, 0.1444, 0.1056, 0.0667] fixed-extent sites above null max 18
1 [('3', 'action', 0.1444), ('1', 'action+3', 0.1278), ('0-1', 'action+3', 0.1222)] null mean 0.083 max 0.156 per-layer action L0..L4 [0.0722, 0.0667, 0.1167, 0.1444, 0.1167] fixed-extent sites above null max 0
2 [('0-1', 'action+ans', 0.2111), ('0-2', 'action+ans', 0.2111), ('1', 'action+ans', 0.2111)] null mean 0.079 max 0.156 per-layer action L0..L4 [0.0722, 0.1056, 0.1389, 0.1111, 0.1111] fixed-extent sites above null max 17
== any arm F site >= 0.8, any label
done
```

### D. The models (section 4)

```
$ cd experiments/rehearsal-successor-measure/out-repairs/models && shasum -a 256 -c SHA256SUMS
ckpt_blind_base_seed0.pt: OK   … (all thirty lines OK, including the twelve
ckpt_{C,F,M,T}_base_seed{0,1,2}.pt and the fifteen of pull request 67)
```

`shacmp.py` compares `verify.json`'s twelve fingerprints with the
`ckpt_<arm>_base_seed<n>.pt` lines of `SHA256SUMS`:

```
C/0 ckpt_C_base_seed0.pt MATCH
C/1 ckpt_C_base_seed1.pt MATCH
C/2 ckpt_C_base_seed2.pt MATCH
F/0 ckpt_F_base_seed0.pt MATCH
F/1 ckpt_F_base_seed1.pt MATCH
F/2 ckpt_F_base_seed2.pt MATCH
M/0 ckpt_M_base_seed0.pt MATCH
M/1 ckpt_M_base_seed1.pt MATCH
M/2 ckpt_M_base_seed2.pt MATCH
T/0 ckpt_T_base_seed0.pt MATCH
T/1 ckpt_T_base_seed1.pt MATCH
T/2 ckpt_T_base_seed2.pt MATCH
12 of 12
```

Every `fit_*.json` for a model records the same fingerprint as `verify.json`,
for example F/0 `c3afe0c6…ea88d`, F/1 `2e51df7e…cb219b`, F/2 `d5b59d8b…683b1`.

### E. The identity check rerun (section 5)

From a scratch copy of `26b737f`, with `verify.json` removed first, models
from `out-repairs/models/` on main:

```
$ python label_search.py --stage verify --device mps --ckpt-dir <worktree>/experiments/rehearsal-successor-measure/out-repairs/models
  F/0: 0.0722 0.1722 0.1444 0.1056 0.0667   largest gap to committed 0.00e+00  MATCH
  F/1: 0.0722 0.0667 0.1167 0.1444 0.1167   largest gap to committed 0.00e+00  MATCH
  F/2: 0.0722 0.1056 0.1389 0.1111 0.1111   largest gap to committed 0.00e+00  MATCH
  T/0: 1.0000 1.0000 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  T/1: 1.0000 1.0000 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  T/2: 1.0000 1.0000 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  C/0: 0.0722 0.9944 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  C/1: 0.0722 0.9833 0.9667 0.9833 0.9611   largest gap to committed 0.00e+00  MATCH
  C/2: 0.0722 0.9778 0.9833 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  M/0: 1.0000 1.0000 1.0000 0.9889 0.9889   largest gap to committed 0.00e+00  MATCH
  M/1: 1.0000 1.0000 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  M/2: 1.0000 1.0000 1.0000 1.0000 1.0000   largest gap to committed 0.00e+00  MATCH
  identity check: all twelve match

$ python label_search.py --stage verify --device cpu --ckpt-dir <same>
  F/0: 0.0722 0.1778 0.1444 0.1056 0.0667   largest gap to committed 5.56e-03  DIFFERS
  F/1: 0.0722 0.0667 0.1167 0.1333 0.1167   largest gap to committed 1.11e-02  DIFFERS
  F/2: 0.0722 0.1000 0.1389 0.1111 0.1111   largest gap to committed 5.56e-03  DIFFERS
  T/0 … T/2, C/0 … C/2, M/1, M/2: as above, MATCH
  M/0: 1.0000 1.0000 1.0000 0.9944 0.9889   largest gap to committed 5.56e-03  DIFFERS
  identity check: FAILED — stop
```

### F. `nullcheck.py` and the device sweep (section 5.3)

```python
import json
base = ".../out-v3-rules/"
for arm in "FTCM":
    for s in (0, 1, 2):
        n = json.load(open(f"{base}null_{arm}_seed{s}.json"))
        nom = json.load(open(f"{base}nominate_{arm}_seed{s}.json"))
        # per-layer fit in the null file against the nomination file's
```

```
F 0 top keys ['arm', 'classes_present', 'held_out', 'permutations', 'seed'] False diffs gpu->null [('1', 0.1722, 0.1778)] L1 p95/p99 0.1278 0.1333
F 1 top keys [...] False diffs gpu->null [('3', 0.1444, 0.1333)] L1 p95/p99 0.1167 0.1223
F 2 top keys [...] False diffs gpu->null [('1', 0.1056, 0.1)] L1 p95/p99 0.1167 0.1333
T 0, T 1, T 2, C 0, C 1, C 2, M 1, M 2: diffs gpu->null []
M 0 top keys [...] False diffs gpu->null [('3', 0.9889, 0.9944)] L1 p95/p99 0.1222 0.1389
```

(`False`: the null file records no device.)

```
$ grep -rhoE '"device": *"[a-z]+"' experiments --include='*.json' | sort | uniq -c
   1 "device": "cuda"
  43 "device": "mps"
```
