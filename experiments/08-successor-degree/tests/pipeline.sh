#!/bin/sh
# Test T6 of docs/successor-code-freeze-method-2026-10-04.md: the whole
# pipeline at the 10-million and the registered 30-million size, on models
# trained for only a handful of steps, exactly as the rented machine would run
# the trainer and the laptop the measurement. Episode counts are scaled to a
# quarter and the null to 3 shuffles, so nothing here is a registered figure;
# untrained models are expected to return "no verdict", which is a pass here.
# Laptop processor, $0.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../src"
OUT="${1:?usage: pipeline.sh OUTDIR [SIZES]}"
SIZES="${2:-10M 30M}"
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
for size in $SIZES; do
  d="$OUT/$size"; mkdir -p "$d"
  for arm in T C M F; do
    "$PY" "$SRC/train_successor.py" --arm $arm --size $size --seed 0 --steps 30 --batch 32 \
      --eval-every 15 --device cpu --no-self-terminate --out "$d/ckpt_${arm}.pt" > "$d/train_${arm}.log" 2>&1
    tail -1 "$d/train_${arm}.log" | sed "s/^/  [$size $arm train] /"
    test -f "$d/ckpt_${arm}.DONE"
    "$PY" "$SRC/procedure.py" model --ckpt "$d/ckpt_${arm}.pt" --seed 0 --out "$d/measure" \
      --episode-scale 0.25 --shuffles 3 > "$d/measure_${arm}.log" 2>&1
    tail -1 "$d/measure_${arm}.log" | sed "s/^/  [$size $arm measure] /"
  done
  "$PY" "$SRC/procedure.py" summarise --dir "$d/measure" > "$d/summary.log" 2>&1
  tail -4 "$d/summary.log" | sed "s/^/  [$size summary] /"
done
echo "T6 ran to the end at: $SIZES"
