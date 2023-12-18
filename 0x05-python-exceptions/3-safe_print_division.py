#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Inside result: {:f}".format(result))
        print("{a} / {b} = None")
    finally:
        print("Inside result: {:f}".format(result))
        print("{a} / {b} = {:f}".format(result))
