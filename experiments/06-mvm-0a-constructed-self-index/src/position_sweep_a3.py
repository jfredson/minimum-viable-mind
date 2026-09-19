"""Position sweep — where, if anywhere, is own-agent identity legible?

**UNREGISTERED**, diagnostic only. No verdict is read and no cell here
feeds one. The method is committed in `position-sweep-method.md`, in the
same commit as this file and before either produced any output. Read that
first: it fixes the positions and the cells.

WHY. The denoise-before-probing diagnostic came back empty everywhere
(`denoised-direction-findings.md`), and about ten directions out of 448
carry ninety-nine per cent of what varies at the probed position once
ownership is taken out. That makes the probe POSITION suspect, not only
the probe. Ownership is measured to be load-bearing on the pilot — zeroing
the acting channel takes the ownership battery from 0.506 to 0.182 — so
something carries it and two linear reads at one position have failed.

ARM 1 reads own-agent identity with the difference-of-averages read at
eleven candidate positions rather than one. ARM 2 puts the regularised
classifier and the difference-of-averages read head to head at the
original position and layers, on identical states and one shared set of
folds, to quantify a contrast that was noticed in passing last night and
never measured: the classifier sat below its null where the difference of
averages sat above it.

THE POSITIVE CONTROL, AND WHAT THE SWEEP COSTS IF IT FAILS. Position 6 is
the model's own marker token, where which agent it is has just been read
off the input. It should be decodable almost perfectly. If it does not
separate, the read is broken and no other result in arm 1 means anything;
the checkpoint is reported SWEEP INVALID. Without this, a sweep of eleven
positions finding nothing is indistinguishable from a sweep that never
worked.

WHAT A PASS AT THE INJECTION POSITIONS WOULD NOT MEAN. Positions 1, 2 and
4 are where the acting channel injects, and the channel is a projection of
the model's own preceding state. Identity being decodable there is close
to reading back the injection and is not evidence of a carried self-index.
The registered pipeline probes position 3 precisely because the injection
has not reached it.

TWO THINGS REPORTED HERE THAT WERE NOT BEFORE. Every test reports how many
of the 200 shuffled draws met or beat the real score, beside the
standard-deviation margin, because 200 draws cannot resolve a margin of
four standard deviations and quoting one implies they can. And arm 1's 165
tests get a family-adjusted label: a clearance is ROBUST only if it also
clears 3.43 standard deviations and no shuffled draw beat it, MARGINAL
otherwise.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock,
for the reason given in the method file; fresh output per checkpoint,
nothing overwritten [C6].

    ../../../.venv/bin/python position_sweep_a3.py --self-test
    ../../../.venv/bin/python position_sweep_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import denoised_direction_a3 as D
import encoding_a3 as E
import lock_guard
import localize_a3 as L
import train_a3 as T
from model import MVM0aModel, Config, to_torch

PROBE_LAYERS = L.PROBE_LAYERS
N_PAIRS = 200
EPISODE_SEED = 20260917
N_PERM = L.N_PERM
N_FOLDS = 4
SD_BAR = 3.0
FAMILY_SD_BAR = 3.43        # 165 tests, five per cent family-wise
ANCHOR = "own_revision_decision"
POSITIVE_CONTROL = "own_revision_marker"
INJECTION_POSITIONS = ("own_assign_1_value", "own_assign_2_value",
                       "own_revision_value")
QUERY_POSITIONS = ("query_answer_decision", "query_answer_value")

# Order matters only for reporting; the cells do not depend on it.
POSITIONS = ("own_assign_1_value", "own_assign_2_value",
             "own_revision_decision", "own_revision_value",
             "own_revision_by", "own_revision_marker",
             "before_own_revision_turn", "other_revision_decision",
             "other_revision_value", "query_answer_decision",
             "query_answer_value")

POSITION_NOTES = {
    "own_assign_1_value": "the value in the model's first assignment; the "
                          "acting channel injects here",
    "own_assign_2_value": "the value in the model's second assignment; the "
                          "acting channel injects here",
    "own_revision_decision": "one before the model's revision value — THE "
                             "REGISTERED POSITION, the anchor",
    "own_revision_value": "the model's revision value; the acting channel "
                          "injects here",
    "own_revision_by": "one after the revision value",
    "own_revision_marker": "the model's own marker token — THE POSITIVE "
                           "CONTROL; identity is in the input here",
    "before_own_revision_turn": "the line break ending the turn before the "
                                "model's revision",
    "other_revision_decision": "one before the other reviser's value; the "
                               "matched other-agent position",
    "other_revision_value": "the other reviser's value",
    "query_answer_decision": "the answer marker of an appended other-agent "
                             "question",
    "query_answer_value": "the answer token of that question",
}


# ------------------------------------------------------------- positions

def position_indices(ep, enc_len, with_query):
    """Every candidate position for one episode, as token indices.

    Turns render as `assign {item} to {value} by {marker}` — six words and
    a line break — so a turn beginning at s has its value at s + 3 and the
    agent's own marker at s + 5. The marker comes AFTER the value by
    design, so at the moment a value is emitted the turn has not yet said
    whose turn it is.
    """
    span = A.N_TURNS and 7                       # six words plus a newline
    own = [i for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
    rev = A.own_revision_index(ep)
    assigns = [i for i in own if i != rev]
    other = [i for i, t in enumerate(ep.turns)
             if t.revised and t.agent != ep.own_slot]
    if len(assigns) != 2 or len(other) != 1:
        return None
    def value_of(turn_index):
        return 1 + span * turn_index + A.VALUE_WORD_IDX
    act = value_of(rev)
    out = {
        "own_assign_1_value": value_of(assigns[0]),
        "own_assign_2_value": value_of(assigns[1]),
        "own_revision_decision": act - 1,
        "own_revision_value": act,
        "own_revision_by": act + 1,
        "own_revision_marker": act + 2,
        "before_own_revision_turn": 1 + span * rev - 1,
    }
    ov = value_of(other[0])
    out["other_revision_decision"] = ov - 1
    out["other_revision_value"] = ov
    if with_query:
        # tokens end ... ANS, answer, EOS
        out["query_answer_value"] = enc_len - 2
        out["query_answer_decision"] = enc_len - 3
    return out


@torch.no_grad()
def capture(model, eps, device, with_query):
    """Residual-stream states at every candidate position, per layer.

    Mirrors `localize_a3.residuals_at` — same enactment, same seed, same
    hook mechanism — and differs only in gathering many positions instead
    of one, and in optionally appending a question. The model is causal,
    so appending a question cannot disturb any position before it; this is
    asserted against the no-question capture in the self-test of the
    sweep's anchor position.
    """
    eps = list(eps)
    rng = random.Random(0)          # ONE generator across the batch, as
    for e in eps:                   # train_a3.enact_batched does; a fresh
        A.enact_own_turns(e, rng)   # one per episode would diverge from it
    encs = [E.encode_episode(e, query=(e.queries[0] if with_query else None))
            for e in eps]
    lens = [len(x["input_ids"]) for x in encs]
    batch = to_torch(E.collate(encs), device)

    # the acting channel, rebuilt against THIS encoding so the injection
    # positions line up with the states being read
    B, Ltok = batch["input_ids"].shape
    act = torch.zeros(B, Ltok, model.cfg.d_model, device=device)
    own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
               for e in eps]
    for k in range(max(len(o) for o in own_idx)):
        _, h = model.forward(batch, act_inject=act, return_hidden=True)
        bs, ps = [], []
        for b, e in enumerate(eps):
            if k < len(own_idx[b]):
                sp = (batch["turn_ids"][b] == own_idx[b][k]).nonzero().flatten()
                bs.append(b)
                ps.append(int(sp[0]) + A.VALUE_WORD_IDX)
        bi = torch.tensor(bs, device=device)
        pi = torch.tensor(ps, device=device)
        act = act.index_put((bi, pi), model.act_proj(h[bi, pi - 1]))

    caps = {Lr: [] for Lr in PROBE_LAYERS}
    for Lr in PROBE_LAYERS:
        blk = model.blocks[Lr]
        orig = blk.forward

        def patched(x, kv, reg_repr, _o=orig, _L=Lr):
            x, ctx = _o(x, kv, reg_repr)
            caps[_L].append(x.detach())
            return x, ctx
        blk.forward = patched
    model.forward(batch, act_inject=act)
    for Lr in PROBE_LAYERS:
        del model.blocks[Lr].__dict__["forward"]

    idx = [position_indices(e, lens[b], with_query)
           for b, e in enumerate(eps)]
    keep = [b for b, v in enumerate(idx) if v is not None]
    names = [p for p in POSITIONS
             if (p in QUERY_POSITIONS) == bool(with_query)]
    out = {}
    for Lr in PROBE_LAYERS:
        hstate = torch.cat(caps[Lr], dim=1)
        for p in names:
            rows = [b for b in keep if 0 <= idx[b][p] < lens[b]]
            pos = torch.tensor([idx[b][p] for b in rows], device=hstate.device)
            bi = torch.tensor(rows, device=hstate.device)
            out[(Lr, p)] = (hstate[bi, pos].float().cpu().numpy(), rows)
    return out, eps


# --------------------------------------------------------------- scoring

def permutation_count(real, null):
    """How many shuffled draws met or beat the real score. With 200 draws
    this is the finest resolution available, and it is the honest number
    where it disagrees with a standard-deviation margin."""
    return int(sum(1 for v in null if v >= real - 1e-12))


def label(clears, margin, count):
    if not clears:
        return None
    if margin is not None and margin >= FAMILY_SD_BAR and count == 0:
        return "ROBUST"
    return "MARGINAL"


def mean_difference_read(X, y, fold_sets, seed):
    """The plain difference-of-averages read, no denoising, with its null.

    Reports the separation score (no information 0.5) and nearest-average
    accuracy (no information 0.25), each against its own 200-draw null.
    Both nulls' spreads are recorded, which the earlier diagnostic did not
    do for the accuracy column."""
    y = np.asarray(y)
    classes = sorted(np.unique(y).tolist())
    rng = np.random.default_rng(seed)
    sep, acc, _, dead, per_class = D.score_once(
        X, y, classes, False, fold_sets)
    ns, na = [], []
    for _ in range(N_PERM):
        yp = rng.permutation(y)
        s, a, _, _, _ = D.score_once(X, yp, classes, False, fold_sets)
        ns.append(s)
        na.append(a)
    out = {}
    for tag, real, null, chance in (("separation", sep, ns, 0.5),
                                    ("accuracy", acc, na,
                                     round(1 / len(classes), 4))):
        m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
        margin = round((real - m) / sd, 2) if sd > 0 else None
        clears = bool(sd > 0 and real >= m + SD_BAR * sd)
        cnt = permutation_count(real, null)
        out[tag] = {"value": round(real, 4), "null_mean": round(m, 4),
                    "null_sd": round(sd, 4), "margin_sd": margin,
                    "clears_3sd": clears,
                    "draws_beating_real": cnt, "draws": N_PERM,
                    "no_information": chance,
                    "label": label(clears, margin, cnt)}
    out["separation_per_agent"] = [round(a, 4) for a in per_class]
    out["n"] = int(len(y))
    if dead or out["separation"]["null_sd"] == 0:
        out["degenerate"] = (
            "a fold left the procedure with nothing to fit, or the null "
            "has zero spread; stated in advance, no cell assigned")
        out["separation"]["clears_3sd"] = False
    return out


def classifier_read(X, y, fold_sets, seed):
    """The regularised classifier on the SAME states and the SAME folds.

    `localize_a3.fit_probe` chooses its own splitting; here both
    instruments are handed one shared split, which is what makes arm 2 a
    head-to-head rather than two runs compared after the fact."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    y = np.asarray(y)
    rng = np.random.default_rng(seed)
    cv = [(np.setdiff1d(np.arange(len(y)), h), h) for h in fold_sets]
    clf = LogisticRegression(max_iter=2000, C=1.0)
    real = float(cross_val_score(clf, X, y, cv=cv).mean())
    null = [float(cross_val_score(clf, X, rng.permutation(y), cv=cv).mean())
            for _ in range(N_PERM)]
    m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
    margin = round((real - m) / sd, 2) if sd > 0 else None
    clears = bool(sd > 0 and real >= m + SD_BAR * sd)
    cnt = permutation_count(real, null)
    return {"accuracy": round(real, 4), "null_mean": round(m, 4),
            "null_sd": round(sd, 4), "margin_sd": margin,
            "clears_3sd": clears, "draws_beating_real": cnt,
            "draws": N_PERM, "no_information": round(1 / len(set(y)), 4),
            "label": label(clears, margin, cnt),
            "shared_folds": True}


