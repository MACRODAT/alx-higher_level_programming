#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        print("{:d} argument{:s}:".format(n, ('s' if (n > 1) else '')))
        for i in range(1, n + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
