#!/usr/bin/env python3
"""Two $0 checks behind the proposed dispositions of the outside reviews of
successor proposal version 4 (parts B and C of
docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements-method.md).

Loads no model and imports no project code. Reads committed records only:
  out-controls-rerun/measure_<arm>_seed<s>.json   (part B)
  out-controls-rerun/summary.json                 (part C, which seeds read)
  out-repairs/gate_base.json                      (part C)
  out-lesion-content-check/lesion_content_check.json  (part C)
Writes out-tier2-dispositions-check/check.json and prints a report.

Run from anywhere:
  python3 experiments/rehearsal-successor-measure/src/tier2_dispositions_check.py
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "out-tier2-dispositions-check")
ARMS, SEEDS = ("T", "C", "M", "F"), (0, 1, 2)
ROOM = 0.018          # version 4, section 6.4, item 3
PAIRS = 800           # fresh matched pairs, version 4, section 9


def load(rel):
    with open(os.path.join(ROOT, rel)) as f:
        return json.load(f)


def binom_pmf(n, k, q):
    return math.comb(n, k) * q ** k * (1 - q) ** (n - k)


def p_flag(n, q, p):
    """Chance the no-transplant rule flags: |k/n - (1-p)/7| > ROOM, k ~ Bin(n, q)."""
    centre = (1 - p) / 7
    return sum(binom_pmf(n, k, q) for k in range(n + 1) if abs(k / n - centre) > ROOM + 1e-12)


def part_b():
    rows = {}
    print("PART B. The no-transplant check's assumption about errors (A9)")
    print("arm/seed | p (own-directed) | U (untouched) | formula (committed) | (1-p)/7 recomputed | "
          "erring trials | share of errors on donor's answer U/(1-p) | review's-case gap | > 0.018")
    for arm in ARMS:
        for s in SEEDS:
            pr = load(f"out-controls-rerun/measure_{arm}_seed{s}.json")["primary"]
            p = pr["reading"]["arm_own_accuracy"]
            u = pr["no_transplant"]["rate"]
            f_c = pr["no_transplant"]["formula"]
            f_r = (1 - p) / 7
            err = PAIRS * (1 - p)
            share = u / (1 - p) if p < 1 else None
            gap = (1 - p) / 3 - (1 - p) / 7
            rows[f"{arm}/{s}"] = dict(p=p, untouched=u, formula_committed=f_c, formula_recomputed=f_r,
                                      formula_equal=abs(f_c - f_r) < 1e-12, erring_trials=err,
                                      share_on_donor=share, review_case_gap=gap,
                                      review_case_exceeds=gap > ROOM)
            print(f"{arm}/{s} | {p:.5f} | {u:.5f} | {f_c:.5f} | {f_r:.5f} | {err:.1f} | "
                  f"{'n/a' if share is None else f'{share:.4f}'} | {gap:.4f} | {gap > ROOM}")
    p_break = 1 - ROOM / (1 / 3 - 1 / 7)
    print(f"review's case exceeds 0.018 for every p below {p_break:.4f}")
    power = {}
    for p in (0.2633, 0.56):
        power[f"broken_pairing_flagged_at_p={p}"] = p_flag(PAIRS, 1 / 8, p)
    for p in (0.2633, 0.56, 0.8):
        power[f"healthy_even_errors_withheld_at_p={p}"] = p_flag(PAIRS, (1 - p) / 7, p)
    for p in (0.56, 0.8):
        power[f"healthy_review_case_withheld_at_p={p}"] = p_flag(PAIRS, (1 - p) / 3, p)
    for k, v in power.items():
        print(f"  {k}: {v:.4f}")
    return dict(rows=rows, review_case_exceeds_below_p=p_break, power_800_pairs=power)


def part_c():
    print("\nPART C. Separate majorities against joint seeds, on the toy gates (A10)")
    gate = load("out-repairs/gate_base.json")["runs"]
    les = load("out-lesion-content-check/lesion_content_check.json")["models"]
    summ = load("out-controls-rerun/summary.json")["arms"]
    res = {}
    for arm in ARMS:
        per_seed = {}
        for s in SEEDS:
            g = gate[f"{arm}/base/{s}"]
            conds = dict(own=bool(g["own_clears"]))
            if arm == "F":
                conds.update(other=bool(g["other_clears"]),
                             collapse=bool(g["lesion_collapses_own"]),
                             ownership_free_line=bool(les[f"F/{s}"]["holds_own"]))
            o = summ[f"{arm}/{s}"]
            pr = o.get("primary")
            reads = bool(pr and not pr["described_only"] and pr["reading"]["degree"] is not None)
            per_seed[s] = dict(conditions=conds, all_pass=all(conds.values()), reads=reads)
        names = list(per_seed[0]["conditions"])
        separate = all(sum(per_seed[s]["conditions"][c] for s in SEEDS) >= 2 for c in names)
        joint = sum(per_seed[s]["all_pass"] for s in SEEDS) >= 2
        both = [s for s in SEEDS if per_seed[s]["all_pass"] and per_seed[s]["reads"]]
        res[arm] = dict(per_seed=per_seed, gate_separate_majorities=separate, gate_joint=joint,
                        seeds_passing_gate_and_reading=both, verdict_differs=separate != joint)
        print(f"{arm}: " + "; ".join(
            f"seed {s} " + ",".join(f"{c}={'P' if v else 'F'}" for c, v in per_seed[s]['conditions'].items())
            + f" reads={per_seed[s]['reads']}" for s in SEEDS)
            + f" | separate majorities: {separate} | joint: {joint} | differs: {separate != joint}"
            + f" | seeds passing the gate and reading: {both}")
    return res


def main():
    out = dict(part_b=part_b(), part_c=part_c())
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "check.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote {os.path.join(OUT, 'check.json')}")


if __name__ == "__main__":
    main()
