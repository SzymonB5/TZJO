#!/usr/bin/env python3

import sys

def printWithoutZero(numb):
    n = str(numb)
    if int(n) == 0:
        return 0       
        
    fr = 0
    while n[fr] == '0':
        fr += 1
        
    return n[fr:len(n)]

def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'g':
            	return 4, format_string[0:i], str(param), format_string[i+2:len(format_string)]
       
    return 0, format_string, -1, -1    

def my_printf(format_string, param):
    #print(format_string)
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
    	print(format_string)
    elif typeOf == 1:
        print(startFormat, end="")
        print(param.swapcase(), end="")
        print(endFormat)
    elif typeOf == 2:
    	print(startFormat, end="")
    	for i in range(0, min(len(param), number)):
        	print(param[i].swapcase(), end="")
    	print(endFormat)
    elif typeOf == 3:
    	print(startFormat, end="")
    	for i in range(0, number - len(param)):
    		print(" ", end="")
    	
    	for i in range(0, (len(param))):
        	print(param[i].swapcase(), end="")
        	
    	print(endFormat)
    else:
        print(startFormat, end="")
        print(printWithoutZero(str(param)[::-1]), end="")
        print(endFormat)

data=sys.stdin.readlines()

for i in range(0,len(data), 2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    
