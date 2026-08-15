#!/bin/bash
# run_post_pilot.sh — staged post-run pipeline for the 30M A1 pilot.
# Runs entirely locally against the watchdog-fetched artifacts ($0):
#   1. verify completion (DONE sentinel + checkpoint) and record md5
#   2. trajectory summary vs the two pre-stated signatures
#      (pilot-a1-findings.md: H_scale = T_si (and plausibly T_sr_rev) to
#      ceiling; H_shortcut-starvation = instant T_sr, flat T_si, floor
#      T_sr_rev) — mechanical readout; the verdict is adjudicated, not
#      auto-emitted (the 10M precedent: 0.96 was not gamed into a pass)
#   3. gate run (iii) against this checkpoint (required at the registered
#      scale before any 5-seed spend)
set -euo pipefail

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
EXP_DIR="$(cd "$SRC_DIR/.." && pwd)"
OUT="${OUT:-pilot_a1_30m_seed0}"
DEST="$EXP_DIR/artifacts/$OUT"
PY="$EXP_DIR/../../.venv/bin/python"

echo "== 1. completion check =="
[ -f "$DEST/$OUT.DONE" ] || { echo "NO DONE SENTINEL — run did not complete cleanly; stop"; exit 1; }
[ -s "$DEST/$OUT.pt" ] || { echo "checkpoint missing/empty"; exit 1; }
cat "$DEST/$OUT.DONE"
md5 "$DEST/$OUT.pt"

echo
echo "== 2. trajectory vs pre-stated signatures =="
"$PY" - "$DEST/$OUT.jsonl" <<'EOF'
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1])]
final = recs[-1]
print(f"steps {final['step']:,}  tokens {final['tokens']:,}  "
      f"wall {final['sec']/3600:.1f}h  evals {len(recs)}")
print(f"final acc: {final['acc']}")

def first_above(key, thr):
    for r in recs:
        if r["acc"][key] >= thr:
            return r["step"]
    return None

for k in ["T_sr", "T_si", "T_state", "T_syntax", "T_sr_rev"]:
    vals = [r["acc"][k] for r in recs]
    print(f"{k:9s} final {vals[-1]:.3f}  max {max(vals):.3f}  "
          f"first>=0.9 @ step {first_above(k, 0.9)}")

print()
print("pre-stated signatures (pilot-a1-findings.md):")
print("  H_scale:              T_si (and plausibly T_sr_rev) reach ceiling")
print("  H_shortcut-starvation: instant T_sr, flat T_si, floor T_sr_rev")
print("  (10M A1 record for comparison: T_si 0.37 final, T_sr_rev 0.00,")
print("   T_sr 0.96, T_state/T_syntax 1.00 — verdict FAIL, no gaming)")
EOF

echo
echo "== 3. gate run (iii) on this checkpoint (n=4000 registered) =="
cd "$SRC_DIR" && "$PY" fingerprint_gate.py --run --ckpt "$DEST/$OUT.pt"
