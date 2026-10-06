"""RT-243: which way do the two forms of the whole-state floor disagree, and
where? Walks every committed record carrying both forms, keeps the path to
each disagreement. Reads files only; imports nothing from the repository."""
import collections, glob, json, os, re
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../rehearsal-successor-measure/")


def walk(x, path):
    if isinstance(x, dict):
        if "clears" in x and "clears_plain_form" in x:
            yield path, x
        for k, v in x.items():
            yield from walk(v, path + (str(k),))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, path + ("[]",))


for pat in ("out-repairs/nominate_base_*.json", "out-grammar-c/nominate_base_F_T_C.json",
            "out-grammar-c/outcomes.json", "out-competing-solver-run/nominate_*.json",
            "out-v3-rules/nominate_*.json", "out-controls-rerun/nominate_*.json"):
    direction = collections.Counter()
    where = collections.Counter()
    for f in sorted(glob.glob(B + pat)):
        for path, r in walk(json.load(open(f)), ()):
            if r["clears"] != r["clears_plain_form"]:
                direction[f"plain {r['clears_plain_form']}, registered {r['clears']}"] += 1
                where[re.sub(r"\d+", "#", "/".join(p for p in path if p != "[]")[:80])] += 1
    print(pat, dict(direction))
    for w, n in where.most_common(8):
        print(f"    {n:5d}  {w}")
