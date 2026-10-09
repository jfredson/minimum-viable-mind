"""Compare the re-run outputs with the committed outputs, every value, every file."""
import json, os, sys
import numpy as np

S = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(S, "committed/experiments/08-successor-degree/out-decoy-w18")
B = os.path.join(S, "rerun/experiments/08-successor-degree/out-decoy-w18")
SKIP = {"seconds", "checkpoint", "reads_source", "elapsed", "time", "when", "started", "finished", "wall_seconds"}


def walk(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in set(a) | set(b):
            if k in SKIP:
                continue
            if k not in a or k not in b:
                out.append((path + "/" + k, "missing on one side"))
                continue
            walk(a[k], b[k], path + "/" + k, out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((path, f"length {len(a)} vs {len(b)}"))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", out)
    else:
        out.append((path, f"{a!r} vs {b!r}")) if a != b else None
    return out


variants = sys.argv[1:] or ["V1", "V2", "V3", "V4", "V5"]
total_vals = 0
for v in variants:
    for name in sorted(os.listdir(os.path.join(A, v))):
        pa, pb = os.path.join(A, v, name), os.path.join(B, v, name)
        if name.endswith(".json"):
            ja, jb = json.load(open(pa)), json.load(open(pb))
            diffs = walk(ja, jb, "", [])
            n = len(json.dumps(ja))
            print(f"{v}/{name}: {'EQUAL' if not diffs else str(len(diffs)) + ' differences'}")
            for d in diffs[:8]:
                print("   ", d)
        elif name.endswith(".npz"):
            za, zb = np.load(pa), np.load(pb)
            eq = set(za.files) == set(zb.files) and all(np.array_equal(za[k], zb[k]) for k in za.files)
            print(f"{v}/{name}: {'bit-identical arrays' if eq else 'ARRAYS DIFFER'}")
        else:
            same = open(pa).read() == open(pb).read()
            print(f"{v}/{name}: {'identical text' if same else 'TEXT DIFFERS'}")
