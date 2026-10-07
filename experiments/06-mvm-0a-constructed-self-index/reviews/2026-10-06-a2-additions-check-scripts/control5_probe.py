"""Probe of the stricter control 5 self-test (grammar.py). Uses grammar.py's
generator (the thing under test) but re-implements the table comparison."""
import os, sys, copy
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..", "08-successor-degree", "src")))
import grammar as G

def table(c):  # my own: which marker holds which value on which item
    return frozenset((G.MARKERS[c["markers"][a]], G.ITEMS[c["items"][j]], int(c["values"][a][j]))
                     for a in range(G.N_AGENTS) for j in range(G.N_ITEMS_PER_EPISODE))

fresh = [p["content"] for p in G.eval_pairs("fresh")]
relaxed = [p["content"] for p in G.eval_pairs("relaxed")]
held = {table(c) for c in fresh + relaxed}
print(f"fresh and relaxed tables: {len(held)} distinct of {len(fresh)+len(relaxed)}")

# 1. planted: same table, different turn order, action order, named agent and agent indices
c = copy.deepcopy(fresh[0])
perm = [2, 0, 3, 1]
c2 = dict(c, markers=[c["markers"][i] for i in perm], values=np.asarray(c["values"])[perm],
          order=list(reversed(c["order"])), action_order=list(reversed(c["action_order"])),
          named=(c["named"] + 1) % 4)
print("planted: same table:", table(c2) == table(c), "| same whole content:", G.fingerprint(c2) == G.fingerprint(c),
      "-> the stricter test catches it, the whole-content test does not" if table(c2) == table(c) and G.fingerprint(c2) != G.fingerprint(c) else "-> UNEXPECTED")

# 2. relaxed tables cannot occur in training at all: one item has two agents on the same value
dup = sum(any(len(set(np.asarray(c["values"])[:, j])) < G.N_AGENTS for j in range(2)) for c in relaxed)
print(f"relaxed tables with a shared value on an item: {dup} of {len(relaxed)}; training draws values without repeats, so these can never match")

# 3. could the 200-step sample catch anything? same sample with NO exclusion at all
def sample(excluded, steps=200, seed=0):
    st = G.TrainingStream(run_seed=seed, excluded=excluded)
    out = set()
    for s in range(1, steps + 1):
        for p in st.pairs_for_step(s, 48):
            out.add(table(p["content"]))
    return out
noex = sample(set())
print(f"200 steps, exclusion switched OFF: {len(noex)} training tables, {len(noex & held)} shared with fresh/relaxed")
for sd in (1, 2):
    print(f"200 steps of run seed {sd} (the self-test samples seed 0 only): {len(sample(set(), seed=sd) & held)} shared, exclusion off")

# 4. size of the table space, and the expected chance overlaps
from math import perm as P
space = P(12, 4) * P(5, 2) * P(8, 4) ** 2 // 24 // 2   # agent labels and item order do not matter in a table
print(f"distinct possible tables (fresh pool, no shared values): about {space:.3g}; "
      f"expected chance matches of 800 fresh tables in 9,600 sampled: {800*9600/space:.2g}")

# 4b. a full registered run: 108,919 steps of 96 episodes (48 contents) per seed
# (train_successor.py's default token budget); arms share a seed's stream
per_run = 108_919 * 48
lam = 800 * per_run / space
import math
print(f"one full run's stream: {per_run:,} contents; expected chance matches with the 800 fresh tables {lam:.2f} "
      f"(chance of at least one {1-math.exp(-lam):.0%}); over the three seeds' streams {3*lam:.2f} "
      f"(chance of at least one {1-math.exp(-3*lam):.0%}). Whole-content exclusion does not block these.")

# 5. the single-triple reading would be unworkable: every (marker, item, value) triple appears in training
trip_train = set().union(*noex)
trip_held = set().union(*held)
print(f"single (marker, item, value) triples: {len(trip_held)} in fresh/relaxed, {len(trip_held & trip_train)} of them in the 200 sampled training steps "
      f"(of {12*5*8} possible); so 'pairing' must mean the whole table, as built")
