"""Checker's script for pull request 115 (training exclusion by pairing).
Generator only; no model; laptop; $0.

usage: python check_stream.py BRANCH_SRC MAIN_GRAMMAR_PY [REPLAY_STEPS]

1. pairing() against main's "control 5, stricter" table, on every fresh and
   relaxed episode and on 20,000 training contents.
2. The replay script's draws against the real old stream (main's code) and the
   new stream, content by content, over the first REPLAY_STEPS steps of seed
   0, including which agents the eligible-model draw picks.
3. Whether step 1 of seed 0 (the pinned digest's batch) draws anything the
   new rule refuses, and the digest with no exclusion at all.
4. The relaxed half: the generator never shares a value in training; every
   relaxed pairing is refused; and a relaxed content planted into the stream's
   own draw is skipped by pairs_for_step.
"""
import hashlib
import importlib.util
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
import grammar as G  # noqa: E402  (the branch)

spec = importlib.util.spec_from_file_location("grammar_main", sys.argv[2])
OLD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OLD)
REPLAY_STEPS = int(sys.argv[3]) if len(sys.argv) > 3 else 2000

results = []


def report(name, ok, detail=""):
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)


# --- 1. the definition -------------------------------------------------------
def table_main(c):  # copied verbatim from main's grammar.py self-test
    return frozenset((int(c["markers"][a]), int(c["items"][j]), int(c["values"][a, j]))
                     for a in range(OLD.N_AGENTS) for j in range(OLD.N_ITEMS_PER_EPISODE))


held = [p["content"] for n in ("fresh", "relaxed") for p in G.eval_pairs(n)]
same = all(G.pairing(c) == table_main(c) for c in held)
rng = np.random.default_rng(12345)
train_cs = [G._content(rng, "train", False) for _ in range(20000)]
same_t = all(G.pairing(c) == table_main(c) for c in train_cs)
report("pairing() equals main's control 5 table on all 1,600 fresh and relaxed episodes "
       "and 20,000 training contents", same and same_t)
report("every pairing has 8 triples (4 agents x 2 items), so no information is lost",
       all(len(G.pairing(c)) == 8 for c in held + train_cs))
report("held_out_pairings() equals main's held_tables",
       G.held_out_pairings() == {table_main(c) for c in held})
report("the whole-content list still covers all five evaluation sets",
       G.eval_fingerprints() == OLD.eval_fingerprints()
       and set(G.EVAL_SETS) == {"dev", "fresh", "relaxed", "gate", "trajectory"}
       and G.EVAL_SETS == OLD.EVAL_SETS,
       f"{len(G.eval_fingerprints()):,} contents")
report("the pairing rule covers fresh and relaxed only", tuple(G.PAIRING_EXCLUDED_SETS) == ("fresh", "relaxed"))

# --- 2. the replay against the real streams ---------------------------------
excl = G.eval_fingerprints()


def replay_step(s, n_pairs=48):
    """count_old_stream.py's inner loop, verbatim, but keeping what it draws."""
    rng = np.random.default_rng([1000 + 0, s])
    got, out = 0, []
    while got < n_pairs:
        c = G._content(rng, "train", False)
        if G.fingerprint(c) in excl:
            continue
        r, d = rng.choice(G.eligible_models(c), size=2, replace=False)
        got += 1
        out.append((G.fingerprint(c), int(r), int(d)))
    return out


old_stream = OLD.TrainingStream(0)
new_stream = G.TrainingStream(0)
mismatch_old = mismatch_new = 0
first_bad = None
for s in range(1, REPLAY_STEPS + 1):
    rep = replay_step(s)
    old = [(OLD.fingerprint(p["content"]), int(p["recipient"]["model"]), int(p["donor"]["model"]))
           for p in old_stream.pairs_for_step(s, 48)]
    new = [(G.fingerprint(p["content"]), int(p["recipient"]["model"]), int(p["donor"]["model"]))
           for p in new_stream.pairs_for_step(s, 48)]
    if rep != old:
        mismatch_old += 1
        first_bad = first_bad or s
    if new != old:
        mismatch_new += 1
report(f"the replay draws exactly the old stream's contents and recipient/donor agents, "
       f"steps 1 to {REPLAY_STEPS:,}", mismatch_old == 0,
       f"{mismatch_old} steps differ (first {first_bad})")
report(f"the new stream draws exactly the old stream's episodes, steps 1 to {REPLAY_STEPS:,}",
       mismatch_new == 0 and new_stream.skipped == 0 and old_stream.skipped == 0,
       f"{mismatch_new} steps differ; skipped old {old_stream.skipped}, new {new_stream.skipped}")