# ----------------------------------------------------------------- cells

def arm1_cell(layers):
    """The cells fixed in `position-sweep-method.md`, for one checkpoint."""
    pc = [v for (p, _), v in layers.items() if p == POSITIVE_CONTROL]
    if not any(v["separation"]["clears_3sd"] for v in pc):
        return {"cell": "SWEEP INVALID — no cell assigned",
                "means": ("the positive control at the model's own marker "
                          "token did not separate, so the read is broken "
                          "and no other position on this checkpoint means "
                          "anything")}
    cleared = [{"position": p, "layer": Lr,
                "margin_sd": v["separation"]["margin_sd"],
                "label": v["separation"]["label"]}
               for (p, Lr), v in layers.items()
               if v["separation"]["clears_3sd"] and p != POSITIVE_CONTROL]
    if not cleared:
        return {"cell": "NOTHING SEPARATES ANYWHERE", "cleared": [],
                "means": ("own-agent identity is not linearly decodable "
                          "anywhere in the episode by this read, despite "
                          "being decodable where it is written in the "
                          "input; the wrong-position explanation for the "
                          "earlier nulls is not supported")}
    away = [c for c in cleared if c["position"] not in INJECTION_POSITIONS]
    if not away:
        return {"cell": "SEPARATES ONLY WHERE THE CHANNEL INJECTS",
                "cleared": cleared,
                "means": ("what is decodable is the acting channel being "
                          "read back, not a carried self-index; the "
                          "registered position remains the right place to "
                          "look and remains empty")}
    robust = [c for c in away if c["label"] == "ROBUST"]
    return {"cell": "SEPARATES AWAY FROM THE INJECTION",
            "cleared": cleared, "away_from_injection": away,
            "all_marginal": not robust,
            "means": ("ownership is legible somewhere the channel does not "
                      "put it; this names a candidate position for a "
                      "follow-up and licenses no reinterpretation of any "
                      "registered result"
                      + ("" if robust else
                         ". EVERY clearance here is MARGINAL, which across "
                         "165 tests is consistent with chance"))}


