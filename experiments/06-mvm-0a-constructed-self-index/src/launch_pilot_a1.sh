#!/bin/bash
# launch_pilot_a1.sh — A1 learnability pilot launcher (pre-registration
# §Amendment A1.6, ladder per §Materials). HUMAN-RUN ONLY [C2]: this script
# creates a billable pod and starts (or resumes) a training run; Claude
# prepares it, John executes it.
#
# Ladder rungs (env overrides):
#   10M rung:  SCALE=10M MAXTOK=171790000 ./launch_pilot_a1.sh   (ran 2026-08-09)
#   30M rung:  defaults below — 39,204,192 actual params x 20 tok/param
#   resume:    RESUME=$RUN_DIR/<ckpt>.pt ./launch_pilot_a1.sh (fresh pod; with
#              the network volume attached the checkpoint is already there)
#
# Registered 5-seed x full+twin (Amendment A2; 5090 SECURE only per A2):
#   full run:  SEED=<n> ./launch_pilot_a1.sh
#   twin run:  SEED=<n> TWIN=1 ./launch_pilot_a1.sh   (passes --twin; OUT
#              gains a _twin suffix; twin has no register params by config)
#   dry run:   DRYRUN=1 [...] ./launch_pilot_a1.sh — prints the pod-create
#              and train commands it WOULD run, creates nothing, spawns
#              nothing. Use before every real launch.
#
# PROCESS FIXES (2026-08-15, after the 30M pilot loss — see STATUS 2026-08-12):
#   1. Checkpoints + train.log go to the mvm-models NETWORK VOLUME
#      (/workspace), not container disk — pod death loses nothing.
#      NETVOL=none opts out (e.g. if EUR-IS-1 has no stock) and falls back
#      to container disk + the watchdog's hourly checkpoint pulls.
#   2. The launch schedules its own FETCH and its own KILL: it spawns
#      watch_run.sh locally (nohup + caffeinate), which polls, pulls
#      artifacts continuously, and on the DONE sentinel — or the deadline —
#      fetches everything and DELETES the pod. Keep this Mac powered on.
#   3. --terminate-after is ADVISORY ONLY (confirmed no-fire on pod
#      6bplni87uzp3ss); the watchdog deadline is the real backstop.
#
# Known-good ops patterns baked in (see memory/runpod-setup.md):
#   template-id not raw image; boot check via .ssh.ssh_command (top-level
#   sshCommand and uptimeSeconds are dead fields); strict=False JSON (raw
#   newlines in env); community pods need --public-ip (secure does not);
#   nohup child needs </dev/null; launch-ssh exit codes unreliable
#   (teardown resets) — trust the explicit aliveness check;
#   COPYFILE_DISABLE + --no-same-owner on tar.
set -uo pipefail

EXP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
SCALE="${SCALE:-30M}"
MAXTOK="${MAXTOK:-784083840}"                  # 20 tok/param x actual params
SEED="${SEED:-0}"
TWIN="${TWIN:-}"                               # TWIN=1 → --twin + _twin suffix
DRYRUN="${DRYRUN:-}"                           # DRYRUN=1 → print, create nothing
TWIN_SUFFIX=""; TWIN_FLAG=""
[ -n "$TWIN" ] && { TWIN_SUFFIX="_twin"; TWIN_FLAG="--twin"; }
OUT="${OUT:-pilot_a1_$(echo "$SCALE" | tr 'A-Z' 'a-z')_seed${SEED}${TWIN_SUFFIX}}"
GPU="${GPU:-NVIDIA GeForce RTX 5090}"          # A2 measured venue (0.65 s/step,
                                               # $0.99/hr; workload is enactment-
                                               # bound — H100 buys nothing)
CLOUD="${CLOUD:-SECURE}"                       # A2 registers SECURE-ONLY for the
                                               # 5-seed spend; COMMUNITY remains
                                               # only for non-registered smoke use
TERM_H="${TERM_H:-24}"                         # advisory runaway note, hours
WATCH_H="${WATCH_H:-24}"                       # watchdog hard deadline, hours
NETVOL="${NETVOL:-8xeftvclmv}"                 # mvm-models 150GB @ EUR-IS-1
RESUME="${RESUME:-}"
TERM_AT=$(date -u -v+"${TERM_H}"H +%Y-%m-%dT%H:%M:%SZ)
DEADLINE_EPOCH=$(( $(date +%s) + WATCH_H * 3600 ))

PUBIP=""
[ "$CLOUD" = "COMMUNITY" ] && PUBIP="--public-ip"

VOLARGS=""
RUN_DIR="/root/mvm/out"
if [ "$NETVOL" != "none" ]; then
  VOLARGS="--network-volume-id $NETVOL"
  RUN_DIR="/workspace/mvm-out"                 # network volume mount
  [ "$CLOUD" = "COMMUNITY" ] && { echo "network volumes are secure-cloud only; set NETVOL=none for COMMUNITY"; exit 1; }
fi

echo "creating $CLOUD pod ($GPU) for $SCALE/$MAXTOK tok (out: $OUT)"
echo "  run dir: $RUN_DIR $([ "$NETVOL" != "none" ] && echo '(network volume — survives pod death)')"
echo "  advisory terminate-after: $TERM_AT; watchdog kill deadline: +${WATCH_H}h"
if [ -n "$DRYRUN" ]; then
  cat <<DRYEOF
