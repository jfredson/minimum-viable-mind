"""Which repair, if any, keeps the four-fifths fit floor reachable when the
running state is as wide as the registered model's? A measurement for the
proposed disposition of the inside review's serious finding RT-240 (the ruled
episode counts were rehearsed only at the toy's width).

UNREGISTERED. NOT A RESULT about any model or about the scientific question.
Method committed before this was run on any committed model:
`docs/2026-10-04-gate-a-v4-dispositions-measurements-method.md`, part B.

The inside review's stand-in (`width_vs_count.py` beside the review of
2026-10-04) took the committed toy models' state at the action position
(160 wide), appended 288 coordinates of independent noise to make it 448 wide,
and fitted the registered read on 420 episodes. The entangled model's read
fell below 144 of 180 on two seeds of three. This script:

1. reproduces that stand-in exactly (same episodes, same noise draws), as a
   check that it is measuring the same thing;
2. on a fixed set of 180 held-out episodes, fits the same read on 420, 900 and
   1,800 fitting episodes (the first of the two repairs the review names:
   more development episodes for the read), five noise draws each;
3. at 420 fitting episodes, fits it with stronger regularisation, C = 0.1 and
   C = 0.01 against the registered 1.0 (the second repair: regularisation
   fixed in advance);
4. with no noise (the toy's own 160 coordinates), fits the read of all twelve
   toy models at each fitting size at every layer 1 to 4, so that a reader can
   see whether more fitting episodes would change any toy verdict, above all
   whether the free model's read would reach the floor.

Every count is of 180 held-out episodes; the floor is 144. Processor only.
Nothing is trained, rented or spent: $0. Output goes to
`../out-width-fit-pool-standin/`. Run from this directory:

    ~/Code/minimum-viable-mind/.venv/bin/python width_fit_pool_standin.py
"""
from __future__ import annotations

import json
import os
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

import arms as A
import grammar as G
import rehearse as RH
import repairs as R
import rerun_v3 as V
import training as T

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out-width-fit-pool-standin")
DEV = torch.device("cpu")
WIDE = 448
HELD = 180
FIT_SIZES = (420, 900, 1800)
REG = (1.0, 0.1, 0.01)
DRAWS = 5
NOISE_SEED = 20261004               # the review's
# the review's cases: (arm, seed, layer at the chosen site set)
CASES = [("C", 0, 2), ("C", 1, 1), ("C", 2, 1), ("M", 0, 1), ("T", 0, 1)]


def fit_count(h, y, n_fit, C=1.0, held=None):
    """Fit on the first n_fit rows, score on the held-out rows (default: the
    last HELD rows). Returns the held-out count and the coefficients."""
    if held is None:
        held = slice(len(y) - HELD, len(y))
    clf = LogisticRegression(max_iter=3000, C=C).fit(h[:n_fit], y[:n_fit])
    hh, yy = h[held], y[held]
    return int(round(clf.score(hh, yy) * len(yy))), clf.coef_


def piece(h, y, n_fit, coef, C=1.0, held=None, r=8):
    q = RH.basis_for(coef, r, DEV).numpy()
    return fit_count(h @ q, y, n_fit, C=C, held=held)[0]


def states(m, recip, layer):
    with torch.no_grad():
        _, st = m(recip, capture=True)
    ap = recip["action_pos"][:, G.OWN]
    return st[layer][torch.arange(ap.shape[0]), ap].numpy().astype(np.float64)


def recipients(n_pairs):
    pairs, _ = T.make_data(n_pairs, seed=4242, pool="dev", device=DEV)
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), DEV)
    return recip, R.read_labels(recip, "own")


