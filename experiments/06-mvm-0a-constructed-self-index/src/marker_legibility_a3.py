"""Why is the marker word so much more legible on the pilot? Descriptive.

**UNREGISTERED**, descriptive only. **No cell, no threshold, no
hypothesis.** The method is committed in `powered-target-test-method.md`,
in the same commit as this file and before either produced any output.

WHAT PROMPTED IT. The position sweep found the same input token, at the
same position and the same layers, decoding at 0.55 on the pilot and 0.06
to 0.12 on seeds 1 and 2 — checkpoints that differ only by training seed
and were read on the same episodes. Until that is understood, a null on
seeds 1 and 2 rests on a positive control that barely holds.

WHAT IS MEASURED. Two quantities across the three checkpoints, and
nothing else:

1. MARKER-TOKEN EMBEDDING NORMS. The length of the embedding row for each
   of the 25 marker words, summarised per checkpoint, against the mean
   length over the whole vocabulary as a reference. If marker embeddings
   are small relative to everything else on a checkpoint, less of the
   token is there to read.

2. ATTENTION MASS FROM THE ANCHOR TO MARKER POSITIONS. At the anchor row,
   how much attention is paid to marker tokens earlier in the episode,
   per layer, averaged over episodes, split into the model's own earlier
   markers and the other agents'. Note the model's own marker in the
   revision turn sits AFTER the anchor and cannot be attended to at all:
   attention is causal, which is the whole reason the anchor is the
   interesting position.

HOW THE WEIGHTS ARE OBTAINED, since the model does not return them. Each
block's attention is recomputed with weights requested, using the same
inputs and the same mask the block builds, and then the block's own
forward is called on the same inputs so the model's actual output path is
untouched. The recomputation is read-only and deterministic in eval mode.

WHAT THIS IS NOT. It is not an explanation and must not be written up as
one. It reports two numbers per checkpoint. Anything that looks like a
cause is a candidate for a later measurement with its own committed
method, and the findings say so rather than assert it.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
fresh output per checkpoint, nothing overwritten [C6].

    ../../../.venv/bin/python marker_legibility_a3.py --self-test
    ../../../.venv/bin/python marker_legibility_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import encoding_a3 as E
import localize_a3 as L
import powered_target_test_a3 as P
from model import MVM0aModel, Config, to_torch

MARKER_WORD_IDX = 5          # assign {item} to {value} by {marker}
N_EPISODES_DEFAULT = 200     # descriptive; no null, so no power argument


def embedding_norms(model) -> dict:
    """Marker-token embedding lengths against the vocabulary as a whole."""
    W = model.tok.weight.detach().float()
    norms = W.norm(dim=1)
    ids = [E.VOCAB[m] for m in A.MARKERS]
    mk = norms[torch.tensor(ids)]
    return {
        "marker_count": len(ids),
        "marker_norm_mean": round(float(mk.mean()), 4),
        "marker_norm_sd": round(float(mk.std(unbiased=True)), 4),
        "marker_norm_min": round(float(mk.min()), 4),
        "marker_norm_max": round(float(mk.max()), 4),
        "vocabulary_norm_mean": round(float(norms.mean()), 4),
        "vocabulary_norm_sd": round(float(norms.std(unbiased=True)), 4),
        "marker_over_vocabulary": round(
            float(mk.mean() / norms.mean()), 4),
    }


def _row(segments, pos):
    """The attention row for absolute position `pos`, from the segment
    that contains it. That row covers every key up to `pos`."""
    for off, w in segments:
        if off <= pos < off + w.shape[1]:
            return w[:, pos - off]
    raise IndexError(f"no segment contains position {pos}")


@torch.no_grad()
def attention_to_markers(model, eps, device) -> dict:
    """Attention paid by the anchor row to earlier marker tokens."""
    eps = list(eps)
    rng = random.Random(0)
    for e in eps:
        A.enact_own_turns(e, rng)
    encs = [E.encode_episode(e) for e in eps]
    batch = to_torch(E.collate(encs), device)
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
        act = act.index_put((torch.tensor(bs, device=device),
                             torch.tensor(ps, device=device)),
                            model.act_proj(h[torch.tensor(bs, device=device),
                                             torch.tensor(ps, device=device)
                                             - 1]))

    # The model runs the episode in SEGMENTS, one per turn, each block
    # seeing a cached prefix. So attention weights arrive one segment at a
    # time and have to be kept with the segment's offset: a segment
    # starting at absolute position `off` returns rows for `off ..
    # off+s-1`, each covering absolute keys `0 .. off+s-1`. Keeping only
    # the last segment, which is the obvious mistake here, gives a matrix
    # seven tokens wide and an index error.
    weights: dict[int, list] = {Lr: [] for Lr in P.PROBE_LAYERS}
    for Lr in P.PROBE_LAYERS:
        blk = model.blocks[Lr]
        orig = blk.forward

        def patched(x, kv, reg_repr, _o=orig, _L=Lr, _b=blk):
            # recompute this block's attention with weights requested,
            # replicating the mask the block builds, then hand the real
            # forward the same inputs so the output path is untouched
            h = _b.ln1(x)
            ctx = h if kv is None else torch.cat([kv, h], dim=1)
            pfx, sl = ctx.shape[1] - h.shape[1], h.shape[1]
            mask = torch.ones(sl, pfx + sl, dtype=torch.bool, device=x.device)
            mask[:, pfx:] = torch.triu(
                torch.ones(sl, sl, dtype=torch.bool, device=x.device),
                diagonal=1) == 0
            _, w = _b.attn(h, ctx, ctx, attn_mask=~mask, need_weights=True,
                           average_attn_weights=True)
            weights[_L].append((pfx, w.detach()))
            return _o(x, kv, reg_repr)
        blk.forward = patched
    model.forward(batch, act_inject=act)
    for Lr in P.PROBE_LAYERS:
        del model.blocks[Lr].__dict__["forward"]

    out = {}
    for Lr in P.PROBE_LAYERS:
        segs = weights[Lr]
        own_mass, other_mass, total_mass = [], [], []
        for b, e in enumerate(eps):
            anchor = P.position_indices(e)[P.ANCHOR]
            row = _row(segs, anchor)[b]
            own, oth = 0.0, 0.0
            for ti, t in enumerate(e.turns):
                pos = 1 + P.TURN_SPAN * ti + MARKER_WORD_IDX
                if pos >= anchor:            # causal: later tokens unseen
                    continue
                v = float(row[pos])
                if t.agent == e.own_slot:
                    own += v
                else:
                    oth += v
            own_mass.append(own)
            other_mass.append(oth)
            total_mass.append(own + oth)
        out[str(Lr)] = {
            "attention_to_all_earlier_markers": round(
                float(np.mean(total_mass)), 5),
            "attention_to_own_earlier_markers": round(
                float(np.mean(own_mass)), 5),
            "attention_to_other_agents_markers": round(
                float(np.mean(other_mass)), 5),
            "episodes": len(eps),
        }
    return out


@torch.no_grad()
def run(ckpt: Path, device: str, n_episodes: int) -> dict:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])
    pairs = L.paired_episodes(max(1, n_episodes // 2), seed=P.EPISODE_SEED)
    flat = [e for p in pairs for e in p][:n_episodes]
    emb = embedding_norms(model)
    att = attention_to_markers(model, flat, device)
    print(f"  marker embedding norm {emb['marker_norm_mean']} vs vocabulary "
          f"{emb['vocabulary_norm_mean']} "
          f"(ratio {emb['marker_over_vocabulary']})", flush=True)
    for Lr, v in att.items():
        print(f"  layer {Lr}: anchor attention to earlier markers "
              f"{v['attention_to_all_earlier_markers']} "
              f"(own {v['attention_to_own_earlier_markers']}, "
              f"other {v['attention_to_other_agents_markers']})", flush=True)
    return {
        "measurement": "marker-token legibility, descriptive",
        "registered": False, "verdict_bearing": False,
        "carries_a_cell": False,
        "method_file": "powered-target-test-method.md",
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "episodes": len(flat),
        "embedding_norms": emb,
        "anchor_attention_to_markers": att,
        "note": ("Descriptive. No cell, no threshold, no hypothesis. These "
                 "are two numbers per checkpoint; anything that looks like "
                 "a cause is a candidate for a later measurement with its "
                 "own committed method."),
    }


def self_test() -> None:
    # the marker word index must really be the marker in the template
    pairs = L.paired_episodes(6, seed=P.EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    for e in flat:
        ids = E.encode_episode(e)["input_ids"]
        for ti, t in enumerate(e.turns):
            pos = 1 + P.TURN_SPAN * ti + MARKER_WORD_IDX
            assert E.IVOCAB[int(ids[pos])] == e.markers[t.agent], \
                "the marker index must find each turn's own marker"
        anchor = P.position_indices(e)[P.ANCHOR]
        rev = A.own_revision_index(e)
        own_marker_pos = 1 + P.TURN_SPAN * rev + MARKER_WORD_IDX
        assert own_marker_pos > anchor, (
            "the model's own marker in the revision turn must sit AFTER "
            "the anchor — that is why the anchor is the interesting place")
    assert len(A.MARKERS) == 25, "the marker pool"

    # the segment lookup, which is what the first version got wrong: the
    # model runs one segment per turn, so a row must be fetched from the
    # segment that contains it and must cover every earlier key
    segs = [(0, torch.zeros(2, 8, 8)), (8, torch.zeros(2, 7, 15)),
            (15, torch.zeros(2, 7, 22))]
    assert _row(segs, 3).shape == (2, 8), "a row in the first segment"
    assert _row(segs, 16).shape == (2, 22), "a later row covers all keys"
    try:
        _row(segs, 99)
        raise AssertionError("a position in no segment must raise")
    except IndexError:
        pass
    print("self-test OK — the marker index finds every turn's own marker, "
          "and the model's own revision marker is confirmed to sit after "
          "the anchor, where causal attention cannot reach it, and the "
          "segment lookup; no checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-episodes", type=int, default=N_EPISODES_DEFAULT)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    for c in a.ckpt:
        out = a.out_dir / f"marker_legibility_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_episodes)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)


if __name__ == "__main__":
    main()
