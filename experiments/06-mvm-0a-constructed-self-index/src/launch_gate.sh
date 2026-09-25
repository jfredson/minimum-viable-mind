# launch_gate.sh — the launch checklist, made a gate the launcher checks.
# Sourced, never run: `. "$SRC_DIR/launch_gate.sh"; launch_gate`.
#
# 2026-09-24. Method, written before this code: ../launcher-sleep-gate-method.md.
# Called by every UNREGISTERED launcher that can rent a machine
# (launch_a3_fetch_first.sh, launch_ctl_pilot.sh, launch_pilot_a1.sh), after
# its settings are read and BEFORE its dry-run block and its first vendor
# command. The registered launcher launch_a3.sh does not call it; the
# amendment that would make it do so is drafted in §7 of the method.
#
# It refuses a real launch unless all three of these hold, and it reports
# every problem it finds rather than stopping at the first, so the operator
# fixes them in one pass:
#
#   1. THIS MAC CANNOT FALL ASLEEP for the run window: the never-sleep
#      override is on, it is on wall power, and the charger is keeping up.
#   2. THE FETCH AND THE DELETE ARE SCHEDULED INSIDE THE RUN WINDOW: the
#      laptop watchdog that fetches the files and deletes the machine exists
#      and parses, the keep-awake command it runs under exists, both
#      deadlines are whole hours, and the laptop's is not later than the
#      machine's own.
#   3. A LEDGER ROW WITH AN ESTIMATE EXISTS BEFORE THE MACHINE DOES: a row in
#      compute-ledger.md, dated within the last two days (Pacific), naming
#      this run's output name, with a dollar estimate and no actual cost yet.
#
# Reads, from the launcher: DRYRUN OUT WATCH_H TERM_H WATCHDOG CAFFEINATE
# EXP_DIR, and GRACE_S if the launcher has one. From the environment:
# ALLOW_LAPTOP_SLEEP (overrides check 1 only, and only with the value 1),
# PMSET and LEDGER (stand-ins for tests; setting either is a deliberate act).
#
# The launchers run under `set -uo pipefail` and deliberately NOT `set -e`
# (ruling 2026-09-22 §5), so a refusal here exits for itself: a gate that
# only printed would print and launch anyway. Written for the bash 3.2 that
# macOS ships, so no empty-array expansions under `set -u`.

