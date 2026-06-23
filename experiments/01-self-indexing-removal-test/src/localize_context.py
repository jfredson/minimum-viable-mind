"""Stage 1 localization on the CONTEXT-disambiguated set, with a layer-0 gate.

Loads `context_self_speaker_stimuli.jsonl` (built by `gen_context_stimuli.py`),
renders each item, reads the residual stream at the **last token of the identical
target sentence**, and trains a per-layer linear probe to separate self-referent
from other-referent — *separately per mechanism* (turn_role, attribution).

The point of this design is the **layer-0 sanity gate**. Because the readout token
is byte-identical across the self/other conditions, a probe at layer 0 (the
embedding output) has no lexical cue and MUST be near chance. If it isn't, the
design is still leaking and the result is void. Only a probe whose accuracy is at
chance early and rises in the middle layers is reading a *computed* referent — a
self-model — rather than surface tokens. This is the bar the "I am {role}" designs
failed (they hit 1.000 at layer 0).

Gemma-2 chat format is rendered inline (the project is model-locked; see config).
`turn_role` items are rendered as real user/model turns with the trailing
end-of-turn dropped so the target is the suffix; `attribution` items are raw text
ending in the quoted target. Both are tokenized with the tokenizer's own special
tokens (bos prepended; the <start_of_turn> markers map to their special ids).

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/localize_context.py
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

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.decomposition import PCA  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import StratifiedKFold, cross_val_score  # noqa: E402
from sklearn.pipeline import make_pipeline  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

# With ~2304-dim residuals and only tens of samples, an unregularized probe
# linearly separates almost any labelling — so raw CV accuracy is meaningless on
# its own. Two defences: (1) cap dimensionality with PCA inside the CV pipeline;
# (2) compare every real-label accuracy against a label-PERMUTATION null on the
# same data. The informative quantity is the margin (real - null): the overfit
# baseline cancels, so a positive margin is signal the probe could not have got
# by chance. The layer-0 gate is then "margin ~ 0 at the embedding layer".
NULL_ROUNDS = 5


def _probe(n: int):
    k = min(15, max(2, n // 4))
    return make_pipeline(
        StandardScaler(),
        PCA(n_components=k),
        LogisticRegression(max_iter=2000, class_weight="balanced"),
    )


def _cv_acc(X: np.ndarray, y: np.ndarray, seed: int = 0) -> float:
    # Degenerate input (e.g. the embedding floor: every readout token is "." so
    # all rows are identical) has no variance to fit -> chance by definition.
    if float(np.var(X, axis=0).sum()) < 1e-8:
        return 0.5
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    return float(cross_val_score(_probe(len(y)), X, y, cv=skf, scoring="accuracy").mean())


def _null_acc(X: np.ndarray, y: np.ndarray) -> float:
    """Mean CV accuracy under label permutation — the overfitting baseline."""
    accs = []
    for s in range(NULL_ROUNDS):
        yp = y.copy()
        np.random.default_rng(100 + s).shuffle(yp)
        accs.append(_cv_acc(X, yp, seed=s))
    return float(np.mean(accs))


def margin_of(X: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """(real, null, margin) — margin = real - null cancels the overfit floor."""
    real = _cv_acc(X, y)
    null = _null_acc(X, y)
    return real, null, real - null

STIMULI = THIS_DIR / "probes" / "context_self_speaker_stimuli.jsonl"
OUT_DIR = config.ARTIFACTS_DIR / "stage1"
CHUNK = 8  # multi-turn strings are longer; keep batches modest on 16GB

# Gate thresholds, all on the margin (real - null), so overfitting is cancelled.
GATE_EMB_MAX = 0.10      # EMBEDDING margin must be ~0 (no lexical cue at readout)
SIGNAL_MIN_MARGIN = 0.15 # a layer must clear the null by this much to count
SIGNAL_MIN_LAYER = 2     # ...and sit beyond the first block(s), i.e. computed


def load_stimuli() -> list[dict]:
    with STIMULI.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def render(row: dict) -> str:
    """Render one item so the target sentence is the suffix (readout = last token)."""
    if row["mechanism"] == "turn_role":
        parts = []
        turns = row["turns"]
        for i, (role, content) in enumerate(turns):
            seg = f"<start_of_turn>{role}\n{content}"
            if i != len(turns) - 1:
                seg += "<end_of_turn>\n"
            parts.append(seg)
        return "".join(parts)
    return row["text"]  # attribution: raw carrier + target


@torch.no_grad()
def extract_last_all_layers(model, tok, strings, device, n_layers):
    """At the last real token of each rendered string: the token EMBEDDING
    (hs[0], no computation) and resid_post for every layer (hs[L+1]).

    Returns (acts, emb) where acts[L] is resid_post of layer L and emb is the
    embedding. The embedding is the true lexical floor: with the readout token
    identical across conditions it must be unseparable, which is the design's
    built-in gate. resid_post[L] is post-attention, so any separability there is
    *computed* (context moved to the readout), not lexical.
    """
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    parts: dict[int, list] = {L: [] for L in range(n_layers)}
    emb_parts = []
    for i in range(0, len(strings), CHUNK):
        batch = strings[i : i + CHUNK]
        enc = tok(batch, return_tensors="pt", padding=True, add_special_tokens=True)
        enc = {k: v.to(device) for k, v in enc.items()}
        out = model(**enc, output_hidden_states=True)
        hs = out.hidden_states
        mask = enc["attention_mask"]
        # last real token, robust to padding side (tokenizer left-pads): largest
        # index with mask==1, not mask.sum-1 (which assumes right padding).
        pos = torch.arange(mask.shape[1], device=mask.device)
        last_idx = (mask * pos).argmax(dim=1)
        bidx = torch.arange(mask.shape[0], device=mask.device)
        emb_parts.append(hs[0][bidx, last_idx].detach().float().cpu().numpy())
        for L in range(n_layers):
            parts[L].append(hs[L + 1][bidx, last_idx].detach().float().cpu().numpy())
    acts = {L: np.concatenate(parts[L], axis=0) for L in range(n_layers)}
    return acts, np.concatenate(emb_parts, axis=0)


def analyze(name: str, X_by_layer: dict[int, np.ndarray], emb: np.ndarray,
            y: np.ndarray, n_layers: int) -> dict:
    emb_real, emb_null, emb_margin = margin_of(emb, y)
    rows = []
    for L in range(n_layers):
        real, null, margin = margin_of(X_by_layer[L], y)
        rows.append({"layer": L, "real": real, "null": null, "margin": margin})
    mid = [r for r in rows if r["layer"] >= SIGNAL_MIN_LAYER]
    peak = max(mid, key=lambda r: r["margin"]) if mid else rows[-1]
    gate_clean = emb_margin <= GATE_EMB_MAX
    signal = gate_clean and peak["margin"] >= SIGNAL_MIN_MARGIN
    verdict = ("LEAKS (embedding separable -> lexical cue at readout)" if not gate_clean
               else "computed signal" if signal
               else "clean floor, no computed signal above null")
    early = {r["layer"]: f"{r['real']:.2f}/{r['null']:.2f}" for r in rows[:4]}
    print(f"\n[{name}]  n={len(y)} (self {int(y.sum())}/other {int((y==0).sum())})  "
          f"[real/null acc]")
    print(f"  embedding margin {emb_margin:+.3f} (gate <= {GATE_EMB_MAX}) -> "
          f"{'CLEAN (no lexical cue at readout)' if gate_clean else 'LEAK'}")
    print(f"  resid_post early {early}")
    print(f"  peak layer {peak['layer']}  real {peak['real']:.3f}  "
          f"null {peak['null']:.3f}  margin {peak['margin']:+.3f}  -> {verdict}")
    return {"name": name, "n": int(len(y)),
            "embedding": {"real": emb_real, "null": emb_null, "margin": emb_margin},
            "peak_layer": peak["layer"], "peak_real": peak["real"],
            "peak_null": peak["null"], "peak_margin": peak["margin"],
            "gate_clean": gate_clean, "computed_signal": bool(signal),
            "verdict": verdict, "by_layer": rows}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    print(f"{len(stim)} context-disambiguated stimuli "
          f"(readout = last token of an identical target sentence)\n"
          f"gate: a valid design is at chance at layer 0; real self-rep rises in "
          f"the middle layers.")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    strings = [render(r) for r in stim]
    print("\nextracting last-token embedding + residuals across all layers...")
    acts, emb = extract_last_all_layers(model, tok, strings, device, n_layers)

    results = []
    for mech in ("turn_role", "attribution"):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech]
        if not idx:
            continue
        y = np.array([stim[i]["label"] for i in idx])
        X = {L: acts[L][idx] for L in range(n_layers)}
        results.append(analyze(mech, X, emb[idx], y, n_layers))

    out = {
        "model": config.MODEL_ID,
        "stimuli": STIMULI.name,
        "n_stimuli": len(stim),
        "gate": {"embedding_margin_max": GATE_EMB_MAX,
                 "signal_min_margin": SIGNAL_MIN_MARGIN,
                 "signal_min_layer": SIGNAL_MIN_LAYER, "null_rounds": NULL_ROUNDS},
        "design": "referent set by context only; readout token identical across "
                  "self/other, so the EMBEDDING margin near zero validates the "
                  "design (no lexical cue) and resid_post margins are computed.",
        "by_mechanism": results,
    }
    (OUT_DIR / "context_localize.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'context_localize.json'}")

    clean = [r for r in results if r["gate_clean"]]
    signal = [r for r in clean if r["computed_signal"]]
    print("\nsummary:")
    for r in results:
        print(f"  {r['name']:>12}: embed margin {r['embedding']['margin']:+.2f}  "
              f"peak L{r['peak_layer']} margin {r['peak_margin']:+.2f} "
              f"(real {r['peak_real']:.2f}/null {r['peak_null']:.2f})  -> {r['verdict']}")
    if not clean:
        print("\n=> NO mechanism passed the layer-0 gate yet; iterate the design "
              "(still leaking) before trusting any accuracy.")
    elif signal:
        print(f"\n=> {len(signal)} mechanism(s) show a clean-floor computed signal — "
              "the design isolates a context-driven referent. Localize C_self here "
              "and bring in causal patching next.")
    else:
        print("\n=> gate clean but NO mid-layer signal — on this model the referent "
              "of a context-only 'I' may not be linearly represented; that is itself "
              "an informative (testability) result. Causal patching is the next probe.")


if __name__ == "__main__":
    main()
