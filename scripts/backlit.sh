#!/bin/sh  
export DBUS_SESSION_BUS_ADDRESS=$(< /tmp/dbus.env)
export DISPLAY=:0
keybright="$(brightnessctl --device='tpacpi::kbd_backlight' get)"
if [[ $keybright == 1 ]]; then 
dunstify -a "kbdbrightness" -r 10009 -u normal -i keyboard-brightness-symbolic "Keyboard Light: Stage One" 
elif [[ $keybright == 2 ]]; then 
dunstify -a "kbdbrightness" -r 10009 -u normal -i keyboard-brightness-symbolic "Keyboard Light: Stage 2" 
else 
dunstify -a "kdbbrightness" -r 10009 -u normal -i keyboard-brightness-symbolic "Keyboard Light: Off"  
fi
