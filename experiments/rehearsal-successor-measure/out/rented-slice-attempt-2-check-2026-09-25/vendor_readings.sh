#!/bin/sh
# Read-only vendor readings for the check of the rented slice's second attempt
# (experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rented-slice-attempt-2-check-claude-worktree.md).
# Every command here lists or reads; none creates, deletes or changes anything.
# The account id and email are removed from the output; nothing else is changed.
redact() { sed -E 's/"id": "user_[^"]*"/"id": "user_<redacted>"/; s/"email": "[^"]*"/"email": "<redacted>"/'; }
date -u +%Y-%m-%dT%H:%M:%SZ
echo '$ runpodctl user'
runpodctl user | redact
echo '$ runpodctl pod list'
runpodctl pod list
echo '$ runpodctl billing pods --pod-id alpua1c0w6jonx --bucket-size hour --grouping podId --start-time 2026-09-26T00:00:00Z'
runpodctl billing pods --pod-id alpua1c0w6jonx --bucket-size hour --grouping podId --start-time 2026-09-26T00:00:00Z
echo '$ runpodctl billing pods --bucket-size hour --grouping podId --start-time 2026-09-25T20:00:00Z'
runpodctl billing pods --bucket-size hour --grouping podId --start-time 2026-09-25T20:00:00Z
echo '$ runpodctl billing network-volume --bucket-size hour --start-time 2026-09-25T20:00:00Z'
runpodctl billing network-volume --bucket-size hour --start-time 2026-09-25T20:00:00Z
