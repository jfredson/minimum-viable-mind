"""Gate C tier 1 review of successor proposal version 3 (2026-10-03).

Question: the fit floor is scored on the FULL straight-line read at a layer
(one logistic regression, every class). The ownership-only transplant moves
only the read's leading `rank` directions. Does that transplanted subspace
itself hold the label?

For every arm and seed, at the primary nominated site set of
out-v3-rules/pass2_summary.json, on the same 600 development episodes and the
same 420/180 split the registered fit uses:
  full    = held-out fit of the full read (must reproduce the committed fit)
  r=1..8  = held-out fit of a fresh read given ONLY the state's coordinates in
            the rank-r subspace the transplant would move (rehearse.basis_for
            on the committed read's coefficients)
For nominations at a multi-position set, the same restricted fit is also taken
at the first own turn and on the span mean, since the transplant moves those
directions at every position of the span.

Reads only committed files. Trains nothing but logistic regressions. $0.
Run from experiments/rehearsal-successor-measure/src:
    ../../../.venv/bin/python <this file>
"""
import json, os, sys
import numpy as np, torch
sys.path.insert(0, os.getcwd())
import rerun_v3 as V, repairs as R, rehearse as RH, transplant as X, grammar as G
from sklearn.linear_model import LogisticRegression

dev = torch.device("cpu")
recip, donor = V.dev_batches(dev)
y = R.read_labels(recip, "own")
n_tr = int(0.7 * len(y))
print(f"development episodes {len(y)}, held out {len(y)-n_tr}, distinct marker words {len(set(y.tolist()))}, "
      f"most common class share {np.bincount(y).max()/len(y):.3f}")

def score(h):
    if h.ndim == 1: h = h[:, None]
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
    return float(clf.score(h[n_tr:], y[n_tr:]))

summ = json.load(open(os.path.join(V.OUT, "pass2_summary.json")))["arms"]
print("arm/seed | nominated site set | full fit | restricted fit at the action position, rank 1 / 2 / 4 / 8 | at nominated rank | dev ownership-only share at that site, rank 1/2/4/8 (whole; untouched)")
for arm in V.ARMS:
    for seed in V.SEEDS:
        spec = summ[f"{arm}/{seed}"]["primary"]["site_set"]
        L, P, r = spec["layers"], spec["positions"], spec["rank"]
        assert len(L) == 1
        l = L[0]
        m = V.load_model(arm, seed, dev)
        with torch.no_grad():
            _, states = m(recip, capture=True)
        st = states[l]
        B_ = st.shape[0]
        ap = recip["action_pos"][:, G.OWN]
        h = st[torch.arange(B_), ap].numpy()
        coef = V.committed_reads(arm, seed)[l]
        full = score(h)
        rs = {}
        for k in R.RANK_CAPS:
            Q = RH.basis_for(coef, k, dev).numpy()
            rs[k] = score(h @ Q)
        nom = json.load(open(os.path.join(V.OUT, f"nominate_{arm}_seed{seed}.json")))
        g = {x["rank"]: x for x in nom["grid"] if x["layers"] == L and x["positions"] == P}
        own = " / ".join(f"{g[k]['accuracy_ownership_only']:.4f}" for k in R.RANK_CAPS)
        line = (f"{arm}/{seed} | layers {tuple(L)} at {P}, rank {r} | {full:.3f} | "
                + " / ".join(f"{rs[k]:.3f}" for k in R.RANK_CAPS)
                + f" | {rs[r]:.3f} | {own} ({g[r]['accuracy_whole']:.4f}; {nom['untouched']:.4f})")
        print(line)
        if P != "action":
            mask = X.position_mask(recip, P).float()
            first = torch.argmax(recip["acting"], dim=1)
            Q = RH.basis_for(coef, r, dev).numpy()
            h_first = st[torch.arange(B_), first].numpy()
            h_mean = ((st * mask[..., None]).sum(1) / mask.sum(1, keepdim=True)).numpy()
            print(f"      at the other positions of {P}: full-state fit at first own turn {score(h_first):.3f}, "
                  f"span mean {score(h_mean):.3f}; restricted to the nominated rank-{r} subspace: "
                  f"first own turn {score(h_first @ Q):.3f}, span mean {score(h_mean @ Q):.3f}")
