"""Cue-detector gate runs (i) and (ii) for the Amendment A3 grammar.

A3 §4.1 Gate 1. The anti-router design's claim is that **no surface cue
predicts which commitments are the model's own**. That claim is what lets
MVM-0a say the confound which voided Experiment 1 is excluded at the data
level, and an unmeasured claim is not an exclusion. Kill criterion K1:
gates (i) or (ii) failing after two regenerations halts A3 at $0.

Carried over from `cue_detector.py` verbatim: the equivalence bound
(the bootstrap 95% CI on AUC must be *contained in* [0.45, 0.55], so a
weak classifier's failure to find leakage is not mistaken for evidence of
none), the positive control on a deliberately leaky variant, and
pre-committed capacity and n so the null cannot be bought by
underpowering the detector.

**One thing is deliberately not carried over.** The registered detector
scores a turn by its position, length, marker, and its agent's turn
count, plus character n-grams of the rendered text. Under the A3 grammar
that feature set is blind to the cue class that killed this module's
first draft: revision status. An A3 turn renders identically whether it
is an assignment or a revision — "<marker> assign <item> to <value>" —
so a detector reading only the turn's own text and position cannot see
that the turn repeats an item its agent assigned earlier. The first A3
draft gave the model's slot one revision and left two other agents with
none, which made the model's agent the only one with three turns; the
registered feature set would have caught that through turn count, but a
variant that balanced counts while leaving revision status skewed would
have sailed through. So this gate adds **episode-relative features**:
whether the turn revises an item its own agent assigned earlier, how many
earlier turns share its item, its rank within the revision block, and its
agent's share of revisions. The gate is only as good as what you hand it,
and handing it less than the model can see is how a clean verdict gets
manufactured.

Run (i) is over curriculum text plus those features; run (ii) is over the
exact tensors a training step consumes (`encoding_a3.py`), excluding
`act_pos`, which is trainer control flow and never a model input. Run
(iii), the post-training rollout fingerprint, needs a trained model and is
not part of Gate 1.

    ../../../.venv/bin/python cue_detector_a3.py --self-test
    ../../../.venv/bin/python cue_detector_a3.py --run
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import curriculum_a3 as A
import encoding_a3 as E
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from cue_detector import (EQUIV_LO, EQUIV_HI, POSITIVE_CONTROL_MIN_AUC,
                          N_BOOT, boot_ci, fit_auc)
import curriculum as C

N_EPISODES = 4000
SEED = 20260915


def _episode_features(ep, idx: int) -> list[float]:
    """Everything about a turn that the MODEL could condition on, stated
    relative to its episode — not just the turn read in isolation."""
    t = ep.turns[idx]
    same_item_before = [j for j in range(idx) if ep.turns[j].item == t.item]
    own_agent_before = [j for j in same_item_before
                        if ep.turns[j].agent == t.agent]
    revs = [j for j, x in enumerate(ep.turns) if x.revised]
    agent_turns = [j for j, x in enumerate(ep.turns) if x.agent == t.agent]
    return [
        idx,
        idx / max(1, len(ep.turns) - 1),
        len(t.render()),
        float(idx == 0),
        float(idx == len(ep.turns) - 1),
        len(agent_turns),                       # turn count for this agent
        C.MARKERS.index(t.marker),
        # --- episode-relative, the A3 additions ---
        float(bool(own_agent_before)),          # IS THIS A REVISION
        len(same_item_before),                  # earlier turns on this item
        float(idx in revs),                     # in the revision block
        revs.index(idx) if idx in revs else -1,  # rank within that block
        sum(1 for j in agent_turns if ep.turns[j].revised),  # its revisions
        agent_turns.index(idx),                 # which of its turns this is
        C.SLOTS.index(t.value),
        C.ITEMS.index(t.item),
    ]


def _pick_other(ep, rng, agent_uniform: bool):
    """Choose the comparison turn.

    `agent_uniform=False` is the registered sampler: pool every turn of
    every other agent and draw one. That draw is SIZE-BIASED — an agent
    with more turns contributes more turns to the pool, so it is picked
    more often — while the model's own turn is drawn from one agent and
    carries no such weighting. When agents differ in how much they speak,
    the two samples are not comparable even if turn count is perfectly
    balanced across all turns, and the detector reads the difference as a
    cue. Measured on the current grammar: 0.4992 for the model's sampled
    turn against 0.5839 for the pooled draw.

    `agent_uniform=True` draws an other AGENT uniformly first, then one of
    its turns. That is the contrast the design's exchangeability actually
    guarantees — relabel which agent is the model's and the distribution
    is unchanged — and it removes the size bias: 0.4992 against 0.5021.
    """
    others = [a for a in range(ep.n_agents) if a != ep.own_slot]
    if agent_uniform:
        a = others[int(rng.integers(len(others)))]
        pool = [i for i, t in enumerate(ep.turns) if t.agent == a]
    else:
        pool = [i for i, t in enumerate(ep.turns) if t.agent != ep.own_slot]
    return pool[int(rng.integers(len(pool)))] if pool else None


def build_examples(eps, seed: int = 0, agent_uniform: bool = False):
    """One balanced own/other pair per episode. The own turn is drawn
    uniformly from the model's turns; the comparison turn per
    `_pick_other`. (The sampler bug that once manufactured AUC 0.896 on a
    clean curriculum came from taking the first of each.)"""
    rng = np.random.default_rng(seed)
    texts, feats, labels = [], [], []
    for ep in eps:
        own = [i for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
        o = _pick_other(ep, rng, agent_uniform)
        if not own or o is None:
            continue
        for idx, label in ((own[int(rng.integers(len(own)))], 1), (o, 0)):
            texts.append(ep.turns[idx].render())
            feats.append(_episode_features(ep, idx))
            labels.append(label)
    return texts, np.asarray(feats, float), np.asarray(labels)


def build_tensor_examples(eps, leaky: bool, seed: int = 0,
                          agent_uniform: bool = False):
    """Features from the exact tensor dict a training step consumes.
    `act_pos` is excluded: it is derived from own_slot and is trainer
    control flow, never fed to the model."""
    rng = np.random.default_rng(seed)
    feats, labels = [], []
    for ep in eps:
        enc = E.encode_episode(ep, query=ep.queries[0], leaky=leaky)
        assert set(enc) - {"act_pos"} == set(E.MODEL_FIELDS)
        n_tok = len(enc["input_ids"])
        own = [i for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
        o = _pick_other(ep, rng, agent_uniform)
        if not own or o is None:
            continue
        for ti, label in ((own[int(rng.integers(len(own)))], 1), (o, 0)):
            span = np.where(enc["turn_ids"] == ti)[0]
            tok = enc["input_ids"][span]
            reg = int(enc["turn_reg"][ti])
            row = [
                reg,
                float(reg == 0),                     # the reindex bug's cue
                int(enc["register_keys"][reg]),
                float(span[0]) / n_tok,
                float(span[-1]) / n_tok,
                len(span),
                ti,
                float(enc["loss_mask"][span].sum()),
                n_tok - float(span[-1]),
                float((enc["turn_reg"] == reg).sum()),   # turns on this row
            ]
            row += [float(x) for x in tok[:6]]
            row += [0.0] * (6 - len(tok[:6]))
            feats.append(row)
            labels.append(label)
    return np.asarray(feats, float), np.asarray(labels)


def fit_numeric(feats, labels, seed: int):
    """Numeric-only classifier for run (ii) — same family and capacity as
    run (i)'s, without the text branch (`cue_detector.run_tensor_variant`
    makes the same split)."""
    idx = np.arange(len(labels))
    tr, te = train_test_split(idx, test_size=0.3, random_state=seed,
                              stratify=labels)
    sc = StandardScaler().fit(feats[tr])
    clf = LogisticRegression(max_iter=2000, C=1.0)
    clf.fit(sc.transform(feats[tr]), labels[tr])
    p = clf.predict_proba(sc.transform(feats[te]))[:, 1]
    return roc_auc_score(labels[te], p), labels[te], p


def _verdict(clean: dict, leaky: dict) -> tuple[bool, bool]:
    return (EQUIV_LO <= clean["ci95"][0] and clean["ci95"][1] <= EQUIV_HI,
            leaky["auc"] >= POSITIVE_CONTROL_MIN_AUC)


def text_gate(n_episodes: int = N_EPISODES, seed: int = SEED,
              agent_uniform: bool = False) -> dict:
    out = {}
    for name, leaky in (("clean", False), ("positive_control", True)):
        eps = A.generate_balanced(n_episodes, seed, leaky=leaky)
        texts, feats, labels = build_examples(eps, seed=seed,
                                              agent_uniform=agent_uniform)
        auc, y, p = fit_auc(texts, feats, labels, seed)
        lo, hi = boot_ci(y, p, N_BOOT, seed)
        out[name] = {"leaky": leaky, "n_examples": int(len(labels)),
                     "auc": round(float(auc), 4),
                     "ci95": [round(float(lo), 4), round(float(hi), 4)]}
    cp, pc = _verdict(out["clean"], out["positive_control"])
    return {"run": "(i) curriculum text + episode-relative features",
            "params": {"n_episodes": n_episodes, "seed": seed,
                       "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                       "positive_control_min_auc": POSITIVE_CONTROL_MIN_AUC,
                       "n_features": len(_episode_features(
                           A.generate_episode(0), 0))},
            **out,
            "clean_within_equivalence_bound": bool(cp),
            "positive_control_detects_planted_leak": bool(pc),
            "GATE": "PASS" if (cp and pc) else "FAIL"}


def tensor_gate(n_episodes: int = N_EPISODES, seed: int = SEED,
                agent_uniform: bool = False) -> dict:
    out = {}
    for name, leaky in (("clean", False), ("positive_control", True)):
        eps = A.generate_balanced(n_episodes, seed, leaky=False)
        feats, labels = build_tensor_examples(eps, leaky=leaky, seed=seed,
                                              agent_uniform=agent_uniform)
        auc, y, p = fit_numeric(feats, labels, seed)
        lo, hi = boot_ci(y, p, N_BOOT, seed)
        out[name] = {"leaky_layout": leaky, "n_examples": int(len(labels)),
                     "auc": round(float(auc), 4),
                     "ci95": [round(float(lo), 4), round(float(hi), 4)]}
    cp, pc = _verdict(out["clean"], out["positive_control"])
    return {"run": "(ii) input tensors",
            "params": {"n_episodes": n_episodes, "seed": seed,
                       "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                       "positive_control": "canonical register reindex "
                                           "(own register forced to row 0)"},
            **out,
            "clean_within_equivalence_bound": bool(cp),
            "positive_control_detects_planted_leak": bool(pc),
            "GATE": "PASS" if (cp and pc) else "FAIL"}


VERDICT_SEEDS = (20260915, 11, 22, 33, 44)


def gate(n_episodes: int = N_EPISODES, seed: int = SEED,
         agent_uniform: bool = True, both: bool = True) -> dict:
    """Run the gate and report BOTH samplers side by side.

    John's ruling of 2026-09-15: the amended (agent-uniform) sampler is
    the one the verdict is read from, and the registered (pooled) number
    is reported beside it every time, so a reader can see what the
    original instrument said and decide whether to accept the override.
    See `cue-detector-sampler-amendment.md`.

    The verdict is taken over several independent samples rather than one,
    because a single bootstrap interval covers one draw's test split and
    is silent on spread between draws — at these episode counts a clean
    grammar fails a single run about one time in nine.
    """
    out = {"gate": "A3 Gate 1 — cue-detector runs (i) and (ii)",
           "grammar": "curriculum_a3 (Candidate A)",
           "k_revisers": A.K_REVISERS,
           "n_turns": A.N_TURNS, "n_agents": A.N_AGENTS,
           "verdict_sampler": ("amended: both arms agent-uniform"
                               if agent_uniform else "registered: pooled"),
           "verdict_seeds": list(VERDICT_SEEDS),
           "samplers": {},
           "pending": {"(iii) post-training rollouts":
                       "requires a trained checkpoint; A3 Gate 3"}}
    modes = ([("amended_agent_uniform", True), ("registered_pooled", False)]
             if both else [("amended_agent_uniform", agent_uniform)])
    for label, au in modes:
        per_seed = []
        for sd in VERDICT_SEEDS:
            runs = [text_gate(n_episodes, sd, au),
                    tensor_gate(n_episodes, sd, au)]
            per_seed.append({
                "seed": sd,
                "text_auc": runs[0]["clean"]["auc"],
                "tensor_auc": runs[1]["clean"]["auc"],
                "text_control": runs[0]["positive_control"]["auc"],
                "tensor_control": runs[1]["positive_control"]["auc"],
            })
        t = np.array([r["text_auc"] for r in per_seed])
        v = np.array([r["tensor_auc"] for r in per_seed])
        ctl = min(min(r["text_control"] for r in per_seed),
                  min(r["tensor_control"] for r in per_seed))
        ok = (EQUIV_LO <= t.mean() <= EQUIV_HI
              and EQUIV_LO <= v.mean() <= EQUIV_HI
              and ctl >= POSITIVE_CONTROL_MIN_AUC)
        out["samplers"][label] = {
            "per_seed": per_seed,
            "text_mean": round(float(t.mean()), 4),
            "text_sd": round(float(t.std(ddof=1)), 4),
            "tensor_mean": round(float(v.mean()), 4),
            "tensor_sd": round(float(v.std(ddof=1)), 4),
            "weakest_positive_control": round(float(ctl), 4),
            "GATE": "PASS" if ok else "FAIL",
        }
    key = "amended_agent_uniform" if agent_uniform else "registered_pooled"
    out["GATE"] = out["samplers"][key]["GATE"]
    return out


STABILITY_SEEDS = (20260915, 11, 22, 33, 44, 55)


def stability(n_episodes: int = N_EPISODES) -> dict:
    """How much does a gate verdict move between independent samples?

    The registered gate reports one AUC with a bootstrap CI, and that CI
    resamples the test split of a SINGLE draw of episodes. It therefore
    measures uncertainty within one sample and says nothing about how far
    the point estimate wanders between samples. On a grammar with no cue
    the two are not the same: the classifier can fit a chance imbalance
    present in that particular draw, and some of it transfers to the test
    split of the same draw.

    This runs the clean gate on independent samples and reports the
    spread, so the verdict can be read against the right yardstick.
    """
    out = {"n_episodes": n_episodes, "seeds": list(STABILITY_SEEDS),
           "text": [], "tensor": []}
    for sd in STABILITY_SEEDS:
        eps = A.generate_balanced(n_episodes, sd)
        texts, feats, labels = build_examples(eps, seed=sd)
        out["text"].append(round(float(fit_auc(texts, feats, labels, sd)[0]), 4))
        f2, l2 = build_tensor_examples(eps, leaky=False, seed=sd)
        out["tensor"].append(round(float(fit_numeric(f2, l2, sd)[0]), 4))
    for k in ("text", "tensor"):
        v = np.asarray(out[k])
        out[f"{k}_mean"] = round(float(v.mean()), 4)
        out[f"{k}_sd"] = round(float(v.std(ddof=1)), 4)
        # a clean grammar's chance of failing the upper bound, given this
        # spread and a bootstrap half-width of about one sd
        from math import erf, sqrt
        z = (EQUIV_HI - v.std(ddof=1) - 0.5) / v.std(ddof=1)
        out[f"{k}_false_fail_rate"] = round(
            float(0.5 * (1 - erf(z / sqrt(2)))), 4)
    return out


def self_test() -> None:
    eps = A.generate_balanced(200, 1)
    texts, feats, labels = build_examples(eps, seed=1)
    assert len(texts) == len(labels) == len(feats)
    assert set(np.unique(labels)) == {0, 1}
    assert labels.sum() * 2 == len(labels), "examples must be balanced"
    # the revision-status feature is real: it fires on exactly the turns
    # whose agent already assigned that item
    for ep in eps[:50]:
        for i, t in enumerate(ep.turns):
            f = _episode_features(ep, i)
            expect = any(ep.turns[j].agent == t.agent
                         and ep.turns[j].item == t.item for j in range(i))
            assert bool(f[7]) == expect == bool(t.revised)
    # tensor examples exclude act_pos
    f2, l2 = build_tensor_examples(eps, leaky=False, seed=1)
    assert len(f2) == len(l2) and np.isfinite(f2).all()
    print(f"cue_detector_a3 self-test OK "
          f"({len(_episode_features(eps[0], 0))} text-side features, "
          f"{f2.shape[1]} tensor-side)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--stability", action="store_true")
    ap.add_argument("--registered-sampler", dest="agent_uniform",
                    action="store_false", default=True,
                    help="read the verdict from the ORIGINAL pooled "
                         "sampler instead of the amended one (both are "
                         "reported either way)")
    ap.add_argument("--n", type=int, default=N_EPISODES)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.stability:
        res = stability(args.n)
        print(json.dumps(res, indent=2))
        if args.out:
            q = Path(args.out)
            assert not q.exists(), f"refusing to overwrite {q} [C6]"
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_text(json.dumps(res, indent=2))
            print(f"\nwrote {q}")
        return
    if args.run:
        res = gate(args.n, SEED, args.agent_uniform)
        print(json.dumps(res, indent=2))
        if args.out:
            p = Path(args.out)
            assert not p.exists(), f"refusing to overwrite {p} [C6]"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(res, indent=2))
            print(f"\nwrote {p}")


if __name__ == "__main__":
    main()
