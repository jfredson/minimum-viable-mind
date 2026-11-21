# The loop removal test, step 4a: a priced proposal for John's go

*Written 2026-11-21 on John's instruction ("Yes, price it"). Step 4a of section 9 of the design
(`docs/loop-removal-test-design-2026-11-20.md`, version 0.8) is the first step that costs money. John's
ruling of 2026-11-21 allowed paper work only (`docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`),
so this step needs his go, with an estimate and a ceiling, as every spend does. Nothing has been rented or
spent.*

## What John should know first

**The free checks settled nothing about the real effect of the swap.** All the step-3 checks on the
practice set passed. But they passed by construction: the two twins of every pair are the same text up to
their final question, so a count of tokens cannot see any difference between the groups. Whether the swap
does the same amount of damage to both groups (RT-345, the one fatal question still open) can be measured
only on the model, at step 4b. This is the plain telling the design promised (RT-391, and the note in
section 11 on choice 3). John chose routine twins expecting the dose question to be settled for free. It
was not, and step 4a does not settle it either.

## What step 4a is for

Step 4a checks that the test can be run at all, before any measurement. On one rented machine, a session
would:

1. **Load the model.** Load the variable-loop research model (TML-d24-varloop-research), and confirm how much
   memory it takes and whether it runs in its native 4-bit format with hooks attached.
2. **Confirm the hooks.** Confirm that the two block sums the message is built from can be read and
   replaced on passes 2 and 3.
3. **Confirm the facts the design takes from Goodfire.** Goodfire studied the sister model, Inkling 2 Mini,
   not this one. Section 2 lists those facts, and three of them are what the bypass check needs:
   - pass 1 has no mixing step;
   - each pass's own block sums start from zero;
   - each pass has its own attention keys and values.
4. **Settle how the model's reply opens,** which the practice set assumed (`<|message_model|><|content_text|>`).
   Also settle whether the reasoning setting "none" stops written reasoning. If the opening differs from
   the assumption, the practice set is rebuilt before anything is scored (specification, section 9).
5. **Measure the noise floor.** Run the same items twice, unchanged, and see how far the answers move.
6. **Run the two checks on the code.**
   - **The identity check:** an item given its own message must reproduce the normal run.
   - **The bypass check:** skipping the mixing step must reproduce the one-pass run.
7. **Return to John if anything fails.** The design returns to John if any of these fail: the hooks cannot
   be built, any of the three facts is false, either check fails, or the reply opening needs the practice
   set rebuilt. None of these failures costs more than step 4a itself.

**What it does not do.** It scores no outcome. It runs no comparison removal. It measures nothing about the
swap's dose, and it says nothing about the hypothesis.

## The machine

| Option | Memory | Price an hour (RunPod secure cloud) | Fits? |
|---|---|---|---|
| **RTX PRO 6000 Blackwell (recommended)** | 96 GB | $2.69 | Yes, in the model's native 4-bit format, and also if the hooks force the weights to be unpacked to 16-bit (about 53 GB, design section 8) |
| RTX 5090 | 32 GB | $1.39 | Only if the hooks work in native 4-bit. If they do not, the run stops and a second machine must be rented |
| A100 80 GB | 80 GB | $2.09 | Only with the weights unpacked to 16-bit, because this older card has no native 4-bit support. The numbers would then differ from the model's native precision |

Prices come from RunPod's public pricing page (https://www.runpod.io/pricing, "Updated November 12, 2026"),
read 2026-11-21. They are the secure-cloud prices the page shows. A cheaper community-cloud machine may be
free when the run starts, and is used if it is. Billing is by the second.

**Why the dearer card.** The RTX PRO 6000 is the one card that runs the model in the precision it was trained
in and still has room if the hooks need the weights unpacked. On the 5090, the most likely failure is
running out of memory, which would mean paying for a second machine and redoing the setup.

