"""Page 1 closure check (the free model's battery clause, inside review RT-237).

Recomputes, without importing lesion_content_check.py (the author's script) or
candidate_counts_independent.py (the first check's, pull request 96):
  1. the line, 1,546 of 3,000, by whole-number arithmetic only;
  2. for every committed trained model and three untrained ones, with the
     acting channel zeroed, how many own-directed answers are one of the four
     allowed answers (the successor of one of the four agents' values on the
     item the action names), read from the episode's WORDS;
  3. the "two seeds of three" verdict per arm;
  4. what simple answer rules would score (the 2,257 caveat and the
     no-successor rules), and how many of each model's answers are the
     successor of ANY value shown (the ruled sentence, measured directly).
Method committed before this ran: docs/2026-10-06-page1-closure-check-method.md.
Processor only, $0. Run from experiments/rehearsal-successor-measure/src/.
"""
import hashlib, json, math, os, sys
import numpy as np
import torch

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..",
                                   "rehearsal-successor-measure", "src"))
sys.path.insert(0, SRC)
import grammar as G          # noqa: E402
import repairs as R          # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(SRC, "..", "out-repairs", "models")
AUTHOR = os.path.join(SRC, "..", "out-lesion-content-check", "lesion_content_check.json")
N = 3000

# ---- 1. the line, whole numbers only: smallest k with 20 * sum_{j>=k} C(N,j) <= 2^N
total = 1 << N
tail, k = 0, N + 1
while 20 * (tail + math.comb(N, k - 1)) <= total:
    tail += math.comb(N, k - 1)
    k -= 1
LINE = k
print(f"line: {LINE}  (count of ways to get >= {LINE} of {N}, times 20, <= 2^{N}; "
      f"one fewer would not be)")

# ---- episodes, read as words
pairs = G.make_pairs(1500, seed=99, pool="dev")
eps = G.episodes_from_pairs(pairs)
assert len(eps) == N
words = [[G.IVOCAB[int(t)] for t in e["tokens"]] for e in eps]

def vnum(w):  # "v5" -> 5
    assert w.startswith("v") and w[1:].isdigit(), w
    return int(w[1:])

allowed, any_succ, named_vals, any_vals, other_succ, own_pos = [], [], [], [], [], []
for ws in words:
    assigns = []  # (item word, value number) from "<marker> assign <item> <value> <nl>"
    for i, w in enumerate(ws):
        if w == "assign":
            assigns.append((ws[i + 1], vnum(ws[i + 2])))
    assert len(assigns) == 8
    acts = [i for i, w in enumerate(ws) if w == G.ACT]
    assert len(acts) == 2
    own = [i for i in acts if ws[i + 2] == G.SELF]
    assert len(own) == 1
    p = own[0]
    item = ws[p + 3]
    assert ws[p + 4] == G.ANS and ws[p + 5] == G.MASK
    on_item = [v for it, v in assigns if it == item]
    assert len(on_item) == 4 and len(set(on_item)) == 4
    allowed.append({f"v{(v + 1) % 8}" for v in on_item})
    any_succ.append([f"v{(v + 1) % 8}" for _, v in assigns])
    other_succ.append([f"v{(v + 1) % 8}" for it, v in assigns if it != item])
    named_vals.append([f"v{v}" for v in on_item])
    any_vals.append([f"v{v}" for _, v in assigns])
    own_pos.append(p + 5)

# the right answer is one of the four, on every episode
tg = [G.IVOCAB[int(e["targets"][G.OWN])] for e in eps]
assert all(t in a for t, a in zip(tg, allowed))

# ---- 4a. answer rules, expected counts (no model)
def expect(choices):
    return float(sum(np.mean([c in a for c in ch]) for ch, a in zip(choices, allowed)))
