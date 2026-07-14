"""Stage 1, method (b) at subspace granularity — the convergence decision test.

The v1 single-feature SAE test was retired: on confound-controlled stimuli no
single GemmaScope feature tracked the referent (best AUC ~0.75-0.8, probe-vs-
decoder cosine ~0.15), and the pre-reg's convergence requirement stalled there.
Next-action 2 registered two ways out: run a SUBSPACE version of the SAE test on
the context design, or fall back to treating causal patching as the second
localization method. This script is the subspace version, run on the
length-matched v2 stimuli for both self-structures.

Per structure (turn_role -> C_self-index, narrative -> C_self-narrative) and
layer, two pre-committed criteria (conventions carried from the existing
instruments):

  1. **Subspace decode, held-out:** rank features by single-feature AUC on the
     TRAINING folds only (no selection leakage), keep the top K=16, fit a
     logistic head on those K codes, score the held-out fold. Report as a
     margin over the label-permutation null (same NULL_ROUNDS=5 discipline).
     Signal bar: margin >= 0.15 (SIGNAL_MIN_MARGIN convention).
  2. **Direction agreement:** the residual-stream probe direction d (as in
     separate_self.fit_dir) must project >= 0.5 of its norm onto the span of
     the selected features' decoder vectors (orthonormalized). Null: the mean
     projection fraction onto random K-subsets of active features (~sqrt(K/d)
     ~ 0.08 at K=16, d=2304), reported alongside.

**Convergence per structure** = both criteria met at some layer. If decode
passes but direction agreement fails, the SAE sees the contrast without
carving the probe's direction — the v1 failure at subspace granularity — and
the registered fallback (causal patching as the independent second method)
is the recommendation, now with evidence rather than assumption.

NB: GemmaScope SAEs are base-model-trained, applied to the IT model's residuals
(the repo's standing pt->it assumption); sandbox-scope like everything else.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/converge_sae_subspace.py
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

from mvm import config  # noqa: E402  — must precede hub imports (sets HF_HOME)
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import (  # noqa: E402
    render, load_stimuli, extract_last_all_layers,
)
from separate_self import fit_dir  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from scipy.stats import rankdata  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import StratifiedKFold  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
SAE_LAYERS = config.scale_layers([8, 12, 15, 18, 21])  # spans both structures' signal bands
TOP_K = 16
NULL_ROUNDS = 5
RAND_SUBSPACE_ROUNDS = 20
DECODE_MARGIN_MIN = 0.15           # SIGNAL_MIN_MARGIN convention
PROJ_FRACTION_MIN = 0.50           # direction-agreement bar (null ~ sqrt(K/d))
STRUCTURES = {"C_self_index": "turn_role", "C_self_narrative": "narrative"}


def feat_aucs(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Vectorized per-feature AUC (Mann-Whitney), sign-agnostic."""
    ranks = rankdata(X, axis=0)
    n1 = int(y.sum())
    n0 = len(y) - n1
    u = ranks[y == 1].sum(axis=0) - n1 * (n1 + 1) / 2
    auc = u / (n1 * n0)
    return np.maximum(auc, 1 - auc)


def subspace_cv_acc(codes: np.ndarray, y: np.ndarray, seed: int = 0) -> float:
    """Held-out accuracy with feature selection INSIDE each training fold."""
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    accs = []
    for tr, te in skf.split(codes, y):
        top = np.argsort(-feat_aucs(codes[tr], y[tr]))[:TOP_K]
        Xtr, Xte = codes[tr][:, top], codes[te][:, top]
        sc = StandardScaler().fit(Xtr)
        clf = LogisticRegression(max_iter=2000, class_weight="balanced")
        clf.fit(sc.transform(Xtr), y[tr])
        accs.append(float((clf.predict(sc.transform(Xte)) == y[te]).mean()))
    return float(np.mean(accs))


