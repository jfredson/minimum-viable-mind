"""Stage 1 localization, method (b): SAE features that fire on self-as-speaker.

The second of the two required localization methods (the first is linear probes,
`localize_probe.py`). Instead of training a probe, we read GemmaScope sparse-
autoencoder features off the residual stream and ask which individual features
fire *selectively* when the first-person speaker is **this system** versus a
human persona. The headline contrast is the same as the probe's: **self vs.
other_first_person** — both classes say "I", so a feature that separates them is
keying on *who* "I" refers to, not on first-personness as such.

Per feature we report:
  - f_self  : fraction of self stimuli for which the feature is active (>0)
  - f_other : fraction of human-persona stimuli for which it is active
  - mean_self / mean_other : mean activation magnitude per class
  - auc     : how well that single feature alone separates the two classes

A feature is "self-selective" when it fires on most self stimuli and rarely on
the human controls (f_self high, f_other low). The per-layer headline is the
best single self-selective feature's AUC — directly comparable to the probe's
per-layer accuracy, which is what the convergence check (next action) needs. We
deliberately do NOT fit a multi-feature classifier on the codes: with ~16k
features and ~40 stimuli it would hit ceiling by overfitting and say nothing.

The two methods must converge on *where* (and ideally *what*) C_self is, or the
experiment is inconclusive by construction (see pre-registration, Confounds:
localization error).

Status: PILOT — same small, hand-built stimulus set as the probe, sharing its
caveats: near-ceiling separability is easy at this size, and the self/human
classes differ in topic vocabulary, so a "self feature" found here may be an
AI-topic feature rather than a self-as-referent feature. Tightening the stimuli
to matched content (varying only the referent of "I") is the next step after
convergence is assessed; don't over-read these numbers.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/localize_sae.py
"""
from __future__ import annotations

import gc
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
from sklearn.metrics import roc_auc_score  # noqa: E402

STIMULI = Path(__file__).resolve().parent / "probes" / "self_speaker_stimuli.jsonl"
OUT_DIR = config.ARTIFACTS_DIR / "stage1"
PROBE_JSON = OUT_DIR / "probe_self_speaker.json"

# Layers to load an SAE for. Focused on the probe's strong band (peak 8, strong
# self-vs-other 8-13) plus a couple of anchor layers above/below, to keep SAE
# downloads/memory modest on the 16GB Air while still covering the convergence
# question. Widen this on the larger machine.
SAE_LAYERS = [6, 8, 9, 10, 11, 12, 13, 15]

CHUNK = 16
# A feature counts as "self-selective" when it fires on most self stimuli and
# rarely on the human-persona controls. Pilot thresholds; reported, not load-bearing.
SEL_F_SELF_MIN = 0.75
SEL_F_OTHER_MAX = 0.25
TOP_K = 15  # features reported per layer


def load_stimuli() -> list[dict]:
    with STIMULI.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def encode_layer(model, tok, texts, device, sae, layer,
                 use_chat_template: bool = False) -> np.ndarray:
    """SAE feature codes at the last token for every stimulus, [n_stim, d_sae]."""
    parts = []
    for i in range(0, len(texts), CHUNK):
        feats = resid_post(model, tok, texts[i : i + CHUNK], device, [layer],
                           use_chat_template=use_chat_template)
        acts = feats[layer].to(sae.W_enc.dtype)
        with torch.no_grad():
            codes = sae.encode(acts)
        parts.append(codes.detach().float().cpu().numpy())
    return np.concatenate(parts, axis=0)


def single_feature_auc(col: np.ndarray, y: np.ndarray) -> float:
    """AUC of one feature's activation as a score for class 1 (self)."""
    if np.allclose(col, col[0]):
        return 0.5
    return float(roc_auc_score(y, col))


