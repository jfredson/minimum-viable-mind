#!/bin/bash
# The local checks behind
# experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rented-slice-attempt-2-check-claude-worktree.md
#
# Reads the checked commit (7da1946, draft pull request 51) and its ledger
# commit (3658a8f) straight out of git, so a re-run does not depend on any
# working copy. Contacts no vendor, rents nothing, spends nothing. The
# vendor readings are a separate, read-only script beside this one
# (vendor_readings.sh).
#
# Run from the repository root, with both commits fetched:
#   bash experiments/rehearsal-successor-measure/out/rented-slice-attempt-2-check-2026-09-25/check_attempt_2.sh
set -uo pipefail

C=7da1946                      # the checked commit
ROW=3658a8f                    # the ledger row, before anything was created
BASE=a96f873                   # main when the slice ran
R=experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2
LEDGER=experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
SRC=experiments/06-mvm-0a-constructed-self-index/src
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

echo "== 1. the ledger row: committed, and pushed, before the machine existed"
git log -1 --format='commit %h  author date %aI  committer date %cI  %s' "$ROW"
echo "  commit time in UTC: $(TZ=UTC git log -1 --date=format-local:%Y-%m-%dT%H:%M:%SZ --format=%cd "$ROW")"
echo "  push record (this Mac's copy of the remote branch; local to this repository):"
git reflog show --date=iso-strict refs/remotes/origin/worktree-mvm-w1f-rented-slice-attempt-2 2>/dev/null | sed 's/^/    /' \
  || echo "    (no local record of the remote branch)"
echo "  dry run started (step0-dryrun.txt line 1): $(git show "$C:$R/step0-dryrun.txt" | head -1)"
echo "  creation record (step1-launch.txt):"
git show "$C:$R/step1-launch.txt" | grep -n 'lastStatusChange\|^pod:\|MACHINE DEADLINE ARMED' | sed 's/^/    /'
git show "$ROW:$LEDGER" > "$T/ledger-row.md"
git show "$C:$LEDGER"   > "$T/ledger-c.md"
git show "$BASE:$LEDGER" > "$T/ledger-base.md"
echo "  lines the row commit added to the ledger: $(diff "$T/ledger-base.md" "$T/ledger-row.md" | grep -c '^>')"
L=$(diff "$T/ledger-base.md" "$T/ledger-row.md" | sed -n 's/^\([0-9]*\)a\([0-9]*\)$/\2/p')
echo "  the row is ledger line $L"
sed -n "${L}p" "$T/ledger-row.md" > "$T/row-before"
sed -n "${L}p" "$T/ledger-c.md"   > "$T/row-after"
for f in row-before row-after; do
  printf '  %-10s estimate "$0.75–1.00, hard cap $2.00" present: %s; go opens: %s; go signed: %s\n' "$f" \
    "$(grep -c -F '**$0.75–1.00, hard cap $2.00**' "$T/$f")" \
    "$(grep -c -F '“Go, second attempt.' "$T/$f")" \
    "$(grep -c -F 'John Fredrickson, 2026-09-25.”' "$T/$f")"
done
python3 - "$T/row-before" "$T/row-after" <<'EOF'
import sys
b, a = (open(p).read() for p in sys.argv[1:3])
go = lambda s: s[s.index("“Go, second attempt."):s.index("John Fredrickson, 2026-09-25.”") + len("John Fredrickson, 2026-09-25.”")]
print(f"  the go's text: {len(go(b))} characters before, {len(go(a))} after; identical: {go(b) == go(a)}")
cells = lambda s: [c.strip() for c in s.split(" | ")]
cb, ca = cells(b), cells(a)
print(f"  cells in the row: {len(cb)} before, {len(ca)} after; cells unchanged: "
      + ", ".join(str(i) for i in range(len(cb)) if cb[i] == ca[i])
      + "; cells changed: " + ", ".join(str(i) for i in range(len(cb)) if cb[i] != ca[i]))
