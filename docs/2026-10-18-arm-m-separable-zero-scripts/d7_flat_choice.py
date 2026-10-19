"""D7, ADDED AFTER THE FIRST OUTPUTS (not in the method file): D2 found arm M's
row choice flat and D3 found its own row larger than the others. This asks
whether a flat (one quarter each) mixture of the four rows is enough to give
the own answer, and whether that survives taking the acting channel out of
the trunk. The lesion wraps `_own_vec` on the loaded object in memory, as in D5."""
import torch
from common import header, load, gate, chunks, final_parts, table_rows, true_agent, separable_mask, G

header("D7: the separable head fed a flat mixture of the four rows (gate, own-directed actions)")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0", "T-toy-seed0"):
    m, _ = load(name)
    orig = m._own_vec
    out = {k: 0 for k in ("n", "check", "frozen", "flat", "flat_lesioned", "true_row_lesioned")}
    ratio, ratio_l = [], []
    for s, sl in chunks(b):
        mask = separable_mask(m, sl)
        ta = true_agent(sl)
        rows = torch.arange(sl["tokens"].shape[0])
        tgt = sl["targets"][:, G.OWN]
        logits, _, h, _ = final_parts(m, sl)
        tr = table_rows(m, sl, h)                                       # (B, 4, d_val)
        # sanity: the rule on the true agent's row is what the head gives with that row forced
        f = dict(sl); f["action_who"] = sl["action_who"].clone(); f["action_who"][:, G.OWN] = ta
        out["check"] += int((~torch.isclose(m.rule(tr[rows, ta]), m(f)[:, G.OWN], atol=1e-4).all(-1) & mask).sum())
        flat = m.rule(tr.mean(1)).argmax(-1) == tgt
        les = dict(sl, acting=torch.zeros_like(sl["acting"]))
        try:
            m._own_vec = lambda bb, _src=sl: orig(_src)
            _, _, h_l, _ = final_parts(m, les)
        finally:
            del m._own_vec
        tr_l = table_rows(m, les, h_l)
        flat_l = m.rule(tr_l.mean(1)).argmax(-1) == tgt
        true_l = m.rule(tr_l[rows, ta]).argmax(-1) == tgt
        out["n"] += int(mask.sum())
        out["frozen"] += int(((logits[:, G.OWN].argmax(-1) == tgt) & mask).sum())
        out["flat"] += int((flat & mask).sum())
        out["flat_lesioned"] += int((flat_l & mask).sum())
        out["true_row_lesioned"] += int((true_l & mask).sum())
        nrm, nrm_l = tr.norm(dim=-1), tr_l.norm(dim=-1)
        other = lambda x: (x.sum(1) - x[rows, ta]) / 3
        ratio.append((nrm[rows, ta] / other(nrm))[mask]); ratio_l.append((nrm_l[rows, ta] / other(nrm_l))[mask])
    n = out["n"]
    print(f"\n{name}: {n} separable own-directed actions "
          f"(sanity: rule on the true row differs from the forced-row head in {out['check']})")
    print(f"  frozen head, own answer right:                         {out['frozen']:5d} ({out['frozen'] / n:.3f})")
    print(f"  flat mixture of the four rows, own answer right:       {out['flat']:5d} ({out['flat'] / n:.3f})")
    print(f"  flat mixture, acting channel out of the trunk:         {out['flat_lesioned']:5d} ({out['flat_lesioned'] / n:.3f})")
    print(f"  true agent's row alone, acting channel out of trunk:   {out['true_row_lesioned']:5d} ({out['true_row_lesioned'] / n:.3f})")
    print(f"  own row's size over the other rows' mean size: {float(torch.cat(ratio).mean()):.3f}; "
          f"with the acting channel out of the trunk: {float(torch.cat(ratio_l).mean()):.3f}")
