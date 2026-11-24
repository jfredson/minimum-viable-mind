"""Step 4b of the loop removal test, the analysis: runs on the Mac from the collection's files. See
step4b-runbook.md.

    python3 -I src/step4b_analyse.py --pilot batteries/pilot-v0.12 --collect <out dir>

Writes step4b-analysis.json beside the collection and prints every return-to-John condition as fired or not.
It does not compute the main removal's gap between the cells, or any outcome: the pilot rehearses the
measurements and reads no pattern.
"""
import argparse
import ast
import json
import os
import random
import statistics

CHANCE = 0.2
MARGIN_MIN = 2.2       # design, section 5, the confidence check
INTRUDE = 1.0          # "no more than 1.0 below"
FIFTH = 0.2


def norm_loss(base_right, alt_right):
    return (base_right - alt_right) / (1 - CHANCE)


def load(d, name):
    return [json.loads(l) for l in open(os.path.join(d, name))]


def boot(units, stat, n=10000, seed=1):
    """Paired resampling by unit (design, section 6): units is a list of lists of per-item values, or a dict of
    such lists by rule kind, in which case each kind is resampled within itself (specification, section 19,
    item 6)."""
    strata = list(units.values()) if isinstance(units, dict) else [units]
    rng = random.Random(seed)
    vals = []
    for _ in range(n):
        flat = []
        for st in strata:
            for _ in st:
                flat.extend(rng.choice(st))
        vals.append(stat(flat))
    vals.sort()
    return vals[int(0.025 * n)], vals[int(0.975 * n) - 1]


GATE_N = 100000   # specification, section 19, item 6


