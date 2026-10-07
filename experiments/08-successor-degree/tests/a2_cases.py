"""The made-up failure cases for the A2 end-to-end run, with the outcome each
must land on, written from the ruling text BEFORE the changed code ran on any
of them.

Method: `docs/2026-10-06-successor-a2-decision-procedure-method.md`.
Rulings: `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` (pages 1,
5, 7, 8 and 9, and the same-day addendum), with the drafted texts it adopts in
the two dispositions files of 2026-10-04.

Every case is the toy's committed records
(`out-freeze-tests/t3a-committed-reads/row_*.json`, checked by SHA-256 before
use) with the named fields changed. Nothing here trains, loads or runs a model.
Changing a reading's `degree` directly (rather than the three accuracies it is
computed from) is deliberate: the procedure decides on the degree and the
floor flag, and a made-up case needs only those to be what it says.

This file holds definitions and expectations only. The runner is
`a2_run_cases.py`. An expectation here must not be edited after the runner has
produced output; a case that lands elsewhere is a finding, reported as such.
"""
from __future__ import annotations

# The committed rehearsal check of the ownership-free line (RT-237): with the
# acting channel zeroed, own-directed answers that are one of the four
# candidate values, of 3,000, per toy model. From
# experiments/rehearsal-successor-measure/out-lesion-content-check/
# lesion_content_check.json (branch rulings-2026-10-06-gate-a-v4). Its
# lesioned own-correct counts equal the T3a rows' (528, 555, 582 on arm F),
# so it was taken on the same 3,000 gate episodes.
TOY_CANDIDATE_COUNTS = {
    ("T", 0): 3000, ("T", 1): 3000, ("T", 2): 3000,
    ("C", 0): 2236, ("C", 1): 2160, ("C", 2): 2132,
    ("M", 0): 2770, ("M", 1): 2686, ("M", 2): 2660,
    ("F", 0): 2100, ("F", 1): 2238, ("F", 2): 2324,
}

ARMS = ("T", "C", "M", "F")
SEEDS = (0, 1, 2)


# ------------------------------------------------------------ field helpers

def gate(rows, arm, seed, own=None, other=None, lesioned_own=None, candidate="keep"):
    g = rows[(arm, seed)]["gate"]
    if own is not None:
        g["own_correct"] = own
    if other is not None:
        g["other_correct"] = other
    if lesioned_own is not None:
        g["lesioned_own_correct"] = lesioned_own
    if candidate != "keep":
        if candidate is None:
            g.pop("lesioned_candidate_own_correct", None)
        else:
            g["lesioned_candidate_own_correct"] = candidate
    # the booleans the frozen code wrote are kept consistent with the counts
    bar = g["bar"]
    g["own_clears"] = g["own_correct"] >= bar
    g["other_clears"] = g["other_correct"] >= bar
    g["lesion_collapses_own"] = g["lesioned_own_correct"] < bar
    g["seed_passes"] = g["own_clears"] and (arm != "F" or g["other_clears"])


def add_candidate_counts(rows):
    """The ownership-free line's field, as the changed gate code writes it,
    filled from the committed rehearsal check."""
    for k, v in TOY_CANDIDATE_COUNTS.items():
        rows[k]["gate"]["lesioned_candidate_own_correct"] = v


def degree(rows, arm, seed, d):
    rows[(arm, seed)]["primary"]["reading"]["degree"] = d
    rows[(arm, seed)]["primary"]["reading"]["status"] = "valid" if d >= 0 else "negative"


def control(rows, arm, seed, which, holds="drop"):
    c = rows[(arm, seed)]["primary"]["controls"]
    if holds == "drop":
        c.pop(which, None)
    else:
        c.setdefault(which, {})["holds"] = holds


def make_F_read(rows, degrees=(0.62, 0.66, 0.71)):
    """Arm F passes everything on all three seeds: both learning conditions,
    the collapse (already true on the toy: 528, 555, 582 against 790), the
    ownership-free line (2,100, 2,238, 2,324 against 1,546), nomination, the
    floors and the controls."""
    add_candidate_counts(rows)
    for s, d in zip(SEEDS, degrees):
        gate(rows, "F", s, other=900)
        r = rows[("F", s)]
        r["nomination_status"] = "nominated"
        p = r["primary"]
        p["described_only"] = False
        p["dev_floor_clears"] = True
        p["reading"]["floor"]["clears"] = True
        degree(rows, "F", s, d)
        control(rows, "F", s, "7", True)
        control(rows, "F", s, "4", True)


