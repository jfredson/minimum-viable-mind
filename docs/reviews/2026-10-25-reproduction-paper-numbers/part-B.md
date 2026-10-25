# Part B: experiment 06 (MVM-0a) and Amendment A3, paper lines 399–637 and 1085–1116

Checked 2026-10-25 against the clean clone at `dacc7b4`. Cost $0: laptop only, and no paid API calls.
Scratch scripts and outputs are in
`<clone>/../work-B/`
(referred to below as `work-B/`). All repository paths are relative to
`experiments/06-mvm-0a-constructed-self-index/` (shortened to `E/`) unless they say otherwise.

## Summary

**Counts.** 108 rows: **Reproduced 101**, **Differs 5**, **Not reproducible 2**.

**The main thing missing: none of the trained models are committed.** `artifacts/` is listed in
`.gitignore` (line 15), so it is not in the clone. `E/artifacts-fingerprints-2026-10-24.md` is the
only record of it in the repository: 15 distinct `.pt` files, about 4.6 GB, with SHA-256
fingerprints and sizes. That covers the three A3 seeds, the control pilot, the five pre-A3 30M
checkpoints and the 10M pilots. As a result, no number in this section can be regenerated from a
model.

**What is committed, and what that let me check.** The raw outputs that the models produced are
committed, and every number in the section can be recomputed from them:

- per-evaluation-seed accuracies for every Table 2 cell (six evaluation seeds per checkpoint, at
  n = 800);
- all 120 null-calibration draws per checkpoint;
- per-probe accuracies with their permutation-null mean and spread;
- per-test results of the fitted and standardised sweeps;
- the register-saturation survey;
- the lesion accuracies.

Where a row says "Reproduced", it means one of three things. Either it was recomputed from those
committed outputs, or it was rerun with a committed script that loads no model (the ceiling
measurement and the attack sweep both reproduce exactly), or it was checked with git.

Per-episode records for the A3 endpoint are not committed; only the six per-seed accuracies are.
They are enough for every mean, spread and corrected drop in Table 2.

**Differs: five rows, each explained.**

1. **"Seven hard kills were registered (K0 to K7)"** (line 463). `E/amendment-a3.md` section 4.2
   lists eight: K0, K1, K2, K3, K4, K5, K6 and K7. Either the count should read eight, or the range
   is wrong.
2. **"forty times the other seeds"** (line 479). The state-battery drop on seed 2 is 0.0769. That
   is about 43 times the pilot's 0.0018, but about 385 times seed 1's 0.0002 (roughly 77 times the
   two seeds' mean of 0.0010). The paper copies this phrase from `seeds-endpoint-findings.md`,
   line 47. It holds against the pilot only.
3. **The K1 cue-detector figures: clean 0.5097 and 0.5259, positive controls 0.9433 and 1.0000**
   (lines 589–590). The paper says these are the figures on which "the registered grammar passed".
   They are not. They come from Gate 1's **twelve-turn** grammar (`a3-gates/cue_detector_gate_a3.json`
   and `_rev2.json`, both with `n_turns` 12), which registration revision 1 then replaced with the
   **ten-turn** grammar (two of four agents revise) that every A3 checkpoint was trained on
   (`batteries-a3/batteries_meta.json`, `n_turns` 10).
   - On the ten-turn grammar, the record is `a3-gates/cue_detector_gate_a3_final.json`. Under the
     amended both-arms-agent-uniform sampler it passes: text mean 0.494 and tensor mean 0.5133 over
     five seeds; 0.5058 and 0.5217 on the registered seed, with controls 0.9873 and 1.0.
   - Under the originally registered sampler it **FAILS**: text mean 0.5395, tensor mean 0.5504
     (above the 0.55 bound), and seed 44's tensor score is 0.5814.
   - The sampler amendment says in its own text that it "was prompted by a grammar failing the old
     detector" (`E/cue-detector-sampler-amendment.md`).
   - The paper should cite the final-grammar figures and mention the sampler amendment. "K1 did not
     fire" itself still stands.
