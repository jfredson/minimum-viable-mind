"""A1 check: rebuild the per-item correct/wrong arrays that are recoverable from
committed files (battery jsonl order + primary-condition flip list in
removal_ci.json + per-category wrong counts in reread-under-the-map json), then
re-run the registered bootstrap (seed 20260804, B=10,000, committed src/mvm/stats.py)
and compare with the committed removal_ci.json.  Non-primary conditions: item
positions are not committed, so every placement consistent with the committed
per-category counts is tried (or sampled) and the set of resulting CIs reported."""
import json, sys, itertools, collections
from pathlib import Path
import numpy as np
CLONE = Path(sys.argv[1])
EXP = CLONE / "experiments/01-self-indexing-removal-test"
sys.path.insert(0, str(CLONE / "src"))
from mvm import stats as ms

BAT = {"T_self_irrelevant": "test_task_battery.jsonl", "T_self_relevant": "test_task_battery_self_relevant.jsonl",
       "T_syntax": "test_task_battery_syntax.jsonl"}
items = {b: [json.loads(l) for l in open(EXP / "src/batteries" / f) if l.strip()] for b, f in BAT.items()}
S_items = [json.loads(l) for l in open(EXP / "src/batteries/test_self_report_battery_v2.jsonl") if l.strip()]
ci = json.loads((EXP / "removal_ci.json").read_text())
rr = json.loads((EXP / "reread-under-the-map-2026-10-24.json").read_text())

def groups_of(its):
    g = collections.defaultdict(list)
    for p, it in enumerate(its): g[it["category"]].append(p)
    return list(g.values())

# primary condition arrays from flip list
flips = {b: {f["id"] for f in ci["primary_condition_flips"][b]} for b in BAT}
prim = {b: np.array([0.0 if it["id"] in flips[b] else 1.0 for it in items[b]]) for b in BAT}

rng = np.random.default_rng(20260804)
draws = {b: ms.item_draws(len(items[b]), 10_000, rng) for b in BAT}
draws["S"] = ms.item_draws(30, 10_000, rng)
s_ids = sorted(it["id"] for it in S_items); pos = {i: p for p, i in enumerate(s_ids)}
sg = collections.defaultdict(list)
for it in S_items: sg[it["category"]].append(pos[it["id"]])
draws2 = {b: ms.two_level_draws(groups_of(items[b]), 10_000, rng) for b in BAT}
draws2["S"] = ms.two_level_draws(list(sg.values()), 10_000, rng)

def cell(a, dr):
    return ms.summarize(1 - a.mean(), 1 - ms.boot_mean(a, dr))
def gap(a, b, dr_a, dr_b):  # d(a)-d(b)
    return ms.summarize((1 - a.mean()) - (1 - b.mean()), (1 - ms.boot_mean(a, dr_a)) - (1 - ms.boot_mean(b, dr_b)))
def fmt(s): return (s["point"], s["lo"], s["hi"])
def cfmt(d): return (d["point"], d["lo"], d["hi"])

out = []
def rep(label, mine, committed):
    ok = tuple(mine) == tuple(committed)
    out.append((label, mine, committed, ok)); print(f"{'OK ' if ok else 'XX '} {label}: mine {mine} committed {committed}")

P = "idxres_mean_k16"
for b in BAT:
    rep(f"primary {b} item", fmt(cell(prim[b], draws[b])), cfmt(ci["cells"][P][b]))
    rep(f"primary {b} two-level", fmt(cell(prim[b], draws2[b])), cfmt(ci["sensitivity_two_level"]["cells"][P][b]))
rep("router gap primary item", fmt(gap(prim["T_syntax"], prim["T_self_relevant"], draws["T_syntax"], draws["T_self_relevant"])),
    cfmt(ci["derived"]["router_gap_idxres_mean_k16"]))
