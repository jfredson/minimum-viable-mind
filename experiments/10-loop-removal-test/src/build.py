"""Generator for the loop removal test's task batteries.

Follows experiments/10-loop-removal-test/battery-authoring-spec.md (committed 2026-11-21, before this file).
Section numbers in comments refer to that specification. Run with the project Python and -I:

    .venv/bin/python -I experiments/10-loop-removal-test/src/build.py --half A --seed 1 --out <dir>

It reads the research model's tokeniser and chat template from the project's ignored model cache, and
writes JSON lines. It downloads nothing.
"""
import argparse
import itertools
import json
import os
import random
import re
import sys

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.sandbox import ImmutableSandboxedEnvironment
from tokenizers import Tokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(EXP))
DATA = os.path.join(EXP, "data")
TOKDIR_DEFAULT = os.path.join(REPO, ".hf-cache.nosync", "tml-d24-varloop-research-tokenizer")
REPLY_OPENING = "<|message_model|><|content_text|>"  # section 6; step 4a confirms (section 9)

# The split test's syllables (experiments/09-split-removal-test/src/batteries.py, SYLL_A and SYLL_B).
SYLL_A = ["zib", "tov", "mek", "dap", "rul", "fen", "gox", "lir", "pash", "wud", "kel", "sorn"]
SYLL_B = ["vam", "jot", "nix", "bré", "quo", "hesk", "dral", "yim", "plo", "tusk", "wev", "zar"]
SYMBOLS = ["◇", "⊛", "⋄", "⊕", "⊗", "△", "▽", "⊞"]  # shared pool, section 2

RULE_KINDS = ["op", "unit", "code", "look"]
ROUTINE_KINDS = ["sum", "prod", "cap", "opp", "col"]
ALLOWED = {"op": ["cap", "opp", "col"], "unit": ["cap", "opp", "col"],
           "code": ["sum", "prod", "cap", "col"], "look": ["sum", "prod", "cap", "opp"]}  # section 5

# Section 6: the fixed final questions, one wording on each side per pairing.
QUESTIONS = {
    ("op", "cap"): ("What does the rule give for them?", "What is the capital of the country?"),
    ("op", "opp"): ("What does the rule give for them?", "What is the opposite of the word?"),
    ("op", "col"): ("What does the rule give for them?", "What colour is the object most often?"),
    ("unit", "cap"): ("How many of the second unit is that?", "What is the capital city of the country?"),
    ("unit", "opp"): ("How many of the second unit?", "Give the opposite of the word."),
    ("unit", "col"): ("How many of the second unit is that?", "Usually, what colour is the object?"),
    ("code", "sum"): ("What word is the coded word here?", "What is the sum of the two numbers?"),
    ("code", "prod"): ("What word is the coded word?", "What do the two numbers multiply to?"),
    ("code", "cap"): ("What word is the coded word?", "What is the capital of the country?"),
    ("code", "col"): ("What word is the coded word?", "What colour is the object most often?"),
    ("look", "sum"): ("What colour does the table give the name?", "What is the sum of the two numbers?"),
    ("look", "prod"): ("What colour does the table give the name?", "What is the product of the two numbers?"),
    ("look", "cap"): ("What colour does the table give the name?", "What is the capital city of the country?"),
    ("look", "opp"): ("What colour does the table give the name?", "What is the opposite of the given word?"),
}

# Pilot allocation (section 10): 30 pairs per rule kind, at most 30 per routine kind (25% cap), even spread.
PILOT_ALLOCATION = {
    ("op", "cap"): 7, ("op", "opp"): 11, ("op", "col"): 12,
    ("unit", "cap"): 7, ("unit", "opp"): 11, ("unit", "col"): 12,
    ("code", "sum"): 8, ("code", "prod"): 8, ("code", "cap"): 8, ("code", "col"): 6,
    ("look", "sum"): 7, ("look", "prod"): 7, ("look", "cap"): 8, ("look", "opp"): 8,
}

# Specification, section 14, item 3: the copying rule ignores only these function words.
STOP = {"a", "an", "the", "is", "of", "and", "to", "do", "does", "that", "what", "how", "many", "for", "them",
        "it", "in", "this", "each", "be"}


