"""Reproduce, from committed files only, what can be reproduced of the Experiment 1
bootstrap intervals (paper Table 1 and the paragraph after it).

Why only part: the per-item scores (artifacts/removal_test/*.json) are gitignored and
absent from a clean clone. What the repository keeps is removal_ci.json, which holds the
flipped-item list for the PRIMARY condition only, and the held-out batteries. With the
baseline at 1.000 on every item, the primary condition's correct/incorrect arrays can be
rebuilt, and with the registered RNG stream (seed 20260804, same draw order as
analyze_removal_ci.py) its intervals can be recomputed.

Usage: python reproduce_removal_ci.py REPO_ROOT
"""
import collections, json, sys
from pathlib import Path
import numpy as np

repo = Path(sys.argv[1])
exp = repo / "experiments/01-self-indexing-removal-test"
import importlib.util
spec = importlib.util.spec_from_file_location("mstats", repo / "src/mvm/stats.py")
mstats = importlib.util.module_from_spec(spec); spec.loader.exec_module(mstats)

ci = json.loads((exp / "removal_ci.json").read_text())
SEED, B, ALPHA = ci["config"]["seed"], ci["config"]["n_boot"], ci["config"]["alpha"]
files = {"T_self_irrelevant": "test_task_battery", "T_self_relevant": "test_task_battery_self_relevant",
         "T_syntax": "test_task_battery_syntax"}
BATS = tuple(files)
ids, groups, arr = {}, {}, {}
for bat, f in files.items():
    rows = [json.loads(l) for l in (exp / "src/batteries" / f"{f}.jsonl").read_text().splitlines() if l.strip()]
    ids[bat] = [r["id"] for r in rows]
    g = collections.defaultdict(list)
    for pos, r in enumerate(rows):
        g[r["category"]].append(pos)
    groups[bat] = list(g.values())
    flipped = {x["id"] for x in ci["primary_condition_flips"][bat]}
    assert flipped <= set(ids[bat]), (bat, flipped - set(ids[bat]))
    arr[bat] = np.array([i not in flipped for i in ids[bat]])
n_s = ci["config"]["n_items"]["S"]

rng = np.random.default_rng(SEED)
draws = {b: mstats.item_draws(len(ids[b]), B, rng) for b in BATS}
draws["S"] = mstats.item_draws(n_s, B, rng)
res = {}
for b in BATS:
    a = arr[b].astype(float)
    res[b] = (1 - a.mean(), 1 - mstats.boot_mean(a, draws[b]))
out = {"primary_item_level": {}, "primary_two_level_T_si": None, "router_gap_primary": None}
for b in BATS:
    out["primary_item_level"][b] = mstats.summarize(*res[b], ALPHA)
gap = mstats.summarize(res["T_syntax"][0] - res["T_self_relevant"][0], res["T_syntax"][1] - res["T_self_relevant"][1], ALPHA)
out["router_gap_primary"] = gap
# two-level: the script draws for the three batteries in order, then S
d2 = {b: mstats.two_level_draws(groups[b], B, rng) for b in BATS}
a = arr["T_self_irrelevant"].astype(float)
out["primary_two_level_T_si"] = mstats.summarize(1 - a.mean(), 1 - mstats.boot_mean(a, d2["T_self_irrelevant"]), ALPHA)

# compare with the committed file
rep = {"checks": []}
def chk(name, mine, theirs):
    ok = all(abs(mine[k] - theirs[k]) < 1e-4 for k in ("point", "lo", "hi"))
    rep["checks"].append((name, mine, theirs, ok))
    print(("MATCH  " if ok else "DIFFER "), name, "recomputed", mine, "committed", theirs)
cond = ci["cells"]["idxres_mean_k16"]
for b in BATS:
    chk(f"primary {b} (item-level)", out["primary_item_level"][b], cond[b])
chk("router gap, primary condition", gap, ci["derived"]["router_gap_idxres_mean_k16"])
chk("primary T_si, two-level sensitivity", out["primary_two_level_T_si"],
    ci["sensitivity_two_level"]["cells"]["idxres_mean_k16"]["T_self_irrelevant"])
for b in ("T_self_relevant", "T_syntax"):
    a = arr[b].astype(float)
    chk(f"primary {b}, two-level sensitivity", mstats.summarize(1 - a.mean(), 1 - mstats.boot_mean(a, d2[b]), ALPHA),
        ci["sensitivity_two_level"]["cells"]["idxres_mean_k16"][b])
# category counts quoted in the paper
cats = collections.Counter(json.loads(l)["category"] for l in (exp/"src/batteries/test_task_battery.jsonl").read_text().splitlines() if l.strip())
flips = ci["primary_condition_flips"]["T_self_irrelevant"]
ms = sum(1 for x in flips if x["category"] == "multi_step_reasoning")
print("T_si flips:", len(flips), "multi-step:", ms, "of", cats["multi_step_reasoning"], "; elsewhere:", len(flips) - ms, "of", sum(cats.values()) - cats["multi_step_reasoning"])
# items per battery
print("battery sizes", {b: len(ids[b]) for b in BATS}, "flips", {b: len(ci['primary_condition_flips'][b]) for b in BATS})
# point estimates of other conditions are recoverable as fractions of n
for c, cells in ci["cells"].items():
    for b in BATS:
        n = len(ids[b]); p = cells[b]["point"]
        print(f"{c:26} {b:18} point {p:.4f} = {round(p*n)}/{n} flipped (x/n = {round(p*n)/n:.4f})")
