#!/usr/bin/env python3

import sys

def transform_number(num):

    num_str = str(num)
    new_digits = []
    
    for i in range(len(num_str)):
        digit = int(num_str[i])
        
        digit -= 1
        
        if digit == -1:
            new_digits.append(9)
          
        else:
            new_digits.append(digit)
    
    new_str = ''.join(map(str, new_digits)).zfill(len(num_str))
    
    return new_str




def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'g':
            	return 4, format_string[0:i], transform_number(param), format_string[i+2:len(format_string)]
       
    return 0, format_string, -1, -1    

def my_printf(format_string, param):
    #print(format_string)
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
    	print(format_string)
    else:
        print(startFormat, end="")
        print(printWithoutZero(str(param)[::-1]), end="")
        print(endFormat)

# data=sys.stdin.readlines()

print(transform_number(1234))
print(transform_number(10101))

# for i in range(0,len(data), 2):
  #   my_printf(data[i].rstrip(),data[i+1].rstrip())
    
