#!/bin/bash
# p105.sh: Yamaha P-105 helpers (USB-MIDI class device, shows as 'Digital Piano', ALSA card, rawmidi hw:N,0,0).
#   ports            list ALSA sequencer ports and raw MIDI
#   record OUT.mid   record what you play (arecordmidi; Ctrl-C stops)
#   play IN.mid      send a file to the keyboard's sounds (aplaymidi; piano must be the output port)
#   monitor          print incoming MIDI events (aseqdump)
P=$(aconnect -l | awk -F"'" '/Digital Piano/ {getline; print}' | head -0); PORT=$(aconnect -l | awk '/client [0-9]+: .Digital Piano/ {gsub(":","",$2); print $2":0"}')
case "$1" in
  ports) lsusb | grep -i yamaha; amidi -l; aconnect -l;;
  record) arecordmidi -p "$PORT" "$2";;
  play) aplaymidi -p "$PORT" "$2";;
  monitor) aseqdump -p "$PORT";;
  *) sed -n 2,6p "$0";;
esac
