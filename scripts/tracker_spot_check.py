#!/usr/bin/env python3
"""John's spot-check of agreed judgements (ruling 7, as ruled 2026-11-20: "Yes, that sample").

THE RULE (the master session's wording): every judgement both readers agreed on that sits
on a Sentient Horizons row, plus half of the other agreed judgements (rounded up), drawn
at random. Reason for half: if one agreed judgement in ten were wrong, reading half gives
about an 80% chance of seeing at least one. Weakest step: John's time.

THE METHOD, fixed and committed before the draw:
- "Agreed" means: both readers (claude and gemini) gave the same answer (the verdict, or
  for testability the pair could-fail and separates), and no ruling changed that answer.
  Judgements whose agreed answer a ruling of John's overturned (they are already his) and
  superseded judgements are left out. A ruling that confirmed the agreed answer does not
  remove a judgement.
- Eligible judgements are split into Sentient Horizons rows (all taken) and the rest.
- The rest are sorted by id (plain string order); n = ceil(len / 2) of them are drawn with
  Python's random.Random(SEED).sample(sorted_ids, n), Python 3.14's Mersenne Twister.
- SEED = 20261120.

Usage:
    python3 scripts/tracker_spot_check.py --eligible   # list what is eligible (no draw)
    python3 scripts/tracker_spot_check.py --draw       # draw, write data/tracker/spot-check-draw.toml
    python3 scripts/tracker_spot_check.py --pages      # write the reading pages from the draw
John's findings go in data/tracker/spot-check.toml (see that file); an "overturn" there is
applied by tracker_scores.py as his ruling.
"""
from __future__ import annotations

import argparse
import math
import random
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tracker_scores as ts  # noqa: E402

SEED = 20261120
DATA = ts.DATA
ROOT = ts.ROOT


def load():
    d = ts.load()
    d["predictions_by_id"] = {p["id"]: p for p in d["predictions"]}
    return d


def key(j, r):
    return (r["could_fail"], r["separates"]) if j["kind"] == "testability" else r["verdict"]


def eligible(d):
    sh, rest = [], []
    for j in d["judgements"]:
        rs = j.get("reading", [])
        if {r["reader"] for r in rs} != {"claude", "gemini"}:
            continue
        ks = {key(j, r) for r in rs}
        if len(ks) != 1:
            continue
        agreed = next(iter(ks))
        ru = j.get("ruling")
        if ru:
            if ru.get("verdict") == "superseded":
                continue
            res = (ru.get("could_fail", agreed[0]), ru["separates"]) if j["kind"] == "testability" else ru["verdict"]
            if res != agreed:
                continue
        (sh if d["predictions_by_id"][j["prediction"]]["theory"] == "sh" else rest).append(j["id"])
    return sorted(sh), sorted(rest)


def draw(d):
    sh, rest = eligible(d)
    n = math.ceil(len(rest) / 2)
    picked = random.Random(SEED).sample(rest, n)
    return sh, rest, picked


def short(text, words=40):
    w = text.split()
    return text if len(w) <= words else " ".join(w[:words]) + " ..."


def first_sentence(s):
    s = s.strip()
    for end in (". ", "; "):
        i = s.find(end)
        if 0 < i < 300:
            return s[: i + 1]
    return short(s, 45)


QUESTION = {
    "outcome": "Did this study's result come out for the prediction, against it, or mixed?",
    "commitment": "Had the theory's own proponents fixed this prediction, in a dated record, before they could have known this study's result?",
    "testability": "Could this prediction fail (is there a result a study could observe that would count against it)? And does a rival theory's own published work predict something different?",
}


def answer(j, r):
    if j["kind"] == "testability":
        s = f"could fail: {'yes' if r['could_fail'] else 'no'}; separates from a rival: {'yes' if r['separates'] else 'no'}"
        if r.get("separates_from"):
            s += f" ({', '.join(r['separates_from'])})"
        return s
    return r["verdict"]


