"""A3 Gate 3 — the post-training fingerprint detector, act-withheld.

The claim this audits: episodes whose own turns an A3 checkpoint enacted
must carry no ownership fingerprint. If they do, the model could tell
which turns were its own from the data rather than from the acting
channel, and the whole design collapses. The registered gate killed a
previous pipeline this way (`fingerprint-gate-findings.md`), so it has
teeth and a history of using them.

Two arms, both under the pre-committed equivalence bound — the bootstrap
95% interval on the area under the curve contained in [0.45, 0.55] — with
every positive control required to fire above 0.70.

**Arm A, the committed classifier family.** The A3 cue detector run over
enacted episodes. Sampling follows the 2026-09-15 amendment: both arms
drawn agent-first, and both samplers reported side by side.

**Arm B, the likelihood attack, act-withheld.** Score every turn's value
token under the model's own policy on a plain forward pass with **no
acting-channel injections at all**. A3 §3.4 makes that explicit and it
matters more here than it did before. Under A3 the policy at a revision
position is perspectival: the model predicts the successor of *its own*
earlier value. Scoring another agent's revision under that policy with
injections present would show low likelihood, and the attack would read
that as a fingerprint. It is not one. It is the model's ownership
knowledge showing through its policy, which is exactly what the design
intends and what a token-only solver cannot have. Withholding the
injections removes that false positive and leaves the real question: do
the *data* carry an ownership cue?

**"Uncertifiable" is a real third outcome, and it is routed.** The
positive control for this arm demonstrated sensitivity on only one of
four earlier checkpoints. If the controls do not fire, the arm is
declared uncertifiable rather than passed or failed, per the registration
revision of 2026-09-15 (decision 12). A gate that cannot tell a clean
result from a blind instrument must say so rather than bless either.

Fresh episode seeds, disjoint from the training stream, the held-out
evaluation and the frozen batteries, none of which this run touches.

Corrigibility: inference only, local checkpoint, $0 [C1/C2].

    ../../../.venv/bin/python fingerprint_gate_a3.py --self-test
    ../../../.venv/bin/python fingerprint_gate_a3.py --ckpt <path> --run
"""
from __future__ import annotations

import argparse
import json
import random as _random
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import roc_auc_score

import curriculum_a3 as A
import encoding_a3 as E
import cue_detector_a3 as D
from cue_detector import (EQUIV_LO, EQUIV_HI, POSITIVE_CONTROL_MIN_AUC,
                          N_BOOT, boot_ci)
from model import MVM0aModel, Config, to_torch

N_EPISODES = 4000
SEED = 20260916
SLOT_IDS = [E.VOCAB[s] for s in A.SLOTS]


def load(ckpt: str, device: str):
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    m = MVM0aModel(Config(**ck["cfg"])).to(device)
    m.load_state_dict(ck["state"])
    return m.eval()


def fill_all(model, eps, device, mode="enact", seed=0, batch=200):
    """'enact' is the pipeline under test: own-turn values drawn from the
    generator's own distribution and the revision set by the shared rule.
    'constant' and 'policy' are deliberately leaky positive controls."""
    if mode == "enact":
        rng = _random.Random(seed + 13)
        for e in eps:
            A.enact_own_turns(e, rng)
        return eps
    if mode == "constant":
        for e in eps:
            for t in e.turns:
                if t.agent == e.own_slot:
                    t.value = A.SLOTS[0]
        return eps
    # 'greedy'  = argmax fill, the registered PRIMARY control for the
    #             likelihood arm: own values become the ones the model
    #             itself considers most likely, so their log-probability
    #             is systematically high and a likelihood attack must see
    #             it. A constant fill does NOT serve here — it changes
    #             which value appears, not how likely the model finds it,
    #             so it leaves the attack blind. Using it as arm B's
    #             control was an error in the first version of this file
    #             and produced a spurious "uncertifiable" verdict.
    # 'policy'  = sampled fill, the retired pipeline this gate killed.
    g = torch.Generator().manual_seed(seed)
    for i in range(0, len(eps), batch):
        chunk = eps[i:i + batch]
        b = to_torch(E.collate([E.encode_episode(e) for e in chunk]), device)
        with torch.no_grad():
            logits = model.forward(b)
        ids = torch.tensor(SLOT_IDS, device=logits.device)
        for j, e in enumerate(chunk):
            for ti, t in enumerate(e.turns):
                if t.agent != e.own_slot:
                    continue
                span = (b["turn_ids"][j] == ti).nonzero().flatten()
                pos = int(span[0]) + A.VALUE_WORD_IDX - 1
                row = logits[j, pos][ids]
                if mode == "greedy":
                    t.value = A.SLOTS[int(row.argmax())]
                else:
                    pr = torch.softmax(row, dim=-1).cpu()
                    t.value = A.SLOTS[int(torch.multinomial(pr, 1,
                                                            generator=g))]
    return eps


