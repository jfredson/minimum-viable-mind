"""Recompute the retained-independence figures the paper quotes (Discussion, last paragraph) from the committed
ladder_analysis_ci.json (per-cell rates with 30 items per bank). The per-conversation scores themselves are not in the
repository (artifacts/ is gitignored), so this works from the stored cell rates.
Usage: python recompute_ri.py REPO_ROOT"""
import json, sys
from pathlib import Path
repo = Path(sys.argv[1]); d = json.loads((repo/"experiments/03-retained-independence/ladder_analysis_ci.json").read_text())
cells = d["cells"]; print("cells:", len(cells), sorted(cells)[:3], "...")
N = 30  # items per bank per cell (30 x 2 banks x 9 cells x 2 arms x ... = 540 preference ladders)
cap = {"a": 0.0, "b": 0.0}; masked = {"a": 0.0, "b": 0.0}
upd = []; pref = []
for k, c in cells.items():
    for bank, key in (("a", "bank_a"), ("b", "bank_b")):
        b = c[key]
        cap[bank] += b["capitulated_rate"]["point"] * N
        masked[bank] += b["masked_rate"]["point"] * N
        upd.append(b["evid_update_r3"]["point"])
        pref.append(b.get("pref_r3", b.get("pref_live_r3"))["point"])
print("preference ladders:", len(cells) * 2 * N, "(cells x 2 banks x 30)")
print("capitulations: bank A %.1f, bank B %.1f, total %.1f" % (cap["a"], cap["b"], cap["a"] + cap["b"]))
print("masked cells : bank A %.1f, bank B %.1f, total %.1f" % (masked["a"], masked["b"], masked["a"] + masked["b"]))
print("evidence update at R3: min %.2f max %.2f" % (min(upd), max(upd)))
print("preference retention at R3: min %.2f max %.2f" % (min(pref), max(pref)))
print("concentration:", d["concentration"])
