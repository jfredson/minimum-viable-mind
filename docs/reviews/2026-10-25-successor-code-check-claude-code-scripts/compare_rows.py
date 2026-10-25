"""Compare every value in the checking session's re-measured rows with the committed rows."""
import json, sys, math
import numpy as np
mine, theirs = sys.argv[1], sys.argv[2]
SKIP = ("seconds", "time", "versions", "ckpt", "path", "out", "host", "started", "finished", "elapsed")
def walk(a, b, p, diffs, n):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if any(s in k.lower() for s in SKIP): continue
            if k not in a or k not in b: diffs.append((p + "/" + k, "missing on one side")); continue
            walk(a[k], b[k], p + "/" + k, diffs, n)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): diffs.append((p, f"length {len(a)} vs {len(b)}")); return
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f"{p}[{i}]", diffs, n)
    else:
        n[0] += 1
        if isinstance(a, float) or isinstance(b, float):
            if a is None or b is None or not (a == b or (math.isnan(a) and math.isnan(b))):
                diffs.append((p, f"{a} vs {b}"))
        elif a != b: diffs.append((p, f"{a!r} vs {b!r}"))
tot = 0
for arm in "TCM":
    d, n = [], [0]
    walk(json.load(open(f"{mine}/row_{arm}_seed0.json")), json.load(open(f"{theirs}/row_{arm}_seed0.json")), "", d, n)
    za, zb = np.load(f"{mine}/reads_{arm}_seed0.npz"), np.load(f"{theirs}/reads_{arm}_seed0.npz")
    rd = [k for k in za.files if not np.array_equal(za[k], zb[k])]
    print(f"arm {arm}: {n[0]} values compared, {len(d)} different; reads: {len(za.files)} arrays, {len(rd)} different")
    for x in d[:15]: print("   ", x)
    tot += len(d) + len(rd)
print("IDENTICAL" if tot == 0 else f"{tot} differences")
