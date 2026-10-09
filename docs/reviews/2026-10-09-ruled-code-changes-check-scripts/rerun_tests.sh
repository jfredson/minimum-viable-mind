#!/bin/sh
# Checker's re-run of every test the pull request names (T1 self-tests, the
# made-up decision cases, the in-use cases, T2 model loading, T7 launcher).
# Run from experiments/08-successor-degree of a checkout of the branch.
#   sh rerun_tests.sh OUTDIR
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
M="${1:?OUTDIR}"; mkdir -p "$M"
export OMP_NUM_THREADS=2
sh src/run_self_tests.sh > "$M/t1.txt" 2>&1; echo "T1 exit $?" >> "$M/t1.txt"
"$PY" tests/a2_run_cases.py "$M/a2-cases" > "$M/a2.txt" 2>&1; echo "a2 exit $?" >> "$M/a2.txt"
"$PY" tests/inuse_cases.py --out "$M" > "$M/inuse.txt" 2>&1; echo "inuse exit $?" >> "$M/inuse.txt"
"$PY" tests/load_toy_models.py > "$M/t2.txt" 2>&1; echo "t2 exit $?" >> "$M/t2.txt"
sh tests/check_launcher.sh > "$M/t7.txt" 2>&1; echo "t7 exit $?" >> "$M/t7.txt"
echo "T1 checks passed: $(grep -c '\[PASS\]' "$M/t1.txt"), failed: $(grep -c '\[FAIL\]' "$M/t1.txt")"
tail -n 2 "$M/t1.txt" "$M/a2.txt" "$M/inuse.txt" "$M/t2.txt" "$M/t7.txt"
