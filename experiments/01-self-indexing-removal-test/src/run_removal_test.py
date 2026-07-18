"""THE REGISTERED REMOVAL TEST — Experiment 1.

Runs the conditions fixed by the θ/δ lock (`thresholds.md`, commit 8b1fcbe)
on the HELD-OUT test batteries (`test-set-authoring-spec.md`), once:

  - baseline
  - C_self-index RESIDUAL k=16 mean ablation      (primary, RT-09 target)
  - C_self-index residual k=16 directional        (OOD-minimizing cross-check)
  - C_self-narrative k=16 mean ablation           (independent, RT-04)
  - C_ctrl-expert k=16 mean ablation              (differential control, RT-06)

Every condition is scored on: the three held-out T batteries, the held-out
S-v2 battery (responses generated here, judged locally afterward by the
held-out judge), and the Pass 5 dual OOD gate (neutral-corpus Δnll +
long-generation Δrep-4, both against this run's own baseline, with the
null-calibrated k=16 bounds from `ood_calibration.json`).

Subspace fitting is byte-identical to the pilot machinery: rank-16 logistic
deflation per structure on the localization stimuli; the index basis is
residualized against d_generic (RT-09) and re-orthonormalized. Nothing here
chooses anything — every parameter was locked before this script runs.

The decision rule (locked θ_task=0.10, θ_self=0.25, δ=0.10) is applied in
the analysis step AFTER local S judging + the standard human spot-check —
not in this script.

Cloud bench: MVM_MODEL=allenai/Llama-3.1-Tulu-3-8B-SFT MVM_N_LAYERS=32
    python experiments/01-self-indexing-removal-test/src/run_removal_test.py
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
from run_s_v2 import generate_responses  # noqa: E402
from run_ood_calibration import longgen_rep  # noqa: E402

import numpy as np  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "removal_test"
ABLATE_LAYERS = config.scale_layers([8, 11, 14, 18, 22])
K = 16
# Pass 5 null-calibrated k=16 bounds (ood_calibration.json, run 2026-07-18;
# registered in prelock-findings.md §e). Deltas vs this run's own baseline.
BOUND_NLL_K16 = 0.0893
BOUND_REP4_K16 = 0.2885
GEN_TOKENS = 256

TEST_BATTERIES = {
    "T_self_irrelevant": THIS_DIR / "batteries" / "test_task_battery.jsonl",
    "T_self_relevant": THIS_DIR / "batteries" / "test_task_battery_self_relevant.jsonl",
    "T_syntax": THIS_DIR / "batteries" / "test_task_battery_syntax.jsonl",
}
TEST_S_BATTERY = THIS_DIR / "batteries" / "test_self_report_battery_v2.jsonl"


def fit_structures(stim, acts):
    """Rank-16 bases for the three registered arms, pilot-identical method."""
    def sel(mech):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        return idx, np.array([stim[i]["label"] for i in idx])

    idx_tr, y_tr = sel("turn_role")
    idx_ob, y_ob = sel("observed_speaker")
    idx_na, y_na = sel("narrative")
    idx_ex, y_ex = sel("expert_persona")

    gen = fit_layer_directions(acts, idx_ob, y_ob, ABLATE_LAYERS, fit_dir)
    gen_dirs = {L: d for L, (d, _mu) in gen.items()}

    return {
        "index_residual": fit_layer_subspace(
            acts, idx_tr, y_tr, ABLATE_LAYERS, fit_dir, K,
            residual_against=gen_dirs),
        "narrative": fit_layer_subspace(
            acts, idx_na, y_na, ABLATE_LAYERS, fit_dir, K),
        "expert": fit_layer_subspace(
            acts, idx_ex, y_ex, ABLATE_LAYERS, fit_dir, K),
    }


def score_condition(model, tok, device, tag):
    t0 = time.time()
    out = {"neutral_nll": neutral_nll(model, tok, device)}
    out.update(longgen_rep(model, tok, device, 16, GEN_TOKENS))
    for bname, path in TEST_BATTERIES.items():
        items = battery.load_task_battery(path)
        r = score_items(model, tok, device, items, verbose=False)
        out[bname] = r
        print(f"  [{tag}] {bname} {r['summary']['accuracy']:.3f}", flush=True)
    s_items = battery.load_self_report_battery(TEST_S_BATTERY)
    s_rows = generate_responses(model, tok, device, s_items)
    (OUT_DIR / f"s_responses_{tag}.json").write_text(json.dumps({
        "model_id": config.MODEL_ID, "condition": tag, "items": s_rows,
    }, indent=2))
    print(f"  [{tag}] done {time.time()-t0:.0f}s  nll {out['neutral_nll']:.4f}  "
          f"rep4 {out['rep4']:.4f}", flush=True)
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("fitting registered structures (k=16)...", flush=True)
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)
    structures = fit_structures(stim, acts)
    del acts

    results = {"model_id": config.MODEL_ID, "k": K,
               "ablate_layers": ABLATE_LAYERS,
               "bounds_k16": {"nll": BOUND_NLL_K16, "rep4": BOUND_REP4_K16},
               "lock_commit": "8b1fcbe", "conditions": {}}
    ckpt = OUT_DIR / "removal_test_scores.json"

    def run(tag, key, mode):
        print(f"\n=== {tag} ===", flush=True)
        if key is None:
            results["conditions"][tag] = score_condition(model, tok, device, tag)
        else:
            with ablation_hooks(model, structures[key], mode):
                results["conditions"][tag] = score_condition(model, tok, device, tag)
        ckpt.write_text(json.dumps(results, indent=2))

    run("baseline", None, None)
    run("idxres_mean_k16", "index_residual", "mean")
    run("idxres_directional_k16", "index_residual", "directional")
    run("narrative_mean_k16", "narrative", "mean")
    run("expert_mean_k16", "expert", "mean")

    base = results["conditions"]["baseline"]
    for tag, row in results["conditions"].items():
        if tag == "baseline":
            continue
        dnll = row["neutral_nll"] - base["neutral_nll"]
        drep = row["rep4"] - base["rep4"]
        row["ood"] = {"dnll": dnll, "drep4": drep,
                      "nll_clean": dnll <= BOUND_NLL_K16,
                      "longgen_clean": drep <= BOUND_REP4_K16}
    ckpt.write_text(json.dumps(results, indent=2))
    print(f"\nsaved -> {ckpt}")
    print("next: pull artifacts; judge s_responses_* locally (rubric v2, "
          "held-out judge); human spot-check; THEN apply the locked decision "
          "rule in the findings memo.")


if __name__ == "__main__":
    main()
