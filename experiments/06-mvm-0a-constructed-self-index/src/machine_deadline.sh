#!/bin/bash
# machine_deadline.sh — delete a rented machine when its money runs out,
# whatever it is doing.
#
# 2026-09-25. Ruled by John 2026-09-25 ("agreed on all"), on section 7 item 4
# of docs/2026-09-25-rented-slice-findings.md: "A hard cap no code enforces."
# That day the unregistered launcher hung before it had spawned anything that
# could delete the machine, and the only thing standing between a $2.00 cap
# and about $24 of billing was a person reading the log.
#
# Spawned by launch_a3_fetch_first.sh the moment the machine exists (only when
# HARD_CAP_USD is set), detached and under the keep-awake command. It takes
# one argument, an env file the launcher writes:
#
#   POD                the machine's id
#   OUT                the run's output name, for the record line
#   CREATED_AT_EPOCH   laptop clock, read just before the create call
#   DELETE_AT_EPOCH    CREATED_AT_EPOCH + HARD_CAP_USD / RATE_PER_HOUR_USD hours
#   HARD_CAP_USD, RATE_PER_HOUR_USD, POSTED_RATE   for the record line
#   POLL_S             how often to read the clock
#
# WHAT IT DOES NOT LOOK AT, ON PURPOSE: whether training finished, whether the
# files are home, whether the launcher or the watchdog are alive. A deadline
# that consults run state is only as good as the run-state reading, and the
# reading is what failed on 2026-09-25.
#
# 2026-10-06, ruled by John (fix 4 of page 2 of the ruling packet on the
# built models that lost their ownership route; method:
# docs/2026-10-06-tripwire-fixes-method.md): in the development run the
# timers outlived their machines and had to be stopped by hand, or they would
# have written false "deadline reached" lines. It now STOPS ITSELF ON A
# CONFIRMED DELETION AND ON NOTHING WEAKER:
#   * the watchdog's own deletion record, $GONE_RECORD (default
#     machine_gone_$POD beside this settings file), naming this machine; or
#   * the vendor SAYING the machine does not exist ("not found" / status
#     404), asked every VENDOR_CHECK_S seconds with a read.
# A failed reading, an empty answer, an unreadable answer, or a record naming
# another machine leaves it armed to its deadline. If TRIP_PY, TRIP_SCRIPT
# and TRIP_DIR are set (the successor launcher sets them), a delete it makes
# is written into the spending alarm's records with its time.
#
# It reads the wall clock in a loop rather than sleeping once, so time the
# laptop spends asleep still counts toward the deadline, as it does toward
# the bill.
#
# The record it writes, in machine-deadline.log beside the run's files, is
# one line in the compute ledger's column order, for a session to copy into
# ../compute-ledger.md with the vendor balance beside it. It never edits the
# ledger itself.
set -uo pipefail

ENVF="${1:?usage: machine_deadline.sh <env file written by the launcher>}"
# shellcheck disable=SC1090
. "$ENVF"
RUNPODCTL="${RUNPODCTL:-runpodctl}"
GONE_RECORD="${GONE_RECORD:-$(dirname "$ENVF")/machine_gone_$POD}"
VENDOR_CHECK_S="${VENDOR_CHECK_S:-300}"

stamp() { date -u +%Y-%m-%dT%H:%M:%SZ; }
say()   { echo "[$(stamp)] machine-deadline: $*"; }

say "armed for machine $POD ($OUT): deletes at $(date -u -r "$DELETE_AT_EPOCH" +%Y-%m-%dT%H:%M:%SZ),"
say "$(( DELETE_AT_EPOCH - CREATED_AT_EPOCH ))s after creation (hard cap \$$HARD_CAP_USD at \$$RATE_PER_HOUR_USD an hour)"

# 2026-10-06: the vendor saying the machine does not exist. Exit status is
# not trusted either way; only the words are.
says_not_found() {
  printf '%s' "$1" | tr -d ' ' | tr 'A-Z' 'a-z' | grep -qE 'notfound|"status":404'
}
stand_down() {
  say "STANDING DOWN without deleting: $POD is confirmed deleted ($1)."
  say "no deadline line is written; the machine's life is in the watchdog's log and the vendor's bill."
  exit 0
}
say "stands down only on a confirmed deletion: $GONE_RECORD naming $POD, or the vendor saying it does not exist (asked every ${VENDOR_CHECK_S}s)"

LAST_VENDOR=$(date +%s)
while :; do
  NOW=$(date +%s)
  [ "$NOW" -ge "$DELETE_AT_EPOCH" ] && break
  if [ -f "$GONE_RECORD" ] && grep -q "machine $POD " "$GONE_RECORD" 2>/dev/null; then
    stand_down "the watchdog's record: $(head -1 "$GONE_RECORD" | cut -c1-200)"
  fi
  if [ $(( NOW - LAST_VENDOR )) -ge "$VENDOR_CHECK_S" ]; then
    LAST_VENDOR=$NOW
    V=$("$RUNPODCTL" pod get "$POD" -o json 2>&1)
    if says_not_found "$V"; then
      stand_down "the vendor answered: $(printf '%s' "$V" | tr '\n' ' ' | cut -c1-160)"
    fi
  fi
  LEFT=$(( DELETE_AT_EPOCH - NOW ))
  sleep $(( LEFT < POLL_S ? LEFT : POLL_S ))
done

REASON="hard cap reached: \$$HARD_CAP_USD at \$$RATE_PER_HOUR_USD an hour allows $(( DELETE_AT_EPOCH - CREATED_AT_EPOCH ))s of machine life; run state was not consulted"
say "DEADLINE REACHED. Deleting $POD. Reason: $REASON"

RC=1
ANSWER=""
for attempt in 1 2 3; do
  ANSWER=$("$RUNPODCTL" pod delete "$POD" 2>&1); RC=$?
  say "delete attempt $attempt: exit $RC: $(printf '%s' "$ANSWER" | tr '\n' ' ' | cut -c1-200)"
  [ "$RC" -eq 0 ] && break
  sleep 20
done

if [ "$RC" -eq 0 ]; then
  RESULT="DELETED by the laptop's machine deadline"
  if [ -n "${TRIP_PY:-}" ] && [ -n "${TRIP_SCRIPT:-}" ] && [ -n "${TRIP_DIR:-}" ]; then
    "$TRIP_PY" "$TRIP_SCRIPT" gone --state "$TRIP_DIR" --pod "$POD" --at "$(date +%s)" \
      --by "the machine deadline" 2>&1 | sed 's/^/  /' \
      || say "could not write the deletion time into the spending alarm's records"
  fi
else
  RESULT="delete command FAILED 3 times (exit $RC) -- the machine may already be gone, or may still be billing: check the vendor's machine list NOW"
fi
LIFE=$(( $(date +%s) - CREATED_AT_EPOCH ))
say "$RESULT"
# The ledger's columns: date | what ran | GPU | hours (est -> act) | $ est | $ actual | running total
echo "LEDGER-STYLE LINE: | $(TZ=America/Los_Angeles date +%Y-%m-%d) | machine deadline for \`$OUT\`: machine \`$POD\` $RESULT at $(stamp). Reason: $REASON | (see the run's row) | act: about $(awk -v s="$LIFE" 'BEGIN { printf "%.2f", s / 3600 }') h of machine life by the laptop clock | cap \$$HARD_CAP_USD | by arithmetic at most about \$$(awk -v s="$LIFE" -v r="$RATE_PER_HOUR_USD" 'BEGIN { printf "%.2f", s / 3600 * r }'); read the vendor balance for the actual | — |"
[ "$RC" -eq 0 ]
