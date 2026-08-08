"""MVM-0a tokenizer / tensorizer (the data interface of the adjudicated
architecture, pre-registration v0.4 §Materials).

Produces the exact tensors a training step consumes, which is what
cue-detector gate run (ii) inspects [RT-08]: token ids, per-token turn
ids, the register key stack, the loss mask, and padding. The adjudicated
architecture constrains this module directly:

- **N registers, marker-keyed, no persistent index [RT-01/RT-02].** The
  register stack is ordered by the *vocab id of each agent's per-episode
  marker* — markers are drawn without replacement at random per episode,
  so the model's own register lands at a uniformly random stack index.
  The tempting implementation shortcut — canonically reindexing so the
  model's own register sits at index 0 — is exactly an identity channel
  smuggled in as a tensor layout, and is this gate's positive control
  (`leaky=True`).
- **No own-slot channel.** The tensor dict deliberately has no field
  derived from `own_slot`; training-time supervision reaches the model
  only through the answer tokens under `loss_mask`, and the loss mask
  covers answer positions regardless of ownership.
- **Closed vocabulary.** Word-level over the curriculum grammar; there is
  no byte fallback, so anything off-grammar fails loudly.

    ../../../.venv/bin/python encoding.py --self-test
"""
from __future__ import annotations

import argparse

import numpy as np

import curriculum as C

PAD, BOS, EOS, NL, QSEP, ANS = "<pad>", "<bos>", "<eos>", "<nl>", "<q>", "<ans>"
SPECIALS = [PAD, BOS, EOS, NL, QSEP, ANS]

_QUERY_WORDS = ["where", "did", "you", "assign", "to", "how", "many",
                "parcels", "went", "which", "parcel", "was", "mentioned",
                "last", "turns", "have", "there", "been", "?"]
_DIGITS = [str(i) for i in range(21)]


def build_vocab() -> dict[str, int]:
    words = (SPECIALS + C.MARKERS + ["assign", "to"] + C.ITEMS + C.SLOTS
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
    """Tensorize one episode (and optionally one query/answer pair).

    Returns the full training-step tensor dict. `leaky=True` produces the
    positive-control layout for gate run (ii): the model's own register
    forced to stack index 0 (the canonical-reindex bug). It exists to be
    caught and must never be used for training.
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

    # Register stack, keyed by per-episode marker [RT-01/RT-02]: one row
    # per agent, ordered by marker vocab id. Markers are a per-episode
    # uniform draw, so this order carries no ownership information.
    order = sorted(range(ep.n_agents), key=lambda a: VOCAB[ep.markers[a]])
    if leaky:
        order = [ep.own_slot] + [a for a in order if a != ep.own_slot]
    register_keys = np.array([VOCAB[ep.markers[a]] for a in order],
                             dtype=np.int64)
    # turn -> register-stack row, so the write path is marker-addressed
    agent_to_reg = {a: r for r, a in enumerate(order)}
    turn_reg = np.array([agent_to_reg[t.agent] for t in ep.turns],
                        dtype=np.int64)

    return {
        "input_ids": np.array([VOCAB[w] for w in tokens], dtype=np.int64),
        "turn_ids": np.array(turn_ids, dtype=np.int64),
        "loss_mask": np.array(loss_mask, dtype=np.int64),
        "register_keys": register_keys,
        "turn_reg": turn_reg,
    }


def collate(batch: list[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    """Right-pad a batch to its max length (input_ids with PAD, turn_ids
    with -1, loss_mask with 0)."""
    n = max(len(b["input_ids"]) for b in batch)
    out = {
        "input_ids": np.full((len(batch), n), PAD_ID, dtype=np.int64),
        "turn_ids": np.full((len(batch), n), -1, dtype=np.int64),
        "loss_mask": np.zeros((len(batch), n), dtype=np.int64),
        "register_keys": np.stack([b["register_keys"] for b in batch]),
        "turn_reg": np.stack([b["turn_reg"] for b in batch]),
    }
    for j, b in enumerate(batch):
        m = len(b["input_ids"])
        for k in ("input_ids", "turn_ids", "loss_mask"):
            out[k][j, :m] = b[k]
    return out


def decode(ids: np.ndarray) -> str:
    return " ".join(IVOCAB[int(i)] for i in ids if int(i) != PAD_ID)


def self_test() -> None:
    # round trip on a rendered episode
    ep = C.generate_episode(7)
    enc = encode_episode(ep, query=ep.queries[0])
    text = decode(enc["input_ids"])
    for t in ep.turns:
        assert t.render().replace("  ", " ") in text.replace(f" {NL} ", "\n")\
            .replace(f" {NL}", "\n") or all(w in text for w in _words(t.render()))
    assert enc["loss_mask"].sum() == 1
    assert IVOCAB[int(enc["input_ids"][enc["loss_mask"] == 1][0])] \
        == ep.queries[0].answer

    # no ownership channel: the tensor dict must not contain own_slot in
    # any form, and the own register's stack index must be uniform
    assert set(enc.keys()) == {"input_ids", "turn_ids", "loss_mask",
                               "register_keys", "turn_reg"}
    counts = np.zeros(4)
    for s in range(4000):
        e = C.generate_episode(s)
        enc = encode_episode(e)
        order = sorted(range(e.n_agents), key=lambda a: VOCAB[e.markers[a]])
        counts[order.index(e.own_slot)] += 1
    freq = counts / counts.sum()
    assert np.all(np.abs(freq - 0.25) < 0.03), \
        f"own register index must be uniform, got {freq}"

    # the leaky layout really is leaky: own register always at index 0
    for s in range(200):
        e = C.generate_episode(s)
        enc = encode_episode(e, leaky=True)
        own_turns = [i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
        assert all(enc["turn_reg"][i] == 0 for i in own_turns)

    # collation pads without disturbing content
    eps = [C.generate_episode(s) for s in range(8)]
    batch = collate([encode_episode(e, query=e.queries[0]) for e in eps])
    assert batch["input_ids"].shape[0] == 8
    assert (batch["turn_ids"][batch["input_ids"] == PAD_ID] == -1).all()
    print("encoding self-test OK "
          f"(vocab {len(VOCAB)}, own-register index freq {np.round(freq, 3)})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
    else:
        ep = C.generate_episode(0)
        enc = encode_episode(ep, query=ep.queries[0])
        print(decode(enc["input_ids"]))
        print({k: v.shape for k, v in enc.items()})