def decode_margin(codes: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    real = subspace_cv_acc(codes, y)
    nulls = []
    for s in range(NULL_ROUNDS):
        yp = y.copy()
        np.random.default_rng(100 + s).shuffle(yp)
        nulls.append(subspace_cv_acc(codes, yp, seed=s))
    null = float(np.mean(nulls))
    return real, null, real - null


def proj_fraction(d: np.ndarray, W_rows: np.ndarray) -> float:
    """Fraction of ||d|| captured by the span of W_rows (rows = directions)."""
    q, _ = np.linalg.qr(W_rows.T)          # [d_model, k] orthonormal basis
    return float(np.linalg.norm(q.T @ d) / np.linalg.norm(d))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting readout residuals...")
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)

    subsets = {}
    for name, mech in STRUCTURES.items():
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        subsets[name] = (idx, np.array([stim[i]["label"] for i in idx]))

    from sae_lens import SAE  # deferred so model load isn't blocked on SAELens

    rng = np.random.default_rng(0)
    results = {name: [] for name in STRUCTURES}
    print(f"\n{'layer':>5} {'structure':>18}  {'decode':>13}  {'proj_frac':>9} "
          f"{'proj_null':>9}  criteria")
    for L in SAE_LAYERS:
        if config.SAE_RELEASE.startswith("llama_scope"):
            # Llama Scope id convention: l{L}r_8x (verified 2026-07-13)
            sae_id = f"l{L}r_" + config.SAE_RELEASE.rsplit("_", 1)[1]
        else:
            sae_id = f"layer_{L}/{config.SAE_WIDTH}/{config.SAE_CANONICAL}"
        loaded = SAE.from_pretrained(config.SAE_RELEASE, sae_id, device=device)
        sae = loaded[0] if isinstance(loaded, tuple) else loaded
        W_dec = sae.W_dec.detach().float().cpu().numpy()   # [d_sae, d_model]

        for name in STRUCTURES:
            idx, y = subsets[name]
            X = acts[L][idx]
            with torch.no_grad():
                codes = sae.encode(torch.as_tensor(X, device=device)
                                   .to(sae.W_enc.dtype)).float().cpu().numpy()

            real, null, margin = decode_margin(codes, y)

            # direction agreement: probe direction vs selected decoder span
            d = fit_dir(X, y)
            top = np.argsort(-feat_aucs(codes, y))[:TOP_K]
            frac = proj_fraction(d, W_dec[top])
            active = np.flatnonzero((codes > 0).any(axis=0))
            null_fracs = []
            for _ in range(RAND_SUBSPACE_ROUNDS):
                pick = rng.choice(active, size=min(TOP_K, len(active)),
                                  replace=False)
                null_fracs.append(proj_fraction(d, W_dec[pick]))
            frac_null = float(np.mean(null_fracs))

            ok_decode = margin >= DECODE_MARGIN_MIN
            ok_proj = frac >= PROJ_FRACTION_MIN
            results[name].append({
                "layer": L, "decode_real": real, "decode_null": null,
                "decode_margin": margin, "proj_fraction": frac,
                "proj_fraction_null": frac_null,
                "top_features": [int(f) for f in top],
                "decode_ok": bool(ok_decode), "proj_ok": bool(ok_proj),
                "converged": bool(ok_decode and ok_proj),
            })
            print(f"{L:>5} {name:>18}  {real:.2f}/{null:.2f} "
                  f"({margin:+.2f})  {frac:>9.3f} {frac_null:>9.3f}  "
                  f"decode {'OK' if ok_decode else '--'} / "
                  f"dir {'OK' if ok_proj else '--'}"
                  + ("  << CONVERGED" if ok_decode and ok_proj else ""))

        del sae, W_dec
        gc.collect()
        if device == "mps":
            torch.mps.empty_cache()

    print()
    verdicts = {}
    for name in STRUCTURES:
        conv = [r["layer"] for r in results[name] if r["converged"]]
        dec = [r["layer"] for r in results[name] if r["decode_ok"]]
        if conv:
            v = f"CONVERGED at layers {conv} — method (b) agrees at subspace granularity"
        elif dec:
            v = (f"DECODES (layers {dec}) BUT DIRECTION DISAGREES — the SAE sees "
                 "the contrast without carving the probe's direction (the v1 "
                 "failure at subspace granularity); registered fallback applies: "
                 "causal patching stands as the second localization method")
        else:
            v = ("NO SUBSPACE SIGNAL — method (b) does not see this contrast "
                 "here; registered fallback applies")
        verdicts[name] = v
        print(f"{name}: {v}")

    out = {
        "model": config.MODEL_ID,
        "sae_release": config.SAE_RELEASE, "sae_width": config.SAE_WIDTH,
        "stimuli": "context_self_speaker_stimuli.jsonl (length-matched v2)",
        "criteria": {"top_k": TOP_K, "decode_margin_min": DECODE_MARGIN_MIN,
                     "proj_fraction_min": PROJ_FRACTION_MIN,
                     "selection": "inside training folds (no selection leakage)",
                     "null_rounds": NULL_ROUNDS,
                     "rand_subspace_rounds": RAND_SUBSPACE_ROUNDS},
        "layers": SAE_LAYERS,
        "by_structure": results,
        "verdicts": verdicts,
        "caveats": "GemmaScope SAEs are base-trained, applied to IT residuals "
                   "(standing pt->it assumption); n=48/structure; probe "
                   "direction from a full-data fit (decode is held-out); "
                   "sandbox scope — the registered substrate uses Llama Scope, "
                   "so method (b) must be re-validated there regardless.",
    }
    (OUT_DIR / "converge_sae_subspace.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'converge_sae_subspace.json'}")


if __name__ == "__main__":
    main()
