#!/bin/bash
cd /Users/john/Code/minimum-viable-mind/.claude/worktrees/agent-a8f4a188ded7c4c33
while read r; do
  git grep -lE "RT-27[4-9]" "$r" -- '*.md' '*.toml' 2>/dev/null | sed "s|^|$r |"
done < /private/tmp/claude-501/-Users-john-Code-minimum-viable-mind/f29d71f5-3807-44d3-bb86-b4053eca7feb/scratchpad/refs.txt
