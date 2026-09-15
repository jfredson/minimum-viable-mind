"""Tensorizer for the Amendment A3 Candidate A grammar.

A mirror of `encoding.py` with one difference: the closed vocabulary gains
the word **"next"**, which the T_other counterfactual needs ("where did
<marker> assign <item> to next ?").

`encoding.py` is deliberately NOT edited. Its vocabulary fixes the token
ids the five existing checkpoints were trained under, and those ids are
what makes every record in `lesion-results/` and `null-calibration/`
reproduce. Adding a word there would renumber the vocabulary and silently
invalidate the lot.

Everything else is carried over verbatim, including the two properties
gate (ii) exists to check: there is no field derived from `own_slot`, and
the register stack is ordered by marker vocab id so the model's own
register lands at a uniformly random index. `leaky=True` reproduces the
canonical-reindex bug as the gate's positive control.

    ../../../.venv/bin/python encoding_a3.py --self-test
"""
from __future__ import annotations

import argparse

import numpy as np

import curriculum as C
import curriculum_a3 as A

PAD, BOS, EOS, NL, QSEP, ANS = "<pad>", "<bos>", "<eos>", "<nl>", "<q>", "<ans>"
SPECIALS = [PAD, BOS, EOS, NL, QSEP, ANS]

# "next" is the A3 addition; the rest matches encoding.py's list.
_QUERY_WORDS = ["where", "did", "you", "assign", "to", "next", "by", "how", "many",
                "parcels", "went", "which", "parcel", "was", "mentioned",
                "last", "turns", "have", "there", "been", "?"]
_DIGITS = [str(i) for i in range(max(21, A.N_TURNS + 2))]


def build_vocab() -> dict[str, int]:
    words = (SPECIALS + C.MARKERS + ["assign", "to", "by"] + C.ITEMS + C.SLOTS
             + _QUERY_WORDS + _DIGITS)
    seen: dict[str, int] = {}
    for w in words:
        if w not in seen:
            seen[w] = len(seen)
    return seen


VOCAB = build_vocab()
IVOCAB = {i: w for w, i in VOCAB.items()}
PAD_ID = VOCAB[PAD]


def _words(text: str) -> list[str]:
    return text.replace("?", " ?").split()


def encode_episode(ep: C.Episode, query: C.Query | None = None,
                   leaky: bool = False) -> dict[str, np.ndarray]:
    """Tensorize one episode, optionally with one query/answer pair.

    `act_pos` is the A3 addition to the tensor dict: the token index of
    the value the model emits at its own revision — the supervised
    position for T_act. It is control flow for the trainer, derived from
    `own_slot`, so it must NEVER be fed to the model as input. Gate (ii)
    is run over the model-visible fields only, and the self-test below
    asserts that separation.
    """
    tokens, turn_ids = [BOS], [-1]
    for i, t in enumerate(ep.turns):
        for w in _words(t.render()):
            tokens.append(w)
            turn_ids.append(i)
        tokens.append(NL)
        turn_ids.append(i)

    loss_mask = [0] * len(tokens)
    if query is not None:
        tokens.append(QSEP)
        turn_ids.append(-2)
        loss_mask.append(0)
        for w in _words(query.text):
            tokens.append(w)
            turn_ids.append(-2)
            loss_mask.append(0)
        tokens += [ANS, query.answer, EOS]
        turn_ids += [-2, -2, -2]
        loss_mask += [0, 1, 0]

    order = sorted(range(ep.n_agents), key=lambda a: VOCAB[ep.markers[a]])
    if leaky:
        order = [ep.own_slot] + [a for a in order if a != ep.own_slot]
    register_keys = np.array([VOCAB[ep.markers[a]] for a in order],
                             dtype=np.int64)
    agent_to_reg = {a: r for r, a in enumerate(order)}
    turn_reg = np.array([agent_to_reg[t.agent] for t in ep.turns],
                        dtype=np.int64)

    ti = A.own_revision_index(ep)
    span = [j for j, x in enumerate(turn_ids) if x == ti]
    # Derived from the template rather than counted from the end, so the
    # two cannot drift apart if the rendering changes again.
    act_pos = span[0] + A.VALUE_WORD_IDX

    return {
        "input_ids": np.array([VOCAB[w] for w in tokens], dtype=np.int64),
        "turn_ids": np.array(turn_ids, dtype=np.int64),
        "loss_mask": np.array(loss_mask, dtype=np.int64),
        "register_keys": register_keys,
        "turn_reg": turn_reg,
        "act_pos": np.array(act_pos, dtype=np.int64),
    }