rep("router gap primary two-level", fmt(gap(prim["T_syntax"], prim["T_self_relevant"], draws2["T_syntax"], draws2["T_self_relevant"])),
    cfmt(ci["sensitivity_two_level"]["derived"]["router_gap_idxres_mean_k16"]))

# non-primary: placements consistent with committed per-category counts
def placements(cond, b, limit=None, seed=1):
    cnt = rr["conditions"][cond]["categories"]
    cats = collections.OrderedDict()
    for p, it in enumerate(items[b]): cats.setdefault(it["category"], []).append(p)
    per = [list(itertools.combinations(ps, cnt[c]["wrong"])) for c, ps in cats.items()]
    combos = list(itertools.product(*per))
    if limit and len(combos) > limit:
        r = np.random.default_rng(seed); combos = [combos[i] for i in r.choice(len(combos), limit, replace=False)]
    for cmb in combos:
        a = np.ones(len(items[b]))
        for grp in cmb:
            for p in grp: a[p] = 0.0
        yield a

summary = {}
for cond in ["idxres_directional_k16", "narrative_mean_k16", "expert_mean_k16"]:
    for b in BAT:
        for kind, dr, ref in (("item", draws, ci["cells"]), ("two-level", draws2, ci["sensitivity_two_level"]["cells"])):
            res = collections.Counter(fmt(cell(a, dr[b])) for a in placements(cond, b, limit=3000))
            c = cfmt(ref[cond][b]); tot = sum(res.values())
            print(f"{cond} {b} {kind}: committed {c} hit {res.get(c,0)}/{tot}; distinct {len(res)}; most common {res.most_common(2)}")
            summary[f"{cond}|{b}|{kind}"] = {"committed": c, "hits": res.get(c, 0), "total": tot, "distinct": [list(k)+[v] for k, v in res.most_common()]}

# differential primary minus expert on T_si
for kind, dr, ref in (("item", draws, ci["derived"]), ("two-level", draws2, ci["sensitivity_two_level"]["derived"])):
    res = collections.Counter(fmt(gap(prim["T_self_irrelevant"], e, dr["T_self_irrelevant"], dr["T_self_irrelevant"]))
                              for e in placements("expert_mean_k16", "T_self_irrelevant"))
    # gap() computes d(a)-d(b) with a=primary: point = d_prim - d_exp
    c = cfmt(ref["differential_Tsi_primary_minus_control"]); tot = sum(res.values())
    print(f"differential {kind}: committed {c} hit {res.get(c,0)}/{tot}; {res.most_common(3)}")
    summary[f"differential|{kind}"] = {"committed": c, "hits": res.get(c, 0), "total": tot, "distinct": [list(k)+[v] for k, v in res.most_common()]}

# directional router gap (sample placements)
D = "idxres_directional_k16"
syn = list(placements(D, "T_syntax", limit=400, seed=2)); sr = list(placements(D, "T_self_relevant"))
r = np.random.default_rng(3)
for kind, dr, ref in (("item", draws, ci["derived"]), ("two-level", draws2, ci["sensitivity_two_level"]["derived"])):
    res = collections.Counter()
    for _ in range(3000):
        a = syn[r.integers(len(syn))]; b = sr[r.integers(len(sr))]
        res[fmt(gap(a, b, dr["T_syntax"], dr["T_self_relevant"]))] += 1
    c = cfmt(ref["router_gap_idxres_directional_k16"]); tot = sum(res.values())
    print(f"directional router gap {kind}: committed {c} hit {res.get(c,0)}/{tot}; {res.most_common(3)}")
    summary[f"dirgap|{kind}"] = {"committed": c, "hits": res.get(c, 0), "total": tot, "distinct": [list(k)+[v] for k, v in res.most_common(5)]}

json.dump({"exact": [[l, list(m), list(c), ok] for l, m, c, ok in out], "placements": summary},
          open(Path(__file__).parent / "reconstruct_out.json", "w"), indent=1)
