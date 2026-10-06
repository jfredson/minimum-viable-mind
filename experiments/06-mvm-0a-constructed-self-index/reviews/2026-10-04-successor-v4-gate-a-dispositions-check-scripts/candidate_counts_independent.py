"""Independent recount of the candidate counts behind the proposed repair of
the battery clause (RT-237). Written by the checking session. It does NOT
import lesion_content_check.py. It uses only the rehearsal's shared generator
(grammar.py), model builders (repairs.build_for, arms) and the committed model
files, none of which the pull request under check changed.

Differences from the author's script, on purpose:
- candidates are read off the TOKEN SEQUENCE (the item word in the action
  turn, then the four assignment turns for that item word), not off the
  episode's `values` field;
- the line is computed with exact integer arithmetic (math.comb), not scipy;
- the model fingerprints are recomputed here.

Processor only, $0. Run from experiments/rehearsal-successor-measure/src/.
"""
import hashlib, json, math, os, sys
from fractions import Fraction
import numpy as np
import torch

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                   "..", "rehearsal-successor-measure", "src"))
sys.path.insert(0, SRC)
import grammar as G          # noqa: E402
import repairs as R          # noqa: E402

MODELS = os.path.join(SRC, "..", "out-repairs", "models")
N = 3000

# exact one-sided line: smallest k with P(X >= k) <= 0.05, X ~ Bin(3000, 1/2)
tail = Fraction(0)
total = 2 ** N
k = N + 1
while True:
    nxt = tail + Fraction(math.comb(N, k - 1), total)
    if nxt > Fraction(1, 20):
        break
    tail, k = nxt, k - 1
print(f"line: candidate count >= {k}  (P(X>={k}) = {float(tail):.5f}; "
      f"P(X>={k-1}) = {float(tail + Fraction(math.comb(N, k-1), total)):.5f})")

pairs = G.make_pairs(1500, seed=99, pool="dev")
eps = G.episodes_from_pairs(pairs)
assert len(eps) == N
tok = np.stack([e["tokens"] for e in eps])
act = np.stack([e["acting"] for e in eps])

slot_word = {G.VOCAB[f"v{i}"]: i for i in range(8)}
succ_word = {w: G.VOCAB[f"v{(s + 1) % 8}"] for w, s in slot_word.items()}
ACT, SELF, MASK = G.VOCAB["<act>"], G.VOCAB["<self>"], G.VOCAB["<mask>"]

# Read each action turn from tokens: '<act> revise <who> <item> <ans> <mask> <nl>'
cand = np.zeros((N, 2, 4), dtype=np.int64)
for i in range(N):
    t = tok[i]
    assigns = [(t[1 + 5 * u + 2], t[1 + 5 * u + 3]) for u in range(8)]  # (item, value)
    starts = [p for p in range(len(t)) if t[p] == ACT]
    assert len(starts) == 2
    for p in starts:
        cond = 0 if t[p + 2] == SELF else 1
        item = t[p + 3]
        vals = [v for (it, v) in assigns if it == item]
        assert len(vals) == 4
        cand[i, cond] = [succ_word[int(v)] for v in vals]

want = {}
for row in open(os.path.join(MODELS, "SHA256SUMS")):
    if row.strip():
        h, name = row.split()
        want[name.lstrip("*")] = h


def batch(zero):
    b = G.batch(eps)
    if zero:
        b["acting"] = np.zeros_like(b["acting"])
    return {kk: torch.as_tensor(v) for kk, v in b.items()}


B_ON, B_OFF = batch(False), batch(True)
tgt = B_ON["targets"].numpy()
assert all(tgt[i, c] in cand[i, c] for i in range(N) for c in (0, 1))


@torch.no_grad()
def preds(m, b):
    out = []
    for s in range(0, N, 500):
        out.append(m({kk: v[s:s + 500] for kk, v in b.items()}).argmax(-1).numpy())
    return np.concatenate(out)


def counts(p):
    r = {}
    for c, nm in ((0, "own"), (1, "other")):
        q = p[:, c]
        r[nm] = dict(correct=int((q == tgt[:, c]).sum()),
                     legal=int(np.isin(q, list(slot_word)).sum()),
                     candidate=int((q[:, None] == cand[:, c]).any(1).sum()))
    return r


res = {"line": k, "models": {}}
cases = [(a, s) for a in ("T", "C", "M", "F", "blind") for s in (0, 1, 2)]
cases += [("untrained-F", s) for s in (0, 1, 2)]
for arm, seed in cases:
    if arm == "untrained-F":
        torch.manual_seed(1000 + seed)
        m = R.build_for("F")().eval()
    else:
        name = f"ckpt_{arm}_base_seed{seed}.pt"
        h = hashlib.sha256(open(os.path.join(MODELS, name), "rb").read()).hexdigest()
        assert h == want[name], name
        m = R.build_for(arm)()
        m.load_state_dict(torch.load(os.path.join(MODELS, name), map_location="cpu"),
                          strict=True)
        m.eval()
    on = counts(preds(m, B_OFF if arm == "blind" else B_ON))
    off = counts(preds(m, B_OFF))
    res["models"][f"{arm}/{seed}"] = dict(channel_on=on, channel_zeroed=off)
    print(f"{arm:>11}/{seed} on : own {on['own']}  other {on['other']}")
    print(f"{'':>13} off: own {off['own']}  other {off['other']}  "
          f"holds(own) {off['own']['candidate'] >= k}")

# compare with the author's committed JSON, value for value
auth = json.load(open(os.path.join(SRC, "..", "out-lesion-content-check",
                                   "lesion_content_check.json")))
diff = 0
for key, v in res["models"].items():
    a = auth["models"][key]
    for side in ("channel_on", "channel_zeroed"):
        for c in ("own", "other"):
            for f in ("correct", "legal", "candidate"):
                if v[side][c][f] != a[side][c][f]:
                    diff += 1
                    print("DIFF", key, side, c, f, v[side][c][f], a[side][c][f])
print(f"author's line {auth['line']['min_candidate_count']}, this line {k}")
print(f"values compared: {len(res['models']) * 12}; differing: {diff}")
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "candidate_counts_independent.json"), "w"),
          indent=1, sort_keys=True)
