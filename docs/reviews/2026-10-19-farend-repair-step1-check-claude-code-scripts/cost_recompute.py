"""Item 7: the step-1 cost, recomputed from measured reply lengths instead of the runner's single average.

The runner's estimate gives every reply the mean length of claude-sonnet-5's probe replies in
experiment D's main record (no synthetic prompt). This uses what was actually measured for the
always-agree reference:
  - ladder replies, per turn: experiment D's construct-gate records for the always-agree reference
    (artifacts/stage3/ladder/gate_always_agree, preference arm, tool framing, 10 bank A items);
  - step-1 replies: the first run's always-agree reference replies to arm S's message, per item
    (artifacts/stage3/battery_rehearsal/entry1/reference_always_agree, 59 items);
  - judge calls: the first run's recorded judge call sizes for those replies, per item (29 bank B).
It keeps the runner's own prices, its characters-to-tokens rule (characters / 4, rounded up) and its
Gemini thinking allowance for the high end. The always-agree ladder replies on bank B are not
measured anywhere; they are given bank A's per-turn lengths, and, as a second version, twice those.
Reads only. Usage, from the worktree root: python cost_recompute.py
"""
import importlib.util
import json
import statistics as st
import sys
from pathlib import Path

RUNNER = Path.cwd() / "docs/filtered-battery-2026-10-07/run_farend_repair_step1.py"
sys.argv = [str(RUNNER)]
spec = importlib.util.spec_from_file_location("step1", RUNNER)
S = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(S)
R = S.R
m = R.GATE_SUBSTRATE
ART = R.ART
refs = R.plan_from(R.load_record())["ref_items"]
sysm = S.system_prompt()

gate = [json.loads(p.read_text()) for p in sorted((ART / "ladder/gate_always_agree").glob(f"{m}__*__preference__tool.json"))]
per_turn = [st.mean(len(g["turns"][t]) for g in gate) for t in range(5)]
print(f"D's construct-gate always-agree ladders on {m}: {len(gate)} items; mean reply characters by turn: "
      + ", ".join(f"{x:.0f}" for x in per_turn))
cells = R.load_record()
vis = sum(c["chars"][4] for c in cells if c["model"] == m) / sum(1 for c in cells if c["model"] == m)
print(f"the runner's single assumed reply length (mean probe reply in D's main record): {vis:.0f} characters")

first = {p.name.split("__")[1]: json.loads(p.read_text()) for p in (ART / "battery_rehearsal/entry1/reference_always_agree").glob("*.json")}
jrec = {p.name.split("__")[1]: json.loads(p.read_text()) for p in (ART / "battery_rehearsal/entry1/judge/reference_always_agree").glob("*.json")}
print(f"the first run's reference replies: {len(first)}; mean {st.mean(len(r['turns'][0]) for r in first.values()):.0f} characters; "
      f"judge records {len(jrec)}")


def cost(b_scale, thinking):
    lad = s1 = jd = 0.0
    for iid in refs:
        item = R.ITEMS_DICT[iid]
        scale = 1.0 if iid in R.A_ITEMS else b_scale
        reps = [per_turn[t] * scale for t in range(5)]
        ctx = len(sysm)
        for turn, rep in zip([R.task_text(iid), *item["preference_rungs"], R.PROBE_TURN], reps):
            ctx += len(turn)
            lad += R.est_call(m, ctx, R.tokens(int(rep)))
            ctx += int(rep)
        msg = S.step1_message(iid, ["x" * int(r) for r in reps[1:4]])
        s1 += R.est_call(m, len(sysm) + len(msg), R.tokens(len(first[iid]["turns"][0])))
        if iid in R.B_ITEMS:
            jm = R.judge_for(m)
            for c in jrec[iid]["calls"]:
                jd += R.est_call(jm, c["in"], R.tokens(c["out"]) + (R.JUDGE_THINKING_ALLOWANCE.get(jm, 0) if thinking else 0))
    return lad, s1, jd


for label, bs in (("bank B ladder replies as long as bank A's", 1.0), ("bank B ladder replies twice bank A's", 2.0)):
    for thinking in (False, True):
        a, b, c = cost(bs, thinking)
        print(f"  {label}, {'with' if thinking else 'without'} the judge's thinking allowance: "
              f"ladders ${a:.2f}, step-1 messages ${b:.2f}, judge ${c:.2f}; total ${a + b + c:.2f}")
est = S.estimate(refs)
print("the runner's own estimate: " + "; ".join(f"{k} ${sum(v):.2f} (ladders ${v[0]:.2f}, step-1 ${v[1]:.2f}, judge ${v[2]:.2f})" for k, v in est.items()))
print(f"calls: {5 * len(refs)} + {len(refs)} + {sum(i in R.B_ITEMS for i in refs)} = {6 * len(refs) + sum(i in R.B_ITEMS for i in refs)}")
