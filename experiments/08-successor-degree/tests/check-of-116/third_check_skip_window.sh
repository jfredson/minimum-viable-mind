#!/bin/bash
# Third check: can the timer's vendor check still delay its delete past the
# deadline? A stand-in vendor whose reads hang; the delete is timestamped by
# the stand-in. $0. The sleep after a check uses the time left as it was
# BEFORE the check, so a long check followed by a long poll can overshoot.
#   bash tests/check-of-116/third_check_skip_window.sh   (from experiments/08-successor-degree)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MD="$HERE/../../../06-mvm-0a-constructed-self-index/src/machine_deadline.sh"
run() {  # $1 cap, $2 poll, $3 seconds to deadline
  local T; T=$(mktemp -d); mkdir -p "$T/bin"
  cat > "$T/bin/runpodctl" <<EOS
#!/bin/bash
echo "\$(date +%s) \$*" >> "$T/calls"
case "\$1 \$2" in
  "pod delete") echo deleted; exit 0 ;;
  *) exec sleep 3600 ;;
esac
EOS
  chmod +x "$T/bin/runpodctl"
  local now; now=$(date +%s)
  printf 'POD="fakepod"\nOUT="t"\nCREATED_AT_EPOCH=%s\nDELETE_AT_EPOCH=%s\nHARD_CAP_USD="1"\nRATE_PER_HOUR_USD="0.99"\nPOSTED_RATE="0.99"\nPOLL_S=%s\nVENDOR_CHECK_S=1\nVENDOR_CAP_S=%s\n' "$now" "$((now + $3))" "$2" "$1" > "$T/m.env"
  PATH="$T/bin:/usr/bin:/bin" bash "$MD" "$T/m.env" > "$T/log" 2>&1
  local del; del=$(grep "pod delete" "$T/calls" | head -1 | cut -d' ' -f1)
  local reads; reads=$(grep -c "pod get" "$T/calls")
  echo "  cap ${1}s, poll ${2}s, deadline ${3}s: vendor reads $reads; delete issued $(( del - now - $3 ))s after the deadline"
  rm -rf "$T"
}
echo "Timer with every vendor read hanging (stand-in):"
run 3 10 20
run 3 10 25
run 5 20 40
