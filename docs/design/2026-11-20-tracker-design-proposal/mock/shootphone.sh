#!/bin/zsh
# usage: shootphone.sh page.html "query" out.png height
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$2")
"$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=430,$4 --virtual-time-budget=3000 --screenshot="$3" "file://$PWD/phone.html?p=$1&q=$q&h=$4" >/dev/null 2>&1
