"""Gate A tier 1, a stand-in for one feasibility question the ruled episode
counts leave open. NOT A RESULT about any model.

Ruled 2026-10-03 (late evening, ruling 4): the registered measurement uses the
toy's counts, so every read is fitted on 420 development episodes and scored
on 180. The toy's running state is 160 wide; the registered model's is 448.
At 160 there are fewer state coordinates than fitting episodes; at 448 there
are more. This asks what that change alone does to the held-out count the
four-fifths floor (144 of 180) is applied to, using the committed toy models:
the state at the chosen layer of the action position, with 288 extra
coordinates of independent noise appended so that it is 448 wide, the noise
scaled to the state's own typical coordinate size. Real extra coordinates in
a wider model carry structured content, not independent noise, so this is a
stand-in and its numbers are a sketch of direction, not a forecast.

The read is the registered one (scikit-learn logistic regression, C = 1.0,
max_iter 3000, first 420 of 600 fitted, last 180 scored), as in
rerun_controls.correct_count; the piece is the read's leading 8 directions,
as rehearse.basis_for builds them. Processor only, $0.

Run from the root of the checkout with the project's Python.
"""
import os
import sys

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

SRC = os.path.abspath("experiments/rehearsal-successor-measure/src")
sys.path.insert(0, SRC)
os.chdir(SRC)
import arms as A          # noqa: E402
import grammar as G       # noqa: E402
import rehearse as RH     # noqa: E402
import repairs as R       # noqa: E402
import rerun_v3 as V      # noqa: E402
import training as T      # noqa: E402

DEV = torch.device("cpu")
torch.manual_seed(0)
pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEV)
recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), DEV)
y = R.read_labels(recip, "own")
n_tr = int(0.7 * len(y))


def count(h):
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
    return int(round(clf.score(h[n_tr:], y[n_tr:]) * (len(y) - n_tr))), clf.coef_


def piece_count(h, coef, r=8):
    q = RH.basis_for(coef, r, DEV).numpy()
    return count(h @ q)[0]


CASES = [("C", 0, 2), ("C", 1, 1), ("C", 2, 1), ("M", 0, 1), ("T", 0, 1)]   # chosen layers (T at 1: stricter row)
print("arm/seed layer | width 160: whole read, piece of 8 | width 448 (288 noise coords), five noise draws: whole read; piece of 8")
for arm, seed, layer in CASES:
    m = V.load_model(arm, seed, DEV)
    with torch.no_grad():
        _, states = m(recip, capture=True)
    ap = recip["action_pos"][:, G.OWN]
    h = states[layer][torch.arange(len(y)), ap].numpy().astype(np.float64)
    w0, c0 = count(h)
    p0 = piece_count(h, c0)
    scale = float(np.median(h.std(axis=0)))
    rng = np.random.default_rng(20261004)
    whole, piece = [], []
    for _ in range(5):
        hp = np.concatenate([h, rng.normal(0, scale, size=(len(y), 448 - h.shape[1]))], axis=1)
        w, c = count(hp)
        whole.append(w)
        piece.append(piece_count(hp, c))
    print(f"{arm}/{seed} layer {layer} | {w0}, {p0} | {whole}; {piece}  (noise scale {scale:.3f})")
print("floor: 144 of 180. NOT A RESULT: a stand-in for width, with independent noise in place of a wider model's own coordinates.")
