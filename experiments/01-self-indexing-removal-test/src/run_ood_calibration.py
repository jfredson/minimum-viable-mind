"""RT-07 OOD-bound calibration run (thresholds.md Pass 5, registered 2026-07-17).

NOT the registered removal test and NOT a behavioural pilot: no batteries, no
S judging. This run produces the two null distributions Pass 5 commits to,
plus the registered rank-k conditions' long-generation scores (never
collected) and a Δnll reproduction of the dose-response table:

  1. **Δnll null, per k ∈ {4, 8, 16}:** 20 random rank-k orthonormal bases
     (seeds 0–19), mean-ablated at the registered layers through the same
     `ablation_hooks` code path as the index-residual conditions — reference
     means derived on the same turn_role stimulus activations; only the basis
     is randomized. Bound_k = 95th percentile (linear interpolation).
  2. **Δrep-4 null, same 20 ablations per k** (one calibration yields both
     bounds): greedy 256-token plain-text continuation of the 16 RT-07
     neutral-corpus sentences (no chat template — the probe targets the
     language manifold, same semantics as `neutral_nll`; pinned here before
     running). rep-4 = 1 − distinct/total token 4-grams of the continuation,
     averaged over prompts; Δrep-4 is over the baseline condition.
  3. **Registered conditions re-scored on both probes** (idxres mean
     k ∈ {1,4,8,16}, expert mean k ∈ {4,16}, idxres directional k=1):
     Δnll is a reproduction check against `prelock-findings.md` §b; rep-4 is
     new (the long-gen gate applies to any re-admitted condition).

Verdicts are reported under BOTH the old 0.05-absolute bound and the
recalibrated Bound_k, per Pass 5's no-silent-replacement clause. The bound
binds whichever way it comes out; nothing in this script selects a strength.

Cloud bench: MVM_MODEL=allenai/Llama-3.1-Tulu-3-8B-SFT MVM_N_LAYERS=32.
    python experiments/01-self-indexing-removal-test/src/run_ood_calibration.py
Sandbox smoke (instrument check only): add --smoke (1 seed, k=4 only,
2 prompts x 32 tokens; numbers meaningless by design).
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
    NEUTRAL_CORPUS, _orthonormalize, ablation_hooks, neutral_nll,
)
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import render, load_stimuli, extract_last_all_layers  # noqa: E402
from run_ablation_pilot import fit_structures  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "prelock"
ABLATE_LAYERS = config.scale_layers([8, 11, 14, 18, 22])
NULL_KS = [4, 8, 16]
N_SEEDS = 20          # seeds 0..19, committed in Pass 5
QUANTILE = 0.95
OLD_BOUND_NATS = 0.05
GEN_TOKENS = 256
NGRAM = 4


def random_subspaces(seed: int, k: int, d_model: int,
                     ref_acts: dict[int, np.ndarray],
                     ) -> dict[int, list[tuple[np.ndarray, float]]]:
    """Random rank-k orthonormal basis per layer, reference means derived on
    the same stimulus activations as the registered conditions (identical
    semantics to `fit_layer_subspace`'s (X @ b).mean(); only the basis is
    random). One rng per (seed, k); per-layer draws consumed in layer order."""
    rng = np.random.default_rng(seed)
    out = {}
    for L in ABLATE_LAYERS:
        basis = _orthonormalize(list(rng.standard_normal((k, d_model))))
        if len(basis) != k:
            raise ValueError(f"seed {seed} layer {L}: degenerate random basis")
        X = ref_acts[L]
        out[L] = [(b.astype(np.float32), float((X @ b).mean())) for b in basis]
    return out


@torch.no_grad()
def longgen_rep(model, tok, device, n_prompts: int, max_new: int) -> dict:
    """Greedy plain-text continuation of the neutral corpus; token-level
    rep-4 of the continuation (pad/eos-stripped), averaged over prompts."""
    reps, lens = [], []
    for text in NEUTRAL_CORPUS[:n_prompts]:
        enc = tok(text, return_tensors="pt", add_special_tokens=True).to(device)
        out = model.generate(**enc, max_new_tokens=max_new, do_sample=False,
                             pad_token_id=tok.pad_token_id)
        gen = out[0][enc["input_ids"].shape[1]:].tolist()
        drop = {tok.pad_token_id, tok.eos_token_id}
        gen = [t for t in gen if t not in drop]
        lens.append(len(gen))
        if len(gen) < NGRAM:
            reps.append(0.0)
            continue
        grams = [tuple(gen[i:i + NGRAM]) for i in range(len(gen) - NGRAM + 1)]
        reps.append(1.0 - len(set(grams)) / len(grams))
    return {"rep4": float(np.mean(reps)), "rep4_per_prompt": reps,
            "gen_lens": lens}


def main() -> None:
    smoke = "--smoke" in sys.argv
    n_seeds = 1 if smoke else N_SEEDS
    null_ks = [4] if smoke else NULL_KS
    n_prompts = 2 if smoke else len(NEUTRAL_CORPUS)
    max_new = 32 if smoke else GEN_TOKENS

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers
    d_model = model.config.hidden_size

    print("extracting activations for subspace fitting...", flush=True)
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)
    structures = fit_structures(stim, acts)
    # Reference-mean activations for the null bases: the turn_role stimuli,
    # exactly the set the index-residual conditions' means are derived on.
    idx_tr = [i for i, r in enumerate(stim) if r["mechanism"] == "turn_role"]
    ref_acts = {L: acts[L][idx_tr] for L in ABLATE_LAYERS}
    del acts

    results = {"model_id": config.MODEL_ID, "smoke": smoke,
               "ablate_layers": ABLATE_LAYERS, "null_ks": null_ks,
               "n_seeds": n_seeds, "quantile": QUANTILE,
               "old_bound_nats": OLD_BOUND_NATS,
               "gen_tokens": max_new, "n_prompts": n_prompts,
               "conditions": {}, "null": {}}
    ckpt = OUT_DIR / ("ood_calibration_smoke.json" if smoke
                      else "ood_calibration.json")

    def score(tag, dirs, mode):
        t0 = time.time()
        if dirs is None:
            nll = neutral_nll(model, tok, device)
            rep = longgen_rep(model, tok, device, n_prompts, max_new)
        else:
            with ablation_hooks(model, dirs, mode):
                nll = neutral_nll(model, tok, device)
                rep = longgen_rep(model, tok, device, n_prompts, max_new)
        row = {"neutral_nll": nll, **rep}
        print(f"  [{tag}] nll {nll:.4f}  rep4 {row['rep4']:.4f}  "
              f"({time.time() - t0:.0f}s)", flush=True)
        return row

    print("\n=== baseline ===", flush=True)
    results["conditions"]["baseline"] = score("baseline", None, None)
    base = results["conditions"]["baseline"]
    ckpt.write_text(json.dumps(results, indent=2))

    print("\n=== registered conditions (repro + long-gen) ===", flush=True)
    reg = ([("idxres_mean_k%d" % k, ("index_residual", k), "mean")
            for k in [1, 4, 8, 16]] +
           [("expert_mean_k%d" % k, ("expert", k), "mean") for k in [4, 16]] +
           [("idxres_directional_k1", ("index_residual", 1), "directional")])
    for tag, key, mode in reg:
        results["conditions"][tag] = score(tag, structures[key], mode)
        ckpt.write_text(json.dumps(results, indent=2))

    print("\n=== null distributions ===", flush=True)
    for k in null_ks:
        rows = []
        for seed in range(n_seeds):
            dirs = random_subspaces(seed, k, d_model, ref_acts)
            row = score(f"null_k{k}_seed{seed}", dirs, "mean")
            row["seed"] = seed
            rows.append(row)
            results["null"][f"k{k}"] = rows
            ckpt.write_text(json.dumps(results, indent=2))

    # Bounds + both-bounds verdicts (report-only; the bound binds as computed).
    summary = {}
    for k in null_ks:
        rows = results["null"][f"k{k}"]
        dnll = [r["neutral_nll"] - base["neutral_nll"] for r in rows]
        drep = [r["rep4"] - base["rep4"] for r in rows]
        summary[f"k{k}"] = {
            "bound_nll_nats": float(np.quantile(dnll, QUANTILE)),
            "bound_rep4": float(np.quantile(drep, QUANTILE)),
            "null_dnll": dnll, "null_drep4": drep,
        }
    results["bounds"] = summary

    def mode_of(tag: str) -> str:
        return "directional" if "directional" in tag else "mean"

    verdicts = {}
    for tag, row in results["conditions"].items():
        if tag == "baseline":
            continue
        dnll = row["neutral_nll"] - base["neutral_nll"]
        drep = row["rep4"] - base["rep4"]
        k = int(tag.rsplit("_k", 1)[1])
        b = summary.get(f"k{k}")
        if b is not None and mode_of(tag) == "mean":
            recal = {"nll_clean": dnll <= b["bound_nll_nats"],
                     "longgen_clean": drep <= b["bound_rep4"]}
        else:
            recal = {"nll_clean": dnll <= OLD_BOUND_NATS,
                     "longgen_clean": None,
                     "note": "keeps 0.05 absolute per Pass 5 (k=1/directional)"}
        verdicts[tag] = {"dnll": dnll, "drep4": drep,
                         "old_bound_clean": dnll <= OLD_BOUND_NATS,
                         "recalibrated": recal}
    results["verdicts"] = verdicts
    ckpt.write_text(json.dumps(results, indent=2))

    print(f"\nsaved -> {ckpt}")
    for k, b in summary.items():
        print(f"  {k}: bound_nll {b['bound_nll_nats']:+.4f} nats, "
              f"bound_rep4 {b['bound_rep4']:+.4f}")
    print("next: findings memo applies Pass 5 (both-bounds reporting; "
          "if re-admitted, spec §b selection re-applies on the existing "
          "dose-response data).")


if __name__ == "__main__":
    main()