**The download.** The model is public and not gated (its Hugging Face page, read 2026-11-21), so no Hugging
Face token is needed on the machine. The download is about 20 GB, to the machine, not to the Mac.

## The estimate and the ceiling

| Part | Machine time |
|---|---|
| Start the machine, install the software, download the model | 30 to 45 minutes |
| Build and debug the hooks, settle the reply opening and the reasoning setting | 1 to 2.5 hours |
| Run the noise floor, identity, bypass and one-pass checks on the 120 pilot pairs and 40 chained items | about 15 minutes |
| **Total** | **about 2 to 3.5 hours** |

- **Estimate: about $5.40 to $9.40,** at $2.69 an hour. The disk adds under $0.10 for the hours involved.
- **Proposed ceiling: $15.** It is enforced the way the last run was: the session on the laptop deletes the
  machine 5.5 hours after creating it, whatever state it is in (5.5 × $2.69 = $14.80). The ceiling is set
  at about one and a half times the top of the estimate, because building hooks on a new model is the most
  uncertain part. If the hooks are not working by the deadline, the machine is deleted, and the findings say
  how far it got.
- **What could cut the cost.** The hook code can be written on the Mac first, for free, against the model's
  published configuration and Goodfire's description. Then the machine is used to test it rather than to
  write it. That would likely put the run at the low end of the estimate. This is recommended.
- **The account balance.** The last recorded RunPod balance was $65.62, on 2026-10-24
  (`experiments/09-split-removal-test/rehearsal/fixes-findings-2026-10-24.md`). The current balance is not
  known here. John would see it on RunPod's billing page.

## How it would be recorded

- **Before the machine is created:** a row in `docs/spending-record.md` with John's go in his words, the
  estimate and the ceiling, and a worklog entry.
- **After it is deleted:** the time used and the cost, from the balance before and after.
- **The findings:** a findings file at `experiments/10-loop-removal-test/step4a-findings-*.md`, then an
  independent check of them, as for every step so far.

## What John is asked

1. **Whether to go:** step 4a on one RTX PRO 6000 Blackwell (96 GB) on RunPod, estimated at $5.40 to $9.40,
   with a ceiling of $15 enforced by deleting the machine after 5.5 hours.
2. **Whether to write the hook code on the Mac first,** for free, before renting. Recommended.

The project pauses on 2027-01-04. Step 4a fits well before that, and nothing after it is started without
another go.

---

## Addendum, 2026-11-21: after the hook code was written on the Mac

*Added on John's instruction ("Yes, write it first"), after `src/step4a.py` and `step4a-runbook.md` were
written. The model's code was read in the public transformers repository (commit 046bdb8, the commit that
added it, dated 2026-11-21), and nothing was rented.*

**What changed.** The source shows that the hooks touch only `message_input`, a module the model keeps in
32-bit. So the 4-bit weights never need unpacking, which was the reason for recommending the 96 GB card. The
32 GB RTX 5090 should be enough, and the time on the machine should be shorter, because the code now exists.

| | Recommended now | Fallback |
|---|---|---|
| Card | RTX 5090 (32 GB), $1.39 an hour | RTX PRO 6000 Blackwell (96 GB), $2.69 an hour |
| Estimated time | about 1.5 to 3 hours | the same |
| Estimate | about $2.10 to $4.20 | about $4.00 to $8.10 |
| Ceiling, enforced by deleting the machine after 5.5 hours | **$8** (5.5 × $1.39 = $7.65) | $15 (5.5 × $2.69 = $14.80) |

If the 5090 runs out of memory, the run stops and the choice comes back to John. Prices are RunPod's
secure-cloud prices (pricing page read 2026-11-21).

**What John is asked, as revised:** step 4a on one RTX 5090, estimated at $2.10 to $4.20, with a ceiling of
$8 enforced by deleting the machine after 5.5 hours. The plain telling above stands: none of this measures
the swap's dose.
