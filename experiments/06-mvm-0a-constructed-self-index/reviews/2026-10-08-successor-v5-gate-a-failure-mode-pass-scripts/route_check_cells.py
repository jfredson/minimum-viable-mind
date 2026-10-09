"""Does the registered in-use check count a built route whose record is
missing? Version 5, section 5.6, part B: route use "must be at least 0.5 on
every built route (arm T's slot; arm C's stirred-in route; both of arm M's)
... a missing field is 'not run'; ... both count against."

Calls the registered decision code's own judge, `measure.route_check`, on
hand-made in-use records. No model, no record edited; $0.

    .venv/bin/python -I route_check_cells.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "08-successor-degree", "src"))
import measure as M  # noqa: E402  the registered decision code

GOOD = dict(actions=3000, right_with_true_answer=2000, still_right_with_swapped_answer=0, route_use=1.0)
FLAT = dict(actions=3000, right_with_true_answer=2000, still_right_with_swapped_answer=1990, route_use=0.005)


def rec(routes):
    return dict(weight_on_true_agent=0.999, sharpness=4.0, sharpness_learned=False,
                use_bar=0.5, weight_bar=0.9, routes=routes)


CASES = [
    ("arm M, both routes present and in use (as procedure.route_in_use writes them)",
     "M", {"separable": GOOD, "entangled_items": GOOD}, "passed"),
    ("arm M, stirred-in route present and flat", "M", {"separable": GOOD, "entangled_items": FLAT}, "failed"),
    ("arm M, stirred-in route MISSING from the record, separable in use", "M", {"separable": GOOD},
     "not run (text: a missing field counts against)"),
    ("arm C, its stirred-in route missing, an unrelated 'slot' route in use", "C", {"slot": GOOD},
     "not run (text: arm C's stirred-in route)"),
    ("arm T, recorded under the wrong name ('entangled', as a2_cases.route_flat builds it), flat", "T",
     {"entangled": FLAT}, "failed (on a route arm T does not have)"),
]

print("measure.route_check on hand-made in-use records (the registered judge of part B)")
for about, arm, routes, text_says in CASES:
    state, reasons = M.route_check(rec(routes), arm)
    print(f"  {about}:\n      code returns {state!r}; the text's rule gives {text_says}"
          + (f"; reasons {reasons}" if reasons else ""))
print()
print("Which route names does the code expect per arm? ROUTE_LABELS:", M.ROUTE_LABELS)
print("Does route_check compare the recorded route names with the arm's built routes? "
      + ("yes" if "slot" in M.route_check.__code__.co_consts or "entangled_items" in M.route_check.__code__.co_consts
         else "no: it judges whichever routes the record lists"))
