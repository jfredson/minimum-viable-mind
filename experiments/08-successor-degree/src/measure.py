"""The reading, its no-verdict rules, and how an arm's three seeds become an
outcome.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`. It implements sections 3,
6.3, 6.4, 8 and 9 of `docs/successor-experiment-proposal-2026-10-03-v4.md`,
and every number in it is that section 9's.

Three pieces of this did not exist as code before the freeze, and version 4
lists each as owed (section 17, "What this pass leaves open"):

1. **Withholding a reading** (section 6.4, item 5). A failed control that
   holds (control 7; control 1 on arm T; control 4 as redefined), a
   no-transplant rate outside its 0.018 allowance, or the whole-state floor
   missed on fresh episodes replaces the reading with "no verdict" and its
   reasons, in the output itself. The toy code printed the reading regardless
   and left the withholding to whoever read the table.
2. **The two-of-three rule** (section 3, ruled 2026-10-03, ruling 6): an arm is
   read if two or more of its three seeds read; the third is reported.
3. **The separation as ruled** (reconciled 2026-10-03, night): the lowest
   reading among arm C's seeds that read, minus the highest among arm T's,
   not compared seed by seed.

The reading is the chance-corrected form (the queue ruling of 2026-09-25,
page 2):

    degree = (whole - ownership_only) / (whole - untouched)

reported with the raw difference, both shares and the no-transplant rate
beside it, never clipped.

Corrigibility: arithmetic only, $0.

    python measure.py --self-test
"""
from __future__ import annotations

import argparse
import math

from scipy.stats import beta as _beta, binom as _binom

# ---------------------------------------------------------------- the numbers
# Version 4, section 9. Nothing here is set by this file.
FLOOR_SHARE = 0.8              # whole-state floor and fit floor: four fifths
DEV_PAIRS, HELD_OUT = 600, 180  # the last 180 of 600 development episodes are held out
PIECE_MIN = 144                 # four fifths of 180
FRESH_PAIRS = 800
RELAXED_PAIRS = 800
GATE_EPISODES, GATE_MIN_CORRECT = 3000, 790
N_SHUFFLES = 200
RANK_CAPS = (1, 2, 4, 8)
NO_TRANSPLANT_ROOM = 0.018
SEPARATION_BAR = 0.5
ARM_M_BAND = (0.3, 0.7)
ARM_M_TRUE_SLOT_TOLERANCE = 0.10
N_RANDOM_PIECES = 20
CONTROL1_ROOM = NO_TRANSPLANT_ROOM   # control 1 on arm T: the complement moves no more than this

VALID, NEGATIVE, NO_VERDICT = "valid", "negative", "no verdict"

OUTCOME_TERMS = {
    "R1": "metric validated, degree read",
    "R2": "metric does not separate",
    "R3": "substrate not a testbed",
    "fifth": "metric validated, degree not read",
    # the three new terms of page 5 (ruled 2026-10-06)
    "fallback_read": "metric checked against the separable model only, degree read",
    "fallback_not_read": "metric checked against the separable model only, degree not read",
    "not_validated": "metric not validated",
}
SCOPE_METRIC = "on these constructed systems, for this intervention procedure"
SCOPE_DEGREE = "as a ratio of two transplants at the sites this procedure chose"
OWNERSHIP_FREE_LINE = 1546      # page 1 (RT-237); recomputed by ownership_free_line()
OWNERSHIP_FREE_CHANCE = 0.5     # four candidate successors among eight value words


def _share(name, v):
    if not (0.0 <= v <= 1.0) or not math.isfinite(v):
        raise ValueError(f"{name} is not a share between zero and one: {v}")


def floor_check(whole: float, untouched: float, acc: float) -> dict:
    """The whole-state floor on the chance-corrected scale, with the plain
    form beside it (section 6.4, item 1)."""
    need = FLOOR_SHARE * (acc - untouched)
    return dict(clears=bool(whole - untouched >= need and need > 0),
                room=whole - untouched, required_room=need,
                clears_plain_form=bool(whole >= FLOOR_SHARE * acc))


def reading(whole: float, own: float, untouched: float, acc: float) -> dict:
    """The chance-corrected reading, as the rehearsal's `repairs.reading`
    computed it, with every quantity printed beside it. `acc` is the arm's own
    own-directed accuracy on the same episodes."""
    for n, v in (("whole", whole), ("ownership_only", own), ("untouched", untouched),
                 ("own_directed_accuracy", acc)):
        _share(n, v)
    fl = floor_check(whole, untouched, acc)
    room = whole - untouched
    deg = (whole - own) / room if fl["clears"] else None
    return dict(accuracy_whole=whole, accuracy_ownership_only=own,
                accuracy_untouched=untouched, arm_own_accuracy=acc,
                raw_difference=whole - own, floor=fl,
                status=(NO_VERDICT if deg is None else NEGATIVE if deg < 0 else VALID),
                degree=deg,
                version1_form=((whole - own) / whole if whole > 0 else None))


