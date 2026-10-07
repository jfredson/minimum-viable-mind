"""Independent check of pull request 116: the two new rules of the spending
alarm against every recorded bill in the repository that can be turned into
"money drawn against money predicted".  $0: no vendor call, nothing rented.

Rule S (in flight): prediction >= $0.25 and drawn >= 1.25 x prediction + $0.05,
at the latest two readings.  Rule D (after a deletion): a reading at least 15
minutes after a recorded deletion, prediction >= $0.10, drawn >= 1.25 x
prediction + $0.02.  The arithmetic below is written here, not taken from the
alarm; the alarm's own rule functions are then run on the same readings and
the two answers compared.

    python tests/check-of-116/thresholds_against_records.py   (from experiments/08-successor-degree)
"""
from __future__ import annotations

import calendar
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "src"))
import tripwire as T  # noqa: E402

DRIP = 0.01


def ep(s: str) -> float:
    return float(calendar.timegm(time.strptime(s, "%Y-%m-%dT%H:%M:%SZ")))


def predicted(t0: float, t1: float, machines: list) -> float:
    p = DRIP * (t1 - t0) / 3600
    for c, g, rate in machines:
        a, b = max(t0, c), min(t1, g if g else t1)
        if b > a:
            p += rate * (b - a) / 3600
    return p


def mine(readings: list, machines: list) -> list:
    """For each reading after the first: (time, drawn, predicted, ratio, S over, D applies, D over)."""
    t0, b0 = readings[0]
    out = []
    for i, (t, b) in enumerate(readings[1:], 1):
        pr = predicted(t0, t, machines)
        dr = b0 - b
        s_over = pr >= 0.25 and dr >= 1.25 * pr + 0.05
        d_app = any(g and t - g >= 900 for _, g, _ in machines)
        d_over = d_app and pr >= 0.10 and dr >= 1.25 * pr + 0.02
        out.append((t, dr, pr, dr / pr if pr else None, s_over, d_app, d_over))
    trip_s = any(out[i][4] and out[i - 1][4] for i in range(1, len(out)))
    trip_d = any(o[6] for o in out)
    return out, trip_s, trip_d


def theirs(readings: list, machines: list) -> tuple:
    """The alarm's own rule functions on the same readings, reading by reading."""
    ms = {f"m{i}": dict(pod=f"m{i}", created=c, rate=r, gone=g) for i, (c, g, r) in enumerate(machines)}
    rs = [dict(t=t, balance=b) for t, b in readings]
    s_any = d_any = False
    for k in range(2, len(rs) + 1):
        vis = {p: dict(m, gone=(m["gone"] if m["gone"] and m["gone"] <= rs[k - 1]["t"] else None))
               for p, m in ms.items()}
        s_any |= T.rule_s(rs[:k], vis)["trip"]
        d_any |= T.rule_d(rs[:k], vis)["trip"]
    return s_any, d_any


def show(name: str, readings: list, machines: list, note: str = "") -> tuple:
    print(f"\n{name}")
    if note:
        print(f"  ({note})")
    rows, s, d = mine(readings, machines)
    for t, dr, pr, ra, so, da, do in rows:
        print(f"  {time.strftime('%H:%M:%S', time.gmtime(t))}  drawn ${dr:7.4f}  predicted ${pr:7.4f}  "
              f"ratio {'-' if ra is None else f'{ra:6.3f}'}  S over {'Y' if so else '.'}  "
              f"D applies {'Y' if da else '.'}  D over {'Y' if do else '.'}")
    ts, td = theirs(readings, machines)
    agree = (s, d) == (ts, td)
    print(f"  => rule S trips: {s}; rule D trips: {d}  (the alarm's own functions: S {ts}, D {td}; "
          f"{'agree' if agree else 'DISAGREE'})")
    return s or d, agree


results = {}

