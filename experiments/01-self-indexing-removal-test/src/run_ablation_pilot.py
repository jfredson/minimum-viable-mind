"""Ablation-strength escalation pilot (pre-lock; spec: ablation-pilot-spec.md).

NOT the registered removal test. The rehearsal's registered consequence: rank-1
ablation of a causally-confirmed direction does not move behaviour, so pilot
rank-k subspace ablation under the RT-07 OOD gate before θ/δ lock. This script
produces the dose-response table the spec commits to — per condition: all three
T batteries (grown versions), S-v2 responses (judged locally afterwards), and
the neutral-corpus NLL.

Conditions (spec §b, committed before running):
  - baseline
  - C_self-index RESIDUAL (RT-09) mean ablation, k in {1, 4, 8, 16}
  - C_ctrl-expert mean ablation, k in {4, 16} (differential control arm)
  - C_self-index residual DIRECTIONAL at the largest OOD-clean k (chosen at
    runtime from the mean runs against the committed 0.05-nat bound — the
    selection rule is fixed here, not the outcome)

Run from the repo root with the venv active (cloud bench: MVM_MODEL/MVM_N_LAYERS
set; long — ~8 conditions x ~122 generations):
    python experiments/01-self-indexing-removal-test/src/run_ablation_pilot.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.ablate import (  # noqa: E402
    ablation_hooks, fit_layer_directions, fit_layer_subspace, neutral_nll,
)
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import battery  # noqa: E402
from localize_context import render, load_stimuli, extract_last_all_layers  # noqa: E402
from separate_self import fit_dir  # noqa: E402
from run_t_controls import score_items  # noqa: E402
from run_s_v2 import generate_responses, BATTERY_V2  # noqa: E402

import numpy as np  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "prelock"
ABLATE_LAYERS = config.scale_layers([8, 11, 14, 18, 22])
K_LADDER = [1, 4, 8, 16]
K_CTRL = [4, 16]
OOD_BOUND_NATS = 0.05  # rehearsal RT-07 bound, carried by the spec


def fit_structures(stim, acts):
    """Rank-k index-residual subspaces (primary target) and expert-persona
    subspaces (control arm), per the spec. Returns
    {("index_residual", k): {L: [(dir, mu), ...]}, ("expert", k): ...}."""
    def sel(mech):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        return idx, np.array([stim[i]["label"] for i in idx])

    idx_tr, y_tr = sel("turn_role")
    idx_ob, y_ob = sel("observed_speaker")
    idx_ex, y_ex = sel("expert_persona")

    # d_generic per layer (rank-1, as registered) for the RT-09 residual path
    gen = fit_layer_directions(acts, idx_ob, y_ob, ABLATE_LAYERS, fit_dir)
    gen_dirs = {L: d for L, (d, _mu) in gen.items()}

    out = {}
    for k in sorted(set(K_LADDER)):
        out[("index_residual", k)] = fit_layer_subspace(
            acts, idx_tr, y_tr, ABLATE_LAYERS, fit_dir, k,
            residual_against=gen_dirs)
    for k in sorted(set(K_CTRL)):
        out[("expert", k)] = fit_layer_subspace(
            acts, idx_ex, y_ex, ABLATE_LAYERS, fit_dir, k)
    return out


def score_condition(model, tok, device, tag):
    """Full re-score under whatever hooks are currently installed (same shape
    as the rehearsal's score_condition; grown batteries load from disk)."""
    t0 = time.time()
    nll = neutral_nll(model, tok, device)
    out = {"neutral_nll": nll}
    for bname, path in (("T_self_irrelevant", battery.TASK_BATTERY),
                        ("T_self_relevant", battery.TASK_BATTERY_SELF_RELEVANT),
                        ("T_syntax", battery.TASK_BATTERY_SYNTAX)):
        items = battery.load_task_battery(path)
        print(f"  [{tag}] {bname} ({len(items)} items)...", flush=True)
        r = score_items(model, tok, device, items, verbose=False)
        out[bname] = r
        print(f"  [{tag}] {bname} accuracy {r['summary']['accuracy']:.3f}",
              flush=True)
    s_items = battery.load_self_report_battery(BATTERY_V2)
    print(f"  [{tag}] S battery v2 ({len(s_items)} items)...", flush=True)
    s_rows = generate_responses(model, tok, device, s_items)
    (OUT_DIR / f"s_responses_{tag}.json").write_text(json.dumps({
        "model_id": config.MODEL_ID, "condition": tag, "items": s_rows,
    }, indent=2))
    print(f"  [{tag}] done in {time.time() - t0:.0f}s (neutral nll {nll:.4f})",
          flush=True)
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting activations for subspace fitting...", flush=True)
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)
    structures = fit_structures(stim, acts)
    del acts

    results = {"model_id": config.MODEL_ID, "ablate_layers": ABLATE_LAYERS,
               "k_ladder": K_LADDER, "k_ctrl": K_CTRL,
               "ood_bound_nats": OOD_BOUND_NATS, "conditions": {}}
    ckpt = OUT_DIR / "ablation_pilot_scores.json"

    def run(tag, key, mode):
        print(f"\n=== condition: {tag} ===", flush=True)
        if key is None:
            results["conditions"][tag] = score_condition(model, tok, device, tag)
        else:
            with ablation_hooks(model, structures[key], mode):
                results["conditions"][tag] = score_condition(model, tok, device, tag)
        ckpt.write_text(json.dumps(results, indent=2))  # checkpoint per condition

    run("baseline", None, None)
    base_nll = results["conditions"]["baseline"]["neutral_nll"]

    for k in K_LADDER:
        run(f"idxres_mean_k{k}", ("index_residual", k), "mean")
    for k in K_CTRL:
        run(f"expert_mean_k{k}", ("expert", k), "mean")

    # Directional cross-check at the largest OOD-clean k (rule fixed in the
    # spec: Δnll over baseline ≤ OOD_BOUND_NATS among the mean runs).
    clean = [k for k in K_LADDER
             if results["conditions"][f"idxres_mean_k{k}"]["neutral_nll"]
             - base_nll <= OOD_BOUND_NATS]
    if clean:
        k_dir = max(clean)
        results["directional_k_rule"] = (f"largest OOD-clean k={k_dir} "
                                         f"(clean set {clean})")
        run(f"idxres_directional_k{k_dir}", ("index_residual", k_dir),
            "directional")
    else:
        results["directional_k_rule"] = ("no OOD-clean k in the ladder — "
                                         "directional cross-check skipped; "
                                         "see spec loss condition")
        ckpt.write_text(json.dumps(results, indent=2))

    print(f"\nsaved -> {ckpt}")
    print("next: pull artifacts; judge each s_responses_<cond>.json locally "
          "(rubric v2); analysis applies the battery-growth cull rule to the "
          "per-item results before computing drops.")


if __name__ == "__main__":
    main()
