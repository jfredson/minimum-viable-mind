#!/bin/sh
# Checker's re-run of the page 4 toy models under the code of pull request 151.
# Run from the root of a checkout of the pull request's branch (the code as it
# would merge: nothing under experiments/ differs between the branch and its
# merge with main). Laptop processor, $0.
#
#   sh rerun_models.sh OUT_B OUT_A
#
# OUT_B, pass B: all twelve toy models, `procedure.py model` called directly
#   (not through the session's driver), at the code's own limit of 10,000.
# OUT_A, pass A sample: arm M seed 1 (240 warnings at the old limit) and arm C
#   seed 2 (the one arm C warning), each after its arm T seed (the rider reads
#   arm T's site set), through the session's driver with --limit 3000, the
#   only way to set the old limit.
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
EXP=experiments/08-successor-degree
MOD=experiments/rehearsal-successor-measure/out-repairs/models
B="${1:?OUT_B}"; A="${2:?OUT_A}"
mkdir -p "$B" "$A"
export OMP_NUM_THREADS=3 MKL_NUM_THREADS=3
laneB() {
  for arm in T C M F; do
    "$PY" $EXP/src/procedure.py model --ckpt $MOD/ckpt_${arm}_base_seed$1.pt --out "$B" \
      --arm $arm --size toy --seed $1 > "$B/log_${arm}_seed$1.txt" 2>&1 || echo "FAILED $arm $1" >> "$B/times.txt"
    echo "$(date +%H:%M:%S) done $arm/$1" >> "$B/times.txt"
  done
}
laneA() {
  for arm in T $2; do
    "$PY" $EXP/tests/page4_ruled_model.py --arm $arm --seed $1 --out "$A" --limit 3000 --threads 3 \
      > "$A/log_${arm}_seed$1.txt" 2>&1 || echo "FAILED $arm $1" >> "$A/times.txt"
    echo "$(date +%H:%M:%S) done $arm/$1" >> "$A/times.txt"
  done
}
date > "$B/times.txt"; date > "$A/times.txt"
laneB 0 & laneB 1 & laneB 2 &
laneA 1 M & laneA 2 C &
wait
"$PY" $EXP/src/procedure.py summarise --dir "$B" > "$B/log_summarise.txt" 2>&1
date >> "$B/times.txt"
echo "all done"
