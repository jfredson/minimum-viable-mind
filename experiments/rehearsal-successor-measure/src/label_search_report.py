"""Tables for the free-arm label search findings, printed as Markdown from the
output files in `../out-label-search/`. Formatting only: it computes nothing
the fit and verdict stages did not already write down.

    ../../../.venv/bin/python label_search_report.py --label own-turn-pair
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

import label_search as S


def load(label, arm, seed):
    p = os.path.join(S.OUT, f"fit_{label}_{arm}_seed{seed}.json")
    if not os.path.exists(p):
        return None
    with open(p) as f:
        d = json.load(f)
    return {(tuple(s["layers"]), s["positions"]): s for s in d["sites"]}, d


def layers_name(L):
    return str(L[0]) if len(L) == 1 else f"{L[0]}–{L[-1]}"


def table(label, arm):
    runs = [load(label, arm, s) for s in S.SEEDS]
    if any(r is None for r in runs):
        return None
    out = [f"**Arm {arm}** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the "
           f"site set clears on that seed (at least {S.FLOOR:.2f} and above every "
           f"shuffle at that seed's best site set).", "",
           "| layers | " + " | ".join(S.POSITION_SETS) + " |",
           "|---|" + "---|" * len(S.POSITION_SETS)]
    for L in S.LAYER_SETS:
        cells = []
        for P in S.POSITION_SETS:
            fits = []
            for r, _ in runs:
                s = r[(L, P)]
                t = f"{s['fit']:.3f}"
                fits.append(f"**{t}**" if s["clears"] else t)
            cells.append(" / ".join(fits))
        out.append(f"| {layers_name(L)} | " + " | ".join(cells) + " |")
    out += ["", "| seed | best site set | fit | null mean | 95th | 99th | highest shuffle "
            "| shuffles at or above the fit | site sets above every shuffle | seconds |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for s, (r, d) in zip(S.SEEDS, runs):
        b, n = d["best_site"], d["null"]
        above = sum(v["fit"] > n["max"] for v in r.values())
        out.append(f"| {s} | layers {layers_name(b['layers'])}, {b['positions']} | "
                   f"{b['fit']:.3f} | {n['mean']:.3f} | {n['p95']:.3f} | {n['p99']:.3f} | "
                   f"{n['max']:.3f} | {n['share_at_or_above_real'] * n['n']:.0f} of {n['n']} | "
                   f"{above} of 60 | {d['seconds']:.0f} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", choices=tuple(S.LABELS), required=True)
    a = ap.parse_args()
    print(f"### {S.LABELS[a.label]}\n")
    for arm in S.ARMS:
        t = table(a.label, arm)
        if t:
            print(t + "\n")


if __name__ == "__main__":
    main()
