#!/bin/sh
# Every self-test of the frozen successor code, in one command (test T1 of
# docs/successor-code-freeze-method-2026-10-04.md). Laptop, $0. Exits non-zero
# if any self-test fails.
cd "$(dirname "$0")" || exit 1
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
st=0
log=$(mktemp)
for m in grammar models transplant measure procedure train_successor tripwire; do
  echo "== $m"
  if "$PY" "$m.py" --self-test > "$log" 2>&1; then :; else st=1; echo "   $m FAILED"; fi
  grep -v '^{"step\|^recipe\|^saved \|^TRAINING COMPLETE\|^resumed from\|^TRIPWIRE\|^TRIPPED\|^HALT, NOT\|^then tell\|^Nothing launches\|^=====\|^tripwire' "$log"
done
rm -f "$log"
[ $st = 0 ] && echo "ALL SELF-TESTS PASS" || echo "A SELF-TEST FAILED"
exit $st
