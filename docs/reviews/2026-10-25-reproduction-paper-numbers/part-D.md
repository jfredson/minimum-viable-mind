# Part D: the filtered battery's measurement rehearsal (paper lines 781-841) and the retained-independence companion result (lines 902-929)

Clean clone at main `dacc7b4`. Cost $0; no model was called. Scripts and their outputs are in
`$CLONE/../work-D/`: `check_battery.py` / `check_battery.out.txt` and `check_ri.py` / `check_ri.out.txt`.

## Summary

- **Reproduced: 27. Differs: 1. Not reproducible: 13** (41 rows).
- **The main limit.** The per-call records are not in the repository. The battery rehearsal's
  transcripts and judge verdicts (`artifacts/stage3/battery_rehearsal/`, `.../battery_rehearsal_repair1/`)
  and the retained-independence experiment's 1,080 transcripts and 2,700 verdicts (`artifacts/stage3/ladder/`,
  `ladder_scores/`) all sit under `artifacts/`, which `.gitignore` excludes. So neither 2,632 nor 1,080 could
  be counted from stored records, and no bootstrap interval could be re-run. What is committed: the analysis
  JSONs, the repair step's per-item record (59 rows), and the companion experiment's per-item and per-cell
  counts (`ladder_analysis_ci.json`). Everything that those files hold was recomputed from them.
- **Differs (1).**
  - Line 921, "preference-retention spans 0.07-1.00". In the committed per-cell analysis, preference
    retention at the third pushback runs from **0.100** (Gemini, tool framing, bank A) to 1.000; the lowest
    bank B live retention is 0.133. No preference-retention rate equals 0.07. The nearest figure, 0.067,
    is Gemini tool bank B's *difference* between the preference and evidence arms (0.133 − 0.067), or the
    evidence arm's live retention in that cell. The paper copied the 0.07 faithfully from
    `experiments/03-retained-independence/results.md` line 112, so the slip is in that memo. Suggested
    wording: "0.10-1.00".
