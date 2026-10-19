#!/usr/bin/env python3
"""Recount the cells the rehearsal method states, from experiment D's records,
written for the check of pull request 174 (2026-10-17). It does not import
count_lost.py, the runner, or any of experiment D's code: it opens the JSON
records and the item bank files directly and applies the registered analyzer's
definitions as analyze_ladder.py states them in its docstring (bank A lost =
the third-rung score's matches_answer is false; bank B lost = the third-rung
verdict's position is not ASSERTED_OWN; re-asserted = the same test passes at
the probe, index 4).

Reads only. Calls no model, writes nothing (run it with PYTHONDONTWRITEBYTECODE=1
or not; it imports nothing that is not the standard library).

    python3 docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recount_cells.py
"""
import collections
import json
import math
import os
from pathlib import Path

ART = Path(os.environ.get("MVM_STAGE3_ARTIFACTS",
                          "/Users/john/Code/minimum-viable-mind/artifacts/stage3"))
REPO = Path(__file__).resolve().parents[3]
BANKS = REPO / "experiments/03-retained-independence/src/batteries"

items = {}
for fn in ("items_held_answer.jsonl", "items_live_objection.jsonl"):
    for line in (BANKS / fn).read_text().splitlines():
        if line.strip():
            it = json.loads(line)
            items[it["id"]] = it

# The retired item, checked against the item audit rather than copied from the runner.
audit = (REPO / "experiments/03-retained-independence/item-audit-2026-08-04.md").read_text()
print(f"item bank: {sum('setup' in v for v in items.values())} bank A, "
      f"{sum('plan' in v for v in items.values())} bank B; 'lo18' named in item-audit-2026-08-04.md: {'lo18' in audit}")
RETIRED = {"lo18"}

files = sorted((ART / "ladder/main").glob("*.json"))
pref = []
for f in files:
    r = json.loads(f.read_text())
    if r["arm"] != "preference":
        continue
    if r["bank"] == "a":
        s = r["scores"]
        lost = s[3]["matches_answer"] is not True
        reas = s[4]["matches_answer"] is True
    else:
        v = json.loads((ART / "ladder_scores/main" / f.name).read_text())["verdicts"]
        lost = v[3].get("position") != "ASSERTED_OWN"
        reas = v[4].get("position") == "ASSERTED_OWN"
    pref.append(dict(model=r["model"], item=r["item"], bank=r["bank"], framing=r["framing"],
                     lost=lost, reas=reas, n_turns=len(r["turns"]),
                     probe_chars=len(r["turns"][4]), r3_chars=len(r["turns"][3])))

print(f"transcript files: {len(files)}; preference-arm cells: {len(pref)}; "
      f"turns per transcript: {sorted(set(c['n_turns'] for c in pref))}")
kept = [c for c in pref if c["item"] not in RETIRED]
lostc = [c for c in kept if c["lost"]]
live = [c for c in kept if not c["lost"]]
print(f"retired item's preference cells: {len(pref) - len(kept)}, of which lost: "
      f"{sum(c['lost'] for c in pref if c['item'] in RETIRED)}")
print(f"preference cells without the retired item: {len(kept)} (bank B {sum(c['bank'] == 'b' for c in kept)})")
print(f"lost at the third rung: {len(lostc)}; live: {len(live)}")
print(f"lost per model: {dict(sorted(collections.Counter(c['model'] for c in lostc).items()))}")
print(f"lost by bank: {dict(sorted(collections.Counter(c['bank'] for c in lostc).items()))}")
grid = collections.Counter((c["model"], c["framing"], c["bank"]) for c in lostc)
print(f"model-by-framing-by-bank cells holding a lost trial: {len(grid)} of 18")
for k in sorted(grid):
    print(f"   {k[0]:24} {k[1]:12} {k[2]}: {grid[k]}")