# A replay that left out the eligible-model draw would diverge at once.
def replay_without_model_draw(s):
    rng = np.random.default_rng([1000, s])
    return [G.fingerprint(G._content(rng, "train", False)) for _ in range(48)]
report("negative control: a replay without the eligible-model draw diverges from the stream at step 1",
       replay_without_model_draw(1) != [x[0] for x in replay_step(1)])

# --- 3. the pinned first batch ----------------------------------------------
def digest(b):
    return hashlib.sha256(b["tokens"].tobytes() + b["acting"].tobytes()).hexdigest()


st_default = G.TrainingStream(0)
b_default = st_default.batch_for_step(1, 96)
b_pinned_call = G.TrainingStream(0, excluded=set()).batch_for_step(1, 96)
b_none = G.TrainingStream(0, excluded=set(), excluded_pairings=set()).batch_for_step(1, 96)
b_old = OLD.TrainingStream(0, excluded=set()).batch_for_step(1, 96)
report("pinned digest constant is the same on main and the branch",
       G.FIRST_BATCH_DIGEST == OLD.FIRST_BATCH_DIGEST and G.EVAL_SETS_DIGEST == OLD.EVAL_SETS_DIGEST)
report("step 1 of seed 0 draws nothing the new rule refuses, so its batch is the same under "
       "every exclusion (full, pairing only, none, main's)",
       st_default.skipped == 0
       and len({digest(b_default), digest(b_pinned_call), digest(b_none), digest(b_old)}) == 1
       and digest(b_none) == G.FIRST_BATCH_DIGEST,
       f"skipped {st_default.skipped}")

# --- 4. the relaxed half -----------------------------------------------------
relaxed = [p["content"] for p in G.eval_pairs("relaxed")]
shared = sum(any(len(set(c["values"][:, j])) < G.N_AGENTS for j in range(G.N_ITEMS_PER_EPISODE))
             for c in train_cs)
report("no training content among 20,000 gives two agents the same value on an item", shared == 0)
report("every relaxed episode does give two agents the same value on one item",
       all(any(len(set(c["values"][:, j])) < G.N_AGENTS for j in range(G.N_ITEMS_PER_EPISODE))
           for c in relaxed))
report("all 800 relaxed episodes are refused by admits, and their 800 pairings are in the list",
       all(not st_default.admits(c) for c in relaxed)
       and {G.pairing(c) for c in relaxed} <= st_default.excluded_pairings
       and len({G.pairing(c) for c in relaxed}) == 800)
fresh_p = {G.pairing(p["content"]) for p in G.eval_pairs("fresh")}
report("no relaxed pairing is also a fresh pairing (so the relaxed half is not covered by the fresh half)",
       not ({G.pairing(c) for c in relaxed} & fresh_p))

# Plant relaxed contents into the stream's own draw: the 2nd and 5th draws of
# step 3 are replaced by relaxed contents, re-dressed (agents and items listed
# in reverse, turn order reversed) so that no whole-content rule matches.
real_content = G._content


def redress(c):
    return dict(markers=list(reversed(c["markers"])), items=list(reversed(c["items"])),
                values=np.asarray(c["values"])[::-1, ::-1].copy(),
                order=list(reversed(c["order"])), named=c["named"], own_item=c["own_item"],
                other_item=c["other_item"], action_order=c["action_order"],
                collide_pair=None, pool="train")


planted = {1: redress(relaxed[0]), 4: redress(relaxed[1])}
calls = {"n": 0}


def patched(rng, pool, collide):
    c = real_content(rng, pool, collide)
    i = calls["n"]
    calls["n"] += 1
    return planted.get(i, c)


# The streams are built before patching: building one makes the evaluation
# sets, which also call _content.
st_p = G.TrainingStream(0)
calls["n"] = 0
G._content = patched
try:
    out = st_p.pairs_for_step(3, 48)
finally:
    G._content = real_content
got_p = {G.pairing(p["content"]) for p in out}
report("relaxed contents planted into the stream's own draw are skipped by pairs_for_step "
       "(re-dressed, so the whole-content rule alone would let them through)",
       st_p.skipped == 2 and len(out) == 48
       and G.pairing(planted[1]) not in got_p and G.pairing(planted[4]) not in got_p
       and all(G.fingerprint(v) not in excl for v in planted.values()),
       f"skipped {st_p.skipped}")
st_q = G.TrainingStream(0, excluded_pairings=set())
calls["n"] = 0
G._content = patched
try:
    out_q = st_q.pairs_for_step(3, 48)
finally:
    G._content = real_content
report("negative control: with the pairing list empty the same planted relaxed contents get through",
       st_q.skipped == 0 and G.pairing(planted[1]) in {G.pairing(p["content"]) for p in out_q})

print(f"\n{sum(results)} of {len(results)} passed")
