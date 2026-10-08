#!/usr/bin/env python3
"""Check 1 of the paired check of pull request 101: the A9 arithmetic,
recomputed from the committed toy records and from first principles.

Independent of the author: does not import or read
`tier2_dispositions_check.py` or its `check.json`. Reads only the twelve
committed controls re-run records
`experiments/rehearsal-successor-measure/out-controls-rerun/measure_<arm>_seed<s>.json`.
Every probability is computed in exact rational arithmetic (fractions.Fraction),
not floating point, so no tolerance is needed at the 0.018 boundary.

Run from the repository root:
  python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-06-successor-v4-tier2-dispositions-check-scripts/a9_recompute.py
"""
import json
import math
import os
from fractions import Fraction as Fr

ROOT = os.getcwd()
REC = os.path.join(ROOT, "experiments/rehearsal-successor-measure/out-controls-rerun")
N = 800                     # fresh matched pairs, version 4 section 9
ROOM = Fr(18, 1000)         # version 4 section 6.4 item 3
BAR = Fr(790, 3000)         # learn-both bar, 790 of 3,000


def flag_prob(n, q, centre):
    """P(|K/n - centre| > ROOM) for K ~ Binomial(n, q), exactly."""
    tot = Fr(0)
    for k in range(n + 1):
        if abs(Fr(k, n) - centre) > ROOM:
            tot += math.comb(n, k) * q ** k * (1 - q) ** (n - k)
    return tot


print("== Part 1: the twelve toy records")
print("arm/seed | p | U (rate) | committed formula | (1-p)/7 recomputed | equal | erring trials | "
      "share of errors on donor's answer | review-case gap (1-p)(1/3-1/7) | gap > 0.018")
shares = {}
for arm in "TCMF":
    for s in range(3):
        d = json.load(open(os.path.join(REC, f"measure_{arm}_seed{s}.json")))["primary"]
        p = d["reading"]["arm_own_accuracy"]
        u = d["no_transplant"]["rate"]
        fc = d["no_transplant"]["formula"]
        fr = (1 - p) / 7
        err = round(N * (1 - p))
        hits = round(N * u)
        share = None if err == 0 else Fr(hits, err)
        if share is not None:
            shares[f"{arm}/{s}"] = share
        gap = (1 - p) * (1 / 3 - 1 / 7)
        print(f"{arm}/{s} | {p:.5f} | {u:.5f} | {fc:.6f} | {fr:.6f} | {abs(fc - fr) < 1e-15} | {err} | "
              f"{'no errors' if share is None else f'{hits}/{err} = {float(share):.4f}'} | {gap:.4f} | {gap > 0.018}")
lo = min(shares, key=shares.get)
hi = max(shares, key=shares.get)
print(f"share range over the nine models with errors: {float(shares[lo]):.4f} ({lo}) to "
      f"{float(shares[hi]):.4f} ({hi}); even spread would be 1/7 = {1/7:.4f}; review's case 1/3")

print("\n== Part 2: the review's case, exactly")
p = Fr(8, 10)
print(f"(1-p)/3 at p=0.8: {float((1-p)/3):.4f}; (1-p)/7: {float((1-p)/7):.4f}; "
      f"gap {float((1-p)/3-(1-p)/7):.4f}; over 0.018 by {float((1-p)/3-(1-p)/7-ROOM):.4f}")
p_star = 1 - ROOM / (Fr(1, 3) - Fr(1, 7))
print(f"gap exceeds 0.018 for every p below {p_star} = {float(p_star):.6f}")

print("\n== Part 3: the rule's behaviour on 800 pairs, p treated as known (as the author did)")
rows = [
    ("broken pairing flagged, p = 790/3000 (exact bar)", Fr(1, 8), BAR),
    ("broken pairing flagged, p = 0.2633 (author's rounding)", Fr(1, 8), Fr(2633, 10000)),
    ("broken pairing flagged, p = 0.56", Fr(1, 8), Fr(56, 100)),
    ("healthy, even errors, withheld, p = 0.2633", None, Fr(2633, 10000)),
    ("healthy, even errors, withheld, p = 0.56", None, Fr(56, 100)),
    ("healthy, even errors, withheld, p = 0.8", None, Fr(8, 10)),
    ("healthy, review's case, withheld, p = 0.56", "r", Fr(56, 100)),
    ("healthy, review's case, withheld, p = 0.8", "r", Fr(8, 10)),
]
for label, q, pp in rows:
    centre = (1 - pp) / 7
    qq = centre if q is None else (1 - pp) / 3 if q == "r" else q
    print(f"  {label}: {float(flag_prob(N, qq, centre)):.4f}")
print(f"  version 4's margin at the bar: 1/8 - (1 - 790/3000)/7 - 0.018 = "
      f"{float(Fr(1,8) - (1-BAR)/7 - ROOM):.5f}")

print("\n== Part 4: weakness W11's control 6 figures, traced to the same records")
for arm in "TCMF":
    sv = [json.load(open(os.path.join(REC, f"measure_{arm}_seed{s}.json")))["primary"]["controls"]["6"]
          for s in range(3)]
    print(f"{arm}: same-value moved {[round(x['same_value_moved'], 4) for x in sv]}, "
          f"different-value moved {[round(x['different_value_moved'], 4) for x in sv]}, "
          f"trials {[(x['same_value_trials'], x['different_value_trials']) for x in sv]}")
