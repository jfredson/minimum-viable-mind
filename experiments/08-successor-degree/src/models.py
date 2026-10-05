"""The successor experiment's four models, at three sizes.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`. What it builds is section 5
of `docs/successor-experiment-proposal-2026-10-03-v4.md`.

Where it comes from
-------------------
Copied from the rehearsal's `arms.py` (arms T, C and F) and `arm_middle.py`
(arm M), in `experiments/rehearsal-successor-measure/src/`, with nothing
changed in what they compute: the same layers, the same names for every
weight, so a committed toy model loads here unchanged and gives the same
outputs bit for bit (test T2 of the method note). What is added is the three
sizes, by name, and the one-scored-token check run on the models' own loss.

The four models
---------------
All share a trunk: token embedding, learned position embedding, a learned
**acting-channel** vector added wherever the "this turn is yours" signal
fires, and pre-normalised causal self-attention and feed-forward blocks. The
acting channel is the only honest source of ownership: the text is identical
whoever the model is.

- **Arm T, separable by construction.** The running state is the content
  dimensions followed by a small block holding the ownership answer, which no
  block may read or write; the action head reads that block as the row
  selector into a table of who assigned what. Degree zero by construction.
- **Arm C, entangled by construction.** No block of its own anywhere; the
  ownership answer enters every block as a scale-and-shift on the whole
  running state, and multiplies the value at the point of binding.
- **Arm M, a mixture by item.** Both routes in one network; actions about
  items it1, it2 and it3 go wholly through the entangled route, actions about
  it0 and it4 wholly through the separable one, so about three fifths of
  actions are entangled.
- **Arm F, the freely trained system.** The trunk and the acting channel, and
  no constraint on where the ownership answer lives. This is what is read.

The sizes
---------
`toy` is the rehearsal's (160 wide, 4 blocks, 4 heads). `10M` and `30M` are
the rungs of the programme's scale ladder of those names
(`experiments/06-mvm-0a-constructed-self-index/src/model.py`, `SCALES`):
256 wide with 8 blocks and 8 heads, and 448 wide with 12 blocks and 8 heads.
30M is the registered size; it is the shape the rented slice of 2026-09-25
timed. Arm T's and arm M's ownership block (24 wide) and lookup entries (64
wide) are the same at every size, as the slice timed them (the freeze
session's choice; the method note, section 6, item 3). With a 46-word
vocabulary the parameter counts are below the rung names; the self-test
prints them.

Patching
--------
`forward` takes `patch_fn(layer_index, state) -> state`, called on the running
state after the input embedding (state 0) and after every block. Every
transplant in `transplant.py` is built from this one hook.

Corrigibility: local, no network, no rented machine, $0 [C1/C2].

    python models.py --self-test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import grammar as G

ARMS = ("T", "C", "M", "F")

SIZES = {
    "toy": dict(d_model=160, n_layers=4, n_heads=4),
    "10M": dict(d_model=256, n_layers=8, n_heads=8),
    "30M": dict(d_model=448, n_layers=12, n_heads=8),
}
REGISTERED_SIZE = "30M"

ENTANGLED_ITEMS = ("it1", "it2", "it3")          # arm M's entangled route
ENTANGLED_ITEM_IDS = tuple(G.VOCAB[i] for i in ENTANGLED_ITEMS)


@dataclass
class Config:
    arm: str = "F"
    vocab: int = len(G.VOCAB)
    d_model: int = 160
    n_layers: int = 4
    n_heads: int = 4
    d_own: int = 24          # width of the ownership block (arms T and M)
    d_val: int = 64          # width of the lookup entries (arms T and M)
    max_len: int = G.SEQ_LEN

    @property
    def d_content(self) -> int:
        return self.d_model - self.d_own if self.arm in ("T", "M") else self.d_model

    @property
    def n_states(self) -> int:
        """Running states the transplanting code sees: after the input
        embedding, and after each block."""
        return self.n_layers + 1


def config_for(arm: str, size: str) -> Config:
    if arm not in ARMS:
        raise ValueError(f"unknown arm {arm!r}; the arms are {ARMS}")
    if size not in SIZES:
        raise ValueError(f"unknown size {size!r}; the sizes are {tuple(SIZES)}")
    return Config(arm=arm, **SIZES[size])


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
            # the entangled route's scale-and-shift on the WHOLE running state
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


class _Shared(nn.Module):
    """What every arm has: the ownership answer, the embedding, the separable
    head, and the loss. Kept as methods so the four classes below stay what
    the rehearsal's were."""

    def _own_vec(self, b):
        """The ownership answer, causally, at every position: (B, S, d_own).
        A running tally over the assignment turns of how often the acting
        channel fired on each agent's turns; flat before the model's first own
        turn, when the identity genuinely is not yet knowable."""
        agent_at = b["assign_agent_at"]
        one = F.one_hot(agent_at.clamp(min=0), G.N_AGENTS).float()
        one = one * (agent_at >= 0).float().unsqueeze(-1)
        tally = torch.cumsum(one * b["acting"].float().unsqueeze(-1), dim=1)
        p_own = torch.softmax(self.own_sharpness * tally, dim=-1)
        marker = self.own_marker(self.tok(b["agent_marker_tok"]))
        return torch.bmm(p_own, marker), p_own

    def _separable_logits(self, b, h, own_slot):
        """Arm T's head: read the ownership block, select the row, apply the
        rule. Used by arm T, and by arm M's separable route."""
        B = h.shape[0]
        ap = b["action_pos"]
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
        return self.rule(torch.einsum("bca,bcad->bcd", sel, tab_i))

    def loss(self, b):
        """Cross-entropy at the two scored positions of every episode, and
        nowhere else: `forward` returns logits only at `action_pos`."""
        logits = self.forward(b)
        tgt = b["targets"]
        return F.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt.reshape(-1))


