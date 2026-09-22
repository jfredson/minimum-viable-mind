#!/bin/sh
# reap_agent.sh — the rented machine's own shutdown watcher.
#
# Runs ON the rented machine, installed and started by the launcher. It
# decides when the machine may delete itself. Written for plain POSIX sh
# because it runs on whatever shell the vendor image ships.
#
# WHY THIS FILE EXISTS
# -------------------
# Two shutdown mechanisms were built a month apart for the same problem and
# ended up cancelling each other out, as the compute ledger's 2026-09-20 row
# records.
#
#   * The trainer (src/train_a3.py, function self_terminate) asks the
#     machine to delete itself within a fraction of a second of writing its
#     finished-marker file. It was added after waiting on a sleeping laptop
#     cost about $10.30 in idle billing across four occasions, and it works:
#     the 2026-09-19 run was the first in this programme's history with none.
#
#   * The laptop watcher (src/watch_run_a3.sh) wakes about every ten minutes
#     and, on seeing the finished-marker, does the LAST copy of the files,
#     checks that copy against the machine, and only then deletes it. It was
#     added because a run whose files never come down is a run that cost
#     money and produced nothing — which is how $97.04 was lost on
#     2026-08-12.
#
# On a run that finishes normally the laptop has to notice a marker inside a
# window about a second wide, once, with no second attempt. It cannot, so
# the last copy never happens and a human has to rent another machine to
# read the files off the network volume.
#
# WHAT THIS SCRIPT DOES INSTEAD
# -----------------------------
# It moves the shutdown decision off the trainer and onto a waiting loop, so
# the two mechanisms cooperate:
#
#   1. Training finishes and writes its finished-marker. Nothing is deleted.
#   2. The laptop notices (it now checks every minute), copies everything
#      down, checks the copy against the machine, and writes a RECEIPT file
#      back onto the machine.
#   3. This script sees the receipt and deletes the machine at once.
#   4. If the receipt never comes — laptop asleep, lid shut, network gone —
#      this script deletes the machine anyway once a bounded wait runs out,
#      but ONLY if the files are sitting on the network volume, which
#      outlives the machine. That keeps the idle bill bounded at the wait
#      rather than at however long the laptop sleeps.
#   5. If there is no network volume, deleting would destroy the only copy,
#      so the wait running out is NOT enough: it keeps waiting for the
#      receipt until the hard deadline.
#   6. At the hard deadline (+24h by default) it deletes regardless. This is
#      the backstop for a run that HANGS and never writes a finished-marker,
#      which nothing else covers, and it replaces the bare
#      `sleep 24h; runpodctl remove pod` line the launchers run today.
#
# The safety gate on the grace path is the same one the trainer already
# carries, and for the same reason: never delete a machine whose own disk
# holds the only copy of the work. The gate is deliberately NOT applied on
# the receipt path — a receipt means the laptop already has the files and
# has checked them, which is a stronger guarantee than the volume.
#
# STANDING FACT this depends on (measured 2026-09-16, paid test $0.29): a
# rented machine carries NO usable credential and does NOT know its own
# identifier — no RUNPOD_POD_ID, and runpodctl installed but unconfigured.
# The launcher supplies both: a dedicated reaper key (John's ruling of
# 2026-09-16: that key only, no fallback to the account key) and the
# machine's own id written to /root/mvm/pod_id. Without those this script
# cannot delete anything, says so, and the laptop watcher is the only reap.
#
# NOTE ON THE COMMAND FORM: verb-first (`runpodctl remove pod ID`). The
# vendor image ships runpodctl 1.14.15, which has no `pod` subcommand at
# all; the laptop's copy is 2.6.1 and takes the noun-first form. Measured on
# a live machine 2026-09-17. Both forms are tried here, verb-first first.
#
# usage: reap_agent.sh <env-file>
#        reap_agent.sh --self-test     (no vendor contact, deletes nothing)

set -u

