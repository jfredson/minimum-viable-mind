"""List which fields of the whole-pipeline test's rows differ between two runs
(the end-to-end test on the final code, method
docs/2026-10-08-end-to-end-final-code-method.md). Timing fields are reported
apart. Also compares the training logs' per-step loss records (ckpt_*.jsonl).

    python tests/e2e_compare_rows.py OLD_SIZE_DIR NEW_SIZE_DIR
"""
import json
import os
import sys

old_d, new_d = sys.argv[1], sys.argv[2]


def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from flat(v, f"{p}.{k}" if p else k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from flat(v, f"{p}[{i}]")
    else:
        yield p, x


for arm in "TCMF":
    j = f"ckpt_{arm}.jsonl"
    if os.path.exists(os.path.join(old_d, j)) and os.path.exists(os.path.join(new_d, j)):
        a = [json.loads(l) for l in open(os.path.join(old_d, j)) if l.strip()]
        b = [json.loads(l) for l in open(os.path.join(new_d, j)) if l.strip()]
        da = dict(p for r in a for p in flat(r))
        same = [k for k in da if "time" not in k and "sec" not in k]
        db = dict(p for r in b for p in flat(r))
        diff = [k for k in same if da.get(k) != db.get(k)]
        print(f"arm {arm} training record: {len(a)} vs {len(b)} lines; non-timing values differing: {len(diff)} {diff[:6]}")
    f = f"row_{arm}_seed0.json"
    a = dict(flat(json.load(open(os.path.join(old_d, "measure", f)))))
    b = dict(flat(json.load(open(os.path.join(new_d, "measure", f)))))
    keys = sorted(set(a) | set(b))
    diff = [k for k in keys if a.get(k) != b.get(k)]
    timing = [k for k in diff if "time" in k or "sec" in k or "elapsed" in k]
    other = [k for k in diff if k not in timing]
    print(f"arm {arm} row: {len(keys)} values; differ {len(diff)} (timing {len(timing)}: {timing}); other: {other[:20]}")
