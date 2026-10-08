#!/usr/bin/env python3
"""Check 1, extension: does the A9 power arithmetic still hold when p is not
known but measured on the same 800 fresh pairs as the untouched rate, as
version 4 section 6.4 item 3 specifies ("the arm's own-directed accuracy on
the same fresh episodes")?

The author (and this check's a9_recompute.py) treated p as fixed. Here each
trial falls in one of these classes, and the exact joint distribution of the
two counts (correct C, hits on the donor's answer D) over 800 trials is built
by dynamic programming; the rule flags when |D/800 - (1 - C/800)/7| > 0.018.

  healthy pairing: correct (p), wrong onto the donor's answer (q), wrong elsewhere;
  broken pairing:  the donor's answer is unrelated to the trial and independent
                   of the model's output, so a trial is correct with chance p and
                   hits it with chance 1/8, independently (four classes).

No project code is imported. Run from the repository root with the project
Python (needs numpy).
"""
import numpy as np

N, ROOM = 800, 0.018


def joint(classes):
    """classes: list of (prob, dC, dD). Returns P[c, d] after N trials."""
    P = np.zeros((N + 1, N + 1))
    P[0, 0] = 1.0
    for _ in range(N):
        Q = np.zeros_like(P)
        for pr, dc, dd in classes:
            if pr == 0:
                continue
            Q[dc:, dd:] += pr * P[:N + 1 - dc, :N + 1 - dd]
        P = Q
    return P


def flag(P):
    c = np.arange(N + 1)[:, None] / N
    d = np.arange(N + 1)[None, :] / N
    return float(P[np.abs(d - (1 - c) / 7) > ROOM + 1e-12].sum())


cases = []
for p in (790 / 3000, 0.56):
    cases.append((f"broken pairing flagged, p = {p:.4f}",
                  [(p / 8, 1, 1), (7 * p / 8, 1, 0), ((1 - p) / 8, 0, 1), (7 * (1 - p) / 8, 0, 0)]))
for p in (790 / 3000, 0.56, 0.8):
    q = (1 - p) / 7
    cases.append((f"healthy, even errors, withheld, p = {p:.4f}", [(p, 1, 0), (q, 0, 1), (1 - p - q, 0, 0)]))
for p in (0.56, 0.8):
    q = (1 - p) / 3
    cases.append((f"healthy, review's case, withheld, p = {p:.4f}", [(p, 1, 0), (q, 0, 1), (1 - p - q, 0, 0)]))
print("p measured on the same 800 pairs (exact joint distribution):")
for label, cl in cases:
    print(f"  {label}: {flag(joint(cl)):.4f}")
