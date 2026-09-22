#!/bin/bash
# reap_handshake_selftest.sh — proves the shutdown order without renting
# anything, contacting any vendor, or spending a cent.
#
# WHAT IS BEING PROVED
# --------------------
# One rule, from ../reap-shutdown-order-method.md §3:
#
#   The rented machine may not be deleted until either (a) the laptop has
#   the finished model file locally and has checked it against the copy on
#   the machine, or (b) a bounded wait has passed AND the file is known to
#   be on the network volume, which outlives the machine.
#
# The test stands up a fake rented machine as a local directory, a fake
# `runpodctl` that records every deletion, and a fake remote-shell command
# that runs against that directory. It then runs the REAL watch_run_a3.sh
# and the REAL reap_agent.sh against them, with the waiting times squeezed
# from minutes to seconds.
#
# The decisive trick: the fake `runpodctl`, at the moment it is asked to
# delete, records whether the laptop's receipt existed AND whether the
# laptop's copy of the model file was byte-identical to the machine's. So
# the rule above is checked at exactly the instant that matters, rather
# than inferred from timestamps afterwards.
#
# usage: bash reap_handshake_selftest.sh          (runs every case)
#        bash reap_handshake_selftest.sh 3        (runs case 3 only)
#
# Case 0 is the negative control: it reproduces the OLD order and expects the
# rule to be broken. It is what shows the other cases are measuring something.
set -uo pipefail

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
WATCH="$SRC_DIR/watch_run_a3.sh"
AGENT="$SRC_DIR/reap_agent.sh"
ONLY="${1:-}"
PASS=0
FAIL=0

red() { printf '\033[31m%s\033[0m\n' "$*"; }
grn() { printf '\033[32m%s\033[0m\n' "$*"; }

ok()   { PASS=$((PASS + 1)); grn "    pass: $*"; }
bad()  { FAIL=$((FAIL + 1)); red "    FAIL: $*"; }
check() { if [ "$1" = "$2" ]; then ok "$3"; else bad "$3 (wanted '$2', got '$1')"; fi; }

# --------------------------------------------------------------- sandbox
# Builds a fake machine and the two fake vendor tools. Nothing here reaches
# the network; `runpodctl` and `ssh` are shell scripts on a private PATH.
make_sandbox() {   # $1 = 1 if the model file goes on the "network volume"
  local on_volume="$1"
  T=$(mktemp -d)
  T=$(cd "$T" && pwd -P)
  MACHINE="$T/machine"
  if [ "$on_volume" = "1" ]; then
    RUN_DIR="$MACHINE/workspace/mvm-out"
  else
    RUN_DIR="$MACHINE/root/mvm-out"       # the machine's own disk
  fi
  DEST="$T/laptop"
  BIN="$T/bin"
  SHIM="$T/shim"
  STATE="$T/state"            # alive | gone
  DELLOG="$T/deletions"       # one line per delete, with what was true then
  APIFAIL="$T/apifail"        # countdown of pretend API errors
  mkdir -p "$RUN_DIR" "$DEST" "$BIN" "$SHIM" "$MACHINE"
  WATCH_PID=""; AGENT_PID=""
  echo alive > "$STATE"
  : > "$DELLOG"
  echo 0 > "$APIFAIL"
  echo "fakepod000001" > "$MACHINE/pod_id"

  # a model file big enough that copying it is a real copy
  dd if=/dev/urandom of="$RUN_DIR/testrun.pt" bs=1024 count=400 2>/dev/null
  printf '{"step": 51500, "tokens": 547136000}\n' > "$RUN_DIR/testrun.jsonl"
  echo "training log line" > "$RUN_DIR/train_testrun.log"

  cat > "$BIN/runpodctl" <<FAKECTL
#!/bin/bash
# fake vendor tool. Never contacts anything.
STATE="$STATE"; DELLOG="$DELLOG"; APIFAIL="$APIFAIL"
POD_CKPT="$RUN_DIR/testrun.pt"; DEST_CKPT="$DEST/testrun.pt"
RECEIPT="$RUN_DIR/testrun.FETCHED"
case "\$1 \$2" in
  "pod get")
    n=\$(cat "\$APIFAIL" 2>/dev/null || echo 0)
    if [ "\$n" -gt 0 ]; then echo \$((n - 1)) > "\$APIFAIL"; exit 1; fi
    [ "\$(cat "\$STATE")" = "alive" ] || exit 1
    echo "{\\"id\\": \\"\$3\\", \\"desiredStatus\\": \\"RUNNING\\"}"
    ;;
  "pod delete"|"remove pod")
    [ "\$(cat "\$STATE")" = "alive" ] || { echo "no such pod" >&2; exit 1; }
    # THE ASSERTION POINT: what was true at the instant of deletion?
    if [ -f "\$RECEIPT" ]; then r=yes; else r=no; fi
    c=no
    if [ -f "\$DEST_CKPT" ] && [ -f "\$POD_CKPT" ]; then
      a=\$(md5 -q "\$DEST_CKPT" 2>/dev/null || md5sum "\$DEST_CKPT" | cut -d' ' -f1)
      b=\$(md5 -q "\$POD_CKPT"  2>/dev/null || md5sum "\$POD_CKPT"  | cut -d' ' -f1)
      [ "\$a" = "\$b" ] && c=yes
    fi
    echo "\$(date +%s) by=\${REAP_CALLER:-unknown} receipt=\$r local_copy_matches=\$c" >> "\$DELLOG"
    echo gone > "\$STATE"
    echo "pod removed"
    ;;
  *) echo "fake runpodctl: unhandled: \$*" >&2; exit 1 ;;
