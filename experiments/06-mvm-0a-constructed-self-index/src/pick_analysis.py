"""Where do a non-binder's T_si picks land? [thread 3 follow-up]

Regenerates the eval episodes (same seed) and classifies each T_si
pick against the episode's structure: correct turn, another turn by
the same agent, the model's own turns, the last turn, etc.
"""
import json
import random
import sys
from collections import Counter
from pathlib import Path

import curriculum as C

OUT = Path(__file__).resolve().parents[1] / "lesion-results"
run = sys.argv[1] if len(sys.argv) > 1 else "pilot_a1_30m_seed1"
rows = [json.loads(l) for l in
        (OUT / f"items_{run}.jsonl").read_text().splitlines()]
meta, rows = rows[0]["meta"], rows[1:]

eps = C.generate_balanced(meta["n_episodes"], meta["seed"],
                          forced_revision_frac=0.25)
# reproduce the eval-time enactment (data-side rng, same seed rule)
rng = random.Random(meta["seed"] + 1)
for e in eps:
    C.enact_own_turns(e, rng)

cats = Counter()
for r in rows:
    if r["battery"] != "T_si" or r["ok"]:
        continue
    e = eps[r["ep"]]
    t = e.turns[r["turn_idx"]]
    pick = r["pick"]
    tags = []
    if any(x.value == pick and x.agent == t.agent and x is not t
           for x in e.turns):
        tags.append("same_agent_other_turn")
    if any(x.value == pick for x in e.own_turns()):
        tags.append("own_turn_value")
    if e.turns[-1].value == pick:
        tags.append("last_turn_value")
    if any(x.value == pick and x.item == t.item and x is not t
           for x in e.turns):
        tags.append("same_item_other_turn")
    if not any(x.value == pick for x in e.turns):
        tags.append("value_not_in_episode")
    cats[tuple(sorted(tags)) or ("other_agent_value",)] += 1

n_err = sum(cats.values())
print(f"{run}: {n_err} T_si errors of "
      f"{sum(1 for r in rows if r['battery'] == 'T_si')}")
for k, v in cats.most_common():
    print(f"  {v:4d} ({v / n_err:.0%})  {' + '.join(k)}")