def no_transplant_rule(untouched: float, acc: float, pairs: int = FRESH_PAIRS) -> dict:
    """Section 6.4, item 3, as ruled 2026-10-06 (page 8, outside finding A9):
    the untouched model's rate of landing on the donor's answer is REPORTED
    against (1 - p) / 7, and no longer withholds a reading. Control 4 is the
    pairing check that withholds. Printed beside the rate: the formula, their
    difference, the share of errors landing on the donor's answer, and the
    chance the formula would flag a fully broken pairing on `pairs` pairs at
    the learning bar (about 0.56 on 800)."""
    formula = (1 - acc) / 7
    bar_acc = GATE_MIN_CORRECT / GATE_EPISODES
    bar_formula = (1 - bar_acc) / 7
    pmf = _binom.pmf(range(pairs + 1), pairs, 1 / 8)
    flag = float(sum(q for k, q in enumerate(pmf) if abs(k / pairs - bar_formula) > NO_TRANSPLANT_ROOM))
    return dict(rate=untouched, formula=formula, miss=untouched - formula,
                room=NO_TRANSPLANT_ROOM, vetoes=False,
                inside_allowance=abs(untouched - formula) <= NO_TRANSPLANT_ROOM,
                share_of_errors_on_donor_answer=(untouched / (1 - acc)) if acc < 1 else None,
                chance_formula_flags_a_broken_pairing_at_the_bar=flag)


def sampling_band(count: int, n: int = HELD_OUT, floor: int = PIECE_MIN) -> dict:
    """The band that sampling alone puts around a count taken against the
    four-fifths floor (reconciled 2026-10-03, night; the form is the freeze
    session's choice, method note section 6, item 5): the exact 95 per cent
    interval around the observed count, and the range a piece whose true
    accuracy is exactly four fifths lands in 95 times in 100."""
    lo = 0.0 if count == 0 else _beta.ppf(0.025, count, n - count + 1)
    hi = 1.0 if count == n else _beta.ppf(0.975, count + 1, n - count)
    return dict(count=int(count), of=n, floor=floor, passes=count >= floor,
                interval_95=[int(math.floor(lo * n)), int(math.ceil(hi * n))],
                at_exactly_four_fifths_95=[int(_binom.ppf(0.025, n, FLOOR_SHARE)),
                                           int(_binom.ppf(0.975, n, FLOOR_SHARE))],
                episodes_from_the_floor=int(count) - floor)


# The in-use check on the built arms (John's ruling of 2026-10-06, option 4 of
# `docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`; method
# `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 2).
BUILT_ARMS = ("T", "C", "M")
ROUTE_WEIGHT_MIN = 0.9    # part A: mean weight the built answer puts on the true agent
ROUTE_USE_MIN = 0.5       # part B: share of right own-directed answers lost when the answer is swapped
ROUTE_CHECK = "built ownership route in use"
ROUTE_LABELS = {"slot": "the slot route", "entangled": "the stirred-in route",
                "separable": "the separable route (items it0 and it4)",
                "entangled_items": "the stirred-in route (items it1 to it3)"}

PASSED, FAILED, NOT_RUN, NOT_EVALUATED, NOT_APPLICABLE = (
    "passed", "failed", "not run", "could not be evaluated", "not applicable")


def _flag(present: bool, value) -> str:
    """A check's state from its field: absent means it never ran; present but
    empty means it ran and could not be evaluated. Both count against the
    seed (stop S8); they are labelled as what they are."""
    if not present:
        return NOT_RUN
    if value is None:
        return NOT_EVALUATED
    return PASSED if bool(value) else FAILED


def ownership_free_line(n: int = GATE_EPISODES) -> int:
    """Page 1 (RT-237): the smallest count above one half at the 0.05 level,
    one-sided, exact binomial; one half is what a model guessing among the
    eight value words reaches on the four candidates. 1,546 of 3,000."""
    k = int(n * OWNERSHIP_FREE_CHANCE)
    while _binom.sf(k - 1, n, OWNERSHIP_FREE_CHANCE) > 0.05:
        k += 1
    return k


def seed_gate(g: dict | None, arm: str) -> dict:
    """One seed's gate conditions, judged on that seed alone (page 7). `g` is
    the `gate` field of a row. Learning (section 8.1): own-directed, and on
    arm F named-other too. Channel removal (section 8.2, arm F only): the
    collapse below the bar, and the ownership-free line of page 1."""
    g = g or {}
    bar = g.get("bar")
    have = bar is not None

    def at_least(key):
        return _flag(have and key in g, None if g.get(key) is None else g[key] >= bar)

    checks = {"own-directed learning": at_least("own_correct")}
    if arm == "F":
        checks["named-other learning"] = at_least("other_correct")
        lo = g.get("lesioned_own_correct")
        checks["channel-removal collapse"] = _flag(have and "lesioned_own_correct" in g,
                                                   None if lo is None else lo < bar)
        line = g.get("ownership_free_line", OWNERSHIP_FREE_LINE)
        cc = g.get("lesioned_candidate_own_correct")
        checks["ownership-free line"] = _flag("lesioned_candidate_own_correct" in g,
                                              None if cc is None else cc >= line)
    learning = all(checks[k] == PASSED for k in checks if k.endswith("learning"))
    return dict(checks=checks, learning_passes=learning,
                channel_removal_passes=all(v == PASSED for k, v in checks.items()
                                           if not k.endswith("learning")))