def pages(d, order):
    preds = d["predictions_by_id"]
    studies = {s["id"]: s for s in d["studies"]}
    sources = {s["id"]: s for s in d["sources"]}
    names = dict(zip(d["theories"]["listed_theory"][0]["ids"], d["theories"]["listed_theory"][0]["names"]))
    js = {j["id"]: j for j in d["judgements"]}
    out = [
        "# John's spot-check: the drawn judgements",
        "",
        "*Drawn 2026-11-20 under ruling 7 as John ruled it (\"Yes, that sample\"): every agreed judgement on a",
        "Sentient Horizons row, plus half of the other agreed judgements, drawn at random (seed 20261120;",
        "method in `scripts/tracker_spot_check.py`, draw in `data/tracker/spot-check-draw.toml`). Each page shows",
        "one judgement that both readers, a Claude model and Google's Gemini, answered the same way. Your",
        "finding goes on the last line: agree, or overturn with a reason. An overturned judgement is recorded",
        "in `data/tracker/spot-check.toml` as your ruling, and the scores move.*",
        "",
        "Rival theories are named by short codes: " + "; ".join(f"{k} = {v}" for k, v in names.items()) + ".",
        "",
    ]
    for n, jid in enumerate(order, 1):
        j = js[jid]
        p = preds[j["prediction"]]
        th = {"gwt": "Global workspace theory", "iit": "Integrated information theory", "sh": "The Sentient Horizons account"}[p["theory"]]
        out += [f"## {n}. {th}: {p['statement'][:90].rstrip(',. ')}{'...' if len(p['statement']) > 90 else ''}", ""]
        out += [f"`{jid}` ({j['kind']} judgement)" + (" — a Sentient Horizons row, taken by the rule" if p["theory"] == "sh" else " — drawn at random"), ""]
        out += [f"**The prediction.** {p['statement']}", ""]
        out += [f"- Counts for it: {p['test_for']}", f"- Counts against it: {p['test_against']}", ""]
        if j["kind"] in ("outcome", "commitment"):
            s = studies[j["study"]]
            out += [f"**The study.** {s['name']} (first appeared {s['first_appeared']['date']}).", ""]
            pas = j.get("passages", [])
            if pas:
                a = pas[0] if j["kind"] == "outcome" else pas[0]
                src = sources[a["source"]]
                out += [f"**The passage it rests on.** \"{short(a['text'])}\" ([{a['source']}]({src.get('url', '')}))", ""]
        else:
            fs = p["first_stated"]
            src = sources[fs["source"]]
            out += [f"**The passage it rests on.** \"{short(fs['passage'])}\" ([{fs['source']}]({src.get('url', '')}), {fs['date']})", ""]
            ru = j.get("ruling")
            if ru and ru.get("source"):
                rs = sources[ru["source"]]
                out += [f"**The rival's own passage (rule C).** \"{short(ru['passage'])}\" ([{ru['source']}]({rs.get('url', '')}))", ""]
        out += [f"**The question.** {QUESTION[j['kind']]}", ""]
        for r in j["reading"]:
            who = "Claude" if r["reader"] == "claude" else "Gemini"
            out += [f"- **{who}** ({r['model']}): {answer(j, r)}. {first_sentence(r['reason'])}"]
        if j.get("ruling"):
            out += [f"- *A ruling of yours confirmed this answer ({j['ruling']['rule']}).*"]
        out += ["", "**Your finding** (agree / overturn, and why): ________________________________", ""]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--eligible", action="store_true")
    ap.add_argument("--draw", action="store_true")
    ap.add_argument("--pages", action="store_true")
    a = ap.parse_args(argv)
    d = load()
    if a.eligible:
        sh, rest = eligible(d)
        print(f"Sentient Horizons rows ({len(sh)}): {sh}")
        print(f"others ({len(rest)}); to draw: {math.ceil(len(rest) / 2)}")
        return 0
    if a.draw:
        sh, rest, picked = draw(d)
        lines = ["# The spot-check draw, made by scripts/tracker_spot_check.py --draw on 2026-11-20,",
                 f"# seed {SEED}, after the method and seed were committed. Do not edit.", "",
                 f"seed = {SEED}", f"eligible_other = {len(rest)}", f"drawn = {len(picked)}",
                 "sentient_horizons = [" + ", ".join(f'"{x}"' for x in sh) + "]",
                 "random = [" + ", ".join(f'"{x}"' for x in picked) + "]", ""]
        (DATA / "spot-check-draw.toml").write_text("\n".join(lines))
        print(f"{len(sh)} Sentient Horizons rows + {len(picked)} drawn of {len(rest)}")
        return 0
    if a.pages:
        dr = tomllib.load(open(DATA / "spot-check-draw.toml", "rb"))
        order = dr["sentient_horizons"] + dr["random"]
        (ROOT / "docs" / "2026-11-20-spot-check-sample.md").write_text(pages(d, order) + "\n")
        print(f"{len(order)} pages written")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
