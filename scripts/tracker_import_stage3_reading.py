#!/usr/bin/env python3
"""Stage 3: turn the second reader's raw answers from the stage 3 run into readings, and count
agreement. Settles nothing.

Reads data/tracker/second-reading/*.json whose "run" is "stage3" (written by
tracker_second_reader.py under John's go of 2026-11-21, "Yes, cap $15") and writes
data/tracker/readings-gemini-stage3.toml: one [[reading]] per judgement, with the exact model
version the API returned. A packet named <id>.c2 is a pilot testability row read again under
rule C as amended ("Yes, flip it"; reading confirmed "Yes, that reading"); its reading replaces
the pilot's Gemini reading of that row in the scores (tracker_scores.py does that), and the
earlier reading stays in readings-gemini.toml for the record. On Sentient Horizons rows the
Gemini reading is the first of record (ruling 7b).

Agreement (data/tracker/agreement-stage3.json) compares Gemini's reading with the first reader's
reading as the records hold it before this run:
  - outcome and dating: Claude's verdict;
  - testability: Claude's "could it fail", and "does it separate" as the records settle it under
    the amended rule C (Claude's reading with any rule C / C2 entry applied, and John's own
    could-fail ruling where there is one). Claude's stage 3 readings were made under the earlier
    question, so this is the fair comparison; the raw comparison is reported beside it.
Every disagreement is listed with both readings. None is settled here, not even by rule E
("mixed" against one side is "mixed") or the dating rule on split readers: those are applied
only when John or the master says so. Each disagreement says which ruled rule would settle it.
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
    judgements = {j["id"]: j for j in tomllib.load(open(DATA / "judgements.toml", "rb"))["judgement"]}
    preds = {p["id"]: p for p in tomllib.load(open(DATA / "predictions.toml", "rb"))["prediction"]}
    rulings = {}
    for r in tomllib.load(open(DATA / "rulings.toml", "rb")).get("ruling", []):
        rulings[r["judgement"]] = r  # last entry wins, as in tracker_scores.py
    lines = [
        "# The second reader's stage 3 readings (Google's Gemini), imported from the raw answers in",
        "# second-reading/ (run = stage3) by scripts/tracker_import_stage3_reading.py. Do not edit by",
        "# hand. Run 2026-11-21 under John's go of that day ('Yes, cap $15', relayed by the master",
        "# session). Blind: no packet held any part of the first reader's readings.",
        "",
    ]
    gem, problems = {}, []
    for f in sorted(RAW.glob("*.json")):
        raw = json.loads(f.read_text())
        if raw.get("run") != "stage3":
            continue
        pid = raw["packet_id"]
        resend = pid.endswith(".c2")
        jid = pid[:-3] if resend else pid
        j = judgements[jid]
        try:
            ans = json.loads(raw["answer_text"])
        except Exception:
            problems.append(f"{pid}: answer is not JSON")
            continue
        sh = preds[j["prediction"]]["theory"] == "sh"
        r = {"judgement": jid, "reader": "gemini", "model": raw["model_version"] or raw["model_requested"],
             "date": raw["called_on"][:10], "order": "first" if sh else "second",
             "reason": ans.get("reason", ""), "unsure": bool(ans.get("unsure", False)),
             "unsure_why": ans.get("unsure_why", "") or "", "response_id": raw.get("response_id") or "",
             "cost_usd": raw["cost_usd"], "run": "stage3"}
        if j["kind"] == "testability":
            r["question"] = "C2"
            cf = ans.get("could_fail")
            r["could_fail"] = cf is True or cf == "partly"
            r["could_fail_partly"] = cf == "partly"  # "only partly" (John, 2026-11-21): scores half
            r["separates"] = bool(ans.get("separates"))
            r["separates_from"] = [str(x) for x in ans.get("separates_from", []) or []]
            r["rival_predicts_same"] = bool(ans.get("rival_predicts_same", False))
            r["which_rivals_same"] = [str(x) for x in ans.get("which_rivals_same", []) or []]
            if resend:
                r["replaces_earlier_gemini_reading"] = True
        else:
            r["verdict"] = str(ans.get("verdict", "")).lower()
        gem[jid] = r
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
    (DATA / "readings-gemini-stage3.toml").write_text("\n".join(lines))

    def first_reading(j):
        c = next(r for r in j["reading"] if r["reader"] == "claude")
        e = dict(c)
        ru = rulings.get(j["id"])
        if j["kind"] == "testability" and ru:
            if "separates" in ru:
                e["separates"] = ru["separates"]
                e["separates_from"] = ru.get("separates_from", [])
            if "could_fail" in ru:
                e["could_fail"] = ru["could_fail"]
        return c, e

    out = {"by_kind": {}, "disagreements": [], "problems": problems}
    for kind in ("outcome", "commitment", "testability"):
        ids = [i for i in gem if judgements[i]["kind"] == kind]
        agree = raw_agree = 0
        part = {"could_fail": 0, "separates": 0}
        for i in ids:
            j = judgements[i]
            c, e = first_reading(j)
            g = gem[i]
            if kind == "testability":
                same = (e["could_fail"], e["separates"]) == (g["could_fail"], g["separates"])
                raw_agree += (c["could_fail"], c["separates"]) == (g["could_fail"], g["separates"])
                part["could_fail"] += e["could_fail"] == g["could_fail"]
                part["separates"] += e["separates"] == g["separates"]
                cv = f"could fail {e['could_fail']}, separates {e['separates']} {e.get('separates_from', [])}"
                gv = (f"could fail {g['could_fail']}, separates {g['separates']} {g['separates_from']}; "
                      f"a rival predicts the same: {g['rival_predicts_same']} {g['which_rivals_same']}")
                would = "no ruled rule; for John"
            else:
                same = c["verdict"] == g["verdict"]
                cv, gv = c["verdict"], g["verdict"]
                if kind == "outcome" and "mixed" in (c["verdict"], g["verdict"]):
                    would = "rule E would record it as mixed (not applied)"
                elif kind == "commitment":
                    would = "the dating rule on split readers would leave it uncounted (not applied)"
                else:
                    would = "no ruled rule; for John"
            agree += same
            if not same:
                out["disagreements"].append({
                    "judgement": i, "kind": kind, "theory": preds[j["prediction"]]["theory"],
                    "prediction": j["prediction"], "prediction_statement": preds[j["prediction"]]["statement"],
                    "study": j.get("study", ""), "claude": cv, "claude_reason": c["reason"],
                    "gemini": gv, "gemini_reason": g["reason"], "gemini_unsure": g["unsure"],
                    "first_of_record": "gemini" if g["order"] == "first" else "claude",
                    "a_ruled_rule_would": would})
        n = len(ids)
        d = {"read_by_both": n, "agree": agree, "disagree": n - agree,
             "disagreement_rate": round((n - agree) / n, 3) if n else None}
        if kind == "testability":
            d["agree_on_could_fail"] = part["could_fail"]
            d["agree_on_separates"] = part["separates"]
            d["raw_agree_against_claudes_earlier_question"] = raw_agree
        out["by_kind"][kind] = d
    o = out["by_kind"].get("outcome", {})
    out["stop_condition"] = {"rule": "the readers disagree on more than a third of the outcome judgements",
                             "outcome_rate": o.get("disagreement_rate"),
                             "stops": bool(o.get("disagreement_rate") is not None and o["disagreement_rate"] > 1 / 3)}
    out["models"] = sorted({r["model"] for r in gem.values()})
    out["calls"] = len(gem)
    out["cost_usd"] = round(sum(r["cost_usd"] for r in gem.values()), 4)
    (DATA / "agreement-stage3.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("by_kind", "stop_condition", "models", "calls", "cost_usd", "problems")}, indent=2))
    print(f"{len(out['disagreements'])} disagreements")
    return 0


if __name__ == "__main__":
    sys.exit(main())
