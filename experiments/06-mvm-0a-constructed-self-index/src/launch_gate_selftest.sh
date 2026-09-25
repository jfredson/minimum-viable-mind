#!/bin/bash
# launch_gate_selftest.sh — proves the launch gate (src/launch_gate.sh) refuses
# on every refusal path, in EVERY launcher that calls it, and lets a properly
# prepared launch through — without renting anything, contacting any vendor,
# spending a cent, or touching this Mac's real power settings.
#
# Method, written before the gate: ../launcher-sleep-gate-method.md §4.
# sleep_guard_selftest.sh covers the sleep check in depth through one
# launcher; this harness covers the gate's other two checks — the fetch and
# the delete scheduled inside the run window, and a ledger row before the
# machine — and runs the refusals through all three unregistered launchers.
#
# THREE INDEPENDENT STOPS, so a broken gate still cannot rent a machine:
#   1. `pmset`, the ledger and the keep-awake command are stand-ins written
#      here, so every reading the gate takes is one this harness chose;
#   2. a stand-in `runpodctl` sits first on the command path. It rents
#      nothing, writes one line per call to a log, and exits 1. Whether a
#      launcher REACHED the rental command is read from that log, not
#      guessed from printed text. The harness checks the command path
#      resolves to the stand-in before every run, and stops if it does not;
#   3. HOME is an empty temporary folder, so even the real `runpodctl`, if
#      somehow reached, has no account key to rent anything with.
# Refusal cases also get a failing Python stand-in, so the two launchers
# that run module self-tests stop there too if the gate lets them through.
#
# THE NEGATIVE CONTROL. For each launcher, a safe Mac, a good ledger row and a
# sound watchdog, run as a REAL launch, must get past the gate and reach the
# stand-in rental command. A gate that refused everything would pass every
# refusal case below and fail this one, which is what makes the refusals
# worth reading (docs/known-failure-modes.md, "Adding to this list").
#
# usage: ./launch_gate_selftest.sh     (no arguments)
# exit:  0 every check passed; 1 a check failed or the harness could not
#        make its stand-ins safe.
set -uo pipefail

if [ "$#" -ne 0 ]; then
  echo "refusing to run: $(basename "$0") takes no arguments." >&2
  exit 2
fi

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
EXP_DIR="$(cd "$SRC_DIR/.." && pwd)"
LAUNCHERS="launch_a3_fetch_first.sh launch_ctl_pilot.sh launch_pilot_a1.sh"
RUN_OUT="gate_test_run"
PASS=0
FAIL=0

red() { printf '\033[31m%s\033[0m\n' "$*"; }
grn() { printf '\033[32m%s\033[0m\n' "$*"; }
ok()  { PASS=$((PASS + 1)); grn "    pass: $*"; }
bad() { FAIL=$((FAIL + 1)); red "    FAIL: $*"; }

today()    { TZ=America/Los_Angeles date +%Y-%m-%d; }
days_ago() { TZ=America/Los_Angeles date -v-"$1"d +%Y-%m-%d; }
days_on()  { TZ=America/Los_Angeles date -v+"$1"d +%Y-%m-%d; }

# ------------------------------------------------------------- stand-ins
T=$(mktemp -d); T=$(cd "$T" && pwd -P)
trap 'rm -rf "$T"' EXIT
mkdir -p "$T/bin" "$T/home"

# the rental command: rents nothing, logs every call, fails
cat > "$T/bin/runpodctl" <<FAKE
#!/bin/bash
echo "\$*" >> "$T/runpodctl.calls"
exit 1
FAKE
chmod +x "$T/bin/runpodctl"
SAFE_PATH="$T/bin:$PATH"
if [ "$(PATH="$SAFE_PATH" command -v runpodctl)" != "$T/bin/runpodctl" ]; then
  red "the stand-in runpodctl is not first on the command path — stopping before any launcher runs"
  exit 1
fi

# Python stand-ins for the module self-tests
printf '#!/bin/bash\nexit 1\n' > "$T/py-fails"; chmod +x "$T/py-fails"
printf '#!/bin/bash\nexit 0\n' > "$T/py-passes"; chmod +x "$T/py-passes"

# pmset: $1 SleepDisabled, $2 power source, $3 battery state
make_pmset() {
  cat > "$T/pmset" <<FAKE
#!/bin/bash
case "\$1 \$2" in
  "-g batt") echo "Now drawing from '$2'"
             echo " -InternalBattery-0 (id=1)	100%; $3; 0:00 remaining present: true" ;;
  "-g custom") printf 'Battery Power:\n sleep                15\nAC Power:\n sleep                15\n' ;;
  "-g "|"-g") printf 'System-wide power settings:\n SleepDisabled\t\t$1\n' ;;
  *) exit 1 ;;
esac
FAKE
  chmod +x "$T/pmset"
}

