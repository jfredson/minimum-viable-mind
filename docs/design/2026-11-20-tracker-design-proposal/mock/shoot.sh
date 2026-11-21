#!/bin/zsh
# usage: shoot.sh page.html "query" out.png width height
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=${6:-1} --window-size=$4,$5 --screenshot="$3" "file://$PWD/$1?$2" >/dev/null 2>&1
