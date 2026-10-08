#!/bin/sh
# Independent check of the page 4 re-run (pull request 121), step 3: the
# findings' "How to recompute the 1,800 run", one model at a time, into a
# separate folder. Method: docs/2026-10-07-page4-rerun-check-method.md.
set -eu
PY=${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}
OUT=../out-page4-check/recompute-1800
mkdir -p "$OUT/models-1800" "$OUT/solver-1800"
date; uptime
for s in 0 1 2; do $PY page4_models_1800.py --pool 1980 --out $OUT/models-1800 --arm T --seed $s > $OUT/models-1800/log_T_seed$s.txt 2>&1; echo "T $s done $(date +%T)"; done
for a in C M F; do for s in 0 1 2; do
  $PY page4_models_1800.py --pool 1980 --out $OUT/models-1800 --arm $a --seed $s > $OUT/models-1800/log_${a}_seed$s.txt 2>&1; echo "$a $s done $(date +%T)"
done; done
$PY page4_models_1800.py --summarise $OUT/models-1800 > $OUT/models-1800/log_summarise.txt 2>&1
$PY page4_solver_1800.py --pool 1980 --out $OUT/solver-1800 > $OUT/log_solver_1800.txt 2>&1
date; uptime
