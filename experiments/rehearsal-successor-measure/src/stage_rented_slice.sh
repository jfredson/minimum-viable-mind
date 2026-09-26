#!/bin/sh
# stage_rented_slice.sh — stage the one short slice of rented time, and refuse
# to run it.
#
# WHAT THIS FILE IS
# -----------------
# John has ruled that a short slice of rented time will happen so that seconds
# per step is measured on the hardware every estimate rests on, rather than
# inferred from a laptop. **That ruling is not a go.** This programme requires
# his spoken go naming the specific run, and it has not been given. So this
# script does the whole of the local half — it checks what can be checked
# here, prints the exact commands, and writes the plan to a file — and it
# contains NO code path that creates a rented machine. It cannot spend money
# because there is nothing in it that could.
#
# WHAT THE SLICE BUYS, FOR ONE RENT
# ---------------------------------
# Two questions that both need the same machine:
#
#   1. HOW FAST IS EACH ARCHITECTURE. Rehearsal item R-7. The three
#      architectures of the successor proposal, at the registered shape, timed
#      on the rented graphics card. Arms T and C add computation per layer and
#      will not cost what arm F costs, and the second release of money is
#      asked for on the measured figure rather than on the per-step premium
#      carried over from another experiment's full-versus-twin runs.
#
#   2. DOES THE SHUTDOWN HANDSHAKE WORK AGAINST THE REAL VENDOR. The fix that
#      landed as pull request 15 is verified against local stand-ins only —
#      twenty-six checks including a negative control that reproduces the old
#      ordering and correctly fails — and its author is explicit that the
#      machine-side process check, the credential handling and the command
#      form are inferred rather than measured. The one thing already measured
#      on a real machine (2026-09-16, a paid test costing $0.29) is that a
#      rented machine carries no usable credential and does not know its own
#      identifier. The fix's answer is that the launcher supplies both. That
#      answer has never been tried.
#
# A toy run that finishes in minutes exercises the whole shutdown path weeks
# before about $110 of registered runs depend on it.
#
# WHICH LAUNCHER
# --------------
# The registered launcher `launch_a3.sh` is registered text and is NOT used
# and NOT edited. The slice uses the derived, unregistered
# `launch_a3_fetch_first.sh`, which landed on the main line as pull request 15
# and is produced from the registered launcher by a script that asserts each
# of its nine replacements matched exactly once.
#
# usage: stage_rented_slice.sh          check, print the plan, write it out
#        stage_rented_slice.sh --help
set -u

REHEARSAL_SRC="$(cd "$(dirname "$0")" && pwd)"
REHEARSAL_DIR="$(cd "$REHEARSAL_SRC/.." && pwd)"
REPO="$(cd "$REHEARSAL_DIR/../.." && pwd)"
EXP06="$REPO/experiments/06-mvm-0a-constructed-self-index"
PLAN="$REHEARSAL_DIR/out/rented-slice-plan.txt"

# The slice's own settings. A toy run: it exists to finish, not to learn.
SLICE_TOKENS="${SLICE_TOKENS:-2000000}"     # about 200 steps at batch 128
SLICE_SCALE="${SLICE_SCALE:-10M}"
SLICE_OUT="${SLICE_OUT:-slice_handshake}"
SLICE_GRACE_S="${SLICE_GRACE_S:-600}"       # ten minutes, not the 1800 default
BENCH_STEPS="${BENCH_STEPS:-50}"
RATE_PER_HOUR="${RATE_PER_HOUR:-0.99}"
HARD_CAP="${HARD_CAP:-2.00}"
# 2026-09-25, after the check of the plan at 60d1496 (findings B and C): the
# slice keeps its files in a folder of its own on the network volume, so the
# laptop's final copy brings home that folder and nothing else; and the timing
# runs on the machine BEFORE training starts, so it is finished, and its file
# written, before anything is allowed to delete the machine.
SLICE_RUN_DIR="/workspace/mvm-out/$SLICE_OUT"
BENCH_CMD="python bench_arms.py --device cuda --steps $BENCH_STEPS --batch 32 --out $SLICE_RUN_DIR/bench_arms.json"
# 2026-09-25, after the first attempt hung (docs/2026-09-25-rented-slice-
# findings.md), ruled by John 2026-09-25 ("agreed on all"): the plan passes
# the hard cap and the rate to the launcher, which then deletes the machine
# from this laptop once HARD_CAP / RATE_PER_HOUR hours have passed since
# creation, whatever the run is doing; and it asks the launcher to list and
# empty the slice's folder before anything on the machine starts, because
# the volume can only be read from a rented machine.
DEADLINE_SECS=$(awk -v c="$HARD_CAP" -v r="$RATE_PER_HOUR" 'BEGIN { printf "%d", c / r * 3600 }')
DEADLINE_HM=$(awk -v s="$DEADLINE_SECS" 'BEGIN { printf "%d h %02d min", s / 3600, (s % 3600) / 60 }')
# The plan is run from the main checkout once this branch has merged, which is
# where the launcher's own DEST_ROOT default already points; the paths it
# PRINTS name that checkout even when it is regenerated from a worktree. Only
# the printed commands use this. Every check above runs against this script's
# own tree.
RUN_FROM="${RUN_FROM:-$HOME/Code/minimum-viable-mind}"
P_EXP06="$RUN_FROM/experiments/06-mvm-0a-constructed-self-index"
P_REHEARSAL_SRC="$RUN_FROM/experiments/rehearsal-successor-measure/src"

