"""Stage 0 configuration — the single source of truth for model identity,
paths, and device choices.

Bumping to Gemma-2-9B on a larger machine (the 48GB M4 Pro mini) is a
one-line change to MODEL_ID plus the matching SAE release below. Nothing
else in the pipeline should hard-code a model name.
"""
from __future__ import annotations

import os
from pathlib import Path

# --- Paths -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # .../minimum-viable-mind
SRC_ROOT = PROJECT_ROOT / "src"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"          # gitignored: probes, caches, results
HF_HOME = PROJECT_ROOT / ".hf-cache"                # gitignored: model + SAE downloads

# Keep every HuggingFace download inside the repo, so disk use is easy to see
# and to clean (rm -rf .hf-cache). Set before transformers/hf imports.
os.environ.setdefault("HF_HOME", str(HF_HOME))
# Let unsupported MPS ops fall back to CPU instead of raising.
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

# --- Model (active = pilot/instrument sandbox) ------------------------------
# Pilot/instrument model for the 16GB Air. The REGISTERED run moves OFF Gemma to
# a less-RLHF'd model (see the REGISTERED-RUN block below and
# experiments/01-.../registered-run-model-comparison.md) — decided 2026-06-23
# per red-team RT-05/06/08. Do NOT switch this to gemma-2-9b-it.
MODEL_ID = "google/gemma-2-2b-it"
MODEL_REVISION = "main"  # TODO: pin to a commit hash before the registered run
# Gemma-2 needs eager attention for correct attention/logit soft-capping;
# the sdpa/flash paths can silently drop it.
ATTN_IMPLEMENTATION = "eager"

# --- REGISTERED-RUN target (confirmed 2026-06-23; NOT yet active) ------------
# Substrate: Llama-3.1-8B, run as the Tülu-3 alignment ladder so RT-06's
# capability-gating can be measured as a controlled comparison of the same base
# at rising alignment. Hardware: 32GB base / 48GB M4 Pro mini (bf16 8B interp
# peaks ~22-23GB; 24GB forces 4-bit). Verify exact revisions before download.
REGISTERED_MODELS = {
    "base":       "meta-llama/Llama-3.1-8B",
    "sft":        "allenai/Llama-3.1-Tulu-3-8B-SFT",   # primary (least-RLHF'd instr.)
    "dpo":        "allenai/Llama-3.1-Tulu-3-8B-DPO",
    "rlvr":       "allenai/Llama-3.1-Tulu-3-8B",        # final Tülu-3
    "meta_instr": "meta-llama/Llama-3.1-8B-Instruct",   # 2nd alignment trajectory
}
# Method (b) SAEs for Llama-3.1-8B (confirm loader before relying on it):
#   - fnlp/Llama-Scope            : 256 SAEs, all layers, base-trained, 32k/128k (primary)
#   - EleutherAI/sae-llama-3.1-8b-32x : base-trained, via EleutherAI `sae` lib
#   - Goodfire/Llama-3.1-8B-Instruct-SAE-l19 : INSTRUCT-trained, select layers
# Llama Scope is base-trained (same pt->it assumption as gemma-scope-pt here).
# NB: SAELens support for Llama Scope is unverified — may need OpenMOSS or the
# EleutherAI sae lib instead of `sae_lens.SAE.from_pretrained`.

# --- SAEs (GemmaScope via SAELens; ACTIVE for the 2b-it sandbox) -------------
# Verify exact ids before use, e.g.:
#   from sae_lens import SAE
#   SAE.from_pretrained(SAE_RELEASE, f"layer_{L}/{SAE_WIDTH}/{SAE_CANONICAL}")
# Recorded here as the registered intent; the smoke test does not touch these.
SAE_RELEASE = "gemma-scope-2b-pt-res-canonical"  # 2B residual-stream SAEs
SAE_WIDTH = "width_16k"                           # smallest practical width
SAE_CANONICAL = "canonical"

# --- SAEs (GemmaScope via SAELens; used from Stage 1 on, NOT the smoke test) -
# Verify exact ids before use, e.g.:
#   from sae_lens import SAE
#   SAE.from_pretrained(SAE_RELEASE, f"layer_{L}/{SAE_WIDTH}/{SAE_CANONICAL}")
# Recorded here as the registered intent; the smoke test does not touch these.
SAE_RELEASE = "gemma-scope-2b-pt-res-canonical"  # 2B residual-stream SAEs
SAE_WIDTH = "width_16k"                           # smallest practical width
SAE_CANONICAL = "canonical"

# Gemma-2-2B has 26 transformer layers. Sweep the middle band first when
# localizing the self-locating structure (Experiment 1).
NUM_LAYERS = 26
CANDIDATE_LAYERS = [6, 9, 12, 15, 18, 21]

# Ensure the artifacts dir exists for downstream scripts.
ARTIFACTS_DIR.mkdir(exist_ok=True)