print("  the settings the go names, each found in the plan's step 1 command at", "a96f873:")
EOF
git show "$BASE:experiments/rehearsal-successor-measure/out/rented-slice-plan.txt" > "$T/plan.txt"
for s in SCALE=10M MAXTOK=2000000 OUT=slice_handshake GRACE_S=600 RUN_SUBDIR=slice_handshake \
         CLEAR_RUN_SUBDIR=1 HARD_CAP_USD=2.00 RATE_PER_HOUR_USD=0.99 PRE_TRAIN_DIR PRE_TRAIN_CMD; do
  printf '    %-28s in the go: %s   in the plan: %s\n' "$s" "$(grep -c -F "$s" "$T/row-before")" "$(grep -c -F "$s" "$T/plan.txt")"
done

echo
echo "== 2. the actual: the two balance readings"
for f in pre-user.txt post-user.txt post-user-2.txt post-user-settled.txt billing-this-pod.txt post-pod-list.txt; do
  printf '  %-22s %s  %s\n' "$f" "$(git show "$C:$R/$f" | head -1)" \
    "$(git show "$C:$R/$f" | grep -o '"clientBalance": [0-9.]*' || git show "$C:$R/$f" | sed -n 2p)"
done
python3 -c "
a, b = 75.917054611, 75.864512286
print(f'  75.917054611 - 75.864512286 = {a-b:.9f}  -> \${a-b:.4f}')
print(f'  190 s at \$0.99 an hour = {190/3600*0.99:.6f}; the remainder {a-b-190/3600*0.99:.6f} is {(a-b-190/3600*0.99)/0.99*3600:.2f} s more at \$0.99, or {(a-b-190/3600*0.99)/0.01*3600:.0f} s at \$0.01')
"

echo
echo "== 3. bench_arms.json against the launcher's log"
git show "$C:$R/bench_arms.json" > "$T/bench.json"
git show "$C:$R/step1-launch.txt" > "$T/launch.txt"
python3 - "$T/bench.json" "$T/launch.txt" <<'EOF'
import json, re, sys
b = json.load(open(sys.argv[1])); a = b["arms"]
print(f'  "complete": {json.dumps(b["complete"])}, "device": {json.dumps(b["device"])}, accelerator {b["machine"]["accelerator"]}')
log = [l for l in open(sys.argv[2]).read().splitlines() if re.match(r"arm [TCF]:|ratios to", l)]
for k, line in zip("TCF", log):
    r = a[k]
    mine = f"arm {k}: {r['seconds_per_step']*1000:.1f} ms/step (median {r['median_seconds_per_step']*1000:.1f}), {r['parameters']:,} parameters"
    print(f"  json, 2 places: arm {k} mean {r['seconds_per_step']*1000:.2f} ms, median {r['median_seconds_per_step']*1000:.2f}, "
          f"fastest {r['fastest']*1000:.2f}, slowest {r['slowest']*1000:.2f}, {r['steps']} steps")
    print(f"    json at the log's precision: {mine}")
    print(f"    the launcher's log line:     {line}")
    print(f"    identical: {mine == line}")
F = a["F"]["seconds_per_step"]
rt, rc = a["T"]["seconds_per_step"] / F, a["C"]["seconds_per_step"] / F
print(f"  ratios recomputed from the means: T {rt:.3f}, C {rc:.3f}")
print(f"  ratios stored in the file:        T {b['ratio_to_arm_F']['T']:.3f}, C {b['ratio_to_arm_F']['C']:.3f}")
print(f"  the launcher's log line:          {log[3]}")
for k in "TCF":
    r = a[k]
    print(f"  arm {k}: slowest step is {100*(r['slowest']/r['median_seconds_per_step']-1):.1f}% above the median")
EOF

