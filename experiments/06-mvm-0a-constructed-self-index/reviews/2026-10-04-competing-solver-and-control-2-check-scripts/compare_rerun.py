"""Compare a re-run's output folder with the committed one, file by file.

Exact byte comparison for .json, .md and .txt files; array-equal comparison
for .npz files (a zip archive can differ in its bytes while its arrays are the
same). Prints the size of any difference.

    python compare_rerun.py <worktree> <commit> <output folder relative to the worktree>
"""
import io
import os
import subprocess
import sys

import numpy as np

wt, rev, folder = sys.argv[1:4]
listed = subprocess.run(["git", "-C", wt, "ls-tree", "-r", "--name-only", rev, folder],
                        capture_output=True, check=True, text=True).stdout.split()
bad = 0
for path in sorted(listed):
    committed = subprocess.run(["git", "-C", wt, "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
    with open(os.path.join(wt, path), "rb") as f:
        rerun = f.read()
    name = os.path.relpath(path, folder)
    if path.endswith(".npz"):
        a, b = np.load(io.BytesIO(committed)), np.load(io.BytesIO(rerun))
        keys_same = sorted(a.files) == sorted(b.files)
        worst = max(float(np.abs(a[k] - b[k]).max()) for k in a.files) if keys_same else float("nan")
        same = keys_same and all(np.array_equal(a[k], b[k]) for k in a.files)
        print(f"{'SAME ' if same else 'DIFF '} {name}: {len(a.files)} arrays, array-equal {same}, "
              f"largest difference {worst}, bytes identical {committed == rerun}")
    else:
        same = committed == rerun
        extra = ""
        if not same:
            ca, ra = committed.decode().splitlines(), rerun.decode().splitlines()
            diff = [(i, x, y) for i, (x, y) in enumerate(zip(ca, ra)) if x != y]
            extra = f"; {len(diff)} lines differ of {len(ca)} / {len(ra)}; first: {diff[:3]}"
        print(f"{'SAME ' if same else 'DIFF '} {name}: byte-identical {same}{extra}")
    bad += not same
print(f"{len(listed)} files compared, {bad} differ")
