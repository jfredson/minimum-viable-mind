# The loop removal test, step 4a: findings

*Written 2026-11-21 by the session that wrote the design, the generator and the step-4a script, and that ran
it. Step 4a of section 9 of the design (`docs/loop-removal-test-design-2026-11-20.md`, version 0.8). The raw
results are in `step4a-run-2026-11-21/`: `step4a-results.json` (the full run on 280 items),
`step4a-results-quick-10-items.json` (the last quick try) and `run-log.txt`. These findings are owed a
check by a session that did not write them.*

## In short

**The machinery works.** The model loads, the hooks reach the message between passes, and both checks on
the code pass exactly, on all 280 practice items:
- the noise floor is zero;
- an item given its own message reproduces the normal run, with a largest difference of 0.0;
- skipping the message on passes 2 and 3 reproduces the one-pass run, with a largest difference of 0.0.

**But the test cannot go on to step 4b as designed. Two findings return it to John:**

1. **The model's native 4-bit format could not be used.** The model ran with its weights unpacked to
   16-bit, which is not the precision it was trained in.
2. **The answers are near chance with the scoring the design chose.** Answers are scored as the first token
   of the reply, forced straight out with no written reasoning. Scored that way, the model is right on
   only about 13% to 27% of simple sums, and near chance on the chained lookups at the full three passes.
   So the bites check cannot be met, and most items would fail the confidence filter. The likeliest cause
   is the scoring method, not the loop: left to itself, the model always starts its reply by writing
   reasoning, even when the reasoning setting is "none".

## The run and its cost

| | |
|---|---|
| John's go | "Go, up to $8" for an RTX 5090. No 5090 was free in either cloud, and nothing was created. John then chose "Full PRO 6000, $15" |
| Machine | One RTX PRO 6000 Blackwell Server Edition (96 GB), RunPod secure cloud, $2.69 an hour, pod `owz9imevb2axdq` |
| Created, deleted | 21:27:01 UTC and 22:47:40 UTC, 2026-11-21, so 1 hour 20 minutes. Deleted by hand once the run was done. RunPod's own terminate-after was set for 02:57 UTC, and a laptop timer for the same time was stopped after the deletion |
| Cost | **$3.61**, from the balance: $59.04 before (`runpodctl me`) and $55.43 after. That matches 1.34 hours × $2.69 |
| Within the ceiling | Yes. The ceiling was $15 |
| Waste, owned | About 30 minutes, roughly $1.35. The author's wait-for-the-script check matched its own command line, so it waited its full 30 minutes after the script had already stopped with an error. It was fixed for the later runs |
| Software | PyTorch 2.9.1 (CUDA 12.8), transformers 5.24.0.dev0 installed from commit 046bdb8 (the commit that added the model), accelerate 1.16.0, tokenizers 0.23.3, in a virtual environment over the image's PyTorch |
| Model | `thinkingmachines/TML-d24-varloop-research` at revision 657b53ba, downloaded to the pod only. It is public, so no token was used |

## What each step found

### 1. Loading: the native 4-bit format could not be used (returns to John)

The checkpoint's configuration declares its quantization as `{"quant_method": "modelopt", "quant_algo": "NVFP4"}`.
Its expert weights are stored in Thinking Machines' own layout: `w13_weight`, `w13_weight_amax`,
`w13_weight_outer_scale_denominator` and `w13_weight_scale`. The last four layers use a different layout.

