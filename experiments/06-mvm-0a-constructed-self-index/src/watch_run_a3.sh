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
#   the pod was to be asked to terminate ITSELF the moment training
#   finishes (see train_a3.py). MEASURED 2026-09-16: that cannot work —
#   a pod carries no RUNPOD_POD_ID and runpodctl has no credential, so
#   this watchdog remains the ONLY reap and the lid must stay open.
#
#   NOTE FOR JOHN: the pod-side self-terminate uses whatever credential
#   the pod already carries. If it turns out RunPod images do not ship a
#   usable one, the robust fix would mean putting an API key on a rented
#   machine, which is a decision about your credentials and is yours to
#   make, not mine. Until then the laptop remains the real backstop and
#   the lid should stay open.
#
# FIXES 3 TO 6 — added 2026-09-21, after the 2026-09-19 control pilot.
#   The credential WAS supplied, so the machine really can delete itself,
#   and on 2026-09-19 it did — about a second after writing its
#   finished-marker, which is long before this watcher's next ten-minute
#   wake-up. This watcher then found the machine already gone, took its
#   give-up branch, and the last copy of the model file never happened.
#   The full-budget file survived only because it was on the network
#   volume, and it took a separately authorised rented machine to read it
#   back. Full diagnosis and the options weighed:
#   ../reap-shutdown-order-method.md.
#
#   The shutdown decision now belongs to src/reap_agent.sh, which runs ON
#   the machine and waits for this watcher to say it has the files. What
#   changes here:
#
#   FIX 3 — write the RECEIPT. After the final copy is checked against the
#     machine, write a receipt file back onto it. The machine's own agent
#     is waiting for exactly that and deletes itself the moment it lands.
#     This watcher then deletes the machine as well, so it remains a real
#     reaper when the agent was never armed.
#
#   FIX 4 — never delete on an unchecked copy. The old code ran
#     `fetch_final; kill_pod` in sequence and deleted the machine even
#     when it had just printed FINAL CHECKPOINT UNVERIFIED. The final copy
#     now retries, and on a completion the machine is deleted only once
#     the copy checks out. Refusing to delete is affordable ONLY because
#     the machine's own agent enforces a deadline; without that this would
#     be an open-ended idle bill.
#
#   FIX 5 — the give-up branch stops giving up quietly. A single failed
#     API call used to be indistinguishable from a deleted machine, which
#     would abandon a LIVE, billing machine; "gone" is now confirmed over
#     several checks. And when the machine really is gone with the files
#     not yet home, a NEEDS-RECOVERY.txt is written beside the artifacts
#     naming the volume, the run, the last step held locally and the exact
#     command, instead of three lines at the end of a log.
#
#   FIX 6 — split the cheap check from the expensive copy. Asking "is
#     there a finished-marker yet" costs one tiny remote command, so it
#     now happens every minute; pulling files stays on the old ten-minute
#     and hourly cadences. This is what keeps the machine's waiting time,
#     and so the worst-case idle bill, short.
#
#   usage: watch_run_a3.sh <env-file>   (the launcher writes the env file)
set -uo pipefail
ENVF="${1:?usage: watch_run_a3.sh <env-file>}"
# shellcheck disable=SC1090
. "$ENVF"
POLL_S="${POLL_S:-600}"          # expensive: small fetches, existence check
PROBE_S="${PROBE_S:-60}"         # cheap: has the run finished yet?
CKPT_EVERY="${CKPT_EVERY:-6}"    # checkpoint pull every N expensive polls
FINAL_TRIES="${FINAL_TRIES:-3}"  # attempts at a checked final copy
MISSING_CONFIRM="${MISSING_CONFIRM:-3}"  # consecutive no-answers = really gone
MISSING_GAP_S="${MISSING_GAP_S:-15}"     # seconds between those checks
FINAL_RETRY_S="${FINAL_RETRY_S:-60}"     # wait between final-copy attempts
KILL_SETTLE_S="${KILL_SETTLE_S:-10}"     # wait before confirming the delete
# The last four exist so the self-test can run the whole sequence in
# seconds without contacting a vendor: src/reap_handshake_selftest.sh.

