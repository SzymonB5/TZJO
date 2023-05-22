#!/usr/bin/env python3

import sys

def alterFloat1(number):
    if 0 <= number <= 9:
        return chr(ord('a') + number)

def alterFloat2(number):
    return (number + 5) % 10

def separateStr(format_string, param):
    for i in range(0, len(format_string) - 1):
        if format_string[i] == '#':
            if format_string[i + 1] == 'h':
                return 1, format_string[0:i], -1, format_string[i + 2:len(format_string)]
            if format_string[i + 1] == '.':
                if not format_string[i + 2].isnumeric():
                    continue
                else:
                    save = 0
                    for j in range(i + 2, len(format_string)):
                        if not format_string[j].isnumeric():
                            save = j
                            break

                    if format_string[save] != 'h':
                        continue
                    return 2, format_string[0:i], int(format_string[i + 2:save]), format_string[
                                                                                  save + 1:len(format_string)]

    return 0, format_string, -1, -1

def separateFloat(param):
    ctr = 0
    for i in param:
        if i == '.':
            return param[0:ctr], param[ctr + 1:len(param)]
        ctr += 1

    return 1, 1

def my_printf(format_string, param):
    # print(format_string)
    typeOf, startFormat, number, endFormat = separateStr(format_string, param)
    if typeOf == 0:
        print(format_string)
    else:
        string = str(param)
        floatOne, floatTwo = separateFloat(string)
        print(startFormat, end="")

        for i in floatOne:
            print(alterFloat1(floatOne), end="")
        print('.', end="")

        for i in floatTwo:
            print(alterFloat2(floatTwo), end="")

        print(endFormat)


if __name__ == '__main__':
    my_printf("---#.3h---", 1.123456)

# data = sys.stdin.readlines()
#
# for i in range(0, len(data), 2):
#     my_printf(data[i].rstrip(), data[i + 1].rstrip())
#
