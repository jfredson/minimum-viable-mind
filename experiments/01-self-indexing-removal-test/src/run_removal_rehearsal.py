"""DRESS REHEARSAL of the removal test, on the pilot sandbox. NOT the
registered run.

Purpose: exercise the full pre-registered pipeline end to end — localize,
ablate, re-score T and S, gate for OOD — so every instrument bug surfaces now,
on the machine where iteration is cheap, and mini-day is turnkey. Thresholds
are NOT locked (they lock on the registered substrate); the analyzer applies
clearly-labeled rehearsal-only reference values.

Conditions (committed before running):
  - baseline (no hooks)
  - C_self-index RESIDUAL (per RT-09: d_index with d_generic projected out),
    mean ablation (registered primary)
  - C_self-narrative, mean
  - C_ctrl-generic (C_speaker-generic), mean
  - C_ctrl-expert (expert_persona), mean
  - C_self-index residual, DIRECTIONAL (the OOD-minimizing cross-check)

Ablation band: per-layer directions fitted and ablated at layers
[8, 11, 14, 18, 22] simultaneously — the band where causal restoration grows.
Every condition re-scores: T_self_irrelevant (Stage-0 battery),
T_self_relevant (RT-02), T_syntax (RT-05), S battery v2 (responses saved for
the held-out judge), plus the RT-07 neutral-corpus NLL.

Run from the repo root with the venv active (long: ~6 conditions x ~62
generations):
    python experiments/01-self-indexing-removal-test/src/run_removal_rehearsal.py
then judge each condition's S responses (see analyze_rehearsal.py header).
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
from mvm.ablate import ablation_hooks, neutral_nll  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import battery  # noqa: E402
from localize_context import render, load_stimuli, extract_last_all_layers  # noqa: E402
from separate_self import fit_dir  # noqa: E402
from run_t_controls import score_items  # noqa: E402
from run_s_v2 import generate_responses, BATTERY_V2  # noqa: E402

import numpy as np  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1" / "rehearsal"
ABLATE_LAYERS = [8, 11, 14, 18, 22]

MECH = {"index": "turn_role", "narrative": "narrative",
        "generic": "observed_speaker", "expert": "expert_persona"}


def fit_all_directions(stim, acts):
    """{structure: {layer: (unit_dir, mean_coord)}} for the four structures,
    plus the RT-09 index residual (primary removal-test target)."""
    dirs = {}
    for name, mech in MECH.items():
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        y = np.array([stim[i]["label"] for i in idx])
        dirs[name] = {}
        for L in ABLATE_LAYERS:
            X = acts[L][idx]
            d = fit_dir(X, y)
            dirs[name][L] = (d.astype(np.float32), float((X @ d).mean()))
    # RT-09 residual: project the generic direction out of the index direction,
    # re-derive the reference mean on the residual direction directly.
    idx_i = [i for i, r in enumerate(stim) if r["mechanism"] == "turn_role"]
    res = {}
    for L in ABLATE_LAYERS:
        d_i, _ = dirs["index"][L]
        d_g, _ = dirs["generic"][L]
        r = d_i - (d_i @ d_g) * d_g
        r = r / np.linalg.norm(r)
        X = acts[L][idx_i]
        res[L] = (r.astype(np.float32), float((X @ r).mean()))
    dirs["index_residual"] = res
    return dirs


def score_condition(model, tok, device, tag):
    """Full re-score under whatever hooks are currently installed."""
    t0 = time.time()
    nll = neutral_nll(model, tok, device)
    out = {"neutral_nll": nll}
    for bname, path in (("T_self_irrelevant", battery.TASK_BATTERY),
                        ("T_self_relevant", battery.TASK_BATTERY_SELF_RELEVANT),
                        ("T_syntax", battery.TASK_BATTERY_SYNTAX)):
        items = battery.load_task_battery(path)
        print(f"  [{tag}] {bname} ({len(items)} items)...")
        r = score_items(model, tok, device, items, verbose=False)
        out[bname] = r
        print(f"  [{tag}] {bname} accuracy {r['summary']['accuracy']:.3f}")
    s_items = battery.load_self_report_battery(BATTERY_V2)
    print(f"  [{tag}] S battery v2 ({len(s_items)} items)...")
    s_rows = generate_responses(model, tok, device, s_items)
    (OUT_DIR / f"s_responses_{tag}.json").write_text(json.dumps({
        "model_id": config.MODEL_ID, "condition": tag, "items": s_rows,
    }, indent=2))
    print(f"  [{tag}] done in {time.time() - t0:.0f}s (neutral nll {nll:.4f})")
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting activations for direction fitting...")
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)
    dirs = fit_all_directions(stim, acts)
    del acts

    conditions = [
        ("baseline", None, None),
        ("cself_index_residual_mean", "index_residual", "mean"),
        ("cself_narrative_mean", "narrative", "mean"),
        ("cctrl_generic_mean", "generic", "mean"),
        ("cctrl_expert_mean", "expert", "mean"),
        ("cself_index_residual_directional", "index_residual", "directional"),
    ]

    results = {"model_id": config.MODEL_ID, "ablate_layers": ABLATE_LAYERS,
               "conditions": {}}
    for tag, structure, mode in conditions:
        print(f"\n=== condition: {tag} ===")
        if structure is None:
            results["conditions"][tag] = score_condition(model, tok, device, tag)
        else:
            with ablation_hooks(model, dirs[structure], mode):
                results["conditions"][tag] = score_condition(model, tok, device, tag)
        (OUT_DIR / "rehearsal_scores.json").write_text(
            json.dumps(results, indent=2))  # checkpoint after every condition

    print(f"\nsaved -> {OUT_DIR / 'rehearsal_scores.json'}")
    print("next: judge each s_responses_<cond>.json (see analyze_rehearsal.py), "
          "then run analyze_rehearsal.py")


if __name__ == "__main__":
    main()
