"""D9, ADDED AFTER THE FIRST OUTPUTS (not in the method file): D5's trunk-only
lesion applied to arm M's stirred-in items (it1 to it3), own-directed, to see
whether those answers, too, come from the acting channel in the trunk. Same
in-memory wrapping of `_own_vec` as D5."""
import torch
from common import header, load, gate, chunks, separable_mask, G, P

header("D9: arm M's stirred-in items with the acting channel out of the trunk only (gate, own-directed)")
b = gate()
for name in ("M-10M-rerun", "M-toy-seed0"):
    m, _ = load(name)
    orig = m._own_vec
    r = dict(frozen=0, swapped=0, trunk_lesioned=0, n=0)
    for s, sl in chunks(b):
        ent = ~separable_mask(m, sl)
        tgt = sl["targets"][:, G.OWN]
        r["frozen"] += int(((m(sl)[:, G.OWN].argmax(-1) == tgt) & ent).sum())
        r["swapped"] += int(((m(P.swap_answer(sl))[:, G.OWN].argmax(-1) == tgt) & ent).sum())
        les = dict(sl, acting=torch.zeros_like(sl["acting"]))
        try:
            m._own_vec = lambda bb, _src=sl: orig(_src)
            r["trunk_lesioned"] += int(((m(les)[:, G.OWN].argmax(-1) == tgt) & ent).sum())
        finally:
            del m._own_vec
        r["n"] += int(ent.sum())
    n = r["n"]
    print(f"\n{name}: {n} stirred-in own-directed actions")
    for k in ("frozen", "swapped", "trunk_lesioned"):
        print(f"  {k:15s} right {r[k]:5d} ({r[k] / n:.3f})")
