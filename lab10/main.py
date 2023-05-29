#!/usr/bin/env python3

import sys


def alterNumber(number):
    N = len(str(abs(number)))
    ret = int((number * 2) / N)
    if ret % 2 != 0:
        return str(hex(ret)).replace('0x', '')

    return str(ret)


def my_printf(format_string, param):
    if '#a' not in format_string:
        print(format_string)
        return

    replace = '#a'

    try:
        param = int(param)
    except Exception:
        param = 0

    replace_with = alterNumber(param)

    print(format_string.replace(replace, replace_with))


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
