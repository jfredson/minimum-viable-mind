"""A2 check: rebuild the primary-condition router-gap CI (removal_ci.json) from
committed data only: test-battery item order (src/batteries/test_*.jsonl) and the
primary-condition flip list committed in removal_ci.json. Uses the committed
mvm.stats draw functions with the committed seed and draw order."""
import json, sys
from pathlib import Path
import numpy as np
clone = Path(sys.argv[1])
sys.path.insert(0, str(clone / "src"))
from mvm import stats as mstats
E = clone / "experiments/01-self-indexing-removal-test"
ci = json.loads((E / "removal_ci.json").read_text())
files = {"T_self_irrelevant": "test_task_battery.jsonl",
         "T_self_relevant": "test_task_battery_self_relevant.jsonl",
         "T_syntax": "test_task_battery_syntax.jsonl"}
ids = {b: [json.loads(l)["id"] for l in open(E / "src/batteries" / f)] for b, f in files.items()}
flips = {b: {x["id"] for x in ci["primary_condition_flips"][b]} for b in files}
rng = np.random.default_rng(20260804)
draws = {b: mstats.item_draws(len(ids[b]), 10_000, rng) for b in files}
d_pt, d_bt = {}, {}
for b in files:
    a = np.array([i not in flips[b] for i in ids[b]], float)
    d_pt[b] = 1 - a.mean(); d_bt[b] = 1 - mstats.boot_mean(a, draws[b])
    print(b, mstats.summarize(d_pt[b], d_bt[b], 0.05), "committed:", ci["cells"]["idxres_mean_k16"][b])
g = mstats.summarize(d_pt["T_syntax"] - d_pt["T_self_relevant"], d_bt["T_syntax"] - d_bt["T_self_relevant"], 0.05)
print("router gap", g, "committed:", ci["derived"]["router_gap_idxres_mean_k16"])