# The volume id, written by the newer launcher; older env files do not carry
# it, and the
# only thing it affects is how helpful the recovery note can be.
NETVOL="${NETVOL:-unknown}"

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
say() { echo "[$(ts)] $*"; }

pod_exists() {
  runpodctl pod get "$POD" -o json 2>/dev/null | grep -q '"id"'
}

# FIX 5: one failed API call is not proof the machine is gone. Believing it
# on a single miss would abandon a live, billing machine — the exact
# failure this watcher exists to prevent, in the other direction. Ask
# several times before concluding anything.
pod_gone_confirmed() {
  local n=0
  while [ "$n" -lt "$MISSING_CONFIRM" ]; do
    pod_exists && return 1
    n=$((n + 1))
    say "the machine did not answer (check $n of $MISSING_CONFIRM)"
    [ "$n" -lt "$MISSING_CONFIRM" ] && sleep "$MISSING_GAP_S"
  done
  return 0
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
  # FIX 4: this now REPORTS whether the copy checked out (0 yes, 1 no).
  # Nothing downstream may delete the machine on a 1.
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
    return 0
  fi
  say "FINAL CHECKPOINT UNVERIFIED (remote ${remote_md5:0:12}, local ${local_md5:0:12}) — re-pull before trusting it"
  return 1
}

# FIX 3: tell the machine, in writing, that the files are home and checked.
# src/reap_agent.sh is sitting in a loop waiting for exactly this file and
# deletes the machine the moment it appears. Writing it to a machine that
# has no agent is harmless, which is why this is safe to do on every run.
write_receipt() {
  if $SSH "printf '%s\n' 'fetched and checked by the laptop watcher at $(ts)' > $RUN_DIR/$OUT.FETCHED" 2>/dev/null; then
    say "receipt written on the machine — it may delete itself now"
  else
    say "could not write the receipt (machine already gone?) — deleting from here"
  fi
}

last_local_step() {
  [ -f "$DEST/$OUT.jsonl" ] || { echo "unknown"; return; }
  tail -1 "$DEST/$OUT.jsonl" 2>/dev/null \
    | sed -n 's/.*"step": *\([0-9]*\).*/\1/p' | head -1 | grep . || echo "unknown"
}

# FIX 5: a loud, machine-readable note instead of three lines at the end of
# a log. Whoever picks this up next should not have to reconstruct what to
# do from the watchdog log and the ledger.
needs_recovery() {
  local reason="$1" note="$DEST/NEEDS-RECOVERY.txt"
  cat > "$note" <<RECEOF
THIS RUN'S FILES ARE NOT FULLY HOME. Written $(ts) by watch_run_a3.sh.

What happened: $reason

Run name:            $OUT
Rented machine:      $POD
Directory on it:     $RUN_DIR
Network volume:      $NETVOL
Artifacts here:      $DEST
Last step held here: $(last_local_step)

The model file at the final step is on the network volume above, which
outlives the machine. Getting it back is a file copy, not a training run:
rent the cheapest secure machine in the volume's region with that volume
mounted, copy $OUT.pt, $OUT.DONE and the training log off it, check the
copy against the volume by checksum BEFORE deleting, then delete the
machine and confirm none are left. The same recovery on 2026-09-20 took a
few minutes and cost \$0.067.

Renting a machine is billable and needs John's go, quoted verbatim in the
compute ledger row, like any other spend.
RECEOF
  say "wrote $note — this run needs a recovery copy from the volume"
}

kill_pod() {
  say "deleting pod $POD"
  runpodctl pod delete "$POD" && sleep "$KILL_SETTLE_S"
  pod_exists && say "WARNING: pod still present after delete — retry manually" \
             || say "pod gone; billing stopped"
}

