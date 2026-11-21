"""The chained-lookup calibration trial of battery-authoring-spec.md, section 16.

Build the four versions on the Mac (free):
    .venv/bin/python -I src/chain_calibration.py build --out <dir>
Run them on a rented GPU machine:
    python -I src/chain_calibration.py run --dir <dir> --out <out dir>

Versions (section 16, item 2), in the order of preference of item 6:
    1 invented-full   invented names, distractor chains of two to six steps (the current task)
    2 invented-short  invented names, distractor chains of one step
    3 words-full      one-token common nouns, distractor chains of two to six steps
    4 words-short     one-token common nouns, distractor chains of one step
"""
import argparse
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

VERSIONS = [("invented-full", "invented", "full"), ("invented-short", "invented", "short"),
            ("words-full", "words", "full"), ("words-short", "words", "short")]
PER_LENGTH = 16
LENGTHS = [2, 3, 4, 5, 6]


def chain_item(b, rng, names_pool, hops, distractors, cid):
    """Section 16, items 1 and 2: five chains; the target has `hops` steps; distractors as the version says."""
    lengths = [hops] + [rng.randint(2, 6) if distractors == "full" else 1 for _ in range(4)]
    need = sum(L + 1 for L in lengths)
    if need > len(names_pool):
        raise ValueError(f"name pool of {len(names_pool)} too small for {need}")
    names = rng.sample(names_pool, need)
    cols = rng.sample(b.colours, 5)
    rows, starts, chains, k = [], [], [], 0
    for L, col in zip(lengths, cols):
        chain = names[k:k + L + 1]
        k += L + 1
        starts.append(chain[0])
        chains.append({"names": chain, "colour": col, "steps": L})
        rows += [f"{chain[j]} points to {chain[j + 1]}" for j in range(L)]
        rows.append(f"{chain[-1]} is {col}")
    rng.shuffle(rows)
    text = b.wrap("In this list: " + "; ".join(rows) + f". Start at {starts[0]} and follow the list to a colour. What colour do you reach?")
    cands = cols[:]
    rng.shuffle(cands)
    return {"id": cid, "hops": hops, "text": text, "answer": cols[0], "candidates": cands, "chains": chains,
            "rows": rows, "prompt_ids": b.m.ids(b.m.render(text))}


def build(a):
    from build import Builder, Model, load_lists, halves, DATA, TOKDIR_DEFAULT
    m = Model(a.tokdir or TOKDIR_DEFAULT)
    b = Builder(m, load_lists(), "A", 1, instruction="start")
    words_all = json.load(open(os.path.join(DATA, "chain_names.json")))
    words = [w for w in halves(words_all)["A"] if len(m.ids(" " + w)) == 1]
    pools = {"invented": b.inv_words, "words": words}
    report = {"half": "A", "seed": 1, "instruction": "start", "pools": {k: len(v) for k, v in pools.items()},
              "chain_names_in_list": len(words_all), "versions": {}}
    os.makedirs(a.out, exist_ok=True)
    for vi, (vname, names, distractors) in enumerate(VERSIONS, start=1):
        rng = random.Random(1 + vi)  # item 4: each version its own stream
        items = [chain_item(b, rng, pools[names], hops, distractors, f"A-cal-{vname}-{hops}-{i:02d}")
                 for hops in LENGTHS for i in range(PER_LENGTH)]
        with open(os.path.join(a.out, f"{vname}.jsonl"), "w") as f:
            for it in items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
        report["versions"][vname] = {"items": len(items),
                                     "prompt_tokens_by_length": {h: [min(len(x["prompt_ids"]) for x in items if x["hops"] == h),
                                                                     max(len(x["prompt_ids"]) for x in items if x["hops"] == h)] for h in LENGTHS}}
    json.dump(report, open(os.path.join(a.out, "build-report.json"), "w"), indent=1)
    print(json.dumps(report, indent=1))