Transformers at commit 046bdb8 does not recognise "modelopt" ("Unknown quantization type ... we will skip the
quantization"). Its own `nvfp4` option compresses full-size weights as they load. It does not read a
checkpoint that is already compressed. So transformers unpacks the weights:
- **At "auto" precision** they came out at 32-bit, about 90 GB, and the 96 GB card ran out of memory.
- **At 16-bit (bfloat16)** the model loaded in 13 seconds, using 49.2 GB, with a peak of 50.9 GB during the
  checks.

The script was changed on the machine to load at 16-bit, and the change is committed with these findings.

**What this means.**
- **The weights.** They are the stored 4-bit values unpacked, so they should be the same numbers.
- **The arithmetic.** It runs at 16-bit, not as the native 4-bit matrix products, so the model's
  activations differ slightly from how it was trained to run.
- **The coherence check.** The model's generated text reads coherently, as the reply-opening probe shows.
- **What it does not show.** Whether accuracy differs from the native path is not measured.
- **What the design wanted.** The design hoped to run in the native precision (section 2). Running at 16-bit
  is a departure, and John should rule whether to accept it.
- **The alternatives:**
  - wait for transformers to support the format;
  - write a loader for it;
  - run the native path in an inference engine (vLLM or SGLang), where hooking the message is far harder.

### 2. The hooks and the architecture facts: confirmed

The script hooks the text model's `message_input`, which the model's source shows is the one place the
message between passes is built (`step4a-runbook.md`). It was found on the loaded model: 12 looped layers
starting at layer 6, and 3 passes. Recording the message's inputs worked on passes 2 and 3.

The three facts the bypass check rests on were read from the source before renting. The bypass result below
confirms them on the model.

### 3. The noise floor: zero

Two unaltered runs over all 280 items gave identical log-probabilities for every candidate, a largest
difference of 0.0. The tolerance for the code checks is therefore the design's floor of 0.01.

### 4. The identity check: passes exactly

Each item given its own recorded message, on passes 2 and 3, reproduced the unaltered run, with a largest
difference of 0.0 over 280 items. The hook replaces the message without disturbing anything else.

### 5. The bypass check: passes exactly

With the message removed on passes 2 and 3, the three-pass model gave exactly the one-pass model's answers,
with a largest difference of 0.0 over 280 items. This confirms on the model that the message is the only
route between passes, as the source showed and the design assumed (section 3).

### 6. The reply opening: the model always starts by writing reasoning (returns to John)

For three practice items, under the reasoning setting "none" and under the default, the model's own reply
began `<|message_model|><|content_thinking|>` and then wrote reasoning. For example: "We need answer puzzle.
Need parse. User: …". So:
- **The opening token is as assumed.** The pilot's prompts end with `<|message_model|><|content_text|>`, and
  `<|message_model|>` is indeed how the reply opens.
- **But the model never chooses to answer at once.** Placing `<|content_text|>` after it forces an immediate
  answer the model would not give unprompted.
- **"None" does not stop written reasoning.** Despite its name, the setting does not stop it.

The design's choice 2 (no written reasoning) is still met by forcing. But the forced answer is off the
model's own path, which may explain the next finding.

### 7. Descriptive accuracy: near chance in most cells (returns to John)

These are descriptive figures only, on pilot items. No outcome is read, and no threshold is set from them.
The right answer is the candidate with the highest probability at the forced answer position. Chance is 20%.

| Passes | Prompt-rule items | Routine twins | Chained lookups, four to six steps |
|---|---|---|---|
| 1 | 27% | 54% | 29% |
| 2 | 22% | 48% | 13% |
| 3 | 34% | 51% | 17% |

**By kind, at three passes:**
- **Prompt-rule items:** operator 23%, unit 20%, letter code 10%, lookup 83%.
- **Routine twins:** sums 13%, products 27%, capitals 83%, opposites 50%, everyday colours 50%.

**What stands out.**
- **Simple arithmetic is near or below chance.** For example, "The two numbers are 5 and 12. What is the sum
  of the two numbers?" is near or below chance when the answer is forced as the reply's first token.
- **Capitals and lookups do well.**
- **What this pattern suggests.** It points to the scoring method rather than the model's knowledge. Numbers
  and invented-rule answers may simply not be what the model puts first in a reply, for example before
  "The answer is". The single-token, five-candidate comparison then picks almost at random among
  near-equal low probabilities. This is a hypothesis, not a measurement.

**What it means for the design.**
- **The bites check fails.** It needs the one-pass run to cost at least 0.15 on chains of four or more
  steps, compared with three passes (design, section 5). Here three passes is at 17%, already below chance,
  so the check cannot be met. The result would be "not testable" for a reason unrelated to the removal,
  which RT-432 warned of.
- **Most items fail the confidence filter.** The filter keeps an item only if its margin is at least 2.2, and
  most items here fall short. Too few pairs would survive.

## Which of the design's return-to-John rules fired

| Rule (design, section 9, step 4a) | Fired? |
|---|---|
| The hooks cannot be built | No: built and verified |
| One of the three facts the bypass check needs is false | No: all three hold (the bypass check passes exactly) |
| The identity or bypass check fails | No: both pass with a difference of 0.0 |
| The reply opening differs from what the pilot assumed | **In part.** The first token is as assumed, but the model always continues with written reasoning, which the forced opening skips |
| Not a listed rule, but the design cannot proceed | **Yes.** The native precision could not be used, and the forced-answer scoring gives near-chance accuracy, so step 4b's checks cannot be met |

## What John is asked to decide

Nothing more is spent until he rules. The options, each of which would be a design change with its own
review:

1. **The scoring method** (choices 1 and 2). The options:
   - (a) keep forced answers, but tell the model in the prompt to answer with the single word or number
     only;
   - (b) add a fixed answer lead-in, such as "The answer is", after the forced opening, and score the
     candidate after it;
   - (c) let the model reason in writing and score its final answer. That drops choice 2, and with it the
     claim that the test reads one moment.

   Options (a) and (b) can be tried cheaply on the pilot. Each would need a short run, priced first.
2. **Precision.** Accept 16-bit as the working precision for this test, or wait for, or build, support for
   the native format.

## Record

- **Spending.** The spending record's step-4a rows now carry the cost.
- **The script.** `src/step4a.py` as committed with these findings is the version that ran. It loads at
  16-bit, uses the reply-opening fix for transformers 5, and has the wait-check fix in the runbook commands.
- **Owed.** RT-345 stays open, and nothing here bears on it. These findings are owed an independent check.
