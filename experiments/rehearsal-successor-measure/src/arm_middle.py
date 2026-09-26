"""Arm M — the fourth arm, built to be partly separable by construction.

UNREGISTERED, toy scale. Built for the rehearsal repairs of 2026-09-25 under
page 5 of `docs/rulings/2026-09-26-weekend-1-queue.md`, which asks for "a
fourth, partially separable arm ... with its predicted reading stated before it
runs". The construction and the prediction are in
`docs/rehearsal-repairs-method-2026-09-25.md`, section 5, committed before this
file.

What it is
----------
Both of the constructed arms' routes to the answer, in one network, with the
**item** the action is about deciding which route answers:

- a slot of its own for the ownership answer, carried unchanged through every
  layer and read only by an arm-T-style head — the **separable route**;
- the ownership answer multiplied into every block and into the value
  representations, read by an ordinary output layer, as in arm C — the
  **entangled route**;
- actions about items `it1`, `it2`, `it3` go through the entangled route,
  actions about `it0` and `it4` through the separable one. The training and
  fresh pools draw items `it0` to `it4` with equal chance, so about three fifths
  of actions are entangled.

Every trial is therefore either fully separable or fully entangled, and the
arm's degree is the share of the identity-driven effect that the entangled
route carries. That is a mixture by item, not a partial separation inside each
trial, and the method file says so before it runs.

The running state the transplanting code sees is the content dimensions
followed by the slot, exactly as arm T's, so every transplant, read and control
in the rehearsal applies to it unchanged.

Corrigibility: local, toy scale, no network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python arm_middle.py --self-test
"""
from __future__ import annotations

import argparse

import torch
import torch.nn as nn
import torch.nn.functional as F

import arms as A
import grammar as G

ENTANGLED_ITEMS = ("it1", "it2", "it3")
ENTANGLED_ITEM_IDS = tuple(G.VOCAB[i] for i in ENTANGLED_ITEMS)


class MiddleConfig(A.Config):
    """Arm T's widths, so the slot and the content block are the same sizes."""

    @property
    def d_content(self) -> int:
        return self.d_model - self.d_own


class MiddleArm(nn.Module):
    def __init__(self, cfg: MiddleConfig | None = None):
        super().__init__()
        cfg = cfg or MiddleConfig(arm="M")
        self.cfg = cfg
        w = cfg.d_content
        self.tok = nn.Embedding(cfg.vocab, w)
        self.pos = nn.Embedding(cfg.max_len, w)
        self.act_vec = nn.Parameter(torch.randn(w) * 0.02)
        self.own_marker = nn.Linear(w, cfg.d_own)
        self.own_sharpness = nn.Parameter(torch.tensor(4.0))
        # the entangled route: scale-and-shift at every block, and binding
        self.blocks = nn.ModuleList(
            [A.Block(w, cfg.n_heads, True, cfg.d_own) for _ in range(cfg.n_layers)])
        self.lnf = nn.LayerNorm(w)
        self.bind = nn.Linear(cfg.d_own, w)
        nn.init.zeros_(self.bind.weight); nn.init.zeros_(self.bind.bias)
        self.head = nn.Linear(w, cfg.vocab)
        # the separable route: arm T's head
        self.read_own = nn.Linear(cfg.d_own, cfg.d_own)
        self.own_key = nn.Linear(cfg.d_own, cfg.d_own)
        self.to_val = nn.Linear(w, cfg.d_val)
        self.rule = nn.Sequential(nn.Linear(cfg.d_val, 4 * cfg.d_val), nn.GELU(),
                                  nn.Linear(4 * cfg.d_val, cfg.vocab))

    # the ownership answer and the embedding are arm C's, verbatim
    _own_vec = A.Arm._own_vec

    def _embed(self, b, own_vec):
        S = b["tokens"].shape[1]
        pos = torch.arange(S, device=b["tokens"].device)
        x = self.tok(b["tokens"]) + self.pos(pos)[None]
        x = x + self.act_vec[None, None] * b["acting"].float().unsqueeze(-1)
        at_value = torch.zeros_like(b["tokens"], dtype=torch.bool)
        at_value.scatter_(1, b["assign_value_pos"].reshape(x.shape[0], -1), True)
        return torch.where(at_value.unsqueeze(-1), x * (1.0 + self.bind(own_vec)), x)

    def entangled_route(self, b) -> torch.Tensor:
        """(B, 2) boolean: which of the two actions the entangled route answers.
        Read off the item word in the action turn, two tokens before the mask."""
        ap = b["action_pos"]
        item_tok = torch.gather(b["tokens"], 1, ap - 2)
        ids = torch.as_tensor(ENTANGLED_ITEM_IDS, device=item_tok.device)
        return (item_tok[..., None] == ids).any(-1)

    def forward(self, b, patch_fn=None, capture: bool = False):
        B, S = b["tokens"].shape
        own_vec, _ = self._own_vec(b)
        x = self._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)
        dc = self.cfg.d_content
        states = []

        state = torch.cat([x, own_vec], dim=-1)
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = state[..., :dc], state[..., dc:]
        for li, blk in enumerate(self.blocks):
            x = blk(x, causal, own_vec)
            state = torch.cat([x, own_slot], dim=-1)
            if patch_fn is not None:
                state = patch_fn(li + 1, state)
            if capture:
                states.append(state)
            x, own_slot = state[..., :dc], state[..., dc:]

        h = self.lnf(x)
        ap = b["action_pos"]
        h_act = torch.gather(h, 1, ap.unsqueeze(-1).expand(-1, -1, h.shape[-1]))
        logits_ent = self.head(h_act)

        # the separable route, as arm T's head
        slot_act = torch.gather(own_slot, 1, ap.unsqueeze(-1).expand(-1, -1, self.cfg.d_own))
        q = self.read_own(slot_act)
        k = self.own_key(self.own_marker(self.tok(b["agent_marker_tok"])))
        sel_own = torch.softmax(torch.einsum("bcd,bad->bca", q, k), dim=-1)
        sel_named = F.one_hot(b["action_who"].clamp(max=G.N_AGENTS - 1), G.N_AGENTS).float()
        is_self = (b["action_who"] == G.N_AGENTS).float().unsqueeze(-1)
        sel = is_self * sel_own + (1 - is_self) * sel_named
        vals = self.to_val(h)
        idx = b["assign_value_pos"].reshape(B, -1)
        tab = torch.gather(vals, 1, idx.unsqueeze(-1).expand(-1, -1, self.cfg.d_val))
        tab = tab.view(B, G.N_AGENTS, G.N_ITEMS_PER_EPISODE, self.cfg.d_val)
        item = b["action_item"]
        tab_i = torch.gather(
            tab, 2, item[:, None, :, None].expand(-1, G.N_AGENTS, -1, self.cfg.d_val))
        tab_i = tab_i.permute(0, 2, 1, 3)
        logits_sep = self.rule(torch.einsum("bca,bcad->bcd", sel, tab_i))

        route = self.entangled_route(b).unsqueeze(-1)
        logits = torch.where(route, logits_ent, logits_sep)
        return (logits, states) if capture else logits

    def loss(self, b):
        logits = self.forward(b)
        tgt = b["targets"]
        return F.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt.reshape(-1))