# ledger: one row, $1 date, $2 what-ran text, $3 estimate cell, $4 actual cell
make_ledger() {
  {
    echo "# stand-in compute ledger"
    echo
    echo "## Ledger"
    echo
    echo "| date | phase | what ran | GPU | hrs (est → act) | \$ est | \$ actual | running total |"
    echo "|---|---|---|---|---|---|---|---|"
    echo "| $1 | test | $2 | 5090 | est 10h | $3 | $4 | — |"
    echo
    echo "## Expected spend"
    echo
    echo "| $1 | a row after the table that must be ignored | $RUN_OUT | x | x | \$1 | — | — |"
  } > "$T/ledger.md"
}

# the three good defaults every case starts from
reset_standins() {
  make_pmset 1 "AC Power" "charged"
  make_ledger "$(today)" "the gate test, OUT=$RUN_OUT" "\$10" "—"
  rm -f "$T/runpodctl.calls"
  LAUNCH_DIR="$SRC_DIR"
  ENV_EXTRA=""
}

# A copy of the launcher's folder, for the cases that must break the watchdog
# the launcher spawns. The gate reads the watchdog from beside the launcher,
# so the only way to take it away is to run a copy with it taken away.
copy_src() {
  rm -rf "$T/exp"; mkdir -p "$T/exp/src"
  cp "$SRC_DIR"/launch_*.sh "$SRC_DIR"/watch_run*.sh "$T/exp/src/"
  LAUNCH_DIR="$T/exp/src"
}

# run $1 (a launcher name) for real unless DRYRUN is in ENV_EXTRA
run() {
  local launcher="$1" py="${2:-$T/py-fails}"
  rm -f "$T/runpodctl.calls"
  OUT_TEXT=$(env PATH="$SAFE_PATH" HOME="$T/home" PMSET="$T/pmset" \
    LEDGER="$T/ledger.md" OUT="$RUN_OUT" PY_LOCAL="$py" \
    DEST_ROOT="$T/dest" DRYRUN= ALLOW_LAPTOP_SLEEP= $ENV_EXTRA \
    "$LAUNCH_DIR/$launcher" 2>&1)
  OUT_ST=$?
}

called()   { [ -s "$T/runpodctl.calls" ]; }

# A refusal is asserted as four things, never as an exit status alone: an
# exit status shared by unrelated refusals cannot say which one fired
# (sleep_guard_selftest.sh, the first mutation run).
assert_refused() {   # $1 = words the refusal must contain
  [ "$OUT_ST" -eq 1 ] && ok "exited 1" || bad "exited $OUT_ST, wanted 1"
  case "$OUT_TEXT" in *"REFUSING TO LAUNCH"*) ok "said it was refusing" ;;
    *) bad "never said it was refusing" ;; esac
  case "$OUT_TEXT" in *"$1"*) ok "named the problem: '$1'" ;;
    *) bad "did not name the problem '$1'" ;; esac
  # WHERE it stopped. Added after the first mutation run below: with the
  # gate downgraded to a warning, two of the three launchers were still
  # stopped short of the rental command — by the failing self-test stand-in,
  # a stop that has nothing to do with the gate — so the rental log alone
  # saw the breakage in one launcher out of three.
  case "$OUT_TEXT" in
    *"local pre-flight: module self-tests"*|*"creating SECURE pod"*|*"creating COMMUNITY pod"*)
      bad "it went on past the gate to the next step" ;;
    *) ok "it stopped at the gate" ;;
  esac
  called && bad "REACHED THE RENTAL COMMAND: $(head -1 "$T/runpodctl.calls")" \
         || ok "never reached the rental command"
}