class Arm(_Shared):
    """Arms T, C and F: the rehearsal's `arms.Arm`, unchanged."""

    def __init__(self, cfg: Config):
        super().__init__()
        assert cfg.arm in ("T", "C", "F")
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

    def _embed(self, b, own_vec):
        S = b["tokens"].shape[1]
        pos = torch.arange(S, device=b["tokens"].device)
        x = self.tok(b["tokens"]) + self.pos(pos)[None]
        x = x + self.act_vec[None, None] * b["acting"].float().unsqueeze(-1)
        if self.cfg.arm == "C":
            at_value = torch.zeros_like(b["tokens"], dtype=torch.bool)
            at_value.scatter_(1, b["assign_value_pos"].reshape(x.shape[0], -1), True)
            x = torch.where(at_value.unsqueeze(-1), x * (1.0 + self.bind(own_vec)), x)
        return x

    def forward(self, b, patch_fn=None, capture: bool = False):
        """Returns logits at the two action positions, (B, 2, vocab)."""
        B, S = b["tokens"].shape
        own_vec, _ = self._own_vec(b)
        x = self._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)
        states = []
        sep = self.cfg.arm == "T"
        dc = self.cfg.d_content

        state = torch.cat([x, own_vec], dim=-1) if sep else x
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = (state[..., :dc], state[..., dc:]) if sep else (state, None)

        for li, blk in enumerate(self.blocks):
            x = blk(x, causal, own_vec)
            state = torch.cat([x, own_slot], dim=-1) if sep else x
            if patch_fn is not None:
                state = patch_fn(li + 1, state)
            if capture:
                states.append(state)
            x, own_slot = (state[..., :dc], state[..., dc:]) if sep else (state, None)

        h = self.lnf(x)
        if not sep:
            ap = b["action_pos"]
            h_act = torch.gather(h, 1, ap.unsqueeze(-1).expand(-1, -1, h.shape[-1]))
            logits = self.head(h_act)
        else:
            logits = self._separable_logits(b, h, own_slot)
        return (logits, states) if capture else logits


