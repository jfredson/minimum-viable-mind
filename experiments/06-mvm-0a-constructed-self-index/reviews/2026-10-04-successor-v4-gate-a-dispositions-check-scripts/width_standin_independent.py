"""Independent re-measurement of the width stand-in behind the proposed repair
of RT-240. Written by the checking session. It does NOT import
width_fit_pool_standin.py, width_vs_count.py, rehearse.py or rerun_v3.py.
It uses the shared generator (grammar.py), the model builder
(repairs.build_for) and the committed model files.

Done independently here: the read's label (the model's own marker word) is
read off the tokens and the acting channel, not off the episode's fields; the
8-direction piece is rebuilt from the read's coefficients with this file's own
SVD and QR; models are loaded with this file's own strict load.

The noise construction must be the same as the review's for the numbers to
be comparable at all (same generator seed 20261004, same scale rule: the
median of the state's per-coordinate standard deviations), so that part is
re-implemented from the description, not shared.

Processor only, $0.
"""
import json, os, sys
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(H, "../../../rehearsal-successor-measure/src"))
sys.path.insert(0, SRC)
import grammar as G      # noqa: E402
import repairs as R      # noqa: E402

MODELS = os.path.join(SRC, "..", "out-repairs", "models")
WIDE, HELD, FLOOR = 448, 180, 144
CASES = [("C", 0, 2), ("C", 1, 1), ("C", 2, 1), ("M", 0, 1), ("T", 0, 1)]


def data(n_pairs):
    pairs = G.make_pairs(n_pairs, seed=4242, pool="dev")
    eps = [p["recipient"] for p in pairs]
    b = {k: torch.as_tensor(v) for k, v in G.batch(eps).items()}
    tok = b["tokens"].numpy(); act = b["acting"].numpy()
    # own marker word: the marker token opening an assignment turn the channel marks
    y = np.array([tok[i, [1 + 5 * u for u in range(8) if act[i, 1 + 5 * u] == 1][0]]
                  for i in range(len(eps))])
    assert all(len({tok[i, 1 + 5 * u] for u in range(8) if act[i, 1 + 5 * u] == 1}) == 1
               for i in range(len(eps)))
    own_pos = np.array([[p + 5 for p in range(len(tok[i])) if tok[i, p] == G.VOCAB["<act>"]
                         and tok[i, p + 2] == G.VOCAB["<self>"]][0] for i in range(len(eps))])
    assert np.array_equal(own_pos, b["action_pos"][:, 0].numpy())
    return b, y, own_pos


def load(arm, seed):
    m = R.build_for(arm)()
    m.load_state_dict(torch.load(os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt"),
                                 map_location="cpu"), strict=True)
    return m.eval()


def state(m, b, pos, layer):
    with torch.no_grad():
        _, st = m(b, capture=True)
    return st[layer][torch.arange(len(pos)), torch.as_tensor(pos)].numpy().astype(np.float64)


def fit(h, y, n_fit, held, C=1.0):
    clf = LogisticRegression(max_iter=3000, C=C).fit(h[:n_fit], y[:n_fit])
    return int(round(clf.score(h[held], y[held]) * len(y[held]))), clf.coef_


def piece(h, y, n_fit, held, coef, C=1.0):
    _, _, vt = np.linalg.svd(coef - coef.mean(0, keepdims=True), full_matrices=False)
    q, _ = np.linalg.qr(vt[:8].T)
    q = q.astype(np.float32)
    return fit(h @ q, y, n_fit, held, C)[0]


def noisy(h, scale, rng):
    return np.concatenate([h, rng.normal(0, scale, size=(h.shape[0], WIDE - h.shape[1]))], 1)


torch.manual_seed(0)
out = {"reproduction": {}, "sweep": {}, "toy": {}}