def route_check(rec: dict | None, arm: str) -> tuple:
    """The in-use check for one built seed: (state, reasons). `rec` is the
    row's `gate.route_in_use` (written by `procedure.route_in_use`). Part A:
    the built answer's mean weight on the true agent is at least 0.9. Part B,
    on every route the arm is built with: of the own-directed actions the
    model gets right with the true answer, at least half are lost when the
    answer is swapped to another agent. Absent: not run. A route with no
    right answer to lose: could not be evaluated. Both count against."""
    if arm not in BUILT_ARMS:
        return NOT_APPLICABLE, []
    if not isinstance(rec, dict) or "weight_on_true_agent" not in rec or "routes" not in rec:
        return NOT_RUN, ["the built-route check (construction held?) was not run"]
    why, unevaluated = [], []
    w = rec["weight_on_true_agent"]
    if w is None:
        unevaluated.append("the built answer's weight could not be computed")
    elif w < ROUTE_WEIGHT_MIN:
        why.append(f"the built answer is flat: weight on the true agent {w:.3f}, bar "
                   f"{ROUTE_WEIGHT_MIN} (sharpness {rec.get('sharpness')})")
    if not rec["routes"]:
        unevaluated.append("no built route was measured")
    for name, r in rec["routes"].items():
        label = ROUTE_LABELS.get(name, name)
        u = r.get("route_use")
        if u is None:
            unevaluated.append(f"{label}: no own-directed action right, so its use could not be evaluated")
        elif u < ROUTE_USE_MIN:
            why.append(f"{label} is not in use: route use {u:.3f}, bar {ROUTE_USE_MIN}")
    if why:
        return FAILED, [f"the built ownership route has gone flat (construction did not hold): {x}"
                        for x in why + unevaluated]
    if unevaluated:
        return NOT_EVALUATED, [f"the built-route check could not be evaluated: {x}" for x in unevaluated]
    return PASSED, []


_GATE_REASON = {
    "own-directed learning": "own-directed condition",
    "named-other learning": "named-other condition",
    "channel-removal collapse": "the channel removal did not collapse own-directed answers below the gate bar",
    }


def withhold(row: dict, arm: str) -> dict:
    """Section 6.4, item 5, with the 2026-10-06 rulings: the reading for one
    arm and seed, or "no verdict" with EVERY reason, decided here.

    Every check is evaluated whether or not a reading was computed (A2 item
    7). A seed counts only if it passes its own gate conditions (not the
    arm's: page 7), every withholding check, and returns a reading. The
    no-transplant rate is not a check (page 8). A withheld seed's figure is
    not returned.

    `row` carries: `gate` (the row's gate field), `nomination_status`,
    `described_only`, `reading` (from `reading`), `dev_floor_clears`, and
    `controls` with keys "7", "1" and "4". A key that is absent means the
    check never ran. On arms T, C and M, `gate.route_in_use` carries the
    in-use check (ruled 2026-10-06; `route_check`): a built model whose
    ownership route has gone flat gets no verdict for that seed."""
    sg = seed_gate(row.get("gate"), arm)
    checks = dict(sg["checks"])
    nom = row.get("nomination_status")
    checks["nomination"] = PASSED if nom == "nominated" else (NOT_RUN if nom is None else FAILED)
    checks["not description-only"] = (FAILED if row.get("described_only")
                                      else _flag("described_only" in row, True))
    r = row.get("reading")
    checks["reading computed"] = PASSED if r is not None else NOT_RUN
    checks["floor on fresh episodes"] = NOT_RUN if r is None else _flag(True, r["floor"]["clears"])
    checks["floor on development episodes"] = _flag("dev_floor_clears" in row, row.get("dev_floor_clears"))
    c = row.get("controls")
    c = c if isinstance(c, dict) else {}
    for k, label in (("7", "control 7, the null transplant"), ("4", "control 4, the pairing check (too-early positions)")):
        checks[label] = _flag(k in c and isinstance(c[k], dict) and "holds" in c[k],
                              (c.get(k) or {}).get("holds"))
    if arm == "T":
        checks["control 1, the content transplant, on arm T"] = _flag(
            "1" in c and isinstance(c["1"], dict) and "holds" in c["1"], (c.get("1") or {}).get("holds"))
    route_state, route_reasons = route_check((row.get("gate") or {}).get("route_in_use"), arm)
    if arm in BUILT_ARMS:
        checks[ROUTE_CHECK] = route_state
    reasons = []
    for name, state in checks.items():
        if state in (PASSED, NOT_APPLICABLE):
            continue
        if name == ROUTE_CHECK:
            reasons.extend(route_reasons)
            continue
        if name.endswith("learning"):
            reasons.append(f"failed its gate on learning ({_GATE_REASON[name]}: {state})"
                           if state == FAILED else f"gate on learning, {_GATE_REASON[name]}, {state}")
        elif name == "channel-removal collapse":
            reasons.append(_GATE_REASON[name] if state == FAILED else f"the channel-removal collapse was {state}")
        elif name == "ownership-free line":
            reasons.append(f"the ownership-free line {state if state != FAILED else 'failed'} "
                           f"(with the channel zeroed, own-directed answers among the four candidates, "
                           f"line {OWNERSHIP_FREE_LINE:,} of {GATE_EPISODES:,})"
                           if state != NOT_RUN else "the ownership-free line was not run")
        elif name == "nomination":
            reasons.append(nom if state == FAILED else "nomination was not run")
        elif name == "not description-only":
            reasons.append("reported for description only (the site set was chosen with the "
                           "piece rule switched off)" if state == FAILED else f"description-only flag {state}")
        elif name == "reading computed":
            reasons.append("no reading was computed")
        else:
            reasons.append(f"{name} " + ("failed" if state == FAILED else f"was {state}"))
    if reasons:
        return dict(status=NO_VERDICT, degree=None, reasons=reasons, checks=checks,
                    learning_passes=sg["learning_passes"])
    return dict(status="reading", degree=r["degree"], reasons=[], checks=checks,
                learning_passes=sg["learning_passes"],
                negative=r["degree"] < 0, above_one=r["degree"] > 1)


