#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if value in (ord('q'), ord('e')):
        continue
    print("{}".format(chr(value)), end='')
