#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        return result
    except (ZeroDivisionError, ValueError, TypeError):
        print("Inside result: {:d}".format(result))
    finally:
        print("Inside result: {:d}".format(result))
