"""Closure check of RT-239, the episode format.

Version 5, section 4.1, registers the episode format in full. This script
generates episodes with the frozen generator and checks each registered field
on every episode, decoding the tokens itself (the model's marker word is found
from where the acting channel fires on the assignment turns, not from the
generator's own index fields; the generator's `content` is used only for the
named agent's index, to cross-check the decoded one).

    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-serious-findings-closure-check-scripts/episode_format.py

Writes `episode_format.json` beside it.
"""
from __future__ import annotations

import collections
import json
import os
import sys

import numpy as np

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "experiments/08-successor-degree/src"))
import grammar as G   # noqa: E402

W = G.IVOCAB          # id -> word


def decode(ep):
    t = [W[int(x)] for x in ep["tokens"]]
    a = [int(x) for x in ep["acting"]]
    return t, a


def check_episode(ep, relaxed, pool, fails):
    t, a = decode(ep)
    f = collections.OrderedDict()
    f["length is 56 tokens"] = len(t) == 56
    f["starts <bos>, ends <eos>"] = t[0] == "<bos>" and t[-1] == "<eos>"
    body = t[1:-1]
    assign = [body[5 * i:5 * i + 5] for i in range(8)]
    acts = [body[40 + 7 * i:40 + 7 * i + 7] for i in range(2)]
    f["ten turns: eight of five tokens, then two of seven"] = len(body) == 8 * 5 + 2 * 7
    f["each assignment turn is: marker, 'assign', item, value, newline"] = all(
        x[0].startswith("m") and x[1] == "assign" and x[2].startswith("it") and x[3].startswith("v")
        and x[4] == "<nl>" for x in assign)
    f["each action turn is: act word, 'revise', who-word, item, answer cue, mask word, newline"] = all(
        x[0] == "<act>" and x[1] == "revise" and x[3].startswith("it") and x[4] == "<ans>"
        and x[5] == "<mask>" and x[6] == "<nl>" for x in acts)
    markers = sorted({x[0] for x in assign})
    items = sorted({x[2] for x in assign})
    f["four agents (four marker words) and two items"] = len(markers) == 4 and len(items) == 2
    mpool, ipool = G.POOLS[pool]
    f[f"marker words and items from the pool ({pool}: m0-m11, it0-it4)"] = (
        all(int(m[1:]) in mpool for m in markers) and all(int(i[2:]) in ipool for i in items)
        and max(mpool) == 11 and max(ipool) == 4)
    pairs = collections.Counter((x[0], x[2]) for x in assign)
    f["eight assignment turns, one per agent and item"] = len(pairs) == 8 and set(pairs.values()) == {1}
    value = {(x[0], x[2]): int(x[3][1:]) for x in assign}
    f["eight value slots (v0-v7)"] = all(0 <= v < 8 for v in value.values())
    shared = []
    for it in items:
        vs = [value[(m, it)] for m in markers]
        shared.append(4 - len(set(vs)))
    if relaxed:
        f["relaxed set: exactly one item has two agents sharing a value, the other item distinct"] = (
            sorted(shared) == [0, 1])
    else:
        f["within an item the four values are distinct"] = shared == [0, 0]
    # who is the model: the marker of the assignment turns on which the acting channel fires
    mine = {assign[i][0] for i in range(8) if all(a[1 + 5 * i + k] == 1 for k in range(5))}
    off = {assign[i][0] for i in range(8) if all(a[1 + 5 * i + k] == 0 for k in range(5))}
    f["the acting channel fires on all of exactly one agent's two assignment turns, and on none of the rest"] = (
        len(mine) == 1 and len(off) == 3 and sum(a[1:41]) == 10)
    own_marker = next(iter(mine)) if len(mine) == 1 else None
    f["the acting channel fires on both action turns, every token"] = all(x == 1 for x in a[41:55])
    whos = [x[2] for x in acts]
    f["one action turn's who-word is the 'your own' word, the other's a marker word"] = (
        sorted(w == "<self>" for w in whos) == [False, True])
    named = next((w for w in whos if w != "<self>"), None)
    f["the named marker word is one of the episode's four agents"] = named in markers
    # departure 1: no marker word of the model's own in either action turn
    f["departure 1: the model's own marker word appears in neither action turn"] = (
        own_marker is not None and all(own_marker not in x for x in acts))
    f["departure 1: the token three before the own-directed answer slot is the 'your own' word"] = all(
        x[5 - 3] == "<self>" for x in acts if x[2] == "<self>")
    # departure 2: the answer is never shown; the slot holds the mask word
    tgt = {c: W[int(ep["targets"][c])] for c in (G.OWN, G.OTHER)}
    f["departure 2: the answer slot holds the mask word in both action turns"] = all(x[5] == "<mask>" for x in acts)
    f["departure 2: no value word appears in either action turn"] = all(
        not w.startswith("v") for x in acts for w in x)
    # the successor rule, from the decoded tokens
    own_turn = next(x for x in acts if x[2] == "<self>")
    oth_turn = next(x for x in acts if x[2] != "<self>")
    want_own = f"v{(value[(own_marker, own_turn[3])] + 1) % 8}" if own_marker else None
    want_oth = f"v{(value[(named, oth_turn[3])] + 1) % 8}"
    f["own-directed answer = successor of the model's own earlier value on that item, round eight"] = (
        tgt[G.OWN] == want_own)
    f["named-other answer = successor of the named agent's earlier value on that item, round eight"] = (
        tgt[G.OTHER] == want_oth)
    f["the scored positions are the two mask words"] = all(
        t[int(p)] == "<mask>" for p in ep["action_pos"])
    for k, ok in f.items():
        if not ok:
            fails[k] += 1
    return f, own_marker, named, whos


