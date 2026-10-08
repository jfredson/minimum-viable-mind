"""How many operations one training step does, per arm, at 10 million, and
how long the training data takes to make.

Builds each arm at the 10M size from the frozen code and runs training steps
(forward, backward, clip, optimiser) on the processor at the runs' batch of
96, counting the operator calls the profiler sees in one step. On a card at
this size, time per step follows the number of small operations more than
their size, so the ratio of counts is set beside the ratio of measured
seconds per step on the card. Also times `TrainingStream.batch_for_step`,
the data generation the trainer runs on a background thread. ARGUED as an
explanation, not a card measurement. $0.

    python op_count.py SRC_DIR
"""
import sys, time
sys.path.insert(0, sys.argv[1])
import torch
from torch.profiler import profile, ProfilerActivity
import grammar as G, models as M

card = {"T": 0.0099, "C": 0.01002, "F": 0.00934, "M": 0.01447}   # the runs' final sec_per_step
stream = G.TrainingStream(0)
t0 = time.time(); raw = [stream.batch_for_step(s, 96) for s in range(1, 41)]
gen = (time.time() - t0) / 40
print(f"data generation on this laptop: {gen*1000:.1f} ms per batch of 96 (40 batches, one thread)")
b = M.to_torch(raw[0], "cpu")
rows = {}
for arm in "TCFM":
    torch.manual_seed(0)
    m = M.build(arm, "10M")
    opt = torch.optim.AdamW(m.parameters(), lr=2e-3, weight_decay=0.01)
    def step():
        loss = m.loss(b); opt.zero_grad(set_to_none=True); loss.backward()
        torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0); opt.step()
    step(); step()                                  # warm up
    with profile(activities=[ProfilerActivity.CPU]) as p:
        step()
    ev = p.key_averages()
    calls = sum(e.count for e in ev if e.key.startswith("aten::"))
    t0 = time.time(); [step() for _ in range(5)]; cpu = (time.time() - t0) / 5
    rows[arm] = (calls, cpu)
base = rows["C"][0]
print(f"{'arm':4} {'aten calls/step':>16} {'vs C':>6} {'laptop cpu s/step':>18} {'card s/step':>12} {'card vs C':>10}")
for arm, (calls, cpu) in rows.items():
    print(f"{arm:4} {calls:16d} {calls/base:6.2f} {cpu:18.3f} {card[arm]:12.5f} {card[arm]/card['C']:10.2f}")
