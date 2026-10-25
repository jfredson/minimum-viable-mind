# Reproduction of every number in the paper from a clean clone, 2026-10-25

*This is step 3 of the paper readiness checklist (`docs/paper-readiness-checklist-2026-10-18.md`,
section 3), and the roadmap task "Paper readiness 3: reproduce every number in the paper" (`1f2020a6`).
The paper checked is `drafts/paper-removal-test-nature-draft.md`, version 0.3 with its dated note of
2026-10-25. John gave his go on 2026-10-25.*

## What was done

- **The clone.** A fresh session cloned `jfredson/minimum-viable-mind` at `main` (commit `dacc7b4`,
  2026-10-25 09:15 Pacific) into an empty folder outside `~/Code`. It worked only from that clone and
  followed only the repository's own instructions: the README, `src/SETUP.md`, the experiments' method
  and findings files, and the committed scripts. It did not read the working checkouts and asked no
  other session.
- **The environment.** Python 3.12.13 with the pinned versions in
  `experiments/08-successor-degree/requirements-measure.txt` (torch 2.12.1, scikit-learn 1.9.0,
  numpy 2.5.0, scipy 1.18.0), plus matplotlib and pandas, all installed free from the public package index.
- **The cost.** $0. The work ran on the laptop only: no machine was rented, no paid model was called, and
  no large model weights were downloaded.
- **Who checked what.** The paper was split into five parts, and a separate checker went through each one.
  Every number got its own row: counts, rates, intervals, thresholds, sizes, costs, layer numbers, commit
  hashes cited as evidence, and dates that are results. For each row the checker recorded how it was checked
  and one of three results. The session that started the checkers spot-checked one difference from each part
  against the committed files, and every one held.

**What the three results mean.**
- **Reproduced:** the number was recomputed from committed records by a committed script, by a short script
  that reads committed data, by arithmetic on other committed numbers, or (for commit hashes and dates) by git.
- **Differs:** the recomputed value, or the committed record, says something other than the paper. The row
  says by how much and why.
- **Not reproducible:** the record the number comes from is not in the repository. The row says what is
  missing and what it would cost to regenerate. Many of these rows also note that the paper copies its
  findings file correctly, but a match with a memo is not counted as a reproduction.

**A note on what "reproduced" covers.** Most of the "reproduced" rows were recomputed from committed
*outputs*: per-seed accuracies, per-arm result rows, the bootstrap file, the ledger. They were not
regenerated from a trained model, because no trained model behind a paper figure is in the repository
(see below). This is what the checklist asks for ("from the committed records and outputs"), but a
reader should know where the chain stops.

## The count

| part | paper lines | numbers | reproduced | differs | not reproducible | table |
|---|---|---|---|---|---|---|
| A1: header notes, abstract, the registered removal test and Table 1, statistics, re-read under the map, Fig. 4 | 1–183, 319–398, 931–967, 1059–1083, 1226–1231 | 112 | 83 | 2 | 27 | `part-A1.md` |
| A2: localisation, the alignment ladder, the validity gates, Discussion, Methods for experiment 1, Figs. 1–3 | 185–318, 842–900, 971–1057, 1205–1225 | 58 | 35 | 5 | 18 | `part-A2.md` |
| B: experiment 06 and Amendment A3 | 399–637, 1085–1116 | 108 | 101 | 5 | 2 | `part-B.md` |
| C: experiment C, Methods "Compute and cost", the Discussion's cost sentence | 638–780, 883–886, 1118–1155 | 99 | 63 | 2 | 34 | `part-C.md` |
| D: the filtered battery's rehearsal, and the retained-independence result | 781–841, 902–929 | 41 | 27 | 1 | 13 | `part-D.md` |
| **all** | | **418** | **309** | **15** | **94** | |

