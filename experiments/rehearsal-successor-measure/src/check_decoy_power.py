"""Probes for the check of the decoy test (pull request 108). Method,
committed before this file produced any output:
`docs/check-decoy-test-method-2026-10-06.md`, section 4.

NOT part of the frozen procedure and NOT a ruled test. Uses the frozen
functions only. Writes only into ../out-decoy-check/. Laptop, $0.

    python check_decoy_power.py --p1   # the transplant's effect on the block (needs the reproduced reads)
    python check_decoy_power.py --p2   # are the 20 marker vectors independent?
    python check_decoy_power.py --p3   # a one-of-20 code of the owner's marker word as the decoy
"""
from __future__ import annotations

import argparse
import copy
import json
import os

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import decoy_test as D

G, MS, M, P, X = D.G, D.MS, D.M, D.P, D.X
OUT = os.path.join(D.REH, "out-decoy-check")
N_CODE = len(G.MARKERS)          # 20 marker words
MARKER_IDS = torch.as_tensor([G.VOCAB[w] for w in G.MARKERS])


def own_rows(b):
    ap = b["action_pos"][:, G.OWN]
    return torch.arange(b["tokens"].shape[0]), ap


def unmoved_share(model, data, basis, block: slice) -> float:
    """Share (by squared size, pooled over the fresh pairs) of the block's
    donor-minus-recipient difference at state 0, own action, that the
    transplant along `basis` leaves unmoved."""
    recip, donor = data.fresh
    rs = X.capture(model, recip)[0]
    ds = X.capture(model, donor)[0]
    rows, ap = own_rows(recip)
    d = (ds[rows, ap] - rs[rows, ap]).double()
    bb = basis.double()
    moved = (d @ bb) @ bb.T
    num = float(((d[:, block] - moved[:, block]) ** 2).sum())
    den = float((d[:, block] ** 2).sum())
    return num / den if den > 0 else float("nan")


def p1(data) -> dict:
    out = {}
    for seed in (0, 1, 2):
        base, _ = D.load_base(seed)
        reads0 = P.fit_reads(base, data.dev[0])
        dc = base.cfg.d_content
        b0 = X.basis_for(reads0["own"][0], 8)
        out[f"unaltered/seed{seed}"] = unmoved_share(base, data, b0, slice(dc, dc + D.D_OWN))
        for scale in (4.0, 0.25, 16.0, 0.0625):
            od = D.out_dir(scale)
            row = json.load(open(os.path.join(od, f"row_T_seed{seed}.json")))
            spec = row["nomination"]["primary"]["site_set"]
            assert spec["layers"] == [0] and spec["positions"] == "action", spec
            reads = P.load_reads(os.path.join(od, f"reads_T_seed{seed}.npz"))["own"]
            dm = D.DecoyArmT(base, scale).eval()
            bas = X.basis_for(reads[0], spec["rank"])
            blk = slice(dm.dc + D.D_OWN, dm.dc + 2 * D.D_OWN)
            out[f"scale_{scale:g}/seed{seed}"] = unmoved_share(dm, data, bas, blk)
        print(json.dumps({k: v for k, v in out.items() if k.endswith(f"seed{seed}")}))
    return out


@torch.no_grad()
def p2() -> dict:
    out = {}
    for seed in (0, 1, 2):
        base, _ = D.load_base(seed)
        mv = base.own_marker(base.tok(MARKER_IDS)).double().numpy()     # (20, 24)
        s = np.linalg.svd(mv, compute_uv=False)
        out[f"seed{seed}"] = dict(rank=int(np.linalg.matrix_rank(mv)),
                                  smallest_over_largest=float(s[-1] / s[0]),
                                  singular_values=[float(x) for x in s])
        print(seed, out[f"seed{seed}"]["rank"], out[f"seed{seed}"]["smallest_over_largest"])
    return out