rules = {
    "guess among the eight value words": expect([[f"v{i}" for i in range(8)]] * N),
    "successor of any of the eight values shown (the caveat)": expect(any_succ),
    "successor of one of the four values on the OTHER item": expect(other_succ),
    "a value shown on the named item, NOT stepped on": expect(named_vals),
    "a value shown on any item, NOT stepped on": expect(any_vals),
}
print("\nexpected own-directed count of 3,000 under answer rules (line %d):" % LINE)
for name, v in rules.items():
    print(f"  {v:7.1f}  {'passes' if v >= LINE else 'fails '}  {name}")

# ---- fingerprints
want = {}
for row in open(os.path.join(MODELS, "SHA256SUMS")):
    if row.strip():
        h, name = row.split()
        want[name.lstrip("*")] = h

def load(arm, seed):
    name = f"ckpt_{arm}_base_seed{seed}.pt"
    path = os.path.join(MODELS, name)
    got = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert got == want[name], f"fingerprint mismatch: {name}"
    m = R.build_for(arm)()
    m.load_state_dict(torch.load(path, map_location="cpu"), strict=True)
    return m.eval()

# ---- forward pass, written here
arr = G.batch(eps)
bt = {k_: torch.as_tensor(v) for k_, v in arr.items()}
bt["acting"] = torch.zeros_like(bt["acting"])          # the channel zeroed
assert int(bt["acting"].sum()) == 0

@torch.no_grad()
def own_answers(m):
    out = []
    for s in range(0, N, 500):
        sl = {k_: v[s:s + 500] for k_, v in bt.items()}
        out.append(m(sl).argmax(dim=-1)[:, G.OWN].numpy())
    return [G.IVOCAB[int(x)] for x in np.concatenate(out)]

author = json.load(open(AUTHOR))
res = dict(line=LINE, rules=rules, models={})
cases = [(a, s) for a in ("T", "C", "M", "F", "blind") for s in (0, 1, 2)]
cases += [("untrained-F", s) for s in (0, 1, 2)]
print("\nchannel zeroed, own-directed, of 3,000:")
print(f"{'model':>14}  allowed  author  same  correct  succ-of-any-shown")
mismatch = 0
for arm, seed in cases:
    if arm == "untrained-F":
        torch.manual_seed(1000 + seed)
        m = R.build_for("F")().eval()
    else:
        m = load(arm, seed)
    ans = own_answers(m)
    cnt = sum(a in al for a, al in zip(ans, allowed))
    cor = sum(a == t for a, t in zip(ans, tg))
    succ_any = sum(a in set(s_) for a, s_ in zip(ans, any_succ))
    a_cnt = author["models"][f"{arm}/{seed}"]["channel_zeroed"]["own"]["candidate"]
    a_cor = author["models"][f"{arm}/{seed}"]["channel_zeroed"]["own"]["correct"]
    same = (cnt == a_cnt) and (cor == a_cor)
    mismatch += (not same)
    res["models"][f"{arm}/{seed}"] = dict(allowed=cnt, correct=cor, succ_of_any_shown=succ_any,
                                          author_allowed=a_cnt, author_correct=a_cor,
                                          same=same, holds=cnt >= LINE)
    print(f"{arm + '/' + str(seed):>14}  {cnt:7d}  {a_cnt:6d}  {str(same):>4}  {cor:7d}  {succ_any:17d}")

print("\nverdict, holds on at least two seeds of three:")
res["verdicts"] = {}
for arm in ("T", "C", "M", "F", "blind", "untrained-F"):
    h = sum(res["models"][f"{arm}/{s}"]["holds"] for s in (0, 1, 2))
    res["verdicts"][arm] = dict(seeds_holding=h, holds=h >= 2)
    print(f"  {arm:>11}: {h} of 3 -> {'holds' if h >= 2 else 'does not hold'}")
f_counts = [res["models"][f"F/{s}"]["allowed"] for s in (0, 1, 2)]
print(f"\nfree model margin over the line: {min(f_counts) - LINE} to {max(f_counts) - LINE}")
print(f"counts differing from the author's file: {mismatch} of {len(cases)}")
res["mismatches"] = mismatch
json.dump(res, open(os.path.join(HERE, "check_counts.json"), "w"), indent=2, sort_keys=True)
