"""Compact cross-checkpoint table from the item sweep [thread 3]."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "lesion-results"
runs = ["pilot_a1_30m_seed0", "pilot_a1_30m_seed1_twin", "pilot_a1_30m_seed1",
        "pilot_a1_30m_seed0_twin", "pilot_a1_30m_seed2"]
print(f"{'run':28s} {'T_sr':>6} {'sr_rev':>7} {'T_si':>6} {'si_uniq':>8} "
      f"{'si_rep':>7}  T_si acc by dist_from_end 0..7")
for r in runs:
    s = json.loads((OUT / f"items_{r}.summary.json").read_text())["summary"]
    sr, si = s["T_sr"], s["T_si"]
    rev = sr.get("revised_turn", {}).get("1", {"acc": None})["acc"]
    uniq = si["item_repeated"]["0"]["acc"]
    rep = si["item_repeated"]["1"]["acc"]
    dist = " ".join(f"{si['dist_from_end'][str(d)]['acc']:.2f}"
                    for d in range(8))
    print(f"{r:28s} {sr['acc']:>6} {str(rev):>7} {si['acc']:>6} "
          f"{uniq:>8} {rep:>7}  {dist}")
print("\nT_sr acc by queried own-turn index, per run:")
for r in runs:
    s = json.loads((OUT / f"items_{r}.summary.json").read_text())
    sr = s["summary"]["T_sr"]
    row = " ".join(f"{k}:{v['acc']:.2f}(n{v['n']})"
                   for k, v in sr["turn_idx"].items())
    print(f"  {r:28s} {row}")