A number is counted each time it is stated. So the abstract's figures are counted again in the body, and the
abstract's rows say which body row they repeat; no repeat disagreed with its body row. The tables are in the
folder beside this file, `docs/reviews/2026-10-25-reproduction-paper-numbers/`. The checkers' scripts and their
outputs are in its `scripts/` folder. Each script takes the clone's path, written there as `<clone>`.

## The main finding: the raw records are not public

Everything under `artifacts/` is excluded by `.gitignore` (line 15), and `git log --all` shows that none of it
was ever committed. That folder holds, for every experiment, the records the paper's numbers are computed
from:

- **The removal test (experiment 1).** It holds the per-item task scores
  (`artifacts/removal_test/removal_test_scores.json`), the per-item judged self-report scores, the gate
  outputs, the null-calibration draws, the per-layer probe margins, and the patching and cross-patch results.
- **Experiment 06.** It holds the fifteen trained 30-million-parameter models (about 4.6 GB; only their
  fingerprints are committed, in `artifacts-fingerprints-2026-10-24.md`).
- **Experiment C.** It holds the 10-million-scale models from the development runs and the reruns. Their
  checksums are committed, but the models are not.
- **The rehearsal and the retained-independence experiment.** It holds the stored call transcripts and judge
  verdicts.

The paper's "Data availability" says the "per-item score artefacts" are at the repository. They are not.
This matters most for the removal test, where the bootstrap analysis (`analyze_removal_ci.py`) cannot run on
a clean clone because its input file is absent.

What the clone *can* do is still a lot. For the removal test's main condition, the task scores could be rebuilt
exactly from three committed sources: the battery files, the all-correct baseline, and the list of failed items
in `removal_ci.json`. Re-running the registered bootstrap (10,000 draws, seed 20260804) on that rebuild
matched every committed interval for that condition. Fig. 4 regenerated from `removal_ci.json` matches the
committed image pixel for pixel. Experiment 06's per-seed outputs are committed, so Table 2 recomputes exactly.
The toy-model route-use figures in experiment C re-ran from committed models and matched line for line.

## The fifteen differences

Each one is explained in full in its part's table.

