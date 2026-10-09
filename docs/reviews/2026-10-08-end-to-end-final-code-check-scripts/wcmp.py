import sys, torch
dirs = sys.argv[1:]
def sd(p):
    x = torch.load(p, map_location="cpu", weights_only=False)
    for k in ("state", "model", "state_dict"):
        if isinstance(x, dict) and k in x and isinstance(x[k], dict): return x[k]
    return x
for arm in "TCMF":
    s = [sd(f"{d}/ckpt_{arm}.pt") for d in dirs]
    tens = {k: v for k, v in s[0].items() if torch.is_tensor(v)}
    ok = all(set(tens) == {k for k, v in t.items() if torch.is_tensor(v)} and all(torch.equal(tens[k], t[k]) for k in tens) for t in s[1:])
    print(arm, len(tens), "tensors; identical across", len(dirs), "runs:", ok)
