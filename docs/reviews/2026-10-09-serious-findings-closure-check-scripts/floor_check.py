"""Closure check of RT-238, the floor's missing condition.

The whole-state floor as version 5 states it (section 6.4 item 1, section 9):
a site set is usable only if
    whole - untouched >= 0.8 x (own - untouched)
AND the requirement on the right is above zero; where own-directed accuracy is
not above the no-transplant rate, no site set is usable.

This script (1) writes that rule from the text as its own function and
compares it with the frozen code's `measure.floor_check` on every input of a
grid of counts and on random draws; (2) builds a small case on the toy's
45-site-set family where own-directed accuracy is at or under the
no-transplant rate and runs it through the frozen nomination rule
(`procedure.pick`) and reading (`measure.reading`); (3) re-judges the
competing solver's six committed nomination grids with the frozen code.

    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-serious-findings-closure-check-scripts/floor_check.py
"""
from __future__ import annotations

import glob
import inspect
import json
import os
import sys

import numpy as np

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "experiments/08-successor-degree/src"))
import measure as MS     # noqa: E402
import procedure as P    # noqa: E402


def text_rule(whole, untouched, own):
    """Version 5's rule, written from the text alone."""
    if not own > untouched:
        return False                       # "not above": no site set is usable
    return whole - untouched >= 0.8 * (own - untouched)


def printed_inequality_alone(whole, untouched, own):
    """The version 4 rule as printed, without the condition (what RT-238 found)."""
    return whole - untouched >= 0.8 * (own - untouched)


def main():
    print("== 1. the frozen code's floor")
    print(inspect.getsource(MS.floor_check))

    print("== 2. text rule against code, every count out of 60 for all three (61^3 inputs)")
    n = 60
    v = [k / n for k in range(n + 1)]
    agree = total = 0
    diffs = []
    for w in v:
        for u in v:
            for a in v:
                total += 1
                c = MS.floor_check(w, u, a)["clears"]
                t = text_rule(w, u, a)
                if c == t:
                    agree += 1
                elif len(diffs) < 5:
                    diffs.append((w, u, a, c, t))
    print(f"   agree on {agree:,} of {total:,}; first disagreements {diffs}")
    rng = np.random.default_rng(20261009)
    k = rng.integers(0, 801, size=(200_000, 3)) / 800
    rnd = sum(MS.floor_check(*x)["clears"] == text_rule(*x) for x in k.tolist())
    print(f"   random counts out of 800: agree on {rnd:,} of {len(k):,}")
    at_or_under = [(w, u, a) for w in v for u in v for a in v if a <= u]
    admitted_alone = sum(printed_inequality_alone(*x) for x in at_or_under)
    admitted_code = sum(MS.floor_check(*x)["clears"] for x in at_or_under)
    print(f"   inputs with own at or under untouched: {len(at_or_under):,}; the printed inequality alone "
          f"admits {admitted_alone:,}; the code admits {admitted_code}")

    print("\n== 3. the small case on the toy's family")
    fam = P.site_family(5)
    print(f"   toy family: {len(fam)} site sets, {len(fam) * len(P.RANKS)} comparisons")
    fits = {l: dict(whole=180, piece={r: 180 for r in P.RANKS}) for l in range(5)}

    def grid_for(untouched, own, seed):
        r = np.random.default_rng(seed)
        rows = []
        for L, Pos in fam:
            whole = float(r.integers(0, 601)) / 600     # anywhere from 0 to 1
            fl = MS.floor_check(whole, untouched, own)
            for rank in P.RANKS:
                rows.append(dict(layers=list(L), positions=Pos, rank=rank, accuracy_whole=whole,
                                 accuracy_ownership_only=float(r.integers(0, 601)) / 600, floor=fl))
        return rows

    cases = [("own equals untouched", 0.24, 0.24),
             ("own below untouched", 0.25, 0.2333),
             ("own a hair below untouched", 0.2417, 0.2400),
             ("positive control: own above untouched", 0.12, 0.95)]
    out = {}
    for name, u, a in cases:
        rows = grid_for(u, a, 7)
        sets = {(tuple(g["layers"]), g["positions"]): g for g in rows}
        alone = sum(printed_inequality_alone(g["accuracy_whole"], u, a) for g in sets.values())
        code = sum(g["floor"]["clears"] for g in sets.values())
        best, why, _ = P.pick(rows, fits, fam, 144)
        rd = MS.reading(0.9, 0.5, u, a)
        out[name] = dict(untouched=u, own=a, site_sets=len(sets), printed_alone_admits=alone,
                         code_clears=code, pick=why, reading_status=rd["status"],
                         required_room=rd["floor"]["required_room"])
        print(f"   {name}: untouched {u}, own {a}; required room {rd['floor']['required_room']:+.4f}; "
              f"printed inequality alone admits {alone} of {len(sets)}; code clears {code}; "
              f"pick -> {why!r}; reading at whole 0.9 -> {rd['status']!r}")

    print("\n== 4. the competing solver's six committed nomination grids, re-judged by the frozen code")
    src = os.path.join(ROOT, "experiments/rehearsal-successor-measure/out-competing-solver-run")
    solver = {}
    for f in sorted(glob.glob(os.path.join(src, "nominate_blind_seed*_*.json"))):
        d = json.load(open(f))
        u, a = d["dev_untouched"], d["dev_accuracy"]
        rows = []
        for g in d["grid"]:
            rows.append(dict(g, floor=MS.floor_check(g["accuracy_whole"], u, a)))
        sets = {(tuple(g["layers"]), g["positions"]): g for g in rows}
        alone = sum(printed_inequality_alone(g["accuracy_whole"], u, a) for g in sets.values())
        code = sum(g["floor"]["clears"] for g in sets.values())
        recorded = sum(g["floor"]["clears"] for g in {(tuple(x["layers"]), x["positions"]): x
                                                     for x in d["grid"]}.values())
        # generous made-up fits, so that only the floor can refuse a site set
        best, why, _ = P.pick(rows, fits, fam, 144)
        name = os.path.basename(f)[len("nominate_"):-len(".json")]
        solver[name] = dict(untouched=u, own=a, required_room=0.8 * (a - u), printed_alone_admits=alone,
                            code_clears=code, recorded_clears=recorded, pick=why)
        print(f"   {name}: untouched {u:.4f}, own {a:.4f}, required room {0.8 * (a - u):+.4f}; "
              f"printed inequality alone admits {alone} of {len(sets)}; frozen code clears {code} "
              f"(the run's own record: {recorded}); pick -> {why!r}")
    all45 = sum(1 for s in solver.values() if s["printed_alone_admits"] == 45)
    print(f"   runs where the printed inequality alone admits all 45: {all45} of {len(solver)}; "
          f"runs where the frozen code clears any: {sum(1 for s in solver.values() if s['code_clears'])}")

    json.dump(dict(grid_agree=[agree, total], random_agree=[rnd, len(k)],
                   at_or_under=dict(inputs=len(at_or_under), printed_alone=admitted_alone,
                                    code=admitted_code),
                   small_case=out, competing_solver=solver),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "floor_check.json"), "w"),
              indent=1)


if __name__ == "__main__":
    main()