def main():
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    torch.manual_seed(0)
    res = {"floor": 144, "held_out": HELD, "torch": torch.__version__}

    # 1. the review's stand-in, reproduced: 600 episodes, first 420 fitted
    r600, y600 = recipients(600)
    n_tr = int(0.7 * len(y600))
    print("1. the review's stand-in, reproduced (600 episodes, 420 fitted, last 180 scored)")
    rep = {}
    for arm, seed, layer in CASES:
        m = V.load_model(arm, seed, DEV)
        h = states(m, r600, layer)
        scale = float(np.median(h.std(axis=0)))
        rng = np.random.default_rng(NOISE_SEED)
        w0, c0 = fit_count(h, y600, n_tr, held=slice(n_tr, None))
        p0 = piece(h, y600, n_tr, c0, held=slice(n_tr, None))
        whole, pc = [], []
        for _ in range(DRAWS):
            hp = np.concatenate([h, rng.normal(0, scale, size=(len(y600), WIDE - h.shape[1]))], 1)
            w, c = fit_count(hp, y600, n_tr, held=slice(n_tr, None))
            whole.append(w)
            pc.append(piece(hp, y600, n_tr, c, held=slice(n_tr, None)))
        rep[f"{arm}/{seed}"] = dict(layer=layer, width160=[w0, p0], whole448=whole, piece448=pc)
        print(f"   {arm}/{seed} layer {layer} | width 160: {w0}, {p0} | width 448: {whole}; {pc}")
    res["reproduction"] = rep

    # 2 and 3. a pool of 1,980: the last 180 held out throughout, fits on the first n
    pool_n = max(FIT_SIZES) + HELD
    rp, yp = recipients(pool_n)
    assert len(yp) == pool_n
    print(f"\n2-3. pool of {pool_n} development episodes; the same last {HELD} held out for every fit")
    print("   arm/seed layer | fit size or C : whole read, five draws ; piece of 8, five draws")
    sweep = {}
    for arm, seed, layer in CASES:
        m = V.load_model(arm, seed, DEV)
        h = states(m, rp, layer)
        scale = float(np.median(h.std(axis=0)))
        rows = {}
        for setting in [("fit", n, 1.0) for n in FIT_SIZES] + [("C", 420, c) for c in REG[1:]]:
            kind, n_fit, C = setting
            rng = np.random.default_rng(NOISE_SEED)
            whole, pc = [], []
            for _ in range(DRAWS):
                hp = np.concatenate([h, rng.normal(0, scale, size=(pool_n, WIDE - h.shape[1]))], 1)
                w, c = fit_count(hp, yp, n_fit, C=C)
                whole.append(w)
                pc.append(piece(hp, yp, n_fit, c, C=C))
            label = f"fit {n_fit}, C {C}"
            rows[label] = dict(whole=whole, piece=pc)
            print(f"   {arm}/{seed} layer {layer} | {label:>16} : {whole} ; {pc}"
                  f"   min piece {min(pc)} {'clears' if min(pc) >= 144 else 'MISSES'} 144")
        sweep[f"{arm}/{seed}"] = dict(layer=layer, noise_scale=scale, rows=rows)
    res["sweep_448"] = sweep

    # 4. the toy's own width, every model and layer, at each fit size
    print(f"\n4. width 160 (no noise), every toy model, layers 1-4: whole read / piece of 8, per fit size {FIT_SIZES}")
    toy = {}
    for arm in ("T", "C", "M", "F"):
        for seed in (0, 1, 2):
            m = V.load_model(arm, seed, DEV)
            with torch.no_grad():
                _, st = m(rp, capture=True)
            ap = rp["action_pos"][:, G.OWN]
            per_layer = {}
            for layer in range(1, len(st)):
                h = st[layer][torch.arange(pool_n), ap].numpy().astype(np.float64)
                vals = []
                for n_fit in FIT_SIZES:
                    w, c = fit_count(h, yp, n_fit)
                    vals.append([w, piece(h, yp, n_fit, c)])
                per_layer[layer] = vals
            toy[f"{arm}/{seed}"] = per_layer
            best = {n: max(per_layer[l][i][1] for l in per_layer) for i, n in enumerate(FIT_SIZES)}
            print(f"   {arm}/{seed}: " + " | ".join(
                f"L{l} " + " ".join(f"{w}/{p}" for w, p in per_layer[l]) for l in per_layer)
                + f"   best piece per fit size {best}")
    res["toy_width"] = toy
    res["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(OUT, "width_fit_pool_standin.json"), "w") as f:
        json.dump(res, f, indent=2, sort_keys=True)
    print(f"\nwrote {os.path.join(OUT, 'width_fit_pool_standin.json')} in {res['seconds']}s")
    print("NOT A RESULT: a stand-in for width, with independent noise in place of a wider model's own coordinates.")


if __name__ == "__main__":
    main()
