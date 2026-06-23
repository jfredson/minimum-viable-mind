"""Stage 1 localization, method (a): linear probes for self-as-speaker.

Trains a linear probe to read, from the residual stream, whether the first-person
speaker of a sentence is *this system* (the assistant/model itself) versus not.
The headline contrast is **self vs. human-first-person**: both classes say "I",
so a probe that separates them must key on *who* "I" refers to, not on
first-personness or on AI-topic vocabulary. A broader **self vs. all** contrast
(adding third-person-about-AI and neutral sentences) is reported alongside.

Output per layer: cross-validated probe accuracy. The peak layer's probe weight
vector is saved as a candidate self-locating direction (C_self) for the later
directional-ablation step. This is the first of two required localization methods
(the other is SAE features); they must converge or the experiment is
inconclusive by construction (see pre-registration).

Status: PILOT. The stimulus set is small and hand-built to validate the pipeline
and get a first localization signal; the matched-control construction and the
registered probe set come later.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/localize_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.activations import resid_post  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import StratifiedKFold, cross_val_score  # noqa: E402
from sklearn.pipeline import make_pipeline  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

STIMULI = Path(__file__).resolve().parent / "probes" / "self_speaker_stimuli.jsonl"
OUT_DIR = config.ARTIFACTS_DIR / "stage1"
CHUNK = 16
N_SPLITS = 5
SEED = 0


def load_stimuli() -> list[dict]:
    with STIMULI.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def extract_all_layers(model, tok, texts, device, n_layers) -> dict[int, np.ndarray]:
    """resid_post at the last token for every layer, as float32 numpy arrays."""
    layers = list(range(n_layers))
    parts: dict[int, list] = {L: [] for L in layers}
    for i in range(0, len(texts), CHUNK):
        feats = resid_post(model, tok, texts[i : i + CHUNK], device, layers)
        for L in layers:
            parts[L].append(feats[L].float().cpu().numpy())
    return {L: np.concatenate(parts[L], axis=0) for L in layers}


def cv_accuracy(X: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    clf = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced"),
    )
    skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    scores = cross_val_score(clf, X, y, cv=skf, scoring="accuracy")
    return float(scores.mean()), float(scores.std())


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    kinds = {s["id"]: s["kind"] for s in stim}
    texts = [s["text"] for s in stim]
    y_all = np.array([s["label"] for s in stim])
    is_primary = np.array(
        [kinds[s["id"]] in ("self", "other_first_person") for s in stim]
    )
    print(f"{len(stim)} stimuli  "
          f"(self {sum(y_all == 1)}, non-self {sum(y_all == 0)}; "
          f"primary self-vs-other n={int(is_primary.sum())})\n")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("extracting residual-stream activations for all layers...")
    acts = extract_all_layers(model, tok, texts, device, n_layers)

    # chance accuracy for each contrast (majority class, balanced CV uses acc)
    print(f"\n{'layer':>5}  {'self-vs-other':>14}  {'self-vs-all':>12}")
    rows = []
    best = (-1.0, None)  # (primary acc, layer)
    for L in range(n_layers):
        Xp, yp = acts[L][is_primary], y_all[is_primary]
        Xa, ya = acts[L], y_all
        acc_p, sd_p = cv_accuracy(Xp, yp)
        acc_a, sd_a = cv_accuracy(Xa, ya)
        rows.append({"layer": L, "self_vs_other": acc_p, "self_vs_other_sd": sd_p,
                     "self_vs_all": acc_a, "self_vs_all_sd": sd_a})
        mark = ""
        if acc_p > best[0]:
            best = (acc_p, L)
            mark = ""
        print(f"{L:>5}  {acc_p:>6.3f} ±{sd_p:4.3f}  {acc_a:>6.3f} ±{sd_a:4.3f}")

    peak_layer = best[1]
    print(f"\npeak self-vs-other layer: {peak_layer}  (acc {best[0]:.3f})")

    # Fit the final probe on ALL self-vs-other data at the peak layer; save the
    # standardized weight direction as the candidate C_self.
    Xp, yp = acts[peak_layer][is_primary], y_all[is_primary]
    scaler = StandardScaler().fit(Xp)
    clf = LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced")
    clf.fit(scaler.transform(Xp), yp)
    # Map the probe direction back to raw residual space (undo standardization),
    # then unit-normalize — this is the direction we'll project out at ablation.
    direction = clf.coef_[0] / scaler.scale_
    direction = direction / np.linalg.norm(direction)

    np.save(OUT_DIR / f"c_self_direction_layer{peak_layer}.npy", direction)
    (OUT_DIR / "probe_self_speaker.json").write_text(json.dumps({
        "model": config.MODEL_ID,
        "n_stimuli": len(stim),
        "n_splits": N_SPLITS,
        "peak_layer": peak_layer,
        "peak_self_vs_other_acc": best[0],
        "by_layer": rows,
        "direction_file": f"c_self_direction_layer{peak_layer}.npy",
        "note": "PILOT probe set; self-vs-other is the headline contrast.",
    }, indent=2))
    print(f"saved C_self direction (layer {peak_layer}) and per-layer accuracies "
          f"to {OUT_DIR}")


if __name__ == "__main__":
    main()
