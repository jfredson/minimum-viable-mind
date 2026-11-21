#!/usr/bin/env python3
"""Compute the tracker's three scores and the ranking from the records alone.

Reads data/tracker/*.toml (layout: data/tracker/README.md), refuses the files on any
broken rule, and prints, for each theory: testability, support, left to test, which
of the three ranking groups it falls in, and the ranking. Writes the same as JSON to
data/tracker/scores.json.

The rules are the kickoff proposal's (docs/2026-11-20-consciousness-tracker-kickoff-
proposal.md), sections 4 and 12, as John ruled them on 2026-11-20. Where a rule can be
read two ways, the script computes the literal reading, and reports the other beside
it under "alternative readings"; it never picks one silently.

Readings. A judgement settles when every reader who has read it agrees. With the
default --mode provisional, a judgement read by one reader only is used as it stands
and the output says so. With --mode settled, only judgements on which two readers
agree are used (the rule for publication: "Where they disagree the row is flagged for
John, and the score does not move until it is settled"). A judgement on which readers
disagree is never used, in either mode.

Usage:
    python3 scripts/tracker_scores.py            # provisional, prints and writes JSON
    python3 scripts/tracker_scores.py --mode settled
    python3 scripts/tracker_scores.py --check    # validate only
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tracker"

OUTCOME_VALUES = {"for": 1, "against": -1, "mixed": 0}
COMMITMENT_VALUES = {"before", "not-before", "unclear"}
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


class RecordError(Exception):
    pass


def load():
    def t(name):
        with open(DATA / name, "rb") as f:
            return tomllib.load(f)

    judgements = t("judgements.toml")["judgement"]
    extra = DATA / "readings-gemini.toml"
    if extra.exists():
        by_id = {j["id"]: j for j in judgements}
        for r in t("readings-gemini.toml").get("reading", []):
            r = dict(r)
            jid = r.pop("judgement")
            by_id[jid].setdefault("reading", []).append(r)
    rul = DATA / "rulings.toml"
    if rul.exists():
        by_id = {j["id"]: j for j in judgements}
        for r in t("rulings.toml").get("ruling", []):
            by_id[r["judgement"]]["ruling"] = r
    return {
        "judgements": judgements,
        "sources": t("sources.toml")["source"],
        "theories": t("theories.toml"),
        "predictions": t("predictions.toml")["prediction"],
        "studies": t("studies.toml")["study"],
        "verify": t("verify.toml").get("entry", []),
    }


# ------------------------------------------------------------------ validation

def validate(d):
    errors = []
    err = errors.append

    def unique(items, kind):
        seen = set()
        for it in items:
            if it["id"] in seen:
                err(f"duplicate {kind} id {it['id']}")
            seen.add(it["id"])
        return seen

    source_ids = unique(d["sources"], "source")
    theories = d["theories"]["theory"]
    claims = d["theories"]["claim"]
    theory_ids = unique(theories, "theory")
    claim_ids = unique(claims, "claim")
    listed = set(d["theories"]["listed_theory"][0]["ids"])
    pred_ids = unique(d["predictions"], "prediction")
    study_ids = unique(d["studies"], "study")
    unique(d["judgements"], "judgement")

    for th in theories:
        if th["core_claims_from"] not in source_ids:
            err(f"theory {th['id']}: unknown source {th['core_claims_from']}")
        n = sum(1 for c in claims if c["theory"] == th["id"])
        if not 3 <= n <= 7:
            err(f"theory {th['id']} has {n} core claims; the rule is 3 to 7")
    for c in claims:
        if c["theory"] not in theory_ids:
            err(f"claim {c['id']}: unknown theory")
        th = next(t for t in theories if t["id"] == c["theory"])
        if c["source"] != th["core_claims_from"]:
            err(f"claim {c['id']}: quoted from {c['source']}, but the theory's claims must all come from {th['core_claims_from']}")
        if not c.get("quote"):
            err(f"claim {c['id']}: no quotation")

    claim_theory = {c["id"]: c["theory"] for c in claims}
    for p in d["predictions"]:
        if p["theory"] not in theory_ids:
            err(f"prediction {p['id']}: unknown theory")
        if claim_theory.get(p["core_claim"]) != p["theory"]:
            err(f"prediction {p['id']}: core claim {p['core_claim']} is not one of {p['theory']}'s")
        if p["stated_by"] not in ("proponent", "site"):
            err(f"prediction {p['id']}: stated_by must be proponent or site")
        fs = p["first_stated"]
        if fs["source"] not in source_ids:
            err(f"prediction {p['id']}: unknown source {fs['source']}")
        if not DATE_RE.match(fs["date"]):
            err(f"prediction {p['id']}: first_stated date {fs['date']!r} is not year-month-day")
        for a in p.get("also_stated", []) + ([p["first_public"]] if "first_public" in p else []):
            if a["source"] not in source_ids:
                err(f"prediction {p['id']}: unknown source {a['source']}")
        for s in p.get("separates_from", []):
            if s["theory"] not in listed:
                err(f"prediction {p['id']}: rival {s['theory']} is not on the ruled list")
            if s["source"] not in source_ids:
                err(f"prediction {p['id']}: unknown source {s['source']}")
        for k in ("statement", "test_for", "test_against"):
            if not p.get(k):
                err(f"prediction {p['id']}: missing {k}")

    for s in d["studies"]:
        if s["source"] not in source_ids:
            err(f"study {s['id']}: unknown source {s['source']}")
        fa = s["first_appeared"]
        if not DATE_RE.match(fa["date"]):
            err(f"study {s['id']}: first_appeared date {fa['date']!r} is not a date")
        for k in ("registered", "outside_camp", "rival_agreed", "replicated"):
            if k not in s.get("protections", {}):
                err(f"study {s['id']}: protection {k} not recorded")
        for c in s.get("camps", []):
            if c not in listed:
                err(f"study {s['id']}: camp {c} is not on the ruled list")
        for b in s.get("bears_on", []):
            if b not in pred_ids:
                err(f"study {s['id']}: bears_on unknown prediction {b}")

    for j in d["judgements"]:
        if j["prediction"] not in pred_ids:
            err(f"judgement {j['id']}: unknown prediction")
        if j["kind"] in ("outcome", "commitment") and j.get("study") not in study_ids:
            err(f"judgement {j['id']}: unknown study")
        if j["kind"] not in ("outcome", "commitment", "testability"):
            err(f"judgement {j['id']}: unknown kind {j['kind']}")
        for a in j.get("passages", []):
            if a["source"] not in source_ids:
                err(f"judgement {j['id']}: unknown source {a['source']}")
        if not j.get("reading"):
            err(f"judgement {j['id']}: no reading")
        for r in j.get("reading", []):
            for k in ("reader", "model", "date", "order", "reason"):
                if k not in r:
                    err(f"judgement {j['id']}: a reading has no {k}")
            if j["kind"] == "outcome" and r.get("verdict") not in OUTCOME_VALUES:
                err(f"judgement {j['id']}: outcome verdict must be for, against or mixed")
            if j["kind"] == "commitment" and r.get("verdict") not in COMMITMENT_VALUES:
                err(f"judgement {j['id']}: commitment verdict must be before, not-before or unclear")
            if j["kind"] == "testability":
                if not isinstance(r.get("could_fail"), bool) or not isinstance(r.get("separates"), bool):
                    err(f"judgement {j['id']}: testability needs could_fail and separates as true or false")
                for rv in r.get("separates_from", []):
                    if rv not in listed:
                        err(f"judgement {j['id']}: rival {rv} is not on the ruled list")
        if d["predictions_by_id"][j["prediction"]]["theory"] == "sh":
            orders = {r["order"] for r in j["reading"] if r["reader"] == "claude"}
            if orders and orders != {"second"}:
                err(f"judgement {j['id']}: on a Sentient Horizons row the Claude reading must be order = 'second' (ruling 7b)")

    # every outcome needs a commitment judgement for the same pair
    pairs = {(j["prediction"], j["study"]) for j in d["judgements"] if j["kind"] == "commitment"}
    for j in d["judgements"]:
        if j["kind"] == "outcome" and (j["prediction"], j["study"]) not in pairs:
            err(f"judgement {j['id']}: outcome with no commitment judgement for the same prediction and study")
    # every prediction needs a testability judgement
    tst = {j["prediction"] for j in d["judgements"] if j["kind"] == "testability"}
    for p in pred_ids - tst:
        err(f"prediction {p}: no testability judgement")

    if errors:
        raise RecordError("\n".join(errors))


# ------------------------------------------------------------------- settling

def settle(j, mode):
    """Return (reading_or_None, status).

    status: agreed | one-reader | disagreed | unread | ruled | open-for-john.
    A ruling (data/tracker/rulings.toml) is applied over the readings: a commitment
    ruling with no open part sets the verdict; one with an open part leaves the row for
    John; a testability ruling sets 'separates' for every reader, and the row settles if
    the readers also agree on 'could fail'.
    """
    rs = j.get("reading", [])
    ru = j.get("ruling")
    if ru and j["kind"] == "commitment":
        if ru.get("open_part"):
            return None, "open-for-john"
        return {"verdict": ru["verdict"], "reader": "ruling"}, "ruled"
    if ru and j["kind"] == "testability" and rs:
        rs = [dict(r, separates=ru["separates"], separates_from=ru.get("separates_from", [])) for r in rs]
        cf = {r["could_fail"] for r in rs}
        readers = {r["reader"] for r in rs}
        if len(cf) > 1:
            return None, "disagreed"
        if len(readers) < 2 and mode == "settled":
            return None, "one-reader"
        return rs[0], "ruled"
    if not rs:
        return None, "unread"
    if j["kind"] == "testability":
        keys = [(r["could_fail"], r["separates"]) for r in rs]
    else:
        keys = [r["verdict"] for r in rs]
    readers = {r["reader"] for r in rs}
    if len(set(keys)) > 1:
        return None, "disagreed"
    if len(readers) >= 2:
        return rs[0], "agreed"
    if mode == "settled":
        return None, "one-reader"
    return rs[0], "one-reader"


# ------------------------------------------------------------------- scoring

def compute(d, mode, flip_study=None, bar_reading="sharp"):
    preds = d["predictions_by_id"]
    studies = {s["id"]: s for s in d["studies"]}
    claims = d["theories"]["claim"]
    theories = d["theories"]["theory"]

    status = {}
    tst = {}
    for j in d["judgements"]:
        r, st = settle(j, mode)
        status[j["id"]] = st
        if j["kind"] == "testability":
            tst[j["prediction"]] = r  # None if unsettled
    com = {}
    for j in d["judgements"]:
        if j["kind"] == "commitment":
            r, _ = settle(j, mode)
            com[(j["prediction"], j["study"])] = r["verdict"] if r else None

    def could_fail(pid):
        r = tst.get(pid)
        return bool(r and r["could_fail"])

    def separates(pid):
        r = tst.get(pid)
        return bool(r and r["could_fail"] and r["separates"])

    def weight(study, theory):
        pr = study["protections"]
        w = 1
        w += 1 if pr["registered"]["value"] else 0
        w += 1 if (pr["outside_camp"]["value"] and theory not in study.get("camps", [])) else 0
        w += 1 if pr["rival_agreed"]["value"] else 0
        w += 1 if pr["replicated"]["value"] else 0
        return min(w, 5)

    # counted outcomes
    counted = []
    for j in d["judgements"]:
        if j["kind"] != "outcome":
            continue
        r, st = settle(j, mode)
        if r is None:
            continue
        p = preds[j["prediction"]]
        s = studies[j["study"]]
        if not s.get("opened", False):
            continue
        if com.get((p["id"], s["id"])) != "before":
            continue
        if not separates(p["id"]):
            continue  # a prediction every theory shares scores nothing
        val = OUTCOME_VALUES[r["verdict"]]
        if flip_study == s["id"]:
            val = -val
        w = weight(s, p["theory"])
        core = 2 if p.get("core_claim") else 1
        counted.append({
            "judgement": j["id"], "theory": p["theory"], "prediction": p["id"],
            "study": s["id"], "group": s["group"], "value": val,
            "weight": w, "multiplier": core, "status": st,
        })

    out = {}
    for th in theories:
        tid = th["id"]
        tclaims = [c for c in claims if c["theory"] == tid]
        tpreds = [p for p in preds.values() if p["theory"] == tid]

        # testability
        per_claim = {}
        for c in tclaims:
            best = 0.0
            for p in tpreds:
                if p["core_claim"] != c["id"] or not separates(p["id"]):
                    continue
                best = max(best, 1.0 if p["stated_by"] == "proponent" else 0.5)
            per_claim[c["id"]] = best
        testability = 100 * sum(per_claim.values()) / len(tclaims)

        # the bar
        failable = {c["id"]: any(p["core_claim"] == c["id"] and could_fail(p["id"]) for p in tpreds) for c in tclaims}
        sharp = {c["id"]: any(p["core_claim"] == c["id"] and separates(p["id"]) for p in tpreds) for c in tclaims}
        use = sharp if bar_reading == "sharp" else failable
        past_bar = sum(use.values()) > len(tclaims) / 2
        lacking = [cid for cid, ok in use.items() if not ok]

        # support
        mine = [c for c in counted if c["theory"] == tid]
        groups = sorted({c["group"] for c in mine})
        total_w = sum(c["weight"] * c["multiplier"] for c in mine)
        wsum = sum(c["value"] * c["weight"] * c["multiplier"] for c in mine)
        support = None
        if len(groups) >= 2 and total_w > 0:
            support = 100 * (wsum / total_w + 1) / 2

        # left to test
        dist = [p for p in tpreds if separates(p["id"])]
        tested = {c["prediction"] for c in mine}
        placeholders = [c["id"] for c in tclaims if not any(p["core_claim"] == c["id"] for p in dist)]
        n_total = len(dist) + len(placeholders)
        n_untested = sum(1 for p in dist if p["id"] not in tested) + len(placeholders)
        left = 100 * n_untested / n_total if n_total else None

        if past_bar and support is not None:
            group = "ranked"
        elif past_bar:
            group = "testable, too little tested to rank"
        else:
            group = "not yet defined sharply enough to rank"

        out[tid] = {
            "name": th["name"],
            "testability": round(testability, 1),
            "testability_by_claim": per_claim,
            "past_bar": past_bar,
            "claims_lacking_for_bar": lacking,
            "support": None if support is None else round(support, 1),
            "support_rests_on": {
                "counted_outcomes": len(mine), "studies": sorted({c["study"] for c in mine}),
                "groups": groups, "total_weight": total_w, "weighted_sum": wsum,
            },
            "left_to_test": None if left is None else round(left, 1),
            "left_to_test_counts": {"distinguishing_core_predictions": len(dist), "placeholders_for_claims_with_none": placeholders, "untested": n_untested, "total": n_total},
            "group": group,
            "leans_against": support is not None and support < 50,
        }
    return out, counted, status


def rank(d, mode, bar_reading="sharp"):
    base, counted, status = compute(d, mode, bar_reading=bar_reading)
    ranked = [t for t, v in base.items() if v["group"] == "ranked"]
    ranked.sort(key=lambda t: (-base[t]["support"], -base[t]["support_rests_on"]["total_weight"]))
    # rule 5: two theories share a rank unless their order survives reversing any one study
    studies_used = sorted({c["study"] for c in counted})
    def strictly_ahead(a, b, scores):
        sa, sb = scores[a]["support"], scores[b]["support"]
        if sa is None or sb is None:
            return False
        if sa != sb:
            return sa > sb
        return scores[a]["support_rests_on"]["total_weight"] > scores[b]["support_rests_on"]["total_weight"]
    shared = set()
    reversals = {}
    for a, b in zip(ranked, ranked[1:]):
        survives = strictly_ahead(a, b, base)
        breaker = None
        for sid in studies_used:
            flipped, _, _ = compute(d, mode, flip_study=sid, bar_reading=bar_reading)
            if not strictly_ahead(a, b, flipped):
                survives, breaker = False, sid
                break
        if not survives:
            shared.add((a, b))
            reversals[f"{a}|{b}"] = breaker
    ranks = {}
    r = 0
    for i, t in enumerate(ranked):
        if i == 0 or (ranked[i - 1], t) not in shared:
            r = i + 1
        ranks[t] = r
    second = sorted([t for t, v in base.items() if v["group"] == "testable, too little tested to rank"], key=lambda t: -base[t]["testability"])
    third = sorted([t for t, v in base.items() if v["group"] == "not yet defined sharply enough to rank"], key=lambda t: -base[t]["testability"])
    return base, counted, status, {"ranked": [{"theory": t, "rank": ranks[t]} for t in ranked], "shared_because_one_study_could_swap_them": reversals, "testable_too_little_tested": second, "not_yet_defined_sharply_enough": third}


def headline(d, mode):
    base, counted, _ = compute(d, mode)
    tot = sum(v["left_to_test_counts"]["distinguishing_core_predictions"] for v in base.values())
    tested = len({c["prediction"] for c in counted})
    return {"tested": tested, "distinguishing_predictions": tot, "share_tested": round(100 * tested / tot, 1) if tot else None,
            "note": "Provisional: the headline is ruling 3, still open. Computed as the kickoff proposal suggests (section 3): the share of the theories' sharp predictions tested at all."}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["provisional", "settled"], default="provisional")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-write", action="store_true")
    a = ap.parse_args(argv)
    d = load()
    d["predictions_by_id"] = {p["id"]: p for p in d["predictions"]}
    try:
        validate(d)
    except RecordError as e:
        print("The records break the layout's rules:\n" + str(e), file=sys.stderr)
        return 1
    open_verify = [v for v in d["verify"] if v.get("status", "open") == "open"]
    if a.check:
        print(f"records valid; {len(open_verify)} open verify entries")
        return 0

    base, counted, status, ranking = rank(d, a.mode)
    alt, _, _, alt_ranking = rank(d, a.mode, bar_reading="literal")
    result = {
        "mode": a.mode,
        "readers": sorted({r["reader"] for j in d["judgements"] for r in j.get("reading", [])}),
        "judgement_status": {k: sum(1 for v in status.values() if v == k) for k in ("agreed", "ruled", "one-reader", "disagreed", "open-for-john", "unread")},
        "unsettled": sorted(k for k, v in status.items() if v in ("one-reader", "disagreed", "open-for-john", "unread")),
        "theories": base,
        "ranking": ranking,
        "headline_provisional": headline(d, a.mode),
        "counted_outcomes": counted,
        "alternative_readings": {
            "bar_counts_any_prediction_that_could_fail": {
                "groups": {t: v["group"] for t, v in alt.items()},
                "ranking": alt_ranking,
                "why": "The first wording of ranking rule 2 did not say whether the prediction must separate the theory from a rival. John ruled on 2026-11-20 ('Yes, must separate') that it must; the main result follows the ruling. This is the superseded literal reading, kept for comparison.",
            },
        },
        "open_verify_entries": len(open_verify),
    }
    if not a.no_write:
        (DATA / "scores.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")

    print(f"Mode: {a.mode}. Readers so far: {', '.join(result['readers'])}. Judgements: {result['judgement_status']}")
    if result["judgement_status"]["one-reader"]:
        print(f"  {result['judgement_status']['one-reader']} judgement(s) have one reading only" + (" and are left out." if a.mode == "settled" else " and are used as read."))
    print()
    for tid, v in base.items():
        s = "too little tested to score" if v["support"] is None else f"{v['support']}"
        print(f"{v['name']}")
        print(f"  testability {v['testability']}   support {s}   left to test {v['left_to_test']}")
        sr = v["support_rests_on"]
        print(f"  support rests on {sr['counted_outcomes']} counted outcome(s) from {len(sr['studies'])} studies, {len(sr['groups'])} groups, total weight {sr['total_weight']}")
        print(f"  group: {v['group']}" + (" (the evidence so far leans against it)" if v["leans_against"] else ""))
        if v["claims_lacking_for_bar"]:
            print(f"  core claims with no prediction that could fail and separates it from a rival: {', '.join(v['claims_lacking_for_bar'])}")
    print()
    print("Ranking:")
    for r in ranking["ranked"]:
        print(f"  {r['rank']}. {base[r['theory']]['name']}")
    for k, by in ranking["shared_because_one_study_could_swap_them"].items():
        a_, b_ = k.split("|")
        print(f"  {a_} and {b_} share a rank: reversing {by} alone would swap or tie them")
    if ranking["testable_too_little_tested"]:
        print("Testable, too little tested to rank: " + ", ".join(base[t]["name"] for t in ranking["testable_too_little_tested"]))
    if ranking["not_yet_defined_sharply_enough"]:
        print("Not yet defined sharply enough to rank: " + ", ".join(base[t]["name"] for t in ranking["not_yet_defined_sharply_enough"]))
    print()
    h = result["headline_provisional"]
    print(f"Headline (provisional, ruling 3 open): {h['tested']} of {h['distinguishing_predictions']} distinguishing predictions tested ({h['share_tested']}%)")
    print()
    print("Superseded reading of ranking rule 2 (any prediction that could fail, not ruled):")
    for t, g in result["alternative_readings"]["bar_counts_any_prediction_that_could_fail"]["groups"].items():
        print(f"  {base[t]['name']}: {g}")
    print(f"\nOpen verify entries: {len(open_verify)} (promotion is blocked while any are open; rule 3.3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