# ------------------------------------------------------------------ cases
for L in $LAUNCHERS; do
  echo
  echo "=== $L"

  echo "  control — a safe Mac, a good ledger row, a sound watchdog: a REAL launch must get through"
  reset_standins
  run "$L" "$T/py-passes"
  case "$OUT_TEXT" in *"launch gate: every check passed."*) ok "the gate passed it" ;;
    *) bad "the gate did not pass a properly prepared launch" ;; esac
  case "$OUT_TEXT" in *"REFUSING TO LAUNCH"*) bad "it refused" ;; *) ok "it did not refuse" ;; esac
  if called && grep -q "pod create" "$T/runpodctl.calls"; then
    ok "it reached the (stand-in) rental command, so the gate let it through"
  else
    bad "it never reached the rental command"
  fi
  case "$OUT_TEXT" in *"ledger row at line 7 names '$RUN_OUT'"*) ok "it found the right row" ;;
    *) bad "it did not report the row it matched" ;; esac

  echo "  1 — the never-sleep override is off"
  reset_standins; make_pmset 0 "AC Power" "charged"; run "$L"
  assert_refused "SleepDisabled 0"

  echo "  2 — no ledger row names this run"
  reset_standins; make_ledger "$(today)" "some other run, OUT=other_run" "\$10" "—"; run "$L"
  assert_refused "no row in the ledger table names this run's output name '$RUN_OUT'"

  echo "  2b — a row names a LONGER name that merely starts with this one"
  reset_standins; make_ledger "$(today)" "OUT=${RUN_OUT}0" "\$10" "—"; run "$L"
  assert_refused "no row in the ledger table names"

  echo "  3 — the only row is five days old"
  reset_standins; make_ledger "$(days_ago 5)" "OUT=$RUN_OUT" "\$10" "—"; run "$L"
  assert_refused "5 days ago (must be within 2)"

  echo "  3b — the only row is dated in the future"
  reset_standins; make_ledger "$(days_on 3)" "OUT=$RUN_OUT" "\$10" "—"; run "$L"
  assert_refused "in the future"

  echo "  4 — the row has no dollar estimate"
  reset_standins; make_ledger "$(today)" "OUT=$RUN_OUT" "to be priced" "—"; run "$L"
  assert_refused "no dollar figure in its estimate column"

  echo "  5 — the row already records an actual cost, so it is an earlier launch's"
  reset_standins; make_ledger "$(today)" "OUT=$RUN_OUT" "\$10" "**\$9.87** (balance-confirmed)"; run "$L"
  assert_refused "already records an actual cost"

  echo "  6 — the ledger file is missing"
  reset_standins; rm -f "$T/ledger.md"; run "$L"
  assert_refused "the compute ledger is not where it should be"

  echo "  7 — the watchdog it would spawn is missing"
  reset_standins; copy_src; rm -f "$T/exp/src"/watch_run*.sh; run "$L"
  assert_refused "is missing"

  echo "  7b — the watchdog it would spawn does not parse"
  reset_standins; copy_src
  for w in "$T/exp/src"/watch_run*.sh; do printf '\nif then fi (\n' >> "$w"; done
  run "$L"
  assert_refused "does not parse"

  echo "  8 — the keep-awake command cannot be found"
  reset_standins; ENV_EXTRA="CAFFEINATE=$T/no-such-caffeinate"; run "$L"
  assert_refused "cannot be found"

  echo "  9 — the laptop's delete is due after the machine's own deadline"
  reset_standins; ENV_EXTRA="WATCH_H=30 TERM_H=24"; run "$L"
  assert_refused "after the machine's own deadline"

  echo "  9b — control: equal deadlines are allowed"
  reset_standins; ENV_EXTRA="WATCH_H=12 TERM_H=12"; run "$L" "$T/py-passes"
  case "$OUT_TEXT" in *"launch gate: every check passed."*) ok "equal deadlines passed" ;;
    *) bad "equal deadlines were refused" ;; esac

  echo "  10 — a delete deadline of zero hours"
  reset_standins; ENV_EXTRA="WATCH_H=0"; run "$L"
  assert_refused "not a whole number of hours"

  echo "  11 — two problems at once are both reported"
  reset_standins; make_pmset 0 "AC Power" "charged"; make_ledger "$(today)" "OUT=other_run" "\$10" "—"; run "$L"
  assert_refused "SleepDisabled 0"
  case "$OUT_TEXT" in *"no row in the ledger table names"*) ok "and the ledger problem in the same refusal" ;;
    *) bad "only the first problem was reported" ;; esac

  echo "  12 — the sleep override does not override anything else"
  reset_standins; make_pmset 0 "AC Power" "charged"; make_ledger "$(today)" "OUT=other_run" "\$10" "—"
  ENV_EXTRA="ALLOW_LAPTOP_SLEEP=1"; run "$L"
  assert_refused "no row in the ledger table names"
  case "$OUT_TEXT" in *"OVERRIDDEN by ALLOW_LAPTOP_SLEEP=1"*) ok "the sleep problem was overridden out loud" ;;
    *) bad "the sleep override was not announced" ;; esac
  case "$OUT_TEXT" in *"what it can cost"*) ok "and said what that can cost" ;;
    *) bad "the override did not say what it can cost" ;; esac

  echo "  13 — a dry run reports every problem, exits 0, and creates nothing"
  reset_standins; make_pmset 0 "AC Power" "charged"; make_ledger "$(days_ago 9)" "OUT=$RUN_OUT" "\$10" "—"
  # passing self-test stand-in: the dry run must get past them to its report
  ENV_EXTRA="DRYRUN=1"; run "$L" "$T/py-passes"
  [ "$OUT_ST" -eq 0 ] && ok "the dry run exited 0" || bad "the dry run exited $OUT_ST"
  case "$OUT_TEXT" in *"WOULD REFUSE a real launch"*) ok "it said a real launch would be refused" ;;
    *) bad "it did not report the problems" ;; esac
  case "$OUT_TEXT" in *"9 days ago"*) ok "including the stale ledger row" ;;
    *) bad "the ledger problem was not in the dry run" ;; esac
  case "$OUT_TEXT" in *"DRYRUN — nothing created"*) ok "and it reached its own dry-run report" ;;
    *) bad "it never reached its dry-run report" ;; esac
  called && bad "the dry run reached the rental command" || ok "and never reached the rental command"
done

echo
echo "checks passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ] || exit 1
echo "launch gate self-test OK — nothing was rented, no vendor was contacted,"
echo "and this Mac's real power settings were never read or changed."
