# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 21 of 22: The compute ledger, part 3 of 3

*This is file 21 of 22 of one review packet, pasted into a single
conversation. It contains the compute ledger - its rules, its baseline, the
rows the text cites and the rows that correct them (part 3 of 3). Reply with
one short line saying you have it, and wait for the rest: the brief you are
answering is in file 1, and your review comes only after file 22 arrives. If
this file looks cut short, say so now.*

---

===== RECORD 22 of 23, part 3 of 3 - the compute ledger - its rules, its baseline, the rows the text cites and the rows that correct them - EXCERPT: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md =====

*Source note: excerpted from `experiments/06-mvm-0a-constructed-self-
index/compute-ledger.md` (86,441 characters in full), which carries a row for
every rented-machine session since 2026-08-07. Reproduced here: the ledger's
opening, its rules, its reconciliation baseline, its column headings, five
rows in full and one dated note. The five rows are the two dated 2026-09-19
and 2026-09-20 that the text under review cites for its money figures, the two
follow-up runs of 2026-09-20 that carry the $1.90 those figures are stale by,
and the measurement rehearsal of 2026-09-21, whose running-total column is
where the ledger states the corrected figures. The dated note is the ledger's
launch-outcome note of 2026-09-20 on those two follow-up runs. The other rows
are left out, so the cited rows and the correcting rows can both be checked
but the running total cannot be re-added from the beginning.*

*This part is the measurement rehearsal of 2026-09-21, whose running total
states the corrected figures, and the ledger's dated note on the two follow-up
runs. The other parts of this record are in file 19 and file 20.*

