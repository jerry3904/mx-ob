#!/bin/sh

if [ x"${DESKTOP_SESSION##*/}" = x"openbox" ]; then 
   # No widgets enabled!
   exit 0
fi
