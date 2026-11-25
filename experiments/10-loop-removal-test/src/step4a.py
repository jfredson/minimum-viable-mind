"""Step 4a of the loop removal test: can the test be run at all? (design, section 9, step 4a)

Runs on a rented GPU machine, never on the Mac. Written on the Mac before any machine was rented, against the
model's published source in Hugging Face transformers at commit 046bdb8cc2cee29d233964bb77fe6fd37cfe4aa3
(src/transformers/models/inkling2_loop/modular_inkling2_loop.py, read 2026-11-21). It has not been run;
the first run on the machine is its test.

What the source shows, and what this script relies on:
- The text model's forward runs the looped layers once, then for each later pass it calls
  `self.message_input(previous_block_states, previous_hidden_states, loop_layer_idx)` once per looped layer
  and passes the result to the layer as `messages`. `previous_block_states` holds the previous pass's
  completed loop block sums, and `previous_hidden_states` its final running state. These are the "two block
  sums" of the design.
- Pass 1 calls the looped layers with no `messages`, and a layer given `messages=None` takes the same path as
  on pass 1. So making `message_input` return None on passes 2 and 3 is exactly the design's bypass.
- Each later pass restarts from the pre-loop hidden and block states, and has its own attention cache slots.
  These are the three facts the bypass check needs (design, section 3).
- The number of passes is read from `config.loop_num_passes` at every forward.

Every removal is done by replacing `message_input.forward` on the model instance, so nothing in the model's
weights or code is changed. Phases:
    env       software and GPU report
    load      load the model, report memory, find the text model and its message_input
    opening   how the model's reply opens, with reasoning "none" and the default (specification, section 9)
    floor     two unaltered runs over every pilot item; the noise floor
    identity  each item given its own recorded message must reproduce the unaltered run
    bypass    skipping the message on passes 2 and 3 must reproduce the one-pass run
    baseline  descriptive accuracy at 1, 2 and 3 passes on the pilot, chained items included (no outcome)

    python -I step4a.py --pilot <pilot dir> --out <out dir> [--phases env,load,opening,floor,identity,bypass,baseline]
"""
import argparse
import json
import os
import platform
import sys
import time

MODEL_ID = "thinkingmachines/TML-d24-varloop-research"
MODEL_REVISION = "657b53ba5da7baefe9ff15dca5cd25f5bd3dbaa2"  # the revision the tokeniser was downloaded at
TRANSFORMERS_COMMIT = "046bdb8cc2cee29d233964bb77fe6fd37cfe4aa3"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f]


def pilot_items(pilot):
    """Every scored item of the pilot as (id, prompt_ids, answer, candidates)."""
    items = []
    for p in load_jsonl(os.path.join(pilot, "pairs.jsonl")):
        for t in ("P", "R"):
            items.append({"id": f"{p['id']}:{t}", "kind": f"{p['rule_kind']}+{p['routine_kind']}:{t}",
                          "prompt_ids": p[t]["prompt_ids"], "answer": p[t]["answer"], "candidates": p[t]["candidates"]})
    for c in load_jsonl(os.path.join(pilot, "chained.jsonl")):
        items.append({"id": c["id"], "kind": f"chain{c['hops']}", "prompt_ids": c["prompt_ids"],
                      "answer": c["answer"], "candidates": c["candidates"]})
    return items


class Loop:
    """Holds the hooks on the text model's message_input."""

    def __init__(self, text_model):
        self.tm = text_model
        self.mi = text_model.message_input
        self.orig = self.mi.forward
        self.n_loop = text_model.config.loop_layer_index_end - text_model.config.loop_layer_index_start
        self.mode, self.calls, self.store, self.inject = None, 0, {}, None
        self.mi.forward = self._forward

    def passes(self, n=None):
        if n is not None:
            self.tm.config.loop_num_passes = n
        return self.tm.config.loop_num_passes

    def _forward(self, block_states, partial_block_states, loop_layer_idx):
        pass_no = 2 + self.calls // self.n_loop  # message_input is first called on pass 2
        self.calls += 1
        if self.mode == "bypass":
            return None
        if self.mode == "record" and loop_layer_idx == 0:
            self.store[pass_no] = (block_states.detach().clone(), partial_block_states.detach().clone())
        if self.mode == "replace":
            bs, ps = self.inject[pass_no]
            L = block_states.shape[1]
            block_states, partial_block_states = bs[:, :L].to(block_states), ps[:, :L].to(partial_block_states)
        return self.orig(block_states, partial_block_states, loop_layer_idx)

    def run(self, model, ids, mode=None, inject=None):
        import torch
        self.mode, self.calls, self.inject = mode, 0, inject
        if mode == "record":
            self.store = {}
        with torch.no_grad():
            out = model(input_ids=torch.tensor([ids], device=model.device), use_cache=False)
        self.mode = None
        return out.logits[0, -1].float()


