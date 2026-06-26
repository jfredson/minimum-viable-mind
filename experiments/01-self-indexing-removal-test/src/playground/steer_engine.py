"""Steerable-model engine for the interactive playground (Stage 1).

*** NON-EVIDENTIAL. This module is a qualitative intuition tool and lives OUTSIDE
the registered measurement path. Nothing here is imported by the scoring scripts,
and its outputs go to artifacts/playground/ (never artifacts/stage1/ results).
Impressions from turning these dials must not feed threshold-setting — that is the
researcher-degrees-of-freedom leak the pre-registration exists to close. See the
README in this directory. ***

What it does
------------
Wraps the same forward-hook mechanism `patch_context.py` validated (add a scalar
multiple of a localized direction at a layer) and runs it *during generation*, with
the coefficient under your hand, so you can chat with the model while dialling a
self-structure down (remove) or up (amplify).

A "dial" is one localized direction:
  - C_self-index    : the thin "who is the current speaker" structure (turn_role).
  - C_self-narrative: the persona/identity structure (narrative contrast).
  - random (control): a norm-matched random direction at the index layer — the
                      "is anybody home" baseline. Steering it should mostly just
                      degrade coherence, not produce a coherent shift.

Coefficient alpha is interpreted in units of the measured self/other projection
gap at the dial's layer (its `ref_scale`). So alpha = +1 injects roughly "one
self/other gap" of the structure, alpha = 0 is baseline, alpha = -1 removes about
one gap (the removal-test direction), alpha = +2 amplifies. NB: unlike the
validated last-token patch, generation-time steering is applied at ALL positions
each decode step — a deliberately stronger intervention for "feel", so magnitudes
do not map 1:1 onto patch_context's ~0.35 restoration number.

Run on the Mac (MPS), from the repo root with the venv active. It cannot run in
the Linux tooling sandbox (no MPS / model weights there).
"""
from __future__ import annotations

import json
import sys
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent          # .../src/playground
EXP_SRC = THIS_DIR.parent                            # .../src  (localize_context.py)
REPO_ROOT = Path(__file__).resolve().parents[4]      # minimum-viable-mind
sys.path.insert(0, str(EXP_SRC))
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

# Reuse the proven, padding-correct readout extractor and renderers.
from localize_context import (  # noqa: E402
    extract_last_all_layers,
    load_stimuli,
    render,
)

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

# Quarantined output dir — deliberately NOT artifacts/stage1 (the scoring path).
DIALS_DIR = config.ARTIFACTS_DIR / "playground" / "dials"

# Default layers: the causal peaks reported in STATUS (index ~L22, narrative ~L23).
DEFAULT_LAYERS = {"index": 22, "narrative": 23}
# mechanism name in the stimuli file -> dial name
MECH_OF = {"index": "turn_role", "narrative": "narrative"}

# A fixed, self-neutral passage for the perplexity gate. No first-person / AI
# content, so a rising perplexity as |alpha| grows means the steering is pushing
# the model off-distribution (breaking it), not revealing a self-structure.
NEUTRAL_TEXT = (
    "The harbour town wakes early. Fishing boats leave before dawn and return "
    "by mid-morning, their decks slick with salt water. Crates of fish are "
    "stacked along the quay, weighed, and carried to the market square, where "
    "vendors arrange them on beds of crushed ice. By noon the stalls are busy "
    "and the smell of fried dough drifts from the corner of the street."
)

# A SELF-RELEVANT passage in the model's own assistant voice: it is about being
# the current speaker, tracking its own turn and its own prior outputs — exactly
# the content C_self-index is supposed to carry. Compared against NEUTRAL_TEXT, it
# is the within-tool probe for self-SPECIFICITY: if removing the index dial
# degrades prediction on THIS passage more than on the neutral one, the structure
# is doing something self-relevant, not just general next-token work. This is the
# RT-02 T-split intuition in miniature — a hint, NOT evidence (still confounded by
# the deflationary turn-state/router reading; the registered T_syntax control is
# what actually adjudicates).
SELF_RELEVANT_TEXT = (
    "I am the assistant in this conversation, and I am the one speaking now. A "
    "moment ago I gave you an answer, and I am building directly on what I just "
    "said. As I write this reply I keep track of my own earlier responses, and I "
    "know that it is my turn to speak rather than yours. The words here are mine."
)


