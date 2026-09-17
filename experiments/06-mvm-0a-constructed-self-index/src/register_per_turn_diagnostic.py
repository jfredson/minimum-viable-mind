"""Descriptive diagnostic, no pre-stated bin attached.

The primary probe read the FINAL register state, which turns out to be
constant across episodes. But the register is not constant at every turn:
it varies for the first three writes of a forward pass and collapses
thereafter. So "empty" is ambiguous between two very different stories:

  (a) the register never encoded own-agent identity at all; or
  (b) it encoded identity early and the writer destroyed it.

This probes every turn of the final forward pass for the same four-agent
target with the same imported probe and null. Added AFTER seeing the
primary result, carries NO pre-stated reading, and is reported as
description. It exists because the difference between (a) and (b) is
decision-relevant and the primary probe cannot separate them.
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
from blind_arm import probe

CKPT = ('/Users/john/Code/minimum-viable-mind/experiments/'
        '06-mvm-0a-constructed-self-index/artifacts/'
        'pilot_a1_30m_seed0/pilot_a1_30m_seed0.pt')

ck = torch.load(CKPT, map_location='cpu', weights_only=True)
model = MVM0aModel(Config(**ck['cfg'])).eval()
model.load_state_dict(ck['state'])

writes = []
orig_write = model._write


def patched_write(reg_state, seg_h, rows, _o=orig_write):
    new = _o(reg_state, seg_h, rows)
    writes.append(new.detach())
    return new


eps = C.generate_balanced(400, NC.REF_SEED, forced_revision_frac=0.25)
with torch.no_grad():
    eps, act = enact_batched(model, list(eps), 'cpu', random.Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), 'cpu')
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch['input_ids'].shape[1] - act.shape[1]))
    model._write = patched_write          # capture ONLY the graded pass
    model.forward(batch, act_inject=a)
    model._write = orig_write

y = [e.own_slot for e in eps]
print(f"writes in the graded forward pass: {len(writes)}")
print(f"episodes: {len(y)}   chance: 0.25   "
      f"majority-class rate: {max(np.bincount(y)) / len(y):.4f}")
print()
print("turn | across-ep sd | probe acc | null mean | null sd | margin")
for i, w in enumerate(writes):
    X = w.reshape(w.shape[0], -1).numpy()
    sd = X.std(0).mean()
    if sd < 1e-5:
        print(f" {i:3d} | {sd:.3e} | (degenerate: register constant "
              f"across episodes, probe cannot be informative)")
        continue
    p = probe(X, y, seed=100 + i)
    m = p['margin_sd']
    print(f" {i:3d} | {sd:.3e} | {p['accuracy']:.4f}    | "
          f"{p['null_mean']:.4f}    | {p['null_sd']:.4f}  | "
          f"{m if m is not None else 'undef'} sd")

print()
print("A margin near zero at EVERY turn, including the pre-collapse turns,")
print("means story (a): the register never encoded own-agent identity.")
print("A large margin early that vanishes later means story (b).")
