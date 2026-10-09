"""Checker's comparison for pull request 151 (the ruled code changes and the page 4 re-run).

Written by the checker; does not import the session's comparison script.
Run from `experiments/` of a checkout of the branch:

    python compare_checker.py headline              # the committed outputs only
    python compare_checker.py mine MY_B MY_A        # also the checker's own re-runs

headline: per model, the iteration-limit warnings in the logs (old 1,800
record, pass A, pass B), pass A's stops by kind, pass B's total and its
largest iteration counts, and the figures version 5 quotes, old against pass B.
mine: every leaf of the checker's pass B rows against the committed pass B
rows, and of the checker's pass A rows against the checked 1,800 record and
the committed pass A rows; read arrays likewise.
"""
import json
import os
import re
import sys

import numpy as np

O = "08-successor-degree/out-ruled-code-changes"
OLD = "rehearsal-successor-measure/out-page4-rerun-1800/models-1800"
A, B = f"{O}/passA-limit3000", f"{O}/passB-limit10000"
SKIP = {"seconds", "checkpoint", "versions", "page4", "torch", "reads_source"}


def load(d, f):
    with open(os.path.join(d, f)) as fh:
        return json.load(fh)


def warns(d, arm, s):
    p = os.path.join(d, f"log_{arm}_seed{s}.txt")
    return len(re.findall("failed to converge", open(p).read())) if os.path.exists(p) else None


def reading(r):
    p = r.get("primary")
    return None if not p else (p.get("reading") or {}).get("degree")


def best_piece(fits):
    return max(max(v["piece"].values()) for v in fits.values())


def quoted(r):
    p = r.get("primary") or {}
    s = r["nomination"]["primary"]["site_set"]
    ts = (p.get("true_slot") or {}).get("reading", {}).get("degree")
    c2 = r["control2"]
    return dict(status=r["nomination_status"],
                site=None if not s else (s["layers"], s["positions"], s["rank"], s["piece_correct"]),
                reading=reading(r), true_slot=ts, best_piece=best_piece(r["fits"]),
                c1=(p.get("controls", {}).get("1") or {}).get("holds"),
                c4=(p.get("controls", {}).get("4") or {}).get("holds"),
                c7=(p.get("controls", {}).get("7") or {}).get("holds"),
                c2=c2["status"], c2_moved=c2.get("own_directed_moved"))


def leaves(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out, only = [], []
        for k in sorted(set(a) | set(b)):
            if k in SKIP:
                continue
            if k not in a or k not in b:
                only.append(f"{path}/{k}")
                continue
            o, n = leaves(a[k], b[k], f"{path}/{k}")
            out += o
            only += n
        return out, only
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        out, only = [], []
        for i, (x, y) in enumerate(zip(a, b)):
            o, n = leaves(x, y, f"{path}[{i}]")
            out += o
            only += n
        return out, only
    return [(path, a == b, a, b)], []


def headline():
    tot = dict(old=0, A=0, B=0)
    for arm in "TCMF":
        for s in range(3):
            f = f"row_{arm}_seed{s}.json"
            ra, rb, ro = load(A, f), load(B, f), load(OLD, f)
            w = dict(old=warns(OLD, arm, s), A=warns(A, arm, s), B=warns(B, arm, s))
            for k in tot:
                tot[k] += w[k]
            ka = {k: v["stopped_at_limit"] for k, v in ra["fits_stopped_at_iteration_limit"]["by_kind"].items()
                  if v["stopped_at_limit"]}
            kb = rb["fits_stopped_at_iteration_limit"]
            most = {k: v["most_iterations"] for k, v in kb["by_kind"].items()}
            print(f"{arm}/{s}: warnings old {w['old']}, A {w['A']}, B {w['B']}; A stops by kind {ka}; "
                  f"B stops {kb['total']}, limit {kb['limit']}; B most iterations: own read "
                  f"{most.get('the read (own)')}, null {most.get('the null (shuffled labels)')}")
            qo, qb = quoted(ro), quoted(rb)
            diff = {k: (qo[k], qb[k]) for k in qo if qo[k] != qb[k]}
            print(f"     old {qo}\n     B   {qb}\n     quoted figures that differ: {diff or 'none'}")
    print("totals of warnings:", tot)


def mine(my_b, my_a):
    for label, mine_dir, ref_dirs in (("my pass B", my_b, (("committed pass B", B),)),
                                      ("my pass A", my_a, (("checked 1,800 record", OLD), ("committed pass A", A)))):
        for f in sorted(x for x in os.listdir(mine_dir) if x.startswith("row_")):
            arm, s = f[4], int(f[-6])
            for rlabel, rd in ref_dirs:
                res, only = leaves(load(mine_dir, f), load(rd, f))
                bad = [r for r in res if not r[1]]
                z1 = np.load(os.path.join(mine_dir, f.replace("row_", "reads_").replace(".json", ".npz")))
                z2 = np.load(os.path.join(rd, f.replace("row_", "reads_").replace(".json", ".npz")))
                arr = [k for k in sorted(set(z1.files) | set(z2.files))
                       if not (k in z1.files and k in z2.files and np.array_equal(z1[k], z2[k]))]
                print(f"{label} {f} vs {rlabel}: {len(res)} values compared, {len(bad)} differ"
                      f"{' ' + str(bad[:6]) if bad else ''}; read arrays differing: {arr or 'none'}; "
                      f"warnings mine {warns(mine_dir, arm, s)} vs {warns(rd, arm, s)}; "
                      f"fields in one only: {len(only)}")


if __name__ == "__main__":
    if sys.argv[1] == "headline":
        headline()
    else:
        mine(sys.argv[2], sys.argv[3])
