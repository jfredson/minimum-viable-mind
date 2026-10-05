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
}


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


def no_transplant_rule(untouched: float, acc: float) -> dict:
    """Section 6.4, item 3: the untouched model lands on the donor's answer
    only by erring onto exactly that one of the seven other slots, so the
    rate should be near (1 - p) / 7, within 0.018. The detection margin at
    the bar is printed beside it."""
    formula = (1 - acc) / 7
    bar_acc = GATE_MIN_CORRECT / GATE_EPISODES
    broken_flag = 1 / 8 - (1 - bar_acc) / 7
    return dict(rate=untouched, formula=formula, miss=untouched - formula,
                room=NO_TRANSPLANT_ROOM,
                inside_allowance=abs(untouched - formula) <= NO_TRANSPLANT_ROOM,
                detection_margin_at_the_bar=broken_flag - NO_TRANSPLANT_ROOM)


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


def withhold(row: dict, arm: str) -> dict:
    """Section 6.4, item 5: the reading for one arm and seed, or "no verdict"
    and every reason, decided here and not by whoever reads the table.

    `row` carries: `nomination_status` ("nominated" or the no-verdict reason
    at nomination), `gate_passes`, `described_only`, `reading` (from
    `reading`), `dev_floor_clears`, `no_transplant` (from
    `no_transplant_rule`), and `controls` with keys "7", "1" and "4" each
    holding a `holds` flag (control 1's is None except on arm T)."""
    reasons = []
    if not row.get("gate_passes", False):
        reasons.append("the arm failed its gate")
    if row.get("nomination_status") != "nominated":
        reasons.append(row.get("nomination_status") or "not nominated")
    r = row.get("reading")
    if r is None:
        if not reasons:
            reasons.append("no reading was computed")
    else:
        if row.get("described_only"):
            reasons.append("reported for description only (the site set was chosen with the "
                           "piece rule switched off)")
        if not r["floor"]["clears"]:
            reasons.append("floor missed on fresh episodes")
        if not row.get("dev_floor_clears", True):
            reasons.append("floor missed on development episodes")
        nt = row.get("no_transplant")
        if nt is None or not nt["inside_allowance"]:
            reasons.append("no-transplant rate outside its allowance: the pairing is suspect")
        c = row.get("controls") or {}
        if c.get("7", {}).get("holds") is not True:
            reasons.append("control 7, the null transplant, failed")
        if arm == "T" and c.get("1", {}).get("holds") is not True:
            reasons.append("control 1, the content transplant, failed on arm T")
        if c.get("4", {}).get("holds") is not True:
            reasons.append("control 4, the too-early-position control, failed")
    if reasons:
        return dict(status=NO_VERDICT, degree=None, reasons=reasons,
                    arithmetic_withheld=None if r is None else r["degree"])
    return dict(status="reading", degree=r["degree"], reasons=[],
                negative=r["degree"] < 0, above_one=r["degree"] > 1)


def arm_outcome(seed_rows: dict) -> dict:
    """Two of three (ruled 2026-10-03, ruling 6): an arm is read if two or
    more of its seeds read; the third is reported. `seed_rows` maps seed to
    the dict `withhold` returned."""
    read = {s: r["degree"] for s, r in seed_rows.items() if r["status"] == "reading"}
    out = dict(seeds=len(seed_rows), seeds_read=len(read), readings=read,
               no_verdict={s: r["reasons"] for s, r in seed_rows.items()
                           if r["status"] != "reading"})
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


def arm_M_check(arm_M: dict, true_slot: dict) -> dict:
    """Arm M's prediction: between 0.3 and 0.7 on every seed that reads, and
    within 0.10 of its true-slot reading on the same fresh episodes."""
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