if [ "${1:-}" = "--self-test" ]; then
    SELFTEST=1
else
    SELFTEST=0
    ENVF="${1:?usage: reap_agent.sh <env-file>}"
    # shellcheck disable=SC1090
    . "$ENVF"
fi

RUN_DIR="${RUN_DIR:-/workspace/mvm-out}"
OUT="${OUT:-run}"
POD_ID_FILE="${POD_ID_FILE:-/root/mvm/pod_id}"
DEADLINE_EPOCH="${DEADLINE_EPOCH:-0}"
# How long the machine waits for the laptop's receipt before giving up and
# deleting itself. A SPENDING choice, not a technical one: at $0.99/hour the
# default costs at most about $0.50 of idle billing on a run whose laptop
# never answers. Compare the 3.9h and 5.8h the old failure actually billed.
GRACE_S="${GRACE_S:-1800}"
AGENT_POLL_S="${AGENT_POLL_S:-15}"
# The prefix that means "this file outlives the machine". Anything under the
# mounted network volume qualifies; the container's own disk does not.
VOLUME_PREFIX="${VOLUME_PREFIX:-/workspace/}"
LOG="${REAP_LOG:-$RUN_DIR/reaper.log}"

DONE_FILE="$RUN_DIR/$OUT.DONE"
RECEIPT_FILE="$RUN_DIR/$OUT.FETCHED"
CKPT_FILE="$RUN_DIR/$OUT.pt"

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
say() { echo "[$(ts)] reap-agent: $*"; }

# Absolute, symlink-resolved path, without depending on readlink -f (absent
# from some of the shells and userlands this has to run on).
# Runs in a subshell so the cd cannot move the caller.
abspath() {
    ( cd -- "$(dirname -- "$1")" 2>/dev/null \
        && printf '%s/%s\n' "$(pwd -P)" "$(basename -- "$1")" ) \
      || printf '%s\n' "$1"
}

# Is the work safe from this machine's deletion? True only when the model
# file exists AND sits on the mounted network volume.
work_is_durable() {
    [ -f "$CKPT_FILE" ] || return 1
    case "$(abspath "$CKPT_FILE")" in
        "$VOLUME_PREFIX"*) return 0 ;;
        *) return 1 ;;
    esac
}

pod_id() {
    [ -f "$POD_ID_FILE" ] || return 1
    tr -d ' \t\r\n' < "$POD_ID_FILE"
}

delete_machine() {
    _why="$1"
    _pod=$(pod_id) || _pod=""
    if [ -z "$_pod" ]; then
        say "NOT deleting: no machine id at $POD_ID_FILE, so this machine"
        say "cannot name itself to the vendor. The laptop watcher is the reap."
        return 1
    fi
    say "deleting this machine ($_pod) — $_why"
    _try=0
    while [ "$_try" -lt 3 ]; do
        _try=$((_try + 1))
        # verb-first first: the vendor image's older CLI only understands it
        if runpodctl remove pod "$_pod" >/dev/null 2>&1; then
            say "delete accepted (remove pod, attempt $_try)"
            return 0
        fi
        if runpodctl pod delete "$_pod" >/dev/null 2>&1; then
            say "delete accepted (pod delete, attempt $_try)"
            return 0
        fi
        say "delete attempt $_try failed; retrying in 10s"
        sleep 10
    done
    say "EVERY DELETE ROUTE FAILED. This machine is still billing. The laptop"
    say "watcher and the vendor's own terminate-after are what is left."
    return 1
}

