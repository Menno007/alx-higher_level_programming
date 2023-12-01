#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    args_str = "argument" if num_args == 1 else "arguments"

    print("{} {}:".format(num_args, args_str))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
