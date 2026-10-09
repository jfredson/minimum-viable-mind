import json, hashlib, sys
rows, ck = sys.argv[1], sys.argv[2]
for size in ("10M", "30M"):
    for arm in "TCMF":
        want = json.load(open(f"{rows}/{size}/measure/row_{arm}_seed0.json"))["checkpoint_sha256"]
        got = hashlib.sha256(open(f"{ck}/{size}/ckpt_{arm}.pt", "rb").read()).hexdigest()
        print(size, arm, "checkpoint on disk matches the row's recorded digest:", want == got)
