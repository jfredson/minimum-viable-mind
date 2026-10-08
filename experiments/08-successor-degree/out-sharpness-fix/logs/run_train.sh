#!/bin/sh
# Nine toy retrains, three at a time on the laptop's graphics processor. $0.
cd "$(dirname "$0")/../.." || exit 1
PY=$HOME/Code/minimum-viable-mind/.venv/bin/python
for s in 0 1 2; do
  for a in T C M; do
    $PY tests/retrain_toy_fixed.py --arm $a --seed $s --out out-sharpness-fix/models > out-sharpness-fix/logs/train_${a}_seed${s}.log 2>&1 &
  done
  wait
  echo "seed $s done $(date)"
done
echo ALL TRAINING DONE
