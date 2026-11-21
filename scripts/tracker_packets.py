#!/usr/bin/env python3
"""Build the blind packets for the second reader, and estimate what reading them costs.

One packet per judgement in data/tracker/judgements.toml, written to
data/tracker/packets/<judgement-id>.json. A packet holds what a reader needs and
nothing a reader has already concluded: the prediction, its test wording for and
against, who stated it and when, the study and its dated first appearance, and the
passages. It never holds a reading, a verdict, a reason, or the records' free notes
(which sometimes say what the first reader thought). Ruling 7b: "it gets the
prediction, the study and the wording of what counts for and against, never the
first reader's answer".

This script makes no API call. It writes the packets and prints a call count and a
cost estimate; calling the second reader is a separate step, behind John's go.

Usage:
    python3 scripts/tracker_packets.py                 # write packets, print estimate
    python3 scripts/tracker_packets.py --check-blind   # fail if any packet leaks a reading
"""
from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tracker"
OUT = DATA / "packets"

INSTRUCTIONS = {
    "outcome": (
        "You are one of two independent readers for a public record that scores theories of "
        "consciousness. Read the prediction, the wording of what would count for and against it, "
        "and the passages from the study. Decide whether this study's result is FOR the prediction, "
        "AGAINST it, or MIXED (parts for and parts against, or a result that cannot tell the two "
        "apart). Judge only from the material given; if you rely on anything else, say what. "
        "Answer in JSON: {\"verdict\": \"for\"|\"against\"|\"mixed\", \"reason\": \"two to four plain "
        "sentences\", \"unsure\": true|false, \"unsure_why\": \"what would change your answer, or empty\"}."
    ),
    "commitment": (
        "You are one of two independent readers for a public record that scores theories of "
        "consciousness. A study counts toward a prediction if that prediction was fixed, by the "
        "theory's proponents, in a dated record made before the study's data were collected, whether a "
        "publication or a registration. What decides is when the record was fixed, not when it became "
        "public. A paper that states a prediction and tests it in the same paper does not count. When "
        "the dates or the commitment are unclear, the study is not counted. Read the passages and the "
        "dates. Decide: BEFORE (a record by the proponents commits the theory to this prediction and was "
        "fixed before the study's data were collected), NOT-BEFORE (it was not), or UNCLEAR. If the study "
        "does not say when its data were collected, say how you decided. "
        "Answer in JSON: {\"verdict\": \"before\"|\"not-before\"|\"unclear\", \"reason\": \"two to four "
        "plain sentences\", \"unsure\": true|false, \"unsure_why\": \"...\"}."
    ),
    "testability": (
        "You are one of two independent readers for a public record that scores theories of "
        "consciousness. For the prediction below, answer two questions. (a) COULD IT FAIL: is there a "
        "result, stated or plainly implied in the wording, that would count against it, and that a "
        "study could actually observe? (b) DOES IT SEPARATE the theory from a rival: does at least one "
        "theory on the list of rivals predict something different (not merely stay silent)? If yes, "
        "name the rival or rivals, and say whether your view of the rival comes from the material given "
        "or from your own knowledge. Answer in JSON: {\"could_fail\": true|false, \"separates\": "
        "true|false, \"separates_from\": [ids], \"rival_view_from\": \"material\"|\"own knowledge\"|\"both\"|\"none\", "
        "\"reason\": \"two to four plain sentences\", \"unsure\": true|false, \"unsure_why\": \"...\"}."
    ),
}

FORBIDDEN_KEYS = {"reading", "verdict", "reason", "unsure", "unsure_why", "could_fail", "separates", "note", "judgement"}


def load(name):
    with open(DATA / name, "rb") as f:
        return tomllib.load(f)


