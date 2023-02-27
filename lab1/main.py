#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'k':
                print(param.swapcase().rstrip('\n'), end = "")
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

format = input()  # sys.stdin.readlines()
str = input()

my_printf(format, str)

