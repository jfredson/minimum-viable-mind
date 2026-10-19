"""E4: how much the starting sizes D6 and D8 divide by would move if the
starting draw were not the trainer's.

D6 and D8 rebuild the starting weights with torch.manual_seed(0) and
models.build(arm, "10M"). No saved start exists, and the training machine's
library version is not recorded, so whether the rebuild is the trainer's exact
draw cannot be checked. This rebuilds the start with twenty seeds (0 to 19) and
reports, for each starting size the findings divide by, the smallest and
largest value over the seeds as a share of the seed-0 value, and the end-over-
start ratios that result at those extremes."""
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2026-10-18-arm-m-separable-zero-scripts"))
from common import header, load, G, M   # noqa: E402

header("E4: spread of the rebuilt starting sizes over twenty seeds")
markers = torch.tensor([G.VOCAB[f"m{i}"] for i in range(12)])


def sizes(m):
    sd = m.state_dict()
    out = {k: float(sd[k].norm()) for k in ("read_own.weight", "own_key.weight", "own_marker.weight",
                                             "to_val.weight", "act_vec")}
    v = m.own_marker(m.tok(markers))
    out["marker embeddings (mean size)"] = float(m.tok(markers).norm(dim=-1).mean())
    out["answer vector, differing part"] = float((v - v.mean(0, keepdim=True)).norm(dim=-1).mean())
    return out


torch.set_grad_enabled(False)
for name in ("M-10M-rerun", "T-10M-rerun"):
    m, _ = load(name)
    end = sizes(m)
    starts = []
    for seed in range(20):
        torch.manual_seed(seed)
        starts.append(sizes(M.build(m.cfg.arm, "10M")))
    print(f"\n{name}")
    for k in end:
        vals = torch.tensor([s[k] for s in starts])
        s0, lo, hi = starts[0][k], float(vals.min()), float(vals.max())
        print(f"  {k:30s} start seed 0 {s0:8.4f}; over 20 seeds {lo / s0:.3f} to {hi / s0:.3f} of it; "
              f"end over start {end[k] / s0:7.4f} (seed 0), {end[k] / hi:7.4f} to {end[k] / lo:7.4f} (extremes)")
