# RunPod support ticket — terminate-after never fired (draft for John to submit)

*2026-08-15. STATUS open item #3. Submit via RunPod console → Support.
Evidence below is from our console reconciliation (compute-ledger.md,
2026-08-12); all times UTC.*

**Subject:** `--terminate-after` never fired on pod 6bplni87uzp3ss — billed
~5.4h ($17.82) past the requested termination time

**Body:**

Pod `6bplni87uzp3ss` (H100 SXM, secure cloud, $3.29/hr) was created on
2026-08-09 at 23:54 UTC via `runpodctl pod create ... --terminate-after
<2026-08-10T23:54Z>` (24 hours after launch).

The terminate-after never executed:

- The pod's audit log shows its **creation as the last recorded event** —
  no termination or delete event from any actor, ever.
- Billing (explorer, UTC days) shows one continuous run: 08-09 $0.254 +
  08-10 $78.96 (exactly 24.00h) + 08-11 $17.821 = **$97.04 = 29.5h at
  $3.29/hr**.
- The pod finally stopped only when the account balance was exhausted,
  ~05:25 UTC on 2026-08-11 — **~5.4 hours past the requested
  terminate-after time**.

The post-deadline portion is **08-11's $17.82**, billed entirely after the
termination we requested at creation should have fired. Since
terminate-after is a RunPod platform feature and the audit log confirms it
never executed, I'm requesting a credit of **$17.82** for the overrun.

Happy to provide the pod create command output or anything else useful.
Account email: jfredson@gmail.com.

---

*Note for us, not the ticket: the 2026-08-08 5090 community row anomaly
(8.47h billed vs ~2.42h pod existence) was previously waived by John and
stays out of this ticket — one clean, provable claim.*

---

## Correspondence log — ticket #45404

**2026-08-16 14:48Z — submitted** (body above, plus a CLI-help quote rebutting
the help bot's doubt that `--terminate-after` exists).

**2026-08-17 09:14Z, followed up 2026-08-19 12:12Z — Runpod (Avtar) asked for
four things:** create-command output, CLI output/logs around 2026-08-10 23:54Z,
`runpodctl version`, and pod status after the deadline passed.

**2026-08-19 — reply drafted** (Gmail draft on the thread). What we could and
could not produce, for the record:

| Asked for | What we have |
|---|---|
| Create command | **Exact**, from git: commit `d7b1283` (2026-08-09 16:54:10 PDT = **23:54:10Z** — the minute the pod was created) is the revision that ran. `runpodctl pod create --name "mvm-a1-pilot-30M" --template-id runpod-torch-v280 --gpu-id "NVIDIA H100 80GB HBM3" --cloud-type "SECURE" --terminate-after "$TERM_AT"`, with `TERM_AT=$(date -u -v+24H +%Y-%m-%dT%H:%M:%SZ)` |
| Create stdout | **Not retained** — echoed to an interactive terminal, never teed to a file. Argued indirectly instead: the script exits if it cannot parse a pod id out of the create JSON, and it did not exit → create returned success with the flag accepted, so the failure is downstream of command acceptance |
| `runpodctl version` | `runpodctl 2.6.1-32e9aec`; Homebrew install date **2026-07-12**, only 2.6.1 in the Cellar → provably the same binary that created the pod |
| Post-deadline pod status | **None of ours** — nobody was at the keyboard, which is the whole point of the ticket. Substituted three Runpod-side records instead |

**Strongest new evidence — Runpod's own email.** `noreply@runpod.io`, subject
"Low Balance", **2026-08-11 05:24:04Z**: *"Your Runpod account balance has been
depleted, and your active Pods have been stopped."* That is Runpod stating,
**5h30m after** the requested termination time, that the pod was still
**active** and was being stopped for non-payment. Independent of any logging of
ours, and it corroborates the audit log (creation is the last event) and the
billing rows (29.5h continuous). Offered to forward it with full headers.

**Correction issued.** The 08-16 submission stated the command included
`--network-volume-id 8xeftvclmv`. It did **not** — that flag entered the
launcher on 2026-08-15 (commit `5818b3d`), six days later; pod
`6bplni87uzp3ss` ran on container disk with no volume attached, which is
exactly why its checkpoint was lost. Corrected proactively in the reply rather
than left for their team to trip over. The reconstructed terminate-after value
is `2026-08-10T23:54:XXZ` (launch + 24h); the earlier `23:54:04Z` was a guess
at the seconds field — their stored value is authoritative.

*Ask unchanged: $17.82 credit for the overrun only.*
