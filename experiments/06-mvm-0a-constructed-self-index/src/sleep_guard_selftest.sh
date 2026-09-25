#!/bin/bash
# sleep_guard_selftest.sh — proves the derived launcher's sleep precondition
# both REFUSES and PASSES, without renting anything, contacting any vendor,
# spending a cent, or touching this Mac's real power settings.
#
# WHAT IS BEING PROVED
# --------------------
# One rule, added to src/launch_a3_fetch_first.sh on 2026-09-24 and moved
# the same day, unchanged, into src/launch_gate.sh, which the fetch-first
# launcher and the other two unregistered launchers now call (method:
# ../launcher-sleep-gate-method.md). This harness still drives it through
# the fetch-first launcher; launch_gate_selftest.sh drives all three and
# covers the gate's other two checks.
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
# Case 5 does the same pairing for the override's value: 0 and false must
# leave the refusal standing, and 5c requires 1 to still work, so that the
# first two cannot pass merely because the check has started refusing
# everything.
#
# TWO OF THE CHECKS ARE ON WORDS RATHER THAN ON BEHAVIOUR, because the words
# are what a person acts on. Case 6 reads the comment giving the reason the
# idle timer is not gated on: it has to say the launch window is uncovered,
# and the order it states — keep-awake cover spawned after the machine
# exists — is checked in every launcher that calls the gate. Case 0 reads the
# banner the operator sees at launch, and requires it to make the same two
# points the comment does — when the cover starts, and that the launch
# itself is outside it.
#
# Case 7 (2026-09-24, added when the check moved) is the charger that is not
# keeping up, with its own control: a Mac holding its charge on purpose
# ("AC attached; not charging") must still pass.
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
GATE="$SRC_DIR/launch_gate.sh"
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
  local batt_state="${5:-charged}"   # the battery line's second field
  T=$(mktemp -d)
  T=$(cd "$T" && pwd -P)
  PMSET_BIN="$T/pmset"
  cat > "$PMSET_BIN" <<FAKE
#!/bin/bash
# fake pmset. Reads nothing real and changes nothing.
case "\$1 \$2" in
  "-g batt")
    if [ "$source" != "-" ]; then echo "Now drawing from '$source'"; fi
    echo " -InternalBattery-0 (id=1)	100%; $batt_state; 0:00 remaining present: true"
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

  # A LEDGER THAT SATISFIES THE GATE'S LEDGER CHECK, so every case here
  # isolates the sleep check. Since the check moved into launch_gate.sh the
  # gate also refuses a real launch with no fresh ledger row for the run,
  # and the real ledger has none for this launcher's default output name —
  # so without this stand-in, case 4b would be refused by the ledger check
  # and never reach the precondition it is testing. The gate's other checks
  # have their own harness, launch_gate_selftest.sh.
  LEDGER_FILE="$T/compute-ledger.md"
  printf '%s\n' "## Ledger" "" \
    "| date | phase | what ran | GPU | hrs (est → act) | \$ est | \$ actual | running total |" \
    "|---|---|---|---|---|---|---|---|" \
    "| $(TZ=America/Los_Angeles date +%Y-%m-%d) | test | a3_30m_seed0 | 5090 | est 10h | \$10 | — | — |" \
    > "$LEDGER_FILE"
}

