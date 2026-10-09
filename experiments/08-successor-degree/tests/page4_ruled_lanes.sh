#!/bin/sh
# The page 4 toy pass under the code ruled 2026-10-08, all twelve committed
# toy models, three lanes side by side (one per seed; arm T first in each,
# because the rider reads arm T's site set), then the summary.
# Method: docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md.
# Laptop processor, $0. NOT A RESULT.
#
#   sh tests/page4_ruled_lanes.sh OUTDIR           # pass B, the registered code
#   sh tests/page4_ruled_lanes.sh OUTDIR 3000      # pass A, the reproduction check
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:?usage: page4_ruled_lanes.sh OUTDIR [3000]}"
LIMIT="$2"
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
mkdir -p "$OUT"
date > "$OUT/log_times.txt"
uptime >> "$OUT/log_times.txt"
lane() {
  s=$1
  for arm in T C M F; do
    if [ -n "$LIMIT" ]; then
      "$PY" "$HERE/page4_ruled_model.py" --arm $arm --seed $s --out "$OUT" --limit "$LIMIT" > "$OUT/log_${arm}_seed${s}.txt" 2>&1 || echo "FAILED $arm $s" >> "$OUT/log_times.txt"
    else
      "$PY" "$HERE/page4_ruled_model.py" --arm $arm --seed $s --out "$OUT" > "$OUT/log_${arm}_seed${s}.txt" 2>&1 || echo "FAILED $arm $s" >> "$OUT/log_times.txt"
    fi
    echo "$(date +%H:%M:%S) done $arm/$s" >> "$OUT/log_times.txt"
  done
}
lane 0 &
lane 1 &
lane 2 &
wait
"$PY" "$HERE/../src/procedure.py" summarise --dir "$OUT" > "$OUT/log_summarise.txt" 2>&1
date >> "$OUT/log_times.txt"
echo "all lanes done"