# ------------------------------------------------------------ the cases
#
# `steps` is the step record written beside the rows as `steps.json`: which
# seed of arm F was its step 5a run (section 11, step 5a; stop S4). None means
# no step record exists, which is the toy's real state.
#
# `expect` is the outcome code; `reason_has` are pieces of text that must
# appear in the reason after the colon (or in R3's reason); `sentence_has`
# must appear in the outcome sentence; `seed_reasons_have` maps "arm/seed" to
# pieces of text that must appear among that seed's listed reasons; `withheld`
# lists (arm, seed) whose computed figure must appear nowhere in the outputs.

def c_toy(rows):
    pass


def c_toy_5a_seed0(rows):
    pass


def c_toy_5a_seed1(rows):
    pass


def c_r1(rows):
    make_F_read(rows)


def c_r2(rows):
    make_F_read(rows)
    for s, d in zip(SEEDS, (0.40, 0.45, 0.50)):
        degree(rows, "C", s, d)


def c_fallback_read(rows):
    make_F_read(rows)
    control(rows, "C", 0, "7", False)
    control(rows, "C", 1, "7", False)


def c_fallback_not_read(rows):
    add_candidate_counts(rows)
    for s in SEEDS:                       # arm F learns, but no site set: the toy's own reason
        gate(rows, "F", s, other=900)
    control(rows, "C", 0, "7", False)
    control(rows, "C", 1, "7", False)


def c_not_validated(rows):
    make_F_read(rows)
    control(rows, "T", 0, "1", False)
    control(rows, "T", 1, "1", False)


def c_not_validated_and_fallback(rows):
    make_F_read(rows)
    control(rows, "T", 0, "1", False)
    control(rows, "T", 1, "1", False)
    control(rows, "C", 0, "7", False)
    control(rows, "C", 1, "7", False)


def c_split_review_table(rows):
    """The review's A10 table on arm F. Seed 0: own pass, named-other fail,
    collapse pass, piece pass. Seed 1: own pass, named-other pass, collapse
    FAIL, piece pass. Seed 2: own FAIL, named-other pass, collapse pass,
    piece FAIL. Every column passes on two seeds; no seed passes everything.
    Only seed 1 passes the learning gate, so arm F fails it at step 5b,
    having passed at step 5a on seed 1."""
    make_F_read(rows)
    gate(rows, "F", 0, other=700)
    gate(rows, "F", 1, lesioned_own=900)
    gate(rows, "F", 2, own=700)
    rows[("F", 2)]["nomination_status"] = "read failed its floor: no size's piece reaches four fifths"


def c_split_learning_passes(rows):
    """Arm F passes the learning gate on all three seeds, and each seed fails
    exactly one different later condition: seed 0 its nomination, seed 1 the
    collapse, seed 2 the ownership-free line. Each condition holds on two
    seeds of three; no seed passes everything. The frozen code would read
    seeds 1 and 2 and land on R1."""
    make_F_read(rows)
    rows[("F", 0)]["nomination_status"] = "read failed its floor: no size's piece reaches four fifths"
    gate(rows, "F", 1, lesioned_own=900)
    gate(rows, "F", 2, candidate=1500)


def c_split_one_seed_everything(rows):
    """One of the frozen code's 18 patterns: seed 0 passes everything; seed 1
    fails named-other (learning); seed 2 passes learning but fails the
    collapse. The arm passes its learning gate (seeds 0 and 2) and the
    collapse holds on two seeds (0 and 1), but only seed 0 passes everything.
    The frozen code would read seeds 0 and 1 and land on R1."""
    make_F_read(rows)
    gate(rows, "F", 1, other=700)
    gate(rows, "F", 2, lesioned_own=900)


def c_overlap_one_seed(rows):
    """Arm T seed 2 fails four things at once, one of them at nomination:
    every reason must be listed, not only the first. T still reads on seeds
    0 and 1."""
    make_F_read(rows)
    r = rows[("T", 2)]
    r["nomination_status"] = "no site set clears the whole-state floor"
    r["primary"]["dev_floor_clears"] = False
    control(rows, "T", 2, "7", False)
    control(rows, "T", 2, "4", False)


def c_M_outside_band(rows):
    make_F_read(rows)
    for s, d in zip(SEEDS, (0.80, 0.85, 0.90)):
        degree(rows, "M", s, d)


def c_M_fails_gate(rows):
    make_F_read(rows)
    gate(rows, "M", 0, own=700)
    gate(rows, "M", 1, own=700)


