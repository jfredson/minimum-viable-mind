"""Can anything that does not know which agent it is beat the ceiling?

Red-team pass 3 (RT-20) found one ownership-free solver that scored 1.000
on the grammar Gate 1 had just certified: read the speaker's name sitting
three tokens back from the graded value, match it to the earlier
assignment, apply the rule. The grammar now renders the name after the
value, and that particular attack is dead.

A regression test for the attack you already found is worth very little.
One shortcut survived the design, its own self-test, and two passing cue
gates. So this sweeps a family of ownership-blind attacks against the
corrected grammar and reports the best score any of them reaches.

**The rule every attack here obeys:** it may use the full rendered
episode, every structural fact about it, and the shared revision rule. It
may NOT use `own_slot`, the acting channel, or anything derived from
them. That is exactly the knowledge A3 §2.1 says the task must require.

Two kinds of attack:

1. **Deterministic rules.** Pick one of the graded item's four earlier
   assignments by some ownership-blind heuristic — position, recency,
   register row, the alphabetical rank of its value, elimination against
   visible revisions — and emit its successor. Reported individually and
   as a best-of-family, because an adversary picks the best one.

2. **A learned attack**, which is the stronger test and mirrors how the
   cue gates work. Fit a classifier on ownership-blind features of each
   of the four candidate assignments to predict which one is the model's
   own, then score its top pick. Chance is 0.25. If a classifier beats
   that, the grammar leaks ownership into its structure and the ceiling
   is not a ceiling.

A pass means: no attack meaningfully exceeds the measured shortcut
ceiling of about 0.2925, and the learned attack sits at 0.25.

Corrigibility: generates data and fits a small classifier. No model, no
pod, no spend [C1/C2].

    ../../../.venv/bin/python shortcut_sweep.py --self-test
    ../../../.venv/bin/python shortcut_sweep.py --run
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import curriculum_a3 as A
import encoding_a3 as E

N_EPISODES = 4000
SEED = 20260915
CEILING = 0.2925


def _graded(ep):
    """The graded turn, its item, and the item's four earlier assignments
    in turn order — the candidate set every attack chooses from."""
    i = A.own_revision_index(ep)
    t = ep.turns[i]
    cands = [(j, x) for j, x in enumerate(ep.turns)
             if j < i and x.item == t.item and not x.revised]
    return i, t, cands


def _visible_revisions(ep, i, item):
    """Revisions of this item already in context at the graded position.
    Inverting the rule on one strikes its source value — the elimination
    a solver is entitled to."""
    return [x for j, x in enumerate(ep.turns)
            if j < i and x.item == item and x.revised]


# ------------------------------------------------------- deterministic

def _rules():
    """Each returns an index into the candidate list, or None."""
    def by_pos(k):
        return lambda ep, i, t, c: k if k < len(c) else None

    def by_value_rank(k):
        def f(ep, i, t, c):
            order = sorted(range(len(c)), key=lambda j: A.SLOTS.index(c[j][1].value))
            return order[k] if k < len(order) else None
        return f

    def by_reg_row(k):
        def f(ep, i, t, c):
            order = sorted(range(len(c)),
                           key=lambda j: E.VOCAB[c[j][1].marker])
            return order[k] if k < len(order) else None
        return f

    def by_other_turn_pos(last: bool):
        """Rank candidates by where that agent's OTHER assignment sits."""
        def f(ep, i, t, c):
            def other_pos(j):
                a = c[j][1].agent
                pos = [k for k, x in enumerate(ep.turns)
                       if x.agent == a and not x.revised
                       and x.item != t.item]
                return pos[0] if pos else -1
            order = sorted(range(len(c)), key=other_pos)
            return order[-1] if last else order[0]
        return f

    def eliminate(ep, i, t, c):
        """Strike candidates whose successor is already a visible revision
        of this item, then take the first survivor."""
        struck = {x.value for x in _visible_revisions(ep, i, t.item)}
        alive = [j for j in range(len(c))
                 if A.successor(c[j][1].value) not in struck]
        return alive[0] if alive else 0

    def already_revised(ep, i, t, c):
        """The attack the sweep found: any agent that has already taken
        its revision turn is not the agent revising now."""
        done = {x.agent for x in ep.turns[:i] if x.revised}
        alive = [j for j in range(len(c)) if c[j][1].agent not in done]
        return alive[0] if alive else 0

    def already_revised_random(ep, i, t, c):
        done = {x.agent for x in ep.turns[:i] if x.revised}
        struck = {x.value for x in _visible_revisions(ep, i, t.item)}
        alive = [j for j in range(len(c)) if c[j][1].agent not in done
                 and A.successor(c[j][1].value) not in struck]
        return random.choice(alive) if alive else 0

    def eliminate_random(ep, i, t, c):
        struck = {x.value for x in _visible_revisions(ep, i, t.item)}
        alive = [j for j in range(len(c))
                 if A.successor(c[j][1].value) not in struck]
        return random.choice(alive) if alive else 0

    rules = {f"position_{k}": by_pos(k) for k in range(A.N_AGENTS)}
    rules.update({f"value_rank_{k}": by_value_rank(k)
                  for k in range(A.N_AGENTS)})
    rules.update({f"register_row_{k}": by_reg_row(k)
                  for k in range(A.N_AGENTS)})
    rules["other_turn_earliest"] = by_other_turn_pos(False)
    rules["other_turn_latest"] = by_other_turn_pos(True)
    rules["eliminate_first"] = eliminate
    rules["eliminate_random"] = eliminate_random
    rules["already_revised_first"] = already_revised
    rules["already_revised_random"] = already_revised_random
    rules["marker_match_RT20"] = None       # handled specially
    return rules