esac
FAKECTL

  # macOS has md5, Linux has md5sum; the scripts call md5sum "on the
  # machine", so supply it there.
  cat > "$SHIM/md5sum" <<'FAKEMD5'
#!/bin/bash
for f in "$@"; do printf '%s  %s\n' "$(md5 -q "$f")" "$f"; done
FAKEMD5

  # the fake remote shell: refuses once the machine is "gone", exactly as a
  # real ssh to a deleted host does.
  cat > "$BIN/fakessh" <<FAKESSH
#!/bin/bash
[ "\$(cat "$STATE")" = "alive" ] || exit 255
export PATH="$SHIM:$BIN:\$PATH"
export REAP_CALLER=machine
exec bash -c "\$*"
FAKESSH

  chmod +x "$BIN/runpodctl" "$BIN/fakessh" "$SHIM/md5sum"

  DEADLINE=$(( $(date +%s) + 3600 ))
  cat > "$T/watch.env" <<WENV
POD="fakepod000001"
SSH="$BIN/fakessh"
RUN_DIR="$RUN_DIR"
OUT="testrun"
DEST="$DEST"
DEADLINE_EPOCH=$DEADLINE
NETVOL="fakevolume123"
POLL_S=3
PROBE_S=1
CKPT_EVERY=2
FINAL_TRIES=2
FINAL_RETRY_S=2
MISSING_CONFIRM=3
MISSING_GAP_S=1
KILL_SETTLE_S=1
WENV

  cat > "$T/agent.env" <<AENV
RUN_DIR="$RUN_DIR"
OUT="testrun"
POD_ID_FILE="$MACHINE/pod_id"
DEADLINE_EPOCH=$DEADLINE
GRACE_S=${GRACE_S_TEST:-6}
AGENT_POLL_S=1
VOLUME_PREFIX="$MACHINE/workspace/"
REAP_LOG="$T/agent.log"
AENV
}

start_watchdog() {
  ( export PATH="$BIN:$PATH"; export REAP_CALLER=laptop;
    bash "$WATCH" "$T/watch.env" > "$T/watchdog.log" 2>&1;
    echo $? > "$T/watchdog.exit" ) &
  WATCH_PID=$!
  # disowned so the shell does not print a job notice when we stop it;
  # completion is read from the exit file, not from wait.
  disown "$WATCH_PID" 2>/dev/null || true
}

start_agent() {
  ( export PATH="$BIN:$PATH"; export REAP_CALLER=machine;
    sh "$AGENT" "$T/agent.env" >/dev/null 2>&1 ) &
  AGENT_PID=$!
  disown "$AGENT_PID" 2>/dev/null || true
}

# NOTE: never `kill 0` here. An unset pid defaulting to 0 signals the whole
# process group, which kills this test script itself — caught while writing
# case 2, where only one of the two is running.
stop_all() {
  local p
  for p in "${WATCH_PID:-}" "${AGENT_PID:-}"; do
    [ -n "$p" ] && kill "$p" 2>/dev/null
  done
  # the background subshells have children of their own
  pkill -f "$T/agent.env" 2>/dev/null
  pkill -f "$T/watch.env" 2>/dev/null
  sleep 1
  WATCH_PID=""; AGENT_PID=""
}

finish_training() {   # what the trainer does at the end of a run
  printf '{"step": 55116, "tokens": 585552384}\n' > "$RUN_DIR/testrun.DONE"
  dd if=/dev/urandom of="$RUN_DIR/testrun.pt" bs=1024 count=400 2>/dev/null
  printf '{"step": 55116, "tokens": 585552384}\n' >> "$RUN_DIR/testrun.jsonl"
}