# 1. the review's stand-in: 600 episodes, fit first 420, score last 180
b6, y6, p6 = data(600)
held6 = slice(420, 600)
print("1. review's stand-in, 600 episodes")
for arm, seed, layer in CASES:
    h = state(load(arm, seed), b6, p6, layer)
    sc = float(np.median(h.std(0)))
    rng = np.random.default_rng(20261004)
    w0, c0 = fit(h, y6, 420, held6); p0 = piece(h, y6, 420, held6, c0)
    W, P = [], []
    for _ in range(5):
        hp = noisy(h, sc, rng); w, c = fit(hp, y6, 420, held6)
        W.append(w); P.append(piece(hp, y6, 420, held6, c))
    out["reproduction"][f"{arm}/{seed}"] = dict(width160=[w0, p0], whole448=W, piece448=P)
    print(f"  {arm}/{seed} L{layer} | {w0}, {p0} | {W}; {P}")

# 2-3. pool of 1,980, last 180 held out
bp, yp, pp = data(1980)
heldp = slice(1800, 1980)
print("2-3. pool of 1,980, last 180 held out")
settings = [(420, 1.0), (900, 1.0), (1800, 1.0), (420, 0.1), (420, 0.01)]
for arm, seed, layer in CASES:
    h = state(load(arm, seed), bp, pp, layer)
    sc = float(np.median(h.std(0)))
    rows = {}
    for n_fit, C in settings:
        rng = np.random.default_rng(20261004)
        W, P = [], []
        for _ in range(5):
            hp = noisy(h, sc, rng); w, c = fit(hp, yp, n_fit, heldp, C)
            W.append(w); P.append(piece(hp, yp, n_fit, heldp, c, C))
        rows[f"fit {n_fit}, C {C}"] = dict(whole=W, piece=P)
        print(f"  {arm}/{seed} L{layer} fit {n_fit} C {C}: whole {W}; piece {P}; min piece {min(P)}")
    out["sweep"][f"{arm}/{seed}"] = rows

# 4. toy width, every model, layers 1-4, best piece per fit size
print("4. width 160, best piece over layers 1-4, fit 420/900/1800")
for arm in ("T", "C", "M", "F"):
    for seed in (0, 1, 2):
        m = load(arm, seed)
        with torch.no_grad():
            _, st = m(bp, capture=True)
        per = {}
        for layer in range(1, len(st)):
            h = st[layer][torch.arange(1980), torch.as_tensor(pp)].numpy().astype(np.float64)
            per[layer] = []
            for n_fit in (420, 900, 1800):
                w, c = fit(h, yp, n_fit, heldp)
                per[layer].append([w, piece(h, yp, n_fit, heldp, c)])
        best = [max(per[l][i][1] for l in per) for i in range(3)]
        out["toy"][f"{arm}/{seed}"] = dict(per_layer=per, best_piece=best)
        print(f"  {arm}/{seed}: best piece {best}")

# compare with the committed outputs
auth = json.load(open(os.path.join(SRC, "..", "out-width-fit-pool-standin",
                                   "width_fit_pool_standin.json")))
d = n = 0
for k, v in out["reproduction"].items():
    a = auth["reproduction"][k]
    for f in ("width160", "whole448", "piece448"):
        n += 1; d += v[f] != a[f]
for k, rows in out["sweep"].items():
    for lab, v in rows.items():
        a = auth["sweep_448"][k]["rows"][lab]
        for f in ("whole", "piece"):
            n += 1
            if v[f] != a[f]:
                d += 1; print("DIFF sweep", k, lab, f, v[f], a[f])
for k, v in out["toy"].items():
    for l, vals in v["per_layer"].items():
        n += 1
        if vals != auth["toy_width"][k][str(l)]:
            d += 1; print("DIFF toy", k, l, vals, auth["toy_width"][k][str(l)])
print(f"lists compared with the committed JSON: {n}; differing: {d}")
json.dump(out, open(os.path.join(H, "width_standin_independent.json"), "w"), indent=1, sort_keys=True)
