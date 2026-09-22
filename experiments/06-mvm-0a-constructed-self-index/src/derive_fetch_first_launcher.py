#!/usr/bin/env python3
"""Derive src/launch_a3_fetch_first.sh from the registered src/launch_a3.sh.

Run once. The registered file is READ ONLY here; it is never written.
Every replacement below is asserted to have matched exactly once, so a
silent drift in the source cannot produce a half-patched launcher.
"""
import sys
from pathlib import Path

SRC = Path(sys.argv[1])
DST = Path(sys.argv[2])
text = SRC.read_text()

NEW_HEADER = '''#!/bin/bash
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
# except the blocks marked "2026-09-21".
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
set -uo pipefail'''

# ---- 1. header ----------------------------------------------------------
head_end = text.index("set -uo pipefail") + len("set -uo pipefail")
text = NEW_HEADER + text[head_end:]

def sub_once(old, new):
    global text
    assert text.count(old) == 1, f"expected exactly one match for:\n{old[:120]}"
    text = text.replace(old, new)

# ---- 2. knobs -----------------------------------------------------------
sub_once(
    'RESUME="${RESUME:-}"\n',
    '''RESUME="${RESUME:-}"
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
''')

# ---- 3. the self-terminate switch, decided later -------------------------
sub_once(
    '--eval-every 500 --eval-n 100 --device cuda"\n',
    '''--eval-every 500 --eval-n 100 --device cuda"
# 2026-09-21: filled in below, once we know whether the machine's own
# shutdown watcher actually started. It is never guessed in advance.
SELFTERM_FLAG=""
''')

# ---- 4. dry run ---------------------------------------------------------
sub_once(
    """  NOTE: the register is never trained in an A3 run; this script has no
        flag that could enable it.
DRYEOF""",
    """  shutdown watcher: sh reap_agent.sh /root/mvm/reap.env
                    (holds the machine open for the laptop's receipt, up to
                     ${GRACE_S}s, then deletes if the files are on the volume;
                     hard deadline +${TERM_H}h)
  trainer gets --no-self-terminate ONLY if that watcher is confirmed running;
  otherwise the fallback is ON_UNARMED=$ON_UNARMED
  NOTE: the register is never trained in an A3 run; this script has no
        flag that could enable it.
DRYEOF""")

# ---- 5. the agent replaces the bare deadline reaper ---------------------
sub_once(
    """  # deadline reaper on the pod: covers a HUNG run, which nothing else did
  $SSH "nohup sh -c 'sleep $((TERM_H * 3600)); \\
        runpodctl remove pod \\$(cat /root/mvm/pod_id)' \\
        > $RUN_DIR/reaper.log 2>&1 < /dev/null &" >/dev/null 2>&1 \\
    && echo "  deadline reaper armed (+${TERM_H}h, laptop-independent)\"""",
    """  # ---- 2026-09-21: the machine's own shutdown watcher -------------------
  # This REPLACES the bare `sleep 24h; runpodctl remove pod` line the
  # registered launcher runs. That line covered one case, a run that HANGS.
  # src/reap_agent.sh covers that and the case the 2026-09-19 run hit: it
  # holds the machine open once training finishes, waiting for the laptop to
  # write a receipt saying it has the files and has checked them, and deletes
  # the moment that receipt lands. If the laptop never answers it deletes
  # anyway after GRACE_S, but only when the model file is on the network
  # volume, which outlives the machine. Same hard deadline as before.
  AGENT_DEADLINE=$(( $(date +%s) + TERM_H * 3600 ))
  $SSH "umask 077; printf '%s\\n' \\
        'RUN_DIR=\\"$RUN_DIR\\"' 'OUT=\\"$OUT\\"' \\
        'POD_ID_FILE=\\"/root/mvm/pod_id\\"' \\
        'DEADLINE_EPOCH=$AGENT_DEADLINE' 'GRACE_S=$GRACE_S' \\
        'AGENT_POLL_S=$AGENT_POLL_S' > /root/mvm/reap.env" >/dev/null 2>&1
  $SSH "cd /root/mvm/src && nohup sh reap_agent.sh /root/mvm/reap.env \\
        >> $RUN_DIR/reaper.log 2>&1 < /dev/null &" >/dev/null 2>&1
  sleep 5
  # [r]eap guard, same trap as the training aliveness check: without the
  # bracket, pgrep matches the checking shell itself and reports a false yes.
  if $SSH "pgrep -f '[r]eap_agent.sh' >/dev/null && echo AGENT_UP" 2>/dev/null \\
       | grep -q AGENT_UP; then
    REAP_ARMED=1
    echo "  shutdown watcher RUNNING on the machine (waits ${GRACE_S}s for the"
    echo "  laptop's receipt; hard deadline +${TERM_H}h, laptop-independent)"
  else
    echo "  SHUTDOWN WATCHER DID NOT START — check $RUN_DIR/reaper.log on the"
    echo "  machine. Falling back per ON_UNARMED below."
  fi""")

# ---- 6. who deletes the machine -----------------------------------------
sub_once(
    '''echo "starting detached training run (log + checkpoints in $RUN_DIR)"''',
    '''# ---- 2026-09-21: who deletes the machine, and when -----------------------
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

echo "starting detached training run (log + checkpoints in $RUN_DIR)"''')

# ---- 7. pass the switch -------------------------------------------------
sub_once(
    """$SSH "cd /root/mvm/src && rm -f $RUN_DIR/$OUT.DONE && nohup $TRAIN_CMD \\
  $RESUME_FLAG --out $RUN_DIR/$OUT.pt \\""",
    """$SSH "cd /root/mvm/src && rm -f $RUN_DIR/$OUT.DONE $RUN_DIR/$OUT.FETCHED \\
  && nohup $TRAIN_CMD $SELFTERM_FLAG \\
  $RESUME_FLAG --out $RUN_DIR/$OUT.pt \\""")

# ---- 8. the watchdog's environment file ---------------------------------
sub_once(
    """DEADLINE_EPOCH=$DEADLINE_EPOCH
ENVEOF""",
    """DEADLINE_EPOCH=$DEADLINE_EPOCH
NETVOL="$NETVOL"
GRACE_S=$GRACE_S
ENVEOF""")

# ---- 9. the closing message --------------------------------------------
sub_once(
    '''echo "watchdog spawned (pid $WPID) — BACKSTOP. The pod reaps itself on completion and at its deadline (credential installed above); this watchdog covers the case where that fails."''',
    '''echo "watchdog spawned (pid $WPID). It takes the LAST copy of the files, checks"
echo "it against the machine, writes the receipt that releases the machine, and"
echo "deletes the machine itself if nothing on it does."''')

sub_once(
    """  watchdog:  tail -f '$DEST/watchdog.log'   (fetches continuously; on DONE or
             +${WATCH_H}h it fetches everything and DELETES the pod)""",
    """  watchdog:  tail -f '$DEST/watchdog.log'   (fetches continuously; on the
             finished-marker or +${WATCH_H}h it fetches everything, checks it,
             releases the machine and DELETES the pod)
  machine's own watcher:  $SSH_CMD 'tail -f $RUN_DIR/reaper.log'
  if anything goes wrong, look for '$DEST/NEEDS-RECOVERY.txt' — the watchdog
  writes it, with the volume id and the exact recovery steps, whenever the
  files did not all make it home.""")

DST.write_text(text)
print(f"wrote {DST} ({len(text.splitlines())} lines)")
