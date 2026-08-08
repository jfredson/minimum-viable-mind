"""MVM-0a model — the registered architecture (pre-registration v1.0
§Materials, adjudicated 2026-08-07).

Registered values implemented here, each traceable:

- **N registers, one per agent, marker-keyed [RT-01/RT-02].** Register
  content states are initialized IDENTICALLY (one shared learned init) and
  are distinguishable only by their marker key embedding — there is no
  per-slot learned init, which would be a persistent index channel. The
  stack order comes from `encoding.py` (marker vocab id), where gate run
  (ii) certified it carries no ownership cue.
- **Register width 32; injection = cross-attention at every layer, same
  mechanism for all N.** Tokens cross-attend to all N registers after
  self-attention in every block.
- **Full-episode causal self-attention [RT-03]** — the residual path the
  no-register twin gate tests exists architecturally.
- **Write path: generic and shared.** After each turn, the register whose
  marker keyed that turn is updated by ONE shared learned update
  (attention-pool over the turn's top-layer states -> GRU cell). The same
  parameters write every register; nothing marks the own register's write
  path [RT-02]. There is **no auxiliary loss on register content and no
  hand-specified self-writing rule** — the update is trained end-to-end
  from the task loss only.
- **No-register twin [RT-03]:** `Config(use_register=False)` removes the
  register machinery from initialization; everything else is identical.

Scale ladder configs (registration decision 1) in `SCALES`.

    ../../../.venv/bin/python model.py --self-test
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import encoding as E

N_AGENTS = 4


@dataclass
class Config:
    vocab: int = len(E.VOCAB)
    d_model: int = 256
    n_layers: int = 8
    n_heads: int = 8
    d_reg: int = 32
    n_agents: int = N_AGENTS
    max_len: int = 128
    use_register: bool = True     # False => no-register twin [RT-03]

    @property
    def n_params_approx(self) -> int:
        return 12 * self.n_layers * self.d_model ** 2


# Registered scale ladder (decision 1): pilots run smallest-first; the
# registered scale is the smallest that learns (pre-registration §Materials).
SCALES = {
    "smoke": Config(d_model=64, n_layers=2, n_heads=2),
    "10M": Config(d_model=256, n_layers=8, n_heads=8),
    "30M": Config(d_model=448, n_layers=12, n_heads=8),
    "100M": Config(d_model=704, n_layers=16, n_heads=16),
}


class Block(nn.Module):
    def __init__(self, cfg: Config):
        super().__init__()
        self.cfg = cfg
        self.ln1 = nn.LayerNorm(cfg.d_model)
        self.attn = nn.MultiheadAttention(cfg.d_model, cfg.n_heads,
                                          batch_first=True)
        if cfg.use_register:
            self.lnx = nn.LayerNorm(cfg.d_model)
            self.xattn = nn.MultiheadAttention(cfg.d_model, 1,
                                               batch_first=True)
        self.ln2 = nn.LayerNorm(cfg.d_model)
        self.mlp = nn.Sequential(
            nn.Linear(cfg.d_model, 4 * cfg.d_model), nn.GELU(),
            nn.Linear(4 * cfg.d_model, cfg.d_model))

    def forward(self, x, kv, reg_repr):
        """x: (B, S, d) current segment; kv: cached prefix states for this
        block (B, P, d) or None; reg_repr: (B, N, d) or None."""
        h = self.ln1(x)
        ctx = h if kv is None else torch.cat([kv, h], dim=1)
        p, s = ctx.shape[1] - h.shape[1], h.shape[1]
        # causal within the segment; full visibility of the cached prefix
        mask = torch.ones(s, p + s, dtype=torch.bool, device=x.device)
        mask[:, p:] = torch.triu(torch.ones(s, s, dtype=torch.bool,
                                            device=x.device), diagonal=1) == 0
        a, _ = self.attn(h, ctx, ctx, attn_mask=~mask, need_weights=False)
        x = x + a
        if reg_repr is not None:
            r, _ = self.xattn(self.lnx(x), reg_repr, reg_repr,
                              need_weights=False)
            x = x + r
        x = x + self.mlp(self.ln2(x))
        return x, ctx


class MVM0aModel(nn.Module):
    def __init__(self, cfg: Config):
        super().__init__()
        self.cfg = cfg
        self.tok = nn.Embedding(cfg.vocab, cfg.d_model)
        self.pos = nn.Embedding(cfg.max_len, cfg.d_model)
        self.blocks = nn.ModuleList(Block(cfg) for _ in range(cfg.n_layers))
        self.ln_f = nn.LayerNorm(cfg.d_model)
        self.head = nn.Linear(cfg.d_model, cfg.vocab, bias=False)
        self.head.weight = self.tok.weight
        if cfg.use_register:
            # ONE shared init for all registers — identity lives only in
            # the marker key [RT-01/RT-02]
            self.reg_init = nn.Parameter(torch.zeros(cfg.d_reg))
            self.key_proj = nn.Linear(cfg.d_model, cfg.d_model, bias=False)
            self.content_proj = nn.Linear(cfg.d_reg, cfg.d_model, bias=False)
            self.pool_q = nn.Parameter(torch.randn(cfg.d_model)
                                       / math.sqrt(cfg.d_model))
            self.writer = nn.GRUCell(cfg.d_model, cfg.d_reg)

    def _reg_repr(self, reg_state, register_keys):
        """(B, N, d_reg) content + marker keys -> (B, N, d_model)."""
        key = self.key_proj(self.tok(register_keys))
        return self.content_proj(reg_state) + key

    def _write(self, reg_state, seg_h, rows):
        """Shared learned write: attention-pool the segment's top-layer
        states, GRU-update the register row that keyed this turn."""
        w = torch.softmax(seg_h @ self.pool_q, dim=1)
        pooled = (w.unsqueeze(-1) * seg_h).sum(1)
        new = self.writer(pooled, reg_state[torch.arange(len(rows)), rows])
        reg_state = reg_state.clone()
        reg_state[torch.arange(len(rows)), rows] = new
        return reg_state

    def forward(self, batch) -> torch.Tensor:
        """batch: collated tensor dict from `encoding.py` (torch tensors).
        Returns logits (B, L, vocab). Segments follow turn_ids: BOS rides
        with turn 0; the query segment (-2) comes last."""
        ids, turn_ids = batch["input_ids"], batch["turn_ids"]
        B, L = ids.shape
        cfg = self.cfg
        x_all = self.tok(ids) + self.pos(torch.arange(L, device=ids.device))

        n_turns = batch["turn_reg"].shape[1]
        # segment boundaries are batch-uniform by construction (fixed
        # 6-token turns); the query/pad tail is one final segment
        bounds = []
        t0 = turn_ids[0]
        for i in range(n_turns):
            span = (t0 == i).nonzero().flatten()
            s, e = int(span[0]), int(span[-1]) + 1
            if i == 0:
                s = 0                      # BOS rides with the first turn
            bounds.append((s, e))
        bounds.append((bounds[-1][1], L))  # query + padding tail

        reg_state = None
        if cfg.use_register:
            reg_state = self.reg_init.expand(B, cfg.n_agents, cfg.d_reg)

        kv = [None] * cfg.n_layers
        outs = []
        for si, (s, e) in enumerate(bounds):
            if s == e:
                continue
            x = x_all[:, s:e]
            reg_repr = None
            if cfg.use_register:
                reg_repr = self._reg_repr(reg_state, batch["register_keys"])
            for li, blk in enumerate(self.blocks):
                x, kv[li] = blk(x, kv[li], reg_repr)
            outs.append(x)
            if cfg.use_register and si < n_turns:
                reg_state = self._write(reg_state, x,
                                        batch["turn_reg"][:, si])
        h = self.ln_f(torch.cat(outs, dim=1))
        return self.head(h)

    def loss(self, batch) -> torch.Tensor:
        """Next-token CE on answer positions only (the registered training
        signal — supervision reaches the model solely through answers)."""
        logits = self.forward(batch)
        tgt, mask = batch["input_ids"][:, 1:], batch["loss_mask"][:, 1:]
        ce = F.cross_entropy(logits[:, :-1].reshape(-1, self.cfg.vocab),
                             tgt.reshape(-1), reduction="none")
        m = mask.reshape(-1).float()
        return (ce * m).sum() / m.sum().clamp(min=1)

    @torch.no_grad()
    def score_choices(self, batch, choice_ids: list[list[int]]) -> list[int]:
        """Forced-choice eval: at each episode's <ans> position, argmax the
        answer logits restricted to that item's choice set."""
        logits = self.forward(batch)
        ans_pos = batch["loss_mask"].argmax(dim=1) - 1   # predict-from here
        picks = []
        for b in range(len(ans_pos)):
            row = logits[b, ans_pos[b]]
            ids = torch.tensor(choice_ids[b], device=row.device)
            picks.append(int(ids[row[ids].argmax()]))
        return picks


