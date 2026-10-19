#!/usr/bin/env python3
"""Export the site's data files to JSON for the Astro site.

    data/project.toml  ->  site/src/data/project.json   (every page)
    data/roadmap.toml  ->  site/src/data/roadmap.json   (/roadmap/)
    data/project.toml  ->  data/headline.json            (the headline file, committed)
                       ->  site/public/data/headline.json (its public copy, served at /data/headline.json)

Same pattern as belt-equation/scripts/export.py: Python owns the data, the
site only renders what passes validation here. Run from anywhere:

    python3 scripts/export_site.py          # write the JSON files, the headline file and its public copy
    python3 scripts/export_site.py --check  # validate both data files, exit 1 on error;
                                            # warn if data/headline.json lags data/project.toml

The headline file (added 2026-10-17, the site's first adoption from the
Sentient Horizons lessons review of the same day) is the few numbers another
site needs to say where this project stands: the stages of the ladder
delivered, the ladder's mean progress, the spend against the ceiling, the day
the log was last updated, the programme's state in one sentence, and a status
line. Every value is read from data/project.toml; nothing is computed from
anything else, and the one sentence is the record's own first sentence.

Needs Python 3.11+ (tomllib). No third-party packages.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from datetime import date, datetime
from zoneinfo import ZoneInfo
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "project.toml"
OUT = ROOT / "site" / "src" / "data" / "project.json"
ROADMAP_SRC = ROOT / "data" / "roadmap.toml"
ROADMAP_OUT = ROOT / "site" / "src" / "data" / "roadmap.json"
HEADLINE_OUT = ROOT / "data" / "headline.json"
HEADLINE_PUBLIC = ROOT / "site" / "public" / "data" / "headline.json"
# The site's address, the same value as `site` in site/astro.config.mjs.
SITE = "https://minimumviablemind.sentient-horizons.com"

# Every date in the data files is Pacific, so "today" for the day counts is
# the Pacific date too, not the build machine's clock (the deploy runs on UTC,
# which is a day ahead every evening from 17:00 Pacific).
PACIFIC = ZoneInfo("America/Los_Angeles")


def today_pacific() -> date:
    return datetime.now(PACIFIC).date()

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

GOAL_STATUS = {"delivered", "in-progress", "not-started"}
STAGE_STATUS = {"delivered", "in-progress", "folded", "waiting", "descoped", "conditional", "not-started"}
QUESTION_STATUS = {"open", "answered", "answered-in-part", "parked", "waiting"}
IDEA_STATUS = {"on-the-table", "authorised", "deferred", "rejected", "done"}
FINDING_KIND = {"registered", "diagnostic", "ruled", "process"}
STEP_STATUS = {"authorised", "in-progress", "pending", "done", "blocked"}
TIMELINE_KIND = {"result", "null", "ruling", "process", "spend", "build"}

# data/roadmap.toml vocabularies (listed in that file's header comment).
WEEKEND_STATUS = {"planned", "active", "done", "partial", "blackout", "slack"}
RM_GOAL_STATUS = {"planned", "done", "carried", "dropped", "not_needed"}
RM_GOAL_OWNER = {"john", "agents", "both"}
MILESTONE_KIND = {"kill_date", "wrap_up", "hibernation"}
EXTENSION_STATUS = {"proposed", "authorised", "running", "done", "deferred", "declined"}
# Goals that count toward progress. "not_needed" (a branch that did not fire)
# is left out; "carried" counts as not yet done and "dropped" counts against.
RM_GOAL_COUNTS = {"planned", "done", "carried", "dropped"}


class Bad(Exception):
    pass


def need(obj: dict, key: str, where: str, typ=None):
    if key not in obj:
        raise Bad(f"{where}: missing '{key}'")
    v = obj[key]
    if typ is not None and not isinstance(v, typ):
        raise Bad(f"{where}: '{key}' should be {typ.__name__}, got {type(v).__name__}")
    return v


def check_date(s: str, where: str):
    if not DATE.match(s):
        raise Bad(f"{where}: bad date '{s}' (want YYYY-MM-DD)")
    try:
        date.fromisoformat(s)
    except ValueError as e:
        raise Bad(f"{where}: '{s}' is not a real date ({e})") from None


def unique_ids(rows: list[dict], where: str):
    seen = set()
    for r in rows:
        i = need(r, "id", where, str)
        if i in seen:
            raise Bad(f"{where}: duplicate id '{i}'")
        seen.add(i)


def validate(d: dict) -> None:
    p = need(d, "project", "top level", dict)
    for k in ("name", "short", "updated_on", "question", "one_line", "where_we_are",
              "where_we_are_going", "hibernation_by", "wrap_up_start", "pipeline_resumes", "repo"):
        need(p, k, "[project]", str)
    for k in ("updated_on", "hibernation_by", "wrap_up_start", "pipeline_resumes"):
        check_date(p[k], f"[project].{k}")

    w = need(d, "wager", "top level", dict)
    for k in ("title", "claim", "status_note", "why_no_verdict", "source"):
        need(w, k, "[wager]", str)

    goals = need(d, "goals", "top level", list)
    unique_ids(goals, "[[goals]]")
    for g in goals:
        w = f"goal {g['id']}"
        for k in ("title", "summary", "evidence"):
            need(g, k, w, str)
        if need(g, "status", w, str) not in GOAL_STATUS:
            raise Bad(f"{w}: status '{g['status']}' not in {sorted(GOAL_STATUS)}")

    stages = need(d, "stages", "top level", list)
    unique_ids(stages, "[[stages]]")
    stage_ids = {s["id"] for s in stages}
    for s in stages:
        w = f"stage {s['id']}"
        for k in ("name", "one_line", "adjudicates"):
            need(s, k, w, str)
        if need(s, "status", w, str) not in STAGE_STATUS:
            raise Bad(f"{w}: status '{s['status']}' not in {sorted(STAGE_STATUS)}")
        pr = need(s, "progress", w, int)
        if not 0 <= pr <= 100:
            raise Bad(f"{w}: progress {pr} out of 0..100")
        need(s, "delivered", w, list)
        need(s, "remaining", w, list)

    qs = need(d, "questions", "top level", list)
    unique_ids(qs, "[[questions]]")
    for q in qs:
        w = f"question {q['id']}"
        for k in ("title", "current_answer", "answered_by", "loses_if"):
            need(q, k, w, str)
        if need(q, "status", w, str) not in QUESTION_STATUS:
            raise Bad(f"{w}: status '{q['status']}' not in {sorted(QUESTION_STATUS)}")

    ideas = need(d, "ideas", "top level", list)
    unique_ids(ideas, "[[ideas]]")
    for i in ideas:
        w = f"idea {i['id']}"
        for k in ("title", "cost", "teaches", "gate"):
            need(i, k, w, str)
        if need(i, "status", w, str) not in IDEA_STATUS:
            raise Bad(f"{w}: status '{i['status']}' not in {sorted(IDEA_STATUS)}")
        if need(i, "stage", w, str) not in stage_ids:
            raise Bad(f"{w}: stage '{i['stage']}' is not a stage id")

    fs = need(d, "findings", "top level", list)
    unique_ids(fs, "[[findings]]")
    for f in fs:
        w = f"finding {f['id']}"
        for k in ("title", "what", "so_what", "source"):
            need(f, k, w, str)
        check_date(need(f, "date", w, str), w)
        if need(f, "kind", w, str) not in FINDING_KIND:
            raise Bad(f"{w}: kind '{f['kind']}' not in {sorted(FINDING_KIND)}")
        if need(f, "stage", w, str) not in stage_ids:
            raise Bad(f"{w}: stage '{f['stage']}' is not a stage id")

    ns = need(d, "next_steps", "top level", list)
    unique_ids(ns, "[[next_steps]]")
    for n in ns:
        w = f"next step {n['id']}"
        for k in ("title", "when", "owner", "cost", "teaches"):
            need(n, k, w, str)
        need(n, "decision", w, bool)
        if need(n, "status", w, str) not in STEP_STATUS:
            raise Bad(f"{w}: status '{n['status']}' not in {sorted(STEP_STATUS)}")

    sp = need(d, "spend", "top level", dict)
    check_date(need(sp, "as_of", "[spend]", str), "[spend].as_of")
    need(sp, "account_balance", "[spend]", (int, float))
    lines = need(sp, "lines", "[spend]", list)
    for ln in lines:
        w = f"spend line '{ln.get('name', '?')}'"
        need(ln, "name", w, str)
        cap = need(ln, "cap", w, (int, float))
        spent = need(ln, "spent", w, (int, float))
        if spent < 0 or cap <= 0:
            raise Bad(f"{w}: cap must be > 0 and spent >= 0")
        if spent > cap:
            raise Bad(f"{w}: spent {spent} exceeds cap {cap}; a cap breach is a protocol violation and must be recorded in STATUS.md before this file changes")

    tl = need(d, "timeline", "top level", list)
    last = None
    for t in tl:
        w = f"timeline '{t.get('title', '?')[:40]}'"
        check_date(need(t, "date", w, str), w)
        for k in ("title", "summary"):
            need(t, k, w, str)
        if need(t, "kind", w, str) not in TIMELINE_KIND:
            raise Bad(f"{w}: kind '{t['kind']}' not in {sorted(TIMELINE_KIND)}")
        if last is not None and t["date"] > last:
            raise Bad(f"{w}: timeline must be newest first (found {t['date']} after {last})")
        last = t["date"]


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return None


def derive(d: dict) -> dict:
    """Numbers the pages need that should be computed, not typed."""
    p = d["project"]
    today = today_pacific()
    hib = date.fromisoformat(p["hibernation_by"])
    wrap = date.fromisoformat(p["wrap_up_start"])
    stages = d["stages"]
    overall = round(sum(s["progress"] for s in stages) / len(stages))

    def by_status(rows, key="status"):
        out: dict[str, int] = {}
        for r in rows:
            out[r[key]] = out.get(r[key], 0) + 1
        return out

    lines = []
    for ln in d["spend"]["lines"]:
        lines.append({**ln, "fraction": round(ln["spent"] / ln["cap"], 4),
                      "remaining": round(ln["cap"] - ln["spent"], 2)})
    d["spend"]["lines"] = lines

    decisions = [n for n in d["next_steps"] if n["decision"] and n["status"] != "done"]
    return {
        "exported_on": today.isoformat(),
        "commit": git_commit(),
        "days_to_hibernation": (hib - today).days,
        "days_to_wrap_up": (wrap - today).days,
        "stage_progress_mean": overall,
        "counts": {
            "stages": by_status(stages),
            "questions": by_status(d["questions"]),
            "ideas": by_status(d["ideas"]),
            "findings": len(d["findings"]),
            "findings_by_kind": by_status(d["findings"], "kind"),
            "timeline": len(d["timeline"]),
            "decisions_pending": len(decisions),
        },
        "decisions_pending": [n["id"] for n in decisions],
    }


def usd(n: float) -> str:
    """$450 for a whole number, $230.94 otherwise; the site's own rule (src/lib/project.ts)."""
    return f"${n:.0f}" if float(n).is_integer() else f"${n:.2f}"


