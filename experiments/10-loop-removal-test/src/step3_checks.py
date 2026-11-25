"""Sections 12 and 17 of battery-authoring-spec.md: the free step-3 checks, run on the pilot with the real tokeniser.

    .venv/bin/python -I experiments/10-loop-removal-test/src/step3_checks.py --pilot <dir> --tokdir <dir>

Writes step3-results.json into the pilot folder and prints a summary. The dose figures are the stand-in
measure only; they cannot forecast RT-345 (design, RT-391).
"""
import argparse
import json
import os
import random
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import (QUESTIONS, REPLY_OPENING, SYLL_A, SYLL_B, SYMBOLS, Model, eligible, halves,  # noqa: E402
                   load_lists)


def load(d, name):
    return [json.loads(l) for l in open(os.path.join(d, name))]


def full(m, item):
    return item["prompt_ids"] + m.ids(item["answer"])


def dose(rec, don, w):
    n = min(len(rec), len(don))
    i0 = next((i for i in range(n) if rec[i] != don[i]), n)
    s = 0.0
    for i in range(i0, len(rec)):
        s += 1.0 if (i >= len(don) or rec[i] != don[i]) else w
    return s, i0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--tokdir", required=True)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    m = Model(a.tokdir)
    L = load_lists()
    pairs, donors = load(a.pilot, "pairs.jsonl"), load(a.pilot, "donor_only.jsonl")
    bites, bites_donors = load(a.pilot, "bites.jsonl"), load(a.pilot, "bites_donor_only.jsonl")
    neutral = load(a.pilot, "neutral.jsonl")
    rep = json.load(open(os.path.join(a.pilot, "build-report.json")))
    R = {}

    # 1. single-token counts per list (both halves)
    caps = L["countries"]
    R["1_single_token"] = {
        "capitals_one_token": sum(m.one_token(c["capital"]) for c in caps), "capitals_total": len(caps),
        "capitals_one_token_no_name_overlap": sum(m.one_token(c["capital"]) and not c["name_overlap"] for c in caps),
        "opposite_answers_one_token": sum(m.one_token(w) for p in L["opposites"] for w in (p["a"], p["b"])),
        "opposite_words_total": 2 * len(L["opposites"]),
        "objects_typical_colour_one_token": sum(m.one_token(o["typical"]) for o in L["objects"]),
        "objects_total": len(L["objects"]),
        "words3_one_token": sum(m.one_token(w) for w in L["words3"]), "words3_total": len(L["words3"]),
        "colours_one_token": sum(m.one_token(c) for c in L["colours"]),
        "numbers_0_999_one_token": sum(m.one_token(str(i)) for i in range(1000)),
        "half_A_pools": rep["pools"]}

    # 2. fixed wording table recount (with a leading space, as joined after the context)
    n = lambda s: len(m.ids(" " + s))
    R["2_wording_table"] = {f"{k[0]}+{k[1]}": [n(p), n(q), n(p) == n(q)] for k, (p, q) in QUESTIONS.items()}
    R["2_wording_table_all_equal"] = all(v[2] for v in R["2_wording_table"].values())

    # 3. twin lengths
    R["3_twin_lengths_equal"] = sum(len(p["P"]["prompt_ids"]) == len(p["R"]["prompt_ids"]) for p in pairs)
    R["3_pairs"] = len(pairs)

    # 4. generation drops, answer spread, capitals by region
    spread = {}
    for p in pairs:
        spread.setdefault(p["routine_kind"], {}).setdefault(p["R"]["answer"], 0)
        spread[p["routine_kind"]][p["R"]["answer"]] += 1
    regions = {}
    for p in pairs:
        if p["routine_kind"] == "cap":
            regions[p["region"]] = regions.get(p["region"], 0) + 1
    R["4_generation"] = {"dropped": rep["stats"]["dropped"],
                         "capital_wrong_source_all_attempts": rep["stats"]["capital_wrong_source"],
                         "capital_right_answers_by_region": regions,
                         "distinct_right_answers_per_routine_kind": {k: len(v) for k, v in spread.items()},
                         "lookup_answer_colours": sorted({p["P"]["answer"] for p in pairs if p["rule_kind"] == "look"}),
                         "order_counts": {o: sum(p["order"] == o for p in pairs) for o in ("rule_facts_last", "routine_fact_last")}}

    # 5. donors
    allpool = pairs + donors
    elig = {p["id"]: [d for d in allpool if eligible(d, p)] for p in pairs}
    counts = [len(v) for v in elig.values()]
    R["5_donors"] = {"donor_only_added": len(donors), "per_group": {k: {kk: vv for kk, vv in v.items() if kk != "eligible_donors"}
                                                                    for k, v in rep["donors"].items()},
                     "scored_with_no_donor": sum(c == 0 for c in counts),
                     "scored_with_fewer_than_five": sum(c < 5 for c in counts),
                     "mean_eligible_donors": round(statistics.mean(counts), 2)}

    # 6-8. stand-in dose, tail shares, average-method counts
    rng = random.Random(a.seed)
    inv = {x + y for x in SYLL_A for y in SYLL_B}
    out6, out7, out8 = {}, {}, {}
    for rk in ("op", "unit", "look"):  # section 17, item 1
        acc = {w: {"P": [], "R": []} for w in (0.0, 0.3, 0.6)}
        tails = {"P": [], "R": []}
        inv_counts = {"P": [], "R": []}
        q_counts = {"P": [], "R": []}
        for p in [x for x in pairs if x["rule_kind"] == rk]:
            ds = elig[p["id"]]
            if not ds:
                continue
            chosen = rng.sample(ds, min(5, len(ds)))
            shared = next(i for i, (x, y) in enumerate(zip(p["P"]["prompt_ids"], p["R"]["prompt_ids"])) if x != y)
            for t in ("P", "R"):
                rec = full(m, p[t])
                for w in acc:
                    acc[w][t].append(statistics.mean(dose(rec, full(m, d[t]), w)[0] for d in chosen))
                spans = [len(rec) - dose(rec, full(m, d[t]), 1.0)[1] for d in chosen]
                tails[t].append((len(rec) - shared) / statistics.mean(spans))
                # a token is counted as part of an invented word or symbol if its text, decoded, holds a symbol,
                # holds a non-ASCII character, or is a piece of an invented word that is not an English word
                words = set(re.findall(r"[a-z]+", " ".join([p["context"].lower(), QUESTIONS[(p["rule_kind"], p["routine_kind"])][0].lower(),
                                                              QUESTIONS[(p["rule_kind"], p["routine_kind"])][1].lower()])))
                invented_here = {w for w in words if any(w.startswith(x) for x in SYLL_A) and any(w.endswith(y) or w.endswith(y + "s") for y in SYLL_B)}
                def is_inv(i):
                    s = m.tok.decode([i]).strip().lower()
                    if not s:
                        return False
                    if any(sy in s for sy in SYMBOLS) or not s.isascii():
                        return True
                    return any(s in w for w in invented_here) and s not in {"a", "s", "is", "the"}
                inv_counts[t].append(sum(1 for i in p[t]["prompt_ids"] if is_inv(i)))
                q_counts[t].append(len(p[t]["prompt_ids"]) - shared)
        out6[rk] = {str(w): round(statistics.mean(acc[w]["R"]) / statistics.mean(acc[w]["P"]), 4) for w in acc}
        out7[rk] = {"P": round(statistics.mean(tails["P"]), 3), "R": round(statistics.mean(tails["R"]), 3)}
        out8[rk] = {"max_abs_diff_invented_or_symbol_tokens": max(abs(x - y) for x, y in zip(inv_counts["P"], inv_counts["R"])),
                    "max_abs_diff_final_question_tokens": max(abs(x - y) for x, y in zip(q_counts["P"], q_counts["R"]))}
    R["6_dose_ratio_R_over_P"] = out6
    R["6_band_pass"] = all(0.95 <= v["0.3"] <= 1.05 and 0.90 <= v["0.0"] <= 1.10 and 0.90 <= v["0.6"] <= 1.10 for v in out6.values())
    R["7_tail_share"] = out7
    R["7_absorbable_difference_per_position"] = {k: round(0.10 / v["P"], 2) for k, v in out7.items()}
    R["8_average_method_counts"] = out8

    # 9. candidate words named in donors' contexts (RT-411)
    out9 = {}
    for p in pairs:
        key = f"{p['rule_kind']}+{p['routine_kind']}"
        for t in ("P", "R"):
            d = out9.setdefault(key, {}).setdefault(t, {"right": 0, "wrong": 0, "n_right": 0, "n_wrong": 0})
            ds = elig[p["id"]]
            for don in random.Random(p["id"]).sample(ds, min(5, len(ds))):  # drawn as at step 4b (RT-427)
                ctx = " " + don["context"].lower() + " "
                for c in p[t]["candidates"]:
                    hit = re.search(r"\b" + re.escape(c.lower()) + r"\b", ctx) is not None
                    if c == p[t]["answer"]:
                        d["n_right"] += 1
                        d["right"] += hit
                    else:
                        d["n_wrong"] += 1
                        d["wrong"] += hit
    R["9_candidates_named_in_donor_context"] = {
        k: {t: {"right_rate": round(v["right"] / max(1, v["n_right"]), 3), "wrong_rate": round(v["wrong"] / max(1, v["n_wrong"]), 3)}
            for t, v in d.items()} for k, d in out9.items()}

    # 10. the average is defined at every position (template slots and text)
    empty = m.ids(m.render("XYZZY"))
    marker = m.ids("XYZZY")
    k = next(i for i in range(len(empty)) if empty[i:i + len(marker)] == marker)
    prefix, suffix = empty[:k], empty[k + len(marker):]
    def slots_ok(ids):
        return ids[:len(prefix)] == prefix and ids[-len(suffix):] == suffix
    R["10_average_defined"] = {
        "template_prefix_tokens": len(prefix), "template_suffix_tokens_incl_reply_opening": len(suffix),
        "items_with_template_slots_matching_neutral": sum(slots_ok(p[t]["prompt_ids"]) for p in pairs for t in ("P", "R")),
        "items": 2 * len(pairs),
        "neutral_with_template_slots": sum(slots_ok(x["prompt_ids"]) for x in neutral), "neutral": len(neutral),
        "neutral_build": sum(x["role"] == "build" for x in neutral), "neutral_measure": sum(x["role"] == "measure" for x in neutral),
        "text_positions_pooled_from_build_passages": sum(len(x["prompt_ids"]) - len(prefix) - len(suffix) for x in neutral if x["role"] == "build"),
        "longest_item_prompt": max(len(p["P"]["prompt_ids"]) for p in pairs),
        "longest_neutral_prompt": max(len(x["prompt_ids"]) for x in neutral)}

    # RT-416: the right number's place among the five, in numeric order, by kind
    places = {}
    for p in pairs:
        for t, kind in (("P", p["rule_kind"]), ("R", p["routine_kind"])):
            if p[t]["answer"].isdigit():
                srt = sorted(int(c) for c in p[t]["candidates"])
                places.setdefault(kind, [0] * 5)[srt.index(int(p[t]["answer"]))] += 1
    R["11_right_number_place_counts"] = places

    # Section 17, item 5: the bites items
    from build import bites_eligible
    bpool = bites + bites_donors
    bcounts = {x["id"]: sum(bites_eligible(d, x) for d in bpool) for x in bites}
    R["bites"] = {"items": len(bites), "donor_only": len(bites_donors),
                  "by_group": {g: sum(f"{x['rule_kind']}+{x['routine_kind']}" == g for x in bites)
                               for g in sorted({f"{x['rule_kind']}+{x['routine_kind']}" for x in bites})},
                  "all_candidates_one_token": all(m.one_token(c) for x in bites for c in x["P"]["candidates"]),
                  "instruction_at_start": all(x["P"]["text"].startswith(rep.get("instruction_text", "")) for x in bites),
                  "repeats_a_scored_pair_or_donor": sum((x["rule_content"], x["routine_content"]) in
                                                        {(p["rule_content"], p["routine_content"]) for p in pairs + donors} for x in bites),
                  "with_no_donor": sum(c == 0 for c in bcounts.values()),
                  "with_fewer_than_five_donors": sum(c < 5 for c in bcounts.values()),
                  "prompt_length_range": [min(len(x["P"]["prompt_ids"]) for x in bites), max(len(x["P"]["prompt_ids"]) for x in bites)]}

    # Section 17, items 4 and 6: the split, on the pools and on the drawn items, and the facts
    import ast
    import split
    drawn = {k: [] for k in split.KINDS}
    for p in pairs + bites:
        if p["rule_kind"] in ("op", "unit"):
            c = ast.literal_eval(p["rule_content"])
            drawn[p["rule_kind"]].append((None, int(p["P"]["answer"]), (c[3], c[4]),
                                          tuple(sorted((c[3], c[4]))) if p["rule_kind"] == "unit" else None))
        if p.get("R") and p["routine_kind"] in ("sum", "prod"):
            c = ast.literal_eval(p["routine_content"])
            drawn[p["routine_kind"]].append((None, int(p["R"]["answer"]), (c[1], c[2]),
                                             (c[1], c[2]) if p["routine_kind"] == "prod" else None))
    out = {}
    for k, v in rep["split"].items():
        f = split.figures(drawn[k]) if drawn[k] else None
        uses = {}
        for it in drawn[k]:
            if it[3] is not None:
                uses[it[3]] = uses.get(it[3], 0) + 1
        out[k] = {"seed": v["seed"], "tolerances_met_on_pools": v["tolerances_met"],
                  "pool_A": v["half_A_pool"], "pool_B": v["half_B_pool"], "drawn_pilot_items": f,
                  "facts_used": len(uses), "most_uses_of_one_fact": max(uses.values()) if uses else None}
    R["split"] = out
    # Section 18, item 8: conditions that fail the script
    from build import RULE_KINDS, problem_key
    import split as _split
    shapes = dict(_split.OP_SHAPES)
    caps_by_country = {c["country"]: c["capital"] for c in L["countries"]}
    opp_of = {}
    for q in L["opposites"]:
        opp_of[q["a"]], opp_of[q["b"]] = q["b"], q["a"]
    col_of = {o["object"]: o["typical"] for o in L["objects"]}

    def right(content):
        c = ast.literal_eval(content)
        k = c[0]
        if k == "op":
            return str(shapes[c[2]](c[3], c[4]))
        if k == "unit":
            return str(c[3] * c[4])
        if k == "look":
            return c[2][c[3]]
        if k == "sum":
            return str(c[1] + c[2])
        if k == "prod":
            return str(c[1] * c[2])
        if k == "cap":
            return caps_by_country[c[1]]
        if k == "opp":
            return opp_of[c[1]]
        if k == "col":
            return col_of[c[1]]
        raise ValueError(k)

    instr = rep.get("instruction_text")
    failures = []
    every = [("pairs", x) for x in pairs] + [("donor_only", x) for x in donors] + [("bites", x) for x in bites] + \
            [("bites_donor_only", x) for x in bites_donors]
    if not instr:
        failures.append("the build report names no instruction")
    for f, x in every:
        if x["rule_kind"] not in RULE_KINDS:
            failures.append(f"{f} {x['id']}: rule kind {x['rule_kind']} not built")
        for side in ("P", "R"):
            if side not in x:
                continue
            if instr and not x[side]["text"].startswith(instr + " "):
                failures.append(f"{f} {x['id']} {side}: does not start with the instruction")
            if not all(m.one_token(c) for c in x[side]["candidates"]):
                failures.append(f"{f} {x['id']} {side}: a candidate is not one token")
            content = x["rule_content"] if side == "P" else x["routine_content"]
            if right(content) != x[side]["answer"]:
                failures.append(f"{f} {x['id']} {side}: stated answer {x[side]['answer']} differs from {right(content)}")
            if x[side]["answer"] not in x[side]["candidates"]:
                failures.append(f"{f} {x['id']} {side}: answer not among the candidates")
        if "R" in x and len(x["P"]["prompt_ids"]) != len(x["R"]["prompt_ids"]):
            failures.append(f"{f} {x['id']}: twins of unequal length")
    if instr:
        for x in neutral:
            if instr in x["text"]:
                failures.append(f"neutral {x['id']}: carries the instruction")
    keys = [problem_key(x["rule_content"]) for x in bites]
    if len(keys) != len(set(keys)):
        failures.append("two bites items share a problem")
    if R["bites"]["repeats_a_scored_pair_or_donor"]:
        failures.append("a bites item repeats a scored pair's or donor's whole content")
    skeys = [problem_key(x["rule_content"]) for x in pairs]
    if len(skeys) != len(set(skeys)):
        failures.append("two scored pairs share a rule problem")
    # reports (section 18, item 8)
    bplaces = {}
    for x in bites:
        if x["P"]["answer"].isdigit():
            srt = sorted(int(c) for c in x["P"]["candidates"])
            bplaces.setdefault(x["rule_kind"], [0] * 5)[srt.index(int(x["P"]["answer"]))] += 1
    R["11b_right_number_place_counts_bites"] = bplaces
    fact_uses = {}
    for x in pairs + bites:
        if x["rule_kind"] == "unit":
            c = ast.literal_eval(x["rule_content"])
            key = str(tuple(sorted((c[3], c[4]))))
            fact_uses[key] = fact_uses.get(key, 0) + 1
    R["unit_fact_uses"] = dict(sorted(fact_uses.items(), key=lambda kv: -kv[1]))
    R["neutral_longest_vs_longest_item"] = [max(len(x["prompt_ids"]) for x in neutral),
                                           max(len(x[s]["prompt_ids"]) for _, x in every for s in ("P", "R") if s in x)]
    if R["neutral_longest_vs_longest_item"][0] < R["neutral_longest_vs_longest_item"][1]:
        failures.append("the longest neutral passage is shorter than the longest item")
    # Section 19, item 11: the reply rendering, the operator's practised sum and donors
    from build import REPLY_REQUEST, REPLY_CLOSING
    op_open = m.ids(m.render(REPLY_REQUEST))
    op_close = m.ids(REPLY_CLOSING)
    bad = []
    for x in neutral:
        s, e = x["prose_span"]
        if x["reply_ids"][:s] != op_open or x["reply_ids"][e:] != op_close or x["reply_ids"][s:e] != x["plain_ids"] \
                or x["plain_ids"] != m.ids(x["text"]):
            bad.append(x["id"])
    if bad:
        failures.append(f"reply rendering wrong for {len(bad)} neutral passages: {bad[:3]}")
    R["reply_rendering"] = {"opening_tokens": len(op_open), "closing_tokens": len(op_close), "passages_checked": len(neutral),
                            "string_tokenises_the_same": sum(x["reply_string_tokenises_the_same"] for x in neutral)}
    psum = 0
    opi = [x for x in pairs + bites if x["rule_kind"] == "op"]
    for x in opi:
        c = ast.literal_eval(x["rule_content"])
        psum += str(c[3] + c[4]) in x["P"]["candidates"]
    R["operator_practised_sum_among_candidates"] = {"items": len(opi), "with_sum": psum}
    R["operator_donors"] = {k: {kk: vv for kk, vv in v.items() if kk != "eligible_donors"} for k, v in rep["donors"].items() if k.startswith("op+")}
    R["failures"] = failures
    json.dump(R, open(os.path.join(a.pilot, "step3-results.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps({k: R[k] for k in ("2_wording_table_all_equal", "3_twin_lengths_equal", "5_donors", "6_dose_ratio_R_over_P",
                                        "6_band_pass", "7_tail_share", "8_average_method_counts", "10_average_defined", "bites", "failures")}, indent=1))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
