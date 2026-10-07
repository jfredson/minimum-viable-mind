"""The successor experiment's episode generator: matched-role revisions.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`; the registration text will
name it by commit. What it builds is section 4 of
`docs/successor-experiment-proposal-2026-10-03-v4.md`.

Where it comes from
-------------------
The episode code (`_content`, `render`, `make_pairs`, `batch` and the
vocabulary) is copied unchanged from the rehearsal's generator,
`experiments/rehearsal-successor-measure/src/grammar.py`, which every toy
figure in version 4 was produced with. The self-test checks that the copy
gives the rehearsal's episodes array for array. Three things differ:

1. **The acting channel fires on both action turns, fixed.** The rehearsal
   carried a switch for redesign (c) of 2026-09-25, which turned the channel
   off on the named-other action turn. That redesign did not clear its pass
   line, so version 4 registers the grammar as it was (section 4.1), and the
   switch is gone rather than left at a default.
2. **The evaluation sets are named here, with their seeds,** so that the
   trainer on the rented machine and the measurement on the laptop build the
   same episodes from the same code (section 7.1 of version 4; the seeds are
   the toy's, carried over).
3. **Training episodes are streamed**, generated at each step from the run's
   seed and the step number, and any episode whose content matches one in an
   evaluation set is skipped, so the three sets of section 7.1 are disjoint by
   construction. The rehearsal drew from a fixed set of 12,000 pairs, which at
   the full token budget would be shown to the model about 430 times over.
   This is the freeze session's choice, not a ruling (the method note,
   section 3). Since 2026-10-06 the stream also skips any episode whose
   *pairing* (which marker holds which value on which item) is that of a
   fresh or relaxed episode, however its turns are ordered, so no such
   pairing can occur in training at all. That is John's ruling of 2026-10-06
   (method note `docs/2026-10-06-successor-training-exclusion-pairing-method.md`).

What one episode is
-------------------
Four agents, two items, eight value slots, a closed vocabulary of 46 words, 56
tokens. Eight assignment turns, one per (agent, item), in a random order,
rendered `<marker> assign <item> <value>`; then two action turns, rendered
`<act> revise <who> <item> <ans> <mask>`:

- **own-directed**: `<who>` is the word meaning *your own*, and the answer is
  the successor of the model's own earlier value on that item;
- **named-other-directed**: `<who>` is another agent's marker word, and the
  answer is the successor of that agent's earlier value.

The answer is never in the input: it is scored at the `<mask>` position. A
matched pair (the same content, a different agent being the model) is token
for token identical and differs only in where the acting channel fires.

The two carried-over rules
--------------------------
- **The even-split rule** (ledger item RT-58, the batch-split bias check):
  rows arrive as matched pairs, so a batch of an odd number of rows cuts a
  pair. `check_even_split` is called by the trainer before it starts.
- **The one-scored-token check** (ledger item RT-59): exactly one token is
  scored per supervised position, it is the mask word and never the answer,
  and nothing shifts it. `scored_token_check` checks a built batch; the models'
  self-test checks that their own loss is the cross-entropy over exactly those
  positions, which is the part the ledger item says a one-line check missed.

Corrigibility: this module generates data. It trains nothing, launches
nothing, rents nothing and costs nothing [C1/C2].

    python grammar.py --self-test
"""
from __future__ import annotations

import argparse
import hashlib

import numpy as np

N_AGENTS = 4
N_ITEMS_PER_EPISODE = 2
N_SLOTS = 8

PAD, BOS, EOS, NL, ACT, ANS, SELF, MASK = (
    "<pad>", "<bos>", "<eos>", "<nl>", "<act>", "<ans>", "<self>", "<mask>")
SPECIALS = [PAD, BOS, EOS, NL, ACT, ANS, SELF, MASK]

MARKERS = [f"m{i}" for i in range(20)]
ITEMS = [f"it{i}" for i in range(8)]
SLOTS = [f"v{i}" for i in range(N_SLOTS)]

# Fresh episodes are unseen COMBINATIONS of words the arms have seen (the weak
# reading of "fresh", registered by version 4, section 7.1). The
# unseen-vocabulary pool is the strong reading, kept as a named diagnostic and
# never the evaluation set.
POOLS = {
    "train": (list(range(0, 12)), list(range(0, 5))),
    "dev": (list(range(0, 12)), list(range(0, 5))),
    "fresh": (list(range(0, 12)), list(range(0, 5))),
    "unseen-vocabulary": (list(range(12, 20)), list(range(5, 8))),
}


def build_vocab() -> dict[str, int]:
    words = SPECIALS + ["assign", "revise"] + MARKERS + ITEMS + SLOTS
    seen: dict[str, int] = {}
    for w in words:
        if w not in seen:
            seen[w] = len(seen)
    return seen


