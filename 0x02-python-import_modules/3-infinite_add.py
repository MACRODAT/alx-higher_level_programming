#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    s = 0
    for d in sys.argv:
        s += int(d)
    print(f"{s}")
