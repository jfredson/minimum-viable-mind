"""D4: named-other accuracy on the gate, split by the item's route."""
import torch
from common import header, load, gate, chunks, G

header("D4: named-other (and own) accuracy by route, gate episodes")
b = gate()
for name in ("M-10M-rerun", "M-toy-seed0", "T-10M-rerun", "T-toy-seed0"):
    m, _ = load(name)
    acc = {}
    for s, sl in chunks(b):
        pred = m(sl).argmax(-1)
        hit = pred == sl["targets"]
        if m.cfg.arm == "M":
            r = m.entangled_route(sl)
        else:
            r = torch.zeros_like(hit)
        for c, cn in ((G.OWN, "own"), (G.OTHER, "named-other")):
            for rn, mk in (("separable items", ~r[:, c]), ("stirred-in items", r[:, c])):
                k = (cn, rn)
                h, t = acc.get(k, (0, 0))
                acc[k] = (h + int(hit[:, c][mk].sum()), t + int(mk.sum()))
    print(f"\n{name}")
    for (cn, rn), (h, t) in acc.items():
        if t:
            print(f"  {cn:12s} {rn:17s} {h:5d} of {t:5d}  {h / t:.3f}")
