#!/bin/bash
# machine_deadline_selftest.sh — proves the laptop's machine deadline
# (src/machine_deadline.sh, armed by launch_a3_fetch_first.sh when
# HARD_CAP_USD is set) deletes the machine when its money runs out, whatever
# the run is doing — without renting anything, contacting any vendor or
# spending a cent. The clock is shortened: caps of a fraction of a cent turn
# hours into seconds.
#
# 2026-09-25. Ruled by John 2026-09-25 ("agreed on all") on section 7 item 4
# of docs/2026-09-25-rented-slice-findings.md.
#
# STOPS, so nothing here can rent a machine: a stand-in `runpodctl` sits first
# on the command path, rents nothing, and logs every call; the harness checks
# the path resolves to it before each launcher run; HOME is an empty folder,
# so no account key is reachable; the power readings, the ledger and the
# keep-awake command are stand-ins too.
#
# CASES
#   1. the deadline program alone: deletes once the deadline passes, not
#      before, names the machine, and writes the reason and a ledger-style line
#   2. NEGATIVE CONTROL: a deadline in the future deletes nothing. A deadline
#      that deleted at once would pass case 1 and fail this one.
#   3. the whole launcher, stuck on its first ssh the way it was stuck on
#      2026-09-25: the machine is still deleted at creation + cap / rate
#   4. the vendor states a higher rate than the one given: the higher is used
#   5. no HARD_CAP_USD: the launcher arms no deadline at all (default off)
#   6. half a setting (a cap with no rate) is refused before anything runs
#
# usage: ./machine_deadline_selftest.sh     (no arguments)
set -uo pipefail
if [ "$#" -ne 0 ]; then
  echo "refusing to run: $(basename "$0") takes no arguments." >&2; exit 2
fi

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0; FAIL=0
ok()  { PASS=$((PASS + 1)); echo "    pass: $*"; }
bad() { FAIL=$((FAIL + 1)); echo "    FAIL: $*"; }

T=$(mktemp -d); T=$(cd "$T" && pwd -P)
cleanup() {
  pkill -f "$T/bin/fakessh" 2>/dev/null
  pkill -f "$T/.*machine_deadline" 2>/dev/null
  pkill -f "machine_deadline.sh $T" 2>/dev/null
  rm -rf "$T"
}
trap cleanup EXIT
mkdir -p "$T/bin" "$T/home" "$T/dest"

RATE_JSON_COST="0.99"
cat > "$T/bin/runpodctl" <<FAKE
#!/bin/bash
echo "\$(date +%s) \$*" >> "$T/runpodctl.calls"
case "\$1 \$2" in
  "pod create") printf '{\n  "costPerHr": %s,\n  "id": "fakepod0000001"\n}\n' "\$(cat "$T/cost")" ;;
  "pod get")    printf '{"ssh": {"ssh_command": "$T/bin/fakessh root@203.0.113.1"}}\n' ;;
  "pod delete") echo "pod fakepod0000001 deleted" ;;
esac
exit 0
FAKE
# an ssh that never returns: the 2026-09-25 hang, at the very first ssh
cat > "$T/bin/fakessh" <<FAKE
#!/bin/bash
echo "\$(date +%s) \$*" >> "$T/ssh.calls"
exec sleep 3600
FAKE
cat > "$T/bin/caffeinate" <<'FAKE'
#!/bin/bash
while [ "${1:-}" != "${1#-}" ]; do shift; done
exec "$@"
FAKE
cat > "$T/pmset" <<'FAKE'
#!/bin/bash
case "$1 $2" in
  "-g batt") echo "Now drawing from 'AC Power'"
             echo " -InternalBattery-0 (id=1)	100%; charged; 0:00 remaining present: true" ;;
  "-g custom") printf 'Battery Power:\n sleep                15\nAC Power:\n sleep                15\n' ;;
  "-g "|"-g") printf 'System-wide power settings:\n SleepDisabled\t\t1\n' ;;
  *) exit 1 ;;
esac
FAKE
printf '#!/bin/bash\nexit 0\n' > "$T/py-passes"
chmod +x "$T/bin/"* "$T/pmset" "$T/py-passes"
TODAY=$(TZ=America/Los_Angeles date +%Y-%m-%d)
cat > "$T/ledger.md" <<LEDGER
# stand-in compute ledger

## Ledger

| date | phase | what ran | GPU | hrs (est → act) | \$ est | \$ actual | running total |
|---|---|---|---|---|---|---|---|
| $TODAY | test | the deadline test, OUT=deadline_test | 5090 | est 1h | \$2 | — | — |
LEDGER
SAFE_PATH="$T/bin:$PATH"