VOCAB = build_vocab()
IVOCAB = {i: w for w, i in VOCAB.items()}
PAD_ID = VOCAB[PAD]
MASK_ID = VOCAB[MASK]
ANS_ID = VOCAB[ANS]
SLOT_IDS = np.array([VOCAB[s] for s in SLOTS], dtype=np.int64)

# 1 <bos> + 8 turns x 5 + 2 turns x 7 + 1 <eos>
SEQ_LEN = 1 + 8 * 5 + 2 * 7 + 1

OWN, OTHER = 0, 1          # the two conditions, in a fixed reporting order

# The acting channel's value on the named-other action turn: it fires, as on
# the own-directed one. Fixed (version 4, section 4.1).
NAMED_OTHER_ACTING = 1


# ------------------------------------------------- the evaluation sets
#
# Version 4, section 9, "the numbers of episodes at the registered size": the
# toy's, unchanged. Seeds are the toy's (method note, section 6, item 4).
# Each entry: (number of matched pairs, seed, pool, relaxed).

EVAL_SETS = {
    "dev": (600, 4242, "dev", False),        # nomination; last 180 held out for fits
    "fresh": (800, 777, "fresh", False),     # the reading
    "relaxed": (800, 778, "fresh", True),    # control 6 only
    "gate": (1500, 99, "dev", False),        # the gates: 3,000 episodes
    "trajectory": (200, 31337, "dev", False),  # watched during training only
}
DEV_SWAP_SEED = 4243       # control 2's donors on development episodes
FRESH_SWAP_SEED = 781      # and on fresh ones


def successor(slot: int) -> int:
    """The revision rule, the same in both conditions."""
    return (slot + 1) % N_SLOTS


def _content(rng: np.random.Generator, pool: str, collide: bool) -> dict:
    """The part of an episode that does not depend on who the model is."""
    marker_pool, item_pool = POOLS[pool]
    markers = list(rng.choice(marker_pool, size=N_AGENTS, replace=False))
    items = list(rng.choice(item_pool, size=N_ITEMS_PER_EPISODE, replace=False))

    values = np.zeros((N_AGENTS, N_ITEMS_PER_EPISODE), dtype=np.int64)
    for j in range(N_ITEMS_PER_EPISODE):
        values[:, j] = rng.choice(N_SLOTS, size=N_AGENTS, replace=False)
    collide_pair = None
    if collide:
        # One item where two agents share a value, so that control 6 ("who is
        # acting, versus which value") has a cell in which the donor's
        # identity dictates the SAME value as the recipient's.
        a, b = rng.choice(N_AGENTS, size=2, replace=False)
        j = int(rng.integers(N_ITEMS_PER_EPISODE))
        values[b, j] = values[a, j]
        collide_pair = (int(a), int(b), j)

    order = rng.permutation(N_AGENTS * N_ITEMS_PER_EPISODE)
    named = int(rng.integers(N_AGENTS))
    own_item = int(rng.integers(N_ITEMS_PER_EPISODE))
    other_item = int(rng.integers(N_ITEMS_PER_EPISODE))
    action_order = list(rng.permutation(2))      # which condition speaks first
    return dict(markers=[int(m) for m in markers], items=[int(i) for i in items],
                values=values, order=[int(o) for o in order], named=named,
                own_item=own_item, other_item=other_item,
                action_order=[int(o) for o in action_order],
                collide_pair=collide_pair, pool=pool)


def eligible_models(content: dict) -> list[int]:
    """Agents that may be the model: anyone but the agent the named-other
    condition names, so that a twin never names itself."""
    return [a for a in range(N_AGENTS) if a != content["named"]]


