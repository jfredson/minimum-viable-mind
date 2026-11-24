"""Step 4b of the loop removal test: the committed sample-size simulation (design, section 5, "Sample size" and
"The simulation's conditions"; section 6). Written and committed on 2026-11-23, while the collection ran and
before its results were opened.

    python3 -I src/step4b_simulate.py --analysis <out dir>/step4b-analysis.json [--sims 1000]

Inputs, all from step4b-analysis.json:
- for each method and cell, the spread of the main removal's per-item loss, and the random comparison's mean
  loss and spread;
- the surviving pairs per pairing, which set the kind shares;
- the bites check's one-pass cost per kind, and its per-item spread.

What it simulates, for each test-half size from 80 to 300 pairs:
- **A after every rename.** The chance that a true normalised gap of 0.20 is read as outcome A under both
  methods, after the checks that can rename an A: one kind left out in turn ("Depends on one kind"), with rule
  kinds and routine kinds. Two scenarios are run:
  - "even": the gap is spread evenly over every pairing;
  - "by kind": the gap sits on the operator and unit pairs only, as the trials' pass gains suggest (RT-445).

  The excess on the prompt-rule cell is 0.20 there and 0 on the lookup pairs, scaled so that the cell's mean
  excess is still 0.20.
- **The bites check,** at the bites set's size of 100 per kind:
  - the one-pass condition, "the interval's lower end at or above 0.15", at the measured one-pass cost;
  - "bites", when the true excess is three quarters of the one-pass cost;
  - "does not bite" (own loss below a quarter of the one-pass cost in each kind), when the true own loss is 0.

Assumptions, stated rather than measured:
- Items are scored right or wrong; a removal's per-item loss is drawn as a normal variable with the measured
  spread, and the comparison's as the 20-draw average.
- **Shared facts in the unit kind.** Items that share a multiplication fact are given a shared random part,
  carrying a share RHO of the variance. The run reports RHO of 0, 0.3 and 0.6, because RHO is not measured.
  Intervals resample by fact there, so the interval widens with RHO.
- Intervals are 95%, by a normal approximation to the resampling interval.
- The two methods are drawn independently, which is cautious: they share items, so in truth they agree more
  often.
- "Not specific" is not simulated. Under the null outside the loop, it renames an A in about 2.5% of runs, a
  rate the report states rather than models.
"""
import argparse
import json
import math
import random
import statistics

DELTA = 0.10
Z = 1.959964
SIZES = list(range(80, 301, 20))


def ci(vals, clusters=None):
    """Mean and a normal-approximation 95% interval; clusters: list of cluster ids for resampling by cluster."""
    n = len(vals)
    m = sum(vals) / n
    if clusters is None:
        sd = statistics.pstdev(vals) if n > 1 else 0.0
        se = sd / math.sqrt(n) if n else float("inf")
    else:
        groups = {}
        for v, c in zip(vals, clusters):
            groups.setdefault(c, []).append(v - m)
        g = len(groups)
        se = math.sqrt(sum(sum(x) ** 2 for x in groups.values())) / n if g > 1 else float("inf")
    return m, m - Z * se, m + Z * se


def classify(P, R, cP, cR):
    """Section 6, stage two, on excess losses per pair (P and R lists, same order) with cluster ids."""
    G = [p - r for p, r in zip(P, R)]
    g, glo, ghi = ci(G, cP)
    p, plo, phi = ci(P, cP)
    r, rlo, rhi = ci(R, cR)
    if g >= DELTA and glo > 0 and plo > 0 and rhi < DELTA:
        return "A"
    if g <= -DELTA and ghi < 0 and rlo > 0 and phi < DELTA:
        return "B"
    if plo > 0 and rlo > 0:
        return "C"
    if phi < DELTA and rhi < DELTA:
        return "D"
    return "E"


def draw_set(n, shares, inp, meth, gap_on, rho, rng, fact_sizes):
    """One simulated test half: per pair (rule kind, routine kind, cluster id, P excess, R excess)."""
    rows = []
    pairings = list(shares)
    weights = [shares[k] for k in pairings]
    sdP, sdR = inp[f"{meth}_P"]["main_loss_sd"], inp[f"{meth}_R"]["main_loss_sd"]
    cP, cR = inp[f"{meth}_P"]["comparison_loss_sd"] / math.sqrt(20), inp[f"{meth}_R"]["comparison_loss_sd"] / math.sqrt(20)
    fact_effect = {}
    for i in range(n):
        rk, qk = rng.choices(pairings, weights)[0]
        if rk == "unit":
            fid = ("unit", rng.randrange(fact_sizes))
            if fid not in fact_effect:
                fact_effect[fid] = (rng.gauss(0, math.sqrt(rho) * sdP), rng.gauss(0, math.sqrt(rho) * sdR))
            fe = fact_effect[fid]
        else:
            fid, fe = ("pair", i), (0.0, 0.0)
        mu_p = gap_on(rk)
        ep = mu_p + fe[0] + rng.gauss(0, math.sqrt(1 - rho if rk == "unit" else 1) * sdP) - rng.gauss(0, cP)
        er = 0.0 + fe[1] + rng.gauss(0, math.sqrt(1 - rho if rk == "unit" else 1) * sdR) - rng.gauss(0, cR)
        rows.append((rk, qk, fid, ep, er))
    return rows


