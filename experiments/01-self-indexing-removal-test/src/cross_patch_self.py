"""Stage 1 (RT-04, decisive test) — causal cross-patching index <-> narrative.

Geometry (`separate_self.py`) says C_self-index and C_self-narrative are
distinguishable but share a decodable component. Geometry cannot say whether
that shared component is *functional*. This script asks it causally, in both
directions, using the same directional set-the-coordinate patching as
`patch_context.py`:

  - **own patches (the baselines):** d_index into the turn_role other-runs
    (restoration toward the turn_role self-run); d_narrative into the narrative
    other-runs (restoration toward the own-persona run).
  - **cross patches (the test):** d_narrative into the turn_role other-runs;
    d_index into the narrative other-runs. Each uses its own per-pair
    set-the-coordinate scale on the target pairs.
  - **controls:** a norm-matched random direction per context, as always.

Decision convention (committed before results, mirroring the RT-09/RT-10
conventions): an own patch is *valid* if it beats its random control by >= 0.10;
given both own patches valid, a **cross-patch ratio** (cross restoration / own
restoration, at the own patch's peak causal layer) < 0.5 in BOTH directions =>
the shared geometric component is not functional — the structures are
**functionally separable** and the removal test can target each independently.
Ratio >= 0.5 in either direction => shared functional structure in that
direction; if both fire, record that the structures are functionally entangled
and the Metzinger seam stands open on this method (RT-04 loss condition).

Runs on the length-matched v2 stimuli (RT-10) — the narrative instruction-length
nuisance the earlier verdict flagged is now controlled by design.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/cross_patch_self.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402  — must precede hub imports (sets HF_HOME)
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import render, load_stimuli  # noqa: E402
from patch_context import (  # noqa: E402
    run_clean, fit_direction, run_patched, restoration,
)

import numpy as np  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
PATCH_LAYERS = config.scale_layers([1, 3, 5, 8, 11, 14, 18, 22])
RAND_SEED = 0
OWN_VALID_GAP = 0.10      # own restoration must beat random by this to count
CROSS_RATIO_MAX = 0.50    # cross/own below this = functionally separable


def build_pairs(stim, mech):
    """Matched (self, other) pairs for a mechanism, keyed by (target, variant)."""
    rows = [r for r in stim if r["mechanism"] == mech]
    selfs = sorted([r for r in rows if r["label"] == 1], key=lambda r: r["id"])
    others = {(r["target"], r["id"][-1]): r for r in rows if r["label"] == 0}
    return [(s, others[(s["target"], s["id"][-1])]) for s in selfs
            if (s["target"], s["id"][-1]) in others]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    pairs_i = build_pairs(stim, "turn_role")
    pairs_n = build_pairs(stim, "narrative")
    print(f"{len(pairs_i)} turn_role pairs, {len(pairs_n)} narrative pairs")

    str_iS = [render(s) for s, _ in pairs_i]
    str_iO = [render(o) for _, o in pairs_i]
    str_nS = [render(s) for s, _ in pairs_n]
    str_nO = [render(o) for _, o in pairs_n]

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("caching clean runs (4 sets)...")
    res_iS, log_iS = run_clean(model, tok, str_iS, device, n_layers)
    res_iO, log_iO = run_clean(model, tok, str_iO, device, n_layers)
    res_nS, log_nS = run_clean(model, tok, str_nS, device, n_layers)
    res_nO, log_nO = run_clean(model, tok, str_nO, device, n_layers)
    delta_i = log_iS - log_iO
    delta_n = log_nS - log_nO

    rng = np.random.default_rng(RAND_SEED)
    print(f"\n{'layer':>5}  {'idx_own':>8} {'narr>idx':>8} {'rand_i':>7}   "
          f"{'narr_own':>8} {'idx>narr':>8} {'rand_n':>7}")
    rows = []
    for L in PATCH_LAYERS:
        Xi = np.concatenate([res_iS[L], res_iO[L]])
        yi = np.concatenate([np.ones(len(pairs_i)), np.zeros(len(pairs_i))])
        Xn = np.concatenate([res_nS[L], res_nO[L]])
        yn = np.concatenate([np.ones(len(pairs_n)), np.zeros(len(pairs_n))])
        d_i = fit_direction(Xi, yi)
        d_n = fit_direction(Xn, yn)
        r_u = rng.standard_normal(d_i.shape)
        r_u = r_u / np.linalg.norm(r_u)

        def scale(res_S, res_O, d):
            return ((res_S[L] @ d) - (res_O[L] @ d))[:, None]

        # own patches
        li = run_patched(model, tok, str_iO, device, L, scale(res_iS, res_iO, d_i) * d_i)
        ln = run_patched(model, tok, str_nO, device, L, scale(res_nS, res_nO, d_n) * d_n)
        # cross patches
        lc_ni = run_patched(model, tok, str_iO, device, L, scale(res_iS, res_iO, d_n) * d_n)
        lc_in = run_patched(model, tok, str_nO, device, L, scale(res_nS, res_nO, d_i) * d_i)
        # random controls (scaled per-context along its own direction gap)
        lr_i = run_patched(model, tok, str_iO, device, L, scale(res_iS, res_iO, d_i) * r_u)
        lr_n = run_patched(model, tok, str_nO, device, L, scale(res_nS, res_nO, d_n) * r_u)

        own_i = float(restoration(li, log_iO, delta_i).mean())
        own_n = float(restoration(ln, log_nO, delta_n).mean())
        cross_ni = float(restoration(lc_ni, log_iO, delta_i).mean())  # narr dir on index behaviour
        cross_in = float(restoration(lc_in, log_nO, delta_n).mean())  # index dir on narrative behaviour
        rand_i = float(restoration(lr_i, log_iO, delta_i).mean())
        rand_n = float(restoration(lr_n, log_nO, delta_n).mean())
        rows.append({"layer": L, "own_index": own_i, "own_narrative": own_n,
                     "cross_narr_on_index": cross_ni,
                     "cross_index_on_narr": cross_in,
                     "random_index_ctx": rand_i, "random_narr_ctx": rand_n})
        print(f"{L:>5}  {own_i:>8.3f} {cross_ni:>8.3f} {rand_i:>7.3f}   "
              f"{own_n:>8.3f} {cross_in:>8.3f} {rand_n:>7.3f}")

    # read at each own patch's peak causal layer (own - random), pre-committed
    peak_i = max(rows, key=lambda r: r["own_index"] - r["random_index_ctx"])
    peak_n = max(rows, key=lambda r: r["own_narrative"] - r["random_narr_ctx"])
    valid_i = peak_i["own_index"] - peak_i["random_index_ctx"] >= OWN_VALID_GAP
    valid_n = peak_n["own_narrative"] - peak_n["random_narr_ctx"] >= OWN_VALID_GAP
    ratio_ni = (peak_i["cross_narr_on_index"] / peak_i["own_index"]
                if peak_i["own_index"] > 0 else None)
    ratio_in = (peak_n["cross_index_on_narr"] / peak_n["own_narrative"]
                if peak_n["own_narrative"] > 0 else None)

    print(f"\nindex context   peak L{peak_i['layer']}: own {peak_i['own_index']:.3f}  "
          f"cross(narr) {peak_i['cross_narr_on_index']:.3f}  "
          f"ratio {ratio_ni if ratio_ni is None else f'{ratio_ni:.3f}'}  "
          f"(own valid: {valid_i})")
    print(f"narrative context peak L{peak_n['layer']}: own {peak_n['own_narrative']:.3f}  "
          f"cross(idx) {peak_n['cross_index_on_narr']:.3f}  "
          f"ratio {ratio_in if ratio_in is None else f'{ratio_in:.3f}'}  "
          f"(own valid: {valid_n})")

    if not (valid_i and valid_n):
        verdict = ("INCONCLUSIVE — an own patch failed to beat its random "
                   "control; the cross test has no baseline")
    else:
        fires_ni = ratio_ni is not None and ratio_ni >= CROSS_RATIO_MAX
        fires_in = ratio_in is not None and ratio_in >= CROSS_RATIO_MAX
        if not fires_ni and not fires_in:
            verdict = ("FUNCTIONALLY SEPARABLE — both cross-patch ratios < "
                       f"{CROSS_RATIO_MAX}; the shared geometric component is "
                       "not functional. Run the removal test on each "
                       "independently (RT-04).")
        elif fires_ni and fires_in:
            verdict = ("FUNCTIONALLY ENTANGLED — both cross-patches substitute; "
                       "the Metzinger seam stands open on this method (RT-04 "
                       "loss condition).")
        else:
            which = "narr->index" if fires_ni else "index->narr"
            verdict = (f"ASYMMETRIC SHARING ({which} fires) — report the "
                       "direction of entanglement; removal-test results must "
                       "be interpreted with the shared axis in view.")
    print(f"\n=> {verdict}")

    out = {
        "model": config.MODEL_ID,
        "design": "bidirectional directional cross-patching, length-matched v2 "
                  "stimuli; set-the-coordinate scale per direction per context",
        "convention": {"own_valid_gap": OWN_VALID_GAP,
                       "cross_ratio_max": CROSS_RATIO_MAX,
                       "read_at": "each own patch's peak causal layer"},
        "patch_layers": PATCH_LAYERS,
        "by_layer": rows,
        "peak_index_ctx": peak_i, "peak_narr_ctx": peak_n,
        "own_valid": {"index": bool(valid_i), "narrative": bool(valid_n)},
        "cross_ratio_narr_on_index": ratio_ni,
        "cross_ratio_index_on_narr": ratio_in,
        "verdict": verdict,
        "caveats": "single behavioural metric (next-token logits); n=24 pairs "
                   "per mechanism; directions from full-data logistic fits; "
                   "narrative retains a mild residual length signal "
                   "(AUC 0.56-0.57, see thresholds.md Pass 4 outcomes).",
    }
    (OUT_DIR / "cross_patch_self.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'cross_patch_self.json'}")


if __name__ == "__main__":
    main()