def render(content: dict, model: int) -> dict:
    """Tokens and index tensors for one episode. The token sequence does NOT
    depend on `model`; only `acting` and the two targets do."""
    markers, items, values = content["markers"], content["items"], content["values"]
    toks: list[int] = [VOCAB[BOS]]
    acting = [0]
    assign_value_pos = np.full((N_AGENTS, N_ITEMS_PER_EPISODE), -1, dtype=np.int64)
    assign_marker_pos = np.full((N_AGENTS, N_ITEMS_PER_EPISODE), -1, dtype=np.int64)
    assign_turn_index = np.full((N_AGENTS, N_ITEMS_PER_EPISODE), -1, dtype=np.int64)

    for turn, code in enumerate(content["order"]):
        a, j = int(code) // N_ITEMS_PER_EPISODE, int(code) % N_ITEMS_PER_EPISODE
        mine = 1 if a == model else 0
        assign_marker_pos[a, j] = len(toks)
        toks.append(VOCAB[MARKERS[markers[a]]])
        toks.append(VOCAB["assign"])
        toks.append(VOCAB[ITEMS[items[j]]])
        assign_value_pos[a, j] = len(toks)
        toks.append(VOCAB[SLOTS[int(values[a, j])]])
        toks.append(VOCAB[NL])
        acting.extend([mine] * 5)
        assign_turn_index[a, j] = turn

    action_pos = np.zeros(2, dtype=np.int64)
    action_item = np.zeros(2, dtype=np.int64)
    action_who = np.zeros(2, dtype=np.int64)     # agent index, or N_AGENTS = self
    action_turn = np.zeros(2, dtype=np.int64)
    targets = np.zeros(2, dtype=np.int64)
    source_turn = np.zeros(2, dtype=np.int64)

    for slot_i, cond in enumerate(content["action_order"]):
        if cond == OWN:
            who_tok, who_idx = VOCAB[SELF], N_AGENTS
            j = content["own_item"]
            src = model
        else:
            who_tok, who_idx = VOCAB[MARKERS[markers[content["named"]]]], content["named"]
            j = content["other_item"]
            src = content["named"]
        toks.append(VOCAB[ACT])
        toks.append(VOCAB["revise"])
        toks.append(who_tok)
        toks.append(VOCAB[ITEMS[items[j]]])
        toks.append(VOCAB[ANS])
        action_pos[cond] = len(toks)
        toks.append(MASK_ID)
        toks.append(VOCAB[NL])
        acting.extend([1 if cond == OWN else NAMED_OTHER_ACTING] * 7)
        action_item[cond] = j
        action_who[cond] = who_idx
        action_turn[cond] = 8 + slot_i
        targets[cond] = VOCAB[SLOTS[successor(int(values[src, j]))]]
        source_turn[cond] = assign_turn_index[src, j]

    toks.append(VOCAB[EOS])
    acting.append(0)
    assert len(toks) == SEQ_LEN, (len(toks), SEQ_LEN)

    assign_agent_at = np.full(SEQ_LEN, -1, dtype=np.int64)
    for a in range(N_AGENTS):
        for j in range(N_ITEMS_PER_EPISODE):
            assign_agent_at[assign_marker_pos[a, j]] = a

    return dict(
        tokens=np.array(toks, dtype=np.int64),
        acting=np.array(acting, dtype=np.int64),
        assign_value_pos=assign_value_pos,
        assign_marker_pos=assign_marker_pos,
        assign_agent_at=assign_agent_at,
        agent_marker_tok=np.array([VOCAB[MARKERS[markers[a]]] for a in range(N_AGENTS)],
                                  dtype=np.int64),
        action_pos=action_pos, action_item=action_item, action_who=action_who,
        action_turn=action_turn, targets=targets, source_turn=source_turn,
        model=model, values=values.copy(), named=content["named"],
        own_item=content["own_item"], other_item=content["other_item"],
    )


def make_pairs(n_pairs: int, seed: int, pool: str = "train",
               collide: bool = False) -> list[dict]:
    """`n_pairs` matched pairs. Each pair shares its content and rotates which
    agent the model is, so recipient and donor differ only in the acting
    channel. The value the donor's identity dictates is already present in the
    recipient's own context."""
    rng = np.random.default_rng(seed)
    pairs = []
    for _ in range(n_pairs):
        content = _content(rng, pool, collide)
        elig = eligible_models(content)
        r, d = rng.choice(elig, size=2, replace=False)
        pairs.append(dict(recipient=render(content, int(r)),
                          donor=render(content, int(d)),
                          content=content))
    return pairs


def episodes_from_pairs(pairs: list[dict]) -> list[dict]:
    """Both halves of every pair, which is what the arms train on."""
    out = []
    for p in pairs:
        out.append(p["recipient"])
        out.append(p["donor"])
    return out


BATCH_KEYS = ["tokens", "acting", "assign_value_pos", "assign_marker_pos",
              "assign_agent_at", "agent_marker_tok", "action_pos", "action_item",
              "action_who", "targets"]


def batch(episodes: list[dict]) -> dict:
    """Stack episodes into arrays. Field names match `render`."""
    return {k: np.stack([e[k] for e in episodes]) for k in BATCH_KEYS}


def named_swap(pairs: list, seed: int) -> list:
    """Control 2's donor: the same content and the same acting agent, with the
    named agent replaced by one that is neither the actor nor the original
    named agent. One token of text differs. Copied from the rehearsal's
    `repairs.named_swap`."""
    rng = np.random.default_rng(seed)
    out = []
    for p in pairs:
        c, r = p["content"], p["recipient"]["model"]
        choices = [a for a in range(N_AGENTS) if a not in (r, c["named"])]
        c2 = dict(c, named=int(rng.choice(choices)))
        out.append(render(c2, r))
    return out


# ------------------------------------------- disjointness and streaming

