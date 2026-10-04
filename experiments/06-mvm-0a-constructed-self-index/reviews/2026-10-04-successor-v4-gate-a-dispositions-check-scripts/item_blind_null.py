"""ARGUED point under RT-237, put to numbers. What candidate count would a
model reach that has lost the item binding but kept the rest (it answers the
successor of a value seen in context, ignoring which item the action names)?
Computed exactly as an expectation on the 3,000 gate episodes (1,500
development pairs, generator seed 99), with three item-blind policies. Reads
tokens only; no model is run. $0."""
import os, sys
import numpy as np
SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../rehearsal-successor-measure/src"))
sys.path.insert(0, SRC)
import grammar as G  # noqa: E402

eps = G.episodes_from_pairs(G.make_pairs(1500, seed=99, pool="dev"))
ACT, SELF = G.VOCAB["<act>"], G.VOCAB["<self>"]
slot = {G.VOCAB[f"v{i}"]: i for i in range(8)}
pol = {"uniform over the eight value words": 0.0,
       "successor of one of the eight assignments in context, uniformly": 0.0,
       "successor of one of the four values on the OTHER item": 0.0}
for e in eps:
    t = e["tokens"]
    assigns = [(t[1 + 5 * u + 2], slot[int(t[1 + 5 * u + 3])]) for u in range(8)]
    p = [q for q in range(len(t)) if t[q] == ACT and t[q + 2] == SELF][0]
    item = t[p + 3]
    cand = {(v + 1) % 8 for it, v in assigns if it == item}
    pol["uniform over the eight value words"] += len(cand) / 8
    pol["successor of one of the eight assignments in context, uniformly"] += \
        np.mean([((v + 1) % 8) in cand for _, v in assigns])
    pol["successor of one of the four values on the OTHER item"] += \
        np.mean([((v + 1) % 8) in cand for it, v in assigns if it != item])
print("expected own-directed candidate count of 3,000 under item-blind policies (line 1,546):")
for k, v in pol.items():
    print(f"  {v:7.1f}  {k}")
