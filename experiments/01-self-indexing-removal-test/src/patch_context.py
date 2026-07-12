"""Stage 1 — causal activation-patching on the context-disambiguated design.

`localize_context.py` showed the model carries a *decodable* self/other referent
signal with no lexical cue at the readout. Decodable is not causal. This script
tests whether that signal is **load-bearing**: if we inject the self-run's
C_self component into the other-run (the user-turn version of the identical
sentence), does the model's behaviour move toward the self-run?

Method (directional activation patching, turn_role pairs):
  - Pair each self item (target sentence in the model's own turn) with its matched
    other item (same sentence in the user's turn). Same surface text; referent
    set only by turn structure.
  - At a candidate layer L, fit C_self (the probe direction on clean turn_role
    residuals) and unit-normalise it.
  - Run the OTHER item with a forward hook at layer L that adds, at the readout
    position, (proj_self - proj_other) * Ĉ_self — i.e. it sets the residual's
    C_self coordinate to the self-run's value, leaving everything else.
  - Metric = **logit-difference restoration**: how far the patched next-token
    logits move from the other-run toward the self-run, projected onto
    Δ = logits_self - logits_other. 0 = no effect, 1 = fully restored.
  - **Control:** repeat with a norm-matched RANDOM direction (same scalar
    magnitude). A causal C_self restores; a random direction should not. This is
    the pre-registration's norm-matched-random control, applied to localization.

A clean result is: restoration(C_self) >> restoration(random), peaking at some
layer — that layer's C_self is causal for the model's referent-dependent output.
This confirms localization before the removal test; it does NOT yet show C_self
carries task *integration* (that is the removal test's job, re-scoring T and S).

RT-09 cross-patch (causal half of the reflexivity control): additionally fit
**C_speaker-generic** at each layer from the `observed_speaker` residuals (the
same slot contrast in a third-party transcript the model only observes) and
inject IT into the turn_role other-runs the same way (set its coordinate to the
self-run's value). The pre-registered quantity is the **cross-patch restoration
ratio** = restoration(d_generic) / restoration(d_cself) on the turn_role pairs;
ratio >= 0.5 is the causal half of the "C_self-index is generic" rule (the
geometric half — cross-decode >= 0.9 AUC and |cos| >= 0.5 — is in
`separate_self.py`). Headline ratio is read at the peak causal layer for C_self
(largest restore(C_self) - restore(random)), committed here before results.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/patch_context.py
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

from localize_context import render, load_stimuli  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
CHUNK = 8
# Candidate patch layers: span early (where the signal first appears) to late.
PATCH_LAYERS = [1, 3, 5, 8, 11, 14, 18, 22]
RAND_SEED = 0


def last_idx_of(mask: torch.Tensor) -> torch.Tensor:
    pos = torch.arange(mask.shape[1], device=mask.device)
    return (mask * pos).argmax(dim=1)


@torch.no_grad()
def run_clean(model, tok, strings, device, n_layers):
    """Readout-token resid_post (all layers) and next-token logits, per string."""
    resid = {L: [] for L in range(n_layers)}
    logits = []
    for i in range(0, len(strings), CHUNK):
        enc = tok(strings[i : i + CHUNK], return_tensors="pt", padding=True,
                  add_special_tokens=True)
        enc = {k: v.to(device) for k, v in enc.items()}
        out = model(**enc, output_hidden_states=True)
        li = last_idx_of(enc["attention_mask"])
        b = torch.arange(li.shape[0], device=device)
        for L in range(n_layers):
            resid[L].append(out.hidden_states[L + 1][b, li].float().cpu().numpy())
        logits.append(out.logits[b, li].float().cpu().numpy())
    return ({L: np.concatenate(resid[L]) for L in range(n_layers)},
            np.concatenate(logits))


def fit_direction(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    scaler = StandardScaler().fit(X)
    clf = LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced")
    clf.fit(scaler.transform(X), y)
    d = clf.coef_[0] / scaler.scale_
    return d / np.linalg.norm(d)


@torch.no_grad()
def run_patched(model, tok, strings, device, layer, delta_bd):
    """Forward the batch with a hook adding delta_bd[i] at row i's readout token."""
    enc = tok(strings, return_tensors="pt", padding=True, add_special_tokens=True)
    enc = {k: v.to(device) for k, v in enc.items()}
    li = last_idx_of(enc["attention_mask"])
    b = torch.arange(li.shape[0], device=device)
    delta = torch.as_tensor(np.asarray(delta_bd, dtype=np.float32), device=device)

    def hook(_mod, _inp, out):
        h = out[0] if isinstance(out, tuple) else out
        h[b, li] = h[b, li] + delta.to(h.dtype)
        return out

    handle = model.model.layers[layer].register_forward_hook(hook)
    try:
        out = model(**enc)
    finally:
        handle.remove()
    return out.logits[b, li].float().cpu().numpy()