def build():
    th = load("theories.toml")
    preds = {p["id"]: p for p in load("predictions.toml")["prediction"]}
    studies = {s["id"]: s for s in load("studies.toml")["study"]}
    sources = {s["id"]: s for s in load("sources.toml")["source"]}
    judgements = load("judgements.toml")["judgement"]
    theory_names = {t["id"]: t["name"] for t in th["theory"]}
    listed = th["listed_theory"][0]
    rivals = dict(zip(listed["ids"], listed["names"]))
    claims = {c["id"]: c for c in th["claim"]}

    def cite(sid):
        s = sources[sid]
        return {"citation": s["citation"], "url": s.get("url", ""), "date": s.get("published", "")}

    packets = []
    for j in judgements:
        p = preds[j["prediction"]]
        c = claims[p["core_claim"]]
        first_reading = "gemini" if p["theory"] == "sh" else "claude"
        packet = {
            "packet_id": j["id"],
            "kind": j["kind"],
            "instructions": INSTRUCTIONS[j["kind"]],
            "theory": theory_names[p["theory"]],
            "core_claim": {"quote": c["quote"], "source": cite(c["source"])},
            "prediction": {
                "statement": p["statement"],
                "stated_by": "the theory's proponents" if p["stated_by"] == "proponent" else "the site, inferred",
                "first_stated": {"date": p["first_stated"]["date"], "passage": p["first_stated"]["passage"], "source": cite(p["first_stated"]["source"])},
                "test_for": p["test_for"],
                "test_against": p["test_against"],
            },
        }
        if j["kind"] == "testability":
            packet["rivals_on_the_list"] = rivals
            packet["what_the_sources_say_about_rivals"] = [
                {"rival": rivals[s["theory"]], "statement": s["how"], "source": cite(s["source"])}
                for s in p.get("separates_from", [])
            ]
            packet["other_statements_of_the_prediction"] = [
                {"passage": a["passage"], "source": cite(a["source"])} for a in p.get("also_stated", [])
            ]
        else:
            s = studies[j["study"]]
            packet["study"] = {
                "name": s["name"],
                "source": cite(s["source"]),
                "first_appeared": s["first_appeared"]["date"] + " (" + s["first_appeared"]["what"] + ")",
            }
            if "data_collected" in s:
                dc = s["data_collected"]
                packet["study"]["data_collected"] = {"when": dc["when"], "basis": dc["reason"]}
            packet["passages"] = [{"text": a["text"], "source": cite(a["source"])} for a in j.get("passages", [])]
            if j["kind"] == "commitment":
                packet["dates"] = j.get("dates", {})
        packet["this_reading_is"] = "the first reading of record" if first_reading == "gemini" else "the second reading"
        packets.append(packet)
    return packets


def leaks(packet, judgements_by_id):
    """True if any reading's text appears in the packet, or a forbidden key is present."""
    def keys(o):
        if isinstance(o, dict):
            for k, v in o.items():
                yield k
                yield from keys(v)
        elif isinstance(o, list):
            for v in o:
                yield from keys(v)
    found = [k for k in keys(packet) if k in FORBIDDEN_KEYS]
    text = json.dumps(packet, ensure_ascii=False)
    j = judgements_by_id[packet["packet_id"]]
    for r in j.get("reading", []):
        for field in ("reason", "unsure_why"):
            v = r.get(field, "")
            if v and v[:60] in text:
                found.append(f"reading text from {field}")
    return found


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-blind", action="store_true")
    ap.add_argument("--output-tokens", type=int, default=3000,
                    help="assumed output tokens per call, thinking included (default 3000)")
    a = ap.parse_args(argv)
    packets = build()
    jby = {j["id"]: j for j in load("judgements.toml")["judgement"]}
    bad = {p["packet_id"]: leaks(p, jby) for p in packets}
    bad = {k: v for k, v in bad.items() if v}
    if bad:
        print("Packets would leak a reading:", json.dumps(bad, indent=2), file=sys.stderr)
        return 1
    if a.check_blind:
        print(f"{len(packets)} packets, none leaks a reading")
        return 0
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()
    for p in packets:
        (OUT / f"{p['packet_id']}.json").write_text(json.dumps(p, indent=2, ensure_ascii=False) + "\n")

    # estimate: about 4 characters per token for English prose
    chars = [len(json.dumps(p, ensure_ascii=False)) for p in packets]
    in_tokens = sum(chars) / 4
    out_tokens = a.output_tokens * len(packets)
    by_kind = {}
    for p in packets:
        by_kind[p["kind"]] = by_kind.get(p["kind"], 0) + 1
    sh = sum(1 for p in packets if p["this_reading_is"] == "the first reading of record")
    # prices: Google, Gemini Developer API pricing, read 2026-11-20 (sources.toml: gemini-pricing)
    # Gemini 4 Carbon, standard tier, per 1M tokens: $2 in / $10 out through 2026-11-30,
    # $4 / $20 from 2026-12-01. Not available on the free tier. Batch is 50% off.
    periods = {"through 2026-11-30": (2.0, 10.0), "from 2026-12-01": (4.0, 20.0)}
    print(f"{len(packets)} packets written to {OUT.relative_to(ROOT)} ({by_kind}); {sh} are Sentient Horizons rows, read first by the second reader")
    print(f"input about {in_tokens:,.0f} tokens in all (largest packet {max(chars)/4:,.0f}); output assumed {a.output_tokens:,} per call, thinking included")
    oc = [c for p, c in zip(packets, chars) if p["kind"] != "testability"]
    oc_in, oc_out = sum(oc) / 4, a.output_tokens * len(oc)
    for name, (pi, po) in periods.items():
        cost = in_tokens / 1e6 * pi + out_tokens / 1e6 * po
        cost2 = oc_in / 1e6 * pi + oc_out / 1e6 * po
        print(f"  Gemini 4 Carbon, standard, {name}: all {len(packets)}: ${cost:.2f} (batch ${cost/2:.2f}); outcomes and commitments only ({len(oc)}): ${cost2:.2f} (batch ${cost2/2:.2f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
