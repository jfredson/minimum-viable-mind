#!/usr/bin/env python3
"""Write the tracker's pages' data from the tracker records, and nothing else.

    python3 scripts/export_tracker.py           # write site/src/data/tracker.json and the
                                                # tracker block of both headline files
    python3 scripts/export_tracker.py --check   # compute and compare only; write nothing

Added 2026-11-21 for stage 3 (the site). The tracker records in data/tracker/ belong to the
scoring work, and the rules that turn them into numbers live in scripts/tracker_scores.py.
This script does not restate those rules: it imports that script's own load, validate,
compute, rank and headline functions, runs them in settled mode (only judgements two readers
agree on, or that a written rule settled), and refuses to write anything if the result
differs from the committed data/tracker/scores.json. So the site can never show a number the
scoring did not produce (tracker pattern rules 1.1 and 1.5).

What it adds is only what the pages need and the scores file does not carry, each worked out
from the same records:

- each prediction's state (untested, supported, contradicted, mixed), from its counted
  outcomes: all for is supported, all against is contradicted, anything else is mixed. The
  scoring script does not compute a prediction's state; this is the site's reading of the
  kickoff's four states, stated on the About page, and it belongs in the scoring script once
  the scoring work takes it (listed in the stage 3 site report);
- which studies were read against a prediction and why each did or did not count;
- "what would move this", computed by the ruled formulas for one hypothetical study;
- the verify entries still open and which records each touches, so every page that shows one
  of those records can say so (tracker pattern rule 3.3);
- the count of theories on the ruled list, so the line above the title never types "ten".

Display values are rounded here, once, so every page shows the same figure.
"""
from __future__ import annotations

import argparse
import datetime as dt
import math
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import tracker_scores as ts  # noqa: E402  (the scoring rules, used as they are)

OUT = ROOT / "site" / "src" / "data" / "tracker.json"
HEADLINE_FILES = [ROOT / "data" / "headline.json", ROOT / "site" / "public" / "data" / "headline.json"]
MODE = "settled"

# The ruled constants the pages state in words (kickoff section 4, ruled 2026-11-20). They
# are written once here so a page never types one in; the site check refuses a digit that
# did not come through this file or the project record.
RULES = {
    "scale_top": 100,
    "even": 50,
    "weight_start": 1,
    "weight_top": 5,
    "groups_needed": 2,
    "claims_fewest": 3,
    "claims_most": 7,
    "core_multiplier": 2,
    "reader_count": 2,
    "protections": 4,
}
# One hypothetical study for "what would move this": registered in advance and run by a
# group outside the theory's camp, so weight 1 + 1 + 1 = 3 by the ruled weights.
PROBE_WEIGHT = RULES["weight_start"] + 2
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]


def ordinal(d: int) -> str:
    return f"{d}{'th' if 10 <= d % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')}"


def long_date(iso: str | None) -> str | None:
    """A date in the house style for public prose: "November 20th, 2026"."""
    if not iso:
        return None
    parts = iso.split("-")
    if len(parts) == 3:
        y, m, d = map(int, parts)
        return f"{MONTHS[m - 1]} {ordinal(d)}, {y}"
    if len(parts) == 2:
        return f"{MONTHS[int(parts[1]) - 1]} {parts[0]}"
    return iso


def r0(x):
    """Round to a whole number, halves up (62.5 shows as 63), the same way as the bars'
    screen-reader labels (Math.round). Python's round() would take halves to the even number."""
    return None if x is None else int(math.floor(x + 0.5))


def support_of(wsum: float, total: float) -> float:
    """The ruled support formula (kickoff section 4): weighted mean put on 0 to 100."""
    return 100 * (wsum / total + 1) / 2