**The removal test and its Methods (parts A1 and A2)**
1. **"Committed seven weeks earlier" (line 352).** The router control's loss condition was first committed on
   2026-06-23 (`3a43bcf`) and the registered run was 2026-07-18, which is 25 days. The quoted wording ("report
   the router reading, do not report a center") is the findings memo's; the registered text says "do not
   report it as a center".
2. **"Leaves the other intervals essentially unchanged" (lines 1067–1070).** The committed two-level
   (category, then item) bootstrap in `removal_ci.json` widens several intervals:
   - The primary condition's lead over the control on self-irrelevant tasks goes from 0.000–0.312 to
     **−0.063 to +0.469**, so it now spans zero.
   - The control's turn-boundary interval goes from 0.000–0.233 to 0.000–0.333.
   - The primary condition's self-report interval goes from −0.062 to +0.185 to −0.116 to +0.215.
3. **"Eight categories" in the self-irrelevant battery (line 1042).** The committed pilot and test batteries
   each have four categories of eight items. The paper's own "6 of 8 in that category, against 1 of 24
   elsewhere" fits four.
4. **All ten controls presented as coming from the adversarial review (lines 230, 1019–1027).** The red-team
   ledger records RT-10 (the length-tracker control) as an internal self-audit, not from the Gemini loop.
5. **"The only S drop ever observed" (lines 312–313).** The registered run also shows small self-report drops
   (+0.059 primary, +0.039 narrative, +0.020 control). The sparse-autoencoder drop is the only one beyond noise.
6. **"RTX 4090/5090 class" (line 996).** The pre-lock runs, the sparse-autoencoder pilot and the null
   calibration ran on an RTX PRO 4500 Blackwell, according to their findings files.
7. **The leakage chain "0.059 → 0.026 → 0.020" (line 290).** It is set beside the SFT → DPO → RLVR chain of
   deflection rates, but its values belong to DPO → RLVR → Instruct. No SFT ratio on Tülu is committed. Also,
   the Fig. 3 legend calls these ratios "stable" where the main text says "falling".

**Experiment 06 and Amendment A3 (part B)**
8. **"Seven hard kills (K0 to K7)" (line 463).** Section 4.2 of `amendment-a3.md` lists eight, K0 to K7.
9. **"Forty times the other seeds" (line 479).** Seed 2's state-battery drop of 0.0769 is 43 times the pilot's
   (0.0018) but about 385 times seed 1's (0.0002). The phrase is copied from `seeds-endpoint-findings.md`.
10. **The figures for the K1 kill (lines 589–590: 0.5097, 0.5259, 0.9433, 1.0000).** These are from the
    superseded twelve-turn grammar. The ten-turn grammar the models were trained on passes only under the
    amended sampler (0.5058 and 0.5217 on the registered seed), and fails under the original sampler (means
    0.5395 and 0.5504). "K1 did not fire" still stands, but the figures and the sampler change should be stated.
11. **"103-token vocabulary" (line 1093).** The A3 models use 105 tokens, because `encoding_a3.py` adds "by"
    and "next".
12. **"Seven to nine times" (line 476), borderline.** It is true of the three means (7.5, 7.6 and 8.6), but
    the individual evaluation draws run from 6.6 to 9.0 times. The sentence says "every primary-battery drop".

**Experiment C (part C)**
13. **"10 million parameters" (lines 653, 686, 1127, and Table 3's caption).** The models at that size have
    5.27 to 6.47 million parameters. "10M" is the name of a rung on the code's scale ladder, and the code says
    so (`experiments/08-successor-degree/src/models.py`, line 55).
14. **"30 million" for experiment C's registered size (lines 654, 1126).** The same naming issue: that rung has
    26.07 to 29.33 million parameters.

**The retained-independence result (part D)**
15. **"Preference-retention spans 0.07–1.00" (line 921).** In the committed per-cell analysis
    (`experiments/03-retained-independence/ladder_analysis_ci.json`), the lowest preference retention is
    **0.100** (Gemini, tool framing, bank A). The paper copied 0.07 correctly from `results.md` (line 112), so
    the slip is in that memo. The nearest 0.067 is a difference between two arms, not a retention rate.

## Other points the checkers raised (not counted as differences)

- **Experiment 1's cost (lines 883 and 1144).** Nothing committed supports "about $10 to $20" of rented time,
  "≈ $3" for the registered day, or "low tens of dollars" of judge calls. The repository's own spending record
  (`docs/spending-record.md`, lines 48 and 181) already flags this sentence: RunPod's exports show $42.85 of
  rented machines before the ledger opened, for "the removal test (experiment 1) and other early rented
  work". This is counted under Not reproducible, but it should be settled before submission.
- **Part A of experiment C's in-use check passes by construction.** The weight on the true agent is 0.999 in
  all three reruns and in the never-trained free arm, because the sharpness is fixed at 4.0. The ruling of
  2026-10-08 says so itself, so "all three passed part A" (line 718) carries no evidence. The paper should say so.
- **The abstract's "route use 0.986, 0.000 and 0.024 against a bar of 0.5"** reads as if all three failed.
  0.986 is arm T, which passed; only arms C and M failed.
- **Several localisation figures come from the Gemma pilot, not the registered model.** These are +0.56
  (line 260), "median |cos| 0.28" (line 271), "0.006 vs 0.348" (line 277) and "17 of 26 layers" (line 242).
  Some come from a pass that the length-confound control (RT-10) later found confounded. The corrected or
  registered-model values are 0.23 and 0.18 for the cosine, −0.005 against 0.340 for the ratio, and a
  turn-role signal that is already perfect by layer 3. Part A2's rows give each one. These figures are counted
  as Not reproducible, because their raw outputs are absent, but they should be re-read before submission.
  Two smaller ones are also there: 0.27 for the cross-patch ratio, where the findings give 0.282 and 0.273;
  and the restoration of 0.206, which is the margin over the random control (the raw restoration is 0.200).
- **The ledger's opening total may leave out $1.255** (part C, row 80). If so, the programme total is about
  $232.2, not $230.94. Re-adding every ledger row independently gives $230.97, because some rows are rounded.
  Experiment A3's $46.75 includes about $0.57 of another experiment's rehearsal booked under it.
- **"The registered comparison was never computable"** and the rest of the experiment 06 closure check out
  against git. The threshold-lock commit `6ad4362` (2026-09-16 20:08) comes after the calibration it locks and
  before the first localised read, as claimed. Experiment C's frozen-code commit `6c47c56` is the last commit
  to touch `experiments/08-successor-degree/src/`, and the ledger rows were committed before the first machine
  existed. The removal test's six registration hashes are all in the claimed order.

## What the 94 numbers that could not be reproduced would cost to regenerate

None of this was run. A re-run would be a *replication*, not a reproduction: training on a graphics card is not
exactly repeatable, the judge model has no fixed seed, and new model calls draw a new sample.

| what is missing | numbers that need it | to regenerate | estimated cost |
|---|---|---|---|
| Removal test: per-item task and self-report scores, gate outputs | Table 1's self-report column and gate cells, three item-placement-dependent intervals, the gate bound 0.0893 | re-run the registered test on the 8-billion-parameter model; about 150 judge calls | about $1–3 of rented machine time, plus about $5–10 of judge calls |
| Experiment 1: localisation, ladder and calibration outputs | the probe margins, patching and cross-patch figures, deflection rates, ladder ratios | about 5–6 hours of rented machine time on the 8B models; about 570 judge calls | about $5–7, plus about $20–40 of judge calls (an estimate scaled from the line above) |
| Gemma pilot figures | the pilot-only localisation figures | laptop, about 1–2 hours | $0, but the model is gated: someone has to accept Google's licence on Hugging Face first |
| Experiment 06: the trained models | the twin's 0.96 and 1.00; re-checking every figure from a model rather than its outputs | retrain three A3 seeds, the control pilot and five pre-A3 models (about 110 hours at $0.99 an hour); about 30 laptop hours to re-evaluate | about $110 |
| Experiment C: the 10M development and rerun models | Table 3 from the models, the development-run figures, arm T's 0.0000, arm M's explanation | retrain seven small models; about 7 laptop hours | about $2.80 |
| The rehearsal's stored calls | 2,632 calls, the gate figures, entry 2's interval, the judge agreement, the cost split by vendor | re-run the rehearsal and the repair step | about $22–42 |
| Retained independence's stored calls | 1,080 conversations as stored, the bootstrap intervals | re-run the grid of 60 items × 2 arms × 3 framings × 3 models | at least $90 |
| Experiment 1's early rented time | "$10–20", "≈ $3" and "low tens of dollars" | nothing to run: the bills, or a ruling on the figure | $0 |

**The total is roughly $255–$330.** About $110 of it is retraining experiment 06's models, and about $115–$135
is new model calls. Each item needs John's go before anything is spent.

**A cheaper route to the same end.** Most of these numbers would become reproducible at no cost to compute if
the existing records were published. That means the `artifacts/` files the paper cites, and possibly the model
files as well: the experiment 06 and experiment C fingerprints are already committed, so a reader could check
that the published files are the originals. A data archive beside the paper would cover this, and the paper's
"Data availability" already promises it. Publishing anything is John's decision.

## Where this leaves step 3

Every number in the paper has a row with a result, so the checklist's "done" condition is met: "a filed record
of every figure". The record is not a clean bill. The fifteen differences, and the first four points in the list
above, are wording or citation fixes to the paper. None of them changes a registered verdict. The ninety-four
numbers that could not be reproduced come down to one thing: the raw records are not public.

*Checked by the session that ran the reproduction, 2026-10-25. The clone was deleted when the work was done.*