echo
echo "== 4. the second-release arithmetic"
mkdir -p "$T/tree"
git archive "$C" "$R" "$LEDGER" | tar -x -C "$T/tree"
( cd "$T/tree" && python3 "$R/second_release_arithmetic.py" ) > "$T/arith.txt"; echo "  script exit $?"
git show "$C:$R/second-release-arithmetic.txt" > "$T/arith-committed.txt"
cmp "$T/arith.txt" "$T/arith-committed.txt" && echo "  the re-run output is byte-identical to the committed second-release-arithmetic.txt"
grep -n -F '20.28 pod-hours at $0.99 = $20.08' "$T/ledger-c.md" | cut -c1-20 | sed 's/^/  ledger anchor ($10.04 a run) on line: /'
python3 - "$T/bench.json" <<'EOF'
import json, sys
a = json.load(open(sys.argv[1]))["arms"]
run = 20.08 / 2
r = {k: a[k]["seconds_per_step"] / a["F"]["seconds_per_step"] for k in "TCF"}
c = {k: run * r[k] for k in "TCF"}
eight = 2 * c["F"] + 3 * c["T"] + 3 * c["C"]
second = eight + c["C"] + 12 + 23
print(f"  independent recomputation: per run F {c['F']:.2f}, T {c['T']:.2f}, C {c['C']:.2f}; eight runs {eight:.2f}; "
      f"re-run {c['C']:.2f}; second release {second:.2f}; both releases {second + 32:.2f}")
print(f"  from the rounded ratios 1.044 and 1.080: second release {2*run + 3*run*1.044 + 3*run*1.080 + run*1.080 + 35:.2f}")
print(f"  headroom from $228.1 spent: $400 ceiling {400 - 228.1 - 32 - second:.1f}, $450 ceiling {450 - 228.1 - 32 - second:.1f}")
EOF
git show "$C:docs/successor-experiment-proposal-2026-09-21.md" > "$T/succ.md"
echo "  the provisional figures, in section 12.4 of the successor proposal:"
grep -n -F '| **$96** |' "$T/succ.md" | cut -d: -f1 | sed 's/^/    $96 (eight runs) on line /'
grep -n -F '| **Provisional total** | | | **$143** |' "$T/succ.md" | cut -d: -f1 | sed 's/^/    $143 (second release) on line /'
grep -n -F '| **First release, total** | | | **about $32** |' "$T/succ.md" | cut -d: -f1 | sed 's/^/    $32 (first release) on line /'
grep -n -F '$32 plus $143 is $175' "$T/succ.md" | cut -d: -f1 | sed 's/^/    $175 (both) on line /'
grep -n -F '**Five hundred steps per arm**' "$T/succ.md" | cut -d: -f1 | sed 's/^/    item R-11, "Five hundred steps per arm", on line /'

echo
echo "== 5. receipt, checksum and delete, in the logs, in order"
git show "$C:$R/watchdog.log" | grep -n 'final fetch OK\|VERIFIED\|receipt written\|deleting pod\|"deleted"\|pod gone'
echo "  the machine's own watcher log (reaper.log), last line fetched home:"
git show "$C:$R/reaper.log" | tail -1 | sed 's/^/    /'
echo "  lines in reaper.log containing 'receipt found': $(git show "$C:$R/reaper.log" | grep -c 'receipt found')"
echo "  model-md5.txt: $(git show "$C:$R/model-md5.txt")"
H=experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/slice_handshake.pt
M=$(git rev-parse --path-format=absolute --git-common-dir)/../$H
if [ -f "$M" ]; then echo "  md5 of the home copy now (git-ignored, main checkout): $(md5 -q "$M" 2>/dev/null || md5sum "$M" | cut -d' ' -f1), $(wc -c < "$M" | tr -d ' ') bytes"
else echo "  the home copy is not on this machine"; fi

