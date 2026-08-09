"""RT-08 gate run (iii) — the post-training fingerprint detector.

FIRED 2026-08-08 against the v1.0 on-policy pipeline (both arms, both
positive controls — `fingerprint-gate-findings.md`), which retired that
pipeline: amendment A1 replaced on-policy fill with ENACTMENT (own-turn
values drawn from the generator's own distribution; authorship carried
by the acting channel, `train.enact_batched`). This run now audits the
A1 pipeline: episodes whose own turns the checkpoint enacted must carry
no ownership fingerprint. Under A1 the clean arms should read chance
for information-theoretic reasons (uniform draws are exchangeable with
generator turns) — the run's job is to verify the implementation
delivers that, with the retired policy pipeline serving as a positive
control that the instruments still have teeth.

Two arms, both under the pre-committed equivalence bound (AUC 95% CI
within [0.45, 0.55], n = 4000 episodes); the gate passes only if BOTH
arms are clean and EVERY positive control fires:

- **Arm A — committed family.** Runs (i)/(ii)'s exact detector (char
  tfidf + positional feats, logistic C=1.0) on enacted episodes.
  Positive control: a degenerate constant-value filler.
- **Arm B — likelihood attack.** Score every turn's value token under
  the model's own policy (plain forward, no injections — the attacker
  does not know which positions were enacted; assuming them would
  presuppose the answer); AUC of that score for own-vs-other turns.
  Positive controls: greedy (argmax) fill, and **policy-sampled fill —
  the retired v1.0 pipeline, which this gate killed and must keep
  catching** [A1.4].

Fresh episode seeds (base 20260808) — disjoint from training stream
(seed*1e6+step), held-out eval (987654321), and the frozen batteries
(20260804), which this run never touches.

    ../../../.venv/bin/python fingerprint_gate.py --run
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch

import curriculum as C
import encoding as E
from cue_detector import (N_EPISODES, EQUIV_LO, EQUIV_HI,
                          POSITIVE_CONTROL_MIN_AUC, N_BOOT,
                          build_examples, fit_auc, boot_ci)
from model import MVM0aModel, Config, to_torch
from train import policy_fill_batched

import random as _random

SEED = 20260808
CKPT = Path(__file__).resolve().parents[1] / "artifacts" / \
    "pilot-a1-10m-seed0" / "pilot_a1_10m_seed0.pt"


def load_pilot(device: str) -> MVM0aModel:
    ck = torch.load(CKPT, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device)
    model.load_state_dict(ck["state"])
    model.eval()
    return model


def fill_all(model, eps, device, batch=256, mode="enact", seed=0):
    """Fill own turns: 'enact' = the A1 pipeline (generator-distribution
    draws — the object under test); 'constant' = degenerate filler (arm A
    positive control); 'greedy' = argmax fill (arm B positive control);
    'policy' = the retired v1.0 on-policy fill (arm B positive control —
    the pipeline this gate killed and must keep catching)."""
    if mode == "constant":
        for e in eps:
            for t in e.turns:
                if t.agent == e.own_slot:
                    t.value = C.SLOTS[0]
            C.rederive_queries_after_fill(e)
        return eps
    if mode == "enact":
        rng = _random.Random(seed + 13)
        for e in eps:
            C.enact_own_turns(e, rng)
        return eps
    if mode == "greedy":
        torch.manual_seed(0)          # greedy is deterministic anyway
    for i in range(0, len(eps), batch):
        chunk = eps[i:i + batch]
        if mode == "greedy":
            _greedy_fill(model, chunk, device)
        else:
            policy_fill_batched(model, chunk, device)
    return eps


@torch.no_grad()
def _greedy_fill(model, eps, device):
    slot_ids = torch.tensor([E.VOCAB[s] for s in C.SLOTS], device=device)
    own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
               for e in eps]
    for k in range(max(len(o) for o in own_idx)):
        b = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
        logits = model.forward(b)
        for j, e in enumerate(eps):
            if k >= len(own_idx[j]):
                continue
            ti = own_idx[j][k]
            span = (b["turn_ids"][j] == ti).nonzero().flatten()
            row = logits[j, int(span[-1]) - 2][slot_ids]
            e.turns[ti].value = C.SLOTS[int(row.argmax())]
    for e in eps:
        C.rederive_queries_after_fill(e)


@torch.no_grad()
def value_logprobs(model, eps, device, batch=256) -> list[np.ndarray]:
    """Per episode: log p(value_token | prefix) under the model for every
    turn, read at the 'to' position. The likelihood-attack feature."""
    out = []
    for i in range(0, len(eps), batch):
        chunk = eps[i:i + batch]
        b = to_torch(E.collate([E.encode_episode(e) for e in chunk]), device)
        logp = torch.log_softmax(model.forward(b), dim=-1)
        for j, e in enumerate(chunk):
            vals = []
            for ti in range(len(e.turns)):
                span = (b["turn_ids"][j] == ti).nonzero().flatten()
                pos = int(span[-1]) - 2            # 'to' predicts the value
                vid = E.VOCAB[e.turns[ti].value]
                vals.append(float(logp[j, pos, vid]))
            out.append(np.array(vals))
    return out


def arm_a(model, n_episodes, seed, device) -> dict:
    def run(mode):
        eps = C.generate_balanced(n_episodes, seed, forced_revision_frac=0.25)
        fill_all(model, eps, device, mode=mode, seed=seed)
        texts, feats, labels = build_examples(eps, seed=seed)
        auc, y, p = fit_auc(texts, feats, labels, seed)
        lo, hi = boot_ci(y, p, N_BOOT, seed)
        return {"mode": mode, "n_examples": len(labels),
                "auc": round(float(auc), 4),
                "ci95": [round(float(lo), 4), round(float(hi), 4)]}
    clean, pc = run("enact"), run("constant")
    return {"arm": "A committed family on enacted text [A1]",
            "clean": clean, "positive_control": pc,
            "clean_pass": EQUIV_LO <= clean["ci95"][0]
            and clean["ci95"][1] <= EQUIV_HI,
            "pc_pass": pc["auc"] >= POSITIVE_CONTROL_MIN_AUC}


def arm_b(model, n_episodes, seed, device) -> dict:
    def run(mode):
        rng = np.random.default_rng(seed)
        eps = C.generate_balanced(n_episodes, seed + 1,
                                  forced_revision_frac=0.25)
        fill_all(model, eps, device, mode=mode, seed=seed)
        lps = value_logprobs(model, eps, device)
        scores, labels = [], []
        for e, lp in zip(eps, lps):
            own = [i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
            oth = [i for i, t in enumerate(e.turns) if t.agent != e.own_slot]
            if not own or not oth:
                continue
            scores += [lp[own[int(rng.integers(len(own)))]],
                       lp[oth[int(rng.integers(len(oth)))]]]
            labels += [1, 0]
        y, s = np.array(labels), np.array(scores)
        from sklearn.metrics import roc_auc_score
        auc = roc_auc_score(y, s)
        lo, hi = boot_ci(y, s, N_BOOT, seed)
        return {"mode": mode, "n_examples": len(y),
                "auc": round(float(auc), 4),
                "ci95": [round(float(lo), 4), round(float(hi), 4)]}
    clean, pc_g, pc_p = run("enact"), run("greedy"), run("policy")
    return {"arm": "B likelihood attack (model-scored values) [A1]",
            "clean": clean, "positive_control": pc_g,
            "positive_control_policy": pc_p,
            "clean_pass": EQUIV_LO <= clean["ci95"][0]
            and clean["ci95"][1] <= EQUIV_HI,
            "pc_pass": pc_g["auc"] >= POSITIVE_CONTROL_MIN_AUC
            and pc_p["auc"] >= POSITIVE_CONTROL_MIN_AUC}


def run_gate(n_episodes: int = N_EPISODES, seed: int = SEED,
             device: str | None = None) -> dict:
    device = device or ("mps" if torch.backends.mps.is_available() else "cpu")
    torch.manual_seed(seed)
    model = load_pilot(device)
    a, b = arm_a(model, n_episodes, seed, device), \
        arm_b(model, n_episodes, seed, device)
    ok = a["clean_pass"] and a["pc_pass"] and b["clean_pass"] and b["pc_pass"]
    import hashlib
    md5 = hashlib.md5(CKPT.read_bytes()).hexdigest()
    return {
        "run": "(iii) post-training rollout fingerprint [A1 pipeline]",
        "params": {"n_episodes": n_episodes, "seed": seed,
                   "checkpoint": CKPT.name,
                   "checkpoint_md5": md5,
                   "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                   "positive_control_min_auc": POSITIVE_CONTROL_MIN_AUC},
        "arms": [a, b],
        "GATE": "PASS" if ok else "FAIL",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--n-episodes", type=int, default=N_EPISODES)
    args = ap.parse_args()
    if not args.run:
        ap.print_help()
        return
    res = run_gate(n_episodes=args.n_episodes)
    out = Path(__file__).resolve().parents[1] / "cue_detector_gate.json"
    full = json.loads(out.read_text())
    full["runs"] = [r for r in full["runs"]
                    if not r["run"].startswith("(iii)")] + [res]
    full["GATE"] = "PASS" if all(r["GATE"] == "PASS"
                                 for r in full["runs"]) else "FAIL"
    full.pop("pending_runs", None)
    out.write_text(json.dumps(full, indent=2))
    print(json.dumps(res, indent=2))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