def outcome(gates: dict, arms: dict, true_slot_M: dict | None = None) -> dict:
    """The registered outcome term, from the gates and the four arms.

    `gates[arm]` is True if the arm passed its gate (section 8.1: own-directed
    only on T, C and M; both conditions on F) after any permitted re-run.
    `arms[arm]` is what `arm_outcome` returned."""
    notes = []
    failed = [a for a in ("T", "C", "F") if not gates.get(a, False)]
    m = arm_M_check(arms["M"], true_slot_M or {}) if "M" in arms else None
    if m is not None and m["status"] == "dropped":
        notes.append(m["reason"])
    if failed:
        return dict(term=OUTCOME_TERMS["R3"], code="R3",
                    reason=f"arm(s) {', '.join(failed)} failed the gate", arm_M=m, notes=notes)
    two_arm = not arms["C"]["read"]
    if two_arm:
        notes.append("arm C returned no verdict: the two-arm fallback fires, anchored at one "
                     "end only, and the R1 sentence is correspondingly weaker")
        sep = dict(computed=False, clears=False, reason="two-arm fallback")
        validated = arms["T"]["read"]
    else:
        sep = separation(arms["T"], arms["C"])
        validated = sep["clears"]
    if not validated:
        return dict(term=OUTCOME_TERMS["R2"], code="R2", separation=sep, arm_M=m, notes=notes)
    if arms["F"]["read"]:
        return dict(term=OUTCOME_TERMS["R1"], code="R1", separation=sep, arm_M=m,
                    arm_F=arms["F"]["readings"], notes=notes)
    reasons = sorted({r for rs in arms["F"]["no_verdict"].values() for r in rs})
    return dict(term=f"{OUTCOME_TERMS['fifth']}: {'; '.join(reasons)}", code="fifth",
                separation=sep, arm_M=m, notes=notes)


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
    check("no-transplant rule: the detection margin at the bar is 0.0018 (version 4, 6.4 item 3)",
          abs(nt["detection_margin_at_the_bar"] - 0.0018) < 0.0001,
          f"{nt['detection_margin_at_the_bar']:.4f}")

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

    # --- withholding ------------------------------------------------------
    good_reading = reading(0.9, 0.05, 0.05, 0.95)
    good = dict(nomination_status="nominated", gate_passes=True, described_only=False,
                reading=good_reading, dev_floor_clears=True,
                no_transplant=no_transplant_rule(0.05, 0.66),
                controls={"7": dict(holds=True), "1": dict(holds=None), "4": dict(holds=True)})
    check("withhold: a clean row reads", withhold(good, "C")["status"] == "reading")
    for label, change, arm in (
        ("control 7 failed", {"controls": {"7": dict(holds=False), "1": dict(holds=None), "4": dict(holds=True)}}, "C"),
        ("control 4 failed", {"controls": {"7": dict(holds=True), "1": dict(holds=None), "4": dict(holds=False)}}, "C"),
        ("control 1 failed on arm T", {"controls": {"7": dict(holds=True), "1": dict(holds=False), "4": dict(holds=True)}}, "T"),
        ("control 1 missing on arm T counts as failed", {"controls": {"7": dict(holds=True), "4": dict(holds=True)}}, "T"),
        ("a control that could not be evaluated counts as failed", {"controls": {"7": dict(holds=None), "1": dict(holds=None), "4": dict(holds=True)}}, "C"),
        ("no-transplant rate outside", {"no_transplant": no_transplant_rule(0.2, 0.66)}, "C"),
        ("floor missed on fresh episodes", {"reading": reading(0.3, 0.1, 0.05, 0.95)}, "C"),
        ("gate failed", {"gate_passes": False}, "F"),
        ("read failed its floor at nomination", {"nomination_status": "read failed its floor: no size's piece reaches four fifths", "described_only": True}, "F"),
    ):
        row = dict(good, **change)
        w = withhold(row, arm)
        check(f"withhold: {label} -> no verdict, with the reason in the output",
              w["status"] == NO_VERDICT and w["degree"] is None and w["reasons"], "; ".join(w["reasons"]))
    check("withhold: control 1 failing on arm C does not withhold (it holds on arm T only)",
          withhold(dict(good, controls={"7": dict(holds=True), "1": dict(holds=False), "4": dict(holds=True)}), "C")["status"] == "reading")

    # --- two of three, the separation, the outcome ---------------------------
    R = lambda d: dict(status="reading", degree=d, reasons=[])
    NV = lambda why: dict(status=NO_VERDICT, degree=None, reasons=[why])
    T = arm_outcome({0: R(0.0), 1: R(0.0), 2: R(0.02)})
    C = arm_outcome({0: R(1.0051), 1: R(0.9926), 2: R(0.9974)})
    Mm = arm_outcome({0: R(0.4886), 1: R(0.4860), 2: R(0.5449)})
    F_nv = arm_outcome({s: NV("read failed its floor") for s in range(3)})
    check("two of three: three readings read", T["read"] and T["seeds_read"] == 3)
    two = arm_outcome({0: R(0.9), 1: NV("control 4 failed"), 2: R(0.95)})
    check("two of three: two readings read, the third is reported", two["read"] and two["reported_not_deciding"] == [1])
    check("two of three: one reading does not read", not arm_outcome({0: R(0.9), 1: NV("x"), 2: NV("y")})["read"])
    s = separation(T, C)
    check("separation: lowest C minus highest T, unpaired (toy figures: 0.9926 - 0.02)",
          s["clears"] and abs(s["value"] - (0.9926 - 0.02)) < 1e-12)
    s2 = separation(arm_outcome({0: R(0.0), 1: R(0.6), 2: R(0.0)}),
                    arm_outcome({0: R(1.0), 1: R(1.0), 2: R(1.0)}))
    check("separation: unpaired means arm T's worst seed counts against any of arm C's",
          not s2["clears"] and abs(s2["value"] - 0.4) < 1e-12)
    g = dict(T=True, C=True, M=True, F=True)
    o = outcome(g, dict(T=T, C=C, M=Mm, F=F_nv), {0: 0.4837, 1: 0.4760, 2: 0.4920})
    check("outcome: the toy lands on the fifth term with its reason after a colon",
          o["code"] == "fifth" and o["term"] == "metric validated, degree not read: read failed its floor"
          and o["arm_M"]["prediction_met"], o["term"])
    F_read = arm_outcome({0: R(0.7), 1: R(0.75), 2: NV("control 7 failed")})
    check("outcome: arm F reads on two seeds -> R1",
          outcome(g, dict(T=T, C=C, M=Mm, F=F_read))["code"] == "R1")
    check("outcome: arm F fails its gate -> R3",
          outcome(dict(g, F=False), dict(T=T, C=C, M=Mm, F=F_read))["code"] == "R3")
    close = arm_outcome({0: R(0.3), 1: R(0.35), 2: R(0.4)})
    check("outcome: anchors do not separate -> R2",
          outcome(g, dict(T=T, C=close, M=Mm, F=F_read))["code"] == "R2")
    C_nv = arm_outcome({s: NV("floor missed on fresh episodes") for s in range(3)})
    o2 = outcome(g, dict(T=T, C=C_nv, M=Mm, F=F_read))
    check("outcome: arm C no verdict fires the two-arm fallback and says so",
          o2["code"] == "R1" and any("two-arm fallback" in n for n in o2["notes"]))
    M_nv = arm_outcome({s: NV("x") for s in range(3)})
    o3 = outcome(g, dict(T=T, C=C, M=M_nv, F=F_read))
    check("outcome: arm M no verdict drops arm M and says so",
          o3["arm_M"]["status"] == "dropped" and any("dropped" in n for n in o3["notes"]))

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
