#!/bin/bash
# sleep_guard_selftest.sh — proves the derived launcher's sleep precondition
# both REFUSES and PASSES, without renting anything, contacting any vendor,
# spending a cent, or touching this Mac's real power settings.
#
# WHAT IS BEING PROVED
# --------------------
# One rule, added to src/launch_a3_fetch_first.sh on 2026-09-24:
#
#   A real launch is refused unless this Mac's never-sleep override is ON
#   and this Mac is on wall power — because idle billing has cost about
#   $10.30 across four occurrences and every one had the same shape: the
#   run finished, the Mac was asleep, and the rented machine went on
#   charging with nothing awake to delete it.
#
# HOW IT AVOIDS SPENDING ANYTHING. The launcher's sleep check is the FIRST
# thing it does after parsing its knobs, and it sits far above the first
# vendor command. Every case here either refuses at that check or stops at
# the dry-run block, which creates nothing. The real `pmset` is never
# consulted and never changed: the launcher reads power settings through a
# `PMSET` variable, and each case points that at a stand-in shell script
# that prints whatever reading the case wants to test. That is the same
# trick reap_handshake_selftest.sh plays on `runpodctl`.
#
# WHY THERE IS A NEGATIVE CONTROL. docs/known-failure-modes.md sets the
# standard that a test never seen to fail has not been shown to detect
# anything. Case 0 feeds the check a machine that is safe in every way and
# requires it NOT to refuse; cases 1 to 4 feed it the unsafe readings and
# require a refusal. If case 0 ever refuses, or any of 1 to 4 ever passes,
# this harness has stopped measuring the property it claims to.
#
# usage: bash sleep_guard_selftest.sh          (runs every case)
#        bash sleep_guard_selftest.sh 3        (runs case 3 only)
# exit:  0 every check passed; 1 a check failed.
set -uo pipefail

if [ "$#" -gt 1 ]; then
  echo "refusing to run: $(basename "$0") takes at most one case number." >&2
  exit 2
fi

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
LAUNCHER="$SRC_DIR/launch_a3_fetch_first.sh"
ONLY="${1:-}"
PASS=0
FAIL=0

red() { printf '\033[31m%s\033[0m\n' "$*"; }
grn() { printf '\033[32m%s\033[0m\n' "$*"; }
ok()  { PASS=$((PASS + 1)); grn "    pass: $*"; }
bad() { FAIL=$((FAIL + 1)); red "    FAIL: $*"; }

want_case() { [ -z "$ONLY" ] || [ "$ONLY" = "$1" ]; }

# --------------------------------------------------------------- stand-in
# Builds a fake `pmset` that prints exactly the three readings the launcher
# asks for, in the real tool's own layout. $1 is the SleepDisabled value
# ("-" means the line is missing entirely, as it would be if the tool
# changed or failed); $2 is the power source ("-" means the line is
# missing); $3 and $4 are the idle sleep timers for battery and wall power,
# which the launcher reports and must not gate on.
make_pmset() {
  local disabled="$1" source="$2" idle_batt="$3" idle_ac="$4"
  T=$(mktemp -d)
  T=$(cd "$T" && pwd -P)
  PMSET_BIN="$T/pmset"
  cat > "$PMSET_BIN" <<FAKE
#!/bin/bash
# fake pmset. Reads nothing real and changes nothing.
case "\$1 \$2" in
  "-g batt")
    if [ "$source" != "-" ]; then echo "Now drawing from '$source'"; fi
    echo " -InternalBattery-0 (id=1)	100%; charged; 0:00 remaining present: true"
    ;;
  "-g custom")
    echo "Battery Power:"
    echo " displaysleep         5"
    echo " sleep                $idle_batt"
    echo "AC Power:"
    echo " displaysleep         5"
    echo " sleep                $idle_ac"
    ;;
  "-g "|"-g")
    echo "System-wide power settings:"
    if [ "$disabled" != "-" ]; then echo " SleepDisabled		$disabled"; fi
    echo "Currently in use:"
    echo " hibernatemode        3"
    ;;
  *) echo "fake pmset: unhandled: \$*" >&2; exit 1 ;;
