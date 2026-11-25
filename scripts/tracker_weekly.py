#!/usr/bin/env python3
"""The weekly reading's mechanical part: rerun the fixed searches, find what is new, count what waits.

Method: docs/weekly-reading.md. Instruction for the run: docs/weekly-reading-prompt.md.

Subcommands:
  search   rerun every fixed per-prediction search (data/tracker/searches-*.toml) on Europe PMC,
           newest first, first 40 results each, exactly as the 2026-11-21 baseline ran them, and
           save the raw results to data/tracker/search-runs-<date>/. A result is NEW when its id
           is in no earlier search-runs folder. Prints the new results by prediction, and writes
           them to data/tracker/readings/<date>.candidates.json for the session to screen.
  check    validate data/tracker/waiting.toml and data/tracker/readings/*.json.
  contrast compare the ConTraSt database's live export (reading list only) with the DOIs seen
           before (data/tracker/contrast-seen.txt, DOIs alone, no ConTraSt field) and print the
           new papers it marks as designed to test global workspace, integrated information,
           higher-order or first-order (recurrent processing) theories. --record adds them to
           the seen list.
  count    print how many studies are waiting to be scored, in all and by theory, as JSON
           (the figure the site shows). A waiting row stops waiting when a [[resolved]] entry
           names it (scored, or dropped with a reason).

Nothing here touches a score, a study record or a judgement. Rows are only ever appended.

Usage:
  python3 scripts/tracker_weekly.py search [--date YYYY-MM-DD] [--out DIR] [--data DIR]
  python3 scripts/tracker_weekly.py check
  python3 scripts/tracker_weekly.py count
  (--out: a dry run, writing the runs and candidates there instead of into the records;
   --data: read the records from another folder, for a dry run against another branch's copy)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tracker"
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
VERDICTS = {"quiet", "noted", "waiting", "flagged"}


def pacific_today():
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()
    except Exception:
        return dt.date.today().isoformat()


def searches(data):
    out = []
    for f in sorted(data.glob("searches-*.toml")):
        for s in tomllib.load(open(f, "rb")).get("search", []):
            out.append(dict(s, file=f.name))
    return out


def seen_ids(data, before_date):
    """Every result id in a search run made before this reading's date: the baseline and earlier readings."""
    seen = set()
    for d in sorted(data.glob("search-runs-*")):
        if d.name.removeprefix("search-runs-") >= before_date:
            continue
        for f in d.glob("*.json"):
            for r in json.loads(f.read_text())["results"]:
                seen.add(r["id"])
    return seen


def run_query(q):
    params = urllib.parse.urlencode({"query": q, "format": "json", "pageSize": 40,
                                     "sort": "P_PDATE_D desc", "resultType": "core"})
    for attempt in range(5):
        try:
            return json.load(urllib.request.urlopen(f"{API}?{params}", timeout=120))
        except urllib.error.HTTPError as e:
            if e.code in (500, 502, 503, 504) and attempt < 4:
                time.sleep(10 * (attempt + 1))
                continue
            raise


def cmd_search(a):
    date = a.date or pacific_today()
    data = Path(a.data) if a.data else DATA
    out_root = Path(a.out) if a.out else data
    run_dir = out_root / f"search-runs-{date}"
    run_dir.mkdir(parents=True, exist_ok=True)
    seen = seen_ids(data, date)
    if not seen:
        print("no earlier search run found: every result would count as new; stopping", file=sys.stderr)
        return 2
    new = {}
    ss = searches(data)
    for s in ss:
        d = run_query(s["query"])
        res = []
        for r in d["resultList"]["result"]:
            res.append({"rank": len(res) + 1, "id": r.get("id"), "source": r.get("source"),
                        "pmid": r.get("pmid"), "pmcid": r.get("pmcid"), "doi": r.get("doi"),
                        "first_publication_date": r.get("firstPublicationDate"),
                        "title": r.get("title"), "authors": r.get("authorString"),
                        "journal": (r.get("journalInfo") or {}).get("journal", {}).get("title"),
                        "pub_types": (r.get("pubTypeList") or {}).get("pubType", []),
                        "open_access": r.get("isOpenAccess"),
                        "abstract": re.sub(r"<[^>]+>", "", r.get("abstractText", "") or "")})
        (run_dir / f"{s['prediction']}.json").write_text(json.dumps(
            {"prediction": s["prediction"], "query": s["query"], "run_on": date,
             "hit_count": d.get("hitCount"), "results": res}, indent=1, ensure_ascii=False))
        fresh = [r for r in res if r["id"] not in seen]
        if fresh:
            new[s["prediction"]] = fresh
        print(f"{s['prediction']}: {d.get('hitCount')} hits, {len(fresh)} new", flush=True)
        time.sleep(1)
    rd = out_root / "readings"
    rd.mkdir(parents=True, exist_ok=True)
    (rd / f"{date}.candidates.json").write_text(json.dumps(
        {"date": date, "searches": len(ss), "new_by_prediction": new}, indent=1, ensure_ascii=False))
    print(f"\n{sum(len(v) for v in new.values())} new results across {len(new)} predictions; "
          f"written to {rd / (date + '.candidates.json')}")
    return 0


CONTRAST = ("https://contrastdb.tau.ac.il/api/studies/experiments_graphs/parameters_distribution_free_queries/"
            "?&breakdown=finding_tag&min_number_of_experiments=0&is_reporting=either&type_of_consciousness=either&is_csv=true")
FAMILIES = {"GNW": "gwt", "IIT": "iit", "HOT": "hot", "FOT": "rpt"}


