#!/bin/bash
# launch_a3_fetch_first.sh — UNREGISTERED launcher: identical to the
# registered A3 launcher except that the rented machine is not allowed to
# delete itself until the files are home and checked.
#
# HUMAN-RUN ONLY [C2]: this script creates a billable pod and starts (or
# resumes) a training run; Claude prepares it, John executes it, and the go
# is quoted verbatim in the ledger row.
#
# WHY THIS IS A SEPARATE FILE, AND NOT A CHANGE TO launch_a3.sh.
# `src/launch_a3.sh` is REGISTERED TEXT: Amendment A3's "What is registered"
# section names it, along with the grammar, the tokenizer, the trainer
# `src/train_a3.py`, the frozen batteries and the gates. Registered text does
# not change without John's ruling. This is the repo's own precedent applied
# a third time: launch_a3.sh was itself split from launch_pilot_a1.sh, and
# launch_ctl_pilot.sh was split from launch_a3.sh, each time saying so.
#
# The trainer is registered too, so it is not edited either. It does not need
# to be: it already carries a `--no-self-terminate` switch. Passing a switch
# that already exists is not changing registered text, and it puts the
# shutdown decision where it belongs — in the operations scripts rather than
# in the scientific instrument.
#
# WHAT IT FIXES. Two shutdown mechanisms, built a month apart for the same
# problem, were cancelling each other out. The trainer asked the machine to
# delete itself within about a second of writing its finished-marker; the
# laptop watcher, which wakes every ten minutes and is the thing that takes
# the LAST copy of the files and checks it, found the machine already gone.
# On 2026-09-19 that is exactly what happened: the run completed its full
# budget, the last copy never happened, and the full-budget model file had to
# be read back off the network volume by a separately authorised rented
# machine. Both mechanisms were earning their keep — self-delete had just
# produced the first run in the programme's history with zero idle billing,
# and the laptop's final copy exists because $97.04 was lost on 2026-08-12 to
# a run whose files never came down. Diagnosis, the options weighed and the
# two questions left open for John: ../reap-shutdown-order-method.md.
#
# WHAT DIFFERS FROM launch_a3.sh, AND NOTHING ELSE DOES:
#   * it installs src/reap_agent.sh on the machine and CHECKS IT IS RUNNING.
#     That agent holds the machine open after training finishes until the
#     laptop writes a receipt saying it has the files and has checked them,
#     then deletes it at once; if the laptop never answers, it deletes anyway
#     after a bounded wait, but only when the files are on the network volume.
#   * it passes `--no-self-terminate` to the trainer, but ONLY when that check
#     passed, so the machine's shutdown decision moves to the agent.
#   * if the agent could not be started it says so loudly and falls back —
#     see ON_UNARMED below, which is a spending policy choice, not a
#     technical one.
#   * it drops the bare `sleep 24h; runpodctl remove pod` line, which the
#     agent now carries along with everything else.
#   * the watchdog environment file gains the volume id and the wait length,
#     so the recovery note the laptop writes can name them.
#
# The training recipe is untouched: same trainer, same grammar, same
# tokenizer, same frozen batteries, same token budget, same act-weight, same
# register-less-by-construction rule. Nothing that a result depends on moves.
#
# Everything below this header is carried over from launch_a3.sh verbatim
# except the blocks marked with a date. Three have been added since this file
# was derived: the shutdown-order blocks marked "2026-09-21", the guard that
# refuses command-line arguments, marked "2026-09-22", and the launch gate
# (sleep, scheduled fetch and delete, ledger row), marked "2026-09-24", which
# lives in src/launch_gate.sh and is shared with the other two unregistered
# launchers.
# src/derive_fetch_first_launcher.py, which produced this file, carries none
# of the three, so re-running it no longer reproduces this file.
#
# What differs from the A1 launcher, and why (carried over):
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
#   dry run:   DRYRUN=1 ./launch_a3_fetch_first.sh — prints what it WOULD do,
#              creates nothing, spawns nothing. Run before every real launch.
#   seeds:     SEED=1 ./launch_a3_fetch_first.sh
#   resume:    RESUME=$RUN_DIR/<ckpt>.pt ./launch_a3_fetch_first.sh — a resume
#              is a training launch and needs a FRESH go from John [C2]
#   before any real launch: a row in ../compute-ledger.md, dated today
#              (Pacific), naming $OUT, with its estimate — the launch gate
#              refuses without one (src/launch_gate.sh).
#   launch on a Mac that can still fall asleep:
#              ALLOW_LAPTOP_SLEEP=1 ./launch_a3_fetch_first.sh — overrides the
#              sleep check in the launch gate, and nothing else. A SPENDING
#              choice, not a technical one; src/launch_gate.sh says what it
#              costs.
#
# PROCESS FIXES carried over (2026-08-15, after the 30M pilot loss):
#   1. Checkpoints + train.log go to the NETWORK VOLUME, not container disk;
#      pod death loses nothing. NETVOL=none opts out.
#   2. The launch schedules its own FETCH and its own KILL: it spawns
#      watch_run_a3.sh locally (nohup + caffeinate), which polls, pulls
#      artifacts continuously, and on the finished-marker — or the deadline —
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

