#!/bin/sh

if [ x"${DESKTOP_SESSION##*/}" = x"openbox" ]; then 
   # No widgets enabled!
   exit 0
fi
if [ x"${DESKTOP_SESSION##*/}" = x"fluxbox" ]; then 
   sleep 20s
   killall conky
   cd "$HOME/.conky/MX-Cowon"
   conky -c "$HOME/.conky/MX-Cowon/MX-Cowon_more_sys_small" &
   exit 0
fi
