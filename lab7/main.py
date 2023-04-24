#!/usr/bin/env python3

import sys


def alterTo(numb):
    if numb.isnumeric():
        return numb
    return chr(ord(numb) + 6)


def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'j':
                return 1, format_string[0:i], format_string[i:i + 2], format_string[i + 2: len(format_string)]

    return 0, format_string, -1, -1


def my_printf(format_string, param):
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
        print(format_string)
    else:
        print(startFormat, end="")
        print("0x", end="")
        for j in str(hex(param)[2:]):
            print(alterTo(j), end="")

        print(endFormat)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