@torch.no_grad()
def value_logprobs(model, eps, device, batch=200):
    """log p(value | prefix) for every turn, on a plain forward pass with
    NO acting-channel injections — the act-withheld scoring A3 §3.4
    specifies. The attacker does not get to know which turns were enacted;
    assuming it would presuppose the answer."""
    out = []
    for i in range(0, len(eps), batch):
        chunk = eps[i:i + batch]
        b = to_torch(E.collate([E.encode_episode(e) for e in chunk]), device)
        logp = torch.log_softmax(model.forward(b), dim=-1)
        for j, e in enumerate(chunk):
            vals = []
            for ti, t in enumerate(e.turns):
                span = (b["turn_ids"][j] == ti).nonzero().flatten()
                pos = int(span[0]) + A.VALUE_WORD_IDX - 1
                vals.append(float(logp[j, pos, E.VOCAB[t.value]]))
            out.append(np.array(vals))
    return out


def _auc(y, s, seed):
    y, s = np.asarray(y), np.asarray(s)
    lo, hi = boot_ci(y, s, N_BOOT, seed)
    return {"n_examples": int(len(y)), "auc": round(float(roc_auc_score(y, s)), 4),
            "ci95": [round(float(lo), 4), round(float(hi), 4)]}


def arm_a(model, n_episodes, seed, device) -> dict:
    out = {}
    for name, leaky in (("clean", False), ("positive_control", True)):
        eps = A.generate_balanced(n_episodes, seed + 1, leaky=leaky)
        fill_all(model, eps, device, mode="enact", seed=seed)
        texts, feats, labels = D.build_examples(eps, seed=seed,
                                                agent_uniform=True)
        auc, y, p = D.fit_auc(texts, feats, labels, seed)
        lo, hi = boot_ci(y, p, N_BOOT, seed)
        out[name] = {"n_examples": int(len(labels)),
                     "auc": round(float(auc), 4),
                     "ci95": [round(float(lo), 4), round(float(hi), 4)]}
    clean_ok = EQUIV_LO <= out["clean"]["ci95"][0] \
        and out["clean"]["ci95"][1] <= EQUIV_HI
    pc_ok = out["positive_control"]["auc"] >= POSITIVE_CONTROL_MIN_AUC
    return {"arm": "A committed classifier family, agent-uniform sampling",
            **out, "clean_pass": bool(clean_ok), "pc_pass": bool(pc_ok)}