def cmd_contrast(a):
    import csv, io
    data = Path(a.data) if a.data else DATA
    seen_f = data / "contrast-seen.txt"
    seen = set(seen_f.read_text().split()) if seen_f.exists() else set()
    rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(CONTRAST, timeout=120).read().decode("utf-8"))))
    new = {}
    for r in rows:
        fams = {FAMILIES[x.strip()] for x in r["Driven_by_theories"].split("||") if x.strip() in FAMILIES}
        if r["Is_the_experiment_theory_driven"] == "driven" and fams and r["DOI"] and r["DOI"] not in seen:
            new.setdefault(r["DOI"], {"doi": r["DOI"], "year": r["Year"], "title": r["Title"], "theories": set()})["theories"] |= fams
    for v in new.values():
        v["theories"] = sorted(v["theories"])
    print(json.dumps({"export_rows": len(rows), "new_designed_to_test": sorted(new.values(), key=lambda v: v["year"], reverse=True)}, indent=1, ensure_ascii=False))
    if a.record:
        all_dois = sorted(seen | {r["DOI"] for r in rows if r["DOI"]})
        seen_f.write_text("\n".join(all_dois) + "\n")
    if not seen:
        print("first run: no seen list yet, so every paper is listed; record it as the baseline with --record", file=sys.stderr)
    return 0


def load_waiting(data):
    p = data / "waiting.toml"
    if not p.exists():
        return [], []
    d = tomllib.load(open(p, "rb"))
    return d.get("waiting", []), d.get("resolved", [])


def cmd_check(a):
    data = Path(a.data) if a.data else DATA
    errs = []
    preds = {p["id"]: p for p in tomllib.load(open(data / "predictions.toml", "rb"))["prediction"]}
    waiting, resolved = load_waiting(data)
    ids = set()
    for w in waiting:
        for k in ("id", "found_on", "prediction", "title", "first_appeared", "screen", "reading"):
            if not w.get(k):
                errs.append(f"waiting {w.get('id')}: missing {k}")
        if w.get("id") in ids:
            errs.append(f"waiting {w['id']}: duplicate id")
        ids.add(w.get("id"))
        if w.get("prediction") not in preds:
            errs.append(f"waiting {w.get('id')}: unknown prediction {w.get('prediction')}")
        if not (data / "readings" / f"{w.get('reading')}.json").exists():
            errs.append(f"waiting {w.get('id')}: no reading record {w.get('reading')}.json")
    for r in resolved:
        if r.get("waiting") not in ids:
            errs.append(f"resolved: unknown waiting row {r.get('waiting')}")
        if r.get("how") not in ("scored", "dropped"):
            errs.append(f"resolved {r.get('waiting')}: how must be scored or dropped")
        if r.get("how") == "dropped" and not r.get("why"):
            errs.append(f"resolved {r.get('waiting')}: a dropped row needs a reason")
    rdir = data / "readings"
    for f in sorted(rdir.glob("*.json")) if rdir.exists() else []:
        if f.name.endswith(".candidates.json"):
            continue
        r = json.loads(f.read_text())
        h = r.get("reading", {})
        if not re.match(r"^\d{4}-\d{2}-\d{2}(-\d)?$", f.stem) or h.get("date") != f.stem[:10]:
            errs.append(f"{f.name}: the file name must be the reading's date")
        for k in ("date", "window_start", "window_end", "commit_before", "by", "searches",
                  "new_results", "waiting_added", "flagged"):
            if k not in h:
                errs.append(f"{f.name}: header missing {k}")
        for it in r.get("items", []):
            if it.get("verdict") not in VERDICTS:
                errs.append(f"{f.name} {it.get('id')}: verdict must be one of {sorted(VERDICTS)}")
            if it.get("verdict") == "flagged" and not it.get("for_john"):
                errs.append(f"{f.name} {it.get('id')}: a flagged item needs for_john")
    if errs:
        print("\n".join(errs), file=sys.stderr)
        return 1
    print(f"weekly-reading records valid: {len(waiting)} waiting rows, {len(resolved)} resolved")
    return 0


def waiting_counts(data=DATA):
    """How many studies wait to be scored, in all and by theory: the figure the site shows."""
    preds = {p["id"]: p for p in tomllib.load(open(data / "predictions.toml", "rb"))["prediction"]}
    waiting, resolved = load_waiting(data)
    done = {r["waiting"] for r in resolved}
    studies = {}
    for w in waiting:
        if w["id"] in done:
            continue
        # one study can wait for two predictions; it is counted once
        key = w.get("doi") or w.get("europepmc_id") or w["id"]
        studies.setdefault(key, set()).add(preds[w["prediction"]]["theory"])
    by_theory = {}
    for ths in studies.values():
        for t in ths:
            by_theory[t] = by_theory.get(t, 0) + 1
    rdir = data / "readings"
    readings = sorted(f.stem for f in rdir.glob("*.json") if not f.name.endswith(".candidates.json")) if rdir.exists() else []
    return {"waiting_studies": len(studies), "by_theory": by_theory,
            "last_reading": readings[-1][:10] if readings else None}


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("--date")
    s.add_argument("--out")
    s.add_argument("--data")
    c = sub.add_parser("check")
    c.add_argument("--data")
    k = sub.add_parser("contrast")
    k.add_argument("--data")
    k.add_argument("--record", action="store_true")
    n = sub.add_parser("count")
    n.add_argument("--data")
    a = ap.parse_args(argv)
    if a.cmd == "search":
        return cmd_search(a)
    if a.cmd == "check":
        return cmd_check(a)
    if a.cmd == "contrast":
        return cmd_contrast(a)
    print(json.dumps(waiting_counts(Path(a.data) if a.data else DATA), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
