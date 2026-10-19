"""D6 (H4): decay arithmetic for both recipes; weight sizes, end against start;
how flat the row choice is."""
import torch
from common import header, load, gate, chunks, final_parts, selection, true_agent, separable_mask, G, M

header("D6: weight decay, weight sizes and the flatness of the row choice")


def decay_factor(steps, peak, decay, warm):
    p = torch.nn.Parameter(torch.tensor(4.0))
    opt = torch.optim.AdamW([p], lr=peak, weight_decay=decay)
    sch = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=peak, total_steps=steps, pct_start=warm)
    f = 1.0
    for _ in range(steps):
        f *= 1 - opt.param_groups[0]["lr"] * decay
        opt.step(); sch.step()
    return f


print("(a) what decoupled weight decay alone multiplies a weight by over the run")
print(f"    10 million recipe (108,919 steps, peak 0.002, decay 0.01, first tenth warming): {decay_factor(108_919, 2e-3, 0.01, 0.1):.4f}")
print(f"    toy recipe (2,500 steps, peak 0.003, decay 0.01, first tenth warming):          {decay_factor(2_500, 3e-3, 0.01, 0.1):.4f}")

NAMES = ["read_own.weight", "read_own.bias", "own_key.weight", "own_key.bias", "own_marker.weight",
         "to_val.weight", "rule.0.weight", "rule.2.weight", "act_vec", "bind.weight"]
print("\n(b) weight sizes (Frobenius norm): end, start (rebuilt with the trainer's seed), end over start")
for name in ("M-10M-rerun", "T-10M-rerun"):
    m, _ = load(name)
    torch.manual_seed(0)
    m0 = M.build(m.cfg.arm, "10M")
    sd, sd0 = m.state_dict(), m0.state_dict()
    print(f"  {name}")
    for k in NAMES:
        if k in sd:
            e, s = float(sd[k].norm()), float(sd0[k].norm())
            print(f"    {k:18s} end {e:8.4f}  start {s:8.4f}  ratio {e / s if s else float('nan'):7.4f}")
    film = [k for k in sd if "to_scale.weight" in k or "to_shift.weight" in k]
    if film:
        e = sum(float(sd[k].norm()) ** 2 for k in film) ** 0.5
        print(f"    {'FiLM weights, all':18s} end {e:8.4f}  start  0.0000  (built at zero)")

print("\n(c) the row choice at the own-directed action (separable actions), true answer")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0", "T-toy-seed0"):
    m, _ = load(name)
    gaps, tops, spread, qn = [], [], [], []
    for s, sl in chunks(b):
        mask = separable_mask(m, sl)
        _, _, _, slot = final_parts(m, sl)
        sc, p = selection(m, sl, slot)
        top2 = sc.topk(2, -1).values
        gaps.append((top2[:, 0] - top2[:, 1])[mask]); tops.append(p.max(-1).values[mask])
        spread.append(sc.std(-1)[mask])
        rows = torch.arange(sl["tokens"].shape[0])
        qn.append(m.read_own(slot[rows, sl["action_pos"][:, G.OWN]]).norm(dim=-1)[mask])
    c = lambda xs: torch.cat(xs)
    print(f"  {name:12s} score gap top minus second {float(c(gaps).mean()):8.3f}; weight on top row "
          f"{float(c(tops).mean()):.4f} (flat would be 0.25); spread of scores across agents "
          f"{float(c(spread).mean()):.3f}; size of the slot's query {float(c(qn).mean()):.3f}")