# FIX 4: the completion path. A checked copy first, THEN the receipt, THEN
# the delete — in that order, every time. The machine is never deleted on a
# copy that did not check out.
on_finished() {
  say "finished-marker found — training complete"
  local tries=0
  while [ "$tries" -lt "$FINAL_TRIES" ]; do
    tries=$((tries + 1))
    if fetch_final; then
      write_receipt
      kill_pod
      say "run complete; artifacts in $DEST"
      exit 0
    fi
    say "final copy attempt $tries of $FINAL_TRIES did not check out"
    [ "$tries" -lt "$FINAL_TRIES" ] \
      && { say "retrying in ${FINAL_RETRY_S}s"; sleep "$FINAL_RETRY_S"; }
  done
  say "FINAL COPY STILL UNCHECKED after $FINAL_TRIES attempts."
  say "NOT deleting the machine and NOT writing a receipt: a machine that is"
  say "still up is recoverable, and a deleted one is not. The machine's own"
  say "agent enforces the deadline, so this does not bill open-endedly."
  needs_recovery "the final copy could not be checked against the machine after $FINAL_TRIES attempts; the machine was deliberately left running"
  exit 4
}

# FIX 5: the machine is gone. This is where the 2026-09-19 run ended up.
on_machine_gone() {
  say "the machine is gone, confirmed over $MISSING_CONFIRM checks: it deleted"
  say "itself on finishing, was killed, or crashed."
  if [ -f "$DEST/$OUT.DONE" ] && [ -f "$DEST/$OUT.pt" ]; then
    say "the finished-marker and the model file are both already here, so the"
    say "run is complete and nothing needs recovering."
    exit 0
  fi
  needs_recovery "the machine was deleted before this watcher took the final copy; what is here stops at the last routine pull"
  exit 3
}

say "watchdog up: pod=$POD out=$OUT dest=$DEST deadline=$(date -u -r "$DEADLINE_EPOCH" +%Y-%m-%dT%H:%M:%SZ)"
say "fix 1 active: checkpoint pulls are archive-based and checksum-verified"
say "fixes 3-6 active: finished-marker checked every ${PROBE_S}s; files copied"
say "every ${POLL_S}s; on finishing, the copy is checked, then a receipt is"
say "written on the machine, then the machine is deleted — in that order."
say "REAP: the machine's own agent (src/reap_agent.sh) holds it open until"
say "that receipt arrives, or a bounded wait runs out. Lid open is still the"
say "right habit — it is what keeps the wait short — but a shut lid now costs"
say "a bounded idle bill and a recovery note, not an unbounded one."
i=0
last_poll=0
while :; do
  now=$(date +%s)

  if [ "$now" -ge "$DEADLINE_EPOCH" ]; then
    # Runaway backstop. Here, and only here, the machine is deleted even on
    # an unchecked copy: a run past its deadline is a runaway and the
    # spending has to stop. Still try for a good copy first.
    say "DEADLINE reached — fetch then kill (runaway backstop, owned locally)"
    fetch_final || needs_recovery "the deadline was reached and the final copy could not be checked before the machine was deleted"
    kill_pod
    exit 2
  fi

  # FIX 6, cheap half: one tiny remote command, every PROBE_S.
  if $SSH "test -f $RUN_DIR/$OUT.DONE" 2>/dev/null; then
    on_finished
  fi

  # FIX 6, expensive half: existence check and file copying, every POLL_S.
  if [ $((now - last_poll)) -ge "$POLL_S" ]; then
    last_poll=$now
    pod_gone_confirmed && on_machine_gone
    fetch_small || say "small fetch failed this poll (transient ssh?)"
    i=$((i + 1))
    [ $((i % CKPT_EVERY)) -eq 0 ] && fetch_ckpt
    [ -f "$DEST/train_$OUT.log.tail" ] \
      && say "poll $i: $(tail -1 "$DEST/train_$OUT.log.tail" 2>/dev/null | cut -c1-160)"
  fi

  sleep "$PROBE_S"
done
