#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        print(f"{n} argument{('s' if (n > 1) else '')}:")
        for i in range(n):
            print(f"{i + 1}: {sys.argv[i]}")