# ---- check 1: this Mac must not be able to fall asleep ---------------------
# Carried over from launch_a3_fetch_first.sh at 97ee3c9, where two checking
# sessions passed it (reviews/2026-09-24-sleep-guard-check-claude-worktree.md,
# reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md). Its reasons,
# kept here because this is now the only copy:
#
# Every launcher in this repository WARNED that the lid must stay open, and
# until 2026-09-24 not one of them CHECKED it. Idle billing — a rented
# machine that has finished its work and goes on charging because nothing
# awake is left to delete it — has cost about $10.30 across four occurrences,
# and every one had the same shape.
#
# WHAT IS READ, AND WHY THIS AND NOT THE OTHER THINGS PMSET REPORTS.
# `pmset -g` prints a single system-wide setting, SleepDisabled, which is the
# "never sleep at all" override. It is the ONLY one of these settings that
# keeps this Mac awake with the LID SHUT, and a shut lid is the failure that
# has actually cost money. The per-power-source idle timers that
# `pmset -g custom` prints — `sleep` and `displaysleep`, separately for
# battery and for wall power — look relevant and are not the thing:
#   * `displaysleep` only darkens the screen. The watchdog keeps running.
#   * `sleep` is the idle timer, and it is held off by `caffeinate` — but
#     only for part of the time a launcher is spending money, and a later
#     reader should not be told otherwise. Every launcher spawns its watchdog
#     under `caffeinate` as the LAST thing it does, after the rented machine
#     already exists (sleep_guard_selftest.sh case 6 checks that order in
#     each launcher on every run, rather than a line number written here).
#     THE LAUNCH WINDOW ITSELF IS NOT COVERED: creating the machine, pushing
#     the code, running the remote checks and starting the training all
#     happen with nothing holding the idle timer off, and on this Mac that
#     timer is fifteen minutes, which is not obviously longer than a slow
#     launch. If it fires in that window the result is the exact shape this
#     check exists to prevent — a rented machine running, this Mac asleep,
#     and nothing awake left to delete it.
#     Refusing here is still the wrong answer to that, and that is why the
#     timer reading below decides nothing: fifteen minutes on a Mac whose
#     override is on and whose lid stays open is safe, so gating on the
#     timer would refuse safe machines, and a guard that refuses safe
#     machines is one somebody switches off. Closing the launch window wants
#     a `caffeinate` started before the machine is created; that is a
#     separate change and it has not been made. Neither the timer nor
#     `caffeinate` survives the lid coming down, which is what the override
#     above is for.
# So the idle timers are read for the report below and never decide anything.
#
# THE POWER SOURCE IS READ TOO, and refused on the same footing. On wall
# power the override is the whole story. On battery it is not: a run is about
# ten hours and the watchdog sits on it for up to a day, which is longer than
# a charge lasts, so an unplugged laptop sleeps when the battery runs out
# however the override is set. Same bill by a second route.
#
# 2026-09-24, added when this moved here: A CHARGER THAT IS NOT KEEPING UP.
# The first check of this guard (its follow-up 5, "the largest of them")
# found that wall power with the battery DISCHARGING passed. The reason for
# requiring wall power applies to it word for word: the battery still runs
# out. `pmset -g batt` prints the battery's state on the line after the power
# source, so the same reading answers it. Only the word `discharging` is
# refused. `AC attached; not charging` is the Mac holding the charge level
# to protect the battery, which is safe, and a looser pattern would catch it.
#
# WHY THIS CHECK CAN BE OVERRIDDEN, WHEN THE OTHER TWO CANNOT.
# The shutdown fix of 2026-09-21 means a sleeping Mac no longer bills without
# limit on the fetch-first launcher: the machine's own watcher deletes it
# after GRACE_S once the files are on the network volume. But that watcher is
# armed LATER, after the machine exists, so nothing here can know it will arm
# — and the other two launchers have no such watcher at all. The risk is
# smaller than it was and it is not gone, so this refuses by default and
# takes an explicit environment variable to proceed: a spending choice made
# out loud rather than by accident. The other two checks are fixed by editing
# a setting or writing a row, and neither is a spending trade-off.
#
# THE OVERRIDE TAKES ONE VALUE AND ONE ONLY, ALLOW_LAPTOP_SLEEP=1. Anything
# else — 0, false, a typo, a value meant for some other setting — leaves the
# refusal standing, and the refusal says the value was seen and not taken.
# The first version fired on the setting being NON-EMPTY, so
# ALLOW_LAPTOP_SLEEP=0 switched the guard off and the banner read
# "OVERRIDDEN by ALLOW_LAPTOP_SLEEP=0", contradicting itself in the same line.
# One value recognised, everything else sent to the money-safe branch.
#
# PMSET is a variable so a test can point it at a stand-in and see this check
# both fail and pass without touching the real machine — the same trick
# reap_handshake_selftest.sh plays on runpodctl.
_gate_sleep() {
  local pmset="${PMSET:-pmset}"
  echo "local pre-flight: can this Mac fall asleep?"
  GATE_SLEEP_OVERRIDE_READ=$("$pmset" -g 2>/dev/null \
    | awk '$1 == "SleepDisabled" { print $2; exit }')
  local batt
  batt=$("$pmset" -g batt 2>/dev/null)
  local source
  source=$(printf '%s\n' "$batt" \
    | sed -n "s/.*Now drawing from '\(.*\)'.*/\1/p" | head -1)
  # the battery's state is the second ';'-separated field of its line:
  # " -InternalBattery-0 (id=…)	100%; charged; 0:00 remaining present: true"
  local batt_state
  batt_state=$(printf '%s\n' "$batt" | awk -F';' '/InternalBattery/ {
    s = $2; gsub(/^[ \t]+|[ \t]+$/, "", s); print s; exit }')
  # context only; these never gate the launch, for the reasons set out above
  local idle_batt idle_ac
  idle_batt=$("$pmset" -g custom 2>/dev/null \
    | awk '/^Battery Power/ { s = 1 } /^AC Power/ { s = 0 } s && $1 == "sleep" { print $2; exit }')
  idle_ac=$("$pmset" -g custom 2>/dev/null \
    | awk '/^AC Power/ { s = 1 } s && $1 == "sleep" { print $2; exit }')

  GATE_SLEEP_REFUSAL=""
  GATE_SLEEP_FIX=""
  if [ -z "$GATE_SLEEP_OVERRIDE_READ" ]; then
    GATE_SLEEP_REFUSAL="could not read the never-sleep override — '$pmset -g' printed no SleepDisabled line"
    GATE_SLEEP_FIX="read it by hand and say what happened:  $pmset -g | grep SleepDisabled"
  elif [ "$GATE_SLEEP_OVERRIDE_READ" != "1" ]; then
    GATE_SLEEP_REFUSAL="the never-sleep override is OFF (SleepDisabled $GATE_SLEEP_OVERRIDE_READ) — shut the lid and this Mac sleeps, taking the watchdog with it"
    GATE_SLEEP_FIX="sudo pmset -a disablesleep 1      (put it back afterwards with: sudo pmset -a disablesleep 0)"
  elif [ -z "$source" ]; then
    GATE_SLEEP_REFUSAL="could not tell whether this Mac is plugged in — '$pmset -g batt' printed no power source"
    GATE_SLEEP_FIX="read it by hand and say what happened:  $pmset -g batt"
  elif [ "$source" != "AC Power" ]; then
    GATE_SLEEP_REFUSAL="this Mac is running on $source, not wall power — the override cannot outlast a flat battery over a ${WATCH_H}h run"
    GATE_SLEEP_FIX="plug in the power adapter, then re-run"
  elif [ "$batt_state" = "discharging" ]; then
    GATE_SLEEP_REFUSAL="this Mac is on wall power but its battery is discharging — the charger is not keeping up, and a flat battery ends the watchdog over a ${WATCH_H}h run just as unplugging does"
    GATE_SLEEP_FIX="use a stronger power adapter, or lighten the load until '$pmset -g batt' reads charging or charged, then re-run"
  fi

  if [ -z "$GATE_SLEEP_REFUSAL" ]; then
    echo "  ok: never-sleep override ON, running on wall power"
    echo "  (idle sleep timers ${idle_ac:-unread} min plugged in / ${idle_batt:-unread} min on battery;"
    echo "   not relied on — the override covers the lid; the keep-awake command"
    echo "   (caffeinate) holds idle sleep off only once the watchdog is running,"
    echo "   so the launch itself is not covered.)"
  else
    echo "  problem: $GATE_SLEEP_REFUSAL"
  fi
}