def check(a):
    """Section 16, item 7: the free checks."""
    from tokenizers import Tokenizer
    from build import TOKDIR_DEFAULT, DATA
    tok = Tokenizer.from_file(os.path.join(a.tokdir or TOKDIR_DEFAULT, "tokenizer.json"))
    one = lambda s: len(tok.encode(s, add_special_tokens=False).ids) == 1
    problems = []
    words_all = json.load(open(os.path.join(DATA, "chain_names.json")))
    others = set(json.load(open(os.path.join(DATA, "words3.json")))) | set(json.load(open(os.path.join(DATA, "colours.json"))))
    for o in json.load(open(os.path.join(DATA, "objects.json"))):
        others |= set(o["object"].lower().split()) | {o["typical"]} | set(o["also"])
    for p in json.load(open(os.path.join(DATA, "opposites.json"))):
        others |= {p["a"].lower(), p["b"].lower()}
    for c in json.load(open(os.path.join(DATA, "countries.json"))):
        others |= set(str(c.get("name", "")).lower().split()) | set(str(c.get("capital", "")).lower().split())
    shared = sorted(set(words_all) & others)
    if shared:
        problems.append(f"chain_names shares words with other lists: {shared}")
    out = {"shared_words": shared, "versions": {}}
    for vname, names, distractors in VERSIONS:
        items = [json.loads(l) for l in open(os.path.join(a.dir, f"{vname}.jsonl"))]
        n_bad = 0
        for it in items:
            bad = []
            if not all(one(c) for c in it["candidates"]):
                bad.append("candidate not one token")
            ends = sorted(ch["colour"] for ch in it["chains"])
            if ends != sorted(it["candidates"]) or len(set(ends)) != 5:
                bad.append("candidates and chain ends differ")
            if it["chains"][0]["steps"] != it["hops"] or it["chains"][0]["colour"] != it["answer"]:
                bad.append("target chain wrong")
            if distractors == "short" and any(ch["steps"] != 1 for ch in it["chains"][1:]):
                bad.append("distractor not one step")
            if distractors == "full" and any(not 2 <= ch["steps"] <= 6 for ch in it["chains"][1:]):
                bad.append("distractor length out of range")
            all_names = [n for ch in it["chains"] for n in ch["names"]]
            if len(all_names) != len(set(all_names)):
                bad.append("name shared between chains")
            if names == "words" and not all(one(" " + n) for n in all_names):
                bad.append("name not one token")
            # follow the shuffled rows from the start name, as a reader must
            nxt = {}
            for r in it["rows"]:
                if " points to " in r:
                    x, y = r.split(" points to "); nxt[x] = ("name", y)
                else:
                    x, y = r.rsplit(" is ", 1); nxt[x] = ("colour", y)
            cur, steps = it["chains"][0]["names"][0], 0
            while nxt[cur][0] == "name":
                cur = nxt[cur][1]; steps += 1
            if nxt[cur][1] != it["answer"] or steps != it["hops"]:
                bad.append("following the rows does not give the answer in the stated steps")
            if bad:
                n_bad += 1
                problems.append(f"{it['id']}: {bad}")
        out["versions"][vname] = {"items": len(items), "items_with_problems": n_bad}
    out["problems"] = problems
    print(json.dumps(out, indent=1))
    sys.exit(1 if problems else 0)


def run(a):
    from step4a import MODEL_ID, MODEL_REVISION, Loop, candidate_ids, score
    import time
    import torch
    import transformers
    from transformers import AutoTokenizer
    os.makedirs(a.out, exist_ok=True)
    model = transformers.AutoModelForImageTextToText.from_pretrained(
        MODEL_ID, revision=MODEL_REVISION, device_map="cuda", dtype=torch.bfloat16)
    model.eval()
    tok = AutoTokenizer.from_pretrained(MODEL_ID, revision=MODEL_REVISION)
    tm = [m for m in model.modules() if hasattr(m, "message_input") and hasattr(m, "layers")][0]
    loop = Loop(tm)
    R = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "transformers": transformers.__version__, "dtype": "bfloat16",
         "versions": {}}
    for vname, _, _ in VERSIONS:
        items = [json.loads(l) for l in open(os.path.join(a.dir, f"{vname}.jsonl"))]
        res = {}
        for n in (1, 2, 3):
            loop.passes(n)
            res[n] = {}
            for it in items:
                ci = candidate_ids(tok, it["candidates"])
                res[n][it["id"]] = score(loop.run(model, it["prompt_ids"]), ci, it["candidates"].index(it["answer"]))
        loop.passes(3)
        acc = lambda n, sel: round(sum(res[n][x["id"]]["right"] for x in sel) / len(sel), 3)
        by_len = {str(n): {str(h): acc(n, [x for x in items if x["hops"] == h]) for h in LENGTHS} for n in (1, 2, 3)}
        long_ = [x for x in items if x["hops"] >= 4]
        a1, a3 = acc(1, long_), acc(3, long_)
        R["versions"][vname] = {"accuracy_by_length": by_len, "chains_4_to_6": {"1": a1, "2": acc(2, long_), "3": a3},
                                "three_minus_one_on_4_to_6": round(a3 - a1, 3),
                                "qualifies": a3 >= 0.50 and a3 - a1 >= 0.15,
                                "per_item": {str(n): {k: {"right": v["right"], "margin": v["margin"]} for k, v in res[n].items()} for n in (1, 3)}}
        json.dump(R, open(os.path.join(a.out, "chain-calibration-results.json"), "w"), indent=1)
        print(vname, json.dumps({k: R["versions"][vname][k] for k in ("chains_4_to_6", "three_minus_one_on_4_to_6", "qualifies")}),
              json.dumps(by_len["3"]))
    chosen = next((v for v, _, _ in VERSIONS if R["versions"][v]["qualifies"]), None)
    R["chosen_by_section_16_item_6"] = chosen
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(R, open(os.path.join(a.out, "chain-calibration-results.json"), "w"), indent=1)
    print("chosen", chosen)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("build"); p.add_argument("--out", required=True); p.add_argument("--tokdir")
    p = sub.add_parser("check"); p.add_argument("--dir", required=True); p.add_argument("--tokdir")
    p = sub.add_parser("run"); p.add_argument("--dir", required=True); p.add_argument("--out", required=True)
    a = ap.parse_args()
    {"build": build, "check": check, "run": run}[a.cmd](a)


if __name__ == "__main__":
    main()
