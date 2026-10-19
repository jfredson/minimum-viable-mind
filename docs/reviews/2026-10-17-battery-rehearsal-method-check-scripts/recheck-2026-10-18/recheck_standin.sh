#!/usr/bin/env bash
# Re-check of the fixed runner's REAL-RUN code (commit 3b22925), 2026-10-18,
# against a stand-in client. Same safety terms as the first check's
# standin_runs.sh: a scratch copy of the code (argument 1) whose clients.py is
# standin_clients_v2.py (canned replies, every call logged, no network);
# experiment D's records COPIED into the scratch folder; a clean environment
# holding no vendor key. No copy of the runner is patched in this re-check: the
# ceilings are set through MVM_CEILING_E1 and MVM_CEILING_E2, as a real run sets
# them. Calls no model.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recheck-2026-10-18/recheck_standin.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}
HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/../../../.." && pwd)
MAIN_ART=/Users/john/Code/minimum-viable-mind/artifacts/stage3
RUNNER=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
rm -rf "$SCR"; mkdir -p "$SCR"
fresh_art() { rm -rf "$SCR/art"; mkdir -p "$SCR/art"; cp -R "$MAIN_ART/ladder" "$MAIN_ART/ladder_scores" "$SCR/art/"; }
make_tree() {
  local T=$1
  mkdir -p "$T/docs" "$T/experiments/03-retained-independence" "$T/src"
  cp -R "$REPO/docs/filtered-battery-2026-10-07" "$T/docs/"
  cp -R "$REPO/experiments/03-retained-independence/src" "$T/experiments/03-retained-independence/"
  cp -R "$REPO/src/mvm" "$T/src/"
  cp "$HERE/standin_clients_v2.py" "$T/experiments/03-retained-independence/src/clients.py"
  cmp -s "$REPO/$RUNNER" "$T/$RUNNER" || echo "  !! the copy's runner differs from the committed runner"
}
run() {   # run <tree> <log> <entry> [env...]
  local T=$1 LOG=$2 E=$3; shift 3
  : > "$LOG"
  (cd "$T" && env -i HOME="$HOME" PATH="$PATH" \
      MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="stand-in, not a go" MVM_WORKLOG_ROW="stand-in" \
      MVM_ENTRY="$E" MVM_STAGE3_ARTIFACTS="$SCR/art" STUB_LOG="$LOG" "$@" \
      python3 "$RUNNER" > "$LOG.stdout" 2> "$LOG.stderr")
  echo "exit $?"
}
count() { wc -l < "$1" | tr -d ' '; }
files() { for d in "$@"; do printf "  %-34s %s files\n" "$d" "$( (ls "$O/$d" 2>/dev/null || true) | wc -l | tr -d ' ')"; done; }
fresh_art; make_tree "$SCR/tree"; T="$SCR/tree"; O="$SCR/art/battery_rehearsal/entry1"

echo "### G. ceiling refusals, with the go quote and the worklog row set (each must refuse before any call)"
for spec in "none" "E1=21" "E1=abc E2=17" "E1=0 E2=17" "E1=150 E2=17" "E1=21 E2=-1"; do
  args=(); [ "$spec" != none ] && for kv in $spec; do args+=("MVM_CEILING_${kv}"); done
  c=$(run "$T" "$SCR/G.log" 1 ${args[@]+"${args[@]}"})
  echo "  [$spec]: $c; calls $(count "$SCR/G.log"); $(head -1 "$SCR/G.log.stderr" | cut -c1-90)"
done

echo; echo "### A. a pinned file changed by one byte: must refuse before any call"
make_tree "$SCR/treeA"; printf ' ' >> "$SCR/treeA/experiments/03-retained-independence/src/batteries/liveness_rubric.md"
run "$SCR/treeA" "$SCR/A.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; echo "calls made: $(count "$SCR/A.log")"; cat "$SCR/A.log.stderr"
echo; echo "### B. the method file missing: must refuse before any call"
make_tree "$SCR/treeB"; rm "$SCR/treeB/docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md"
run "$SCR/treeB" "$SCR/B.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; echo "calls made: $(count "$SCR/B.log")"; cat "$SCR/B.log.stderr"

echo; echo "### C. entry 1 at \$10, stand-in replies at D's mean lengths"
run "$T" "$SCR/C1.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; echo "calls made: $(count "$SCR/C1.log")"; head -1 "$SCR/C1.log.stderr"
files arm_S2 arm_B arm_B2 arm_S reference_always_agree judge/arm_S2 judge/arm_B judge/arm_B2 judge/arm_S

echo; echo "### D. the same command again, same \$10: the estimate must include the earlier start"
run "$T" "$SCR/C2.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; echo "new calls made: $(count "$SCR/C2.log")"; head -1 "$SCR/C2.log.stderr"
files arm_S judge/arm_S

echo; echo "### D2. again, with the ceiling raised to \$15 (a fresh go naming a new ceiling for the whole entry)"
run "$T" "$SCR/C3.log" 1 MVM_CEILING_E1=15 MVM_CEILING_E2=10; echo "new calls made: $(count "$SCR/C3.log")"; head -1 "$SCR/C3.log.stderr"
files arm_S judge/arm_S reference_always_agree

