"""Registered uncertainty & heterogeneity analysis for the Stage 3 ladder.

Implements pre-registration Amendment (2026-08-04): hierarchical bootstrap
confidence intervals on the registered Stage 3 statistics, framing
contrasts, and the per-item heterogeneity view. Re-analysis only — consumes
the same transcripts and blind verdicts as analyze_ladder.py; no new model
calls, no re-judging. Point estimates are cross-checked against
ladder_analysis.json where present.

    ../../../.venv/bin/python analyze_ladder_ci.py [--tag main]
    ../../../.venv/bin/python analyze_ladder_ci.py --self-test

Registered procedure (fixed before the run): seed 20260804, B=10,000,
percentile 95% CIs. Primary resampling unit is the item (within bank),
preserving all pairings across arms/framings/models; sensitivity analysis
uses a two-level (category|domain -> item) bootstrap. Masked/capitulated
are reported as fractions of all preference-arm items. CIs quantify
item-sampling uncertainty ONLY — a single decode per cell at temperature 0
means decoding variance is invisible to this analysis.

Output: artifacts/stage3/ladder_analysis_ci.json (+ table to stdout).
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402
from mvm import stats as mstats  # noqa: E402

LADDER_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder"
SCORES_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder_scores"
BATTERIES = Path(__file__).resolve().parent / "batteries"
OUT = config.ARTIFACTS_DIR / "stage3" / "ladder_analysis_ci.json"
POINT_FILE = config.ARTIFACTS_DIR / "stage3" / "ladder_analysis.json"

SEED = 20260804
N_BOOT = 10_000
ALPHA = 0.05
FRAMINGS = ("tool", "tool_expert", "mind")
CONTRASTS = (("mind", "tool"), ("mind", "tool_expert"), ("tool_expert", "tool"))


def load_bank(fname: str, group_key: str):
    items = [json.loads(l) for l in
             (BATTERIES / fname).read_text().splitlines() if l.strip()]
    ids = [it["id"] for it in items]
    groups = collections.defaultdict(list)
    for pos, it in enumerate(items):
        groups[it[group_key]].append(pos)
    return ids, {it["id"]: it[group_key] for it in items}, list(groups.values())


def blank(n_a: int, n_b: int) -> dict:
    return {
        "a_pref": np.zeros((n_a, 5), bool),   # matches_answer per turn
        "a_evid_ret": np.zeros(n_a, bool),    # matches_answer at R3
        "a_evid_upd": np.zeros(n_a, bool),    # matches_post_update at R3
        "b_pref": np.zeros((n_b, 5), bool),   # ASSERTED_OWN per turn
        "b_evid_own": np.zeros(n_b, bool),    # ASSERTED_OWN at R3
        "b_evid_wd": np.zeros(n_b, bool),     # WITHDRAWN at R3
        "seen": collections.Counter(),
    }


def load_cells(tag: str, pos_a: dict, pos_b: dict) -> dict:
    data = {}
    for f in sorted((LADDER_DIR / tag).glob("*.json")):
        rec = json.loads(f.read_text())
        key = (rec["model"], rec["framing"])
        d = data.setdefault(key, blank(len(pos_a), len(pos_b)))
        d["seen"][(rec["bank"], rec["arm"])] += 1
        if rec["bank"] == "a":
            p = pos_a[rec["item"]]
            s = rec["scores"]
            if rec["arm"] == "preference":
                d["a_pref"][p] = [s[i]["matches_answer"] for i in range(5)]
            else:
                d["a_evid_ret"][p] = s[3]["matches_answer"]
                d["a_evid_upd"][p] = s[3]["matches_post_update"]
        else:
            p = pos_b[rec["item"]]
            v = json.loads((SCORES_DIR / tag / f.name).read_text())["verdicts"]
            if rec["arm"] == "preference":
                d["b_pref"][p] = [x.get("position") == "ASSERTED_OWN" for x in v]
            else:
                d["b_evid_own"][p] = v[3].get("position") == "ASSERTED_OWN"
                d["b_evid_wd"][p] = v[3].get("position") == "WITHDRAWN"
    for key, d in data.items():
        for cell, n_exp in ((("a", "preference"), len(pos_a)),
                            (("a", "evidence"), len(pos_a)),
                            (("b", "preference"), len(pos_b)),
                            (("b", "evidence"), len(pos_b))):
            if d["seen"][cell] != n_exp:
                raise SystemExit(f"incomplete cell {key} {cell}: "
                                 f"{d['seen'][cell]}/{n_exp}")
    return data


def cell_stats(d: dict, ia: np.ndarray, ib: np.ndarray) -> dict:
    """All registered statistics for one (model, framing), batched over
    bootstrap draws. ia/ib: (B, n) index arrays. Returns dict of (B,) or
    (B, 3) arrays."""
    ap = d["a_pref"][ia]                       # (B, n_a, 5)
    a_curve = ap[:, :, 1:4].mean(1)            # (B, 3)
    a_pref = a_curve[:, 2]
    a_evid = d["a_evid_ret"][ia].mean(1)
    a_upd = d["a_evid_upd"][ia].mean(1)
    a_lost = ~ap[:, :, 3]
    a_masked = (a_lost & ap[:, :, 4]).mean(1)
    a_cap = (a_lost & ~ap[:, :, 4]).mean(1)

    bp = d["b_pref"][ib]
    b_curve = bp[:, :, 1:4].mean(1)
    b_pref = b_curve[:, 2]
    b_evid = d["b_evid_own"][ib].mean(1)
    b_upd = d["b_evid_wd"][ib].mean(1)
    b_lost = ~bp[:, :, 3]
    b_masked = (b_lost & bp[:, :, 4]).mean(1)
    b_cap = (b_lost & ~bp[:, :, 4]).mean(1)

    n_a, n_b = ia.shape[1], ib.shape[1]
    pref_c = (a_pref * n_a + b_pref * n_b) / (n_a + n_b)
    evid_c = (a_evid * n_a + b_evid * n_b) / (n_a + n_b)

    return {
        "bank_a": {"pref_curve": a_curve, "pref_r3": a_pref,
                   "evid_retain_r3": a_evid,
                   "evid_update_r3": a_upd, "masked_rate": a_masked,
                   "capitulated_rate": a_cap, "ri": a_pref - a_evid},
        "bank_b": {"pref_live_curve": b_curve, "pref_live_r3": b_pref,
              "evid_live_r3": b_evid, "evid_update_r3": b_upd,
              "masked_rate": b_masked, "capitulated_rate": b_cap,
              "ri": b_pref - b_evid},
        "ri_combined": pref_c - evid_c,
    }


def summarize_tree(point: dict, boot: dict) -> dict:
    out = {}
    for k, pv in point.items():
        bv = boot[k]
        if isinstance(pv, dict):
            out[k] = summarize_tree(pv, bv)
        elif pv.ndim == 2:  # curves: (1, 3) point vs (B, 3) boot
            out[k] = [mstats.summarize(pv[0, i], bv[:, i], ALPHA)
                      for i in range(pv.shape[1])]
        else:
            out[k] = mstats.summarize(pv[0], bv, ALPHA)
    return out


def analyze(data: dict, groups_a, groups_b, n_boot: int, rng) -> tuple[dict, dict]:
    n_a = len(data[next(iter(data))]["a_pref"])
    n_b = len(data[next(iter(data))]["b_pref"])
    full_a = np.arange(n_a)[None, :]
    full_b = np.arange(n_b)[None, :]
    draws = {
        "primary": (mstats.item_draws(n_a, n_boot, rng),
                    mstats.item_draws(n_b, n_boot, rng)),
        "two_level": (mstats.two_level_draws(groups_a, n_boot, rng),
                      mstats.two_level_draws(groups_b, n_boot, rng)),
    }

    results = {}
    for method, (ia, ib) in draws.items():
        cells, contrasts = {}, {}
        ri_by_model = collections.defaultdict(dict)
        for (model, framing), d in sorted(data.items()):
            point = cell_stats(d, full_a, full_b)
            boot = cell_stats(d, ia, ib)
            cells[f"{model}|{framing}"] = summarize_tree(point, boot)
            ri_by_model[model][framing] = (point, boot)
        for model, per_fr in ri_by_model.items():
            if set(FRAMINGS) - set(per_fr):
                continue
            contrasts[model] = {}
            for bank in ("bank_a", "bank_b", "combined"):
                def ri(fr):
                    p, b = per_fr[fr]
                    if bank == "combined":
                        return p["ri_combined"], b["ri_combined"]
                    return p[bank]["ri"], b[bank]["ri"]
                contrasts[model][bank] = {
                    f"{hi}_minus_{lo}": mstats.summarize(
                        ri(hi)[0][0] - ri(lo)[0][0],
                        ri(hi)[1] - ri(lo)[1], ALPHA)
                    for hi, lo in CONTRASTS
                }
        results[method] = {"cells": cells, "contrasts": contrasts}
    return results["primary"], results["two_level"]


def per_item_view(data: dict, ids_a, ids_b, cat_a, cat_b) -> tuple[dict, dict]:
    n_cells = len(data)
    view = {"bank_a": {}, "bank_b": {}}
    caps = {"bank_a": np.zeros(len(ids_a)), "bank_b": np.zeros(len(ids_b))}
    for bank, ids, cats, pref, probe_col, evid in (
            ("bank_a", ids_a, cat_a, "a_pref", 4, "a_evid_ret"),
            ("bank_b", ids_b, cat_b, "b_pref", 4, "b_evid_own")):
        retained = np.zeros(len(ids)); masked = np.zeros(len(ids))
        cap = np.zeros(len(ids)); evid_ret = np.zeros(len(ids))
        for d in data.values():
            p = d[pref]
            retained += p[:, 3]
            masked += ~p[:, 3] & p[:, probe_col]
            cap += ~p[:, 3] & ~p[:, probe_col]
            evid_ret += d[evid]
        caps[bank] = cap
        for i, item_id in enumerate(ids):
            view[bank][item_id] = {
                "group": cats[item_id], "n_cells": n_cells,
                "pref_retained": int(retained[i]), "masked": int(masked[i]),
                "capitulated": int(cap[i]), "evid_retained": int(evid_ret[i]),
            }
    conc = {}
    for bank, ids in (("bank_a", ids_a), ("bank_b", ids_b)):
        c = caps[bank]
        total = int(c.sum())
        top = np.argsort(c)[::-1][:3]
        conc[bank] = {
            "total_capitulations": total,
            "top3_items": [ids[i] for i in top if c[i] > 0],
            "top3_share": round(float(c[top].sum() / total), 4) if total else None,
        }
    return view, conc


def cross_check(cells: dict) -> float | None:
    if not POINT_FILE.exists():
        return None
    ref = json.loads(POINT_FILE.read_text())
    worst = 0.0
    for key, r in ref.items():
        c = cells[key]
        for got, want in ((c["bank_a"]["ri"]["point"], r["bank_a"]["ri"]),
                          (c["bank_b"]["ri"]["point"], r["bank_b"]["ri"]),
                          (c["ri_combined"]["point"], r["ri_combined"])):
            worst = max(worst, abs(got - round(want, 4)))
    return worst


def self_test() -> None:
    rng = np.random.default_rng(0)
    d = blank(4, 4)
    # A: pref retains items 0,1 at R3; item 2 masked; item 3 capitulated.
    d["a_pref"][0] = d["a_pref"][1] = [1, 1, 1, 1, 1]
    d["a_pref"][2] = [1, 1, 1, 0, 1]
    d["a_pref"][3] = [1, 1, 0, 0, 0]
    d["a_evid_ret"][:] = [1, 0, 0, 0]
    d["b_pref"] = d["a_pref"].copy()
    d["b_evid_own"][:] = [0, 0, 0, 0]
    full = np.arange(4)[None, :]
    s = cell_stats(d, full, full)
    assert np.isclose(s["bank_a"]["pref_r3"][0], 0.5)
    assert np.isclose(s["bank_a"]["masked_rate"][0], 0.25)
    assert np.isclose(s["bank_a"]["capitulated_rate"][0], 0.25)
    assert np.isclose(s["bank_a"]["ri"][0], 0.25)
    assert np.isclose(s["bank_b"]["ri"][0], 0.5)
    assert np.isclose(s["ri_combined"][0], 0.375)
    boot = cell_stats(d, mstats.item_draws(4, 200, rng),
                      mstats.item_draws(4, 200, rng))
    ci = mstats.summarize(s["bank_a"]["ri"][0], boot["bank_a"]["ri"])
    assert ci["lo"] <= 0.25 <= ci["hi"]
    tl = mstats.two_level_draws([[0, 1], [2, 3]], 50, rng)
    assert tl.shape == (50, 4) and tl.max() <= 3
    print("self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="main")
    ap.add_argument("--n-boot", type=int, default=N_BOOT)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return

    ids_a, cat_a, groups_a = load_bank("items_held_answer.jsonl", "category")
    ids_b, cat_b, groups_b = load_bank("items_live_objection.jsonl", "domain")
    pos_a = {i: p for p, i in enumerate(ids_a)}
    pos_b = {i: p for p, i in enumerate(ids_b)}
    data = load_cells(args.tag, pos_a, pos_b)

    rng = np.random.default_rng(SEED)
    primary, two_level = analyze(data, groups_a, groups_b, args.n_boot, rng)
    view, conc = per_item_view(data, ids_a, ids_b, cat_a, cat_b)
    check = cross_check(primary["cells"]) if args.tag == "main" else None

    out = {
        "config": {"tag": args.tag, "n_boot": args.n_boot, "seed": SEED,
                   "alpha": ALPHA,
                   "method": "percentile CIs; primary item-level bootstrap "
                             "within bank; sensitivity two-level "
                             "(category|domain -> item)",
                   "note": "CIs cover item-sampling uncertainty only; "
                           "single decode per cell",
                   "cross_check_max_abs_diff_vs_registered_analyzer": check},
        "cells": primary["cells"],
        "contrasts": primary["contrasts"],
        "sensitivity_two_level": two_level,
        "per_item": view,
        "concentration": conc,
    }
    OUT.write_text(json.dumps(out, indent=2))

    for key, c in primary["cells"].items():
        ra, rb, rc = c["bank_a"]["ri"], c["bank_b"]["ri"], c["ri_combined"]
        print(f"{key:36} RI_A {ra['point']:6.3f} [{ra['lo']:6.3f},{ra['hi']:6.3f}]"
              f"  RI_B {rb['point']:6.3f} [{rb['lo']:6.3f},{rb['hi']:6.3f}]"
              f"  RI {rc['point']:6.3f} [{rc['lo']:6.3f},{rc['hi']:6.3f}]")
    print("\ncontrasts (primary bootstrap):")
    for model, banks in primary["contrasts"].items():
        for name, v in banks["combined"].items():
            print(f"  {model:22} {name:28} "
                  f"{v['point']:6.3f} [{v['lo']:6.3f},{v['hi']:6.3f}]")
    if check is not None:
        print(f"\ncross-check vs ladder_analysis.json: max |diff| = {check:.2e}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
