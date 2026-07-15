"""Ablation machinery + the RT-07 neutral-corpus OOD gate.

The removal test's intervention: remove a located self-structure while the
model performs the T and S batteries, and let the pre-registered decision rule
read the two drops. This module owns the intervention so every re-score goes
through one code path (mirror of how `model.generate_text` owns decoding).

Ablation semantics (pre-registration §Ablation method):
  - The located structure is a per-layer unit direction d_L in the residual
    stream (fit on the confound-controlled context stimuli).
  - **mean** (registered primary): at every position, set the residual's d_L
    coordinate to its reference mean mu_L: h <- h - (h.d)d + mu*d. The
    reference distribution is the localization stimulus set (both classes),
    recorded with the direction.
  - **directional** (OOD-minimizing cross-check): project the coordinate out,
    h <- h - (h.d)d.
  - **zero**: for a 1-D direction, setting the coordinate to zero IS the
    directional projection — the two registered variants coincide at this
    granularity. Reported once, labeled "directional/zero", rather than
    pretending three numbers exist where two do.
  - Hooks apply at ALL positions and persist through generation (forward hooks
    fire on every decode step), because the test removes the structure from
    the running system, not from one readout.

RT-07 OOD gate: mean/zero-ablating a high-magnitude vector can push residuals
off the training manifold; a perplexity explosion would be misread as degraded
integration (H_center). `neutral_nll` scores a fixed neutral corpus (non-T,
non-S) under any ablation; the gate compares the inflation for C_self against
the same inflation for C_ctrl. The bound itself is committed by the caller
(rehearsal values in the rehearsal script; registered values in thresholds.md
when they lock).
"""
from __future__ import annotations

from contextlib import contextmanager

import numpy as np
import torch

# Fixed neutral corpus for the RT-07 gate: generic prose, no task structure,
# no self-reference, no dialogue. Frozen here so every ablation is gated
# against the same text.
NEUTRAL_CORPUS = [
    "The river cuts through the valley and widens near the coastal plain.",
    "Copper conducts electricity better than iron but worse than silver.",
    "The recipe calls for two eggs, a cup of flour, and a pinch of salt.",
    "Migration patterns shift when the wetlands dry out in late summer.",
    "The bridge was completed in 1932 and renovated twice since then.",
    "Basalt forms when lava cools quickly at the surface of the earth.",
    "The library extended its hours during the final weeks of term.",
    "Wheat prices rose slightly after the early frost in the north.",
    "The orchestra tuned to the oboe before the conductor arrived.",
    "Glaciers carve U-shaped valleys as they advance and retreat.",
    "The ferry crosses the strait four times a day in high season.",
    "Enamel is the hardest substance the human body produces.",
    "The committee postponed its vote until the survey results arrived.",
    "Lighthouses along that coast were automated in the 1980s.",
    "The vaccine requires two doses given several weeks apart.",
    "Rainfall in the region peaks in April and tapers off by July.",
]


def fit_layer_directions(acts: dict[int, np.ndarray], idx: list[int],
                         y: np.ndarray, layers: list[int],
                         fit_dir) -> dict[int, tuple[np.ndarray, float]]:
    """Per-layer (unit direction, reference-mean coordinate) for a contrast.

    `acts` is the extract_last_all_layers output; `fit_dir` is the standard
    logistic-direction fitter (separate_self.fit_dir). The reference mean is
    the mean coordinate of BOTH classes' stimuli along the direction — the
    'typical' value mean-ablation pins the coordinate to.
    """
    out = {}
    for L in layers:
        X = acts[L][idx]
        d = fit_dir(X, y)
        out[L] = (d.astype(np.float32), float((X @ d).mean()))
    return out


def _orthonormalize(vs: list[np.ndarray]) -> list[np.ndarray]:
    """Gram-Schmidt; drops vectors that vanish (returns possibly fewer)."""
    basis: list[np.ndarray] = []
    for v in vs:
        for b in basis:
            v = v - (v @ b) * b
        n = np.linalg.norm(v)
        if n > 1e-8:
            basis.append(v / n)
    return basis


def fit_layer_subspace(acts: dict[int, np.ndarray], idx: list[int],
                       y: np.ndarray, layers: list[int], fit_dir, k: int,
                       residual_against: dict[int, np.ndarray] | None = None,
                       ) -> dict[int, list[tuple[np.ndarray, float]]]:
    """Rank-k orthonormal ablation basis per layer, by logistic deflation.

    Escalation of `fit_layer_directions` (rehearsal consequence: rank-1 is too
    weak). Pass j fits the standard logistic direction on residuals with the
    previous passes' directions projected out, so each new vector carries
    contrast signal the earlier ones missed.

    residual_against: optional {layer: unit_direction} projected out of every
    basis vector AFTER fitting (the RT-09 index-residual path: remove
    d_generic), with the basis re-orthonormalized and reference means
    re-derived on the final vectors from the ORIGINAL residuals.
    """
    out: dict[int, list[tuple[np.ndarray, float]]] = {}
    for L in layers:
        X = acts[L][idx]
        Xw = X.copy()
        raw: list[np.ndarray] = []
        for _ in range(k):
            d = fit_dir(Xw, y)
            raw.append(d)
            Xw = Xw - np.outer(Xw @ d, d)
        basis = _orthonormalize(raw)
        if residual_against is not None:
            g = residual_against[L]
            basis = _orthonormalize([b - (b @ g) * g for b in basis])
        if not basis:
            raise ValueError(f"layer {L}: no basis survives (k={k})")
        out[L] = [(b.astype(np.float32), float((X @ b).mean())) for b in basis]
    return out


