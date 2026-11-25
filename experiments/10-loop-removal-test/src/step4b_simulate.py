"""Step 4b of the loop removal test: the committed sample-size simulation, by resampling the pilot's real losses
(design version 0.16; specification, section 20, items 5 to 7). Rewritten 2026-11-23, before the rerun's results
are opened. The earlier version drew from normal curves and divided the comparison's spread by the square root
of 20 twice (RT-510); it is withdrawn.

    python3 -I src/step4b_simulate.py --analysis <out dir>/step4b-analysis.json [--sims 1000]

Inputs, all from step4b-analysis.json: C, the surviving pairs' excesses in units of C with their rooms
(`sim_pairs`), and the bites items' one-pass losses, own losses and excesses in nats (`sim_bites`).

What it reports:
- outcome A's power, under both methods together, after the "depends on one kind" rename, for test halves of
  80 to 300 pairs, with the gap (1.0 C) spread evenly or on the operator and unit kinds only, each item's planted
  gap capped at its room; and the rate of wrong A's when the true gap is 0;
- the bites set's branch choice: both kinds (100 + 100) or unit alone (200).
"""
import argparse
import json
import math
import random
import statistics

DELTA = 0.5      # John's choice 9, in units of C
GAP = 1.0
Z = 1.959964
SIZES = list(range(80, 301, 20))


def ci(vals, clusters):
    """Mean and a normal-approximation 95% interval, resampling by cluster."""
    n = len(vals)
    m = sum(vals) / n
    groups = {}
    for v, c in zip(vals, clusters):
        groups.setdefault(c, []).append(v - m)
    se = math.sqrt(sum(sum(x) ** 2 for x in groups.values())) / n if len(groups) > 1 else float("inf")
    return m, m - Z * se, m + Z * se


def classify(P, R, cl):
    """Design, section 6, stage two, on excesses in units of C."""
    G = [p - r for p, r in zip(P, R)]
    g, glo, ghi = ci(G, cl)
    p, plo, phi = ci(P, cl)
    r, rlo, rhi = ci(R, cl)
    if g >= DELTA and glo > 0 and plo > 0 and rhi < DELTA:
        return "A"
    if g <= -DELTA and ghi < 0 and rlo > 0 and phi < DELTA:
        return "B"
    if plo > 0 and rlo > 0:
        return "C"
    if phi < DELTA and rhi < DELTA:
        return "D"
    return "E"


def with_renames(rows, meth):
    """rows: (rk, qk, cluster, exP, exR) for one method; 'Depends on one kind' renames an A."""
    P, R, C_ = [r[3] for r in rows], [r[4] for r in rows], [r[2] for r in rows]
    o = classify(P, R, C_)
    if o != "A":
        return o
    for key in sorted({("rk", r[0]) for r in rows} | {("qk", r[1]) for r in rows}):
        sub = [r for r in rows if (r[0] if key[0] == "rk" else r[1]) != key[1]]
        if len(sub) < 10:
            continue
        if classify([r[3] for r in sub], [r[4] for r in sub], [r[2] for r in sub]) in ("B", "C", "D"):
            return "Depends on one kind"
    return "A"


def units_of(recs):
    """Resampling units: whole unit facts in the unit kind, single records elsewhere."""
    u = {}
    for i, r in enumerate(recs):
        key = r["fact"] if r["rk"] == "unit" else f"item-{i}"
        u.setdefault(key, []).append(r)
    return list(u.values())


def draw(units, n, rng):
    out, k = [], 0
    while len(out) < n:
        for r in rng.choice(units):
            out.append((r, k))
        k += 1
    return out[:n]


def power(pairs, gap_on, n, sims, seed):
    means = {f"{c}_{m}": statistics.mean(p[f"{c}_{m}"] for p in pairs) for c in ("exP", "exR") for m in ("swap", "avg")}
    units = units_of(pairs)
    rng = random.Random(seed)
    hits = 0
    for _ in range(sims):
        s = draw(units, n, rng)
        ok = True
        for meth in ("swap", "avg"):
            rows = []
            for r, cl in s:
                planted = min(gap_on(r["rk"]), r[f"roomP_{meth}"])
                rows.append((r["rk"], r["qk"], cl, r[f"exP_{meth}"] - means[f"exP_{meth}"] + planted,
                             r[f"exR_{meth}"] - means[f"exR_{meth}"]))
            if with_renames(rows, meth) != "A":
                ok = False
                break
        hits += ok
    return hits / sims