def fingerprint(content: dict) -> bytes:
    """What makes two episodes' content the same: every random draw that goes
    into it except who the model is."""
    h = hashlib.blake2b(digest_size=16)
    for key in ("markers", "items", "order", "action_order"):
        h.update(np.asarray(content[key], dtype=np.int64).tobytes())
    h.update(np.asarray(content["values"], dtype=np.int64).tobytes())
    h.update(np.asarray([content["named"], content["own_item"], content["other_item"]],
                        dtype=np.int64).tobytes())
    return h.digest()


def eval_pairs(name: str) -> list[dict]:
    n, seed, pool, relaxed = EVAL_SETS[name]
    return make_pairs(n, seed=seed, pool=pool, collide=relaxed)


def eval_fingerprints() -> set[bytes]:
    """Every content in every evaluation set. Training skips these."""
    out: set[bytes] = set()
    for name in EVAL_SETS:
        out |= {fingerprint(p["content"]) for p in eval_pairs(name)}
    return out


# Version 4, section 7.1: training contains no fresh or relaxed pairing. By
# John's ruling of 2026-10-06 this is guaranteed by the stream, not sampled.
PAIRING_EXCLUDED_SETS = ("fresh", "relaxed")


def pairing(content: dict) -> frozenset:
    """An episode's pairing: its assignment table, the set of (marker word,
    item word, value word) triples, one per agent and item. It is built from
    the markers, items and values only, so it ignores the turn order, the
    named agent, the asked-about items, the action order and the order in
    which agents and items are listed. The same table as the A2 branch's
    stricter control 5 check."""
    markers, items, values = content["markers"], content["items"], content["values"]
    return frozenset((int(markers[a]), int(items[j]), int(values[a][j]))
                     for a in range(N_AGENTS) for j in range(N_ITEMS_PER_EPISODE))


def held_out_pairings() -> set[frozenset]:
    """The pairing of every fresh and relaxed episode. Training skips these."""
    return {pairing(p["content"]) for name in PAIRING_EXCLUDED_SETS for p in eval_pairs(name)}


# What the evaluation sets and the first training batch of seed 0 are, as
# built on the laptop on 2026-10-04 (numpy 2.5.0). The rented machine has its
# own numpy; if it built different episodes from the same seeds, training
# would skip the wrong ones and the sets would no longer be disjoint by
# construction. The self-test, which the machine runs before any training
# step, fails if either differs, and the launcher then deletes the machine.
EVAL_SETS_DIGEST = "0cc3dafb2348eec07d8b4c0c9e9f3263809102f656bffc344c65a97577a8cf1f"
FIRST_BATCH_DIGEST = "81a96f086be9d09f09acc6aa052fbf28521b2b170177462f6044881e8eec8659"


def eval_sets_digest() -> str:
    h = hashlib.sha256()
    for f in sorted(eval_fingerprints()):
        h.update(f)
    return h.hexdigest()


def check_even_split(n_rows: int) -> bool:
    """The even-split rule, ledger item RT-58. Rows arrive as matched pairs,
    so any number of rows that is odd cuts a pair in half."""
    return n_rows > 0 and n_rows % 2 == 0


