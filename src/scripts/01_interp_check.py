"""Stage 1 interp smoke test — confirm the localization bench works.

Validates the two ingredients Stage 1 localization needs, before any real
probing/ablation logic is built on them:

  1. Residual-stream extraction from the HF model (mvm.activations.resid_post)
     — correct shapes at the candidate layers, on the selected device.
  2. A GemmaScope SAE loads via SAELens and encodes those activations into
     sparse features — confirming the d_in matches the model's d_model and that
     the feature codes are actually sparse (a sanity check on the hook-point
     convention: resid_post of layer L == hidden_states[L+1]).

Run from the repo root with the venv active:
    python src/scripts/01_interp_check.py

A green run means probes (method a) and SAE features (method b) can both be
built on this bench. Claims nothing about the model.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mvm import config  # noqa: E402
from mvm.activations import resid_post  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import torch  # noqa: E402


def main() -> None:
    device = get_device()
    print(f"device {device}  model {config.MODEL_ID}\n")
    tok = load_tokenizer()
    model, device, _ = load_model(device)

    d_model = model.config.hidden_size
    print(f"n_layers {model.config.num_hidden_layers}  d_model {d_model}\n")

    prompts = [
        "I am a language model, and right now I am answering you.",
        "The river flows past the old stone bridge at dawn.",
    ]
    print("=== 1. residual-stream extraction (resid_post, last token) ===")
    feats = resid_post(model, tok, prompts, device, config.CANDIDATE_LAYERS)
    for L in config.CANDIDATE_LAYERS:
        v = feats[L]
        assert v.shape == (len(prompts), d_model), (L, v.shape)
    probe_layer = config.CANDIDATE_LAYERS[len(config.CANDIDATE_LAYERS) // 2]
    print(f"  layers {config.CANDIDATE_LAYERS} -> each [{len(prompts)}, {d_model}]  OK")
    print(f"  using layer {probe_layer} for the SAE check\n")

    print("=== 2. GemmaScope SAE via SAELens ===")
    from sae_lens import SAE  # noqa: E402  (import here so step 1 runs even if SAELens is odd)

    sae_id = f"layer_{probe_layer}/{config.SAE_WIDTH}/{config.SAE_CANONICAL}"
    print(f"  loading {config.SAE_RELEASE}  {sae_id}")
    loaded = SAE.from_pretrained(config.SAE_RELEASE, sae_id, device=device)
    sae = loaded[0] if isinstance(loaded, tuple) else loaded
    d_sae = sae.cfg.d_sae
    print(f"  d_in {sae.cfg.d_in}  d_sae {d_sae}")
    assert sae.cfg.d_in == d_model, (sae.cfg.d_in, d_model)

    acts = feats[probe_layer].to(sae.W_enc.dtype)
    codes = sae.encode(acts)
    l0 = (codes > 0).sum(dim=-1).float()
    print(f"  encoded {tuple(acts.shape)} -> codes {tuple(codes.shape)}")
    print(f"  active features (L0) per prompt: {[int(x) for x in l0]}  "
          f"(of {d_sae}; sparse as expected)")
    assert codes.shape == (len(prompts), d_sae), codes.shape
    assert l0.max() < d_sae, "codes should be sparse, not dense"

    print("\nOK — interp bench is working (activations + SAE features).")


if __name__ == "__main__":
    main()
