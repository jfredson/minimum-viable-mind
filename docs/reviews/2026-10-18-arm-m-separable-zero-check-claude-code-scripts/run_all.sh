#!/bin/sh
# Re-run the check of pull request 180 (why arm M's separable half reads zero route use
# at 10 million parameters). From the worktree root:
#   sh docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code-scripts/run_all.sh
# $0: forward passes of saved checkpoints on the laptop's processor. About eight minutes.
set -e
PY=~/Code/minimum-viable-mind/.venv/bin/python
ROOT=$(pwd)
HERE="$ROOT/docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code-scripts"
SCRIPTS="$ROOT/docs/2026-10-18-arm-m-separable-zero-scripts"
TMP=$(mktemp -d)

echo "== the frozen folder against 6c47c56 (bytes of diff; 0 means unchanged)"
git diff 6c47c56 -- experiments/08-successor-degree/src/ | wc -c

echo "== the writer's ten scripts re-run, each output compared with the committed one"
cd "$SCRIPTS"
for f in d0_reproduce d1_bookkeeping d2_swap_reach d3_forced_row d4_named_by_route \
         d5_trunk_lesion d6_weights d7_flat_choice d8_answer_vector d9_stirred_in_items; do
  "$PY" "$f.py" > "$TMP/${f}_output.txt"
  if cmp -s "$TMP/${f}_output.txt" "${f}_output.txt"; then echo "$f: identical"
  else echo "$f: differs:"; diff "${f}_output.txt" "$TMP/${f}_output.txt" || true; fi
done

echo "== this check's own scripts"
cd "$HERE"
"$PY" e1_trunk_redirect.py
"$PY" e2_lesion_audit.py
"$PY" e3_figures_and_labels.py pr180_body_2026-10-18.md
"$PY" e4_start_spread.py
"$PY" e5_unused_markers.py
