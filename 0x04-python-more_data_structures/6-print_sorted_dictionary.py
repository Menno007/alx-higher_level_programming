#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary)
    for key in dic:
        print("{}: {}".format(key, a_dictionary[key]))
