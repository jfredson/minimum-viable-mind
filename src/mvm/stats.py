"""Shared bootstrap statistics for experiment analyzers.

Registered with the Stage 3 uncertainty amendment (pre-registration
Amendment 2026-08-04). Pure resampling helpers — no experiment-specific
arithmetic lives here, so Stage 1 / removal-test analyzers can reuse it.
"""
from __future__ import annotations

import numpy as np


def item_draws(n_items: int, n_boot: int, rng: np.random.Generator) -> np.ndarray:
    """Item-level bootstrap: (n_boot, n_items) index arrays, sampled with
    replacement from range(n_items)."""
    return rng.integers(0, n_items, size=(n_boot, n_items))


def two_level_draws(groups: list[list[int]], n_boot: int,
                    rng: np.random.Generator) -> np.ndarray:
    """Two-level (group -> item) bootstrap. `groups` maps each top-level
    unit (domain/category) to the item indices it owns. Each draw resamples
    len(groups) groups with replacement, then, within each chosen group,
    resamples its own item count with replacement. With equal-sized groups
    the draw size equals the original n."""
    n_groups = len(groups)
    out = np.empty((n_boot, sum(len(g) for g in groups)), dtype=np.int64)
    for b in range(n_boot):
        picked = rng.integers(0, n_groups, size=n_groups)
        parts = [np.asarray(groups[g])[rng.integers(0, len(groups[g]),
                                                    size=len(groups[g]))]
                 for g in picked]
        out[b] = np.concatenate(parts)
    return out


def summarize(point: float, samples: np.ndarray, alpha: float = 0.05) -> dict:
    """Percentile CI record: {point, lo, hi}."""
    lo, hi = np.quantile(samples, [alpha / 2, 1 - alpha / 2])
    return {"point": round(float(point), 4),
            "lo": round(float(lo), 4), "hi": round(float(hi), 4)}