class TrainingStream:
    """Training episodes, generated fresh for every step.

    Step `s` of a run with seed `k` draws its pairs from the generator seeded
    with `(1000 + k, s)`, so a resumed run sees exactly the episodes it would
    have seen, and two runs with different seeds see different ones. A content
    is used only if `admits` passes it; anything else is skipped and counted.

    Two exclusion lists: `excluded`, whole contents (every evaluation set), and
    `excluded_pairings`, pairings (the fresh and relaxed sets; John's ruling of
    2026-10-06). Each defaults to the full list when not given."""

    def __init__(self, run_seed: int, excluded: set[bytes] | None = None,
                 excluded_pairings: set[frozenset] | None = None):
        self.run_seed = int(run_seed)
        self.excluded = eval_fingerprints() if excluded is None else excluded
        self.excluded_pairings = (held_out_pairings() if excluded_pairings is None
                                  else excluded_pairings)
        self.skipped = 0

    def admits(self, content: dict) -> bool:
        """The whole exclusion, in one place: not the whole content of any
        evaluation episode, and not the pairing of any fresh or relaxed one."""
        return (fingerprint(content) not in self.excluded
                and pairing(content) not in self.excluded_pairings)

    def pairs_for_step(self, step: int, n_pairs: int) -> list[dict]:
        rng = np.random.default_rng([1000 + self.run_seed, int(step)])
        pairs = []
        while len(pairs) < n_pairs:
            content = _content(rng, "train", False)
            if not self.admits(content):
                self.skipped += 1
                continue
            r, d = rng.choice(eligible_models(content), size=2, replace=False)
            pairs.append(dict(recipient=render(content, int(r)),
                              donor=render(content, int(d)), content=content))
        return pairs

    def batch_for_step(self, step: int, rows: int) -> dict:
        if not check_even_split(rows):
            raise ValueError(f"the even-split rule (RT-58): {rows} rows would cut a "
                             f"matched pair; use an even number")
        return batch(episodes_from_pairs(self.pairs_for_step(step, rows // 2)))


def scored_token_check(b: dict) -> list[str]:
    """The one-scored-token check (RT-59) on a built batch. Returns the
    problems found; an empty list is a pass."""
    problems = []
    tok, ap, tgt = b["tokens"], b["action_pos"], b["targets"]
    n = tok.shape[0]
    rows = np.arange(n)
    if ap.shape != (n, 2) or tgt.shape != (n, 2):
        problems.append(f"expected two supervised positions per episode, got {ap.shape}")
        return problems
    if not (ap[:, 0] != ap[:, 1]).all():
        problems.append("the two supervised positions coincide in some episode")
    for c in (OWN, OTHER):
        if not (tok[rows, ap[:, c]] == MASK_ID).all():
            problems.append(f"condition {c}: a scored position does not hold the mask word")
        if not (tok[rows, ap[:, c] - 1] == ANS_ID).all():
            problems.append(f"condition {c}: the token before a scored position is not the answer cue")
        if not np.isin(tgt[:, c], SLOT_IDS).all():
            problems.append(f"condition {c}: a target is not one of the eight value words")
    # the answer is never in the input after the cue: the only value words in
    # the input are the eight assignment values, all before the action turns
    first_action = ap.min(axis=1) - 5
    for i in range(n):
        tail = tok[i, first_action[i]:]
        if np.isin(tail, SLOT_IDS).any():
            problems.append(f"episode {i}: a value word appears inside the action turns")
            break
    if (tok == MASK_ID).sum(axis=1).tolist() != [2] * n:
        problems.append("an episode holds a number of mask words other than two")
    return problems


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("grammar.py self-test")
    pairs = make_pairs(3000, seed=20260921, pool="train")
    eps = episodes_from_pairs(pairs)

    same = all(np.array_equal(p["recipient"]["tokens"], p["donor"]["tokens"]) for p in pairs)
    check("matched pairs are token-for-token identical", same)
    differ = all(not np.array_equal(p["recipient"]["acting"], p["donor"]["acting"]) for p in pairs)
    check("matched pairs differ in the acting channel", differ)

    counts = []
    for p in pairs[:500]:
        v = p["content"]["values"]
        counts.append(len(set(v[:, p["content"]["own_item"]].tolist())))
        counts.append(len(set(v[:, p["content"]["other_item"]].tolist())))
    check("matched property 1: four distinct candidate values per item",
          set(counts) == {N_AGENTS}, f"distinct counts seen: {sorted(set(counts))}")

    d_own = [int(e["action_turn"][OWN] - e["source_turn"][OWN]) for e in eps]
    d_other = [int(e["action_turn"][OTHER] - e["source_turn"][OTHER]) for e in eps]
    h_own = np.bincount(np.array(d_own), minlength=12)[:12] / len(d_own)
    h_other = np.bincount(np.array(d_other), minlength=12)[:12] / len(d_other)
    gap = float(np.abs(h_own - h_other).max())
    check("matched property 2: distance distributions match", gap < 0.02,
          f"largest bin difference {gap:.4f} over {len(d_own)} episodes")

    sup_ok = all(len(e["targets"]) == 2 and len(set(e["action_pos"].tolist())) == 2 for e in eps)
    check("matched property 3: one supervised position of each kind", sup_ok)

    trans_ok = True
    for e in eps[:2000]:
        want_own = VOCAB[SLOTS[successor(int(e["values"][e["model"], e["own_item"]]))]]
        want_oth = VOCAB[SLOTS[successor(int(e["values"][e["named"], e["other_item"]]))]]
        trans_ok &= (e["targets"][OWN] == want_own and e["targets"][OTHER] == want_oth)
    check("matched property 4: the same successor rule in both conditions", trans_ok)

    turn_counts = {a: 0 for a in range(N_AGENTS)}
    for code in pairs[0]["content"]["order"]:
        turn_counts[code // N_ITEMS_PER_EPISODE] += 1
    check("no turn-count cue: every agent takes the same number of turns",
          set(turn_counts.values()) == {2})
    who_toks = {int(e["tokens"][e["action_pos"][OWN] - 3]) for e in eps[:500]}
    check("no name badge: the own-directed turn shows only the self word",
          who_toks == {VOCAB[SELF]})
    act_own = {int(e["acting"][e["action_pos"][OWN]]) for e in eps[:500]}
    act_other = {int(e["acting"][e["action_pos"][OTHER]]) for e in eps[:500]}
    check("the acting channel fires at both scored positions (fixed, version 4 section 4.1)",
          act_own == {1} and act_other == {1})

    # --- the evaluation sets are disjoint from one another ----------------
    fps = {name: [fingerprint(p["content"]) for p in eval_pairs(name)] for name in EVAL_SETS}
    sizes = {name: len(v) for name, v in fps.items()}
    check("evaluation sets have the registered sizes",
          sizes == {"dev": 600, "fresh": 800, "relaxed": 800, "gate": 1500, "trajectory": 200},
          str(sizes))
    names = list(EVAL_SETS)
    overlap = {f"{a}/{b}": len(set(fps[a]) & set(fps[b]))
               for i, a in enumerate(names) for b in names[i + 1:]}
    check("no content is shared between any two evaluation sets",
          sum(overlap.values()) == 0, str({k: v for k, v in overlap.items() if v}))
    within = {name: len(v) - len(set(v)) for name, v in fps.items()}
    check("no content repeats inside an evaluation set (fresh, at least)",
          within["fresh"] == 0, f"repeats per set {within}")

    # --- the streamed training data -----------------------------------------
    excluded = set().union(*map(set, fps.values()))
    st = TrainingStream(run_seed=0, excluded=excluded)
    b1 = st.batch_for_step(1, 96)
    b1_again = TrainingStream(run_seed=0, excluded=excluded).batch_for_step(1, 96)
    check("a step's batch is the same every time it is generated (resume-safe)",
          all(np.array_equal(b1[k], b1_again[k]) for k in BATCH_KEYS))
    b1_other_seed = TrainingStream(run_seed=1, excluded=excluded).batch_for_step(1, 96)
    check("a different run seed gives different episodes",
          not np.array_equal(b1["tokens"], b1_other_seed["tokens"]))
    check("rows 2k and 2k+1 of a streamed batch are a matched pair",
          all(np.array_equal(b1["tokens"][2 * i], b1["tokens"][2 * i + 1])
              and not np.array_equal(b1["acting"][2 * i], b1["acting"][2 * i + 1])
              for i in range(48)))
    seen = set()
    for s in range(1, 401):
        for p in st.pairs_for_step(s, 48):
            seen.add(fingerprint(p["content"]))
    check("streamed training content never matches an evaluation set",
          not (seen & excluded), f"{len(seen):,} training contents over 400 steps, "
                                 f"{len(seen & excluded)} shared")
    # a planted match is skipped, which is the exclusion working rather than luck
    planted = TrainingStream(run_seed=0, excluded=set())
    victim = planted.pairs_for_step(7, 48)[3]["content"]
    planted2 = TrainingStream(run_seed=0, excluded={fingerprint(victim)})
    got = [fingerprint(p["content"]) for p in planted2.pairs_for_step(7, 48)]
    check("a training content planted in the exclusion list is skipped",
          fingerprint(victim) not in got and planted2.skipped == 1 and len(got) == 48)

    # --- control 5, unseen combinations (RT-255, adopted 2026-10-06) ---------
    # No fresh or relaxed episode's combination occurs in the training stream.
    # A "combination" is the episode's whole content (every random draw except
    # which agent the model is), which is what `fingerprint` covers. Two parts:
    # the default stream's exclusion list holds every fresh and relaxed content,
    # so the stream cannot yield one at any step; and over sampled steps of the
    # default stream none appears.
    held = set(fps["fresh"]) | set(fps["relaxed"])
    default_stream = TrainingStream(run_seed=0)
    sampled = set()
    for s in range(1, 201):
        for p in default_stream.pairs_for_step(s, 48):
            sampled.add(fingerprint(p["content"]))
    check("control 5: no fresh or relaxed episode's combination occurs in the training stream "
          "(every one is in the stream's exclusion list, and none in 200 sampled steps)",
          held <= default_stream.excluded and not (sampled & held),
          f"{len(held):,} fresh and relaxed contents; {len(sampled):,} training contents sampled, "
          f"{len(sampled & held)} shared; {default_stream.skipped} skipped by the exclusion")

    # Stricter (John, 2026-10-06 follow-up): the pairing that makes an episode
    # fresh or relaxed, i.e. its assignment table of (marker word, item word,
    # value) triples (version 4, section 7.1: unseen combinations of marker
    # words, items and values), ignoring turn order, the named agent, the
    # items the actions name and the action order. Sampled, not guaranteed:
    # the stream's exclusion is by whole content.
    def table(c):
        return frozenset((int(c["markers"][a]), int(c["items"][j]), int(c["values"][a, j]))
                         for a in range(N_AGENTS) for j in range(N_ITEMS_PER_EPISODE))
    held_tables = {table(p["content"]) for name in ("fresh", "relaxed") for p in eval_pairs(name)}
    sampled_tables = set()
    st5 = TrainingStream(run_seed=0, excluded=default_stream.excluded)
    for s in range(1, 201):
        for p in st5.pairs_for_step(s, 48):
            sampled_tables.add(table(p["content"]))
    check("control 5, stricter: no fresh or relaxed episode's assignment table (which marker holds "
          "which value on which item) occurs in 200 sampled training steps",
          not (sampled_tables & held_tables),
          f"{len(held_tables):,} fresh and relaxed tables; {len(sampled_tables):,} training tables, "
          f"{len(sampled_tables & held_tables)} shared")

    # --- this machine builds the episodes the laptop built -----------------
    check("the evaluation sets are the ones built on the laptop (pinned digest)",
          eval_sets_digest() == EVAL_SETS_DIGEST)
    fb = TrainingStream(0, excluded=set()).batch_for_step(1, 96)
    check("the first training batch of seed 0 is the one built on the laptop (pinned digest)",
          hashlib.sha256(fb["tokens"].tobytes() + fb["acting"].tobytes()).hexdigest() == FIRST_BATCH_DIGEST)

    # --- the two carried-over rules on the built generator ------------------
    check("even-split rule (RT-58): an even row count is accepted, an odd one is not",
          check_even_split(96) and not check_even_split(95) and not check_even_split(0))
    try:
        st.batch_for_step(2, 95)
        check("even-split rule (RT-58): the stream refuses an odd batch", False)
    except ValueError:
        check("even-split rule (RT-58): the stream refuses an odd batch", True)
    probs = scored_token_check(b1) + scored_token_check(batch(eps[:2000]))
    check("one-scored-token check (RT-59): two scored positions, each the mask word, "
          "after the answer cue, targets are value words, no value word in the action turns",
          not probs, "; ".join(probs))
    broken = {k: v.copy() for k, v in b1.items()}
    broken["tokens"][0, broken["action_pos"][0, OWN]] = broken["targets"][0, OWN]
    check("one-scored-token check (RT-59) catches an answer leaked into the input",
          bool(scored_token_check(broken)))
    shifted = {k: v.copy() for k, v in b1.items()}
    shifted["action_pos"] = shifted["action_pos"] - 1
    check("one-scored-token check (RT-59) catches scoring shifted by one position",
          bool(scored_token_check(shifted)))

    # --- fresh and relaxed pairings never reach training (2026-10-06) ------
    # John's ruling of 2026-10-06: guaranteed, not sampled. Method note and
    # the made-up cases' expected results, committed before this ran:
    # docs/2026-10-06-successor-training-exclusion-pairing-method.md.
    held_contents = [p["content"] for name in PAIRING_EXCLUDED_SETS for p in eval_pairs(name)]
    want_pairings = {frozenset((int(c["markers"][a]), int(c["items"][j]), int(c["values"][a, j]))
                               for a in range(N_AGENTS) for j in range(N_ITEMS_PER_EPISODE))
                     for c in held_contents}
    default_stream = TrainingStream(run_seed=0)
    check("G1: the stream's pairing exclusion list is every fresh and relaxed pairing, and only those",
          default_stream.excluded_pairings == want_pairings and held_out_pairings() == want_pairings,
          f"{len(held_contents):,} fresh and relaxed episodes, {len(want_pairings):,} distinct pairings")

    import itertools

    def relisted(c: dict, agent_order, item_order, rng) -> dict:
        """The same pairing, listed differently, with everything else that is
        not the pairing drawn again."""
        ao, io = list(agent_order), list(item_order)
        return dict(
            markers=[c["markers"][a] for a in ao],
            items=[c["items"][j] for j in io],
            values=np.asarray(c["values"])[np.ix_(ao, io)].copy(),
            order=[int(o) for o in rng.permutation(N_AGENTS * N_ITEMS_PER_EPISODE)],
            named=int(rng.integers(N_AGENTS)),
            own_item=int(rng.integers(N_ITEMS_PER_EPISODE)),
            other_item=int(rng.integers(N_ITEMS_PER_EPISODE)),
            action_order=[int(o) for o in rng.permutation(2)],
            collide_pair=None, pool="train")

    rng_g2 = np.random.default_rng(20261006)
    tried = refused = 0
    same_pairing = True
    for c in held_contents:
        tried += 1
        refused += not default_stream.admits(c)
        for ao in itertools.permutations(range(N_AGENTS)):
            for io in itertools.permutations(range(N_ITEMS_PER_EPISODE)):
                v = relisted(c, ao, io, rng_g2)
                same_pairing &= pairing(v) == pairing(c)
                tried += 1
                refused += not default_stream.admits(v)
    check("G2: the exclusion function refuses every fresh and relaxed episode and every "
          "re-listing of it (all agent and item orders, turns, named agent, asked items and "
          "action order changed)",
          same_pairing and tried == len(held_contents) * 49 and refused == tried,
          f"{refused:,} of {tried:,} refused")

    victim = TrainingStream(run_seed=0, excluded=set(), excluded_pairings=set()).pairs_for_step(7, 48)[3]["content"]
    pl = TrainingStream(run_seed=0, excluded=set(), excluded_pairings={pairing(victim)})
    got = [pairing(p["content"]) for p in pl.pairs_for_step(7, 48)]
    check("G3: a training pairing planted only in the pairing list is skipped by the stream",
          pairing(victim) not in got and pl.skipped == 1 and len(got) == 48)
    twin = relisted(victim, (3, 1, 0, 2), (1, 0), np.random.default_rng(7))
    pl2 = TrainingStream(run_seed=0, excluded=set(), excluded_pairings={pairing(twin)})
    got2 = [pairing(p["content"]) for p in pl2.pairs_for_step(7, 48)]
    check("G3: planting a same-table copy with a different turn order (and listing), which no "
          "whole-content rule matches, makes training skip the original all the same",
          fingerprint(twin) != fingerprint(victim) and twin["order"] != victim["order"]
          and pairing(twin) == pairing(victim) and pairing(victim) not in got2
          and pl2.skipped == 1 and len(got2) == 48)

    # The made-up cases. Expected (method note, section 4, committed first):
    # A and B: the old whole-content rule lets them through, the new one
    # blocks them. C: both let it through.
    every_eval = eval_fingerprints()
    old_rule = TrainingStream(run_seed=0, excluded=every_eval, excluded_pairings=set())

    def made_up(c: dict) -> dict:
        n = N_AGENTS
        return dict(
            markers=list(reversed(c["markers"])),
            items=list(reversed(c["items"])),
            values=np.asarray(c["values"])[::-1, ::-1].copy(),
            order=list(reversed(c["order"])),
            named=(n - 1 - c["named"] + 1) % n,
            own_item=1 - (N_ITEMS_PER_EPISODE - 1 - c["own_item"]),
            other_item=1 - (N_ITEMS_PER_EPISODE - 1 - c["other_item"]),
            action_order=list(reversed(c["action_order"])),
            collide_pair=None, pool="train")

    case_a = made_up(eval_pairs("fresh")[0]["content"])
    case_b = made_up(eval_pairs("relaxed")[0]["content"])
    case_c = dict(case_a, values=case_a["values"].copy())
    case_c["values"][[0, 1], 0] = case_c["values"][[1, 0], 0]
    verdicts = {name: ("through" if old_rule.admits(c) else "blocked",
                       "through" if default_stream.admits(c) else "blocked")
                for name, c in (("A", case_a), ("B", case_b), ("C", case_c))}
    expected = {"A": ("through", "blocked"), "B": ("through", "blocked"),
                "C": ("through", "through")}
    check("G4: case A (a fresh pairing re-dressed) gets through the old rule and is blocked by the new",
          verdicts["A"] == expected["A"] and pairing(case_a) == pairing(eval_pairs("fresh")[0]["content"]),
          f"old {verdicts['A'][0]}, new {verdicts['A'][1]}")
    check("G4: case B (a relaxed pairing re-dressed) gets through the old rule and is blocked by the new",
          verdicts["B"] == expected["B"] and pairing(case_b) == pairing(eval_pairs("relaxed")[0]["content"]),
          f"old {verdicts['B'][0]}, new {verdicts['B'][1]}")
    check("G4: case C (case A with two values swapped) gets through both rules",
          verdicts["C"] == expected["C"], f"old {verdicts['C'][0]}, new {verdicts['C'][1]}")

    # --- the copy is the rehearsal's generator ------------------------------
    import importlib.util
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    reh = os.path.join(here, "..", "..", "rehearsal-successor-measure", "src", "grammar.py")
    if os.path.exists(reh):
        spec = importlib.util.spec_from_file_location("rehearsal_grammar", reh)
        RG = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(RG)
        ok = RG.VOCAB == VOCAB and RG.SEQ_LEN == SEQ_LEN
        for name, (n, seed, pool, relaxed) in EVAL_SETS.items():
            if name == "trajectory":
                continue
            a = batch(episodes_from_pairs(make_pairs(n, seed, pool, relaxed)))
            b = RG.batch(RG.episodes_from_pairs(RG.make_pairs(n, seed, pool, relaxed)))
            ok &= all(np.array_equal(a[k], b[k]) for k in BATCH_KEYS)
        check("the toy's evaluation sets come out array for array as the rehearsal "
              "generator builds them", ok)
    else:
        # On the rented machine only this folder is pushed. The comparison is a
        # property of the committed code, checked on the laptop; it is not
        # something the machine can add to.
        print("  [SKIP] comparison with the rehearsal generator: not present on this machine")

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
