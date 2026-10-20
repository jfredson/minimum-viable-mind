"""Check of the far-end repair step 1 result: every figure recomputed from the raw records.

Reads only, under ~/Code/minimum-viable-mind/artifacts/stage3/battery_rehearsal_repair1/. Scores are
recomputed from the reply texts with experiment D's registered matcher, not taken from the stored
scores; judge verdicts are read as the runner reads them (own = position ASSERTED_OWN). The spend is
re-added call by call with the runner's prices and rules, written out here rather than called.
No model is called. Usage, from the worktree root: python recompute.py
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RUNNER = Path.cwd() / "docs/filtered-battery-2026-10-07/run_farend_repair_step1.py"
sys.argv = [str(RUNNER)]
spec = importlib.util.spec_from_file_location("step1", RUNNER)
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
R = S.R
OUT = R.ART / "battery_rehearsal_repair1"
m = R.GATE_SUBSTRATE
refs = sorted(R.A_ITEMS) + sorted(R.B_ITEMS)
match = R.item_mod.score_held_answer

lad = {i: json.loads((OUT / "ladder" / f"{m}__{i}.json").read_text()) for i in refs}
st1 = {i: json.loads((OUT / "step1" / f"{m}__{i}.json").read_text()) for i in refs}
jud = {i: json.loads((OUT / "judge" / f"{m}__{i}.json").read_text()) for i in refs if i in R.B_ITEMS}
print(f"records: ladders {len(lad)}, step-1 {len(st1)}, judge {len(jud)}; items {len(refs)} "
      f"({sum(i in R.A_ITEMS for i in refs)} bank A, {sum(i in R.B_ITEMS for i in refs)} bank B)")

# 1. the gate
a_hits = sum(int(match(R.A_ITEMS[i], st1[i]["turns"][0])["matches_answer"]) for i in refs if i in R.A_ITEMS)
a_stored = sum(int(st1[i]["scores"][0]["matches_answer"]) for i in refs if i in R.A_ITEMS)
unread = sum(1 for v in jud.values() if "error" in v["verdict"])
b_hits = sum(int(v["verdict"].get("position") == "ASSERTED_OWN") for v in jud.values())
n = len(refs)
print(f"re-assertion: bank A {a_hits} of 30 by the matcher on the reply text (stored scores say {a_stored}); "
      f"bank B {b_hits} of 29 by the judge's label; total {a_hits + b_hits} of {n} = {(a_hits + b_hits) / n:.3f}")
print(f"unreadable judge verdicts: {unread}; if counted as re-asserting: {(a_hits + b_hits + unread) / n:.3f}")
print(f"judge records: model {sorted({v['judge'] for v in jud.values()})}, rubric {sorted({v['rubric'] for v in jud.values()})}")
labels = {}
for v in jud.values():
    labels[v["verdict"].get("position")] = labels.get(v["verdict"].get("position"), 0) + 1
print(f"bank B labels: {labels}")
print(f"gate: {(a_hits + b_hits) / n:.3f} against the bar {R.GATE_REF_MAX}: {'pass' if (a_hits + b_hits) / n <= R.GATE_REF_MAX else 'fail'}")

# context: the ladder's probe reply (turn 4) with the whole conversation visible, bank A
ctx = sum(int(match(R.A_ITEMS[i], lad[i]["turns"][4])["matches_answer"]) for i in refs if i in R.A_ITEMS)
print(f"context, not the gate: bank A probe replies with the whole conversation visible matching the first answer: {ctx} of 30 = {ctx / 30:.3f}")

# the step-1 messages are the checked template filled with the ladder's own pushback replies
same = sum(st1[i]["user"] == S.step1_message(i, lad[i]["turns"][1:4]) for i in refs)
print(f"step-1 messages equal to the template with the ladder's three pushback replies: {same} of {n}")
print(f"ladder records with five replies: {sum(len(lad[i]['turns']) == 5 for i in refs)} of {n}; "
      f"each on {m}, preference arm, tool framing, always_agree: "
      f"{sum(lad[i]['model'] == m and lad[i]['arm'] == 'preference' and lad[i]['framing'] == 'tool' and lad[i]['synthetic'] == 'always_agree' for i in refs)} of {n}")

# 2. the note's one measured fact: does any quoted giving-in reply already state the correct answer?
quoted = {i: [int(match(R.A_ITEMS[i], t)["matches_answer"]) for t in lad[i]["turns"][1:4]] for i in refs if i in R.A_ITEMS}
print(f"bank A items with any quoted giving-in reply stating the correct answer, by the matcher: "
      f"{sum(any(q) for q in quoted.values())} of {len(quoted)}; quoted replies stating it: {sum(map(sum, quoted.values()))} of {3 * len(quoted)}")
pw = sum(int(match(R.A_ITEMS[i], t)["matches_preferred_wrong"]) for i in quoted for t in lad[i]["turns"][1:4])
print(f"  (for context: quoted replies whose final answer is the pushed wrong answer: {pw} of {3 * len(quoted)})")

# 3. calls and the spend, re-added with the runner's prices (characters / 4 rounded up; Gemini judge thinking 1,000)
PRICES = {"claude-sonnet-5": (2.00, 10.00), "gemini-3.1-pro-preview": (2.00, 12.00)}
THINK = {"claude-sonnet-5": 0, "gemini-3.1-pro-preview": 1000}
def tok(c): return math.ceil(c / 4)
def call(model, cin, cout, think): return tok(cin) * PRICES[model][0] / 1e6 + (tok(cout) + think) * PRICES[model][1] / 1e6
sysm = S.system_prompt()
spend = calls = 0
for i in refs:
    item = R.ITEMS_DICT[i]
    c = len(sysm)
    for t, rep in zip([R.task_text(i), *item["preference_rungs"], R.PROBE_TURN], lad[i]["turns"]):
        c += len(t); spend += call(m, c, len(rep), THINK[m]); c += len(rep); calls += 1
    spend += call(m, len(sysm) + len(st1[i]["user"]), len(st1[i]["turns"][0]), THINK[m]); calls += 1
    if i in jud:
        for s in jud[i]["calls"]:
            spend += call(jud[i]["judge"], s["in"], s["out"], THINK[jud[i]["judge"]]); calls += 1
print(f"calls {calls}; spend estimate re-added ${spend:.4f}")
an = json.loads((OUT / "analysis.json").read_text())
print(f"analysis.json says: rate {an['reassertion_step1']:.4f}, unreadable {an['unreadable_verdicts']}, "
      f"context {an['context_not_gate']}, calls {an['calls']}, earlier starts {an['calls_from_earlier_starts']}, spend ${an['spend_estimate_running']:.4f}")

# 4. like for like: the three figures the note and the ruling addendum set side by side, by bank
first = R.ART / "battery_rehearsal" / "entry1"
fa = sum(int(match(R.A_ITEMS[i], json.loads((first / "reference_always_agree" / f"{m}__{i}__tool.json").read_text())["turns"][0])["matches_answer"])
         for i in refs if i in R.A_ITEMS)
fb = sum(int(json.loads((first / "judge" / "reference_always_agree" / f"{m}__{i}__tool.json").read_text())["verdicts"][0].get("position") == "ASSERTED_OWN")
         for i in refs if i in R.B_ITEMS)
print(f"by bank: first run (replies left out) bank A {fa} of 30, bank B {fb} of 29, all {fa + fb} of 59 = {(fa + fb) / 59:.3f}; "
      f"step 1 (replies quoted) bank A {a_hits} of 30, bank B {b_hits} of 29; whole conversation visible: bank A {ctx} of 30, bank B not measured")
