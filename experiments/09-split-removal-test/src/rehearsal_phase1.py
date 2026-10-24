"""The split removal test: measurement rehearsal, phase 1 (`rehearsal-method.md`).

Runs in the method's order: locate (step 2), the two removal methods (step 3),
the normal-range bound (step 5) and the split's damage (step 6), written to disk
first; then the removal check (step 4); then the baseline checks (step 1).

    HF_HOME=~/Code/minimum-viable-mind/.hf-cache.nosync \
    HF_TOKEN_PATH=~/.cache/huggingface/token \
    python3 src/rehearsal_phase1.py [steps]      # steps: a comma list, default all

Results: rehearsal/phase1-2026-10-24.json (committed); per-item outputs under
artifacts/split_rehearsal/ (gitignored).
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REPO = HERE.parents[1]
EXP01 = REPO / "experiments" / "01-self-indexing-removal-test" / "src"
sys.path.insert(0, str(EXP01))
sys.path.insert(0, str(REPO / "src"))

from mvm import config  # noqa: E402
from mvm.ablate import ablation_hooks, fit_layer_directions, fit_layer_subspace  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402
from localize_context import render, extract_last_all_layers, margin_of  # noqa: E402
from separate_self import fit_dir  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import GroupKFold  # noqa: E402
from sklearn.neural_network import MLPClassifier  # noqa: E402
from sklearn.pipeline import make_pipeline  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

PILOT = HERE / "batteries" / "pilot"
OUT_JSON = HERE / "rehearsal" / "phase1-2026-10-24.json"
ART = config.ARTIFACTS_DIR / "split_rehearsal"
LAYERS = [8, 11, 14, 18, 22]
K = 16
READ_LAYERS = list(range(8, 26))
N_RANDOM = 20
PROBE_MAX = 0.55
SHUFFLES = 5
METHODS = {"mean": "mean", "projection": "directional"}


def jl(path):
    return [json.loads(l) for l in open(path) if l.strip()]


def load_results():
    return json.loads(OUT_JSON.read_text()) if OUT_JSON.exists() else {}


def save_results(res):
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(res, indent=2))


# ---------------------------------------------------------------- scoring ---
_ANS = re.compile(r"answer\s*:", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def answer_region(out):
    parts = _ANS.split(out)
    return parts[-1] if len(parts) > 1 else None


def score(item, out):
    """Strict: only the text after the last 'Answer:' counts; no marker is wrong."""
    reg = answer_region(out)
    if reg is None:
        return False
    words = norm(reg).split()
    if norm(item["answer"]) not in words:
        return False
    other = item.get("distractor")
    return not (other and norm(other) in words)


def w_distractor(item):
    a, b = re.findall(r"'([^']+)' and '([^']+)'", item["turns"][-1][1])[0]
    return b if item["answer"] == a else a


# ------------------------------------------------------------- generation ---
def chat_text(tok, turns):
    role = {"user": "user", "model": "assistant"}
    chat = [{"role": role[r], "content": c} for r, c in turns]
    return tok.apply_chat_template(chat, add_generation_prompt=True, tokenize=False)


@torch.no_grad()
def generate(model, tok, device, turn_lists, max_new, n=1, temp=None, bs=16, seed=1):
    tok.padding_side = "left"
    outs = []
    texts = [chat_text(tok, t) for t in turn_lists]
    step = max(1, bs // n)
    for i in range(0, len(texts), step):
        enc = tok(texts[i:i + step], return_tensors="pt", padding=True,
                  add_special_tokens=False).to(device)
        kw = dict(max_new_tokens=max_new, pad_token_id=tok.pad_token_id)
        if temp:
            torch.manual_seed(seed + i)
            kw.update(do_sample=True, temperature=temp, top_p=1.0, top_k=0,
                      num_return_sequences=n)
        else:
            kw.update(do_sample=False)
        g = model.generate(**enc, **kw)
        dec = tok.batch_decode(g[:, enc["input_ids"].shape[1]:], skip_special_tokens=True)
        if n > 1:
            outs.extend([dec[j * n:(j + 1) * n] for j in range(len(dec) // n)])
        else:
            outs.extend(dec)
    return outs


# --------------------------------------------------------- neutral text -----
@torch.no_grad()
def nll_and_kl(model, tok, device, texts, dirs=None, mode=None, bs=8):
    """Mean per-token NLL with the removal on, and mean KL(base || removed)
    per position. Baseline is recomputed per batch so no logits are stored."""
    tok.padding_side = "right"
    tot_nll = tot_kl = 0.0
    n_tok = 0
    for i in range(0, len(texts), bs):
        enc = tok(texts[i:i + bs], return_tensors="pt", padding=True,
                  add_special_tokens=True).to(device)
        m = enc["attention_mask"][:, 1:].bool()
        tgt = enc["input_ids"][:, 1:]
        base = torch.log_softmax(model(**enc).logits[:, :-1].float(), -1)
        if dirs is None:
            lp = base
        else:
            with ablation_hooks(model, dirs, mode):
                lp = torch.log_softmax(model(**enc).logits[:, :-1].float(), -1)
        nll = -lp.gather(-1, tgt.unsqueeze(-1)).squeeze(-1)
        kl = (base.exp() * (base - lp)).sum(-1)
        tot_nll += float(nll[m].sum())
        tot_kl += float(kl[m].sum())
        n_tok += int(m.sum())
        del base, lp
    return tot_nll / n_tok, tot_kl / n_tok


# ------------------------------------------------------------------ probes --
def probe_acc(X, y, groups, kind, seed=0):
    if kind == "linear":
        clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=1.0))
    else:
        clf = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(64,),
                            max_iter=2000, random_state=seed))
    correct = 0
    for tr, te in GroupKFold(n_splits=5).split(X, y, groups):
        clf.fit(X[tr], y[tr])
        correct += int((clf.predict(X[te]) == y[te]).sum())
    return correct / len(y)


def probe_layers(acts, y, groups):
    rng = np.random.default_rng(0)
    out = {}
    for L in READ_LAYERS:
        row = {}
        for kind in ("linear", "nonlinear"):
            real = probe_acc(acts[L], y, groups, kind)
            shuf = []
            for _ in range(SHUFFLES):
                # shuffle labels within the grouping so folds stay by sentence
                shuf.append(probe_acc(acts[L], rng.permutation(y), groups, kind))
            row[kind] = {"acc": real, "shuffled": float(np.mean(shuf))}
        out[L] = row
    return out


# -------------------------------------------------------------------- main --
def main(steps):
    ART.mkdir(parents=True, exist_ok=True)
    res = load_results()
    res.setdefault("model", config.MODEL_ID)
    res.setdefault("method_file", "experiments/09-split-removal-test/rehearsal-method.md")
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    n_layers = model.config.num_hidden_layers
    t0 = time.time()

    stim = jl(PILOT / "locate.jsonl")
    neutral = json.loads((PILOT / "neutral.json").read_text())

    def sel(mech, split):
        idx = [i for i, r in enumerate(stim) if r["mechanism"] == mech and r["split"] == split]
        return idx, np.array([stim[i]["label"] for i in idx])

    # ---- step 2: locate ----------------------------------------------------
    fit_ids = [i for i, r in enumerate(stim) if r["split"] == "fit"
               and r["mechanism"] in ("turn_role", "observed_speaker")]
    strings = [render(stim[i]) for i in fit_ids]
    tok.padding_side = "left"
    acts_l, emb_l = extract_last_all_layers(model, tok, strings, device, n_layers)
    acts = {L: np.zeros((len(stim), a.shape[1]), np.float32) for L, a in acts_l.items()}
    emb = np.zeros((len(stim), emb_l.shape[1]), np.float32)
    for j, i in enumerate(fit_ids):
        emb[i] = emb_l[j]
        for L in acts:
            acts[L][i] = acts_l[L][j]
    idx_tr, y_tr = sel("turn_role", "fit")
    idx_ob, y_ob = sel("observed_speaker", "fit")
    gen = fit_layer_directions(acts, idx_ob, y_ob, LAYERS, fit_dir)
    split_dirs = fit_layer_subspace(acts, idx_tr, y_tr, LAYERS, fit_dir, K,
                                    residual_against={L: d for L, (d, _) in gen.items()})
    emb_real, emb_null, emb_margin = margin_of(emb[idx_tr], y_tr)
    res["step2_locate"] = {
        "fit_items": len(idx_tr), "layers": LAYERS, "rank": K,
        "layer0_check": {"real": emb_real, "shuffled": emb_null, "margin": emb_margin,
                         "passes": emb_margin <= 0.10},
        "fit_margin_by_layer": {L: margin_of(acts[L][idx_tr], y_tr)[2] for L in LAYERS},
    }
    print("step 2", res["step2_locate"]["layer0_check"], f"{time.time()-t0:.0f}s", flush=True)
    save_results(res)

    # mean coordinates for random bases come from the same fitting items
    d_model = model.config.hidden_size

    def random_dirs(seed):
        rng = np.random.default_rng(seed)
        out = {}
        for L in LAYERS:
            Q, _ = np.linalg.qr(rng.standard_normal((d_model, K)))
            X = acts[L][idx_tr]
            out[L] = [(Q[:, j].astype(np.float32), float((X @ Q[:, j]).mean())) for j in range(K)]
        return out

    # ---- steps 5 and 6: normal-range bound and the split's damage ----------
    if "bound" in steps:
        base_nll, _ = nll_and_kl(model, tok, device, neutral)
        b = {"baseline_nll": base_nll, "methods": {}}
        for mname, mode in METHODS.items():
            rises, kls = [], []
            for s in range(N_RANDOM):
                nll, kl = nll_and_kl(model, tok, device, neutral, random_dirs(s), mode)
                rises.append(nll - base_nll)
                kls.append(kl)
            bound = float(np.percentile(rises, 95))
            snll, skl = nll_and_kl(model, tok, device, neutral, split_dirs, mode)
            b["methods"][mname] = {
                "random_rises": rises, "random_damage_kl": kls, "bound_95th": bound,
                "split_rise": snll - base_nll, "split_damage_kl": skl,
                "room_under_bound": bound - (snll - base_nll),
                "split_within_bound": (snll - base_nll) <= bound,
                "random_damage_median": float(np.median(kls)),
                "split_damage_over_random_median": skl / float(np.median(kls)),
            }
            print("bound", mname, {k: v for k, v in b["methods"][mname].items()
                                   if not isinstance(v, list)}, f"{time.time()-t0:.0f}s", flush=True)
        b["written_at"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
        res["step5_6_bound_and_damage"] = b
        save_results(res)

    # ---- step 4: the removal check -----------------------------------------
    if "check" in steps:
        idx_ho, y_ho = sel("turn_role", "heldout")
        groups = np.array([stim[i]["sentence_id"] for i in idx_ho])
        ho_strings = [render(stim[i]) for i in idx_ho]
        witems = jl(PILOT / "which_did_you_say.jsonl")
        for w in witems:
            w["distractor"] = w_distractor(w)
        chk = {"heldout_items": len(idx_ho), "read_layers": READ_LAYERS, "conditions": {}}
        for cond, spec in [("baseline", None)] + [(m, md) for m, md in METHODS.items()]:
            tok.padding_side = "left"
            if spec is None:
                a, _ = extract_last_all_layers(model, tok, ho_strings, device, n_layers)
                wout = generate(model, tok, device, [w["turns"] for w in witems], 32)
            else:
                with ablation_hooks(model, split_dirs, spec):
                    a, _ = extract_last_all_layers(model, tok, ho_strings, device, n_layers)
                    wout = generate(model, tok, device, [w["turns"] for w in witems], 32)
            probes = probe_layers(a, y_ho, groups)
            wacc = float(np.mean([score(w, o) for w, o in zip(witems, wout)]))
            worst = max(max(v["linear"]["acc"], v["nonlinear"]["acc"]) for v in probes.values())
            chk["conditions"][cond] = {"probes": probes, "highest_probe_acc": worst,
                                       "which_did_you_say_acc": wacc}
            (ART / f"w_outputs_{cond}.json").write_text(json.dumps(
                [{"id": w["id"], "out": o, "ok": score(w, o)} for w, o in zip(witems, wout)], indent=1))
            print("check", cond, "highest probe", round(worst, 3), "W acc", round(wacc, 3),
                  f"{time.time()-t0:.0f}s", flush=True)
        base_w = chk["conditions"]["baseline"]["which_did_you_say_acc"]
        for m in METHODS:
            c = chk["conditions"][m]
            c["probe_test_passes"] = c["highest_probe_acc"] <= PROBE_MAX
            c["task_test_passes"] = c["which_did_you_say_acc"] <= base_w / 2
            c["removal_check_passes"] = c["probe_test_passes"] and c["task_test_passes"]
        res["step4_removal_check"] = chk
        save_results(res)

    # ---- step 1: baseline checks -------------------------------------------
    if "baseline" in steps:
        items = jl(PILOT / "routine.jsonl") + jl(PILOT / "prompt_rule.jsonl")
        greedy = generate(model, tok, device, [it["turns"] for it in items], 96)
        print("baseline greedy done", f"{time.time()-t0:.0f}s", flush=True)
        samples = generate(model, tok, device, [it["turns"] for it in items], 96,
                           n=10, temp=0.7, bs=40, seed=1)
        print("baseline samples done", f"{time.time()-t0:.0f}s", flush=True)
        pitems = [it for it in items if it["cell"] == "P"]
        norule = generate(model, tok, device, [it["turns_no_rule"] for it in pitems], 96)
        rows = []
        for it, g, ss in zip(items, greedy, samples):
            rows.append({"id": it["id"], "cell": it["cell"], "kind": it["kind"],
                         "greedy_ok": score(it, g), "passes_of_10": sum(score(it, s) for s in ss)})
        nr = {it["id"]: (score(it, o), o) for it, o in zip(pitems, norule)}
        (ART / "baseline_outputs.json").write_text(json.dumps(
            [{"id": it["id"], "greedy": g, "samples": ss, "no_rule": nr.get(it["id"], (None, None))[1]}
             for it, g, ss in zip(items, greedy, samples)], indent=1))
        chance = {"p_operator": 0.0, "p_cipher": 0.0}
        kinds = {}
        for k in sorted({r["kind"] for r in rows}):
            kr = [r for r in rows if r["kind"] == k]
            kept = [r for r in kr if r["greedy_ok"] and r["passes_of_10"] >= 9]
            entry = {"candidates": len(kr), "greedy_acc": float(np.mean([r["greedy_ok"] for r in kr])),
                     "kept_confident": len(kept)}
            if k.startswith("p_"):
                its = [it for it in pitems if it["kind"] == k]
                acc_nr = float(np.mean([nr[it["id"]][0] for it in its]))
                if k in chance:
                    ch = chance[k]
                else:
                    sizes = [len(re.findall(r"(?:list is|in this order): (.*?)(?:\.| \(after)", it["turns"][0][1])[0].split(", "))
                             for it in its]
                    ch = float(np.mean([1 / s for s in sizes]))
                entry.update({"no_rule_acc": acc_nr, "chance": ch,
                              "rule_needed": acc_nr <= ch + 0.10})
                if k == "p_operator":
                    plain = 0
                    for it in its:
                        a, b = map(int, re.findall(r"What is (\d+) \S+ (\d+)\?", it["turns"][0][1])[0])
                        reg = answer_region(nr[it["id"]][1]) or ""
                        plain += str(a + b) in norm(reg).split()
                    entry["no_rule_plain_sum_share"] = plain / len(its)
            kinds[k] = entry
        dropped = [k for k, e in kinds.items() if k.startswith("p_") and not e["rule_needed"]]
        keep = [r for r in rows if r["greedy_ok"] and r["passes_of_10"] >= 9 and r["kind"] not in dropped]
        rng = np.random.default_rng(1)
        matched = {"R": [], "P": []}
        for bin_ in (9, 10):
            R = [r["id"] for r in keep if r["cell"] == "R" and r["passes_of_10"] == bin_]
            P = [r["id"] for r in keep if r["cell"] == "P" and r["passes_of_10"] == bin_]
            n = min(len(R), len(P))
            matched["R"] += sorted(rng.choice(R, n, replace=False).tolist()) if n else []
            matched["P"] += sorted(rng.choice(P, n, replace=False).tolist()) if n else []
        res["step1_baseline"] = {
            "kinds": kinds, "dropped_prompt_rule_kinds": dropped,
            "matched_counts": {c: len(v) for c, v in matched.items()},
            "cell_usable": {c: len(v) >= 40 for c, v in matched.items()},
            "matched_ids": matched,
        }
        save_results(res)
        print("baseline", json.dumps({k: v for k, v in res["step1_baseline"].items() if k != "matched_ids"}, indent=1))
    res["elapsed_seconds_last_run"] = time.time() - t0
    save_results(res)


if __name__ == "__main__":
    main(sys.argv[1].split(",") if len(sys.argv) > 1 else ["bound", "check", "baseline"])
