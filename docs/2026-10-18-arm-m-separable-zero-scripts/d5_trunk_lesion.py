"""D5 (H1): the acting channel taken out of the trunk only; the built ownership
answer still computed from the true episode. The lesion is made by wrapping
`_own_vec` on the loaded object in memory; no file of the frozen code changes."""
import torch
from common import header, load, gate, chunks, separable_mask, G, P

header("D5: acting channel removed from the trunk only (gate, own-directed actions)")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0", "T-toy-seed0"):
    m, _ = load(name)
    orig = m._own_vec
    res = {k: [0, 0, 0] for k in ("frozen", "trunk-lesioned")}   # right, still right after swap, actions
    full = [0, 0]
    for s, sl in chunks(b):
        mask = separable_mask(m, sl)
        ssl = P.swap_answer(sl)
        tgt = sl["targets"][:, G.OWN]
        # unlesioned, frozen forward
        base = m(sl)[:, G.OWN].argmax(-1) == tgt
        sw = m(ssl)[:, G.OWN].argmax(-1) == tgt
        # trunk lesioned: trunk sees acting = 0; the ownership answer reads the real acting channel
        les = dict(sl, acting=torch.zeros_like(sl["acting"]))
        les_sw = dict(ssl, acting=torch.zeros_like(ssl["acting"]))
        try:
            m._own_vec = lambda bb, _src=sl: orig(_src)
            lb = m(les)[:, G.OWN].argmax(-1) == tgt
            m._own_vec = lambda bb, _src=ssl: orig(_src)
            lsw = m(les_sw)[:, G.OWN].argmax(-1) == tgt
        finally:
            del m._own_vec          # back to the class's own method
        assert m._own_vec.__func__ is type(m)._own_vec
        for k, (x, y) in (("frozen", (base, sw)), ("trunk-lesioned", (lb, lsw))):
            res[k][0] += int((x & mask).sum()); res[k][1] += int((x & y & mask).sum()); res[k][2] += int(mask.sum())
        # the full lesion (acting zeroed everywhere, as the frozen gate's lesion does), for reference
        full[0] += int(((m(les)[:, G.OWN].argmax(-1) == tgt) & mask).sum()); full[1] += int(mask.sum())
    print(f"\n{name}")
    for k, (r, rs, n) in res.items():
        use = (r - rs) / r if r else float("nan")
        print(f"  {k:15s} right {r:5d} of {n:5d} ({r / n:.3f}); still right after swap {rs:5d}; route use {use:.3f}")
    print(f"  full lesion (acting zeroed in the trunk and in the answer): right {full[0]} of {full[1]} ({full[0] / full[1]:.3f})")
