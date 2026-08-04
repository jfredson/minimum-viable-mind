"""Fig. 4 artwork for the removal-test draft (pre-registration Amendment
2026-08-04). Reads artifacts/removal_test/removal_ci.json and writes
../figures/fig4_registered_run.png. Presentation only.

    ../../../.venv/bin/python plot_removal.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402

CI_FILE = config.ARTIFACTS_DIR / "removal_test" / "removal_ci.json"
FIG_DIR = Path(__file__).resolve().parents[1] / "figures"

INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, BASELINE, SURF = "#e1e0d9", "#c3c2b7", "#fcfcfb"
BLUE = "#2a78d6"

CONDS = (("idxres_mean_k16", "index-res\nmean", False),
         ("idxres_directional_k16", "index-res\ndirectional", False),
         ("narrative_mean_k16", "narrative †", True),
         ("expert_mean_k16", "expert\ncontrol †", True))
PANELS = (("T_self_irrelevant", "d(T_si) — self-irrelevant", 0.10),
          ("T_self_relevant", "d(T_sr) — self-relevant", 0.10),
          ("T_syntax", "d(T_syntax) — router control", 0.10),
          ("d_self", "d_self — judged self-report", 0.25))


def main():
    FIG_DIR.mkdir(exist_ok=True)
    d = json.loads(CI_FILE.read_text())["cells"]
    fig, axes = plt.subplots(1, 4, figsize=(10.4, 3.8))
    fig.set_facecolor(SURF)
    for ax, (key, title, theta) in zip(axes, PANELS):
        ax.set_facecolor(SURF)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(BASELINE)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(colors=MUTED, labelsize=7, length=0)
        ax.axhline(0, color=BASELINE, lw=1)
        ax.axhline(theta, color=INK2, lw=1.2, ls=(0, (4, 3)))
        label = "θ_task" if key != "d_self" else "θ_self"
        ax.text(3.45, theta, f"{label} = {theta:.2f}", fontsize=6.8,
                color=INK2, va="bottom", ha="right")
        for x, (cond, clabel, gated) in enumerate(CONDS):
            v = d[cond][key]
            color = MUTED if gated else BLUE
            ax.plot([x, x], [v["lo"], v["hi"]], color=color, lw=2,
                    solid_capstyle="round")
            ax.plot(x, v["point"], "o", ms=6.5, color=color,
                    mec=SURF, mew=1.5)
        ax.set_xticks(range(4), [c[1] for c in CONDS], fontsize=6.8)
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim((-0.22, 0.42) if key == "d_self" else (-0.06, 0.42))
        ax.set_title(title, fontsize=8.5, color=INK, pad=7)
    fig.suptitle("The registered run: drops against locked thresholds, 95% CIs",
                 fontsize=11.5, color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.015,
             "Item-level bootstrap (B=10,000; n = 32/30/30/30 items); single "
             "registered pass per condition — item-sampling uncertainty only. "
             "† = neutral-corpus Δnll gate breached (bound 0.0893); "
             "shown for completeness.", fontsize=6.6, color=MUTED)
    fig.tight_layout(rect=(0, 0.06, 1, 0.92))
    fig.savefig(FIG_DIR / "fig4_registered_run.png", dpi=200, facecolor=SURF)
    print(f"wrote {FIG_DIR / 'fig4_registered_run.png'}")


if __name__ == "__main__":
    main()
