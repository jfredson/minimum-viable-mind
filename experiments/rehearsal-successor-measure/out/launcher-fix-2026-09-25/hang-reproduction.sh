#!/bin/bash
mkdir -p /Users/john/.claude/jobs/3eb5118f/tmp/repro/root/mvm/src
cd /Users/john/.claude/jobs/3eb5118f/tmp/repro || exit 1
P=$PWD
echo "== the findings' reproduction, rerun $(date -u +%FT%TZ) ($(TZ=America/Los_Angeles date +%F) Pacific)"
s=$(date +%s); bash -c 'cd /tmp && nohup sleep 8 >> /dev/null 2>&1 < /dev/null &' | cat; echo "form as launched (cd && nohup ... &): returned after $(( $(date +%s)-s ))s"
s=$(date +%s); bash -c 'cd /tmp; nohup sleep 8 >> /dev/null 2>&1 < /dev/null &' | cat; echo "control (cd ; nohup ... &): returned after $(( $(date +%s)-s ))s"
echo "== the launcher's watcher-start form, old (line 467 at 4d98cfc) and new, with the watcher replaced by sleep 8"
s=$(date +%s); bash -c "cd $P/root/mvm/src && nohup sleep 8 >> $P/reaper.log 2>&1 < /dev/null &" | cat; echo "OLD  cd … && nohup … &        : returned after $(( $(date +%s)-s ))s"
s=$(date +%s); bash -c "cd $P/root/mvm/src || exit 1; nohup sleep 8 >> $P/reaper.log 2>&1 < /dev/null &" | cat; echo "NEW  cd … || exit 1; nohup … & : returned after $(( $(date +%s)-s ))s"
sleep 1; pgrep -f 'sleep 8' >/dev/null && echo "(a background sleep 8 is still running after the new form returned: it was started, not skipped)"
