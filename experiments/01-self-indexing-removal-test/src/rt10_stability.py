"""RT-10 causal-margin stability check (pre-lock; spec: ablation-pilot-spec.md §c).

Substrate-gates caveat 3: on Tulu-3-8B-SFT the C_self vs length-direction
causal margin narrowed to +0.117 — over the ≥0.10 bar, but the length control
was a single lstsq fit on 48 turn_role readout residuals. If the PASS depends
on that fit's fragility, it isn't a PASS. This script re-runs the patched
comparison with four length-direction fits of increasing independence:

  1. repro          — lstsq, turn_role residuals only (the original control)
  2. pooled         — lstsq, all five mechanisms' residuals
  3. ridge          — RidgeCV (LOO over alphas {0.1, 1, 10, 100}), pooled
  4. out_of_contrast— lstsq on length-varied NEUTRAL texts (no self/other
                      contrast anywhere in the fit set), same chat template

Margin is read at C_self's peak causal layer by the registered rule (max
restore(C_self) − restore(random) over the swept late band). Pass rule
(committed in the spec before running): margin ≥ 0.10 under ALL four variants;
any failure reopens RT-10 for adjudication.

Run from the repo root with the venv active (cloud bench: MVM_MODEL /
MVM_N_LAYERS set):
    python experiments/01-self-indexing-removal-test/src/rt10_stability.py
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
from mvm.ablate import NEUTRAL_CORPUS  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

from localize_context import render, load_stimuli  # noqa: E402
from patch_context import (  # noqa: E402
    fit_direction, restoration, run_clean, run_patched,
)

import numpy as np  # noqa: E402
from sklearn.linear_model import RidgeCV  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "prelock"
SWEEP_LAYERS = config.scale_layers([18, 20, 22, 24])
MARGIN_BAR = 0.10
RAND_SEED = 0


def lstsq_dir(X: np.ndarray, t: np.ndarray) -> np.ndarray:
    tz = (t - t.mean()) / t.std()
    d = np.linalg.lstsq(X - X.mean(0), tz, rcond=None)[0]
    return d / np.linalg.norm(d)


def ridge_dir(X: np.ndarray, t: np.ndarray) -> tuple[np.ndarray, float]:
    tz = (t - t.mean()) / t.std()
    m = RidgeCV(alphas=[0.1, 1.0, 10.0, 100.0]).fit(X - X.mean(0), tz)
    d = m.coef_
    return d / np.linalg.norm(d), float(m.alpha_)


def neutral_length_texts(tok) -> list[str]:
    """Length-varied neutral texts through the same chat template: 1..8
    neutral sentences as a user turn, generation prompt appended (readout at
    the same structural position as the stimuli — the assistant-turn start)."""
    rng = np.random.default_rng(RAND_SEED)
    texts = []
    for n in range(1, 9):
        for _ in range(6):
            picks = rng.choice(len(NEUTRAL_CORPUS), size=n, replace=False)
            content = " ".join(NEUTRAL_CORPUS[i] for i in picks)
            texts.append(tok.apply_chat_template(
                [{"role": "user", "content": content}],
                tokenize=False, add_generation_prompt=True))
    return texts


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()
    tr = [r for r in stim if r["mechanism"] == "turn_role"]
    selfs = sorted([r for r in tr if r["referent"] == "self"], key=lambda r: r["id"])
    others = sorted([r for r in tr if r["referent"] == "other"], key=lambda r: r["id"])

    def key(r):
        return (r["target"], r["id"][-1])

    omap = {key(r): r for r in others}
    pairs = [(s, omap[key(s)]) for s in selfs if key(s) in omap]
    self_str = [render(s) for s, _ in pairs]
    other_str = [render(o) for _, o in pairs]
    all_str = [render(r) for r in stim]
    print(f"{len(pairs)} matched turn_role pairs; {len(stim)} pooled stimuli")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("caching clean runs...", flush=True)
    self_resid, self_logits = run_clean(model, tok, self_str, device, n_layers)
    other_resid, other_logits = run_clean(model, tok, other_str, device, n_layers)
    pooled_resid, _ = run_clean(model, tok, all_str, device, n_layers)
    neut_str = neutral_length_texts(tok)
    neut_resid, _ = run_clean(model, tok, neut_str, device, n_layers)
    delta_logits = self_logits - other_logits

    def counts(strs):
        return np.array([len(tok(s, add_special_tokens=True)["input_ids"])
                         for s in strs], dtype=float)

    nt_pair = counts(self_str + other_str)
    nt_pool = counts(all_str)
    nt_neut = counts(neut_str)

    rng = np.random.default_rng(RAND_SEED)
    rows = []
    print(f"\n{'layer':>5}  {'C_self':>7}  {'random':>7}  "
          f"{'len:repro':>9}  {'len:pooled':>10}  {'len:ridge':>9}  {'len:ooc':>8}")
    for L in SWEEP_LAYERS:
        X = np.concatenate([self_resid[L], other_resid[L]])
        y = np.concatenate([np.ones(len(pairs)), np.zeros(len(pairs))])
        d_unit = fit_direction(X, y)
        r_unit = rng.standard_normal(d_unit.shape)
        r_unit /= np.linalg.norm(r_unit)
        scale = ((self_resid[L] @ d_unit) - (other_resid[L] @ d_unit))[:, None]

        variants = {"repro": lstsq_dir(X, nt_pair),
                    "pooled": lstsq_dir(pooled_resid[L], nt_pool)}
        variants["ridge"], alpha = ridge_dir(pooled_resid[L], nt_pool)
        variants["out_of_contrast"] = lstsq_dir(neut_resid[L], nt_neut)

        logits_c = run_patched(model, tok, other_str, device, L, scale * d_unit)
        logits_r = run_patched(model, tok, other_str, device, L, scale * r_unit)
        row = {"layer": L, "ridge_alpha": alpha,
               "restore_cself": float(restoration(logits_c, other_logits,
                                                  delta_logits).mean()),
               "restore_random": float(restoration(logits_r, other_logits,
                                                   delta_logits).mean()),
               "restore_length": {}}
        for name, d_len in variants.items():
            s_l = ((self_resid[L] @ d_len) - (other_resid[L] @ d_len))[:, None]
            logits_l = run_patched(model, tok, other_str, device, L, s_l * d_len)
            row["restore_length"][name] = float(
                restoration(logits_l, other_logits, delta_logits).mean())
        rows.append(row)
        rl = row["restore_length"]
        print(f"{L:>5}  {row['restore_cself']:>7.3f}  {row['restore_random']:>7.3f}  "
              f"{rl['repro']:>9.3f}  {rl['pooled']:>10.3f}  {rl['ridge']:>9.3f}  "
              f"{rl['out_of_contrast']:>8.3f}", flush=True)

    peak = max(rows, key=lambda r: r["restore_cself"] - r["restore_random"])
    margins = {name: peak["restore_cself"] - v
               for name, v in peak["restore_length"].items()}
    stable = all(m >= MARGIN_BAR for m in margins.values())
    print(f"\npeak causal layer {peak['layer']} "
          f"(C_self {peak['restore_cself']:.3f}, random {peak['restore_random']:.3f})")
    for name, m in margins.items():
        print(f"  margin vs {name:>15}: {m:+.3f}  "
              f"({'>=' if m >= MARGIN_BAR else '< '} {MARGIN_BAR})")
    print("=> RT-10 margin " + ("STABLE — passes under all four length fits."
                                if stable else
                                "NOT stable — at least one fit takes the margin "
                                "under the bar; RT-10 reopens for adjudication."))

    out = {"model": config.MODEL_ID, "sweep_layers": SWEEP_LAYERS,
           "margin_bar": MARGIN_BAR, "n_pairs": len(pairs),
           "peak_rule": "max restore(C_self) - restore(random) over sweep",
           "by_layer": rows, "peak_layer": peak["layer"],
           "margins_at_peak": margins, "stable": bool(stable)}
    (OUT_DIR / "rt10_stability.json").write_text(json.dumps(out, indent=2))
    print(f"saved -> {OUT_DIR / 'rt10_stability.json'}")


if __name__ == "__main__":
    main()
