#!/bin/sh
# Claims the two ruling files and the roadmap notes make about other records.
# Run from the repository root, after `git fetch origin`:
#   sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/record_claims.sh

echo "== v4 opening list, item 3"
grep -n "Opening the registration review is John's step" docs/successor-experiment-proposal-2026-10-03-v4.md
echo "== v4 section 11 title"
grep -n "^## 11\." docs/successor-experiment-proposal-2026-10-03-v4.md
echo "== protocol Amendments, the 2026-09-21 task-time quote"
grep -n "We are not working on a" docs/outside-review-protocol.md
echo "== pull requests 76, 79, 85 to 91 on origin/main (subject line, date)"
git log origin/main --format='%h %ad %s' --date=short -80 | grep -E '#(76|79|85|86|87|88|89|90|91)\b'
echo "== pull request 97 (the code freeze): on origin/main? in 655b371?"
git log origin/main --format='%h %ad %s' --date=iso -80 | grep -E '#97\b'
git log -1 --format='655b371 committed %ad' --date=iso 655b371
if git merge-base --is-ancestor 53ae82c 655b371; then echo "freeze merge IS in 655b371"; else echo "freeze merge is NOT in 655b371"; fi
echo "== kill dates and what they bind"
grep -n -A3 'id = "K[12]"' data/roadmap.toml | grep -E 'date|title|note'
grep -n "binds\*\*\|which step the second kill date\|launch of the remaining eight runs\|fresh ruling that names" docs/rulings/2026-09-21-review-verification-and-staged-spending.md
grep -n "kill dates are accepted\|registration committed by 2026-10-18" docs/rulings/2026-09-20-december-result-roadmap.md
echo "== wrap-up and hibernation"
grep -n "wrap_up_start\|hibernation_by" data/roadmap.toml
grep -n "Starts 2026-12-21\|complete by 2027-01-04" docs/december-result-roadmap-2026-09-20.md
echo "== tier 1 counts quoted in W2.1"
grep -n "One fatal finding, four serious" experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md
echo "== John's go on the development runs (W2.4 note)"
git log -1 --format='%h %ad %s' --date=short c9791c9
