#!/bin/sh
# Re-run the check of pull request 190 from the worktree root. Needs origin/main fetched. $0, no model called.
S=docs/reviews/2026-10-18-paper-reserved-places-check-scripts
python3 -I $S/ruled_wording.py  > $S/ruled_wording.out.txt
python3 -I $S/spelling_only.py  > $S/spelling_only.out.txt
git diff --stat origin/main HEAD > $S/files_changed.out.txt
grep -n -F 'under $20' drafts/paper-removal-test-nature-draft.md > $S/twenty_dollars.out.txt
grep -n -F '$10–20' drafts/paper-removal-test-nature-draft.md >> $S/twenty_dollars.out.txt
grep -n 'programme' drafts/paper-removal-test-nature-draft.md >> $S/twenty_dollars.out.txt
