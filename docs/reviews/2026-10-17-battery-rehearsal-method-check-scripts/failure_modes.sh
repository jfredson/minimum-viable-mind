#!/usr/bin/env bash
# Check 8 of the check of pull request 174 (2026-10-17): the commands of
# docs/known-failure-modes.md, pointed at the rehearsal method and its runner.
# Items 3 (part three), 5 and 6 also rest on standin_runs.sh and
# checks_dryrun_gates_rubric.sh, whose outputs are beside this script.
# Reads only; calls no model.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/failure_modes.sh
set -u
cd "$(dirname "$0")/../../.."
M=docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md
P=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py

echo "## 1. denominators and the top of each reading's scale"
echo "  divisions in the runner by a difference or a distance to a ceiling, such as '/ (1 - x)' or '/ (a - b)':"
grep -nE '/ *\(1 *-|/ *\([^()]* - [^()]*\)' $P | sed 's/^/    /' || true
echo "    (end of list)"
echo "  self-test, the same pattern on a line that does divide by a distance: $(echo 'r = (w - o) / (1 - c)' | grep -cE '/ *\(1 *-|/ *\([^()]* - [^()]*\)') match"
python3 - <<'EOF'
rF, own = 101 / 107, {"pooled": 50 / 87, "opus": 25 / 29, "sonnet": 21 / 29, "gemini": 4 / 29}
print(f"  entry 1, top of scale with nothing to detect: r_B2 - r_S up to r_B2 (about 1.0); r_F - r_S up to {rF:.3f}; "
      f"r_S - r_F up to {1 - rF:.3f} (no band, so nothing to fail)")
for k, v in own.items():
    print(f"  entry 2 {k:7}: own minus other can reach {v:.3f}; other minus own can reach {1 - v:.3f}"
          + ("   <- the 0.20 band applies here" if k == "pooled" else "   (no threshold)"))
EOF
echo "  ceilings typed above, traced: 101/107 and 50/87 are in count_lost.out.txt and recount_cells.out.txt"
grep -n "101 of 107\|live at third rung=50" docs/filtered-battery-2026-10-07/count_lost.out.txt | sed 's/^/    /'

echo; echo "## 2. the route sentence, part one (part two needs a run)"
grep -n "carried by the" $M | sed 's/^/  /'

echo; echo "## 3. empty cells: what the plan puts in each pre-stated cell, and how it draws"
grep -nE '\.sample\(|\.shuffle\(|permutation|set\(|distinct|unique' $P | sed 's/^/  /'
python3 - <<'EOF'
print("  gate samples: 20 per model drawn without replacement from pools of 87 (entry 1, bank B per model) and 29 (entry 2); 20 <= 29, so no pool is short")
print("  pre-stated pooled cells: entry 1 107 lost cells (gate iv needs 80); entry 2 87 per arm; per-model cells carry no threshold")
EOF
echo "  part three, each gate at both ends (healthy end: the instrument works; broken end: it does not):"
echo "    gate (i)  arm S2 <= 0.10: healthy ~0 passes; a leaking template ~1 fails"
echo "    gate (ii) reference <= 0.20, live >= 0.80: healthy passes; an instrument blind to the far end fails"
echo "    judge gates >= 0.8 agreement: healthy passes; an unparseable judge PASSES (standin_runs.out.txt, run F):"
grep -n "judge gate:" docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/standin_runs.out.txt | sed 's/^/      /'
echo "    the comparison that makes it pass (an error record has no position and no flag, so None == None):"
grep -n '"agree": v1.get("position") == v2.get("position")' $P | sed 's/^/      /'
grep -n 'agree = (v1.get("position") == v2.get("position")' experiments/03-retained-independence/src/gate_judge_reliability.py | sed 's/^/      experiment D, the same: /'
echo "    experiment D's judge files holding an unparseable-verdict record: $(grep -rl 'unparseable judge output' /Users/john/Code/minimum-viable-mind/artifacts/stage3/ladder_scores | wc -l | tr -d ' ') of $(find /Users/john/Code/minimum-viable-mind/artifacts/stage3/ladder_scores -name '*.json' | wc -l | tr -d ' ')"

echo; echo "## 4. claims of measurement in the method: the two sweeps, then every MEASURED label"
echo "  claim-word sweep: $(grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' $M || true) lines"
echo "  number sweep:     $(grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' $M || true) lines"
echo "  lines labelled MEASURED:"
grep -n "MEASURED" $M | cut -c1-150 | sed 's/^/    /'
echo "  the stand-in run of the writing session (section 7) is committed anywhere in the pull request: $(git diff --name-only origin/main...HEAD | grep -ci 'stand' || true) files"

echo; echo "## 5. a command that creates something while documented as creating nothing"
echo "  the runner's and the method's words:"
grep -nE 'writes nothing|creates nothing|left none' $P $M | cut -c1-140 | sed 's/^/    /'
echo "  what the dry run created with Python's default bytecode caching (checks_dryrun_gates_rubric.out.txt, section 2a):"
grep -n "new: \|  file: " docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/checks_dryrun_gates_rubric.out.txt | sed 's/^/    /'
echo "  the argument guard precedes every network import: guard line $(grep -n '^if len(sys.argv) > 1' $P | cut -d: -f1), first network import line $(grep -n 'from clients import chat' $P | cut -d: -f1)"

echo; echo "## 6. a remote step tested only against stand-ins"
echo "  ssh or nohup in the runner: $(grep -cE '\bssh\b|nohup' $P || true)"
echo "  the far-end checks the method relies on: gate (ii) and the two judge gates; the judge gates cannot see an"
echo "  unparseable far end (item 3 above). Experiment D's judge script on why its cap is 3000:"
grep -n "Generous cap" -A1 experiments/03-retained-independence/src/judge_objection.py | sed 's/^/    /'