def c_withheld_seed(rows):
    make_F_read(rows, degrees=(0.62, 0.66, 0.123456))
    control(rows, "F", 2, "4", False)


def c_never_run(rows):
    """Arm F otherwise reads, but the ownership-free line was never run (the
    field is absent, as on every toy record)."""
    make_F_read(rows)
    for s in SEEDS:
        gate(rows, "F", s, candidate=None)


def c_never_run_control(rows):
    """Control 4 never ran on arm C seeds 0 and 1 (the field is absent)."""
    make_F_read(rows)
    control(rows, "C", 0, "4", "drop")
    control(rows, "C", 1, "4", "drop")


def c_no_transplant_outside(rows):
    """Arm T's no-transplant rate is far outside its old allowance on every
    seed. Under page 8 it is reported and withholds nothing."""
    make_F_read(rows)
    for s in SEEDS:
        nt = rows[("T", s)]["primary"]["no_transplant"]
        nt["rate"] = nt["formula"] + 0.05
        nt["miss"] = 0.05
        nt["inside_allowance"] = False


def c_F_channel_removal(rows):
    """Arm F learns on every seed, but its channel removal does not collapse
    on two seeds."""
    make_F_read(rows)
    gate(rows, "F", 0, lesioned_own=900)
    gate(rows, "F", 1, lesioned_own=900)


def c_T_fails_gate(rows):
    """Arm T fails its learning gate on two seeds; arm C is also no verdict.
    The gate comes first, whatever else happened."""
    make_F_read(rows)
    gate(rows, "T", 0, own=700)
    gate(rows, "T", 1, own=700)
    control(rows, "C", 0, "7", False)
    control(rows, "C", 1, "7", False)


def c_F_fails_5a(rows):
    """Arm F fails named-other on its step 5a seed (seed 1, after its re-run).
    Nothing else launched: only arm F's records exist."""
    for k in [k for k in rows if k[0] != "F"]:
        del rows[k]


