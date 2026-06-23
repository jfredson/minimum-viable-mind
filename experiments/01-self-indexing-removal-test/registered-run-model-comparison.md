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
5. **Fits the 48GB M4 Pro mini** for the registered run: 7–13B in bf16 is
   comfortable (~16–26GB); 32B needs 4-bit quant (degrades activation fidelity for
   interp) — avoid. 7–13B is the sweet spot.

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
