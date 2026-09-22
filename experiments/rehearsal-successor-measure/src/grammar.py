"""The matched-role revision grammar, shrunk to rehearsal scale.

UNREGISTERED. This is a stand-in built for the measurement rehearsal of the
successor experiment proposal (`docs/successor-experiment-proposal-2026-09-21.md`,
section 4). It is not the registered generator, it trains nothing on its own,
it costs nothing, and no result about the scientific question may be read off
anything it produces.

What one episode is
-------------------
Four agents, two items, eight value slots, and a closed vocabulary.

- **Eight assignment turns**, one per (agent, item) pair, in a uniformly
  random order, rendered `<marker> assign <item> <value>`. Within an item the
  four values are distinct, so the four assignments differ only in who made
  them.
- **Two action turns**, last, in a random order between them, rendered
  `<act> revise <who> <item> <ans> <mask>`:
    * **own-directed** — `<who>` is the special word meaning *your own*, and
      the answer is the successor of the model's own earlier value on that
      item;
    * **named-other-directed** — `<who>` is another agent's marker word, and
      the answer is the successor of that agent's earlier value on that item.
  Both are actions at the model's own turn, supervised the same way and
  scored the same way. That is the whole point of the redesign the proposal
  makes: in the closed Amendment A3 design the ownership condition was an
  action and its comparison was a question at the end of the episode, so the
  two were never at the same kind of position.

Two departures from the registered A3 grammar, both deliberate
--------------------------------------------------------------
1. **The action turn carries no marker word.** In `curriculum_a3.py` the
   model's own turn renders its own marker three tokens before it acts, and
   that module's own header records the consequence as an honest limit: a
   model can read a name badge at the moment it acts instead of having
   carried a binding. Here the only route to the ownership answer is the
   acting channel.
2. **The answer token is never shown.** The slot where the answer goes is a
   dedicated `<mask>` word in the input, and the model's prediction is read
   at that position. Nothing downstream ever sees the answer.

Together these make a matched pair of episodes — the same content with a
different agent being the model — come out **token-for-token identical**,
differing only in which positions the acting channel fires on. That is what
lets a transplant between the two be a clean comparison: nothing but
ownership can differ anywhere in the state.

What is matched, and checked rather than asserted (proposal section 4.2)
------------------------------------------------------------------------
1. candidate count: four earlier values in context in both conditions;
2. distance: the gap between source assignment and action, same distribution;
3. supervision: one supervised position of each kind, one scored token each;
4. transformation: the same successor rule in both conditions.

Carried-forward rules from the red-team ledger of experiment 06
---------------------------------------------------------------
- the **even-split rule** (ledger item `RT-58`, the batch-split bias check):
  any batch fraction that splits rows must not cut the generator's matched
  pairs;
- the **one-scored-token check** (ledger item `RT-59`, the check that exactly
  one token per supervised position is scored and that the check survives the
  shift the loss function applies). Here the answer is scored **at** the
  `<mask>` position rather than at the position before it, so the shift does
  not arise; the self-test asserts that too, rather than leaving it implied.

Corrigibility: this module generates data. It trains nothing, launches
nothing, rents nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python grammar.py --self-test
"""
from __future__ import annotations

import argparse

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

