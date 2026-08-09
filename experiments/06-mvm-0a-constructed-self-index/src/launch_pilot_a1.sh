#!/bin/bash
# launch_pilot_a1.sh — A1 learnability pilot launcher (pre-registration
# §Amendment A1.6, ladder per §Materials). HUMAN-RUN ONLY [C2]: this script
# creates a billable pod and starts (or resumes) a training run; Claude
# prepares it, John executes it.
#
# Ladder rungs (env overrides):
#   10M rung:  SCALE=10M MAXTOK=171790000 ./launch_pilot_a1.sh   (ran 2026-08-09)
#   30M rung:  defaults below — 39,204,192 actual params x 20 tok/param
#   resume:    RESUME=/root/mvm/out/<ckpt>.pt ./launch_pilot_a1.sh (fresh pod;
#              fetch the checkpoint onto the pod first, or re-push artifacts)
#
# Known-good ops patterns baked in (see memory/runpod-setup.md):
#   template-id not raw image; --terminate-after ISO datetime as runaway
#   backstop; boot check via .ssh.ssh_command (top-level sshCommand and
#   uptimeSeconds are dead fields); strict=False JSON (raw newlines in env);
#   community pods need --public-ip (secure does not); nohup child needs
#   </dev/null; launch-ssh exit codes unreliable (teardown resets) — trust
#   the explicit aliveness check; COPYFILE_DISABLE + --no-same-owner on tar.
set -uo pipefail

EXP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCALE="${SCALE:-30M}"
MAXTOK="${MAXTOK:-784083840}"                  # 20 tok/param x actual params
OUT="${OUT:-pilot_a1_$(echo "$SCALE" | tr 'A-Z' 'a-z')_seed0}"
GPU="${GPU:-NVIDIA H100 80GB HBM3}"
CLOUD="${CLOUD:-SECURE}"                       # CLOUD=COMMUNITY adds --public-ip
TERM_H="${TERM_H:-24}"                         # runaway backstop, hours
RESUME="${RESUME:-}"
TERM_AT=$(date -u -v+"${TERM_H}"H +%Y-%m-%dT%H:%M:%SZ)

PUBIP=""
[ "$CLOUD" = "COMMUNITY" ] && PUBIP="--public-ip"

echo "creating $CLOUD pod ($GPU) for $SCALE/$MAXTOK tok, terminate-after $TERM_AT"
CREATE_OUT=$(runpodctl pod create --name "mvm-a1-pilot-$SCALE" \
  --template-id runpod-torch-v280 --gpu-id "$GPU" \
  --cloud-type "$CLOUD" $PUBIP --terminate-after "$TERM_AT")
echo "$CREATE_OUT"
POD=$(echo "$CREATE_OUT" | python3 -c '
import sys, json
try:
    d = json.JSONDecoder(strict=False).decode(sys.stdin.read())
    print(d.get("id") or "")
except Exception:
    print("")')
[ -n "$POD" ] || POD=$(echo "$CREATE_OUT" | grep -oE '"id"[": ]+[a-z0-9]{12,16}' | grep -oE '[a-z0-9]{12,16}$' | head -1)
[ -n "$POD" ] || { echo "could not parse pod id — inspect output above"; exit 1; }
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
  echo "re-run me (stock rotates), or try e.g. GPU=\"NVIDIA GeForce RTX 5090\" CLOUD=COMMUNITY $0"
  exit 1
fi
SSH="$SSH_CMD -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
echo "ssh up: $SSH_CMD"

echo "pushing code + frozen batteries"
COPYFILE_DISABLE=1 tar czf - --exclude='__pycache__' --exclude='._*' \
    -C "$EXP_DIR" src batteries-a1 | \
  $SSH "mkdir -p /root/mvm/out && tar xzf - -C /root/mvm --no-same-owner"

RESUME_FLAG=""
[ -n "$RESUME" ] && RESUME_FLAG="--resume $RESUME"

echo "starting detached training run"
$SSH "cd /root/mvm/src && nohup python train.py \
  --scale $SCALE --seed 0 --batch 128 --steps 200000 \
  --max-tokens $MAXTOK --eval-every 500 --eval-n 100 \
  --eval-mode heldout --device cuda $RESUME_FLAG \
  --out /root/mvm/out/$OUT.pt \
  > /root/mvm/train.log 2>&1 < /dev/null &" \
  || echo "ssh teardown reset (benign if the aliveness check passes)"

sleep 20
$SSH 'pgrep -f "train.py --scale" >/dev/null && echo "ALIVE: training process confirmed" || echo "NOT RUNNING — check /root/mvm/train.log"' \
  || echo "aliveness check ssh failed — poll manually"

cat <<EOF

LAUNCHED. pod=$POD  (terminate-after backstop: $TERM_AT)

poll:    $SSH_CMD 'tail -3 /root/mvm/train.log'
fetch:   mkdir -p '$EXP_DIR/artifacts/$OUT' && $SSH_CMD 'tar czf - -C /root/mvm/out .' | tar xzf - -C '$EXP_DIR/artifacts/$OUT'
delete:  runpodctl pod delete $POD    # ALWAYS delete when done (stopped pods bill disk)
resume after crash (C2 — John's go required): RESUME=/root/mvm/out/$OUT.pt $0
EOF
