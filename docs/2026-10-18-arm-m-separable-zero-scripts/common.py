"""Shared, read-only helpers for the arm M separable-zero diagnostics (2026-10-18).

Imports the frozen code from experiments/08-successor-degree/src/ and changes
nothing in it. Method: docs/2026-10-18-arm-m-separable-zero-method.md.
Everything runs on the laptop's processor; no training, no network, $0.
"""
import hashlib
import os
import sys

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(REPO, "experiments", "08-successor-degree", "src")
sys.path.insert(0, SRC)
import grammar as G        # noqa: E402
import models as M         # noqa: E402
import procedure as P      # noqa: E402

# the rerun checkpoints live in the main checkout's untracked artifacts folder
ART = os.path.expanduser("~/Code/minimum-viable-mind/experiments/08-successor-degree/artifacts")
TOY = os.path.join(REPO, "experiments", "08-successor-degree", "out-sharpness-fix", "models")
CKPTS = {
    "M-10M-rerun": (os.path.join(ART, "succ_m_10m_seed0_rerun", "succ_m_10m_seed0_rerun.pt"),
                    "c4701f70e7967e008954640c88e89112"),
    "T-10M-rerun": (os.path.join(ART, "succ_t_10m_seed0_rerun", "succ_t_10m_seed0_rerun.pt"),
                    "c9f2684070a67920577b26f2f1662ffd"),
    "M-toy-seed0": (os.path.join(TOY, "ckpt_M_fixed_seed0.pt"), None),
    "M-toy-seed1": (os.path.join(TOY, "ckpt_M_fixed_seed1.pt"), None),
    "M-toy-seed2": (os.path.join(TOY, "ckpt_M_fixed_seed2.pt"), None),
    "T-toy-seed0": (os.path.join(TOY, "ckpt_T_fixed_seed0.pt"), None),
}

torch.set_grad_enabled(False)


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(name):
    path, want = CKPTS[name]
    got = md5(path)
    if want is not None:
        assert got == want, f"{name}: md5 {got} is not the recorded {want}"
    m, meta = P.load_model(path, None, None)
    return m, dict(meta, md5=got, path=path)


_DATA = {}


def gate():
    """The gate episodes exactly as the frozen procedure builds them."""
    if "gate" not in _DATA:
        _DATA["gate"] = P.EvalData().gate
    return _DATA["gate"]


def true_agent(b):
    at = b["assign_agent_at"]
    one = torch.nn.functional.one_hot(at.clamp(min=0), G.N_AGENTS).float() * (at >= 0).float().unsqueeze(-1)
    return (one * b["acting"].float().unsqueeze(-1)).sum(1).argmax(-1)


def separable_mask(m, b):
    """Own-directed actions on the separable route: all of them for arm T,
    the ~entangled_route ones for arm M (the frozen check's own mask)."""
    n = b["tokens"].shape[0]
    if m.cfg.arm == "M":
        return ~m.entangled_route(b)[:, G.OWN]
    return torch.ones(n, dtype=torch.bool)


def chunks(b, size=500):
    n = b["tokens"].shape[0]
    for s in range(0, n, size):
        yield s, {k: v[s:min(s + size, n)] for k, v in b.items()}


def final_parts(m, b):
    """From the frozen forward with capture: the final running state split
    into the trunk part and the slot, and the trunk after the last norm."""
    logits, states = m(b, capture=True)
    dc = m.cfg.d_content
    st = states[-1]
    x, slot = st[..., :dc], st[..., dc:]
    return logits, states, m.lnf(x), slot


def selection(m, b, slot):
    """The separable head's row choice for the own-directed action, the same
    arithmetic as `_separable_logits` (scores before and weights after the
    softmax), read out rather than recomputed differently."""
    ap = b["action_pos"][:, G.OWN]
    rows = torch.arange(ap.shape[0])
    q = m.read_own(slot[rows, ap])
    k = m.own_key(m.own_marker(m.tok(b["agent_marker_tok"])))
    scores = torch.einsum("bd,bad->ba", q, k)
    return scores, torch.softmax(scores, -1)


def table_rows(m, b, h):
    """Each agent's table row for the own-directed action's item: (B, 4, d_val)."""
    B = h.shape[0]
    vals = m.to_val(h)
    idx = b["assign_value_pos"].reshape(B, -1)
    tab = torch.gather(vals, 1, idx.unsqueeze(-1).expand(-1, -1, m.cfg.d_val))
    tab = tab.view(B, G.N_AGENTS, G.N_ITEMS_PER_EPISODE, m.cfg.d_val)
    item = b["action_item"][:, G.OWN]
    return tab[torch.arange(B), :, item]


SLOT_OF_TOKEN = {G.VOCAB[s]: i for i, s in enumerate(G.SLOTS)}


def agent_answers(b, cond=G.OWN):
    """(B, 4): for each agent, the answer the action would have if that agent
    were the one acted on (the successor of its value on the action's item)."""
    B = b["tokens"].shape[0]
    item = b["action_item"][:, cond]
    out = torch.zeros(B, G.N_AGENTS, dtype=torch.long)
    rows = torch.arange(B)
    for a in range(G.N_AGENTS):
        pos = b["assign_value_pos"][rows, a, item]
        tok = b["tokens"][rows, pos]
        out[:, a] = torch.tensor([G.VOCAB[G.SLOTS[G.successor(SLOT_OF_TOKEN[int(t)])]] for t in tok])
    return out


def header(title):
    import platform
    import sklearn
    print(title)
    print(f"torch {torch.__version__}, scikit-learn {sklearn.__version__}, numpy {np.__version__}, "
          f"python {platform.python_version()}, device cpu")
