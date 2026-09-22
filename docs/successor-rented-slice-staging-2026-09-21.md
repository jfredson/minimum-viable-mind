# The one short slice of rented time — staged, and not run

*2026-09-21 (Pacific). **UNREGISTERED.** Nothing here is a ruling and nothing
here has been executed. No machine was rented, no vendor was contacted and no
money was spent to write it.*

*Written under the workspace plain-language rule. The rental service's word for
one rented machine is not used; this file says **rented machine**.*

---

## 1. What this is, and why it is one slice and not two

John ruled on 2026-09-21 that the second release of money is asked for only
after the rehearsal has measured seconds per step for all three architectures,
so that the figure rests on a measurement rather than on the per-step premium
carried over from a different experiment's full-versus-twin step times. A
throughput figure measured on the laptop cannot do that job: seconds per step
on an Apple M4 predicts nothing about seconds per step on a rented graphics
card, which is the whole reason the ruling declined to rely on an inference.
So a short slice of rented time is owed.

Separately, the fix for the race between the trainer deleting its own machine
and the laptop taking the final copy has landed on the main line as pull
request 15. Its own method note says, in its closing recommendations, that the
right place to test it against the real vendor is this rehearsal: a toy run
that finishes in minutes exercises the whole shutdown path — the credential on
the machine, the watcher starting, the finished-marker, the receipt, the
deletion — for a few cents, well before about $110 of registered runs depend
on it.

**Both questions need the same thing: one rented machine, briefly.** So they
are one slice, and the money buys two answers.

**This slice is staged and has not been run.** John's ruling that a rented
slice will happen is a ruling on a plan; it is not the spoken go naming a
specific run that this programme's corrigibility commitments require, and that
go has not been given.

## 2. What blocks it, named as tasks rather than as dates

Nothing here is waiting for a calendar slot. What it is waiting for:

1. **John's spoken go naming this run.** Owed at the moment the run is staged,
   which is now.
2. **A decision on the dedicated reaper key** (section 5). Without it the
   machine's own shutdown watcher is not armed and the slice tests only the
   smaller half of what it is for. Checked locally while staging: a dedicated
   key is present and carries the file permissions John's ruling of
   2026-09-16 requires, so on today's laptop the launcher would arm the
   watcher and the slice would test the full path. The staging script
   re-checks this every time it runs and says which path the slice would
   take.
3. **A ledger row written before the spend**, quoting the go, per the compute
   ledger's own second rule.

The two kill dates are unchanged and are backstops rather than pacing:
registration committed by 2026-10-18, registered runs launched by 2026-11-01.

## 3. What the slice does

One rented machine, one short session.

- **A toy run through the derived launcher.** Small enough to finish in
  minutes. Its purpose is not to learn anything; it is to reach the
  finished-marker so the shutdown handshake happens for real.
- **While that run trains, the three architectures are timed on the same
  machine**, at the registered shape, and the result is written into the run
  directory on the network volume so that the laptop's final copy brings it
  home. That makes the throughput measurement ride on the same fetch whose
  correctness the other half of the slice is testing, which is a small bonus:
  if the fetch fails, the absence of the file says so.

The exact commands, the settings and the plan are produced by
`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`, which
checks what can be checked locally, writes the plan to a file, and **contains
no command that creates a rented machine**. It cannot spend money because
there is nothing in it that could.

## 4. Which launcher, and what is not touched

**`launch_a3.sh` is registered text and is neither used nor edited.** Amendment
A3's "what is registered" section names it, along with the grammar, the
tokenizer, the trainer, the frozen batteries and the gates.

The slice uses the derived, unregistered `launch_a3_fetch_first.sh`, which
landed with the shutdown fix. It is produced from the registered launcher by
a script that applies nine named replacements and asserts that each one matched
exactly once, so "derived verbatim" is a checkable claim rather than a promise.
The registered launcher and the registered trainer were both confirmed
untouched by that change — an empty difference against the state before it.

**This staging does not change the shutdown fix and does not duplicate it.** It
exercises it. The fix is another session's work and its author's own account of
what is inferred rather than measured is what section 5 is built around.

## 5. The thing this slice is really for