esac
FAKE
  chmod +x "$PMSET_BIN"

  # A SECOND, INDEPENDENT STOP, so this harness cannot spend money even if
  # the thing it is testing is broken. Every case that asks for a REAL
  # launch (not a dry run) also points the launcher's local interpreter at
  # a stand-in that always fails. The launcher's own module self-tests then
  # refuse the launch a few lines after the sleep check and long before its
  # first vendor command, so a sleep check that let everything through
  # would still create nothing. The dry-run cases do not need this: the
  # dry-run block creates nothing by construction.
  FAILING_PY="$T/never-passes"
  cat > "$FAILING_PY" <<'STOPPER'
#!/bin/bash
echo "self-test stand-in: failing on purpose so this test cannot launch" >&2
exit 1
STOPPER
  chmod +x "$FAILING_PY"
}

# Runs the REAL launcher with the stand-ins in place, capturing output and
# exit status. $1 is "1" for a dry run and "" for a real launch; a real
# launch gets the failing interpreter described above.
run_launcher() {   # $1 = DRYRUN value, $2 = ALLOW_LAPTOP_SLEEP value
  local py=""
  [ -n "$1" ] || py="$FAILING_PY"
  OUT_TEXT=$(PMSET="$PMSET_BIN" DRYRUN="$1" ALLOW_LAPTOP_SLEEP="$2" \
    PY_LOCAL="$py" "$LAUNCHER" 2>&1)
  OUT_ST=$?
}

# Every case asserts this: the launcher never got as far as anything that
# could create a rented machine. The launcher prints "creating $CLOUD pod"
# immediately before its first vendor command, so its absence is the proof.
assert_nothing_created() {
  case "$OUT_TEXT" in
    *"creating SECURE pod"*|*"creating COMMUNITY pod"*)
      bad "the launcher reached the pod-creating step" ;;
    *) ok "nothing was created — the launcher never reached a vendor command" ;;
  esac
}

# The refusal itself, asserted as three things at once and NOT as an exit
# status alone. Written that way after the mutation run described at the
# bottom of this file: with the sleep check downgraded to a mere warning,
# an exit-status-only assertion still PASSED, because the harness's own
# second stop exits 1 a few lines later for an unrelated reason. An exit
# code that two different refusals share cannot tell you which one fired.
assert_refused_at_the_sleep_check() {
  if [ "$OUT_ST" -eq 1 ]; then ok "it exited 1"
  else bad "it exited $OUT_ST, wanted 1"; fi
  case "$OUT_TEXT" in
    *"REFUSING TO LAUNCH"*) ok "it said it was refusing, in those words" ;;
    *) bad "it never said it was refusing" ;;
  esac
  case "$OUT_TEXT" in
    *"local pre-flight: module self-tests"*)
      bad "it ran on past the sleep check to the next precondition" ;;
    *) ok "and it stopped there, before any later precondition" ;;
  esac
}

cleanup() { [ -n "${T:-}" ] && rm -rf "$T"; T=""; }

# ---------------------------------------------------------------- case 0
# NEGATIVE CONTROL, and it runs first on purpose. A safe Mac: the
# never-sleep override is on and it is plugged in. The check must NOT
# refuse. If it does, every refusal below is worthless, because a check
# that refuses everything detects nothing.
if want_case 0; then
  echo "case 0 — negative control: a safe Mac must NOT be refused"
  make_pmset 1 "AC Power" 15 15
  run_launcher "1" ""
  case "$OUT_TEXT" in
    *"ok: never-sleep override ON, running on wall power"*)
      ok "the check passed the safe Mac and said so" ;;
    *) bad "the check did not report a pass on a safe Mac" ;;
  esac
  case "$OUT_TEXT" in
    *"REFUSING TO LAUNCH"*) bad "it refused a Mac that cannot sleep" ;;
    *) ok "it did not refuse" ;;
  esac
  case "$OUT_TEXT" in
    *"DRYRUN — nothing created"*)
      ok "the launcher ran on past the check to its dry-run block" ;;
    *) bad "the launcher stopped before the dry-run block" ;;
  esac
  # The idle timers are reported and must not decide anything. Here they
  # are 15 minutes on both power sources — a Mac that WOULD idle-sleep —
  # and the launch is allowed regardless, because caffeinate covers idle
  # sleep and the override covers the lid.
  case "$OUT_TEXT" in
    *"idle sleep timers 15 min plugged in / 15 min on battery"*)
      ok "it reported the idle timers it read from 'pmset -g custom'" ;;
    *) bad "it did not report the idle timers" ;;
  esac
  cleanup
