#!/usr/bin/python3
a = 1
b = 2
if __name__ == "__main__":
    add_0 = __import__("add_0").add
    print("{} + {} = {}".format(a, b, add_0(a, b)))
