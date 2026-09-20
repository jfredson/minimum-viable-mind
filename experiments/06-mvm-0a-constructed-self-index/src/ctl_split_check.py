#!/usr/bin/env python3
"""ctl_split_check.py — the two $0 closures from the control-learnability
pilot review of 2026-09-20.

UNREGISTERED, AND NOTHING REGISTERED IS TOUCHED. Amendment A3 registers
the grammar (`curriculum_a3.py`), the tokenizer (`encoding_a3.py`), the
trainer (`train_a3.py`), the frozen batteries, the gates, the calibration,
the lock guard and the launcher. This file is a new, separate reader. It
imports those modules and calls them; it changes nothing in them. That is
why the one-scored-token test lives here and not inside the trainer's own
`--self-test`, which would have meant editing registered text to check a
claim registered text makes.

WHAT THE TWO CHECKS ARE (red-team ledger rows, control-learnability pilot
review, PR 7):

  RT-58, the fixed positional split. Under the pilot flag the control
  battery's rows are the FIRST half of every batch -- `training_pairs`
  marks rows `0 .. n_ctl-1` as control rows and gives them the control
  query. That is a fixed positional split, and nobody had ever checked
  whether position in the batch carries information about the episode. If
  it does, the control battery was trained on a systematically different
  slice of the distribution from the one the other batteries saw, and the
  pilot's headline number is about that slice rather than about the
  battery. Ruled closure: "a $0 local check of episode order against the
  split, filed as a findings note."

  RT-59, the one-scored-token assumption. `loss_a3` sums the per-token
  cross-entropy across each row's positions and calls the result that
  row's answer cross-entropy. That step is only valid if every row has
  EXACTLY ONE scored token; the code says so in a comment and never
  tested it. If a row ever carried two, its loss would be double-counted
  and its weight in the split term silently doubled. Ruled closure:
  "one-line self-test, $0."

HOW THE PILOT'S BATCHES ARE REPRODUCED, EXACTLY. The training loop builds
each step's batch like this:

    eps = A.generate_balanced(batch, seed=seed * 10**6 + step)
    eps, act = enact_batched(model, eps, device,
                             random.Random(seed * 10**6 + step), grad=True)
    pairs, ctl_rows = training_pairs(eps, step, ctl_weight, ctl_frac)
    batch = to_torch(E.collate([E.encode_episode(e, query=q)
                                for e, q in pairs]), device)

`enact_batched` is `A.enact_own_turns` over the episodes in order, then
the acting-channel injection. Only the second half needs a model, and the
injection changes neither the episodes, nor the queries, nor the loss
mask. So everything both checks look at is reproducible on a laptop with
no model and no checkpoint, bit for bit, by replaying the same two seeds.
That is what makes this $0, and it is why the sweep below runs over EVERY
step the pilot trained rather than a sample of them.

The pilot's settings, from `launch_ctl_pilot.sh` and the run's own log:
seed 0, batch 128, ctl-weight 2.0, ctl-frac 0.5, 55,116 steps.

THE DECISION RULE, PRE-STATED (written and committed before the sweep was
run, per the house rule that method is committed before output).

A significance test is the wrong instrument at this sample size and is
reported only for completeness: the full sweep compares about 3.5 million
rows against 3.5 million, where a difference far too small to matter is
certain to clear any p-value bar. The finding is read off EFFECT SIZE
against a bar fixed in advance:

  * categorical properties -- Cramer's V below 0.01 is no material bias.
  * continuous properties -- |Cohen's d| below 0.02 is no material bias.

Anything above its bar is reported as a real difference between the two
halves whatever its p-value, and anything below it is reported as no
material bias whatever its p-value. Significance is also reported, at a
Bonferroni-adjusted 0.05 over the number of properties tested.

A structural result outranks both. The properties are a finite list and
cannot prove the absence of every possible bias; the structural checks
(S1 to S4 below) are exact statements about the code and hold for every
batch, not on average.

Usage:
    python ctl_split_check.py --self-test        # the module's own tests
    python ctl_split_check.py --scored-token     # RT-59
    python ctl_split_check.py --split            # RT-58 (full sweep)
    python ctl_split_check.py --all --out ../a3-gates
"""
from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