def candidate_ids(tok, cands):
    ids = []
    for c in cands:
        e = tok.encode(c, add_special_tokens=False)
        if len(e) != 1:
            raise ValueError(f"candidate {c!r} is not one token: {e}")
        ids.append(e[0])
    return ids


def score(logits, cand_ids, answer_index):
    import torch
    lp = torch.log_softmax(logits, -1)[cand_ids]
    probs = torch.softmax(lp, -1)
    order = torch.argsort(lp, descending=True)
    best_wrong = max(lp[i].item() for i in range(len(cand_ids)) if i != answer_index)
    return {"logprobs": [round(x, 6) for x in lp.tolist()], "chosen": int(order[0]), "right": int(order[0]) == answer_index,
            "margin": round(lp[answer_index].item() - best_wrong, 6), "p_right": round(probs[answer_index].item(), 6)}


def maxdiff(a, b):
    return max(abs(x - y) for x, y in zip(a["logprobs"], b["logprobs"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--phases", default="env,load,opening,floor,identity,bypass,baseline")
    ap.add_argument("--limit", type=int, default=0, help="score only the first N items, for a quick first try")
    a = ap.parse_args()
    phases = a.phases.split(",")
    os.makedirs(a.out, exist_ok=True)
    R = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "phases": phases}

    def save():
        json.dump(R, open(os.path.join(a.out, "step4a-results.json"), "w"), indent=1)

    import torch
    import transformers
    R["env"] = {"python": platform.python_version(), "torch": torch.__version__, "transformers": transformers.__version__,
                "cuda": torch.version.cuda, "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
                "gpu_memory_gb": round(torch.cuda.get_device_properties(0).total_memory / 2**30, 1) if torch.cuda.is_available() else None}
    save()
    if phases == ["env"]:
        return

    from transformers import AutoConfig, AutoTokenizer
    t0 = time.time()
    cfg = AutoConfig.from_pretrained(MODEL_ID, revision=MODEL_REVISION)
    model = None
    for cls_name in ("AutoModelForImageTextToText", "AutoModelForCausalLM"):
        # Found on the machine, 2026-11-21: the checkpoint's 4-bit storage is labelled "modelopt", which transformers
        # at the pinned commit does not recognise; it skips the quantizer and unpacks the weights. With dtype "auto"
        # they came out at 32-bit (about 90 GB, out of memory on 96 GB). So the weights are unpacked to 16-bit
        # (bfloat16, about 53 GB). This is not the model's native 4-bit precision; the findings record it.
        for dtype_kw in ("dtype", "torch_dtype"):  # the keyword was renamed in recent transformers
            try:
                cls = getattr(transformers, cls_name)
                model = cls.from_pretrained(MODEL_ID, revision=MODEL_REVISION, device_map="cuda",
                                            **{dtype_kw: torch.bfloat16})
                R["load"] = {"class": cls_name, "dtype_keyword": dtype_kw, "dtype": "bfloat16"}
                break
            except Exception as e:  # record and try the next form
                R.setdefault("load_errors", []).append(f"{cls_name}/{dtype_kw}: {type(e).__name__}: {e}"[:2000])
        if model is not None:
            break
    if model is None:
        save()
        sys.exit("could not load the model; see load_errors")
    model.eval()
    tok = AutoTokenizer.from_pretrained(MODEL_ID, revision=MODEL_REVISION)
    text_models = [m for m in model.modules() if hasattr(m, "message_input") and hasattr(m, "layers")]
    if len(text_models) != 1:
        R["load"]["error"] = f"expected one text model with message_input, found {len(text_models)}"
        save()
        sys.exit(R["load"]["error"])
    loop = Loop(text_models[0])
    R["load"].update({"seconds": round(time.time() - t0, 1), "loop_num_passes": loop.passes(), "n_loop_layers": loop.n_loop,
                      "loop_layer_index_start": loop.tm.config.loop_layer_index_start,
                      "gpu_memory_allocated_gb": round(torch.cuda.memory_allocated() / 2**30, 2),
                      "config_model_type": getattr(cfg, "model_type", None)})
    save()

    items = pilot_items(a.pilot)
    if a.limit:
        items = items[:a.limit]
    for it in items:
        it["cand_ids"] = candidate_ids(tok, it["candidates"])
        it["answer_index"] = it["candidates"].index(it["answer"])

    if "opening" in phases:
        # how the reply opens (specification, section 9; design RT-400)
        from tokenizers import Tokenizer  # noqa: F401  (the pilot was tokenised with the same tokenizer.json)
        sample = load_jsonl(os.path.join(a.pilot, "pairs.jsonl"))[:3]
        rows = []
        for effort in ("none", None):
            for p in sample:
                msgs = [{"role": "user", "content": p["R"]["text"]}]
                kw = {"reasoning_effort": effort} if effort else {}
                rendered = tok.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False, **kw)
                ids = tok.encode(rendered, add_special_tokens=False)  # transformers 5 returns an Encoding when tokenize=True
                with torch.no_grad():
                    gen = model.generate(torch.tensor([ids], device=model.device), max_new_tokens=24, do_sample=False)
                new = gen[0, len(ids):].tolist()
                rows.append({"effort": effort or "default", "item": p["id"], "rendered_prompt_tail": tok.decode(ids[-6:]),
                             "first_tokens": [tok.decode([i]) for i in new[:8]], "text": tok.decode(new)})
        assumed = tok.encode("<|message_model|><|content_text|>", add_special_tokens=False)
        R["opening"] = {"assumed_opening_ids": assumed, "samples": rows,
                        "pilot_prompt_ends_with_assumed_opening": all(it["prompt_ids"][-len(assumed):] == assumed for it in items)}
        save()

    def sweep(mode=None, passes=3, inject_from=None):
        loop.passes(passes)
        out = {}
        for it in items:
            inj = None
            if inject_from is not None:
                inj = inject_from(it)
            logits = loop.run(model, it["prompt_ids"], mode=mode, inject=inj)
            out[it["id"]] = score(logits, it["cand_ids"], it["answer_index"])
        loop.passes(3)
        return out

    base = None
    if "floor" in phases or "identity" in phases or "bypass" in phases:
        t0 = time.time()
        base = sweep()
        R["timing_seconds_per_sweep"] = round(time.time() - t0, 1)
    if "floor" in phases:
        again = sweep()
        diffs = [maxdiff(base[k], again[k]) for k in base]
        R["floor"] = {"max_abs_logprob_diff": max(diffs), "items": len(diffs),
                      "tolerance": max(0.01, 3 * max(diffs))}
        save()
    tol = R.get("floor", {}).get("tolerance", 0.01)
    if "identity" in phases:
        diffs = []
        for it in items:
            loop.run(model, it["prompt_ids"], mode="record")
            own = {k: v for k, v in loop.store.items()}
            s = score(loop.run(model, it["prompt_ids"], mode="replace", inject=own), it["cand_ids"], it["answer_index"])
            diffs.append(maxdiff(s, base[it["id"]]))
        R["identity"] = {"max_abs_logprob_diff": max(diffs), "tolerance": tol, "pass": max(diffs) <= tol,
                         "passes_recorded": sorted(loop.store)}
        save()
    if "bypass" in phases:
        one = sweep(passes=1)
        byp = sweep(mode="bypass", passes=3)
        diffs = [maxdiff(byp[k], one[k]) for k in one]
        R["bypass"] = {"max_abs_logprob_diff": max(diffs), "tolerance": tol, "pass": max(diffs) <= tol}
        save()
    if "baseline" in phases:
        acc = {}
        for n in (1, 2, 3):
            res = base if (n == 3 and base is not None) else sweep(passes=n)
            by = {}
            for it in items:
                k = it["kind"].split(":")[-1] if it["kind"].startswith("chain") else it["kind"]
                by.setdefault(k, []).append(res[it["id"]]["right"])
            acc[n] = {k: round(sum(v) / len(v), 3) for k, v in sorted(by.items())}
        R["baseline_accuracy_descriptive"] = acc
        R["baseline_note"] = "Descriptive only, on pilot items: no outcome is read, and no threshold is set from these numbers."
        save()
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    R["peak_gpu_memory_gb"] = round(torch.cuda.max_memory_allocated() / 2**30, 2)
    save()
    print(json.dumps({k: R.get(k) for k in ("load", "floor", "identity", "bypass", "peak_gpu_memory_gb")}, indent=1))


if __name__ == "__main__":
    main()
