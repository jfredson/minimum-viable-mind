#!/bin/bash
# launch_a3.sh — Amendment A3 run launcher. HUMAN-RUN ONLY [C2]: this script
# creates a billable pod and starts (or resumes) a training run; Claude
# prepares it, John executes it, and the go is quoted verbatim in the
# ledger row.
#
# A SEPARATE FILE from launch_pilot_a1.sh on purpose. That launcher is the
# registered instrument of the A2 five-seed programme and the five existing
# checkpoints were produced by it; editing it would put their provenance in
# doubt. Every hard-won ops fix in it is carried over here verbatim, each
# with the incident that produced it.
#
# What differs from the A1 launcher, and why:
#   * runs train_a3.py, not train.py — the A3 grammar, tokenizer and the
#     action loss at the model's own revision position
#   * pushes batteries-a3, not batteries-a1
#   * REGISTER-LESS ONLY. A3 §2.4: the register is not trained in any A3
#     run. train_a3.py defaults to the twin; this script refuses to pass
#     --register at all, so there is no way to launch the wrong thing.
#   * token budget 585,544,960 = 20 tok/param x 29,277,248 actual params
#     (measured on the A3 twin config with the 105-token A3 vocabulary)
#   * no --eval-mode flag: A3 has one evaluation path
#   * --act-weight is passed explicitly because it is a registered choice
#     (A3 revision proposal, decision 10), never an implicit default
#   * a remote PRE-FLIGHT runs the module self-tests on the pod before a
#     single training step. A broken or truncated push previously cost a
#     whole run; the self-tests catch it in seconds, before billing starts
#     in earnest.
#
# Usage:
#   dry run:   DRYRUN=1 ./launch_a3.sh    — prints what it WOULD do, creates
#              nothing, spawns nothing. Run before every real launch.
#   pilot:     SEED=0 ./launch_a3.sh      (A3 Gate 2)
#   seeds:     SEED=1 ./launch_a3.sh      (after the lock)
#   resume:    RESUME=$RUN_DIR/<ckpt>.pt ./launch_a3.sh  — a resume is a
#              training launch and needs a FRESH go from John [C2]
#
# PROCESS FIXES carried over (2026-08-15, after the 30M pilot loss):
#   1. Checkpoints + train.log go to the NETWORK VOLUME, not container disk;
#      pod death loses nothing. NETVOL=none opts out.
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
MAXTOK="${MAXTOK:-585544960}"                  # 20 tok/param, A3 twin config
SEED="${SEED:-0}"
ACT_WEIGHT="${ACT_WEIGHT:-1.0}"                # registered, not implicit
DRYRUN="${DRYRUN:-}"
OUT="${OUT:-a3_$(echo "$SCALE" | tr 'A-Z' 'a-z')_seed${SEED}}"
GPU="${GPU:-NVIDIA GeForce RTX 5090}"          # measured venue: the workload
                                               # is enactment-bound, so an
                                               # H100 buys nothing
CLOUD="${CLOUD:-SECURE}"                       # A2 registers SECURE-ONLY for
                                               # registered spend
TERM_H="${TERM_H:-24}"
WATCH_H="${WATCH_H:-24}"
NETVOL="${NETVOL:-x9f8pkn58t}"                 # mvm-models-ro 100GB @ EU-RO-1
                                               # (waves 1-2 venue; the older
                                               # EUR-IS-1 volume 8xeftvclmv
                                               # predates the stock move and
                                               # may no longer exist — CHECK
                                               # before the first real launch)
RESUME="${RESUME:-}"
# Where fetched artifacts land. Defaults to the MAIN checkout, never the
# worktree this script happens to be running from: a git worktree is scratch
# space and can be removed when a session ends, which would take a ten-hour
# paid run's checkpoint with it. The canonical artifacts directory is where
# the existing checkpoints already live.
DEST_ROOT="${DEST_ROOT:-$HOME/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index}"
TERM_AT=$(date -u -v+"${TERM_H}"H +%Y-%m-%dT%H:%M:%SZ)
DEADLINE_EPOCH=$(( $(date +%s) + WATCH_H * 3600 ))