def outcome_with_renames(rows):
    P = [r[3] for r in rows]
    R = [r[4] for r in rows]
    C = [r[2] for r in rows]
    o = classify(P, R, C, C)
    if o != "A":
        return o
    for key in sorted({("rk", r[0]) for r in rows} | {("qk", r[1]) for r in rows}):
        sub = [r for r in rows if (r[0] if key[0] == "rk" else r[1]) != key[1]]
        if len(sub) < 10:
            continue
        o2 = classify([r[3] for r in sub], [r[4] for r in sub], [r[2] for r in sub], [r[2] for r in sub])
        if o2 in ("B", "C", "D"):
            return "Depends on one kind"
    return "A"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--analysis", required=True)
    ap.add_argument("--sims", type=int, default=1000)
    a = ap.parse_args()
    An = json.load(open(a.analysis))
    inp = An["simulation_inputs"]
    after = {k: v for k, v in An["strike_counts"].items()}
    table = An["pairing_table"]
    shares = {}
    for rk, qks in table.items():
        for qk in qks:
            shares[(rk, qk)] = max(1, after.get(f"{rk}+{qk}", {}).get("confident", 1))
    fact_sizes = 30  # about the number of unit facts per half (specification, section 17, item 6)
    out = {"inputs_used": {"pairings": {f"{k[0]}+{k[1]}": v for k, v in shares.items()}, "fact_pool": fact_sizes},
           "A_power": {}, "bites": {}}
    op_unit_share = sum(v for (rk, _), v in shares.items() if rk in ("op", "unit")) / sum(shares.values())
    scenarios = {"even": lambda rk: 0.20,
                 "by_kind": lambda rk: (0.20 / op_unit_share) if rk in ("op", "unit") else 0.0}
    for rho in (0.0, 0.3, 0.6):
        for sc, gap_on in scenarios.items():
            res = {}
            for n in SIZES:
                rng = random.Random(f"{rho}-{sc}-{n}")
                hits = 0
                for _ in range(a.sims):
                    both = all(outcome_with_renames(draw_set(n, shares, inp, meth, gap_on, rho, rng, fact_sizes)) == "A"
                               for meth in ("swap", "avg"))
                    hits += both
                res[n] = hits / a.sims
            smallest = next((n for n in SIZES if res[n] >= 0.80), None)
            out["A_power"][f"rho_{rho}_{sc}"] = {"power_by_pairs": res, "smallest_for_80pct": smallest}
            print(f"rho {rho} {sc}: smallest test half for 80% = {smallest}", flush=True)

    # the bites check at 100 per kind
    bo = An["bites_one_pass"]
    rng = random.Random(7)
    for kind in ("op", "unit"):
        if kind not in bo:
            continue
        cost = bo[kind]["cost"]
        lo, hi = bo[kind]["interval"]
        sd_item = (hi - lo) / (2 * Z) * math.sqrt(bo[kind]["items"])  # per-item spread recovered from the pilot interval
        n = 100
        se = sd_item / math.sqrt(n)
        p_onepass = sum(rng.gauss(cost, se) - Z * se >= 0.15 for _ in range(a.sims)) / a.sims
        p_bites = sum((lambda e: e >= 0.5 * cost and e - Z * se > 0)(rng.gauss(0.75 * cost, se)) for _ in range(a.sims)) / a.sims
        p_notbite = sum((rng.gauss(0.0, se) + Z * se) < 0.25 * cost for _ in range(a.sims)) / a.sims
        out["bites"][kind] = {"one_pass_cost_pilot": cost, "per_item_sd": sd_item, "at_items": n,
                              "p_one_pass_condition": p_onepass, "p_bites_at_three_quarters": p_bites,
                              "p_does_not_bite_at_zero": p_notbite}
    json.dump(out, open(a.analysis.replace("step4b-analysis.json", "step4b-simulation.json"), "w"), indent=1, default=str)
    print(json.dumps(out["bites"], indent=1))


if __name__ == "__main__":
    main()
