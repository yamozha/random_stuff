arecord -D plughw:1,0 -f dat | ssh user@ip aplay -f dat
