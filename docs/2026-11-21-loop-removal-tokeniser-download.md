# The research model's tokeniser and chat format, downloaded (2026-11-21)

*Recorded 2026-11-21 by the session that wrote the loop removal test design. The download was made on John's go of the same day ("Yes, download them"), given in answer to the roadmap step "GO (John): download the variable-loop research model's tokeniser and chat template (small files, no model weights)". Nothing else was downloaded, and nothing was spent.*

## What was downloaded, and from where

The files come from Thinking Machines Lab's Hugging Face repository for the variable-loop research model,
[thinkingmachines/TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research).
The repository was public and not gated when the files were fetched. They were fetched at a pinned revision, `657b53ba5da7baefe9ff15dca5cd25f5bd3dbaa2`, so that the same files can be fetched again.

They are stored outside git, in the project's ignored model cache: `.hf-cache.nosync/tml-d24-varloop-research-tokenizer/`, about 29 MB in all. The revision is written in a `REVISION` file beside them. The model's weights (`model-00001-of-00001.safetensors`, about 20 GB, and `mtp.safetensors`) and its `config.json` were **not** downloaded.

| File | Bytes | SHA-256 |
|---|---|---|
| `tokenizer.json` | 26178678 | `7f332727f9a3f093dd452a39cc978e6757627e5dad1b0673aa4e75174f236dd6` |
| `tokenizer_config.json` | 13235 | `bf09342d285139fd37ce10c70878af1d52cb390e9901e10248654293a80ee636` |
| `special_tokens_map.json` | 529 | `c16f44b3594563d82743ddb0417a2be1bfe3e2000dfad2da4b8f32554593e1a0` |
| `chat_template.jinja` | 6868 | `53a9035f3255945704b5857657cfb00c1165090c0641c4f782a0cbf268cc16dc` |
| `tiktoken/tokenizer.model` | 3386494 | `f170372dd655728909228220d77cf6b8104a59f38a91262a7d2c4027906ec0d8` |

## What a first look at the files shows, read without running any of their code

- **The tokeniser needs no outside code.** `tokenizer_config.json` names the standard `PreTrainedTokenizerFast` class and has no `auto_map` entry, so loading it runs no code from the repository.
- **Its contents.** `tokenizer.json` describes a byte-pair tokeniser with 199,998 entries and 424,413 merges, plus 60 added special tokens. Among them are the role markers `<|message_user|>`, `<|message_model|>` and `<|message_system|>`, and a marker for written reasoning, `<|content_thinking|>`.
- **The chat format has a setting for how much the model thinks.** `chat_template.jinja` takes a `reasoning_effort` between 0.0 and 0.99, with named levels from "none" (0.0) to "max" (0.99). The default is 0.9. It writes the setting into a system message reading "Thinking effort level: ...". This bears on choice 2 of the design (no written reasoning). The setting "none", which writes "Thinking effort level: 0", is the obvious candidate. Whether the model then writes no reasoning at all can only be seen by running it, at step 4a.

## What is still needed before the step-3 checks can run

Reading these files properly needs two Python libraries that are not installed on this Mac: `tokenizers`, to split text into the model's tokens, and `jinja2`, to render the chat format. Both are standard, widely used packages from the Python package index. Installing them is a download beyond the files John approved, so it goes to him first. Until then, no token count in the design's checks has been made with the real tokeniser.