if [ "${1:-}" = "--help" ]; then sed -n '2,60p' "$0"; exit 0; fi

fail=0
ok()   { echo "  [ ok ] $*"; }
bad()  { echo "  [FAIL] $*"; fail=$((fail + 1)); }
warn() { echo "  [note] $*"; }

echo "staging the rented slice — NOTHING IS RENTED AND NOTHING IS SPENT"
echo

echo "local preconditions"
PY=""
for c in "$REPO/.venv/bin/python" "$HOME/Code/minimum-viable-mind/.venv/bin/python"; do
    [ -x "$c" ] && { PY="$c"; break; }
done
[ -n "$PY" ] && ok "interpreter: $PY" || bad "no interpreter found"

for m in grammar arms transplant measure; do
    if [ -n "$PY" ] && (cd "$REHEARSAL_SRC" && "$PY" "$m.py" --self-test >/dev/null 2>&1); then
        ok "$m self-test passes"
    else
        bad "$m self-test does not pass — the payload is not fit to push"
    fi
done

if [ -x "$EXP06/src/launch_a3_fetch_first.sh" ]; then
    ok "the derived launcher is present (registered launcher untouched)"
else
    bad "the derived launcher launch_a3_fetch_first.sh is missing"
fi
if [ -x "$EXP06/src/machine_deadline.sh" ]; then
    ok "the laptop's machine deadline is present"
else
    bad "machine_deadline.sh is missing -- the hard cap would not be enforced"
fi
if [ -x "$EXP06/src/reap_agent.sh" ]; then
    ok "the machine's own shutdown watcher is present"
else
    bad "reap_agent.sh is missing"
fi
if [ -n "$PY" ] && sh -n "$EXP06/src/reap_agent.sh" 2>/dev/null; then
    ok "the shutdown watcher parses"
fi

# The credential the whole machine-side delete depends on. Its ABSENCE is not
# a failure of this staging — it is the thing the slice exists to test — but
# the operator has to know which of the two paths the slice will take.
KEYF="$HOME/.runpod/reaper-key"
if [ -s "$KEYF" ]; then
    MODE=$(stat -f '%Lp' "$KEYF" 2>/dev/null || stat -c '%a' "$KEYF" 2>/dev/null)
    if [ "$MODE" = "600" ]; then
        ok "a dedicated reaper key is present and is mode 600"
    else
        warn "the reaper key is mode $MODE, not 600 — by John's ruling of"
        warn "2026-09-16 the launcher will refuse to arm the machine's own"
        warn "watcher, and the slice would test the laptop-only path instead"
    fi
else
    warn "no dedicated reaper key at $KEYF — the machine's own watcher will"
    warn "NOT be armed, and the slice would test only the laptop-only path."
    warn "Arming it is John's call, not this script's."
fi

