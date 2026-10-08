#!/bin/sh
# Page 4 toy re-run: every step, in order. Method, committed before this ran:
# docs/2026-10-06-page4-toy-rerun-1800-method.md, section 3.
# Run from experiments/rehearsal-successor-measure/src. Laptop, processor, $0.
# Usage: sh page4_run_all.sh [JOBS]   (JOBS: models run side by side; default 4)
set -eu
PY=${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}
JOBS=${1:-4}
OUT=../out-page4-rerun-1800
mkdir -p "$OUT"

models() {   # $1 pool, $2 directory
  d="$OUT/$2"; mkdir -p "$d"
  # arm T first, its three seeds side by side: the rider of every other arm reads arm T's site set
  for s in 0 1 2; do echo "T $s"; done | xargs -P 3 -n 2 sh -c \
    "$PY page4_models_1800.py --pool $1 --out $d --arm \$0 --seed \$1 > $d/log_\$0_seed\$1.txt 2>&1"
  for a in C M F; do for s in 0 1 2; do echo "$a $s"; done; done | xargs -P "$JOBS" -n 2 sh -c \
    "$PY page4_models_1800.py --pool $1 --out $d --arm \$0 --seed \$1 > $d/log_\$0_seed\$1.txt 2>&1"
  $PY page4_models_1800.py --summarise "$d" > "$d/log_summarise.txt" 2>&1
}

# 1. reproduction checks at 420 fitted (section 4): must equal the committed runs
models 600 models-420
$PY page4_solver_1800.py --pool 600 --out "$OUT/solver-420" > "$OUT/log_solver_420.txt" 2>&1
$PY page4_compare.py --reproduction-only > "$OUT/log_reproduction.txt" 2>&1 \
  || { cat "$OUT/log_reproduction.txt"; echo "stop"; exit 1; }   # stops here if either differs
cat "$OUT/log_reproduction.txt"
# 2. the re-run at 1,800 fitted (section 2)
models 1980 models-1800
$PY page4_solver_1800.py --pool 1980 --out "$OUT/solver-1800" > "$OUT/log_solver_1800.txt" 2>&1
# 3. the comparison (sections 4 to 6)
$PY page4_compare.py | tee "$OUT/log_compare.txt"