write_env() {   # $1 file, $2 seconds from now
  local now; now=$(date +%s)
  cat > "$1" <<ENV
POD="fakepod0000001"
OUT="deadline_test"
CREATED_AT_EPOCH=$now
DELETE_AT_EPOCH=$(( now + $2 ))
HARD_CAP_USD="0.0011"
RATE_PER_HOUR_USD="0.99"
POSTED_RATE="0.99"
POLL_S=1
ENV
}

echo "=== 1. the deadline program alone, deadline 3s away"
rm -f "$T/runpodctl.calls"
write_env "$T/case1.env" 3
S=$(date +%s)
PATH="$SAFE_PATH" bash "$SRC_DIR/machine_deadline.sh" "$T/case1.env" > "$T/case1.log" 2>&1
E=$(( $(date +%s) - S ))
sed 's/^/      | /' "$T/case1.log"
DEL=$(grep -c 'pod delete fakepod0000001' "$T/runpodctl.calls" 2>/dev/null)
[ "$DEL" = "1" ] && ok "one delete call, naming the machine" || bad "delete calls naming the machine: ${DEL:-0}, wanted 1"
[ "$E" -ge 3 ] && ok "not before the deadline (took ${E}s for a 3s deadline)" || bad "returned after ${E}s, before the 3s deadline"
grep -q 'Reason: hard cap reached' "$T/case1.log" && ok "wrote the reason" || bad "no reason written"
grep -q 'run state was not consulted' "$T/case1.log" && ok "said run state was not consulted" || bad "did not say run state was ignored"
grep -q '^LEDGER-STYLE LINE: | [0-9-]* | machine deadline' "$T/case1.log" && ok "wrote a ledger-style line" || bad "no ledger-style line"

echo "=== 2. NEGATIVE CONTROL: deadline 60s away, watched for 4s"
rm -f "$T/runpodctl.calls"
write_env "$T/case2.env" 60
PATH="$SAFE_PATH" bash "$SRC_DIR/machine_deadline.sh" "$T/case2.env" > "$T/case2.log" 2>&1 &
P2=$!
sleep 4
kill "$P2" 2>/dev/null; wait "$P2" 2>/dev/null
[ ! -s "$T/runpodctl.calls" ] && ok "nothing deleted before the deadline, so case 1 measured the deadline" \
                             || bad "DELETED BEFORE THE DEADLINE: $(cat "$T/runpodctl.calls")"

run_launcher() {   # extra env in "$@"; runs the real launcher in the background
  rm -f "$T/runpodctl.calls" "$T/ssh.calls"; rm -rf "$T/dest"
  if [ "$(PATH="$SAFE_PATH" command -v runpodctl)" != "$T/bin/runpodctl" ]; then
    echo "the stand-in runpodctl is not first on the command path -- stopping"; exit 1
  fi
  env PATH="$SAFE_PATH" HOME="$T/home" PMSET="$T/pmset" LEDGER="$T/ledger.md" \
      PY_LOCAL="$T/py-passes" CAFFEINATE="$T/bin/caffeinate" DEST_ROOT="$T/dest" \
      OUT=deadline_test SCALE=10M MAXTOK=2000000 GRACE_S=600 DRYRUN= \
      ALLOW_LAPTOP_SLEEP= DEADLINE_POLL_S=1 "$@" \
      "$SRC_DIR/launch_a3_fetch_first.sh" > "$T/launcher.log" 2>&1 &
  LPID=$!
  disown "$LPID"   # so bash does not print "Terminated" when it is stopped
}
stop_launcher() {
  kill "$LPID" 2>/dev/null; pkill -f "$T/bin/fakessh" 2>/dev/null
  for _ in 1 2 3 4 5; do kill -0 "$LPID" 2>/dev/null || break; sleep 1; done
}

echo "=== 3. the whole launcher, hung on its first ssh; cap \$0.0011 at \$0.99/h = 4s"
echo 0.99 > "$T/cost"
run_launcher HARD_CAP_USD=0.0011 RATE_PER_HOUR_USD=0.99
S=$(date +%s)
for _ in $(seq 1 30); do
  grep -q 'pod delete' "$T/runpodctl.calls" 2>/dev/null && break; sleep 1
done
E=$(( $(date +%s) - S ))
sleep 1
grep -q 'MACHINE DEADLINE ARMED' "$T/launcher.log" && ok "the launcher armed the deadline" || bad "the launcher never armed the deadline"
[ -s "$T/ssh.calls" ] && kill -0 "$LPID" 2>/dev/null \
  && ok "the launcher is still stuck on its first ssh (the hang is reproduced)" \
  || bad "the launcher is not stuck on ssh, so this case is not testing a hung run"