# John's ruling of 2026-09-22 [RT-198]: until the Gate A amendment clears, no
# session invokes a registered launcher with any argument, AND THE PRE-FLIGHT
# ASSERTS IT. A prohibition nobody checks is the warning-in-a-document that
# ruling rejected. The check creates nothing and never runs the registered
# launcher.
GUARDCHK="$EXP06/src/check_launcher_argument_guard.sh"
if [ -x "$GUARDCHK" ]; then
    if GUARDOUT=$("$GUARDCHK" 2>&1); then
        ok "launchers refuse arguments (RT-198 check passes)"
        if printf '%s' "$GUARDOUT" | grep -q 'does NOT carry the guard'; then
            warn "launch_a3.sh is registered and still unguarded: pass it NO"
            warn "arguments until the Gate A amendment clears."
        fi
    else
        bad "the RT-198 argument-guard check FAILED — a launcher does not"
        bad "refuse arguments. Run $GUARDCHK to see which."
    fi
else
    bad "the RT-198 argument-guard check is missing at $GUARDCHK"
fi

# 2026-09-25: the check for failure 6 of docs/known-failure-modes.md. Every
# background start the launcher sends over ssh is run against a real local
# shell; one that would hold the connection with no cap fails the staging.
FORMCHK="$EXP06/src/check_remote_forms.py"
if [ -n "$PY" ] && [ -f "$FORMCHK" ]; then
    if "$PY" "$FORMCHK" >/dev/null 2>&1; then
        ok "no remote background start can hold the launcher (check_remote_forms.py passes)"
    else
        bad "a remote background start can hold the launcher open. Run $FORMCHK to see which."
    fi
else
    bad "the remote-forms check is missing at $FORMCHK, or there is no interpreter"
fi

if command -v runpodctl >/dev/null 2>&1; then
    ok "runpodctl is on the path: $(command -v runpodctl)"
else
    warn "runpodctl is not on the path here"
fi

echo
echo "the plan"
mkdir -p "$REHEARSAL_DIR/out"
cat > "$PLAN" <<PLANEOF
THE RENTED SLICE — STAGED, NOT RUN
==================================
Written by stage_rented_slice.sh. Nothing in this plan has been executed.
It needs John's spoken go naming this run. That go has not been given.

WHAT IT IS
  One rented machine, one short session, answering two questions:
    1. seconds per step for the three successor architectures at the
       registered shape, on the rented graphics card (rehearsal item R-7);
    2. whether the shutdown handshake that landed as pull request 15 works
       against the real vendor, end to end.