def join_words(items: list[str]) -> str:
    """'a, b and c', the way the home page joins the delivered stages' names."""
    if len(items) <= 1:
        return "".join(items)
    return f"{', '.join(items[:-1])} and {items[-1]}"


def first_sentence(text: str) -> str:
    """The record's own first sentence: up to the first full stop, question mark or
    exclamation mark (a closing quote may follow it) that is followed by a space and
    a capital letter, or by the end of the text. A decimal point or a date inside a
    sentence does not end it, because no space follows it."""
    m = re.match(r"(.+?[.!?]['’\"”]?)(?:\s+(?=[A-Z\"'“‘])|\s*$)", text, re.S)
    if not m or len(m.group(1)) < 40:
        raise Bad("[project].where_we_are: could not take a first sentence from it")
    return m.group(1).strip()


def headline(d: dict, derived: dict) -> dict:
    """The headline file: the few numbers another site needs to say where this
    project stands, every one read from data/project.toml (nothing from anywhere
    else). What the home page shows is what this says: the count of delivered
    stages with their names, the ladder's mean progress, and the spend line the
    record calls the programme's ceiling (the spend line with the largest cap)."""
    p = d["project"]
    stages = d["stages"]
    delivered = [s for s in stages if s["status"] == "delivered"]
    names = [s["name"][0].lower() + s["name"][1:] for s in delivered]
    by_status: dict[str, int] = {}
    for s in stages:
        by_status[s["status"]] = by_status.get(s["status"], 0) + 1
    ceiling = max(d["spend"]["lines"], key=lambda ln: ln["cap"])
    latest = d["timeline"][0]
    state = first_sentence(p["where_we_are"])
    ladder_words = (f"{len(delivered)} of {len(stages)} stages of the project's ladder "
                    f"delivered so far: {join_words(names)}")
    # [spend].headline_words, when set, says the spend in the record's own words
    # (since 2026-10-18 the running total across every vendor is a record, not a
    # cap: docs/rulings/2026-10-18-spending-ruling.md); otherwise the largest cap.
    words = d["spend"].get("headline_words")
    spend_words = words if isinstance(words, str) and words.strip() else \
        f"about {usd(ceiling['spent'])} of the {usd(ceiling['cap'])} ceiling spent"
    return {
        "computed_on": derived["exported_on"],
        "project": {
            "name": p["name"],
            "short": p["short"],
            "repo": p["repo"],
            "site": SITE,
            "served_at": f"{SITE}/data/headline.json",
        },
        "source": {
            "file": "data/project.toml",
            "script": "scripts/export_site.py",
            "record": "STATUS.md is the record of record; data/project.toml is its structured twin and the only input here",
            "rule": "every value is read from the data file as written; nothing is computed from anything else, and the one-sentence state is the record's own first sentence",
        },
        "record_updated_on": p["updated_on"],
        "ladder": {
            "delivered": len(delivered),
            "total": len(stages),
            "delivered_names": [s["name"] for s in delivered],
            "by_status": by_status,
            "mean_progress": derived["stage_progress_mean"],
            "words": ladder_words,
            "mean_progress_words": f"Ladder progress, mean across the {len(stages)} stages: {derived['stage_progress_mean']}%",
        },
        "spend": {
            "spent": ceiling["spent"],
            "cap": ceiling["cap"],
            "line": ceiling["name"],
            "as_of": d["spend"]["as_of"],
            "words": spend_words,
            "lines": [{"name": ln["name"], "spent": ln["spent"], "cap": ln["cap"]} for ln in d["spend"]["lines"]],
        },
        "state": state,
        "latest_entry": {"date": latest["date"], "title": latest["title"]},
        "status": (f"{len(delivered)} of {len(stages)} stages delivered; {spend_words}; "
                   f"log last updated {p['updated_on']}."),
        "dates": {
            "wrap_up_start": p["wrap_up_start"],
            "hibernation_by": p["hibernation_by"],
        },
    }


