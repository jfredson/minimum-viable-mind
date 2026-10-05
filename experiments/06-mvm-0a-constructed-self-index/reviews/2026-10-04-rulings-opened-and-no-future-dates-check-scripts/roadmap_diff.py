"""Compare data/roadmap.toml before and after commit 655b371.

Prints: every weekend whose status changed; every goal whose status changed;
any goal id or goal text that appears in more than one weekend after the
commit (the file's own rule: a carried goal is never copied into a later
weekend); and, for every goal marked "carried", whether its note names the
weekend it moved to (the file's own rule: "say which in `note`").

Run from the repository root:
    python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/roadmap_diff.py
"""
import collections, re, subprocess, tomllib

def load(rev):
    raw = subprocess.run(["git", "show", f"{rev}:data/roadmap.toml"],
                         capture_output=True, check=True).stdout
    return tomllib.loads(raw.decode())

before, after = load("655b371^"), load("655b371")
wb = {w["id"]: w for w in before["weekends"]}
wa = {w["id"]: w for w in after["weekends"]}

print("weekend status changes:")
n = 0
for wid in wa:
    if wb[wid]["status"] != wa[wid]["status"]:
        n += 1
        print(f"  {wid}: {wb[wid]['status']} -> {wa[wid]['status']}")
print(f"  total weekends changed: {n} of {len(wa)}")

gb = {g["id"]: g for w in before["weekends"] for g in w.get("goals", [])}
print("goal status changes:")
for w in after["weekends"]:
    for g in w.get("goals", []):
        old = gb.get(g["id"])
        if old is None:
            print(f"  {g['id']}: NEW GOAL")
        elif old["status"] != g["status"]:
            print(f"  {g['id']}: {old['status']} -> {g['status']}")
print(f"  goals before: {len(gb)}, after: {sum(len(w.get('goals', [])) for w in after['weekends'])}")

ids = collections.Counter(g["id"] for w in after["weekends"] for g in w.get("goals", []))
texts = collections.Counter(g["text"] for w in after["weekends"] for g in w.get("goals", []))
print("goal ids in more than one place:", [i for i, c in ids.items() if c > 1] or "none")
print("goal texts in more than one place:", [t[:50] for t, c in texts.items() if c > 1] or "none")

print("carried goals: does the note name a weekend?")
pat = re.compile(r"\bweekends? \d+|\bW\d+\b(?!\.)")
for w in after["weekends"]:
    for g in w.get("goals", []):
        if g["status"] == "carried":
            hit = pat.search(g.get("note", ""))
            print(f"  {g['id']}: {'names ' + repr(hit.group(0)) if hit else 'NAMES NO WEEKEND'}")
