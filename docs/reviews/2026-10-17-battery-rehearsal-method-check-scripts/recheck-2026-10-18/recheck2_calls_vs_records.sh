#!/usr/bin/env bash
# Second re-check, 2026-10-18, of commit 8850f66 (every record written before its
# cost counts): the dry run against its committed output, what the commit
# touched, and the stand-in cases C, D, E and H with calls made counted against
# calls held in records. Same stand-in terms as recheck_standin.sh (scratch copy,
# stand-in client, copied records, no vendor key, no runner copy patched). Calls
# no model.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recheck-2026-10-18/recheck2_calls_vs_records.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}
HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/../../../.." && pwd)
MAIN_ART=/Users/john/Code/minimum-viable-mind/artifacts/stage3
RUNNER=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
OUTF=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
rm -rf "$SCR"; mkdir -p "$SCR"
cd "$REPO"
echo "## the dry run (default bytecode caching on, clean environment)"
env -i HOME="$HOME" PATH="$PATH" python3 $RUNNER > "$SCR/dry.txt"; echo "exit $?"
cmp "$SCR/dry.txt" $OUTF && echo "cmp: identical"; shasum -a 256 $OUTF
echo ".pyc files left: $(find docs/filtered-battery-2026-10-07 experiments/03-retained-independence/src -name '*.pyc' | wc -l | tr -d ' ')"
echo; echo "## what commit 8850f66 touched"
git show --stat --format= 8850f66 | sed 's/^/  /'
echo "  runner diff lines outside the dry run's note and the four record-then-cost blocks:"
git show 8850f66 -- $RUNNER | grep -E '^[-+][^-+]' | grep -vE 'spend\.add|write_json|costs|NOTE|John.s go names|messages, replies, ctx|for s in calls|for ic, oc in costs|v1, ic1|v2, ic2' | sed 's/^/    /'
echo "    (end of list)"
echo "  committed dry-run output, lines changed: $(git show 8850f66 -- $OUTF | grep -cE '^[-+][^-+]')"

fresh_art() { rm -rf "$SCR/art"; mkdir -p "$SCR/art"; cp -R "$MAIN_ART/ladder" "$MAIN_ART/ladder_scores" "$SCR/art/"; }
T="$SCR/tree"; mkdir -p "$T/docs" "$T/experiments/03-retained-independence" "$T/src"
cp -R docs/filtered-battery-2026-10-07 "$T/docs/"; cp -R experiments/03-retained-independence/src "$T/experiments/03-retained-independence/"
cp -R src/mvm "$T/src/"; cp "$HERE/standin_clients_v2.py" "$T/experiments/03-retained-independence/src/clients.py"
cmp -s $RUNNER "$T/$RUNNER" && echo && echo "stand-in copy's runner identical to the committed runner"
run() { local LOG=$1 E=$2; shift 2; : > "$LOG"
  (cd "$T" && env -i HOME="$HOME" PATH="$PATH" MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="stand-in, not a go" MVM_WORKLOG_ROW="stand-in" \
     MVM_ENTRY="$E" MVM_STAGE3_ARTIFACTS="$SCR/art" STUB_LOG="$LOG" "$@" python3 "$RUNNER" > "$LOG.stdout" 2> "$LOG.stderr"); echo "exit $?"; }
held() { python3 - "$SCR/art/battery_rehearsal" <<'PY'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1]); n = 0; parts = {}
for p in root.rglob("*.json"):
    if p.name in ("plan.json", "analysis.json") or p.name.startswith("gate_judge_reliability"): continue
    d = json.loads(p.read_text())
    if "pass1" in d: k = 2                               # a gate pair: two judge calls
    elif "verdicts" in d: k = len(d["verdicts"])         # a judge record: one call per verdict
    else: k = len(d["turns"])                            # a subject record: one call per reply
    n += k; key = p.parent.relative_to(root).as_posix(); parts[key] = parts.get(key, 0) + k
print(n, "|", ", ".join(f"{k} {v}" for k, v in sorted(parts.items())))
PY
}
fresh_art
echo; echo "### C. entry 1 at \$10"; run "$SCR/C.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; head -1 "$SCR/C.log.stderr" | cut -c1-110
echo "  calls made $(wc -l < "$SCR/C.log" | tr -d ' '); calls held in records: $(held)"
echo "### D. the same command again"; run "$SCR/D.log" 1 MVM_CEILING_E1=10 MVM_CEILING_E2=10; head -1 "$SCR/D.log.stderr" | cut -c1-110
echo "  new calls made $(wc -l < "$SCR/D.log" | tr -d ' '); all calls made so far $(( $(wc -l < "$SCR/C.log") + $(wc -l < "$SCR/D.log") )); held: $(held | cut -d'|' -f1)"
echo "### E. entry 2 at \$10"; run "$SCR/E.log" 2 MVM_CEILING_E1=10 MVM_CEILING_E2=10; head -1 "$SCR/E.log.stderr" | cut -c1-110
E1=$(( $(wc -l < "$SCR/C.log") + $(wc -l < "$SCR/D.log") ))
echo "  entry 2 calls made $(wc -l < "$SCR/E.log" | tr -d ' '); held in all records now: $(held) (entry 1's share: $E1)"
fresh_art
echo "### H. entry 1 stopped inside the judge gate (ceiling \$20.22), then restarted at \$100"
run "$SCR/H1.log" 1 MVM_CEILING_E1=20.22 MVM_CEILING_E2=10; head -1 "$SCR/H1.log.stderr" | cut -c1-110
echo "  calls made $(wc -l < "$SCR/H1.log" | tr -d ' '); held: $(held | cut -d'|' -f1); gate pairs on disk: $(ls "$SCR/art/battery_rehearsal/entry1/gate_judge_reliability_pairs" | wc -l | tr -d ' ')"
run "$SCR/H2.log" 1 MVM_CEILING_E1=100 MVM_CEILING_E2=10
echo "  restart: new calls $(wc -l < "$SCR/H2.log" | tr -d ' '); total made $(( $(wc -l < "$SCR/H1.log") + $(wc -l < "$SCR/H2.log") )) (an uninterrupted entry 1 makes 1555); held: $(held | cut -d'|' -f1)"
echo; echo "repository files changed outside this re-check's folder: $(git status --porcelain --ignored | grep -v recheck-2026-10-18 | wc -l | tr -d ' ')"