def main():
    out = {}
    sets = [(name, *G.EVAL_SETS[name]) for name in G.EVAL_SETS]
    sets.append(("train sample", 3000, 20261009, "train", False))
    print(f"vocabulary size {len(G.VOCAB)} words; episode length {G.SEQ_LEN} tokens")
    for name, n, seed, pool, relaxed in sets:
        pairs = G.make_pairs(n, seed=seed, pool=pool, collide=relaxed)
        fails = collections.Counter()
        names = None
        own_first = 0
        first_agent = collections.Counter()
        twin_same = twin_acting_differ = 0
        named_ok = 0
        for p in pairs:
            r, d = p["recipient"], p["donor"]
            twin_same += np.array_equal(r["tokens"], d["tokens"])
            twin_acting_differ += not np.array_equal(r["acting"], d["acting"])
            for ep in (r, d):
                f, own_marker, named, whos = check_episode(ep, relaxed, pool, fails)
                names = list(f)
                own_first += whos[0] == "<self>"
                named_ok += named == G.MARKERS[p["content"]["markers"][p["content"]["named"]]]
            first_agent[(p["content"]["order"][0] // 2)] += 1
        n_ep = 2 * len(pairs)
        res = dict(pairs=len(pairs), episodes=n_ep,
                   failures={k: fails[k] for k in names},
                   matched_pairs_token_identical=f"{twin_same} of {len(pairs)}",
                   matched_pairs_acting_differs=f"{twin_acting_differ} of {len(pairs)}",
                   decoded_named_agent_matches_generator=f"{named_ok} of {n_ep}",
                   own_directed_action_first_share=round(own_first / n_ep, 4),
                   first_assignment_turn_by_agent_index=dict(sorted(first_agent.items())))
        out[name] = res
        bad = {k: v for k, v in res["failures"].items() if v}
        print(f"\n== {name}: {len(pairs)} pairs, {n_ep} episodes (pool {pool}, relaxed {relaxed})")
        print(f"   every field holds on every episode: {not bad}" + (f"  FAILURES {bad}" if bad else ""))
        print(f"   matched pairs token-for-token identical: {res['matched_pairs_token_identical']}; "
              f"acting channel differs: {res['matched_pairs_acting_differs']}")
        print(f"   decoded named agent agrees with the generator: {res['decoded_named_agent_matches_generator']}")
        print(f"   share of episodes whose own-directed action comes first: {res['own_directed_action_first_share']}")
        print(f"   first assignment turn, by agent index: {res['first_assignment_turn_by_agent_index']}")
    print("\nfields checked on every episode:")
    for k in names:
        print(f"   - {k}")
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "episode_format.json"), "w"),
              indent=1)


if __name__ == "__main__":
    main()