# Runs the REAL launcher with the stand-ins in place, capturing output and
# exit status. $1 is "1" for a dry run and "" for a real launch; a real
# launch gets the failing interpreter described above.
run_launcher() {   # $1 = DRYRUN value, $2 = ALLOW_LAPTOP_SLEEP value
  local py=""
  [ -n "$1" ] || py="$FAILING_PY"
  OUT_TEXT=$(PMSET="$PMSET_BIN" DRYRUN="$1" ALLOW_LAPTOP_SLEEP="$2" \
    LEDGER="$LEDGER_FILE" PY_LOCAL="$py" "$LAUNCHER" 2>&1)
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
  # and the launch is allowed regardless, because the override covers the
  # lid and the keep-awake command covers idle sleep once the watchdog is
  # running.
  case "$OUT_TEXT" in
    *"idle sleep timers 15 min plugged in / 15 min on battery"*)
      ok "it reported the idle timers it read from 'pmset -g custom'" ;;
    *) bad "it did not report the idle timers" ;;
  esac
  # AND IT MUST NOT OVERSTATE THE COVER IT IS LETTING THEM THROUGH ON. The
  # keep-awake command is spawned with the watchdog as the last thing the
  # launcher does, so it holds nothing off while the machine is being
  # created, the code pushed and the training started. The comment in the
  # launcher now says so; this requires the banner the operator actually
  # reads to say so too, in the same two parts the comment gives — when the
  # cover starts, and that the launch is outside it. The earlier wording,
  # "caffeinate covers idle sleep, the override covers the lid", fails both
  # of these — watched, not argued for: put back, it fails the first two of
  # the three checks below. The third, on the lid, passes under either
  # wording; it is here so that shortening the banner again cannot quietly
  # drop the one thing the old line did get right.
  case "$OUT_TEXT" in
    *"holds idle sleep off only once the watchdog is running"*)
      ok "the banner says when the idle-sleep cover starts" ;;
    *) bad "the banner does not say when the idle-sleep cover starts" ;;
  esac
  case "$OUT_TEXT" in
    *"the launch itself is not covered"*)
      ok "and that the launch window is outside it" ;;
    *) bad "the banner does not say the launch window is uncovered" ;;
  esac
  case "$OUT_TEXT" in
    *"the override covers the lid"*)
      ok "and that the lid is what the override covers" ;;
    *) bad "the banner does not say the override covers the lid" ;;
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

# ---------------------------------------------------------------- case 5
# THE OVERRIDE TAKES ONE VALUE AND ONE ONLY. The first version of this check
# fired on the setting being non-empty, so ALLOW_LAPTOP_SLEEP=0 switched the
# guard OFF and the banner then read "OVERRIDDEN by ALLOW_LAPTOP_SLEEP=0",
# contradicting itself in the same line. Someone who writes 0 means "do not
# allow" and was getting the opposite, on a check whose whole job is to stop
# money being spent. These cases pin the corrected shape: 1 overrides,
# everything else leaves the refusal standing.
if want_case 5; then
  echo "case 5 — ALLOW_LAPTOP_SLEEP=0 must NOT switch the guard off"
  make_pmset 0 "AC Power" 15 15
  run_launcher "" "0"
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"OVERRIDDEN by ALLOW_LAPTOP_SLEEP"*)
      bad "0 switched the guard off, and the banner contradicted itself" ;;
    *) ok "it did not announce an override it was not given" ;;
  esac
  # A value that was seen and not taken has to be said out loud, or the
  # operator reads the refusal, believes the override is broken, and reaches
  # for something blunter.
  case "$OUT_TEXT" in
    *"ALLOW_LAPTOP_SLEEP was set to '0', which is not 1"*)
      ok "it said the value was seen and not taken" ;;
    *) bad "it ignored the value silently" ;;
  esac
  assert_nothing_created
  cleanup

  echo "case 5b — ALLOW_LAPTOP_SLEEP=false must NOT switch the guard off"
  make_pmset 0 "AC Power" 15 15
  run_launcher "" "false"
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"OVERRIDDEN by ALLOW_LAPTOP_SLEEP"*)
      bad "an unrecognised value switched the guard off" ;;
    *) ok "an unrecognised value left the refusal standing" ;;
  esac
  assert_nothing_created
  cleanup

  # CONTROL for the two cases above, and it is the same argument case 0 makes
  # for the check as a whole: a test that refuses every value is not
  # measuring the values, it is just refusing. Case 4b proves this too; it is
  # repeated here so that running case 5 on its own still carries its control.
  echo "case 5c — control: the one value that IS the override still works"
  make_pmset 0 "AC Power" 15 15
  run_launcher "" "1"
  case "$OUT_TEXT" in
    *"OVERRIDDEN by ALLOW_LAPTOP_SLEEP=1"*)
      ok "1 still overrides, so 0 and false are being read, not refused wholesale" ;;
    *) bad "1 no longer overrides — the check now refuses everything" ;;
  esac
  case "$OUT_TEXT" in
    *"REFUSING TO LAUNCH"*) bad "it refused despite being given 1" ;;
    *) ok "it did not refuse" ;;
  esac
  assert_nothing_created
  cleanup