class CodeDecoyArmT(nn.Module):
    """Arm T with an unused one-of-20 code of the owner's marker word appended,
    built the way the block is (tally weights times each agent's code), times
    `k`, and discarded before every block and the head, as in DecoyArmT."""

    def __init__(self, base: nn.Module, k: float):
        super().__init__()
        self.base = base.eval()
        self.k = float(k)
        self.dc = base.cfg.d_content
        self.cfg = copy.deepcopy(base.cfg)
        self.cfg.d_model = base.cfg.d_model + N_CODE
        assert self.cfg.d_content == self.dc + N_CODE

    def code(self, b):
        _, p_own = self.base._own_vec(b)                                   # (B, S, agents)
        idx = (b["agent_marker_tok"].unsqueeze(-1) == MARKER_IDS).float()  # (B, agents, 20)
        assert torch.all(idx.sum(-1) == 1)
        return self.k * torch.bmm(p_own, idx)

    def forward(self, b, patch_fn=None, capture: bool = False):
        m = self.base
        B, S = b["tokens"].shape
        own_vec, _ = m._own_vec(b)
        code = self.code(b)
        x = m._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)
        states = []

        def widen(x, own_slot):
            return torch.cat([x, code, own_slot], dim=-1)

        def split(st):
            return st[..., :self.dc], st[..., self.dc + N_CODE:]

        state = widen(x, own_vec)
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = split(state)
        for li, blk in enumerate(m.blocks):
            x = blk(x, causal, own_vec)
            state = widen(x, own_slot)
            if patch_fn is not None:
                state = patch_fn(li + 1, state)
            if capture:
                states.append(state)
            x, own_slot = split(state)
        h = m.lnf(x)
        logits = m._separable_logits(b, h, own_slot)
        return (logits, states) if capture else logits


@torch.no_grad()
def p3(data) -> dict:
    out = {}
    recip, donor = data.fresh
    dev = data.dev[0]
    for seed in (0, 1, 2):
        base, _ = D.load_base(seed)
        # k = 4 times the block's root-mean-square size at the own action, development episodes
        rows, ap = own_rows(dev)
        own_vec, _ = base._own_vec(dev)
        rms = float(own_vec[rows, ap].pow(2).sum(-1).mean().sqrt())
        cm = CodeDecoyArmT(base, 4.0 * rms).eval()
        dc = cm.dc
        res = dict(k=4.0 * rms, block_rms=rms)
        # checks: bit-identical outputs; overwriting the code with noise changes nothing
        res["outputs_bit_identical"] = bool(torch.equal(base(recip), cm(recip)))
        g = torch.Generator().manual_seed(20261006 + seed)

        def noise(li, st):
            st = st.clone()
            st[..., dc:dc + N_CODE] = 100.0 * torch.randn(st[..., dc:dc + N_CODE].shape, generator=g)
            return st
        res["noise_in_code_bit_identical"] = bool(torch.equal(cm(recip), cm(recip, patch_fn=noise)))
        if not (res["outputs_bit_identical"] and res["noise_in_code_bit_identical"]):
            raise SystemExit(f"STOP: the one-of-20 code is not unused: {res}")
        reads = P.fit_reads(cm, dev)["own"]
        d_states = X.capture(cm, donor)
        d_tgt = donor["targets"][:, G.OWN]
        clean = cm(recip)
        u = float(P.hits(clean, d_tgt, G.OWN).mean())
        acc = float(P.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
        s0 = X.Sites((0,), "action")
        m0 = X.position_mask(recip, "action")
        w = float(P.hits(X.transplanted_logits(cm, recip, d_states, s0, m0, None), d_tgt, G.OWN).mean())
        res["whole"], res["untouched"], res["own_accuracy"] = w, u, acc
        parts = dict(content=slice(0, dc), code=slice(dc, dc + N_CODE), block=slice(dc + N_CODE, dc + N_CODE + D.D_OWN))
        for rank in (1, 2, 4, 8):
            bas = X.basis_for(reads[0], rank)
            o = float(P.hits(X.transplanted_logits(cm, recip, d_states, s0, m0, {0: bas}), d_tgt, G.OWN).mean())
            bn = bas.numpy()
            tot = float((bn ** 2).sum())
            res[f"rank{rank}"] = dict(ownership_only=o, reading=MS.reading(w, o, u, acc)["degree"],
                                      piece_share={k2: float((bn[s] ** 2).sum()) / tot for k2, s in parts.items()},
                                      block_unmoved_share=unmoved_share(cm, data, bas, parts["block"]))
        out[f"seed{seed}"] = res
        print(json.dumps({f"seed{seed}": res}, default=P._json_default))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p1", action="store_true")
    ap.add_argument("--p2", action="store_true")
    ap.add_argument("--p3", action="store_true")
    a = ap.parse_args()
    torch.set_num_threads(D.THREADS)
    os.makedirs(OUT, exist_ok=True)
    if a.p2:
        json.dump(dict(p2=p2(), versions=P.versions()), open(os.path.join(OUT, "p2.json"), "w"), indent=1)
    if a.p1 or a.p3:
        data = P.EvalData(1.0)
        if a.p1:
            json.dump(dict(p1=p1(data), versions=P.versions()), open(os.path.join(OUT, "p1.json"), "w"), indent=1)
        if a.p3:
            json.dump(dict(p3=p3(data), versions=P.versions()), open(os.path.join(OUT, "p3.json"), "w"),
                      indent=1, default=P._json_default)


if __name__ == "__main__":
    main()
