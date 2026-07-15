"""SAE-feature ablation pilot (pre-lock; spec: ablation-pilot-spec.md Addendum
2026-07-15). NOT the registered removal test.

The rank-k ladder is exhausted (prelock-findings.md §b); this is the registered
escalation at feature granularity. Everything decision-relevant is pinned in
the addendum, committed before this runs:

  - Selection: per band layer, features with turn_role AUC >= 0.80, minus any
    with observed_speaker AUC >= 0.70 (feature-level RT-09), top-m by
    turn_role AUC for m in {8, 32, 128}; shortfalls recorded, never silent.
  - Semantics: clamp selected features to reference mean (primary) or zero
    (cross-check), applied as a decoder-space delta (mvm.ablate
    .sae_ablation_hooks) so reconstruction error is untouched.
  - Controls: random count- and liveness-matched feature sets (m in {32,128});
    expert_persona-selective features (m=32, no generic exclusion).
  - Gates/readout: RT-07 0.05-nat bound unchanged; candidate strength =
    smallest OOD-clean m moving >= 1 T battery by >= 3 items beyond the
    matched-m random control.

Run from the repo root with the venv active (cloud bench: MVM_MODEL,
MVM_N_LAYERS, MVM_SAE_RELEASE set):
    python experiments/01-self-indexing-removal-test/src/run_sae_pilot.py
"""
from __future__ import annotations

import gc
import json
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.ablate import neutral_nll, sae_ablation_hooks  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import render, load_stimuli, extract_last_all_layers  # noqa: E402
from converge_sae_subspace import feat_aucs  # noqa: E402
from run_ablation_pilot import score_condition, OUT_DIR  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402

ABLATE_LAYERS = config.scale_layers([8, 11, 14, 18, 22])
M_LADDER = [8, 32, 128]
M_RANDOM = [32, 128]
M_EXPERT = 32
AUC_MIN = 0.80          # candidate bar (turn_role contrast)
GENERIC_AUC_MAX = 0.70  # feature-level RT-09 exclusion (observed_speaker)
FREQ_BAND = 0.25        # random control: activation frequency within ±25%
OOD_BOUND_NATS = 0.05
RAND_SEED = 0


def load_sae(L, device):
    from sae_lens import SAE
    if config.SAE_RELEASE.startswith("llama_scope"):
        sae_id = f"l{L}r_" + config.SAE_RELEASE.rsplit("_", 1)[1]
    else:
        sae_id = f"layer_{L}/{config.SAE_WIDTH}/{config.SAE_CANONICAL}"
    loaded = SAE.from_pretrained(config.SAE_RELEASE, sae_id, device=device)
    return loaded[0] if isinstance(loaded, tuple) else loaded