| 2026-09-21 | measurement rehearsal — the rented slice (UNREGISTERED) | **ROW WRITTEN BEFORE ANYTHING WAS CREATED**, per ledger rule 2 (estimate before spend) and commitment C2(b) (the go quoted verbatim in the run’s own ledger row). **THE MEASUREMENT REHEARSAL’S ONE RENTED SLICE.** One rented machine, one short session, bought to answer two questions that need the same thing: (1) **seconds per step for the three successor architectures at the registered shape**, measured on a rented graphics card instead of inferred from an Apple M4 laptop, which is what John’s ruling of 2026-09-21 required before the second release of money is asked for; and (2) **whether the shutdown handshake that landed as pull request 15 — the fix for the trainer deleting its own machine before the laptop takes the final copy — works against the real vendor end to end.** Staged in `docs/successor-rented-slice-staging-2026-09-21.md` (the plan of record for this run, written before the machine existed) and produced by `experiments/rehearsal-successor-measure/src/stage_rented_slice.sh` (the staging script, which contains no command that can create a machine). **Nothing about the successor design’s science is read off this run; it is sized to finish, not to learn.** **John’s go, quoted verbatim per C2(b):** “Go. Run the rented slice exactly as staged in docs/successor-rented-slice-staging-2026-09-21.md, and nothing beyond it. What is authorised: one rented machine, one short session, the toy run through the derived launch_a3_fetch_first.sh, and fifty timed steps on each of the three architectures at the registered shape, with the results written into the run directory on the network volume so the final copy brings them home. Estimate $0.75 to $1.00, hard cap $2.00, drawn from the rehearsal line of the first release (up to $10), which nothing has been spent from. This go covers this run and nothing else. The registered wave still needs its own. Before anything is created: write the ledger row quoting this message as the authorisation, per ledger rule 2. Confirm zero machines are running. Confirm the rate at creation time rather than assuming the $0.99 the estimate descends from. launch_a3.sh is registered text. Do not use it and do not edit it. No tolerance is widened and no registered file is touched. If the slice can only be made to pass by changing the instrument, it fails instead. Report back whatever happens: the three seconds-per-step figures with their spread; which shutdown path the launcher actually armed, said plainly, including the case where the machine’s own watcher never started and the run only looked normal; the handshake signals in order, receipt written, receipt found, deletion, and whether the copied model matched by checksum; and the actual billed amount against the estimate. Stop conditions: if the machine bills at the anomalous rate of the 2026-08-08 row, S9 fires, halt and bring me the billed row beside the estimate. If any architecture will not run at the registered shape, stop and treat it as a finding about the design, which goes back into the proposal before registration. Nothing about the successor’s science is read off this run. It is sized to finish, not to learn.” **Pre-creation checks — all three done immediately before creation and recorded here rather than assumed.** (i) **Zero machines running:** the vendor’s machine list came back empty, and the account’s own current-spend-per-hour read **$0.01**, which is the network volume’s storage drip alone — two independent confirmations rather than one. (ii) **The rate read from the vendor at creation time, not assumed:** RTX 5090 secure cloud at **$0.99 an hour** (stock “Low” but present), which is **the registered rate and not an elevated one**. The estimate descends from the 2026-09-17 row’s $0.99 and the live figure agrees with it. (iii) **Funding rule:** balance **$77.3451**, against about $1 in flight plus the $10 margin — passes with room. **Rule 2’s own test passes:** the worst case of this run is the $2.00 hard cap, which takes the A3 cumulative from about $46.2 to about $48.2 of $100 and the wider programme envelope from about $227.6 to about $229.6 of $400. **Launcher: the derived, unregistered `launch_a3_fetch_first.sh`.** `src/launch_a3.sh` is **registered text and was neither used nor edited**; no tolerance was widened and no registered file was touched. **One honest wrinkle recorded rather than smoothed over:** commitment C2(d) says a delegated launch uses “the registered launcher and venue”, and this slice deliberately uses the derived one. John named that derived launcher himself in the go, the venue is unchanged, and no registered result is read off the run — so the clause’s purpose (a delegated launch must not silently swap the instrument) is served. It is recorded here because a clause satisfied in spirit and not in letter should be visible in the audit trail, not argued away in a session that nobody can read later. A second wrinkle, smaller: the launcher’s header still carries the v1.0 wording “HUMAN-RUN ONLY [C2] … Claude prepares it, John executes it”, which C2 v1.1 (2026-08-16) superseded by delegating the keystroke and never the decision; the same stale line sits in `launch_a3.sh` and in `launch_ctl_pilot.sh`, both of which have been executed under the delegated reading. **What runs, in the order the plan file sets out:** a dry run that creates nothing; then the toy run through the derived launcher at the 10M shape with a 2,000,000-token budget, small enough to finish in minutes, whose only job is to reach the finished-marker so the shutdown handshake happens for real; then, while that trains, fifty timed steps on each of the three architectures at the registered shape, written to `bench_arms.json` inside the run directory on the network volume **so that the laptop’s final copy is what brings the numbers home** — which makes the throughput measurement ride on the same fetch whose correctness the other half of the slice is testing. If the fetch fails, the absence of the file says so. **What passing looks like, written down before it ran.** Throughput: three seconds-per-step figures with their spread, fetched home. The handshake, in this order and no other: `receipt written on the machine` in the laptop’s log, then `receipt found` in the machine’s own log, then a deletion within seconds of it, and the copied model file matching the one on the machine by checksum. A machine log reading `grace ran out` is the bounded-wait failure; a machine that cannot delete itself at all is the 2026-09-16 credential measurement repeating. **And the quiet fourth outcome, named in advance because it is the one that looks like success:** the machine’s own shutdown watcher never starts, the launcher falls back to the trainer deleting itself, and everything looks normal while the thing the slice exists to test was never tested. The staging script checked the precondition for that today and it passed — a dedicated reaper key is present at file permissions 600, per John’s ruling of 2026-09-16 — so the full path is expected to be armed; the launcher says loudly which path it took and that line is read before anything is believed. **Stop conditions carried from the go:** if the machine bills at the anomalous rate of the 2026-08-08 row — that row billed 8.47 hours against about 2.42 hours of actual machine existence, about 3.5× — stop condition S9 fires, the slice halts and the billed row goes to John beside the estimate. If any architecture will not run at the registered shape, that is a **finding about the design and not about the machine**, and it goes back into the successor proposal before registration. | RTX 5090 SECURE EU-RO-1, **$0.99/hr confirmed from the vendor at creation time**, network volume `x9f8pkn58t` (`mvm-models-ro`, the 100GB volume in EU-RO-1 that outlives the machine) | **est well under 1h** — a toy run of a few minutes, fifty timed steps on each of three architectures a few minutes more, and a bounded wait of 600 seconds that the passing path never reaches. **ACT: about ONE MINUTE of machine life, and none of it was the authorised run.** Machine `f1vtz2adz4dj8v`, named `mvm-a3_30m_seed0`, created about 2026-09-22T04:12:19Z and deleted about 2026-09-22T04:13:1xZ. See the annotation below: it was created by the plan's own step 0, which was supposed to create nothing. | **$0.75–1.00, hard cap $2.00** | **about $0.02** — one minute of an RTX 5090 at $0.99 an hour, for a machine nobody meant to create. The account balance read **$77.3451129146** immediately before creation and **$77.3451129146** immediately after deletion, identical to ten decimal places, so the charge had not yet landed when this was written and the figure is arithmetic on the machine's lifetime rather than a balance reading. **The authorised slice was NOT run and none of the $0.75–1.00 estimate was spent.** It is halted and back with John, per his own instruction to stop and report rather than fix anything found wrong in the plan. | Before this run: A3 cumulative about **$46.2 / $100**, programme about **$227.6 / $400**, account balance **$77.3451**. This slice is drawn from **the rehearsal line of the first release of money John authorised on 2026-09-21 (up to $10), from which nothing had been spent** — everything else in the rehearsal ran on the laptop for nothing. **Running total: essentially unmoved.** A3 cumulative about **$46.2 → about $46.2 / $100** and the wider programme envelope about **$227.6 → about $227.6 / $400**; the two cents do not move either figure at the precision this ledger carries them. Of the rehearsal line's $10, **about $0.02 is spent and about $9.98 remains**. The $0.75–1.00 estimate stands unspent and the go is not used up: John decides whether it still covers a re-run once the step 0 defect is ruled on. |