import curriculum_a3 as A
import encoding_a3 as E
import train_a3 as T
from model import MVM0aModel, Config, SCALES, to_torch

# The pilot, as launched. Not defaults to be edited -- the run these
# checks are about used exactly these.
PILOT = {"seed": 0, "batch": 128, "ctl_weight": 2.0, "ctl_frac": 0.5,
         "steps": 55116}

# Pre-stated bars. See the module docstring.
V_BAR = 0.01          # Cramer's V, categorical
D_BAR = 0.02          # Cohen's d, continuous
ALPHA = 0.05


# ---------------------------------------------------------------- stats
# torch only: the repo carries no scipy and this check does not add one.

def chi2_sf(x: float, df: int) -> float:
    """Upper tail of the chi-square distribution."""
    if x <= 0:
        return 1.0
    return float(torch.special.gammaincc(torch.tensor(df / 2.0),
                                         torch.tensor(x / 2.0)))


def normal_sf2(z: float) -> float:
    """Two-sided tail of the standard normal."""
    return math.erfc(abs(z) / math.sqrt(2.0))


def chi2_table(counts: list[list[int]]) -> tuple[float, int, float, float]:
    """Chi-square on a 2 x k contingency table of half against category.

    Returns (statistic, degrees of freedom, p, Cramer's V). Columns with
    no observations on either side are dropped -- they carry no
    information and would otherwise make the degrees of freedom a lie.
    """
    cols = [j for j in range(len(counts[0]))
            if counts[0][j] + counts[1][j] > 0]
    obs = [[counts[i][j] for j in cols] for i in (0, 1)]
    n = sum(sum(r) for r in obs)
    if n == 0 or len(cols) < 2:
        return 0.0, 0, 1.0, 0.0
    rows = [sum(r) for r in obs]
    colsum = [obs[0][j] + obs[1][j] for j in range(len(cols))]
    stat = 0.0
    for i in (0, 1):
        for j in range(len(cols)):
            exp = rows[i] * colsum[j] / n
            if exp > 0:
                stat += (obs[i][j] - exp) ** 2 / exp
    df = len(cols) - 1                      # (2-1) * (k-1)
    # Cramer's V with min(rows-1, cols-1) = 1 for a 2 x k table
    v = math.sqrt(stat / n)
    return stat, df, chi2_sf(stat, df), v


def welch(sum1, sq1, n1, sum2, sq2, n2) -> tuple[float, float, float]:
    """Welch's t from running sums, plus Cohen's d on the pooled sd."""
    if n1 < 2 or n2 < 2:
        return 0.0, 1.0, 0.0
    m1, m2 = sum1 / n1, sum2 / n2
    v1 = max(sq1 / n1 - m1 * m1, 0.0) * n1 / (n1 - 1)
    v2 = max(sq2 / n2 - m2 * m2, 0.0) * n2 / (n2 - 1)
    se = math.sqrt(v1 / n1 + v2 / n2)
    if se == 0.0:
        return 0.0, 1.0, 0.0
    t = (m1 - m2) / se
    pooled = math.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    d = (m1 - m2) / pooled if pooled > 0 else 0.0
    # normal approximation to the t tail: df here is in the millions
    return t, normal_sf2(t), d


# ------------------------------------------------------- batch replay

def replay(step: int, seed: int, batch: int, ctl_weight: float,
           ctl_frac: float):
    """Rebuild one training step's episodes, queries and control flags
    exactly as the trainer built them. No model, no checkpoint."""
    eps = A.generate_balanced(batch, seed=seed * 10 ** 6 + step)
    rng = random.Random(seed * 10 ** 6 + step)
    for e in eps:
        A.enact_own_turns(e, rng)
    pairs, flags = T.training_pairs(eps, step, ctl_weight, ctl_frac)
    return eps, pairs, flags


# ------------------------------------------------------------- RT-59