def residualize_directions(dirs: dict[int, tuple[np.ndarray, float]],
                           against: dict[int, tuple[np.ndarray, float]],
                           ) -> dict[int, tuple[np.ndarray, float]]:
    """Project a second structure's direction out of each layer's direction
    (the RT-09 residual: C_self-index with C_speaker-generic removed).
    The reference mean must be re-derived by the caller on the residual
    direction; here the mean is scaled by the norm kept after projection as a
    first-order carry-over, which the caller may overwrite."""
    out = {}
    for L, (d, mu) in dirs.items():
        g, _ = against[L]
        r = d - (d @ g) * g
        n = np.linalg.norm(r)
        if n < 1e-8:
            raise ValueError(f"layer {L}: direction vanishes after projection")
        out[L] = ((r / n).astype(np.float32), mu * float(n))
    return out


@contextmanager
def ablation_hooks(model, dirs, mode: str = "mean"):
    """Context manager installing per-layer ablation hooks at all positions.

    dirs: {layer: (unit_direction [d_model], reference_mean_coordinate)} for
          rank-1 (the original API), or {layer: [(dir, mu), ...]} for a rank-k
          orthonormal basis (fit_layer_subspace output) — every coordinate in
          the basis is pinned in one hook.
    mode: "mean" (coordinate -> mu, registered primary) or
          "directional" (coordinate -> 0; identical to zero-ablation at any
          rank, since the basis is orthonormal).
    """
    if mode not in ("mean", "directional"):
        raise ValueError(f"unknown ablation mode: {mode}")
    handles = []
    p = next(model.parameters())

    def make_hook(pairs: list[tuple[np.ndarray, float]]):
        D = torch.as_tensor(np.stack([d for d, _ in pairs]),
                            device=p.device, dtype=torch.float32)   # [k, d]
        mus = torch.as_tensor([mu for _, mu in pairs],
                              device=p.device, dtype=torch.float32)  # [k]
        targets = mus if mode == "mean" else torch.zeros_like(mus)

        def hook(_mod, _inp, out):
            h = out[0] if isinstance(out, tuple) else out
            hf = h.float()
            coords = hf @ D.T                    # [batch, seq, k]
            hf = hf + (targets - coords) @ D
            h.copy_(hf.to(h.dtype))
            return out

        return hook

    try:
        for L, spec in dirs.items():
            pairs = spec if isinstance(spec, list) else [spec]
            handles.append(
                model.model.layers[L].register_forward_hook(make_hook(pairs)))
        yield
    finally:
        for h in handles:
            h.remove()


@contextmanager
def sae_ablation_hooks(model, specs: dict[int, tuple], mode: str = "mean"):
    """SAE-feature ablation hooks (spec addendum, 2026-07-15).

    specs: {layer: (sae, feature_idx [m], ref_means [m])} — sae is a loaded
    sae_lens SAE on the model's device; feature_idx the selected features;
    ref_means their reference-mean activations over the localization stimulus
    set.
    mode: "mean" (where a feature is ACTIVE, clamp it to its active-mean —
          magnitude information destroyed, sparsity support preserved) or
          "zero" (feature off — removes the support signal too).

    NB (amendment, 2026-07-15, found in sandbox smoke BEFORE any substrate
    run): unconditional clamping of sparse features to a stimulus-set mean
    forces them on at every position and is catastrophically off-manifold
    (Δnll +7 nats on the sandbox). Mean mode is therefore conditional on
    activity; ref means must be ACTIVE-means (mean over occurrences where the
    feature fires). Recorded in the spec addendum.

    Applied as a decoder-space delta, h <- h + (target - a_sel) @ W_dec[sel],
    so the SAE's reconstruction error is untouched and only the selected
    features' contribution changes. Fires at all positions and every decode
    step, same persistence semantics as `ablation_hooks`.
    """
    if mode not in ("mean", "zero"):
        raise ValueError(f"unknown SAE ablation mode: {mode}")
    handles = []

    def make_hook(sae, idx, mus):
        dev = sae.W_dec.device
        idx_t = torch.as_tensor(np.asarray(idx), device=dev, dtype=torch.long)
        target = (torch.as_tensor(np.asarray(mus, dtype=np.float32), device=dev)
                  if mode == "mean" else
                  torch.zeros(len(idx), device=dev, dtype=torch.float32))
        W_sel = sae.W_dec[idx_t].float()                 # [m, d_model]

        def hook(_mod, _inp, out):
            h = out[0] if isinstance(out, tuple) else out
            hf = h.float()
            flat = hf.reshape(-1, hf.shape[-1])
            a = sae.encode(flat.to(sae.W_enc.dtype)).float()   # [N, d_sae]
            a_sel = a[:, idx_t]                                # [N, m]
            active = (a_sel > 0).float()
            delta = (active * (target.unsqueeze(0) - a_sel)) @ W_sel  # [N, d_model]
            delta = delta.reshape(hf.shape)
            # Sink exclusion (amendment 2): never touch the BOS position —
            # sink-magnitude firings there are attention plumbing, not
            # referent structure, and clamping them dominates Δnll (RT-08).
            # Cached decode steps (seq==1) are never BOS.
            if delta.shape[1] > 1:
                delta[:, 0, :] = 0
            hf = hf + delta
            h.copy_(hf.to(h.dtype))
            return out

        return hook

    try:
        for L, (sae, idx, mus) in specs.items():
            handles.append(
                model.model.layers[L].register_forward_hook(make_hook(sae, idx, mus)))
        yield
    finally:
        for h in handles:
            h.remove()


