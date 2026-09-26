#!/bin/bash
# Failure paths of machine_deadline.sh at 8aaf6e4, behind a stand-in runpodctl.
# Nothing is rented; no vendor is contacted (the stand-in is first on PATH and
# RUNPODCTL points at it explicitly).
set -uo pipefail
MD=/Users/john/.claude/jobs/1a8d030f/tmp/fix/experiments/06-mvm-0a-constructed-self-index/src/machine_deadline.sh
T=$(mktemp -d); T=$(cd "$T" && pwd -P)
mkdir -p "$T/bin"
env_file() {  # $1 seconds from now
  local now; now=$(date +%s)
  printf 'POD="fakepod"\nOUT="t"\nCREATED_AT_EPOCH=%s\nDELETE_AT_EPOCH=%s\nHARD_CAP_USD="0.0011"\nRATE_PER_HOUR_USD="0.99"\nPOSTED_RATE="0.99"\nPOLL_S=1\n' "$now" $(( now + $1 )) > "$T/e.env"
}
fake() {  # $1 = body of the stand-in's "pod delete" branch
  cat > "$T/bin/runpodctl" <<EOF
#!/bin/bash
echo "\$(date +%s) \$*" >> "$T/calls"
case "\$1 \$2" in "pod delete") $1 ;; esac
EOF
  chmod +x "$T/bin/runpodctl"; rm -f "$T/calls" "$T/n"
}
run() { PATH="$T/bin:/usr/bin:/bin" RUNPODCTL="$T/bin/runpodctl" "$@"; }

echo "=== A. the vendor tool errors on every call (network down, key revoked)"
fake 'echo "Error: request failed" >&2; exit 1'
env_file 1; S=$(date +%s)
run bash "$MD" "$T/e.env" 2>&1 | sed 's/^/  | /'; echo "  exit=${PIPESTATUS[0]} after $(( $(date +%s)-S ))s; delete calls: $(grep -c delete "$T/calls")"

echo "=== B. the vendor tool fails twice, then succeeds (network back after ~40s)"
fake 'n=$(cat '"$T"'/n 2>/dev/null || echo 0); n=$((n+1)); echo $n > '"$T"'/n; [ $n -ge 3 ] && echo deleted || { echo "Error" >&2; exit 1; }'
env_file 1; S=$(date +%s)
run bash "$MD" "$T/e.env" 2>&1 | grep -E 'attempt|DELETED|FAILED' | sed 's/^/  | /'; echo "  after $(( $(date +%s)-S ))s"

echo "=== C. the vendor tool hangs on delete (watched for 20s)"
fake 'exec sleep 3600'
env_file 1
run bash "$MD" "$T/e.env" > "$T/c.log" 2>&1 &
P=$!; sleep 20
kill -0 $P 2>/dev/null && echo "  still waiting on attempt 1 after 20s (no time limit on the delete call)" || echo "  finished"
sed 's/^/  | /' "$T/c.log"
pkill -P $P 2>/dev/null; kill $P 2>/dev/null; pkill -f "$T/bin/runpodctl" 2>/dev/null

echo "=== D. the vendor tool exits 0 but says it did not delete (answer not checked)"
fake 'echo "{\"error\": \"pod not found\"}"; exit 0'
env_file 1
run bash "$MD" "$T/e.env" 2>&1 | grep -E 'attempt|DELETED|FAILED' | sed 's/^/  | /'

echo "=== E. signals to the launcher's whole process group, spawned exactly as the launcher does"
fake 'echo deleted'
for SIG in INT TERM HUP; do
  env_file 4; rm -f "$T/calls"
  cat > "$T/parent.sh" <<EOF
#!/bin/bash
nohup /usr/bin/caffeinate -dimsu bash "$MD" "$T/e.env" >> "$T/d.log" 2>&1 < /dev/null &
sleep 30
EOF
  python3 - "$T" "$SIG" <<'PY'
import os, signal, subprocess, sys, time
T, sig = sys.argv[1], sys.argv[2]
env = dict(os.environ, PATH=f"{T}/bin:/usr/bin:/bin", RUNPODCTL=f"{T}/bin/runpodctl")
p = subprocess.Popen(["bash", f"{T}/parent.sh"], start_new_session=True, env=env)
time.sleep(1)
os.killpg(p.pid, getattr(signal, "SIG" + sig))
p.wait()
PY
  sleep 6
  echo "  SIG$SIG to the group: delete calls after the deadline: $(grep -c delete "$T/calls" 2>/dev/null || echo 0)"
done
rm -rf "$T"
