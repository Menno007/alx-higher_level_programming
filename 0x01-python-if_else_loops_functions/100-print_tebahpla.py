#!/usr/bin/python3
for c in reversed(range(97, 123)):
    print("{:c}".format(c) if c % 2 == 0 else "{:c}".format(c - 32), end='')
"""
    i = 0
    for c in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(c - i)), end="")
        i = 32 if i == 0 else 0
"""