**ANNOTATION 2026-09-20, launch outcome — BOTH PODS WERE CREATED, BOTH
WERE REFUSED BY THE INSTRUMENT CHECK, AND BOTH WERE DELETED. Total
measured spend $1.904. Neither follow-up run produced a single sweep
number on rented hardware, and the reason is worth more than the two
dollars it cost to learn.**

- **What was created.** Two pods in EU-RO-1 secure, each four RTX PRO 4000
  Blackwell cards, 48 virtual cores on an **AMD EPYC 7352 (24 physical
  cores)**, 124 GB, $2.28/hr, the A3 network volume `x9f8pkn58t` mounted,
  all three A3 checkpoints present on it at the byte sizes this ledger
  already records. Pod `g0u3gwttjmhpyj` carried run 1, pod
  `3pvwvjkicbbsov` run 2. Both were created at about 19:33Z and both were
  gone by about 20:01Z.
- **Both committed self-tests passed on the rented machines**, which is
  worth stating because it means the refusal that followed was not a
  broken push or a missing file. The code arrived intact and said so.
- **Then the anchor reproduction failed, on every checkpoint, on both
  runs.** The instrument check re-runs a recorded classifier accuracy and
  demands it come back to within **one episode in 400 (0.0025)**. On the
  rented processor it came back off by as much as **0.0275 — eleven
  episodes in 400, about eleven times the tolerance.** Run 2 failed the
  same way: its part A control reproduces the same unscaled numbers, so
  the standardised read was stopped by the same wall.
