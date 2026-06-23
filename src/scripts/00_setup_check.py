"""Stage 0 smoke test — confirm the bench works before any experiment logic.

What it does:
  - prints versions, the selected device, and the HF cache location
  - loads Gemma-2-2B-it (first run downloads ~5GB into .hf-cache/)
  - runs one short greedy generation
  - reports peak MPS memory

Run from the repo root, with the venv active:
    python src/scripts/00_setup_check.py

A green run (a sensible one-sentence answer, no errors) means the model,
device, and tokenizer are all working and the next stage can be built.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

# Make `mvm` importable without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mvm import config  # noqa: E402  (sets HF_HOME + MPS fallback on import)
from mvm.device import get_device, get_dtype  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import torch  # noqa: E402
import transformers  # noqa: E402


def gb(n_bytes: float) -> str:
    return f"{n_bytes / 1e9:.1f} GB"


def main() -> None:
    print("=== environment ===")
    print(f"python        {sys.version.split()[0]}")
    print(f"torch         {torch.__version__}")
    print(f"transformers  {transformers.__version__}")
    device = get_device()
    print(f"device        {device}  (dtype {get_dtype(device)})")
    print(f"HF_HOME       {config.HF_HOME}")
    print(f"model         {config.MODEL_ID} @ {config.MODEL_REVISION}")
    print()

    print("=== loading tokenizer + model (first run downloads ~5GB) ===")
    t0 = time.time()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    print(f"loaded in {time.time() - t0:.1f}s")
    n_params = sum(p.numel() for p in model.parameters())
    print(f"parameters    {n_params / 1e9:.2f}B")
    print()

    print("=== one greedy generation ===")
    prompt = "In one sentence, what is a melody?"
    chat = [{"role": "user", "content": prompt}]
    # transformers 5.x returns a dict (input_ids + attention_mask), not a bare tensor.
    inputs = tok.apply_chat_template(
        chat, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).to(device)
    prompt_len = inputs["input_ids"].shape[1]
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=40, do_sample=False)
    text = tok.decode(out[0][prompt_len:], skip_special_tokens=True)
    print(f"prompt:  {prompt}")
    print(f"output:  {text.strip()}")
    print()

    if device == "mps" and hasattr(torch, "mps"):
        try:
            print(f"mps peak memory  {gb(torch.mps.current_allocated_memory())}")
        except Exception:
            pass
    print("OK — bench is working.")


if __name__ == "__main__":
    main()
