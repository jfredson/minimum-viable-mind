#!/bin/sh
# Item 1: the dry run twice in a clean environment, compared byte for byte, a search for any file it
# wrote, and a third run with networking blocked. From the worktree root.
PY=/Users/john/Code/minimum-viable-mind/.venv/bin/python
R=docs/filtered-battery-2026-10-07/run_farend_repair_step1.py
S=docs/reviews/2026-10-19-farend-repair-step1-check-claude-code-scripts
T=$(mktemp -d); touch "$T/marker"; sleep 1
env -i HOME=$HOME PATH=/usr/bin:/bin $PY $R > "$T/1.txt" 2> "$T/1.err"; echo "run 1 exit $?"
env -i HOME=$HOME PATH=/usr/bin:/bin $PY $R > "$T/2.txt" 2> "$T/2.err"; echo "run 2 exit $?"
cmp -s "$T/1.txt" "$T/2.txt" && echo "standard output of runs 1 and 2: identical" || echo "standard output DIFFERS"
echo "error output bytes: $(wc -c < "$T/1.err" | tr -d ' ') and $(wc -c < "$T/2.err" | tr -d ' ')"
shasum -a 256 "$T/1.txt" "$T/2.txt" | awk '{print "sha256 " $1}'
echo "files created or changed since the first run started, under this worktree (outside this check's folder), the main checkout's artifacts and experiment D: $(find . /Users/john/Code/minimum-viable-mind/artifacts /Users/john/Code/minimum-viable-mind/experiments/03-retained-independence -newer "$T/marker" 2>/dev/null | grep -v "^./$S" | grep -v '^\.$' | wc -l | tr -d ' ')"
echo "run 3, networking blocked:"
env -i HOME=$HOME PATH=/usr/bin:/bin $PY $S/no_network_dry_run.py $R
echo "--- the dry run's output:"; cat "$T/1.txt"
echo; echo "--- the method file: lines added and removed by the pull request (sections 1 to 13 unchanged if 0 removed)"
git diff --numstat origin/main...HEAD -- docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md
echo "--- step-1 outputs on disk before any run:"; ls -d /Users/john/Code/minimum-viable-mind/artifacts/stage3/battery_rehearsal_repair1 2>&1
