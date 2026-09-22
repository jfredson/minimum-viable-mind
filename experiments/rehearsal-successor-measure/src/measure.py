"""The measure, and its no-verdict rule, with the arithmetic exercised on
cases chosen to break it.

UNREGISTERED. Implements section 6 of
`docs/successor-experiment-proposal-2026-09-21.md`:

    degree = (accuracy_whole - accuracy_ownership_only) / accuracy_whole

Zero means fully separable — transplanting the ownership answer alone does
everything transplanting the whole state does. The number rises toward one as
the act resists being pulled apart.

Why this file exists at all
---------------------------
The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (red-team ledger item `RT-21`, the
unsatisfiable denominator). So this measure gets an explicit no-verdict rule,
written before it runs, and the rule is exercised on cases built to break it.

The three outcomes
------------------
- **A number.** The whole-state transplant cleared the floor, so there is
  something for the ratio to be a share of.
- **A negative number.** The ownership-only transplant beat the whole-state
  one. Reported as observed and treated as a warning about the instrument,
  never quietly clipped to zero.
- **No verdict.** The whole-state transplant did not reproduce the
  counterfactual at these sites. No degree is reported and the reason is
  recorded.

**The floor's value is not set here.** It is an output of the rehearsal and
John's to fix; every function below takes it as an argument and the rehearsal
reports the measured curve a floor would be chosen against.

    ../../../.venv/bin/python measure.py --self-test
"""
from __future__ import annotations

import argparse
import math

VALID, NEGATIVE, NO_VERDICT = "valid", "negative", "no verdict"


def reading(accuracy_whole: float, accuracy_ownership_only: float,
            floor: float) -> dict:
    """The reading, with its no-verdict rule attached.

    `floor` is the threshold on `accuracy_whole` below which no degree is
    reported. It is a parameter and never a default: naming one here would be
    inventing the number this rehearsal exists to measure."""
    if floor <= 0.0:
        raise ValueError("the floor must be positive: a floor of zero is the "
                         "unsatisfiable-denominator defect all over again")
    for name, v in (("accuracy_whole", accuracy_whole),
                    ("accuracy_ownership_only", accuracy_ownership_only)):
        if not (0.0 <= v <= 1.0) or not math.isfinite(v):
            raise ValueError(f"{name} is not a share between zero and one: {v}")

    raw = accuracy_whole - accuracy_ownership_only
    if accuracy_whole < floor:
        return dict(status=NO_VERDICT, degree=None, raw_difference=raw,
                    accuracy_whole=accuracy_whole,
                    accuracy_ownership_only=accuracy_ownership_only,
                    reason=(f"the whole-state transplant reached "
                            f"{accuracy_whole:.4f}, below the floor of {floor:.4f}, "
                            f"so there is nothing for the ratio to be a share of"))
    degree = raw / accuracy_whole
    return dict(status=NEGATIVE if degree < 0 else VALID, degree=degree,
                raw_difference=raw, accuracy_whole=accuracy_whole,
                accuracy_ownership_only=accuracy_ownership_only,
                reason=("the ownership-only transplant beat the whole-state one; "
                        "reported as observed, not clipped to zero")
                       if degree < 0 else "")


def reading_corrected(accuracy_whole: float, accuracy_ownership_only: float,
                      accuracy_untouched: float, floor: float) -> dict:
    """The candidate floor-corrected form, added BESIDE the registered one and
    never in place of it.

        degree = (whole - ownership_only) / (whole - untouched)

    The share of trials that land on the donor's value with no transplant at
    all sits under BOTH of the registered form's terms, and a floor under both
    terms does not cancel in a ratio. Subtracting it makes the top of the scale
    the same for every arm: the denominator becomes how much room the
    whole-state transplant actually had, rather than where it ended up.

    `floor` here applies to that room, `whole - untouched`, not to `whole`.
    Its value is not set in this file and is not set by this rehearsal's code;
    it is an output the rehearsal hands to John."""
    if floor <= 0.0:
        raise ValueError("the floor must be positive")
    for name, v in (("accuracy_whole", accuracy_whole),
                    ("accuracy_ownership_only", accuracy_ownership_only),
                    ("accuracy_untouched", accuracy_untouched)):
        if not (0.0 <= v <= 1.0) or not math.isfinite(v):
            raise ValueError(f"{name} is not a share between zero and one: {v}")
    room = accuracy_whole - accuracy_untouched
    raw = accuracy_whole - accuracy_ownership_only
    if room < floor:
        return dict(status=NO_VERDICT, degree=None, raw_difference=raw,
                    room=room,
                    reason=(f"the whole-state transplant cleared the untouched rate "
                            f"by only {room:.4f}, below the floor of {floor:.4f}"))
    degree = raw / room
    return dict(status=NEGATIVE if degree < 0 else VALID, degree=degree,
                raw_difference=raw, room=room,
                reason=("the ownership-only transplant beat the whole-state one; "
                        "reported as observed, not clipped to zero")
                       if degree < 0 else "")


