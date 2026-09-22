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

  Step 0 — prove the plan with no machine and no money:
    $EXP06/src/launch_a3_fetch_first.sh --help >/dev/null
    DRYRUN=1 SCALE=$SLICE_SCALE MAXTOK=$SLICE_TOKENS OUT=$SLICE_OUT \\
      GRACE_S=$SLICE_GRACE_S \\
      $EXP06/src/launch_a3_fetch_first.sh

  Step 1 — the toy run, through the DERIVED launcher (the registered
  launcher launch_a3.sh is not used and not edited):
    SCALE=$SLICE_SCALE MAXTOK=$SLICE_TOKENS OUT=$SLICE_OUT \\
      GRACE_S=$SLICE_GRACE_S \\
      $EXP06/src/launch_a3_fetch_first.sh

  Step 2 — while that run is training, time the three architectures on the
  same machine and write the result where the laptop's final copy will
  bring it home:
    tar czf - -C $REHEARSAL_DIR src | \\
      \$SSH "mkdir -p /root/rehearsal && tar xzf - -C /root/rehearsal"
    \$SSH "cd /root/rehearsal/src && python bench_arms.py --device cuda \\
             --steps $BENCH_STEPS --batch 32 \\
             --out /workspace/mvm-out/bench_arms.json"
  (\$SSH is the handle the launcher prints as "ssh up:".)

  Step 3 — watch for the three signals, in this order, and nothing else.

WHAT PASSING LOOKS LIKE, WRITTEN DOWN BEFORE IT RUNS

  Throughput:
    PASS  three seconds-per-step figures, one per architecture, with the
          spread over the timed steps, written to bench_arms.json and
          fetched home by the laptop's final copy.
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
    NO VERDICT  the slice does not run. Then the handshake is exercised
          against local stand-ins only, and the registration says so in its
          own text.

WHAT IT COSTS
  A toy run at $SLICE_TOKENS tokens finishes in a few minutes; timing 50
  steps on three architectures takes a few more; the bounded wait is set to
  $SLICE_GRACE_S seconds and should not be reached at all on the passing
  path. Well under an hour of rented time at \$$RATE_PER_HOUR an hour.
    estimate   about \$0.75 to \$1.00
    hard cap   \$$HARD_CAP
  The precedent for a short deliberately-capped test is the self-delete test
  of 2026-09-16, authorised at a \$0.50 cap and billed at \$0.29. This sits
  inside the first release of money John authorised on 2026-09-21, whose
  rehearsal line is up to \$10.

WHAT IS OWED BEFORE IT RUNS
  - John's spoken go naming this run, per commitment C2(b).
  - A decision on the dedicated reaper key: without it the machine's own
    watcher is not armed and only the laptop-only path is tested, which is
    the smaller half of what the slice is for.
  - A ledger row written BEFORE the spend, quoting the go, per the ledger's
    own rule 2.
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
