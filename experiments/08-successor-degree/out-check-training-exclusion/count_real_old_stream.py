"""Checker's second count, independent of the author's replay: calls the REAL
old stream (main's grammar.py, TrainingStream.pairs_for_step, rendering and
all) for every one of the development runs' 108,919 steps of 48 pairs, seed 0,
and counts contents whose pairing is a fresh or relaxed pairing. Each step's
draws depend only on (seed, step), so the steps are split across processes.
Generator only; no model; laptop; $0.

usage: python count_real_old_stream.py BRANCH_SRC MAIN_GRAMMAR_PY [WORKERS]
"""
import importlib.util
import sys
import time
from multiprocessing import Pool

STEPS, NP = 108919, 48


def load(branch_src, main_py):
    sys.path.insert(0, branch_src)
    import grammar as G
    spec = importlib.util.spec_from_file_location("grammar_main", main_py)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    return G, old


def work(args):
    branch_src, main_py, lo, hi = args
    G, OLD = load(branch_src, main_py)
    held = G.held_out_pairings()
    st = OLD.TrainingStream(0)
    n = shared = 0
    hits = []
    for s in range(lo, hi):
        for i, p in enumerate(st.pairs_for_step(s, NP)):
            c = p["content"]
            n += 1
            shared += any(len(set(c["values"][:, j])) < G.N_AGENTS for j in range(G.N_ITEMS_PER_EPISODE))
            if G.pairing(c) in held:
                hits.append((s, i))
    return n, st.skipped, shared, hits


if __name__ == "__main__":
    branch_src, main_py = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    edges = [1 + (STEPS * k) // (workers * 8) for k in range(workers * 8 + 1)]
    edges[-1] = STEPS + 1
    chunks = [(branch_src, main_py, edges[k], edges[k + 1]) for k in range(len(edges) - 1)]
    t0 = time.time()
    tot_n = tot_skip = tot_shared = 0
    hits = []
    with Pool(workers) as pool:
        for k, (n, sk, sh, h) in enumerate(pool.imap(work, chunks)):
            tot_n += n; tot_skip += sk; tot_shared += sh; hits += h
            print(f"chunk {k + 1}/{len(chunks)} done, {tot_n:,} contents, {len(hits)} hits, "
                  f"{round(time.time() - t0)} s", flush=True)
    print(f"steps {STEPS:,}; contents {tot_n:,}; old-rule skips {tot_skip}; contents with a shared "
          f"value {tot_shared}; fresh or relaxed pairings {len(hits)} {hits}")
