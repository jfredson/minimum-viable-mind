#!/bin/sh
# Run every module self-test and write the output where the findings can
# quote it. Local, free, nothing rented.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="${PY:-$HERE/../../../.venv/bin/python}"
[ -x "$PY" ] || PY="$HOME/Code/minimum-viable-mind/.venv/bin/python"
OUT="$HERE/../out/self-tests.txt"
: > "$OUT"
for m in grammar arms transplant measure; do
    echo "=== $m.py --self-test ===" >> "$OUT"
    "$PY" "$HERE/$m.py" --self-test 2>&1 \
      | grep -v -i "userwarning\|consider using\|^  log(f" >> "$OUT"
    echo >> "$OUT"
done
echo "passes: $(grep -c 'PASS' "$OUT")   failures: $(grep -c 'FAIL' "$OUT")"
echo "wrote $OUT"
