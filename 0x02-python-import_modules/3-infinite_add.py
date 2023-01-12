#!/usr/bin/python3

if __name__ == "__main__":
    """print the addition of all arguments."""

    import sys

    toatal = 0
    for i  in range(len(sys.argv) - 1):
        toatal += int(sys.argv[i + 1])
        print("{}".format(total))
