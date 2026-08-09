#!/bin/bash
# launch_pilot_a1.sh — A1 10M learnability pilot (pre-registration §Amendment
# A1.6). HUMAN-RUN ONLY [C2]: this script creates a billable pod and starts a
# training run; Claude prepares it, John executes it.
#
# Known-good ops patterns baked in (see memory/runpod-setup.md):
#   template-id not raw image; --terminate-after ISO datetime as runaway
#   backstop; boot check via .ssh.ssh_command (top-level sshCommand and
#   uptimeSeconds are dead fields); strict=False JSON (raw newlines in env);
#   community pods need --public-ip; nohup child needs </dev/null;
#   COPYFILE_DISABLE + --no-same-owner on the tar push.
set -euo pipefail

EXP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
GPU="${GPU:-NVIDIA GeForce RTX 5090}"          # fallback: GPU="NVIDIA GeForce RTX 4090" ./launch_pilot_a1.sh
TERM_AT=$(date -u -v+6H +%Y-%m-%dT%H:%M:%SZ)   # est ~2.5-3.5h; 6h backstop

echo "creating community pod ($GPU), terminate-after $TERM_AT"
CREATE_OUT=$(runpodctl pod create --name mvm-a1-pilot \
  --template-id runpod-torch-v280 --gpu-id "$GPU" \
  --cloud-type COMMUNITY --public-ip --terminate-after "$TERM_AT")
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
  echo "re-run me (stock rotates), or try GPU=\"NVIDIA GeForce RTX 4090\" $0"
  exit 1
fi
SSH="$SSH_CMD -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
echo "ssh up: $SSH_CMD"

echo "pushing code + frozen batteries"
COPYFILE_DISABLE=1 tar czf - --exclude='__pycache__' --exclude='._*' \
    -C "$EXP_DIR" src batteries-a1 | \
  $SSH "mkdir -p /root/mvm/out && tar xzf - -C /root/mvm --no-same-owner"

echo "starting detached training run"
$SSH "cd /root/mvm/src && nohup python train.py \
  --scale 10M --seed 0 --batch 128 --steps 100000 \
  --max-tokens 171790000 --eval-every 500 --eval-n 100 \
  --eval-mode heldout --device cuda \
  --out /root/mvm/out/pilot_a1_10m_seed0.pt \
  > /root/mvm/train.log 2>&1 < /dev/null &"

cat <<EOF

LAUNCHED. pod=$POD  (terminate-after backstop: $TERM_AT)

poll:    $SSH_CMD 'tail -3 /root/mvm/train.log'
fetch:   mkdir -p '$EXP_DIR/artifacts/pilot-a1-10m-seed0' && $SSH_CMD 'tar czf - -C /root/mvm/out .' | tar xzf - -C '$EXP_DIR/artifacts/pilot-a1-10m-seed0'
delete:  runpodctl pod delete $POD    # ALWAYS delete when done (stopped pods bill disk)
EOF
