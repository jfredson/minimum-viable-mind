"""Step 4b of the loop removal test, the collection (rerun under specification section 19): runs on a rented GPU machine. See step4b-runbook.md.

    python -I step4b_collect.py --pilot batteries/pilot-v0.12 --out out [--limit 10]

Writes into --out:
  collect-summary.json   the checks, the averages' sizes, the neutral damages, the factors, the bounds
  items.jsonl            one record per scored pair item and bites item, every condition
Nothing here reads an outcome. The analysis is step4b_analyse.py, on the Mac.
"""
import argparse
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step4a import MODEL_ID, MODEL_REVISION  # noqa: E402

SEED = 1            # the donor and noise seed (the registration fixes the test's)
N_DRAWS = 20        # design, section 4
SEARCH_DRAWS = 5    # draws a passage while searching for a factor (runbook, phase 6)
MATCH = 0.20        # damage within 20%


def load_jsonl(d, name):
    p = os.path.join(d, name)
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


class Hooks:
    """Replaces, perturbs or removes the two block-sum inputs of message_input on passes 2 and 3, and can add
    noise to block 1's output (the output of the last layer before the loop)."""

    def __init__(self, tm):
        import torch
        self.torch = torch
        self.tm = tm
        self.mi = tm.message_input
        self.orig = self.mi.forward
        self.n_loop = tm.config.loop_layer_index_end - tm.config.loop_layer_index_start
        self.pre = tm.layers[tm.config.loop_layer_index_start - 1]
        self.mi.forward = self._mi
        self.pre.register_forward_hook(self._pre)
        self.reset()

    def reset(self):
        self.mode, self.calls, self.data = None, 0, None
        self.outside = None      # [B, L, H] noise for block 1's output, or None
        self.rec = {}            # pass -> (block_states, partial) of batch element 0
        self.rec_pre = None

    def passes(self, n):
        self.tm.config.loop_num_passes = n

    def _pre(self, module, inputs, output):
        h = output[0] if isinstance(output, tuple) else output
        if self.mode == "record":
            self.rec_pre = h[0].detach().clone()
        if self.outside is not None:
            h = (h.float() + self.outside).to(h.dtype)
            return (h,) + tuple(output[1:]) if isinstance(output, tuple) else h
        return None

    def _mi(self, block_states, partial, loop_layer_idx):
        pass_no = 2 + self.calls // self.n_loop
        self.calls += 1
        if self.mode == "bypass":
            return None
        if self.mode == "record" and loop_layer_idx == 0:
            self.rec[pass_no] = (block_states[0].detach().clone(), partial[0].detach().clone())
        elif self.mode == "inject":
            bs, ps = self.data[pass_no]
            block_states, partial = bs.to(block_states.dtype), ps.to(partial.dtype)
        elif self.mode == "noise":
            nb, npart = self.data[pass_no]
            block_states = (block_states.float() + nb).to(block_states.dtype)
            partial = (partial.float() + npart).to(partial.dtype)
        return self.orig(block_states, partial, loop_layer_idx)

    def run(self, model, ids, batch=1, mode=None, data=None, outside=None, full=False):
        torch = self.torch
        self.mode, self.calls, self.data, self.outside = mode, 0, data, outside
        if mode == "record":
            self.rec, self.rec_pre = {}, None
        x = torch.tensor([ids] * batch, device=model.device)
        with torch.no_grad():
            out = model(input_ids=x, use_cache=False)
        self.mode, self.data, self.outside = None, None, None
        return out.logits.float() if full else out.logits[:, -1].float()


def stack(bs, ps):
    """[L, k, H] and [L, H] -> [L, k+1, H] in float, as the reader stacks them."""
    import torch
    return torch.cat([bs.float(), ps.float().unsqueeze(-2)], dim=-2)


def unit_rms(x):
    return x / x.pow(2).mean(-1, keepdim=True).clamp_min(1e-12).sqrt()


def dist(true_bs, true_ps, giv_bs, giv_ps):
    """Specification, section 17, item 7: per position and sum, the distance between the true and given sums,
    each scaled to a root-mean-square of 1, divided by the true sum's length (sqrt of the width). [L, k+1]"""
    t, g = stack(true_bs, true_ps), stack(giv_bs, giv_ps)
    H = t.shape[-1]
    return (unit_rms(t) - unit_rms(g)).norm(dim=-1) / math.sqrt(H)