fi

# ---------------------------------------------------------------- case 6
# THE COMMENT THAT EXPLAINS WHY THE IDLE TIMER IS NOT GATED ON MUST TELL THE
# TRUTH ABOUT WHEN THE COVER STARTS. This is a check on words rather than on
# behaviour, and it is here because the words are load-bearing: they are the
# stated reason case 0 requires a fifteen-minute timer to be let through. The
# reason is sound, but the cover it names does not begin until the watchdog
# is spawned, while the rented machine exists from much earlier in the
# script, and a later session reading an unqualified "already covered" would
# be told the launch window needs nothing.
#
# Until 2026-09-24 the comment gave two line numbers and this case compared
# them with the launcher. The comment now lives in launch_gate.sh, which
# serves three launchers with three different line numbers, so it states the
# ORDER instead, and this case checks that order in every launcher that
# calls the gate: the keep-awake spawn comes after the machine is created.
# That also retires the hand-kept pair of numbers the second check of this
# guard named as the part that could rot.
if want_case 6; then
  echo "case 6 — the comment says when the idle-sleep cover begins, and when it does not"
  for L in launch_a3_fetch_first.sh launch_ctl_pilot.sh launch_pilot_a1.sh; do
    CAFF_LINE=$(grep -n '^nohup "\$CAFFEINATE"' "$SRC_DIR/$L" | head -1 | cut -d: -f1)
    CREATE_LINE=$(grep -n '^CREATE_OUT=\$(runpodctl pod create' "$SRC_DIR/$L" | head -1 | cut -d: -f1)
    if [ -z "$CAFF_LINE" ] || [ -z "$CREATE_LINE" ]; then
      bad "$L: could not find the keep-awake spawn or the pod-creating line"
    elif [ "$CAFF_LINE" -gt "$CREATE_LINE" ]; then
      ok "$L: the cover starts at line $CAFF_LINE, after the machine exists at line $CREATE_LINE, as the comment says"
    else
      bad "$L: the cover starts at line $CAFF_LINE, BEFORE the machine at $CREATE_LINE — the comment is now wrong"
    fi
  done
  if grep -q "THE LAUNCH WINDOW ITSELF IS NOT COVERED" "$GATE"; then
    ok "the comment says plainly that the launch window is uncovered"
  else
    bad "the comment never says the launch window is uncovered"
  fi
  if grep -q "spawns its watchdog" "$GATE" && grep -q "after the rented machine" "$GATE"; then
    ok "and it states the order this case checks"
  else
    bad "the comment no longer states the order this case checks"
  fi
fi

