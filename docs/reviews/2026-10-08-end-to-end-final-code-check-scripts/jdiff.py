import json, sys
def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from flat(v, f"{p}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from flat(v, f"{p}[{i}]")
    else: yield p, x
A, B = sys.argv[1], sys.argv[2]
for size in sys.argv[3:] or ("10M", "30M"):
    for arm in "TCMF":
        r = [dict(flat(json.load(open(f"{d}/{size}/measure/row_{arm}_seed0.json")))) for d in (A, B)]
        dk = sorted(k for k in set(r[0]) | set(r[1]) if r[0].get(k) != r[1].get(k))
        la = [dict(flat(json.loads(l))) for l in open(f"{A}/{size}/ckpt_{arm}.jsonl")]
        lb = [dict(flat(json.loads(l))) for l in open(f"{B}/{size}/ckpt_{arm}.jsonl")]
        jk = sorted({k for x, y in zip(la, lb) for k in set(x) | set(y) if x.get(k) != y.get(k)})
        print(size, arm, "row keys differing:", dk, "| training-record keys differing:", jk, len(la), len(lb))
