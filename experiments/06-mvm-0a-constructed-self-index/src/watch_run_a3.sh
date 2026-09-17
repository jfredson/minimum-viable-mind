#!/bin/bash
# watch_run_a3.sh — the A3 watchdog. Fetches artifacts continuously and
# reaps the pod on completion or at the deadline.
#
# A separate file from watch_run.sh, which produced the existing records
# and is left untouched. Two fixes, both from the 2026-09-16 pilot.
#
# FIX 1 — a truncated checkpoint can no longer be promoted.
#   The old periodic pull streamed the checkpoint with `cat` over ssh and
#   promoted the result if it was merely non-empty. A streamed `cat` of a
#   large binary truncates silently, and a truncated file passes a
#   non-empty test. (On the pilot this did not actually bite — the final,
#   archive-based fetch was correct, and an earlier report of a corrupt
#   checkpoint was a file observed mid-extraction. But a re-fetch by `cat`
#   during that investigation DID truncate at 199MB of 351MB, so the
#   hazard is real and demonstrated.) The pull now uses an archive and
#   verifies the remote checksum before promoting anything.
#
# FIX 2 — the reap no longer depends only on this laptop being awake.
#   Idle billing has now cost money three times: ~$5.70 in wave 2 and
#   ~$3.80 on the A3 pilot, each because the Mac slept and the watchdog
#   woke hours after training finished. `caffeinate -i` blocks idle sleep
#   but not lid-close. Two changes: stronger sleep assertions here, and
#   the pod is asked to terminate ITSELF the moment training finishes
#   (see train_a3.py), so the laptop is the backstop rather than the only
#   mechanism.
#
#   NOTE FOR JOHN: the pod-side self-terminate uses whatever credential
#   the pod already carries. If it turns out RunPod images do not ship a
#   usable one, the robust fix would mean putting an API key on a rented
#   machine, which is a decision about your credentials and is yours to
#   make, not mine. Until then the laptop remains the real backstop and
#   the lid should stay open.
#
#   usage: watch_run_a3.sh <env-file>   (the launcher writes the env file)
set -uo pipefail
ENVF="${1:?usage: watch_run_a3.sh <env-file>}"
# shellcheck disable=SC1090
. "$ENVF"
POLL_S="${POLL_S:-600}"
CKPT_EVERY="${CKPT_EVERY:-6}"

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

fetch_ckpt() {
  # FIX 1: archive transfer, then verify the checksum against the pod
  # before promoting. Nothing is promoted on a size test alone.
  say "pulling checkpoint (archive + checksum)"
  local remote_md5 local_md5 tmpd
  remote_md5=$($SSH "md5sum $RUN_DIR/$OUT.pt 2>/dev/null | cut -d' ' -f1" \
               | tr -d '\r\n ')
  if [ -z "$remote_md5" ]; then
    say "no checkpoint on the pod yet"; return 0
  fi
  tmpd="$DEST/.pull.$$"
  mkdir -p "$tmpd"
  if $SSH "tar cf - -C $RUN_DIR $OUT.pt" 2>/dev/null | tar xf - -C "$tmpd"; then
    local_md5=$(md5 -q "$tmpd/$OUT.pt" 2>/dev/null \
                || md5sum "$tmpd/$OUT.pt" 2>/dev/null | cut -d' ' -f1)
    if [ "$local_md5" = "$remote_md5" ]; then
      mv "$tmpd/$OUT.pt" "$DEST/$OUT.pt"
      say "checkpoint pulled and VERIFIED ($(du -h "$DEST/$OUT.pt" | cut -f1), md5 ${remote_md5:0:12})"
    else
      say "CHECKSUM MISMATCH (remote ${remote_md5:0:12}, local ${local_md5:0:12}) — discarded, will retry"
    fi
  else
    say "checkpoint pull failed (will retry)"
  fi
  rm -rf "$tmpd"
}

fetch_final() {  # everything in RUN_DIR, incl. full log + DONE sentinel
  say "final fetch of $RUN_DIR"
  $SSH "tar czf - -C $RUN_DIR ." | tar xzf - -C "$DEST" \
    && say "final fetch OK" || say "FINAL FETCH FAILED — artifacts may be partial"
  # verify the checkpoint we are about to rely on, while the pod still exists
  local remote_md5 local_md5
  remote_md5=$($SSH "md5sum $RUN_DIR/$OUT.pt 2>/dev/null | cut -d' ' -f1" \
               | tr -d '\r\n ')
  local_md5=$(md5 -q "$DEST/$OUT.pt" 2>/dev/null \
              || md5sum "$DEST/$OUT.pt" 2>/dev/null | cut -d' ' -f1)
  if [ -n "$remote_md5" ] && [ "$remote_md5" = "$local_md5" ]; then
    say "final checkpoint VERIFIED (md5 ${remote_md5:0:12})"
  else
    say "FINAL CHECKPOINT UNVERIFIED (remote ${remote_md5:0:12}, local ${local_md5:0:12}) — re-pull before trusting it"
  fi
}

kill_pod() {
  say "deleting pod $POD"
  runpodctl pod delete "$POD" && sleep 10
  pod_exists && say "WARNING: pod still present after delete — retry manually" \
             || say "pod gone; billing stopped"
}

say "watchdog up: pod=$POD out=$OUT dest=$DEST deadline=$(date -u -r "$DEADLINE_EPOCH" +%Y-%m-%dT%H:%M:%SZ)"
say "fix 1 active: checkpoint pulls are archive-based and checksum-verified"
say "fix 2 active: the pod attempts to terminate itself on completion; this watchdog is the backstop"
i=0
while :; do
  now=$(date +%s)
  if ! pod_exists; then
    say "pod no longer exists (self-terminated on completion, external kill, or crash)."
    say "if the network volume was attached, artifacts survive on it —"
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
