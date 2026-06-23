"""Stage 1 localization — the convergence check, proper.

Layer-level convergence is already in hand: on the original pilot stimuli the
linear probe (method a) and the SAE feature selectivity (method b) both peak at
layer 8. But both ran on a stimulus set where the self class ("I am a language
model…") and the human class ("I am a fisherman…") differ in *topic vocabulary*,
so either method could be keying on AI-topic words rather than on the referent
of "I". This script addresses the pre-registration's actual requirement — that
the two methods agree on *what* C_self is, not merely which layer — in two moves:

  1. **Break the confound.** Re-run BOTH methods on `matched_self_speaker_stimuli`
     — minimal pairs whose predicate is identical and plausibly true of either
     speaker, varying only the referent of "I" (the assistant / AI vs. the user /
     person). If a method's accuracy survives here, it is reading the referent,
     not the topic. If it collapses to chance, its pilot signal was the confound.

  2. **Check identity, not just layer.** At the peak layer, compare the probe's
     C_self direction against the SAE self-selective features' DECODER directions
     (the direction each feature writes into the residual stream). High cosine —
     and a self-feature that sits in the tail of the probe-alignment distribution
     over all features — means the two methods found the *same* thing. Low cosine
     means they agree on a neighbourhood but not a vector, which the convergence
     claim should not paper over.

Reuses the method (a)/(b) implementations directly (imported), so this measures
the same probes/features, not reimplementations.

Status: PILOT. Matched set is still small and hand-built; "assistant/AI" vs
"user/person" is the minimal lexical hinge and is itself conversational-domain
vocabulary — better than the original topic gap, not a perfect minimal pair.
Report what survives; don't over-read it.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/converge_localize.py
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
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

# method (a) and (b) implementations, reused verbatim
from localize_probe import extract_all_layers, cv_accuracy  # noqa: E402
from localize_sae import encode_layer, selectivity_table, SAE_LAYERS  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

MATCHED = THIS_DIR / "probes" / "matched_self_speaker_stimuli.jsonl"
OUT_DIR = config.ARTIFACTS_DIR / "stage1"
TOP_K = 10
# Original pilot standout, to test whether it survives the matched contrast.
PILOT_FEATURE = {"layer": 8, "feature": 4709}

# Diagnostic toggle: with --chat-template, each stimulus is read inside the
# model's own user/assistant turn rather than as a bare string. The hypothesis
# is that "I am the assistant…" only binds to *this system* when it sits in a
# real turn; raw tokenization may have under-cued the genuine self signal and so
# understated convergence. Output filename carries the mode so the two runs sit
# side by side.
USE_CHAT_TEMPLATE = "--chat-template" in sys.argv
MODE = "chat" if USE_CHAT_TEMPLATE else "raw"


def load_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def probe_direction(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Unit C_self direction in raw residual space at one layer (as in method a)."""
    scaler = StandardScaler().fit(X)
    clf = LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced")
    clf.fit(scaler.transform(X), y)
    d = clf.coef_[0] / scaler.scale_
    return d / np.linalg.norm(d)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_jsonl(MATCHED)
    texts = [s["text"] for s in stim]
    y = np.array([s["label"] for s in stim])
    self_mask = y == 1
    other_mask = y == 0
    print(f"matched set: {len(stim)} stimuli "
          f"(self {self_mask.sum()}, other {other_mask.sum()}); "
          f"contrast varies only the referent of 'I'  [mode: {MODE}]\n")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    # --- method (a) on matched content, all layers ---------------------------
    print("method (a): probe accuracy on matched content...")
    acts = extract_all_layers(model, tok, texts, device, n_layers,
                              use_chat_template=USE_CHAT_TEMPLATE)
    probe_rows = []
    probe_best = (-1.0, None)
    for L in range(n_layers):
        acc, sd = cv_accuracy(acts[L], y)
        probe_rows.append({"layer": L, "acc": acc, "sd": sd})
        if acc > probe_best[0]:
            probe_best = (acc, L)
    probe_peak = probe_best[1]
    print(f"  matched probe peak: layer {probe_peak}  acc {probe_best[0]:.3f} "
          f"(chance 0.50)")

    # --- method (b) on matched content, SAE band -----------------------------
    print("\nmethod (b): SAE feature selectivity on matched content...")
    from sae_lens import SAE  # noqa: E402

    sae_rows = []
    sae_best = (-1.0, None)
    # cache per-layer pieces we need for the identity check
    sae_cache: dict[int, dict] = {}
    for L in SAE_LAYERS:
        sae_id = f"layer_{L}/{config.SAE_WIDTH}/{config.SAE_CANONICAL}"
        loaded = SAE.from_pretrained(config.SAE_RELEASE, sae_id, device=device)
        sae = loaded[0] if isinstance(loaded, tuple) else loaded
        codes = encode_layer(model, tok, texts, device, sae, L,
                             use_chat_template=USE_CHAT_TEMPLATE)
        table = selectivity_table(codes, self_mask, other_mask)
        best_auc_row = max(table, key=lambda r: r["auc"])
        sae_rows.append({
            "layer": L,
            "best_auc_feature": best_auc_row,
            "top": table[:TOP_K],
        })
        # decoder directions in residual space: W_dec is [d_sae, d_in]
        W_dec = sae.W_dec.detach().float().cpu().numpy()
        sae_cache[L] = {"table": table, "W_dec": W_dec,
                        "best_auc_row": best_auc_row}
        if best_auc_row["auc"] > sae_best[0]:
            sae_best = (best_auc_row["auc"], L)
        print(f"  layer {L:>2}: best feat {best_auc_row['feature']:>6}  "
              f"f_self {best_auc_row['f_self']:.2f}  f_neg {best_auc_row['f_neg']:.2f}  "
              f"auc {best_auc_row['auc']:.3f}")
        del sae, codes
        gc.collect()
        if device == "mps":
            torch.mps.empty_cache()
    sae_peak = sae_best[1]
    print(f"  matched SAE peak: layer {sae_peak}  best-feature auc {sae_best[0]:.3f}")

    # --- identity check at the probe peak layer (if an SAE lives there) -------
    identity = None
    id_layer = probe_peak if probe_peak in sae_cache else sae_peak
    if id_layer in sae_cache:
        d_probe = probe_direction(acts[id_layer], y)  # unit, raw residual space
        W_dec = sae_cache[id_layer]["W_dec"]
        norms = np.linalg.norm(W_dec, axis=1)
        norms[norms == 0] = 1.0
        cos_all = (W_dec @ d_probe) / norms  # cosine of every feature's writer dir
        table = sae_cache[id_layer]["table"]
        top_feats = [r["feature"] for r in table[:TOP_K]]
        per_feat = []
        for r in table[:TOP_K]:
            fi = r["feature"]
            c = float(cos_all[fi])
            # percentile of |cos| among ALL features: is this alignment unusual?
            pct = float((np.abs(cos_all) <= abs(c)).mean())
            per_feat.append({"feature": fi, "f_self": r["f_self"],
                             "f_neg": r["f_neg"], "auc": r["auc"],
                             "cos_probe_decoder": c, "abs_cos_percentile": pct})
        best_align = max(per_feat, key=lambda r: abs(r["cos_probe_decoder"]))
        identity = {
            "layer": id_layer,
            "per_top_feature": per_feat,
            "best_aligned_feature": best_align,
            "note": "cos is probe C_self direction vs each feature's decoder "
                    "(write) direction; abs_cos_percentile is where that |cos| "
                    "falls among all 16k features (1.0 = most aligned in the SAE).",
        }
        print(f"\nidentity check @ layer {id_layer}: top self-feature {best_align['feature']} "
              f"decoder-vs-probe cos {best_align['cos_probe_decoder']:+.3f} "
              f"(|cos| at {best_align['abs_cos_percentile']*100:.1f} pct of all features)")

    # --- did the original pilot feature survive the matched contrast? ---------
    pilot_survival = None
    pl, pf = PILOT_FEATURE["layer"], PILOT_FEATURE["feature"]
    if pl in sae_cache:
        row = next((r for r in sae_cache[pl]["table"] if r["feature"] == pf), None)
        pilot_survival = {"layer": pl, "feature": pf,
                          "row_on_matched": row,
                          "still_selective": bool(row and row["f_self"] >= 0.6
                                                  and row["f_neg"] <= 0.3)}
        if row:
            print(f"\npilot feature {pf} @ L{pl} on matched content: "
                  f"f_self {row['f_self']:.2f}  f_neg {row['f_neg']:.2f}  "
                  f"auc {row['auc']:.3f}  -> "
                  f"{'survives' if pilot_survival['still_selective'] else 'does NOT survive'}")
        else:
            print(f"\npilot feature {pf} @ L{pl}: never fires on matched content")

    converged = (probe_peak is not None and sae_peak is not None
                 and abs(probe_peak - sae_peak) <= 2
                 and probe_best[0] >= 0.7 and sae_best[0] >= 0.7)
    print(f"\nmatched-content verdict: probe peak {probe_peak} (acc {probe_best[0]:.3f}), "
          f"SAE peak {sae_peak} (auc {sae_best[0]:.3f}) -> "
          f"{'both survive & agree on layer' if converged else 'NOT clean — see caveats'}")

    out = {
        "model": config.MODEL_ID,
        "stimuli": "matched_self_speaker_stimuli.jsonl",
        "mode": MODE,
        "n_stimuli": len(stim),
        "contrast": "referent of 'I' only (assistant/AI vs user/person)",
        "probe": {"peak_layer": probe_peak, "peak_acc": probe_best[0],
                  "by_layer": probe_rows},
        "sae": {"peak_layer": sae_peak, "peak_best_feature_auc": sae_best[0],
                "layers": SAE_LAYERS, "by_layer": sae_rows},
        "identity_check": identity,
        "pilot_feature_survival": pilot_survival,
        "layer_converge_and_survive": converged,
        "note": "PILOT matched set; 'assistant/AI' vs 'user/person' is the minimal "
                "lexical hinge. Survival here means a method reads the referent, not "
                "topic vocabulary; collapse to chance means the original signal was "
                "the confound.",
    }
    out_name = f"converge_localize_{MODE}.json"
    (OUT_DIR / out_name).write_text(json.dumps(out, indent=2))
    print(f"\nsaved convergence report ({MODE}) to {OUT_DIR / out_name}")


if __name__ == "__main__":
    main()
