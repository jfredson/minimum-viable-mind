"""Length-confound check on the context-disambiguated stimuli (found 2026-07-12).

Reconciling RT-09's first geometry pass surfaced a confound the embedding-floor
gate cannot catch: in `turn_role` and `observed_speaker` the other/asker
condition carries one extra filler exchange, so **label is perfectly predictable
from token count alone** — the classes do not even overlap in length. The floor
gate proves there is no lexical cue *at the readout token*; it says nothing
about sequence length, and a length/position representation is exactly the kind
of nobody-home signal the corpus rule says to discount.

This script quantifies three things, per mechanism / layer:
  1. label-from-token-count alone (1-feature logistic, held-out CV);
  2. how well a pure length direction (least-squares from residuals to token
     count) decodes each contrast — if ~1.0, any direction containing a length
     component cross-decodes everything;
  3. the RT-09 cross-decode (d_generic on turn_role) before vs after projecting
     the length direction out of d_generic — how much of the saturation is
     length.

It is evidence FOR a stimulus redesign (length-matched conditions), not a fix:
partialling length out post-hoc is a crude single-direction correction and does
not rescue the registered decision rule. See the findings memo / STATUS.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/check_length_confound.py
"""
from __future__ import annotations

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
from separate_self import fit_dir, projected_auc  # noqa: E402

import numpy as np  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import StratifiedKFold, cross_val_score  # noqa: E402

LAYERS = [4, 8, 10, 14, 18, 22]
MECHS = ("turn_role", "attribution", "narrative", "observed_speaker")


def label_from_length(nt: np.ndarray, y: np.ndarray) -> float:
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    return float(cross_val_score(LogisticRegression(max_iter=2000),
                                 nt.astype(float)[:, None], y,
                                 cv=skf, scoring="accuracy").mean())


def length_dir(X: np.ndarray, nt: np.ndarray) -> np.ndarray:
    t = (nt - nt.mean()) / nt.std()
    d = np.linalg.lstsq(X - X.mean(0), t, rcond=None)[0]
    return d / np.linalg.norm(d)


def main() -> None:
    stim = load_stimuli()
    strings = [render(r) for r in stim]
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers
    acts, _ = extract_last_all_layers(model, tok, strings, device, n_layers)

    nt = np.array([len(tok(s, add_special_tokens=True)["input_ids"])
                   for s in strings])
    sub = {}
    for mech in MECHS:
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        sub[mech] = (np.array(idx), np.array([stim[i]["label"] for i in idx]))

    print("1) label from token count ALONE (5-fold CV acc; 1.0 = total confound):")
    for mech, (idx, y) in sub.items():
        acc = label_from_length(nt[idx], y)
        r1 = (int(nt[idx][y == 1].min()), int(nt[idx][y == 1].max()))
        r0 = (int(nt[idx][y == 0].min()), int(nt[idx][y == 0].max()))
        print(f"   {mech:>16}: acc {acc:.3f}   len(label=1) {r1}  len(label=0) {r0}")

    print("\n2) pure length direction as a decoder of each contrast (AUC):")
    for L in LAYERS:
        cells = []
        for mech, (idx, y) in sub.items():
            X = acts[L][idx]
            dl = length_dir(X, nt[idx])
            cells.append(f"{mech[:9]} {projected_auc(X, y, dl):.2f}")
        print(f"   L{L:>2}  " + "   ".join(cells))

    print("\n3) RT-09 cross-decode gen->idx: raw vs with length projected out of d_generic:")
    idx_i, y_i = sub["turn_role"]
    idx_g, y_g = sub["observed_speaker"]
    for L in LAYERS:
        Xi, Xg = acts[L][idx_i], acts[L][idx_g]
        dg = fit_dir(Xg, y_g)
        dl = length_dir(Xg, nt[idx_g])
        dg_p = dg - (dg @ dl) * dl
        dg_p = dg_p / np.linalg.norm(dg_p)
        print(f"   L{L:>2}  raw {projected_auc(Xi, y_i, dg):.3f}   "
              f"gen⊥length {projected_auc(Xi, y_i, dg_p):.3f}")

    print("\n=> if (1) is ~1.0 the design confounds label with length and the "
          "geometry/cross-patch numbers cannot be read as referent structure; "
          "length-matched stimuli are required (see findings memo).")


if __name__ == "__main__":
    main()