class Generation(Extension):
    """Treats the Hugging Face {% generation %}...{% endgeneration %} tag as a plain block."""
    tags = {"generation"}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(["name:endgeneration"], drop_needle=True)
        return nodes.Scope(body, lineno=lineno)


class Model:
    def __init__(self, tokdir):
        self.tok = Tokenizer.from_file(os.path.join(tokdir, "tokenizer.json"))
        env = ImmutableSandboxedEnvironment(trim_blocks=True, lstrip_blocks=True, extensions=[Generation])

        def raise_exception(m):
            raise ValueError(m)
        env.globals["raise_exception"] = raise_exception
        self.template = env.from_string(open(os.path.join(tokdir, "chat_template.jinja")).read())

    def render(self, user_text):
        out = self.template.render(messages=[{"role": "user", "content": user_text}],
                                   add_generation_prompt=True, reasoning_effort="none")
        return out + REPLY_OPENING

    def ids(self, s):
        return self.tok.encode(s, add_special_tokens=False).ids

    def one_token(self, s):
        return len(self.ids(s)) == 1


def halves(items, seed=0):
    """Section 2: one fixed split with seed 0; an odd item goes to half B."""
    idx = list(range(len(items)))
    random.Random(seed).shuffle(idx)
    k = len(items) // 2
    a = [items[i] for i in idx[:k]]
    b = [items[i] for i in idx[k:]]
    return {"A": a, "B": b}


def load_lists():
    j = lambda n: json.load(open(os.path.join(DATA, n)))
    return {"countries": j("countries.json"), "regions": j("regions.json")["nearest_neighbouring_region"],
            "opposites": j("opposites.json"), "objects": j("objects.json"), "words3": j("words3.json"),
            "colours": j("colours.json")}


def content_words(*texts):
    ws = set()
    for t in texts:
        for w in re.findall(r"[A-Za-z']+", t.lower()):
            if w not in STOP and len(w) >= 3:
                ws.add(w)
    return ws


def copies(cand, words):
    """Section 7: the copying rule, on whole words; numbers exempt."""
    if cand.isdigit():
        return False
    c = cand.lower()
    for w in words:
        if c in w or w in c:
            return True
    return False


def near_numbers(rng, ans, spread, lo=0, hi=999, pool=None):
    """Specification, section 14, item 2: the right answer's place among the five, in numeric order, is drawn
    uniformly first; the wrong numbers are then drawn below and above it. Returns None if the place cannot be
    filled, and the caller redraws the item."""
    digits = len(str(ans))
    opts = [x for x in (pool if pool is not None else range(max(lo, ans - spread), min(hi, ans + spread) + 1))
            if x != ans and len(str(x)) == digits and abs(x - ans) <= spread]
    place = rng.randrange(5)
    below = [x for x in opts if x < ans]
    above = [x for x in opts if x > ans]
    if len(below) < place or len(above) < 4 - place:
        return None
    return [str(x) for x in rng.sample(below, place) + rng.sample(above, 4 - place)]