def to_torch(batch: dict, device="cpu") -> dict:
    return {k: torch.as_tensor(v, device=device) for k, v in batch.items()}


def self_test() -> None:
    import curriculum as C
    torch.manual_seed(0)
    cfg = SCALES["smoke"]
    model = MVM0aModel(cfg)
    twin = MVM0aModel(Config(**{**cfg.__dict__, "use_register": False}))

    eps = [C.generate_episode(s) for s in range(6)]
    batch = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                for e in eps]))
    logits = model(batch)
    assert logits.shape == (*batch["input_ids"].shape, cfg.vocab)
    l1, l2 = model.loss(batch), twin.loss(batch)
    assert l1.isfinite() and l2.isfinite()
    l1.backward()
    # the write path must carry gradient (utilization gate's premise)
    assert model.writer.weight_ih.grad is not None and \
        model.writer.weight_ih.grad.abs().sum() > 0
    # twin really has no register machinery
    assert not any("reg" in n or "writer" in n or "xattn" in n
                   for n, _ in twin.named_parameters())
    # register identity comes only from marker keys: identical init rows
    rs = model.reg_init.expand(2, cfg.n_agents, cfg.d_reg)
    assert (rs[0, 0] == rs[0, 1]).all()
    # causality: a token's logits must not depend on later tokens
    b2 = {k: v.clone() for k, v in batch.items()}
    b2["input_ids"][:, -1] = E.VOCAB["<pad>"]
    with torch.no_grad():
        assert torch.allclose(model(batch)[:, :20], model(b2)[:, :20],
                              atol=1e-4), "future token leaked backwards"
    n10 = SCALES["10M"].n_params_approx / 1e6
    n30 = SCALES["30M"].n_params_approx / 1e6
    n100 = SCALES["100M"].n_params_approx / 1e6
    print(f"model self-test OK (smoke loss {float(l1):.3f}; ladder approx "
          f"{n10:.0f}M / {n30:.0f}M / {n100:.0f}M params)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
