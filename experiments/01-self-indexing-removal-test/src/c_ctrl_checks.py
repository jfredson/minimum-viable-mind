"""C_ctrl construction checks — RT-06 (third-person) and RT-01 (frequency).

The removal test's differential needs matched controls: other-structures at
comparable decode strength and causal centrality whose ablation baselines the
damage. Two candidates, both from the context design:

  - **C_ctrl-generic** = C_speaker-generic (observed_speaker) — already
    localized (RT-09); here its OWN-context causality is measured (patching it
    on observed_speaker pairs), which RT-09 never needed.
  - **C_ctrl-expert** = the `expert_persona` contrast (RT-06's capability-
    gating persona), localized here with the same floor/null discipline.

**RT-06 verification (pre-committed, following the RT-04 precedent):** the
expert persona counts as kept-third-person iff its direction is CAUSALLY
third-person — cross-patch ratio of d_expert on the narrative and turn_role
contrasts < 0.5 of each own-patch restoration at the own peaks. Geometry
(cos / cross-decode) is reported but not decisive: v2 established that
cross-decode saturates on shared components that causal patching then shows
to be functionally subordinate. RT-06's loss condition: if d_expert
substitutes causally for C_self (ratio >= 0.5), the model has adopted the
expert persona into its own first-person self — the differential is dead on
this model class; report "not testable here yet". (On heavily-RLHF'd 2b-it
the ledger EXPECTS this to be live — either outcome is informative.)

**RT-01 frequency check (rehearsal bound, committed):** on the neutral corpus
(ablate.NEUTRAL_CORPUS), the per-token mean |coordinate| of C_self along its
direction must not exceed 2x that of a C_ctrl for the pair to count as
frequency-matched; the asymmetry is reported for every direction either way.

**Comparable-centrality check:** each C_ctrl's own-context restoration should
be within the same order as C_self-index's (>= 0.10 gap over random at its own
peak) — a control with no causal handle can't baseline anything.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/c_ctrl_checks.py
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
from separate_self import fit_dir, cv_auc, projected_auc  # noqa: E402
from patch_context import run_clean, run_patched, restoration  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
PATCH_LAYERS = [8, 14, 18, 22]
OWN_VALID_GAP = 0.10
CROSS_RATIO_MAX = 0.50
FREQ_RATIO_MAX = 2.0
RAND_SEED = 0


def pairs_by_label(stim, mech):
    rows = [r for r in stim if r["mechanism"] == mech]
    pos = sorted([r for r in rows if r["label"] == 1], key=lambda r: r["id"])
    neg = {(r["target"], r["id"][-1]): r for r in rows if r["label"] == 0}
    return [(p, neg[(p["target"], p["id"][-1])]) for p in pos
            if (p["target"], p["id"][-1]) in neg]


@torch.no_grad()
def neutral_coords(model, tok, device, d_by_layer):
    """Mean per-token |coordinate| of each direction on the neutral corpus."""
    sums = {name: 0.0 for name in d_by_layer}
    count = 0
    for t in NEUTRAL_CORPUS:
        enc = tok(t, return_tensors="pt", add_special_tokens=True).to(device)
        out = model(**enc, output_hidden_states=True)
        count += int(enc["input_ids"].shape[1])
        for name, (L, d) in d_by_layer.items():
            h = out.hidden_states[L + 1][0].float().cpu().numpy()
            sums[name] += float(np.abs(h @ d).sum())
    return {name: s / count for name, s in sums.items()}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stim = load_stimuli()

    P = {
        "index": pairs_by_label(stim, "turn_role"),
        "narrative": pairs_by_label(stim, "narrative"),
        "generic": pairs_by_label(stim, "observed_speaker"),
        "expert": pairs_by_label(stim, "expert_persona"),
    }
    for k, v in P.items():
        print(f"{k}: {len(v)} matched pairs")

    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers

    print("caching clean runs (8 sets)...")
    R = {}
    for k, pairs in P.items():
        s_str = [render(s) for s, _ in pairs]
        o_str = [render(o) for _, o in pairs]
        rs, ls = run_clean(model, tok, s_str, device, n_layers)
        ro, lo = run_clean(model, tok, o_str, device, n_layers)
        R[k] = {"s_str": s_str, "o_str": o_str, "rs": rs, "ro": ro,
                "ls": ls, "lo": lo, "delta": ls - lo}

    rng = np.random.default_rng(RAND_SEED)

    def direction(k, L):
        X = np.concatenate([R[k]["rs"][L], R[k]["ro"][L]])
        y = np.concatenate([np.ones(len(P[k])), np.zeros(len(P[k]))])
        return fit_dir(X, y), X, y

    def patch(k_ctx, d, L):
        """Restoration of context k_ctx's other-runs patched along d."""
        scale = ((R[k_ctx]["rs"][L] @ d) - (R[k_ctx]["ro"][L] @ d))[:, None]
        logits = run_patched(model, tok, R[k_ctx]["o_str"], device, L, scale * d)
        return float(restoration(logits, R[k_ctx]["lo"], R[k_ctx]["delta"]).mean())

    # --- own-causality + RT-06 cross-patches, per layer -----------------------
    print(f"\n{'layer':>5}  {'own_idx':>7} {'own_nar':>7} {'own_gen':>7} "
          f"{'own_exp':>7}  {'exp>idx':>7} {'exp>nar':>7}  {'rand_idx':>8}")
    rows = []
    for L in PATCH_LAYERS:
        d = {k: direction(k, L)[0] for k in P}
        r_u = rng.standard_normal(d["index"].shape)
        r_u /= np.linalg.norm(r_u)
        own = {k: patch(k, d[k], L) for k in P}
        exp_on_idx = patch("index", d["expert"], L)
        exp_on_nar = patch("narrative", d["expert"], L)
        scale_i = ((R["index"]["rs"][L] @ d["index"])
                   - (R["index"]["ro"][L] @ d["index"]))[:, None]
        rand_idx = float(restoration(
            run_patched(model, tok, R["index"]["o_str"], device, L, scale_i * r_u),
            R["index"]["lo"], R["index"]["delta"]).mean())
        rows.append({"layer": L, **{f"own_{k}": v for k, v in own.items()},
                     "expert_on_index": exp_on_idx,
                     "expert_on_narrative": exp_on_nar,
                     "random_index_ctx": rand_idx})
        print(f"{L:>5}  {own['index']:>7.3f} {own['narrative']:>7.3f} "
              f"{own['generic']:>7.3f} {own['expert']:>7.3f}  "
              f"{exp_on_idx:>7.3f} {exp_on_nar:>7.3f}  {rand_idx:>8.3f}")

    # --- read at own peaks (pre-committed convention) --------------------------
    def peak(key):
        return max(rows, key=lambda r: r[key])

    pk_i, pk_n = peak("own_index"), peak("own_narrative")
    pk_g, pk_e = peak("own_generic"), peak("own_expert")
    # random restorations are ~0.00 in every run to date, so the centrality bar
    # is the absolute own-peak restoration (same 0.10 magnitude convention).
    centrality = {
        "generic": pk_g["own_generic"] >= OWN_VALID_GAP,
        "expert": pk_e["own_expert"] >= OWN_VALID_GAP,
    }
    ratio_exp_idx = (pk_i["expert_on_index"] / pk_i["own_index"]
                     if pk_i["own_index"] > 0 else None)
    ratio_exp_nar = (pk_n["expert_on_narrative"] / pk_n["own_narrative"]
                     if pk_n["own_narrative"] > 0 else None)
    rt06_third_person = (ratio_exp_idx is not None and ratio_exp_idx < CROSS_RATIO_MAX
                         and ratio_exp_nar is not None
                         and ratio_exp_nar < CROSS_RATIO_MAX)

    # geometry, reported not decisive
    L_geo = pk_n["layer"]
    d_geo = {k: direction(k, L_geo)[0] for k in P}
    _, Xn, yn = direction("narrative", L_geo)
    _, Xi, yi = direction("index", L_geo)
    geo = {
        "layer": L_geo,
        "cos_expert_narrative": abs(float(d_geo["expert"] @ d_geo["narrative"])),
        "cos_expert_index": abs(float(d_geo["expert"] @ d_geo["index"])),
        "crossdecode_expert_on_narrative": projected_auc(Xn, yn, d_geo["expert"]),
        "crossdecode_expert_on_index": projected_auc(Xi, yi, d_geo["expert"]),
        "own_auc_expert": cv_auc(*direction("expert", L_geo)[1:]),
    }

    # --- RT-01 frequency on the neutral corpus --------------------------------
    d_by = {
        "C_self_index": (pk_i["layer"], direction("index", pk_i["layer"])[0]),
        "C_self_narrative": (pk_n["layer"], direction("narrative", pk_n["layer"])[0]),
        "C_ctrl_generic": (pk_g["layer"], direction("generic", pk_g["layer"])[0]),
        "C_ctrl_expert": (pk_e["layer"], direction("expert", pk_e["layer"])[0]),
    }
    freq = neutral_coords(model, tok, device, d_by)
    freq_ratios = {
        f"{s}/{c}": freq[s] / freq[c]
        for s in ("C_self_index", "C_self_narrative")
        for c in ("C_ctrl_generic", "C_ctrl_expert")
    }
    freq_ok = {k: bool(v <= FREQ_RATIO_MAX and v >= 1 / FREQ_RATIO_MAX)
               for k, v in freq_ratios.items()}

    print(f"\nRT-06 (causal third-person check): expert->index ratio "
          f"{ratio_exp_idx:.3f}, expert->narrative ratio {ratio_exp_nar:.3f} "
          f"(bar < {CROSS_RATIO_MAX})")
    print("=> " + ("expert persona stays functionally THIRD-PERSON — usable as "
                   "capability-gating C_ctrl" if rt06_third_person else
                   "expert persona substitutes for C_self — RT-06 loss "
                   "condition LIVE on this model: differential not testable "
                   "here; report, do not force"))
    print(f"   geometry at L{L_geo} (reported): |cos| exp-nar "
          f"{geo['cos_expert_narrative']:.2f}, exp-idx {geo['cos_expert_index']:.2f}; "
          f"cross-decode exp->nar {geo['crossdecode_expert_on_narrative']:.2f}, "
          f"exp->idx {geo['crossdecode_expert_on_index']:.2f}")
    print(f"comparable centrality: generic {pk_g['own_generic']:.3f} "
          f"({'ok' if centrality['generic'] else 'WEAK'}), "
          f"expert {pk_e['own_expert']:.3f} "
          f"({'ok' if centrality['expert'] else 'WEAK'})")
    print("RT-01 neutral-corpus mean |coord|/token: "
          + ", ".join(f"{k} {v:.2f}" for k, v in freq.items()))
    print("   ratios: " + ", ".join(f"{k} {v:.2f}{'' if freq_ok[k] else ' (BREACH)'}"
                                    for k, v in freq_ratios.items()))

    out = {
        "model": config.MODEL_ID,
        "conventions": {"own_valid_gap": OWN_VALID_GAP,
                        "cross_ratio_max": CROSS_RATIO_MAX,
                        "freq_ratio_max": FREQ_RATIO_MAX,
                        "rt06_decision": "causal cross-patch ratios at own peaks; "
                                         "geometry reported, not decisive "
                                         "(RT-04 precedent)"},
        "patch_layers": PATCH_LAYERS,
        "by_layer": rows,
        "peaks": {"index": pk_i, "narrative": pk_n, "generic": pk_g,
                  "expert": pk_e},
        "rt06": {"ratio_expert_on_index": ratio_exp_idx,
                 "ratio_expert_on_narrative": ratio_exp_nar,
                 "third_person": bool(rt06_third_person), "geometry": geo},
        "centrality_ok": centrality,
        "rt01_freq_mean_abs_coord": freq,
        "rt01_freq_ratios": freq_ratios,
        "rt01_freq_ok": freq_ok,
        "caveats": "n=24 pairs/context; single behavioural metric; rehearsal "
                   "bounds (2x freq, 0.5 ratio) — registered bounds get set "
                   "with pilot data on the registered substrate.",
    }
    (OUT_DIR / "c_ctrl_checks.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 'c_ctrl_checks.json'}")


if __name__ == "__main__":
    main()