PUBIP=""
[ "$CLOUD" = "COMMUNITY" ] && PUBIP="--public-ip"

VOLARGS=""
RUN_DIR="/root/mvm/out"
if [ "$NETVOL" != "none" ]; then
  VOLARGS="--network-volume-id $NETVOL"
  RUN_DIR="/workspace/mvm-out"
  [ "$CLOUD" = "COMMUNITY" ] && { echo "network volumes are secure-cloud only; set NETVOL=none for COMMUNITY"; exit 1; }
fi

# ---- local pre-flight: never push a tree whose own tests fail -------------
echo "local pre-flight: module self-tests"
# the venv lives at the repo root; in a git worktree that is the worktree's
# own root, where the interpreter may not exist
PY_LOCAL="${PY_LOCAL:-}"
if [ -z "$PY_LOCAL" ]; then
  for c in "$EXP_DIR/../../.venv/bin/python" \
           "$HOME/Code/minimum-viable-mind/.venv/bin/python" \
           "$(command -v python3 2>/dev/null)"; do
    [ -n "$c" ] && [ -x "$c" ] && { PY_LOCAL="$c"; break; }
  done
fi
if [ -n "$PY_LOCAL" ] && [ -x "$PY_LOCAL" ]; then
  echo "  interpreter: $PY_LOCAL"
  for m in curriculum_a3 encoding_a3 train_a3; do
    if ! (cd "$SRC_DIR" && "$PY_LOCAL" "$m.py" --self-test >/dev/null 2>&1); then
      echo "  FAIL: $m self-test — refusing to launch"; exit 1
    fi
    echo "  ok: $m"
  done
else
  echo "  (no local interpreter at $PY_LOCAL — skipping; remote pre-flight still runs)"
fi
[ -f "$EXP_DIR/batteries-a3/batteries_meta.json" ] || {
  echo "batteries-a3 not frozen — run: python curriculum_a3.py --freeze ../batteries-a3"
  exit 1; }
echo "  ok: frozen batteries present"

echo "creating $CLOUD pod ($GPU) for $SCALE/$MAXTOK tok (out: $OUT)"
echo "  register-less by construction [A3 §2.4]; act-weight $ACT_WEIGHT"
echo "  run dir: $RUN_DIR $([ "$NETVOL" != "none" ] && echo '(network volume — survives pod death)')"
echo "  advisory terminate-after: $TERM_AT; watchdog kill deadline: +${WATCH_H}h"
echo "  artifacts -> $DEST_ROOT/artifacts/$OUT"

# --twin is passed EXPLICITLY even though train_a3.py already defaults to
# it. A3 section 2.4 forbids training the register, and a registered design
# choice must not be encoded as the absence of a flag: if that default ever
# moved, the absence would silently train the wrong architecture.
TRAIN_CMD="python train_a3.py --scale $SCALE --seed $SEED --twin --batch 128 \
--steps 200000 --max-tokens $MAXTOK --act-weight $ACT_WEIGHT \
--eval-every 500 --eval-n 100 --device cuda"

if [ -n "$DRYRUN" ]; then
  cat <<DRYEOF
