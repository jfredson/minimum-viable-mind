"""D8, ADDED AFTER THE FIRST OUTPUTS (not in the method file): D6 found arm M's
row-choice weights larger than at the start, yet its row choice flat and its
slot small. The slot and the row keys are both built from the agents' marker
words through `own_marker`. This measures how different those vectors are from
one marker word to the next (the only thing that lets the row choice tell the
agents apart), at the start and at the end of training."""
import torch
from common import header, load, gate, chunks, final_parts, separable_mask, G, M

header("D8: how far the built answer's vectors differ between agents (the twelve marker words in use)")
markers = torch.tensor([G.VOCAB[f"m{i}"] for i in range(12)])


def spread(m):
    v = m.own_marker(m.tok(markers))                       # (12, 24)
    centred = v - v.mean(0, keepdim=True)
    k = m.own_key(v)
    kc = k - k.mean(0, keepdim=True)
    return (float(v.norm(dim=-1).mean()), float(centred.norm(dim=-1).mean()),
            float(kc.norm(dim=-1).mean()), float(m.tok(markers).norm(dim=-1).mean()))


print("columns: mean size of the vector; mean size of its part that differs between marker words;")
print("         the same for the row keys; mean size of the marker words' embeddings")
for name, size in (("M-10M-rerun", "10M"), ("T-10M-rerun", "10M"), ("M-toy-seed0", "toy"), ("T-toy-seed0", "toy")):
    m, _ = load(name)
    e = spread(m)
    line = f"  {name:12s} end   vector {e[0]:7.3f}  differing part {e[1]:7.3f}  keys' differing part {e[2]:8.3f}  embeddings {e[3]:7.3f}"
    if size == "10M":
        torch.manual_seed(0)
        s = spread(M.build(m.cfg.arm, "10M"))
        line += (f"\n  {'':12s} start vector {s[0]:7.3f}  differing part {s[1]:7.3f}  keys' differing part {s[2]:8.3f}  embeddings {s[3]:7.3f}"
                 f"\n  {'':12s} differing part, end over start {e[1] / s[1]:.4f} (decay alone: 0.3350)")
    print(line)
