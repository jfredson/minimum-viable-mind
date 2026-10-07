"""Re-check of pull request 116 (second round): (a) what a top-up during a
wave costs the in-flight comparison, and (b) whether an honest bill can read
below the new 0.90 line.  $0; every vendor call is a stand-in.

(a) drives the alarm itself (watch_once, with a stand-in clock, balance and
machine list), the way its watcher would run: a reading every 5 minutes from
one minute after the first machine starts, charges posted `lag` minutes late
in 5-minute steps at `m` times the posted rate, and a $75 top-up at minute 13.
For each case it reports whether, and at which minute, the alarm trips.

(b) is arithmetic on the end-of-wave comparison: billed time over machine
life, when the machine's deletion time in the alarm's records is late (an
inferred deletion is up to one 5-minute reading late) or the laptop's
creation time is late.

    python tests/check-of-116/recheck_topup_and_bills.py   (from experiments/08-successor-degree)
"""
from __future__ import annotations

import math
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "src"))
import tripwire as T  # noqa: E402

RATE, DRIP, B0, T0 = 0.99, 0.01, 75.0, 1_900_000_000.0


def quiet(f, *a):
    so = sys.stdout
    sys.stdout = open(os.devnull, "w")
    try:
        return f(*a)
    finally:
        sys.stdout.close()
        sys.stdout = so


def run(machines, m=1.0, lag=8.0, topup_at=13.0, topup=75.0, step=5.0, after=30):
    """machines: list of (start_min, end_min). Returns (tripped_minute or None, final ratio)."""
    def spent(x):                                    # true spending up to minute x
        a = DRIP * max(0.0, x) / 60
        for c, g in machines:
            a += RATE * max(0.0, min(x, g) - c) / 60
        return a

    def balance(t):
        x = t - lag
        posted = 0.0 if x <= 0 else m * spent(math.floor(x / step) * step)
        return B0 - posted + (topup if topup_at is not None and t >= topup_at else 0.0)

    d = tempfile.mkdtemp()
    clock = [T0]
    T.now = lambda: clock[0]
    T.read_balance = lambda: balance((clock[0] - T0) / 60)
    T.running_pods = lambda: {f"p{i}" for i, (c, g) in enumerate(machines) if c <= (clock[0] - T0) / 60 < g}
    quiet(T.cmd_preflight, d)
    for i, (c, g) in enumerate(machines):
        clock[0] = T0 + c * 60
        quiet(T.cmd_register, d, f"p{i}", RATE, 2.0, "o")
    for i, (c, g) in enumerate(machines):            # every deletion recorded at once, as the fixes intend
        quiet(T.cmd_gone, d, f"p{i}", T0 + g * 60, "test")
    last = max(g for _, g in machines)
    tripped, t = None, 1.0
    while t <= last + after:
        clock[0] = T0 + t * 60
        r = quiet(T.watch_once, d, False)
        if r == "tripped":
            tripped = t
            break
        t += 5
    st = T.load_state(d)
    seg, back = T.segment(st["readings"])
    rb = T.ratio_b(seg, st["machines"], seg[-1]["t"], back)
    shutil.rmtree(d, ignore_errors=True)
    return tripped, rb.get("ratio")


print("(a) a $75 top-up at minute 13; charges posted late in 5-minute steps")
print("    honest waves first (must not trip), at several lags:")
for lag in (0, 6.5, 8, 12, 15, 20):
    for ms in ([(0, 40)], [(0, 120)], [(0, 60), (3, 63), (6, 66), (9, 69)]):
        tr, ra = run(ms, 1.0, lag)
        print(f"      lag {lag:>4} min, machines {ms if len(ms) == 1 else '4 x 60 min'}: "
              f"{'TRIPS at minute %g' % tr if tr else 'no trip'}; final {ra:.3f}")
print("    overbilled waves (should trip), lag 8 min, by length of the wave after the top-up:")
for m in (1.3, 1.4, 1.5, 2.0, 3.5):
    row = []
    for life in (40, 60, 120, 240, 480):
        tr, ra = run([(0, life)], m, 8)
        row.append(f"{life:>3} min: {'trip @%g' % tr if tr else 'MISSED (%.2f)' % ra}")
    print(f"      {m} times, one machine:  " + ";  ".join(row))
for m in (1.4, 2.0):
    tr, ra = run([(0, 60), (3, 63), (6, 66), (9, 69)], m, 8)
    print(f"      {m} times, four machines of 60 min: {'trip @%g' % tr if tr else 'MISSED (%.2f)' % ra}")
print("    the same 1.4 times, no top-up (for comparison):")
for life in (40, 60, 120):
    tr, ra = run([(0, life)], 1.4, 8, topup_at=None)
    print(f"      {life} min: {'trip @%g' % tr if tr else 'MISSED (%.2f)' % ra}")

print("\n(b) the end-of-wave comparison: billed time over machine life, honest bill")
print("    (the vendor bills from creation: the first 2026-09-25 machine billed 1,871.9 s")
print("     against 1,873 s of life by the laptop's clock, start-up time included)")
for life_min in (3, 10, 20, 30, 45, 60, 120):
    cells = []
    for late_s in (12, 60, 150, 300, 330):
        ra = (life_min * 60) / (life_min * 60 + late_s)
        cells.append(f"{late_s:>3}s late: {ra:.3f}{' TRIP' if ra < T.BILL_COMPLETE_MIN - 1e-9 else ''}")
    print(f"    life {life_min:>3} min, deletion time in the records  " + ";  ".join(cells))
print("    (12 s is the watchdog's own recorded time; up to 300-330 s is a deletion the watcher")
print("     only inferred: one reading interval plus the read; below 0.90 is 'cannot be checked yet')")
