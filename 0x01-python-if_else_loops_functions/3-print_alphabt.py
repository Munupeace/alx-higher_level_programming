#!/usr/bin/python3
for value in range(ord('a'), ord('z')):
    if value in (ord('q'), ord('e')):
        continue
    print("{}".format(chr(value)), end='')
