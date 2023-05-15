#!/usr/bin/env python3

import sys


def alterTo(numb):
    if numb.isnumeric():
        if numb == '0':
            return 'o'
        return numb
    return chr(ord(numb) + 6)


def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':

            if format_string[i + 1] == '.':
                if len(format_string) == i + 2:
                    continue
                if not format_string[i + 2].isnumeric():
                    continue
                else:
                    save = 0
                    for j in range(i + 2, len(format_string)):
                        if not format_string[j].isnumeric():
                            save = j
                            break

                    if format_string[save] != 'j':
                        continue
                    return 1, format_string[0:i], int(format_string[i + 2: save]), \
                        format_string[save + 1:len(format_string)]

    return 0, format_string, -1, -1


def my_printf(format_string, param):
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
        print(format_string)
    else:
        print(startFormat, end="")
        for i in range(int(number) - len(str(param)) + 2):
            print("0", end="")
        # par = hex(param)
        par = str(param)
        par = par[2:]
        for j in par:
            print(alterTo(j), end="")

        print(endFormat)

# my_printf("#.9j", 0x123456)
data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
