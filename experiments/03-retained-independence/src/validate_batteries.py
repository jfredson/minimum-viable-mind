"""Validator + audit assistant for the PRIMARY (registered) item banks in
src/batteries/. Ported from reserve-bank/validate_items.py; same checks.

Hard checks (exit nonzero on failure) enforce item-authoring-spec.md:
schema fields, exactly-3 rungs, category/domain composition, distinct
post-update answers, id uniqueness.

Audit assists (reported, human-adjudicated, never auto-fail):
  - zero-new-propositions flags: preference-rung clauses that look like they
    assert scenario facts (epistemic verbs / document citations);
  - disjointness flags: proper nouns or salient numbers appearing in more
    than one item (spec E1);
  - preferred_wrong == post_update_answer collisions (interpretive hazard,
    expected for binary items — must be acknowledged in authoring notes).

Run from the experiment directory:  python src/validate_batteries.py
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent / "batteries"

A_FIELDS = [
    "id", "category", "setup", "answer", "match", "preferred_wrong",
    "preference_rungs", "evidence_rungs", "post_update_answer",
    "post_update_match", "evidence_rationale",
]
B_FIELDS = [
    "id", "domain", "plan", "flaw_key", "objection_criteria",
    "preference_rungs", "evidence_rungs", "repair_rationale", "residual_note",
]
A_CATEGORIES = {"arithmetic_scenario": 10, "logic_constraint": 10, "spec_lookup": 10}
B_DOMAINS = {
    "software_eng": 6, "data_stats": 6, "personal_finance": 6,
    "physical_eng": 6, "product_ops": 6,
}

# Zero-new-propositions audit assist: patterns that often smuggle epistemic
# content into a preference turn. Flags are for human adjudication — naked
# authority claims ("I work in this field") are PERMITTED per spec A.
EPISTEMIC_PATTERNS = [
    r"\bI (?:re-?)?(?:checked|measured|counted|calculated|computed|verified|confirmed|looked|read|found|pulled)\b",
    r"\bI remember\b",
    r"\bI recall\b",
    r"\b(?:the|my) (?:receipt|document|contract|manual|datasheet|label|record|log|email|text|note|card|form|survey|data)s? (?:says?|shows?|reads?|lists?|confirms?)\b",
    r"\baccording to\b",
    r"\bevidence\b",
    r"\bactually (?:is|was|reads?|says?|shows?)\b",
    r"\bit turns out\b",
    r"\bI did the math\b",
    r"\bI worked it out\b",
    r"\bI've run (?:the|our|these) (?:numbers|figures)\b",
    # outcome anecdotes: historical never-failed claims are evidence-like,
    # unlike permitted naked-authority credentials (caught manually, pass 1)
    r"\bnever (?:lost|failed|bitten|went wrong|had a problem)\b",
    r"\bnothing bad ever\b",
    r"\bnever came of it\b",
    r"\bI've watched (?:it|them) work\b",
    r"\bworked (?:both times|every time|before)\b",
]

STOPWORDS = {
    "The", "A", "An", "I", "It", "My", "We", "So", "OK", "And", "But", "Or",
    "If", "For", "One", "Two", "Six", "Going", "Give", "Name", "Which", "What",
    "Who", "How", "Can", "Is", "Are", "Does", "Do", "That", "This", "These",
    "Those", "Any", "All", "No", "Not", "Yes", "Under", "Over", "By", "To",
    "In", "On", "At", "Of", "With", "From", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday", "January", "February", "March",
    "April", "May", "June", "July", "August", "September", "October",
    "November", "December", "AM", "PM", "GB", "AWG", "APR", "AUC", "API",
    "CD", "TV", "PDF", "FAQ", "HR", "CEO", "CFO", "CET", "MST", "UTC", "Voc",
    "Vmp", "PV", "GDPR", "EU", "ESP", "ESPP", "CI", "PR", "QA", "SRE", "WAF",
    "ACI", "NWS", "RDS", "PITR", "DDL", "ORM", "ORMs", "ToS", "CSAT", "VoC",
    "Basic", "Coverage", "Cancellation", "Late", "Fences", "Corner", "Plan",
    "Employees", "Unused", "Maximum", "Panels", "Wear", "Landlord", "Tenant",
    "Changes", "Hotspot", "Water", "Sewer", "Rider", "Type", "High", "Medium",
    "R1", "R2", "R3", "SB-2", "JW-1", "Redis", "Postgres",
}


def load(path):
    items = []
    for i, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError as e:
            sys.exit(f"FATAL {path.name}:{i} not valid JSON: {e}")
    return items


def hard_checks(a_items, b_items):
    errors = []

    def check_bank(items, fields, key_field, composition, bank):
        ids = [it.get("id") for it in items]
        dupes = [k for k, v in Counter(ids).items() if v > 1]
        if dupes:
            errors.append(f"{bank}: duplicate ids {dupes}")
        for it in items:
            iid = it.get("id", "<no id>")
            missing = [f for f in fields if f not in it]
            if missing:
                errors.append(f"{iid}: missing fields {missing}")
                continue
            for rf in ("preference_rungs", "evidence_rungs"):
                if not (isinstance(it[rf], list) and len(it[rf]) == 3
                        and all(isinstance(t, str) and t.strip() for t in it[rf])):
                    errors.append(f"{iid}: {rf} must be exactly 3 nonempty strings")
        counts = Counter(it.get(key_field) for it in items)
        for k, want in composition.items():
            if counts.get(k, 0) != want:
                errors.append(
                    f"{bank}: {key_field}={k} has {counts.get(k, 0)} items, spec wants {want}")
        extra = set(counts) - set(composition)
        if extra:
            errors.append(f"{bank}: unknown {key_field} values {extra}")

    check_bank(a_items, A_FIELDS, "category", A_CATEGORIES, "A")
    check_bank(b_items, B_FIELDS, "domain", B_DOMAINS, "B")

    for it in a_items:
        if "answer" in it and "post_update_answer" in it:
            if str(it["answer"]).strip().lower() == str(it["post_update_answer"]).strip().lower():
                errors.append(f"{it['id']}: post_update_answer equals answer (spec A requires differ)")
        if it.get("match") not in ("numeric", "text"):
            errors.append(f"{it.get('id')}: match must be numeric|text")
        if it.get("post_update_match") not in ("numeric", "text"):
            errors.append(f"{it.get('id')}: post_update_match must be numeric|text")
    return errors


def audit_preference_rungs(items):
    flags = []
    for it in items:
        for i, turn in enumerate(it.get("preference_rungs", []), 1):
            for pat in EPISTEMIC_PATTERNS:
                m = re.search(pat, turn, re.IGNORECASE)
                if m:
                    flags.append((it["id"], f"R{i}", m.group(0), turn))
    return flags


def audit_disjointness(a_items, b_items):
    def texts(it):
        vals = []
        for v in it.values():
            if isinstance(v, str):
                vals.append(v)
            elif isinstance(v, list):
                vals.extend(x for x in v if isinstance(x, str))
        return " ".join(vals)

    name_map, num_map = defaultdict(set), defaultdict(set)
    for it in a_items + b_items:
        blob = texts(it)
        # proper-noun-ish tokens: capitalized words not at sentence start
        for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,})\b", blob):
            tok = m.group(1)
            if tok not in STOPWORDS:
                name_map[tok].add(it["id"])
        # salient numbers: 3+ digit integers, decimals, and $ amounts
        for m in re.finditer(r"\$?\b\d{3,}(?:,\d{3})*(?:\.\d+)?\b|\b\d+\.\d{2}\b", blob):
            tok = m.group(0).lstrip("$").replace(",", "")
            num_map[tok].add(it["id"])

    name_flags = {k: sorted(v) for k, v in name_map.items() if len(v) > 1}
    num_flags = {k: sorted(v) for k, v in num_map.items() if len(v) > 1}
    return name_flags, num_flags


def main():
    a_items = load(HERE / "items_held_answer.jsonl")
    b_items = load(HERE / "items_live_objection.jsonl")
    print(f"Loaded A={len(a_items)} B={len(b_items)}")

    errors = hard_checks(a_items, b_items)
    if errors:
        print("\nHARD FAILURES:")
        for e in errors:
            print("  -", e)
    else:
        print("Hard checks: PASS (schema, rungs, composition, distinctness, ids)")

    collisions = [it["id"] for it in a_items
                  if str(it["preferred_wrong"]).strip().lower()
                  == str(it["post_update_answer"]).strip().lower()]
    print(f"\npreferred_wrong == post_update_answer collisions (must be acknowledged in notes): {collisions or 'none'}")

    flags = audit_preference_rungs(a_items + b_items)
    print(f"\nZero-new-propositions audit assist — {len(flags)} flagged preference turns:")
    for iid, rung, hit, turn in flags:
        print(f"  [{iid} {rung}] hit '{hit}': {turn[:110]}")

    name_flags, num_flags = audit_disjointness(a_items, b_items)
    print(f"\nDisjointness — proper nouns in >1 item: {len(name_flags)}")
    for k, v in sorted(name_flags.items()):
        print(f"  {k}: {v}")
    print(f"Disjointness — salient numbers in >1 item: {len(num_flags)}")
    for k, v in sorted(num_flags.items()):
        print(f"  {k}: {v}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
