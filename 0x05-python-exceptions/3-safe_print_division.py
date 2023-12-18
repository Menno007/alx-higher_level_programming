#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        return result
    except (ZeroDivisionError, ValueError, TypeError):
        print("Inside result: {}".format(None))
    finally:
        if 'result' in locals():
            print("Inside result: {}".format(result))
