"""Part D: recompute the retained-independence companion figures from the committed
experiments/03-retained-independence/ladder_analysis_ci.json (per-item and per-cell records).
Usage: python check_ri.py <clone>"""
import json, sys
from pathlib import Path
d = json.loads((Path(sys.argv[1]) / "experiments/03-retained-independence/ladder_analysis_ci.json").read_text())
cells = d["cells"]
print("cells:", len(cells), sorted({k.split('|')[0] for k in cells}))
ev, pr = [], []
for k, c in cells.items():
    a, b = c["bank_a"], c["bank_b"]
    ev += [a["evid_update_r3"]["point"], b["evid_update_r3"]["point"]]
    pr += [a["pref_r3"]["point"], b["pref_live_r3"]["point"]]
    print(f"{k:35s} evid_upd A {a['evid_update_r3']['point']:.4f} B {b['evid_update_r3']['point']:.4f} | pref A {a['pref_r3']['point']:.4f} B-live {b['pref_live_r3']['point']:.4f}")
print(f"evidence-update range {min(ev):.4f}-{max(ev):.4f}; preference-retention range {min(pr):.4f}-{max(pr):.4f}")
tot = {"n_cells": 0, "masked": 0, "capitulated": 0, "pref_retained": 0}
cap_items = {}
for bank, items in d["per_item"].items():
    sub = {k: 0 for k in tot}
    for i, r in items.items():
        for k in sub: sub[k] += r[k]
        if r["capitulated"]: cap_items[i] = r["capitulated"]
    print(bank, len(items), "items", sub)
    for k in tot: tot[k] += sub[k]
print("total", tot)
print("capitulations by item:", cap_items)
# cross-check per-cell masked/capitulated rates x 30 items
m = sum(round(c[b]["masked_rate"]["point"] * 30) for c in cells.values() for b in ("bank_a", "bank_b"))
cp = sum(round(c[b]["capitulated_rate"]["point"] * 30) for c in cells.values() for b in ("bank_a", "bank_b"))
print("from per-cell rates x30: masked", m, "capitulated", cp)
print("grid arithmetic: 60 items x 2 arms x 3 framings x 3 models =", 60*2*3*3, "; preference ladders =", 60*3*3)