def select_features(stim, acts, device):
    """Per-layer feature selections + reference stats, per the committed rule.
    Returns (saes, selections, meta): saes = {L: sae};
    selections = {(arm, m): {L: (idx, ref_means)}}; meta = selection audit."""
    def sub(mech):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        return idx, np.array([stim[i]["label"] for i in idx])

    idx_tr, y_tr = sub("turn_role")
    idx_ob, y_ob = sub("observed_speaker")
    idx_ex, y_ex = sub("expert_persona")

    rng = np.random.default_rng(RAND_SEED)
    saes, selections, meta = {}, {}, {}
    for arm_m in [("self", m) for m in M_LADDER] + \
                 [("random", m) for m in M_RANDOM] + [("expert", M_EXPERT)]:
        selections[arm_m] = {}

    for L in ABLATE_LAYERS:
        sae = load_sae(L, device)
        saes[L] = sae
        with torch.no_grad():
            codes = sae.encode(torch.as_tensor(acts[L], device=device)
                               .to(sae.W_enc.dtype)).float().cpu().numpy()
        # ACTIVE-mean (amendment 2026-07-15): mean over occurrences where the
        # feature fires — the clamp target for conditional mean mode. A plain
        # mean over the set would force sparse features on everywhere.
        n_active = (codes > 0).sum(axis=0)
        ref_mean = codes.sum(axis=0) / np.maximum(n_active, 1)
        freq = (codes > 0).mean(axis=0)

        auc_tr = feat_aucs(codes[idx_tr], y_tr)
        auc_ob = feat_aucs(codes[idx_ob], y_ob)
        auc_ex = feat_aucs(codes[idx_ex], y_ex)

        cand = np.flatnonzero(auc_tr >= AUC_MIN)
        excluded = cand[auc_ob[cand] >= GENERIC_AUC_MAX]
        survivors = cand[auc_ob[cand] < GENERIC_AUC_MAX]
        survivors = survivors[np.argsort(-auc_tr[survivors])]
        meta[L] = {"n_candidates": int(len(cand)),
                   "n_generic_excluded": int(len(excluded)),
                   "n_survivors": int(len(survivors)),
                   "top8_auc": [round(float(a), 3) for a in auc_tr[survivors[:8]]]}
        print(f"  L{L}: {len(cand)} candidates (AUC>={AUC_MIN}), "
              f"{len(excluded)} generic-excluded, {len(survivors)} survive",
              flush=True)

        for m in M_LADDER:
            pick = survivors[:m]
            if len(pick) < m:
                print(f"    L{L} m={m}: SHORTFALL — only {len(pick)} survivors",
                      flush=True)
                meta[L][f"shortfall_m{m}"] = int(len(pick))
            selections[("self", m)][L] = (pick, ref_mean[pick])
        meta[L]["self_feature_ids_m32"] = selections[("self", 32)][L][0][:32].tolist()

        # random control: frequency within ±FREQ_BAND of the m=32 self set's
        # mean frequency (or the largest available self set if short)
        base_set = selections[("self", 32)][L][0]
        f0 = float(freq[base_set].mean()) if len(base_set) else float(freq.mean())
        pool = np.flatnonzero((freq >= f0 * (1 - FREQ_BAND)) &
                              (freq <= f0 * (1 + FREQ_BAND)))
        pool = pool[~np.isin(pool, survivors)]   # controls must not be target features
        for m in M_RANDOM:
            pick = rng.choice(pool, size=min(m, len(pool)), replace=False)
            if len(pick) < m:
                meta[L][f"random_shortfall_m{m}"] = int(len(pick))
            selections[("random", m)][L] = (pick, ref_mean[pick])

        # expert-selective control (no generic exclusion, per the addendum)
        ex_cand = np.flatnonzero(auc_ex >= AUC_MIN)
        ex_pick = ex_cand[np.argsort(-auc_ex[ex_cand])][:M_EXPERT]
        if len(ex_pick) < M_EXPERT:
            meta[L][f"expert_shortfall_m{M_EXPERT}"] = int(len(ex_pick))
        selections[("expert", M_EXPERT)][L] = (ex_pick, ref_mean[ex_pick])

        del codes
        gc.collect()
    return saes, selections, meta


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting readout residuals...", flush=True)
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)
    print("selecting SAE features (committed rule)...", flush=True)
    saes, selections, meta = select_features(stim, acts, device)
    del acts
    gc.collect()

    results = {"model_id": config.MODEL_ID, "sae_release": config.SAE_RELEASE,
               "ablate_layers": ABLATE_LAYERS, "m_ladder": M_LADDER,
               "m_random": M_RANDOM, "m_expert": M_EXPERT,
               "auc_min": AUC_MIN, "generic_auc_max": GENERIC_AUC_MAX,
               "ood_bound_nats": OOD_BOUND_NATS,
               "selection_meta": {str(k): v for k, v in meta.items()},
               "conditions": {}}
    ckpt = OUT_DIR / "sae_pilot_scores.json"

    def specs_for(key):
        return {L: (saes[L], idx, mus)
                for L, (idx, mus) in selections[key].items() if len(idx)}

    def run(tag, key, mode):
        print(f"\n=== condition: {tag} ===", flush=True)
        if key is None:
            results["conditions"][tag] = score_condition(model, tok, device, tag)
        else:
            with sae_ablation_hooks(model, specs_for(key), mode):
                results["conditions"][tag] = score_condition(model, tok, device, tag)
        ckpt.write_text(json.dumps(results, indent=2, default=str))

    run("sae_baseline", None, None)
    base_nll = results["conditions"]["sae_baseline"]["neutral_nll"]

    for m in M_LADDER:
        run(f"sae_self_mean_m{m}", ("self", m), "mean")
    for m in M_RANDOM:
        run(f"sae_random_mean_m{m}", ("random", m), "mean")
    run(f"sae_expert_mean_m{M_EXPERT}", ("expert", M_EXPERT), "mean")

    clean = [m for m in M_LADDER
             if results["conditions"][f"sae_self_mean_m{m}"]["neutral_nll"]
             - base_nll <= OOD_BOUND_NATS]
    if clean:
        m_zero = max(clean)
        results["zero_m_rule"] = f"largest OOD-clean m={m_zero} (clean set {clean})"
        run(f"sae_self_zero_m{m_zero}", ("self", m_zero), "zero")
    else:
        results["zero_m_rule"] = ("no OOD-clean m — zero cross-check skipped; "
                                  "see addendum loss condition")
        ckpt.write_text(json.dumps(results, indent=2, default=str))

    print(f"\nsaved -> {ckpt}")
    print("next: pull artifacts; judge s_responses_sae_* locally (rubric v2); "
          "read against the addendum's selection rule and loss condition.")


if __name__ == "__main__":
    main()