CASES = [
    dict(name="toy", build=c_toy, steps=None,
         expect="R3", reason_has=["arm F"],
         seed_reasons_have={"F/0": ["ownership-free line was not run"],
                            "F/1": ["failed its gate on learning", "ownership-free line was not run"]},
         withheld=[("F", 0), ("F", 1), ("F", 2)],
         about="the toy as it actually is: no step record, no ownership-free field"),
    dict(name="toy-step5a-seed0", build=c_toy_5a_seed0, steps={"arm_F_step_5a_seed": 0},
         expect="fifth", reason_has=["failed its gate on learning"], withheld=[("F", 0), ("F", 1), ("F", 2)],
         about="the toy, if seed 0 is taken as arm F's step 5a run"),
    dict(name="toy-step5a-seed1", build=c_toy_5a_seed1, steps={"arm_F_step_5a_seed": 1},
         expect="R3", reason_has=["step 5a"], withheld=[("F", 0), ("F", 1), ("F", 2)],
         about="the toy, if seed 1 is taken as arm F's step 5a run"),
    dict(name="r1", build=c_r1, steps={"arm_F_step_5a_seed": 0}, expect="R1",
         sentence_has=["on these constructed systems, for this intervention procedure",
                       "as a ratio of two transplants at the sites this procedure chose"],
         about="every arm reads, the anchors separate"),
    dict(name="r2", build=c_r2, steps={"arm_F_step_5a_seed": 0}, expect="R2",
         about="arm C reads 0.40 to 0.50: separation 0.40 - 0.02 is under 0.5"),
    dict(name="fallback-read", build=c_fallback_read, steps={"arm_F_step_5a_seed": 0},
         expect="fallback_read", sentence_has=["on these constructed systems, for this intervention procedure"],
         about="arm C no verdict on two seeds (control 7), arm F reads"),
    dict(name="fallback-not-read", build=c_fallback_not_read, steps={"arm_F_step_5a_seed": 0},
         expect="fallback_not_read", reason_has=["no size's piece reaches four fifths"],
         about="arm C no verdict, arm F learns but fails nomination on every seed"),
    dict(name="T-no-verdict", build=c_not_validated, steps={"arm_F_step_5a_seed": 0},
         expect="not_validated", reason_has=["control 1"],
         about="arm T no verdict on two seeds (control 1), everything else reads"),
    dict(name="T-and-C-no-verdict", build=c_not_validated_and_fallback, steps={"arm_F_step_5a_seed": 0},
         expect="not_validated", reason_has=["control 1"],
         about="arm T and arm C both no verdict: arm T's row of the table applies"),
    dict(name="split-review-table", build=c_split_review_table, steps={"arm_F_step_5a_seed": 1},
         expect="fifth", reason_has=["failed its gate on learning"],
         about="the review's A10 table on arm F, step 5a on seed 1"),
    dict(name="split-learning-passes", build=c_split_learning_passes, steps={"arm_F_step_5a_seed": 0},
         expect="fifth", reason_has=["did not collapse", "ownership-free line", "no size's piece"],
         about="each F seed fails one different later condition"),
    dict(name="split-one-seed-everything", build=c_split_one_seed_everything, steps={"arm_F_step_5a_seed": 0},
         expect="fifth",
         about="only seed 0 of arm F passes everything; separate counts would pass"),
    dict(name="overlap-one-seed", build=c_overlap_one_seed, steps={"arm_F_step_5a_seed": 0},
         expect="R1",
         seed_reasons_have={"T/2": ["no site set clears", "development episodes", "control 7", "control 4"]},
         withheld=[("T", 2)],
         about="four failures on arm T seed 2, all listed; T reads on 0 and 1"),
    dict(name="M-outside-band", build=c_M_outside_band, steps={"arm_F_step_5a_seed": 0},
         expect="R1", sentence_has=["arm M missed its predicted reading", "against arms T and C only"],
         about="arm M reads 0.80 to 0.90: no term changes, the sentence says so"),
    dict(name="M-fails-gate", build=c_M_fails_gate, steps={"arm_F_step_5a_seed": 0},
         expect="R1", sentence_has=["arm M", "dropped"],
         about="arm M fails its gate on two seeds: dropped, no term changes"),
    dict(name="withheld-seed", build=c_withheld_seed, steps={"arm_F_step_5a_seed": 0},
         expect="R1", seed_reasons_have={"F/2": ["control 4"]}, withheld=[("F", 2)],
         about="arm F seed 2 computes 0.123456 but fails control 4: withheld everywhere"),
    dict(name="never-run-line", build=c_never_run, steps={"arm_F_step_5a_seed": 0},
         expect="fifth", reason_has=["ownership-free line was not run"],
         seed_reasons_have={"F/0": ["ownership-free line was not run"]},
         withheld=[("F", 0), ("F", 1), ("F", 2)],
         about="the ownership-free line never ran on arm F"),
    dict(name="never-run-control", build=c_never_run_control, steps={"arm_F_step_5a_seed": 0},
         expect="fallback_read", seed_reasons_have={"C/0": ["control 4", "not run"]},
         withheld=[("C", 0), ("C", 1)],
         about="control 4 never ran on two arm C seeds"),
    dict(name="no-transplant-outside", build=c_no_transplant_outside, steps={"arm_F_step_5a_seed": 0},
         expect="R1", about="arm T's no-transplant rate is 0.05 off the formula on every seed"),
    dict(name="F-channel-removal", build=c_F_channel_removal, steps={"arm_F_step_5a_seed": 0},
         expect="fifth", reason_has=["did not collapse"],
         about="arm F learns but its channel removal does not collapse on two seeds"),
    dict(name="T-fails-gate", build=c_T_fails_gate, steps={"arm_F_step_5a_seed": 0},
         expect="R3", reason_has=["arm T"],
         about="arm T fails its learning gate; arm C is no verdict too"),
    dict(name="F-fails-5a", build=c_F_fails_5a, steps={"arm_F_step_5a_seed": 1},
         expect="R3", reason_has=["step 5a"],
         about="arm F fails at step 5a; nothing else launched, only F's records exist"),
]


# ------------------------------------------------------------ addendum, 2026-10-06
# Added after the independent check (pull request 107) and John's two
# follow-up rulings, committed BEFORE the changed code or these cases ran.
# Method: the dated addendum at the end of
# docs/2026-10-06-successor-a2-decision-procedure-method.md.

def floor_fresh(rows, arm, seed):
    rows[(arm, seed)]["primary"]["reading"]["floor"]["clears"] = False


def c_C_fresh_floor(rows):
    make_F_read(rows)
    floor_fresh(rows, "C", 0)
    floor_fresh(rows, "C", 1)


def c_T_dev_floor(rows):
    make_F_read(rows)
    rows[("T", 0)]["primary"]["dev_floor_clears"] = False
    rows[("T", 1)]["primary"]["dev_floor_clears"] = False