def waiting():
    """The weekly reading's count of new studies waiting to be scored, from the weekly-reading
    script's own `waiting_counts` (scripts/tracker_weekly.py), never worked out here. None when
    that script is not in this checkout."""
    try:
        import tracker_weekly as tw
    except ImportError:
        # Refuse rather than let every page say that no reading has run.
        raise SystemExit("export_tracker: scripts/tracker_weekly.py is missing, so the waiting count cannot be shown")
    w = tw.waiting_counts(ts.DATA)
    return {"waiting_studies": w["waiting_studies"], "by_theory": w["by_theory"],
            "last_reading": w["last_reading"], "last_reading_long": long_date(w["last_reading"])}


def hand_check(d, preds):
    """What the person's hand check of the readers' agreements covered, from its own records
    (data/tracker/spot-check-draw.toml and spot-check.toml), and how many of the judgements it
    read were read again afterwards, so About says only what was done."""
    import tomllib
    fd, fs = ts.DATA / "spot-check-draw.toml", ts.DATA / "spot-check.toml"
    if not (fd.exists() and fs.exists()):
        return None
    draw = tomllib.loads(fd.read_text())
    found = tomllib.loads(fs.read_text()).get("finding", [])
    by_id = {j["id"]: j for j in d["judgements"]}
    again = 0
    theories = set()
    for f_ in found:
        j = by_id[f_["judgement"]]
        theories.add(preds[j["prediction"]]["theory"])
        ru = j.get("ruling") or {}
        if any(r.get("date", "") > f_["date"] for r in j.get("reading", [])) or \
                (ru.get("date", "") > f_["date"] and "spot-check" not in str(ru.get("rule", ""))):
            again += 1
    return {"checked": len(found), "random": len(draw.get("random", [])), "own": len(draw.get("sentient_horizons", [])),
            "read_again": again, "theories": len(theories), "date": min(f_["date"] for f_ in found) if found else None}


def short_refs(sources, studies):
    """A short readable name for every source and study id ("Lamme 2018", "Mashour and
    colleagues 2020"), so record text that names one by its id reads as a citation, not a code.
    Built from the citation's first author and the publication year; linked where there is an
    address."""
    out = {}
    for sid, s in sources.items():
        cit = s.get("citation", "")
        head = cit.split(".")[0]
        authors = [a.strip() for a in re.split(r",| and ", head) if a.strip()]
        first = authors[0].split()[0] if authors else sid
        year = (str(s.get("published") or "")[:4]) if re.match(r"\d{4}", str(s.get("published") or "")) else (re.findall(r"\b(19|20)\d\d\b", cit) and re.search(r"\b(?:19|20)\d\d\b", cit).group(0)) or ""
        many = len(authors) > 2 or "et al" in head
        two = len(authors) == 2
        consortium = re.match(r"^([A-Z][\w-]* Consortium)", head)
        name = f"the {consortium.group(1)}" if consortium else f"{first} and colleagues" if many else (f"{first} and {authors[1].split()[0]}" if two else first)
        url = s.get("url", "")
        m = re.search(r"ebi\.ac\.uk/europepmc/webservices/rest/(PMC\d+)/fullTextXML", url)
        if m:
            url = f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(1)}/"
        out[sid] = {"label": f"{name} {year}".strip(), "url": url if url.startswith("http") else None}
    for stid, st in studies.items():
        if stid not in out and st.get("source") in out:
            out[stid] = out[st["source"]]
    return out


def links():
    """The opened links for named people, unscored theories and groups (data/links.toml)."""
    import tomllib
    f = ROOT / "data" / "links.toml"
    d = tomllib.loads(f.read_text()) if f.exists() else {}
    out = {k: d.get(k, {}) for k in ("people", "theories", "groups")}
    out["person_pages"] = d.get("person_pages", [])
    return out