def headline_is_current(fresh: dict) -> bool:
    """Whether the committed data/headline.json says what the data file says now,
    the day it was computed aside."""
    try:
        old = json.loads(HEADLINE_OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    strip = lambda h: {k: v for k, v in h.items() if k != "computed_on"}
    return strip(old) == strip(fresh)


def one_of(obj: dict, key: str, allowed: set[str], where: str) -> str:
    v = need(obj, key, where, str)
    if v not in allowed:
        raise Bad(f"{where}: {key} '{v}' not in {sorted(allowed)}")
    return v


def validate_roadmap(d: dict) -> None:
    r = need(d, "roadmap", "top level", dict)
    for k in ("title", "written_on", "updated_on", "source", "one_line", "question",
              "wrap_up_start", "hibernation_by", "weekday_rule", "replan_rule"):
        need(r, k, "[roadmap]", str)
    for k in ("written_on", "updated_on", "wrap_up_start", "hibernation_by"):
        check_date(r[k], f"[roadmap].{k}")

    ms = need(d, "milestones", "top level", list)
    unique_ids(ms, "[[milestones]]")
    for m in ms:
        w = f"milestone {m['id']}"
        need(m, "title", w, str)
        check_date(need(m, "date", w, str), w)
        one_of(m, "kind", MILESTONE_KIND, w)

    wks = need(d, "weekends", "top level", list)
    if not wks:
        raise Bad("[[weekends]]: at least one weekend is needed")
    unique_ids(wks, "[[weekends]]")
    goal_ids: set[str] = set()
    prev = None
    active = []
    for wk in wks:
        w = f"weekend {wk['id']}"
        for k in ("title", "outcome", "beside", "john_hours"):
            need(wk, k, w, str)
        n = need(wk, "number", w, int)
        days = need(wk, "days", w, int)
        if days < 0:
            raise Bad(f"{w}: days {days} is negative")
        start = need(wk, "start", w, str)
        end = need(wk, "end", w, str)
        check_date(start, f"{w}.start")
        check_date(end, f"{w}.end")
        if start > end:
            raise Bad(f"{w}: start {start} is after end {end}")
        if prev is not None:
            if n != prev["number"] + 1:
                raise Bad(f"{w}: number {n} does not follow {prev['number']}")
            if start <= prev["end"]:
                raise Bad(f"{w}: starts {start}, not after weekend {prev['id']} ends {prev['end']}; weekends must be in order")
        prev = wk
        if one_of(wk, "status", WEEKEND_STATUS, w) == "active":
            active.append(wk["id"])
        items = need(wk, "john_items", w, list)
        if not all(isinstance(i, str) for i in items):
            raise Bad(f"{w}: every john_items entry must be a string")
        for g in need(wk, "goals", w, list):
            gid = need(g, "id", f"{w} goal", str)
            gw = f"goal {gid}"
            if gid in goal_ids:
                raise Bad(f"{gw}: duplicate goal id")
            goal_ids.add(gid)
            need(g, "text", gw, str)
            one_of(g, "owner", RM_GOAL_OWNER, gw)
            st = one_of(g, "status", RM_GOAL_STATUS, gw)
            if "note" in g:
                need(g, "note", gw, str)
            if st == "carried" and not g.get("note", "").strip():
                raise Bad(f"{gw}: a carried goal needs a note saying which weekend it moved to")
    if len(active) > 1:
        raise Bad(f"[[weekends]]: more than one weekend is active ({', '.join(active)})")

    exts = need(d, "extensions", "top level", list)
    unique_ids(exts, "[[extensions]]")
    for e in exts:
        w = f"extension {e['id']}"
        for k in ("title", "when", "cost", "teaches"):
            need(e, k, w, str)
        one_of(e, "status", EXTENSION_STATUS, w)


def derive_roadmap(d: dict) -> dict:
    """Progress counts, days to each milestone, and positions on the timeline
    axis, all computed at export (build) time from today's date."""
    today = today_pacific()
    wks = d["weekends"]
    goals = [g for wk in wks for g in wk["goals"]]

    def by_status(rows):
        out: dict[str, int] = {}
        for r in rows:
            out[r["status"]] = out.get(r["status"], 0) + 1
        return out

    goal_counts = by_status(goals)
    wk_counts = by_status(wks)

    # One date axis for the weekend segments and the milestone ticks: from the
    # first weekend's start to the last date on the plan, inclusive.
    day = date.fromisoformat
    first = day(wks[0]["start"])
    last = max([day(wks[-1]["end"])] + [day(m["date"]) for m in d["milestones"]])
    span = (last - first).days + 1

    def pct(dt: date, mid: bool = False) -> float:
        # mid=True places a single-day mark (a milestone, today) at the middle
        # of its day, so it lines up inside the weekend segment it falls in.
        return round(((dt - first).days + (0.5 if mid else 0)) / span * 100, 3)

    return {
        "exported_on": today.isoformat(),
        "commit": git_commit(),
        "goals_done": goal_counts.get("done", 0),
        "goals_counting": sum(1 for g in goals if g["status"] in RM_GOAL_COUNTS),
        "goals_total": len(goals),
        "goal_counts": goal_counts,
        "weekends_done": wk_counts.get("done", 0),
        "weekends_working": sum(1 for wk in wks if wk["status"] != "blackout"),
        "weekend_counts": wk_counts,
        "active_weekend": next((wk["id"] for wk in wks if wk["status"] == "active"), None),
        "milestones": [{"id": m["id"], "days_to": (day(m["date"]) - today).days} for m in d["milestones"]],
        "axis": {
            "start": first.isoformat(),
            "end": last.isoformat(),
            "today": pct(today, mid=True) if first <= today <= last else None,
            "weekends": [{"id": wk["id"], "left": pct(day(wk["start"])),
                          "width": round(((day(wk["end"]) - day(wk["start"])).days + 1) / span * 100, 3)}
                         for wk in wks],
            "milestones": [{"id": m["id"], "at": pct(day(m["date"]), mid=True)} for m in d["milestones"]],
        },
    }


def load(src: Path, check) -> dict:
    with open(src, "rb") as fh:
        d = tomllib.load(fh)
    try:
        check(d)
    except Bad as e:
        raise Bad(f"{src.relative_to(ROOT)}: {e}") from None
    return d


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    try:
        d = load(SRC, validate)
        rm = load(ROADMAP_SRC, validate_roadmap)
    except (Bad, tomllib.TOMLDecodeError, OSError) as e:
        print(f"export_site: {e}", file=sys.stderr)
        return 1
    d["derived"] = derive(d)
    rm["derived"] = derive_roadmap(rm)
    try:
        hl = headline(d, d["derived"])
    except Bad as e:
        print(f"export_site: {SRC.relative_to(ROOT)}: {e}", file=sys.stderr)
        return 1
    if check_only:
        print(f"export_site: {SRC.relative_to(ROOT)} is valid "
              f"({len(d['stages'])} stages, {len(d['questions'])} questions, "
              f"{len(d['ideas'])} ideas, {len(d['findings'])} findings, "
              f"{len(d['next_steps'])} next steps, {len(d['timeline'])} timeline rows)")
        rd = rm["derived"]
        print(f"export_site: {ROADMAP_SRC.relative_to(ROOT)} is valid "
              f"({len(rm['weekends'])} weekends, {rd['goals_total']} goals, "
              f"{len(rm['milestones'])} milestones, {len(rm['extensions'])} extensions)")
        print(f"export_site: headline reads: {hl['status']}")
        if not headline_is_current(hl):
            # A warning, not an error: the build always writes the served copy fresh,
            # so the site stays honest; only the committed copy is behind.
            print(f"export_site: warning: {HEADLINE_OUT.relative_to(ROOT)} lags "
                  f"{SRC.relative_to(ROOT)}; run `python3 scripts/export_site.py` and commit it",
                  file=sys.stderr)
        return 0
    for out, obj in ((OUT, d), (ROADMAP_OUT, rm), (HEADLINE_OUT, hl), (HEADLINE_PUBLIC, hl)):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"export_site: wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
