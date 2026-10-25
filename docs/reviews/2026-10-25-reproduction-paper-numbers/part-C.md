# Part C: experiment C (the successor), from a clean clone

Paper: `drafts/paper-removal-test-nature-draft.md` at `dacc7b4`, lines 638–780, 883–886, 1118–1155.
Checked 2026-10-25 on the laptop, $0, no paid API calls, no rented machine. Scripts and outputs are in
`$CLONE/../work-C/` (CLONE = the clean clone).

## Summary

| result | rows |
|---|---|
| Reproduced | 63 |
| Differs | 2 |
| Not reproducible | 34 |

**The main gap: the 10-million-parameter checkpoints are not committed, for the three reruns or the four development runs.**
They sit in the main checkout's `artifacts/` folder, which git ignores (`.gitignore` line 15 and
`experiments/08-successor-degree/.gitignore`). No `succ_*_10m*.pt` file appears anywhere in git history. So the
registered in-use check behind Table 3 could not be re-run. What *is* committed, and what I did with it:
- The procedure's per-arm rows (`out-reruns-10m/row_*_seed0.json`) and reads (`reads_*.npz`), with the checkpoints'
  sha256 and md5, and the pinned versions (torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, Python 3.12.13). Every
  number in Table 3 matches these rows. Re-running `procedure.py summarise` on copies of the committed rows gives a
  `table.md` and `summary.json` **identical** to the committed ones (`work-C/resummarise/`). The route-use ratios
  recompute from the counts in the rows (2,918/2,959 = 0.986; 33/1,387 = 0.024; 0/1,190; 0/3,000).
- The training logs (`run-logs/*/succ_*_rerun.jsonl`): each rerun reaches step 108,919 and 585,548,544 tokens.
- The end-of-wave reconcile record (`tripwire-records/reconcile.json`) and the alarm's state file (rate $1.19).
  All the rerun money figures recompute from these.

**What regenerating the missing checkpoints would cost.** Three reruns: $1.3032 as billed at $1.19 an hour (about
$1.08 at the $0.99 rate of record), plus about 4.7 hours of laptop time for the procedure (the rows record 6,660 s,
5,650 s and 5,138 s). Four development runs: $1.4655 at $0.99 (about $1.76 at $1.19), plus 27–44 minutes of laptop
time each. Training on a GPU is not guaranteed to be bit-identical. The committed checksums would show whether a
retrain matched, but if it does not match, the figures could move slightly.

**The toy-model route-use figures reproduce exactly.** `tests/retrained_toy_inuse.py` on the committed toy
checkpoints (`out-sharpness-fix/models/` after the fix, `rehearsal-successor-measure/out-repairs/models/` before it,
each checked by sha256) printed nine lines identical to the committed `retrained_inuse.txt`. It took 2 min 14 s.

**The money figures reproduce.** $1.47 (1.4655), $1.3032, the three per-arm bills, ratio A of 1.000, the $1.19 against
$0.99 explanation, $20.89–$40.49, and $230.94 (to within 3 cents; see row 80) all recompute from the ledger and
records.

**The two Differs:**
1. **"10 million parameters" (lines 653, 686, 1127; Table 3 caption).** The models at the size called "10M" have
   5,265,758 (arm T), 6,471,750 (C), 5,375,076 (M) and 6,362,951 (F) parameters, about half the stated size. "10M" is
   the name of a rung on the programme's scale ladder. The code's own docstring says "the parameter counts are below
   the rung names" (`src/models.py`, lines 46–55). The paper reads it as a count.
2. **"30 million" (lines 654, 1126).** The registered size has 26,065,470 (T) to 29,329,734 (C) parameters, the same
   naming issue but smaller (about 2–13% under). Counted with `models.n_params(models.build(arm, size))`.

