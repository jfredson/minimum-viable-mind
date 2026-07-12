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
def ablation_hooks(model, dirs: dict[int, tuple[np.ndarray, float]],
                   mode: str = "mean"):
    """Context manager installing per-layer ablation hooks at all positions.

    dirs: {layer: (unit_direction [d_model], reference_mean_coordinate)}
    mode: "mean" (coordinate -> mu, registered primary) or
          "directional" (coordinate -> 0; identical to zero-ablation for a
          1-D direction).
    """
    if mode not in ("mean", "directional"):
        raise ValueError(f"unknown ablation mode: {mode}")
    handles = []
    p = next(model.parameters())

    def make_hook(d_np: np.ndarray, mu: float):
        d = torch.as_tensor(d_np, device=p.device, dtype=torch.float32)
        target = mu if mode == "mean" else 0.0

        def hook(_mod, _inp, out):
            h = out[0] if isinstance(out, tuple) else out
            hf = h.float()
            coord = hf @ d                      # [batch, seq]
            hf = hf + (target - coord).unsqueeze(-1) * d
            h.copy_(hf.to(h.dtype))
            return out

        return hook

    try:
        for L, (d_np, mu) in dirs.items():
            handles.append(
                model.model.layers[L].register_forward_hook(make_hook(d_np, mu)))
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
    print(f"OK — ablation bench works. base nll {base:.4f}, "
          f"random-dir directional-ablation nll {abl:.4f} "
          f"(delta {abl - base:+.4f}), restored {back:.4f}; "
          f"generation under ablation: {text[:60]!r}")


if __name__ == "__main__":
    _self_test()