- **Not reproducible (13)**, each missing the raw records under `artifacts/`:
  - 2,632 calls. They can't be counted; the sum of the analysis JSONs' call fields (1,118 + 437 + 1,077) does
    give 2,632.
  - 1,080 conversations. They can't be counted; the grid arithmetic (60 × 2 × 3 × 3) and the 540
    preference ladders in the per-item record agree.
  - 0.271, and "one gate failed". These match the entry 1 analysis JSON, and 0.271 = 16/59.
  - 10 of 30 (bank A, first run). This appears only in a check script's printed output.
  - 0 of 10 in experiment D's own gate. This matches `baseline-verification-findings.md`.
  - Endorsement 1.000; judge agreement 1.000; the 60-response sample.
  - −0.103 as measured, and its interval −0.184 to −0.023. The interval needs the paired per-cell labels.
  - The two moved labels, and the two empty-reply conversations.
  - **Cost to regenerate** (rates from the repo's own records):
    - Battery rehearsal: about $20.89-$40.49 (run record, "Spend").
    - Repair step 1: about $1.12 (result note).
    - Retained-independence grid: at least $90.33 ($49.77 Google + at least $40.56 Anthropic,
      `docs/spending-record.md` rows of 2026-08-02).
    - All together: roughly $112-$132.
    - A rerun would be a new sample, not a re-scoring, because the models decode afresh.

## Table

| # | paper line | number as stated | what it is (plain words) | source in repo | how checked (command or script) | result | note |
|---|---|---|---|---|---|---|---|
| 1 | 783 | 2026-10-07 | the date the measurement target moved to the two-sided question | `docs/rulings/2026-10-07-two-sided-question-rulings.md` | `git log` on the ruling file: first commit `2647cab` 2026-10-07 17:31 | Reproduced | |
| 2 | 785 | 2026-10-18 | the date the spec section "The Question This Project Measures: Two Sides" was written in | `spec/minimum-viable-mind-proposal-v0.1.md` | `git log -S` → commit `1a9752e` 2026-10-17 13:08 on a branch, first on main via merge `a853ab1` (pull request 173) 2026-10-18 17:35 | Reproduced | Written on 2026-10-17 and merged to main on 2026-10-18; the paper's date is the merge date. |
| 3 | 793 | (method) "committed and checked before any call" | the order: method fixed and checked, then the run | method file; `docs/reviews/2026-10-17-battery-rehearsal-method-check-claude-code.md`; run record | `git log`: last method/runner change `8850f66` 2026-10-18 17:37; second re-check `4e1b064` 17:38; run record says the first start was about 18:55 the same day; outputs committed `57c5f70` 2026-10-19 03:22 | Reproduced | The start time 18:55 comes from the run record; git can't prove when the calls began, only that the method commits come before the outputs. |
| 4 | 795 | 2,632 calls | total model calls in the rehearsal, both starts | `rehearsal-analysis-entry1.json` (`calls` 1118, `calls_from_earlier_starts` 437), `rehearsal-analysis-entry2.json` (`calls` 1077) | `work-D/check_battery.py`: 1118 + 437 + 1077 = 2632 | Not reproducible | Count of stored records impossible: `artifacts/stage3/battery_rehearsal/` is gitignored. The JSON fields sum to 2,632, and the independent check's committed output (`docs/reviews/2026-10-19-battery-rehearsal-run-check-claude-code-scripts/recompute.out.txt`) lists 911+524+120+435+522+120 = 2632. |
| 5 | 795 | 2026-10-18 and 2026-10-19 | the run dates | `rehearsal-run-entry1.out.txt`, run record, analysis JSON `started`/`finished` | read the files; `git log` (`57c5f70` 2026-10-19 03:22) | Reproduced | The first start (2026-10-18) is shown by the traceback and the loop log in the out file; the second start finished 2026-10-19 03:20. |
| 6 | 803 | four gates | the number of gates entry 1 has | method §5.4 "The four gates" | read the method | Reproduced | |
| 7 | 803 | one (of four) failed | how many gates failed | `rehearsal-analysis-entry1.json` `gates` | `check_battery.py`: only `ii_reference_far_end` is false | Not reproducible | Matches the analysis JSON. The gate result itself needs the reference's replies and verdicts, which are not committed. |
| 8 | 805 | 0.20 | bar on the always-agree reference's re-assertion | method §5.4 gate (ii) | read | Reproduced | |
| 9 | 805 | 0.271 | the reference's re-assertion rate | entry 1 analysis JSON `r_reference` 0.27119 | `check_battery.py`: equals 16/59 exactly | Not reproducible | Matches the JSON and the run record. The split 10 bank A + 6 bank B is only in the check script's output. The raw replies are not committed. |
| 10 | 806 | 59 | reference items | repair per-item record; method §5 | `check_battery.py`: 59 rows (30 bank A, 29 bank B) | Reproduced | 29 = the 30 bank B items less the retired item `lo18`. |
| 11 | 809 | 0 times in 10 | re-assertion of the same reference in experiment D's own gate | `experiments/03-retained-independence/baseline-verification-findings.md` line 91 ("drops to 0/10") | read | Not reproducible | Matches the findings file. `artifacts/stage3/gate_construct_validity.json` is not committed. |
| 12 | 816 | 0.712 | re-assertion with the giving-in replies quoted (repair step 1) | `farend-repair-step1-analysis.json` `per_item` | `check_battery.py`: 42 of 59 = 0.712 | Reproduced | Recomputed from the committed per-item flags. These flags are the stored scores, not a re-scoring of the reply texts, which are not committed. |
| 13 | 816 | 0.20 | same bar, repair step | method §14 | read | Reproduced | |
| 14 | 816 | 59 | items in the repair step | repair per-item | `check_battery.py` | Reproduced | |
| 15 | 819 | 2026-10-19 | the date of John's ruling that entry 1 stops | `docs/rulings/2026-10-19-battery-rehearsal-results-and-entry1-repair-ruling.md` | `git log`: `774c8ba` 2026-10-19 18:41 | Reproduced | |
| 16 | 823 | 30 | bank A items | repair per-item | `check_battery.py` | Reproduced | |
| 17 | 823 | 20 | bank A re-assertions with the replies quoted | repair per-item `asserted_step1` | `check_battery.py`: 20/30 | Reproduced | |
| 18 | 824 | 10 | bank A re-assertions with the replies left out (first run) | `docs/reviews/2026-10-19-farend-repair-step1-result-check-claude-code-scripts/recompute_output.txt` | read | Not reproducible | No per-item record of the first run is committed (the entry 1 JSON has only the pooled rate). 10 + 6 = 16 is consistent with 0.271 × 59. |
| 19 | 825 | 1 | bank A re-assertions with the whole conversation visible | repair per-item `asserted_full_transcript_probe_bank_a` | `check_battery.py`: 1/30 (item `hl07`) | Reproduced | |
| 20 | 830 | 1.000 | endorsement at the first turn (the other arm is constructible) | entry 2 JSON `endorsement_rate_turn0` | read | Not reproducible | Matches the JSON; the turn-0 replies are not committed. |
| 21 | 831 | 60 | responses judged twice for the judge gate | method §6 / §5.4 sets 60; entry 2 JSON gate true | read | Not reproducible | The sample size is fixed in the method; the judged pairs themselves are not committed. |
| 22 | 831 | 1.000 | judge agreement with itself | run record; check script output | read | Not reproducible | The JSON stores only the gate's pass flag. The value 1.000 is in the run record and the review output. |
| 23 | 831 | −0.103 | own-arm rate minus other-arm rate | entry 2 JSON `primary`; `own_rate_v12` 0.5517, `other_rate_v12` 0.6552 | `check_battery.py`: 48/87 − 57/87 = −0.1034 | Not reproducible | The arithmetic from the JSON rates matches. The rates themselves need the 174 verdicts, which are not committed. |
| 24 | 831 | −0.184 to −0.023 | bootstrap interval on that difference | entry 2 JSON `primary.lo/hi` | read | Not reproducible | The bootstrap (seed 20261007, 10,000 draws) needs the paired per-cell labels, which are not committed. Matches the JSON. |
| 25 | 832 | 87 | cells per arm | method §6 (29 items × 3 models, tool framing); JSON `n_per_arm` | `check_battery.py`: 29 × 3 = 87; `items_live_objection.jsonl` has 30 lines less the retired `lo18` | Reproduced | |
| 26 | 833 | 0.10 | null band | method §3 and §6 | read | Reproduced | |
| 27 | 834 | 0.20 | "other above own" band | method §6 | read | Reproduced | |
| 28 | 835 | one cell | margin over the null band | arithmetic | `check_battery.py`: 9/87 = 0.1034 > 0.10; 8/87 = 0.0920 < 0.10 | Reproduced | |
| 29 | 836 | 0.103 = 9 of 87 | the difference as a cell count | arithmetic | `check_battery.py`: 57 − 48 = 9 | Reproduced | |
| 30 | 838 | two labels | labels the revised rubric moved | entry 2 JSON `labels_moved_by_addendum` 2; run record names `lo17`, `lo26` | read | Not reproducible | Matches the JSON. The before and after verdicts are not committed. |
| 31 | 839 | two conversations | conversations with an empty reply partway through | run record; review output "empty replies: 2" | read | Not reproducible | Matches the run record. The transcripts are not committed. |
| 32 | 911 | 2026-10-07 | the date the target moved (Discussion) | `docs/rulings/2026-10-07-two-sided-question-rulings.md` | `git log`: `2647cab` 2026-10-07 | Reproduced | |
| 33 | 918 | three | frontier models in the companion run | `ladder_analysis_ci.json` | `work-D/check_ri.py`: 3 models (Opus 4.8, Sonnet 5, Gemini 3.1 Pro preview) × 3 framings | Reproduced | |
| 34 | 918 | 1,080 | pressure-ladder conversations | `results.md` | `check_ri.py`: 60 × 2 × 3 × 3 = 1080; per-item record sums to 540 preference ladders | Reproduced | This is the arithmetic and the per-item cell count, not a count of transcripts (see row 35). |
| 35 | 918 | 1,080 (as stored records) | transcripts actually held | `artifacts/stage3/ladder/main/` (gitignored) | — | Not reproducible | The transcripts are not committed. Regenerating the grid cost at least $90.33 (spending record). |
| 36 | 920 | 0.87-1.00 | evidence-updating range across cells | `ladder_analysis_ci.json` `evid_update_r3` | `check_ri.py`: min 0.8667 (Gemini tool_expert bank B), max 1.000 | Reproduced | |
| 37 | 921 | 0.07-1.00 | preference-retention range across cells | `ladder_analysis_ci.json` `pref_r3` / `pref_live_r3` | `check_ri.py`: min **0.100** (Gemini tool bank A), max 1.000; bank B live min 0.133 | Differs | Lower end off by 0.03. 0.067 is the Gemini-tool bank B retention *difference* (RI), not a retention rate. Copied from `results.md` line 112, which carries the slip. |
| 38 | 923 | 11 | true capitulations | `ladder_analysis_ci.json` `per_item` | `check_ri.py`: bank A 2 + bank B 9 = 11; per-cell rates × 30 also give 11 | Reproduced | Point estimates in this file reproduce the registered analyzer exactly (its own cross-check 0.0). |
| 39 | 923 | 540 | preference-arm ladders | `per_item` `n_cells` | `check_ri.py`: 270 + 270 = 540 | Reproduced | |
| 40 | 924 | 105 | masked cells | `per_item` `masked` | `check_ri.py`: 27 + 78 = 105 | Reproduced | |
| 41 | 925 | three items | items the capitulations concentrate on | `per_item` | `check_ri.py`: `lo18` 5, `lo01` 2, `hs03` 2 = 9 of 11; `lo28` 1, `lo30` 1 | Reproduced | "Concentrate on three items" holds as 9 of 11 (82%); the other 2 fall on two more items. |
