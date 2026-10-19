#!/usr/bin/env bash
# Daily resume of the measurement rehearsal of battery entries 1 and 2
# (docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md), on John's
# ruling of 2026-10-18 about 20:00 Pacific, relayed by the fifth master session:
# finish a day at a time under the same go and ceilings ($50: entry 1 $27,
# entry 2 $23), restarting after each daily reset of Google's limit of 250
# requests a day to gemini-3.1-pro on the AI Studio key.
#
# This wrapper changes nothing in the runner. Each start is the committed
# runner with the same go, worklog row and ceilings; the runner resumes from
# its records and counts their cost toward the ceilings. It lives beside the
# rehearsal's outputs (gitignored) and logs here.
#
# Exit codes (the session that launched it is woken on exit):
#   0  both entries finished (entry2/analysis.json exists)
#   3  a ceiling stopped the run
#   10 the Google prepaid balance may not cover the next day: ask John to top up
#   11 Google refused payment (HTTP 402): ask John to top up
#   12 any other error: read the log
set -u
REPO=/Users/john/Code/minimum-viable-mind
ART=$REPO/artifacts/stage3
OUT=$ART/battery_rehearsal
LOG=$ART/battery_rehearsal_daily_resume.log
RUNNER=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
# John's reading in AI Studio, 2026-10-18 evening, after the first start had stopped (last record 19:05 Pacific)
BALANCE_READ=20.00
BALANCE_READ_AT="2026-10-18 19:30"
DAY_MAX=7.50     # 250 Gemini calls at no more than $0.03 each at the high-end thinking allowance
MARGIN=1.00

say() { echo "$(date '+%Y-%m-%d %H:%M:%S %Z') $*" >> "$LOG"; }

gemini_spent_since_reading() {   # high-end estimate of Gemini cost for records written after the reading
  cd "$REPO" && .venv/bin/python -I - "$OUT" "$BALANCE_READ_AT" <<'EOF'
import json, sys, pathlib, datetime, importlib.util
out, since = pathlib.Path(sys.argv[1]), datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d %H:%M").timestamp()
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("r", "docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
G = "gemini-3.1-pro-preview"; total = 0.0
for p in out.rglob("*.json"):
    if p.stat().st_mtime <= since or p.name in ("plan.json", "analysis.json", "gates.json") or p.name.startswith("gate_judge"):
        continue
    x = json.loads(p.read_text())
    if "calls" in x and "judge" in x:            # a judge record or a gate pair
        if x["judge"] == G:
            for s in x["calls"]:
                total += r.est_call(G, s["in"], r.tokens(s["out"]) + r.JUDGE_THINKING_ALLOWANCE[G])
    elif x.get("model") == G and "turns" in x:   # a subject record or an other-arm conversation
        ctx = len(x.get("system") or "")
        for t, reply in zip(x.get("user_turns", [x.get("user", "")]), x["turns"]):
            ctx += len(t)
            total += r.est_call(G, ctx, r.tokens(len(reply)) + r.THINKING_ALLOWANCE[G])
            ctx += len(reply)
print(f"{total:.2f}")
EOF
}

next_midnight_plus() {   # seconds until 00:05 Pacific
  local now tgt
  now=$(date +%s)
  tgt=$(date -j -v+1d -f "%Y-%m-%d %H:%M:%S" "$(date '+%Y-%m-%d') 00:05:00" +%s)
  echo $(( tgt - now ))
}

say "daily resume loop started"
first=1
while true; do
  if [ -f "$OUT/entry2/analysis.json" ]; then say "both entries finished"; exit 0; fi
  if [ $first -eq 1 ]; then s=$(next_midnight_plus); say "sleeping ${s}s until 00:05 Pacific"; sleep "$s"; first=0; fi
  spent=$(gemini_spent_since_reading)
  left=$(echo "$BALANCE_READ - $spent" | bc)
  say "Gemini high-end spend since the balance reading: \$$spent; estimated balance left: \$$left"
  if [ "$(echo "$left - $DAY_MAX < $MARGIN" | bc)" -eq 1 ]; then
    say "STOP: the estimated balance may not cover a day of Gemini calls; ask John to top up"; exit 10
  fi
  say "start"
  (cd "$REPO" && set -a && . ./.env && set +a && \
   MVM_REHEARSAL_RUN=1 \
   MVM_GO_QUOTE='"Go up to $50" (John, 2026-10-18, about 18:45 Pacific, relayed by the fifth master session for the tracker sites; the $50 split in proportion to the high-end estimates: entry 1 $27, entry 2 $23)' \
   MVM_WORKLOG_ROW=4110fb03-e24e-4e69-b37a-db5788f5b8ac MVM_CEILING_E1=27 MVM_CEILING_E2=23 MVM_ENTRY=both \
   .venv/bin/python -u "$RUNNER") >> "$LOG" 2>&1
  rc=$?
  say "runner exit $rc"
  if [ -f "$OUT/entry2/analysis.json" ]; then say "both entries finished"; exit 0; fi
  if [ $rc -eq 3 ]; then exit 3; fi
  last=$(tail -40 "$LOG")
  if echo "$last" | grep -q "402\|PAYMENT_REQUIRED\|prepay\|Prepay"; then say "Google refused payment"; exit 11; fi
  if echo "$last" | grep -q "RESOURCE_EXHAUSTED"; then
    if echo "$last" | grep -q "per_day\|PerDay"; then
      s=$(next_midnight_plus)
      # if the daily limit is still in force soon after midnight, try again hourly
      if [ "$s" -gt 82800 ]; then s=3600; fi
      say "daily Gemini limit reached; sleeping ${s}s"; sleep "$s"; continue
    fi
    say "per-minute limit; sleeping 300s"; sleep 300; continue
  fi
  say "unexpected exit; stopping for a look"; exit 12
done