def scored_token_check(n_steps: int, seed: int, batch: int,
                       ctl_weight: float, ctl_frac: float) -> dict:
    """Every row of every batch carries exactly one scored token.

    Four claims, each of which has to hold on every row:

      B1  the collated loss mask has exactly one 1 per row.
      B2  the SHIFTED mask `loss_mask[:, 1:]`, which is the one `loss_a3`
          actually sums over, also has exactly one 1 per row. B1 does not
          imply B2: a mask whose single 1 sat at index 0 would satisfy B1
          and vanish under the shift, leaving that row scored on nothing
          and silently dropped from its half of the split.
      B3  the token being scored is the query's own answer token, so the
          per-row sum is that row's ANSWER cross-entropy and not some
          other token's.
      B4  the numerical identity the comment relies on: when every row
          has exactly one scored token, the registered pooled query term
          equals the mean of the per-row terms. Checked by running the
          real `loss_a3` both ways on the same batch -- the registered
          path (`ctl_weight = 0`) against the split path with every row
          marked as a control row at weight 1.0, which reduces to that
          mean. This is the claim the comment makes, tested end to end
          through the code that makes it rather than restated.

    B1 to B3 need no model. B4 does, and uses an untrained smoke-scale
    model on the CPU -- the loss path under test does not care what the
    weights are.
    """
    rows = worst = 0
    b1 = b2 = b3 = True
    first_fail = None
    t0 = time.time()
    for step in range(1, n_steps + 1):
        _, pairs, _ = replay(step, seed, batch, ctl_weight, ctl_frac)
        enc = [E.encode_episode(e, query=q) for e, q in pairs]
        col = E.collate(enc)
        m = col["loss_mask"]
        per_row = m.sum(axis=1)
        worst = max(worst, int(per_row.max()), 1) if len(per_row) else worst
        if not (per_row == 1).all():
            b1 = False
            first_fail = first_fail or ("B1", step)
        shifted = m[:, 1:].sum(axis=1)
        if not (shifted == 1).all():
            b2 = False
            first_fail = first_fail or ("B2", step)
        for j, (_, q) in enumerate(pairs):
            pos = int(m[j].argmax())
            if E.IVOCAB[int(col["input_ids"][j, pos])] != q.answer:
                b3 = False
                first_fail = first_fail or ("B3", step)
                break
        rows += len(pairs)

    # B4: the identity, through the real loss function
    cfg = Config(**{**SCALES["smoke"].__dict__, "vocab": len(E.VOCAB),
                    "max_len": 512})
    torch.manual_seed(0)
    model = MVM0aModel(cfg).eval()
    eps, pairs, _ = replay(1, seed, 32, ctl_weight, ctl_frac)
    bt = to_torch(E.collate([E.encode_episode(e, query=q)
                             for e, q in pairs]), "cpu")
    act = T.compute_act_inject(model, eps, "cpu", grad=False)
    act = F.pad(act, (0, 0, 0, bt["input_ids"].shape[1] - act.shape[1]))
    ones = torch.ones(len(pairs), dtype=torch.long)
    with torch.no_grad():
        _, q_pooled, _ = T.loss_a3(model, bt, act, 1.0,
                                   ctl_rows=None, ctl_weight=0.0)
        _, q_rowmean, _ = T.loss_a3(model, bt, act, 1.0,
                                    ctl_rows=ones, ctl_weight=1.0)
    b4 = bool(torch.allclose(q_pooled, q_rowmean, atol=1e-6))

    return {
        "ledger_row": "RT-59",
        "claim": "exactly one scored token per row",
        "steps_checked": n_steps,
        "rows_checked": rows,
        "batch": batch,
        "max_scored_tokens_seen_on_any_row": worst,
        "B1_one_masked_token_per_row": b1,
        "B2_survives_the_shift_loss_a3_applies": b2,
        "B3_scored_token_is_the_query_answer": b3,
        "B4_pooled_equals_mean_of_per_row": b4,
        "pooled_q": round(float(q_pooled), 6),
        "row_mean_q": round(float(q_rowmean), 6),
        "first_failure": first_fail,
        "verdict": ("HOLDS" if (b1 and b2 and b3 and b4) else "FAILS"),
        "seconds": round(time.time() - t0, 1),
    }


