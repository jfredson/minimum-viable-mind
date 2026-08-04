"""Registered figures for the Stage 3 ladder (pre-registration Amendment
2026-08-04). Reads artifacts/stage3/ladder_analysis_ci.json (produced by
analyze_ladder_ci.py) and writes four figures to ../figures/:

    retention_curves.png   preference-arm retention by rung, CI bands
    ri_forest.png          RI per (model, framing) per bank, 95% CIs
    outcome_stack.png      live / masked / capitulated shares at R3+probe
    item_heterogeneity.png per-item capitulation/masked counts (pooled)

Presentation only — no statistics are computed here beyond reading the
analyzer's output.

    ../../../.venv/bin/python plot_ladder.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402

CI_FILE = config.ARTIFACTS_DIR / "stage3" / "ladder_analysis_ci.json"
FIG_DIR = Path(__file__).resolve().parents[1] / "figures"

# dataviz reference palette (light mode), validated 2026-08-04:
# categorical slots 1-3 pass all-pairs; aqua < 3:1 contrast => direct
# labels / committed table view are the registered relief.
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, BASELINE, SURF = "#e1e0d9", "#c3c2b7", "#fcfcfb"
FRAMING_COLOR = {"tool": "#2a78d6", "tool_expert": "#eb6834", "mind": "#1baf7a"}
FRAMING_LABEL = {"tool": "tool", "tool_expert": "tool-expert", "mind": "mind"}
STATUS = {"live": "#0ca30c", "masked": "#fab219", "capitulated": "#d03b3b"}
FRAMINGS = ("tool", "tool_expert", "mind")
FOOT = ("95% percentile CIs, item-level bootstrap (B=10,000), n=30 items/bank; "
        "single decode per cell — item-sampling uncertainty only.")


MODEL_LABELS = {"claude-opus-4-8": "Opus 4.8", "claude-sonnet-5": "Sonnet 5",
                "gemini-3.1-pro-preview": "Gemini 3.1 Pro"}


def model_label(mid: str) -> str:
    return MODEL_LABELS.get(mid, mid)


def style(ax, ymax=1.05):
    ax.set_facecolor(SURF)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BASELINE)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, labelsize=8, length=0)
    if ymax:
        ax.set_ylim(0, ymax)


def load():
    d = json.loads(CI_FILE.read_text())
    models = sorted({k.split("|")[0] for k in d["cells"]})
    return d, models


def fig_curves(d, models):
    fig, axes = plt.subplots(2, len(models), figsize=(9.6, 5.6),
                             sharex=True, sharey=True)
    fig.set_facecolor(SURF)
    banks = (("bank_a", "pref_curve", "Bank A — held answer retained (mechanical)"),
             ("bank_b", "pref_live_curve", "Bank B — objection live (judged)"))
    for r, (bank, curve_key, rtitle) in enumerate(banks):
        for c, m in enumerate(models):
            ax = axes[r, c]
            style(ax)
            for fr in FRAMINGS:
                cell = d["cells"][f"{m}|{fr}"][bank][curve_key]
                x = [1, 2, 3]
                pts = [v["point"] for v in cell]
                ax.fill_between(x, [v["lo"] for v in cell],
                                [v["hi"] for v in cell],
                                color=FRAMING_COLOR[fr], alpha=0.15, lw=0)
                ax.plot(x, pts, color=FRAMING_COLOR[fr], lw=2,
                        marker="o", ms=5.5, label=FRAMING_LABEL[fr])
            ax.set_xticks([1, 2, 3], ["R1", "R2", "R3"])
            if r == 0:
                ax.set_title(model_label(m), fontsize=10, color=INK, pad=8)
            if c == 0:
                ax.set_ylabel(rtitle, fontsize=8, color=INK2)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper right", frameon=False,
               fontsize=8.5, labelcolor=INK2, ncol=3, bbox_to_anchor=(0.99, 1.0))
    fig.suptitle("Preference-arm retention by pressure rung",
                 fontsize=12, color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.01, FOOT, fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))
    fig.savefig(FIG_DIR / "retention_curves.png", dpi=200, facecolor=SURF)
    plt.close(fig)


def fig_forest(d, models):
    panels = (("bank_a", "Bank A (mechanical)"),
              ("bank_b", "Bank B (judged liveness)"),
              ("ri_combined", "Combined (n-weighted)"))
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.6), sharey=True)
    fig.set_facecolor(SURF)
    rows, ylabels, group_y = [], [], []
    y = 0
    for m in models:
        group_y.append((y, m))
        for fr in FRAMINGS:
            rows.append((y, m, fr))
            ylabels.append(FRAMING_LABEL[fr])
            y -= 1
        y -= 0.8
    for ax, (bank, title) in zip(axes, panels):
        style(ax, ymax=None)
        ax.grid(axis="x", color=GRID, linewidth=0.8)
        ax.grid(axis="y", visible=False)
        ax.axvline(0, color=BASELINE, lw=1)
        for ry, m, fr in rows:
            cell = d["cells"][f"{m}|{fr}"]
            v = cell[bank] if bank == "ri_combined" else cell[bank]["ri"]
            ax.plot([v["lo"], v["hi"]], [ry, ry], color=FRAMING_COLOR[fr], lw=2,
                    solid_capstyle="round")
            ax.plot(v["point"], ry, "o", ms=6.5, color=FRAMING_COLOR[fr],
                    mec=SURF, mew=1.5)
        ax.set_title(title, fontsize=9.5, color=INK, pad=8)
        ax.set_xlim(-0.55, 1.1)
        ax.set_xlabel("RI  =  P(retain | preference) − P(retain | evidence)",
                      fontsize=7.5, color=INK2)
    axes[0].set_ylim(rows[-1][0] - 0.9, 1.3)
    axes[0].set_yticks([r[0] for r in rows], ylabels)
    axes[0].tick_params(axis="y", labelcolor=INK2, labelsize=8.5)
    for gy, m in group_y:
        axes[0].text(-0.52, gy + 0.45, model_label(m), fontsize=9, color=INK,
                     weight="bold", ha="left", va="bottom")
    fig.suptitle("Retained independence with 95% CIs",
                 fontsize=12, color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.01, FOOT, fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(FIG_DIR / "ri_forest.png", dpi=200, facecolor=SURF)
    plt.close(fig)


def fig_stack(d, models):
    panels = (("bank_a", "pref_r3", "Bank A (mechanical)"),
              ("bank_b", "pref_live_r3", "Bank B (judged liveness)"))
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.4), sharey=True)
    fig.set_facecolor(SURF)
    for ax, (bank, live_key, title) in zip(axes, panels):
        style(ax)
        xticks, xlabels = [], []
        for gi, m in enumerate(models):
            for fi, fr in enumerate(FRAMINGS):
                x = gi * 4 + fi
                cell = d["cells"][f"{m}|{fr}"][bank]
                shares = (cell[live_key]["point"],
                          cell["masked_rate"]["point"],
                          cell["capitulated_rate"]["point"])
                bottom = 0.0
                for share, state in zip(shares, STATUS):
                    ax.bar(x, share, 0.86, bottom=bottom, color=STATUS[state],
                           edgecolor=SURF, linewidth=2)
                    if share >= 0.06:
                        ax.text(x, bottom + share / 2, f"{share:.0%}",
                                ha="center", va="center", fontsize=6.8,
                                color=SURF if state != "masked" else INK)
                    bottom += share
                xticks.append(x)
                xlabels.append(FRAMING_LABEL[fr].replace("tool-expert", "expert"))
            ax.text(gi * 4 + 1, -0.22, model_label(m), ha="center",
                    fontsize=8.5, color=INK, weight="bold")
        ax.set_xticks(xticks, xlabels, fontsize=7.5)
        ax.set_title(title, fontsize=9.5, color=INK, pad=8)
    handles = [plt.Rectangle((0, 0), 1, 1, color=STATUS[s]) for s in STATUS]
    fig.legend(handles, list(STATUS), loc="upper right", frameon=False,
               fontsize=8.5, labelcolor=INK2, ncol=3, bbox_to_anchor=(0.99, 1.0))
    fig.suptitle("Where positions go under preference pressure (R3 + de-pressured probe)",
                 fontsize=12, color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.01, "Point estimates; masked = surrendered at R3, intact at "
             "the probe; capitulated = gone even when released.\n"
             "Shares of n=30 preference-arm items per cell; single decode per "
             "cell.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.06, 1, 0.92))
    fig.savefig(FIG_DIR / "outcome_stack.png", dpi=200, facecolor=SURF)
    plt.close(fig)


def fig_items(d):
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 6.4))
    fig.set_facecolor(SURF)
    for ax, bank, title in ((axes[0], "bank_a", "Bank A items"),
                            (axes[1], "bank_b", "Bank B items")):
        items = d["per_item"][bank]
        order = sorted(items, key=lambda i: (items[i]["capitulated"],
                                             items[i]["masked"]), reverse=True)
        ys = np.arange(len(order))[::-1]
        cap = [items[i]["capitulated"] for i in order]
        msk = [items[i]["masked"] for i in order]
        style(ax, ymax=None)
        ax.grid(axis="x", color=GRID, linewidth=0.8)
        ax.grid(axis="y", visible=False)
        ax.barh(ys, cap, 0.72, color=STATUS["capitulated"],
                edgecolor=SURF, linewidth=1.5, label="capitulated")
        ax.barh(ys, msk, 0.72, left=cap, color=STATUS["masked"],
                edgecolor=SURF, linewidth=1.5, label="masked")
        ax.set_yticks(ys, order, fontsize=6.5)
        ax.tick_params(axis="y", labelcolor=MUTED)
        n_cells = items[order[0]]["n_cells"]
        ax.set_xlim(0, n_cells)
        ax.set_xlabel(f"preference-arm cells lost at R3 (of {n_cells})",
                      fontsize=8, color=INK2)
        conc = d["concentration"][bank]
        share = conc["top3_share"]
        sub = (f"{conc['total_capitulations']} capitulations pooled; "
               f"top-3 items carry {share:.0%}" if share is not None
               else "no capitulations pooled")
        ax.set_title(f"{title}\n{sub}", fontsize=9, color=INK, pad=8)
    axes[0].legend(loc="lower right", frameon=False, fontsize=8,
                   labelcolor=INK2)
    fig.suptitle("Which items carry the losses (pooled over models × framings)",
                 fontsize=12, color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.01, "Counts of (model, framing) preference cells; "
             "an aggregate carried by few items is a statement about those "
             "items, not the models.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    fig.savefig(FIG_DIR / "item_heterogeneity.png", dpi=200, facecolor=SURF)
    plt.close(fig)


def main():
    FIG_DIR.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "sans-serif", "text.color": INK,
                         "axes.labelcolor": INK2, "figure.facecolor": SURF})
    d, models = load()
    fig_curves(d, models)
    fig_forest(d, models)
    fig_stack(d, models)
    fig_items(d)
    print(f"wrote 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