def score(logits_last, cand_ids, ai):
    """Design, section 5, with the tie rule of RT-446: a tie for the top counts as right in the share 1/k."""
    import torch
    lp = torch.log_softmax(logits_last, -1)[..., cand_ids]
    out = []
    for row in lp.reshape(-1, len(cand_ids)):
        r = row.tolist()
        top = max(r)
        tied = [i for i, v in enumerate(r) if v == top]
        right = (1.0 / len(tied)) if ai in tied else 0.0
        best_wrong = max(v for i, v in enumerate(r) if i != ai)
        out.append({"right": right, "margin": round(r[ai] - best_wrong, 5), "lp": [round(v, 5) for v in r]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0, help="quick try: this many pairs and bites items, 20 neutral")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    import torch
    import transformers
    from transformers import AutoTokenizer
    t0 = time.time()
    model = transformers.AutoModelForImageTextToText.from_pretrained(
        MODEL_ID, revision=MODEL_REVISION, device_map="cuda", dtype=torch.bfloat16)
    model.eval()
    tok = AutoTokenizer.from_pretrained(MODEL_ID, revision=MODEL_REVISION)
    tm = [m for m in model.modules() if hasattr(m, "message_input") and hasattr(m, "layers")][0]
    hk = Hooks(tm)
    S = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "transformers": transformers.__version__, "dtype": "bfloat16",
         "load_seconds": round(time.time() - t0, 1), "seed": SEED}

    def cand_ids(cands):
        ids = []
        for c in cands:
            e = tok.encode(c, add_special_tokens=False)
            assert len(e) == 1, c
            ids.append(e[0])
        return ids

    pairs = load_jsonl(a.pilot, "pairs.jsonl")
    donors = load_jsonl(a.pilot, "donor_only.jsonl")
    bites = load_jsonl(a.pilot, "bites.jsonl")
    bdonors = load_jsonl(a.pilot, "bites_donor_only.jsonl")
    neutral = load_jsonl(a.pilot, "neutral.jsonl")
    base = {x["id"]: x for x in load_jsonl(a.pilot, "baseline_ids.jsonl")}
    rep = json.load(open(os.path.join(a.pilot, "build-report.json")))
    from build import eligible, bites_eligible  # noqa: E402
    if a.limit:
        pairs, bites = pairs[:a.limit], bites[:a.limit]
        build_n = [x for x in neutral if x["role"] == "build"][:10]
        meas_n = [x for x in neutral if x["role"] == "measure"][:10]
        neutral = build_n + meas_n
    S["counts"] = {"pairs": len(pairs), "donor_only": len(donors), "bites": len(bites), "bites_donor_only": len(bdonors),
                   "neutral": len(neutral)}

    # template slots: taken from the pilot's own step-3 results (specification, section 12, check 10), and
    # checked here against every item and passage
    s3 = json.load(open(os.path.join(a.pilot, "step3-results.json")))["10_average_defined"]
    PREF, SUF = s3["template_prefix_tokens"], s3["template_suffix_tokens_incl_reply_opening"]
    ref = neutral[0]["prompt_ids"]
    for x in [q["P"]["prompt_ids"] for q in pairs + donors + bites + bdonors] + [q["R"]["prompt_ids"] for q in pairs + donors] + \
             [q["prompt_ids"] for q in neutral]:
        assert x[:PREF] == ref[:PREF] and x[-SUF:] == ref[-SUF:], "template slots differ"
    S["template"] = {"prefix_slots": PREF, "suffix_slots_incl_reply_opening": SUF}

    # ---------- 2. floor, identity, bypass on the first 20 scored items
    probe = [(p["id"] + ":P", p["P"]) for p in pairs[:10]] + [(p["id"] + ":R", p["R"]) for p in pairs[:10]]
    floor = identity = bypass = 0.0
    for _, it in probe:
        x1 = hk.run(model, it["prompt_ids"], mode="record")
        rec = dict(hk.rec)
        x2 = hk.run(model, it["prompt_ids"])
        floor = max(floor, (torch.log_softmax(x1, -1) - torch.log_softmax(x2, -1)).abs().max().item())
        xi = hk.run(model, it["prompt_ids"], mode="inject", data={k: (v[0].unsqueeze(0), v[1].unsqueeze(0)) for k, v in rec.items()})
        identity = max(identity, (torch.log_softmax(x1, -1) - torch.log_softmax(xi, -1)).abs().max().item())
        xb = hk.run(model, it["prompt_ids"], mode="bypass")
        hk.passes(1)
        x0 = hk.run(model, it["prompt_ids"])
        hk.passes(3)
        bypass = max(bypass, (torch.log_softmax(xb, -1) - torch.log_softmax(x0, -1)).abs().max().item())
    tol = max(0.01, 3 * floor)
    S["checks"] = {"noise_floor": floor, "tolerance": tol, "identity": identity, "identity_pass": identity <= tol,
                   "bypass": bypass, "bypass_pass": bypass <= tol, "items": len(probe)}
    print("checks", json.dumps(S["checks"]), flush=True)
    if not (S["checks"]["identity_pass"] and S["checks"]["bypass_pass"]):
        json.dump(S, open(os.path.join(a.out, "collect-summary.json"), "w"), indent=1)
        sys.exit("identity or bypass check failed: the design returns to John")

    # ---------- 3. unaltered runs, recorded (items; neutral passages in both renderings)
    R = {}       # key -> {"rec": {2: (bs, ps), 3: ...}, "pre": h, "ids": [...]}
    def record(key, ids):
        hk.run(model, ids, mode="record")
        R[key] = {"rec": dict(hk.rec), "pre": hk.rec_pre, "ids": ids}
    for p in pairs + donors:
        record(p["id"] + ":P", p["P"]["prompt_ids"])
        record(p["id"] + ":R", p["R"]["prompt_ids"])
    for b in bites + bdonors:
        record(b["id"] + ":P", b["P"]["prompt_ids"])
    for n in neutral:
        record(n["id"], n["prompt_ids"])                     # user turn: builds the average
        record(n["id"] + ":reply", n["reply_ids"])           # reply: damage and perplexity (section 19, item 3)
    S["recorded"] = len(R)
    k1 = next(iter(R.values()))["rec"][2][0].shape
    S["block_states_shape_per_item"] = list(k1)
    OPEN = neutral[0]["prose_span"][0]
    CLOSE = len(neutral[0]["reply_ids"]) - neutral[0]["prose_span"][1]
    for n in neutral:
        assert n["reply_ids"][:OPEN] == neutral[0]["reply_ids"][:OPEN] and len(n["reply_ids"]) - n["prose_span"][1] == CLOSE
    S["reply_template"] = {"opening_slots": OPEN, "closing_slots": CLOSE}
    print("recorded", len(R), "block_states", list(k1), flush=True)

    # ---------- 4. the averages (section 19, item 5): user-built (used) and reply-built (measured only)
    build = [n for n in neutral if n["role"] == "build"]
    measure = [n for n in neutral if n["role"] == "measure"]

    def build_avg(key_of, span_of):
        A = {}
        for ps in (2, 3):
            texts_b, texts_p, pre_b, pre_p, suf_b, suf_p = [], [], [], [], [], []
            bins_b = [[] for _ in range(10)]
            bins_p = [[] for _ in range(10)]
            for n in build:
                bs, pp = R[key_of(n)]["rec"][ps]
                s, e = span_of(n)
                pre_b.append(bs[:s].float()); pre_p.append(pp[:s].float())
                suf_b.append(bs[e:].float()); suf_p.append(pp[e:].float())
                texts_b.append(bs[s:e].float()); texts_p.append(pp[s:e].float())
                for j, pos in enumerate(range(s, e)):
                    bins_b[10 * j // (e - s)].append(bs[pos].float()); bins_p[10 * j // (e - s)].append(pp[pos].float())
            A[ps] = {"pre": (torch.stack(pre_b).mean(0), torch.stack(pre_p).mean(0)),
                     "suf": (torch.stack(suf_b).mean(0), torch.stack(suf_p).mean(0)),
                     "text": (torch.cat(texts_b).mean(0), torch.cat(texts_p).mean(0)),
                     "bins": [(torch.stack(bins_b[i]).mean(0), torch.stack(bins_p[i]).mean(0)) for i in range(10)]}
        return A
    avg_user = build_avg(lambda n: n["id"], lambda n: (PREF, len(n["prompt_ids"]) - SUF))
    avg_reply = build_avg(lambda n: n["id"] + ":reply", lambda n: tuple(n["prose_span"]))

    def avg_sums(L, ps, span, slots, text, fallback=False):
        """Template slots from `slots`, prose or text positions from `text` (pooled, or binned for the fallback)."""
        s, e = span
        bsl, psl = [], []
        for pos in range(L):
            if pos < s:
                b, p_ = slots[ps]["pre"][0][pos], slots[ps]["pre"][1][pos]
            elif pos >= e:
                b, p_ = slots[ps]["suf"][0][pos - e], slots[ps]["suf"][1][pos - e]
            elif fallback:
                b, p_ = text[ps]["bins"][10 * (pos - s) // (e - s)]
            else:
                b, p_ = text[ps]["text"]
            bsl.append(b); psl.append(p_)
        return torch.stack(bsl), torch.stack(psl)

    # ---------- per-item replacement plans
    def swap_plan(key, donor_keys):
        """For each donor: the injected sums (truncated to L), the per-position distances on passes 2 and 3,
        the first divergence position, the change ratio and the swap size."""
        rec, ids = R[key]["rec"], R[key]["ids"]
        L = len(ids)
        plans = []
        for dk in donor_keys:
            drec, dids = R[dk]["rec"], R[dk]["ids"]
            div = next((i for i in range(min(L, len(dids))) if ids[i] != dids[i]), min(L, len(dids)))
            inj, dd = {}, {}
            for ps in (2, 3):
                gb, gp = drec[ps][0][:L], drec[ps][1][:L]
                inj[ps] = (gb, gp)
                dd[ps] = dist(rec[ps][0], rec[ps][1], gb, gp)
                dd[ps][:div] = 0.0  # identical prefixes give identical sums; rounding is zeroed
            used = torch.stack([dd[2][div:], dd[3][div:]])
            plans.append({"inject": inj, "dist": dd, "div": div,
                          "ratio": used.mean().item() if used.numel() else 0.0,
                          "ratio_by_sum": used.mean(dim=(0, 1)).tolist() if used.numel() else [],
                          "size": used.sum().item()})
        return plans

    def avg_plan(key, span, slots, text, fallback=False):
        rec, ids = R[key]["rec"], R[key]["ids"]
        L = len(ids)
        inj, dd = {}, {}
        for ps in (2, 3):
            gb, gp = avg_sums(L, ps, span, slots, text, fallback)
            inj[ps] = (gb, gp)
            dd[ps] = dist(rec[ps][0], rec[ps][1], gb, gp)
        sp_ = list(range(span[0], span[1]))
        ratio_pos = sp_ + [L - 1]                       # specification, section 17, item 7
        used = torch.stack([dd[2][ratio_pos], dd[3][ratio_pos]])
        size = torch.stack([dd[2][sp_], dd[3][sp_]]).sum().item()  # design, section 5: the text span
        noise_d = {ps: torch.zeros_like(dd[ps]) for ps in (2, 3)}
        for ps in (2, 3):
            noise_d[ps][sp_] = dd[ps][sp_]              # the comparison acts where the size is counted
        return {"inject": inj, "dist": noise_d, "ratio": used.mean().item(),
                "ratio_by_sum": used.mean(dim=(0, 1)).tolist(), "size": size}

    def item_avg_plan(key, fallback=False):
        L = len(R[key]["ids"])
        return avg_plan(key, (PREF, L - SUF), avg_user, avg_user, fallback)

    def noise_loop(key, dmap, factor, draws, gen):
        """Design, section 4: at each position and sum, a random direction whose length is the position's
        distance x factor x the true sum's raw length. Returns {pass: (nb [B,L,k,H], np [B,L,H])}."""
        rec = R[key]["rec"]
        out = {}
        for ps in (2, 3):
            t = stack(*rec[ps])                                    # [L, k+1, H]
            g = torch.randn((draws,) + tuple(t.shape), device=t.device, generator=gen)
            g = g / g.norm(dim=-1, keepdim=True)
            lens = t.norm(dim=-1)                                  # [L, k+1]
            n = g * (dmap[ps] * factor * lens).unsqueeze(0).unsqueeze(-1)
            out[ps] = (n[:, :, :-1, :], n[:, :, -1, :])
        return out

    def noise_outside(key, dmap, factor, draws, gen):
        """Design, section 4: block 1's output, one tensor; at each position the total distance over passes and
        sums, x factor x the output's raw length at that position."""
        h = R[key]["pre"].float()                                  # [L, H]
        tot = (dmap[2].sum(-1) + dmap[3].sum(-1))                  # [L]
        g = torch.randn((draws,) + tuple(h.shape), device=h.device, generator=gen)
        g = g / g.norm(dim=-1, keepdim=True)
        return g * (tot * factor * h.norm(dim=-1)).unsqueeze(0).unsqueeze(-1)

    # ---------- 5. neutral, in the reply rendering (section 19, item 3): predictions of the prose tokens
    def prose_stats(logits_full, ids, span):
        s, e = span
        lp = torch.log_softmax(logits_full[:, s - 1:e - 1], -1)
        tgt = torch.tensor(ids[s:e], device=lp.device)
        nll = -lp.gather(-1, tgt.view(1, -1, 1).expand(lp.shape[0], -1, 1)).squeeze(-1)   # [B, T]
        return lp, nll

    # the 1-nat check (design version 0.14, section 4): reply rendering, user turn and plain text
    nll_r = nll_u = nll_p = 0.0
    tok_r = tok_u = tok_p = 0
    base_lp, base_nll = {}, {}
    for n in measure:
        span = tuple(n["prose_span"])
        lp, nll = prose_stats(hk.run(model, n["reply_ids"], full=True), n["reply_ids"], span)
        base_lp[n["id"]], base_nll[n["id"]] = lp[0], nll[0]
        nll_r += nll.sum().item(); tok_r += nll.shape[1]
        _, nu = prose_stats(hk.run(model, n["prompt_ids"], full=True), n["prompt_ids"], (PREF, len(n["prompt_ids"]) - SUF))
        nll_u += nu.sum().item(); tok_u += nu.shape[1]
        _, npl = prose_stats(hk.run(model, n["plain_ids"], full=True), n["plain_ids"], (1, len(n["plain_ids"])))
        nll_p += npl.sum().item(); tok_p += npl.shape[1]
    S["one_nat_check"] = {"reply_nll_per_token": nll_r / tok_r, "user_turn_nll_per_token": nll_u / tok_u,
                          "plain_nll_per_token": nll_p / tok_p,
                          "reply_minus_plain": nll_r / tok_r - nll_p / tok_p,
                          "passes": nll_r / tok_r - nll_p / tok_p <= 1.0}
    print("one-nat check", json.dumps(S["one_nat_check"]), flush=True)

    def damage_and_nll(n, lp_alt, nll_alt):
        b = base_lp[n["id"]].exp()
        kl = (b * (base_lp[n["id"]] - lp_alt)).sum(-1).mean(-1)              # [B]
        return kl, nll_alt.sum(-1)                                            # per draw: mean KL, summed NLL

    ntok = tok_r
    base_ppl = math.exp(nll_r / tok_r)
    nplan = {}
    main = {}
    for n in measure:
        rk = n["id"] + ":reply"
        L = len(n["reply_ids"])
        span = tuple(n["prose_span"])
        cands = [m["id"] + ":reply" for m in neutral if m["id"] != n["id"] and len(m["reply_ids"]) >= L]
        dks = random.Random(f"{SEED}-{n['id']}").sample(cands, min(5, len(cands)))
        sp = swap_plan(rk, dks) if dks else []
        ap_ = avg_plan(rk, span, avg_reply, avg_user)                     # used: user-built prose average
        fp = avg_plan(rk, span, avg_reply, avg_user, fallback=True)
        rp = avg_plan(rk, span, avg_reply, avg_reply)                     # reply-built, measured only
        nplan[n["id"]] = {"swap": sp, "avg": ap_, "fallback": fp, "avg_reply_built": rp}
        for meth, plans in (("swap", sp), ("avg", [ap_]), ("fallback", [fp]), ("avg_reply_built", [rp])):
            if not plans:
                continue
            data = {ps: (torch.stack([q["inject"][ps][0] for q in plans]), torch.stack([q["inject"][ps][1] for q in plans]))
                    for ps in (2, 3)}
            lp, nll = prose_stats(hk.run(model, n["reply_ids"], batch=len(plans), mode="inject", data=data, full=True),
                                  n["reply_ids"], span)
            kl, snll = damage_and_nll(n, lp, nll)
            m_ = main.setdefault(meth, {"kl": [], "nll": 0.0, "tok": 0, "passages": 0})
            m_["kl"].append(kl.mean().item()); m_["nll"] += snll.mean().item(); m_["tok"] += nll.shape[1]; m_["passages"] += 1
    S["neutral_main"] = {}
    for meth, m_ in main.items():
        S["neutral_main"][meth] = {"damage": sum(m_["kl"]) / len(m_["kl"]), "passages": m_["passages"],
                                   "ppl_rise": math.exp(m_["nll"] / m_["tok"]) - base_ppl}
    S["neutral_base_ppl"] = base_ppl
    S["neutral_swap_passages_without_donor"] = sum(1 for n in measure if not nplan[n["id"]]["swap"])
    print("neutral main", json.dumps(S["neutral_main"]), flush=True)

    def mean_dist(plans):
        return {ps: torch.stack([q["dist"][ps] for q in plans]).mean(0) for ps in (2, 3)}

    def comparison_on_neutral(kind, meth, factor, draws, seed):
        """Mean damage over passages and draws, and the perplexity rise of each draw, on the reply rendering."""
        gen = torch.Generator(device="cuda").manual_seed(seed)
        kls, nll_draw, ntok_c = [], torch.zeros(draws, device="cuda"), 0
        for n in measure:
            rk = n["id"] + ":reply"
            plans = nplan[n["id"]]["swap"] if meth == "swap" else [nplan[n["id"]]["avg"]]
            if not plans:
                continue
            dmap = mean_dist(plans)
            if kind == "loop":
                out = hk.run(model, n["reply_ids"], batch=draws, mode="noise",
                             data=noise_loop(rk, dmap, factor, draws, gen), full=True)
            else:
                out = hk.run(model, n["reply_ids"], batch=draws, outside=noise_outside(rk, dmap, factor, draws, gen),
                             full=True)
            lp, nll = prose_stats(out, n["reply_ids"], tuple(n["prose_span"]))
            kl, snll = damage_and_nll(n, lp, nll)
            kls.append(kl.mean().item()); nll_draw += snll; ntok_c += nll.shape[1]
        rises = [math.exp(x / ntok_c) - base_ppl for x in nll_draw.tolist()]
        return sum(kls) / len(kls), rises

    # ---------- 6. damage matching (section 19, item 4): bracketing search over 0.001 to 100,000
    S["factors"] = {}
    steps = 8 if a.limit else 18
    for kind in ("loop", "outside"):
        for meth in ("swap", "avg"):
            target = S["neutral_main"][meth]["damage"]
            lo, hi, best, path = 1e-3, 1e5, None, []
            for i in range(steps):
                mid = math.sqrt(lo * hi)
                d, _ = comparison_on_neutral(kind, meth, mid, SEARCH_DRAWS, 1000 + i)
                path.append([mid, d])
                if best is None or abs(d - target) < abs(best[1] - target):
                    best = (mid, d)
                if d < target:
                    lo = mid
                else:
                    hi = mid
            bracketed = any(d < target for _, d in path) and any(d >= target for _, d in path)
            d20, rises = comparison_on_neutral(kind, meth, best[0], N_DRAWS, 2000)
            within = abs(d20 - target) <= MATCH * target
            S["factors"][f"{kind}_{meth}"] = {"factor": best[0], "target_damage": target, "damage_20_draws": d20,
                                              "bracketed": bracketed, "within_20pct": within,
                                              "matched": bracketed and within, "search_path": path,
                                              "ppl_rise_draws": rises}
            print("factor", kind, meth, json.dumps({k: v for k, v in S["factors"][f"{kind}_{meth}"].items()
                                                    if k not in ("ppl_rise_draws", "search_path")}), flush=True)

    # ---------- 7. the normal-range bound (same size: in-loop noise at factor 1), on the reply rendering
    S["normal_range"] = {}
    for meth in ("swap", "avg"):
        _, rises = comparison_on_neutral("loop", meth, 1.0, N_DRAWS, 3000)
        srt = sorted(rises)
        bound = srt[min(len(srt) - 1, int(math.ceil(0.95 * len(srt))) - 1)]
        S["normal_range"][meth] = {"bound": bound, "rises": rises, "main_rise": S["neutral_main"][meth]["ppl_rise"]}
    json.dump(S, open(os.path.join(a.out, "collect-summary.json"), "w"), indent=1)

    # ---------- 8 and 9. every scored pair item and bites item
    pool = pairs + donors
    bpool = bites + bdonors
    gen = torch.Generator(device="cuda").manual_seed(4000)
    fout = open(os.path.join(a.out, "items.jsonl"), "w")

    def run_item(key, it, donor_keys, kind_name, extra_ids=None):
        cids = cand_ids(it["candidates"])
        ai = it["candidates"].index(it["answer"])
        rec = {"key": key, "kind": kind_name, "n_donors": len(donor_keys)}
        rec["unaltered"] = score(hk.run(model, it["prompt_ids"]), cids, ai)[0]
        rec["unaltered_2"] = score(hk.run(model, it["prompt_ids"]), cids, ai)[0]
        for n in (1, 2):
            hk.passes(n)
            rec[f"passes_{n}"] = score(hk.run(model, it["prompt_ids"]), cids, ai)[0]
            hk.passes(3)
        sp = swap_plan(key, donor_keys) if donor_keys else []
        apl, fpl = item_avg_plan(key), item_avg_plan(key, fallback=True)
        if sp:
            data = {ps: (torch.stack([q["inject"][ps][0] for q in sp]), torch.stack([q["inject"][ps][1] for q in sp]))
                    for ps in (2, 3)}
            rec["swap"] = score(hk.run(model, it["prompt_ids"], batch=len(sp), mode="inject", data=data), cids, ai)
            rec["swap_ratio"] = [q["ratio"] for q in sp]
            rec["swap_ratio_by_sum"] = [q["ratio_by_sum"] for q in sp]
            rec["swap_size"] = [q["size"] for q in sp]
            rec["swap_div"] = [q["div"] for q in sp]
        for nm, pl in (("avg", apl), ("fallback", fpl)):
            data = {ps: (pl["inject"][ps][0].unsqueeze(0), pl["inject"][ps][1].unsqueeze(0)) for ps in (2, 3)}
            rec[nm] = score(hk.run(model, it["prompt_ids"], mode="inject", data=data), cids, ai)[0]
            rec[nm + "_ratio"], rec[nm + "_ratio_by_sum"], rec[nm + "_size"] = pl["ratio"], pl["ratio_by_sum"], pl["size"]
        kinds = ("loop", "outside") if kind_name == "pair" else ("loop",)
        for kind in kinds:
            for meth in ("swap", "avg"):
                plans = sp if meth == "swap" else [apl]
                if not plans:
                    continue
                f = S["factors"][f"{kind}_{meth}"]["factor"]
                dmap = mean_dist(plans)
                if kind == "loop":
                    out = hk.run(model, it["prompt_ids"], batch=N_DRAWS, mode="noise",
                                 data=noise_loop(key, dmap, f, N_DRAWS, gen))
                else:
                    out = hk.run(model, it["prompt_ids"], batch=N_DRAWS, outside=noise_outside(key, dmap, f, N_DRAWS, gen))
                rec[f"{kind}_{meth}"] = [{"right": s["right"], "margin": s["margin"]} for s in score(out, cids, ai)]
        for nm, ids in (extra_ids or {}).items():
            rec[nm] = score(hk.run(model, ids), cids, ai)[0]
        fout.write(json.dumps(rec) + "\n")
        fout.flush()

    for i, p in enumerate(pairs):
        el = [d for d in pool if eligible(d, p)]
        chosen = random.Random(f"{SEED}-{p['id']}").sample(el, min(5, len(el)))
        b_ = base.get(p["id"], {})
        run_item(p["id"] + ":P", p["P"], [d["id"] + ":P" for d in chosen], "pair",
                 {"without_rule": b_.get("P_without_rule"), "baseline": b_.get("P_baseline")} if b_ else None)
        run_item(p["id"] + ":R", p["R"], [d["id"] + ":R" for d in chosen], "pair",
                 {"baseline": b_.get("R_baseline")} if b_ else None)
        if i % 10 == 0:
            print("pairs", i, round(time.time() - t0), flush=True)
    for i, b in enumerate(bites):
        el = [d for d in bpool if bites_eligible(d, b)]
        chosen = random.Random(f"{SEED}-{b['id']}").sample(el, min(5, len(el)))
        run_item(b["id"] + ":P", b["P"], [d["id"] + ":P" for d in chosen], "bites")
    fout.close()
    S["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    S["seconds"] = round(time.time() - t0)
    S["peak_gpu_memory_gb"] = round(torch.cuda.max_memory_allocated() / 1e9, 2)
    json.dump(S, open(os.path.join(a.out, "collect-summary.json"), "w"), indent=1)
    print("done", S["seconds"], "s, peak", S["peak_gpu_memory_gb"], "GB", flush=True)


if __name__ == "__main__":
    main()