# ------------------------------------------------------------- RT-58

def split_check(n_steps: int, seed: int, batch: int, ctl_weight: float,
                ctl_frac: float, progress: int = 5000) -> dict:
    """Episode order against the fixed positional split.

    Structural checks, exact and on every batch:

      S1  `generate_balanced` emits episodes in MATCHED CONTENT PAIRS:
          one content seed, the owning slot rotated, appended
          back-to-back. So rows 2k and 2k+1 are the same episode content
          with a different agent being the model. This is the crossing
          RT-11 asked for, and it is what makes batch position
          non-random in the first place.
      S2  the split boundary never cuts a pair. n_ctl = round(128 * 0.5)
          = 64 is EVEN, so pairs fall wholly inside one half or the
          other, and the ownership crossing is preserved separately
          within the control half and within the rest. This is the
          hinge: an odd n_ctl would split pairs and could hand the
          control battery a different mix of own-slots than the other
          batteries saw.
      S3  the control half really does hold n_ctl rows -- no episode
          falls through the `and ctl` guard in `training_pairs` for want
          of a control query.
      S4  every control row carries a control-battery query and no other
          row does.

    Then eight episode properties, compared between the two halves and
    read against the pre-stated effect-size bars.
    """
    seen = 0
    # categorical accumulators: name -> [half][category] -> count
    cat: dict[str, list[list[int]]] = {
        "own_slot": [[0] * A.N_AGENTS for _ in (0, 1)],
        "model_revises": [[0] * 2 for _ in (0, 1)],
        "ctl_answer_slot": [[0] * len(A.SLOTS) for _ in (0, 1)],
        "ctl_item_rank": [[0] * 8 for _ in (0, 1)],
        "ctl_named_agent_offset": [[0] * A.N_AGENTS for _ in (0, 1)],
        "ctl_named_agent_revised": [[0] * 2 for _ in (0, 1)],
        "state_query_variant": [[0] * 2 for _ in (0, 1)],
    }
    # continuous accumulators: name -> [half] -> [sum, sumsq, n]
    con: dict[str, list[list[float]]] = {
        "n_turns": [[0.0, 0.0, 0.0] for _ in (0, 1)],
        "n_tokens": [[0.0, 0.0, 0.0] for _ in (0, 1)],
    }
    s1 = s2 = s3 = s4 = True
    n_ctl_expected = int(round(batch * ctl_frac))
    pair_straddles = 0
    t0 = time.time()

    for step in range(1, n_steps + 1):
        eps, pairs, flags = replay(step, seed, batch, ctl_weight, ctl_frac)
        fl = flags.tolist()

        # S3 / S4
        if sum(fl) != n_ctl_expected:
            s3 = False
        for (_, q), f in zip(pairs, fl):
            if bool(f) != (q.battery == T.CONTROL_BATTERY):
                s4 = False

        # S1 / S2: pairs are adjacent, and the boundary sits between them
        for k in range(0, len(eps) - 1, 2):
            if eps[k].seed != eps[k + 1].seed:
                s1 = False
            if fl[k] != fl[k + 1]:
                s2 = False
                pair_straddles += 1

        lens = [len(e["input_ids"])
                for e in (E.encode_episode(e, query=q) for e, q in pairs)]

        for i, ((e, q), f) in enumerate(zip(pairs, fl)):
            h = 0 if f else 1
            cat["own_slot"][h][e.own_slot] += 1
            cat["model_revises"][h][int(A.has_own_revision(e))] += 1
            ctl_q = next(x for x in e.queries
                         if x.battery == T.CONTROL_BATTERY)
            cat["ctl_answer_slot"][h][A.SLOTS.index(ctl_q.answer)] += 1
            # which contested item the control query asks about, by its
            # rank in the episode's own contested list
            item = next((it for it in e.contested if it in ctl_q.text),
                        None)
            if item is not None:
                cat["ctl_item_rank"][h][e.contested.index(item) % 8] += 1
            named = next((a for a in range(e.n_agents)
                          if e.markers[a] in ctl_q.text), None)
            if named is not None:
                cat["ctl_named_agent_offset"][h][
                    (named - e.own_slot) % A.N_AGENTS] += 1
                cat["ctl_named_agent_revised"][h][
                    int(e.revises.get(named) is not None)] += 1
            st = next((x for x in e.queries if x.battery == "T_state"),
                      None)
            if st is not None:
                cat["state_query_variant"][h][
                    int(st.text.startswith("how many"))] += 1
            for name, val in (("n_turns", float(len(e.turns))),
                              ("n_tokens", float(lens[i]))):
                con[name][h][0] += val
                con[name][h][1] += val * val
                con[name][h][2] += 1
            seen += 1

        if progress and step % progress == 0:
            print(f"  step {step}/{n_steps} "
                  f"({time.time() - t0:.0f}s)", flush=True)

    n_tests = len(cat) + len(con)
    bar = ALPHA / n_tests
    props = {}
    worst_v = worst_d = 0.0
    for name, counts in cat.items():
        stat, df, p, v = chi2_table(counts)
        worst_v = max(worst_v, v)
        props[name] = {
            "kind": "categorical", "chi2": round(stat, 3), "df": df,
            "p": p, "cramers_v": round(v, 6),
            "control_half": counts[0], "other_half": counts[1],
            "material": bool(v >= V_BAR),
            "significant_at_adjusted_bar": bool(p < bar),
        }
    for name, acc in con.items():
        t, p, d = welch(acc[0][0], acc[0][1], acc[0][2],
                        acc[1][0], acc[1][1], acc[1][2])
        worst_d = max(worst_d, abs(d))
        props[name] = {
            "kind": "continuous", "t": round(t, 3), "p": p,
            "cohens_d": round(d, 6),
            "control_half_mean": round(acc[0][0] / max(acc[0][2], 1), 4),
            "other_half_mean": round(acc[1][0] / max(acc[1][2], 1), 4),
            "n_control": int(acc[0][2]), "n_other": int(acc[1][2]),
            "material": bool(abs(d) >= D_BAR),
            "significant_at_adjusted_bar": bool(p < bar),
        }

    structural = bool(s1 and s2 and s3 and s4)
    material = [k for k, v in props.items() if v["material"]]
    return {
        "ledger_row": "RT-58",
        "claim": "the fixed positional split is not biased",
        "pilot": {"seed": seed, "batch": batch, "ctl_weight": ctl_weight,
                  "ctl_frac": ctl_frac},
        "steps_checked": n_steps,
        "rows_checked": seen,
        "n_ctl_per_batch": n_ctl_expected,
        "n_ctl_is_even": n_ctl_expected % 2 == 0,
        "S1_content_pairs_are_adjacent": s1,
        "S2_boundary_never_cuts_a_pair": s2,
        "S3_control_half_is_full": s3,
        "S4_control_rows_carry_the_control_query": s4,
        "pair_straddles": pair_straddles,
        "prestated_bars": {"cramers_v": V_BAR, "cohens_d": D_BAR,
                           "adjusted_alpha": bar, "n_tests": n_tests},
        "max_cramers_v": round(worst_v, 6),
        "max_abs_cohens_d": round(worst_d, 6),
        "properties": props,
        "material_differences": material,
        "verdict": ("NO MATERIAL BIAS" if structural and not material
                    else "BIAS FOUND"),
        "seconds": round(time.time() - t0, 1),
    }