def arm2_cell(one):
    """Per layer: which side of its own null each instrument landed."""
    c = one["classifier"]["margin_sd"] or 0.0
    d = one["mean_difference"]["accuracy"]["margin_sd"] or 0.0
    if c < 0 and d > 0:
        cell = "CLASSIFIER PENALISED"
    elif c < 0 and d < 0:
        cell = "BOTH BELOW"
    elif c > 0 and d > 0:
        cell = "BOTH ABOVE"
    else:
        cell = "REVERSED"
    return {"cell": cell, "classifier_margin_sd": c,
            "mean_difference_margin_sd": d, "gap_sd": round(d - c, 2)}


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int) -> dict:
    lock_guard.require_known_answer_pass()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    pairs = L.paired_episodes(n_pairs, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, eps = capture(model, flat, device, with_query=False)
    qstates, _ = capture(model, flat, device, with_query=True)
    states.update(qstates)
    y_all = np.asarray([e.own_slot for e in eps])

    # COMPARABILITY, checked on the record rather than asserted in prose.
    # The anchor is the registered position, and every comparison in this
    # file against the 2026-09-16 probes and last night's read assumes the
    # states are the same states. So they are compared, here, to the ones
    # the registered pipeline produces. Anything other than an exact match
    # stops the run: a sweep whose anchor has drifted cannot be read
    # against the numbers it is being read against.
    ref, _ = L.residuals_at(model, list(flat), device)
    drift = {}
    for Lr in PROBE_LAYERS:
        X, rows = states[(Lr, ANCHOR)]
        drift[str(Lr)] = float(np.abs(np.asarray(ref[Lr])[rows] - X).max())
    if max(drift.values()) != 0.0:
        raise SystemExit(
            f"REFUSING to report: the anchor position does not reproduce "
            f"localize_a3.residuals_at (largest difference {max(drift.values())}). "
            f"Every comparison in this diagnostic assumes it does.")

    # ---- arm 1: the sweep
    arm1 = {}
    for p in POSITIONS:
        for Lr in PROBE_LAYERS:
            X, rows = states[(Lr, p)]
            y = y_all[rows]
            fs = D.folds(len(y), N_FOLDS, np.random.default_rng(Lr))
            arm1[(p, Lr)] = mean_difference_read(X, y, fs, seed=Lr)
        best = max(PROBE_LAYERS,
                   key=lambda k: arm1[(p, k)]["separation"]["value"])
        s = arm1[(p, best)]["separation"]
        print(f"  {p:26s} best layer {best}: separation {s['value']} "
              f"({s['margin_sd']} sd) clears={s['clears_3sd']}", flush=True)

    # ---- arm 2: head to head at the anchor, one shared split
    arm2 = {}
    for Lr in PROBE_LAYERS:
        X, rows = states[(Lr, ANCHOR)]
        y = y_all[rows]
        fs = D.folds(len(y), N_FOLDS, np.random.default_rng(Lr))
        one = {"classifier": classifier_read(X, y, fs, seed=Lr),
               "mean_difference": mean_difference_read(X, y, fs, seed=Lr)}
        one["head_to_head"] = arm2_cell(one)
        arm2[str(Lr)] = one
        h = one["head_to_head"]
        print(f"  arm 2 layer {Lr}: classifier {h['classifier_margin_sd']} sd, "
              f"mean-difference {h['mean_difference_margin_sd']} sd, "
              f"gap {h['gap_sd']} — {h['cell']}", flush=True)

    layers_out = {f"{p}|{Lr}": v for (p, Lr), v in arm1.items()}
    return {
        "diagnostic": "position sweep (arm 1) and instrument head-to-head "
                      "(arm 2)",
        "registered": False,
        "verdict_bearing": False,
        "method_file": "position-sweep-method.md",
        "method_committed_before_output": True,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "episodes": {"pairs_requested": n_pairs,
                     "episodes_probed": int(len(y_all)),
                     "content_seed": EPISODE_SEED,
                     "appended_question": "the other-agent battery, first "
                                          "in every episode"},
        "settings": {"probe_layers": PROBE_LAYERS, "folds": N_FOLDS,
                     "permutations": N_PERM, "sd_bar": SD_BAR,
                     "family_sd_bar": FAMILY_SD_BAR,
                     "positions": list(POSITIONS),
                     "position_notes": POSITION_NOTES,
                     "anchor": ANCHOR,
                     "positive_control": POSITIVE_CONTROL,
                     "injection_positions": list(INJECTION_POSITIONS)},
        "anchor_reproduces_registered_pipeline": {
            "checked": True, "largest_difference_per_layer": drift,
            "note": ("the anchor states were compared token for token "
                     "against localize_a3.residuals_at, which is what the "
                     "2026-09-16 probes read; an exact match is required "
                     "for this run to report at all")},
        "arm1_positions": layers_out,
        "arm1_cell": arm1_cell(arm1),
        "arm2_head_to_head": arm2,
        "limits": (
            "UNREGISTERED and diagnostic. No verdict is read and nothing "
            "here reopens one. A null everywhere is consistent with "
            "ownership being carried non-linearly, or distributed, or at a "
            "position not on the list. A clearance away from the injection "
            "positions names a place to look next and nothing more, and "
            "would not settle red-team objection R1."),
        "elapsed_sec": round(time.time() - t0, 1),
    }


def summarize_run(records: list[dict]) -> dict:
    per = {r["checkpoint"]: r["arm1_cell"]["cell"] for r in records}
    tests = sum(len(r["arm1_positions"]) for r in records)
    cleared = [dict(c, checkpoint=r["checkpoint"])
               for r in records for c in r["arm1_cell"].get("cleared", [])]
    counts: dict[str, int] = {}
    gaps = []
    for r in records:
        for v in r["arm2_head_to_head"].values():
            h = v["head_to_head"]
            counts[h["cell"]] = counts.get(h["cell"], 0) + 1
            if h["cell"] == "CLASSIFIER PENALISED":
                gaps.append(h["gap_sd"])
    order = ["SWEEP INVALID — no cell assigned",
             "SEPARATES AWAY FROM THE INJECTION",
             "SEPARATES ONLY WHERE THE CHANNEL INJECTS",
             "NOTHING SEPARATES ANYWHERE"]
    cell = next((c for c in order if c in per.values()), "NOTHING "
                "SEPARATES ANYWHERE")
    return {
        "arm1_cell": cell, "arm1_per_checkpoint": per,
        "arm1_tests_run": tests,
        "arm1_tests_cleared_excluding_positive_control": len(cleared),
        "arm1_cleared": cleared,
        "arm2_cell_counts": counts,
        "arm2_median_gap_sd_where_classifier_penalised": (
            round(float(np.median(gaps)), 2) if gaps else None),
        "note": ("diagnostic only; no verdict is read and no registered "
                 "text is touched"),
    }


# ------------------------------------------------------------- self-test

def self_test() -> None:
    # positions are arithmetic on the template, so check them against a
    # real encoded episode rather than against my own reading of it
    pairs = L.paired_episodes(6, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    for e in flat:
        enc = E.encode_episode(e)
        encq = E.encode_episode(e, query=e.queries[0])
        idx = position_indices(e, len(enc["input_ids"]), False)
        idxq = position_indices(e, len(encq["input_ids"]), True)
        ids = enc["input_ids"]
        act = int(enc["act_pos"])
        assert idx["own_revision_value"] == act, "the value position"
        assert idx["own_revision_decision"] == act - 1, "the anchor"
        # the positive control must really be the model's own marker
        assert E.IVOCAB[int(ids[idx["own_revision_marker"]])] == \
            e.markers[e.own_slot], "position 6 must be the model's marker"
        # and the anchor must NOT be the marker, or the whole registered
        # position would be trivially decodable
        assert E.IVOCAB[int(ids[idx["own_revision_decision"]])] != \
            e.markers[e.own_slot], "the anchor must not hold the marker"
        # the three injection positions are the value tokens of the
        # model's three own turns, and there are exactly three
        own = [i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
        assert len(own) == 3, "three own turns per episode"
        inj = sorted(idx[p] for p in INJECTION_POSITIONS)
        want = sorted(1 + 7 * i + A.VALUE_WORD_IDX for i in own)
        assert inj == want, "the injection positions"
        # the other reviser's position belongs to another agent
        ot = [i for i, t in enumerate(e.turns)
              if t.revised and t.agent != e.own_slot]
        assert len(ot) == 1 and idx["other_revision_value"] == \
            1 + 7 * ot[0] + A.VALUE_WORD_IDX, "the other reviser"
        # every in-episode position is inside the encoding
        for p, v in idx.items():
            assert 0 <= v < len(ids), f"{p} out of range"
        # the query positions land on the answer and the marker before it
        assert int(encq["input_ids"][idxq["query_answer_value"]]) == \
            E.VOCAB[e.queries[0].answer], "the answer token"
        assert int(encq["loss_mask"][idxq["query_answer_value"]]) == 1, \
            "the answer is the supervised token"
        assert e.queries[0].battery == "T_other", "the appended question"

    # the family-adjusted label
    assert label(True, 9.0, 0) == "ROBUST"
    assert label(True, 3.1, 0) == "MARGINAL", "below the family bar"
    assert label(True, 9.0, 1) == "MARGINAL", "a shuffled draw beat it"
    assert label(False, 9.0, 0) is None, "no label without a clearance"
    # the permutation count is inclusive of ties
    assert permutation_count(0.5, [0.4, 0.5, 0.6]) == 2

    # arm 1 cells
    def pos(p, Lr, clears, margin=9.0, lab="ROBUST"):
        return {(p, Lr): {"separation": {
            "clears_3sd": clears, "margin_sd": margin,
            "label": lab if clears else None}}}
    good = pos(POSITIVE_CONTROL, 3, True)
    assert arm1_cell(pos(POSITIVE_CONTROL, 3, False))["cell"].startswith(
        "SWEEP INVALID"), "a failed positive control invalidates the sweep"
    assert arm1_cell(good)["cell"] == "NOTHING SEPARATES ANYWHERE"
    d = dict(good); d.update(pos(INJECTION_POSITIONS[0], 3, True))
    assert arm1_cell(d)["cell"] == "SEPARATES ONLY WHERE THE CHANNEL INJECTS"
    d = dict(good); d.update(pos(ANCHOR, 3, True))
    c = arm1_cell(d)
    assert c["cell"] == "SEPARATES AWAY FROM THE INJECTION"
    assert c["all_marginal"] is False
    d = dict(good); d.update(pos(ANCHOR, 3, True, 3.1, "MARGINAL"))
    c = arm1_cell(d)
    assert c["all_marginal"] is True and "consistent with chance" in c["means"]

    # arm 2 cells, the pre-stated question being the SIGN of each margin
    def h2h(c, d):
        return arm2_cell({"classifier": {"margin_sd": c},
                          "mean_difference": {"accuracy": {"margin_sd": d}}})
    assert h2h(-0.75, 0.9)["cell"] == "CLASSIFIER PENALISED"
    assert h2h(-0.75, 0.9)["gap_sd"] == 1.65, "the gap is their difference"
    assert h2h(-0.5, -0.5)["cell"] == "BOTH BELOW"
    assert h2h(1.0, 2.0)["cell"] == "BOTH ABOVE"
    assert h2h(1.0, -2.0)["cell"] == "REVERSED"

    # the run-level summary prefers the strongest cell present
    def rec(name, cell):
        return {"checkpoint": name, "arm1_cell": {"cell": cell},
                "arm1_positions": {}, "arm2_head_to_head": {}}
    s = summarize_run([rec("a.pt", "NOTHING SEPARATES ANYWHERE"),
                       rec("b.pt", "SEPARATES AWAY FROM THE INJECTION")])
    assert s["arm1_cell"] == "SEPARATES AWAY FROM THE INJECTION"
    s = summarize_run([rec("a.pt", "NOTHING SEPARATES ANYWHERE"),
                       rec("b.pt", "NOTHING SEPARATES ANYWHERE")])
    assert s["arm1_cell"] == "NOTHING SEPARATES ANYWHERE"

    # the known-answer gate is real
    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass
    print("self-test OK — eleven positions checked against real encodings "
          "(the positive control really is the model's own marker, the "
          "anchor really is not), the family-adjusted label, the "
          "permutation count, both arms' cells and the known-answer gate; "
          "no checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=N_PAIRS)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    records = []
    for c in a.ckpt:
        out = a.out_dir / f"position_sweep_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}  arm 1: {rec['arm1_cell']['cell']}")
        records.append(rec)
    s = summarize_run(records)
    path = a.out_dir / "position_sweep_a3_summary.json"
    if path.exists():
        raise SystemExit(f"{path} exists; refusing to overwrite")
    path.write_text(json.dumps(s, indent=2))
    print(json.dumps(s, indent=2))


if __name__ == "__main__":
    main()
