#!/bin/bash
cd /Users/john/Code/minimum-viable-mind/.claude/worktrees/agent-a8f4a188ded7c4c33
for r in check-serious-findings-238-239-251 ruled-code-changes-2026-10-09 check-v5-open-items-rulings v5-open-items-rulings-2026-10-08 outside-perspective-poll land-cited-branches-2026-10-08 drop-with-claude-footer-2026-10-08; do echo "== $r"; git grep -nE "RT-27[4-9]" origin/$r -- '*.md' '*.toml' | grep -v "ledger-rows-findings.md:31\|ledger-rows-method.md:4[78]\|filtered-battery-check.md:23\|v5-wording-check-claude-code.md:175" | cut -c1-260; done