echo; echo "### H. a stop inside the judge gate, then a restart: gate pairs already judged must not be called again"
fresh_art
run "$T" "$SCR/H0.log" 1 MVM_CEILING_E1=100 MVM_CEILING_E2=10 > /dev/null
TOTAL=$(python3 -c "import json;print(json.load(open('$O/analysis.json'))['spend_estimate_running'])")
echo "  a full entry 1 in the stand-in: $(count "$SCR/H0.log") calls, running estimate \$$TOTAL"
fresh_art
CUT=$(python3 -c "print(round($TOTAL - 0.9, 2))")
run "$T" "$SCR/H1.log" 1 MVM_CEILING_E1=$CUT MVM_CEILING_E2=10; echo "  ceiling \$$CUT: calls made $(count "$SCR/H1.log"); $(head -1 "$SCR/H1.log.stderr" | cut -c1-120)"
PAIRS=$(ls "$O/gate_judge_reliability_pairs" 2>/dev/null | wc -l | tr -d ' ')
echo "  gate pairs on disk after the stop: $PAIRS"
run "$T" "$SCR/H2.log" 1 MVM_CEILING_E1=100 MVM_CEILING_E2=10
N2=$(count "$SCR/H2.log")
echo "  restart at \$100: new calls $N2 (all should be gate calls: 120 - 2 x $PAIRS = $((120 - 2 * PAIRS)))"
python3 - "$O/analysis.json" "$TOTAL" <<'EOF'
import json, sys
a = json.load(open(sys.argv[1]))
print(f"  after the restart: running estimate ${a['spend_estimate_running']:.4f} (an uninterrupted run: ${float(sys.argv[2]):.4f}); "
      f"new calls {a['calls']}, calls from earlier starts {a['calls_from_earlier_starts']}")
EOF

echo; echo "### E. entry 2 at \$10, and what the version 1.2 judge receives"
run "$T" "$SCR/E.log" 2 MVM_CEILING_E1=10 MVM_CEILING_E2=10; echo "calls made: $(count "$SCR/E.log")"; head -1 "$SCR/E.log.stderr"
O2="$SCR/art/battery_rehearsal/entry2"
for d in own_rejudged_v12 other other_judge_v12; do printf "  %-34s %s files\n" "$d" "$( (ls "$O2/$d" 2>/dev/null || true) | wc -l | tr -d ' ')"; done
python3 - "$SCR/E.log" "$O2/plan.json" "$REPO/docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt" "$REPO" <<'EOF'
import hashlib, json, re, sys
from pathlib import Path
recs = [json.loads(l) for l in open(sys.argv[1])]
plan = json.load(open(sys.argv[2]))
dry = Path(sys.argv[3]).read_text()
repo = Path(sys.argv[4])
j = [r for r in recs if r["judge"] and r["v12"]]
print(f"  v1.2 judge calls: {len(j)}; carrying the file's HTML comment: {sum(r['system_has_html_comment'] for r in j)}")
print(f"  distinct system prompts among them: {len(set(r['system_sha256'] for r in j))}; equals plan.json's judge_system_prompt_v12_sha256: "
      f"{set(r['system_sha256'] for r in j) == {plan['judge_system_prompt_v12_sha256']}}")
printed = re.search(r"handed to the judge: (\d+) characters, sha256 ([0-9a-f]{64})", dry)
print(f"  rubric part the judge received equals the dry run's printed sha256: {set(r['rubric_part_sha256'] for r in j) == {printed.group(2)}}")
v11 = (repo / "experiments/03-retained-independence/src/batteries/liveness_rubric.md").read_text()
v12 = (repo / "docs/filtered-battery-2026-10-07/liveness_rubric_v1.2_entry2.md").read_text()
add = v12[v12.index("\n## Named-source addendum"):]
mine = hashlib.sha256((v11 + add).encode()).hexdigest()
print(f"  this check's own build of 'v1.1 text + addendum' (sha {mine[:16]}...) equals what the judge received: {mine == printed.group(2)}")
print(f"  first words after D's preamble: {j[0]['system_after_preamble_head'][:60]!r}")
EOF

echo; echo "### F. every judge reply unreadable (STUB_JUDGE=garbage), entry 1, ceiling \$100 through the variable"
fresh_art
run "$T" "$SCR/F.log" 1 MVM_CEILING_E1=100 MVM_CEILING_E2=10 STUB_JUDGE=garbage; echo "calls made: $(count "$SCR/F.log")"
python3 - "$O" <<'EOF'
import json, sys, pathlib
o = pathlib.Path(sys.argv[1])
g = json.loads((o / "gate_judge_reliability.json").read_text())
print(f"  judge gate: n {g['n']}, agreement {g['agreement']}, gate_pass {g['gate_pass']}, unreadable verdicts {g['unreadable_verdicts']}, "
      f"pairs with an unreadable pass {g['pairs_with_an_unreadable_pass']}")
a = json.loads((o / "analysis.json").read_text())
print(f"  gates: {a['gates']}")
print(f"  readings: {a['readings']}")
print(f"  unreadable verdicts by arm in analysis.json: {a['unreadable_verdicts_by_arm']}; gate: {a['gate_iii_unreadable_verdicts']}")
EOF

echo; echo "### checks on the repository itself"
echo "  files changed in the repository outside this re-check's folder: $(cd "$REPO" && git status --porcelain --ignored | grep -v 'recheck-2026-10-18' | wc -l | tr -d ' ')"
echo "  battery_rehearsal/ in the main checkout: $( [ -e "$MAIN_ART/battery_rehearsal" ] && echo yes || echo no)"
