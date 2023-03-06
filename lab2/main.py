#!/usr/bin/env python3

import sys


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
       
    return 0, format_string, -1, -1    

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(format_string,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

# data=sys.stdin.readlines()

# for i in range(0,len(data),2):
  #  my_printf(data[i].rstrip(),data[i+1].rstrip())
  
print(separateStr("test", "ignore"))
print(separateStr("AA#kAA", "ignore"))
print(separateStr("#.05k", "ignore"))
print(separateStr("#", "ignore"))
print(separateStr("test", "ignore"))