MODEL_FIELDS = ("input_ids", "turn_ids", "loss_mask", "register_keys",
                "turn_reg")


def collate(batch: list[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    n = max(len(b["input_ids"]) for b in batch)
    out = {
        "input_ids": np.full((len(batch), n), PAD_ID, dtype=np.int64),
        "turn_ids": np.full((len(batch), n), -1, dtype=np.int64),
        "loss_mask": np.zeros((len(batch), n), dtype=np.int64),
        "register_keys": np.stack([b["register_keys"] for b in batch]),
        "turn_reg": np.stack([b["turn_reg"] for b in batch]),
        "act_pos": np.stack([b["act_pos"] for b in batch]),
    }
    for j, b in enumerate(batch):
        m = len(b["input_ids"])
        for k in ("input_ids", "turn_ids", "loss_mask"):
            out[k][j, :m] = b[k]
    return out


def decode(ids: np.ndarray) -> str:
    return " ".join(IVOCAB[int(i)] for i in ids if int(i) != PAD_ID)


def self_test() -> None:
    import random
    ep = A.generate_episode(7)
    enc = encode_episode(ep, query=ep.queries[0])
    text = decode(enc["input_ids"])
    assert "next" in text
    assert enc["loss_mask"].sum() == 1
    assert IVOCAB[int(enc["input_ids"][enc["loss_mask"] == 1][0])] \
        == ep.queries[0].answer

    # act_pos really points at the value token of the OWN revision, and
    # that token is the T_act target
    assert IVOCAB[int(enc["input_ids"][int(enc["act_pos"])])] \
        == A.act_target(ep)
    ti = A.own_revision_index(ep)
    assert int(enc["turn_ids"][int(enc["act_pos"])]) == ti

    # act_pos is trainer control flow, never a model input
    assert set(enc.keys()) == set(MODEL_FIELDS) | {"act_pos"}
    for f in MODEL_FIELDS:
        assert "act" not in f

    # no ownership channel: the own register's stack index is uniform
    counts = np.zeros(A.N_AGENTS)
    for s in range(4000):
        e = A.generate_episode(s)
        order = sorted(range(e.n_agents), key=lambda a: VOCAB[e.markers[a]])
        counts[order.index(e.own_slot)] += 1
    freq = counts / counts.sum()
    assert np.all(np.abs(freq - 1 / A.N_AGENTS) < 0.03), \
        f"own register index must be uniform, got {freq}"

    # the leaky layout really is leaky
    for s in range(200):
        e = A.generate_episode(s, leaky=True)
        enc = encode_episode(e, leaky=True)
        own = [i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
        assert all(enc["turn_reg"][i] == 0 for i in own)

    # enactment keeps the encoding well-formed and moves act_pos's token
    e = A.generate_episode(11)
    A.enact_own_turns(e, random.Random(3))
    enc = encode_episode(e, query=e.queries[0])
    assert IVOCAB[int(enc["input_ids"][int(enc["act_pos"])])] \
        == A.act_target(e)

    # collation pads without disturbing content
    eps = [A.generate_episode(s) for s in range(8)]
    batch = collate([encode_episode(e, query=e.queries[0]) for e in eps])
    assert batch["input_ids"].shape[0] == 8
    assert (batch["turn_ids"][batch["input_ids"] == PAD_ID] == -1).all()
    for j, e in enumerate(eps):
        assert IVOCAB[int(batch["input_ids"][j, int(batch["act_pos"][j])])] \
            == A.act_target(e)

    # the registered vocabulary is untouched by this module
    import encoding as E0
    assert len(E0.VOCAB) != len(VOCAB) or "next" in E0.VOCAB
    assert "next" not in E0.VOCAB, "encoding.py must not gain A3's word"
    print(f"encoding_a3 self-test OK (vocab {len(VOCAB)} vs registered "
          f"{len(E0.VOCAB)}; own-register index freq {np.round(freq, 3)}; "
          f"max len {len(encode_episode(eps[0], eps[0].queries[0])['input_ids'])})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()


if __name__ == "__main__":
    main()
