#!/usr/bin/env python3

import sys

def printWithoutZero(numb):
    if int(numb) == 0:
        return 0
        
        
    fr = 0
    while numb[fr] == '0':
        fr += 1
        
    return numb[fr:len(numb)]

def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'k': 
                return 1, format_string[0:i], -1, format_string[i + 2:len(format_string)]
                
            if format_string[i + 1] == '.':
            	if format_string[i + 2].isnumeric() == False:
            	    continue
            	else:
            	    save = 0
            	    for j in range(i + 2, len(format_string)):
            	        if format_string[j].isnumeric() == False:
            	            save = j
            	            break
            	            
            	    if format_string[save] != 'k':
            	        continue
            	    return 2, format_string[0:i], int(format_string[i + 2:save]), format_string[save + 1:len(format_string)]
            	    
            if format_string[i + 1].isnumeric():
                save = 0
                for j in range(i + 2, len(format_string)):
            	        if format_string[j].isnumeric() == False:
            	            save = j
            	            break
            	            
                if format_string[save] != 'k':
                    continue
            
                return 3, format_string[0:i], int(format_string[i + 1:save]), format_string[save + 1:len(format_string)]
            if format_string[i + 1] == 'g':
            	return 4, format_string[0:i], str(param)[::-1], format_string[i+2:len(format_string)]
       
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
        print(printWithoutZero(param), end="")
        print(endFormat)

# data=sys.stdin.readlines()

print(separateStr("---#g---", 213700))
print(printWithoutZero("002"))
# for i in range(0,len(data), 2):
  # my_printf(data[i].rstrip(),data[i+1].rstrip())
    
