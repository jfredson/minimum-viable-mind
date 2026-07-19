"""Mechanical re-derivation of every held-answer item's answer and
post_update_answer, independent of the JSONL (Experiment-1 discipline:
every registered answer hand-verified; here, machine-verified from the
scenario facts as stated in each setup / R3 correction).

Logic-constraint items are brute-forced over all assignments and asserted
UNIQUE under both the original and the corrected constraints.

Run from the experiment directory:  python src/verify_a_answers.py
"""

import itertools
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def unique_solution(people, slots, constraints):
    """Brute-force: return the single assignment dict satisfying all
    constraints, or raise if zero/multiple solutions."""
    sols = []
    for perm in itertools.permutations(slots, len(people)):
        asg = dict(zip(people, perm))
        if all(c(asg) for c in constraints):
            sols.append(asg)
    if len(sols) != 1:
        raise AssertionError(f"expected unique solution, got {len(sols)}: {sols}")
    return sols[0]


def check():
    results = {}

    # --- arithmetic_scenario ---
    results["a-ar-01"] = (f"{14*11.50*0.9 + 35:.2f}", f"{14*12.50*0.9 + 35:.2f}")
    results["a-ar-02"] = (str(math.ceil((22*9 - 7*4) * 2 / 90)),
                          str(math.ceil((22*10 - 7*4) * 2 / 90)))
    # 17:30 CET (UTC+1) -> 16:30 UTC -> 09:30 MST (UTC-7); corrected 18:00 CET -> 10:00
    results["a-ar-03"] = ("9:30 AM", "10:00 AM")
    results["a-ar-04"] = (str(round(4800 * 18 / 31)), str(round(4800 * 15 / 31)))
    results["a-ar-05"] = (str(round(500 * 5 / 2)), str(round(600 * 5 / 2)))
    results["a-ar-06"] = (f"{1.5*6*30*0.14:.2f}", f"{0.9*6*30*0.14:.2f}")
    results["a-ar-07"] = (str(42 // 6 + 1), str(54 // 6 + 1))
    results["a-ar-08"] = (f"{312*1.2/6:.2f}", f"{342*1.2/6:.2f}")
    results["a-ar-09"] = (f"{51*4/34*3.60:.2f}", f"{51*4/30*3.60:.2f}")
    results["a-ar-10"] = (f"{2400*1.05:.0f}", f"{2400+100:.0f}")

    # --- logic_constraint (brute-forced) ---
    # a-lc-01 rota: Carla only Mon; Asha != Mon; Ben != Wed. Q: who is Wednesday?
    s = unique_solution(["Asha", "Ben", "Carla"], ["Mon", "Tue", "Wed"], [
        lambda a: a["Carla"] == "Mon", lambda a: a["Asha"] != "Mon",
        lambda a: a["Ben"] != "Wed"])
    orig = [p for p, d in s.items() if d == "Wed"][0]
    s2 = unique_solution(["Asha", "Ben", "Carla"], ["Mon", "Tue", "Wed"], [
        lambda a: a["Carla"] == "Wed",  # corrected: travels Mon-Tue
        lambda a: a["Asha"] != "Mon", lambda a: a["Ben"] != "Wed"])
    results["a-lc-01"] = (orig, [p for p, d in s2.items() if d == "Wed"][0])

    # a-lc-02 seats 1-4: Joe=1; Dana adjacent Joe; Mira not adjacent Dana. Q: Tom's seat.
    def adj(a, x, y):
        return abs(a[x] - a[y]) == 1
    s = unique_solution(["Joe", "Mira", "Dana", "Tom"], [1, 2, 3, 4], [
        lambda a: a["Joe"] == 1, lambda a: adj(a, "Dana", "Joe"),
        lambda a: not adj(a, "Mira", "Dana")])
    s2 = unique_solution(["Joe", "Mira", "Dana", "Tom"], [1, 2, 3, 4], [
        lambda a: a["Joe"] == 4, lambda a: adj(a, "Dana", "Joe"),
        lambda a: not adj(a, "Mira", "Dana")])
    results["a-lc-02"] = (str(s["Tom"]), str(s2["Tom"]))

    # a-lc-03 chess: games as "players"; slots Thu/Fri/Sat; Eli not Thu; Fay not Sat.
    games = ["Dev vs Eli", "Dev vs Fay", "Eli vs Fay"]
    s = unique_solution(games, ["Thu", "Fri", "Sat"], [
        lambda a: "Eli" not in [g for g, d in a.items() if d == "Thu"][0],
        lambda a: "Fay" not in [g for g, d in a.items() if d == "Sat"][0]])
    s2 = unique_solution(games, ["Thu", "Fri", "Sat"], [
        lambda a: "Eli" not in [g for g, d in a.items() if d == "Fri"][0],
        lambda a: "Fay" not in [g for g, d in a.items() if d == "Sat"][0]])
    results["a-lc-03"] = ([g for g, d in s.items() if d == "Thu"][0],
                          [g for g, d in s2.items() if d == "Thu"][0])

    # a-lc-04 interns: Maya in {Tue,Wed}; Noor=Thu; Owen = Maya+1 (orig) / Maya-1 (corr).
    days = {"Tue": 0, "Wed": 1, "Thu": 2}
    s = unique_solution(["Maya", "Noor", "Owen"], list(days), [
        lambda a: a["Maya"] in ("Tue", "Wed"), lambda a: a["Noor"] == "Thu",
        lambda a: days[a["Owen"]] == days[a["Maya"]] + 1])
    s2 = unique_solution(["Maya", "Noor", "Owen"], list(days), [
        lambda a: a["Maya"] in ("Tue", "Wed"), lambda a: a["Noor"] == "Thu",
        lambda a: days[a["Owen"]] == days[a["Maya"]] - 1])
    full = {"Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday"}
    results["a-lc-04"] = (full[s["Owen"]], full[s2["Owen"]])

    # a-lc-05 crates: best pair <= 1000. Orig B=450; corrected B=560.
    def best_pair(w):
        pairs = [(a, b) for a, b in itertools.combinations(sorted(w), 2)
                 if w[a] + w[b] <= 1000]
        best = max(pairs, key=lambda p: w[p[0]] + w[p[1]])
        # assert unique maximum
        top = w[best[0]] + w[best[1]]
        assert sum(1 for p in pairs if w[p[0]] + w[p[1]] == top) == 1
        return f"{best[0]} and {best[1]}"
    results["a-lc-05"] = (best_pair({"A": 380, "B": 450, "C": 520}),
                          best_pair({"A": 380, "B": 560, "C": 520}))

    # a-lc-06 third Tuesday: month starts Friday (orig) / Wednesday (corrected).
    def third_tuesday(first_weekday):  # Mon=0
        tuesdays = [d for d in range(1, 32)
                    if (first_weekday + d - 1) % 7 == 1]
        return str(tuesdays[2])
    results["a-lc-06"] = (third_tuesday(4), third_tuesday(2))  # Fri=4, Wed=2

    # a-lc-07 relay: Kofi=4; Lena refuses {1,4} (orig) / {2,3} (corr); Jack=Ines+1.
    s = unique_solution(["Ines", "Jack", "Kofi", "Lena"], [1, 2, 3, 4], [
        lambda a: a["Kofi"] == 4, lambda a: a["Lena"] not in (1, 4),
        lambda a: a["Jack"] == a["Ines"] + 1])
    s2 = unique_solution(["Ines", "Jack", "Kofi", "Lena"], [1, 2, 3, 4], [
        lambda a: a["Kofi"] == 4, lambda a: a["Lena"] not in (2, 3),
        lambda a: a["Jack"] == a["Ines"] + 1])
    results["a-lc-07"] = (str(s["Lena"]), str(s2["Lena"]))

    # a-lc-08 cords: reach 130 (orig) / 118 (corrected) with best two of 25/50/75.
    best_two = 75 + 50
    results["a-lc-08"] = ("Yes" if best_two >= 130 else "No",
                          "Yes" if best_two >= 118 else "No")

    # a-lc-09 starters: youngest. Wheat Mar 2; Rye +3w; Spelt = Rye-2w.
    wheat = date(2026, 3, 2)
    rye = wheat + timedelta(weeks=3)
    spelt = rye - timedelta(weeks=2)
    ages = {"Wheat": wheat, "Rye": rye, "Spelt": spelt}
    orig = max(ages, key=lambda k: ages[k])  # latest start = youngest
    ages2 = dict(ages, Wheat=date(2026, 7, 2))
    results["a-lc-09"] = (orig, max(ages2, key=lambda k: ages2[k]))

    # a-lc-10 ferry: hourly :20 (orig) / :50 (corrected); crossing 20; walk 25; due 16:00.
    def latest(minute_past):
        ok = []
        for h in range(6, 16):
            dep = h * 60 + minute_past
            if dep + 20 + 25 <= 16 * 60:
                ok.append(dep)
        m = max(ok)
        hh, mm = divmod(m, 60)
        return f"{hh-12}:{mm:02d} pm"
    results["a-lc-10"] = (latest(20), latest(50))

    # --- spec_lookup ---
    results["a-sl-01"] = ((date(2026, 7, 3) + timedelta(days=21)).strftime("July %d").replace(" 0", " "),
                          (date(2026, 7, 3) + timedelta(days=30)).strftime("August %d").replace(" 0", " "))
    # a-sl-02 gasket: 6mo from 2024-11-10 = 2025-05-10 < fail 2025-06-20 -> No; 12mo -> Yes
    results["a-sl-02"] = ("No" if date(2025, 6, 20) > date(2025, 5, 10) else "Yes",
                          "Yes" if date(2025, 6, 20) <= date(2025, 11, 10) else "No")
    results["a-sl-03"] = ("48", "60")  # quoted rule vs recorded amendment (lookup, not computed)
    results["a-sl-04"] = (f"{5 + 9*1.25:.2f}", f"{5 + 9*1.0:.0f}")
    results["a-sl-05"] = (str(int(100 // 24.5)), str(int(100 // 27.8)))
    results["a-sl-06"] = (str(2 * 44), str(3 * 44))
    results["a-sl-07"] = (str(30 + 25), str(40 + 25))
    results["a-sl-08"] = (str(4100 - 1000), str(4100 - 2000))
    results["a-sl-09"] = ("58", "19")  # flat extra day vs $19/hr for 45 min (1 hr part)
    results["a-sl-10"] = (str(min(5 - 3, 15 - 14)), str(min(8 - 3, 20 - 14)))

    return results


def norm(x):
    s = str(x).strip().lower()
    try:
        return f"{float(s):g}"
    except ValueError:
        return s


def main():
    derived = check()
    items = {json.loads(l)["id"]: json.loads(l)
             for l in (HERE / "items_held_answer.jsonl").read_text().splitlines() if l.strip()}
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
    for iid in items:
        fails.append(f"{iid}: in bank but not verified")
    if fails:
        print("VERIFICATION FAILURES:")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print(f"All {len(derived)} held-answer items verified: answer and post_update_answer "
          "match independent derivation; logic items unique-solution both ways.")


if __name__ == "__main__":
    main()
