#!/bin/bash
# Re-run of the hang reproduction, from a clean environment, nothing rented.
date -u +%FT%TZ
s=$(date +%s); /usr/bin/env -i PATH=/usr/bin:/bin /bin/bash -c 'cd /tmp && nohup sleep 8 >> /dev/null 2>&1 < /dev/null &' | cat
echo "form as launched (cd && nohup ... &): returned after $(( $(date +%s)-s ))s"
s=$(date +%s); /usr/bin/env -i PATH=/usr/bin:/bin /bin/bash -c 'cd /tmp; nohup sleep 8 >> /dev/null 2>&1 < /dev/null &' | cat
echo "control (cd ; nohup ... &): returned after $(( $(date +%s)-s ))s"
