"""Page 4 toy re-run, the twelve toy models: the frozen measurement procedure
with every straight-line read fitted on 1,800 development episodes.

UNREGISTERED rehearsal code. NOT A RESULT about the scientific question.
Method, committed before this was run:
`docs/2026-10-06-page4-toy-rerun-1800-method.md`. Section numbers in comments
are that file's.

What it does. It runs `experiments/08-successor-degree/src/procedure.py`
(the frozen procedure, unmodified on disk) on one committed toy model, with
three changes made from here at run time and nothing else:

1. every straight-line read (the ownership read, and the named agent's read
   for control 2) is fitted on the first `--pool` minus 180 development
   episodes and scored on the last 180 (the frozen code fits on the first
   seven tenths, which is 420 of 600);
2. those reads, their held-out counts, the 200-shuffle null and the piece's
   counts at the other positions of its site use a development pool of
   `--pool` episodes, built by the same generator with the same seed as the
   frozen 600, whose first 600 are those 600 (checked below);
3. nothing else: the transplant passes of the nomination, control 2's grid,
   the fresh, relaxed and gate sets, the seeds, the site-set family, the
   floors and every rule are the frozen code's own, on the frozen 600 pairs.

With `--pool 600` the three changes do nothing, so the output must equal the
committed fresh-fit test of the code freeze (test T3b,
`experiments/08-successor-degree/out-freeze-tests/t3b-fresh-fit/`) field for
field. That is the reproduction check of section 4; `page4_compare.py` makes
it.

    cd experiments/rehearsal-successor-measure/src
    PY=~/Code/minimum-viable-mind/.venv/bin/python
    $PY page4_models_1800.py --pool 1980 --out ../out-page4-rerun-1800/models-1800 --arm T --seed 0
    ...   (arm T's seed before the other arms' same seed: the rider reads it)
    $PY page4_models_1800.py --summarise ../out-page4-rerun-1800/models-1800

Laptop, processor only, $0. Trains nothing but small logistic regressions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
REH = os.path.abspath(os.path.join(HERE, ".."))
FROZEN = os.path.abspath(os.path.join(REH, "..", "08-successor-degree", "src"))
sys.path.insert(0, FROZEN)          # the frozen grammar, measure, models, transplant
import procedure as P               # noqa: E402
from sklearn.linear_model import LogisticRegression   # noqa: E402

G, MS, M, X = P.G, P.MS, P.M, P.X
assert os.path.dirname(os.path.abspath(G.__file__)) == FROZEN, "imported the wrong grammar"
MODELS = os.path.join(REH, "out-repairs", "models")
HELD = 180                          # the last 180 of the pool are held out, at every pool size
STATE = {}                          # the frozen 600 and the pool, set in main


def _fit(h, y):
    """Section 2, change 1: fit on all but the last 180, whatever the pool."""
    n_tr = len(y) - HELD
    return LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr]), n_tr


def _null(m, recip, seed: int, shuffles: int) -> dict:
    """`procedure.null`, line for line, with the split of change 1."""
    hs, _ = P.action_states(m, recip, G.OWN)
    y = P.read_labels(recip, "own")
    n_tr = len(y) - HELD
    out = {}
    for l, h in enumerate(hs):
        rng = np.random.default_rng([20260926, seed, l])
        sc = []
        for _ in range(shuffles):
            yy = rng.permutation(y)
            clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], yy[:n_tr])
            sc.append(clf.score(h[n_tr:], yy[n_tr:]) * (len(y) - n_tr))
        sc = np.array(sc)
        out[l] = dict(p95=float(np.percentile(sc, 95)), p99=float(np.percentile(sc, 99)),
                      max=float(sc.max()), mean=float(sc.mean()), shuffles=shuffles)
    return out


def _swap(b):
    """Change 2: wherever the frozen code fits or scores a read on the frozen
    600 development recipients, it gets the pool instead."""
    return STATE["pool"] if b is STATE["dev600"] else b


_fit_reads, _accuracies, _piece_elsewhere = P.fit_reads, P.accuracies, P.piece_elsewhere
P._fit = _fit
P.null = lambda m, recip, seed, shuffles: _null(m, _swap(recip), seed, shuffles)
P.fit_reads = lambda m, dev_recip: _fit_reads(m, _swap(dev_recip))
P.accuracies = lambda m, recip, coefs, target, cond: _accuracies(m, _swap(recip), coefs, target, cond)
P.piece_elsewhere = lambda m, dev, spec, coefs: _piece_elsewhere(m, _swap(dev), spec, coefs)


def sha_ok(arm, seed):
    want = dict(reversed(line.split()) for line in open(os.path.join(MODELS, "SHA256SUMS")))
    path = os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt")
    got = hashlib.sha256(open(path, "rb").read()).hexdigest()
    return got == want[os.path.basename(path)], path


def build_pool(data, n):
    """The development pool: the frozen generator, the frozen seed, `n` pairs;
    the recipients only (the reads are fitted on recipients)."""
    if n == len(data.dev_pairs):
        return data.dev[0]
    _, seed, pool, relaxed = G.EVAL_SETS["dev"]
    pairs = G.make_pairs(n, seed=seed, pool=pool, collide=relaxed)
    head = pairs[:len(data.dev_pairs)]
    same = all(json.dumps(a, sort_keys=True, default=str) == json.dumps(b, sort_keys=True, default=str)
               for a, b in zip(head, data.dev_pairs))
    assert same, "stop: the pool's first 600 pairs are not the frozen 600"
    recip = M.to_torch(G.batch([p["recipient"] for p in pairs]), P.DEVICE)
    assert torch.equal(recip["tokens"][:len(head)], data.dev[0]["tokens"]), "stop: pool tokens differ"
    return recip


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", type=int, choices=(600, 1980))
    ap.add_argument("--out")
    ap.add_argument("--arm", choices=("T", "C", "M", "F"))
    ap.add_argument("--seed", type=int, choices=(0, 1, 2))
    ap.add_argument("--shuffles", type=int, default=MS.N_SHUFFLES)
    ap.add_argument("--summarise")
    a = ap.parse_args()
    if a.summarise:
        res = P.summarise(a.summarise)
        print(json.dumps(dict(gates=res["gates"], outcome=res.get("outcome")), default=P._json_default))
        return
    ok, path = sha_ok(a.arm, a.seed)
    assert ok, f"stop: {path} does not match SHA256SUMS"
    data = P.EvalData(1.0)
    STATE["dev600"] = data.dev[0]
    STATE["pool"] = build_pool(data, a.pool)
    n = STATE["pool"]["tokens"].shape[0]
    assert n == a.pool and n - HELD == a.pool - 180
    if a.arm != "T":
        assert os.path.exists(os.path.join(a.out, f"row_T_seed{a.seed}.json")), \
            "run arm T's same seed first: the rider reads its site set"
    print(f"[{a.arm}/{a.seed}] pool {n} development episodes: reads fitted on the first {n - HELD}, "
          f"scored on the last {HELD}; transplants on the frozen {len(data.dev_pairs)} pairs; "
          f"torch threads {torch.get_num_threads()}", flush=True)
    row = P.run_model(path, a.out, a.arm, "toy", a.seed, None, a.shuffles, 1.0, False, data)
    row["page4"] = dict(pool=n, fitted_on=n - HELD, held_out=HELD,
                        held_out_episodes=f"{n - HELD + 1} to {n} of the pool",
                        transplant_pairs=len(data.dev_pairs),
                        method="docs/2026-10-06-page4-toy-rerun-1800-method.md")
    with open(os.path.join(a.out, f"row_{a.arm}_seed{a.seed}.json"), "w") as f:
        json.dump(row, f, indent=1, sort_keys=True, default=P._json_default)


if __name__ == "__main__":
    main()