- **This is a real difference between machines, not a random one, and
  that was established rather than assumed.** Running the identical
  command twice on the same pod with processor threads pinned to one gave
  **bit-identical output both times** — the rented machine is perfectly
  repeatable. It simply lands on a *different* answer than the laptop,
  which reproduces the same recorded numbers **exactly, to four decimals
  on all five layers.**
- **Why a tiny numerical difference moves the answer so much.** The
  recorded accuracies sit between about 0.46 and 0.55 — chance, for a
  four-way rank read at these positions — and the fit has **more
  directions (448) than episodes (400)**. A boundary drawn through data
  it can separate perfectly is not pinned down by the data; where it ends
  up depends on where the solver stopped, and that depends on the order
  the processor happened to add its numbers in. Apple's arithmetic
  library and the rented machine's add them in different orders. At
  chance level that is enough to move ten held-out episodes.
- **The honest conclusion, and it costs the day's plan:** **these two runs
  cannot be moved off this laptop without changing the instrument**, and
  changing a registered instrument so that it passes on a machine we want
  to use is precisely the move this programme's rules exist to prevent.
  The committed method files were not touched, no tolerance was widened,
  and no result was taken from a machine that failed the check. **The
  instrument did its job.** The two dollars bought the discovery that the
  fitted read is machine-dependent — which is a fact about the read worth
  knowing whatever happens next, and which nothing in the record had
  established before today.
- **Teardown went the way the rows said it would**, which is the one
  process win here. No self-terminate was armed. Each pod's output was
  archived, checksummed on the pod, fetched, and checksummed again
  locally; **both pairs of checksums agreed** (`15086d62e5e8607b445f7008
  63bd8575` for run 1, `b8777a737f0ce5eac0a40b9c0d525c40` for run 2);
  only then were the pods deleted. **Zero pods confirmed after deletion
  by listing them, and the account's spend rate is back to the $0.01/hr
  volume drip.** The 2026-09-19 race did not recur, because the thing that
  caused it was not armed.
- **The refusal records are kept** in `a3-gates/followup-x86-refusal/`,
  because a failed instrument check is evidence about the instrument and
  should not be thrown away just because it produced no sweep numbers.
- **Where the work actually goes.** The laptop's run 1 was never touched
  and is running well — **measured at about 20 tests an hour, faster than
  the 15.3 the estimate assumed** — so it should finish in the evening
  rather than after midnight. **Run 2 is queued to start on the same
  machine the moment run 1 exits**, at four workers, with no thread
  settings changed, because that is the exact configuration under which
  the anchor reproduces here. **Run 2 needs no fresh go:** the follow-up
  brief already ruled it, local and $0, and only the paid venue required
  John's word. The paid venue is off.
- **What this means for finishing both today, stated plainly rather than
  buried:** **it will not happen.** There are 360 tests between the two
  runs and one machine that can legitimately run them at about 20 an
  hour, which is roughly eighteen hours of work. Run 1 should land this
  evening; run 2 will land tomorrow morning. Running them side by side on
  the same laptop would not fix it — the job is limited by memory
  bandwidth, which is why nine workers already measured slower than four
  — and it would put the one clean run at risk to buy nothing.
- **Balance and caps.** $79.7159 → **$77.8119**, measured rather than
  inferred. A3 cumulative ~$44.2 → **~$46.1 of $100**, leaving ~$53.9;
  wider envelope ~$217.6 of $400. Both runs remain $0 from here. **[Corrected 2026-09-21, on the merge of this branch into main: the three figures in this bullet were computed off the pre-RT-147 lineage (~$215.7), which the 2026-09-21 money-citation finding had already superseded on main. Against the corrected ledger (~$225.7 after the checkpoint recovery), A3 cumulative is ~$44.3 -> ~$46.2 of $100, leaving ~$53.8, and the programme running total is ~$227.6 / $400, headroom ~$172.40. The measured balance figures are untouched, and nothing above is altered.]**

===== END OF RECORD 22, part 3 =====
