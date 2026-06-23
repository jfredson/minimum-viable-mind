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
