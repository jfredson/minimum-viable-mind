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
