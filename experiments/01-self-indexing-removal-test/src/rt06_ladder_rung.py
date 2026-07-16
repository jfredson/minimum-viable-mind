"""One RT-06 ladder rung: baseline scoring + the k=4 unmasking probe
(spec: rt06-ladder-spec.md, committed before any rung runs).

Runs on whatever checkpoint MVM_MODEL selects. Fits the C_self-index residual
rank-4 subspace on THIS rung's stimuli (same machinery and band as the
prelock pilot), then scores baseline and idxres_mean_k4 conditions (three
post-cull T batteries + S-v2 responses + neutral NLL each). Artifacts to
artifacts/ladder/<rung>/.

The rung name comes from MVM_RUNG (falls back to the model id's basename).
Localization/`c_ctrl_checks` run separately per rung (see run_ladder.sh) —
this script owns only the scoring conditions.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.ablate import ablation_hooks, fit_layer_directions, fit_layer_subspace  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import render, load_stimuli, extract_last_all_layers  # noqa: E402
from separate_self import fit_dir  # noqa: E402
import run_ablation_pilot as rap  # noqa: E402

import numpy as np  # noqa: E402

RUNG = os.environ.get("MVM_RUNG") or config.MODEL_ID.rsplit("/", 1)[-1]
LADDER_DIR = config.ARTIFACTS_DIR / "ladder" / RUNG
ABLATE_LAYERS = config.scale_layers([8, 11, 14, 18, 22])
K = 4  # the prelock condition with the largest S increase on SFT


def main() -> None:
    LADDER_DIR.mkdir(parents=True, exist_ok=True)
    rap.OUT_DIR = LADDER_DIR  # score_condition's s_responses_* land per rung

    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print(f"[{RUNG}] extracting activations for direction fitting...", flush=True)
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)

    def sel(mech):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        return idx, np.array([stim[i]["label"] for i in idx])

    idx_tr, y_tr = sel("turn_role")
    idx_ob, y_ob = sel("observed_speaker")
    gen = fit_layer_directions(acts, idx_ob, y_ob, ABLATE_LAYERS, fit_dir)
    subspace = fit_layer_subspace(
        acts, idx_tr, y_tr, ABLATE_LAYERS, fit_dir, K,
        residual_against={L: d for L, (d, _mu) in gen.items()})
    del acts

    results = {"model_id": config.MODEL_ID, "rung": RUNG,
               "ablate_layers": ABLATE_LAYERS, "k": K, "conditions": {}}
    ckpt = LADDER_DIR / "ladder_rung_scores.json"

    print(f"\n=== [{RUNG}] condition: baseline ===", flush=True)
    results["conditions"]["baseline"] = rap.score_condition(
        model, tok, device, f"{RUNG}_baseline")
    ckpt.write_text(json.dumps(results, indent=2))

    print(f"\n=== [{RUNG}] condition: idxres_mean_k{K} ===", flush=True)
    with ablation_hooks(model, subspace, "mean"):
        results["conditions"][f"idxres_mean_k{K}"] = rap.score_condition(
            model, tok, device, f"{RUNG}_idxres_mean_k{K}")
    ckpt.write_text(json.dumps(results, indent=2))

    print(f"\n[{RUNG}] saved -> {ckpt}", flush=True)


if __name__ == "__main__":
    main()