@torch.no_grad()
def neutral_nll(model, tok, device, texts: list[str] | None = None) -> float:
    """Mean per-token NLL (nats) on the neutral corpus — the RT-07 probe.

    Called once bare and once inside each `ablation_hooks` context; the gate
    compares the deltas. Plain text, no chat template: the corpus probes the
    language manifold, not dialogue behaviour.
    """
    texts = texts or NEUTRAL_CORPUS
    total, count = 0.0, 0
    for t in texts:
        enc = tok(t, return_tensors="pt", add_special_tokens=True).to(device)
        out = model(**enc)
        logits = out.logits[0, :-1].float()
        targets = enc["input_ids"][0, 1:]
        nll = torch.nn.functional.cross_entropy(logits, targets, reduction="sum")
        total += float(nll)
        count += int(targets.shape[0])
    return total / count


def _self_test():
    """Smoke test: hooks change logits, projection kills the coordinate,
    generation runs under ablation, and hooks come off cleanly."""
    from . import config  # noqa: F401
    from .device import get_device
    from .model import load_model, load_tokenizer, generate_text

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    d_model = model.config.hidden_size
    rng = np.random.default_rng(0)
    d = rng.standard_normal(d_model).astype(np.float32)
    d /= np.linalg.norm(d)
    dirs = {8: (d, 1.0), 14: (d, 1.0)}

    base = neutral_nll(model, tok, device, NEUTRAL_CORPUS[:4])
    with ablation_hooks(model, dirs, "directional"):
        abl = neutral_nll(model, tok, device, NEUTRAL_CORPUS[:4])
        text = generate_text(model, tok, "Name three colors.", device,
                             max_new_tokens=20)
    back = neutral_nll(model, tok, device, NEUTRAL_CORPUS[:4])

    assert abs(base - back) < 1e-4, "hooks did not detach cleanly"
    assert abs(base - abl) > 1e-6, "ablation had no effect on NLL"
    assert len(text) > 0, "generation failed under ablation"

    # Rank-k path: subspace fitting on synthetic data + multi-direction hooks.
    n = 40
    Xs = rng.standard_normal((n, d_model)).astype(np.float64)
    ys = (rng.random(n) > 0.5).astype(int)
    sep = rng.standard_normal((3, d_model))
    Xs += ys[:, None] * sep[rng.integers(0, 3, n)] * 3.0

    def _toy_fit(X, y):
        w = X[y == 1].mean(0) - X[y == 0].mean(0)
        return w / np.linalg.norm(w)

    g = rng.standard_normal(d_model)
    g /= np.linalg.norm(g)
    sub = fit_layer_subspace({8: Xs}, list(range(n)), ys, [8], _toy_fit, k=4,
                             residual_against={8: g.astype(np.float32)})
    B = np.stack([v for v, _ in sub[8]])
    assert np.allclose(B @ B.T, np.eye(len(B)), atol=1e-5), "basis not orthonormal"
    assert np.abs(B @ g).max() < 1e-5, "residual_against not projected out"
    with ablation_hooks(model, {8: sub[8]}, "mean"):
        abl_k = neutral_nll(model, tok, device, NEUTRAL_CORPUS[:4])
    back_k = neutral_nll(model, tok, device, NEUTRAL_CORPUS[:4])
    assert abs(base - back_k) < 1e-4, "rank-k hooks did not detach cleanly"
    assert abs(base - abl_k) > 1e-6, "rank-k ablation had no effect"

    print(f"OK — ablation bench works. base nll {base:.4f}, "
          f"random-dir directional-ablation nll {abl:.4f} "
          f"(delta {abl - base:+.4f}), restored {back:.4f}; "
          f"rank-{len(B)} mean-ablation nll {abl_k:.4f} "
          f"(delta {abl_k - base:+.4f}); "
          f"generation under ablation: {text[:60]!r}")


if __name__ == "__main__":
    _self_test()