# 1. The 2026-10-04 development run: the alarm's own readings (fixture), the
#    check's 00:56:28 reading, the 01:11:20 reading; deletions at the
#    watchdogs' "pod gone" times.
FIX = os.path.join(HERE, "..", "fixtures", "dev-10m-2026-10-04")
snap = json.load(open(os.path.join(FIX, "state-0052Z.json")))
after = json.load(open(os.path.join(FIX, "state-after-0111Z.json")))
gone = {"pfk1yqygezezlo": "2026-10-05T00:40:02Z", "4kabf0hn4erbbg": "2026-10-05T00:34:56Z",
        "n4q0qur7iqdrom": "2026-10-05T00:38:01Z", "28guwiucofsjyr": "2026-10-05T00:40:22Z"}
mach = [(m["created"], ep(gone[p]), m["rate"]) for p, m in snap["machines"].items()]
rd = [(r["t"], r["balance"]) for r in snap["readings"]]
rd += [(snap["readings"][0]["t"] + 0.753 * 3600, 72.3178), (after["readings"][-1]["t"], after["readings"][-1]["balance"])]
rd.sort()
results["development run 2026-10-04 (honest)"] = show(
    "1. development run, 2026-10-04 (four machines, honest: final about 0.99)", rd, mach)

# 2. Rented slice, first attempt, 2026-09-25: machine c14x21x0u3ju7r
#    23:48:33 -> 00:19:46; balance 23:45:19 $76.4526535694, 00:19:56
#    $75.9553006582, 01:25:56 $75.917054611 (launcher-fix check vendor readings).
m2 = [(ep("2026-09-25T23:48:33Z"), ep("2026-09-26T00:19:46Z"), 0.99)]
r2 = [(ep("2026-09-25T23:45:19Z"), 76.4526535694), (ep("2026-09-26T00:19:56Z"), 75.9553006582),
      (ep("2026-09-26T01:25:56Z"), 75.917054611)]
results["rented slice, first attempt (honest)"] = show(
    "2. rented slice, first attempt, 2026-09-25 (one machine, 31 min, honest)", r2, m2,
    "only three readings exist; the vendor's bill for it, 1,871,875 ms against 1,873 s of life, is 1.00")

# 3. Rented slice, second attempt: machine alpua1c0w6jonx, 191 s of life,
#    deleted 01:49:43 (accepted) / gone 01:49:55.  Balance readings as recorded.
g3 = ep("2026-09-26T01:49:55Z")
m3 = [(g3 - 191.063 - 12, g3 - 12, 0.99)]
r3 = [(ep("2026-09-26T01:43:03Z"), 75.917054611), (ep("2026-09-26T01:50:01Z"), 75.917054611),
      (ep("2026-09-26T01:52:46Z"), 75.917054611), (ep("2026-09-26T01:54:04Z"), 75.864512286),
      (ep("2026-09-26T02:13:45Z"), 75.8547900638), (ep("2026-09-26T02:19:40Z"), 75.8547900638),
      (ep("2026-09-26T03:49:18Z"), 75.8450678416)]
results["rented slice, second attempt (honest)"] = show(
    "3. rented slice, second attempt, 2026-09-25 (one machine, 191 s, honest)", r3, m3,
    "prediction never reaches either floor: a 3-minute machine is below what either rule can judge")

# 4. The 2026-08-08 shape, modelled: billed 8.47 h for about 2.42 h of life
#    (3.5 times).  The record does not say WHEN the extra reached the balance;
#    it says the balance agreed with the bill the same day and the bill grew a
#    further 0.94 h overnight, after the machine was gone.  Three shapes, at the
#    successor's $0.99 rate (the 2026-08-08 machine was $0.69 community):
#    (a) the extra posts in flight at 3.5 times, 6.5 min late (the lag seen on
#        2026-10-04), readings every 5 minutes as the watcher takes them;
#    (b) in flight at the posted rate, the extra 2.5 times posted in one lump
#        2 hours after deletion (after the watcher has stopped);
#    (c) as (b) but the lump posts 20 minutes after deletion.
def wave(m_mult_inflight: float, lump_at_min: float | None, life_min: float = 145, lag_min: float = 6.5,
         rate: float = 0.99, stop_after_min: float = 30):
    c, g = 0.0, life_min * 60
    pts, t = [], 0.0
    while t <= g + stop_after_min * 60 + 1e-9:
        x = max(0.0, t - lag_min * 60)
        honest = DRIP * t / 3600 + rate * min(x, g) / 3600
        extra = (m_mult_inflight - 1) * rate * min(x, g) / 3600
        if lump_at_min is not None and t >= g + lump_at_min * 60:
            extra += 2.5 * rate * g / 3600
        pts.append((1e9 + t, 100.0 - honest - extra))
        t += 300
    return pts, [(1e9 + c, 1e9 + g, rate)]


