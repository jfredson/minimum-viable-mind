"""Gate A tier 1: how long the registered nomination takes on the laptop's
processor, which ruling 3 of 2026-10-03 (late evening) makes the device of the
registered fit, and which section 11, step 5a, of version 4 says will run on
the laptop ("ARGUED: ... fit on the laptop").

Times, on the processor, the forward passes the rule makes, at the registered
shape (448 wide, 12 blocks, 8 heads; the shape bench_arms.py and the rented
slice used), on the toy grammar's 600 development pairs (sequence 56; the
registered grammar is the same grammar per section 4 of version 4, but its
length at registered scale is not fixed anywhere, so this is a lower bound if
it is longer). The model is untrained: time per pass does not depend on the
weights. Also times the toy shape the same way, as a calibration against the
controls re-run's own recorded time (967 s for twelve models, with controls).

Laptop only; trains nothing; $0. Run from the root of the checkout.
"""
import os
import sys
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

SRC = os.path.abspath("experiments/rehearsal-successor-measure/src")
sys.path.insert(0, SRC)
os.chdir(SRC)
import arms as A          # noqa: E402
import grammar as G       # noqa: E402
import training as T      # noqa: E402
import transplant as X    # noqa: E402

DEV = torch.device("cpu")
torch.manual_seed(0)
pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEV)
recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), DEV)
donor = A.to_torch(G.batch([p["donor"] for p in pairs]), DEV)
print(f"torch {torch.__version__}, threads {torch.get_num_threads()}, sequence {G.SEQ_LEN}, pairs 600")


def timed(shape, label, n_states):
    cfg = A.Config(arm="F", **shape)
    m = A.Arm(cfg).to(DEV).eval()
    t0 = time.time()
    d = X.capture(m, donor)
    t_cap = time.time() - t0
    sites = X.Sites((1,), "post-identity")
    mask = X.position_mask(recip, "post-identity")
    q, _ = np.linalg.qr(np.random.default_rng(0).normal(size=(cfg.d_model, 8)))
    basis = {1: torch.as_tensor(q, dtype=torch.float32)}
    X.transplanted_logits(m, recip, d, sites, mask, None)       # warm
    ts = []
    for b in (None, basis, None, basis, None, basis):
        t0 = time.time()
        X.transplanted_logits(m, recip, d, sites, mask, b)
        ts.append(time.time() - t0)
    per = float(np.median(ts))
    h = d[1][torch.arange(600), recip["action_pos"][:, G.OWN]].numpy()
    y = np.arange(600) % 12
    t0 = time.time()
    LogisticRegression(max_iter=3000, C=1.0).fit(h[:420], y[:420])
    t_fit = time.time() - t0
    contig = n_states * (n_states + 1) // 2
    family = (contig - n_states) * 4 + n_states     # layer-0 sets at `action` only
    passes = 2 + family * 5                          # donor capture, clean, then whole + four sizes per site set
    fits = n_states * 5                              # whole read and four pieces per running state
    est = passes * per + fits * t_fit
    print(f"{label}: {A.n_params(m):,} parameters; capture {t_cap:.2f} s; one transplant pass over 600 pairs {per:.3f} s "
          f"(median of 6); one read fit {t_fit:.2f} s")
    print(f"   nomination grid: {family} site sets -> {passes} passes, {fits} fits -> about {est / 60:.1f} minutes per model and seed"
          f" (control 2's own grid, where it runs, about doubles it)")
    return est


toy = timed(dict(d_model=160, n_layers=4, n_heads=4), "toy shape (160 wide, 4 blocks)", 5)
reg = timed(dict(d_model=448, n_layers=12, n_heads=8), "registered shape (448 wide, 12 blocks)", 13)
print(f"registered against toy, per model and seed: {reg / toy:.0f} times")
print(f"twelve registered models, nomination grids only: about {12 * reg / 3600:.1f} hours on this processor")
