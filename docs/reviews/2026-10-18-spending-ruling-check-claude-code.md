**Verdict: PASS WITH CONDITIONS.** All six items asked about hold. Two figures lack a source a reader can open, and supplying them is the two changes.

# Check of pull request 196: John's spending ruling of 2026-10-18 (2026-10-18)

*This is a pairing-rule check (`docs/outside-review-protocol.md`) by a Claude
Code session that wrote none of pull request 196 or of pull request 195,
which 196 corrects. The work was done in its own worktree
(`.claude/worktrees/check-196`), on branch `check-spending-ruling`, cut from
`spending-ruling-2026-10-18` at `19be2db`. $0. Nothing under check was
edited. Written under the workspace plain-language rule.*

**To re-run, from the worktree root:**

    sh docs/reviews/2026-10-18-spending-ruling-check-claude-code-scripts/check_196.sh

The full output is beside the script as `check_196_output.txt`.

## The changes owed before merge

1. **`docs/spending-record.md`, second row of the running total: name the
   documents.** The row says "John's figure of about $281 to $300 of true
   spend across every vendor on 2026-08-30, when the ledger read about
   $181". It names no file, and the record's own header promises that "a
   figure here cites its source". Both sources exist (item 5 below):
   - the $281 to $300 is in John's binding rulings of 2026-08-30, quoted at
     the top of `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`;
   - the $181 is the compute ledger's 2026-08-17 row, "~$181.4 / $400 (A2)".
     That is the last ledger row before 2026-09-14.
2. **`explainer.md`: give the total across every vendor a source that holds
   it.** The sentence "roughly $335 to $360 so far" cites "`STATUS.md`, entry
   of 2026-10-12; `compute-ledger.md`, the 2026-10-04 and 2026-10-09 rows".
   - Neither status file has an entry dated 2026-10-12.
   - The ledger holds only the $230.94 (it contains no "335").
   - The citation was there before pull request 195 and supported only the
     $230.94. Pull request 195 then attached the new total to it, and pull
     request 196 keeps that.

   Cite `docs/spending-record.md` (or the 2026-10-18 evening status entry)
   for the total, and either drop or correct the 2026-10-12 entry, which does
   not exist.

## What was opened

**From pull request 196:**
- the pull request's description and its one commit, `19be2db`;
- the full diff against the main line (8 files, including `explainer.md`
  and `data/headline.json`, which the brief did not list);
- `scripts/export_site.py`: `headline()` and `main()`;
- the ruling file `docs/rulings/2026-10-18-spending-ruling.md`;
- `docs/spending-record.md`.

**From the history and the sources:**
- `data/project.toml` at three points: before pull request 195 (`af59d73^1`),
  after it (`af59d73`), and now;
- the compute ledger's rows of 2026-08-17 to 2026-09-14 and 2026-10-09;
- the opening rulings line of `amendment-a3.md`;
- "What it cost" in `docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`;
- the list of status-entry headings in `STATUS.md` and `STATUS-archive.md`;
- the TimeAssembler worklog's Minimum Viable Mind entries for 2026-10-18,
  including rows `4110fb03` and `255fff69` by id through the v1 API.

**Not opened:**
- the poll's method file, beyond checking that it exists, since its row
  carries no figure;
- the vendors' consoles.

## The six items

**1. The headline uses `[spend].headline_words` when set, and the old
wording otherwise. Holds. MEASURED.**
- With the field present (the worktree): exit 0, and the headline reads
  "about $335 to $360 spent in total across every vendor so far, each new
  spend under its own go from John".
- With the line deleted (a copy in a temporary folder; 0 such lines left):
  exit 0, and the headline reads "about $230.94 of the $450 ceiling spent".
  The check also warns that `headline.json` lags. That is expected, since
  the committed file holds the new words.
- The worktree run gives no lag warning, so the committed `data/headline.json`
  is current.