fi

# ---------------------------------------------------------------- case 1
# THE FAILURE THAT HAS ACTUALLY COST MONEY. The override is off, so
# shutting the lid puts the Mac to sleep. This is the state the Mac was
# found in on 2026-09-24.
if want_case 1; then
  echo "case 1 — the never-sleep override is OFF: a real launch must refuse"
  make_pmset 0 "AC Power" 15 15
  run_launcher "" ""
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"SleepDisabled 0"*) ok "it named the reading it refused on" ;;
    *) bad "it refused without naming the reading" ;;
  esac
  # A refusal that does not say how to fix it just moves the problem.
  case "$OUT_TEXT" in
    *"sudo pmset -a disablesleep 1"*)
      ok "it printed the command that corrects the setting" ;;
    *) bad "it did not print the fix" ;;
  esac
  case "$OUT_TEXT" in
    *"sudo pmset -a disablesleep 0"*)
      ok "and the command that puts it back afterwards" ;;
    *) bad "it did not say how to undo the fix" ;;
  esac
  case "$OUT_TEXT" in
    *"ALLOW_LAPTOP_SLEEP=1"*) ok "it named the way to override it" ;;
    *) bad "it did not name the override" ;;
  esac
  assert_nothing_created
  cleanup
fi

# ---------------------------------------------------------------- case 2
# On battery. The override is ON, so the lid is covered — but a run is
# about ten hours and the watchdog sits on it for up to a day, which is
# longer than a charge lasts. Same bill by a second route.
if want_case 2; then
  echo "case 2 — override ON but on battery: a real launch must still refuse"
  make_pmset 1 "Battery Power" 15 15
  run_launcher "" ""
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"running on Battery Power, not wall power"*)
      ok "it named the power source it refused on" ;;
    *) bad "it did not name the power source" ;;
  esac
  case "$OUT_TEXT" in
    *"plug in the power adapter"*) ok "it printed the fix" ;;
    *) bad "it did not print the fix" ;;
  esac
  assert_nothing_created
  cleanup
fi

# ---------------------------------------------------------------- case 3
# The reading cannot be taken at all. A check that cannot read its input
# must refuse, not assume the best — assuming the best is how a warning
# becomes decoration.
if want_case 3; then
  echo "case 3 — the setting cannot be read: silence must not count as safe"
  make_pmset "-" "AC Power" 15 15
  run_launcher "" ""
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"could not read the never-sleep override"*)
      ok "it said the reading was missing rather than guessing" ;;
    *) bad "it did not say the reading was missing" ;;
  esac
  assert_nothing_created
  cleanup

  echo "case 3b — the power source cannot be read either"
  make_pmset 1 "-" 15 15
  run_launcher "" ""
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"could not tell whether this Mac is plugged in"*)
      ok "it said which reading was missing" ;;
    *) bad "it did not say which reading was missing" ;;
  esac
  assert_nothing_created
  cleanup
fi

