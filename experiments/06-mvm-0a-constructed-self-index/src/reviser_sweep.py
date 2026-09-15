"""Decision 1, measured: how many agents should revise?

The A3 grammar has one free structural parameter, `K_REVISERS` — how many
of the four agents revise in an episode, drawn uniformly. Three drafts
have each picked a value and been surprised by what it cost. This
measures all four values on the same four axes, so the choice can be made
from a table instead of from an argument:

- **ownership-blind ceiling** — the best score any attack that does not
  know which agent the model is can reach (`shortcut_sweep`). Lower is
  better: it is the gap between "solved by a shortcut" and "solved by
  knowing which agent you are".
- **cell density** — the share of episodes that carry a supervised
  action, which sets how many episodes a 400-cell verdict needs.
- **cue gate, registered sampling** — one comparison turn pooled over all
  other agents. This draw is size-biased: an agent with more turns
  contributes more turns to the pool.
- **cue gate, agent-uniform sampling** — an other agent drawn uniformly
  first, then one of its turns. This is the contrast the design's
  exchangeability guarantees and carries no size bias.

The two samplings are expected to disagree whenever agents differ in how
much they speak, which is whenever K_REVISERS is not 4. Which of them the
gate should use is itself a decision, and it is the one that most changes
the answer.

Gates here run at a reduced episode count: this is a comparison between
options, not the registered verdict on the option that wins.

    ../../../.venv/bin/python reviser_sweep.py
"""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "a3-gates"
GATE_N = 2000
SWEEP_N = 6000


def measure(k: int) -> dict:
    import curriculum_a3 as A
    A.K_REVISERS = k
    A.N_TURNS = A.N_AGENTS * A.N_CONTESTED + k
    for m in ("encoding_a3", "cue_detector_a3", "shortcut_sweep"):
        if m in sys.modules:
            importlib.reload(sys.modules[m])
    import shortcut_sweep as S
    import cue_detector_a3 as D
    importlib.reload(S)
    importlib.reload(D)

    eps = A.generate_balanced(4000, 4242)
    density = sum(A.has_own_revision(e) for e in eps) / len(eps)

    sw = S.sweep(SWEEP_N, 20260915)
    row = {
        "k_revisers": k,
        "turns_per_episode": A.N_TURNS,
        "cell_density": round(density, 4),
        "episodes_for_400_cells": int(round(400 / max(density, 1e-9))),
        "ownership_blind_ceiling": sw["best_attack"],
        "sweep_verdict": sw["VERDICT"].split(" ")[0],
    }
    for label, au in (("registered_pooled", False), ("agent_uniform", True)):
        g = D.gate(GATE_N, D.SEED, au)
        row[f"gate_{label}"] = {
            "text_auc": g["runs"][0]["clean"]["auc"],
            "tensor_auc": g["runs"][1]["clean"]["auc"],
            "verdict": g["GATE"],
        }
    return row


def main() -> None:
    rows = []
    for k in (1, 2, 3, 4):
        print(f"=== K_REVISERS = {k} ===", flush=True)
        rows.append(measure(k))
        print(json.dumps(rows[-1], indent=1), flush=True)
    out = {
        "question": "A3 decision 1 — how many agents revise per episode?",
        "gate_n": GATE_N, "sweep_n": SWEEP_N,
        "note": "gates at reduced n: a comparison between options, not the "
                "registered verdict on the one that wins",
        "rows": rows,
    }
    p = OUT / "reviser_sweep.json"
    assert not p.exists(), f"refusing to overwrite {p} [C6]"
    p.write_text(json.dumps(out, indent=2))
    print(f"wrote {p}")
    print()
    print("| revisers | turns | cell density | eps for 400 cells | "
          "ownership-blind ceiling | gate (registered sampling) | "
          "gate (agent-uniform) |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['k_revisers']} | {r['turns_per_episode']} | "
              f"{r['cell_density']:.2f} | {r['episodes_for_400_cells']} | "
              f"{r['ownership_blind_ceiling']:.4f} | "
              f"{r['gate_registered_pooled']['verdict']} "
              f"({r['gate_registered_pooled']['tensor_auc']:.3f}) | "
              f"{r['gate_agent_uniform']['verdict']} "
              f"({r['gate_agent_uniform']['tensor_auc']:.3f}) |")


if __name__ == "__main__":
    main()
