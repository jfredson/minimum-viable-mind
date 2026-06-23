"""Device and dtype selection.

On Apple Silicon we run on the MPS backend at bf16. CPU falls back to
float32 for numerical stability (bf16 on CPU is slow and lossy). CUDA is
handled too, for the day this runs on a rented cloud GPU.
"""
from __future__ import annotations

import torch


def get_device() -> str:
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def get_dtype(device: str) -> torch.dtype:
    if device in ("mps", "cuda"):
        return torch.bfloat16
    return torch.float32