def build() -> MiddleArm:
    return MiddleArm(MiddleConfig(arm="M"))


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("arm_middle.py self-test")
    torch.manual_seed(0)
    pairs = G.make_pairs(400, seed=1)
    eps = G.episodes_from_pairs(pairs)
    b = A.to_torch(G.batch(eps), "cpu")
    m = build()
    logits = m(b)
    check("forward runs and is the right shape",
          tuple(logits.shape) == (len(eps), 2, len(G.VOCAB)),
          f"{A.n_params(m):,} parameters")
    l = m.loss(b); l.backward()
    check("loss is finite and gradients flow", bool(torch.isfinite(l)))

    route = m.entangled_route(b)
    share = float(route[:, G.OWN].float().mean())
    check("about three fifths of own-directed actions take the entangled route",
          0.5 < share < 0.7, f"share {share:.4f} over {len(eps)} episodes")

    logits, states = m(b, capture=True)
    dc = m.cfg.d_content
    same = all(torch.equal(states[0][..., dc:], s[..., dc:]) for s in states[1:])
    check("the slot is carried unchanged through every layer", same)

    def perturb(li, st):
        if li == 0:
            st = st.clone(); st[..., dc:] += 3.0
        return st
    moved = (m(b, patch_fn=perturb) - logits).abs().amax(-1)       # (B, 2)
    ent_moved = float(moved[route].max())
    sep_moved = float(moved[~route].max())
    check("perturbing the slot never moves an entangled-route action",
          ent_moved < 1e-5, f"largest logit movement there {ent_moved:.2e}")
    check("perturbing the slot does move separable-route actions",
          sep_moved > 1e-3, f"largest logit movement there {sep_moved:.2e}")

    r = A.to_torch(G.batch([pairs[0]["recipient"]]), "cpu")
    d = A.to_torch(G.batch([pairs[0]["donor"]]), "cpu")
    check("the twins' content states differ, so ownership reaches the entangled route",
          not torch.allclose(m(r, capture=True)[1][-1][..., :dc],
                             m(d, capture=True)[1][-1][..., :dc], atol=1e-6))

    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
    else:
        ap.print_help()