self_test() {
    _tmp=$(mktemp -d 2>/dev/null || echo /tmp/reapselftest.$$)
    mkdir -p "$_tmp"
    # resolve symlinks in the temp path itself (on macOS /tmp and /var are
    # symlinks), so the prefix we compare against is the resolved one
    _tmp=$(cd "$_tmp" && pwd -P)
    mkdir -p "$_tmp/workspace-like" "$_tmp/disk-like"
    # durability gate: a file under the volume prefix counts, one outside
    # does not. Exercised with a temporary prefix so the test needs no
    # /workspace and touches nothing real.
    VOLUME_PREFIX="$_tmp/workspace-like/"
    CKPT_FILE="$_tmp/workspace-like/x.pt"
    : > "$CKPT_FILE"
    work_is_durable || { echo "reap_agent self-test FAILED: volume file not judged durable"; exit 1; }
    CKPT_FILE="$_tmp/disk-like/x.pt"
    : > "$CKPT_FILE"
    work_is_durable && { echo "reap_agent self-test FAILED: container-disk file judged durable"; exit 1; }
    CKPT_FILE="$_tmp/workspace-like/missing.pt"
    work_is_durable && { echo "reap_agent self-test FAILED: missing file judged durable"; exit 1; }
    # a machine that cannot name itself must refuse to delete
    POD_ID_FILE="$_tmp/no-such-id"
    delete_machine "self-test" && { echo "reap_agent self-test FAILED: deleted without a machine id"; exit 1; }
    rm -rf "$_tmp"
    echo "reap_agent self-test OK"
    exit 0
}

[ "$SELFTEST" = "1" ] && self_test

mkdir -p "$(dirname -- "$LOG")" 2>/dev/null || true
exec >>"$LOG" 2>&1

say "up. run dir $RUN_DIR, run $OUT"
say "waits for the laptop's receipt at $RECEIPT_FILE once $DONE_FILE appears"
say "grace after finishing: ${GRACE_S}s; hard deadline epoch: $DEADLINE_EPOCH"
if pod_id >/dev/null 2>&1; then
    say "machine id present; deletion is armed"
else
    say "WARNING: no machine id at $POD_ID_FILE — this agent CANNOT delete"
    say "anything. Tell the operator: the laptop watcher is the only reap and"
    say "the lid must stay open."
fi

DONE_SEEN_AT=""
while :; do
    NOW=$(date +%s)

    if [ "$DEADLINE_EPOCH" -gt 0 ] && [ "$NOW" -ge "$DEADLINE_EPOCH" ]; then
        say "HARD DEADLINE reached. This is the backstop for a run that hung"
        say "and never finished; nothing else covers that case."
        delete_machine "hard deadline"
        exit 2
    fi

    if [ -f "$DONE_FILE" ]; then
        if [ -z "$DONE_SEEN_AT" ]; then
            DONE_SEEN_AT="$NOW"
            say "training finished. Holding this machine open so the laptop can"
            say "take the last copy and check it. Waiting up to ${GRACE_S}s for"
            say "the receipt."
            if work_is_durable; then
                say "the model file is on the network volume, so it outlives"
                say "this machine if the receipt never comes."
            else
                say "the model file is NOT on the network volume: this machine's"
                say "own disk holds the only copy, so the grace running out will"
                say "NOT be enough to delete. Waiting for the receipt until the"
                say "hard deadline."
            fi
        fi

        if [ -f "$RECEIPT_FILE" ]; then
            say "receipt found: the laptop has the files and has checked them."
            delete_machine "laptop receipt"
            exit 0
        fi

        if [ $((NOW - DONE_SEEN_AT)) -ge "$GRACE_S" ]; then
            if work_is_durable; then
                say "grace ran out with no receipt. The laptop did not answer —"
                say "asleep, lid shut, or the link is down. Deleting anyway to"
                say "stop the billing; the files are on the network volume."
                say "THE LOCAL COPY IS SHORT OF THE FINAL STEP and needs"
                say "recovering from the volume."
                delete_machine "grace ran out, work is on the volume"
                exit 0
            else
                say "grace ran out with no receipt, but the only copy is on this"
                say "machine's disk. NOT deleting. Waiting for the receipt or"
                say "the hard deadline."
                DONE_SEEN_AT="$NOW"   # log this again one grace period later
            fi
        fi
    fi

    sleep "$AGENT_POLL_S"
done
