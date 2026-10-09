#!/bin/bash
S=/private/tmp/claude-501/-Users-john-Code-minimum-viable-mind/f29d71f5-3807-44d3-bb86-b4053eca7feb/scratchpad
cd "$S/rerun/experiments/08-successor-degree/out-decoy-w18" || exit 1
for v in "$@"; do
  start=$(date +%s)
  if [ "$v" = checks ]; then
    /Users/john/Code/minimum-viable-mind/.venv/bin/python decoy_w18.py --checks-only > "$S/rerun_$v.log" 2>&1
  else
    /Users/john/Code/minimum-viable-mind/.venv/bin/python decoy_w18.py --variant "$v" > "$S/rerun_$v.log" 2>&1
  fi
  echo "$v exit $? seconds $(( $(date +%s) - start ))" >> "$S/times.txt"
done
