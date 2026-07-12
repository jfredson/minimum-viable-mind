"""Model + tokenizer loading.

Stage 0 uses plain transformers (smallest failure surface) to confirm the
bench works. The interpretability stages (probes, ablation, SAEs) will add
a TransformerLens loader alongside this once the smoke test is green.
"""
from __future__ import annotations

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from . import config
from .device import get_device, get_dtype


def load_tokenizer():
    return AutoTokenizer.from_pretrained(
        config.MODEL_ID, revision=config.MODEL_REVISION
    )


def load_model(device: str | None = None):
    """Load the registered model in eval mode on the chosen device.

    Returns (model, device, dtype). First call downloads weights into
    HF_HOME (~5GB for Gemma-2-2B).
    """
    device = device or get_device()
    dtype = get_dtype(device)
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_ID,
        revision=config.MODEL_REVISION,
        dtype=dtype,  # transformers 5.x renamed torch_dtype -> dtype
        attn_implementation=config.ATTN_IMPLEMENTATION,
    )
    model.to(device)
    model.eval()
    return model, device, dtype


@torch.no_grad()
def generate_text(
    model,
    tok,
    prompt: str,
    device: str,
    max_new_tokens: int = 256,
) -> str:
    """Greedy single-turn generation for one user prompt.

    Centralizes the chat-template detail (transformers 5.x returns a dict from
    apply_chat_template) so every battery and, later, every ablation re-score
    goes through the same decoding path. Deterministic by construction
    (do_sample=False), which is what the removal test needs: the only thing
    that may move a score between baseline and ablation is the intervention.
    """
    chat = [{"role": "user", "content": prompt}]
    inputs = tok.apply_chat_template(
        chat, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).to(device)
    prompt_len = inputs["input_ids"].shape[1]
    out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    return tok.decode(out[0][prompt_len:], skip_special_tokens=True).strip()


@torch.no_grad()
def generate_from_turns(
    model,
    tok,
    turns: list,
    device: str,
    max_new_tokens: int = 256,
) -> str:
    """Greedy generation continuing a scripted multi-turn conversation.

    `turns` is a list of [role, content] pairs ("user"/"model", the repo's
    stimulus convention) ending with a user turn; the model generates the next
    assistant turn. Scripted prior model turns are teacher-forced context —
    the battery item defines what the model previously "said," which is what
    the T_self_relevant / T_syntax items need (binding to own prior turns).
    Deterministic, same rationale as generate_text.
    """
    role_map = {"user": "user", "model": "assistant", "assistant": "assistant"}
    chat = [{"role": role_map[r], "content": c} for r, c in turns]
    inputs = tok.apply_chat_template(
        chat, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).to(device)
    prompt_len = inputs["input_ids"].shape[1]
    out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    return tok.decode(out[0][prompt_len:], skip_special_tokens=True).strip()
