#!/usr/bin/python3
import sys


def print_args():
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("Number of argument: {}".format(num_args))
    else:
        print("Number of arguments: {}".format(num_args))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_args()
