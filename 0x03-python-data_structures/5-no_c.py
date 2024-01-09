#!/usr/bin/env python3
def no_c(my_string):
    newstring_array = []
    for i in my_string:
        newstring_array.append(i)

    for i in range(len(newstring_array)):
        if newstring_array[i] == 'c' or newstring_array[i] == 'C':
            newstring_array[i] = ''

    return "".join(newstring_array)
