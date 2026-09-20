"""Is the probe target decodable in principle? An after-the-fact diagnosis.

**UNREGISTERED**, diagnostic only, and — unlike everything else in this
folder — **NOT pre-stated**. It was written after the position sweep's
positive control failed, to find out why. It carries no cell, decides
nothing, and is labelled this way on purpose: a measurement designed
after seeing a result is worth less than one designed before, and the way
to keep that honest is to say so rather than to dress it up.

WHAT PROMPTED IT. `position-sweep-method.md` pre-stated a positive
control: at the model's own marker token, which agent the model is has
just been read off the input, so it should decode almost perfectly, and
if it does not the read is broken. It did not. Separation at that
position reached 0.5355 against a no-information value of 0.5.

THE SUSPICION. Every probe in the localization stack — the 2026-09-16
blind arm, the denoise-before-probing diagnostic, this sweep — predicts
`own_slot`, the generator's index for whichever agent the model is. But
the episode generator draws four marker words per episode at random and
assigns them to agents in index order, so the marker belonging to
`own_slot = 0` is a different word in almost every episode. If nothing
the model can see is consistently tied to that index, then no read of the
residual stream can recover it, and every null the stack has produced was
guaranteed rather than informative.

WHAT IS MEASURED. At the model's own marker token and at the registered
anchor position, the same instrument is pointed at three targets:

  own_slot        the current target: the generator's index for the
                  agent the model is.
  register_index  the rank of the model's own marker among the four
                  markers in the episode, sorted by vocabulary order.
                  This is what `encoding_a3` already computes as
                  `turn_reg`, it is consistently defined across episodes,
                  and it is recoverable from the input by the model's
                  revision turn, since all four markers have appeared.
  marker_token    which marker word sits at that position. At the marker
                  position this is the input token itself, so anything
                  other than near-perfect accuracy means the capture or
                  the probe is broken, independent of any question about
                  ownership.

`marker_token` is the real positive control — the one the method file
should have used. It tests the READ. `own_slot` and `register_index` test
what is being read FOR.

HOW TO REASON ABOUT THE ANSWER. If `marker_token` decodes and `own_slot`
does not, the read works and the target is wrong. If `register_index`
also decodes, there is a consistently defined own-agent quantity the
model does carry, and the stack has been asking for the wrong one. If
neither `own_slot` nor `register_index` decodes while `marker_token`
does, the read works, the target is wrong, and the replacement is not
obvious either.

WHICH INSTRUMENT. The difference-of-averages read, the same one arm 1 of
the sweep uses, for all three targets. The regularised classifier is run
too, but only on the two four-class targets: on the marker word, which
has twenty-five classes here, a multinomial fit under a permutation null
does not finish in a useful time, and the classifier adds nothing the
difference-of-averages read does not already say about whether the token
is there to be read. That is a cost decision and it is recorded rather
than hidden.

Permutation draws are reduced from 200 to 50 here because this is a
diagnosis and not a verdict; the margins are correspondingly coarser and
the permutation counts are reported beside them.

THE POWER PROBLEM ON THE MARKER TARGET, stated rather than discovered
later. Twenty-five marker words across 400 episodes is about sixteen
episodes per class, so a difference of averages built from sixteen
examples is weak. A null on that target at a position where the word is
absent from the input is underpowered, and a null result there is much
softer evidence than a null on a four-class target.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
fresh output file, nothing overwritten [C6].

    ../../../.venv/bin/python probe_target_diagnostic_a3.py --self-test
    ../../../.venv/bin/python probe_target_diagnostic_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

import denoised_direction_a3 as D
import encoding_a3 as E
import localize_a3 as L
import position_sweep_a3 as P
from model import MVM0aModel, Config

N_PERM = 50
N_FOLDS = 4
SD_BAR = 3.0
READ_POSITIONS = ("own_revision_marker", "own_revision_decision")


def targets(eps):
    """The three labels, from the episodes themselves."""
    own = np.asarray([e.own_slot for e in eps])
    reg = np.asarray([
        sorted(range(e.n_agents), key=lambda a: E.VOCAB[e.markers[a]])
        .index(e.own_slot) for e in eps])
    mk = np.asarray([E.VOCAB[e.markers[e.own_slot]] for e in eps])
    return {"own_slot": own, "register_index": reg, "marker_token": mk}


MAX_CLASSES_FOR_CLASSIFIER = 8


def probe(X, y, seed):
    """The difference-of-averages read with a reduced permutation null,
    and the regularised classifier beside it where it is affordable.

    Accuracy is compared against the MAJORITY-CLASS RATE as well as the
    null, because with unequal class sizes a constant classifier already
    beats the no-information value and quoting only the latter flatters
    the result."""
    y = np.asarray(y)
    classes = sorted(np.unique(y).tolist())
    fs = D.folds(len(y), N_FOLDS, np.random.default_rng(seed))
    rng = np.random.default_rng(seed + 1)

    _, real, _, _, _ = D.score_once(X, y, classes, False, fs)
    null = []
    for _ in range(N_PERM):
        _, a, _, _, _ = D.score_once(X, rng.permutation(y), classes, False, fs)
        null.append(a)
    m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
    vals, counts = np.unique(y, return_counts=True)
    majority = float(counts.max() / len(y))
    out = {"instrument": "difference of averages, nearest-average accuracy",
           "accuracy": round(real, 4), "null_mean": round(m, 4),
           "null_sd": round(sd, 4),
           "margin_sd": round((real - m) / sd, 2) if sd > 0 else None,
           "clears_3sd": bool(sd > 0 and real >= m + SD_BAR * sd),
           "beats_majority_class": bool(real > majority),
           "draws_beating_real": P.permutation_count(real, null),
           "draws": N_PERM,
           "classes": int(len(vals)),
           "no_information": round(1 / len(vals), 4),
           "majority_class_rate": round(majority, 4),
           "episodes_per_class": round(len(y) / len(vals), 1)}

    if len(classes) <= MAX_CLASSES_FOR_CLASSIFIER:
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import cross_val_score
        cv = [(np.setdiff1d(np.arange(len(y)), h), h) for h in fs]
        clf = LogisticRegression(max_iter=2000, C=1.0)
        r2 = float(cross_val_score(clf, X, y, cv=cv).mean())
        n2 = [float(cross_val_score(clf, X, rng.permutation(y),
                                    cv=cv).mean()) for _ in range(N_PERM)]
        m2, sd2 = float(np.mean(n2)), float(np.std(n2, ddof=1))
        out["classifier"] = {
            "accuracy": round(r2, 4), "null_mean": round(m2, 4),
            "null_sd": round(sd2, 4),
            "margin_sd": round((r2 - m2) / sd2, 2) if sd2 > 0 else None,
            "clears_3sd": bool(sd2 > 0 and r2 >= m2 + SD_BAR * sd2),
            "beats_majority_class": bool(r2 > majority)}
    else:
        out["classifier"] = {
            "skipped": f"{len(classes)} classes; a multinomial fit under a "
                       f"permutation null does not finish in a useful time, "
                       f"and it adds nothing the read above does not say"}
    return out


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int) -> dict:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])
    pairs = L.paired_episodes(n_pairs, seed=P.EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, eps = P.capture(model, flat, device, with_query=False)
    tg = targets(eps)

    # How badly is the current target scrambled? Descriptive, no cell.
    scramble = {}
    for name, y in tg.items():
        if name == "own_slot":
            continue
        tab = {}
        for a, b in zip(tg["own_slot"], y):
            tab.setdefault(int(a), set()).add(int(b))
        scramble[name] = {str(k): len(v) for k, v in sorted(tab.items())}

    out = {}
    for pos in READ_POSITIONS:
        for Lr in P.PROBE_LAYERS:
            X, rows = states[(Lr, pos)]
            for name, y in tg.items():
                out[f"{pos}|{Lr}|{name}"] = probe(X, y[rows], seed=Lr)
        best = {n: max(P.PROBE_LAYERS,
                       key=lambda k: out[f"{pos}|{k}|{n}"]["accuracy"])
                for n in tg}
        for n, k in best.items():
            r = out[f"{pos}|{k}|{n}"]
            print(f"  {pos:24s} {n:15s} best layer {k}: "
                  f"accuracy {r['accuracy']} vs no-information "
                  f"{r['no_information']} ({r['margin_sd']} sd) "
                  f"clears={r['clears_3sd']}", flush=True)

    read_works = any(
        out[f"own_revision_marker|{Lr}|marker_token"]["clears_3sd"] and
        out[f"own_revision_marker|{Lr}|marker_token"]["beats_majority_class"]
        for Lr in P.PROBE_LAYERS)
    own_works = any(out[f"{p}|{Lr}|own_slot"]["clears_3sd"] and
                    out[f"{p}|{Lr}|own_slot"]["beats_majority_class"]
                    for p in READ_POSITIONS for Lr in P.PROBE_LAYERS)
    reg_works = any(out[f"{p}|{Lr}|register_index"]["clears_3sd"] and
                    out[f"{p}|{Lr}|register_index"]["beats_majority_class"]
                    for p in READ_POSITIONS for Lr in P.PROBE_LAYERS)
    if not read_works:
        reading = ("THE READ IS BROKEN. The marker word sitting at the "
                   "probed position is the input token there, and it does "
                   "not decode. Nothing else in this file or in the sweep "
                   "can be interpreted until that is explained.")
    elif own_works:
        reading = ("THE TARGET IS FINE. The generator's own-agent index "
                   "decodes somewhere, so the sweep's positive control "
                   "failing needs a different explanation.")
    elif reg_works:
        reading = ("THE READ WORKS AND THE TARGET IS WRONG. The input "
                   "token decodes and a consistently defined own-agent "
                   "quantity decodes, while the generator's index — what "
                   "every probe in the stack has asked for — does not.")
    else:
        reading = ("THE READ WORKS AND THE TARGET IS WRONG, WITH NO "
                   "OBVIOUS REPLACEMENT. The input token decodes; neither "
                   "the generator's index nor the register index does.")

    return {
        "diagnostic": "is the probe target decodable in principle?",
        "registered": False,
        "pre_stated": False,
        "written_after_seeing": ("the position sweep's positive control "
                                 "failing on the pilot checkpoint"),
        "verdict_bearing": False,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "episodes_probed": int(len(eps)),
        "permutations": N_PERM,
        "permutation_note": ("reduced from the 200 used for verdict-bearing "
                             "nulls because this is a diagnosis; margins "
                             "are coarser and the counts are reported"),
        "distinct_values_per_own_slot": scramble,
        "scramble_note": ("how many distinct values of each consistently "
                          "defined quantity share one generator index. "
                          "Anything much above 1 means the generator index "
                          "has no stable surface realisation."),
        "probes": out,
        "reading": reading,
        "well_posed_self_index_read": {
            "what": ("the model's OWN MARKER WORD, read at the registered "
                     "anchor position. The marker has not been emitted yet "
                     "at that position — it comes after the value — so the "
                     "model would have to be carrying it. Unlike the "
                     "generator index, this target is decodable in "
                     "principle, which is what makes a null here mean "
                     "something"),
            "per_layer": {str(Lr): out[f"own_revision_decision|{Lr}|"
                                       f"marker_token"] for Lr
                          in P.PROBE_LAYERS},
            "caveat": ("underpowered: about sixteen episodes per marker "
                       "word, so a difference of averages built from them "
                       "is weak and a null is soft evidence")},
        "limits": ("NOT pre-stated. Designed after seeing the sweep fail, "
                   "so it is worth less than a measurement designed before. "
                   "It carries no cell and settles nothing on its own; what "
                   "it can do is say whether the instrument was pointed at "
                   "a quantity that could ever have been recovered."),
    }


def self_test() -> None:
    pairs = L.paired_episodes(8, seed=P.EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    tg = targets(flat)
    assert set(tg) == {"own_slot", "register_index", "marker_token"}
    for e, r in zip(flat, tg["register_index"]):
        order = sorted(range(e.n_agents), key=lambda a: E.VOCAB[e.markers[a]])
        assert order[r] == e.own_slot, "the register index must invert"
    for e, m in zip(flat, tg["marker_token"]):
        assert E.IVOCAB[int(m)] == e.markers[e.own_slot], "the marker token"
    # the whole suspicion, stated as a check: the generator index does NOT
    # pin down the marker word
    tab: dict[int, set] = {}
    for a, b in zip(tg["own_slot"], tg["marker_token"]):
        tab.setdefault(int(a), set()).add(int(b))
    assert max(len(v) for v in tab.values()) > 1, (
        "if one generator index mapped to one marker word, the target "
        "would be decodable and this diagnostic would be pointless")
    print("self-test OK — the three targets invert correctly, and the "
          "generator index is confirmed not to pin down the marker word; "
          "no checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=P.N_PAIRS)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    for c in a.ckpt:
        out = a.out_dir / f"probe_target_diagnostic_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(rec["reading"])
        print(f"written: {out}")


if __name__ == "__main__":
    main()