# --------------------------------------------------------- self-test

def self_test() -> None:
    """This module's own tests. Cheap, and they run before the sweep."""
    # the statistics agree with known values
    assert abs(chi2_sf(7.8147, 3) - 0.05) < 1e-4
    assert abs(normal_sf2(1.95996) - 0.05) < 1e-4
    # a table with no association gives V = 0 and p = 1
    _, _, p, v = chi2_table([[100, 100], [100, 100]])
    assert v < 1e-9 and p > 0.99
    # a table that is pure association gives V = 1
    _, _, _, v = chi2_table([[100, 0], [0, 100]])
    assert abs(v - 1.0) < 1e-9
    # empty columns are dropped rather than inflating the degrees of freedom
    _, df, _, _ = chi2_table([[10, 0, 10], [10, 0, 10]])
    assert df == 1, df
    # Welch on identical samples is t = 0, d = 0
    t, p, d = welch(100.0, 200.0, 100, 100.0, 200.0, 100)
    assert abs(t) < 1e-9 and abs(d) < 1e-9 and p > 0.99

    # the replay really does reproduce the trainer's own construction
    seed, step, bs = PILOT["seed"], 7, 32
    eps_a = A.generate_balanced(bs, seed=seed * 10 ** 6 + step)
    rng_a = random.Random(seed * 10 ** 6 + step)
    for e in eps_a:
        A.enact_own_turns(e, rng_a)
    pairs_a, flags_a = T.training_pairs(eps_a, step, 2.0, 0.5)
    _, pairs_b, flags_b = replay(step, seed, bs, 2.0, 0.5)
    assert [q.text for _, q in pairs_a] == [q.text for _, q in pairs_b]
    assert [q.answer for _, q in pairs_a] == [q.answer for _, q in pairs_b]
    assert flags_a.tolist() == flags_b.tolist()

    # the replay is deterministic: the same step twice is the same batch
    _, pairs_c, _ = replay(step, seed, bs, 2.0, 0.5)
    assert [q.answer for _, q in pairs_b] == [q.answer for _, q in pairs_c]

    # a two-step scored-token check passes on a real batch
    r = scored_token_check(2, seed, 32, 2.0, 0.5)
    assert r["verdict"] == "HOLDS", r

    # a two-step split check runs and reports the structure
    s = split_check(2, seed, 32, 2.0, 0.5, progress=0)
    assert s["S1_content_pairs_are_adjacent"] is True
    assert s["S3_control_half_is_full"] is True
    assert s["S4_control_rows_carry_the_control_query"] is True

    # THE NEGATIVE CONTROL. The bias check must be able to SEE a bias, or
    # a clean result means nothing. An odd n_ctl cuts content pairs at
    # the boundary, which is the exact failure S2 is there to catch.
    odd = split_check(2, seed, 32, 2.0, 0.53, progress=0)
    assert int(round(32 * 0.53)) % 2 == 1, "the control must be odd"
    assert odd["S2_boundary_never_cuts_a_pair"] is False, \
        "an odd split must be caught, or the check cannot fail"
    assert odd["pair_straddles"] > 0

    print("ctl_split_check self-test OK", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--split", action="store_true", help="RT-58")
    ap.add_argument("--scored-token", action="store_true", help="RT-59")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--steps", type=int, default=PILOT["steps"],
                    help="how many of the pilot's steps to replay")
    ap.add_argument("--scored-token-steps", type=int, default=2000,
                    help="steps for the RT-59 sweep (it also encodes)")
    ap.add_argument("--out", type=str, default="")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        if not (args.split or args.scored_token or args.all):
            return

    out = Path(args.out) if args.out else None
    if args.scored_token or args.all:
        r = scored_token_check(args.scored_token_steps, PILOT["seed"],
                               PILOT["batch"], PILOT["ctl_weight"],
                               PILOT["ctl_frac"])
        print(json.dumps(r, indent=2), flush=True)
        if out:
            (out / "ctl_scored_token_selftest.json").write_text(
                json.dumps(r, indent=2) + "\n")
    if args.split or args.all:
        r = split_check(args.steps, PILOT["seed"], PILOT["batch"],
                        PILOT["ctl_weight"], PILOT["ctl_frac"])
        print(json.dumps(r, indent=2), flush=True)
        if out:
            (out / "ctl_split_bias_check.json").write_text(
                json.dumps(r, indent=2) + "\n")


if __name__ == "__main__":
    main()