for key, (mult, lump, note) in {
        "(a) 3.5 times, in flight": (3.5, None, "the extra reaches the balance while the machine runs"),
        "(b) lump 2 h after deletion": (1.0, 120, "the watcher stops 30 min after the last deletion"),
        "(c) lump 20 min after deletion": (1.0, 20, "inside the watcher's last 30 minutes")}.items():
    pts, m = wave(mult, lump)
    tripped, agree = show(f"4{key[:3]} the 2026-08-08 shape, modelled: {key[4:]}", pts, m, note)
    if tripped:
        # when: first reading of the trip, minutes after creation
        rows, _, _ = mine(pts, m)
        first = next((i for i in range(1, len(rows)) if rows[i][4] and rows[i - 1][4]), None)
        firstd = next((i for i in range(len(rows)) if rows[i][6]), None)
        i = min(x for x in (first, firstd) if x is not None)
        print(f"  first trip at minute {(rows[i][0] - 1e9) / 60:.0f} after creation")
    results[f"2026-08-08 shape {key}"] = (tripped, agree)

# 5. Honest made-up waves at the edges: one honest machine charged in advance,
#    in blocks of 5, 10, 15 or 20 minutes each charged in full at its start
#    (nothing recorded shows charges posting early; this is the worst case the
#    $0.05 allowance and the two-in-a-row rule must absorb), lengths 10 to 120 min.
print("\n5. honest machines charged in advance in blocks of 5 to 20 minutes, lengths 10 to 120 min")
worst = None
for life in (10, 15, 20, 30, 45, 60, 120):
    for early in (5, 10, 15, 20):
        g = life * 60
        pts, t = [], 0.0
        while t <= g + 1800:
            posted_to = 0.0 if t == 0 else min(g, (math.floor(t / (early * 60)) + 1) * early * 60)   # block charged at its start; the first reading is before any charge
            pts.append((1e9 + t, 100.0 - DRIP * t / 3600 - 0.99 * posted_to / 3600))
            t += 300
        rows, s, d = mine(pts, [(1e9, 1e9 + g, 0.99)])
        top = max((r[3] or 0) for r in rows if r[2] >= 0.25) if any(r[2] >= 0.25 for r in rows) else 0
        if s or d:
            print(f"  FALSE TRIP: life {life} min, blocks of {early} min: S {s}, D {d}")
        worst = max(worst or 0, top)
print(f"  highest in-flight ratio once the prediction passed $0.25: {worst:.3f}; no false trip unless listed above")

# 6. The end-of-wave comparison against a bill posted only in part: the first
#    attempt's machine had two hourly rows (566,260 ms and 1,305,615 ms).
print("\n6. end-of-wave comparison (billed hours against machine life), first attempt's machine")
life_h = 1873 / 3600
for label, ms in (("both rows posted", 566260 + 1305615), ("only the first hour's row posted", 566260),
                  ("only the second hour's row posted", 1305615)):
    ra = (ms / 3.6e6) / life_h
    print(f"  {label}: {ra:.3f} -> {'trip' if ra >= 1.25 else 'passes'}")
print("  (a bill posted in part passes as 'billed less than it lived'; the fix catches only an empty or zero bill)")

print("\nSUMMARY")
for k, (tripped, agree) in results.items():
    print(f"  {k}: {'TRIPS' if tripped else 'no trip'}; my arithmetic and the alarm's {'agree' if agree else 'DISAGREE'}")
