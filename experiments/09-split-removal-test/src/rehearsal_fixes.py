"""The split removal test: the two free fixes (`rehearsal-fixes-method.md`).

Fix 1 removes at more layers (every layer; the earliest layers), by mean-ablation
and projection. Fix 2 swaps own and user activity (a reflection across the two
sides' midpoint) at phase 1's five layers and at every layer. Same removal check
and normal-range check as phase 1; bounds are written before any task is scored.

    HF_HOME=~/Code/minimum-viable-mind/.hf-cache.nosync HF_HUB_OFFLINE=1 \
    python3 src/rehearsal_fixes.py
"""
from __future__ import annotations

import json
import time
from contextlib import contextmanager

import numpy as np
import torch

import rehearsal_phase1 as p1
from rehearsal_phase1 import (ART, PILOT, K, METHODS, PROBE_MAX, SHUFFLES, jl, generate,
                              score, w_distractor, probe_acc, config)
from mvm.ablate import ablation_hooks, fit_layer_directions, fit_layer_subspace
from mvm.device import get_device
from mvm.model import load_model, load_tokenizer
from localize_context import render, extract_last_all_layers, margin_of
from separate_self import fit_dir

OUT_JSON = p1.HERE / "rehearsal" / "fixes-2026-10-24.json"
FIVE = [8, 11, 14, 18, 22]
N_RANDOM = 20


@contextmanager
def swap_hooks(model, spec):
    """spec: {layer: [(dir, mu_own, mu_user), ...]}; c -> mu_own + mu_user - c."""
    handles = []
    p = next(model.parameters())

    def make(triples):
        D = torch.as_tensor(np.stack([d for d, _, _ in triples]), device=p.device, dtype=torch.float32)
        s = torch.as_tensor([a + b for _, a, b in triples], device=p.device, dtype=torch.float32)

        def hook(_m, _i, out):
            h = out[0] if isinstance(out, tuple) else out
            hf = h.float()
            c = hf @ D.T
            hf = hf + (s - 2 * c) @ D
            h.copy_(hf.to(h.dtype))
            return out
        return hook

    try:
        for L, triples in spec.items():
            handles.append(model.model.layers[L].register_forward_hook(make(triples)))
        yield
    finally:
        for h in handles:
            h.remove()


def intervene(model, spec, rule):
    return swap_hooks(model, spec) if rule == "swap" else ablation_hooks(model, spec, METHODS[rule])


@torch.no_grad()
def nll_and_kl(model, tok, device, texts, spec=None, rule=None, bs=8):
    tok.padding_side = "right"
    tn = tk = 0.0
    n = 0
    for i in range(0, len(texts), bs):
        enc = tok(texts[i:i + bs], return_tensors="pt", padding=True, add_special_tokens=True).to(device)
        m = enc["attention_mask"][:, 1:].bool()
        tgt = enc["input_ids"][:, 1:]
        base = torch.log_softmax(model(**enc).logits[:, :-1].float(), -1)
        if spec is None:
            lp = base
        else:
            with intervene(model, spec, rule):
                lp = torch.log_softmax(model(**enc).logits[:, :-1].float(), -1)
        nll = -lp.gather(-1, tgt.unsqueeze(-1)).squeeze(-1)
        kl = (base.exp() * (base - lp)).sum(-1)
        tn += float(nll[m].sum()); tk += float(kl[m].sum()); n += int(m.sum())
        del base, lp
    return tn / n, tk / n


def probes_at(acts, y, groups, layers, base_acts=None):
    rng = np.random.default_rng(0)
    out = {}
    for L in layers:
        row = {}
        for kind in ("linear", "nonlinear"):
            real = probe_acc(acts[L], y, groups, kind)
            shuf = [probe_acc(acts[L], rng.permutation(y), groups, kind) for _ in range(SHUFFLES)]
            row[kind] = {"acc": real, "shuffled": float(np.mean(shuf))}
        if base_acts is not None:  # fixed probe: trained unmodified, scored intervened
            from sklearn.linear_model import LogisticRegression
            from sklearn.pipeline import make_pipeline
            from sklearn.preprocessing import StandardScaler
            clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)).fit(base_acts[L], y)
            row["fixed_probe_acc"] = float((clf.predict(acts[L]) == y).mean())
        out[L] = row
    return out


