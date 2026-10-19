#!/usr/bin/env bash
# Stand-in runs of the rehearsal runner's REAL-RUN code, for the check of pull
# request 174 (2026-10-17). Calls no model and spends nothing:
#   - everything runs in a scratch copy (argument 1) of the runner's folder, of
#     experiment D's src/ and of src/mvm/, never in the repository;
#   - the copy's clients.py is replaced by standin_clients.py, which returns
#     canned text and logs each call; D's real clients.py is not in the copy;
#   - every run gets a clean environment (env -i) holding no vendor key;
#   - experiment D's records are COPIED into the scratch folder, so the runner
#     reads copies and writes only under the copy's battery_rehearsal/.
# The runner file itself is copied unchanged, except in run F, where the copy's
# ceiling table is raised (and that copy is named as patched) so the run can
# reach the judge gate.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/standin_runs.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}
HERE=/Users/john/Code/minimum-viable-mind/.claude/worktrees/battery-method-2026-10-17/docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts
REPO=/Users/john/Code/minimum-viable-mind/.claude/worktrees/battery-method-2026-10-17
MAIN_ART=/Users/john/Code/minimum-viable-mind/artifacts/stage3
rm -rf "$SCR"; mkdir -p "$SCR/art"
cp -R "$MAIN_ART/ladder" "$MAIN_ART/ladder_scores" "$SCR/art/"

make_tree() {   # make_tree <dir>
  local T=$1
  mkdir -p "$T/docs" "$T/experiments/03-retained-independence" "$T/src"
  cp -R "$REPO/docs/filtered-battery-2026-10-07" "$T/docs/"
  cp -R "$REPO/experiments/03-retained-independence/src" "$T/experiments/03-retained-independence/"
  cp -R "$REPO/src/mvm" "$T/src/"
  cp "$HERE/standin_clients.py" "$T/experiments/03-retained-independence/src/clients.py"
}
RUNNER=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
run() {   # run <tree> <log> <entry> [extra env...]
  local T=$1 LOG=$2 E=$3; shift 3
  : > "$LOG"
  (cd "$T" && env -i HOME="$HOME" PATH="$PATH" PYTHONDONTWRITEBYTECODE=1 \
      MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="stand-in, not a go" MVM_WORKLOG_ROW="stand-in" \
      MVM_CEILING_E1="${CE1:-10}" MVM_CEILING_E2="${CE2:-10}" MVM_ENTRY="$E" MVM_STAGE3_ARTIFACTS="$SCR/art" STUB_LOG="$LOG" "$@" \
      python3 "$RUNNER" > "$LOG.stdout" 2> "$LOG.stderr")
  echo "exit $?"
}
count() { wc -l < "$1" | tr -d ' '; }

echo "### A. a pinned file changed by one byte (the copy's v1.1 rubric): the real run must refuse before any call"
make_tree "$SCR/treeA"; printf ' ' >> "$SCR/treeA/experiments/03-retained-independence/src/batteries/liveness_rubric.md"
run "$SCR/treeA" "$SCR/A.log" 1; echo "calls made: $(count "$SCR/A.log")"; cat "$SCR/A.log.stderr"

echo; echo "### B. the method file missing beside the runner: must refuse before any call"
make_tree "$SCR/treeB"; rm "$SCR/treeB/docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md"
run "$SCR/treeB" "$SCR/B.log" 1; echo "calls made: $(count "$SCR/B.log")"; cat "$SCR/B.log.stderr"

echo; echo "### C. entry 1 with the committed ceilings, stand-in replies at D's mean lengths"
make_tree "$SCR/treeC"
run "$SCR/treeC" "$SCR/C1.log" 1; echo "calls made: $(count "$SCR/C1.log")"; cat "$SCR/C1.log.stderr"
O="$SCR/art/battery_rehearsal/entry1"
for d in arm_S2 arm_B arm_B2 arm_S reference_always_agree judge/arm_S2 judge/arm_B judge/arm_B2 judge/arm_S; do
  printf "  %-28s %s files\n" "$d" "$( (ls "$O/$d" 2>/dev/null || true) | wc -l | tr -d ' ')"
done
grep "running spend" "$SCR/C1.log.stdout"

echo; echo "### D. the same command again (a resume): does the running estimate start from zero?"
run "$SCR/treeC" "$SCR/C2.log" 1; echo "new calls made: $(count "$SCR/C2.log")"; cat "$SCR/C2.log.stderr"
for d in arm_S judge/arm_S reference_always_agree; do
  printf "  %-28s %s files\n" "$d" "$( (ls "$O/$d" 2>/dev/null || true) | wc -l | tr -d ' ')"
done

echo; echo "### E. entry 2 with the committed ceilings"
run "$SCR/treeC" "$SCR/E.log" 2; echo "calls made: $(count "$SCR/E.log")"; cat "$SCR/E.log.stderr"
O2="$SCR/art/battery_rehearsal/entry2"
for d in own_rejudged_v12 other other_judge_v12; do
  printf "  %-28s %s files\n" "$d" "$( (ls "$O2/$d" 2>/dev/null || true) | wc -l | tr -d ' ')"
done
grep "labels moved" "$SCR/E.log.stdout"
python3 - "$SCR/E.log" <<'EOF'
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1])]
j = [r for r in recs if r["judge"] and r["v12"]]
print(f"  v1.2 judge calls: {len(j)}; system prompt carries the file's HTML comment: {sum(r['system_has_html_comment'] for r in j)} of {len(j)}")
if j:
    print(f"  what the judge reads first after D's preamble: {j[0]['system_after_preamble_head']!r}")
EOF

echo; echo "### F. unparseable judge output everywhere (STUB_JUDGE=garbage), entry 1, in a copy whose ceilings are raised to \$100000 (PATCHED COPY)"
make_tree "$SCR/treeF"
echo "  (fixed runner: ceilings raised through MVM_CEILING_E1=100, no copy patched)"
rm -rf "$SCR/art/battery_rehearsal"
CE1=100 run "$SCR/treeF" "$SCR/F.log" 1 STUB_JUDGE=garbage; echo "calls made: $(count "$SCR/F.log")"; tail -3 "$SCR/F.log.stderr"
python3 - "$SCR/art/battery_rehearsal/entry1" <<'EOF'
import json, sys, pathlib
o = pathlib.Path(sys.argv[1])
g = json.loads((o / "gate_judge_reliability.json").read_text())
print(f"  judge gate: n {g['n']}, agreement {g['agreement']}, gate_pass {g['gate_pass']}, disagreements {len(g['disagreements'])}, unreadable verdicts {g.get('unreadable_verdicts')}")
print(f"  analysis unreadable counts: {a_unread}") if False else None
a = json.loads((o / "analysis.json").read_text())
print(f"  rates: { {k: round(v, 3) for k, v in a['rates'].items()} }")
print(f"  gates: {a['gates']}")
print(f"  readings: {a['readings']}")
errs = sum("error" in json.loads(p.read_text())["verdicts"][0] for p in (o / "judge").rglob("*.json"))
print(f"  judge files holding an unparseable-verdict error record: {errs}")
EOF

echo; echo "### checks on the scratch copy itself"
echo "  repository files touched: $(cd "$REPO" && git status --porcelain | grep -v '^?? docs/reviews/2026-10-17-battery-rehearsal-method-check' | wc -l | tr -d ' ')"
echo "  main checkout's artifacts/stage3 has battery_rehearsal: $( [ -e "$MAIN_ART/battery_rehearsal" ] && echo yes || echo no)"
