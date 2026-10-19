#!/usr/bin/env bash
# The dry run under the other Python interpreters on this Mac, for the check of
# pull request 174 (2026-10-17): experiment D's virtual environment (which the
# method names as one of the two interpreters to use) and the command-line
# tools' Python 3.9. The seeded draws are in the output (the gate samples, the
# bootstrap self-check), so a different sequence would show as a difference.
# Calls no model; bytecode writing off.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/dryrun_other_pythons.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}; mkdir -p "$SCR"
cd "$(dirname "$0")/../../.."
P=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
OUTF=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
for PY in /Users/john/Code/minimum-viable-mind/.venv/bin/python /Library/Developer/CommandLineTools/usr/bin/python3; do
  echo "## $($PY --version 2>&1) ($PY)"
  env -i HOME="$HOME" PATH="$PATH" PYTHONDONTWRITEBYTECODE=1 $PY $P > "$SCR/py.out" 2> "$SCR/py.err"; echo "exit $?"
  if cmp -s "$SCR/py.out" $OUTF; then echo "cmp: identical to the committed output"; else
    echo "differs from the committed output:"; diff "$SCR/py.out" $OUTF | head -8; tail -3 "$SCR/py.err"; fi
done