echo
echo "== 6. the code behind 'the machine half cannot be seen on a normal run'"
echo "  code unchanged by the checked branch (files under both src folders, $BASE..$C): $(git diff --name-only "$BASE" "$C" -- "$SRC" experiments/rehearsal-successor-measure/src | wc -l | tr -d ' ')"
git show "$C:$SRC/watch_run_a3.sh" > "$T/watch.sh"
git show "$C:$SRC/reap_agent.sh" > "$T/reap.sh"
git show "$C:$SRC/launch_a3_fetch_first.sh" > "$T/launch.sh"
echo "  watch_run_a3.sh lines 235-245 (on_finished):"; sed -n 235,245p "$T/watch.sh" | sed 's/^/    /'
echo "  watch_run_a3.sh line 91: $(sed -n 91p "$T/watch.sh")"
echo "  watch_run_a3.sh: every line naming fetch_final (on_finished exits at line 244, after kill_pod):"
grep -n 'fetch_final' "$T/watch.sh" | sed 's/^/    /' 
echo "  reap_agent.sh line 97: $(sed -n 97p "$T/reap.sh")"
echo "  reap_agent.sh lines 234-236 and 258:"; sed -n 234,236p "$T/reap.sh" | sed 's/^/    /'; sed -n 258p "$T/reap.sh" | sed 's/^/    /'
echo "  launch_a3_fetch_first.sh: where AGENT_POLL_S is set and passed to the machine:"
grep -n 'AGENT_POLL_S' "$T/launch.sh" | sed 's/^/    /'
echo "  AGENT_POLL_S set anywhere in the plan's step 1 command: $(grep -c AGENT_POLL_S "$T/plan.txt")"
python3 - <<'EOF'
# The watcher saw the finished-marker at 01:49:01 (reaper.log). Each later pass
# of its loop is a check, then sleep 15. The receipt was written at 01:49:43 and
# the delete returned before 01:49:45 (watchdog.log: "pod gone" at :55, after a
# 10 s settle and a list call).
seen, poll = 1 * 60 + 1, 15
polls = [seen + poll * k for k in range(1, 4)]
print("  the watcher's next checks after 01:49:01, at 15 s apart: " + ", ".join(f"01:49:{p - 60:02d}" for p in polls))
print("  receipt written 01:49:43; delete issued 01:49:43; next check 01:49:46: the watcher sees the receipt")
print("  only if the vendor has not yet stopped the machine about 1 to 3 s after the delete returned.")
EOF

echo
echo "== 7. failure 6's test, on the launcher that ran (unchanged at $C)"
git archive "$C" experiments/06-mvm-0a-constructed-self-index/src | tar -x -C "$T/tree"
( cd "$T/tree" && python3 experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py ); echo "  exit $?"

echo
echo "== 8. the first attempt's leftover reaper.log: 469 bytes then, 469 bytes found"
git show "$C:experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25/remote-state-at-stop.txt" | grep -F 'reaper.log' | grep -F 'rw' | sed 's/^/  first attempt at its stop: /'
git show "$C:$R/step1-launch.txt" | grep -F 'reaper.log' | head -1 | sed 's/^ */  second attempt before clearing: /'

echo
echo "== 9. smaller checks cited in the review"
HB=$(git rev-parse --path-format=absolute --git-common-dir)/../experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/bench_arms.json
if [ -f "$HB" ]; then
  cmp "$HB" "$T/bench.json" && echo "  bench_arms.json: the fetched home copy is byte-identical to the slice receipts' copy"
else echo "  the home copy of bench_arms.json is not on this machine"; fi
echo "  reaper.log in the slice receipts: $(git show "$C:$R/reaper.log" | wc -c | tr -d ' ') bytes"
echo "  launcher line 510 (the folder-clear listing): $(sed -n 510p "$T/launch.sh" | sed 's/^ *//')"
echo "  the word 'probe' in the findings: $(git show "$C:docs/2026-09-25-rented-slice-attempt-2-findings.md" | grep -c -i probe); in the arithmetic note: $(git show "$C:docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md" | grep -c -i probe)"
echo "  files in the slice receipts carrying an email address: $(for f in $(git ls-tree --name-only "$C" "$R/"); do git show "$C:$f" | grep -q '"email": "[^<]' && echo "$f"; done | wc -l | tr -d ' ')"
echo "  files on main ($BASE) carrying one: $(git grep -l -E '"email": "[^<"]+@' "$BASE" | wc -l | tr -d ' ')"