wait_for_exit() {   # $1 = seconds
  local n=0
  while [ "$n" -lt "$1" ]; do
    [ -f "$T/watchdog.exit" ] && return 0
    n=$((n + 1)); sleep 1
  done
  return 1
}

deletions() { wc -l < "$DELLOG" | tr -d ' '; }

want_case() { [ -z "$ONLY" ] || [ "$ONLY" = "$1" ]; }

# ---------------------------------------------------------------- case 0
# NEGATIVE CONTROL. A test that can only ever pass proves nothing, so this
# case reproduces the OLD arrangement and expects it to FAIL the rule.
#
# The old order is the trainer's, in train_a3.py: save the model file, write
# the finished-marker, then ask the machine to delete itself — three steps
# with nothing between them. The laptop is running and healthy; it simply
# has no opportunity. If this case ever reports the rule holding, the
# harness is not measuring what it claims to measure.
if want_case 0; then
  echo "case 0 — negative control: the OLD order, which must break the rule"
  make_sandbox 1
  start_watchdog          # laptop running, healthy, no machine-side agent
  sleep 3
  # exactly what the trainer does today, in the same order
  dd if=/dev/urandom of="$RUN_DIR/testrun.pt" bs=1024 count=400 2>/dev/null
  printf '{"step": 55116, "tokens": 585552384}\n' > "$RUN_DIR/testrun.DONE"
  REAP_CALLER=trainer "$BIN/runpodctl" remove pod fakepod000001 >/dev/null 2>&1
  wait_for_exit 60 || bad "the watchdog never finished"
  stop_all
  check "$(deletions)" "1" "the machine was deleted (by the trainer)"
  del=$(head -1 "$DELLOG")
  case "$del" in
    *by=trainer*receipt=no*local_copy_matches=no*)
      ok "the rule was BROKEN, as expected: deleted with no receipt and a stale local copy" ;;
    *)
      bad "the old order did not break the rule as expected — the harness may not be measuring it: $del" ;;
  esac
  if [ -f "$DEST/testrun.pt" ]; then
    a=$(md5 -q "$DEST/testrun.pt")
    b=$(md5 -q "$RUN_DIR/testrun.pt")
    [ "$a" != "$b" ] && ok "the laptop was left holding an out-of-date model file" \
      || bad "the laptop somehow had the final file"
  else
    ok "the laptop was left with no model file at all"
  fi
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 1
# The run finishes normally with the laptop awake. This is the case that
# broke on 2026-09-19 and the whole reason the fix exists.
if want_case 1; then
  echo "case 1 — run finishes normally, laptop awake"
  make_sandbox 1
  start_agent
  start_watchdog
  sleep 3
  finish_training
  wait_for_exit 60 || bad "the watchdog never finished"
  sleep 2
  stop_all
  check "$(cat "$T/watchdog.exit" 2>/dev/null)" "0" "the watchdog reported success"
  local_md5=$(md5 -q "$DEST/testrun.pt" 2>/dev/null)
  pod_md5=$(md5 -q "$RUN_DIR/testrun.pt" 2>/dev/null)
  check "$local_md5" "$pod_md5" "the laptop's model file matches the machine's, byte for byte"
  check "$(deletions)" "1" "the machine was deleted exactly once"
  del=$(head -1 "$DELLOG")
  case "$del" in
    *receipt=yes*) ok "the receipt existed at the moment of deletion" ;;
    *) bad "the machine was deleted with no receipt: $del" ;;
  esac
  case "$del" in
    *local_copy_matches=yes*) ok "THE RULE HELD: the files were home and checked before the machine went" ;;
    *) bad "THE RULE BROKE: deleted while the laptop's copy did not match: $del" ;;
  esac
  [ -f "$DEST/NEEDS-RECOVERY.txt" ] && bad "a recovery note was written on a clean run" \
    || ok "no recovery note on a clean run"
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 2
# The laptop never answers — asleep, lid shut, network gone. The machine
# must stop billing on its own, and within the bounded wait, not hours later.
if want_case 2; then
  echo "case 2 — laptop never answers; the bounded wait must end the billing"
  GRACE_S_TEST=6 make_sandbox 1
  start_agent
  sleep 2
  t0=$(date +%s)
  finish_training
  n=0
  while [ "$(deletions)" = "0" ] && [ "$n" -lt 40 ]; do n=$((n + 1)); sleep 1; done
  t1=$(date +%s)
  stop_all
  check "$(deletions)" "1" "the machine deleted itself with no laptop present"
  waited=$((t1 - t0))
  if [ "$waited" -ge 5 ] && [ "$waited" -le 20 ]; then
    ok "it waited about the grace period first (${waited}s, grace 6s)"
  else
    bad "it waited ${waited}s, which is not about the 6s grace period"
  fi
  case "$(head -1 "$DELLOG")" in
    *receipt=no*) ok "it recorded that no receipt had arrived" ;;
    *) bad "unexpected deletion record: $(head -1 "$DELLOG")" ;;
  esac
  grep -q "grace ran out" "$T/agent.log" \
    && ok "the machine's log says why it went, and that the copy needs recovering" \
    || bad "the machine's log does not explain the deletion"
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 3
# No network volume: the machine's own disk holds the only copy. Running out
# of patience must NOT be enough to delete. This is the 2026-08-12 failure
# mode and the reason the trainer's own gate exists.
if want_case 3; then
  echo "case 3 — files are only on the machine's disk; the wait must NOT be enough"
  GRACE_S_TEST=3 make_sandbox 0
  start_agent
  sleep 2
  finish_training
  sleep 10
  stop_all
  check "$(deletions)" "0" "the machine refused to delete itself"
  grep -q "NOT deleting" "$T/agent.log" \
    && ok "it says why: deleting would destroy the only copy" \
    || bad "the machine's log does not explain the refusal"
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 4
# The final copy does not check out. The old code deleted the machine anyway,
# straight after printing FINAL CHECKPOINT UNVERIFIED.
if want_case 4; then
  echo "case 4 — the final copy does not check out; nothing may be deleted"
  make_sandbox 1
  # make the machine report a checksum that will never match
  cat > "$SHIM/md5sum" <<'BADMD5'
