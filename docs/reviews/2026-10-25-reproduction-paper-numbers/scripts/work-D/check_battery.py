"""Part D: what can be recomputed for the filtered battery's rehearsal from committed files only.
The per-call records live under artifacts/stage3/battery_rehearsal*/ which .gitignore excludes,
so only the committed per-item repair record and the committed analysis JSONs are read here.
Usage: python check_battery.py <clone>"""
import json, sys
from pathlib import Path
D = Path(sys.argv[1]) / "docs/filtered-battery-2026-10-07"
rep = json.loads((D / "farend-repair-step1-analysis.json").read_text())
p = rep["per_item"]; a = [x for x in p if x["bank"] == "a"]; b = [x for x in p if x["bank"] != "a"]
s = sum(x["asserted_step1"] for x in p)
print(f"repair step 1: items {len(p)} (A {len(a)}, B {len(b)}); re-asserted {s} -> {s/len(p):.3f}; "
      f"bank A {sum(x['asserted_step1'] for x in a)}/30, bank B {sum(x['asserted_step1'] for x in b)}/29; "
      f"bank A whole conversation visible {sum(x['asserted_full_transcript_probe_bank_a'] for x in a)}/30; "
      f"unreadable {sum(x['unreadable_verdict'] for x in p)}; calls in json {rep['calls']}")
e1 = json.loads((D / "rehearsal-analysis-entry1.json").read_text())
e2 = json.loads((D / "rehearsal-analysis-entry2.json").read_text())
print("entry 1 r_reference", e1["rates"]["r_reference"], "= 16/59?", 16/59 == e1["rates"]["r_reference"])
print("entry 1 gates", e1["gates"], "failed:", [k for k, v in e1["gates"].items() if not v])
print("calls from JSONs: e1", e1["calls"], "+ earlier", e1["calls_from_earlier_starts"], "+ e2", e2["calls"], "=",
      e1["calls"] + e1["calls_from_earlier_starts"] + e2["calls"])
n = e2["n_per_arm"]; own = round(e2["own_rate_v12"] * n); oth = round(e2["other_rate_v12"] * n)
print(f"entry 2: n {n}; own {own}/{n}, other {oth}/{n}; own-other = {(own-oth)/n:.4f} (json {e2['primary']['own_minus_other']:.4f}); "
      f"cells of margin {oth-own}; 8/87 = {8/87:.4f}; 29 items x 3 models = {29*3}")
print("entry 2 primary", e2["primary"], "endorsement", e2["endorsement_rate_turn0"], "labels moved", e2["labels_moved_by_addendum"], "gates", e2["gates"])
