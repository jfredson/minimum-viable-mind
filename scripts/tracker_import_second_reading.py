#!/usr/bin/env python3
"""Turn the second reader's raw answers into reading records, and count agreement.

Reads data/tracker/second-reading/*.json (written by tracker_second_reader.py) and
writes data/tracker/readings-gemini.toml: one [[reading]] per judgement, with the
exact model version the API returned. On the five Sentient Horizons rows the Gemini
reading is the first of record (ruling 7b); elsewhere it is the second.
tracker_scores.py merges these readings into the judgements.

Then prints, and writes to data/tracker/agreement.json, the agreement between the two
readers by kind of judgement, and lists every disagreement with both readings. It
settles nothing: disagreements go to John.
"""
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tracker"
RAW = DATA / "second-reading"


def q(s):
    return json.dumps(s, ensure_ascii=False)


def main():
    judgements = tomllib.load(open(DATA / "judgements.toml", "rb"))["judgement"]
    preds = {p["id"]: p for p in tomllib.load(open(DATA / "predictions.toml", "rb"))["prediction"]}
    lines = [
        "# The second reader's readings (Google's Gemini), one per judgement, imported from the",
        "# raw answers in second-reading/ by scripts/tracker_import_second_reading.py. Do not edit",
        "# by hand. Run 2026-11-20 under John's go of that day ('Yes, up to $10', relayed by the",
        "# master session). Blind: each packet held no part of the first reader's readings.",
        "",
    ]
    problems = []
    gem = {}
    for j in judgements:
        f = RAW / f"{j['id']}.json"
        if not f.exists():
            problems.append(f"{j['id']}: no answer yet")
            continue
        raw = json.loads(f.read_text())
        try:
            ans = json.loads(raw["answer_text"])
        except Exception:
            problems.append(f"{j['id']}: answer is not JSON")
            continue
        sh = preds[j["prediction"]]["theory"] == "sh"
        r = {"judgement": j["id"], "reader": "gemini", "model": raw["model_version"] or raw["model_requested"],
             "date": raw["called_on"][:10], "order": "first" if sh else "second",
             "reason": ans.get("reason", ""), "unsure": bool(ans.get("unsure", False)),
             "unsure_why": ans.get("unsure_why", "") or "", "response_id": raw.get("response_id") or "",
             "cost_usd": raw["cost_usd"]}
        if j["kind"] == "testability":
            r["could_fail"] = bool(ans.get("could_fail"))
            r["separates"] = bool(ans.get("separates"))
            r["separates_from"] = [str(x) for x in ans.get("separates_from", []) or []]
            r["rival_view_from"] = ans.get("rival_view_from", "") or ""
        else:
            r["verdict"] = str(ans.get("verdict", "")).lower()
        gem[j["id"]] = r
        lines.append("[[reading]]")
        for k, v in r.items():
            if isinstance(v, bool):
                lines.append(f"{k} = {'true' if v else 'false'}")
            elif isinstance(v, (int, float)):
                lines.append(f"{k} = {v}")
            elif isinstance(v, list):
                lines.append(f"{k} = [{', '.join(q(x) for x in v)}]")
            else:
                lines.append(f"{k} = {q(v)}")
        lines.append("")
    (DATA / "readings-gemini.toml").write_text("\n".join(lines))

    # agreement
    out = {"by_kind": {}, "disagreements": [], "problems": problems}
    for kind in ("outcome", "commitment", "testability"):
        js = [j for j in judgements if j["kind"] == kind and j["id"] in gem]
        agree = 0
        part = {"could_fail": 0, "separates": 0}
        for j in js:
            c = j["reading"][0]
            g = gem[j["id"]]
            if kind == "testability":
                same = (c["could_fail"], c["separates"]) == (g["could_fail"], g["separates"])
                part["could_fail"] += c["could_fail"] == g["could_fail"]
                part["separates"] += c["separates"] == g["separates"]
                cv = f"could fail {c['could_fail']}, separates {c['separates']} {c.get('separates_from', [])}"
                gv = f"could fail {g['could_fail']}, separates {g['separates']} {g.get('separates_from', [])}"
            else:
                same = c["verdict"] == g["verdict"]
                cv, gv = c["verdict"], g["verdict"]
            agree += same
            if not same:
                out["disagreements"].append({"judgement": j["id"], "kind": kind, "prediction": j["prediction"],
                                             "study": j.get("study", ""), "claude": cv, "claude_reason": c["reason"],
                                             "gemini": gv, "gemini_reason": g["reason"],
                                             "first_of_record": "gemini" if g["order"] == "first" else "claude"})
        n = len(js)
        d = {"read_by_both": n, "agree": agree, "disagree": n - agree,
             "disagreement_rate": round((n - agree) / n, 3) if n else None}
        if kind == "testability":
            d["agree_on_could_fail"] = part["could_fail"]
            d["agree_on_separates"] = part["separates"]
        out["by_kind"][kind] = d
    o = out["by_kind"].get("outcome", {})
    out["stop_condition"] = {"rule": "stage 2 stops if the readers disagree on more than a third of the outcome judgements",
                             "outcome_rate": o.get("disagreement_rate"),
                             "stops": bool(o.get("disagreement_rate") is not None and o["disagreement_rate"] > 1 / 3)}
    out["models"] = sorted({r["model"] for r in gem.values()})
    out["cost_usd"] = round(sum(r["cost_usd"] for r in gem.values()), 4)
    (DATA / "agreement.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("by_kind", "stop_condition", "models", "cost_usd", "problems")}, indent=2))
    for d in out["disagreements"]:
        print(f"\n{d['judgement']} ({d['kind']}): claude {d['claude']} | gemini {d['gemini']}")
        print(f"  gemini: {d['gemini_reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