#!/bin/bash
for f in "$@"; do printf '%s  %s\n' "00000000000000000000000000000000" "$f"; done
BADMD5
  chmod +x "$SHIM/md5sum"
  start_watchdog
  sleep 2
  finish_training
  wait_for_exit 60 || bad "the watchdog never finished"
  stop_all
  check "$(cat "$T/watchdog.exit" 2>/dev/null)" "4" "the watchdog reported an unchecked copy"
  check "$(deletions)" "0" "the machine was left running rather than deleted"
  [ -f "$RUN_DIR/testrun.FETCHED" ] && bad "a receipt was written on an unchecked copy" \
    || ok "no receipt was written, so the machine stays up"
  [ -f "$DEST/NEEDS-RECOVERY.txt" ] && ok "a recovery note was written" \
    || bad "no recovery note was written"
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 5
# The machine vanishes mid-run. This is what the laptop met on 2026-09-19,
# and it used to end with three lines of log and nothing else.
if want_case 5; then
  echo "case 5 — the machine vanishes mid-run; the laptop must leave instructions"
  make_sandbox 1
  start_watchdog
  sleep 4
  echo gone > "$STATE"
  wait_for_exit 60 || bad "the watchdog never finished"
  stop_all
  check "$(cat "$T/watchdog.exit" 2>/dev/null)" "3" "the watchdog reported a vanished machine"
  if [ -f "$DEST/NEEDS-RECOVERY.txt" ]; then
    ok "a recovery note was written"
    grep -q "fakevolume123" "$DEST/NEEDS-RECOVERY.txt" \
      && ok "the note names the network volume to recover from" \
      || bad "the note does not name the volume"
    grep -q "John's go" "$DEST/NEEDS-RECOVERY.txt" \
      && ok "the note says renting a machine needs John's go" \
      || bad "the note does not say the recovery is billable"
  else
    bad "no recovery note was written"
  fi
  rm -rf "$T"
fi

# ---------------------------------------------------------------- case 6
# One failed API call must not convince the laptop the machine is gone.
# Believing it would abandon a LIVE, billing machine.
if want_case 6; then
  echo "case 6 — a single failed API call must not look like a deleted machine"
  make_sandbox 1
  echo 1 > "$APIFAIL"          # exactly one "pod get" fails
  start_agent
  start_watchdog
  sleep 8
  if [ -f "$T/watchdog.exit" ]; then
    bad "the watchdog gave up on one failed API call (exit $(cat "$T/watchdog.exit"))"
  else
    ok "the watchdog kept going through the failed API call"
  fi
  [ -f "$DEST/NEEDS-RECOVERY.txt" ] && bad "it wrote a recovery note for a live machine" \
    || ok "no recovery note for a live machine"
  finish_training
  wait_for_exit 60 || bad "the watchdog never finished after the run completed"
  sleep 2
  stop_all
  check "$(cat "$T/watchdog.exit" 2>/dev/null)" "0" "and it still completed the run normally afterwards"
  rm -rf "$T"
fi

echo
echo "checks passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ] || exit 1
echo "reap handshake self-test OK — no machine was rented and no vendor contacted"
