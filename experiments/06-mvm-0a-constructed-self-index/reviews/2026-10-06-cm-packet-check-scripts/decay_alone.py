"""How far would weight decay alone move the ownership sharpness over the
10-million-parameter development runs?

The recipe is the one recorded by `train_successor.py` (pull request 106's
branch): AdamW, peak learning rate 0.002, weight decay 0.01, PyTorch's
one-cycle schedule with the first tenth warming up, 108,919 steps (the
ledger rows of pull request 98). AdamW's decay is decoupled: each step
multiplies every parameter by (1 - lr * decay), whatever the gradient does.
So with no gradient at all, a parameter starting at 4.0 ends at
4.0 * product(1 - lr_t * 0.01). This script asks the real scheduler for
lr_t at every step and multiplies it out. No model is loaded or trained.
"""
import torch

STEPS, PEAK, DECAY, WARM = 108_919, 2e-3, 0.01, 0.1
p = torch.nn.Parameter(torch.tensor(4.0))
opt = torch.optim.AdamW([p], lr=PEAK, weight_decay=DECAY)
sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=PEAK, total_steps=STEPS, pct_start=WARM)
factor, lr_sum = 1.0, 0.0
for _ in range(STEPS):
    lr = opt.param_groups[0]["lr"]
    factor *= 1 - lr * DECAY
    lr_sum += lr
    opt.step()          # no gradient: AdamW skips the parameter, as for arm F
    sched.step()
print(f"sum of learning rates over the run: {lr_sum:.2f}")
print(f"decay alone multiplies a parameter by {factor:.4f}")
print(f"sharpness 4.0 under decay alone would end at {4.0 * factor:+.3f}")
print("measured at the end (pull request 106): arm T +1.947, arm C -0.089, arm M -0.008")
print(f"parameter untouched without a gradient (arm F's case): {float(p.detach()):+.4f}")
