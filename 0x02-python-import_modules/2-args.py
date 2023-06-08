#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of arguements and list of arguments"""
    import sys

    n = len(sys.argv) - 1

    if (n == 1):
        print("1 argument:")
    elif (n == 0):
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
