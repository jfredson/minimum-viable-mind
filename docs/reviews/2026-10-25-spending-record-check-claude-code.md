# Check of the completed spending record (commit `edadfa8`)

*Saved by the session that wrote the record. The checker's report is below, shortened only where it repeated its own arithmetic; what was done about each finding is at the end.*

**Checker:** a Claude Code session that wrote none of the work, working read-only with no paid calls.
**Commit:** `edadfa8`, on branch `claude/spending-record-complete-2026-10-25`.
**Read:** the commit's five files, the compute ledger, section 6 of the spending review of 2026-09-16, the split-test fixes note of 2026-10-24, the poll's token record, the cost section of the Gate A review index, the battery rehearsal's run record, the far-end repair result, the spending ruling, and all 342 worklog entries for the project.

## Checks

1. **The rented-machine figure: holds.** $150 + $25 + $75 + $120 = $370.00 put in; last balance $65.62; spent $304.38. No top-up after 2026-08-16 in the ledger, `STATUS.md`, `STATUS-archive.md` or the worklog. RunPod's exports put spend to 2026-09-16 at $258.18, so the balance should have read $111.82; the ledger read $111.74. The rows after 2026-09-16 come to $36.08, leaving $10.12 for storage, as stated.
2. **The API rows: hold.** The poll recomputed from its token record: Gemini $0.14, GPT $0.81 (OpenAI's output count already includes reasoning), Claude Opus $0.72. Gate A's outside review: $0.156 and $0.884, matching the index; the overseer's $1 line is sourced in worklog entry "Gate A on the two-sided question text…" (`155a7dc2`). The battery rehearsal $20.89 to $40.49 and the far-end repair $1.12 match their files. Stage 3's Gemini $49.77 and Anthropic $20.38 + $20.18 match the cost-finding entry (`558a695a`) and John's ruling of 2026-08-30 (`a3834db7`).
3. **Completeness: holds, with two gaps** (findings 1 and 2). Every script that calls a paid model is covered or makes no network call; Stage 3's later amendment parts were never run. The programme review of 2026-09-20 went through John's apps and rightly has no row, but is not named. No other vendor carries a recorded charge (Hugging Face, Cloudflare, the subdomain).
4. **The total, the "How firm" labels and the "go" column: hold, with one overstatement** (finding 3). Recomputed total $419.43 to $439.03. Every quoted go checked is on record, including the split test's "up to $2" in worklog entry "Go for RunPod, before the spend…" (`4f914dc1`).
5. **"Why the total is higher than the range": holds.** The new low end adds about $84 to the old one, against an actual gap of $84.49.
6. **Where the figure appears: holds, with one stale place** (finding 5). `python3 scripts/export_site.py --check` passes.
7. **Plain language: mostly holds** (finding 6).

## Findings

1. Experiment 1's outside design review (`red_team.py` sending the design to Gemini, `defend.py` answering through Anthropic) is missing from "Untraced".
2. The $2.75 of Google's August bill outside the Gemini arm is left out, while July's $2.86 is listed.
3. The go for the lost 30M pilot is overstated: about $17.82 was spent past its safety cut-off, which no go covered.
4. The record silently contradicts the 2026-09-16 review's rebuild of John's figure, which left out the Anthropic top-ups; say it is superseded.
5. `README.md` line 51 still says "About $230.94 of the $450 ceiling is spent".
6. Shorthand a stranger cannot read ("30M pilot", "10M", "seeds 1 and 2, one wave", "Gate A tier 2", "community cloud", "Claude arm"), and worklog ids labelled only "(before)" or "(after)".
7. Minor: "Everything else in the total was paid by card or prepaid balance" goes further than the record.

**A note for John.** The two recorded Anthropic top-ups were about $20 each, so the third was probably about $20 too, which would make the true total about $440 to $460. The record is right to leave it untraced until it is read on Anthropic's console.

**My recomputed total:** $419.43 to $439.03; the high end is probably about $2 too high, because Google's $20.00 prepaid balance capped the second start's Gemini spend.

**Overall verdict: passes with minor fixes.**

---

## What was done (2026-10-25, by the session that wrote the record)

- Findings 1, 2, 3, 4 and 7: applied as suggested; the programme review of 2026-09-20 is named among the reviews that cost nothing per call.
- Finding 6: the shorthand in the new tables is spelled out and the three worklog ids carry plain labels. The kept paragraphs of 2026-10-18 are otherwise unchanged.
- Finding 5: **not changed here.** `README.md` line 51 is one long line that pull request 226 (closing RT-302) also edits, so changing it here would make the two pull requests conflict. It is left for whichever merges second, or a one-line follow-up.
- The total is unchanged by the fixes.
