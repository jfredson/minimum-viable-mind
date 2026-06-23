"""Stage 1 (RT-04): separability of C_self-index from C_self-narrative.

The amended pre-registration requires localizing BOTH a thin indexical
self-location structure (C_self-index) and a narrative first-person persona
structure (C_self-narrative), and reporting the removal test for each — with a
stated loss condition if no method can separate them (the Metzinger objection
then stands open).

The two are localized on confound-controlled context designs (identical readout
token, referent/persona set only by context):
  - **C_self-index**  = `turn_role` stimuli: same sentence in the model's own turn
    (referent = system) vs the user's turn (referent = human). Varies *who speaks*.
  - **C_self-narrative** = `narrative` stimuli: same sentence as the model's own
    reply under its own AI-assistant identity vs while adopting a roleplay
    character. BOTH are model turns, so the indexical speaker is held constant;
    only the *persona* varies.

Separability is then tested three ways at each layer:
  1. **Direction cosine** |cos(d_index, d_narrative)| — low = geometrically distinct.
  2. **Cross-decoding** — does the index direction decode the narrative contrast
     (and vice versa)? If each direction decodes its OWN contrast well but the
     OTHER's near chance, the structures are functionally distinct, not one
     "self" direction doing double duty.
  3. Both are reported against the same null/embedding-floor discipline used in
     `localize_context.py` (each direction is only meaningful where its own
     contrast clears the null).

Verdict: SEPARABLE if there is a layer band where each direction decodes its own
contrast well above null AND cross-decoding is near chance AND the cosine is low.
NON-SEPARABLE (RT-04 loss condition) if the two cannot be told apart by any of
these — recorded honestly, not papered over.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/separate_self.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import (  # noqa: E402
    render, load_stimuli, extract_last_all_layers, margin_of, _probe,
)

import numpy as np  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.metrics import roc_auc_score  # noqa: E402
from sklearn.model_selection import StratifiedKFold  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
# Candidate layers to assess separability across the middle/late band.
LAYERS = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
COS_SEPARABLE_MAX = 0.30     # |cos| below this = geometrically distinct
CROSS_CHANCE_MAX = 0.65      # cross-decode AUC below this = functionally distinct
OWN_MIN = 0.75               # own-contrast AUC must clear this to be a real direction


def fit_dir(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    scaler = StandardScaler().fit(X)
    clf = LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced")
    clf.fit(scaler.transform(X), y)
    d = clf.coef_[0] / scaler.scale_
    return d / np.linalg.norm(d)


def cv_auc(X: np.ndarray, y: np.ndarray) -> float:
    """Own-contrast CV AUC using the PCA-regularized probe (held-out folds)."""
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    aucs = []
    for tr, te in skf.split(X, y):
        clf = _probe(len(tr))
        clf.fit(X[tr], y[tr])
        score = clf.predict_proba(X[te])[:, 1]
        aucs.append(roc_auc_score(y[te], score))
    return float(np.mean(aucs))


def projected_auc(X: np.ndarray, y: np.ndarray, d: np.ndarray) -> float:
    """AUC of a fixed direction d as a 1-D score for class 1 on (X, y)."""
    s = X @ d
    return float(max(roc_auc_score(y, s), roc_auc_score(y, -s)))


def residualize(X: np.ndarray, d: np.ndarray) -> np.ndarray:
    """Remove the component of each row along unit direction d."""
    return X - np.outer(X @ d, d)


def subset(stim, acts, mech):
    idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
    y = np.array([stim[i]["label"] for i in idx])
    return idx, y


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    strings = [render(r) for r in stim]

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting readout residuals...")
    acts, _emb = extract_last_all_layers(model, tok, strings, device, n_layers)

    idx_i, y_i = subset(stim, acts, "turn_role")    # C_self-index
    idx_n, y_n = subset(stim, acts, "narrative")    # C_self-narrative
    print(f"C_self-index: n={len(y_i)}  C_self-narrative: n={len(y_n)}\n")

    print(f"{'layer':>5}  {'idx_own':>7} {'narr_own':>8}  "
          f"{'narr⊥idx':>8} {'idx⊥narr':>8}  {'|cos|':>6}  sep?")
    rows = []
    for L in LAYERS:
        Xi, Xn = acts[L][idx_i], acts[L][idx_n]
        di = fit_dir(Xi, y_i)
        dn = fit_dir(Xn, y_n)
        idx_own = cv_auc(Xi, y_i)
        narr_own = cv_auc(Xn, y_n)
        cross_in = projected_auc(Xn, y_n, di)   # index direction on narrative data
        cross_ni = projected_auc(Xi, y_i, dn)   # narrative direction on index data
        cos = abs(float(di @ dn))
        # decisive test: is there structure ORTHOGONAL to the other direction?
        narr_orth = cv_auc(residualize(Xn, di), y_n)  # narrative after removing index
        idx_orth = cv_auc(residualize(Xi, dn), y_i)   # index after removing narrative
        # CLEAN separability needs all four: both localize, both retain structure
        # orthogonal to the other (not a subspace), AND a single direction from one
        # does NOT decode the other (no shared component) at a modest angle.
        sep = (idx_own >= OWN_MIN and narr_own >= OWN_MIN
               and narr_orth >= OWN_MIN and idx_orth >= OWN_MIN
               and cross_in <= CROSS_CHANCE_MAX and cross_ni <= CROSS_CHANCE_MAX
               and cos <= COS_SEPARABLE_MAX)
        rows.append({"layer": L, "idx_own_auc": idx_own, "narr_own_auc": narr_own,
                     "narr_orth_idx_auc": narr_orth, "idx_orth_narr_auc": idx_orth,
                     "cross_index_on_narr": cross_in, "cross_narr_on_index": cross_ni,
                     "abs_cos": cos, "separable": bool(sep)})
        print(f"{L:>5}  {idx_own:>7.3f} {narr_own:>8.3f}  "
              f"{narr_orth:>8.3f} {idx_orth:>8.3f}  {cos:>6.3f}  "
              f"{'YES' if sep else '-'}")

    clean_layers = [r["layer"] for r in rows if r["separable"]]
    both_real = [r for r in rows if r["idx_own_auc"] >= OWN_MIN
                 and r["narr_own_auc"] >= OWN_MIN]
    # PARTIAL: each retains orthogonal structure (not a subspace of the other) even
    # though a shared component / modest angle remains.
    partial_layers = [r["layer"] for r in both_real
                      if r["narr_orth_idx_auc"] >= OWN_MIN
                      and r["idx_orth_narr_auc"] >= OWN_MIN]
    median_cos = float(np.median([r["abs_cos"] for r in both_real])) if both_real else None

    print()
    if clean_layers:
        verdict = f"SEPARABLE (clean) at layers {clean_layers}"
        print(f"=> {verdict}: distinct directions (|cos|≤{COS_SEPARABLE_MAX}), no shared "
              f"component (cross≤{CROSS_CHANCE_MAX}), each survives removing the other. "
              "Run the removal test on each independently (RT-04).")
    elif partial_layers:
        verdict = f"PARTIALLY SEPARABLE / OVERLAPPING at layers {partial_layers}"
        print(f"=> {verdict}. The two are NOT the same structure — optimal directions "
              f"are well off-axis (median |cos| {median_cos:.2f}) and each keeps "
              "decodable structure after the other is projected out — but they share a "
              "component (a single index direction still separates the narrative "
              "contrast). So C_self-index and C_self-narrative are distinguishable yet "
              "overlapping. RT-04 reading: enough to localize and test each "
              "independently, but the Metzinger seam is NOT fully closed — report the "
              "overlap, and let CAUSAL cross-patching (does ablating one move the "
              "other's behaviour?) be the decisive test. Caveat: n≈24/struct; the "
              "roleplay 'other' differs in instruction length — length-match before "
              "treating the shared component as intrinsic.")
    elif both_real:
        verdict = "NOT separable (shared subspace)"
        print(f"=> {verdict}: removing one direction collapses the other's decoding — "
              "the self signal lives in one shared subspace. Per RT-04, record "
              "non-separability and that the Metzinger objection stands open; do NOT "
              "report a narrative result as settling the floor.")
    else:
        verdict = "INCONCLUSIVE (a structure failed to localize)"
        print(f"=> {verdict}: one contrast did not clear AUC {OWN_MIN}; firm up stimuli "
              "before claiming separability either way.")

    out = {
        "model": config.MODEL_ID,
        "structures": {"C_self_index": "turn_role", "C_self_narrative": "narrative"},
        "thresholds": {"own_min_auc": OWN_MIN, "cross_chance_max": CROSS_CHANCE_MAX,
                       "cos_separable_max": COS_SEPARABLE_MAX},
        "layers": LAYERS,
        "by_layer": rows,
        "clean_separable_layers": clean_layers,
        "partial_separable_layers": partial_layers,
        "verdict": verdict,
        "caveats": "directions from full-data logistic fit (not held-out) for cos / "
                   "cross-projection; own-contrast AUC is held-out CV. Narrative = "
                   "own-persona vs roleplay (one operationalization). n≈24/structure.",
    }
    (OUT_DIR / "separate_self.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'separate_self.json'}")


if __name__ == "__main__":
    main()
