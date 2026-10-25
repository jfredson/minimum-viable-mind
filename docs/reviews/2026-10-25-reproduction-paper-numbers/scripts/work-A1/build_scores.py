"""Build a stand-in removal_test_scores.json from committed files only: baseline all
correct (paper/findings: 92/92), primary condition from the committed flip list
(removal_ci.json), other conditions with the committed per-category wrong counts
(reread json) placed on the first items of each category (true positions unknown)."""
import json, sys
from pathlib import Path
E = Path(sys.argv[1]); out = Path(sys.argv[2])
BAT = {"T_self_irrelevant": "test_task_battery.jsonl", "T_self_relevant": "test_task_battery_self_relevant.jsonl", "T_syntax": "test_task_battery_syntax.jsonl"}
items = {b: [json.loads(l) for l in open(E / "src/batteries" / f) if l.strip()] for b, f in BAT.items()}
ci = json.loads((E / "removal_ci.json").read_text()); rr = json.loads((E / "reread-under-the-map-2026-10-24.json").read_text())
conds = {"baseline": {b: {"items": [{"id": i["id"], "category": i["category"], "correct": True} for i in items[b]]} for b in BAT}}
fl = {b: {f["id"] for f in ci["primary_condition_flips"][b]} for b in BAT}
conds["idxres_mean_k16"] = {b: {"items": [{"id": i["id"], "category": i["category"], "correct": i["id"] not in fl[b]} for i in items[b]]} for b in BAT}
for c in ["idxres_directional_k16", "narrative_mean_k16", "expert_mean_k16"]:
    cnt = {k: v["wrong"] for k, v in rr["conditions"][c]["categories"].items()}
    seen = {}; conds[c] = {}
    for b in BAT:
        L = []
        for i in items[b]:
            k = seen.get(i["category"], 0); seen[i["category"]] = k + 1
            L.append({"id": i["id"], "category": i["category"], "correct": k >= cnt[i["category"]]})
        conds[c][b] = {"items": L}
out.write_text(json.dumps({"conditions": conds}, indent=1))
