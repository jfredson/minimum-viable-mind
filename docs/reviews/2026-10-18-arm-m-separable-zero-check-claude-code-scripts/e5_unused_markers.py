"""E5: a measured stand-in for F7's "decay alone takes a weight to 33.5 per cent".

The vocabulary has twenty marker words (m0 to m19); the gate episodes use
m0 to m11. If m12 to m19 never appear in training, their embedding rows get no
gradient, so AdamW changes them by decay alone, and their end-over-start size
measures what decay alone did in this very run. This prints, for each arm at
10 million, each marker word's embedding size at the end over its rebuilt start
(torch.manual_seed(0), models.build, as D6 and D8 do), and how often each marker
word appears in a sample of the training stream."""
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2026-10-18-arm-m-separable-zero-scripts"))
from common import header, load, G, M   # noqa: E402

header("E5: marker-word embeddings, end over start, words in use against words never used")
words = [f"m{i}" for i in range(20)]
ids = torch.tensor([G.VOCAB[w] for w in words])

# how often each marker word appears in the training stream (steps 0 to 199 of seed 0, as the trainer draws them)
stream = G.TrainingStream(0)
counts = torch.zeros(len(G.VOCAB), dtype=torch.long)
for step in range(200):
    tok = torch.as_tensor(stream.batch_for_step(step, 96)["tokens"])
    counts += torch.bincount(tok.flatten(), minlength=len(G.VOCAB))
print("appearances in 200 training batches (seed 0, batch 96): "
      + ", ".join(f"{w} {int(counts[i])}" for w, i in zip(words, ids.tolist())))

torch.set_grad_enabled(False)
for name in ("M-10M-rerun", "T-10M-rerun"):
    m, _ = load(name)
    torch.manual_seed(0)
    m0 = M.build(m.cfg.arm, "10M")
    r = (m.tok.weight[ids].norm(dim=-1) / m0.tok.weight[ids].norm(dim=-1))
    used, unused = r[:12], r[12:]
    print(f"\n{name}: end over start, per marker word")
    print("  m0-m11:  " + " ".join(f"{float(x):.3f}" for x in used))
    print("  m12-m19: " + " ".join(f"{float(x):.3f}" for x in unused))
    print(f"  mean: words in use {float(used.mean()):.4f}; words never used {float(unused.mean()):.4f} "
          f"(decay arithmetic: 0.3350)")
    # is the rebuilt seed-0 start the trainer's exact draw? A different draw would scatter these ratios
    for seed in (0, 1):
        torch.manual_seed(seed)
        ms = M.build(m.cfg.arm, "10M")
        ru = m.tok.weight[ids[12:]].norm(dim=-1) / ms.tok.weight[ids[12:]].norm(dim=-1)
        print(f"  start rebuilt with seed {seed}: words never used, end over start from {float(ru.min()):.5f} "
              f"to {float(ru.max()):.5f}")
