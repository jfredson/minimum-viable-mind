"""Is the constant register a property of the model, or a bug in my capture?

If only the final write is constant, my capture is suspect. If every write
is constant across episodes from the first turn on, the writer itself is
producing an episode-independent output and the model is what is constant.
"""
import random
import sys

import numpy as np
import torch

sys.path.insert(0, '/Users/john/Code/minimum-viable-mind/.claude/worktrees/'
                   'gate0-null-calibration/experiments/'
                   '06-mvm-0a-constructed-self-index/src')

import curriculum as C
import encoding as E
import null_calibration as NC
from model import MVM0aModel, Config, to_torch
from train import enact_batched

CKPT = ('/Users/john/Code/minimum-viable-mind/experiments/'
        '06-mvm-0a-constructed-self-index/artifacts/'
        'pilot_a1_30m_seed0/pilot_a1_30m_seed0.pt')

ck = torch.load(CKPT, map_location='cpu', weights_only=True)
model = MVM0aModel(Config(**ck['cfg'])).eval()
model.load_state_dict(ck['state'])

writes, pooled_in = [], []
orig_write = model._write
orig_writer = model.writer


def patched_write(reg_state, seg_h, rows, _o=orig_write):
    w = torch.softmax(seg_h @ model.pool_q, dim=1)
    pooled_in.append((w.unsqueeze(-1) * seg_h).sum(1).detach())
    new = _o(reg_state, seg_h, rows)
    writes.append(new.detach())
    return new


model._write = patched_write
eps = C.generate_balanced(200, NC.REF_SEED, forced_revision_frac=0.25)
with torch.no_grad():
    eps, act = enact_batched(model, list(eps), 'cpu', random.Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), 'cpu')
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch['input_ids'].shape[1] - act.shape[1]))
    model.forward(batch, act_inject=a)
model._write = orig_write

print(f"writes captured: {len(writes)}")
print()
print("per-turn across-episode spread of the register state:")
print(" turn | max sd across episodes | mean sd")
for i, w in enumerate(writes):
    x = w.reshape(w.shape[0], -1).numpy()
    print(f"  {i:3d} | {x.std(0).max():.6e} | {x.std(0).mean():.6e}")

print()
print("per-turn across-episode spread of the WRITER'S INPUT (pooled "
      "top-layer states):")
print(" turn | max sd across episodes | mean sd")
for i, x in enumerate(pooled_in):
    v = x.numpy()
    print(f"  {i:3d} | {v.std(0).max():.6e} | {v.std(0).mean():.6e}")

print()
print("If the writer's INPUT varies across episodes but its OUTPUT does")
print("not, the GRU is collapsing episode-specific content to a constant.")
print("If the input is also constant, the collapse is upstream of it.")
