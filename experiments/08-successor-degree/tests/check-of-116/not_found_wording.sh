#!/bin/bash
# Independent check of pull request 116: answers that contain "not found" but
# do NOT mean "this machine does not exist", fed to the laptop deadline timer
# through a stand-in vendor tool. $0: nothing rented, the vendor never called.
#
# Each wording below is one the vendor tool 2.6.1 (installed on this laptop,
# public source github.com/runpod/runpodctl, tag v2.6.1) or the shell can
# actually produce:
#   * internal/api/client.go wraps EVERY non-2xx answer as
#     "api error: <body> (status N)"; a wrong address or a gateway in front of
#     the service answers 404 with a body like "404 page not found";
#   * the shell itself prints "runpodctl: command not found" when the tool is
#     not on the timer's command path;
#   * the recorded answer to a delete of a machine already gone (2026-09-26):
#     {"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404} (status 404)"}
#
#   bash tests/check-of-116/not_found_wording.sh   (from experiments/08-successor-degree)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MD="$HERE/../../../06-mvm-0a-constructed-self-index/src/machine_deadline.sh"
run_case() {   # $1 label, $2 the stand-in's answer to "pod get" ("" = leave the tool off the path)
  local T; T=$(mktemp -d)
  mkdir -p "$T/bin"
  if [ -n "$2" ]; then
    cat > "$T/bin/runpodctl" <<EOF
#!/bin/bash
echo "\$*" >> "$T/calls"
case "\$1 \$2" in
  "pod get") printf '%s\n' '$2'; exit 1 ;;
  "pod delete") echo deleted; exit 0 ;;
esac
exit 2
EOF
    chmod +x "$T/bin/runpodctl"
  fi
  local now; now=$(date +%s)
  cat > "$T/machine_deadline_fakepod.env" <<EOF
POD="fakepod"
OUT="t"
CREATED_AT_EPOCH=$now
DELETE_AT_EPOCH=$((now + 6))
HARD_CAP_USD="0.0016"
RATE_PER_HOUR_USD="0.99"
POSTED_RATE="0.99"
POLL_S=1
VENDOR_CHECK_S=1
VENDOR_CAP_S=3
EOF
  PATH="$T/bin:/usr/bin:/bin" bash "$MD" "$T/machine_deadline_fakepod.env" > "$T/log" 2>&1
  if grep -q "STANDING DOWN" "$T/log"; then
    echo "  STANDS DOWN (timer disarmed, nothing deleted): $1"
  else
    echo "  stays armed: $1"
  fi
  grep -m1 "STANDING DOWN" "$T/log" | sed 's/^/      /' | cut -c1-200
  rm -rf "$T"
}
echo "The deadline timer, given answers that do not mean 'the machine does not exist':"
run_case "a gateway or wrong address answers 404" 'Error: api error: 404 page not found (status 404)'
run_case "the vendor tool is not on the timer's command path" ''
run_case "a viper-style config message (in the 2.6.1 binary's text)" 'Config File "config" Not Found in "[/Users/x/.runpod]"'
echo "For comparison, the answers that do mean it:"
run_case "the recorded 2026-09-26 wording (to a delete)" '{"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404} (status 404)"}'
run_case "a failed request (network down), recorded form" 'Error: request failed'
