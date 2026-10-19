"""E1, the checking session's own check (prediction committed first in PREDICTION.md).

The trunk sees the acting channel on the next agent round's two assignment
turns instead of the model's own; the built-in ownership answer still reads the
real episode (the same in-memory wrapping of `_own_vec` as D5). If H1 holds,
arm M 10M's separable answers follow the trunk to the next agent; arm T 10M's
and toy arm M's stay with the built-in answer. Read-only; no file of the frozen
code changes."""
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2026-10-18-arm-m-separable-zero-scripts"))
from common import (header, load, gate, chunks, final_parts, table_rows, true_agent,   # noqa: E402
                    separable_mask, agent_answers, G)

TURN = 5   # an assignment turn is five tokens, marker first (grammar.py: acting.extend([mine] * 5))


def redirected_acting(b, shift=1):
    """The acting channel with the model's own two assignment turns switched off
    and the turns of agent (own + shift) mod 4 switched on; action turns unchanged."""
    ac = b["acting"].clone()
    at = b["assign_agent_at"]
    ta = true_agent(b)
    tgt = (ta + shift) % G.N_AGENTS
    B = ac.shape[0]
    for i in range(B):
        own = (at[i] == ta[i]).nonzero().flatten().tolist()
        nxt = (at[i] == tgt[i]).nonzero().flatten().tolist()
        assert len(own) == 2 and len(nxt) == 2
        for p in own:
            assert ac[i, p:p + TURN].tolist() == [1] * TURN
            ac[i, p:p + TURN] = 0
        for p in nxt:
            assert ac[i, p:p + TURN].tolist() == [0] * TURN
            ac[i, p:p + TURN] = 1
    assert torch.equal(ac.sum(1), b["acting"].sum(1))
    return ac, tgt


header("E1: acting channel in the trunk moved to the next agent's assignment turns; "
       "built-in answer reads the real episode (gate, own-directed actions)")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0"):
    m, _ = load(name)
    orig = m._own_vec
    routes = {"separable": [0] * 6} if m.cfg.arm == "T" else {"separable": [0] * 6, "stirred-in": [0] * 6}
    # per route: actions, right unmoved, own answer moved, next agent's answer moved,
    #            own answer moved among those right unmoved, next-agent answer among those right unmoved
    ratio_next, ratio_own = [], []
    for s, sl in chunks(b):
        sep = separable_mask(m, sl)
        ans = agent_answers(sl)
        own_tgt = sl["targets"][:, G.OWN]
        rows = torch.arange(own_tgt.shape[0])
        new_ac, nxt = redirected_acting(sl)
        red = dict(sl, acting=new_ac)
        base = m(sl)[:, G.OWN].argmax(-1)
        try:
            m._own_vec = lambda bb, _src=sl: orig(_src)
            logits, _, h, _ = final_parts(m, red)
        finally:
            del m._own_vec
        assert "_own_vec" not in m.__dict__
        pred = logits[:, G.OWN].argmax(-1)
        next_ans = ans[rows, nxt]
        assert not bool((next_ans == own_tgt).any())
        for route, mask in (("separable", sep), ("stirred-in", ~sep)):
            if route not in routes:
                continue
            r = routes[route]
            ok = (base == own_tgt) & mask
            r[0] += int(mask.sum()); r[1] += int(ok.sum())
            r[2] += int(((pred == own_tgt) & mask).sum()); r[3] += int(((pred == next_ans) & mask).sum())
            r[4] += int(((pred == own_tgt) & ok).sum()); r[5] += int(((pred == next_ans) & ok).sum())
        nrm = table_rows(m, red, h).norm(dim=-1)
        ta = true_agent(sl)
        others = lambda a: (nrm.sum(1) - nrm[rows, a]) / 3
        ratio_next.append((nrm[rows, nxt] / others(nxt))[sep]); ratio_own.append((nrm[rows, ta] / others(ta))[sep])
    print(f"\n{name}")
    for route, (n, ok, own, nx, own_ok, nx_ok) in routes.items():
        print(f"  {route:10s} actions {n:5d}; right unmoved {ok:5d}")
        print(f"             moved: own answer {own:5d} ({own / n:.3f}); next agent's answer {nx:5d} ({nx / n:.3f})")
        print(f"             of those right unmoved: own answer {own_ok:5d} ({own_ok / ok:.3f}); "
              f"next agent's answer {nx_ok:5d} ({nx_ok / ok:.3f})")
    print(f"  separable table rows, moved: next agent's row over the others' mean "
          f"{float(torch.cat(ratio_next).mean()):.3f}; own row over the others' mean {float(torch.cat(ratio_own).mean()):.3f}")