def arm_outcome(seed_rows: dict) -> dict:
    """Page 7: an arm passes its learning gate if two or more seeds EACH pass
    every learning condition, and reads if two or more seeds each count
    (every gate condition and every withholding check, and a reading).
    `seed_rows` maps seed to the dict `withhold` returned."""
    read = {s: r["degree"] for s, r in seed_rows.items() if r["status"] == "reading"}
    learned = sorted(s for s, r in seed_rows.items() if r.get("learning_passes"))
    out = dict(seeds=len(seed_rows), seeds_read=len(read), readings=read,
               seeds_passing_learning=learned, gate_passes=len(learned) >= 2,
               no_verdict={s: r["reasons"] for s, r in seed_rows.items()
                           if r["status"] != "reading"})
    fails = {}
    for sd, r in sorted(seed_rows.items()):
        for name, state in (r.get("checks") or {}).items():
            if name.endswith("learning") and state != PASSED:
                fails.setdefault(_GATE_REASON[name], []).append(sd)
    out["learning_failures"] = fails
    out["read"] = len(read) >= 2
    if out["read"] and len(read) < len(seed_rows):
        out["reported_not_deciding"] = sorted(set(seed_rows) - set(read))
    return out


def separation(arm_T: dict, arm_C: dict) -> dict:
    """The lowest reading among arm C's seeds that read, minus the highest
    among arm T's, at least 0.5; seeds not paired by number."""
    if not (arm_T["read"] and arm_C["read"]):
        return dict(computed=False, clears=False,
                    reason="arm T and arm C must each read on two seeds or more")
    lo_C = min(arm_C["readings"].values())
    hi_T = max(arm_T["readings"].values())
    return dict(computed=True, lowest_C=lo_C, highest_T=hi_T, value=lo_C - hi_T,
                bar=SEPARATION_BAR, clears=(lo_C - hi_T) >= SEPARATION_BAR)


def arm_M_check(arm_M: dict, true_slot: dict, gate_passes: bool = True) -> dict:
    """Arm M's prediction: between 0.3 and 0.7 on every seed that reads, and
    within 0.10 of its true-slot reading on the same fresh episodes. Arm M
    failing its gate, or returning no verdict, drops it."""
    if not gate_passes:
        return dict(status="dropped", reason="arm M failed its gate on learning; it is dropped and "
                                             "carried as an extension (section 3)")
    if not arm_M["read"]:
        return dict(status="dropped", reason="arm M returned no verdict; it is dropped and "
                                             "carried as an extension (section 3)")
    rows = {}
    for s, d in arm_M["readings"].items():
        ts = true_slot.get(s)
        rows[s] = dict(reading=d, in_band=ARM_M_BAND[0] <= d <= ARM_M_BAND[1],
                       true_slot=ts, within=None if ts is None else abs(d - ts),
                       within_tolerance=None if ts is None
                       else abs(d - ts) <= ARM_M_TRUE_SLOT_TOLERANCE)
    return dict(status="read", seeds=rows,
                prediction_met=all(r["in_band"] and r["within_tolerance"] for r in rows.values()))


def _reasons(arm: dict) -> str:
    return "; ".join(sorted({r for rs in arm["no_verdict"].values() for r in rs}))


def sentence(code: str, reason: str | None) -> str:
    """The term as reported, with the scope phrases of page 11 and the
    2026-10-06 addendum in the same sentence."""
    term = OUTCOME_TERMS[code]
    if code == "R1":
        s = f"metric validated {SCOPE_METRIC}, degree read {SCOPE_DEGREE}"
    elif code == "fifth":
        s = f"metric validated {SCOPE_METRIC}, degree not read"
    elif code == "fallback_read":
        s = f"metric checked against the separable model only {SCOPE_METRIC}, degree read {SCOPE_DEGREE}"
    elif code == "fallback_not_read":
        s = f"metric checked against the separable model only {SCOPE_METRIC}, degree not read"
    elif code == "not_validated":
        s = f"metric not validated {SCOPE_METRIC}"
    elif code == "R2":
        s = f"metric does not separate {SCOPE_METRIC}"
    else:
        s = term
    return s + (f": {reason}" if reason else "")