def run_rules(eps) -> dict:
    rules = _rules()
    score = {k: 0 for k in rules}
    best_possible = 0
    for ep in eps:
        i, t, c = _graded(ep)
        target = A.act_target(ep)
        for name, fn in rules.items():
            if fn is None:
                g = A.ownership_free_solver(ep)
                score[name] += int(g == target) if g is not None else 0
                continue
            j = fn(ep, i, t, c)
            if j is None:
                continue
            score[name] += int(A.successor(c[j][1].value) == target)
        # an oracle over the family: could ANY rule have got it right?
        best_possible += int(any(
            fn is not None and (lambda j: j is not None
                                and A.successor(c[j][1].value) == target)(
                fn(ep, i, t, c)) for fn in rules.values()))
    n = len(eps)
    out = {k: round(v / n, 4) for k, v in sorted(
        score.items(), key=lambda kv: -kv[1])}
    out["_best_single_rule"] = max(out.values())
    out["_union_oracle"] = round(best_possible / n, 4)
    return out


# ------------------------------------------------------------- learned

def features(ep, i, t, c, j) -> list[float]:
    """Ownership-blind features of candidate j.

    **Everything here is computed on `ep.turns[:i]`, the context the model
    actually has at the graded position.** The first version of this
    function ranged over the whole episode, which let it read the graded
    turn itself: the own agent's "last spoke" index equalled the graded
    position in 300 of 300 episodes, so the attack scored a perfect 1.000
    and looked like a fatal leak. It was a bug in the attack. An attack
    allowed to see the answer proves nothing, and the self-test below now
    fails if any feature depends on a turn at or after the graded one.
    """
    pos, turn = c[j]
    agent = turn.agent
    seen = ep.turns[:i]                       # the visible prefix, nothing more
    same_agent = [k for k, x in enumerate(seen) if x.agent == agent]
    struck = {x.value for x in _visible_revisions(ep, i, t.item)}
    return [
        pos,                                   # where the assignment sits
        pos / max(1, len(ep.turns) - 1),
        i - pos,                               # distance to the graded turn
        j,                                     # rank in candidate order
        A.SLOTS.index(turn.value),             # the value itself
        E.VOCAB[turn.marker],                  # the speaker's name id
        sorted(range(len(c)),
               key=lambda k: E.VOCAB[c[k][1].marker]).index(j),  # reg row
        float(A.successor(turn.value) in struck),   # eliminated?
        len(same_agent),                       # its turns SO FAR
        min(same_agent) if same_agent else -1,  # when it first spoke
        max(same_agent) if same_agent else -1,  # when it last spoke so far
        float(any(x.revised for x in seen if x.agent == agent)),  # the leak

        sum(1 for x in seen if x.value == turn.value),  # value frequency
    ]


