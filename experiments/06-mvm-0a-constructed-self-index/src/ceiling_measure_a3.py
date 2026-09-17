"""What IS the control battery's ownership-blind ceiling?

**Method written and committed BEFORE this ran**, at
`ceiling-measurement-method.md`, commit `2fba2ea`. This implements it and
adds nothing.

The registered figure is 0.3227 and the registration says it was verified
by the attack sweep. It was not: the sweep contains no control-battery
code. The figure rests on one reference solver that never reads the
marker the control question names.

THE RULE, quoted from the sweep, which every solver here obeys: an attack
"may use the full rendered episode, every structural fact about it, and
the shared revision rule. It may NOT use `own_slot`, the acting channel,
or anything derived from them."

No model is loaded and no inference runs. A ceiling is a fact about the
grammar, not about a checkpoint. No spend, no network.

    ../../../.venv/bin/python ceiling_measure_a3.py --self-test
    ../../../.venv/bin/python ceiling_measure_a3.py --run
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np

import curriculum_a3 as A

REGISTERED_CONTROL = 0.3227
REGISTERED_PRIMARY = 0.2921
BAND = 0.05                 # stated convention, mine
CHECK_TOL = 0.01            # known-answer checks must land this close


def rendered(ep):
    """What a solver can actually read: one triple per turn, exactly as
    the grammar renders it. Never touches own_slot."""
    return [(t.item, t.value, ep.markers[t.agent], t.revised)
            for t in ep.turns]


def query_facts(ep):
    q = [q for q in ep.queries if q.battery == "T_other"][0]
    toks = q.text.split()
    return q, toks[2], toks[4]          # query, marker asked about, item


def s1_name_keyed(ep, rng):
    """Read the marker in the question, find its turn for the queried
    item in the RENDERED episode, apply the shared rule to its value.
    Uses no own_slot and nothing derived from it."""
    q, marker, item = query_facts(ep)
    hits = [v for (it, v, mk, _rev) in rendered(ep)
            if mk == marker and it == item]
    if not hits:
        return rng.choice(A.SLOTS)      # information absent: guess
    return A.successor(hits[-1])


def s2_registered_reference(ep):
    """The registered name-blind solver, reproduced. Returns its EXPECTED
    score, which is how the registered figure is defined."""
    q, _marker, item = query_facts(ep)
    qc = {A.successor(ep.values[item][a]) for a in range(A.N_AGENTS)}
    qs = {t.value for t in ep.turns if t.revised and t.item == item}
    return 1.0 / max(1, len(qc - qs))


def primary_reference(ep):
    """The registered solver's PRIMARY-battery path, reproduced, as the
    second known-answer check on this harness."""
    if not A.has_own_revision(ep):
        return None
    i = A.own_revision_index(ep)
    item = ep.turns[i].item
    cands = set(range(A.N_AGENTS))
    cands -= {t.agent for t in ep.turns[:i] if t.revised}
    struck = {t.value for t in ep.turns[:i] if t.revised and t.item == item}
    cands = {a for a in cands
             if A.successor(ep.values[item][a]) not in struck}
    return 1.0 / max(1, len(cands))


def s3_features(ep, slot):
    """Ownership-blind features of one candidate answer slot. Mirrors the
    sweep's learned attack: structure only, never own_slot."""
    q, marker, item = query_facts(ep)
    tri = rendered(ep)
    on_item = [(v, mk, rev) for (it, v, mk, rev) in tri if it == item]
    vals = [v for v, _, _ in on_item]
    return [
        float(slot in vals),
        float(A.successor(slot) in vals),
        float(any(v == slot and mk == marker for v, mk, _ in on_item)),
        float(any(A.successor(v) == slot for v in vals)),
        float(any(A.successor(v) == slot and mk == marker
                  for v, mk, _ in on_item)),
        float(any(v == slot and rev for v, _, rev in on_item)),
        float(sum(1 for v in vals if v == slot)),
        float(A.SLOTS.index(slot)) / len(A.SLOTS),
        float(len(on_item)),
    ]


def s3_learned(eps, rng, n_fit):
    """Fit a ranker on ownership-blind features and score its top pick."""
    from sklearn.linear_model import LogisticRegression
    fit, test = eps[:n_fit], eps[n_fit:]
    X, y = [], []
    for ep in fit:
        q, _m, _i = query_facts(ep)
        for s in A.SLOTS:
            X.append(s3_features(ep, s))
            y.append(int(s == q.answer))
    clf = LogisticRegression(max_iter=2000).fit(np.array(X), np.array(y))
    hits = 0
    for ep in test:
        q, _m, _i = query_facts(ep)
        sc = clf.decision_function(
            np.array([s3_features(ep, s) for s in A.SLOTS]))
        hits += int(A.SLOTS[int(np.argmax(sc))] == q.answer)
    return hits / max(1, len(test))


