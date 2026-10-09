"""Checker's replay of the training stream under the NEW exclusion (pull request 151).

The session's own replay (`experiments/08-successor-degree/tests/replay_stream_dev_reads.py`)
re-implements the stream's draw loop. This one does not: it runs the frozen
code's own `grammar.TrainingStream.pairs_for_step`, with its default exclusion
as the pull request leaves it (every evaluation set, the 1,980 reads' set
included, plus the fresh and relaxed pairings), and only replaces `render`
with a no-op so no episode is drawn as tokens (rendering uses no random draw:
it is called after `rng.choice`, on the content alone).

If the stream skips nothing over the registered 108,919 steps of 48 pairs,
then no training draw is any excluded content, the 1,380 new ones included,
so the batches are the same under the old and the new exclusion.
It also counts drawn contents that are one of the 1,380, directly.

    cd <checkout> && python replay_real_stream.py SEED
Laptop, $0. Generator only; no model.
"""
import os
import sys
import time

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "experiments/08-successor-degree/src"))
import grammar as G  # noqa: E402

seed = int(sys.argv[1])
steps = int(sys.argv[2]) if len(sys.argv) > 2 else 108919
extra = {G.fingerprint(p["content"]) for p in G.eval_pairs("dev_reads")[600:]}
assert len(extra) == 1380
G.render = lambda content, who: None        # tokens are not needed; no random draw is skipped
st = G.TrainingStream(run_seed=seed)        # the default exclusion, as the pull request leaves it
assert extra <= st.excluded, "the 1,380 are not in the default exclusion"
n = hits = 0
t0 = time.time()
for s in range(1, steps + 1):
    for p in st.pairs_for_step(s, 48):
        n += 1
        if G.fingerprint(p["content"]) in extra:
            hits += 1
    if s % 20000 == 0:
        print(s, n, st.skipped, hits, round(time.time() - t0), flush=True)
print(f"seed {seed}: {n} training contents over {steps} steps under the new default exclusion "
      f"({len(st.excluded)} contents, {len(st.excluded_pairings)} pairings); skipped by it: {st.skipped}; "
      f"drawn contents among the 1,380: {hits}")