def run_learned(eps, seed: int) -> dict:
    X, y, groups = [], [], []
    for g, ep in enumerate(eps):
        i, t, c = _graded(ep)
        for j in range(len(c)):
            X.append(features(ep, i, t, c, j))
            y.append(int(c[j][1].agent == ep.own_slot))
            groups.append(g)
    X = np.asarray(X, float)
    y = np.asarray(y)
    groups = np.asarray(groups)
    gtr, gte = train_test_split(np.unique(groups), test_size=0.3,
                                random_state=seed)
    tr = np.isin(groups, gtr)
    te = np.isin(groups, gte)
    sc = StandardScaler().fit(X[tr])
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(sc.transform(X[tr]),
                                                       y[tr])
    p = clf.predict_proba(sc.transform(X[te]))[:, 1]
    # top-1 accuracy per episode: does the classifier pick the own one?
    hit = tot = 0
    for g in np.unique(groups[te]):
        m = groups[te] == g
        if m.sum() < 2:
            continue
        hit += int(y[te][m][p[m].argmax()] == 1)
        tot += 1
    return {"top1_accuracy": round(hit / max(1, tot), 4),
            "chance": round(1 / A.N_AGENTS, 4),
            "n_episodes_scored": int(tot),
            "n_features": X.shape[1]}


def sweep(n_episodes: int = N_EPISODES, seed: int = SEED) -> dict:
    random.seed(seed)
    eps = A.generate_balanced(n_episodes, seed)
    for k, ep in enumerate(eps):
        A.enact_own_turns(ep, random.Random(seed + k))
    # only episodes carrying a supervised action can be attacked
    eps = [e for e in eps if A.has_own_revision(e)]
    rules = run_rules(eps)
    learned = run_learned(eps, seed)
    worst = max(rules["_best_single_rule"], learned["top1_accuracy"])
    return {
        "sweep": "ownership-blind attacks on the corrected A3 grammar",
        "n_episodes": n_episodes, "seed": seed,
        "template": A.TEMPLATE,
        "measured_shortcut_ceiling": CEILING,
        "chance": round(1 / len(A.SLOTS), 4),
        "deterministic_rules": rules,
        "learned_attack": learned,
        "best_attack": round(worst, 4),
        "VERDICT": ("PASS — no ownership-blind attack beats the ceiling"
                    if worst <= CEILING + 0.03 else
                    "FAIL — an ownership-blind attack beats the ceiling"),
    }


def self_test() -> None:
    eps = A.generate_balanced(200, 3)
    for k, ep in enumerate(eps):
        A.enact_own_turns(ep, random.Random(k))
    eps = [e for e in eps if A.has_own_revision(e)]
    assert eps, "no episode carried a supervised action"
    for ep in eps:
        i, t, c = _graded(ep)
        assert len(c) == A.N_AGENTS, "four earlier assignments on the item"
        assert any(x.agent == ep.own_slot for _, x in c)
        # the target is the successor of exactly one candidate
        target = A.act_target(ep)
        owns = [j for j in range(len(c)) if c[j][1].agent == ep.own_slot]
        assert A.successor(c[owns[0]][1].value) == target
        # no feature may read own_slot: permuting which slot is "own"
        # must leave every feature vector unchanged
        f0 = [features(ep, i, t, c, j) for j in range(len(c))]
        saved = ep.own_slot
        ep.own_slot = (saved + 1) % A.N_AGENTS
        f1 = [features(ep, i, t, c, j) for j in range(len(c))]
        ep.own_slot = saved
        assert f0 == f1, "a feature leaks own_slot — the sweep is invalid"
        # No feature may depend on the graded turn or anything after it.
        # The first version of this file failed exactly here: it read the
        # own agent's last-spoken index, which IS the graded position.
        import copy
        ep2 = copy.deepcopy(ep)
        for x in ep2.turns[i:]:
            x.value = A.SLOTS[(A.SLOTS.index(x.value) + 3) % len(A.SLOTS)]
            x.marker = ep2.markers[(x.agent + 1) % A.N_AGENTS]
        i2, t2, c2 = i, ep2.turns[i], [(k, ep2.turns[k]) for k, _ in c]
        f2 = [features(ep2, i2, t2, c2, j) for j in range(len(c2))]
        assert f0 == f2, \
            "a feature reads the graded turn or later — the attack cheats"
    # RT-20's attack must be unavailable
    assert A.ownership_free_solver(eps[0]) is None
    print("shortcut_sweep self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--n", type=int, default=N_EPISODES)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.run:
        res = sweep(args.n, SEED)
        print(json.dumps(res, indent=2))
        if args.out:
            p = Path(args.out)
            assert not p.exists(), f"refusing to overwrite {p} [C6]"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(res, indent=2))
            print(f"\nwrote {p}")


if __name__ == "__main__":
    main()
