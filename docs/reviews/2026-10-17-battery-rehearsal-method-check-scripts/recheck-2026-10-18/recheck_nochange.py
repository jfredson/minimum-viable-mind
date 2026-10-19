#!/usr/bin/env python3
"""Re-check, 2026-10-18: did the fix commit 3b22925 change any figure, band, gate
bar, prompt or ruling? Compares the runner before the fix (5ead4a0, the branch
with the first check merged) and after, as parsed source: every module-level
constant, and every function that builds a prompt, draws a sample, scores a cell
or calls a reading. Then lists which files the fix touched and every number the
fix removed from or added to the method file. Reads git only; calls nothing.

    python3 docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recheck-2026-10-18/recheck_nochange.py
"""
import ast
import re
import subprocess

OLD, NEW = "5ead4a0", "3b22925"
RUN = "docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py"
METHOD = "docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md"
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout

def parse(rev):
    t = ast.parse(git("show", f"{rev}:{RUN}"))
    consts, funcs = {}, {}
    for n in t.body:
        if isinstance(n, ast.Assign):
            for tg in n.targets:
                for name in ([tg] if isinstance(tg, ast.Name) else getattr(tg, "elts", [])):
                    if isinstance(name, ast.Name) and name.id.isupper():
                        consts[name.id] = ast.unparse(n.value)
        if isinstance(n, ast.FunctionDef):
            funcs[n.name] = ast.unparse(n)
    return consts, funcs

oc, of = parse(OLD)
nc, nf = parse(NEW)
print(f"## module-level constants, {OLD} -> {NEW}")
for k in sorted(set(oc) | set(nc)):
    if oc.get(k) != nc.get(k):
        print(f"  CHANGED {k}: {oc.get(k, '(absent)')[:70]}  ->  {nc.get(k, '(absent)')[:70]}")
same = [k for k in sorted(oc) if oc.get(k) == nc.get(k)]
print(f"  unchanged ({len(same)}): {', '.join(same)}")
print("\n## functions that build prompts, draw samples, score cells or call readings")
for f in ("task_text", "arm_B", "arm_B2", "arm_S", "arm_S2", "other_arm_turns", "own", "load_record", "plan_from",
          "bootstrap_diff", "call_reading", "family", "judge_for", "tokens", "est_call"):
    print(f"  {f:16} {'unchanged' if of.get(f) == nf.get(f) else 'CHANGED'}")
print("\n## the reading code inside real_run: lines naming a band, a gate bar or the rule, before and after")
def rule_lines(rev):
    src = git("show", f"{rev}:{RUN}")
    body = src.split("def real_run", 1)[1]
    return sorted(set(l.strip() for l in body.splitlines()
                      if re.search(r"BAND_|GATE_[A-Z]|call_reading\(|bootstrap_diff\(|readings\.append|reading = ", l)))
ol, nl = rule_lines(OLD), rule_lines(NEW)
print(f"  {len(ol)} lines before, {len(nl)} after; identical sets: {ol == nl}")
for l in sorted(set(ol) ^ set(nl)):
    print(f"    differs: {l[:120]}")
print("\n## files the fix commit touched")
print("  " + git("diff", "--name-only", OLD, NEW).replace("\n", "\n  ").rstrip())
for f in ("docs/filtered-battery-proposal-2026-10-07.md", "docs/filtered-battery-2026-10-07/liveness_rubric_v1.2_entry2.md",
          "experiments/03-retained-independence/src/batteries/liveness_rubric.md"):
    print(f"  {f}: {'unchanged' if not git('diff', OLD, NEW, '--', f) else 'CHANGED'}")
print("\n## numbers removed from and added to the method file by the fix")
d = git("diff", "-U0", OLD, NEW, "--", METHOD)
num = r"\$?\d[\d,]*(?:\.\d+)?"
rem = [x for l in d.splitlines() if l.startswith("-") and not l.startswith("---") for x in re.findall(num, l)]
add = [x for l in d.splitlines() if l.startswith("+") and not l.startswith("+++") for x in re.findall(num, l)]
print(f"  removed: {' '.join(rem)}")
print(f"  added:   {' '.join(add)}")