**Not reproducible, by what is missing:**
- *Rerun checkpoints (uncommitted):* every Table 3 count and figure (gate counts, part A 0.999, route use) and arm T's
  reading 0.0000. These match the committed rows and the run record. Retraining costs about $1.30 plus about 4.7 laptop hours.
- *Development checkpoints (uncommitted):* sharpness −0.089 / −0.008 / 1.947, weights 0.218 / 0.247 / 0.942, route use
  0.018 / 0.000 / 0.924, and the best whole reads 41 and 45 of 180. These match the committed outputs
  (`ownership_answer_sharpness_output.txt`, `out-sharpness-fix/inuse-cases/stdout.txt`, and the per-layer counts in
  `out-dev-10m-check/row_*.json`, whose maxima I recomputed). Retraining costs about $1.47 plus about 2–3 laptop hours.
- *Battery rehearsal call records (uncommitted, in `artifacts/stage3/battery_rehearsal`):* the Anthropic $13.06 and
  Gemini $7.83–$27.43 split. These match the run record and the committed check output. Regenerating them means
  re-running the paid rehearsal (about $21–$40), which was not done.
- *Experiment 1's cost (lines 883, 1144): "$10–20" of rented time and "registered-day ≈ $3".* No committed record
  gives either figure. **The repository's own spending record flags the sentence:** RunPod exports show **$42.85**
  of rented machines before the ledger opened, covering "the removal test (experiment 1) and other early rented work".
  It says the sentence "should be checked against this record" (`docs/spending-record.md`, lines 181–184 and the first
  rented-machines row). The ledger's baseline agrees: $150 − $106.73 = $43.27 spent before 2026-08-07. This needs
  checking before submission.
- *"Low tens of dollars of judge calls" (lines 884, 1144–1145):* there is no committed per-call record for experiment 1's judges.
- *Arm M's 0.000 explanation (2026-10-18 findings):* it uses the uncommitted rerun checkpoints.
- *Line 772, "learnable at 30 million parameters ... on three seeds":* this is experiment 06's claim and outside this
  part's materials. The ledger shows that rung's model at 39,204,192 parameters.

**Two other things worth knowing:**
- **Part A passes by construction.** The weight on the true agent is 0.9989947 in all three reruns and in the never-trained arm F
  (0.9990). That is what the stored sharpness of 4.0 gives, whatever the network learned. The 2026-10-08 ruling says
  so itself: "part A alone, which the fixed sharpness passes by construction and so tests nothing". The paper's "All
  three passed ... part A" is true but carries no evidence.
- **The programme total.** The ledger's $230.94 builds on its own corrected base of $228.17. Re-adding every ledger
  row from 2026-08-07 independently gives $230.97. The 3-cent gap comes from the rows written with "~", rounded at each step. The
  ledger's running totals start at $105.62 = $6.645 + $1.943 + $97.035. The console check in the same file adds
  another $1.255 (total $106.88). If that is also rented time inside the ledger's period, the total would be about
  $232.2. I could not tell from the file which is right.

## Table

Scripts: `work-C/retrained_inuse_rerun.txt` (toy re-run output), `work-C/dev_best_reads.py` (+ `.txt`),
`work-C/rerun_bills.py` (+ `.txt`), `work-C/ledger_sums.py` (+ `.txt`), `work-C/resummarise/` (summarise re-run).
EXP = `experiments/08-successor-degree`; LEDGER = `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`;
V5 = `docs/successor-experiment-proposal-2026-10-07-v5.md`; RR = `docs/2026-10-09-reruns-10m-run-record.md`.

