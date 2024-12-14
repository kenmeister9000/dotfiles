#!/bin/sh 
export DBUS_SESSION_BUS_ADDRESS=$(< /tmp/dbus.env)
export DISPLAY=:0  
batstage="$(acpi -b | grep -c 'Charging')"
batlevel="$(acpi -b | grep -P -o '[0-9]+(?=%)')"
batfull="$(acpi -b | grep -c 'Full')"
if [[ "$batstage" == 1 ]]; then
dunstify -a "battery" -r 10004 -u normal -i ac-adapter-symbolic -h int:value:"$batlevel" "Battery Charging: ${batlevel}%"
elif [[ "$batfull" == 1 ]]; then
dunstify -a "battery" -r 10004 -u low -i battery-symbolic -h int:value:"$batlevel" "Battery Full: ${batlevel}%"
else
dunstify -a "battery" -r 10004 -u normal -i battery-symbolic -h int:value:"$batlevel" "Battery Discharging: ${batlevel}%"
fi
