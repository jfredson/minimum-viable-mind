#!/bin/bash
# Failures 5 and 6 of docs/known-failure-modes.md, run by the Gate A tier 1
# reviewer of version 5 (2026-10-08). Runs the list's own two tests and the
# successor launcher's test T7, each with a stand-in `runpodctl` first on
# PATH that records any call and exits 99, so that even a broken guard could
# not reach the vendor. Creates nothing, spends nothing. Writes its outputs
# beside itself.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../../.." && pwd)"
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
STUB=$(mktemp -d); trap 'rm -rf "$STUB"' EXIT
printf '#!/bin/sh\necho "STAND-IN runpodctl CALLED: $*" >> "%s/called"; exit 99\n' "$STUB" > "$STUB/runpodctl"
chmod +x "$STUB/runpodctl"
export PATH="$STUB:$PATH"
OPS="$ROOT/experiments/06-mvm-0a-constructed-self-index/src"

"$OPS/check_launcher_argument_guard.sh" > "$HERE/failure5_launcher_guard.out.txt" 2>&1
echo "failure 5, check_launcher_argument_guard.sh: exit $?"
"$PY" "$OPS/check_remote_forms.py" > "$HERE/failure6_remote_forms_parent.out.txt" 2>&1
echo "failure 6, check_remote_forms.py on launch_a3_fetch_first.sh: exit $?"
LAUNCHER="$ROOT/experiments/08-successor-degree/src/launch_successor.sh" "$PY" "$OPS/check_remote_forms.py" \
  > "$HERE/failure6_remote_forms_successor.out.txt" 2>&1
echo "failure 6, check_remote_forms.py on launch_successor.sh: exit $?"
PY="$PY" "$ROOT/experiments/08-successor-degree/tests/check_launcher.sh" > "$HERE/t7_check_launcher.out.txt" 2>&1
echo "test T7 on launch_successor.sh: exit $?"
if [ -f "$STUB/called" ]; then
  echo "the stand-in vendor tool WAS called:"; cat "$STUB/called"
else
  echo "the stand-in vendor tool was never called"
fi
