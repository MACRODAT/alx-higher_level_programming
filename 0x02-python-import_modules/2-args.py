if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n == 0:
        print("0 arguments.")
    else:
        print(f"{n} argument{('s' if (n > 1) else '')}:")
        for i in range(n):
            print(f"{i}: {sys.argv[i]}")