def main():
    ART.mkdir(parents=True, exist_ok=True)
    res = json.loads(OUT_JSON.read_text()) if OUT_JSON.exists() else {}
    res.update({"model": config.MODEL_ID,
                "method_file": "experiments/09-split-removal-test/rehearsal-fixes-method.md"})
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    nL = model.config.num_hidden_layers
    ALL = list(range(nL))
    t0 = time.time()
    stim = jl(PILOT / "locate.jsonl")
    neutral = json.loads((PILOT / "neutral.json").read_text())

    def sel(mech, split):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech and r["split"] == split]
        return idx, np.array([stim[i]["label"] for i in idx])

    fit_ids = [i for i, r in enumerate(stim) if r["split"] == "fit"
               and r["mechanism"] in ("turn_role", "observed_speaker")]
    tok.padding_side = "left"
    al, _ = extract_last_all_layers(model, tok, [render(stim[i]) for i in fit_ids], device, nL)
    acts = {L: np.zeros((len(stim), a.shape[1]), np.float32) for L, a in al.items()}
    for j, i in enumerate(fit_ids):
        for L in acts:
            acts[L][i] = al[L][j]
    idx_tr, y_tr = sel("turn_role", "fit")
    idx_ob, y_ob = sel("observed_speaker", "fit")

    # 1. the earliest-layer set, from the fitting items alone
    fit_acc = {L: margin_of(acts[L][idx_tr], y_tr)[0] for L in ALL}
    first = next((L for L in ALL if fit_acc[L] >= 0.95), None)
    EARLY = list(range(0, first + 1)) if first is not None else list(range(0, 8))
    res["earliest"] = {"fit_acc_by_layer": fit_acc, "first_layer_at_0.95": first, "layers": EARLY}
    print("earliest", first, EARLY, f"{time.time()-t0:.0f}s", flush=True)

    # 2. bases
    gen = fit_layer_directions(acts, idx_ob, y_ob, ALL, fit_dir)
    basis = fit_layer_subspace(acts, idx_tr, y_tr, ALL, fit_dir, K,
                               residual_against={L: d for L, (d, _) in gen.items()})
    own = [i for i, y in zip(idx_tr, y_tr) if y == 1]
    usr = [i for i, y in zip(idx_tr, y_tr) if y == 0]

    def ablate_spec(layers, src=basis):
        return {L: src[L] for L in layers}

    def swap_spec(layers, src=basis):
        return {L: [(d, float((acts[L][own] @ d).mean()), float((acts[L][usr] @ d).mean()))
                    for d, _ in src[L]] for L in layers}

    d_model = model.config.hidden_size

    def random_basis(seed, layers):
        rng = np.random.default_rng(seed)
        out = {}
        for L in layers:
            Q, _ = np.linalg.qr(rng.standard_normal((d_model, K)))
            out[L] = [(Q[:, j].astype(np.float32), float((acts[L][idx_tr] @ Q[:, j]).mean())) for j in range(K)]
        return out

    conds = {
        "every_mean": (ALL, "mean"), "every_projection": (ALL, "projection"),
        "earliest_mean": (EARLY, "mean"), "earliest_projection": (EARLY, "projection"),
        "swap_five": (FIVE, "swap"), "swap_every": (ALL, "swap"),
    }

    def spec_for(layers, rule, src=basis):
        return swap_spec(layers, src) if rule == "swap" else ablate_spec(layers, src)

    # 3. bounds and damage, written before any task is scored
    base_nll, _ = nll_and_kl(model, tok, device, neutral)
    res["baseline_nll"] = base_nll
    res.setdefault("bounds", {})
    for name, (layers, rule) in conds.items():
        if name in res["bounds"]:  # resume: bounds are deterministic (seeds 0-19), keep saved ones
            continue
        rises, kls = [], []
        for s in range(N_RANDOM):
            nll, kl = nll_and_kl(model, tok, device, neutral, spec_for(layers, rule, random_basis(s, layers)), rule)
            rises.append(nll - base_nll); kls.append(kl)
        bound = float(np.percentile(rises, 95))
        snll, skl = nll_and_kl(model, tok, device, neutral, spec_for(layers, rule), rule)
        res["bounds"][name] = {
            "layers": layers, "rule": rule, "random_rises": rises, "random_damage_kl": kls,
            "bound_95th": bound, "split_rise": snll - base_nll, "split_damage_kl": skl,
            "within_bound": (snll - base_nll) <= bound,
            "damage_over_random_median": skl / float(np.median(kls)),
        }
        print("bound", name, round(bound, 3), "rise", round(snll - base_nll, 3), "dmg x",
              round(skl / float(np.median(kls)), 1), f"{time.time()-t0:.0f}s", flush=True)
        OUT_JSON.write_text(json.dumps(res, indent=2))

    # 4. removal checks
    idx_ho, y_ho = sel("turn_role", "heldout")
    groups = np.array([stim[i]["sentence_id"] for i in idx_ho])
    ho = [render(stim[i]) for i in idx_ho]
    w = jl(PILOT / "which_did_you_say.jsonl")
    for it in w:
        it["distractor"] = w_distractor(it)
    tok.padding_side = "left"
    base_acts, _ = extract_last_all_layers(model, tok, ho, device, nL)
    wout = generate(model, tok, device, [it["turns"] for it in w], 32)
    base_w = float(np.mean([score(it, o) for it, o in zip(w, wout)]))
    res["baseline_which_did_you_say"] = base_w
    res.setdefault("checks", {})
    for name, (layers, rule) in conds.items():
        if name in res["checks"]:
            continue
        read = list(range(min(layers), nL))
        tok.padding_side = "left"
        with intervene(model, spec_for(layers, rule), rule):
            a, _ = extract_last_all_layers(model, tok, ho, device, nL)
            wo = generate(model, tok, device, [it["turns"] for it in w], 32)
        pr = probes_at(a, y_ho, groups, read, base_acts if rule == "swap" else None)
        wacc = float(np.mean([score(it, o) for it, o in zip(w, wo)]))
        other = float(np.mean([score({**it, "answer": it["distractor"], "distractor": it["answer"]}, o)
                               for it, o in zip(w, wo)]))
        hi = max(max(v["linear"]["acc"], v["nonlinear"]["acc"]) for v in pr.values())
        c = {"read_layers": read, "probes": pr, "highest_probe_acc": hi,
             "which_did_you_say_acc": wacc, "names_other_word": other,
             "probe_test_passes": hi <= PROBE_MAX, "task_test_passes": wacc <= base_w / 2}
        c["removal_check_passes"] = c["probe_test_passes"] and c["task_test_passes"]
        c["passes_both_checks"] = c["removal_check_passes"] and res["bounds"][name]["within_bound"]
        res["checks"][name] = c
        (ART / f"fixes_w_{name}.json").write_text(json.dumps(
            [{"id": it["id"], "out": o} for it, o in zip(w, wo)], indent=1))
        print("check", name, "highest probe", round(hi, 3), "W", round(wacc, 3), "other", round(other, 3),
              f"{time.time()-t0:.0f}s", flush=True)
        OUT_JSON.write_text(json.dumps(res, indent=2))
    res["elapsed_seconds"] = time.time() - t0
    OUT_JSON.write_text(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
