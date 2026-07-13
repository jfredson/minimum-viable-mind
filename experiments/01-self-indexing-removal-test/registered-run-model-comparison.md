# Registered-run model comparison (substrate pin)

*Supports the substrate decision in `red_team_ledger.md` (Pass 2) and
`pre-registration.md` (Materials): `gemma-2-2b-it` stays the pilot/instrument
sandbox; the registered run moves to a less-RLHF'd model. This note pins the
specific model against the constraints. Facts verified June 2026; exact HF repo
IDs and revisions to be confirmed and pinned in `config.py` before any download.*

## Constraints (from the substrate decision)

1. **Lightly-aligned instruction model, not a base model.** The C_self-index /
   `turn_role` localization and the S battery need chat-turn structure and
   self-report — a pure pretrained base has no assistant turn. So the primary
   registered model must be SFT-only / DPO-light (instruction-following but not
   heavily RLHF'd).
2. **Staged checkpoints (base → SFT → DPO → RLHF/RLVR) of the same model** — this
   is what turns RT-06 (RLHF capability-gating) from a possible dead-end into a
   *controlled* measurement: localize and ablate at each alignment stage and watch
   the C_self / capability entanglement grow.
3. **Open weights + full activation access** (ablation, not just prompting).
4. **SAE availability for localization method (b)** — or accept training SAEs /
   leaning on causal patching (already validated) as the second method.
5. **Runs in bf16 on the available hardware** (see "Hardware / memory" below):
   8B in bf16 needs ~22–23GB peak for the full interp pipeline; 32B needs 4-bit
   quant (degrades activation fidelity for interp) — avoid. 7–13B is the sweet spot.

## Hardware / memory (the registered run is interp, not plain inference)

The registered run holds the **model + cached activations + an SAE + a KV cache
for generation** at once, so it needs more than weight size alone. For bf16
Llama-3.1-8B:

| Component | bf16 |
|---|---|
| 8B weights | ~16.1 GB |
| macOS + Python + libs | ~4–6 GB |
| One Llama Scope SAE (32k, per-layer) | ~0.5–1 GB |
| Activations (short battery prompts, small batches) | a few hundred MB |
| KV cache (generation, ~2k ctx) | ~0.3–0.5 GB |
| **Peak** | **~22–23 GB** |

Mac-specific gotcha: macOS caps GPU-usable unified memory (Metal "wired" limit) at
~65–75% of total by default, so a 24GB machine exposes only ~16GB to the GPU —
about the weight size alone.

The binding constraint is **usable-GPU memory, not GPU core count** — an interp
run is memory-bound (cache activations across all layers + SAE + KV cache) before
it is compute-bound. Memory bandwidth helps throughput once you fit; it does not
let you fit. So read the table memory-first.

macOS-usable GPU memory ≈ 65–75% of total. M4-generation bandwidth: base ~120 GB/s,
M4 Pro ~273 GB/s, M4 Max ~410 GB/s (14-core/32-core GPU) / ~546 GB/s
(16-core/40-core GPU).

**Pricing updated 2026-06-26 (military-discount quotes John was given).** The
earlier configs/prices (24/32/48GB mini at ~$799/$999/$1,599) are superseded.

| Config | Price | ~GPU-usable | bf16 8B interp run | Verdict |
|---|---|---|---|---|
| **M4 mini**, 24GB (10c/10c) | $899 | ~17 GB | ❌ over the Metal wired limit on weights alone; fits only via **4-bit quant**, which alters the activations being measured/ablated | Reject — memory is binding; the low price doesn't fix it |
| **M4 Pro mini**, 48GB (12c/16c GPU) | $1,979 | ~33 GB | ✅ comfortable; room for 13B, multiple SAEs, larger batches | **Recommended** — best capability-per-dollar |
| **M4 Max Studio**, 36GB (14c/32c GPU) | $2,249 | ~25 GB | ✅ fits, but only ~2–3 GB slack | **Avoid — the trap.** Costs *more* than the 48GB mini for *less* usable memory; the Max's ~1.5× bandwidth doesn't compensate for thin interp headroom |
| **M4 Max Studio**, 64GB (16c/40c GPU) | $3,149 | ~45 GB | ✅ luxurious | **Splurge pick** — only config that buys both ~2× throughput *and* comfortable headroom |

**Recommendation:** the **48GB M4 Pro mini ($1,979)** remains the pick — it is the
cheapest config that clears the memory bar with real headroom. Avoid the 24GB
(forces 4-bit) and especially the **36GB Studio** (more money than the 48GB mini
for less usable memory — the Max chip is wasted when you're memory-bound). The only
reason to leave the mini is the **64GB M4 Max Studio ($3,149)**: it adds the Max's
~2× bandwidth + GPU cores (which compounds across the 5-checkpoint RT-06 ladder)
*and* ~45 GB usable (room to hold two checkpoints at once, or move to 13B+). That is
a +$1,170 bet on going deeper into local interp work, not a need for *this* run —
Stages 0–1 run on the existing Air sandbox, and the mini only becomes the bottleneck
at step 5.

**Decision (2026-06-26): 48GB M4 Pro mini ($1,979), confirmed at the updated
pricing.** Rationale: clears the memory bar with real headroom, matches the
project's "minimum viable / don't over-provision" ethos, and the ~$1,170 saved
versus the 64GB Studio is preserved for possible robotics-specific hardware if that
avenue is pursued later. The 64GB Studio stays the documented upgrade path if local
interp work scales past 8B or needs a high-frequency iteration loop; the 36GB Studio
is rejected (less usable memory than the mini at a higher price).

## Candidates

| Model | Lightly-aligned instr.? | Staged checkpoints (RT-06) | Off-the-shelf SAEs (method b) | Open | Fits mini | Verdict |
|---|---|---|---|---|---|---|
| **Llama-3.1-8B + Tülu-3-8B** | ✅ Tülu-3-8B-**SFT** (SFT-only) | ✅ base → SFT → DPO → RLVR (AI2) **+** Meta's own RLHF'd Instruct as a 2nd trajectory | ✅ **Llama Scope** (256 SAEs, all layers, 32k/128k) + Goodfire; trained on the **base** | weights open (Llama license; data not fully open) | ✅ 8B | **Recommended** |
| **OLMo-2-7B / OLMo-3-7B** | ✅ Instruct-SFT released separately | ✅ base → SFT → DPO → Instruct, fully documented | ❌ none found — train SAEs or use causal patching | ✅ **fully open** (data, code, intermediate ckpts) | ✅ 7B | Strong fallback (purist) |
| **gemma-2-9b-it + GemmaScope** | ❌ RLHF'd only; no SFT-only variant | ❌ no staged ladder | ✅ GemmaScope | weights open | ✅ 9B | Dominated — doesn't address RT-06 |
| Qwen2.5-7B-Instruct | partial (base+instruct) | ❌ no public intermediate stages | partial/none mainstream | weights open | ✅ 7B | No staged ladder |

## The trade-off, and why Llama-3.1-8B wins

The real fork is **staged checkpoints (RT-06)** vs **off-the-shelf SAEs (method b)** —
and Llama-3.1-8B is the rare option that has *both*:

- **RT-06 controlled comparison.** AI2's Tülu-3 pipeline publishes
  `…-8B-SFT`, `…-8B-DPO`, and the final RLVR model, all from Llama-3.1-8B-base. So
  the same base can be localized/ablated at four alignment levels (base → SFT →
  DPO → RLVR), *plus* Meta's independently-RLHF'd Instruct as a second trajectory.
  That measures the capability-gating effect directly instead of arguing about it.
- **Method (b) transfers under our existing assumptions.** Llama Scope SAEs are
  trained on Llama-3.1-8B-**base** — exactly the pattern we already rely on
  (`gemma-scope-2b-pt` SAEs applied to `gemma-2-2b-it`: pretrained SAEs on an
  instruct model). So adopting Llama Scope adds no new methodological assumption
  beyond the one Stage-1 already makes. The SAE-trained-on-base / model-is-instruct
  gap is the *same* gap we accept today.
- **Primary registered model = Tülu-3-8B-SFT** (the SFT-only, least-RLHF'd
  instruction checkpoint that still has chat structure) — the literal "less-RLHF'd
  instruction model" the substrate decision asks for.

**OLMo-2/3-7B is the purist fallback:** maximally open (data + code + intermediate
checkpoints) and the cleanest staged ladder, at the cost of having to *train* SAEs
(or run method (b) as causal patching only, which we've already validated). Pick
OLMo if full data-provenance openness outweighs off-the-shelf SAEs; pick Llama if
keeping method (b) cheap matters more.

**gemma-2-9b-it is dominated** for the registered run: staying in-family keeps
GemmaScope + tooling but it is RLHF'd-only with no SFT/DPO ladder, so it cannot
address RT-06 — which was the whole reason to move substrate.

## Recommendation

**Register Llama-3.1-8B as the substrate**, with:
- **Primary model:** `Llama-3.1-Tulu-3-8B-SFT` (less-RLHF'd instruction model).
- **RT-06 ladder:** base → Tülu-3-SFT → Tülu-3-DPO → Tülu-3 (RLVR) [+ Meta Instruct].
- **Method (b):** Llama Scope SAEs (base-trained), same pt→it assumption as now.
- **Fallback:** OLMo-3-7B if we prefer full openness and accept training SAEs.

Pilot/instrument development continues on `gemma-2-2b-it`. Before download, confirm
exact HF repo IDs + revisions and pin them in `config.py` (the codebase already
treats the model id as a one-line, single-source-of-truth change).

## Sources
- [OLMo 2 — Ai2](https://allenai.org/blog/olmo2) · [OLMo 2 collection (HF)](https://huggingface.co/collections/allenai/olmo-2) · [Olmo-3-7B-Instruct-SFT (HF)](https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT)
- [Tülu 3 — Ai2](https://allenai.org/blog/tulu-3-technical) · [Tülu 3 paper](https://arxiv.org/abs/2411.15124) · [open-instruct (GitHub)](https://github.com/allenai/open-instruct)
- [Llama Scope paper](https://arxiv.org/abs/2410.20526) · [Llama-Scope SAEs (HF: fnlp)](https://huggingface.co/fnlp/Llama-Scope) · [Goodfire open-source SAEs](https://www.goodfire.ai/blog/sae-open-source-announcement)

## Addendum 2026-07-13 — Llama Scope loader verified; substrate weights staged

Verified on a cloud GPU (RunPod, RTX-class, CUDA bf16):

- `sae_lens` 6.45.3 ships all 7 `llama_scope` release families in its pretrained
  registry, including the primary pinned here: `llama_scope_lxr_8x` (residual
  stream, 8x expansion, 32 layers).
- `SAE.from_pretrained("llama_scope_lxr_8x", "l15r_8x")` loads cleanly:
  d_in 4096 (= Llama d_model), d_sae 32768.
- Encoding real `allenai/Llama-3.1-Tulu-3-8B-SFT` resid_post (layer 15, last
  token, hidden_states[L+1] convention — same as the 2B sandbox) yields sparse
  codes: L0 = [19, 24] of 32768 on the two standard probe prompts.
- Method (b) therefore transfers to the registered substrate with **no custom
  loader and no new assumptions** (sae_lens ≥ 6 moved the registry import to
  `sae_lens.loading.pretrained_saes_directory`).

Weights staged for the migration: Tulu-3-8B-SFT downloaded alongside
Llama-3.1-8B base + Meta Instruct. DPO/RLVR ladder checkpoints (RT-06) not yet
staged. Compute note: the registered-run hardware gate ("on the mini") can now
also be satisfied by the cloud bench (same pipeline verified end-to-end on
CUDA); decision on which substrate hosts the registered run itself remains open.