def gate_interval(units, stat, threshold, end):
    """A gate decision's interval at 100,000 resamples, with the spread over 20 seeds when it lies within 0.005."""
    lo, hi = boot(units, stat, n=GATE_N, seed=1)
    v = lo if end == "lower" else hi
    out = {"interval": [lo, hi]}
    if abs(v - threshold) < 0.005:
        ends = [boot(units, stat, n=GATE_N, seed=s)[0 if end == "lower" else 1] for s in range(1, 21)]
        out["end_over_20_seeds"] = [min(ends), max(ends)]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--collect", required=True)
    a = ap.parse_args()
    S = json.load(open(os.path.join(a.collect, "collect-summary.json")))
    items = {x["key"]: x for x in load(a.collect, "items.jsonl")}
    pairs = load(a.pilot, "pairs.jsonl")
    bites = load(a.pilot, "bites.jsonl")
    pairs = [p for p in pairs if p["id"] + ":P" in items]
    bites = [b for b in bites if b["id"] + ":P" in items]
    out, fired = {}, {}

    # ---------- the code checks
    c = S["checks"]
    fired["noise floor above 0.01, identity or bypass fails"] = not (c["identity_pass"] and c["bypass_pass"]) or c["noise_floor"] > 0.01
    out["checks"] = c

    # ---------- baseline checks (design, section 5)
    rule_kinds = sorted({p["rule_kind"] for p in pairs})
    need = {}
    for rk in rule_kinds:
        xs = [items[p["id"] + ":P"]["without_rule"]["right"] for p in pairs if p["rule_kind"] == rk and "without_rule" in items[p["id"] + ":P"]]
        need[rk] = {"accuracy_without_rule": statistics.mean(xs) if xs else None,
                    "rule_needed": (statistics.mean(xs) <= CHANCE + 0.10) if xs else None}
    out["rule_is_needed"] = need
    keep_kinds = [rk for rk in rule_kinds if need[rk]["rule_needed"]]

    # baseline checks (design version 0.14, section 5; specification, section 19, item 8)
    right = lambda x: x["right"] == 1.0     # a tie is not right here
    rows = []
    for p in pairs:
        P, R = items[p["id"] + ":P"], items[p["id"] + ":R"]
        rows.append({"id": p["id"], "rk": p["rule_kind"], "qk": p["routine_kind"], "rule_content": p["rule_content"],
                     "donors": P["n_donors"],
                     "confident": P["unaltered"]["margin"] >= MARGIN_MIN and R["unaltered"]["margin"] >= MARGIN_MIN,
                     "R_base_right": right(R["baseline"]), "R_full_right": right(R["unaltered"]),
                     "P_base_right": right(P["baseline"]), "P_full_right": right(P["unaltered"]),
                     "R_below_bar": right(R["baseline"]) and right(R["unaltered"]) and R["baseline"]["margin"] >= MARGIN_MIN
                                    and R["unaltered"]["margin"] < MARGIN_MIN,
                     "P_below_bar": right(P["baseline"]) and right(P["unaltered"]) and P["baseline"]["margin"] >= MARGIN_MIN
                                    and P["unaltered"]["margin"] < MARGIN_MIN,
                     "mP": P["unaltered"]["margin"], "mR": R["unaltered"]["margin"]})
    strikes, table = {}, {}
    for (rk, qk) in sorted({(r["rk"], r["qk"]) for r in rows}):
        g = [r for r in rows if (r["rk"], r["qk"]) == (rk, qk)]
        conf = [r for r in g if r["confident"]]
        baseR = [r for r in g if r["R_base_right"]]
        baseP = [r for r in g if r["P_base_right"]]
        intR = sum(not r["R_full_right"] for r in baseR)
        intP = sum(not r["P_full_right"] for r in baseP)
        too_few = len(conf) < 3
        struck = too_few or not baseR or not baseP or intR > FIFTH * len(baseR) or intP > FIFTH * len(baseP)
        strikes[f"{rk}+{qk}"] = {"pairs": len(g), "confident": len(conf), "fewer_than_three_confident": too_few,
                                 "routine_right_without_rule": len(baseR), "routine_interfered": intR,
                                 "rule_right_without_routine_fact": len(baseP), "rule_interfered": intP,
                                 "routine_fell_below_bar_staying_right": sum(r["R_below_bar"] for r in g),
                                 "rule_fell_below_bar_staying_right": sum(r["P_below_bar"] for r in g),
                                 "median_margins": {"routine_full": statistics.median(r["mR"] for r in g),
                                                    "rule_full": statistics.median(r["mP"] for r in g)},
                                 "struck": struck}
        if rk in keep_kinds:
            table.setdefault(rk, [])
            if not struck:
                table[rk].append(qk)
    out["strike_counts"] = strikes
    out["pairing_table"] = table
    surviving_kinds = [rk for rk in keep_kinds if len(table.get(rk, [])) >= 2]
    fired["fewer than three rule kinds, or a rule kind with one routine kind or none (after both checks and the minimum of three)"] = \
        len(surviving_kinds) < 3 or any(len(table.get(rk, [])) <= 1 for rk in keep_kinds)

    kept = [r for r in rows if r["rk"] in keep_kinds and r["qk"] in table.get(r["rk"], []) and r["confident"]
            and r["R_full_right"] and r["P_full_right"] and r["donors"] > 0]  # interfered items are not right
    out["pairs_after_baseline_checks"] = {rk: sum(r["rk"] == rk for r in kept) for rk in keep_kinds}
    out["pairs_dropped_no_donor"] = [r["id"] for r in rows if r["donors"] == 0]

    # ---------- margin matching (design, section 5)
    after_margin, margin_report = [], {}
    for rk in keep_kinds:
        rs = [r for r in kept if r["rk"] == rk]
        n0 = len(rs)
        rs = sorted(rs, key=lambda r: r["id"])
        dropped = []
        while rs and abs(statistics.mean(r["mR"] for r in rs) - statistics.mean(r["mP"] for r in rs)) > 0.5:
            sign = 1 if statistics.mean(r["mR"] for r in rs) > statistics.mean(r["mP"] for r in rs) else -1
            worst = max(rs, key=lambda r: sign * (r["mR"] - r["mP"]))
            rs.remove(worst)
            dropped.append(worst["id"])
        margin_report[rk] = {"before": n0, "dropped": len(dropped), "limit_third": n0 / 3, "over_limit": len(dropped) > n0 / 3}
        after_margin += rs
    out["margin_matching"] = margin_report
    fired["margin matching removes more than a third of a rule kind"] = any(v["over_limit"] for v in margin_report.values())

    # ---------- swap-size matching, for each method
    def size(key, meth):
        it = items[key]
        return statistics.mean(it["swap_size"]) if meth == "swap" else it["avg_size"]
    size_report = {}
    for meth in ("swap", "avg"):
        size_report[meth] = {}
        for rk in keep_kinds:
            rs = [r for r in after_margin if r["rk"] == rk]
            n0 = len(rs)
            dropped = []
            def ratio(rs_):
                return statistics.mean(size(r["id"] + ":R", meth) for r in rs_) / statistics.mean(size(r["id"] + ":P", meth) for r in rs_)
            r0 = ratio(rs) if rs else None
            while rs and not (0.90 <= ratio(rs) <= 1.10):
                sign = 1 if ratio(rs) > 1 else -1
                worst = max(rs, key=lambda r: sign * (size(r["id"] + ":R", meth) - size(r["id"] + ":P", meth)))
                rs.remove(worst)
                dropped.append(worst["id"])
            size_report[meth][rk] = {"before": n0, "ratio_before": r0, "ratio_after": ratio(rs) if rs else None,
                                     "dropped": len(dropped), "limit_tenth": n0 / 10, "over_limit": len(dropped) > n0 / 10}
    out["swap_size_matching"] = size_report
    fired["swap-size matching needs more than a tenth of a rule kind (the dose question, RT-345)"] = \
        any(v["over_limit"] for m in size_report.values() for v in m.values())

    # ---------- neutral set: damage of the two methods, the factor-of-two rule, damage matching, normal range
    nm = S["neutral_main"]
    out["neutral_damage"] = {k: v["damage"] for k, v in nm.items()}
    r2 = max(nm["swap"]["damage"], nm["avg"]["damage"]) / min(nm["swap"]["damage"], nm["avg"]["damage"])
    rf = max(nm["swap"]["damage"], nm["fallback"]["damage"]) / min(nm["swap"]["damage"], nm["fallback"]["damage"])
    out["factor_of_two"] = {"swap_vs_average": r2, "average_trips": r2 > 2, "swap_vs_fallback": rf, "fallback_trips": rf > 2}
    fired["both the average and its fallback differ from the swap by more than a factor of two (choice 5: the test stops)"] = r2 > 2 and rf > 2
    if "avg_reply_built" in nm:
        ra = max(nm["avg"]["damage"], nm["avg_reply_built"]["damage"]) / min(nm["avg"]["damage"], nm["avg_reply_built"]["damage"])
        out["factor_of_two"]["user_built_vs_reply_built_average"] = ra
        fired["the two averages differ by more than a factor of two (design version 0.14)"] = ra > 2
    if "one_nat_check" in S:
        out["one_nat_check"] = S["one_nat_check"]
        fired["the reply rendering's loss is more than 1 nat a token above plain text's"] = not S["one_nat_check"]["passes"]
    out["damage_matching"] = {k: {kk: vv for kk, vv in v.items() if kk not in ("ppl_rise_draws",)} for k, v in S["factors"].items()}
    fired["a comparison cannot be matched (bracketed, and within 20%)"] = not all(v.get("matched", v["within_20pct"]) for v in S["factors"].values())
    nr = {}
    for meth in ("swap", "avg"):
        b = S["normal_range"][meth]["bound"]
        comp = {k: statistics.mean(v["ppl_rise_draws"]) for k, v in S["factors"].items() if k.endswith(meth)}
        nr[meth] = {"bound": b, "main_rise": nm[meth]["ppl_rise"], "main_within": nm[meth]["ppl_rise"] <= b,
                    "room": b - nm[meth]["ppl_rise"], "comparisons_rise": comp,
                    "comparisons_within": {k: v <= b for k, v in comp.items()}}
    out["normal_range"] = nr
    fired["the main removal or a comparison fails the normal-range check"] = \
        not all(v["main_within"] and all(v["comparisons_within"].values()) for v in nr.values())

    # ---------- the bites check's one-pass condition, pooled and per kind (resampled within kind, by fact in unit)
    def units_for(bs, f):
        units = {}
        for b in bs:
            c_ = ast.literal_eval(b["rule_content"])
            key = ("unit", tuple(sorted((c_[3], c_[4])))) if b["rule_kind"] == "unit" else b["id"]
            units.setdefault(b["rule_kind"], {}).setdefault(key, []).append(f(b))
        return {k: list(v.values()) for k, v in units.items()}
    bites = [b for b in bites if items[b["id"] + ":P"]["n_donors"] > 0]
    f1 = lambda b: norm_loss(items[b["id"] + ":P"]["unaltered"]["right"], items[b["id"] + ":P"]["passes_1"]["right"])
    one_pass = {}
    for name, sel in (("pooled", bites), ("op", [b for b in bites if b["rule_kind"] == "op"]),
                      ("unit", [b for b in bites if b["rule_kind"] == "unit"])):
        if not sel:
            continue
        vals = [f1(b) for b in sel]
        g = gate_interval(units_for(sel, f1), statistics.mean, 0.15, "lower")
        one_pass[name] = {"items": len(sel), "cost": statistics.mean(vals), "per_item_sd": statistics.pstdev(vals),
                          **g, "lower_end_at_least_0.15": g["interval"][0] >= 0.15}
    out["bites_one_pass"] = one_pass
    fired["the bites check's one-pass condition fails (every outcome not testable)"] = not one_pass.get("pooled", {}).get("lower_end_at_least_0.15", False)
    # the branch choice's inputs (specification, section 19, item 7): spreads of the swap's own loss on bites items
    own = {}
    for kind in ("op", "unit"):
        sel = [b for b in bites if b["rule_kind"] == kind and items[b["id"] + ":P"].get("swap")]
        if sel:
            vals = [norm_loss(items[b["id"] + ":P"]["unaltered"]["right"],
                              statistics.mean(s["right"] for s in items[b["id"] + ":P"]["swap"])) for b in sel]
            own[kind] = {"items": len(sel), "per_item_sd": statistics.pstdev(vals)}
    out["bites_swap_own_loss_spread"] = own

    # ---------- the change ratio on the bites items, each method, against 0.5
    cr = {}
    for meth in ("swap", "avg"):
        vals = []
        for b in bites:
            it = items[b["id"] + ":P"]
            if meth == "swap" and it.get("swap_ratio"):
                vals.append(statistics.mean(it["swap_ratio"]))
            elif meth == "avg":
                vals.append(it["avg_ratio"])
        if vals:
            cr[meth] = {"mean": statistics.mean(vals), "sd": statistics.pstdev(vals), "min": min(vals), "max": max(vals),
                        "distance_from_0.5": statistics.mean(vals) - 0.5, "below_0.5": statistics.mean(vals) < 0.5}
    out["change_ratio_bites"] = cr
    fired["the change ratio is below 0.5 under either method (outcome F out of reach)"] = any(v["below_0.5"] for v in cr.values())

    # ---------- what the sample-size simulation needs: spreads, and the comparisons' losses (no main-removal gap)
    sim = {}
    for meth in ("swap", "avg"):
        for cell in ("P", "R"):
            keys = [r["id"] + ":" + cell for r in after_margin]
            if not keys:
                continue
            def main_loss(k):
                it = items[k]
                alt = statistics.mean(s["right"] for s in it["swap"]) if meth == "swap" else it["avg"]["right"]
                return norm_loss(it["unaltered"]["right"], alt)
            def comp_loss(k):
                it = items[k]
                return norm_loss(it["unaltered"]["right"], statistics.mean(s["right"] for s in it[f"loop_{meth}"]))
            sim[f"{meth}_{cell}"] = {"items": len(keys), "main_loss_sd": statistics.pstdev([main_loss(k) for k in keys]),
                                     "comparison_loss_mean": statistics.mean([comp_loss(k) for k in keys]),
                                     "comparison_loss_sd": statistics.pstdev([comp_loss(k) for k in keys])}
    out["simulation_inputs"] = sim
    out["ties_at_unaltered"] = sum(1 for it in items.values() if 0 < it["unaltered"]["right"] < 1)

    out["return_to_john"] = fired
    json.dump(out, open(os.path.join(a.collect, "step4b-analysis.json"), "w"), indent=1)
    for k, v in fired.items():
        print(("FIRED      " if v else "not fired  ") + k)


if __name__ == "__main__":
    main()
