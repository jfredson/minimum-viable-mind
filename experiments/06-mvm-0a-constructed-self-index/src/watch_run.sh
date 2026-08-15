#!/bin/bash
# watch_run.sh — local fetch-and-kill watchdog for a launched training pod.
# Spawned automatically by launch_pilot_a1.sh (process-fix, 2026-08-15:
# every launch schedules its own fetch AND its own kill; --terminate-after
# is advisory only — it provably failed to fire on pod 6bplni87uzp3ss).
#
# This script creates nothing billable [C2-compatible]: it only polls,
# copies artifacts down, and deletes the pod. It is safe to re-run.
#
# Usage: watch_run.sh <run-env-file>
#   env file (written by the launcher) defines:
#     POD        pod id
#     SSH        full ssh command incl. -o options
#     RUN_DIR    remote dir holding checkpoint/log (network volume when attached)
#     OUT        run basename (checkpoint $OUT.pt, evals $OUT.jsonl,
#                log train_$OUT.log, sentinel $OUT.DONE)
#     DEST       local artifacts dir
#     DEADLINE_EPOCH  hard kill time (fetch, then delete pod, regardless)
#     POLL_S     poll interval seconds        (default 600)
#     CKPT_EVERY pull checkpoint every N polls (default 6 ≈ hourly)
set -uo pipefail

ENVF="${1:?usage: watch_run.sh <run-env-file>}"
# shellcheck disable=SC1090
source "$ENVF"
POLL_S="${POLL_S:-600}"
CKPT_EVERY="${CKPT_EVERY:-6}"
mkdir -p "$DEST"

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
say() { echo "[$(ts)] $*"; }

pod_exists() {
  runpodctl pod get "$POD" -o json 2>/dev/null | grep -q '"id"'
}

fetch_small() {  # evals jsonl + log tail — cheap, every poll
  $SSH "cat $RUN_DIR/$OUT.jsonl 2>/dev/null" > "$DEST/$OUT.jsonl.tmp" \
    && mv "$DEST/$OUT.jsonl.tmp" "$DEST/$OUT.jsonl"
  $SSH "tail -c 200000 $RUN_DIR/train_$OUT.log 2>/dev/null" \
    > "$DEST/train_$OUT.log.tail"
}

fetch_ckpt() {   # atomic local write; remote save is atomic too (os.replace)
  say "pulling checkpoint"
  if $SSH "cat $RUN_DIR/$OUT.pt" > "$DEST/$OUT.pt.tmp" \
      && [ -s "$DEST/$OUT.pt.tmp" ]; then
    mv "$DEST/$OUT.pt.tmp" "$DEST/$OUT.pt"
    say "checkpoint pulled ($(du -h "$DEST/$OUT.pt" | cut -f1))"
  else
    rm -f "$DEST/$OUT.pt.tmp"; say "checkpoint pull failed (will retry)"
  fi
}

fetch_final() {  # everything in RUN_DIR, incl. full log + DONE sentinel
  say "final fetch of $RUN_DIR"
  $SSH "tar czf - -C $RUN_DIR ." | tar xzf - -C "$DEST" \
    && say "final fetch OK" || say "FINAL FETCH FAILED — artifacts may be partial"
}

kill_pod() {
  say "deleting pod $POD"
  runpodctl pod delete "$POD" && sleep 10
  pod_exists && say "WARNING: pod still present after delete — retry manually" \
             || say "pod gone; billing stopped"
}

say "watchdog up: pod=$POD out=$OUT dest=$DEST deadline=$(date -u -r "$DEADLINE_EPOCH" +%Y-%m-%dT%H:%M:%SZ)"
i=0
while :; do
  now=$(date +%s)
  if ! pod_exists; then
    say "pod no longer exists (external kill or crash)."
    say "if the network volume was attached, the checkpoint survives on it —"
    say "attach it to a throwaway CPU pod to recover; nothing more to do here."
    exit 3
  fi
  if [ "$now" -ge "$DEADLINE_EPOCH" ]; then
    say "DEADLINE reached — fetch then kill (runaway backstop, owned locally)"
    fetch_final; kill_pod; exit 2
  fi
  if $SSH "test -f $RUN_DIR/$OUT.DONE" 2>/dev/null; then
    say "DONE sentinel found — training complete"
    fetch_final; kill_pod
    say "run complete; artifacts in $DEST"
    exit 0
  fi
  fetch_small || say "small fetch failed this poll (transient ssh?)"
  i=$((i + 1))
  [ $((i % CKPT_EVERY)) -eq 0 ] && fetch_ckpt
  [ -f "$DEST/train_$OUT.log.tail" ] \
    && say "poll $i: $(tail -1 "$DEST/train_$OUT.log.tail" 2>/dev/null | cut -c1-160)"
  sleep "$POLL_S"
done