DRYRUN — nothing created. Would run:
  runpodctl pod create --name "mvm-$OUT" \\
    --template-id runpod-torch-v280 --gpu-id "$GPU" \\
    --cloud-type "$CLOUD" $PUBIP $VOLARGS --terminate-after "$TERM_AT"
  train: python train.py --scale $SCALE --seed $SEED $TWIN_FLAG --batch 128 \\
    --steps 200000 --max-tokens $MAXTOK --eval-every 500 --eval-n 100 \\
    --eval-mode heldout --device cuda --out $RUN_DIR/$OUT.pt
  watchdog env dest: $EXP_DIR/artifacts/$OUT
DRYEOF
  exit 0
fi
CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \
  --template-id runpod-torch-v280 --gpu-id "$GPU" \
  --cloud-type "$CLOUD" $PUBIP $VOLARGS --terminate-after "$TERM_AT")
echo "$CREATE_OUT"
POD=$(echo "$CREATE_OUT" | python3 -c '
import sys, json
try:
    d = json.JSONDecoder(strict=False).decode(sys.stdin.read())
    print(d.get("id") or "")
except Exception:
    print("")')
[ -n "$POD" ] || POD=$(echo "$CREATE_OUT" | grep -oE '"id"[": ]+[a-z0-9]{12,16}' | grep -oE '[a-z0-9]{12,16}$' | head -1)
if [ -z "$POD" ]; then
  echo "could not parse pod id — inspect output above"
  [ "$NETVOL" != "none" ] && echo "(if EUR-IS-1 has no $GPU stock: try GPU=\"NVIDIA H100 80GB HBM3\" [SECURE, ~3.3x cost], or wait for stock — COMMUNITY is NOT permitted for registered runs per Amendment A2)"
  exit 1
fi
echo "pod: $POD"

echo "waiting for SSH (uptimeSeconds is a dead field — polling .ssh.ssh_command)"
SSH_CMD=""
for i in $(seq 1 32); do
  SSH_CMD=$(runpodctl pod get "$POD" -o json 2>/dev/null | python3 -c '
import sys, json
try:
    d = json.JSONDecoder(strict=False).decode(sys.stdin.read())
    print((d.get("ssh") or {}).get("ssh_command") or "")
except Exception:
    print("")')
  [ -n "$SSH_CMD" ] && break
  sleep 15
done
if [ -z "$SSH_CMD" ]; then
  echo "no SSH after 8 min — pod will never boot; deleting (bills nothing while stuck)"
  runpodctl pod delete "$POD"
  echo "re-run me (stock rotates), or try NETVOL=none / another GPU"
  exit 1
fi
# keepalive/timeout opts: without them one network hang freezes the watchdog's
# fetch loop AND its deadline kill for the rest of the run
SSH="$SSH_CMD -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=20 -o ServerAliveInterval=30 -o ServerAliveCountMax=4 -o BatchMode=yes"
echo "ssh up: $SSH_CMD"

echo "pushing code + frozen batteries"
COPYFILE_DISABLE=1 tar czf - --exclude='__pycache__' --exclude='._*' \
    -C "$EXP_DIR" src batteries-a1 | \
  $SSH "mkdir -p $RUN_DIR /root/mvm && tar xzf - -C /root/mvm --no-same-owner"

RESUME_FLAG=""
[ -n "$RESUME" ] && RESUME_FLAG="--resume $RESUME"

echo "starting detached training run (log + checkpoints in $RUN_DIR)"
$SSH "cd /root/mvm/src && rm -f $RUN_DIR/$OUT.DONE && nohup python train.py \
  --scale $SCALE --seed $SEED $TWIN_FLAG --batch 128 --steps 200000 \
  --max-tokens $MAXTOK --eval-every 500 --eval-n 100 \
  --eval-mode heldout --device cuda $RESUME_FLAG \
  --out $RUN_DIR/$OUT.pt \
  > $RUN_DIR/train_$OUT.log 2>&1 < /dev/null &" \
  || echo "ssh teardown reset (benign if the aliveness check passes)"

sleep 20
# [t]rain guard: without it pgrep matches the checking shell itself — this
# false-positived "ALIVE" on the 2026-08-15 launch while nothing was running
$SSH "pgrep -f '[t]rain.py --scale' >/dev/null && echo 'ALIVE: training process confirmed' || echo \"NOT RUNNING — check $RUN_DIR/train_$OUT.log\"" \
  || echo "aliveness check ssh failed — poll manually"

# ---- process fix 2: the launch owns its fetch and its kill ----------------
DEST="$EXP_DIR/artifacts/$OUT"
mkdir -p "$DEST"
ENVF="$DEST/run_$POD.env"
cat > "$ENVF" <<ENVEOF
POD="$POD"
SSH="$SSH"
RUN_DIR="$RUN_DIR"
OUT="$OUT"
DEST="$DEST"
DEADLINE_EPOCH=$DEADLINE_EPOCH
ENVEOF
nohup caffeinate -i bash "$SRC_DIR/watch_run.sh" "$ENVF" \
  >> "$DEST/watchdog.log" 2>&1 < /dev/null &
WPID=$!
echo "watchdog spawned (pid $WPID, caffeinate holds off idle sleep) — KEEP THIS MAC POWERED ON"

cat <<EOF

LAUNCHED. pod=$POD
  watchdog:  tail -f '$DEST/watchdog.log'   (fetches continuously; on DONE or
             +${WATCH_H}h it fetches everything and DELETES the pod)
  poll:      $SSH_CMD 'tail -3 $RUN_DIR/train_$OUT.log'
  manual fetch:  $SSH_CMD 'tar czf - -C $RUN_DIR .' | tar xzf - -C '$DEST'
  manual kill:   runpodctl pod delete $POD
  resume after crash (C2 — John's go required): RESUME=$RUN_DIR/$OUT.pt $0
EOF
