# The loop removal test, step 4a: runbook

*Written 2026-11-21, before any machine was rented, together with `src/step4a.py`. Nothing in this runbook
runs until John has given his go in his own words, with the ceiling. His go and the ceiling are recorded
first, as a row in `docs/spending-record.md` and a worklog entry.*

## What reading the model's source settled before renting

The model's code is public in Hugging Face transformers, added on 2026-11-21 at commit
`046bdb8cc2cee29d233964bb77fe6fd37cfe4aa3` ("Add Inkling2 Mini (#51050)"). It is at
`src/transformers/models/inkling2_loop/modular_inkling2_loop.py`, read on GitHub on 2026-11-21. Reading it,
without running it, settles points that step 4a was going to settle on the machine:

- **The message is built in one place.** The text model's `forward` calls
  `self.message_input(previous_block_states, previous_hidden_states, loop_layer_idx)` once per looped layer
  on each pass after the first. `previous_block_states` holds the previous pass's completed loop block sums,
  and `previous_hidden_states` its final running state. These are the design's "two block sums the message
  readers read". Hooking `message_input` therefore reaches every reader, as the design asks (section 3).
- **The three facts the bypass check needs hold in the source:**
  1. Pass 1 calls the looped layers with no messages. A layer given `messages=None` takes exactly the pass-1
     path, with no mixing step.
  2. Each later pass restarts from the pre-loop hidden and block states (`hidden_states, block_states =
     pre_loop_hidden_states, pre_loop_block_states`).
  3. Each later pass uses its own cache slots (`cache_offset`), and the script runs with no cache at all.

  So making `message_input` return nothing on passes 2 and 3 is the design's bypass, and it should
  reproduce the one-pass run.
- **The number of passes** is read from `config.loop_num_passes` at every forward call. So the fewer-passes
  runs need only that setting changed.
- **The mixing.** It is the design's keep-and-gain step (`Inkling2LoopMessageGate`):
  `(1 - forget_gate) * hidden_states + message_gate * message`, with both gates passed through `tanh`.
- **The precision of what the hooks touch.** `message_input` and the message gates are listed among the
  modules kept in 32-bit (`_keep_in_fp32_modules_strict`). So the hooks touch no 4-bit weight, and the
  weights should never need unpacking to 16-bit.

What reading cannot settle, and step 4a must:
- whether the model loads and runs on the card;
- the noise floor;
- the identity and bypass checks as measured;
- how the reply opens;
- whether reasoning "none" stops written reasoning.

## Which card, revised

The priced proposal recommended the 96 GB RTX PRO 6000 Blackwell at $2.69 an hour, in case the hooks forced
the weights to be unpacked to 16-bit (about 53 GB). The source shows they do not (above). The model is about
20 GB, the practice items are at most about 300 tokens, and the hooks store only small activations. So the
32 GB **RTX 5090 at $1.39 an hour** (RunPod secure cloud, pricing page read 2026-11-21) should be enough. It
is also a Blackwell card, so it runs the model's native 4-bit format.

**If the 5090 runs out of memory,** the run stops, the machine is deleted, and the choice of card comes back
to John. The design's other return-to-John rules for step 4a are unchanged.

## The steps

1. **Before anything is created.**
   - Record John's go in his words, the estimate and the ceiling: a row in `docs/spending-record.md`, and a
     worklog entry.
   - Note the RunPod balance from the billing page or `runpodctl`.
2. **Create one pod.** Use the card John approved, from the secure cloud unless a community-cloud one of
   the same card is free. The image is a current PyTorch image with CUDA 12.8 or newer, which Blackwell
   cards need, and a container disk of 60 GB. Record the pod's id and its creation time.
3. **Start the deadline at once, on the laptop.** A background command deletes the pod at the ceiling's time
   (5.5 hours), whatever its state:

   ```bash
   (sleep 19800; runpodctl remove pod <pod id>) &
   ```

4. **Copy the code and the pilot to the pod:** `experiments/10-loop-removal-test/src/` and
   `experiments/10-loop-removal-test/batteries/pilot/`.
5. **Install the software on the pod:**

   ```bash
   pip install "git+https://github.com/huggingface/transformers@046bdb8cc2cee29d233964bb77fe6fd37cfe4aa3" accelerate
   ```

   If loading reports that the 4-bit format needs NVIDIA's modelopt package, install `nvidia-modelopt` and
   record it in the findings. The model is public and not gated, so no Hugging Face token is needed.
6. **A quick first try on 10 items:**

   ```bash
   python -I src/step4a.py --pilot batteries/pilot --out out-quick --limit 10
   ```

   Fix anything that breaks. Every fix to `step4a.py` is copied back and committed with the findings, so that
   the record shows what changed.
7. **The full run** over all 280 practice items (240 pair items and 40 chained items):

   ```bash
   python -I src/step4a.py --pilot batteries/pilot --out out
   ```

8. **Copy the results back.** That is `out/step4a-results.json` and the run's log. **Delete the pod.** Cancel
   the deadline command. Note the balance again.
9. **Write it up.**
   - Record the cost: a spending-record row and a worklog entry.
   - Write `step4a-findings-<date>.md`. It states what passed and what failed, and which of the design's
     return-to-John rules fired:
     - the hooks could not be built;
     - one of the three facts was false;
     - the identity or bypass check failed;
     - the reply opening differs from the pilot's assumption, so the pilot must be rebuilt.
   - The findings are then checked by a session that did not write them.

## What the script reports

`out/step4a-results.json` holds:
- the software and card;
- the load, with time and memory;
- the reply opening, under reasoning "none" and the default;
- the noise floor and the tolerance derived from it;
- the identity check and the bypass check, each against that tolerance;
- descriptive accuracy at 1, 2 and 3 passes on the practice items, chained items included. These are
  descriptive only: no outcome is read and no threshold is set from them. They give the first sign of the
  risk RT-432 raised, that the chained items may be too hard at three passes;
- the peak memory.

## What step 4a does not do

It runs no swap between items, no average method and no comparison removal. It measures nothing about the
swap's dose (RT-345), and it reads no outcome.
