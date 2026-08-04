"""Registered uncertainty re-analysis of the Experiment 1 removal test.

Implements pre-registration Amendment (2026-08-04): item-level bootstrap
CIs on the registered removal-test statistics, within-draw differentials,
and the per-item flip view. Re-analysis of registered artifacts only.

    ../../../.venv/bin/python analyze_removal_ci.py

Registered procedure: B=10,000, seed 20260804, percentile 95% CIs;
item-level primary, two-level category->item sensitivity. CIs cover
item-sampling uncertainty only (single registered pass per condition).

Output: artifacts/removal_test/removal_ci.json (+ table to stdout).
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402
from mvm import stats as mstats  # noqa: E402

ART = config.ARTIFACTS_DIR / "removal_test"
OUT = ART / "removal_ci.json"

SEED = 20260804
N_BOOT = 10_000
ALPHA = 0.05
CONDITIONS = ("idxres_mean_k16", "idxres_directional_k16",
              "narrative_mean_k16", "expert_mean_k16")
BATTERIES = ("T_self_irrelevant", "T_self_relevant", "T_syntax")


def load_t() -> tuple[dict, dict, dict]:
    """Return correct-arrays[cond][battery], item ids, category groups."""
    rec = json.loads((ART / "removal_test_scores.json").read_text())
    ids, groups, arrays = {}, {}, {}
    for bat in BATTERIES:
        base_items = rec["conditions"]["baseline"][bat]["items"]
        ids[bat] = [it["id"] for it in base_items]
        g = collections.defaultdict(list)
        for pos, it in enumerate(base_items):
            g[it["category"]].append(pos)
        groups[bat] = list(g.values())
    for cond in CONDITIONS:
        arrays[cond] = {}
        for bat in BATTERIES:
            by_id = {it["id"]: bool(it["correct"])
                     for it in rec["conditions"][cond][bat]["items"]}
            if set(by_id) != set(ids[bat]):
                raise SystemExit(f"item mismatch {cond}/{bat}")
            arrays[cond][bat] = np.array([by_id[i] for i in ids[bat]])
    return arrays, ids, groups


def load_s() -> tuple[dict, list, list]:
    """Return fidelity-arrays[cond] incl. baseline, item ids, category groups."""
    def per_item(name):
        rec = json.loads((ART / f"s_scores_{name}.json").read_text())
        return {it["id"]: float(it["fidelity"]) for it in rec["items"]}
    base = per_item("baseline")
    ids = sorted(base)
    rec = json.loads((ART / "s_scores_baseline.json").read_text())
    g = collections.defaultdict(list)
    pos = {i: p for p, i in enumerate(ids)}
    for it in rec["items"]:
        g[it["category"]].append(pos[it["id"]])
    arrays = {"baseline": np.array([base[i] for i in ids])}
    for cond in CONDITIONS:
        by_id = per_item(cond)
        if set(by_id) != set(ids):
            raise SystemExit(f"S item mismatch {cond}")
        arrays[cond] = np.array([by_id[i] for i in ids])
    return arrays, ids, list(g.values())


def summarize_batch(point: float, samples: np.ndarray) -> dict:
    return mstats.summarize(point, samples, ALPHA)


def main() -> None:
    t_arr, t_ids, t_groups = load_t()
    s_arr, s_ids, s_groups = load_s()
    rng = np.random.default_rng(SEED)

    methods = {}
    for method in ("primary", "two_level"):
        if method == "primary":
            draws = {bat: mstats.item_draws(len(t_ids[bat]), N_BOOT, rng)
                     for bat in BATTERIES}
            draws["S"] = mstats.item_draws(len(s_ids), N_BOOT, rng)
        else:
            draws = {bat: mstats.two_level_draws(t_groups[bat], N_BOOT, rng)
                     for bat in BATTERIES}
            draws["S"] = mstats.two_level_draws(s_groups, N_BOOT, rng)

        d_point, d_boot = {}, {}
        for cond in CONDITIONS:
            d_point[cond], d_boot[cond] = {}, {}
            for bat in BATTERIES:
                a = t_arr[cond][bat].astype(float)
                d_point[cond][bat] = 1.0 - a.mean()
                d_boot[cond][bat] = 1.0 - mstats.boot_mean(a, draws[bat])
            sb, sc = s_arr["baseline"], s_arr[cond]
            d_point[cond]["d_self"] = float((sb.mean() - sc.mean()) / sb.mean())
            bs = mstats.boot_mean(sb, draws["S"])
            cs = mstats.boot_mean(sc, draws["S"])
            d_boot[cond]["d_self"] = (bs - cs) / bs

        cells = {cond: {k: summarize_batch(d_point[cond][k], d_boot[cond][k])
                        for k in d_point[cond]} for cond in CONDITIONS}
        derived = {
            "differential_Tsi_primary_minus_control": summarize_batch(
                d_point["idxres_mean_k16"]["T_self_irrelevant"]
                - d_point["expert_mean_k16"]["T_self_irrelevant"],
                d_boot["idxres_mean_k16"]["T_self_irrelevant"]
                - d_boot["expert_mean_k16"]["T_self_irrelevant"]),
        }
        for cond in ("idxres_mean_k16", "idxres_directional_k16"):
            derived[f"router_gap_{cond}"] = summarize_batch(
                d_point[cond]["T_syntax"] - d_point[cond]["T_self_relevant"],
                d_boot[cond]["T_syntax"] - d_boot[cond]["T_self_relevant"])
        methods[method] = {"cells": cells, "derived": derived}

    rec = json.loads((ART / "removal_test_scores.json").read_text())
    flips = {}
    for bat in BATTERIES:
        prim = {it["id"]: it for it in
                rec["conditions"]["idxres_mean_k16"][bat]["items"]}
        flips[bat] = [{"id": i, "category": prim[i]["category"]}
                      for i in t_ids[bat] if not prim[i]["correct"]]

    out = {
        "config": {"n_boot": N_BOOT, "seed": SEED, "alpha": ALPHA,
                   "n_items": {b: len(t_ids[b]) for b in BATTERIES} | {"S": len(s_ids)},
                   "method": "percentile CIs; primary item-level bootstrap "
                             "within battery; sensitivity two-level "
                             "category->item; draws shared across conditions "
                             "(paired)",
                   "note": "CIs cover item-sampling uncertainty only; single "
                           "registered pass per condition"},
        "cells": methods["primary"]["cells"],
        "derived": methods["primary"]["derived"],
        "sensitivity_two_level": methods["two_level"],
        "primary_condition_flips": flips,
    }
    OUT.write_text(json.dumps(out, indent=2))

    for cond in CONDITIONS:
        c = methods["primary"]["cells"][cond]
        parts = [f"{k.replace('T_self_irrelevant','d_si').replace('T_self_relevant','d_sr').replace('T_syntax','d_syn')} "
                 f"{v['point']:+.3f} [{v['lo']:+.3f},{v['hi']:+.3f}]"
                 for k, v in c.items()]
        print(f"{cond:26} " + "  ".join(parts))
    print("\nderived (primary bootstrap):")
    for k, v in methods["primary"]["derived"].items():
        print(f"  {k:44} {v['point']:+.3f} [{v['lo']:+.3f},{v['hi']:+.3f}]")
    print(f"\nprimary-condition flips: " +
          ", ".join(f"{b}: {len(flips[b])}" for b in BATTERIES))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
