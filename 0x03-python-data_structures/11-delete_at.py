#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        return new_list[:idx] + new_list[idx + 1:]