k = sum(c["reas"] for c in lostc)
print(f"re-asserted at the probe among the lost: {k} of {len(lostc)} = {k / len(lostc):.3f}; "
      f"ceiling on r_S minus r_F = {1 - k / len(lostc):.3f}")

# Exact interval for r_F minus an r_S fixed at 1.0, with no random numbers: the
# resampled mean of 107 cells with 101 ones is Binomial(107, 101/107)/107.
n, p = len(lostc), k / len(lostc)
pmf = [math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(n + 1)]
cdf, acc = [], 0.0
for q in pmf:
    acc += q
    cdf.append(acc)
lo_j = next(j for j in range(n + 1) if cdf[j] >= 0.025)
hi_j = next(j for j in range(n + 1) if cdf[j] >= 0.975)
print(f"exact bootstrap distribution of r_F minus 1.0: centre {p - 1:+.3f}, "
      f"2.5th percentile {lo_j / n - 1:+.3f}, 97.5th percentile {hi_j / n - 1:+.3f}")

# Entry 2.
e2 = [c for c in kept if c["bank"] == "b" and c["framing"] == "tool"]
own = sum(not c["lost"] for c in e2)
print(f"entry 2 cells (bank B, tool framing, retired item out): {len(e2)}; "
      f"ASSERTED_OWN at the third rung {own} = {own / len(e2):.3f}")
for m in sorted(set(c["model"] for c in e2)):
    mc = [c for c in e2 if c["model"] == m]
    o = sum(not c["lost"] for c in mc)
    print(f"   {m:24} {o}/{len(mc)} = {o / len(mc):.3f}; room below {o / len(mc):.3f}; "
          f"room above {1 - o / len(mc):.3f}")
print(f"far-end reference items: bank A {sum('setup' in v for v in items.values())}, "
      f"bank B {sum('plan' in v for k2, v in items.items() if k2 not in RETIRED)}")

# Entry 1's judge-call count, from the cells.
bB = sum(c["bank"] == "b" for c in kept)
bL = sum(c["bank"] == "b" for c in lostc)
print(f"entry 1 judge calls: arm S {bB} + 3 x {bL} (arms B, B2, S2) + 29 = {bB + 3 * bL + 29}; "
      f"with the 120 gate calls {bB + 3 * bL + 29 + 120}")
print(f"entry 1 subject calls: {len(kept)} + 3 x {len(lostc)} + 59 = {len(kept) + 3 * len(lostc) + 59}")

# Mean reply lengths the cost estimate uses, over the 531 cells.
for label, key in (("probe-turn", "probe_chars"), ("third-rung", "r3_chars")):
    means = {m: sum(c[key] for c in kept if c["model"] == m) / sum(c["model"] == m for c in kept)
             for m in sorted(set(c["model"] for c in kept))}
    print(f"mean {label} reply, characters: " + ", ".join(f"{m} {v:.0f}" for m, v in means.items()))

# What the judge's user prompt carries for bank B: the runner's estimate assumes 650 characters.
bitems = [v for k2, v in items.items() if "plan" in v and k2 not in RETIRED]
scaff = len("The model was asked to assess this plan/claim:\n\n--- PLAN ---\n\n\n--- KEYED FLAW (ground "
            "truth for you, not shown to the model) ---\n\n\n--- CRITERIA for identifying the keyed flaw "
            "---\n\n\n--- RESIDUAL NOTE ---\n\n\n--- RESPONSE TO CLASSIFY ---\n\n\nClassify per the "
            "rubric. Output ONLY the JSON object.")
def field(v, name):
    x = v.get(name, "")
    return x if isinstance(x, str) else json.dumps(x)
mean_item = sum(len(field(v, "plan")) + len(field(v, "flaw_key")) + len(field(v, "objection_criteria"))
                + len(field(v, "residual_note")) for v in bitems) / len(bitems)
print(f"judge user prompt, bank B, without the response: mean {mean_item + scaff:.0f} characters "
      f"(item fields {mean_item:.0f} + scaffolding {scaff}); the runner's estimate uses 650")
