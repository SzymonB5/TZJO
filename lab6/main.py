#!/usr/bin/env python3

import sys


def alterTo(numb):
    return (numb * 9 + 1) % 10


def separateStr(format_string):
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

                    if format_string[save] != 'g':
                        continue
                    return 1, format_string[0:i], int(format_string[i + 2: save]), \
                        format_string[save + 1:len(format_string)]

    return 0, format_string, "", ""


def my_printf(format_string, param):
    typeOf, startFormat, number, endFormat = separateStr(format_string)
    if typeOf == 0:
        print(format_string)
    else:
        print(startFormat, end="")
        for i in range(int(number) - len(str(param))):
            print("0", end="")

        if param == '1':
            print("0", end="")
        else:
            rem0 = 1
            for j in str(param):
                x = alterTo(int(j))
                if x == 0 and rem0 == 1:
                    pass
                elif x != 0:
                    rem0 = 0
                    print(x, end="")

        print(endFormat)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