def c_F_fresh_floor(rows):
    make_F_read(rows)
    floor_fresh(rows, "F", 0)
    floor_fresh(rows, "F", 1)


CASES += [
    dict(name="C-fresh-floor", build=c_C_fresh_floor, steps={"arm_F_step_5a_seed": 0},
         expect="fallback_read", seed_reasons_have={"C/0": ["floor on fresh episodes failed"],
                                                    "C/1": ["floor on fresh episodes failed"]},
         withheld=[("C", 0), ("C", 1)],
         about="addendum: arm C misses the fresh-episode floor on seeds 0 and 1"),
    dict(name="T-dev-floor", build=c_T_dev_floor, steps={"arm_F_step_5a_seed": 0},
         expect="not_validated", reason_has=["floor on development episodes failed"],
         withheld=[("T", 0), ("T", 1)],
         about="addendum: arm T misses the development-episode floor on seeds 0 and 1"),
    dict(name="F-fresh-floor", build=c_F_fresh_floor, steps={"arm_F_step_5a_seed": 0},
         expect="fifth", reason_has=["floor on fresh episodes failed"],
         withheld=[("F", 0), ("F", 1)],
         about="addendum: arm F misses the fresh-episode floor on seeds 0 and 1"),
]

# Addendum expectations on existing cases (the originals above are unchanged):
# R3 names the failed gate condition as well as the arm (check, defect 2);
# R2 carries the scope phrase (John, 2026-10-06 follow-up).
ADDENDUM_EXPECT = {
    "toy": dict(sentence_has=["arm F", "named-other condition"]),
    "toy-step5a-seed1": dict(sentence_has=["arm F", "named-other condition", "step 5a"]),
    "T-fails-gate": dict(sentence_has=["arm T", "own-directed condition"]),
    "F-fails-5a": dict(sentence_has=["arm F", "named-other condition", "step 5a"]),
    "r2": dict(sentence_has=["metric does not separate on these constructed systems, "
                             "for this intervention procedure"]),
}



# ---------------------------------------------------------------------------
# The in-use check on the built arms (John's ruling of 2026-10-06, option 4;
# method `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 3,
# cases 18 to 20; expectations written there before this ran).
#
# The committed toy rows predate the check, so a2_run_cases.py gives every
# built-arm row a passing `route_in_use` (ROUTE_PASS) before a case's own
# changes, and the 25 cases above keep testing what they tested.

ROUTE_PASS = dict(sharpness=4.0, weight_on_true_agent=0.999, made_up=True,
                  routes={"entangled": dict(actions=3000, right_with_true_answer=2000,
                                            still_right_with_swapped_answer=100, route_use=0.95)})


def route_flat(rows, arm, seed):
    r = dict(ROUTE_PASS, routes={"entangled": dict(actions=3000, right_with_true_answer=2000,
                                                   still_right_with_swapped_answer=1990,
                                                   route_use=0.005)})
    rows[(arm, seed)]["gate"]["route_in_use"] = r


def c_inuse_C(rows):
    make_F_read(rows)
    route_flat(rows, "C", 0)
    route_flat(rows, "C", 1)


def c_inuse_T(rows):
    make_F_read(rows)
    route_flat(rows, "T", 0)
    route_flat(rows, "T", 1)


def c_inuse_M(rows):
    make_F_read(rows)
    route_flat(rows, "M", 0)
    route_flat(rows, "M", 1)


CASES += [
    dict(name="inuse-C-flat", build=c_inuse_C, steps={"arm_F_step_5a_seed": 0},
         expect="fallback_read",
         seed_reasons_have={"C/0": ["construction did not hold"], "C/1": ["construction did not hold"]},
         withheld=[("C", 0), ("C", 1)],
         about="in-use check: every arm reads (as case r1) but arm C's route is flat on seeds 0 and 1"),
    dict(name="inuse-T-flat", build=c_inuse_T, steps={"arm_F_step_5a_seed": 0},
         expect="not_validated", reason_has=["construction did not hold"],
         withheld=[("T", 0), ("T", 1)],
         about="in-use check: arm T's route is flat on seeds 0 and 1"),
    dict(name="inuse-M-flat", build=c_inuse_M, steps={"arm_F_step_5a_seed": 0},
         expect="R1",
         seed_reasons_have={"M/0": ["construction did not hold"], "M/1": ["construction did not hold"]},
         withheld=[("M", 0), ("M", 1)],
         about="in-use check: arm M's route is flat on seeds 0 and 1; arm M has no verdict, outcome unchanged"),
]
