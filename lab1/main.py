#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    skip = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'k':
                print(param.swapcase().rstrip('\n'), end = "")
                skip = False
            else:
            	if (skip):
                	print(format_string[idx],end="")
            	skip = True
        else:
            shouldDo=True
    print("")
    
for i in range(10):
	format = input()  # sys.stdin.readlines()
	str = input()
	my_printf(format, str)

