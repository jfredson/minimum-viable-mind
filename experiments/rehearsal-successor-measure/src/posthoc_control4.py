"""POST HOC, NOT PRE-STATED. Written 2026-10-03 AFTER the controls re-run's
output was seen (docs/2026-10-03-controls-rerun.md, section on control 4).

Control 4 transplants the whole state at the positions before the RECIPIENT's
first own turn. The donor twin is a different agent, whose first own turn may
come earlier, so at some of those positions the donor's state may already
carry the donor's identity. This prints control 4 as run, and again with the
positions restricted to those before BOTH twins' first own turns, at the site
sets the re-run used. A diagnostic of the control, not a result. $0.
"""
import json, os, sys
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rerun_controls as C, rerun_v3 as V, repairs as R, transplant as X, grammar as G, training as T

fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=C.DEVICE)
recip, donor = C.batches(fresh_pairs)
d_tgt = donor["targets"][:, G.OWN]
S = recip["tokens"].shape[1]
idx = torch.arange(S)[None].expand(recip["tokens"].shape[0], -1)
fr, fd = torch.argmax(recip["acting"], 1), torch.argmax(donor["acting"], 1)
pre_r = idx < fr[:, None]
pre_both = idx < torch.minimum(fr, fd)[:, None]
assert torch.equal(pre_r, X.position_mask(recip, "pre-identity"))
print(f"pairs where the donor's first own turn comes before the recipient's: {float((fd < fr).float().mean()):.4f}")
summ = json.load(open(os.path.join(C.OUT, "summary.json")))["arms"]
print("arm/seed | layers | untouched | control 4 as run | positions before both twins' first own turn")
for arm in C.ARMS:
    for seed in C.SEEDS:
        spec = summ[f"{arm}/{seed}"]["primary"]["site_set"]
        m = V.load_model(arm, seed, C.DEVICE)
        with torch.no_grad():
            clean = m(recip)
        u = float(R.hits(clean, d_tgt, G.OWN).mean())
        ds = X.capture(m, donor)
        sites = X.Sites(tuple(spec["layers"]), spec["positions"])
        a = float(R.hits(R.run(m, recip, ds, sites, pre_r, None), d_tgt, G.OWN).mean())
        b = float(R.hits(R.run(m, recip, ds, sites, pre_both, None), d_tgt, G.OWN).mean())
        print(f"{arm}/{seed} | {tuple(spec['layers'])} | {u:.4f} | {a:.4f} ({a-u:+.4f}) | {b:.4f} ({b-u:+.4f})")