| # | paper line | number as stated | what it is (plain words) | source in repo | how checked (command or script) | result | note |
|---|---|---|---|---|---|---|---|
| 1 | 643, 1118 | 2026-10-09 | date experiment C was registered | `docs/rulings/2026-10-09-registration-commit-ruling.md`; merge `e7c6f23` | `git log` on the ruling (a9680b2, 2026-10-09 10:25 PDT); `e7c6f23` merge of PR 162 "registration-commit-2026-10-09", 2026-10-09 10:52 PDT, ancestor of main | Reproduced | |
| 2 | 644, 1121 | `6c47c56` | commit holding the frozen code | git | `git cat-file -t` = commit, 2026-10-08 19:21 PDT, ancestor of main, touches `EXP/src/procedure.py`; `git diff 6c47c56 dacc7b4 -- EXP/src/` and `6c47c56..e7c6f23` both empty; the ruling names it (line 16) | Reproduced | Last commit touching `src/` is `6c47c56` |
| 3 | 1122 | method committed first | registration method before registration text | git | method `127ed04` 2026-10-07 19:35 PDT; v5 text `c9b0259` 20:05 PDT | Reproduced | |
| 4 | 648–649 | two tiers of review at each of two gates | review process | V5 source table | not counted | Not reproducible | Process claim, not checked in this part |
| 5 | 649 | four arms | arms T, C, M, F | V5; `EXP/src/models.py` | build all four | Reproduced | |
| 6 | 653, 686, 1127; Table 3 | 10 million parameters | development model size | `EXP/src/models.py` | `models.n_params(models.build(a,"10M"))` → T 5,265,758; C 6,471,750; M 5,375,076; F 6,362,951; the run logs' recipe lines agree | **Differs** | "10M" is a rung name; real counts are 5.3–6.5 million. The docstring says counts are below the rung names |
| 7 | 654, 1126 | 30 million | registered size | same | `build(a,"30M")` → 26,065,470 to 29,329,734 | **Differs** | Same naming issue, 2–13% under |
| 8 | 661 | eight outcome terms | registered outcome terms | V5 section 3 table | counted rows R1–R4 and the fifth to eighth terms | Reproduced | |
| 9 | 662 | 2026-10-07 | renaming ruling date | `docs/rulings/2026-10-07-two-sided-question-rulings.md` | git add date 2026-10-07 17:31 PDT | Reproduced | |
| 10 | 669 | 2026-10-04 | date of the four development runs | LEDGER rows 105–108 | rows dated 2026-10-04 (Pacific); machines 2026-10-05 00:11–00:40Z | Reproduced | |
| 11 | 669, 748, 1138 | $1.47 | four development runs, total | LEDGER rows 105–108 | `ledger_sums.py`: 0.4744+0.3347+0.3341+0.3223 = 1.4655 | Reproduced | Figures are lifetime × rate; vendor bills never posted in the ledger |
| 12 | 669 | $0.4744 | arm M dev run | LEDGER annotation table | 28 min 45 s × $0.99 = 0.4744 | Reproduced | |
| 13 | 670 | $0.3347 | arm T dev run | same | 20 min 17 s × 0.99 = 0.3347 | Reproduced | |
| 14 | 670 | $0.3341 | arm C dev run | same | 20 min 15 s × 0.99 = 0.3341 | Reproduced | |
| 15 | 670 | $0.3223 | arm F dev run | same | 19 min 32 s × 0.99 = 0.3223 | Reproduced | |
| 16 | 674 | 4.0 | starting sharpness | `EXP/src/models.py` line 123 | read code; toy arm F (never trained) reads +4.0000 | Reproduced | |
| 17 | 674 | −0.089 | arm C dev sharpness | `experiments/06-…/reviews/2026-10-04-development-runs-check-scripts/ownership_answer_sharpness_output.txt` | dev checkpoint not committed | Not reproducible | Output prints −0.0886; matches. Regen about $0.33 + laptop |
| 18 | 675 | −0.008 | arm M dev sharpness | same | same | Not reproducible | −0.0083; matches |
| 19 | 675 | 0.218 | arm C weight on the true agent | same | same | Not reproducible | 0.2183; matches |
| 20 | 676 | 0.247 | arm M weight | same | same | Not reproducible | 0.2469; matches |
| 21 | 676 | 0.25 | weight of a flat answer | arithmetic | 1/4 agents | Reproduced | |
| 22 | 677 | 1.947 | arm T dev sharpness | same output | same | Not reproducible | +1.9469; matches |
| 23 | 677 | 0.942 | arm T dev weight | same | same | Not reproducible | 0.9424; matches |
| 24 | 679 | 41 of 180 | arm C best whole read (dev) | `EXP/out-dev-10m-check/row_C_seed0.json` (`fits`) | `dev_best_reads.py`: max over nine layers = 41 (layer 4) | Not reproducible | The maximum recomputes from committed per-layer counts, but the counts need the dev checkpoint |
| 25 | 679 | 45 of 180 | arm M best whole read (dev) | `row_M_seed0.json` | same: 45 (layer 8) | Not reproducible | Same |
| 26 | 679, 1129 | floor 144 | read floor | rows `band.floor`; V5 | 4/5 × 180 = 144; every row's band has floor 144 | Reproduced | |
| 27 | 683–684 | 2026-10-07, 2026-10-08 | repair rulings | rulings folder | files added 2026-10-07 / 2026-10-08 in git | Reproduced | |
| 28 | 684 | 4.0 stored | fixed sharpness in reruns | rerun rows | `gate.route_in_use.sharpness` 4.0, `sharpness_learned` False in all three | Reproduced | |
| 29 | 688 | 2026-10-08 | bars ruled fixed | `docs/rulings/2026-10-08-verification-bar-ruling.md` | git add `ada10a9` 2026-10-08 | Reproduced | |
| 30 | 690, 722, 1132 | 0.9 | part A bar | rerun rows `weight_bar` | read rows | Reproduced | |
| 31 | 692, 722, 1133 | 0.5 | part B bar | rows `use_bar` | read rows | Reproduced | |
| 32 | 695 | 2026-10-08 | ending-words ruling | `docs/rulings/2026-10-08-december-result-restatement-rulings.md` | git add 2026-10-08 | Reproduced | |
| 33 | 701 | 0.269, 0.233, 0.221 | toy arm C route use before fix, seeds 0–2 | toy checkpoints `rehearsal-successor-measure/out-repairs/models/ckpt_C_base_seed*.pt` | `cd EXP; $PY tests/retrained_toy_inuse.py --models out-sharpness-fix/models --out …` → `work-C/retrained_inuse_rerun.txt`; identical to committed `retrained_inuse.txt` | Reproduced | Three numbers |
| 34 | 702 | 0.285, 0.273, 0.244 | toy arm C after fix | `out-sharpness-fix/models/ckpt_C_fixed_seed*.pt` | same run | Reproduced | |
| 35 | 702 | 0.071, 0.090, 0.109 | toy arm M stirred-in route before | out-repairs M models | same run | Reproduced | |
| 36 | 703 | 0.090, 0.106, 0.100 | toy arm M stirred-in route after | fixed M models | same run | Reproduced | |
| 37 | 703–704 | 1.000 | toy arm T slot and arm M separable route, before and after | toy models | same run: slot 1.0 and separable 1.0 on all seeds | Reproduced | |
| 38 | 704 | 0.018 | arm C dev route use | `EXP/out-sharpness-fix/inuse-cases/stdout.txt` case 10 | dev checkpoint not committed (`tests/inuse_cases.py` `ten()` reads it from `artifacts/`) | Not reproducible | matches |
| 39 | 704 | 0.000 both routes | arm M dev route use | same, case 11 | same | Not reproducible | matches |
| 40 | 705 | 0.924 | arm T dev route use | same, case 12 | same | Not reproducible | matches |
| 41 | 707 | about $1.14 | approved/expected rerun cost | V5 line 1546; LEDGER rows 109–111 "$ est" | 0.47 + 0.34 + 0.33 (the dev costs of M, T, C) = 1.14 | Reproduced | |
| 42 | 707–708 | three alternatives, 2026-10-08 | options declined | verification-bar ruling, "What is declined" | counted (b), (c), (d) | Reproduced | |
| 43 | 712 | 2026-10-09 | rerun date | RR; run logs; LEDGER rows 109–111 | machines 18:10–18:54Z 2026-10-09 | Reproduced | |
| 44 | 713–714 | rows committed before any machine | ledger before launch | git `3ba6ff8` | committed 2026-10-09 10:57:32 PDT = 17:57Z; first machine created 18:10:04Z | Reproduced | |
| 45 | 715, 1139 | 108,919 steps | training length each | `EXP/out-reruns-10m/run-logs/*/succ_*_rerun.jsonl` | last line step 108919 in all three | Reproduced | Dev runs: committed `checkpoints_end_to_end_output.txt` says the same (checkpoints absent) |
| 46 | 1139 | 585,548,544 tokens | tokens each | same jsonl | last line tokens 585548544; 108,919 × 96 × 56 = 585,548,544 | Reproduced | Dev runs: same per committed check output |
| 47 | Table 3 | seed 0 | seed of reruns | rows | `seed` 0 | Reproduced | |
| 48 | Table 3 | bar 790 (of 3,000) | learning gate bar | rows `gate.bar`, `episodes` | read | Reproduced | Also 1131 |
| 49 | Table 3 T | 2,959 and 2,980 | arm T own / named-other right | `row_T_seed0.json` | rerun checkpoint not committed | Not reproducible | matches row and RR |
| 50 | Table 3 T | 0.999 | arm T part A | row | same | Not reproducible | 0.99899; set by the fixed sharpness alone (see summary) |
| 51 | Table 3 T | 0.986 (2,918 of 2,959) | arm T slot route use | row: right 2,959, still right after swap 41 | counts need checkpoint; arithmetic (2,959−41)/2,959 = 0.9861 | Not reproducible | arithmetic consistent |
| 52 | Table 3 C | 3,000 and 3,000 | arm C gate | `row_C_seed0.json` | checkpoint absent | Not reproducible | matches |
| 53 | Table 3 C | 0.999 | arm C part A | row | same | Not reproducible | same value as T, by construction |
| 54 | Table 3 C | 0.000 (0 of 3,000) | arm C route use | row: right 3,000, still right 3,000 | same | Not reproducible | arithmetic consistent |
| 55 | Table 3 M | 2,577 and 1,733 | arm M gate | `row_M_seed0.json` | same | Not reproducible | matches |
| 56 | Table 3 M | 0.999 | arm M part A | row | same | Not reproducible | by construction |
| 57 | Table 3 M | 0.024 (33 of 1,387) | arm M stirred-in route use | row: right 1,387, still right 1,354 | same; (1,387−1,354)/1,387 = 0.0238 | Not reproducible | arithmetic consistent |
| 58 | Table 3 M | 0.000 (0 of 1,190) | arm M separable route use | row: 1,190 / 1,190 | same | Not reproducible | arithmetic consistent |
| 59 | Table 3; 732–734 | passed / failed; "no verdict"; "gate not decidable on one seed" | in-use states and printed reasons | rows, `summary.json`, `table.md` | `procedure.py summarise --dir work-C/resummarise` on copies of committed rows → table.md and summary.json identical | Reproduced | From committed rows; the rows themselves need the checkpoints |
| 60 | 735–736 | 0.0000; states (0,); 8 directions; 180 of 180 | arm T reading on its seed | `table.md`, `row_T_seed0.json` (`primary`) | checkpoint absent; summarise regenerates the same table row | Not reproducible | matches |
| 61 | 739 | 2026-10-12 | stop ruling | `docs/rulings/2026-10-12-experiment-c-stop-ruling.md` | git add `d6d7977` 2026-10-12; header "Authorship: john"; quotes "accept the stop" | Reproduced | |
| 62 | 746 | about $12 | free-arm run at registered size | stop ruling line 73; V5 section 12.4 ($12 planning figure) | read | Reproduced | Planning figure copied correctly; nothing measured |
| 63 | 747 | about $150 to $172 | second release | V5 section 12.4 | $119.06 + $30 = $149.06 (ruled split) to $129.90 + $42 = $171.90 (note's split) | Reproduced | The range spans the two splits |
| 64 | 749 | $1.3032 | three reruns, billed | `EXP/out-reruns-10m/tripwire-records/reconcile.json` + state.json rate 1.19 | `rerun_bills.py`: 1.0951 billed h × 1.19 = 1.3032 | Reproduced | |
| 65 | 749 | $0.5045 | arm M rerun | same | 0.42391 h × 1.19 = 0.5045 | Reproduced | |
| 66 | 750 | $0.3980 | arm T rerun | same | 0.33447 h × 1.19 = 0.3980 | Reproduced | |
| 67 | 750 | $0.4007 | arm C rerun | same | 0.33672 h × 1.19 = 0.4007 | Reproduced | |
| 68 | 750 | about $1.14 approved | approval | as row 41 | — | Reproduced | Billed is 1.143 × approved |
| 69 | 751 | $1.19 | vendor hourly rate | `tripwire-records/state.json` ("rate": 1.19, three times) | read | Reproduced | |
| 70 | 751 | $0.99 of record | rate of record | LEDGER rows; RR launch settings `RATE_PER_HOUR_USD=0.99` | read; lifetimes 1.0949 h × 0.99 = $1.0839 < $1.14, so the overrun is the rate | Reproduced | |
| 71 | 752–753 | 1.000 on every machine | billed hours ÷ machine lifetime | reconcile.json | ratio_a 1.0004 (M), 1.0001 (T), 1.0001 (C) | Reproduced | |
| 72 | 753, 885, 1146 | about $230.94 | programme rented-machine spend to the stop | LEDGER rows 87–111 and 2026-10-06 annotation | `ledger_sums.py`: corrected base 228.17 + 1.4655 + 1.3032 = 230.9387; independent re-add of all rows = 230.97 | Reproduced | Within 3 cents (rounded "~" rows). The ledger's start leaves out $1.255 that its own console check includes; with it, about $232.2 (unresolved) |
| 73 | 753, 1146 | $450 ceiling | programme ceiling | LEDGER ceiling note (2026-09-25) | read | Reproduced | |
| 74 | 755–756 | 0.000 / 1.000 / 0.986 | arm M separable (rerun) vs toy vs arm T slot | rows; toy re-run | toy 1.000 reproduced; 0.000 and 0.986 need rerun checkpoints | Not reproducible | See rows 37, 51, 58 |
| 75 | 759–762 | arm M's 0.000 explained at $0 | finding of 2026-10-18 | `docs/2026-10-18-arm-m-separable-zero-findings.md` | method `cb3b9ee` committed 16:58, findings `8fa464d` 17:06 PDT 2026-10-18 (order holds); diagnostics need the rerun checkpoints | Not reproducible | Order of method and output checked |
| 76 | 763 | 2026-10-17 | stays-stopped ruling | `docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md` | git add `8d0c2af` 2026-10-17; "Authorship mixed" | Reproduced | |
| 77 | 772–773 | 30 million parameters; three seeds | experiment 06's learnable task | LEDGER | not this part's materials | Not reproducible | Ledger gives 39,204,192 parameters for that rung, the same naming issue as rows 6–7 |
| 78 | 883, 1144 | about $10 to $20 / ≈ $10–20 | experiment 1's rented GPU time | none found; `docs/spending-record.md` | grep the whole clone; the spending record shows $42.85 before the ledger opened (experiment 1 + other early work); the ledger baseline gives $150 − $106.73 = $43.27 | Not reproducible | **Flagged by the repo itself** (spending-record "What needs John's ruling", item 3). Upper bound in the record is about $43 |
| 79 | 884, 1144–1145 | low tens of dollars | experiment 1's judge calls | none committed | — | Not reproducible | No per-call record found |
| 80 | 1145 | ≈ $3 | experiment 1's registered-day cost | none found | grep | Not reproducible | No source in the clone |
| 81 | 1126 | three seeds per arm | registered seeds | V5 | read (e.g. line 675) | Reproduced | |
| 82 | 1133 | S1 to S10; S4b | stop conditions | V5 section 11 | `grep -o 'S[0-9]+[ab]?'`: S1…S10 and S4a/S4b present | Reproduced | |
| 83 | 1134–1135 | two releases ruled 2026-09-21 | money releases | `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` | git add `6831a39` 2026-09-21 | Reproduced | |
| 84 | 1136 | 1.25 | alarm halt ratio | V5 line 255 | read | Reproduced | Rerun ratio B peaked at 1.007 (RR) |
| 85 | 1138 | RTX 5090 | GPU of all seven runs | LEDGER rows 105–111; RR | read | Reproduced | |
| 86 | 1140 | torch 2.12.1, sklearn 1.9.0, numpy 2.5.0, Python 3.12.13 | pinned versions | rerun rows `versions` | read; same versions in this check's venv | Reproduced | |
| 87 | 1141 | nothing at registered size launched | — | LEDGER (no row after 2026-10-09 for C) | read | Reproduced | |
| 88 | 1145 | 2026-08-07 | ledger opened | LEDGER "Reconciliation baseline" | read | Reproduced | |
| 89 | 1151 | 2026-10-18 and 2026-10-19 | battery rehearsal dates | `docs/spending-record.md` rows; run record | read | Reproduced | |
| 90 | 1152 | $20.89 to $40.49 | rehearsal cost estimate | spending record line 208; `docs/filtered-battery-2026-10-07/rehearsal-run-record-2026-10-19.md` "Spend" | 13.06 + 7.83 = 20.89; 13.06 + 27.43 = 40.49; the high end also = committed runner totals 21.8237 + 18.6635 = 40.4872 (`rehearsal-run-entry{1,2}.out.txt`) | Reproduced | Arithmetic only; components below |
| 91 | 1153 | about $13.06 | Anthropic share | run record; `docs/reviews/2026-10-19-battery-rehearsal-run-check-claude-code-scripts/spend_and_secrets.out.txt` | the call records are in uncommitted `artifacts/stage3/battery_rehearsal` | Not reproducible | matches two committed outputs |
| 92 | 1153 | about $7.83 to $27.43 | Gemini share | same | same | Not reproducible | matches |
| 93 | 1154 | up to $50 | rehearsal approval | spending record ("Go up to $50") | read | Reproduced | |
| 94 | 750 | $1.47 (again), 1138 | dev runs total | as row 11 | — | Reproduced | |
| 95 | 1138 | $1.3032 (again) | reruns total | as row 64 | — | Reproduced | |
| 96 | 1132 | in-use check of section 5.6 | where the bars sit | V5 section 5.6 | read | Reproduced | |
| 97 | 715–716 | each checkpoint checked against the machine's copy | integrity | `out-reruns-10m/checkpoints.sha256-md5.txt`; rows' `checkpoint_sha256` | the rows' sha256 equal the committed list (T 0d39dea7…, C f1615d14…, M a76f3c9a…); the files themselves are absent | Not reproducible | Hashes agree with each other; nothing to hash |
| 98 | 718 | all three passed gate and part A | outcome | rows | as rows 49–56 | Not reproducible | Part A is passed by construction (verification-bar ruling, option (c)) |
| 99 | 718–719 | part B failed on both built routes of C and M | outcome | rows | as rows 54, 57, 58 | Not reproducible | consistent with rows |