class MiddleArm(_Shared):
    """Arm M: the rehearsal's `arm_middle.MiddleArm`, unchanged."""

    def __init__(self, cfg: Config):
        super().__init__()
        assert cfg.arm == "M"
        self.cfg = cfg
        w = cfg.d_content
        self.tok = nn.Embedding(cfg.vocab, w)
        self.pos = nn.Embedding(cfg.max_len, w)
        self.act_vec = nn.Parameter(torch.randn(w) * 0.02)
        self.own_marker = nn.Linear(w, cfg.d_own)
        self.own_sharpness = nn.Parameter(torch.tensor(4.0))
        self.blocks = nn.ModuleList(
            [Block(w, cfg.n_heads, True, cfg.d_own) for _ in range(cfg.n_layers)])
        self.lnf = nn.LayerNorm(w)
        self.bind = nn.Linear(cfg.d_own, w)
        nn.init.zeros_(self.bind.weight); nn.init.zeros_(self.bind.bias)
        self.head = nn.Linear(w, cfg.vocab)
        self.read_own = nn.Linear(cfg.d_own, cfg.d_own)
        self.own_key = nn.Linear(cfg.d_own, cfg.d_own)
        self.to_val = nn.Linear(w, cfg.d_val)
        self.rule = nn.Sequential(nn.Linear(cfg.d_val, 4 * cfg.d_val), nn.GELU(),
                                  nn.Linear(4 * cfg.d_val, cfg.vocab))

    def _embed(self, b, own_vec):
        S = b["tokens"].shape[1]
        pos = torch.arange(S, device=b["tokens"].device)
        x = self.tok(b["tokens"]) + self.pos(pos)[None]
        x = x + self.act_vec[None, None] * b["acting"].float().unsqueeze(-1)
        at_value = torch.zeros_like(b["tokens"], dtype=torch.bool)
        at_value.scatter_(1, b["assign_value_pos"].reshape(x.shape[0], -1), True)
        return torch.where(at_value.unsqueeze(-1), x * (1.0 + self.bind(own_vec)), x)

    def entangled_route(self, b) -> torch.Tensor:
        """(B, 2) boolean: which actions the entangled route answers, read off
        the item word two tokens before the mask."""
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
        logits_sep = self._separable_logits(b, h, own_slot)
        route = self.entangled_route(b).unsqueeze(-1)
        logits = torch.where(route, logits_ent, logits_sep)
        return (logits, states) if capture else logits


def build(arm: str, size: str) -> nn.Module:
    cfg = config_for(arm, size)
    return MiddleArm(cfg) if arm == "M" else Arm(cfg)


def build_from_config(cfg: dict) -> nn.Module:
    c = Config(**cfg)
    return MiddleArm(c) if c.arm == "M" else Arm(c)


def config_dict(m: nn.Module) -> dict:
    return asdict(m.cfg)


def to_torch(arr: dict, device) -> dict:
    return {k: torch.as_tensor(v, device=device) for k, v in arr.items()}


def n_params(m: nn.Module) -> int:
    return sum(p.numel() for p in m.parameters())


# ---------------------------------------------------------------- self-test

