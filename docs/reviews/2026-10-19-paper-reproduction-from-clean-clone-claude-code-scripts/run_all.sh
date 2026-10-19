#!/bin/sh
# Re-runs, from a fresh clone, every check recorded in
# docs/reviews/2026-10-19-paper-reproduction-from-clean-clone-claude-code.md
# that can be re-run on a laptop at $0 (no model, nothing rented, no network after the install).
#
#   sh run_all.sh CLONE_DIR OUTPUT_DIR
#
# Needs Python 3.12 and the pinned libraries of experiments/08-successor-degree/requirements-measure.txt,
# installed in CLONE_DIR/.venv (python3.12 -m venv .venv; .venv/bin/pip install -r experiments/08-successor-degree/requirements-measure.txt).
set -u
R=${1:?clone directory}; O=${2:?output directory}
HERE=$(cd "$(dirname "$0")" && pwd)
PY="$R/.venv/bin/python"
mkdir -p "$O"
cd "$R" || exit 1

echo "== 1. cited paths exist";                 "$PY" "$HERE/check_cited_paths.py" "$R"        > "$O/check_cited_paths.out.txt" 2>&1
echo "== 2. Table 1 against removal_ci.json";   "$PY" "$HERE/check_table1.py" "$R"             > "$O/check_table1.out.txt" 2>&1
echo "== 3. bootstrap re-run (primary cells)";  "$PY" "$HERE/reproduce_removal_ci.py" "$R"     > "$O/reproduce_removal_ci.out.txt" 2>&1
echo "== 4. Table 2 from per-seed records";     "$PY" "$HERE/recompute_table2.py" "$R"         > "$O/recompute_table2.out.txt" 2>&1
echo "== 5. retained independence counts";      "$PY" "$HERE/recompute_ri.py" "$R"             > "$O/recompute_ri.out.txt" 2>&1
echo "== 6. frozen-code self-tests (about 5 min)"
PY="$PY" sh experiments/08-successor-degree/src/run_self_tests.sh                               > "$O/run_self_tests.out.txt" 2>&1
echo "== 7. toy in-use check (about 1 min)"
"$PY" experiments/08-successor-degree/tests/retrained_toy_inuse.py --models experiments/08-successor-degree/out-sharpness-fix/models --out "$O/retrained_toy_inuse.json" > "$O/retrained_toy_inuse.out.txt" 2>/dev/null
echo "== 8. summary step on the three committed rows"
rm -rf "$O/reruns-copy"; mkdir -p "$O/reruns-copy"; cp experiments/08-successor-degree/out-reruns-10m/row_*_seed0.json "$O/reruns-copy/"
"$PY" experiments/08-successor-degree/src/procedure.py summarise --dir "$O/reruns-copy" > "$O/summarise.out.txt" 2>/dev/null
cmp "$O/summarise.out.txt" experiments/08-successor-degree/out-reruns-10m/stdout_summarise.txt && echo "   stdout identical"
cmp "$O/reruns-copy/table.md" experiments/08-successor-degree/out-reruns-10m/table.md && echo "   table identical"
cmp "$O/reruns-copy/summary.json" experiments/08-successor-degree/out-reruns-10m/summary.json && echo "   summary identical"
echo "== 9. gate 1 cue detector (about 5 min), ceiling measurement (1 s)"
( cd experiments/06-mvm-0a-constructed-self-index/src && \
  "$PY" cue_detector_a3.py --run --out "$O/cue_detector_gate_a3_rerun.json" > "$O/cue_detector_run.out.txt" 2>&1 && \
  cmp "$O/cue_detector_gate_a3_rerun.json" ../a3-gates/cue_detector_gate_a3_final.json && echo "   gate 1 record identical" ; \
  "$PY" ceiling_measure_a3.py --run --out "$O/ceiling_measure_a3_rerun.json" > "$O/ceiling_run.out.txt" 2>&1 && \
  cmp "$O/ceiling_measure_a3_rerun.json" ../a3-gates/ceiling_measure_a3.json && echo "   ceiling record identical" )
echo "done; outputs in $O"