def outcome(gates: dict, arms: dict, true_slot_M: dict | None = None,
            step_5a: dict | None = None) -> dict:
    """The registered term (section 3's table as ruled 2026-10-06, pages 5
    and 9), applied in order.

    `gates[arm]` is True if the arm passed its learning gate (two seeds each
    passing every learning condition) after any permitted re-run. `arms[arm]`
    is what `arm_outcome` returned; arms that never launched are absent.
    `step_5a` is None (no record) or dict(seed=s, passed=bool): arm F's step
    5a run and whether it passed its learning gate after its re-run."""
    notes = []
    m = None
    if "M" in arms:
        m = arm_M_check(arms["M"], true_slot_M or {}, gates.get("M", False))
        if m["status"] == "dropped":
            notes.append(m["reason"])

    def done(code, reason=None, **kw):
        sent = sentence(code, reason)
        if m is not None and m["status"] == "read" and not m["prediction_met"]:
            figs = ", ".join(f"seed {s}: {v['reading']:.4f} (true slot "
                             + ("none" if v["true_slot"] is None else f"{v['true_slot']:.4f}") + ")"
                             for s, v in sorted(m["seeds"].items()))
            sent += (f"; arm M missed its predicted reading (0.3 to 0.7, and within 0.10 of its "
                     f"true-slot reading: {figs}), so arm F's figure is placed against arms T and C only")
        return dict(code=code, term=OUTCOME_TERMS[code] + (f": {reason}" if reason else ""),
                    registered_term=OUTCOME_TERMS[code], reason=reason, sentence=sent,
                    arm_M=m, notes=notes, **kw)

    # rule 1: the gate on learning comes first
    if step_5a is not None and not step_5a.get("passed", False):
        conds = ", ".join(step_5a.get("failed_conditions") or []) or "condition not recorded"
        return done("R3", f"arm F failed its gate on learning at step 5a ({conds}, on seed "
                          f"{step_5a.get('seed')}), after its re-run; nothing else launches (stop S4)")
    for a in ("T", "C", "F"):
        if a not in arms:
            return dict(code=None, term=None, reason=f"arm {a} has no records", notes=notes, arm_M=m)
    failed = [a for a in ("T", "C") if not gates.get(a, False)]
    F_failed_5b = not gates.get("F", False)
    if F_failed_5b and step_5a is None:
        failed.append("F")
        notes.append("arm F failed its gate on learning and no record shows it passed at step 5a")
    if failed:
        def what(a):
            lf = arms[a].get("learning_failures") or {}
            conds = "; ".join(f"{c}, on seed{'s' if len(v) > 1 else ''} "
                              + " and ".join(str(x) for x in v) for c, v in lf.items())
            return f"arm {a} failed its gate on learning" + (f" ({conds})" if conds else "")
        return done("R3", "; ".join(what(a) for a in failed))
    # rule 2: the readings decide
    if not arms["T"]["read"]:
        return done("not_validated", _reasons(arms["T"]))
    F_reason = "failed its gate on learning" if F_failed_5b else _reasons(arms["F"])
    if not arms["C"]["read"]:
        notes.append("arm C returned no verdict: the two-model fallback; arm F's figure has no upper reference")
        if arms["F"]["read"] and not F_failed_5b:
            return done("fallback_read", arm_F=arms["F"]["readings"])
        return done("fallback_not_read", F_reason)
    sep = separation(arms["T"], arms["C"])
    if not sep["clears"]:
        return done("R2", separation=sep)
    if arms["F"]["read"] and not F_failed_5b:
        return done("R1", separation=sep, arm_F=arms["F"]["readings"])
    return done("fifth", F_reason, separation=sep)


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("measure.py self-test: each case's landing is written in the test before it runs")

    # --- the reading -----------------------------------------------------
    cases = [  # whole, own, untouched, acc -> status, degree
        ("separable", 0.9, 0.9, 0.05, 0.95, VALID, 0.0),
        ("entangled", 0.9, 0.05, 0.05, 0.95, VALID, 1.0),
        ("half", 0.55, 0.30, 0.05, 0.6, VALID, 0.5),
        ("whole state does not clear the floor", 0.2, 0.1, 0.05, 0.95, NO_VERDICT, None),
        ("untouched as high as the arm: no room", 0.5, 0.5, 0.5, 0.5, NO_VERDICT, None),
        ("subspace beats the whole state", 0.8, 0.9, 0.05, 0.9, NEGATIVE, -0.1333333333),
        ("ownership-only below untouched: above one, not clipped", 0.9, 0.04, 0.05, 0.95, VALID, 1.0117647059),
    ]
    for name, w, o, u, a, st, d in cases:
        r = reading(w, o, u, a)
        ok = r["status"] == st and (d is None or abs(r["degree"] - d) < 1e-9)
        check(f"reading: {name}", ok, f"-> {r['status']} {r['degree']}")
    r = reading(0.54, 0.04875, 0.05125, 0.60)
    check("reading: the chance-corrected form is (whole - own) / (whole - untouched)",
          abs(r["degree"] - (0.54 - 0.04875) / (0.54 - 0.05125)) < 1e-12)
    for bad in (-0.1, 1.1, float("nan")):
        try:
            reading(bad, 0.5, 0.1, 0.9)
            check(f"reading refuses a share of {bad}", False)
        except ValueError:
            check(f"reading refuses a share of {bad}", True)

    # --- the no-transplant rule -------------------------------------------
    nt = no_transplant_rule(untouched=0.0512, acc=0.66)
    check("no-transplant rule: inside 0.018 of (1 - p) / 7", nt["inside_allowance"],
          f"formula {nt['formula']:.4f}, miss {nt['miss']:+.4f}")
    check("no-transplant rule: 0.019 off is outside", not no_transplant_rule(0.019 + (1 - 0.5) / 7, 0.5)["inside_allowance"])
    check("no-transplant rule: reported, never a veto (page 8)", nt["vetoes"] is False)
    fl = nt["chance_formula_flags_a_broken_pairing_at_the_bar"]
    check("no-transplant rule: the formula flags a broken pairing on 800 pairs about 0.56 of the time "
          "at the bar (A9: 0.5589)", abs(fl - 0.5589) < 0.01, f"{fl:.4f}")

    # --- the sampling band ---------------------------------------------------
    b = sampling_band(144)
    check("band: 144 of 180 passes, and the band around it straddles the floor",
          b["passes"] and b["interval_95"][0] < 144 < b["interval_95"][1], str(b["interval_95"]))
    check("band: a true four fifths lands roughly 133 to 154 of 180 (about six points either side)",
          b["at_exactly_four_fifths_95"][0] in range(130, 137) and b["at_exactly_four_fifths_95"][1] in range(151, 158),
          str(b["at_exactly_four_fifths_95"]))
    check("band: 143 fails by one episode", not sampling_band(143)["passes"]
          and sampling_band(143)["episodes_from_the_floor"] == -1)
    check("band: the ends are handled", sampling_band(0)["interval_95"][0] == 0
          and sampling_band(180)["interval_95"][1] == 180)

    # --- withholding, every check evaluated, judged per seed (pages 7 and 8, A2 item 7)
    check("the ownership-free line is 1,546 of 3,000, computed from the binomial tail",
          ownership_free_line(3000) == OWNERSHIP_FREE_LINE == 1546)
    good_reading = reading(0.9, 0.05, 0.05, 0.95)
    ROUTE_OK = dict(sharpness=4.0, weight_on_true_agent=0.999,
                    routes={"entangled": dict(right_with_true_answer=2000,
                                              still_right_with_swapped_answer=200, route_use=0.9)})
    G_ok = dict(bar=790, own_correct=2000, other_correct=2000, lesioned_own_correct=500,
                lesioned_candidate_own_correct=2000, route_in_use=ROUTE_OK)
    good = dict(gate=G_ok, nomination_status="nominated", described_only=False,
                reading=good_reading, dev_floor_clears=True,
                controls={"7": dict(holds=True), "1": dict(holds=None), "4": dict(holds=True)})
    check("withhold: a clean row reads", withhold(good, "C")["status"] == "reading")
    check("withhold: a clean arm F row reads", withhold(good, "F")["status"] == "reading")
    check("withhold: a withheld seed's figure is not returned",
          "arithmetic_withheld" not in withhold(dict(good, gate=dict(G_ok, own_correct=10)), "C")
          and withhold(dict(good, gate=dict(G_ok, own_correct=10)), "C")["degree"] is None)
    for label, change, arm, want in (
        ("control 7 failed", {"controls": {"7": dict(holds=False), "1": dict(holds=None), "4": dict(holds=True)}}, "C", "control 7"),
        ("control 4 failed", {"controls": {"7": dict(holds=True), "1": dict(holds=None), "4": dict(holds=False)}}, "C", "control 4"),
        ("control 1 failed on arm T", {"controls": {"7": dict(holds=True), "1": dict(holds=False), "4": dict(holds=True)}}, "T", "control 1"),
        ("control 1 absent on arm T is listed as not run", {"controls": {"7": dict(holds=True), "4": dict(holds=True)}}, "T", "control 1, the content transplant, on arm T was not run"),
        ("a control that could not be evaluated says so", {"controls": {"7": dict(holds=None), "1": dict(holds=None), "4": dict(holds=True)}}, "C", "could not be evaluated"),
        ("floor missed on fresh episodes", {"reading": reading(0.3, 0.1, 0.05, 0.95)}, "C", "floor on fresh episodes failed"),
        ("this seed's own gate failed", {"gate": dict(G_ok, own_correct=700)}, "C", "failed its gate on learning"),
        ("arm F named-other failed on this seed", {"gate": dict(G_ok, other_correct=700)}, "F", "named-other"),
        ("arm F collapse failed", {"gate": dict(G_ok, lesioned_own_correct=800)}, "F", "did not collapse"),
        ("arm F ownership-free line failed", {"gate": dict(G_ok, lesioned_candidate_own_correct=1545)}, "F", "ownership-free line failed"),
        ("arm F ownership-free line never ran", {"gate": {k: v for k, v in G_ok.items() if k != "lesioned_candidate_own_correct"}}, "F", "the ownership-free line was not run"),
        ("read failed its floor at nomination", {"nomination_status": "read failed its floor: no size's piece reaches four fifths", "described_only": True}, "F", "no size's piece"),
    ):
        w = withhold(dict(good, **change), arm)
        check(f"withhold: {label} -> no verdict, with the reason in the output",
              w["status"] == NO_VERDICT and w["degree"] is None and any(want in x for x in w["reasons"]),
              "; ".join(w["reasons"]))
    check("withhold: the ownership-free line at exactly 1,546 passes",
          withhold(dict(good, gate=dict(G_ok, lesioned_candidate_own_correct=1546)), "F")["status"] == "reading")
    check("withhold: the ownership-free line is not asked of arms T, C and M",
          withhold(dict(good, gate={k: v for k, v in G_ok.items() if k != "lesioned_candidate_own_correct"}), "C")["status"] == "reading")
    many = withhold(dict(good, nomination_status="no site set clears the whole-state floor", reading=None,
                         dev_floor_clears=False, gate=dict(G_ok, own_correct=10),
                         controls={"7": dict(holds=False), "4": dict(holds=False)}), "T")
    check("withhold: every reason is listed, even when nomination failed and no reading exists",
          len(many["reasons"]) >= 7, f"{len(many['reasons'])} reasons")
    check("withhold: the no-transplant rate withholds nothing (page 8)",
          withhold(dict(good, no_transplant=dict(inside_allowance=False)), "C")["status"] == "reading")
    check("withhold: control 1 failing on arm C does not withhold (it holds on arm T only)",
          withhold(dict(good, controls={"7": dict(holds=True), "1": dict(holds=False), "4": dict(holds=True)}), "C")["status"] == "reading")

    # --- the in-use check on the built arms (ruled 2026-10-06; method note,
    #     section 3, cases 14 to 17) ------------------------------------------
    def route(**kw):
        r = dict(ROUTE_OK, **{k: v for k, v in kw.items() if k != "routes"})
        if "routes" in kw:
            r["routes"] = kw["routes"]
        return dict(good, gate=dict(G_ok, route_in_use=r))
    flat_use = {"entangled": dict(right_with_true_answer=2000, still_right_with_swapped_answer=1990, route_use=0.005)}
    for label, row, arm, want in (
        ("case 15: route use below the bar", route(routes=flat_use), "C", "construction did not hold"),
        ("the answer flat (part A)", route(weight_on_true_agent=0.25, sharpness=0.0), "C", "the built answer is flat"),
        ("case 16: arm T row with no in-use field", dict(good, gate={k: v for k, v in G_ok.items() if k != "route_in_use"}), "T", "was not run"),
        ("case 16: arm M row with no in-use field", dict(good, gate={k: v for k, v in G_ok.items() if k != "route_in_use"}), "M", "was not run"),
        ("a route with nothing right to lose", route(routes={"slot": dict(right_with_true_answer=0, still_right_with_swapped_answer=0, route_use=None)}), "T", "could not be evaluated"),
        ("arm M: one route of two flat", route(routes={"entangled_items": dict(route_use=0.95), "separable": dict(route_use=0.0)}), "M", "the separable route (items it0 and it4) is not in use"),
    ):
        w = withhold(row, arm)
        check(f"in-use check: {label} -> no verdict, reason given", w["status"] == NO_VERDICT
              and w["checks"].get(ROUTE_CHECK) != PASSED and any(want in x for x in w["reasons"]),
              "; ".join(w["reasons"]))
    check("in-use check, case 14: a clean built row with a passing check reads",
          all(withhold(g_, a)["status"] == "reading" and withhold(g_, a)["checks"][ROUTE_CHECK] == PASSED
              for a in ("T", "C", "M")
              for g_ in [dict(good, controls={"7": dict(holds=True), "1": dict(holds=True), "4": dict(holds=True)})]))
    check("in-use check, case 17: arm F is not judged, field or no field",
          withhold(dict(good, gate={k: v for k, v in G_ok.items() if k != "route_in_use"}), "F")["status"] == "reading"
          and ROUTE_CHECK not in withhold(good, "F")["checks"])
    check("in-use check: exactly at the bars passes (0.9 weight, 0.5 use)",
          withhold(route(weight_on_true_agent=0.9, routes={"slot": dict(route_use=0.5)}), "C")["status"] == "reading")
    check("in-use check: the in-use failure is not a learning failure (never R3 by itself)",
          withhold(route(routes=flat_use), "C")["learning_passes"] is True)

    # --- two seeds, each passing everything; the separation; the outcome ----
    R = lambda d: dict(status="reading", degree=d, reasons=[], learning_passes=True)
    NV = lambda why, learned=True: dict(status=NO_VERDICT, degree=None, reasons=[why], learning_passes=learned)
    T = arm_outcome({0: R(0.0), 1: R(0.0), 2: R(0.02)})
    C = arm_outcome({0: R(1.0051), 1: R(0.9926), 2: R(0.9974)})
    Mm = arm_outcome({0: R(0.4886), 1: R(0.4860), 2: R(0.5449)})
    check("two seeds: three readings read", T["read"] and T["seeds_read"] == 3)
    two = arm_outcome({0: R(0.9), 1: NV("control 4 failed"), 2: R(0.95)})
    check("two seeds: two readings read, the third is reported", two["read"] and two["reported_not_deciding"] == [1])
    check("two seeds: one reading does not read", not arm_outcome({0: R(0.9), 1: NV("x"), 2: NV("y")})["read"])
    check("two seeds: the learning gate needs two seeds each passing every learning condition",
          not arm_outcome({0: R(0.9), 1: NV("x", False), 2: NV("y", False)})["gate_passes"])
    s = separation(T, C)
    check("separation: lowest C minus highest T, unpaired (toy figures: 0.9926 - 0.02)",
          s["clears"] and abs(s["value"] - (0.9926 - 0.02)) < 1e-12)
    s2 = separation(arm_outcome({0: R(0.0), 1: R(0.6), 2: R(0.0)}),
                    arm_outcome({0: R(1.0), 1: R(1.0), 2: R(1.0)}))
    check("separation: unpaired means arm T's worst seed counts against any of arm C's",
          not s2["clears"] and abs(s2["value"] - 0.4) < 1e-12)
    ts = {0: 0.4837, 1: 0.4760, 2: 0.4920}
    g = dict(T=True, C=True, M=True, F=True)
    # the toy's real gate: arm F learns named-other on seed 0 only
    F_toy = arm_outcome({0: NV("read failed its floor"), 1: NV("failed its gate on learning", False),
                         2: NV("failed its gate on learning", False)})
    toy_g = dict(g, F=F_toy["gate_passes"])
    o = outcome(toy_g, dict(T=T, C=C, M=Mm, F=F_toy), ts, dict(seed=0, passed=True))
    check("outcome: the toy's real gate, seed 0 as step 5a -> fifth term, failed its gate on learning",
          o["code"] == "fifth" and o["term"] == "metric validated, degree not read: failed its gate on learning"
          and o["arm_M"]["prediction_met"], o["term"])
    check("outcome: the toy's real gate, seed 1 as step 5a -> R3",
          outcome(toy_g, dict(T=T, C=C, M=Mm, F=F_toy), ts, dict(seed=1, passed=False))["code"] == "R3")
    check("outcome: the toy's real gate, no step record -> R3",
          outcome(toy_g, dict(T=T, C=C, M=Mm, F=F_toy), ts, None)["code"] == "R3")
    F_read = arm_outcome({0: R(0.7), 1: R(0.75), 2: NV("control 7 failed")})
    o1 = outcome(g, dict(T=T, C=C, M=Mm, F=F_read), ts)
    check("outcome: arm F reads on two seeds -> R1, with both scope phrases",
          o1["code"] == "R1" and SCOPE_METRIC in o1["sentence"] and SCOPE_DEGREE in o1["sentence"])
    check("outcome: arm T fails its gate -> R3 whatever else",
          outcome(dict(g, T=False), dict(T=T, C=C, M=Mm, F=F_read))["code"] == "R3")
    check("outcome: arm M fails its gate -> dropped, term unchanged",
          outcome(dict(g, M=False), dict(T=T, C=C, M=Mm, F=F_read))["code"] == "R1")
    close = arm_outcome({0: R(0.3), 1: R(0.35), 2: R(0.4)})
    check("outcome: anchors do not separate -> R2",
          outcome(g, dict(T=T, C=close, M=Mm, F=F_read))["code"] == "R2"
          and SCOPE_METRIC in outcome(g, dict(T=T, C=close, M=Mm, F=F_read))["sentence"])
    T_gf = arm_outcome({0: dict(NV("x", False), checks={"own-directed learning": FAILED}),
                        1: dict(NV("x", False), checks={"own-directed learning": FAILED}), 2: R(0.0)})
    check("outcome: R3 names the failed condition and its seeds",
          "own-directed condition, on seeds 0 and 1" in outcome(dict(g, T=False), dict(T=T_gf, C=C, M=Mm, F=F_read))["sentence"])
    C_nv = arm_outcome({s: NV("floor missed on fresh episodes") for s in range(3)})
    o2 = outcome(g, dict(T=T, C=C_nv, M=Mm, F=F_read))
    check("outcome: arm C no verdict, arm F reads -> the fallback, degree read",
          o2["code"] == "fallback_read" and SCOPE_METRIC in o2["sentence"])
    F_nv = arm_outcome({s: NV("read failed its floor") for s in range(3)})
    check("outcome: arm C no verdict, arm F no verdict -> the fallback, degree not read, with the reason",
          outcome(g, dict(T=T, C=C_nv, M=Mm, F=F_nv))["term"]
          == "metric checked against the separable model only, degree not read: read failed its floor")
    T_nv = arm_outcome({s: NV("control 1 failed") for s in range(3)})
    check("outcome: arm T no verdict -> metric not validated (not R2)",
          outcome(g, dict(T=T_nv, C=C, M=Mm, F=F_read))["term"] == "metric not validated: control 1 failed")
    M_nv = arm_outcome({s: NV("x") for s in range(3)})
    o3 = outcome(g, dict(T=T, C=C, M=M_nv, F=F_read))
    check("outcome: arm M no verdict drops arm M and says so",
          o3["arm_M"]["status"] == "dropped" and any("dropped" in n for n in o3["notes"]) and o3["code"] == "R1")
    M_out = arm_outcome({0: R(0.8), 1: R(0.85), 2: R(0.9)})
    o4 = outcome(g, dict(T=T, C=C, M=M_out, F=F_read), ts)
    check("outcome: arm M outside its band changes no term; the sentence says so",
          o4["code"] == "R1" and "arm M missed its predicted reading" in o4["sentence"]
          and "against arms T and C only" in o4["sentence"])
    check("outcome: arm F failed at step 5a -> R3 with nothing else launched",
          outcome({"F": False}, dict(F=F_toy), None, dict(seed=1, passed=False))["code"] == "R3")

    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
    else:
        ap.print_help()
