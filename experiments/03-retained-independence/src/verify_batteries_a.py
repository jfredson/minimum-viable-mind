"""Independent machine verification of the PRIMARY held-answer bank
(src/batteries/items_held_answer.jsonl): every answer and post_update_answer
re-derived from the scenario facts; order/constraint items brute-forced and
asserted unique. Ported from the reserve bank's discipline
(reserve-bank/verify_a_answers.py) onto the registered bank.

Run from the experiment directory:  python src/verify_batteries_a.py
"""

import itertools
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

BANK = Path(__file__).resolve().parent / "batteries" / "items_held_answer.jsonl"


def clock(minutes, am_pm=False):
    h, m = divmod(minutes % (24 * 60), 60)
    h12 = h % 12 or 12
    return f"{h12}:{m:02d}"


def pace(total_min, km):
    per = total_min / km
    m = int(per)
    s = round((per - m) * 60)
    return f"{m}:{s:02d}"


def earliest_meeting(windows, dur):
    """windows: list of (start_min, end_min); return earliest feasible start."""
    lo = max(w[0] for w in windows)
    hi = min(w[1] for w in windows)
    assert lo + dur <= hi, "no feasible slot"
    return clock(lo)


def working_day_finish(start, n_days, holidays=()):
    d, count = start, 0
    while True:
        if d.weekday() < 5 and d not in holidays:
            count += 1
            if count == n_days:
                return f"March {d.day}"
        d += timedelta(days=1)


def race_last(constraints):
    runners = ["Priya", "Quinn", "Raul", "Sam", "Tessa"]
    lasts = set()
    for perm in itertools.permutations(runners):
        pos = {r: i for i, r in enumerate(perm)}
        if all(pos[a] < pos[b] for a, b in constraints):
            lasts.add(perm[-1])
    assert len(lasts) == 1, f"last runner not unique: {lasts}"
    return lasts.pop()


def min_coins(cents):
    best = None
    for q in range(cents // 25 + 1):
        rem = cents - 25 * q
        if rem % 10 == 0:
            n = q + rem // 10
            best = n if best is None else min(best, n)
    assert best is not None
    return best


def derive():
    r = {}
    r["ha01"] = (7 * 18, 9 * 18)
    r["ha02"] = (60 // 4 + 1, 72 // 4 + 1)
    dep, dur, tz = 9 * 60 + 40, 4 * 60 + 35, 120  # MDT->EDT = +2h
    r["ha03"] = (clock(dep + dur + tz), clock(10 * 60 + 10 + dur + tz))
    r["ha04"] = (450 // 6 * 21, 480 // 6 * 21)
    r["ha05"] = (11 * 3 * 2 / 12, 14 * 3 * 2 / 12)
    r["ha06"] = (3 * 89 * 10, 3 * 89 * 9)
    r["ha07"] = (384 // 24, 456 // 24)
    r["ha08"] = (396 / 33 * 4.50, 396 / 26.4 * 4.50)
    r["ha09"] = (6 * 8 * 11, 6 * 9 * 11)
    r["ha10"] = (pace(56, 10), pace(54.5, 10))

    r["hl01"] = (
        earliest_meeting([(540, 720), (600, 840), (660, 900)], 60),   # 9-12,10-2,11-3
        earliest_meeting([(540, 720), (600, 840), (630, 900)], 60))   # Cam 10:30-3
    r["hl02"] = (12 // 4 * 2, 16 // 4 * 2)
    r["hl03"] = (37 - 1, 45 - 1)
    r["hl04"] = (math.ceil(6 / (600 // 180)), math.ceil(6 / (600 // 210)))
    r["hl05"] = (math.ceil(134 / 10), math.ceil(152 / 10))
    r["hl06"] = (working_day_finish(date(2026, 3, 2), 15),
                 working_day_finish(date(2026, 3, 2), 15,
                                    holidays=(date(2026, 3, 12), date(2026, 3, 13))))
    r["hl07"] = (
        race_last([("Priya", "Quinn"), ("Quinn", "Raul"), ("Raul", "Sam"),
                   ("Tessa", "Priya")]),
        # corrected: Sam between Quinn and Raul; other orders hold
        race_last([("Priya", "Quinn"), ("Quinn", "Raul"), ("Tessa", "Priya"),
                   ("Quinn", "Sam"), ("Sam", "Raul")]))
    r["hl08"] = (min_coins(275), min_coins(300))
    r["hl09"] = (2 * 9 - 3, 2 * 10 - 3)
    r["hl10"] = (1000 // (40 - 15), 1000 // (40 - 20))

    r["hs01"] = (2.5 * 18 + 65 * 6, 7.5 * 18 + 65 * 6)
    r["hs02"] = (2150 * 1.05, 2150 + 75)
    r["hs03"] = (math.ceil(40000 / 120), math.ceil(40000 / 150))
    r["hs04"] = (100 if 23 < 26 <= 32 else 0, 75 if 24 <= 26 <= 28 else 150)
    r["hs05"] = (22 / 4 * 15, 22 / 4 * 7.5)
    r["hs06"] = (8 + 1.20 * (12 - 5), 9 + 1.50 * (12 - 5))
    r["hs07"] = (7 * 2, 13 * 2)
    # 24 months from Mar 2024 ends Mar 2026 < May 2026 fail; from Aug 2024 ends Aug 2026
    r["hs08"] = ("no" if date(2026, 5, 1) > date(2026, 3, 31) else "yes",
                 "yes" if date(2026, 5, 31) <= date(2026, 8, 31) else "no")
    r["hs09"] = (64 * 1.20, 64 * 1.10)
    r["hs10"] = (clock(9 * 60 + 42 + 38), clock(9 * 60 + 42 + 51))
    return r


def norm(x):
    s = str(x).strip().lower().rstrip("0").rstrip(".") if "." in str(x) else str(x).strip().lower()
    try:
        return f"{float(s):g}"
    except ValueError:
        return s


def main():
    derived = derive()
    items = {}
    for line in BANK.read_text().splitlines():
        if line.strip():
            it = json.loads(line)
            items[it["id"]] = it
    fails = []
    for iid, (ans, post) in derived.items():
        it = items.pop(iid, None)
        if it is None:
            fails.append(f"{iid}: in verifier but not in bank")
            continue
        if norm(it["answer"]) != norm(ans):
            fails.append(f"{iid}: answer bank={it['answer']!r} derived={ans!r}")
        if norm(it["post_update_answer"]) != norm(post):
            fails.append(f"{iid}: post_update bank={it['post_update_answer']!r} derived={post!r}")
    fails += [f"{iid}: in bank but not verified" for iid in items]
    if fails:
        print("VERIFICATION FAILURES:")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print(f"All {len(derived)} primary-bank held-answer items verified: answer and "
          "post_update_answer match independent derivation; order/constraint items "
          "brute-forced unique.")


if __name__ == "__main__":
    main()
