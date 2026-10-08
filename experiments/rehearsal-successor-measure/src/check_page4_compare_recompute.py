"""Independent check of the page 4 re-run (pull request 121), step 3: the
recomputed 1,800 run against the committed one, value for value.

UNREGISTERED check code. NOT A RESULT. Method: docs/2026-10-07-page4-rerun-check-method.md.
Skips only run times, file paths and library lists. Written here; does not use
page4_compare.py.
"""
from __future__ import annotations

import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REH = os.path.abspath(os.path.join(HERE, ".."))
COMMITTED = os.path.join(REH, "out-page4-rerun-1800")
MINE = os.path.join(REH, "out-page4-check", "recompute-1800")
SKIP = {"seconds", "checkpoint", "versions", "torch"}


def walk(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k in SKIP:
                continue
            if k not in a or k not in b:
                out.append((f"{path}/{k}", "missing on one side"))
            else:
                walk(a[k], b[k], f"{path}/{k}", out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((path, f"lengths {len(a)} and {len(b)}"))
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", out)
    else:
        out.append((path, None if a == b else f"{a!r} vs {b!r}"))


def main():
    values = arrays = 0
    diffs = []
    for sub in ("models-1800", "solver-1800"):
        cdir, mdir = os.path.join(COMMITTED, sub), os.path.join(MINE, sub)
        names = sorted(f for f in os.listdir(cdir) if f.endswith((".json", ".npz", ".md")))
        mine_names = sorted(f for f in os.listdir(mdir) if f.endswith((".json", ".npz", ".md")))
        if names != mine_names:
            diffs.append((sub, f"file lists differ: {sorted(set(names) ^ set(mine_names))}"))
        for f in names:
            if f not in mine_names:
                continue
            p, q = os.path.join(cdir, f), os.path.join(mdir, f)
            if f.endswith(".json"):
                out = []
                walk(json.load(open(p)), json.load(open(q)), f"{sub}/{f}", out)
                values += len(out)
                diffs += [(x, d) for x, d in out if d]
            elif f.endswith(".npz"):
                za, zb = np.load(p), np.load(q)
                for k in sorted(set(za.files) | set(zb.files)):
                    arrays += 1
                    if not (k in za.files and k in zb.files and np.array_equal(za[k], zb[k])):
                        diffs.append((f"{sub}/{f}:{k}", "array differs"))
            else:
                values += 1
                if open(p).read() != open(q).read():
                    diffs.append((f"{sub}/{f}", "text differs"))
    # the solver's log lines, without the output-path line
    def solver_lines(path):
        return [l for l in open(path) if l.startswith(("channel_", "stop", "solver")) and "output" not in l]
    a, b = solver_lines(os.path.join(COMMITTED, "log_solver_1800.txt")), solver_lines(os.path.join(MINE, "log_solver_1800.txt"))
    values += 1
    if a != b:
        diffs.append(("log_solver_1800.txt", "solver log lines differ"))
    print(f"{values} values and {arrays} arrays compared; {len(diffs)} differ")
    for d in diffs[:60]:
        print("  DIFFERS", d)
    json.dump(dict(values=values, arrays=arrays, differ=len(diffs), differences=diffs),
              open(os.path.join(REH, "out-page4-check", "recompute_comparison.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
