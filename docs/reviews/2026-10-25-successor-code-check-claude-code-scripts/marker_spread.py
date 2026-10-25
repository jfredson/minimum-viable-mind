"""Finding 13: how different the built answer's marker projection is across the 20 marker words, per saved model.
Run with PYTHONPATH=experiments/08-successor-degree/src and the saved-models folder as the argument."""
import sys, torch, grammar as G
A = sys.argv[1]
ids = torch.tensor([G.VOCAB[w] for w in G.VOCAB if w.startswith("m") and w[1:].isdigit()])
for n in ["succ_t_10m_seed0_rerun", "succ_c_10m_seed0_rerun", "succ_m_10m_seed0_rerun", "succ_c_10m_seed0", "succ_f_10m_seed0"]:
    sd = torch.load(f"{A}/{n}/{n}.pt", map_location="cpu", weights_only=False)["state"]
    v = sd["tok.weight"][ids] @ sd["own_marker.weight"].T + sd["own_marker.bias"]
    mean = v.mean(0)
    print(f"{n}: sharpness {float(sd['own_sharpness']):.3f}; {len(ids)} markers; mean projection norm {mean.norm():.3f}; "
          f"average distance from the mean {(v - mean).norm(dim=1).mean():.4f}")