4. **"closed 103-token vocabulary"** (Methods, line 1093). That size is right for the original
   MVM-0a grammar (`encoding.py`, 103 tokens). The A3 models were built with `encoding_a3.py`,
   which adds "by" and "next" and gives **105** tokens. I checked this by building the configuration
   in `train_a3.py`, which sets `vocab = len(E.VOCAB)`. Because this Methods sentence describes the
   substrate for both designs, it needs "103 (105 under A3)".
5. **"Every primary-battery drop cleared the locked threshold by seven to nine times"**
   (line 476). This one is borderline. The means are 7.5, 7.6 and 8.6, all inside the range. But
   the individual evaluation draws run from **6.6×** (seed 1, one evaluation seed at d = 1.1811) to
   9.0×. Read as "every mean drop", the claim is correct.

**Not reproducible: two rows.**

- **The twin's T_si 0.96 and T_sr_rev 1.00** (line 436), from `twin-binding-anomaly.md`. This was
  the n = 100 training-endpoint evaluation of `pilot_a1_30m_seed1_twin.pt`, and its record is not
  committed. The committed n = 400 evaluation of the same checkpoint reads T_si 0.968 and
  T_sr_rev 1.000 (`null-calibration/null_calibration_pilot_a1_30m_seed1_twin.json` baseline, and
  `lesion-results/items_pilot_a1_30m_seed1_twin.summary.json`). That is consistent, but it is not
  the same figure. Regenerating it needs the checkpoint.
- **"about seventy processor-hours"** (line 630). This is an estimate given in
  `E/amendment-a3.md`, lines 669 and 780, and the paper matches it. A partial cross-check: the
  committed fitted sweep took 10.8 hours for 135 tests on one target.

**Cost to regenerate the checkpoints, estimated from the ledger's own rows** (RTX 5090 at $0.99 an
hour; $1.19 at the later rate):

| what | ledger basis | cost at $0.99/h | GPU time |
|---|---|---|---|
| Three A3 seeds | pilot $13.92 including $3.8 of idle time, so about $10.1 of training; seeds 1 and 2 $20.1 for the pair | about **$30** (about $36 at $1.19) | about 30 h |
| Control pilot (only for the 0.3125 figure) | | $9.9 | about 10 h |
| Five pre-A3 30M checkpoints (102,095 steps, 784M tokens each; needed for the saturation, lesion, Gate 0 and blind-arm figures) | seed-0 full $18.9 (19.07 h); waves 1 and 2 $25.29 + $31.63 for four, less $5.7 of idle time | about **$70** | about 70 h |
| **Total** | | **about $110** | about 110 GPU-hours |

**Caveat on retraining.** Training on a GPU is not bit-deterministic, so retrained models would not
match the committed fingerprints. That would be a replication, not a reproduction of these exact
numbers.

**Laptop time to re-evaluate, if the checkpoints were available**, from the `elapsed_sec` values in
the committed records:

| run | laptop time |
|---|---|
| A3 null calibration | 1.7 h |
| Five pre-A3 null calibrations and escalations | about 3.8 h |
| Fitted sweep | 10.8 h |
| Standardised refit | 10.9 h |
| Endpoints (4 checkpoints × 6 evaluation seeds × 2 conditions at n = 800; not timed in the records) | about 1–2 h, my estimate |
| Blind arm, positive control, known-answer test, saturation survey and lesions | under 1 h together |
| **Total** | **about 29–30 h on the M4** |

**Spending sums.** "About $46.75" reproduces exactly as the sum of the A3 rows' `$ actual` cells
(46.7509; script `work-B/ledger_sum.py`), with two caveats:

- $0.57 of it is three "measurement rehearsal" rented slices for a different experiment, which the
  ledger books under the A3 running total.
- The 2026-09-21 slice later billed at $0.0077 against the $0.02 written, which would make the total
  $46.74.

The $13.92 is the ledger row's figure; its two balance readings differ by $13.93, a rounding
difference.

## Table