# Disjoint pools, so the fresh set carries marker and content combinations
# that appear in neither the training nor the development set (proposal
# section 7.1, and control 5 of section 7.3).
POOLS = {
    "train": (list(range(0, 12)), list(range(0, 5))),
    "dev": (list(range(0, 12)), list(range(0, 5))),
    "fresh": (list(range(12, 20)), list(range(5, 8))),
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
SLOT_IDS = np.array([VOCAB[s] for s in SLOTS], dtype=np.int64)

# 1 <bos> + 8 turns x 5 + 2 turns x 7 + 1 <eos>
SEQ_LEN = 1 + 8 * 5 + 2 * 7 + 1

OWN, OTHER = 0, 1          # the two conditions, in a fixed reporting order


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
        # One item where two agents share a value, so that control 6 of the
        # proposal ("who is acting, versus which value") has a cell in which
        # the donor's identity dictates the SAME value as the recipient's.
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
    # where the value token of each (agent, item) assignment sits
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
        acting.extend([1] * 7)
        action_item[cond] = j
        action_who[cond] = who_idx
        action_turn[cond] = 8 + slot_i
        targets[cond] = VOCAB[SLOTS[successor(int(values[src, j]))]]
        source_turn[cond] = assign_turn_index[src, j]

    toks.append(VOCAB[EOS])
    acting.append(0)
    assert len(toks) == SEQ_LEN, (len(toks), SEQ_LEN)

    # the agent whose marker keys each assignment turn, at the marker token —
    # a surface fact, and the only routing the ownership module needs
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
    recipient's own context — that is what keeps a successful transplant from
    importing an answer from outside."""
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


def batch(episodes: list[dict]) -> dict:
    """Stack episodes into arrays. Field names match `render`."""
    keys = ["tokens", "acting", "assign_value_pos", "assign_marker_pos",
            "assign_agent_at", "agent_marker_tok", "action_pos", "action_item",
            "action_who", "targets"]
    return {k: np.stack([e[k] for e in episodes]) for k in keys}


# ---------------------------------------------------------------- self-test

def _check_even_split(n_rows: int) -> bool:
    """The even-split rule, ledger item RT-58 (the batch-split bias check).
    Rows arrive as matched pairs, so any split that leaves an odd number of
    rows cuts a pair in half."""
    return n_rows % 2 == 0


def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("grammar.py self-test")
    pairs = make_pairs(3000, seed=20260921, pool="train")
    eps = episodes_from_pairs(pairs)

    # --- twins are token-for-token identical -----------------------------
    same = all(np.array_equal(p["recipient"]["tokens"], p["donor"]["tokens"])
               for p in pairs)
    check("matched pairs are token-for-token identical", same)
    differ = all(not np.array_equal(p["recipient"]["acting"], p["donor"]["acting"])
                 for p in pairs)
    check("matched pairs differ in the acting channel", differ)

    # --- matched property 1: candidate count ------------------------------
    counts = []
    for p in pairs[:500]:
        v = p["content"]["values"]
        counts.append(len(set(v[:, p["content"]["own_item"]].tolist())))
        counts.append(len(set(v[:, p["content"]["other_item"]].tolist())))
    check("matched property 1 — four distinct candidate values per item",
          set(counts) == {N_AGENTS}, f"distinct counts seen: {sorted(set(counts))}")

    # --- matched property 2: distance distribution ------------------------
    d_own, d_other = [], []
    for e in eps:
        d_own.append(int(e["action_turn"][OWN] - e["source_turn"][OWN]))
        d_other.append(int(e["action_turn"][OTHER] - e["source_turn"][OTHER]))
    h_own = np.bincount(np.array(d_own), minlength=12)[:12] / len(d_own)
    h_other = np.bincount(np.array(d_other), minlength=12)[:12] / len(d_other)
    gap = float(np.abs(h_own - h_other).max())
    check("matched property 2 — distance distributions match",
          gap < 0.02,
          f"largest bin difference {gap:.4f} over {len(d_own)} episodes; "
          f"mean distance own {np.mean(d_own):.3f} vs other {np.mean(d_other):.3f}")

    # --- matched property 3: supervision ----------------------------------
    sup_ok = all(len(e["targets"]) == 2 and len(set(e["action_pos"].tolist())) == 2
                 for e in eps)
    check("matched property 3 — one supervised position of each kind", sup_ok)
    mask_ok = all(e["tokens"][e["action_pos"][OWN]] == MASK_ID
                  and e["tokens"][e["action_pos"][OTHER]] == MASK_ID for e in eps)
    check("matched property 3 — every scored position holds the mask word", mask_ok)

    # --- matched property 4: transformation -------------------------------
    trans_ok = True
    for e in eps[:2000]:
        want_own = VOCAB[SLOTS[successor(int(e["values"][e["model"], e["own_item"]]))]]
        want_oth = VOCAB[SLOTS[successor(int(e["values"][e["named"], e["other_item"]]))]]
        trans_ok &= (e["targets"][OWN] == want_own and e["targets"][OTHER] == want_oth)
    check("matched property 4 — the same successor rule in both conditions", trans_ok)

    # --- the one-scored-token check, ledger item RT-59 ---------------------
    # Exactly one token is scored per supervised position, the scored position
    # is the mask position itself, and no shift is applied — so the check
    # cannot be defeated by the off-by-one the ledger item records.
    e = eps[0]
    scored = np.zeros(SEQ_LEN, dtype=np.int64)
    scored[e["action_pos"]] = 1
    check("one-scored-token check — exactly two scored tokens per episode",
          int(scored.sum()) == 2)
    check("one-scored-token check — scored at the mask position, unshifted",
          all(e["tokens"][pos] == MASK_ID for pos in e["action_pos"])
          and all(e["tokens"][pos - 1] == VOCAB[ANS] for pos in e["action_pos"]))

    # --- the even-split rule, ledger item RT-58 ---------------------------
    check("even-split rule — a paired batch has an even number of rows",
          _check_even_split(len(eps)) and not _check_even_split(len(eps) - 1))

    # --- no ownership cue in the text ------------------------------------
    # Every agent takes exactly two assignment turns and the action turns
    # carry no marker, so nothing about how much an agent speaks, or where,
    # can predict which agent the model is.
    turn_counts = {a: 0 for a in range(N_AGENTS)}
    for code in pairs[0]["content"]["order"]:
        turn_counts[code // N_ITEMS_PER_EPISODE] += 1
    check("no turn-count cue — every agent takes the same number of turns",
          set(turn_counts.values()) == {2})
    who_toks = set()
    for e in eps[:500]:
        who_toks.add(int(e["tokens"][e["action_pos"][OWN] - 3]))
    check("no name badge — the own-directed turn shows only the self word",
          who_toks == {VOCAB[SELF]})

    # --- the model identity is uniform over the three eligible agents -----
    ident = np.bincount([e["model"] for e in eps], minlength=N_AGENTS) / len(eps)
    check("model identity spread over all four agent slots",
          float(ident.min()) > 0.2, f"share per agent slot {np.round(ident, 3).tolist()}")

    # --- the fresh pool is disjoint ---------------------------------------
    fp = make_pairs(200, seed=7, pool="fresh")
    tr_m = {int(m) for p in pairs[:200] for m in p["content"]["markers"]}
    fr_m = {int(m) for p in fp for m in p["content"]["markers"]}
    tr_i = {int(i) for p in pairs[:200] for i in p["content"]["items"]}
    fr_i = {int(i) for p in fp for i in p["content"]["items"]}
    check("fresh episodes use markers and items seen in neither other set",
          not (tr_m & fr_m) and not (tr_i & fr_i))

    # --- the collision set, for control 6 ---------------------------------
    cp = make_pairs(400, seed=11, pool="dev", collide=True)
    same_val = 0
    for p in cp:
        c, r, d = p["content"], p["recipient"]["model"], p["donor"]["model"]
        if c["values"][r, c["own_item"]] == c["values"][d, c["own_item"]]:
            same_val += 1
    check("collision set supplies a same-value cell for control 6",
          same_val > 10, f"{same_val} of {len(cp)} pairs have donor and recipient "
                         f"dictating the same value")

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
