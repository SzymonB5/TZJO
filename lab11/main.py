#!/usr/bin/env python3

import sys

helpString = "abcdefghij"


def set_char_at_index(string, index, char):
    return string[:index] + char + string[index + 1:]


def separateStr(format_string):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'b':
                return 1, format_string[0:i], format_string[i:i + 2], format_string[i + 2: len(format_string)]

    return 0, format_string, -1, -1


def my_printf(format_string, param):
    typeOf, startFormat, number, endFormat = separateStr(format_string)
    if typeOf == 0:
        print(format_string)
    else:
        print(startFormat, end="")
        binaryParam = bin(int(param))[2:]
        binaryParam = binaryParam[::-1]

        counter = 0
        for i in range(len(binaryParam)):
            if binaryParam[i] == '1':
                binaryParam = set_char_at_index(binaryParam, i, helpString[counter])
            counter += 1
            if counter == 10:
                counter = 0

        print(binaryParam[::-1], end="")

        print(endFormat)


if __name__ == '__main__':
    my_printf("--#b==", 123123123)

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