# ---------------------------------------------------------------- case 7
# A CHARGER THAT IS NOT KEEPING UP. The first check of this guard (its
# follow-up 5) found that wall power with a discharging battery passed. The
# guard's own reason for requiring wall power — a flat battery ends the
# watchdog — applies word for word. 7b is its control: "AC attached; not
# charging" is the Mac holding its charge on purpose, which is safe, and a
# check that refused it would refuse a healthy Mac.
if want_case 7; then
  echo "case 7 — wall power but the battery is discharging: a real launch must refuse"
  make_pmset 1 "AC Power" 15 15 "discharging"
  run_launcher "" ""
  assert_refused_at_the_sleep_check
  case "$OUT_TEXT" in
    *"its battery is discharging"*) ok "it named what it refused on" ;;
    *) bad "it did not say the battery is discharging" ;;
  esac
  case "$OUT_TEXT" in
    *"stronger power adapter"*) ok "it printed the fix" ;;
    *) bad "it did not print the fix" ;;
  esac
  assert_nothing_created
  cleanup

  echo "case 7b — control: a Mac holding its charge on purpose must NOT be refused"
  make_pmset 1 "AC Power" 15 15 "AC attached; not charging"
  run_launcher "1" ""
  case "$OUT_TEXT" in
    *"ok: never-sleep override ON, running on wall power"*)
      ok "the check passed a Mac that is plugged in and holding its charge" ;;
    *) bad "the check refused a Mac that is plugged in and holding its charge" ;;
  esac
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
#
# ---------------------------------------------------------------------------
# THE SECOND FAILING RUN: cases 5 and 6, seen failing before they passed
# ---------------------------------------------------------------------------
# 2026-09-24, same standard, same reason. Cases 5, 5b, 5c and 6 were written
# and run BEFORE either of the two fixes they describe was applied to the
# launcher, so that what they detect was watched rather than argued for. That
# run reported:
#
#   checks passed: 46   failed: 10
#
#   case 5 - ALLOW_LAPTOP_SLEEP=0 must NOT switch the guard off
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#       FAIL: 0 switched the guard off, and the banner contradicted itself
#       FAIL: it ignored the value silently
#   case 5b - ALLOW_LAPTOP_SLEEP=false must NOT switch the guard off
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#       FAIL: an unrecognised value switched the guard off
#   case 6 - the comment says when the idle-sleep cover begins
#       FAIL: the comment does not say the cover begins on line 597
#       FAIL: the comment does not say the machine exists from line 360
#       FAIL: the comment never says the launch window is uncovered
#
# Two things in that run are worth keeping. First, case 5c PASSED throughout,
# which is the control doing its job: the old non-empty test did accept 1, so
# the four failures above were about the other values and not about the
# override having stopped working. Second, "it exited 1" PASSED in cases 5
# and 5b against the unfixed launcher, for the same reason it did in the
# first failing run - the launch ran on and was stopped a few lines later by
# this harness's own second stop. The two assertions added after that run,
# the refusal's words and its position, are again what saw the breakage.
#
# With both fixes applied the harness reported 56 passed, 0 failed. The line
# numbers in case 6 are recomputed from the launcher on every run, so they
# read 641 and 404 today rather than the 597 and 360 above; the point of
# computing them is that editing the launcher without re-reading the comment
# fails this case instead of quietly leaving the comment wrong. That is what
# happened next, and it worked as intended: the banner fix below moved both
# lines by two, case 6 failed on the stale numbers, and the comment was
# corrected rather than left wrong.
#
# ---------------------------------------------------------------------------
# THE THIRD FAILING RUN: the banner, seen failing before it passed
# ---------------------------------------------------------------------------
# 2026-09-24, same standard. The comment case 6 guards was corrected to say
# the launch window is uncovered, but the banner the operator reads at launch
# still carried the old overstatement, "caffeinate covers idle sleep, the
# override covers the lid". Nothing in this harness measured that line, so
# nothing complained. Three checks were added to case 0 and the old wording
# put back under them. That run reported, for case 0:
#
#   checks passed: 5   failed: 2
#
#   case 0 - negative control: a safe Mac must NOT be refused
#       FAIL: the banner does not say when the idle-sleep cover starts
#       FAIL: the banner does not say the launch window is uncovered
#
# The third new check, that the override covers the lid, passed against the
# old wording too, which is right: the old line said that much correctly and
# only the cover it claimed was overstated. With the banner corrected the
# harness reports 59 passed, 0 failed.
#
# ---------------------------------------------------------------------------
# THE FOURTH ROUND: the check moved into launch_gate.sh, 2026-09-24
# ---------------------------------------------------------------------------
# The check moved, unchanged, into src/launch_gate.sh so the other two
# unregistered launchers carry it (../launcher-sleep-gate-method.md). Case 6
# stopped comparing two hand-kept line numbers and now checks the order they
# stood for in all three launchers; case 7 was added for a charger that is
# not keeping up. Against the moved check this harness reported
#
#   checks passed: 67   failed: 0
#
# and against deliberately broken copies of the gate (recorded in full in
# ../launcher-sleep-gate-findings.md):
#
#   the refusal downgraded to a warning   checks passed: 60   failed: 7
#       7 x FAIL: it ran on past the sleep check to the next precondition
#   the discharging check removed         checks passed: 63   failed: 4
#       case 7 - wall power but the battery is discharging
#       FAIL: it never said it was refusing
#       FAIL: it ran on past the sleep check to the next precondition
#       FAIL: it did not say the battery is discharging
#       FAIL: it did not print the fix