def branch_choice(sim_bites, C, sims):
    """Specification, section 20, item 7."""
    kinds = sorted({b["rk"] for b in sim_bites})
    cost = {k: statistics.mean(b["one_pass"] for b in sim_bites if b["rk"] == k) for k in kinds}
    mown = {k: statistics.mean(b["own"] for b in sim_bites if b["rk"] == k) for k in kinds}
    mex = {k: statistics.mean(b["excess"] for b in sim_bites if b["rk"] == k) for k in kinds}
    units = {k: units_of([b for b in sim_bites if b["rk"] == k]) for k in kinds}
    out = {"inputs": {"C": C, "one_pass_cost_nats": cost}}
    for name, nk in (("both", {"op": 100, "unit": 100}), ("unit_only", {"unit": 200})):
        if any(k not in units for k in nk):
            out[name] = {"possible": False}
            continue
        rng = random.Random(f"branch-{name}")
        pooled_cost = sum(nk[k] * cost[k] for k in nk) / sum(nk.values())
        h1 = h2 = h3 = 0
        for _ in range(sims):
            s = {k: draw(units[k], nk[k], rng) for k in nk}
            # stratified pooled intervals: per-kind cluster-robust standard errors, weighted by share
            def pooled(f):
                m = se2 = 0.0
                tot = sum(nk.values())
                per = {}
                for k, rows in s.items():
                    vals = [f(b, k) for b, _ in rows]
                    mk, lo, hi = ci(vals, [f"{k}-{c}" for _, c in rows])
                    per[k] = (mk, lo, hi)
                    w = len(rows) / tot
                    m += w * mk
                    se2 += (w * (hi - lo) / (2 * Z)) ** 2
                se = math.sqrt(se2)
                return (m, m - Z * se, m + Z * se), per
            (_, lo, _), _ = pooled(lambda b, k: b["one_pass"])
            h1 += lo >= C / 4
            (m, lo, _), _ = pooled(lambda b, k: b["excess"] - mex[k] + 0.75 * cost[k])
            h2 += m >= 0.5 * pooled_cost and lo > 0
            _, per = pooled(lambda b, k: b["own"] - mown[k])
            h3 += all(per[k][2] < 0.25 * cost[k] for k in nk)
        p = {"one_pass": h1 / sims, "bites_at_three_quarters": h2 / sims, "does_not_bite_at_zero": h3 / sims}
        out[name] = {"possible": True, **p, "qualifies": all(v >= 0.80 for v in p.values())}
    out["choice"] = ("both kinds" if out.get("both", {}).get("qualifies") else
                     "unit alone" if out.get("unit_only", {}).get("qualifies") else "neither: the design returns to John")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--analysis", required=True)
    ap.add_argument("--sims", type=int, default=1000)
    a = ap.parse_args()
    An = json.load(open(a.analysis))
    out = {"method": "resampling the pilot's real losses (specification, section 20)", "delta": DELTA, "gap": GAP}
    pairs, C = An.get("sim_pairs", []), (An.get("C") or {}).get("nats")
    if pairs:
        kinds = {p["rk"] for p in pairs}
        share_ou = sum(p["rk"] in ("op", "unit") for p in pairs) / len(pairs)
        scen = {"even": lambda rk: GAP, "op_unit_only": lambda rk: (GAP / share_ou) if rk in ("op", "unit") else 0.0}
        out["rule_kinds_in_pilot"] = sorted(kinds)
        out["A_power"] = {}
        for name, f in scen.items():
            res = {n: power(pairs, f, n, a.sims, f"{name}-{n}") for n in SIZES}
            smallest = next((n for n in SIZES if res[n] >= 0.80), None)
            false_A = power(pairs, lambda rk: 0.0, smallest, a.sims, f"null-{name}") if smallest else None
            out["A_power"][name] = {"power_by_pairs": res, "smallest_for_80pct": smallest, "wrong_A_rate_at_that_size": false_A}
            print(name, "smallest", smallest, "wrong A", false_A, {n: round(v, 3) for n, v in res.items() if n in (80, 140, 200, 260)}, flush=True)
    else:
        print("no surviving pairs: the A-power simulation is skipped")
    if An.get("sim_bites") and C:
        out["bites_branch"] = branch_choice(An["sim_bites"], C, a.sims)
        print(json.dumps({k: v for k, v in out["bites_branch"].items() if k != "inputs"}), flush=True)
    json.dump(out, open(a.analysis.replace("step4b-analysis.json", "step4b-simulation.json"), "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
