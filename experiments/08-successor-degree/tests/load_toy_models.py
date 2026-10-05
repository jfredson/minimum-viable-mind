"""Test T2 of `docs/successor-code-freeze-method-2026-10-04.md`: the frozen
models are the rehearsal's models. Each of the twelve committed toy models
(checked against SHA256SUMS) is loaded twice, into the rehearsal's
`arms.py`/`arm_middle.py` in a separate process and into the frozen
`models.py` here, with no missing or extra weights, and the outputs and every
running state on 400 episodes must be bit-identical.

    python tests/load_toy_models.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
import grammar as G   # noqa: E402
import models as M    # noqa: E402

REH = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure"))
MODELS = os.path.join(REH, "out-repairs", "models")
PY = sys.executable

REHEARSAL_SIDE = r'''
import sys, numpy as np, torch
sys.path.insert(0, sys.argv[1])
import arms as A, arm_middle as MID, grammar as G
arm, ckpt, out = sys.argv[2], sys.argv[3], sys.argv[4]
m = MID.build() if arm == "M" else A.Arm(A.Config(arm=arm))
m.load_state_dict(torch.load(ckpt, map_location="cpu"), strict=True)
m.eval()
pairs = G.make_pairs(200, seed=20261004, pool="fresh")
b = A.to_torch(G.batch(G.episodes_from_pairs(pairs)), "cpu")
with torch.no_grad():
    logits, states = m(b, capture=True)
np.savez(out, logits=logits.numpy(), **{f"s{i}": s.numpy() for i, s in enumerate(states)})
'''

fails = 0
want = dict(reversed(line.split()) for line in open(os.path.join(MODELS, "SHA256SUMS")))
with tempfile.TemporaryDirectory() as tmp:
    script = os.path.join(tmp, "side.py")
    open(script, "w").write(REHEARSAL_SIDE)
    pairs = G.make_pairs(200, seed=20261004, pool="fresh")
    b = M.to_torch(G.batch(G.episodes_from_pairs(pairs)), "cpu")
    for arm in ("T", "C", "M", "F"):
        for seed in (0, 1, 2):
            ck = os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt")
            sha = hashlib.sha256(open(ck, "rb").read()).hexdigest()
            if sha != want[os.path.basename(ck)]:
                print(f"  [FAIL] {arm}/{seed}: checkpoint does not match SHA256SUMS"); fails += 1; continue
            out = os.path.join(tmp, f"{arm}{seed}.npz")
            subprocess.run([PY, script, os.path.join(REH, "src"), arm, ck, out], check=True)
            ref = np.load(out)
            m = M.build(arm, "toy")
            missing, extra = m.load_state_dict(torch.load(ck, map_location="cpu"), strict=False)
            m.eval()
            with torch.no_grad():
                logits, states = m(b, capture=True)
            same = (not missing and not extra and np.array_equal(logits.numpy(), ref["logits"])
                    and all(np.array_equal(s.numpy(), ref[f"s{i}"]) for i, s in enumerate(states)))
            print(f"  [{'PASS' if same else 'FAIL'}] {arm}/{seed}: loads with no missing or extra weights; "
                  f"outputs and all {len(states)} running states bit-identical on 400 episodes")
            fails += not same
print("\nT2 " + ("PASSES" if not fails else f"FAILS ({fails})"))
sys.exit(1 if fails else 0)
