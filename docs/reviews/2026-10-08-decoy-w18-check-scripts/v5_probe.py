"""Checker's test of the V5 claim: at the action the soft code is almost one-hot, so the
hard code is almost the same numbers there; and the soft code is an exact straight-line
function of the block (so V1 is linear and V5 is the only non-straight-line form). Seeds 0-2."""
import os, sys
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(S, "rerun/experiments/08-successor-degree/out-decoy-w18"))
import torch
import decoy_w18 as W
G, P = W.G, W.P
torch.set_num_threads(2)
data = P.EvalData(1.0)
recip, _ = data.fresh
rows = torch.arange(recip["tokens"].shape[0])
for seed in (0, 1, 2):
    base, _, soft, info = W.build(seed, "V1", data)
    _, _, hard, _ = W.build(seed, "V5", data)
    with torch.no_grad():
        cs, ch = soft.code(recip), hard.code(recip)
        own, _ = base._own_vec(recip)
    k = soft.k
    for c, name in ((G.OWN, "own-directed action"), (G.OTHER, "named-other action")):
        ap = recip["action_pos"][:, c]
        a, b = cs[rows, ap] / k, ch[rows, ap] / k
        print(f"seed {seed}, {name}: soft code's owner-word weight mean {float(a.max(-1).values.mean()):.4f}, "
              f"min {float(a.max(-1).values.min()):.4f}; largest |soft - hard| / k = {float((a - b).abs().max()):.4f}")
    allpos_diff = float(((cs - ch).abs() / k).max())
    # straight-line map from block (24) to soft code (20), all positions
    Xb = own.reshape(-1, 24).double(); Y = cs.reshape(-1, 20).double()
    sol = torch.linalg.lstsq(torch.cat([Xb, torch.ones(len(Xb), 1, dtype=Xb.dtype)], 1), Y).solution
    res = float((torch.cat([Xb, torch.ones(len(Xb), 1, dtype=Xb.dtype)], 1) @ sol - Y).abs().max() / k)
    print(f"seed {seed}: largest |soft - hard| / k at any position = {allpos_diff:.4f}; "
          f"soft code from block by one straight-line map, largest residual / k = {res:.2e}")
