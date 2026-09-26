#!/bin/bash
# Run the four launcher self-tests at 8aaf6e4 with a blocking runpodctl first
# on the command path: any call that gets past a test's own stand-ins is
# recorded and refused (exit 97), never sent to the vendor.
J=/Users/john/.claude/jobs/1a8d030f/tmp
B=$J/block
mkdir -p "$B"
printf '#!/bin/bash\necho "$(date +%%s) BLOCKED: runpodctl $*" >> %s/calls\nexit 97\n' "$B" > "$B/runpodctl"
chmod +x "$B/runpodctl"
rm -f "$B/calls"
cd "$J/fix/experiments/06-mvm-0a-constructed-self-index/src" || exit 1
date -u +%FT%TZ
for t in check_launcher_argument_guard.sh launch_gate_selftest.sh sleep_guard_selftest.sh reap_handshake_selftest.sh; do
  PATH="$B:$PATH" "./$t" > "$J/st-$t.out" 2>&1
  echo "$t exit=$?"
  tail -3 "$J/st-$t.out" | sed 's/\x1b\[[0-9;]*m//g'
done
echo "calls that reached the blocking runpodctl: $(cat "$B/calls" 2>/dev/null | wc -l)"
