# A1: paper lines 1–183, 319–398, 931–967, 1059–1083, 1226–1231

Clone at `dacc7b4`. Checked 2026-10-25. Cost $0: no model was run and no API was called.
Scripts are in `work-A1/`, next to the clone:
- `reconstruct.py` re-runs the registered bootstrap: seed 20260804, B = 10,000, using the committed `src/mvm/stats.py`.
- `build_scores.py` builds a stand-in per-item record from committed files only.
- `src/reread_under_map.py` is an unchanged copy of the committed re-read script. Its output lands in `work-A1/`.
- `run_plot.py` runs the committed `plot_removal.py` unchanged; only its two paths are redirected.
- `reconstruct_out.json` holds the bootstrap results; `figures/fig4_registered_run.png` is the regenerated figure.

## Where the per-item records live

The analysis reads `artifacts/removal_test/removal_test_scores.json` and `artifacts/removal_test/s_scores_<condition>.json`. The `artifacts/` folder is gitignored (`.gitignore`, and the comment on `config.py`'s artifacts directory), and `git log --all` shows that no such file was ever committed. The removal-test findings also say "Raw artifacts: `artifacts/removal_test/` (gitignored)". The per-item records are therefore **not committed**.

Some of the record can still be rebuilt from committed files:
- **Primary condition (index-residual, mean, k=16), task batteries: rebuilt exactly.** Three committed sources give every item:
  - the item order and categories, from the held-out battery files `src/batteries/test_*.jsonl`;
  - the baseline, which is all correct (92/92);
  - the list of items that flipped under the removal, from `removal_ci.json` ("primary_condition_flips").

  Re-running the registered bootstrap on this rebuild reproduces every committed primary-condition number exactly:
  - all three item-level intervals;
  - all three two-level intervals;
  - the router gap at both levels.

  Running the committed re-read script on it gives a primary-condition output identical, value for value, to the committed `reread-under-the-map-2026-10-24.json`.
- **Other three conditions, task batteries:** only the number of wrong items in each category is committed (in the re-read JSON), not which items they were. So I tried every placement of those wrong items that fits the committed counts. Where all placements give the same interval, the interval is fixed by committed data, and I count it as Reproduced. Where they disagree, I count it as Not reproducible and give the share of placements that match.
- **Self-report scores (d_self):** the per-item judged scores are not committed, so nothing can be rebuilt.

## Summary

| result | count |
|---|---|
| Reproduced | 83 |
| Differs | 2 |
| Not reproducible | 27 |

**Differs**
1. **Line 352, "committed seven weeks earlier".** The registered loss condition of the router control (RT-05) was first committed in `3a43bcf` on 2026-06-23, in `thresholds.md` and `pre-registration.md`. The registered run was on 2026-07-18 (`692510c`). That is 25 days, about 3.6 weeks, not seven. Even counted to the confidence-interval re-analysis (2026-08-04) it is 6 weeks. The same sentence quotes the condition as *"…void — report the router reading, do not report a center."* That wording is in the findings memo of 2026-07-18. The committed registration text of 2026-06-23 reads "…void — do not report it as a center."
2. **Lines 1067–1070: the two-level bootstrap "leaves the other intervals essentially unchanged".** The committed two-level results contradict this:
   - The primary-minus-control gap on the self-irrelevant tasks widens from [0.000, 0.312] to [−0.063, 0.469], so its lower bound crosses zero.
   - The control arm's turn-boundary interval widens from [0.000, 0.233] to [0.000, 0.333].
   - The primary condition's d_self widens from [−0.062, 0.185] to [−0.116, 0.215].
   - The primary condition's turn-boundary interval widens from [0.033, 0.267] to [0.000, 0.300].

   The figures come from `removal_ci.json` under "sensitivity_two_level", and my re-run reproduces them exactly.

**Not reproducible.** Three things are missing: the per-item records, the gate outputs, and the judge scores. Regenerating them means re-running the registered removal test on the 8-billion-parameter model.

What a re-run would cost, roughly:
- **Rented graphics card.** Five conditions (baseline plus four) over 92 task items and 30 self-report generations, plus the two gate passes (the neutral-text likelihood check and the long-generation repetition check). For scale, the 20-ablation calibration took 47 minutes and cost about $0.60 (`prelock-findings.md` §e). So about 1 to 2 hours on one rented card, roughly $1 to $3.
- **Judge calls.** About 150 Opus calls for the self-report scoring. The judge was run through the API (`docs/spending-record.md` note 107), so this is roughly $5 to $10.

The 8-billion-parameter download alone rules this out on the laptop. The tasks are scored by a fixed rule, so their scores would only need to match; the judge is not run with a fixed seed, so a re-run would not give the same judged scores.

The 30 items:
- **d_self points and intervals, all four conditions** (Table 1 and lines 371–372). Missing: per-item judged fidelity (`s_scores_*.json`). The points are consistent with the committed baseline of 0.6375.
- **The eight gate cells** (Table 1: Δnll and Δrep-4 for each of the four conditions) and **+0.347** (line 378). Missing: gate outputs. They match the findings memo.
- **Gate bound 0.0893** (line 331). Missing: `ood_calibration.json`. It matches `prelock-findings.md` §e.
- **Control-arm turn-boundary interval [0.000, 0.233]** (Table 1). Consistent: 109 of the 120 possible placements of the control's 3 wrong items give it. Missing: the item ids.
- **Gap over the control, 95% CI 0.000–0.312** (line 344). Consistent: 44 of 64 placements give it. Missing: the control's item ids.
- **Directional-condition gap, [−0.067, +0.233]** (line 351). Consistent: 2,543 of 3,000 sampled placements give it. Missing: the directional condition's item ids.
- **"2–3 features per layer"** (line 381). It matches `prelock-findings.md`; the dictionary-selection outputs are not committed.
- **"reproduced to four decimal places"** and **judge drift 0.008** (lines 1072–1073). These match the findings memo and `prelock-findings.md`; the raw runs are not committed.
- **Activation ratios 0.92–0.99** (line 1083). Found only in `STATUS-archive.md`; the outputs of `c_ctrl_checks.py` are not committed.
- **The revised account approved 2026-10-23** (line 934). That document is in another repository (sentient-horizons), which this clone does not contain.
- **Abstract: "30-million-parameter" and "three seeds"** (lines 168–170). These match the body of the paper; I did not retrain anything. They belong to the experiment-06 checker's range.

**Fig. 4:**
- **Pixels: identical.** I regenerated it from the committed `removal_ci.json` with the committed script. All 1,580,800 pixels match the committed PNG.
- **Bytes: not identical.** The only difference is the embedded "Software" tag: Matplotlib 3.11.2 here against 3.11.1 in the committed file. The file size is the same (105,516 bytes).
- **One wording point in the legend.** It says the figure shows "the RT-05 router control firing on the primary condition". The figure shows this only implicitly, through the T_sr and T_syntax panels; nothing in it marks the control as firing.

## Table

The results column says "Reproduced" for 83 rows; where the check was only against a git commit, the note says so.

| # | paper line | number as stated | what it is (plain words) | source in repo | how checked (command or script) | result | note |
|---|---|---|---|---|---|---|---|
| 1 | 3 | v0.2 was 2026-08-04 | date of the previous draft | commit `10481e2` | `git log` | Reproduced | `10481e2` "EXP-1 CI RESULT + paper v0.2", 2026-08-04 |
| 2 | 6–9 | 2026-10-17 voice and Cold Reader passes | date the v0.3 additions were checked | `drafts/2026-10-17-voice-calibration-pass-…md`, `drafts/2026-10-17-cold-reader-report-…md` | `test -f` | Reproduced | both files exist |
| 3 | 13–14 | Figs. 1–3 placeholder; Fig. 4 generated | which figures exist | `experiments/01-…/figures/` | `ls` | Reproduced | only `fig4_registered_run.png` is there |
| 4 | 17 | amendment 2026-08-04, committed before computation | order of the re-analysis registration and its result | `10afc15` (10:02:18), `10481e2` (10:10:04) | `git log`, `git show --stat` | Reproduced | the amendment commit adds `pre-registration.md` and `analyze_removal_ci.py` but no `removal_ci.json`; the result follows 8 minutes later |
| 5 | 17–18 | 95% bootstrap CIs | interval level | `removal_ci.json` config (alpha 0.05) | read JSON | Reproduced | |
| 6 | 21 | ruling of 2026-10-07, relabel 2026-10-09 | dated ruling behind the relabel | `docs/rulings/2026-10-07-two-sided-question-rulings.md` | `test -f` | Reproduced | file exists |
| 7 | 32 | experiment 06 registered 2026-08-07 | registration date | `435c904` "REGISTRATION: MVM-0a pre-registration v1.0 is binding", 2026-08-07 | `git log` | Reproduced | |
| 8 | 32–33 | A3 registered 2026-09-15 | registration date of Amendment A3 | `12900ef` "REGISTRATION COMMIT: Amendment A3", 2026-09-15 | `git log` | Reproduced | |
| 9 | 33 | A3 closed 2026-09-25 "not testable" | closure date | `7b15c88` 2026-09-25, `STATUS-archive.md` line 991, ruling file of 2026-09-25 | `git log`, grep | Reproduced | |
| 10 | 34 | experiment C registered 2026-10-09 | registration date | `e7c6f23`, merge of branch registration-commit-2026-10-09 | `git log` | Reproduced | |
| 11 | 34–35 | C stopped 2026-10-12 at stop S4b | stop date and which stop | `docs/rulings/2026-10-12-experiment-c-stop-ruling.md` | read | Reproduced | the file's title reads "Ruling 2026-10-12: experiment C stops at its registered stop S4b" |
| 12 | 37 | abstract gains four sentences | count | paper lines 167–179 | count | Reproduced | four sentences, from "We then took" to "the measure was not reached" |
| 13 | 42–43 | founding wager adopted 2026-09-20, after A, B and D had run | date ordering | `docs/rulings/2026-09-20-center-as-degree.md`, plus `692510c` (A, 2026-07-18), A3 runs mid-September (`MORNING-BRIEF-2026-09-17.md`), `29dd03f` (D's registered result, 2026-08-02) | `git log` | Reproduced | the ruling file is named and dated 2026-09-20 but was first committed 2026-09-22 (`acd8305`) |
| 14 | 53–55 | 2026-10-18 ruling on the three reserved places | ruling date | `docs/rulings/2026-10-18-paper-reserved-places-ruling.md` | `test -f` | Reproduced | |
| 15 | 76 | 0.219 | primary drop, self-irrelevant tasks (repeats row 33) | rebuilt primary record | `reconstruct.py` | Reproduced | point 0.2188 = 7/32; agrees with the body |
| 16 | 79 | six of the seven flipped | primary condition's self-irrelevant failures that are multi-step reasoning (repeats row 54) | `removal_ci.json` flips | read | Reproduced | tt02, 05, 06, 07, 08, 34 are multi-step; tt27 is instruction-following; agrees with the body |
| 17 | 80 | 6 of 8 | multi-step items flipped, of the 8 in that category | flips + battery file | count | Reproduced | agrees with the body |
| 18 | 80 | 1 of 24 | flips in the other three categories | flips + battery file | count | Reproduced | agrees with the body |
| 19 | 84 | +0.033 | router-control gap (repeats row 49) | rebuilt record | `reconstruct.py` | Reproduced | |
| 20 | 84 | 95% CI −0.133 to +0.200 | its interval (repeats row 50) | rebuilt record | `reconstruct.py` | Reproduced | exact |
| 21 | 102 | 30 million parameters | size of the constructed model (repeats abstract row 30) | `blind-arm-findings.md` | cited only | Not reproducible | not re-derived; belongs to the experiment-06 checker |
| 22 | 121–124 | 2026-10-25 note; ruling 3a of 2026-10-24 | dates | `docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`, `64eb944` (2026-10-25) | `git log` | Reproduced | |
| 23 | 129 | four wording fixes | count applied after the check | `64eb944` "apply the four wording fixes" | `git log` | Reproduced | checked against the commit message only |
| 24 | 155 | Ten adversarially generated controls | red-team items settled before the threshold lock | `red_team_ledger.md`, RT-01 to RT-10 | grep | Reproduced | 10 entries, the last dated 2026-07-12, before the lock of 2026-07-18; they are red-team findings, not all "controls" in the narrow sense |
| 25 | 157 | d = 0.219 | primary drop, self-irrelevant tasks (repeats row 33) | rebuilt record | `reconstruct.py` | Reproduced | agrees |
| 26 | 157–158 | 95% CI 0.094–0.375 | its interval (repeats row 33) | rebuilt record | `reconstruct.py` | Reproduced | 0.0938 to 0.375, exact |
| 27 | 158–159 | "exceeding a matched control by the registered margin" | gap +0.156 at or above δ = 0.10 (repeats row 46) | rebuilt record + category counts | arithmetic 0.2188 − 0.0625 | Reproduced | |
| 28 | 168 | 30-million-parameter | size of the constructed model (repeats row 21) | body line 421 | cited only | Not reproducible | listed under Not reproducible in the summary |
| 29 | 170 | three seeds | seeds that learned the task (repeats Table 2, body line 483) | body | cited only | Not reproducible | listed under Not reproducible in the summary |
| 30 | 177 | route use 0.986 | arm T's share of right answers that used the built route (repeats Table 3) | `experiments/08-successor-degree/out-reruns-10m/row_T_seed0.json` | (2959 − 41)/2959 | Reproduced | 0.98614. Arm T **passed** its bar, so listing 0.986 under "verification … failed" reads as if all three failed; the failure was in arms C and M |
| 31 | 177 | 0.000 | arm C's route use | `row_C_seed0.json` | (3000 − 3000)/3000 | Reproduced | recomputed from committed counts; the checkpoints were not re-run |
| 32 | 177 | 0.024 | arm M's route use on its stirred-in items | `row_M_seed0.json` | (1387 − 1354)/1387 = 0.0238 | Reproduced | same note as row 31 |
| 32a | 177 | bar of 0.5 | registered bar for route use | row JSONs, `use_bar` 0.5 | read | Reproduced | |
| 32b | 180–181 | three registered designs, two ended at their own stop rules | counts | A3 closure, C stop S4b | records | Reproduced | |
| 33 | 321 | θ_task = 0.10 | threshold for "the task was damaged" | `thresholds.md` line 304; `8b1fcbe` | read, `git show` | Reproduced | |
| 34 | 321 | θ_self = 0.25 | threshold for "the self-report was subtracted" | `thresholds.md` line 305 | read | Reproduced | |
| 35 | 321 | δ = 0.10 | required margin over the control | `thresholds.md` line 306 | read | Reproduced | |
| 36 | 322 | "separate commit, before the test set existed" | ordering | lock `8b1fcbe` 15:35:02; test items first written in `cf06b49` 15:48:35 (all 2026-07-18) | `git log --diff-filter=A` | Reproduced | |
| 37 | 323 | 122 items | test items authored | `cf06b49` | `git show` + line counts: 32+30+30+30 | Reproduced | |
| 38 | 323 | 92/92 | task items surviving the baseline check | battery files, 32+30+30 = 92; `a11e769` "92/92 baseline-verified" | count | Reproduced | the count is reproduced; the baseline correctness itself is not committed |
| 39 | 327 | n = 32 | self-irrelevant items | `test_task_battery.jsonl` | count | Reproduced | |
| 40 | 328 | n = 30 | self-relevant items | `test_task_battery_self_relevant.jsonl` | count | Reproduced | |
| 41 | 329 | n = 30 | turn-boundary items | `test_task_battery_syntax.jsonl` | count | Reproduced | |
| 42 | 331 | n = 30 | self-report items | `test_self_report_battery_v2.jsonl` | count | Reproduced | |
| 43 | 331 | 0.0893 | gate bound on Δnll, from the null calibration | `prelock-findings.md` line 253 | read | Not reproducible | matches findings; `ood_calibration.json` not committed |
| 44 | 332 | B = 10,000 | bootstrap draws | `removal_ci.json` config | read + re-run | Reproduced | |
| T1 | 337 | 0.219 [0.094, 0.375] | primary, self-irrelevant | rebuilt record | `reconstruct.py` | Reproduced | exact |
| T2 | 337 | 0.100 [0.000, 0.200] | primary, self-relevant | rebuilt record | `reconstruct.py` | Reproduced | exact |
| T3 | 337 | 0.133 [0.033, 0.267] | primary, turn-boundary | rebuilt record | `reconstruct.py` | Reproduced | exact |
| T4 | 337 | +0.059 [−0.062, +0.185] | primary, d_self | `removal_ci.json` | compared | Not reproducible | matches committed JSON and findings; judged scores not committed |
| T5 | 337 | +0.0867 ✅ | primary Δnll gate | findings memo | compared | Not reproducible | matches findings |
| T6 | 337 | −0.085 ✅ | primary Δrep-4 gate | findings memo | compared | Not reproducible | matches findings |
| T7 | 338 | 0.125 [0.031, 0.250] | directional, self-irrelevant | category counts in the re-read JSON | `reconstruct.py`, all 1,792 placements | Reproduced | every placement gives the committed interval |
| T8 | 338 | 0.067 [0.000, 0.167] | directional, self-relevant | same | all 100 placements | Reproduced | |
| T9 | 338 | 0.133 [0.033, 0.267] | directional, turn-boundary | same | 3,000 sampled placements | Reproduced | every sampled placement agrees |
| T10 | 338 | −0.039 [−0.136, +0.051] | directional, d_self | `removal_ci.json` | compared | Not reproducible | matches |
| T11 | 338 | +0.0856 ✅ | directional Δnll | findings | compared | Not reproducible | matches |
| T12 | 338 | +0.020 ✅ | directional Δrep-4 | findings | compared | Not reproducible | matches |
| T13 | 339 | 0.063 [0.000, 0.156] | narrative, self-irrelevant | category counts | all 64 placements | Reproduced | |
| T14 | 339 | 0.033 [0.000, 0.100] | narrative, self-relevant | same | all 10 | Reproduced | |
| T15 | 339 | 0.067 [0.000, 0.167] | narrative, turn-boundary | same | all 100 | Reproduced | |
| T16 | 339 | +0.039 [−0.060, +0.146] | narrative, d_self | `removal_ci.json` | compared | Not reproducible | matches |
| T17 | 339 | +0.3468 ❌ | narrative Δnll | findings | compared | Not reproducible | matches |
| T18 | 339 | +0.114 ✅ | narrative Δrep-4 | findings | compared | Not reproducible | matches |
| T19 | 340 | 0.063 [0.000, 0.156] | control, self-irrelevant | category counts | all 64 | Reproduced | |
| T20 | 340 | 0.000 [0.000, 0.000] | control, self-relevant | category counts (0 wrong) | — | Reproduced | |
| T21 | 340 | 0.100 [0.000, 0.233] | control, turn-boundary | category counts | 120 placements | Not reproducible | the point 3/30 is reproduced. The interval is given by 109 of 120 placements; 9 give [0, 0.200]. It matches `removal_ci.json` |
| T22 | 340 | +0.020 [−0.079, +0.112] | control, d_self | `removal_ci.json` | compared | Not reproducible | matches |
| T23 | 340 | +0.1244 ❌ | control Δnll | findings | compared | Not reproducible | matches |
| T24 | 340 | +0.039 ✅ | control Δrep-4 | findings | compared | Not reproducible | matches |
| 45 | 343 | all three batteries | primary over θ_task on self-irrelevant, self-relevant and turn-boundary | rows T1–T3 | 0.219, 0.100, 0.133 ≥ 0.10 | Reproduced | self-relevant is exactly at the threshold |
| 46 | 344 | +0.156 | primary minus control, self-irrelevant | rebuilt + counts | 7/32 − 2/32 = 0.15625 | Reproduced | |
| 47 | 344 | 95% CI 0.000–0.312 | its interval | `removal_ci.json` | 64 placements | Not reproducible | 44 of 64 placements give it (others give [−0.031, 0.344] and [0.031, 0.281]); the control's item ids are not committed |
| 48 | 349 | 0.133 vs. 0.100 | turn-boundary vs self-relevant, primary | rows T2–T3 | — | Reproduced | |
| 49 | 349 | gap +0.033 | router gap, primary | rebuilt record | `reconstruct.py` | Reproduced | |
| 50 | 349–350 | 95% CI −0.133 to +0.200 | its interval | rebuilt record | `reconstruct.py` | Reproduced | exact |
| 51 | 351 | gap +0.067 | router gap, directional | counts | 4/30 − 2/30 | Reproduced | |
| 52 | 351 | [−0.067, +0.233] | its interval | `removal_ci.json` | 3,000 sampled placements | Not reproducible | 2,543 of 3,000 give it; the directional item ids are not committed |
| 53 | 352 | seven weeks earlier | time between committing RT-05's loss condition and the run | `3a43bcf` 2026-06-23; run `692510c` 2026-07-18 | `git log -S` | **Differs** | 25 days, about 3.6 weeks; the quoted wording is the findings memo's, not the registered text's (see Summary) |
| 54 | 356 | 0.219 | primary drop, self-irrelevant | row T1 | — | Reproduced | |
| 55 | 359 | six of the seven | flipped self-irrelevant items that are multi-step | flips | count | Reproduced | |
| 56 | 360 | 6 of 8 | — | flips | count | Reproduced | |
| 57 | 360 | 1 of 24 | — | flips | count | Reproduced | |
| 58 | 364 | [0.000, 0.594] | two-level (category, then item) interval, primary self-irrelevant | rebuilt record | `reconstruct.py` | Reproduced | exact (0.0, 0.5938) |
| 59 | 365–366 | +0.033, −0.133 to +0.200 | repeats rows 49–50 | — | — | Reproduced | |
| 60 | 371–372 | +0.059, CI −0.062 to +0.185 | primary d_self (repeats T4) | `removal_ci.json` | compared | Not reproducible | matches |
| 61 | 373 | θ_self = 0.25 | repeats row 34 | — | — | Reproduced | upper bound 0.185 < 0.25 holds |
| 62 | 374 | "slightly up" | directional d_self −0.039 | T10 | — | Not reproducible | matches |
| 63 | 378 | Δnll +0.347 | narrative gate (repeats T17) | findings | compared | Not reproducible | matches (0.3468) |
| 64 | 378–379 | 4× the index residual | ratio | 0.3468 / 0.0867 | arithmetic | Reproduced | 4.00 |
| 65 | 381 | 2–3 features per layer | dictionary selection result | `prelock-findings.md` line 170 | grep | Not reproducible | matches |
| 66 | 934 | approved 2026-10-23 | date of the revised account | sentient-horizons repo (not in this clone) | — | Not reproducible | outside this repo |
| 67 | 949–950 | method commit holds no output | ordering | `8530a8d` touches only `reread-under-the-map-method-2026-10-24.md` | `git show --stat` | Reproduced | |
| 68 | 953 | flexible lost 0.250 | group G1 (flexible, not about turns), primary | rebuilt record → committed script copy | `work-A1/src/reread_under_map.py work-A1/standin_scores.json` | Reproduced | 6/24; the primary block is identical to the committed JSON |
| 69 | 953 | routine 0.125 | group G2 (routine, not about turns) | same | same | Reproduced | 1/8 |
| 70 | 953 | gap +0.125 | G1 − G2 | same | same | Reproduced | |
| 71 | 953–954 | −0.167 to +0.375 | its interval | same | same | Reproduced | exact |
| 72 | 954 | eight routine items | size of G2 | battery file (instruction-following, 8) | count | Reproduced | |
| 73 | 955 | spans 0.54 | interval width | 0.375 + 0.1667 | arithmetic | Reproduced | 0.5417 |
| 74 | 955 | 0.5 | widest readable width in the method | `reread-under-the-map-method-2026-10-24.md` line 76 | grep | Reproduced | |
| 75 | 957 | all six flexible failures multi-step | — | re-read JSON categories (multi-step 6, coreference 0, finding a fact 0) | read | Reproduced | |
| 76 | 958 | seventh failure a routine item | tt27, instruction-following | flips | read | Reproduced | |
| 77 | 1062 | 2026-08-04, committed before computation | repeats row 4 | — | — | Reproduced | |
| 78 | 1064 | B = 10,000, fixed seed | — | `analyze_removal_ci.py` (seed 20260804) | read + re-run | Reproduced | |
| 79 | 1065 | n = 32, 30, 30, 30 | repeats rows 39–42 | — | — | Reproduced | |
| 80 | 1068 | [0.000, 0.594] | repeats row 58 | — | — | Reproduced | |
| 81 | 1069–1070 | six of seven | repeats row 55 | — | — | Reproduced | |
| 82 | 1070 | "other intervals essentially unchanged" | effect of the two-level bootstrap on the other intervals | `removal_ci.json` "sensitivity_two_level"; re-run | `reconstruct.py` | **Differs** | the primary-minus-control gap widens to [−0.063, 0.469]; the control's turn-boundary interval to [0, 0.333]; primary d_self to [−0.116, 0.215] (see Summary) |
| 83 | 1072–1073 | four decimal places | repeat runs of the control arm's Δnll agree (0.1244) | findings memo, instrument note 1 | compared | Not reproducible | matches |
| 84 | 1073 | \|Δ\| = 0.008 | drift between two judge passes | `prelock-findings.md` line 155 (0.6417 / 0.6333) | arithmetic 0.0084 | Not reproducible | consistent; raw judge passes not committed |
| 85 | 1083 | 0.92–0.99 | activation-frequency ratios for the control (RT-01) | `STATUS-archive.md` line 3235 only | grep | Not reproducible | matches the status log; no committed output |
| 86 | 1226–1231 | Fig. 4 (thresholds 0.10 / 0.25, 95% CIs, gated arms greyed, n 32/30/30/30, bound 0.0893) | the figure | `figures/fig4_registered_run.png` | `work-A1/run_plot.py`, then a per-pixel compare | Reproduced | pixel-identical (0 of 1,580,800 pixels differ); the bytes differ only in the Matplotlib version tag (3.11.2 against 3.11.1); the legend's "RT-05 firing" is shown only implicitly |
