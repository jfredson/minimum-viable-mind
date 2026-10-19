#!/bin/sh
# Item 2: the real run refuses without its three settings, refuses a bad ceiling, and refuses any argument.
# Run from the worktree root. Every case runs with networking blocked (run_blocked.py), and no case sets all three.
PY=/Users/john/Code/minimum-viable-mind/.venv/bin/python
R=docs/filtered-battery-2026-10-07/run_farend_repair_step1.py
B=docs/reviews/2026-10-19-farend-repair-step1-check-claude-code-scripts/run_blocked.py
E0="env -i HOME=$HOME PATH=/usr/bin:/bin"
case_() { echo "-- $1"; shift; $E0 "$@" 2>&1 | sed 's/^/  /'; }
case_ "MVM_REPAIR1_RUN=1, nothing else" MVM_REPAIR1_RUN=1 $PY $B $R
case_ "MVM_REPAIR1_RUN=1, no MVM_GO_QUOTE" MVM_REPAIR1_RUN=1 MVM_WORKLOG_ROW=x MVM_CEILING=5 $PY $B $R
case_ "MVM_REPAIR1_RUN=1, no MVM_WORKLOG_ROW" MVM_REPAIR1_RUN=1 MVM_GO_QUOTE=x MVM_CEILING=5 $PY $B $R
case_ "MVM_REPAIR1_RUN=1, no MVM_CEILING" MVM_REPAIR1_RUN=1 MVM_GO_QUOTE=x MVM_WORKLOG_ROW=x $PY $B $R
case_ "MVM_REPAIR1_RUN=1, MVM_GO_QUOTE only spaces" MVM_REPAIR1_RUN=1 "MVM_GO_QUOTE=   " MVM_WORKLOG_ROW=x MVM_CEILING=5 $PY $B $R
for c in 0 -1 11 abc; do case_ "MVM_REPAIR1_RUN=1, MVM_CEILING=$c" MVM_REPAIR1_RUN=1 MVM_GO_QUOTE=x MVM_WORKLOG_ROW=x MVM_CEILING=$c $PY $B $R; done
case_ "one argument, dry-run mode" $PY $B $R --dry-run
case_ "one argument, real-run mode with nothing set" MVM_REPAIR1_RUN=1 $PY $B $R go