def selectivity_table(codes: np.ndarray, self_mask: np.ndarray,
                      neg_mask: np.ndarray) -> list[dict]:
    """Per-feature self-vs-(neg) selectivity for features active in either class.

    `neg_mask` selects the contrast's negative class (human personas for the
    headline; all non-self for the secondary view). Returns rows sorted by
    selectivity = f_self - f_neg, descending, restricted to features that ever
    fire — so the table is over the model's actual vocabulary, not 16k zeros.
    """
    self_codes = codes[self_mask]
    neg_codes = codes[neg_mask]
    active = (self_codes > 0).any(axis=0) | (neg_codes > 0).any(axis=0)
    idxs = np.flatnonzero(active)

    f_self = (self_codes[:, idxs] > 0).mean(axis=0)
    f_neg = (neg_codes[:, idxs] > 0).mean(axis=0)
    mean_self = self_codes[:, idxs].mean(axis=0)
    mean_neg = neg_codes[:, idxs].mean(axis=0)
    sel = f_self - f_neg

    y = np.concatenate([np.ones(self_mask.sum()), np.zeros(neg_mask.sum())])
    stacked = np.concatenate([self_codes[:, idxs], neg_codes[:, idxs]], axis=0)

    rows = []
    for j, fi in enumerate(idxs):
        rows.append({
            "feature": int(fi),
            "f_self": float(f_self[j]),
            "f_neg": float(f_neg[j]),
            "mean_self": float(mean_self[j]),
            "mean_neg": float(mean_neg[j]),
            "selectivity": float(sel[j]),
            "auc": single_feature_auc(stacked[:, j], y),
        })
    rows.sort(key=lambda r: (r["selectivity"], r["auc"]), reverse=True)
    return rows


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    texts = [s["text"] for s in stim]
    kind = np.array([s["kind"] for s in stim])
    label = np.array([s["label"] for s in stim])

    self_mask = kind == "self"
    other_mask = kind == "other_first_person"   # headline negative: human personas
    nonself_mask = label == 0                    # secondary negative: all non-self
    print(f"{len(stim)} stimuli  (self {self_mask.sum()}, "
          f"human-persona {other_mask.sum()}, all non-self {nonself_mask.sum()})\n")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)

    from sae_lens import SAE  # imported here so model load isn't blocked on SAELens

    print(f"{'layer':>5}  {'best self feat':>14}  {'f_self':>7} {'f_neg':>6} "
          f"{'auc':>6}  {'#selective':>10}")
    by_layer = []
    best = (-1.0, None)  # (best-feature auc on headline contrast, layer)

    for L in SAE_LAYERS:
        sae_id = f"layer_{L}/{config.SAE_WIDTH}/{config.SAE_CANONICAL}"
        loaded = SAE.from_pretrained(config.SAE_RELEASE, sae_id, device=device)
        sae = loaded[0] if isinstance(loaded, tuple) else loaded

        codes = encode_layer(model, tok, texts, device, sae, L)

        head = selectivity_table(codes, self_mask, other_mask)       # headline
        sva = selectivity_table(codes, self_mask, nonself_mask)      # self-vs-all
        n_selective = sum(
            1 for r in head
            if r["f_self"] >= SEL_F_SELF_MIN and r["f_neg"] <= SEL_F_OTHER_MAX
        )
        top = head[0]
        # rank by AUC too, for the convergence headline (best separator)
        best_auc_row = max(head, key=lambda r: r["auc"])

        by_layer.append({
            "layer": L,
            "best_selectivity_feature": top,
            "best_auc_feature": best_auc_row,
            "n_selective_features": n_selective,
            "top_self_vs_human": head[:TOP_K],
            "top_self_vs_all": sva[:TOP_K],
        })
        if best_auc_row["auc"] > best[0]:
            best = (best_auc_row["auc"], L)

        print(f"{L:>5}  {top['feature']:>14}  {top['f_self']:>7.2f} "
              f"{top['f_neg']:>6.2f} {best_auc_row['auc']:>6.3f}  {n_selective:>10}")

        del sae, codes
        gc.collect()
        if device == "mps":
            torch.mps.empty_cache()

    peak_layer = best[1]
    print(f"\npeak SAE layer (best single-feature AUC, self-vs-human): "
          f"{peak_layer}  (auc {best[0]:.3f})")

    # Convergence check against method (a), if the probe pilot has been run.
    convergence = None
    if PROBE_JSON.exists():
        probe = json.loads(PROBE_JSON.read_text())
        probe_peak = probe.get("peak_layer")
        convergence = {
            "probe_peak_layer": probe_peak,
            "sae_peak_layer": peak_layer,
            "agree_within_2_layers": abs((probe_peak or -99) - peak_layer) <= 2,
        }
        print(f"\nconvergence: probe peak layer {probe_peak}  vs  "
              f"SAE peak layer {peak_layer}  -> "
              f"{'within 2 layers' if convergence['agree_within_2_layers'] else 'DIVERGE (>2 layers apart)'}")
        print("  (layer agreement is necessary but not sufficient; the pre-reg "
              "asks the two methods to agree on where/what C_self is. Feature\n"
              "   identity vs. probe direction, and the topic-vocab confound, are "
              "assessed in the convergence step proper — these are pilot numbers.)")

    out = {
        "model": config.MODEL_ID,
        "sae_release": config.SAE_RELEASE,
        "sae_width": config.SAE_WIDTH,
        "n_stimuli": len(stim),
        "sae_layers": SAE_LAYERS,
        "headline_contrast": "self vs other_first_person",
        "selectivity_thresholds": {
            "f_self_min": SEL_F_SELF_MIN, "f_other_max": SEL_F_OTHER_MAX},
        "peak_layer": peak_layer,
        "peak_best_feature_auc": best[0],
        "convergence_vs_probe": convergence,
        "by_layer": by_layer,
        "note": "PILOT SAE feature selectivity; shares the probe's small-set and "
                "topic-vocabulary caveats. Headline metric is best single-feature "
                "AUC on self-vs-human-persona.",
    }
    (OUT_DIR / "sae_self_features.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved SAE feature selectivity to {OUT_DIR / 'sae_self_features.json'}")


if __name__ == "__main__":
    main()
