# The split removal test: run notes

*Standing notes for anyone planning or briefing a run of this experiment. Newest first.*

## Where model runs happen (John's standing rule, 2026-10-24)

John's words, relayed by the fourth weekend master session on 2026-10-24: "let's prioritize using RunPod until I am able to get a dedicated desktop computer for this kind of research work."

- **Plan every model run on RunPod, not the Mac.** The Mac ran hot and slow during the fixes run on 2026-10-24, which is what prompted the rule.
- **Each run still needs John's go first.** It goes to the master session with an estimate and a ceiling. Running on RunPod is a spend, so a pod is never started without that go.
- **The gated test model needs John's Hugging Face read token on the machine.** He enters it himself. It is never asked for in chat, and never written into the repository or a log.
- **Enforce the ceiling from the laptop.** RunPod's own auto-terminate time is advisory: the compute ledger records that it once never fired (`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`). Each launch therefore runs a timer on the laptop that deletes the machine at the ceiling, with the laptop kept awake.
- **Record the spend in `docs/spending-record.md`,** with John's go quoted. Write a worklog row before the machine is created and another after it is deleted, with the actual cost from RunPod's billing rows.

## The 2026-10-24 fixes run

- **Started on the Mac** at $0, under the ruling "on the bench model at $0".
- **Stopped partway at John's request,** because the Mac was running hot. Four of six normal-range bounds were saved (commit 71dfed8).
- **Moved to RunPod** under John's go: "Go on RunPod for the rest of the Minimum Viable Mind run, up to $2. I'll put my Hugging Face token on the pod."
  - No community-cloud RTX 4090 was free, so the machine is a secure-cloud RTX 4090 at $0.89 an hour.
  - It was created at 13:31 PDT, with a laptop timer set to delete it at 15:31 PDT (at most about $1.78). It was deleted at 14:25 PDT at the master session's instruction, before three of the six removal checks had run. It cost about $0.77.
- **Lessons for the next launch.** The image's preinstalled `torchvision` breaks model loading after `torch` is upgraded, so uninstall it at setup. The probes run on the machine's ordinary processor and take about 10 minutes per check at 26 layers, so budget for that, or move the probes onto the graphics card.
- **The first four bounds ran on the Mac (Apple's graphics chip) and the rest on the RunPod card.** Each bound compares an intervention with random interventions on the same hardware, so every bound is consistent within itself. The baseline for the which-did-you-say items is re-measured on the RunPod card before the checks.
