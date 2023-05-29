#!/usr/bin/env python3

import sys


def count_digits(number):
    if number == 0:
        return 1

    count = 0
    number = abs(number)

    while number > 0:
        number //= 10
        count += 1

    return count


def alter_param(number):
    N = count_digits(number)
    F = int((number * 2) / N)
    if F % 2:
        F = str(hex(F)).replace('0x', '')

    return F


def my_printf(format_string, param):
    shouldDo = True
    for idx in range(0, len(format_string) - 1):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'a':
                print(alter_param(param), end="")
                shouldDo = False
            else:
                print(format_string[idx], end="")
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