The shutdown fix is verified against local stand-ins only: twenty-six checks,
including a negative control that reproduces the old ordering and correctly
fails, which is the part that makes the suite worth anything. Its author is
explicit that the machine-side process check, the credential handling and the
command form are **inferred rather than measured**.

That matters more than it sounds, because the one thing this programme has
actually measured on a real rented machine is that **a rented machine carries
no usable credential and does not know its own identifier**. That was a paid
test on 2026-09-16 costing $0.29: no identifier in the environment, no
variables from the vendor at all, and the vendor's own command-line tool
installed but unconfigured. The conclusion drawn at the time was that the
laptop was the only reap.

The fix's answer is that the launcher supplies both — a dedicated key whose
only job is deleting machines, and the machine's own identifier written to a
file. **That answer has never been tried against the vendor.** Everything the
handshake does on the machine's side rests on it. If it does not work, the
machine cannot delete itself, the bounded wait cannot end the billing, and the
laptop is once again the only reap — which is exactly the state the fix was
built to leave behind.

There is a second inferred detail worth watching: the two ends run different
versions of the vendor's command-line tool, and the version on the vendor's own
image has no subcommand for machines at all, so the machine-side script tries
two command forms. Which one answers is a measurement nobody has taken.

## 6. What passing looks like, written down before it runs

### Throughput

- **Pass** — three seconds-per-step figures, one per architecture, with the
  spread over the timed steps, written to a results file and fetched home.
  The second release of money is then asked for on that measurement.
- **Fail** — any architecture will not run at the registered shape on the
  rented hardware, for instance because it runs out of memory. That is a
  finding about the design, not about the machine, and it goes back into the
  proposal before registration.
- **No verdict** — the machine is unavailable, or it bills at the anomalous
  rate of the 2026-08-08 row. Stop condition S9 fires: the wave halts and the
  billed row goes to John beside the estimate.

### The shutdown handshake

The signals are the fix author's own, and they are expected in this order:

- **Pass** — `receipt written on the machine` in the laptop's log, then
  `receipt found` in the machine's log, then a deletion within seconds of it;
  and the copied model file matches the one on the machine by checksum.
- **Fail, the bounded-wait path** — the machine's log says `grace ran out`.
  The receipt path did not work and only the bounded wait ended the billing.
  The run is treated as unsafe to leave unattended until that is understood,
  and the registration cannot lean on the handshake.
- **Fail, the credential path** — the machine cannot delete itself even after
  the bounded wait. That is the 2026-09-16 measurement repeating, and it means
  the laptop is still the only reap.
- **No verdict** — the slice does not run. Then the handshake stands verified
  against local stand-ins only, and the registration text says so in its own
  words rather than implying more.

A fourth outcome worth naming because it is the quiet one: the machine's own
watcher **never starts**, the launcher falls back to the trainer deleting
itself, and everything looks normal while nothing has been tested. The
launcher says so loudly when it happens, and the plan file tells the operator
to read that line before believing the run tested anything.

## 7. What it costs

A toy run that finishes in a few minutes, fifty timed steps on each of three
architectures, and a bounded wait that the passing path never reaches. Well
under an hour of rented time.

| | |
|---|---|
| Rate, from the most recent registered runs (the 2026-09-17 ledger row: two machines, 20.28 machine-hours, $20.08) | **$0.99 an hour** |
| Estimate | **about $0.75 to $1.00** |
| Hard cap | **$2.00** |
| Precedent for a short, deliberately capped test | the self-delete test of 2026-09-16, authorised at a $0.50 cap and billed at $0.29 |

It sits inside the first release of money John authorised on 2026-09-21, whose
rehearsal line is up to $10 and of which nothing has been spent: everything
else in this rehearsal ran on the laptop for nothing.

## 8. What the slice cannot answer

- **It is not a learnability run.** The toy run is sized to finish, not to
  learn, and nothing about the successor design's science may be read off it.
- **It does not settle the seed count or the separation bar.** Those come from
  the rehearsal's own measurements and from John.
- **It measures the handshake once.** One passing run shows the path works; it
  does not show the path is reliable. The honest claim afterwards is "it has
  been seen to work once, against the real vendor", which is still enormously
  more than "it has never met the vendor".