The code also falls back when the field is empty or only spaces (ARGUED,
from `isinstance(words, str) and words.strip()`).

**2. `cd site && npm run check` passes. Holds. MEASURED: exit 0.** That
command runs the same `export_site.py --check`.

**3. The $450 line is $230.94 against 450 again, and its note keeps the old
note's text after the marker. Holds. MEASURED.**

| | Before pull request 195 | After 195 | Now |
|---|---|---|---|
| cap | 450 | 450 | 450 |
| spent | 230.94 | 335 | 230.94 |

The marker "As written before 2026-10-18:" appears once. The text after it
is the note from before pull request 195, character for character (1,965
characters).

The line's name is not quite restored. It went from "MVM-0a registered
design envelope (Amendment A2)" to the same words plus ": rented machines
from 2026-08-07". That addition is accurate (ARGUED: the ledger opened on
2026-08-07 and holds only rented machines), but the description does not
mention it.

**4. The STATUS.md correction quotes John's words exactly as the ruling file
does. Holds. MEASURED.** The two quotations, with whitespace collapsed, are
identical: "I'm not so worried about the $450 ceiling, I just want to make
sure we are keeping track of any new spending. Any new spending needs to get
ruled on rather than counted against some long term cap." The correction
also carries a dated note saying that the paragraph first said otherwise.

**5. `docs/spending-record.md`: every figure cited, and the sources say what
the rows say. Holds, except one row's citation (change 1). MEASURED.**

The figures against their sources:
- **The ledger's running total.** $230.94 is in the ledger's last row
  (2026-10-09): "after this run: programme about **$230.94 of $450**".
- **The Gate A tier 2 cost.** "about $1.04 at most" is in the Gate A index's
  "What it cost" table, word for word.
- **The rehearsal's worklog rows.** Both rows exist, both dated 2026-10-18.
  Their bodies are empty, and the figures are in their titles:
  - row `4110fb03` (the "before" row): John's go "Go up to $50", "ceilings
    $27 for entry 1 and $23 for entry 2 (estimate $18.26 to $37.86)";
  - row `255fff69` (the "after" row): "about $2.88 to $7.13 spent by
    estimate".

  These match the record's row exactly.
- **John's $281 to $300 and the ledger's $181.** Both sources exist and say
  what the row says. The row just does not name them (change 1).
- **The total.** 230.94 + (100 to 119) + (1.04 + 2.88 to 7.13) comes to
  334.86 to 358.11. That fits "roughly $335 to $360" and "at least about $4
  to $8".

**6. `compute-ledger.md` gains only rule 6. Holds. MEASURED.** The diff
against `af59d73` is 9 lines added and 0 removed: rule 6 and one blank line.

**Own check (item 7 in the script): the explainer's citation. MEASURED.**
This is what gives change 2:
- entries headed 2026-10-12: 0 in `STATUS.md`, 0 in `STATUS-archive.md`;
- "$335 to $360" in `explainer.md`: 0 before pull request 195, 1 after it,
  1 now;
- "entry of 2026-10-12" in `explainer.md` before pull request 195: 1;
- "335" in the compute ledger: 0.

## Notes, not conditions

- **The export script's fallback.** It still says "about $X of the $450
  ceiling spent", and `headline()`'s docstring still describes the headline
  as the ceiling line. If `headline_words` is ever removed, the site would
  call the $450 a ceiling again, against the ruling. Worth rewording when the
  script is next touched.
- **Outside this repository.** The TimeAssembler worklog still holds the
  2026-10-18 decision entry "John's four answers of 2026-10-18 about 20:00
  Pacific … count every vendor against the $450 ceiling" (`ee7b7dc1`,
  authorship mixed). Later sessions read decision entries as binding, so
  that entry carries the same wrong relay that this pull request corrects.
  The new decision entry, John's spending ruling (`641d2844`, authorship
  john), sits beside it, but the old one is not marked as superseded.