| # | paper line | number as stated | what it is (plain words) | source in repo | how checked (command or script) | result | note |
|---|---|---|---|---|---|---|---|
| 1 | 408 | 2026-08-07 | date experiment 06 was registered | git, `E/pre-registration.md` | `git log -- E/pre-registration.md` → `435c904` 2026-08-07 21:36 "REGISTRATION: ... v1.0 is binding" | Reproduced | |
| 2 | 417 | 2026-08-09 | date of Amendment A1 | git | `a11b434` 2026-08-09 "REGISTERED AMENDMENT A1" | Reproduced | |
| 3 | 420 | 2026-08-16 | date of Amendment A2 | git | `23c9af9` 2026-08-16 "Amendment A2 REGISTERED (scale 30M, cap $400)" | Reproduced | |
| 4 | 421 | 30 million parameters | model size fixed by A2 | `E/src/model.py` SCALES['30M'], `E/src/launch_a3.sh` | built the model: A3 register-less 30M = 29,277,248 parameters; register-bearing A1 = 39,204,192 (ledger) | Reproduced | a size class label; the actual counts are 29.3M (A3) and 39.2M (A1) |
| 5 | 422 | 10-million pilot failed | the smaller pilot did not reach ceiling | `E/pilot-a1-10m-seed0-eval.jsonl` (committed trajectory) | final row, step 22369: T_si 0.37, T_sr_rev 0.0 | Reproduced | |
| 6 | 423 | T_sr 1.00 | 30M pilot endpoint, self-reference | `E/lesion-results/register_lesion_pilot_a1_30m_seed0.json` ("none" lesion, eval seed 987654321, n = 100) | read the committed reproduction run | Reproduced | the lesion script's intact run reproduces the endpoint |
| 7 | 423 | T_si 0.93 | 30M pilot endpoint, self-index | same | same | Reproduced | |
| 8 | 424 | T_state 1.00 | 30M pilot endpoint, state | same | same | Reproduced | |
| 9 | 424 | T_syntax 1.00 | 30M pilot endpoint, syntax | same | same | Reproduced | |
| 10 | 424 | T_sr_rev 1.00 | 30M pilot endpoint, revised self-reference | same | same | Reproduced | |
| 11 | 425 | $200 to $400 | spending cap raised by A2 | `E/compute-ledger.md` top-up paragraph of 2026-08-16; commit `23c9af9` | read | Reproduced | a documentary fact |
| 12 | 429 | 7.6 × 10⁻⁸ | across-episode spread of the register writer, seed 0 | `E/a3-gates/register_saturation_survey.json` | per-turn `across_episode_sd_mean` from turn 3 on: 7.60e-08 to 7.63e-08 | Reproduced | regenerating it needs `pilot_a1_30m_seed0.pt` (not committed) |
| 13 | 430 | 2.8 × 10⁻⁸ | same, seed 1 | same | 2.81e-08 to 2.82e-08 | Reproduced | |
| 14 | 430 | 5.9 × 10⁻⁸ | same, seed 2 | same | 5.93e-08 | Reproduced | |
| 15 | 432 | ≥ 0.99 | every battery with the register's injection removed, except T_si | `E/lesion-results/register_lesion_pilot_a1_30m_seed0.json`, lesion "no-xattn" | eval seed 987654321: T_sr 1.0, T_state 1.0, T_syntax 1.0, T_sr_rev 1.0; eval seed 20260819: T_state 0.99, T_si 0.99 | Reproduced | n = 100 per evaluation seed |
| 16 | 433 | 0.93 to 0.94 | T_si intact against no-injection, registered evaluation seed | same | "none" T_si 0.93 → "no-xattn" T_si 0.94 | Reproduced | |
| 17 | 436 | T_si 0.96, T_sr_rev 1.00 | register-less twin at ceiling | `E/twin-binding-anomaly.md` line 54; ledger wave-2 row | n = 100 endpoint record not committed; committed n = 400 reads 0.968 and 1.000 (`null_calibration_pilot_a1_30m_seed1_twin.json` baseline) | Not reproducible | matches findings file; regenerating needs `pilot_a1_30m_seed1_twin.pt`, about $13 of retraining, then minutes on the laptop |
| 18 | 438 | four of nine launches | where the five-seed run was halted | ledger rows "wave 1/5" and "wave 2/5" (2 launches each); `3cd82d9` "9 launches remain" | counted | Reproduced | |
| 19 | 445 | 2026-09-15 | date Amendment A3 was registered | git | `12900ef` 2026-09-15 16:57 "REGISTRATION COMMIT: Amendment A3 registered with fourteen revisions" | Reproduced | |
| 20 | 449 | 0.2921 | the ownership-blind ceiling on the primary battery | `E/src/ceiling_measure_a3.py`, `E/src/shortcut_sweep.py` (neither loads a model) | reran both: `work-B/ceiling_measure_a3.rerun.json` is byte-identical to the committed record (known-answer check: measured 0.2921); `work-B/shortcut_sweep.rerun.json` gives an analytic 0.2925, best rule 0.2923 | Reproduced | the learned attack reached 0.2993 (n = 4000) and 0.3036 (registered n = 12000), above 0.2921; the amendment calls this one standard error |
| 21 | 459 | rank 16 | largest subspace rank searched | `null-calibration/a3_pilot_seed0.json` `pre_commitments.ks` = [4, 8, 16] | read | Reproduced | |
| 22 | 463 | Seven hard kills (K0 to K7) | number of registered kill criteria | `E/amendment-a3.md` section 4.2 | counted the list: K0, K1, K2, K3, K4, K5, K6, K7 = **8** | **Differs** | eight are listed; "seven" is wrong, or the range is |
| 23 | 469 | θ = 0.1777 | locked threshold, primary battery | `null-calibration/a3_pilot_seed0.json` (120 draws) | `work-B/theta_recompute.py`: recomputed each draw's d from raw accuracy and ceilings (0 mismatches), then ran the committed `summarize()` → p95 = 0.1777 | Reproduced | lock file `theta_delta.lock.json` matches; SHA-256 of the calibration record matches the lock |
| 24 | 469 | 0.1172 | locked threshold, state battery | same | same → 0.1172 | Reproduced | |
| 25 | 468 | 2026-09-16, before any localised read | threshold lock | git `6ad4362` | `git show --stat 6ad4362`: 2026-09-16 20:08 -0700, adds only `null-calibration/theta_delta.lock.json`; the calibration it locks is `35a714f` (16:42, earlier); the first localised A3 read, `4318bfd` blind_control_a3.json, is 21:35, later | Reproduced | the commit exists, touches the named file and is ordered as claimed |
| 26 | 474 | $13.92 | cost of the A3 pilot | ledger row 2026-09-15 Gate 2 | read; balance arithmetic 126.05 − 112.12 = 13.93 | Reproduced | $0.01 rounding between the row and its balance readings |
| 27 | 476 | seven to nine times | primary drop against θ | three endpoint records | `work-B/table2_recompute.py`: 7.52, 7.55, 8.60 | **Differs** (borderline) | true of the means; individual evaluation-seed drops run 6.65× to 9.03×, so "every drop" is not strictly 7–9× |
| 28 | 477 | above 1.0 | the lesion takes the battery below the ownership-blind ceiling | same | all 18 per-evaluation-seed d values are between 1.18 and 1.60 | Reproduced | |
| 29 | 479 | 0.0769 | state-battery drop on seed 2 | `a3-gates/endpoint_a3_30m_seed2.json` | recomputed mean d over six seeds = 0.0769 | Reproduced | this is the ceiling-corrected d; the raw accuracy fall is 0.0712 |
| 30 | 479 | forty times the other seeds | seed 2 state drop against the others | Table 2 | 0.0769 / 0.0018 = 43; 0.0769 / 0.0002 = 385 | **Differs** | true against the pilot only; matches `seeds-endpoint-findings.md` line 47, which carries the same imprecision |
| 31 | 480 | inside its 0.1172 threshold | | | 0.0769 < 0.1172 | Reproduced | |
| 32 | 487 | six evaluation seeds, n = 800 | Table 2 basis | endpoint records | `per_seed` has 6 entries (seeds 771000 to 771185), `eval_n` 800 | Reproduced | |
| 33 | 494 | 0.5683 (sd 0.0076) | pilot T_act intact | `a3-gates/endpoint_validation_pilot.json` `per_seed` | `work-B/table2_recompute.py` | Reproduced | sample sd |
| 34 | 494 | 0.1988 (sd 0.0173) | pilot T_act under L0 | same | same | Reproduced | |
| 35 | 494 | 1.337 (sd 0.057) | pilot corrected drop | same | per-seed (intact − lesioned)/(intact − 0.2921), then mean and sd | Reproduced | |
| 36 | 494 | 7.5× | pilot drop / θ | same | 1.3370 / 0.1777 = 7.52 | Reproduced | |
| 37 | 494 | +0.0018 | pilot T_state drop | same | mean d = 0.0018 | Reproduced | |
| 38 | 494 | 0.0000 | pilot T_syntax drop | same | 0.0000 | Reproduced | |
| 39 | 494 | 0.2877 (sd 0.0302) | pilot T_other intact | same | same | Reproduced | |
| 40 | 495 | 0.5633 (sd 0.0316) | seed 1 T_act intact | `a3-gates/endpoint_a3_30m_seed1.json` | same | Reproduced | |
| 41 | 495 | 0.2015 (sd 0.0215) | seed 1 T_act under L0 | same | same | Reproduced | |
| 42 | 495 | 1.342 (sd 0.103) | seed 1 corrected drop | same | 1.3422 (sd 0.1026) | Reproduced | |
| 43 | 495 | 7.6× | seed 1 drop / θ | same | 7.553 → 7.6 | Reproduced | |
| 44 | 495 | +0.0002 | seed 1 T_state drop | same | 0.0002 | Reproduced | |
| 45 | 495 | 0.0000 | seed 1 T_syntax drop | same | 0.0000 | Reproduced | |
| 46 | 495 | 0.3057 (sd 0.0281) | seed 1 T_other intact | same | same | Reproduced | |
| 47 | 496 | 0.5738 (sd 0.0284) | seed 2 T_act intact | `a3-gates/endpoint_a3_30m_seed2.json` | same | Reproduced | |
| 48 | 496 | 0.1447 (sd 0.0127) | seed 2 T_act under L0 | same | same | Reproduced | |
| 49 | 496 | 1.528 (sd 0.068) | seed 2 corrected drop | same | 1.5279 (sd 0.0676) | Reproduced | |
| 50 | 496 | 8.6× | seed 2 drop / θ | same | 8.60 | Reproduced | |
| 51 | 496 | +0.0769 | seed 2 T_state drop | same | 0.0769 | Reproduced | |
| 52 | 496 | 0.0000 | seed 2 T_syntax drop | same | 0.0000 | Reproduced | |
| 53 | 496 | 0.3195 (sd 0.0150) | seed 2 T_other intact | same | same | Reproduced | |
| 54 | 499 | 0.506 | pilot intact, default evaluation seed | `a3-gates/pilot_endpoint.json`, `endpoint_validation_pilot.json` `default_seed` | read | Reproduced | |
| 55 | 499 | 0.182 | pilot lesioned, default seed | same | read | Reproduced | |
| 56 | 500 | 1.515 | its corrected drop | | (0.506 − 0.182)/(0.506 − 0.2921) = 1.5147 | Reproduced | |
| 57 | 505 | 0.3227 | the control's recorded ceiling | `batteries-a3/batteries_meta.json`; lock file; ceiling rerun | rerun reproduces 0.3227 (known-answer check S2) | Reproduced | |
| 58 | 507 | 2026-09-17 | date the defect was registered | git `45ca78a` 2026-09-17 09:57 "REGISTERED DEFECT" | git log | Reproduced | |
| 59 | 511 | 1.0000 (both solvers) | true ownership-blind ceiling on the control | `E/src/ceiling_measure_a3.py` | reran (`work-B/ceiling_measure_a3.rerun.json`): S1 1.0, S3 1.0; identical to the committed `a3-gates/ceiling_measure_a3.json` | Reproduced | loads no model; about 4 s |
| 60 | 513 | 0.10 | floor rule margin | `null-calibration/a3_pilot_seed0.json` `pre_commitments.floor_margin` 0.1 | read | Reproduced | |
| 61 | 520 | 0.2877, 0.3057, 0.3195 | control battery on the three seeds | as rows 39, 46 and 53 | | Reproduced | |
| 62 | 520 | 0.3227 | recorded ceiling (repeat) | | | Reproduced | |
| 63 | 521 | 0.3125 (sd 0.0240) | control in the up-weighted diagnostic | `a3-gates/endpoint_a3ctl_30m_seed0.json` | `work-B/table2_recompute.py` → 0.3125 (sd 0.0240) | Reproduced | |
| 64 | 523 | 0.60 | pre-stated boundary for "learned" | `E/control-learnability-pilot.md` line 113 | git: pre-statement `7eee3c5` (2026-09-19 13:09) is earlier than the result `062636e` (2026-09-20 01:17) | Reproduced | |
| 65 | 524 | $9.9 plus $0.067 | cost of the diagnostic and of recovering its checkpoint | ledger rows 2026-09-19 and 2026-09-20 | read: "~10.0h ≈ $9.9"; recovery "$0.067 (balance $79.8897 → $79.8228)" | Reproduced | 79.8897 − 79.8228 = 0.0669 |
| 66 | 531 | $0 | cost of the null calibration | ledger row 2026-09-14 | $0.00 | Reproduced | |
| 67 | 532 | five pre-A3 checkpoints | | `null-calibration/null_calibration_pilot_a1_30m_*.json` | 5 files | Reproduced | |
| 68 | 532 | script committed before it read any checkpoint | | git | `3d08807` (script, 2026-09-14 20:02) is earlier than `02b55d5` (records, 23:51) | Reproduced | |
| 69 | 532 | 120 | content-blind ablations per checkpoint | each record has `draws` of length 120 | read | Reproduced | |
| 70 | 533 | 0.0060 | T_si null band, pilot seed-0 full | null records | ran the committed `E/src/summarize_null.py` (output `work-B/summarize_null.out`) → 0.0060 | Reproduced | every table in `gate0-null-calibration-findings.md` matches the script output |
| 71 | 533 | 0.0095 | T_si null band, seed-1 twin | same | 0.0095 | Reproduced | |
| 72 | 534 | about 0.73 | the learner/non-learner split in the same units | same, K0 table | 0.731 and 0.733 | Reproduced | |
| 73 | 536 | 52% | share of the mean-centred residual at which the binders fall apart | `null-calibration/escalation_*.json` via `summarize_null.py` | rank 128 = "52% of centred" for both | Reproduced | at 52%, the seed-0 full model falls (T_si 0.618); the seed-1 twin's T_si holds at 0.893 and its T_state falls to 0.288. "Both fall apart" is loose for the twin's ownership battery, which collapses at 75% |
| 74 | 539 | 0.25 | K0 band as applied | `null-calibration/a3_pilot_seed0.json` `k0_band`; `gate0-null-calibration-findings.md` line 347 | read | Reproduced | |
| 75 | 540 | 0.379 | the one checkpoint above 0.25 | `summarize_null.py` | seed-0 twin T_si 0.3790 | Reproduced | |
| 76 | 548 | best layer 7 | blind arm, best layer | `a3-gates/blind_arm_seed0_full.json` | read | Reproduced | |
| 77 | 548 | 0.2750 | its accuracy | same | read | Reproduced | |
| 78 | 548 | 0.2441 (sd 0.0237) | permutation null | same | read | Reproduced | |
| 79 | 549 | 1.30 sd | margin | same | (0.275 − 0.2441)/0.0237 = 1.304 | Reproduced | |
| 80 | 549 | bar of 3; chance 0.25 | | `blind-arm-findings.md` line 172; four classes | read | Reproduced | |
| 81 | 550 | −0.0739 | largest drop (an increase) | same, `d_found` | T_sr_rev d = −0.0739; largest magnitude | Reproduced | |
| 82 | 563 | −0.75, −0.54, −0.96, −0.24, −1.01 sd at layers 3, 4, 5, 7, 8 | positive-control probe margins | `a3-gates/blind_control_a3.json` | read | Reproduced | |
| 83 | 565 | 0.440 to 0.492 | primary battery under the carved ablation | same | read | Reproduced | |
| 84 | 566 | 1.000 to 0.858 | state battery under the same | same | read | Reproduced | |
| 85 | 568 | absolute drop reached θ | | same | \|d T_act\| = 0.3516 ≥ 0.1777 | Reproduced | |
| 86 | 570 | +0.052 | the movement | | 0.492 − 0.440 | Reproduced | |
| 87 | 571 | twelve draws at 400; sd 0.0284; range 0.079 | evaluation noise | `a3-gates/eval_noise_a3.json` `raw_ownership_battery` | recomputed from the 12 raw values: sd 0.0284, range 0.079 | Reproduced | |
| 88 | 572 | 1.0 against a null of 0.1306 | known-answer test | `a3-gates/known_answer_test_a3.json` | read | Reproduced | |
| 89 | 577 | eleven positions, five layers, three seeds | fitted read scope | `a3-gates/fitted_position_sweep_a3_*.json` settings | read | Reproduced | |
| 90 | 579 | 135 | discovery tests | same | `work-B/fitted_sweep_recompute.py`: 45 testable tests per seed × 3 | Reproduced | |
| 91 | 579 | 3.38 sd | family-adjusted bar | same | one-sided normal at 0.05/135 = 3.374 | Reproduced | |
| 92 | 580 | +34.0 to +53.7 sd | positive-control margins | same | marker-position margins: min 34.01, max 53.73 | Reproduced | |
| 93 | 582 | 0.2770, +3.34 sd | the MARGINAL cell, seed 2 | same | other_revision_value, layer 4: 0.277, 3.34 | Reproduced | |
| 94 | 584 | +2.33, +2.39, +3.34 | highest testable position on each seed | same | best per seed: 2.33, 2.39, 3.34, all at other_revision_value | Reproduced | |
| 95 | 586 | one episode in twenty-seven | the original sensitivity figure | same | `work-B/sensitivity_recompute.py`: median smallest-detectable share 0.0365–0.0371 = 1 in 27.0–27.4 | Reproduced | |
| 96 | 587 | about one episode in eleven | the corrected sensitivity figure | same, together with `fitted-position-sweep-findings-CORRECTION-2026-09-20.md` | (bar accuracy − 0.25)/(marker ceiling − 0.25) = 1 in 10.4–11.6 | Reproduced | my reconstruction of the correction's method; "about" holds |
| 97 | 590 | 0.000484 | accuracy margin of the one standardised crossing | `a3-gates/standardised_position_sweep_a3_a3_30m_seed2.json` | 0.2778 − (0.2496 + 3.38 × 0.0082) = 0.000484 | Reproduced | |
| 98 | 591 | 1.94 of 4,000 | the same, in episodes | | 0.000484 × 4000 = 1.94 | Reproduced | |
| 99 | 588–590 | n = 4,000; band [0.45, 0.55] | cue-detector gate size and pass band | `a3-gates/cue_detector_gate_a3*.json`; `cue-detector-sampler-amendment.md` | read | Reproduced | |
| 100 | 589–590 | clean 0.5097 and 0.5259; controls 0.9433 and 1.0000 | K1 figures for "the registered grammar" | `a3-gates/cue_detector_gate_a3.json` (12 turns) against `_final.json` (10 turns, the trained grammar) | read both records | **Differs** | figures belong to the superseded 12-turn grammar. The registered 10-turn grammar passes only under the amended sampler (0.5058/0.5217 on the registered seed; means 0.494/0.5133) and fails under the original sampler (means 0.5395/0.5504) |
| 101 | 592 | 0.214 | pilot primary above the ceiling | `pilot_endpoint.json` | 0.506 − 0.2921 = 0.2139 | Reproduced | |
| 102 | 602 | 2026-09-25 | closure | git `7b15c88` 2026-09-25 18:20 "closure text v5 appended" | git log | Reproduced | |
| 103 | 604 | fifteen serious findings, none fatal | outside reviews | `E/reviews/2026-09-21-a3-closure-gemini.md` (4 serious), `...-chatgpt.md` (11 Serious); `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md` line 16 | counted the severity labels | Reproduced | |
| 104 | 625 | about $46.75 against $100 | A3 spend | `E/compute-ledger.md` A3 rows (lines 93–104) | `work-B/ledger_sum.py`: 13.92 + 0.29 + 20.1 + 9.9 + 0.067 + 1.904 + 0.02 + 0.4974 + 0.0525 = 46.7509; the second 2026-09-25 row states "$46.75 / $100" | Reproduced | includes $0.57 of rented slices for another experiment's rehearsal; with the 09-21 slice at its billed $0.0077, the total is $46.74 |
| 105 | 630 | about seventy processor-hours | cost of the unread marker-word target | `E/amendment-a3.md` lines 669, 780 | estimate only | Not reproducible | matches the amendment; it is a forecast, not a measurement |
| 106 | 1086–1090 | 2026-08-07, 08-09, 08-16, 09-15; fourteen registration revisions; 6ad4362 on 2026-09-16; closed 2026-09-25 | Methods dates and counts | git (rows 1–3, 19, 25, 102); `amendment-a3.md` "All fourteen were ruled" | git log; the revision text counts 12 decisions + RT-20 + K0's number = 14, set out in ten numbered sections | Reproduced | |
| 107 | 1093 | 12 blocks, width 448; 103-token vocabulary | model shape | `E/src/model.py` SCALES['30M'] (448, 12 layers); `encoding.py` 103 against `encoding_a3.py` 105 | built the configuration in Python | **Differs** | shape correct; the A3 models use 105 tokens ("by" and "next" added) |
| 108 | 1099–1115 | chance 0.125; ceilings 0.2921, 0.3227, 1.0000; 400-item skeletons; n = 800, six seeds; rank ≤ 16; 120 ablations at blocks 3, 4, 5, 7, 8; 585,552,384 tokens per seed; $0.99/hour; $400 → $450 on 2026-09-25 | Methods parameters | `batteries-a3/batteries_meta.json` (chance 0.125; 4 × 400 lines); `pre_commitments`; endpoint records `tokens` 585552384 for all three seeds; ledger seeds row (20.28 pod-hours × $0.99 = $20.08); ledger ceiling note | read and arithmetic | Reproduced | the token budget was 585,544,960 (20 per parameter); the actual count runs over to the batch boundary |

### Scripts written (all in `work-B/`)

| script | what it does |
|---|---|
| `table2_recompute.py` | Table 2 means, spreads, corrected drops and ratios to θ, from the `per_seed` lists |
| `theta_recompute.py` | θ and δ from the 120 null draws, using the committed `summarize()` |
| `fitted_sweep_recompute.py` | family bar, best margins, control margins |
| `sensitivity_recompute.py` | the "1 in 27" and "1 in 11" figures |
| `ledger_sum.py` | the A3 spending sum |

Committed scripts rerun:

- `E/src/summarize_null.py`, output in `work-B/summarize_null.out`;
- `E/src/ceiling_measure_a3.py --run`, output in `work-B/ceiling_measure_a3.rerun.json`;
- `E/src/shortcut_sweep.py --run`, output in `work-B/shortcut_sweep.rerun.json`.

Run time was seconds; no model was loaded.
