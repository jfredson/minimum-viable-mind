"""A free check, 2026-11-23, on John's "Check margin scoring": would scoring each item by its margin, in place of
right or wrong, give the loop removal test the power it needs? Run on the Mac, on step 4b's recorded data.

    python3 -I src/margin_power_check.py --analysis <the step-4b analysis json from the code test> \
        --items step4b-run-2026-11-23/items.jsonl --pilot batteries/pilot-v0.12 --sims 1000

How the two scales are compared. A margin and a right-or-wrong score are on different scales, so the
design's thresholds (a gap of 0.20 and δ of 0.10, on the normalised accuracy scale) cannot be carried over
as numbers. They are carried over as shares of what one pass costs. On the surviving pairs, the prompt-rule
cell's one-pass cost is measured on both scales: accuracy (normalised) and margin (nats). Every margin loss is
divided by the ratio of the two, k = margin cost / accuracy cost, so that a gap of 0.20 in these units is the
same share of what the passes supply on either scale. The bites items get their own ratio. Then the step-4b
simulation's own code is run on the converted spreads.

This is a check of the idea, not a design. Margins have long tails, which the simulation's normal draws
smooth over; the report states the tail.
"""
import argparse
import copy
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import step4b_simulate as sim  # noqa: E402

CHANCE = 0.2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--analysis", required=True)
    ap.add_argument("--items", required=True)
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--sims", type=int, default=1000)
    a = ap.parse_args()
    An = json.load(open(a.analysis))
    items = {x["key"]: x for x in map(json.loads, open(a.items))}
    pairs = [json.loads(l) for l in open(os.path.join(a.pilot, "pairs.jsonl"))]
    bites = [json.loads(l) for l in open(os.path.join(a.pilot, "bites.jsonl"))]
    table = An["pairing_table"]
    kept = [p for p in pairs if p["routine_kind"] in table.get(p["rule_kind"], [])
            and items[p["id"] + ":P"]["unaltered"]["margin"] >= 2.2 and items[p["id"] + ":R"]["unaltered"]["margin"] >= 2.2
            and items[p["id"] + ":P"]["n_donors"] > 0]
    out = {"pairs_used": len(kept)}

    acc = lambda x: x["right"]
    mar = lambda x: x["margin"]
    # the conversion: the prompt-rule cell's one-pass cost on each scale
    c_acc = statistics.mean((acc(items[p["id"] + ":P"]["unaltered"]) - acc(items[p["id"] + ":P"]["passes_1"])) / (1 - CHANCE) for p in kept)
    c_mar = statistics.mean(mar(items[p["id"] + ":P"]["unaltered"]) - mar(items[p["id"] + ":P"]["passes_1"]) for p in kept)
    k = c_mar / c_acc if c_acc else float("nan")
    out["conversion"] = {"one_pass_cost_accuracy": c_acc, "one_pass_cost_margin_nats": c_mar, "k": k}

    def loss(it, alt_vals, scale):
        if scale == "acc":
            return (acc(it["unaltered"]) - statistics.mean(alt_vals)) / (1 - CHANCE)
        return (mar(it["unaltered"]) - statistics.mean(alt_vals)) / k

    inputs = {}
    for scale in ("acc", "mar"):
        f = acc if scale == "acc" else mar
        for meth in ("swap", "avg"):
            for cell in ("P", "R"):
                its = [items[p["id"] + ":" + cell] for p in kept]
                main = [loss(it, [f(s) for s in it["swap"]] if meth == "swap" else [f(it["avg"])], scale) for it in its]
                comp = [loss(it, [f(s) for s in it[f"loop_{meth}"]], scale) for it in its]
                inputs.setdefault(scale, {})[f"{meth}_{cell}"] = {
                    "items": len(its), "main_loss_sd": statistics.pstdev(main),
                    "comparison_loss_mean": statistics.mean(comp), "comparison_loss_sd": statistics.pstdev(comp)}
        # long tails of the swap's margin loss, in converted units
    tails = sorted(loss(items[p["id"] + ":P"], [mar(s) for s in items[p["id"] + ":P"]["swap"]], "mar") for p in kept)
    out["margin_swap_loss_P_quantiles"] = {q: tails[int(q * (len(tails) - 1))] for q in (0.05, 0.25, 0.5, 0.75, 0.95)}
    out["inputs"] = inputs

    # outcome A power on each scale, through the step-4b simulation's own code
    shares = {}
    for rk, qks in table.items():
        for qk in qks:
            shares[(rk, qk)] = max(1, An["strike_counts"].get(f"{rk}+{qk}", {}).get("confident", 1))
    op_unit_share = sum(v for (rk, _), v in shares.items() if rk in ("op", "unit")) / sum(shares.values())
    scenarios = {"even": lambda rk: 0.20, "by_kind": lambda rk: (0.20 / op_unit_share) if rk in ("op", "unit") else 0.0}
    out["A_power"] = {}
    for scale in ("acc", "mar"):
        for rho in (0.0, 0.3):
            for sc, gap_on in scenarios.items():
                res = {}
                for n in (80, 140, 200, 260):
                    import random
                    rng = random.Random(f"{scale}-{rho}-{sc}-{n}")
                    hits = sum(all(sim.outcome_with_renames(sim.draw_set(n, shares, inputs[scale], meth, gap_on, rho, rng, 30)) == "A"
                                   for meth in ("swap", "avg")) for _ in range(a.sims))
                    res[n] = hits / a.sims
                out["A_power"][f"{scale}_rho_{rho}_{sc}"] = res
                print(scale, rho, sc, res, flush=True)

    # the bites branch choice on each scale (margins converted by the bites' own ratio)
    bk = [b for b in bites if items[b["id"] + ":P"]["n_donors"] > 0]
    out["bites"] = {}
    for scale in ("acc", "mar"):
        An2 = copy.deepcopy(An)
        bo, own = {}, {}
        for kind in ("op", "unit"):
            sel = [items[b["id"] + ":P"] for b in bk if b["rule_kind"] == kind]
            if scale == "acc":
                one = [(acc(it["unaltered"]) - acc(it["passes_1"])) / (1 - CHANCE) for it in sel]
                ow = [(acc(it["unaltered"]) - statistics.mean(acc(s) for s in it["swap"])) / (1 - CHANCE) for it in sel]
            else:
                ca = statistics.mean((acc(it["unaltered"]) - acc(it["passes_1"])) / (1 - CHANCE) for it in sel)
                cm = statistics.mean(mar(it["unaltered"]) - mar(it["passes_1"]) for it in sel)
                kb = cm / ca if ca else float("nan")
                one = [(mar(it["unaltered"]) - mar(it["passes_1"])) / kb for it in sel]
                ow = [(mar(it["unaltered"]) - statistics.mean(mar(s) for s in it["swap"])) / kb for it in sel]
            bo[kind] = {"cost": statistics.mean(one), "per_item_sd": statistics.pstdev(one), "items": len(sel)}
            own[kind] = {"per_item_sd": statistics.pstdev(ow)}
        An2["bites_one_pass"], An2["bites_swap_own_loss_spread"] = bo, own
        out["bites"][scale] = sim.branch_choice(An2, a.sims, 29)
        print(scale, "bites", json.dumps({k: v for k, v in out["bites"][scale].items() if k != "inputs"}), flush=True)
    json.dump(out, open(os.path.join(os.path.dirname(a.analysis), "margin-power-check.json"), "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