# ---------------------------------------------------------------- case 4
# The two escape hatches, which must behave differently from each other.
# A DRY RUN reports the verdict and carries on, because it creates nothing
# and because check_launcher_argument_guard.sh requires every launcher's
# dry run to exit 0. The EXPLICIT OVERRIDE carries on for a real launch,
# and must say out loud what it is accepting.
if want_case 4; then
  echo "case 4 — a dry run reports the problem and still exits 0"
  make_pmset 0 "AC Power" 15 15
  run_launcher "1" ""
  if [ "$OUT_ST" -eq 0 ]; then ok "the dry run still exited 0"
  else bad "the dry run exited $OUT_ST, wanted 0"; fi
  case "$OUT_TEXT" in
    *"WOULD REFUSE a real launch"*) ok "it still told the operator the problem" ;;
    *) bad "the dry run said nothing about the problem" ;;
  esac
  case "$OUT_TEXT" in
    *"sudo pmset -a disablesleep 1"*) ok "and still printed the fix" ;;
    *) bad "the dry run did not print the fix" ;;
  esac
  case "$OUT_TEXT" in
    *"DRYRUN — nothing created"*) ok "and still reported creating nothing" ;;
    *) bad "the dry run did not reach its own report" ;;
  esac
  cleanup

  echo "case 4b — the explicit override launches anyway, out loud"
  make_pmset 0 "AC Power" 15 15
  run_launcher "" "1"
  case "$OUT_TEXT" in
    *"OVERRIDDEN by ALLOW_LAPTOP_SLEEP=1"*)
      ok "it said the guard had been overridden" ;;
    *) bad "it did not announce the override" ;;
  esac
  case "$OUT_TEXT" in
    *"what it can cost"*) ok "it said what the override can cost" ;;
    *) bad "it overrode silently about the money" ;;
  esac
  case "$OUT_TEXT" in
    *"REFUSING TO LAUNCH"*) bad "it refused despite the override" ;;
    *) ok "it did not refuse" ;;
  esac
  # It must get PAST the sleep check. What stops it here is the launcher's
  # own module self-tests, run against the deliberately failing interpreter
  # this harness supplies — a precondition that has nothing to do with
  # sleep, which is exactly what makes it evidence that the sleep check let
  # the launch through.
  case "$OUT_TEXT" in
    *"local pre-flight: module self-tests"*)
      ok "it carried on to the next precondition" ;;
    *) bad "it stopped at the sleep check anyway" ;;
  esac
  case "$OUT_TEXT" in
    *"self-test — refusing to launch"*)
      ok "and was stopped there instead, by the harness's own second stop" ;;
    *) bad "the harness's second stop did not fire" ;;
  esac
  assert_nothing_created
  cleanup
fi

echo
echo "checks passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ] || exit 1
echo "sleep guard self-test OK — nothing was rented, no vendor was contacted,"
echo "and this Mac's real power settings were never read or changed."

# ---------------------------------------------------------------------------
# THE MUTATION RUN: what this harness looked like FAILING, 2026-09-24
# ---------------------------------------------------------------------------
# docs/known-failure-modes.md sets the standard that a test never seen to
# fail has not been shown to detect anything. Case 0 is half of that answer:
# it shows the check does not simply refuse everything. This is the other
# half. The sleep precondition in launch_a3_fetch_first.sh was temporarily
# downgraded to what every launcher in this repository did before today --
# print the warning, then carry on and launch -- and this harness was run
# against it unchanged. It reported:
#
#   checks passed: 29   failed: 9
#
#   case 1 - the never-sleep override is OFF: a real launch must refuse
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#       FAIL: it did not name the override
#   case 2 - override ON but on battery: a real launch must still refuse
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#   case 3 - the setting cannot be read: silence must not count as safe
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#   case 3b - the power source cannot be read either
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#
# The mutation was then undone and the harness reported 38 passed, 0 failed
# against the real file. Case 0 and case 4 passed throughout, which is
# right: a warning-only launcher still lets a safe Mac through and still
# dry-runs cleanly, so those two cases are not what detects this.
#
# WHAT THE MUTATION RUN CHANGED ABOUT THE HARNESS ITSELF, and the reason it
# was worth doing rather than reasoning about. On the first attempt the
# refusal cases asserted only an exit status of 1, and every one of them
# PASSED against the warning-only launcher. The launcher still exited 1 --
# a few lines further down, at the module self-tests, for a reason that had
# nothing to do with sleep. An exit code shared by two different refusals
# cannot say which fired. The assertion was rewritten to require the
# refusal's own words and its position in the script as well, which is the
# form above and the form that catches the mutation.
