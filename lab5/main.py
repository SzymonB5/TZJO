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
            
            if format_string[i + 1].isnumeric():
                save = 0
                for j in range(i + 2, len(format_string)):
            	        if format_string[j].isnumeric() == False:
            	            save = j
            	            break
            	            
                if format_string[save] != 'g':
                    continue
            
                return 3, format_string[0:i], int(format_string[i + 1:save]), format_string[save + 1:len(format_string)]
       
    return 0, format_string, -1, -1
    

def my_printf(format_string, param):
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
    	print(format_string)
    else:
        print(startFormat, end="")
        
        for i in range(0, number - len(param)):
            print(" ", end="")
        
        print(transform_number(param), end="")
        
        print(endFormat)

# print(separateStr("-#5g-", 222))


data=sys.stdin.readlines()

for i in range(0,len(data), 2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    