class Builder:
    def __init__(self, model, lists, half, seed):
        self.m, self.L, self.half = model, lists, half
        self.rng = random.Random(seed)
        self.stats = {"dropped": {}, "capital_wrong_source": {"same_region": 0, "neighbour_region": 0, "dropped": 0}}
        H = lambda x: halves(x)[half]
        self.syl1, self.syl2 = H(SYLL_A), H(SYLL_B)
        self.inv_words = [a + b for a in self.syl1 for b in self.syl2]
        cols = lists["colours"]
        self.colours = [c for c in cols if model.one_token(c)]
        # countries: single-token capitals, no name overlap as right answers (section 3)
        half_c = H(lists["countries"])
        self.capitals_ok = [c for c in half_c if model.one_token(c["capital"])]
        self.capital_answers = [c for c in self.capitals_ok if not c["name_overlap"]]
        self.drop("capital_not_one_token", len(half_c) - len(self.capitals_ok))
        self.drop("capital_name_overlap", len(self.capitals_ok) - len(self.capital_answers))
        # opposites: each direction is a question; answer single token
        half_o = H(lists["opposites"])
        self.opp_pairs = half_o
        self.opp_questions = [(p["a"], p["b"]) for p in half_o] + [(p["b"], p["a"]) for p in half_o]
        n0 = len(self.opp_questions)
        self.opp_questions = [q for q in self.opp_questions if model.one_token(q[1])]
        self.drop("opposite_answer_not_one_token", n0 - len(self.opp_questions))
        self.objects = [o for o in H(lists["objects"]) if model.one_token(o["typical"])]
        self.words3 = [w for w in H(lists["words3"]) if model.one_token(w)]
        self.used_routine, self.used_rule = set(), set()

    def drop(self, why, n=1):
        self.stats["dropped"][why] = self.stats["dropped"].get(why, 0) + n

    # ---------- rule kinds (section 4)
    def rule_op(self):
        lo, hi = (2, 15) if self.half == "A" else (25, 99)
        shapes = [("2 times a, plus b", lambda a, b: 2 * a + b), ("a plus 2 times b", lambda a, b: a + 2 * b),
                  ("3 times a, minus b", lambda a, b: 3 * a - b), ("a times 2, minus b, plus 1", lambda a, b: 2 * a - b + 1)]
        for _ in range(200):
            a, b = self.rng.randint(lo, hi), self.rng.randint(lo, hi)
            name, f = self.rng.choice(shapes)
            ans = f(a, b)
            # half A operands give answers of 10 to 45; half B answers are kept at 100 to 999 so that no
            # operator answer value is possible in both halves (specification, section 11)
            if (10 <= ans <= 45) if self.half == "A" else (100 <= ans <= 999):
                sym = self.rng.choice(SYMBOLS)
                wrong = near_numbers(self.rng, ans, 5)
                if wrong:
                    return {"rule": f"In this puzzle, a {sym} b means {name}.", "facts": f"Here a is {a} and b is {b}.",
                            "answer": str(ans), "wrong": wrong, "content": ("op", sym, name, a, b)}
        self.drop("operator_no_valid_item")
        return None

    def rule_unit(self):
        klo, khi, nlo, nhi = (2, 5, 2, 9) if self.half == "A" else (6, 9, 11, 99)
        u1, u2 = self.rng.sample(self.inv_words, 2)
        k, n = self.rng.randint(klo, khi), self.rng.randint(nlo, nhi)
        ans = k * n
        wrong = near_numbers(self.rng, ans, 5)
        if not wrong:
            self.drop("unit_no_wrong_answers")
            return None
        return {"rule": f"In this puzzle, 1 {u1} is {k} {u2}s.", "facts": f"You have {n} {u1}s.",
                "answer": str(ans), "wrong": wrong, "content": ("unit", u1, u2, k, n)}

    def rule_code(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for _ in range(200):
            w = self.rng.choice(self.words3)
            others = [x for x in self.words3 if x != w]
            best = None
            for _ in range(60):
                extra = self.rng.sample([c for c in letters if c not in w], 5)
                plain = set(w) | set(extra)
                spell = [x for x in others if set(x) <= plain]
                if len(spell) >= 4:
                    best = (extra, spell)
                    break
            if not best:
                continue
            extra, spell = best
            plain = list(w) + extra
            code = self.rng.sample(letters, 26)
            mapping, pool = {}, [c for c in code]
            for p in plain:
                choices = [c for c in pool if c != p]
                c = choices[0]
                pool.remove(c)
                mapping[p] = c
            cipher = "".join(mapping[ch] for ch in w)
            wrong = self.rng.sample(spell, 4)
            if cipher in wrong or cipher == w:
                continue
            rows = [f"{mapping[p]} stands for {p}" for p in plain]
            self.rng.shuffle(rows)
            return {"rule": "In this code, each letter stands for another: " + ", ".join(rows) + ".",
                    "facts": f"The coded word is {cipher}.", "answer": w, "wrong": wrong,
                    "content": ("code", w, tuple(sorted(mapping.items())))}
        self.drop("code_no_valid_item")
        return None

    def rule_look(self):
        names = self.rng.sample(self.inv_words, 6)
        cols = self.rng.sample(self.colours, 6)
        t = self.rng.randrange(6)
        rows = [f"a {n} is {c}" for n, c in zip(names, cols)]
        wrong = self.rng.sample([c for i, c in enumerate(cols) if i != t], 4)
        return {"rule": "In this table, each name has a colour: " + ", ".join(rows) + ".",
                "facts": f"The name to look up is {names[t]}.", "answer": cols[t], "wrong": wrong,
                "content": ("look", tuple(names), tuple(cols), t)}

    def rule(self, kind):
        return getattr(self, "rule_" + kind)()

    # ---------- routine kinds (section 5)
    def routine(self, kind, allow_reuse=False):
        for _ in range(500):
            r = getattr(self, "rt_" + kind)()
            if r is None:
                return None
            key = r["content"]
            if allow_reuse or key not in self.used_routine:
                return r
        self.drop(f"routine_{kind}_pool_exhausted")
        return None

    def rt_sum(self):
        lo, hi = (4, 49) if self.half == "A" else (50, 99)
        s = self.rng.randint(lo, hi)
        a = self.rng.randint(2, s // 2)
        b = s - a
        wrong = near_numbers(self.rng, s, 5)
        if not wrong:
            return None
        return {"fact": f"The two numbers are {a} and {b}.", "answer": str(s), "wrong": wrong, "content": ("sum", a, b)}

    def rt_prod(self):
        prods = [(a, b) for a in range(2, 13) for b in range(a, 13)
                 if ((a * b < 40) if self.half == "A" else (a * b >= 40))]
        a, b = self.rng.choice(prods)
        ans = a * b
        allp = sorted({x * y for x in range(2, 13) for y in range(2, 13)})
        wrong = near_numbers(self.rng, ans, 12, pool=allp)
        if not wrong:
            return None
        return {"fact": f"The two numbers are {a} and {b}.", "answer": str(ans), "wrong": wrong, "content": ("prod", a, b)}

    def rt_cap(self):
        c = self.rng.choice(self.capital_answers)
        cw = content_words(c["country"])
        same = [x["capital"] for x in self.capitals_ok if x["region"] == c["region"] and x["capital"] != c["capital"]
                and not copies(x["capital"], cw)]
        if len(same) >= 4:
            self.stats["capital_wrong_source"]["same_region"] += 1
            wrong = self.rng.sample(same, 4)
        else:
            nb = self.L["regions"][c["region"]]
            more = [x["capital"] for x in self.capitals_ok if x["region"] == nb and not copies(x["capital"], cw)]
            pool = same + [x for x in more if x not in same]
            if len(pool) < 4:
                self.stats["capital_wrong_source"]["dropped"] += 1
                return None
            self.stats["capital_wrong_source"]["neighbour_region"] += 1
            wrong = same + self.rng.sample([x for x in more if x not in same], 4 - len(same))
        return {"fact": f"The country is {c['country']}.", "answer": c["capital"], "wrong": wrong,
                "content": ("cap", c["country"]), "region": c["region"]}

    def rt_opp(self):
        w, ans = self.rng.choice(self.opp_questions)
        cw = content_words(w)
        pool = [q[1] for q in self.opp_questions if q[1] not in (ans, w) and not copies(q[1], cw | {ans.lower()})]
        if len(pool) < 4:
            return None
        return {"fact": f"The word is {w}.", "answer": ans, "wrong": self.rng.sample(pool, 4), "content": ("opp", w)}

    def rt_col(self):
        o = self.rng.choice(self.objects)
        pool = [c for c in self.colours if c != o["typical"] and c not in o["also"]]
        if len(pool) < 4:
            return None
        return {"fact": f"The object is {o['object']}.", "answer": o["typical"], "wrong": self.rng.sample(pool, 4),
                "content": ("col", o["object"])}

    # ---------- a pair (sections 6 and 7)
    def pair(self, rk, qk, order_flag, allow_reuse=False, pair_id=None):
        r = self.rule(rk)
        if r is None:
            return None
        rt = self.routine(qk, allow_reuse=allow_reuse)
        if rt is None:
            return None
        pq, rq = QUESTIONS[(rk, qk)]
        parts = [r["rule"], rt["fact"], r["facts"]] if order_flag else [r["rule"], r["facts"], rt["fact"]]
        context = " ".join(parts)
        words = content_words(rt["fact"], pq, rq)
        # cross-cell rules and copying rule (section 7)
        p_wrong = [x for x in r["wrong"] if x != rt["answer"] and not copies(x, words)]
        r_wrong = [x for x in rt["wrong"] if x != r["answer"] and not copies(x, words)]
        if copies(rt["answer"], words) or (not r["answer"].isdigit() and copies(r["answer"], words)):
            self.drop("copying_rule_right_answer")
            return None
        if len(p_wrong) < 4 or len(r_wrong) < 4:
            self.drop("copying_or_cross_rule_left_too_few_wrong_answers")
            return None
        cands_p, cands_r = [r["answer"]] + p_wrong[:4], [rt["answer"]] + r_wrong[:4]
        for c in cands_p + cands_r:
            if not self.m.one_token(c):
                self.drop("candidate_not_one_token")
                return None
        self.rng.shuffle(cands_p)
        self.rng.shuffle(cands_r)
        P = {"text": context + " " + pq, "answer": r["answer"], "candidates": cands_p,
             "without_rule": " ".join([p for p in parts if p != r["rule"]]) + " " + pq,
             "baseline_variant": r["rule"] + " " + r["facts"] + " " + pq}
        R = {"text": context + " " + rq, "answer": rt["answer"], "candidates": cands_r,
             "baseline_variant": rt["fact"] + " " + rq}
        for x in (P, R):
            x["prompt_ids"] = self.m.ids(self.m.render(x["text"]))
        if len(P["prompt_ids"]) != len(R["prompt_ids"]):
            self.drop("twins_unequal_length")
            return None
        return {"id": pair_id, "rule_kind": rk, "routine_kind": qk, "order": "routine_fact_last" if not order_flag else "rule_facts_last",
                "context": context, "P": P, "R": R, "rule_content": repr(r["content"]), "routine_content": repr(rt["content"]),
                "region": rt.get("region"), "half": self.half}


def build_scored(b, allocation):
    pairs, pid = [], 0
    for (rk, qk), n in allocation.items():
        orders = [i % 2 == 1 for i in range(n - n % 2)]
        if n % 2:
            orders.append(b.rng.random() < 0.5)  # specification, section 14, item 4
        b.rng.shuffle(orders)
        made, tries = 0, 0
        while made < n and tries < 2000:
            tries += 1
            p = b.pair(rk, qk, orders[made], pair_id=f"{b.half}-{pid:04d}")
            if p is None or p["routine_content"] in b.used_routine or p["rule_content"] in b.used_rule:
                continue
            b.used_routine.add(p["routine_content"])
            b.used_rule.add(p["rule_content"])
            pairs.append(p)
            pid += 1
            made += 1
        if made < n:
            b.drop(f"group_{rk}_{qk}_short_by", n - made)
    return pairs


def eligible(donor, rec):
    """Section 8: length, answers, same group, and no copy of the recipient (RT-412)."""
    if (donor["rule_kind"], donor["routine_kind"]) != (rec["rule_kind"], rec["routine_kind"]):
        return False
    if donor.get("id") == rec.get("id"):
        return False
    if donor["rule_content"] == rec["rule_content"] or donor["routine_content"] == rec["routine_content"]:
        return False
    for t in ("P", "R"):
        if len(donor[t]["prompt_ids"]) < len(rec[t]["prompt_ids"]) + 1:
            return False
        if donor[t]["answer"] in rec[t]["candidates"]:
            return False
    return True


def build_donor_only(b, scored, budget_per_pair=200, cap_factor=3):
    """Section 8: aimed donor-only pairs, with the draw budget of RT-409."""
    donors, report = [], {}
    groups = {}
    for p in scored:
        groups.setdefault((p["rule_kind"], p["routine_kind"]), []).append(p)
    for (rk, qk), members in groups.items():
        pool = list(members)
        counts = {p["id"]: sum(eligible(d, p) for d in pool) for p in members}
        kept, draws, k = [], 0, 0
        budget = budget_per_pair * len(members)
        while draws < budget and len(kept) < cap_factor * len(members) and any(c < 5 for c in counts.values()):
            draws += 1
            d = b.pair(rk, qk, b.rng.random() < 0.5, allow_reuse=True, pair_id=f"{b.half}-donor-{rk}-{qk}-{k:04d}")
            if d is None:
                continue
            serves = [p for p in members if counts[p["id"]] < 5 and eligible(d, p)]
            if not serves:
                continue
            d["donor_only"] = True
            kept.append(d)
            pool.append(d)
            k += 1
            for p in members:
                if eligible(d, p):
                    counts[p["id"]] += 1
        donors.extend(kept)
        lengths = sorted(len(p["P"]["prompt_ids"]) for p in members)
        report[f"{rk}+{qk}"] = {
            "scored": len(members), "donor_only_kept": len(kept), "draws": draws,
            "stopped_by": "all_have_five" if all(c >= 5 for c in counts.values()) else
                          ("cap" if len(kept) >= cap_factor * len(members) else "draw_budget"),
            "no_donor": [{"id": p["id"], "text": p["P"]["text"],
                          "length_rank_from_longest": len(lengths) - sorted(lengths).index(len(p["P"]["prompt_ids"]))}
                         for p in members if counts[p["id"]] == 0],
            "eligible_donors": {p["id"]: counts[p["id"]] for p in members}}
    return donors, report


def chained_item(b, hops, cid):
    """Specification, section 14, item 1: five chains, each of "points to" rows ending in a colour row.
    The target chain has `hops` steps; each distractor chain has two to six steps, drawn independently."""
    lengths = [hops] + [b.rng.randint(2, 6) for _ in range(4)]
    need = sum(L + 1 for L in lengths)
    if need > len(b.inv_words):
        return None
    names = b.rng.sample(b.inv_words, need)
    cols = b.rng.sample(b.colours, 5)
    rows, starts, k = [], [], 0
    for L, col in zip(lengths, cols):
        chain = names[k:k + L + 1]
        k += L + 1
        starts.append(chain[0])
        rows += [f"{chain[j]} points to {chain[j + 1]}" for j in range(L)]
        rows.append(f"{chain[-1]} is {col}")
    b.rng.shuffle(rows)
    text = "In this list: " + "; ".join(rows) + f". Start at {starts[0]} and follow the list to a colour. What colour do you reach?"
    cands = cols[:]
    b.rng.shuffle(cands)
    return {"id": cid, "hops": hops, "text": text, "answer": cols[0], "candidates": cands,
            "content": repr((starts[0], tuple(sorted(rows)))), "prompt_ids": b.m.ids(b.m.render(text))}


def chained_eligible(d, rec):
    return (d["id"] != rec["id"] and d["hops"] == rec["hops"] and d["content"] != rec["content"]
            and len(d["prompt_ids"]) >= len(rec["prompt_ids"]) + 1 and d["answer"] not in rec["candidates"])


def build_chained(b, n=40, budget_per_item=200, cap_factor=3):
    """Specification, section 10 as amended in section 14: scored chained items, then aimed donor-only chained
    items on the rules of section 8."""
    items = []
    for i in range(n):
        it = None
        while it is None:
            it = chained_item(b, 2 + i % 5, f"{b.half}-chain-{i:03d}")
        items.append(it)
    donors, report = [], {}
    for hops in sorted({x["hops"] for x in items}):
        members = [x for x in items if x["hops"] == hops]
        pool = list(members)
        counts = {x["id"]: sum(chained_eligible(d, x) for d in pool) for x in members}
        kept, draws, k = [], 0, 0
        while draws < budget_per_item * len(members) and len(kept) < cap_factor * len(members) and any(c < 5 for c in counts.values()):
            draws += 1
            d = chained_item(b, hops, f"{b.half}-chain-donor-{hops}-{k:04d}")
            if d is None or not any(counts[x["id"]] < 5 and chained_eligible(d, x) for x in members):
                continue
            d["donor_only"] = True
            kept.append(d)
            pool.append(d)
            k += 1
            for x in members:
                if chained_eligible(d, x):
                    counts[x["id"]] += 1
        donors.extend(kept)
        report[f"hops_{hops}"] = {"scored": len(members), "donor_only_kept": len(kept), "draws": draws,
                                  "no_donor": [x["id"] for x in members if counts[x["id"]] == 0],
                                  "fewer_than_five": sum(c < 5 for c in counts.values()),
                                  "eligible_donors": counts}
    return items, donors, report


NEUTRAL_SENTENCES = [
    "The river runs past the old mill before it reaches the town.", "Most of the shops close early on a Sunday.",
    "The library keeps its oldest books in a cool room downstairs.", "A path leads from the station to the park.",
    "Rain is expected later in the week, mostly in the evening.", "The bakery opens before dawn on weekdays.",
    "Children walk to the school along the main road.", "The bridge was repainted two summers ago.",
    "A small market fills the square every Saturday morning.", "The museum has a room of maps and old clocks.",
    "Fishing boats leave the harbour when the tide is high.", "The garden behind the house is full of herbs.",
    "Buses run every twenty minutes during the day.", "The hill above the village gives a wide view of the valley.",
    "A new bench was placed beside the pond last spring.", "The hotel near the station has thirty rooms.",
    "Walkers often stop at the cafe halfway up the trail.", "The orchard is busiest when the apples are picked.",
    "An old wall marks the edge of the farm.", "The ferry crosses the bay twice each afternoon.",
    "The town hall clock was repaired in the autumn.", "Swallows nest under the roof of the barn each year.",
    "The lane narrows where it passes the church.", "Visitors can borrow bicycles at the information office.",
    "The lake freezes over in a very cold winter.", "A band plays in the park on summer evenings.",
    "The road to the coast winds through low hills.", "Most houses on the street have red front doors.",
    "The theatre puts on a play every month.", "A stream runs along the bottom of the field.",
    "The kitchen window looks out over the yard.", "The post office is next to the pharmacy.",
    "The old school is now used as a community hall.", "A narrow staircase leads to the attic.",
    "The forest trail is marked with small wooden posts.", "Trains to the city leave from the second platform.",
    "The cafe serves soup and bread at lunchtime.", "The tower can be climbed on most afternoons.",
    "The sheep are moved to higher fields in the summer.", "A row of trees shades the side of the road.",
]


def build_neutral(b, items, n=200):
    """Section 10: neutral prose, lengths spread from the shortest to the longest item, in the chat template."""
    sents = halves(NEUTRAL_SENTENCES)[b.half]
    lens = [len(p["P"]["prompt_ids"]) for p in items]
    lo, hi = min(lens), max(lens)
    prefix = len(b.m.ids(b.m.render("")))
    out = []
    for i in range(n):
        target = lo + (hi - lo) * i // max(1, n - 1)
        text = ""
        while True:
            nxt = (text + " " + b.rng.choice(sents)).strip()
            if len(b.m.ids(b.m.render(nxt))) > target and text:
                break
            text = nxt
            if len(b.m.ids(b.m.render(text))) >= target:
                break
        out.append({"id": f"{b.half}-neutral-{i:03d}", "text": text, "role": "build" if i % 2 == 0 else "measure",
                    "prompt_ids": b.m.ids(b.m.render(text))})
    return out, prefix


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--half", default="A")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tokdir", default=TOKDIR_DEFAULT)
    a = ap.parse_args()
    m = Model(a.tokdir)
    b = Builder(m, load_lists(), a.half, a.seed)
    scored = build_scored(b, PILOT_ALLOCATION)
    donors, report = build_donor_only(b, scored)
    chained, chained_donors, chained_report = build_chained(b)
    neutral, prefix = build_neutral(b, scored)
    os.makedirs(a.out, exist_ok=True)
    def dump(name, rows):
        with open(os.path.join(a.out, name), "w") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    dump("pairs.jsonl", scored)
    dump("donor_only.jsonl", donors)
    dump("chained.jsonl", chained)
    dump("chained_donor_only.jsonl", chained_donors)
    dump("neutral.jsonl", neutral)
    json.dump({"half": a.half, "seed": a.seed, "reply_opening": REPLY_OPENING, "stats": b.stats, "donors": report, "chained_donors": chained_report,
               "pools": {"capitals_one_token": len(b.capitals_ok), "capital_answers": len(b.capital_answers),
                         "opposite_questions": len(b.opp_questions), "objects": len(b.objects),
                         "words3": len(b.words3), "invented_words": len(b.inv_words), "colours": len(b.colours)}},
              open(os.path.join(a.out, "build-report.json"), "w"), indent=1, ensure_ascii=False)
    print(f"scored {len(scored)}, donor-only {len(donors)}, chained {len(chained)}, neutral {len(neutral)}")
    print(json.dumps(b.stats, indent=1))


if __name__ == "__main__":
    main()
