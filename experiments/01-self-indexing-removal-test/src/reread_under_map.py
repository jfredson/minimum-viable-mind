"""Re-read the July removal test under the revised theory's map (unregistered, $0).

Implements reread-under-the-map-method-2026-10-24.md exactly: groups the 92
test items by registered category, reports each removal condition's drop per
group and per category with item-resampled 95% intervals (10,000 resamples,
seed 0), and the selectivity gaps G1 - G2 and G3 - G4.

    python3 src/reread_under_map.py [path/to/removal_test_scores.json]
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent.parent
DEFAULT_SCORES = Path.home() / "Code/minimum-viable-mind/artifacts/removal_test/removal_test_scores.json"
OUT = HERE / "reread-under-the-map-2026-10-24.json"

GROUPS = {
    "G1_flexible_not_about_turns": ["multi_step_reasoning", "coreference_binding", "needle_synthesis"],
    "G2_routine_not_about_turns": ["instruction_following"],
    "G3_flexible_about_turns": ["own_output_binding", "own_commitment", "role_binding"],
    "G4_routine_about_turns": ["syntax_own_turn", "syntax_user_turn", "syntax_turn_count"],
}
CONDITIONS = ["idxres_mean_k16", "idxres_directional_k16", "narrative_mean_k16", "expert_mean_k16"]
BATTERIES = ["T_self_irrelevant", "T_self_relevant", "T_syntax"]
N_BOOT = 10_000


def wrong_by_category(cond):
    out = {}
    for b in BATTERIES:
        for it in cond[b]["items"]:
            out.setdefault(it["category"], []).append(0.0 if it["correct"] else 1.0)
    return {c: np.array(v) for c, v in out.items()}


def interval(x, rng):
    idx = rng.integers(0, len(x), size=(N_BOOT, len(x)))
    m = x[idx].mean(axis=1)
    return [float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


def gap_interval(a, b, rng):
    ma = a[rng.integers(0, len(a), size=(N_BOOT, len(a)))].mean(axis=1)
    mb = b[rng.integers(0, len(b), size=(N_BOOT, len(b)))].mean(axis=1)
    d = ma - mb
    return [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))]


def main():
    scores = json.loads(Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCORES).read_text())
    base = wrong_by_category(scores["conditions"]["baseline"])
    assert all(v.sum() == 0 for v in base.values()), "an item failed at baseline"
    result = {"method": "reread-under-the-map-method-2026-10-24.md", "n_boot": N_BOOT, "seed": 0, "conditions": {}}
    for name in CONDITIONS:
        rng = np.random.default_rng(0)
        cats = wrong_by_category(scores["conditions"][name])
        groups = {g: np.concatenate([cats[c] for c in cs]) for g, cs in GROUPS.items()}
        r = {
            "categories": {c: {"n": len(v), "wrong": int(v.sum()), "drop": float(v.mean()), "ci95": interval(v, rng)} for c, v in sorted(cats.items())},
            "groups": {g: {"n": len(v), "wrong": int(v.sum()), "drop": float(v.mean()), "ci95": interval(v, rng)} for g, v in groups.items()},
        }
        g = groups
        r["gap_G1_minus_G2"] = {"value": float(g["G1_flexible_not_about_turns"].mean() - g["G2_routine_not_about_turns"].mean()),
                                "ci95": gap_interval(g["G1_flexible_not_about_turns"], g["G2_routine_not_about_turns"], rng)}
        r["gap_G3_minus_G4"] = {"value": float(g["G3_flexible_about_turns"].mean() - g["G4_routine_about_turns"].mean()),
                                "ci95": gap_interval(g["G3_flexible_about_turns"], g["G4_routine_about_turns"], rng)}
        result["conditions"][name] = r
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    for name, r in result["conditions"].items():
        print(name)
        for gname, v in r["groups"].items():
            print(f"  {gname:30s} {v['wrong']:2d}/{v['n']:2d}  drop {v['drop']:.3f}  [{v['ci95'][0]:.3f}, {v['ci95'][1]:.3f}]")
        for k in ("gap_G1_minus_G2", "gap_G3_minus_G4"):
            v = r[k]
            print(f"  {k:30s} {v['value']:+.3f}  [{v['ci95'][0]:+.3f}, {v['ci95'][1]:+.3f}]")


if __name__ == "__main__":
    main()
