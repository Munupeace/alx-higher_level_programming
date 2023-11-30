#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        if ord(iterator) >= 97  and ord(iterator) <= 122:
            temp = chr(ord(iterator) - 32)
            print("{}".format(temp), end='')
        print()