@dataclass
class Dial:
    """One localized direction plus how strongly to apply it."""
    name: str
    layer: int
    direction: np.ndarray            # unit vector in residual space (points self-ward)
    ref_scale: float                 # mean self/other projection gap at `layer`
    method: str = "add"              # v1 implements "add" only (forward-looking field)
    meta: dict = field(default_factory=dict)

    def to_npz(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.savez(
            path,
            name=self.name, layer=self.layer, direction=self.direction,
            ref_scale=self.ref_scale, method=self.method,
            meta=json.dumps(self.meta),
        )

    @classmethod
    def from_npz(cls, path: Path) -> "Dial":
        z = np.load(path, allow_pickle=False)
        return cls(
            name=str(z["name"]), layer=int(z["layer"]),
            direction=z["direction"].astype(np.float32),
            ref_scale=float(z["ref_scale"]), method=str(z["method"]),
            meta=json.loads(str(z["meta"])),
        )


def _fit_unit_direction(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Logistic-regression direction, de-standardized and unit-normed.

    Same recipe as patch_context.fit_direction so the playground steers along the
    same axis the causal test validated.
    """
    scaler = StandardScaler().fit(X)
    clf = LogisticRegression(max_iter=2000, C=1.0, class_weight="balanced")
    clf.fit(scaler.transform(X), y)
    d = clf.coef_[0] / scaler.scale_
    return d / np.linalg.norm(d)


class SteerEngine:
    """Holds the model and a set of dials; steers during generation."""

    def __init__(self, model, tok, device: str):
        self.model = model
        self.tok = tok
        self.device = device
        self.n_layers = model.config.num_hidden_layers
        self.d_model = model.config.hidden_size
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token

    # ---- construction -------------------------------------------------------
    @classmethod
    def load(cls) -> "SteerEngine":
        device = get_device()
        tok = load_tokenizer()
        model, device, _ = load_model(device)
        return cls(model, tok, device)

    # ---- dial fitting -------------------------------------------------------
    def _fit_self_dial(self, name: str, acts_by_layer, stim, layer: int) -> Dial:
        mech = MECH_OF[name]
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        if not idx:
            raise ValueError(f"no stimuli for mechanism {mech!r}")
        y = np.array([stim[i]["label"] for i in idx])
        X = acts_by_layer[layer][idx]
        d = _fit_unit_direction(X, y)
        proj = X @ d
        gap = float(proj[y == 1].mean() - proj[y == 0].mean())
        # Keep the direction pointing self-ward and ref_scale positive, so
        # alpha>0 always means "more self".
        if gap < 0:
            d, gap = -d, -gap
        return Dial(
            name=name, layer=layer, direction=d.astype(np.float32), ref_scale=gap,
            method="add",
            meta={"mechanism": mech, "n": int(len(y)),
                  "note": "fit on context-disambiguated stimuli; self-ward, "
                          "ref_scale = mean self/other projection gap at layer"},
        )

    def build_standard_dials(self, layers: dict | None = None,
                             ctrl_seed: int = 0, refit: bool = False) -> dict:
        """Fit (or load) the three standard dials with ONE forward pass.

        Returns {name: Dial} for index, narrative, random. Caches each to npz so
        relaunches are instant unless refit=True or the layer changed.
        """
        layers = {**DEFAULT_LAYERS, **(layers or {})}
        wanted = {"index": layers["index"], "narrative": layers["narrative"]}

        cached: dict[str, Dial] = {}
        if not refit:
            for nm, L in wanted.items():
                p = DIALS_DIR / f"{nm}.npz"
                if p.exists():
                    d = Dial.from_npz(p)
                    if d.layer == L:
                        cached[nm] = d

        if len(cached) < len(wanted):
            stim = load_stimuli()
            strings = [render(r) for r in stim]
            acts, _emb = extract_last_all_layers(
                self.model, self.tok, strings, self.device, self.n_layers
            )
            for nm, L in wanted.items():
                if nm in cached:
                    continue
                d = self._fit_self_dial(nm, acts, stim, L)
                d.to_npz(DIALS_DIR / f"{nm}.npz")
                cached[nm] = d

        # Control: norm-matched random direction at the index layer, borrowing the
        # index dial's ref_scale so its steering magnitude is comparable.
        idx = cached["index"]
        rng = np.random.default_rng(ctrl_seed)
        r = rng.standard_normal(self.d_model).astype(np.float32)
        r /= np.linalg.norm(r)
        cached["random"] = Dial(
            name="random", layer=idx.layer, direction=r, ref_scale=idx.ref_scale,
            method="add",
            meta={"control": True, "seed": ctrl_seed,
                  "note": "norm-matched random direction; the 'nobody home' baseline"},
        )
        return cached

    # ---- steering -----------------------------------------------------------
    def _steer_vectors(self, settings: list[tuple[Dial, float]]) -> dict:
        """Group settings into one additive vector per layer (device tensor)."""
        per_layer: dict[int, torch.Tensor] = {}
        for dial, alpha in settings:
            if alpha == 0.0:
                continue
            d = torch.as_tensor(dial.direction, device=self.device, dtype=torch.float32)
            v = (alpha * dial.ref_scale) * d
            per_layer[dial.layer] = per_layer.get(
                dial.layer, torch.zeros(self.d_model, device=self.device)
            ) + v
        return per_layer

    @contextmanager
    def _hooks(self, settings: list[tuple[Dial, float]]):
        """Add the steering vector at each dial's layer, all positions, all steps."""
        per_layer = self._steer_vectors(settings)
        handles = []

        def make_hook(vec: torch.Tensor):
            def hook(_mod, _inp, out):
                h = out[0] if isinstance(out, tuple) else out
                h = h + vec.to(h.dtype)
                if isinstance(out, tuple):
                    return (h,) + tuple(out[1:])
                return h
            return hook

        try:
            for L, vec in per_layer.items():
                handles.append(
                    self.model.model.layers[L].register_forward_hook(make_hook(vec))
                )
            yield
        finally:
            for h in handles:
                h.remove()

    # ---- behaviours ---------------------------------------------------------
    @torch.no_grad()
    def generate(self, prompt: str, settings: list[tuple[Dial, float]],
                 max_new_tokens: int = 200) -> str:
        chat = [{"role": "user", "content": prompt}]
        inputs = self.tok.apply_chat_template(
            chat, add_generation_prompt=True, return_tensors="pt", return_dict=True
        ).to(self.device)
        prompt_len = inputs["input_ids"].shape[1]
        with self._hooks(settings):
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False
            )
        return self.tok.decode(
            out[0][prompt_len:], skip_special_tokens=True
        ).strip()

    @torch.no_grad()
    def perplexity(self, settings: list[tuple[Dial, float]],
                   text: str | None = None) -> float:
        """Token-level perplexity of a fixed neutral passage under the dials.

        Flat across alpha = on-manifold steering. A spike = the model is being
        pushed off-distribution (breaking), and any 'personality' is an artifact.
        """
        text = text or NEUTRAL_TEXT
        enc = self.tok(text, return_tensors="pt", add_special_tokens=True).to(self.device)
        ids = enc["input_ids"]
        with self._hooks(settings):
            out = self.model(**enc)
        logits = out.logits[:, :-1, :].float()
        targets = ids[:, 1:]
        logp = torch.log_softmax(logits, dim=-1)
        tok_logp = logp.gather(-1, targets.unsqueeze(-1)).squeeze(-1)
        return float(torch.exp(-tok_logp.mean()).item())

    def perplexity_both(self, settings: list[tuple[Dial, float]]) -> dict:
        """Perplexity on the neutral AND self-relevant passages, under the dials.

        Returns {"neutral": float, "self": float}. The pair is the self-specificity
        probe: compare each against its own alpha=0 baseline, and a self ratio that
        outruns the neutral ratio under removal is a (non-evidential) hint that the
        structure is self-relevant rather than a generic LM axis.
        """
        return {
            "neutral": self.perplexity(settings, text=NEUTRAL_TEXT),
            "self": self.perplexity(settings, text=SELF_RELEVANT_TEXT),
        }

    @torch.no_grad()
    def sweep(self, prompt: str, dial: Dial, alphas, max_new_tokens: int = 160):
        """Same prompt at several alpha values for the one dial — controlled compare.

        Returns list of dicts: {alpha, text, ppl_neutral, ppl_self}.
        """
        rows = []
        for a in alphas:
            settings = [(dial, float(a))]
            ppl = self.perplexity_both(settings)
            rows.append({
                "alpha": float(a),
                "text": self.generate(prompt, settings, max_new_tokens=max_new_tokens),
                "ppl_neutral": ppl["neutral"],
                "ppl_self": ppl["self"],
            })
        return rows
