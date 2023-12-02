#!/usr/bin/python3
def no_c(my_string):
    copy_string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            copy_string = copy_string + x
    return (copy_string)
