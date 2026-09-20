#!/usr/bin/env python3
"""Export data/project.toml to site/src/data/project.json for the Astro site.

Same pattern as belt-equation/scripts/export.py: Python owns the data, the
site only renders what passes validation here. Run from anywhere:

    python3 scripts/export_site.py          # write the JSON
    python3 scripts/export_site.py --check  # validate only, exit 1 on error

Needs Python 3.11+ (tomllib). No third-party packages.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "project.toml"
OUT = ROOT / "site" / "src" / "data" / "project.json"

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

GOAL_STATUS = {"delivered", "in-progress", "not-started"}
STAGE_STATUS = {"delivered", "in-progress", "folded", "waiting", "descoped", "conditional", "not-started"}
QUESTION_STATUS = {"open", "answered", "answered-in-part", "parked", "waiting"}
IDEA_STATUS = {"on-the-table", "authorised", "deferred", "rejected", "done"}
FINDING_KIND = {"registered", "diagnostic", "ruled", "process"}
STEP_STATUS = {"authorised", "in-progress", "pending", "done", "blocked"}
TIMELINE_KIND = {"result", "null", "ruling", "process", "spend", "build"}


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
    date.fromisoformat(s)


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
    today = date.today()
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


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    try:
        with open(SRC, "rb") as fh:
            d = tomllib.load(fh)
        validate(d)
    except (Bad, tomllib.TOMLDecodeError, OSError) as e:
        print(f"export_site: {e}", file=sys.stderr)
        return 1
    d["derived"] = derive(d)
    if check_only:
        print(f"export_site: {SRC.relative_to(ROOT)} is valid "
              f"({len(d['stages'])} stages, {len(d['questions'])} questions, "
              f"{len(d['ideas'])} ideas, {len(d['findings'])} findings, "
              f"{len(d['next_steps'])} next steps, {len(d['timeline'])} timeline rows)")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"export_site: wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
