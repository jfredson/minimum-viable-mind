"""The learned sharpness of the built-in ownership answer, per checkpoint.

Every arm carries `own_sharpness` (initialised at 4.0): the ownership answer
is softmax(sharpness x tally of acting-channel firings per agent). Arms T, C
and M use it (T and M's separable route as the row selector; C and M as the
scale-and-shift on the running state); arm F computes it and does not use it.
At sharpness near 0 the answer is flat, one quarter on each agent, and says
nothing about who the model is. Prints the sharpness and, on the 3,000 gate
episodes at the own-directed action, the mean weight the answer puts on the
agent the model actually is. Processor only, $0.

    python ownership_answer_sharpness.py SRC_DIR CKPT [CKPT ...]
"""
import sys
sys.path.insert(0, sys.argv[1])
import torch, grammar as G, models as M
n, seed, pool, rel = G.EVAL_SETS["gate"]
eps = G.episodes_from_pairs(G.make_pairs(n, seed=seed, pool=pool, collide=rel))
b = M.to_torch(G.batch(eps), "cpu"); ta = torch.as_tensor([e["model"] for e in eps])
for path in sys.argv[2:]:
    obj = torch.load(path, map_location="cpu", weights_only=True)
    if "state" in obj:
        m = M.build_from_config(obj["cfg"]); m.load_state_dict(obj["state"], strict=True)
    else:
        arm = path.split("ckpt_")[1][0]; m = M.build(arm, "toy"); m.load_state_dict(obj, strict=True)
    with torch.no_grad():
        _, p = m._own_vec(b)
        ap = b["action_pos"][:, G.OWN]; i = torch.arange(len(ap))
        w = p[i, ap, ta].mean()
    print(f"{path.split('/')[-1]:32} arm {m.cfg.arm} d_model {m.cfg.d_model}: sharpness "
          f"{float(m.own_sharpness):+.4f}; weight on the true agent {float(w):.4f}")