# ---- check 2: the fetch and the delete are scheduled inside the run window --
# The run window is from launch to the moment the machine is guaranteed gone.
# Two things end it: the laptop watchdog (WATCHDOG), which fetches the files
# and deletes the machine on the finished-marker or at +WATCH_H hours, and the
# machine's own deadline at +TERM_H hours. The watchdog is spawned as the
# launcher's LAST act, after the machine exists, with `nohup … &`, and nobody
# reads its exit status — so a missing or broken watchdog there is a machine
# with no scheduled fetch and no scheduled delete, and the launcher would
# still print "watchdog spawned". Everything that can be checked about it is
# checked here, before the machine exists.
#
# WATCH_H ≤ TERM_H is the shutdown order the reap-race fix (pull request 15,
# ../reap-shutdown-order-method.md) established: the laptop takes the last
# copy, then the machine goes. A laptop deadline later than the machine's
# means a run that hangs is deleted by the machine before the laptop's final
# fetch. Defaults are 24 and 24.
_gate_is_hours() {   # a whole number of hours, at least 1
  case "$1" in ''|*[!0-9]*) return 1 ;; esac
  [ "$1" -ge 1 ] 2>/dev/null
}
_gate_schedule() {
  echo "local pre-flight: are the fetch and the delete scheduled inside the run window?"
  local wd="${WATCHDOG:-}" caf="${CAFFEINATE:-caffeinate}" found=0
  if [ -z "$wd" ]; then
    _gate_add "this launcher did not name the watchdog it spawns (WATCHDOG is empty) — nothing is scheduled to fetch the files or delete the machine" \
              "a launcher bug: set WATCHDOG to the watch_run script it spawns, before calling launch_gate"
    found=1
  elif [ ! -f "$wd" ]; then
    _gate_add "the watchdog this launcher spawns after the machine exists is missing ($wd) — nothing would fetch the files or delete the machine" \
              "restore it (git checkout -- $(basename "$wd")) or run from a checkout that has it"
    found=1
  elif ! bash -n "$wd" 2>/dev/null; then
    _gate_add "the watchdog this launcher spawns does not parse ($wd) — it would die at once and nothing would fetch the files or delete the machine" \
              "see what is wrong with:  bash -n $wd"
    found=1
  fi
  if ! command -v "$caf" >/dev/null 2>&1; then
    _gate_add "the keep-awake command the watchdog is spawned under ($caf) cannot be found — the spawn would fail and no watchdog would run" \
              "it ships with macOS at /usr/bin/caffeinate; check PATH, or CAFFEINATE if it was set"
    found=1
  fi
  if ! _gate_is_hours "$WATCH_H"; then
    _gate_add "the watchdog's delete deadline WATCH_H is '$WATCH_H', not a whole number of hours of at least 1" \
              "set WATCH_H to whole hours, e.g. WATCH_H=24"
    found=1
  fi
  if ! _gate_is_hours "$TERM_H"; then
    _gate_add "the machine's own deadline TERM_H is '$TERM_H', not a whole number of hours of at least 1" \
              "set TERM_H to whole hours, e.g. TERM_H=24"
    found=1
  fi
  if _gate_is_hours "$WATCH_H" && _gate_is_hours "$TERM_H" \
     && [ "$WATCH_H" -gt "$TERM_H" ]; then
    _gate_add "the laptop's fetch-and-delete is due at +${WATCH_H}h, after the machine's own deadline at +${TERM_H}h — a run that hangs would be deleted before the laptop takes the last copy" \
              "set WATCH_H no larger than TERM_H (both default to 24)"
    found=1
  fi
  if [ "$found" = 0 ]; then
    echo "  ok: watchdog $(basename "$wd") present and parses; runs under $caf"
    echo "  ok: laptop fetch-and-delete by +${WATCH_H}h, machine's own deadline +${TERM_H}h"
  fi
}