def run(n: int, seed: int) -> dict:
    eps = [A.generate_episode(seed + i) for i in range(n)]
    rng = random.Random(seed)

    # --- known-answer checks, before anything new is reported
    s2 = float(np.mean([s2_registered_reference(e) for e in eps]))
    prim = [primary_reference(e) for e in eps]
    prim = float(np.mean([p for p in prim if p is not None]))
    checks = {
        "control_name_blind_reproduces_registered": {
            "measured": round(s2, 4), "registered": REGISTERED_CONTROL,
            "ok": abs(s2 - REGISTERED_CONTROL) <= CHECK_TOL},
        "primary_reproduces_registered": {
            "measured": round(prim, 4), "registered": REGISTERED_PRIMARY,
            "ok": abs(prim - REGISTERED_PRIMARY) <= CHECK_TOL},
    }
    harness_ok = all(c["ok"] for c in checks.values())

    s1 = float(np.mean([int(s1_name_keyed(e, rng) == query_facts(e)[0].answer)
                        for e in eps]))
    s3 = s3_learned(eps, rng, n_fit=n // 2)
    best = max(s1, s2, s3)

    if not harness_ok:
        v = {"verdict": "D — NOT MEASURABLE (HARNESS UNVERIFIED)",
             "means": "a known-answer check failed; no ceiling is asserted"}
    elif best > 0.90:
        v = {"verdict": "A — STRUCTURALLY UNSATISFIABLE",
             "means": ("a defined drop would need a baseline above 1.0, "
                       "which no model can reach, so the registered "
                       "differential clause was never computable for any "
                       "model at any budget on any architecture")}
    elif best > REGISTERED_CONTROL + BAND:
        v = {"verdict": "B — REGISTERED NUMBER WRONG, CLAUSE REACHABLE",
             "means": ("the registered ceiling is wrong by more than the "
                       "stated band, but a model could clear ceiling+0.10"),
             "accuracy_a_model_would_need": round(best + 0.10, 4)}
    else:
        v = {"verdict": "C — REGISTERED NUMBER SURVIVES",
             "means": ("no ownership-blind solver meaningfully beats the "
                       "registered figure; the permissive reading is wrong "
                       "and the control's failure is an ordinary learning "
                       "failure")}

    return {
        "measurement": "control battery ownership-blind ceiling",
        "method_committed_before_running": "ceiling-measurement-method.md, 2fba2ea",
        "registered": False, "loads_no_checkpoint": True,
        "n_episodes": n, "band": BAND,
        "known_answer_checks": checks, "harness_verified": harness_ok,
        "solvers": {
            "S1_name_keyed_lookup": round(s1, 4),
            "S2_registered_reference_expected": round(s2, 4),
            "S3_learned_attack": round(s3, 4),
            "S4_best_of_family": round(best, 4)},
        "note_on_kinds": ("S2 is an expected-value calculation, as the "
                          "registered figure is defined; S1 and S3 are "
                          "realized accuracies. Reported side by side and "
                          "the difference in kind is stated, not hidden."),
        "verdict": v,
    }


def self_test() -> None:
    eps = [A.generate_episode(4242 + i) for i in range(40)]
    rng = random.Random(0)
    for ep in eps[:5]:
        q, marker, item = query_facts(ep)
        assert marker in ep.markers, "marker parsed from the query text"
        assert q.answer in A.SLOTS, "answer is a slot"
    # The blindness scan must read CODE, not prose. A first version of
    # this tripped on its own docstring, which is the same self-match trap
    # the pod-reaper check hit earlier today: a scan a comment can satisfy
    # or defeat tests nothing. Strip docstrings and comments first.
    def code_only(text):
        import io, tokenize
        keep = []
        for tok in tokenize.generate_tokens(io.StringIO(text).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            keep.append(tok.string)
        return " ".join(keep)

    src = Path(__file__).read_text()
    for a, b, who in [("def s1_name_keyed", "def s2_", "S1"),
                      ("def s3_features", "def s3_learned", "S3")]:
        body = code_only(src[src.index(a):src.index(b)])
        assert "own_slot" not in body, f"{who} must be ownership-blind"
        assert "act_proj" not in body, f"{who} must not read the channel"
    s1 = np.mean([int(s1_name_keyed(e, rng) == query_facts(e)[0].answer)
                  for e in eps])
    assert 0.0 <= s1 <= 1.0, "score in range"
    print("self-test OK — query parsing, blindness scan, score range; "
          "no ceiling asserted")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--n", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=4242)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/ceiling_measure_a3.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite")
    res = run(a.n, a.seed)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
