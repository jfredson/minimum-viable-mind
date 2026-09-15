"""Regression check on the amended cue-detector sampler.

John's ruling of 2026-09-15, third condition: the amended detector must
be re-run against every grammar the original one already passed. The size
bias in the registered sampler can cut either way depending on which
agents speak more, so if it was HELPING some earlier grammar pass, that
has to surface now rather than later.

Grammars checked:

- **The registered MVM-0a grammar** (`curriculum.py`), which passed cue
  runs (i) and (ii) before the five existing checkpoints were trained.
  This is the important one: five trained checkpoints and every result in
  `lesion-results/` and `null-calibration/` rest on its clean verdict.
- **A3 draft 2**, every agent revising, which passed both gates on
  2026-09-15 before the shortcut sweep found its ceiling was 0.52.
- **A3 draft 3**, two revisers drawn uniformly, the current grammar.

The registered grammar is checked through its own detector
(`cue_detector.py`), reusing that module's classifier and bounds
untouched; only the sampling of the comparison turn changes, which is the
whole point of the amendment.

    ../../../.venv/bin/python sampler_regression.py
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import curriculum as C
import cue_detector as D0
import curriculum_a3 as A
import cue_detector_a3 as D3

OUT = Path(__file__).resolve().parents[1] / "a3-gates"
N_EPISODES = 4000
SEEDS = (20260804, 11, 22, 33, 44)


def _registered_examples(eps, seed, agent_uniform):
    """`cue_detector.build_examples` with the comparison turn drawn
    agent-first instead of pooled. Everything else is that function."""
    rng = np.random.default_rng(seed)
    texts, feats, labels = [], [], []
    for ep in eps:
        own = [(i, t) for i, t in enumerate(ep.turns)
               if t.agent == ep.own_slot]
        others = [a for a in range(ep.n_agents) if a != ep.own_slot]
        if agent_uniform:
            a = others[int(rng.integers(len(others)))]
            oth = [(i, t) for i, t in enumerate(ep.turns) if t.agent == a]
        else:
            oth = [(i, t) for i, t in enumerate(ep.turns)
                   if t.agent != ep.own_slot]
        if not own or not oth:
            continue
        pick_own = own[int(rng.integers(len(own)))]
        pick_oth = oth[int(rng.integers(len(oth)))]
        for (idx, turn), label in ((pick_own, 1), (pick_oth, 0)):
            texts.append(turn.render())
            feats.append([
                idx,
                idx / max(1, len(ep.turns) - 1),
                len(turn.render()),
                float(idx == 0),
                float(idx == len(ep.turns) - 1),
                sum(1 for t in ep.turns if t.agent == turn.agent),
                C.MARKERS.index(turn.marker),
            ])
            labels.append(label)
    return texts, np.asarray(feats, float), np.asarray(labels)


def registered_grammar(agent_uniform: bool) -> dict:
    aucs, ctl = [], []
    for sd in SEEDS:
        eps = C.generate_balanced(N_EPISODES, sd, forced_revision_frac=0.25)
        t, f, l = _registered_examples(eps, sd, agent_uniform)
        aucs.append(float(D0.fit_auc(t, f, l, sd)[0]))
        leaky = C.generate_balanced(N_EPISODES, sd, leaky=True,
                                    forced_revision_frac=0.25)
        t2, f2, l2 = _registered_examples(leaky, sd, agent_uniform)
        ctl.append(float(D0.fit_auc(t2, f2, l2, sd)[0]))
    a = np.array(aucs)
    return {"text_mean": round(float(a.mean()), 4),
            "text_sd": round(float(a.std(ddof=1)), 4),
            "weakest_positive_control": round(float(min(ctl)), 4),
            "GATE": "PASS" if (D0.EQUIV_LO <= a.mean() <= D0.EQUIV_HI
                               and min(ctl) >= D0.POSITIVE_CONTROL_MIN_AUC)
                    else "FAIL"}


def a3_grammar(k: int, agent_uniform: bool) -> dict:
    A.K_REVISERS = k
    A.N_TURNS = A.N_AGENTS * A.N_CONTESTED + k
    aucs, ctl = [], []
    for sd in SEEDS:
        eps = A.generate_balanced(N_EPISODES, sd)
        t, f, l = D3.build_examples(eps, seed=sd, agent_uniform=agent_uniform)
        aucs.append(float(D3.fit_auc(t, f, l, sd)[0]))
        leaky = A.generate_balanced(N_EPISODES, sd, leaky=True)
        t2, f2, l2 = D3.build_examples(leaky, seed=sd,
                                       agent_uniform=agent_uniform)
        ctl.append(float(D3.fit_auc(t2, f2, l2, sd)[0]))
    a = np.array(aucs)
    return {"text_mean": round(float(a.mean()), 4),
            "text_sd": round(float(a.std(ddof=1)), 4),
            "weakest_positive_control": round(float(min(ctl)), 4),
            "GATE": "PASS" if (D3.EQUIV_LO <= a.mean() <= D3.EQUIV_HI
                               and min(ctl) >= D3.POSITIVE_CONTROL_MIN_AUC)
                    else "FAIL"}


def main() -> None:
    rows = {}
    print("=== registered MVM-0a grammar (curriculum.py) ===", flush=True)
    rows["registered_grammar"] = {
        "registered_pooled": registered_grammar(False),
        "amended_agent_uniform": registered_grammar(True),
    }
    print(json.dumps(rows["registered_grammar"], indent=1), flush=True)
    for k, label in ((4, "a3_draft2_every_agent_revises"),
                     (2, "a3_draft3_two_revisers")):
        print(f"=== {label} ===", flush=True)
        rows[label] = {
            "registered_pooled": a3_grammar(k, False),
            "amended_agent_uniform": a3_grammar(k, True),
        }
        print(json.dumps(rows[label], indent=1), flush=True)
    A.K_REVISERS = 2
    A.N_TURNS = A.N_AGENTS * A.N_CONTESTED + 2

    out = {"check": "amended sampler re-run against every grammar the "
                    "registered sampler already passed (John, 2026-09-15)",
           "n_episodes": N_EPISODES, "seeds": list(SEEDS),
           "rows": rows}
    p = OUT / "sampler_regression.json"
    assert not p.exists(), f"refusing to overwrite {p} [C6]"
    p.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {p}\n")
    print("| grammar | registered (pooled) | amended (agent-uniform) |")
    print("|---|---|---|")
    for name, r in rows.items():
        print(f"| {name} | {r['registered_pooled']['GATE']} "
              f"({r['registered_pooled']['text_mean']:.4f}) | "
              f"{r['amended_agent_uniform']['GATE']} "
              f"({r['amended_agent_uniform']['text_mean']:.4f}) |")


if __name__ == "__main__":
    main()