# ---- check 3: a ledger row with an estimate exists before the machine does --
# Ledger rule 2 ("Estimate before spend") has so far been kept by habit. One
# row in the `## Ledger` table must: name this run's output name OUT as a
# whole word (so seed1 does not match seed10); be dated today or in the two
# days before, Pacific (output names are reused, and a row for an earlier run
# must not satisfy a new launch); carry a dollar figure in its `$ est` column;
# and not yet carry an actual cost (a filled actual-cost column means a launch
# that already happened). It does NOT check that John's go is quoted in the
# row: whether a sentence is a go is not something a pattern can decide.
#
# THE ROW MUST HAVE EXACTLY EIGHT CELLS, the table's eight columns. Corrected
# 2026-09-24 after the check of pull request 33
# (reviews/2026-09-24-launch-gate-pr33-check-claude-worktree.md, section 8).
# The first version counted columns from the right, on the claim that this
# survives a `|` inside the "what ran" prose. It does, but the ledger's real
# 2026-08-17 row also has an annotation appended as an extra cell, and
# counting from the right then read the actual-cost cell as the estimate: a
# good row was refused for a "missing" dollar figure that was there. A `|`
# in prose and an appended cell both give a row more than eight cells, and
# nothing tells them apart. So the gate does not guess which it is. It says
# "line N has C cells, expected 8" and names both causes. A `|` written as
# `\|`, the table's own escape, is prose and not a cell border.
#
# WHAT COUNTS AS A WHOLE WORD. The run name must not continue into more of a
# name: `slice_handshake` is not matched by `slice_handshake_v2`,
# `slice_handshake-v2` or `slice_handshake.v2`. Also corrected after that
# check: the first version treated `-` as a boundary, so a row for
# `slice_handshake-v2` satisfied a launch of `slice_handshake`. A full stop
# that ends a sentence (`… slice_handshake.`) still counts as the end. The
# one hyphenated prefix accepted is `mvm-`, the name the launchers give the
# machine (`mvm-slice_handshake`); `x-slice_handshake` does not match.
GATE_LEDGER_MAX_AGE_D=2
_gate_days_old() {   # $1 = YYYY-MM-DD; prints whole days before today, Pacific
  local today d0 d1
  today=$(TZ=America/Los_Angeles date +%Y-%m-%d)
  d0=$(date -j -u -f '%Y-%m-%d %H' "$1 12" +%s 2>/dev/null) || return 1
  d1=$(date -j -u -f '%Y-%m-%d %H' "$today 12" +%s 2>/dev/null) || return 1
  echo $(( (d1 - d0) / 86400 ))
}
_gate_ledger() {
  local ledger="${LEDGER:-$EXP_DIR/compute-ledger.md}"
  echo "local pre-flight: is there a ledger row with an estimate for '$OUT'?"
  local fix="write it before the machine exists: a row in the '## Ledger' table of $ledger, dated today (Pacific), naming '$OUT', with a dollar figure in the \$ est column and the actual left as —"
  if [ ! -f "$ledger" ]; then
    _gate_add "the compute ledger is not where it should be ($ledger)" "$fix"
    return
  fi
  case "$OUT" in
    ''|*[!A-Za-z0-9_.-]*)
      _gate_add "the output name '$OUT' has characters the ledger check cannot match safely" \
                "use letters, digits, '_', '.' and '-' only"
      return ;;
  esac
  local re
  re=$(printf '%s' "$OUT" | sed 's/\./\\./g')
  local rows
  # the pattern goes in through the environment, not `awk -v`, which
  # rewrites backslashes and would turn the escaped '.' back into "any"
  # Before the name: start of line or a character that cannot be part of a
  # name, optionally followed by exactly "mvm-" — the launchers name the
  # machine mvm-$OUT, and a row naming the machine names the run (the real
  # 2026-09-21 row does). No other hyphenated prefix counts. After the name:
  # end of line, a character that cannot be part of a name, or a full stop
  # NOT followed by more name (a sentence ending, not ".v2").
  rows=$(GATE_RE="(^|[^A-Za-z0-9_.-])(mvm-)?${re}([^A-Za-z0-9_.-]|\\.([^A-Za-z0-9_-]|\$)|\$)" awk -F'|' '
    BEGIN { re = ENVIRON["GATE_RE"] }
    /^## Ledger[ \t]*$/ { inl = 1; next }
    inl && /^## / { exit }
    inl && /^\|/ {
      if ($0 ~ /^\|[- |:]*$/) next                 # the separator row
      d = $2; gsub(/^[ \t]+|[ \t]+$/, "", d)
      if (d == "date") next                         # the header row
      if ($0 !~ re) next
      line = $0; gsub(/\\\|/, "", line)            # "\|" is prose, not a border
      k = split(line, c, "|")
      if (c[k] ~ /^[ \t]*$/) k--                    # a trailing "|" leaves an empty field
      cells = k - 1                                 # the field before the first "|" is not a cell
      est = ""; act = ""
      if (cells == 8) { est = c[7]; act = c[8] }
      date = ""
      if (match(c[2], /20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)) date = substr(c[2], RSTART, 10)
      gsub(/\t/, " ", est); gsub(/\t/, " ", act)
      # every field after the line number carries a leading "=", so an empty
      # one cannot vanish: `read` merges runs of tabs, which would shift the
      # fields after it
      print NR "\t=" date "\t=" cells "\t=" est "\t=" act
    }' "$ledger")
  if [ -z "$rows" ]; then
    _gate_add "no row in the ledger table names this run's output name '$OUT'" "$fix"
    return
  fi
  local why="" ok_line="" line date cells est act age act_n
  while IFS="$(printf '\t')" read -r line date cells est act; do
    date="${date#=}"; cells="${cells#=}"; est="${est#=}"; act="${act#=}"
    if [ -z "$date" ]; then
      why="$why; line $line has no date"; continue
    fi
    age=$(_gate_days_old "$date") || { why="$why; line $line has an unreadable date '$date'"; continue; }
    if [ "$age" -lt 0 ]; then
      why="$why; line $line is dated $date, in the future"; continue
    fi
    if [ "$age" -gt "$GATE_LEDGER_MAX_AGE_D" ]; then
      why="$why; line $line is dated $date, $age days ago (must be within $GATE_LEDGER_MAX_AGE_D)"; continue
    fi
    if [ "$cells" != 8 ]; then
      why="$why; line $line has $cells cells, expected 8 (a '|' inside the prose, which must be written '\\|', or an annotation added as an extra cell, which belongs below the table)"; continue
    fi
    if ! printf '%s' "$est" | grep -q '\$[0-9]'; then
      why="$why; line $line has no dollar figure in its estimate column"; continue
    fi
    act_n=$(printf '%s' "$act" | tr -d '*' | sed 's/^[ \t]*//' | tr 'A-Z' 'a-z')
    case "$act_n" in
      ''|—*|–*|-*|*pending*|*"not launched"*|*"not yet"*|*"nothing spent"*) ;;
      *) why="$why; line $line already records an actual cost ('$(printf '%s' "$act_n" | cut -c1-50)'), so it belongs to a launch that has happened"
         continue ;;
    esac
    ok_line="$line"; break
  done <<ROWS