grep -q 'pod delete fakepod0000001' "$T/runpodctl.calls" 2>/dev/null \
  && ok "the machine was deleted anyway, about ${E}s after the launch began" \
  || bad "NO DELETE while the launcher hung: $(cat "$T/runpodctl.calls" 2>/dev/null)"
CR=$(awk '/pod create/ {print $1; exit}' "$T/runpodctl.calls"); DL=$(awk '/pod delete/ {print $1; exit}' "$T/runpodctl.calls")
if [ -n "$CR" ] && [ -n "$DL" ]; then
  GAP=$(( DL - CR ))
  [ "$GAP" -ge 3 ] && [ "$GAP" -le 7 ] && ok "creation to delete: ${GAP}s, for a 4s deadline" \
                                          || bad "creation to delete: ${GAP}s, wanted about 4s"
fi
LOGF="$T/dest/artifacts/deadline_test/machine-deadline.log"
grep -q 'Reason: hard cap reached' "$LOGF" 2>/dev/null && ok "reason written to $(basename "$LOGF") beside the run's files" || bad "no reason in the run's machine-deadline.log"
grep -q '^LEDGER-STYLE LINE' "$LOGF" 2>/dev/null && ok "ledger-style line written there too" || bad "no ledger-style line in the run's log"
echo "      launcher output, from creation:"; sed -n '/^pod: /,$p' "$T/launcher.log" | sed 's/^/      | /'
echo "      deadline log:"; sed 's/^/      | /' "$LOGF" 2>/dev/null
stop_launcher

echo "=== 4. the vendor states \$1.98/h, above the \$0.99 given: deadline halves to 2s"
echo 1.98 > "$T/cost"
run_launcher HARD_CAP_USD=0.0011 RATE_PER_HOUR_USD=0.99
for _ in $(seq 1 20); do grep -q 'pod delete' "$T/runpodctl.calls" 2>/dev/null && break; sleep 1; done
sleep 1
grep -q 'the machine deadline uses \$1.98' "$T/launcher.log" && ok "said it used the higher stated rate" || bad "did not use the higher rate"
grep -q 'DELETE_AT_EPOCH=' "$T/dest/artifacts/deadline_test/"machine_deadline_*.env 2>/dev/null
A=$(sed -n 's/^CREATED_AT_EPOCH=//p' "$T/dest/artifacts/deadline_test/"machine_deadline_*.env 2>/dev/null)
B=$(sed -n 's/^DELETE_AT_EPOCH=//p' "$T/dest/artifacts/deadline_test/"machine_deadline_*.env 2>/dev/null)
[ -n "$A" ] && [ $(( B - A )) -eq 2 ] && ok "deadline set to 2s after creation" || bad "deadline was $(( ${B:-0} - ${A:-0} ))s, wanted 2s"
stop_launcher

echo "=== 5. default off: no HARD_CAP_USD, launcher hung on ssh, watched for 6s"
echo 0.99 > "$T/cost"
run_launcher
sleep 6
grep -q 'MACHINE DEADLINE' "$T/launcher.log" && bad "armed a deadline with no cap given" || ok "no deadline armed"
grep -q 'pod delete' "$T/runpodctl.calls" 2>/dev/null && bad "something deleted the machine" || ok "nothing deleted the machine (the behaviour before this change)"
[ -s "$T/runpodctl.calls" ] && ok "(the launcher did reach the stand-in create, so this case ran)" || bad "the launcher never reached the create, so this case tested nothing"
stop_launcher

echo "=== 6. a cap with no rate is refused before anything runs"
rm -f "$T/runpodctl.calls"
OUT6=$(env PATH="$SAFE_PATH" HOME="$T/home" HARD_CAP_USD=2.00 DRYRUN=1 "$SRC_DIR/launch_a3_fetch_first.sh" 2>&1); ST=$?
[ "$ST" = 2 ] && ok "exit 2" || bad "exit $ST, wanted 2"
case "$OUT6" in *"set both HARD_CAP_USD and RATE_PER_HOUR_USD"*) ok "said why" ;; *) bad "did not say why: $OUT6" ;; esac
[ ! -s "$T/runpodctl.calls" ] && ok "never reached the rental command" || bad "reached the rental command"

echo
echo "$PASS passed, $FAIL failed. Nothing was rented and nothing was spent."
[ "$FAIL" -eq 0 ]