def self_test(sizes=("toy", "10M", "30M")) -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("models.py self-test")
    torch.manual_seed(0)
    pairs = G.make_pairs(32, seed=1)
    eps = G.episodes_from_pairs(pairs)
    b = to_torch(G.batch(eps), "cpu")

    for size in sizes:
        for arm in ARMS:
            torch.manual_seed(0)
            m = build(arm, size)
            logits, states = m(b, capture=True)
            check(f"{size} arm {arm}: forward runs, right shape, {m.cfg.n_states} running states",
                  tuple(logits.shape) == (len(eps), 2, len(G.VOCAB))
                  and len(states) == m.cfg.n_states
                  and all(s.shape[-1] == m.cfg.d_model for s in states),
                  f"{n_params(m):,} parameters")
            l = m.loss(b)
            l.backward()
            check(f"{size} arm {arm}: loss finite and gradients flow",
                  bool(torch.isfinite(l)) and any(p.grad is not None and bool(torch.isfinite(p.grad).all())
                                                  for p in m.parameters()))

    # --- the one-scored-token check (RT-59) on the models' own loss --------
    for arm in ARMS:
        torch.manual_seed(0)
        m = build(arm, "toy").eval()
        with torch.no_grad():
            logits = m(b)
            want = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), b["targets"].reshape(-1))
            got = m.loss(b)
        check(f"RT-59, arm {arm}: the loss is the cross-entropy over exactly the two "
              f"scored positions per episode", torch.equal(want, got)
              and logits.shape[1] == 2)
        # nothing after the later scored position can reach the loss, and the
        # cue just before a scored position does: so the scoring is not shifted
        last = int(b["action_pos"].max())
        after = {k: v.clone() for k, v in b.items()}
        after["tokens"][:, last + 1:] = G.VOCAB[G.NL]
        before = {k: v.clone() for k, v in b.items()}
        rows = torch.arange(before["tokens"].shape[0])
        before["tokens"][rows, before["action_pos"][:, G.OWN] - 1] = G.VOCAB["revise"]
        with torch.no_grad():
            unchanged = torch.equal(m.loss(after), got)
            changed = not torch.equal(m.loss(before), got)
        if arm == "T":
            # arm T's answer is built only from the assignment turns and its
            # ownership block, so by construction the cue cannot reach it
            check("RT-59, arm T: tokens after the scored positions cannot change the loss "
                  "(and, by construction, neither can the cue before them)",
                  unchanged and not changed)
        else:
            check(f"RT-59, arm {arm}: tokens after the scored positions cannot change the loss; "
                  f"the cue before them can", unchanged and changed)
        probs = G.scored_token_check({k: v.numpy() for k, v in b.items()})
        check(f"RT-59, arm {arm}: the batch the loss is computed on passes the generator's check",
              not probs, "; ".join(probs))

    # --- arm T: the trunk structurally cannot touch the ownership block ----
    for size in sizes:
        m = build("T", size)
        logits, states = m(b, capture=True)
        dc = m.cfg.d_content
        same = all(torch.equal(states[0][..., dc:], s[..., dc:]) for s in states[1:])

        def perturb(li, st):
            if li == 0:
                st = st.clone(); st[..., dc:] += 3.0
            return st
        _, st2 = m(b, patch_fn=perturb, capture=True)
        content_moved = not torch.allclose(states[-1][..., :dc], st2[-1][..., :dc], atol=1e-6)
        head_moved = not torch.allclose(logits, m(b, patch_fn=perturb), atol=1e-6)
        check(f"{size} arm T: the ownership block passes every layer unchanged, content "
              f"never reads it, the head does", same and not content_moved and head_moved)

    # --- arm C: no block of its own -----------------------------------------
    mc = build("C", "toy")
    check("arm C: the ownership signal reaches every block as a scale-and-shift, "
          "and its running state has no ownership dimensions",
          all(blk.film for blk in mc.blocks) and mc.cfg.d_content == mc.cfg.d_model)

    # --- arm M: the routes ---------------------------------------------------
    for size in sizes:
        mm = build("M", size).eval()
        route = mm.entangled_route(b)
        share = float(route[:, G.OWN].float().mean())
        dc = mm.cfg.d_content

        def perturb(li, st):
            if li == 0:
                st = st.clone(); st[..., dc:] += 3.0
            return st
        with torch.no_grad():
            base = mm(b)
            moved = (mm(b, patch_fn=perturb) - base).abs().amax(-1)
        check(f"{size} arm M: about three fifths entangled; the slot never moves an "
              f"entangled action and does move separable ones",
              0.5 < share < 0.7 and float(moved[route].max()) < 1e-5
              and float(moved[~route].max()) > 1e-3, f"share {share:.4f}")

    # --- the ownership answer is causal --------------------------------------
    m = build("F", "toy")
    _, p_own = m._own_vec(b)
    e = eps[0]
    first_own = int(np.min(np.where(e["acting"] == 1)[0]))
    check("the ownership answer is flat before the model's first own turn and correct "
          "by the action",
          bool((p_own[0, :first_own].std(dim=-1) < 1e-6).all())
          and int(p_own[0, -1].argmax()) == e["model"])

    # --- twins differ only in the acting channel, and it reaches the state ---
    r = to_torch(G.batch([pairs[0]["recipient"]]), "cpu")
    d = to_torch(G.batch([pairs[0]["donor"]]), "cpu")
    for arm in ARMS:
        mm = build(arm, "toy")
        check(f"arm {arm}: the twins' final states differ",
              not torch.allclose(mm(r, capture=True)[1][-1], mm(d, capture=True)[1][-1], atol=1e-6))

    # --- a model rebuilt from its saved configuration is the same model ------
    for arm in ARMS:
        m1 = build(arm, "10M")
        m2 = build_from_config(config_dict(m1))
        m2.load_state_dict(m1.state_dict(), strict=True)
        with torch.no_grad():
            same = torch.equal(m1.eval()(b), m2.eval()(b))
        check(f"10M arm {arm}: rebuilt from its saved configuration, bit-identical", same)

    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--sizes", default="toy,10M,30M")
    a = ap.parse_args()
    if a.self_test:
        self_test(tuple(a.sizes.split(",")))
    else:
        ap.print_help()