def both_forms(accuracy_whole: float, accuracy_ownership_only: float,
               accuracy_untouched: float, floor: float) -> dict:
    """Both candidate forms, always reported together. Nothing in this
    rehearsal chooses between them."""
    return dict(
        registered=reading(accuracy_whole, accuracy_ownership_only, floor),
        floor_corrected=reading_corrected(accuracy_whole, accuracy_ownership_only,
                                          accuracy_untouched, floor))


def self_test() -> None:
    """Made-up cases, each with the landing written down before it runs."""
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("measure.py self-test — the arithmetic on cases chosen to break it")
    floor = 0.30          # a made-up floor for the self-test only, not a bar

    cases = [
        # (name, whole, ownership-only, expected status, expected degree)
        ("fully separable: the subspace does everything", 0.90, 0.90, VALID, 0.0),
        ("fully entangled: the subspace does nothing", 0.90, 0.00, VALID, 1.0),
        ("half and half", 0.80, 0.40, VALID, 0.5),
        ("the denominator is exactly zero", 0.00, 0.00, NO_VERDICT, None),
        ("the denominator is just under the floor", 0.2999, 0.10, NO_VERDICT, None),
        ("the denominator is just over the floor", 0.3001, 0.10, VALID, None),
        ("the subspace beats the whole state", 0.50, 0.80, NEGATIVE, -0.6),
        ("both at the ceiling", 1.00, 1.00, VALID, 0.0),
        ("whole state at the ceiling, subspace at zero", 1.00, 0.00, VALID, 1.0),
        ("both zero", 0.00, 0.00, NO_VERDICT, None),
    ]
    for name, w, o, want_status, want_degree in cases:
        r = reading(w, o, floor)
        ok = r["status"] == want_status
        if want_degree is not None:
            ok &= abs(r["degree"] - want_degree) < 1e-9
        check(f"{name}", ok,
              f"whole {w:.4f}, ownership-only {o:.4f} -> {r['status']}"
              + (f", degree {r['degree']:.4f}" if r["degree"] is not None else ""))

    # --- the review's arithmetic, reproduced rather than trusted -----------
    # Two systems with identical true separability by the proposal's own
    # account, and different transplant accuracies.
    print("\n  the review's two systems, both with half the identity-driven "
          "difference outside the subspace:")
    for label, w, o in (("strong transplant", 0.9, 0.5125),
                        ("weak transplant", 0.35, 0.2375)):
        reg = reading(w, o, 0.10)["degree"]
        cor = reading_corrected(w, o, 0.125, 0.10)["degree"]
        print(f"    {label:18s} whole {w:.4f} ownership-only {o:.4f}: "
              f"registered form {reg:.4f}, floor-corrected form {cor:.4f}")
    a = reading(0.9, 0.5125, 0.10)["degree"]
    b = reading(0.35, 0.2375, 0.10)["degree"]
    ca = reading_corrected(0.9, 0.5125, 0.125, 0.10)["degree"]
    cb = reading_corrected(0.35, 0.2375, 0.125, 0.10)["degree"]
    check("the registered form gives the two systems different readings",
          abs(a - b) > 0.05, f"{a:.4f} against {b:.4f}, a gap of {abs(a - b):.4f}")
    check("the floor-corrected form gives them the same reading",
          abs(ca - cb) < 1e-9 and abs(ca - 0.5) < 1e-9,
          f"{ca:.4f} against {cb:.4f}")

    # a formula that only survives on the values its author had in mind
    bad = 0
    for w in [i / 100 for i in range(0, 101)]:
        for o in [i / 100 for i in range(0, 101)]:
            r = reading(w, o, floor)
            if r["status"] != NO_VERDICT and not math.isfinite(r["degree"]):
                bad += 1
    check("every share pair from zero to one returns a finite number or no verdict",
          bad == 0, f"{101 * 101} pairs swept, {bad} non-finite")

    # the floor may not be switched off
    try:
        reading(0.5, 0.2, 0.0)
        check("a floor of zero is refused", False)
    except ValueError:
        check("a floor of zero is refused", True,
              "the unsatisfiable-denominator defect cannot be reintroduced by "
              "passing a floor of zero")

    for bad_v in (-0.1, 1.1, float("nan"), float("inf")):
        try:
            reading(bad_v, 0.5, floor)
            check(f"a score of {bad_v} is refused", False)
        except ValueError:
            check(f"a score of {bad_v} is refused", True)

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
