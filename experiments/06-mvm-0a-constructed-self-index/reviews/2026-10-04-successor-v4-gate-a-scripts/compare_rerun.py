"""Gate A tier 1: compare a fresh run of the controls re-run's committed code
(experiments/rehearsal-successor-measure/src/rerun_controls.py, run unchanged
from a copy whose output folder points elsewhere, so nothing committed is
overwritten) with the committed outputs, file by file and value by value.
The only field allowed to differ is the run's own running time.

Usage, from the root of the checkout:
    .venv/bin/python <this file> <folder the fresh run wrote>
"""
import json
import os
import sys

COMMITTED = "experiments/rehearsal-successor-measure/out-controls-rerun"
FRESH = sys.argv[1]


def walk(a, b, path, diffs, n):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k == "seconds":
                continue
            if k not in a or k not in b:
                diffs.append(f"{path}/{k}: present in one file only")
                continue
            walk(a[k], b[k], f"{path}/{k}", diffs, n)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append(f"{path}: lengths {len(a)} and {len(b)}")
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", diffs, n)
    else:
        n[0] += 1
        if a != b:
            diffs.append(f"{path}: committed {a!r}, fresh {b!r}")


total_files = total_values = 0
all_diffs = []
for f in sorted(os.listdir(COMMITTED)):
    if not f.endswith(".json"):
        continue
    a = json.load(open(os.path.join(COMMITTED, f)))
    b = json.load(open(os.path.join(FRESH, f)))
    n, diffs = [0], []
    walk(a, b, f, diffs, n)
    total_files += 1
    total_values += n[0]
    all_diffs += diffs
    print(f"{f:<24} values compared {n[0]:>6}; differ {len(diffs)}")
same_table = open(os.path.join(COMMITTED, "table.md")).read() == open(os.path.join(FRESH, "table.md")).read()
print(f"table.md identical: {same_table}")
print(f"TOTAL: {total_files} JSON files, {total_values} values, {len(all_diffs)} differ")
for d in all_diffs[:20]:
    print("  ", d)
s = json.load(open(os.path.join(FRESH, "summary.json")))
print("fresh run: separation field", {k: round(v["C_minus_T"], 4) for k, v in s["separation"].items()},
      "| device", s["device"], "| torch", s["torch"], "| seconds", round(s["seconds"]))
