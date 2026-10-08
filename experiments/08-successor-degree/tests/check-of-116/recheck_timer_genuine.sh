#!/bin/bash
# Re-check (second round): the deadline timer with the vendor's genuine wording
# and a machine list. $0; a stand-in vendor tool, never the vendor.
#   bash tests/check-of-116/recheck_timer_genuine.sh   (from experiments/08-successor-degree)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MD="$HERE/../../../06-mvm-0a-constructed-self-index/src/machine_deadline.sh"
GENUINE='{"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404} (status 404)"}'
case_() {  # $1 label, $2 pod get answer, $3 pod list answer (exit 0), $4 seconds to deadline
  local T; T=$(mktemp -d); mkdir -p "$T/bin"
  cat > "$T/bin/runpodctl" <<EOS
#!/bin/bash
echo "\$*" >> "$T/calls"
case "\$1 \$2" in
  "pod get") printf '%s\n' '$2'; exit 1 ;;
  "pod list") printf '%s\n' '$3'; exit 0 ;;
  "pod delete") echo deleted; exit 0 ;;
esac
exit 2
EOS
  chmod +x "$T/bin/runpodctl"
  local now; now=$(date +%s)
  printf 'POD="fakepod"\nOUT="t"\nCREATED_AT_EPOCH=%s\nDELETE_AT_EPOCH=%s\nHARD_CAP_USD="1"\nRATE_PER_HOUR_USD="0.99"\nPOSTED_RATE="0.99"\nPOLL_S=1\nVENDOR_CHECK_S=1\nVENDOR_CAP_S=3\n' "$now" "$((now + $4))" > "$T/m.env"
  PATH="$T/bin:/usr/bin:/bin" bash "$MD" "$T/m.env" > "$T/log" 2>&1
  if grep -q "STANDING DOWN" "$T/log"; then r="STANDS DOWN"; else r="stays armed"; fi
  echo "  $r; delete called: $(cat "$T/calls" 2>/dev/null | grep -c 'pod delete'): $1"
  rm -rf "$T"
}
echo "Deadline timer, second round:"
case_ "genuine wording, good empty list, time for two checks" "$GENUINE" "[]" 20
case_ "genuine wording, the list still shows the machine" "$GENUINE" '[{"id":"fakepod"}]' 6
case_ "404 page wording, good empty list" 'Error: api error: 404 page not found (status 404)' '[]' 6
case_ "'pod not found' without '(status 404)', good empty list" '{"error":"pod not found"}' '[]' 6
case_ "genuine wording, list answers not-a-list" "$GENUINE" '{"error":"x"}' 6
