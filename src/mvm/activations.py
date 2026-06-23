"""Residual-stream activation extraction via HuggingFace forward passes.

Stage 1 localization needs to read the residual stream at chosen layers and
token positions — for training linear probes, for fitting/decoding GemmaScope
SAE features, and (later) for activation patching and ablation. We get it from
the HF model's `output_hidden_states` rather than loading a second copy of the
weights through TransformerLens: on a 16GB machine one bf16 model on MPS is the
budget, and `hidden_states[L+1]` IS the residual stream after layer L
(`resid_post`), which is exactly where the GemmaScope residual SAEs are trained.

Convention (HF): for an n-layer model, `output_hidden_states` returns n+1
tensors. `hidden_states[0]` is the embedding output (resid_pre of layer 0);
`hidden_states[L+1]` is the output of layer L (resid_post of layer L). So the
GemmaScope hook `blocks.L.hook_resid_post` maps to `hidden_states[L+1]`.
"""
from __future__ import annotations

import torch


def _ensure_pad_token(tok) -> None:
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token


@torch.no_grad()
def resid_post(
    model,
    tok,
    prompts: list[str],
    device: str,
    layers: list[int],
    use_chat_template: bool = False,
) -> dict[int, torch.Tensor]:
    """Residual-stream activations at the last real token of each prompt.

    Returns {layer L: tensor of shape [n_prompts, d_model]} where the vector is
    `resid_post` of layer L at each prompt's final non-pad token. Right-padded;
    the last-token index is read from the attention mask so padding never leaks
    into the extracted vector.

    use_chat_template=True wraps each prompt as a user turn (matching how the
    batteries are run); False tokenizes the raw string (useful for minimal-pair
    probe stimuli).
    """
    _ensure_pad_token(tok)
    if use_chat_template:
        texts = [
            tok.apply_chat_template(
                [{"role": "user", "content": p}],
                add_generation_prompt=True,
                tokenize=False,
            )
            for p in prompts
        ]
        enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False)
    else:
        enc = tok(prompts, return_tensors="pt", padding=True)
    enc = {k: v.to(device) for k, v in enc.items()}

    out = model(**enc, output_hidden_states=True)
    hs = out.hidden_states  # tuple length n_layers + 1
    mask = enc["attention_mask"]
    # Index of the last real token, robust to padding side: among positions with
    # mask==1, take the largest index. (mask.sum-1 is only correct for RIGHT
    # padding; this tokenizer left-pads by default, which would otherwise read a
    # length-correlated interior token.)
    pos = torch.arange(mask.shape[1], device=mask.device)
    last_idx = (mask * pos).argmax(dim=1)  # [n_prompts]
    batch_idx = torch.arange(mask.shape[0], device=mask.device)

    feats = {}
    for L in layers:
        h = hs[L + 1]  # resid_post of layer L: [n_prompts, seq, d_model]
        feats[L] = h[batch_idx, last_idx].detach()
    return feats