def support_example(base, ranking):
    """One worked example of the support formula for About, from a ranked theory's own figures:
    the last ranked theory (the lowest support), so the example shows a negative sum."""
    ranked = [x["theory"] for x in ranking["ranked"]]
    if not ranked:
        return None
    tid = ranked[-1]
    v = base[tid]
    sr = v["support_rests_on"]
    ratio = sr["weighted_sum"] / sr["total_weight"]
    return {"theory": tid, "name": v["name"], "weighted_sum": sr["weighted_sum"], "total_weight": sr["total_weight"],
            "ratio": round(ratio, 2), "half_ratio": round(50 * ratio, 1), "half_ratio_abs": abs(round(50 * ratio, 1)), "support_exact": v["support"],
            "support": r0(v["support"])}


def git_commit():
    """The commit the records were read at, short form, as the headline file's version."""
    import subprocess
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=True).stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def open_questions(pred_out):
    """The open questions (data/open-questions.toml), each with the predictions that bear on
    it: those named in the file, plus any prediction whose record lists the question in a
    `questions` field (none do yet)."""
    import tomllib
    f = ROOT / "data" / "open-questions.toml"
    qs = tomllib.loads(f.read_text())["question"] if f.exists() else []
    out = []
    for q in qs:
        ids = list(q.get("bears_on", []))
        ids += [pid for pid, p in pred_out.items() if q["id"] in p.get("questions", []) and pid not in ids]
        for pid in ids:
            if pid not in pred_out:
                raise SystemExit(f"export_tracker: open question {q['id']} names {pid}, which is not a prediction")
        out.append({"id": q["id"], "title": q["title"], "plain": q["plain"], "bears_on": ids})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)

    d = ts.load()
    d["predictions_by_id"] = {p["id"]: p for p in d["predictions"]}
    ts.validate(d)
    base, counted, status, ranking = ts.rank(d, MODE)
    head = ts.headline(d, MODE)

    committed = json.loads((ts.DATA / "scores.json").read_text())
    if committed.get("mode") != MODE or committed["theories"] != json.loads(json.dumps(base)) \
            or committed["ranking"] != ranking or committed["headline"] != head:
        print("export_tracker: the scores computed from the records differ from data/tracker/scores.json.\n"
              "Run scripts/tracker_scores.py --mode settled (the scoring work owns it) before building the site.",
              file=sys.stderr)
        return 1

    sources = {s["id"]: s for s in d["sources"]}
    studies = {s["id"]: s for s in d["studies"]}
    preds = d["predictions_by_id"]
    claims = d["theories"]["claim"]
    listed = d["theories"]["listed_theory"][0]
    listed_names = dict(zip(listed["ids"], listed["names"]))
    theory_recs = {t["id"]: t for t in d["theories"]["theory"]}

    def src(sid):
        s = sources.get(sid)
        if not s:
            return None
        url = s.get("url", "")
        # A Europe PMC web-service address opens raw XML; a reader gets the article page instead.
        m = re.search(r"ebi\.ac\.uk/europepmc/webservices/rest/(PMC\d+)/fullTextXML", url)
        if m:
            url = f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(1)}/"
        return {"id": sid, "citation": s["citation"], "url": url if url.startswith("http") else None,
                "published": s.get("published"), "published_long": long_date(s.get("published"))}

    # settled testability per prediction
    tst = {}
    for j in d["judgements"]:
        if j["kind"] == "testability":
            r, st = ts.settle(j, MODE)
            tst[j["prediction"]] = (r, st)

    def weight(study, theory):
        pr = study["protections"]
        w = 1
        w += 1 if pr["registered"]["value"] else 0
        w += 1 if (pr["outside_camp"]["value"] and theory not in study.get("camps", [])) else 0
        w += 1 if pr["rival_agreed"]["value"] else 0
        w += 1 if pr["replicated"]["value"] else 0
        return min(w, 5)

    # every outcome judgement and its commitment, for the prediction pages
    com = {}
    for j in d["judgements"]:
        if j["kind"] == "commitment":
            r, st = ts.settle(j, MODE)
            if st != "superseded":
                com[(j["prediction"], j["study"])] = (r["verdict"] if r else None, st)
    counted_by = {(c["prediction"], c["study"]): c for c in counted}

    open_verify = [v for v in d["verify"] if v.get("status", "open") == "open"]

    def verify_for(ids):
        ids = set(ids)
        return [v["id"] for v in open_verify if ids & set(v["records"])]

    reader_label = {"first": "first reader", "second": "second reader"}

    def readings(j):
        out = []
        for r in j.get("reading", []):
            out.append({"who": "the outside reader" if r.get("order") == "first" and j["prediction"].startswith("sh-") else reader_label.get(r.get("order"), "a reader"),
                        "verdict": r.get("verdict") if j["kind"] != "testability" else ("could fail" if r.get("could_fail") else "could not fail"),
                        "reason": r.get("reason", ""), "date": r.get("date")})
        return out

    pred_out = {}
    for p in d["predictions"]:
        pid = p["id"]
        r, st = tst.get(pid, (None, "unread"))
        could_fail = bool(r and r["could_fail"])
        separates = bool(r and r["could_fail"] and r["separates"])
        # Why a separating prediction scores half on testability, by the scoring script's rule
        # (John, 2026-11-21, "Add the half-score line"); None when it scores a full point.
        half_reason = None
        if separates:
            if p["stated_by"] != "proponent":
                half_reason = "inferred"
            elif "null_excused" in p:
                half_reason = "null_excused"
            elif r.get("could_fail_partly"):
                half_reason = "partly"
        rows = []
        for j in d["judgements"]:
            if j["kind"] != "outcome" or j["prediction"] != pid:
                continue
            s = studies[j["study"]]
            o, ost = ts.settle(j, MODE)
            cverdict, cst = com.get((pid, s["id"]), (None, "unread"))
            c = counted_by.get((pid, s["id"]))
            if c:
                why = "counted"
            elif not s.get("opened", False):
                why = "not yet read"
            elif cverdict == "not-before":
                why = "explained afterwards, not counted"
            elif cverdict != "before":
                why = "not counted: the dates do not show the prediction came first"
            elif not separates:
                why = "not counted: the prediction does not separate this theory from a rival"
            elif o is None:
                why = "waiting: the two readers disagree"
            else:
                why = "not counted"
            pr = s["protections"]
            rows.append({
                "study": s["id"], "name": s["name"], "url": (src(s.get("source")) or {}).get("url"),
                "group": s["group"], "first_appeared": s["first_appeared"]["date"],
                "first_appeared_long": long_date(s["first_appeared"]["date"]),
                "outcome": o["verdict"] if o else None, "settled_by": ost,
                "counted": bool(c), "why": why,
                "weight": weight(s, p["theory"]), "multiplier": c["multiplier"] if c else (2 if p.get("core_claim") else 1),
                "protections": {
                    "registered": pr["registered"]["value"],
                    "outside_camp": bool(pr["outside_camp"]["value"] and p["theory"] not in s.get("camps", [])),
                    "rival_agreed": pr["rival_agreed"]["value"],
                    "replicated": pr["replicated"]["value"],
                },
                "readings": readings(j),
                "judgement": j["id"],
            })
        vals = [row for row in rows if row["counted"]]
        values = {ts.OUTCOME_VALUES[row["outcome"]] for row in vals}
        if not separates:
            state = "scores nothing"
        elif not vals:
            state = "untested"
        elif values == {1}:
            state = "supported"
        elif values == {-1}:
            state = "contradicted"
        else:
            state = "mixed"
        fs = p["first_stated"]
        record_ids = [pid, p["core_claim"]] + [row["study"] for row in rows] + [row["judgement"] for row in rows] + \
            [j["id"] for j in d["judgements"] if j.get("prediction") == pid]
        pred_out[pid] = {
            "id": pid, "theory": p["theory"], "theory_name": base[p["theory"]]["name"],
            "core_claim": p["core_claim"], "statement": p["statement"],
            "stated_by": p["stated_by"],
            "half_reason": half_reason,
            "null_excused_by": src(p["null_excused"]["by"]) if "null_excused" in p else None,
            "first_stated": {"source": src(fs["source"]), "date": fs.get("date"), "date_long": long_date(fs.get("date")),
                             "passage": fs.get("passage"), "location": fs.get("location")},
            "test_for": p["test_for"], "test_against": p["test_against"],
            "separates_from": [{"theory": s_["theory"], "name": listed_names.get(s_["theory"], s_["theory"]),
                                "how": s_["how"], "source": src(s_.get("source"))} for s_ in p.get("separates_from", [])],
            "could_fail": could_fail, "separates": separates, "testability_settled": st,
            "state": state, "studies": rows,
            "counted_count": len(vals),
            "verify_open": verify_for(record_ids),
            "questions": p.get("questions", []),
        }

    th_out = {}
    for tid, v in base.items():
        rec = theory_recs[tid]
        tclaims = [c for c in claims if c["theory"] == tid]
        tpreds = [pred_out[p["id"]] for p in d["predictions"] if p["theory"] == tid]
        rank_row = next((x for x in ranking["ranked"] if x["theory"] == tid), None)
        tied = []
        for k, by in ranking["shared_because_one_study_could_swap_them"].items():
            a_, b_ = k.split("|")
            if tid in (a_, b_):
                other = b_ if tid == a_ else a_
                tied.append({"with": other, "with_name": base[other]["name"], "study": by, "study_name": studies[by]["name"]})
        cl = []
        for c in tclaims:
            level = v["testability_by_claim"][c["id"]]
            mine = [p for p in tpreds if p["core_claim"] == c["id"]]
            sharp = [p for p in mine if p["separates"]]
            mine_level = max([0.5 if q["half_reason"] else 1.0 for q in sharp], default=0.0)
            if mine_level != level:
                raise SystemExit(f"export_tracker: main claim {c['id']}'s level {level} in the scores is not what its predictions give ({mine_level})")
            reasons = sorted({q["half_reason"] for q in sharp if q["half_reason"]}) if level == 0.5 else []
            cl.append({"id": c["id"], "plain": c["plain"], "quote": c["quote"], "location": c["location"],
                       "level": level, "half_reasons": reasons, "predictions": [p["id"] for p in mine], "sharp": len(sharp)})
        sr = v["support_rests_on"]
        lc = v["left_to_test_counts"]

        # what would move this, by the ruled formulas
        move = []
        n_claims = len(tclaims)
        if not v["past_bar"] or v["claims_lacking_for_bar"]:
            for cid in v["claims_lacking_for_bar"][:3]:
                new_t = v["testability"] + 100 * (1 - v["testability_by_claim"][cid]) / n_claims
                lacking_after = len(v["claims_lacking_for_bar"]) - 1
                passes = (n_claims - lacking_after) > n_claims / 2
                move.append({"kind": "claim", "claim": cid, "claim_plain": next(c["plain"] for c in tclaims if c["id"] == cid),
                             "from": r0(v["testability"]), "to": r0(new_t),
                             "passes_bar": passes and not v["past_bar"]})
        dist = [p for p in tpreds if p["separates"]]
        untested = [p for p in dist if p["state"] == "untested"]
        probe = (untested or dist)[:3]
        for p in probe:
            mult = 2 if p["core_claim"] else 1
            tot = sr["total_weight"] + PROBE_WEIGHT * mult
            groups_after = len(sr["groups"]) + 1
            if groups_after < RULES["groups_needed"]:
                move.append({"kind": "probe-short", "prediction": p["id"], "statement": p["statement"],
                             "groups": len(sr["groups"]), "groups_needed": RULES["groups_needed"]})
                continue
            up = support_of(sr["weighted_sum"] + PROBE_WEIGHT * mult, tot)
            down = support_of(sr["weighted_sum"] - PROBE_WEIGHT * mult, tot)
            move.append({"kind": "probe", "prediction": p["id"], "statement": p["statement"],
                         "from": r0(v["support"]), "for": r0(up), "against": r0(down),
                         "weight": PROBE_WEIGHT, "starts_score": v["support"] is None})

        first = [r_.get("date") for j in d["judgements"] if preds.get(j.get("prediction"), {}).get("theory") == tid
                 for r_ in j.get("reading", []) if r_.get("date")]
        first_scored = min(first) if first else None
        explained = [{"prediction": p["id"], "study": row["study"], "name": row["name"]}
                     for p in tpreds for row in p["studies"] if row["why"] == "explained afterwards, not counted"]
        th_out[tid] = {
            "id": tid, "name": v["name"], "plain": rec["plain"], "proponents": rec.get("proponents", []),
            "own": "by_exception" in rec,
            "first_scored": first_scored, "first_scored_long": long_date(first_scored),
            "claims_from": src(rec["core_claims_from"]), "fixed_on": rec["fixed_on"], "fixed_on_long": long_date(rec["fixed_on"]),
            "testability": r0(v["testability"]), "support": r0(v["support"]), "left_to_test": r0(v["left_to_test"]),
            "exact": {"testability": v["testability"], "support": v["support"], "left_to_test": v["left_to_test"]},
            "past_bar": v["past_bar"], "group": v["group"], "leans_against": v["leans_against"],
            "claims_count": n_claims, "claims_sharp": n_claims - len(v["claims_lacking_for_bar"]),
            "claims_lacking": v["claims_lacking_for_bar"],
            "claims_needed_more": max(0, n_claims // 2 + 1 - (n_claims - len(v["claims_lacking_for_bar"]))),
            "rests_on": {"outcomes": sr["counted_outcomes"], "studies": len(sr["studies"]), "groups": len(sr["groups"]),
                         "group_names": sr["groups"], "total_weight": sr["total_weight"]},
            "left_counts": {"untested": lc["untested"], "total": lc["total"], "placeholders": len(lc["placeholders_for_claims_with_none"]),
                            "distinguishing": lc["distinguishing_core_predictions"]},
            "rank": rank_row["rank"] if rank_row else None,
            "ranked_count": len(ranking["ranked"]),
            "tied": tied,
            "claims": cl,
            "predictions": [p["id"] for p in tpreds],
            "move": move,
            "explained_afterwards": explained,
            # a theory page shows each prediction's state, which rests on its studies and
            # judgements, so it carries every entry its predictions carry
            "verify_open": sorted(set(verify_for([tid] + [c["id"] for c in tclaims] + [p["id"] for p in tpreds]))
                                  | {e for p in tpreds for e in p["verify_open"]}),
        }

    scored = list(base)
    groups = {
        "ranked": [{"theory": x["theory"], "rank": x["rank"]} for x in ranking["ranked"]],
        "testable": ranking["testable_too_little_tested"],
        "not_sharp": ranking["not_yet_defined_sharply_enough"],
        "not_scored": [t for t in listed["ids"] if t not in base],
        # Ruled by John on 2026-11-21 ("Yes, pairs only"): the ranked group shows no rank numbers;
        # two neighbours that reversing one study could swap are said, in words, to be too close
        # to separate. The pairs are the scoring script's own output, never recomputed here.
        "close_pairs": [{"a": k.split("|")[0], "b": k.split("|")[1], "study": by, "study_name": studies[by]["name"]}
                        for k, by in ranking["shared_because_one_study_could_swap_them"].items()],
    }
    dates = [r.get("date") for j in d["judgements"] for r in j.get("reading", []) if r.get("date")]
    dates += [j["ruling"].get("date") for j in d["judgements"] if j.get("ruling") and j["ruling"].get("date")]
    last_judgement = max(x for x in dates if x)
    all_dist = sum(v["left_to_test_counts"]["distinguishing_core_predictions"] for v in base.values())
    headline = {
        "share_tested": r0(head["share_tested"]), "share_tested_exact": head["share_tested"],
        "tested": head["tested"], "distinguishing": head["distinguishing_predictions"],
        "theories_scored": len(scored), "theories_listed": len(listed["ids"]),
        "worked_out_on": last_judgement, "worked_out_on_long": long_date(last_judgement),
        "last_reading": None,
    }
    w_ = waiting()
    if w_:
        headline["last_reading"] = w_["last_reading"]
        headline["last_reading_long"] = w_["last_reading_long"]
        headline["waiting_studies"] = w_["waiting_studies"]
    assert all_dist == headline["distinguishing"]

    out = {
        "mode": MODE,
        "rules": RULES,
        "probe_weight": PROBE_WEIGHT,
        "listed": [{"id": t, "name": listed_names[t], "scored": t in base} for t in listed["ids"]],
        "listed_count": len(listed["ids"]),
        "scored_count": len(scored),
        "groups": groups,
        "theories": th_out,
        "predictions": pred_out,
        "studies": {sid: {"id": sid, "name": s["name"], "group": s["group"], "opened": s.get("opened", False),
                          "url": (src(s.get("source")) or {}).get("url"),
                          "found_through_contrast": s.get("found_through") == "contrast"}
                    for sid, s in studies.items()},
        "studies_count": len(studies),
        "contrast_count": sum(1 for s in studies.values() if s.get("found_through") == "contrast"),
        "judgement_count": sum(1 for j in d["judgements"] if status.get(j["id"]) != "superseded"),
        "judgement_status": {k: sum(1 for x in status.values() if x == k) for k in ("agreed", "ruled", "one-reader", "disagreed", "open-for-john", "unread")},
        "verify_open": [{"id": v_["id"], "statement": v_["statement"], "records": v_["records"]} for v_ in open_verify],
        "verify_open_count": len(open_verify),
        "headline": headline,
        "last_judgement": last_judgement,
        "last_judgement_long": long_date(last_judgement),
        "open_questions": open_questions(pred_out),
        "support_example": support_example(base, ranking),
        "links": links(),
        "refs": short_refs(sources, studies),
        "hand_check": hand_check(d, preds),
        "waiting": waiting(),
    }

    if a.check:
        print(f"export_tracker: records and scores agree; {len(scored)} of {len(listed['ids'])} listed theories scored, "
              f"{len(open_verify)} open verify entries")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    # The headline file (tracker pattern rule 1.6): the tracker's block is added beside the
    # project's existing fields, which the parent site's Projects page still reads.
    block = {
        "what": "The share of the theories' distinguishing predictions, tied to their core claims, that at least one counted study has tested at all. It measures how widely the theories have been tested, not how firmly.",
        "share_tested": headline["share_tested"], "share_tested_exact": headline["share_tested_exact"],
        "tested": headline["tested"], "distinguishing_predictions": headline["distinguishing"],
        "theories_scored": headline["theories_scored"], "theories_listed": headline["theories_listed"],
        "worked_out_on": headline["worked_out_on"], "last_reading": headline["last_reading"],
        "waiting_studies": headline.get("waiting_studies"),
        "version": git_commit(),
        "script": "scripts/tracker_scores.py --mode settled, through scripts/export_tracker.py",
    }
    for f in HEADLINE_FILES:
        if not f.exists():
            continue
        h = json.loads(f.read_text())
        h["tracker"] = block
        f.write_text(json.dumps(h, indent=2, ensure_ascii=False) + "\n")
    print(f"export_tracker: wrote {OUT.relative_to(ROOT)}; {len(scored)} of {len(listed['ids'])} listed theories scored; "
          f"headline {headline['tested']} of {headline['distinguishing']} tested at all ({headline['share_tested']}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