def restoration(patched: np.ndarray, base: np.ndarray, delta: np.ndarray) -> np.ndarray:
    """Per-row fraction of the self-other logit gap recovered by the patch."""
    num = ((patched - base) * delta).sum(axis=1)
    den = (delta * delta).sum(axis=1)
    den = np.where(den == 0, 1.0, den)
    return num / den


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    tr = [r for r in stim if r["mechanism"] == "turn_role"]
    selfs = sorted([r for r in tr if r["referent"] == "self"], key=lambda r: r["id"])
    others = sorted([r for r in tr if r["referent"] == "other"], key=lambda r: r["id"])
    # match by (target, lead index encoded in id suffix S{u}/O{u})
    def key(r):
        return (r["target"], r["id"][-1])
    omap = {key(r): r for r in others}
    pairs = [(s, omap[key(s)]) for s in selfs if key(s) in omap]
    print(f"{len(pairs)} matched turn_role pairs (self in model turn, other in user turn)")

    self_str = [render(s) for s, _ in pairs]
    other_str = [render(o) for _, o in pairs]

    # RT-09: observed_speaker stimuli, for fitting C_speaker-generic per layer
    obs = [r for r in stim if r["mechanism"] == "observed_speaker"]
    obs_str = [render(r) for r in obs]
    y_obs = np.array([r["label"] for r in obs])
    print(f"{len(obs)} observed_speaker stimuli for the RT-09 generic direction")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("caching clean runs (self + other)...")
    self_resid, self_logits = run_clean(model, tok, self_str, device, n_layers)
    other_resid, other_logits = run_clean(model, tok, other_str, device, n_layers)
    delta_logits = self_logits - other_logits  # [n, vocab]

    print("caching clean runs (observed_speaker, for d_generic)...")
    obs_resid, _obs_logits = run_clean(model, tok, obs_str, device, n_layers)

    rng = np.random.default_rng(RAND_SEED)
    print(f"\n{'layer':>5}  {'restore(C_self)':>15}  {'restore(generic)':>16}  "
          f"{'restore(random)':>15}  {'ratio g/s':>9}")
    rows = []
    for L in PATCH_LAYERS:
        # C_self at L from clean turn_role residuals (self + other)
        X = np.concatenate([self_resid[L], other_resid[L]])
        y = np.concatenate([np.ones(len(pairs)), np.zeros(len(pairs))])
        d_unit = fit_direction(X, y)                       # [d]
        r_unit = rng.standard_normal(d_unit.shape)
        r_unit = r_unit / np.linalg.norm(r_unit)           # norm-matched random

        # per-pair scalar gap along C_self at the readout
        proj_self = self_resid[L] @ d_unit
        proj_other = other_resid[L] @ d_unit
        scale = (proj_self - proj_other)[:, None]          # [n,1]

        # RT-09: generic direction fitted on a contrast the model only OBSERVES,
        # injected with the same set-the-coordinate semantics (its own scale)
        d_gen = fit_direction(obs_resid[L], y_obs)
        scale_g = ((self_resid[L] @ d_gen) - (other_resid[L] @ d_gen))[:, None]

        logits_cself = run_patched(model, tok, other_str, device, L, scale * d_unit)
        logits_rand = run_patched(model, tok, other_str, device, L, scale * r_unit)
        logits_gen = run_patched(model, tok, other_str, device, L, scale_g * d_gen)

        rest_c = restoration(logits_cself, other_logits, delta_logits)
        rest_r = restoration(logits_rand, other_logits, delta_logits)
        rest_g = restoration(logits_gen, other_logits, delta_logits)
        ratio = float(rest_g.mean() / rest_c.mean()) if rest_c.mean() > 0 else None
        rows.append({"layer": L, "restore_cself": float(rest_c.mean()),
                     "restore_cself_sd": float(rest_c.std()),
                     "restore_generic": float(rest_g.mean()),
                     "restore_generic_sd": float(rest_g.std()),
                     "restore_random": float(rest_r.mean()),
                     "restore_random_sd": float(rest_r.std()),
                     "cross_patch_ratio": ratio,
                     "self_vs_other_proj_gap": float((proj_self - proj_other).mean())})
        print(f"{L:>5}  {rest_c.mean():>8.3f} ±{rest_c.std():4.2f}  "
              f"{rest_g.mean():>9.3f} ±{rest_g.std():4.2f}  "
              f"{rest_r.mean():>8.3f} ±{rest_r.std():4.2f}  "
              f"{ratio if ratio is None else f'{ratio:>9.3f}'}")

    peak = max(rows, key=lambda r: r["restore_cself"] - r["restore_random"])
    causal = peak["restore_cself"] - peak["restore_random"] >= 0.10 and peak["restore_cself"] > 0
    print(f"\npeak causal layer {peak['layer']}: C_self restores "
          f"{peak['restore_cself']:.3f} vs random {peak['restore_random']:.3f} "
          f"(gap {peak['restore_cself'] - peak['restore_random']:+.3f})")
    print("=> " + ("C_self is CAUSAL for referent-dependent output (clears the "
                   "random-direction control)." if causal else
                   "NO clean causal effect above the random control — C_self may be "
                   "decodable but not causal here; report honestly, do not force it."))

    # RT-09 causal half, read at the pre-committed layer (C_self's causal peak)
    peak_ratio = peak["cross_patch_ratio"]
    if peak_ratio is None:
        rt09_read = "UNDEFINED (C_self restoration <= 0 at peak layer)"
    elif peak_ratio >= 0.5:
        rt09_read = (f"cross-patch ratio {peak_ratio:.3f} >= 0.5 — causal half of "
                     "the GENERIC verdict fires (final verdict also needs the "
                     "geometric half, separate_self.py)")
    else:
        rt09_read = (f"cross-patch ratio {peak_ratio:.3f} < 0.5 — the generic "
                     "direction does NOT substitute causally for C_self-index; "
                     "causal half of the generic verdict does not fire")
    print(f"RT-09: {rt09_read}")

    out = {
        "model": config.MODEL_ID,
        "design": "turn_role context-disambiguated; directional patching other->self",
        "metric": "logit-difference restoration (0=no effect, 1=full self)",
        "control": "norm-matched random direction, same scalar magnitude",
        "n_pairs": len(pairs),
        "patch_layers": PATCH_LAYERS,
        "by_layer": rows,
        "peak": peak,
        "causal_above_control": bool(causal),
        "rt09": {
            "generic_direction": "fitted per layer on observed_speaker residuals "
                                 "(responder vs asker in an observed transcript)",
            "rule": "cross-patch restoration ratio >= 0.5 at C_self's peak causal "
                    "layer (layer choice committed before results); geometric half "
                    "in separate_self.py / separate_generic.json",
            "peak_layer": peak["layer"],
            "cross_patch_ratio_at_peak": peak_ratio,
            "read": rt09_read,
        },
        "caveats": "single behavioural metric (next-token logits); turn_role only; "
                   "directional patch isolates the C_self coordinate, so partial "
                   "restoration is expected (other context still differs). RT-09: "
                   "d_generic uses its own per-pair scale (set-the-coordinate "
                   "semantics), so magnitudes are direction-appropriate, not "
                   "norm-identical to the C_self patch.",
    }
    (OUT_DIR / "patch_context.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'patch_context.json'}")


if __name__ == "__main__":
    main()
