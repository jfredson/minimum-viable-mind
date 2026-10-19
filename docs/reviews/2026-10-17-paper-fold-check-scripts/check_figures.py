#!/usr/bin/env python3
"""Check 1 of the paper-fold check (2026-10-17 pull request 175).

For every figure the pull request body lists as carried into the paper and the
explainer, grep the source file the body names for it and print HIT (with the
line number and the form that matched) or MISS. A figure is matched as a fixed
string; where the source writes a number differently (a hyphen for a minus
sign, "e-08" for "x 10^-8"), the alternative forms are listed in the table
below, in the open, so a reader can see what was allowed.

Run from the worktree root:  python3 -I docs/reviews/2026-10-17-paper-fold-check-scripts/check_figures.py
Files not on this branch are read from origin/main with `git show` and say so.
"""
import subprocess, sys, os

E = "experiments/06-mvm-0a-constructed-self-index/"
D = "docs/"
R = "docs/rulings/"

def read(path):
    if os.path.exists(path):
        return open(path, encoding="utf-8").read(), "branch"
    try:
        out = subprocess.run(["git", "show", "origin/main:" + path], capture_output=True, text=True, check=True).stdout
        return out, "origin/main"
    except subprocess.CalledProcessError:
        return None, "absent"

# (label, source file, [forms]) -- the first form is the text as written in the PR body / paper.
FIG = [
 # Experiment 06, original design
 ("register spread seed 0", E+"register-saturation-findings.md", ["7.6 × 10⁻⁸", "7.6e-08", "7.6e-8", "7.6×10⁻⁸"]),
 ("register spread seed 1", E+"register-saturation-findings.md", ["2.8 × 10⁻⁸", "2.8e-08", "2.8e-8", "2.8×10⁻⁸"]),
 ("register spread seed 2", E+"register-saturation-findings.md", ["5.9 × 10⁻⁸", "5.9e-08", "5.9e-8", "5.9×10⁻⁸"]),
 ("T_si 0.93 -> 0.94, amendment-a3 s1", E+"amendment-a3.md", ["0.93 → 0.94", "0.93 to 0.94", "0.93→0.94", "0.94"]),
 ("T_si 0.94 in register-lesion thread 4", E+"register-lesion-findings.md", ["0.94"]),
 ("twin T_si 0.96", E+"twin-binding-anomaly.md", ["0.96"]),
 ("twin T_sr_rev 1.00", E+"twin-binding-anomaly.md", ["1.00"]),
 ("A2 pilot endpoint T_si 0.93", E+"pre-registration.md", ["T_si 0.93", "T_si = 0.93", "T_si=0.93", "0.93"]),
 # Amendment A3, Table 2
 ("intact seed 0", E+"seeds-endpoint-findings.md", ["0.5683"]),
 ("intact seed 1", E+"seeds-endpoint-findings.md", ["0.5633"]),
 ("intact seed 2", E+"seeds-endpoint-findings.md", ["0.5738"]),
 ("L0 seed 0", E+"seeds-endpoint-findings.md", ["0.1988"]),
 ("L0 seed 1", E+"seeds-endpoint-findings.md", ["0.2015"]),
 ("L0 seed 2", E+"seeds-endpoint-findings.md", ["0.1447"]),
 ("corrected drop seed 0", E+"seeds-endpoint-findings.md", ["1.337"]),
 ("corrected drop seed 1", E+"seeds-endpoint-findings.md", ["1.342"]),
 ("corrected drop seed 2", E+"seeds-endpoint-findings.md", ["1.528"]),
 ("x theta 7.5", E+"seeds-endpoint-findings.md", ["7.5×", "7.5x", "7.5 ×", "7.5 times"]),
 ("x theta 7.6", E+"seeds-endpoint-findings.md", ["7.6×", "7.6x", "7.6 ×", "7.6 times"]),
 ("x theta 8.6", E+"seeds-endpoint-findings.md", ["8.6×", "8.6x", "8.6 ×", "8.6 times"]),
 ("state drop seed 0", E+"seeds-endpoint-findings.md", ["+0.0018", "0.0018"]),
 ("state drop seed 1", E+"seeds-endpoint-findings.md", ["+0.0002", "0.0002"]),
 ("state drop seed 2", E+"seeds-endpoint-findings.md", ["+0.0769", "0.0769"]),
 ("control seed 0", E+"seeds-endpoint-findings.md", ["0.2877"]),
 ("control seed 1", E+"seeds-endpoint-findings.md", ["0.3057"]),
 ("control seed 2", E+"seeds-endpoint-findings.md", ["0.3195"]),
 ("theta primary", E+"seeds-endpoint-findings.md", ["0.1777"]),
 ("theta state", E+"seeds-endpoint-findings.md", ["0.1172"]),
 ("table 2 sd intact s0", E+"seeds-endpoint-findings.md", ["0.0076"]),
 ("table 2 sd intact s1", E+"seeds-endpoint-findings.md", ["0.0316"]),
 ("table 2 sd intact s2", E+"seeds-endpoint-findings.md", ["0.0284"]),
 ("table 2 sd L0 s0", E+"seeds-endpoint-findings.md", ["0.0173"]),
 ("table 2 sd L0 s1", E+"seeds-endpoint-findings.md", ["0.0215"]),
 ("table 2 sd L0 s2", E+"seeds-endpoint-findings.md", ["0.0127"]),
 ("table 2 sd drop s0", E+"seeds-endpoint-findings.md", ["0.057"]),
 ("table 2 sd drop s1", E+"seeds-endpoint-findings.md", ["0.103"]),
 ("table 2 sd drop s2", E+"seeds-endpoint-findings.md", ["0.068"]),
 ("table 2 sd control s0", E+"seeds-endpoint-findings.md", ["0.0302"]),
 ("table 2 sd control s1", E+"seeds-endpoint-findings.md", ["0.0281"]),
 ("table 2 sd control s2", E+"seeds-endpoint-findings.md", ["0.0150"]),
 ("pilot 0.506", E+"gate2-pilot-findings.md", ["0.506"]),
 ("pilot 0.182", E+"gate2-pilot-findings.md", ["0.182"]),
 ("pilot drop 1.515", E+"gate2-pilot-findings.md", ["1.515"]),
 ("ceiling 1.0000", E+"ceiling-measurement-findings.md", ["1.0000"]),
 ("control pilot 0.3125", E+"control-learnability-pilot-findings.md", ["0.3125"]),
 ("control pilot bar 0.60", E+"control-learnability-pilot-findings.md", ["0.60"]),
 ("control pilot $9.9", E+"control-learnability-pilot-findings.md", ["$9.9", "9.9"]),
 ("control pilot $0.067", E+"control-learnability-pilot-findings.md", ["$0.067", "0.067"]),
 ("control pilot sd 0.0240", E+"control-learnability-pilot-findings.md", ["0.0240", "0.024"]),
 # The nulls
 ("gate0 band 0.0060", E+"gate0-null-calibration-findings.md", ["0.0060"]),
 ("gate0 band 0.0095", E+"gate0-null-calibration-findings.md", ["0.0095"]),
 ("gate0 split ~0.73", E+"gate0-null-calibration-findings.md", ["0.73"]),
 ("K0 at 0.25", E+"gate0-null-calibration-findings.md", ["0.25"]),
 ("non-binder 0.379", E+"gate0-null-calibration-findings.md", ["0.379"]),
 ("breakage 52%", E+"gate0-null-calibration-findings.md", ["52%", "52 %", "0.52"]),
 ("120 ablations", E+"gate0-null-calibration-findings.md", ["120"]),
 ("blind arm best 0.2750", E+"blind-arm-findings.md", ["0.2750", "0.275"]),
 ("blind arm null 0.2441", E+"blind-arm-findings.md", ["0.2441"]),
 ("blind arm sd 0.0237", E+"blind-arm-findings.md", ["0.0237"]),
 ("blind arm 1.30 sd", E+"blind-arm-findings.md", ["1.30", "1.3"]),
 ("blind arm bar 3", E+"blind-arm-findings.md", ["3 sd", "3σ", "3.0", "≥ 3", ">= 3", "bar of 3"]),
 ("blind arm drop -0.0739", E+"blind-arm-findings.md", ["−0.0739", "-0.0739"]),
 ("blind arm best layer 7", E+"blind-arm-findings.md", ["layer 7", "L7", "layer=7", "| **7** |"]),
 ("posctl margin -0.75", E+"blind-control-findings.md", ["−0.75", "-0.75"]),
 ("posctl margin -0.54", E+"blind-control-findings.md", ["−0.54", "-0.54"]),
 ("posctl margin -0.96", E+"blind-control-findings.md", ["−0.96", "-0.96"]),
 ("posctl margin -0.24", E+"blind-control-findings.md", ["−0.24", "-0.24"]),
 ("posctl margin -1.01", E+"blind-control-findings.md", ["−1.01", "-1.01"]),
 ("posctl 0.440", E+"blind-control-findings.md", ["0.440"]),
 ("posctl 0.492", E+"blind-control-findings.md", ["0.492"]),
 ("posctl 1.000", E+"blind-control-findings.md", ["1.000"]),
 ("posctl 0.858", E+"blind-control-findings.md", ["0.858"]),
 ("posctl +0.052", E+"blind-control-findings.md", ["+0.052", "0.052"]),
 ("noise sd 0.0284", E+"blind-control-findings.md", ["0.0284"]),
 ("noise range 0.079", E+"blind-control-findings.md", ["0.079"]),
 ("noise twelve draws", E+"blind-control-findings.md", ["twelve", "12 draws", "12 "]),
 ("known-answer 1.0", E+"known-answer-test-findings.md", ["1.0"]),
 ("known-answer null 0.1306", E+"known-answer-test-findings.md", ["0.1306"]),
 ("sweep 135 tests", E+"fitted-position-sweep-findings.md", ["135"]),
 ("sweep bar 3.38", E+"fitted-position-sweep-findings.md", ["3.38"]),
 ("sweep posctl +34.0", E+"fitted-position-sweep-findings.md", ["+34.0", "34.0"]),
 ("sweep posctl +53.7", E+"fitted-position-sweep-findings.md", ["+53.7", "53.7"]),
 ("sweep MARGINAL 0.2770", E+"fitted-position-sweep-findings.md", ["0.2770"]),
 ("sweep MARGINAL +3.34", E+"fitted-position-sweep-findings.md", ["+3.34", "3.34"]),
 ("sweep +2.33", E+"fitted-position-sweep-findings.md", ["+2.33", "2.33"]),
 ("sweep +2.39", E+"fitted-position-sweep-findings.md", ["+2.39", "2.39"]),
 ("sweep one in twenty-seven", E+"fitted-position-sweep-findings.md", ["27", "twenty-seven"]),
 ("one in eleven", E+"fitted-position-sweep-findings-CORRECTION-2026-09-20.md", ["eleven", "1 in 11", "one in 11", "1/11"]),
 ("refit margin 0.000484", E+"amendment-a3.md", ["0.000484"]),
 ("refit 1.94 of 4,000", E+"amendment-a3.md", ["1.94"]),
 # The kills
 ("gate1 clean 0.5097", E+"gate1-curriculum-findings.md", ["0.5097"]),
 ("gate1 clean 0.5259", E+"gate1-curriculum-findings.md", ["0.5259"]),
 ("gate1 control 0.9433", E+"gate1-curriculum-findings.md", ["0.9433"]),
 ("gate1 control 1.0000", E+"gate1-curriculum-findings.md", ["1.0000"]),
 ("gate1 band [0.45, 0.55]", E+"gate1-curriculum-findings.md", ["0.45", "[0.45, 0.55]"]),
 ("K2 margin 0.214", E+"gate2-pilot-findings.md", ["0.214"]),
 ("K5 not reached", R+"2026-09-25-a3-closure-tier2-dispositions.md", ["not reached", "K5"]),
 # A3 money and closure
 ("A3 spend $46.75", E+"compute-ledger.md", ["46.75"]),
 ("A3 stop $100", E+"compute-ledger.md", ["$100", "100"]),
 ("closure outcome sentence", E+"amendment-a3.md", ["the registered comparison was undefined for every possible"]),
 ("closure 'Separately, removing the ownership-input channel'", E+"amendment-a3.md", ["Separately, removing the ownership-input channel reduced", "separately, removing the ownership-input channel reduced"]),
 ("closure public sentence 'integration degree was not measured'", E+"amendment-a3.md", ["integration degree was not measured", "degree of integration was not measured"]),
 # Experiment C development
 ("C dev $1.47", E+"compute-ledger.md", ["1.47"]),
 ("C dev $0.47", E+"compute-ledger.md", ["0.47"]),
 ("C dev $0.34", E+"compute-ledger.md", ["0.34"]),
 ("C dev $0.33", E+"compute-ledger.md", ["0.33"]),
 ("sharpness -0.089", D+"successor-experiment-proposal-2026-10-07-v5.md", ["−0.089", "-0.089"]),
 ("sharpness -0.008", D+"successor-experiment-proposal-2026-10-07-v5.md", ["−0.008", "-0.008"]),
 ("sharpness 1.947", D+"successor-experiment-proposal-2026-10-07-v5.md", ["1.947"]),
 ("weight 0.218", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.218"]),
 ("weight 0.247", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.247"]),
 ("weight 0.942", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.942"]),
 ("reads 41 of 180", D+"successor-experiment-proposal-2026-10-07-v5.md", ["41 of 180", "41/180"]),
 ("reads 45 of 180", D+"successor-experiment-proposal-2026-10-07-v5.md", ["45 of 180", "45/180"]),
 ("floor 144", D+"successor-experiment-proposal-2026-10-07-v5.md", ["144"]),
 ("toy C before 0.269", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.269"]),
 ("toy C before 0.233", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.233"]),
 ("toy C before 0.221", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.221"]),
 ("toy C after 0.285", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.285"]),
 ("toy C after 0.273", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.273"]),
 ("toy C after 0.244", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.244"]),
 ("toy M before 0.071", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.071"]),
 ("toy M before 0.090", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.090"]),
 ("toy M before 0.109", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.109"]),
 ("toy M after 0.106", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.106"]),
 ("toy M after 0.100", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.100"]),
 ("dev checkpoint C 0.018", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.018"]),
 ("dev checkpoint T 0.924", D+"successor-experiment-proposal-2026-10-07-v5.md", ["0.924"]),
 ("~$1.14 stop estimate", D+"successor-experiment-proposal-2026-10-07-v5.md", ["1.14"]),
 ("sharpness 4.0", D+"successor-experiment-proposal-2026-10-07-v5.md", ["4.0"]),
 # Experiment C Table 3
 ("gate T 2,959", D+"2026-10-09-reruns-10m-run-record.md", ["2,959", "2959"]),
 ("gate T 2,980", D+"2026-10-09-reruns-10m-run-record.md", ["2,980", "2980"]),
 ("gate C 3,000", D+"2026-10-09-reruns-10m-run-record.md", ["3,000", "3000"]),
 ("gate M 2,577", D+"2026-10-09-reruns-10m-run-record.md", ["2,577", "2577"]),
 ("gate M 1,733", D+"2026-10-09-reruns-10m-run-record.md", ["1,733", "1733"]),
 ("gate bar 790", D+"2026-10-09-reruns-10m-run-record.md", ["790"]),
 ("part A 0.999", D+"2026-10-09-reruns-10m-run-record.md", ["0.999"]),
 ("route use T 0.986", D+"2026-10-09-reruns-10m-run-record.md", ["0.986"]),
 ("route use T 2,918 (body cites run record)", D+"2026-10-09-reruns-10m-run-record.md", ["2,918", "2918"]),
 ("route use T 2,918 (paper also cites stop ruling)", R+"2026-10-12-experiment-c-stop-ruling.md", ["2,918 of 2,959"]),
 ("route use C 0 of 3,000 (body cites run record)", D+"2026-10-09-reruns-10m-run-record.md", ["0 of 3,000", "0/3000", "0 / 3000", "0/3,000"]),
 ("route use C 0 of 3,000 (stop ruling)", R+"2026-10-12-experiment-c-stop-ruling.md", ["0 of 3,000"]),
 ("route use M 0.024", D+"2026-10-09-reruns-10m-run-record.md", ["0.024"]),
 ("route use M 33 of 1,387", D+"2026-10-09-reruns-10m-run-record.md", ["33 of 1,387", "33/1387", "1,387", "1387"]),
 ("route use M 0 of 1,190", D+"2026-10-09-reruns-10m-run-record.md", ["0 of 1,190", "0/1190", "1,190", "1190"]),
 ("route use M 33 of 1,387 (stop ruling)", R+"2026-10-12-experiment-c-stop-ruling.md", ["33 of 1,387"]),
 ("route use M 0 of 1,190 (stop ruling)", R+"2026-10-12-experiment-c-stop-ruling.md", ["0 of 1,190"]),
 ("arm T reading 0.0000", D+"2026-10-09-reruns-10m-run-record.md", ["0.0000"]),
 ("108,919 steps", D+"2026-10-09-reruns-10m-run-record.md", ["108,919", "108919"]),
 ("585,548,544 tokens", D+"2026-10-09-reruns-10m-run-record.md", ["585,548,544", "585548544"]),
 ("spend $1.3032", D+"2026-10-09-reruns-10m-run-record.md", ["1.3032"]),
 ("spend M $0.5045", D+"2026-10-09-reruns-10m-run-record.md", ["0.5045"]),
 ("spend T $0.3980", D+"2026-10-09-reruns-10m-run-record.md", ["0.3980", "0.398"]),
 ("spend C $0.4007", D+"2026-10-09-reruns-10m-run-record.md", ["0.4007"]),
 ("rate $1.19", D+"2026-10-09-reruns-10m-run-record.md", ["1.19"]),
 ("rate $0.99", D+"2026-10-09-reruns-10m-run-record.md", ["0.99"]),
 ("ratio 1.000", D+"2026-10-09-reruns-10m-run-record.md", ["1.000"]),
 ("spend $1.3032 in ledger", E+"compute-ledger.md", ["1.3032"]),
 ("programme $230.94 in ledger", E+"compute-ledger.md", ["230.94"]),
 ("programme ceiling $450 in ledger", E+"compute-ledger.md", ["450"]),
 # Rulings quoted
 ("ruled stop sentence", R+"2026-10-08-december-result-restatement-rulings.md", ["the built arms as designed are not references; the measure was not reached"]),
 ("accept the stop", R+"2026-10-12-experiment-c-stop-ruling.md", ["accept the stop"]),
 ("C stays stopped", R+"2026-10-17-experiment-c-stays-stopped-ruling.md", ["stays stopped"]),
 ("relabel sentence", R+"2026-10-07-two-sided-question-rulings.md", ["the test could not discriminate routing from a centre; the cheaper account was taken in advance"]),
]

X = "experiments/01-self-indexing-removal-test/"
P = "drafts/paper-removal-test-nature-draft.md"
# Figures in the new text that the PR body does not list (from unlisted_numbers.out.txt),
# each grepped in the file the new text cites for it, or, where it cites none, the file
# this check found it in (said in the label).
TRACE = [
 ("expl: si drop 0.22 (=0.219)", X+"removal-test-findings.md", ["0.219"]),
 ("expl: sr drop 0.10 (=0.100)", X+"removal_ci.json", ['"point": 0.1,']),
 ("expl: syntax drop 0.13 (=0.133)", X+"removal_ci.json", ['"point": 0.1333']),
 ("expl: d_self +0.059", X+"removal-test-findings.md", ["+0.059", "0.059"]),
 ("expl: d_self lo -0.062", X+"removal_ci.json", ['"lo": -0.062']),
 ("expl: d_self hi +0.185", X+"removal_ci.json", ['"hi": 0.1852']),
 ("expl: router gap +0.033", X+"removal_ci.json", ['"point": 0.0333']),
 ("expl: router gap lo -0.133", X+"removal_ci.json", ['"lo": -0.1333']),
 ("expl: router gap hi +0.200", X+"removal_ci.json", ['"hi": 0.2']),
 ("expl: cross-patch 0.006 (paper v0.2)", P, ["0.006 vs."]),
 ("expl: cross-patch 0.348 (paper v0.2)", P, ["0.348 for the self-index"]),
 ("expl: six of the seven (paper v0.2)", P, ["six of the seven flipped"]),
 ("paper note: 6 of 8, 1 of 24 (paper v0.2)", P, ["(6 of 8 in that category, against 1 of 24"]),
 ("ownership-blind ceiling 0.2921", E+"amendment-a3.md", ["0.2921"]),
 ("recorded control ceiling 0.3227", E+"amendment-a3.md", ["0.3227"]),
 ("T_act chance 0.125", E+"amendment-a3.md", ["chance 0.125"]),
 ("floor rule: drop defined only if base - ceiling >= 0.10", E+"ceiling-measurement-findings.md", ["0.10"]),
 ("rank cap 16", E+"amendment-a3.md", ["rank 16", "k≤16", "≤ 16", "rank ≤ 16", "rank ≤16"]),
 ("n = 800, six evaluation seeds", E+"seeds-endpoint-findings.md", ["800"]),
 ("pilot cost $13.92 (paper cites none; found in gate2)", E+"gate2-pilot-findings.md", ["$13.92"]),
 ("A2: $200 -> $400 cap", E+"pre-registration.md", ["$400"]),
 ("Methods: width 448", E+"gate0-null-calibration-findings.md", ["d_model 448"]),
 ("Methods: 103-token vocabulary", E+"amendment-a3.md", ["103-token closed vocab"]),
 ("Methods: 12 blocks (found in model source)", E+"src/model.py", ["n_layer=12", "n_layer: int = 12", "n_layers=12", "n_layers: int = 12", "12"]),
 ("Methods: 585,552,384 tokens per A3 seed", E+"ctl-pilot-log-provenance-findings.md", ["585,552,384"]),
 ("Methods: $0.99 an hour", E+"amendment-a3.md", ["$0.99/hr"]),
 ("Methods: ceiling raised $400 -> $450", E+"compute-ledger.md", ["from $400 to **$450**"]),
 ("Methods: blocks 3,4,5,7,8", E+"gate0-null-calibration-findings.md", ["3, 4, 5, 7", "3/4/5/7/8", "3,4,5,7,8"]),
 ("Methods: fourteen registration revisions", E+"amendment-a3.md", ["fourteen"]),
 ("Methods: commit 6ad4362 threshold lock (git log also shows it)", D+"public-path-roadmap-2026-09-16.md", ["6ad4362"]),
 ("C: free-arm about $12", R+"2026-10-12-experiment-c-stop-ruling.md", ["about $12"]),
 ("C: second release $150 to $172", R+"2026-10-12-experiment-c-stop-ruling.md", ["$150 to $172"]),
 ("C: alarm ratio 1.25", D+"successor-experiment-proposal-2026-10-07-v5.md", ["1.25 halts"]),
 ("C: software versions", D+"2026-10-09-reruns-10m-run-record.md", ["torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, Python 3.12.13"]),
 ("C: eight outcome terms", D+"successor-experiment-proposal-2026-10-07-v5.md", ["eight outcome terms", "Eight outcome terms", "eight terms"]),
 ("C: 'very likely fail ... about $1.14' quote", D+"successor-experiment-proposal-2026-10-07-v5.md", ["would very likely fail the verification and experiment C would stop at"]),
 ("C: 'Approved.'", D+"2026-10-09-reruns-10m-run-record.md", ['"Approved."']),
 ("closure: two outside reviews named", R+"2026-09-25-a3-closure-tier2-dispositions.md", ["Gemini 3.1 Pro"]),
 ("closure: 15 serious, closable by rewording", R+"2026-09-25-a3-closure-tier2-dispositions.md", ["15 serious findings, all closable by rewording"]),
 ("closure: about seventy processor-hours", E+"amendment-a3.md", ["about seventy processor-hours"]),
 ("5-seed run halted at four of nine", E+"amendment-a3.md", ["halted at four of nine"]),
 ("noise: twelve draws at 400 episodes", E+"blind-control-findings.md", ["| 400 |"]),
 ("expl: wager adopted 2026-09-20", R+"2026-10-07-two-sided-question-rulings.md", ["2026-09-20, after A, B and"]),
 ("John's 2026-09-16 ruling: unvalidated at 30M", E+"blind-arm-findings.md", ["30M", "30 million"]),
 ("sweep: eleven positions and five layers", E+"fitted-position-sweep-findings.md", ["eleven", "11 positions"]),
]

TABLE = TRACE if sys.argv[1:] == ["unlisted"] else FIG
hits = misses = 0
for label, src, forms in TABLE:
    text, where = read(src)
    if text is None:
        print(f"MISS  {label:<48} source absent: {src}"); misses += 1; continue
    found = None
    for f in forms:
        for i, line in enumerate(text.splitlines(), 1):
            if f in line:
                k = line.index(f)
                found = (f, i, line[max(0, k-50):k+len(f)+40].strip()); break
        if found: break
    if not found:
        # second try: the same form with runs of whitespace (line wraps) collapsed
        import re
        flat = re.sub(r"\s+", " ", text)
        for f in forms:
            if f in flat:
                k = flat.index(f)
                found = (f, "wrapped", flat[max(0, k-50):k+len(f)+40].strip()); break
    tag = "" if where == "branch" else f" [{where}]"
    if found:
        hits += 1
        print(f"HIT   {label:<48} {os.path.basename(src)}:{found[1]}  form={found[0]!r}{tag}\n        context: {found[2]}")
    else:
        misses += 1
        print(f"MISS  {label:<48} {os.path.basename(src)}{tag}  tried={forms}")
print(f"\n{hits} hit, {misses} miss, {len(TABLE)} figures")