THE COMMANDS, IN ORDER

  Step 0 — prove the plan with no machine and no money. This step USED to
  open with \`launch_a3_fetch_first.sh --help\`, which was withdrawn by John on
  2026-09-22 [RT-198]: the launcher had no --help and no argument handling at
  all, so the flag was silently ignored and the script went on to a REAL
  launch at its defaults. It created a rented machine on 2026-09-21. The dry
  run below is the genuinely inert path — its guard exits before anything is
  created — and the launchers now refuse any argument outright.
    DRYRUN=1 SCALE=$SLICE_SCALE MAXTOK=$SLICE_TOKENS OUT=$SLICE_OUT \\
      GRACE_S=$SLICE_GRACE_S RUN_SUBDIR=$SLICE_OUT CLEAR_RUN_SUBDIR=1 \\
      HARD_CAP_USD=$HARD_CAP RATE_PER_HOUR_USD=$RATE_PER_HOUR \\
      PRE_TRAIN_DIR=$P_REHEARSAL_SRC \\
      PRE_TRAIN_CMD="$BENCH_CMD" \\
      $P_EXP06/src/launch_a3_fetch_first.sh
  Before going on, the dry run must print "run dir: $SLICE_RUN_DIR"
  and a "before training" block naming bench_arms.py. If it prints the
  shared folder /workspace/mvm-out instead, stop: the final copy would
  bring home every earlier run's model files as well.
  It must also print these two, added 2026-09-25 after the first attempt
  hung; if either is missing, stop:
    "machine deadline: ON -- hard cap \$$HARD_CAP at \$$RATE_PER_HOUR an hour"
        and "deletes the machine ${DEADLINE_SECS}s after creation"
    "clear the run folder, before the shutdown watcher starts"
        naming $SLICE_RUN_DIR

  Step 1 — the toy run, through the DERIVED launcher (the registered
  launcher launch_a3.sh is not used and not edited):
    SCALE=$SLICE_SCALE MAXTOK=$SLICE_TOKENS OUT=$SLICE_OUT \\
      GRACE_S=$SLICE_GRACE_S RUN_SUBDIR=$SLICE_OUT CLEAR_RUN_SUBDIR=1 \\
      HARD_CAP_USD=$HARD_CAP RATE_PER_HOUR_USD=$RATE_PER_HOUR \\
      PRE_TRAIN_DIR=$P_REHEARSAL_SRC \\
      PRE_TRAIN_CMD="$BENCH_CMD" \\
      $P_EXP06/src/launch_a3_fetch_first.sh
  This one command also does the timing (step 2). There is nothing to type
  on the machine.
  Straight after "pod:" it must print "MACHINE DEADLINE ARMED", with the
  time this laptop will delete the machine: ${DEADLINE_HM} (${DEADLINE_SECS}s)
  after creation, which is the hard cap of \$$HARD_CAP at \$$RATE_PER_HOUR an
  hour. If it does not, delete the machine at once
  (runpodctl pod delete <id>) and stop: the cap is not enforced.

  Step 1a — the pre-flight clear, done by the launcher inside step 1,
  BEFORE the machine's shutdown watcher starts. The first attempt, on
  2026-09-25, left $SLICE_RUN_DIR holding one file,
  reaper.log (docs/2026-09-25-rented-slice-findings.md, section 6), read
  on the machine 33 seconds before it was deleted. The volume cannot be
  read from this laptop, so this is the first moment it can be checked.
  The launcher lists the folder, names any "LEFTOVER:" finished-marker
  ($SLICE_OUT.DONE), receipt ($SLICE_OUT.FETCHED), model file or timing
  file, and then empties it. A leftover marker would otherwise let the
  watcher delete the machine before training. Look for:
    "clearing the run folder before anything on the machine starts"
    "files left after clearing: 0"
  Any "LEFTOVER:" line is a finding to record, not a reason to stop: the
  clear has already removed it.

  Step 2 — the timing, done by the launcher inside step 1. After the
  machine is up and its shutdown path is settled, and BEFORE training
  starts, the launcher pushes the timing script and runs it, waiting for
  it to finish. Training writes the finished-marker that every deletion
  waits for, so the timing is done before the machine can be deleted, and
  it has the graphics card to itself. The timing file is rewritten after
  each architecture, so a cut-short run still leaves what it measured.
  It lands in the slice's own folder, $SLICE_RUN_DIR,
  and the laptop's final copy brings that folder home and nothing else.
  (Section 3 of the staging document had the timing run WHILE the toy run
  trained. That is changed here: on a toy run that finishes in minutes,
  the machine could be deleted before the timing file existed, and the
  figures would be taken on a card busy with training.)
  Look for, in the launcher's output:
    "wrote $SLICE_RUN_DIR/bench_arms.json (3 of 3 architectures)"
    "before-training step finished (exit 0)"

  Step 3 — FIRST, read which shutdown path the launcher armed. It says so
  after "ssh up:" and before training starts. Since 2026-09-25 the command
  that starts the machine's watcher cannot hold the launcher: it returns at
  once, and is cut off at 60 seconds if it does not. A silence of more than
  a couple of minutes after "VERIFIED" is therefore a difference from the
  plan: stop and delete.
    "shutdown watcher RUNNING on the machine"  — the handshake is being
        tested; go on to the three signals below.
    "SHUTDOWN WATCHER DID NOT START" or "REAP: pod-side reaping NOT armed"
        — the handshake is NOT being tested, whatever follows. The run can
        look entirely normal. Record the NOT TESTED outcome below.
  Then watch for the three handshake signals, in this order.

WHAT PASSING LOOKS LIKE, WRITTEN DOWN BEFORE IT RUNS

  Throughput:
    PASS  three seconds-per-step figures, one per architecture, with the
          spread over the timed steps, written to bench_arms.json with
          "complete": true, and fetched home by the laptop's final copy to
          $P_EXP06/artifacts/$SLICE_OUT/bench_arms.json.
          A file with "complete": false was cut short; its figures stand
          only for the architectures it lists.
    FAIL  any architecture will not run at the registered shape on the
          rented hardware — for instance it runs out of memory. That is a
          finding about the design, not about the machine.
    NO VERDICT  the machine is unavailable, or it bills at the anomalous
          rate of the 2026-08-08 row. Stop condition S9: the wave halts and
          the billed row goes to John beside the estimate.

  The shutdown handshake — the fix author's own signals:
    PASS  "receipt written on the machine" in the laptop's log, then
          "receipt found" in the machine's log, then a deletion within
          seconds of it, in that order; and the copied model file matches
          the one on the machine by checksum.
    FAIL (bounded-wait path)  the machine's log says "grace ran out". The
          receipt path did not work and only the bounded wait ended the
          billing. The run is unsafe to leave unattended until that is
          understood, and the registration cannot lean on the handshake.
    FAIL (credential path)  the machine cannot delete itself even after the
          bounded wait. That is the 2026-09-16 measurement repeating, and it
          means the laptop is still the only reap.
    NOT TESTED  the quiet one (staging document, section 6). The machine's
          own watcher never started: the launcher printed "SHUTDOWN WATCHER
          DID NOT START" or "REAP: pod-side reaping NOT armed", then fell
          back to "SHUTDOWN ORDER: the trainer deletes the machine itself"
          (or "LAPTOP ONLY"). Everything can look normal while the handshake
          was never exercised. Record it as not tested, never as a pass.
    NO VERDICT  the slice does not run. Then the handshake is exercised
          against local stand-ins only, and the registration says so in its
          own text.
    CUT OFF BY THE CAP  (added 2026-09-25) the laptop's machine deadline
          deleted the machine: its log, machine-deadline.log beside the
          run's files, says "DEADLINE REACHED". Whatever the handshake had
          reached by then is reported as far as it got, and the handshake
          is NOT a pass: the thing that ended the billing was the cap.

WHAT IT COSTS
  A toy run at $SLICE_TOKENS tokens finishes in a few minutes; timing 50
  steps on three architectures takes a few more; the bounded wait is set to
  $SLICE_GRACE_S seconds and should not be reached at all on the passing
  path. The final copy takes only the slice's own folder, not the shared
  one (2.5 GB on each of the last two A3 copies). Well under an hour of
  rented time at \$$RATE_PER_HOUR an hour.
    estimate   about \$0.75 to \$1.00
    hard cap   \$$HARD_CAP, ENFORCED BY CODE since 2026-09-25: this laptop
               deletes the machine ${DEADLINE_HM} after creation
               (\$$HARD_CAP / \$$RATE_PER_HOUR an hour = ${DEADLINE_SECS}s),
               whatever the run is doing, and sooner if the vendor's
               creation record states a higher rate. The first attempt had
               no such deadline, and unattended would have billed until the
               machine's own +24h deadline, about \$24.
               The deadline keeps this laptop's clock, so the laptop must
               stay awake and on the network until then, as it already
               must for the watchdog. Billing between the deadline and the
               vendor acting on the delete is not covered (seconds).
  The precedent for a short deliberately-capped test is the self-delete test
  of 2026-09-16, authorised at a \$0.50 cap and billed at \$0.29. This sits
  inside the first release of money John authorised on 2026-09-21, whose
  rehearsal line is up to \$10.

WHAT IS OWED BEFORE IT RUNS
  - John's spoken go naming this run, per commitment C2(b). The go of
    2026-09-25 named one run of the plan at commit 4d98cfc; that run
    happened and was stopped when the launcher hung
    (docs/2026-09-25-rented-slice-findings.md), so a fresh go names this
    plan and the fixed launcher.
  - A decision on the dedicated reaper key: without it the machine's own
    watcher is not armed and only the laptop-only path is tested, which is
    the smaller half of what the slice is for.
  - A ledger row written BEFORE the spend, quoting the go, per the ledger's
    own rule 2.

WHAT IS LEFT BEHIND
  The slice's folder, $SLICE_RUN_DIR, stays on the shared
  volume. The registered launcher's final copy takes the whole shared
  folder, subfolders included, so later registered runs will carry it home
  (its model file should be roughly 120 MB, going by the 30M files' size
  per parameter; not measured) unless it is removed from the volume first.
PLANEOF
sed 's/^/  /' "$PLAN"
echo
echo "  wrote $PLAN"
echo
if [ "$fail" -gt 0 ]; then
    echo "$fail precondition(s) failed — the slice is NOT ready to be asked for"
    exit 1
fi
echo "preconditions pass. THE SLICE IS STAGED AND HAS NOT BEEN RUN."
echo "It needs John's spoken go naming the run. This script cannot rent"
echo "anything: it contains no command that creates a machine."
