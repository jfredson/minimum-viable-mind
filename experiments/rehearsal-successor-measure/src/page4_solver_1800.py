"""Page 4 toy re-run, the competing solver: `competing_solver_run.py` with its
straight-line read fitted on 1,800 development episodes.

UNREGISTERED rehearsal code. NOT A RESULT about the scientific question.
Method, committed before this was run:
`docs/2026-10-06-page4-toy-rerun-1800-method.md`.

What it does. It runs `competing_solver_run.main` (the committed solver run
of 2026-10-03, unmodified on disk) on the three committed solver models,
under both of its readings, with three changes made from here at run time:

1. the read is fitted on the first `--pool` minus 180 development episodes
   and scored on the last 180 (the committed run fitted on the first seven
   tenths, 420 of 600);
2. the read and its held-out counts use a development pool of `--pool`
   episodes from the same generator and seed, whose first 600 are the
   committed 600 (checked);
3. nothing else: the gate, the nomination's transplant passes (on the
   committed 600 pairs), the fresh episodes and every rule are unchanged.

Output goes to `--out` instead of `../out-competing-solver-run/`. With
`--pool 600` the changes do nothing and the output must equal the committed
run file for file (the reproduction check; `page4_compare.py` makes it).

    cd experiments/rehearsal-successor-measure/src
    ~/Code/minimum-viable-mind/.venv/bin/python page4_solver_1800.py --pool 1980 --out ../out-page4-rerun-1800/solver-1800

Laptop, processor only, $0.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import competing_solver_run as CS   # noqa: E402

A, G, R, RH, C, T = CS.A, CS.G, CS.R, CS.RH, CS.C, CS.T
HELD = 180
STATE = {}


def correct_count(h, y):
    """`rerun_controls.correct_count` with the split of change 1."""
    if h.ndim == 1:
        h = h[:, None]
    n_tr = len(y) - HELD
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
    return int(round(clf.score(h[n_tr:], y[n_tr:]) * (len(y) - n_tr)))


def _pool_for(fed_b, true_b):
    """Change 2: the frozen 600 recipients become the pool, fed the same way."""
    if true_b is not STATE.get("dev600"):
        return fed_b, true_b
    pool = STATE["pool"]
    if fed_b is true_b:                                   # channel left on: fed unchanged
        return pool, pool
    assert int(fed_b["acting"].abs().sum()) == 0          # channel removed
    return CS.fed(pool, "channel_removed"), pool


def fit_reads(m, fed_b, true_b):
    """`competing_solver_run.fit_reads`, line for line, with changes 1 and 2."""
    fed_b, true_b = _pool_for(fed_b, true_b)
    with torch.no_grad():
        _, states = m(fed_b, capture=True)
    ap = true_b["action_pos"][:, G.OWN]
    y = R.read_labels(true_b, "own")
    n_tr = len(y) - HELD
    out = {}
    for l, st in enumerate(states):
        h = st[torch.arange(st.shape[0]), ap].numpy()
        clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
        out[l] = clf.coef_.astype(np.float64)
    return out


def accuracies(m, fed_b, true_b, coefs):
    """`competing_solver_run.accuracies`, line for line, with changes 1 and 2."""
    fed_b, true_b = _pool_for(fed_b, true_b)
    with torch.no_grad():
        _, states = m(fed_b, capture=True)
    ap = true_b["action_pos"][:, G.OWN]
    y = R.read_labels(true_b, "own")
    assert len(y) - (len(y) - HELD) == C.HELD_OUT
    out = {}
    for l, st in enumerate(states):
        h = st[torch.arange(st.shape[0]), ap].numpy()
        out[l] = dict(whole=correct_count(h, y),
                      piece={r: correct_count(h @ RH.basis_for(coefs[l], r, CS.DEVICE).numpy(), y)
                             for r in CS.RANKS})
    return out, int(len(np.unique(y)))


_run_one = CS.run_one


def run_one(m, seed, reading, dev, fresh, gate_b, write=True):
    STATE["dev600"] = dev[0]
    if "pool" not in STATE:
        STATE["pool"] = build_pool(dev[0], STATE["n"])
    return _run_one(m, seed, reading, dev, fresh, gate_b, write)


def build_pool(dev600, n):
    if n == dev600["tokens"].shape[0]:
        return dev600
    small, _ = T.make_data(dev600["tokens"].shape[0], seed=4242, pool="dev", device=CS.DEVICE)
    pairs, _ = T.make_data(n, seed=4242, pool="dev", device=CS.DEVICE)
    same = all(json.dumps(a, sort_keys=True, default=str) == json.dumps(b, sort_keys=True, default=str)
               for a, b in zip(pairs[:len(small)], small))
    assert same, "stop: the pool's first 600 pairs are not the committed 600"
    pool = A.to_torch(G.batch([p["recipient"] for p in pairs]), CS.DEVICE)
    assert torch.equal(pool["tokens"][:len(small)], dev600["tokens"]), "stop: pool tokens differ"
    return pool


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", type=int, choices=(600, 1980), required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    STATE["n"] = a.pool
    CS.OUT = os.path.abspath(a.out)
    CS.fit_reads, CS.accuracies, CS.run_one = fit_reads, accuracies, run_one
    C.correct_count = correct_count
    print(f"solver: pool {a.pool} development episodes, reads fitted on the first {a.pool - HELD}, "
          f"scored on the last {HELD}; output {CS.OUT}; torch threads {torch.get_num_threads()}", flush=True)
    sys.argv = [sys.argv[0]]
    CS.main()


if __name__ == "__main__":
    main()
