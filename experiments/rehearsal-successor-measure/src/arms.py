"""The three architectures of the successor proposal, at rehearsal scale.

UNREGISTERED stand-ins, roughly one to three million parameters each. They
exist to show that the three arms of
`docs/successor-experiment-proposal-2026-09-21.md` (section 5) are
constructible and that the proposal's measure can be read off them. No result
about the scientific question may be read off anything here.

The shared trunk
----------------
Token embedding, learned position embedding, a learned **acting-channel**
vector added wherever the channel fires, four pre-normalised causal
self-attention and feed-forward blocks. The acting channel is the only honest
source of ownership in the episode: the text is identical whoever the model
is.

The ownership answer, computed the same way for the two constructed arms
-------------------------------------------------------------------------
A running, causal, acting-masked tally over the assignment turns: at position
t, the score for agent a is how many of agent a's assignment turns before t
the acting channel fired on. Softmax over the four agents gives the ownership
answer as a distribution, and the ownership vector is the matching blend of
the four agents' marker representations. Before the model's first own turn the
tally is empty and the distribution is flat — the identity genuinely is not
yet knowable, which is what makes control 4 of the proposal (transplanting
before the identity can be known) mean anything.

Arm T — the ownership answer kept separable
-------------------------------------------
The running state is split by construction: content dimensions and a small
block of **ownership dimensions**. The blocks read and write content only;
nothing in the trunk may touch the ownership block, and the module self-test
asserts it by checking the gradient. The ownership vector is written into the
ownership block and carried forward unchanged through every layer. The action
head reads the ownership block as the row selector into a lookup over the
assignment turns, and a learned map over the eight value slots supplies the
revision rule. The factoring into (lookup table, ownership answer, selection)
is the architecture, not something the network may or may not discover.
**Degree zero by construction, and one place to patch.**

Arm C — the ownership answer entangled
--------------------------------------
No block of its own anywhere. The ownership vector enters as a scale-and-shift
on the whole running state at **every** block, and it multiplies the value
representation at the point where item and value are bound, so that "which
item, whose value" is one quantity rather than two. Nothing reads ownership
alone. **Degree should be high, and there should be no single site to patch.**

Arm F — the freely trained system
---------------------------------
The trunk and the acting channel, and no constraint at all on where the
ownership answer may live. This is the shape of system the registered
experiment would actually read.

Patching
--------
`forward` takes a `patch_fn(layer_index, state) -> state` called on the
running state after the input embedding (layer 0) and after every block. That
one hook is what every transplant in `transplant.py` is built from, which is
what makes the ownership-only transplant provably a restriction of the
whole-state transplant to a subspace rather than a different intervention.

Corrigibility: local, toy scale, no network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python arms.py --self-test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import grammar as G

ARMS = ("T", "C", "F")


@dataclass
class Config:
    arm: str = "F"
    vocab: int = len(G.VOCAB)
    d_model: int = 160
    n_layers: int = 4
    n_heads: int = 4
    d_own: int = 24          # width of arm T's ownership block
    d_val: int = 64          # width of arm T's lookup entries
    max_len: int = G.SEQ_LEN

    @property
    def d_content(self) -> int:
        return self.d_model - self.d_own if self.arm == "T" else self.d_model


class Block(nn.Module):
    def __init__(self, width: int, n_heads: int, film: bool, d_own: int):
        super().__init__()
        self.ln1 = nn.LayerNorm(width)
        self.attn = nn.MultiheadAttention(width, n_heads, batch_first=True)
        self.ln2 = nn.LayerNorm(width)
        self.mlp = nn.Sequential(nn.Linear(width, 4 * width), nn.GELU(),
                                 nn.Linear(4 * width, width))
        self.film = film
        if film:
            # the entangled arm's scale-and-shift on the WHOLE running state
            self.to_scale = nn.Linear(d_own, width)
            self.to_shift = nn.Linear(d_own, width)
            nn.init.zeros_(self.to_scale.weight); nn.init.zeros_(self.to_scale.bias)
            nn.init.zeros_(self.to_shift.weight); nn.init.zeros_(self.to_shift.bias)

    def forward(self, x, causal_mask, own_vec):
        h = self.ln1(x)
        a, _ = self.attn(h, h, h, attn_mask=causal_mask, need_weights=False)
        x = x + a
        x = x + self.mlp(self.ln2(x))
        if self.film:
            x = x * (1.0 + self.to_scale(own_vec)) + self.to_shift(own_vec)
        return x


class Arm(nn.Module):
    def __init__(self, cfg: Config):
        super().__init__()
        assert cfg.arm in ARMS
        self.cfg = cfg
        w = cfg.d_content
        self.tok = nn.Embedding(cfg.vocab, w)
        self.pos = nn.Embedding(cfg.max_len, w)
        self.act_vec = nn.Parameter(torch.randn(w) * 0.02)
        self.own_marker = nn.Linear(w, cfg.d_own)
        self.own_sharpness = nn.Parameter(torch.tensor(4.0))
        film = cfg.arm == "C"
        self.blocks = nn.ModuleList(
            [Block(w, cfg.n_heads, film, cfg.d_own) for _ in range(cfg.n_layers)])
        self.lnf = nn.LayerNorm(w)
        if cfg.arm == "C":
            # multiplicative binding: the value representation at each
            # assignment turn is multiplied by the ownership signal, so
            # "which item, whose value" is one quantity rather than two
            self.bind = nn.Linear(cfg.d_own, w)
            nn.init.zeros_(self.bind.weight); nn.init.zeros_(self.bind.bias)
        if cfg.arm == "T":
            self.read_own = nn.Linear(cfg.d_own, cfg.d_own)
            self.own_key = nn.Linear(cfg.d_own, cfg.d_own)
            self.to_val = nn.Linear(w, cfg.d_val)
            self.rule = nn.Sequential(nn.Linear(cfg.d_val, 4 * cfg.d_val), nn.GELU(),
                                      nn.Linear(4 * cfg.d_val, cfg.vocab))
        else:
            self.head = nn.Linear(w, cfg.vocab)

    # ------------------------------------------------------------- pieces

    def _own_vec(self, b) -> torch.Tensor:
        """The ownership answer, causally, at every position: (B, S, d_own)."""
        agent_at = b["assign_agent_at"]                      # (B, S), -1 off-turn
        one = F.one_hot(agent_at.clamp(min=0), G.N_AGENTS).float()
        one = one * (agent_at >= 0).float().unsqueeze(-1)
        tally = torch.cumsum(one * b["acting"].float().unsqueeze(-1), dim=1)
        p_own = torch.softmax(self.own_sharpness * tally, dim=-1)   # (B, S, 4)
        marker = self.own_marker(self.tok(b["agent_marker_tok"]))   # (B, 4, d_own)
        return torch.bmm(p_own, marker), p_own

    def _embed(self, b, own_vec) -> torch.Tensor:
        S = b["tokens"].shape[1]
        pos = torch.arange(S, device=b["tokens"].device)
        x = self.tok(b["tokens"]) + self.pos(pos)[None]
        x = x + self.act_vec[None, None] * b["acting"].float().unsqueeze(-1)
        if self.cfg.arm == "C":
            at_value = torch.zeros_like(b["tokens"], dtype=torch.bool)
            at_value.scatter_(1, b["assign_value_pos"].reshape(x.shape[0], -1), True)
            x = torch.where(at_value.unsqueeze(-1),
                            x * (1.0 + self.bind(own_vec)), x)
        return x

    # ------------------------------------------------------------ forward

    def forward(self, b, patch_fn=None, capture: bool = False):
        """`b` holds torch tensors with the field names `grammar.render` uses.
        Returns logits at the two action positions, (B, 2, vocab)."""
        B, S = b["tokens"].shape
        own_vec, _ = self._own_vec(b)
        x = self._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)

        states = []

        def running(content):
            """The running state as the transplanting code sees it."""
            if self.cfg.arm == "T":
                return torch.cat([content, own_vec], dim=-1)
            return content

        def split(state):
            if self.cfg.arm == "T":
                return state[..., :self.cfg.d_content], state[..., self.cfg.d_content:]
            return state, None

        state = running(x)
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = split(state)

        for li, blk in enumerate(self.blocks):
            x = blk(x, causal, own_vec)
            state = torch.cat([x, own_slot], dim=-1) if own_slot is not None else x
            if patch_fn is not None:
                state = patch_fn(li + 1, state)
            if capture:
                states.append(state)
            x, own_slot = split(state)

        h = self.lnf(x)
        ap = b["action_pos"]                                    # (B, 2)
        gather = ap.unsqueeze(-1).expand(-1, -1, h.shape[-1])
        h_act = torch.gather(h, 1, gather)                      # (B, 2, w)

        if self.cfg.arm != "T":
            logits = self.head(h_act)
            return (logits, states) if capture else logits

        # ---- arm T: read the ownership block, select the row, apply the rule
        slot_act = torch.gather(own_slot, 1,
                                ap.unsqueeze(-1).expand(-1, -1, self.cfg.d_own))
        q = self.read_own(slot_act)                             # (B, 2, d_own)
        k = self.own_key(self.own_marker(self.tok(b["agent_marker_tok"])))
        sel_own = torch.softmax(torch.einsum("bcd,bad->bca", q, k), dim=-1)
        sel_named = F.one_hot(b["action_who"].clamp(max=G.N_AGENTS - 1),
                              G.N_AGENTS).float()
        is_self = (b["action_who"] == G.N_AGENTS).float().unsqueeze(-1)
        sel = is_self * sel_own + (1 - is_self) * sel_named      # (B, 2, 4)

        vals = self.to_val(h)                                    # (B, S, d_val)
        idx = b["assign_value_pos"].reshape(B, -1)               # (B, 4*2)
        tab = torch.gather(vals, 1, idx.unsqueeze(-1).expand(-1, -1, self.cfg.d_val))
        tab = tab.view(B, G.N_AGENTS, G.N_ITEMS_PER_EPISODE, self.cfg.d_val)
        item = b["action_item"]                                  # (B, 2)
        tab_i = torch.gather(
            tab, 2, item[:, None, :, None].expand(-1, G.N_AGENTS, -1, self.cfg.d_val))
        tab_i = tab_i.permute(0, 2, 1, 3)                        # (B, 2, 4, d_val)
        read = torch.einsum("bca,bcad->bcd", sel, tab_i)
        logits = self.rule(read)
        return (logits, states) if capture else logits

    # --------------------------------------------------------------- loss

    def loss(self, b):
        logits = self.forward(b)
        tgt = b["targets"]
        return F.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt.reshape(-1))


def to_torch(arr: dict, device) -> dict:
    return {k: torch.as_tensor(v, device=device) for k, v in arr.items()}


def n_params(m: nn.Module) -> int:
    return sum(p.numel() for p in m.parameters())


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("arms.py self-test")
    torch.manual_seed(0)
    pairs = G.make_pairs(8, seed=1)
    eps = G.episodes_from_pairs(pairs)
    b = to_torch(G.batch(eps), "cpu")

    for arm in ARMS:
        m = Arm(Config(arm=arm))
        logits = m(b)
        check(f"arm {arm} — forward runs and is the right shape",
              tuple(logits.shape) == (len(eps), 2, len(G.VOCAB)),
              f"{n_params(m):,} parameters")
        l = m.loss(b)
        l.backward()
        check(f"arm {arm} — loss is finite and gradients flow",
              torch.isfinite(l).item() and
              any(p.grad is not None and torch.isfinite(p.grad).all() for p in m.parameters()))

    # --- arm T's trunk structurally cannot touch the ownership block -------
    m = Arm(Config(arm="T"))
    logits, states = m(b, capture=True)
    own_blocks = [s[..., m.cfg.d_content:] for s in states]
    same = all(torch.equal(own_blocks[0], o) for o in own_blocks[1:])
    check("arm T — the ownership block is carried unchanged through every layer", same)
    # the content dimensions are not a function of the ownership block: perturb
    # the ownership block at layer 0 and the content at the last layer must not move
    def perturb(li, st):
        if li == 0:
            st = st.clone()
            st[..., m.cfg.d_content:] += 3.0
        return st
    _, st2 = m(b, patch_fn=perturb, capture=True)
    content_moved = not torch.allclose(states[-1][..., :m.cfg.d_content],
                                       st2[-1][..., :m.cfg.d_content], atol=1e-6)
    check("arm T — content never reads the ownership block", not content_moved)
    head_moved = not torch.allclose(logits, m(b, patch_fn=perturb), atol=1e-6)
    check("arm T — but the action head does read it", head_moved)

    # --- arm C has no block carrying ownership alone ----------------------
    mc = Arm(Config(arm="C"))
    own_vec, p_own = mc._own_vec(b)
    check("arm C — the ownership signal reaches every block as a scale-and-shift",
          all(blk.film for blk in mc.blocks))
    check("arm C — no dedicated ownership dimensions exist in its running state",
          mc.cfg.d_content == mc.cfg.d_model)

    # --- the ownership answer is causal -----------------------------------
    e = eps[0]
    first_own = int(np.min(np.where((e["acting"] == 1))[0]))
    flat = p_own[0, :first_own]
    check("the ownership answer is flat before the model's first own turn",
          bool((flat.std(dim=-1) < 1e-6).all()),
          f"first own-turn token at position {first_own}")
    late = p_own[0, -1]
    check("the ownership answer is sharp and correct by the action position",
          int(late.argmax()) == e["model"] and float(late.max()) > 0.9,
          f"model is agent slot {e['model']}, read {float(late.max().detach()):.4f}")

    # --- the acting channel is the only difference between twins ----------
    r = to_torch(G.batch([pairs[0]["recipient"]]), "cpu")
    d = to_torch(G.batch([pairs[0]["donor"]]), "cpu")
    check("twins differ only in the acting channel",
          torch.equal(r["tokens"], d["tokens"]) and not torch.equal(r["acting"], d["acting"]))
    for arm in ARMS:
        mm = Arm(Config(arm=arm))
        check(f"arm {arm} — the twins' states differ, so ownership does reach the state",
              not torch.allclose(mm(r, capture=True)[1][-1], mm(d, capture=True)[1][-1],
                                 atol=1e-6))

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
