#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(n, ('s' if (n > 1) else '')))
        for i in range(1, n + 1):
            print("{}: {}".format(i, sys.argv[i]))
