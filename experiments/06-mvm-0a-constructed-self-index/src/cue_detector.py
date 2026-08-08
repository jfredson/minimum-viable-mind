"""The RT-08 cue-detector gate for the MVM-0a curriculum.

The anti-router design's central claim is that *no surface cue predicts
which commitments are the model's own*. That claim is what lets MVM-0a
say the confound which voided Experiment 1 is excluded at the data level.
An unmeasured claim is not an exclusion, so this is the gate that can
fail the whole design before a single training run.

Red-team requirements implemented here:

- **Equivalence bound, not a point null.** A weak classifier failing to
  find leakage is not evidence of no leakage. The gate passes only if the
  bootstrap 95% CI on AUC is *contained in* [0.45, 0.55].
- **Positive control.** The same detector is run on a deliberately leaky
  curriculum variant and must exceed a pre-committed AUC. A detector that
  cannot find planted leakage has no standing to certify a clean one.
- **Pre-committed capacity and n**, so the null cannot be bought with an
  underpowered model.

Scope note: runs (i) and (ii) of the three the pre-registration requires
are implemented — (i) over curriculum *text*, (ii) over the exact *input
tensors* the adjudicated architecture consumes (`encoding.py`: token ids,
turn ids, register key stack, loss mask, padding). Run (ii)'s positive
control plants the realistic implementation bug: canonically reindexing
the register stack so the model's own register sits at index 0, which is
an identity channel wearing a tensor layout. Run (iii) is the
post-training fingerprint detector over the model's own rollouts and
needs a trained model; it stays stubbed with an explicit
NotImplementedError rather than silently skipped — a gate that quietly
does not run is worse than one that fails.

    ../../../.venv/bin/python cue_detector.py --self-test
    ../../../.venv/bin/python cue_detector.py --run
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import StandardScaler

import curriculum as C
import encoding as E

# Pre-committed gate parameters. Changing these after seeing a result is
# exactly the move the equivalence bound exists to prevent.
N_EPISODES = 4000
EQUIV_LO, EQUIV_HI = 0.45, 0.55
POSITIVE_CONTROL_MIN_AUC = 0.70
N_BOOT = 2000
SEED = 20260804
MAX_NGRAM = 3


def build_examples(eps: list[C.Episode], seed: int = 0
                   ) -> tuple[list[str], np.ndarray, np.ndarray]:
    """One balanced binary example per episode: a self-owned turn and an
    other-owned turn, labelled. Balanced construction puts chance at
    AUC 0.5, matching the equivalence bound.

    Both turns are drawn UNIFORMLY at random from their groups. An earlier
    version took the first of each, which manufactured a position
    asymmetry (with N agents the episode's first turn belongs to another
    agent with probability 1-1/N) and made the detector read AUC 0.896 on
    a clean curriculum. That was a defect in the sampler, not a cue in the
    data — a standing reminder that this gate tests whatever you hand it,
    and that a FAIL is a hypothesis about the data, not a verdict on it."""
    rng = np.random.default_rng(seed)
    texts, feats, labels = [], [], []
    for ep in eps:
        own = [(i, t) for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
        oth = [(i, t) for i, t in enumerate(ep.turns) if t.agent != ep.own_slot]
        if not own or not oth:
            continue
        own = [own[int(rng.integers(len(own)))]]
        oth = [oth[int(rng.integers(len(oth)))]]
        for (idx, turn), label in ((own[0], 1), (oth[0], 0)):
            texts.append(turn.render())
            # explicit positional/surface features — the attack surface a
            # bag-of-words model would miss on its own
            feats.append([
                idx,                                   # absolute turn index
                idx / max(1, len(ep.turns) - 1),       # relative position
                len(turn.render()),                    # length
                float(idx == 0),                       # speaks first?
                float(idx == len(ep.turns) - 1),       # speaks last?
                sum(1 for t in ep.turns if t.agent == turn.agent),  # turn count
                C.MARKERS.index(turn.marker),          # marker identity
            ])
            labels.append(label)
    return texts, np.asarray(feats, dtype=float), np.asarray(labels)


class _Text:
    """Adapter so text and numeric features can join one FeatureUnion."""
    def __init__(self, texts): self.texts = texts


def fit_auc(texts, feats, labels, seed: int) -> float:
    idx = np.arange(len(labels))
    tr, te = train_test_split(idx, test_size=0.3, random_state=seed,
                              stratify=labels)
    vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(1, MAX_NGRAM),
                          min_df=2)
    Xtr_t = vec.fit_transform([texts[i] for i in tr]).toarray()
    Xte_t = vec.transform([texts[i] for i in te]).toarray()
    sc = StandardScaler().fit(feats[tr])
    Xtr = np.hstack([Xtr_t, sc.transform(feats[tr])])
    Xte = np.hstack([Xte_t, sc.transform(feats[te])])
    clf = LogisticRegression(max_iter=2000, C=1.0)
    clf.fit(Xtr, labels[tr])
    return roc_auc_score(labels[te], clf.predict_proba(Xte)[:, 1]), \
        labels[te], clf.predict_proba(Xte)[:, 1]


def boot_ci(y, p, n_boot: int, seed: int) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    n = len(y)
    out = []
    for _ in range(n_boot):
        ix = rng.integers(0, n, n)
        if len(np.unique(y[ix])) < 2:
            continue
        out.append(roc_auc_score(y[ix], p[ix]))
    return tuple(np.quantile(out, [0.025, 0.975]))


def run_variant(leaky: bool, n_episodes: int, seed: int) -> dict:
    eps = C.generate_balanced(n_episodes, seed, leaky=leaky,
                              forced_revision_frac=0.25)
    texts, feats, labels = build_examples(eps, seed=seed)
    auc, y, p = fit_auc(texts, feats, labels, seed)
    lo, hi = boot_ci(y, p, N_BOOT, seed)
    return {"leaky": leaky, "n_examples": len(labels),
            "auc": round(float(auc), 4),
            "ci95": [round(float(lo), 4), round(float(hi), 4)]}


def text_gate(n_episodes: int = N_EPISODES, seed: int = SEED) -> dict:
    clean = run_variant(False, n_episodes, seed)
    leaky = run_variant(True, n_episodes, seed)
    clean_pass = EQUIV_LO <= clean["ci95"][0] and clean["ci95"][1] <= EQUIV_HI
    pc_pass = leaky["auc"] >= POSITIVE_CONTROL_MIN_AUC
    return {
        "run": "(i) curriculum text",
        "params": {"n_episodes": n_episodes, "seed": seed,
                   "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                   "positive_control_min_auc": POSITIVE_CONTROL_MIN_AUC,
                   "classifier": "char_wb tfidf(1-3) + positional feats, "
                                 "logistic C=1.0"},
        "clean": clean, "positive_control": leaky,
        "clean_within_equivalence_bound": bool(clean_pass),
        "positive_control_detects_planted_leak": bool(pc_pass),
        "GATE": "PASS" if (clean_pass and pc_pass) else "FAIL",
    }


def gate(n_episodes: int = N_EPISODES, seed: int = SEED) -> dict:
    runs = [text_gate(n_episodes, seed), run_tensor_gate(n_episodes, seed)]
    return {
        "runs": runs,
        "GATE": "PASS" if all(r["GATE"] == "PASS" for r in runs) else "FAIL",
        "pending_runs": {
            "(iii) post-training rollouts": "requires a trained model",
        },
    }


def build_tensor_examples(eps: list[C.Episode], leaky: bool, seed: int = 0
                          ) -> tuple[np.ndarray, np.ndarray]:
    """Balanced own/other examples whose features come from the exact
    tensor dict a training step consumes (`encoding.py`), not from text.
    Per selected turn: its register-stack row and key id, its token-level
    span and position, its turn id, loss-mask overlap, distance to
    padding, and the raw token ids of the turn — every auxiliary channel
    RT-08 names, plus the register stack that run (i) could not see."""
    rng = np.random.default_rng(seed)
    feats, labels = [], []
    for ep in eps:
        enc = E.encode_episode(ep, query=ep.queries[0], leaky=leaky)
        n_tok = len(enc["input_ids"])
        own = [i for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
        oth = [i for i, t in enumerate(ep.turns) if t.agent != ep.own_slot]
        if not own or not oth:
            continue
        for ti, label in ((own[int(rng.integers(len(own)))], 1),
                          (oth[int(rng.integers(len(oth)))], 0)):
            span = np.where(enc["turn_ids"] == ti)[0]
            tok = enc["input_ids"][span]
            reg = int(enc["turn_reg"][ti])
            feats.append([
                reg,                                    # register-stack row
                float(reg == 0),                        # the reindex bug's cue
                int(enc["register_keys"][reg]),         # marker key id
                int(span[0]), int(span[-1]),            # token span
                span[0] / max(1, n_tok - 1),            # relative position
                ti,                                     # turn id
                len(span),                              # tokens in turn
                int(enc["loss_mask"][span].sum()),      # loss-mask overlap
                n_tok - 1 - int(span[-1]),              # distance to pad/end
                *[int(x) for x in tok[:6]],             # raw turn token ids
            ])
            labels.append(label)
    return np.asarray(feats, dtype=float), np.asarray(labels)


def run_tensor_variant(leaky: bool, n_episodes: int, seed: int) -> dict:
    eps = C.generate_balanced(n_episodes, seed, forced_revision_frac=0.25)
    feats, labels = build_tensor_examples(eps, leaky=leaky, seed=seed)
    idx = np.arange(len(labels))
    tr, te = train_test_split(idx, test_size=0.3, random_state=seed,
                              stratify=labels)
    sc = StandardScaler().fit(feats[tr])
    clf = LogisticRegression(max_iter=2000, C=1.0)
    clf.fit(sc.transform(feats[tr]), labels[tr])
    p = clf.predict_proba(sc.transform(feats[te]))[:, 1]
    auc = roc_auc_score(labels[te], p)
    lo, hi = boot_ci(labels[te], p, N_BOOT, seed)
    return {"leaky": leaky, "n_examples": len(labels),
            "auc": round(float(auc), 4),
            "ci95": [round(float(lo), 4), round(float(hi), 4)]}


def run_tensor_gate(n_episodes: int = N_EPISODES, seed: int = SEED) -> dict:
    """RT-08 run (ii): the detector sees the exact input tensors. Same
    pre-committed n, equivalence bound, positive-control floor, and
    classifier family as run (i). The leaky variant is the
    canonical-reindex bug (own register forced to stack index 0)."""
    clean = run_tensor_variant(False, n_episodes, seed)
    leaky = run_tensor_variant(True, n_episodes, seed)
    clean_pass = EQUIV_LO <= clean["ci95"][0] and clean["ci95"][1] <= EQUIV_HI
    pc_pass = leaky["auc"] >= POSITIVE_CONTROL_MIN_AUC
    return {
        "run": "(ii) input tensors",
        "params": {"n_episodes": n_episodes, "seed": seed,
                   "equivalence_bound": [EQUIV_LO, EQUIV_HI],
                   "positive_control_min_auc": POSITIVE_CONTROL_MIN_AUC,
                   "classifier": "tensor feats (register row/keys, spans, "
                                 "turn ids, loss mask, padding, token ids), "
                                 "logistic C=1.0",
                   "positive_control": "canonical-reindex bug: own register "
                                       "forced to stack index 0"},
        "clean": clean, "positive_control": leaky,
        "clean_within_equivalence_bound": bool(clean_pass),
        "positive_control_detects_planted_leak": bool(pc_pass),
        "GATE": "PASS" if (clean_pass and pc_pass) else "FAIL",
    }


def run_fingerprint_gate():
    raise NotImplementedError(
        "RT-08 run (iii): post-training self-vs-generated fingerprint "
        "detector over the model's own rollouts. Requires a trained model.")


def self_test() -> None:
    small = text_gate(n_episodes=300, seed=1)
    assert small["positive_control"]["auc"] > small["clean"]["auc"], \
        "planted leak must be easier to detect than the clean curriculum"
    small_t = run_tensor_gate(n_episodes=300, seed=1)
    assert small_t["positive_control"]["auc"] > small_t["clean"]["auc"], \
        "the reindex bug must be easier to detect than the clean tensors"
    try:
        run_fingerprint_gate()
    except NotImplementedError:
        pass
    else:
        raise AssertionError("pending gates must not silently pass")
    print("cue-detector self-test OK "
          f"(text clean {small['clean']['auc']:.3f} vs leaky "
          f"{small['positive_control']['auc']:.3f}; "
          f"tensor clean {small_t['clean']['auc']:.3f} vs leaky "
          f"{small_t['positive_control']['auc']:.3f})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--n-episodes", type=int, default=N_EPISODES)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    res = gate(n_episodes=args.n_episodes)
    out = Path(__file__).resolve().parents[1] / "cue_detector_gate.json"
    out.write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