# 2026-09-22 [RT-198]: this launcher takes NO command-line arguments and never
# has. Before this guard an unrecognised flag was SILENTLY IGNORED and the
# script proceeded to a real launch at its defaults -- which is how a rented
# machine came to be created on 2026-09-21 by a command whose stated purpose
# was to create nothing. The exit below is explicit on purpose: this file runs
# under `set -uo pipefail` and deliberately NOT `set -e` (the remote launch
# command returns a benign non-zero status on a teardown reset), so a guard
# that only complained would complain and launch anyway.
# Method: ../argument-guard-method.md. Ruled by John 2026-09-22.
if [ "$#" -ne 0 ]; then
  echo "refusing to run: $(basename "$0") takes no command-line arguments." >&2
  echo "  got $# argument(s): $*" >&2
  echo "  this launcher is configured by environment variables; see the usage header." >&2
  echo "  to preview a launch without creating anything: DRYRUN=1 $0" >&2
  exit 2
fi

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
# ---- 2026-09-21: the shutdown-order knobs --------------------------------
# How long the machine waits for the laptop's receipt after training finishes
# before deleting itself anyway. A SPENDING choice: at $0.99/hour the default
# costs at most about $0.50 of idle billing on a run whose laptop never
# answers, against the 3.9h and 5.8h the old failure actually billed.
GRACE_S="${GRACE_S:-1800}"
AGENT_POLL_S="${AGENT_POLL_S:-15}"
# What to do if the machine's shutdown watcher will not start. Two honest
# choices, and this one is John's to make (see ../reap-shutdown-order-method.md
# §8): "self-terminate" keeps the trainer's own delete, so spending stays
# bounded and a normal finish costs one manual recovery, exactly as it does
# today; "laptop-only" leaves the delete to the laptop, which takes the final
# copy properly but bills open-endedly if the lid is shut. The default takes
# the money-safe side.
ON_UNARMED="${ON_UNARMED:-self-terminate}"
REAP_ARMED=0
# ---- 2026-09-25: a run of its own folder, and one step before training ----
# Both are OFF unless set, so every run that does not set them launches
# exactly as before. The rented slice sets them (stage_rented_slice.sh).
#
# RUN_SUBDIR: put this run's files in a folder of their own on the volume.
# The laptop's final copy takes EVERYTHING in the run folder, and the shared
# folder holds every earlier run's model files (2.5 GB on the last two A3
# copies), so without this a toy run brings all of them home again, on the
# clock, before its machine may be deleted.
RUN_SUBDIR="${RUN_SUBDIR:-}"
case "$RUN_SUBDIR" in
  */*|.|..) echo "refusing to run: RUN_SUBDIR must be a plain folder name, got '$RUN_SUBDIR'" >&2
            exit 2 ;;
esac
# PRE_TRAIN_DIR / PRE_TRAIN_CMD: push a local folder to /root/pre-train and
# run one command there, on the machine, BEFORE training starts, waiting for
# it to finish (at most PRE_TRAIN_TIMEOUT_S). Nothing can delete the machine
# before training writes its finished-marker except the +TERM_H deadline, so a
# step placed here always completes before the deletion. It also has the
# graphics card to itself. Its exit status is reported and does not stop the
# launch: training and the shutdown handshake go ahead either way.
PRE_TRAIN_DIR="${PRE_TRAIN_DIR:-}"
PRE_TRAIN_CMD="${PRE_TRAIN_CMD:-}"
PRE_TRAIN_TIMEOUT_S="${PRE_TRAIN_TIMEOUT_S:-1800}"
if [ -n "$PRE_TRAIN_DIR$PRE_TRAIN_CMD" ]; then
  if [ -z "$PRE_TRAIN_DIR" ] || [ -z "$PRE_TRAIN_CMD" ]; then
    echo "refusing to run: set both PRE_TRAIN_DIR and PRE_TRAIN_CMD, or neither" >&2
    exit 2
  fi
  [ -d "$PRE_TRAIN_DIR" ] || { echo "refusing to run: PRE_TRAIN_DIR '$PRE_TRAIN_DIR' is not a folder" >&2; exit 2; }
fi
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
[ -n "$RUN_SUBDIR" ] && RUN_DIR="$RUN_DIR/$RUN_SUBDIR"

# ---- local pre-flight: the launch gate -----------------------------------
# 2026-09-24. Refuses a real launch unless this Mac cannot fall asleep, the
# fetch and the delete are scheduled inside the run window, and a ledger row
# with an estimate exists for $OUT — the launch checklist, checked rather
# than trusted. The sleep check that sat here since pull request 28 moved
# into src/launch_gate.sh unchanged, with its reasons, so the other two
# unregistered launchers carry it too. A dry run reports and carries on.
# Method: ../launcher-sleep-gate-method.md.
WATCHDOG="$SRC_DIR/watch_run_a3.sh"            # spawned last, below
CAFFEINATE="${CAFFEINATE:-caffeinate}"         # the gate checks what is spawned
. "$SRC_DIR/launch_gate.sh"
launch_gate

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
# 2026-09-21: filled in below, once we know whether the machine's own
# shutdown watcher actually started. It is never guessed in advance.
SELFTERM_FLAG=""

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
$(if [ -n "$PRE_TRAIN_CMD" ]; then
  echo "  before training (waits for it, at most ${PRE_TRAIN_TIMEOUT_S}s):"
  echo "    push: $PRE_TRAIN_DIR  ->  /root/pre-train"
  echo "    run:  cd /root/pre-train && $PRE_TRAIN_CMD"
fi)
  train: $TRAIN_CMD \\
    --out $RUN_DIR/$OUT.pt
  aliveness: pgrep -f '[t]rain_a3.py'
  watchdog env dest: $DEST_ROOT/artifacts/$OUT
  shutdown watcher: sh reap_agent.sh /root/mvm/reap.env
                    (holds the machine open for the laptop's receipt, up to
                     ${GRACE_S}s, then deletes if the files are on the volume;
                     hard deadline +${TERM_H}h)
  trainer gets --no-self-terminate ONLY if that watcher is confirmed running;
  otherwise the fallback is ON_UNARMED=$ON_UNARMED
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

# ---- pod-side reaping: ENABLED by John's ruling of 2026-09-17 ------------
# A paid test on 2026-09-16 established that a pod carries NO credential and
# NO identifier of its own: RUNPOD_POD_ID absent, runpodctl present at
# /usr/bin/runpodctl but unconfigured. So pod-side reaping is impossible
# unless both are supplied.
#
# John ruled on 2026-09-17 to supply them, and ruled again on 2026-09-16
# Pacific that the credential pushed to a pod must NOT be his account key.
#
#   "Change it to read ONLY from ~/.runpod/reaper-key (a dedicated key,
#   mode 600, already saved ...). No fallback to config.toml."
#
# THE TRADEOFF AS IT NOW STANDS. The full-write account key in
# ~/.runpod/config.toml is no longer pushed to pods, and this script no
# longer reads that file at all. What goes onto the rented machine is a
# dedicated key scoped in the RunPod console to api.runpod.io/graphql
# read and write, with api.runpod.ai set to none. It can still manage pods,
# which is the whole point of a reaper and cannot be given up without
# giving up pod-side reaping, so a leak still costs pods and spend up to
# the account limit. What it no longer carries is the serverless surface,
# and being dedicated it can be rotated on its own without disturbing the
# local tooling that uses the account key.
#
# NO FALLBACK, BY RULING. If the file is missing, empty, or not mode 600,
# pod-side reaping is not armed and the run continues with the laptop
# watchdog as the only reap. Falling back to the account key would silently
# undo the ruling, which is worse than an unarmed reaper the operator is
# told about.
#
# What this buys: idle billing has cost about $9.50 across three runs
# because the reap waited on a laptop that was asleep, and a hung run that
# writes no DONE sentinel was covered by nothing at all. Both are now
# covered by the pod itself.
REAPER_KEY_FILE="$HOME/.runpod/reaper-key"
POD_KEY=""
REAP_REFUSAL=""
if [ ! -s "$REAPER_KEY_FILE" ]; then
  REAP_REFUSAL="no dedicated reaper key at ~/.runpod/reaper-key (missing or empty)"
else
  # BSD stat first (this launches from macOS), GNU stat as the fallback
  KEY_MODE=$(stat -f '%Lp' "$REAPER_KEY_FILE" 2>/dev/null \
             || stat -c '%a' "$REAPER_KEY_FILE" 2>/dev/null)
  if [ "$KEY_MODE" != "600" ]; then
    REAP_REFUSAL="reaper key mode is ${KEY_MODE:-unreadable}, not 600 — refusing to arm"
  else
    POD_KEY=$(tr -d ' \t\r\n' < "$REAPER_KEY_FILE")
    [ -n "$POD_KEY" ] || REAP_REFUSAL="reaper key file holds nothing once trimmed"
  fi
fi
# the key itself is never echoed, logged, or written to the ledger; only
# the refusal reason and the file's mode are ever printed.
if [ -n "$POD_KEY" ] && [ "$NETVOL" != "none" ]; then
  echo "arming pod-side reaping (credential + pod id supplied)"
  # configure the tool and record the pod's own id, which it does not know.
  # umask 077 so neither lands world-readable; nothing is echoed.
  $SSH "umask 077; runpodctl config --apiKey '$POD_KEY' >/dev/null 2>&1; \
        printf '%s' '$POD' > /root/mvm/pod_id; chmod 600 /root/mvm/pod_id" \
    >/dev/null 2>&1 && echo "  credential installed" \
                    || echo "  FAILED to install credential"
  # verify by a harmless read, never by a delete.
  # VERB-FIRST on purpose: the pod image ships runpodctl 1.14.15, which
  # has no `pod` subcommand at all ("unknown command \"pod\""). The local
  # CLI is 2.6.1 and takes the noun-first form, which is why line ~183
  # above differs. Measured on a live pod 2026-09-17; before this fix the
  # check could only ever report NOT VERIFIED, which after the
  # reaper-key change means a launch would stop on a false alarm.
  $SSH "runpodctl get pod \$(cat /root/mvm/pod_id) -o json 2>/dev/null \
        | grep -q '\"id\"' && echo VERIFIED || echo NOT_VERIFIED" \
    2>/dev/null | grep -qi VERIFIED \
    && echo "  VERIFIED: the pod can reach the API as itself" \
    || { echo "  NOT VERIFIED — the restricted reaper key could not reach"
         echo "  pod management. By John's ruling of 2026-09-16 there is NO"
         echo "  fallback to the account key: STOP and tell John. Until he"
         echo "  rules, the laptop watchdog is the only reap — lid OPEN."; }
  # ---- 2026-09-21: the machine's own shutdown watcher -------------------
  # This REPLACES the bare `sleep 24h; runpodctl remove pod` line the
  # registered launcher runs. That line covered one case, a run that HANGS.
  # src/reap_agent.sh covers that and the case the 2026-09-19 run hit: it
  # holds the machine open once training finishes, waiting for the laptop to
  # write a receipt saying it has the files and has checked them, and deletes
  # the moment that receipt lands. If the laptop never answers it deletes
  # anyway after GRACE_S, but only when the model file is on the network
  # volume, which outlives the machine. Same hard deadline as before.
  AGENT_DEADLINE=$(( $(date +%s) + TERM_H * 3600 ))
  $SSH "umask 077; printf '%s\n' \
        'RUN_DIR=\"$RUN_DIR\"' 'OUT=\"$OUT\"' \
        'POD_ID_FILE=\"/root/mvm/pod_id\"' \
        'DEADLINE_EPOCH=$AGENT_DEADLINE' 'GRACE_S=$GRACE_S' \
        'AGENT_POLL_S=$AGENT_POLL_S' > /root/mvm/reap.env" >/dev/null 2>&1
  $SSH "cd /root/mvm/src && nohup sh reap_agent.sh /root/mvm/reap.env \
        >> $RUN_DIR/reaper.log 2>&1 < /dev/null &" >/dev/null 2>&1
  sleep 5
  # [r]eap guard, same trap as the training aliveness check: without the
  # bracket, pgrep matches the checking shell itself and reports a false yes.
  if $SSH "pgrep -f '[r]eap_agent.sh' >/dev/null && echo AGENT_UP" 2>/dev/null \
       | grep -q AGENT_UP; then
    REAP_ARMED=1
    echo "  shutdown watcher RUNNING on the machine (waits ${GRACE_S}s for the"
    echo "  laptop's receipt; hard deadline +${TERM_H}h, laptop-independent)"
  else
    echo "  SHUTDOWN WATCHER DID NOT START — check $RUN_DIR/reaper.log on the"
    echo "  machine. Falling back per ON_UNARMED below."
  fi
else
  if [ "$NETVOL" = "none" ]; then
    REAP_REFUSAL="${REAP_REFUSAL:-NETVOL=none}"
  fi
  echo "REAP: pod-side reaping NOT armed — $REAP_REFUSAL"
  echo "  The laptop watchdog is then the ONLY reap — keep the lid OPEN."
fi

# ---- 2026-09-21: who deletes the machine, and when -----------------------
# With the shutdown watcher running, the TRAINER must not delete the machine
# itself — that is precisely the defect this launcher exists to fix. The
# trainer already carries the switch, so nothing registered changes here;
# only which switches this unregistered launcher passes.
if [ "$REAP_ARMED" = "1" ]; then
  SELFTERM_FLAG="--no-self-terminate"
  echo "SHUTDOWN ORDER: copy, check, receipt, delete — in that order."
  echo "  The trainer will NOT delete the machine; the watcher on it will,"
  echo "  as soon as this laptop confirms the files are home and checked,"
  echo "  or after ${GRACE_S}s if this laptop never answers."
else
  case "$ON_UNARMED" in
    laptop-only)
      SELFTERM_FLAG="--no-self-terminate"
      echo "SHUTDOWN ORDER: LAPTOP ONLY (ON_UNARMED=laptop-only)."
      echo "  Nothing on the machine will delete it. If this Mac sleeps or the"
      echo "  lid is shut, the machine bills until its +${WATCH_H}h deadline."
      echo "  KEEP THE LID OPEN." ;;
    *)
      echo "SHUTDOWN ORDER: the trainer deletes the machine itself"
      echo "  (ON_UNARMED=self-terminate, the money-safe fallback)."
      echo "  This is today's known defect: a run that finishes normally will"
      echo "  delete its machine before this laptop takes the final copy, and"
      echo "  the full-budget model file will need recovering from the volume."
      echo "  The laptop will write a NEEDS-RECOVERY.txt saying exactly how." ;;
  esac
fi

# ---- 2026-09-25: the step before training, if one was set ----------------
# Here, after the shutdown order is settled and before the trainer exists, so
# the finished-marker every deletion waits for cannot appear until it is done.
# The same hang guard as the training start below: a hung ssh must not hold
# the launch (and the watchdog it has yet to spawn) forever.
if [ -n "$PRE_TRAIN_CMD" ]; then
  echo "before training: pushing $PRE_TRAIN_DIR and running, at most ${PRE_TRAIN_TIMEOUT_S}s:"
  echo "  $PRE_TRAIN_CMD"
  COPYFILE_DISABLE=1 tar czf - --exclude='__pycache__' --exclude='._*' \
      -C "$PRE_TRAIN_DIR" . | \
    $SSH "mkdir -p /root/pre-train && tar xzf - -C /root/pre-train --no-same-owner"
  $SSH "cd /root/pre-train && $PRE_TRAIN_CMD" &
  PRE_PID=$!
  ( sleep "$PRE_TRAIN_TIMEOUT_S"; kill "$PRE_PID" 2>/dev/null ) >/dev/null 2>&1 &
  PRE_KILLER=$!
  if wait "$PRE_PID"; then
    echo "  before-training step finished (exit 0)"
  else
    echo "  BEFORE-TRAINING STEP DID NOT FINISH CLEANLY (failed, or cut off at"
    echo "  ${PRE_TRAIN_TIMEOUT_S}s). Its output above says which. Training goes ahead."
  fi
  kill "$PRE_KILLER" 2>/dev/null
fi

echo "starting detached training run (log + checkpoints in $RUN_DIR)"
# 2026-08-17: this ssh can HANG after the remote nohup succeeds — the
# keepalive opts keep the drained connection open forever (both wave-1
# launches needed their local ssh killed by hand). Hard-cap it at 60s;
# the explicit aliveness check below is the truth, not this exit status.
$SSH "cd /root/mvm/src && rm -f $RUN_DIR/$OUT.DONE $RUN_DIR/$OUT.FETCHED \
  && nohup $TRAIN_CMD $SELFTERM_FLAG \
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
NETVOL="$NETVOL"
GRACE_S=$GRACE_S
ENVEOF
nohup "$CAFFEINATE" -dimsu bash "$WATCHDOG" "$ENVF" \
  >> "$DEST/watchdog.log" 2>&1 < /dev/null &
WPID=$!
echo "watchdog spawned (pid $WPID). It takes the LAST copy of the files, checks"
echo "it against the machine, writes the receipt that releases the machine, and"
echo "deletes the machine itself if nothing on it does."

cat <<EOF

LAUNCHED. pod=$POD
  watchdog:  tail -f '$DEST/watchdog.log'   (fetches continuously; on the
             finished-marker or +${WATCH_H}h it fetches everything, checks it,
             releases the machine and DELETES the pod)
  machine's own watcher:  $SSH_CMD 'tail -f $RUN_DIR/reaper.log'
  if anything goes wrong, look for '$DEST/NEEDS-RECOVERY.txt' — the watchdog
  writes it, with the volume id and the exact recovery steps, whenever the
  files did not all make it home.
  poll:      $SSH_CMD 'tail -3 $RUN_DIR/train_$OUT.log'
  manual fetch:  $SSH_CMD 'tar czf - -C $RUN_DIR .' | tar xzf - -C '$DEST'
  manual kill:   runpodctl pod delete $POD
  resume after crash (C2 — John's go required): RESUME=$RUN_DIR/$OUT.pt $0
  ledger: write the row in this session, with John's go quoted verbatim
EOF
