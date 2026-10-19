"""D2 (H2): does the swap reach the slot and move the row choice, in arm M as in arm T?"""
import torch
from common import header, load, gate, chunks, final_parts, selection, true_agent, separable_mask, G, P

header("D2: does the swapped answer reach the separable route? (gate, own-directed actions)")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0", "T-toy-seed0"):
    m, _ = load(name)
    moved, size, w_true, w_next_sw, w_true_sw, top_true, top_next_sw, cnt = [], [], [], [], [], [], [], 0
    for s, sl in chunks(b):
        mask = separable_mask(m, sl)
        ssl = P.swap_answer(sl)
        _, _, _, slot = final_parts(m, sl)
        _, _, _, slot_s = final_parts(m, ssl)
        rows = torch.arange(sl["tokens"].shape[0])
        ap = sl["action_pos"][:, G.OWN]
        d = (slot[rows, ap] - slot_s[rows, ap]).norm(dim=-1)
        ta = true_agent(sl)
        nxt = (ta + 1) % G.N_AGENTS
        _, p = selection(m, sl, slot)
        _, ps = selection(m, ssl, slot_s)
        moved.append((d > 1e-6)[mask]); size.append(d[mask])
        w_true.append(p[rows, ta][mask]); w_true_sw.append(ps[rows, ta][mask]); w_next_sw.append(ps[rows, nxt][mask])
        top_true.append((p.argmax(-1) == ta)[mask]); top_next_sw.append((ps.argmax(-1) == nxt)[mask])
    cat = lambda xs: torch.cat(xs).float()
    print(f"\n{name}: {int(cat(moved).numel())} separable own-directed actions")
    print(f"  (a) slot at the action moves under the swap: {int(cat(moved).sum())} of them; "
          f"mean size of the move {float(cat(size).mean()):.4f}")
    print(f"  (b) row choice, true answer: mean weight on the true agent {float(cat(w_true).mean()):.4f}, "
          f"true agent's row the top choice {int(cat(top_true).sum())}")
    print(f"      row choice, swapped answer: mean weight on the next agent {float(cat(w_next_sw).mean()):.4f}, "
          f"on the true agent {float(cat(w_true_sw).mean()):.4f}, next agent's row the top choice {int(cat(top_next_sw).sum())}")
