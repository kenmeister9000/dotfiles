#!/bin/bash 
volume="$(amixer -c 0 get Master | tail -1 | awk '{print $4}' | sed 's/[^0-9]*//g')" 
mute="$(amixer -c 0 get Master | tail -1 | awk '{print $6}' | sed 's/[^a-z]*//g')" 

if [[ $volume == 0 || "$mute" == "off" ]]; then 
dunstify -a "soundchange" -r 10003 -u low -i audio-volume-muted "Sound Muted" 
else 
dunstify -a "soundchange" -r 10003 -u low -i audio-volume-high -h int:value:"$volume" "Volume: ${volume}%"  
fi 
