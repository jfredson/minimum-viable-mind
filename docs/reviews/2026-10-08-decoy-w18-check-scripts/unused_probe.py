"""Checker's own test that the decoy code is unused by the action, independent of the
author's checks (a), (b), (b'): (1) the gradient of every output with respect to the
code numbers at every state is exactly zero; (2) shuffling the code across episodes at
every state leaves outputs bit-identical; (3) the decoy model's state at the code slice
equals the code built from the input, and the content/block slices equal the committed
model's states. Seed 0, variants V1 and V5, on the fresh recipients."""
import os, sys
S = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(S, "rerun/experiments/08-successor-degree/out-decoy-w18")
sys.path.insert(0, D)
import torch
import decoy_w18 as W
P, X = W.P, W.X
torch.set_num_threads(2)
data = P.EvalData(1.0)
recip, _ = data.fresh
for variant in ("V1", "V5"):
    base, _, dm, info = W.build(0, variant, data)
    dc, n = dm.dc, W.N_CODE
    leaves = []

    def grab(li, st):
        st = st.clone()
        c = st[..., dc:dc + n].detach().clone().requires_grad_(True)
        leaves.append(c)
        return torch.cat([st[..., :dc], c, st[..., dc + n:]], dim=-1)
    out = dm(recip, patch_fn=grab)
    grads = torch.autograd.grad(out.sum(), leaves, allow_unused=True)
    gmax = max(0.0 if g is None else float(g.abs().max()) for g in grads)
    perm = torch.randperm(recip["tokens"].shape[0], generator=torch.Generator().manual_seed(7))

    def shuffle(li, st):
        st = st.clone()
        st[..., dc:dc + n] = st[perm][..., dc:dc + n]
        return st
    with torch.no_grad():
        clean = dm(recip)
        sh = dm(recip, patch_fn=shuffle)
        _, ds = dm(recip, capture=True)
        _, bs = base(recip, capture=True)
        code = dm.code(recip)
    same_code = all(torch.equal(s[..., dc:dc + n], code) for s in ds)
    same_rest = all(torch.equal(torch.cat([s[..., :dc], s[..., dc + n:]], -1), b) for s, b in zip(ds, bs))
    print(f"{variant} seed 0 k={info['k']:.4f}: largest |gradient| of outputs wrt code at any state = {gmax}; "
          f"code shuffled across episodes bit-identical = {torch.equal(clean, sh)}; "
          f"code slice equals built code at all {len(ds)} states = {same_code}; "
          f"content+block slices equal committed model's states = {same_rest}")