DRYRUN — nothing created, nothing spawned. Would run:
  runpodctl pod create --name "mvm-$OUT" \\
    --template-id runpod-torch-v280 --gpu-id "$GPU" \\
    --cloud-type "$CLOUD" $PUBIP $VOLARGS --terminate-after "$TERM_AT"
  push: src + batteries-a3  ->  /root/mvm
  remote pre-flight: python curriculum_a3.py --self-test
                     python encoding_a3.py  --self-test
                     python train_a3.py     --self-test
  train: $TRAIN_CMD \\
    --out $RUN_DIR/$OUT.pt
  aliveness: pgrep -f '[t]rain_a3.py'
  watchdog env dest: $DEST_ROOT/artifacts/$OUT
  NOTE: the register is never trained in an A3 run; this script has no
        flag that could enable it.
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
  [ "$NETVOL" != "none" ] && echo "(if the region has no $GPU stock: wait for stock — COMMUNITY is NOT permitted for registered runs per Amendment A2)"
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
    -C "$EXP_DIR" src batteries-a3 | \
  $SSH "mkdir -p $RUN_DIR /root/mvm && tar xzf - -C /root/mvm --no-same-owner"

# ---- remote pre-flight: a truncated push must not become a billed run ----
echo "remote pre-flight (self-tests on the pod, before any training step)"
PREFLIGHT=$($SSH "cd /root/mvm/src && python curriculum_a3.py --self-test \
  && python encoding_a3.py --self-test && python train_a3.py --self-test" 2>&1)
echo "$PREFLIGHT" | sed 's/^/  /'
if ! echo "$PREFLIGHT" | grep -q "train_a3 self-test OK"; then
  echo "REMOTE PRE-FLIGHT FAILED — deleting the pod rather than billing a"
  echo "run on a broken tree. Inspect the output above."
  runpodctl pod delete "$POD"
  exit 1
fi

RESUME_FLAG=""
[ -n "$RESUME" ] && RESUME_FLAG="--resume $RESUME"

echo "starting detached training run (log + checkpoints in $RUN_DIR)"
# 2026-08-17: this ssh can HANG after the remote nohup succeeds — the
# keepalive opts keep the drained connection open forever (both wave-1
# launches needed their local ssh killed by hand). Hard-cap it at 60s;
# the explicit aliveness check below is the truth, not this exit status.
$SSH "cd /root/mvm/src && rm -f $RUN_DIR/$OUT.DONE && nohup $TRAIN_CMD \
  $RESUME_FLAG --out $RUN_DIR/$OUT.pt \
  > $RUN_DIR/train_$OUT.log 2>&1 < /dev/null &" &
START_PID=$!
( sleep 60; kill "$START_PID" 2>/dev/null ) >/dev/null 2>&1 &
wait "$START_PID" \
  || echo "ssh teardown reset/timeout (benign if the aliveness check passes)"

sleep 20
# [t]rain guard: without it pgrep matches the checking shell itself — this
# false-positived "ALIVE" on the 2026-08-15 launch while nothing was running
$SSH "pgrep -f '[t]rain_a3.py' >/dev/null && echo 'ALIVE: training process confirmed' || echo \"NOT RUNNING — check $RUN_DIR/train_$OUT.log\"" \
  || echo "aliveness check ssh failed — poll manually"

# ---- process fix 2: the launch owns its fetch and its kill ----------------
DEST="$DEST_ROOT/artifacts/$OUT"
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
nohup caffeinate -dimsu bash "$SRC_DIR/watch_run_a3.sh" "$ENVF" \
  >> "$DEST/watchdog.log" 2>&1 < /dev/null &
WPID=$!
echo "watchdog spawned (pid $WPID) — the pod now also self-terminates on completion, so this is the BACKSTOP not the only reap; still keep this Mac powered and the lid OPEN"

cat <<EOF

LAUNCHED. pod=$POD
  watchdog:  tail -f '$DEST/watchdog.log'   (fetches continuously; on DONE or
             +${WATCH_H}h it fetches everything and DELETES the pod)
  poll:      $SSH_CMD 'tail -3 $RUN_DIR/train_$OUT.log'
  manual fetch:  $SSH_CMD 'tar czf - -C $RUN_DIR .' | tar xzf - -C '$DEST'
  manual kill:   runpodctl pod delete $POD
  resume after crash (C2 — John's go required): RESUME=$RUN_DIR/$OUT.pt $0
  ledger: write the row in this session, with John's go quoted verbatim
EOF