def arm_b(model, n_episodes, seed, device) -> dict:
    def run(mode):
        rng = np.random.default_rng(seed)
        eps = A.generate_balanced(n_episodes, seed + 2)
        fill_all(model, eps, device, mode=mode, seed=seed)
        lps = value_logprobs(model, eps, device)
        scores, labels = [], []
        for e, lp in zip(eps, lps):
            own = [i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
            others = [a for a in range(e.n_agents) if a != e.own_slot]
            a = others[int(rng.integers(len(others)))]
            oth = [i for i, t in enumerate(e.turns) if t.agent == a]
            if not own or not oth:
                continue
            scores += [lp[own[int(rng.integers(len(own)))]],
                       lp[oth[int(rng.integers(len(oth)))]]]
            labels += [1, 0]
        return {"mode": mode, **_auc(labels, scores, seed)}

    clean, pc_g, pc_p = run("enact"), run("greedy"), run("policy")
    clean_ok = EQUIV_LO <= clean["ci95"][0] and clean["ci95"][1] <= EQUIV_HI
    pc_ok = (pc_g["auc"] >= POSITIVE_CONTROL_MIN_AUC
             or pc_p["auc"] >= POSITIVE_CONTROL_MIN_AUC)
    return {"arm": "B likelihood attack, ACT-WITHHELD [A3 §3.4]",
            "clean": clean, "positive_control_greedy": pc_g,
            "positive_control_policy": pc_p,
            "clean_pass": bool(clean_ok), "pc_pass": bool(pc_ok)}


def run_gate(ckpt: str, n_episodes: int = N_EPISODES, seed: int = SEED,
             device: str = "cpu") -> dict:
    model = load(ckpt, device)
    a = arm_a(model, n_episodes, seed, device)
    b = arm_b(model, n_episodes, seed, device)
    arms = []
    for arm in (a, b):
        if not arm["pc_pass"]:
            arm["VERDICT"] = "UNCERTIFIABLE"
        elif arm["clean_pass"]:
            arm["VERDICT"] = "PASS"
        else:
            arm["VERDICT"] = "FAIL"
        arms.append(arm["VERDICT"])
    gate = ("FAIL" if "FAIL" in arms
            else "UNCERTIFIABLE" if "UNCERTIFIABLE" in arms else "PASS")
    return {"gate": "A3 Gate 3 — fingerprint detector, act-withheld arm B",
            "checkpoint": Path(ckpt).name,
            "params": {"n_episodes": n_episodes, "seed": seed,
                       "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                       "positive_control_min_auc": POSITIVE_CONTROL_MIN_AUC},
            "arm_a": a, "arm_b": b, "GATE": gate,
            "note": "UNCERTIFIABLE is a registered outcome (2026-09-15 "
                    "decision 12): if the positive controls do not fire, "
                    "the arm cannot certify a clean result and says so "
                    "rather than blessing one."}


def self_test() -> None:
    cfg = Config(vocab=len(E.VOCAB), d_model=64, n_layers=2, n_heads=2,
                 max_len=128, use_register=False)
    torch.manual_seed(0)
    m = MVM0aModel(cfg).eval()
    eps = A.generate_balanced(12, 5)
    fill_all(m, eps, "cpu", mode="enact", seed=1)
    lp = value_logprobs(m, eps, "cpu")
    assert len(lp) == len(eps) and all(len(x) == len(e.turns)
                                       for x, e in zip(lp, eps))
    assert all(np.isfinite(x).all() and (x <= 0).all() for x in lp), \
        "log probabilities must be finite and non-positive"
    # the scoring position really is the value token
    b = to_torch(E.collate([E.encode_episode(eps[0])]))
    span = (b["turn_ids"][0] == 0).nonzero().flatten()
    pos = int(span[0]) + A.VALUE_WORD_IDX
    assert E.IVOCAB[int(b["input_ids"][0, pos])] == eps[0].turns[0].value
    # the leaky control really differs from clean
    e2 = A.generate_balanced(12, 5)
    fill_all(m, e2, "cpu", mode="constant", seed=1)
    assert all(t.value == A.SLOTS[0] for e in e2 for t in e.turns
               if t.agent == e.own_slot)
    # policy and greedy fills stay on-grammar; greedy is deterministic
    for mode in ("policy", "greedy"):
        e3 = A.generate_balanced(12, 5)
        fill_all(m, e3, "cpu", mode=mode, seed=1)
        assert all(t.value in A.SLOTS for e in e3 for t in e.turns)
    e4 = A.generate_balanced(12, 5)
    fill_all(m, e4, "cpu", mode="greedy", seed=99)
    e5 = A.generate_balanced(12, 5)
    fill_all(m, e5, "cpu", mode="greedy", seed=1)
    assert [t.value for e in e4 for t in e.turns] == \
           [t.value for e in e5 for t in e.turns], "greedy must not vary"
    print("fingerprint_gate_a3 self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=N_EPISODES)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.run:
        assert args.ckpt, "--ckpt required"
        res = run_gate(args.ckpt, args.n, SEED, args.device)
        print(json.dumps(res, indent=2))
        if args.out:
            p = Path(args.out)
            assert not p.exists(), f"refusing to overwrite {p} [C6]"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(res, indent=2))
            print(f"\nwrote {p}")


if __name__ == "__main__":
    main()
