#!/bin/sh
# Re-read the nine retrained built toy models and the three committed arm F
# toy models with the registered procedure (reads fitted fresh, processor). $0.
cd "$(dirname "$0")/../.." || exit 1
PY=$HOME/Code/minimum-viable-mind/.venv/bin/python
MD=out-sharpness-fix/models; OUT=out-sharpness-fix/reread; L=out-sharpness-fix/logs
FMD=../rehearsal-successor-measure/out-repairs/models
mkdir -p $OUT
wait_for() { until [ -f "$1" ]; do sleep 20; done; sleep 5; }
for s in 0 1 2; do
  wait_for $MD/ckpt_T_fixed_seed$s.pt
  $PY src/procedure.py model --ckpt $MD/ckpt_T_fixed_seed$s.pt --seed $s --out $OUT > $L/read_T_seed$s.log 2>&1
  $PY src/procedure.py model --ckpt $FMD/ckpt_F_base_seed$s.pt --arm F --size toy --seed $s --out $OUT > $L/read_F_seed$s.log 2>&1 &
  wait_for $MD/ckpt_C_fixed_seed$s.pt
  $PY src/procedure.py model --ckpt $MD/ckpt_C_fixed_seed$s.pt --seed $s --out $OUT > $L/read_C_seed$s.log 2>&1 &
  wait_for $MD/ckpt_M_fixed_seed$s.pt
  $PY src/procedure.py model --ckpt $MD/ckpt_M_fixed_seed$s.pt --seed $s --out $OUT > $L/read_M_seed$s.log 2>&1 &
  wait
  echo "seed $s read $(date)"
done
$PY src/procedure.py summarise --dir $OUT > $L/summarise.log 2>&1
echo ALL READS DONE