$rows
ROWS
  if [ -n "$ok_line" ]; then
    echo "  ok: ledger row at line $ok_line names '$OUT', dated within $GATE_LEDGER_MAX_AGE_D days, estimate written, no actual cost yet"
  else
    _gate_add "rows in the ledger name '$OUT' but none will do: ${why#; }" "$fix"
  fi
}

# ---- the decision -----------------------------------------------------------
_gate_add() {   # $1 = what was found, $2 = how to fix it
  GATE_PROBLEMS[${#GATE_PROBLEMS[@]}]="$1"
  GATE_FIXES[${#GATE_FIXES[@]}]="$2"
  echo "  problem: $1"
}
_gate_list() {   # every non-sleep problem and its fix, to stderr or stdout
  local i=0
  while [ "$i" -lt "${#GATE_PROBLEMS[@]}" ]; do
    echo "    - ${GATE_PROBLEMS[$i]}"
    echo "      fix: ${GATE_FIXES[$i]}"
    i=$((i + 1))
  done
}

launch_gate() {
  GATE_PROBLEMS=()
  GATE_FIXES=()
  local allow="${ALLOW_LAPTOP_SLEEP:-}" taken=0
  [ "$allow" = "1" ] && taken=1

  _gate_sleep
  _gate_schedule
  _gate_ledger

  local sleep_bad=0 other_bad="${#GATE_PROBLEMS[@]}"
  [ -n "$GATE_SLEEP_REFUSAL" ] && sleep_bad=1

  # the sleep override, said out loud, and only for the sleep check
  if [ "$sleep_bad" = 1 ] && [ "$taken" = 1 ]; then
    echo "  OVERRIDDEN by ALLOW_LAPTOP_SLEEP=$allow — carrying on anyway."
    echo "  what was found: $GATE_SLEEP_REFUSAL"
    if [ -n "${GRACE_S:-}" ]; then
      echo "  what it can cost: if this Mac sleeps after training finishes, the"
      echo "  rented machine keeps billing until the watcher on it gives up (about"
      echo "  \$0.50 at ${GRACE_S}s and \$0.99/hour), or, if that watcher never"
      echo "  armed and ON_UNARMED=laptop-only, until the +${WATCH_H}h deadline."
    else
      echo "  what it can cost: this launcher has no watcher on the machine, so if"
      echo "  this Mac sleeps after training finishes the rented machine keeps"
      echo "  billing until the machine's own +${TERM_H}h deadline — up to about"
      echo "  \$0.99 for every hour of that."
    fi
    echo "  Record this in the ledger row alongside John's go."
    sleep_bad=0
  fi

  if [ "$sleep_bad" = 0 ] && [ "$other_bad" = 0 ]; then
    echo "launch gate: every check passed."
    return 0
  fi

  if [ -n "${DRYRUN:-}" ]; then
    echo "  WOULD REFUSE a real launch (this is a dry run, so it carries on and"
    echo "  creates nothing):"
    if [ "$sleep_bad" = 1 ]; then
      echo "    - $GATE_SLEEP_REFUSAL"
      echo "      fix: $GATE_SLEEP_FIX"
      if [ -n "$allow" ]; then
        echo "      (ALLOW_LAPTOP_SLEEP is set to '$allow', which is not 1, so a real"
        echo "       launch would not take it as an override either.)"
      fi
    fi
    _gate_list
    return 0
  fi

  {
    echo "  REFUSING TO LAUNCH — the launch checklist is not met:"
    if [ "$sleep_bad" = 1 ]; then
      echo "    - $GATE_SLEEP_REFUSAL"
      echo "      fix: $GATE_SLEEP_FIX"
    fi
    _gate_list
    echo "  then re-run. Nothing was created and nothing was spent."
    if [ "$sleep_bad" = 1 ]; then
      if [ -n "$allow" ]; then
        echo "  ALLOW_LAPTOP_SLEEP was set to '$allow', which is not 1,"
        echo "  so it did not override anything. Only the value 1 overrides this."
      fi
      echo "  To launch on a Mac that can sleep anyway, knowing what it costs:"
      echo "    ALLOW_LAPTOP_SLEEP=1 $0"
      [ "$other_bad" = 0 ] || echo "  (that overrides the sleep check only; the rest has no override.)"
    fi
  } >&2
  exit 1
}
