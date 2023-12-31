#!/usr/bin/python3

if __name__ == "__main__":
    """wefwe."""
    from calculator_1 import add, sub, mul, div

    import sys

    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    _perator_ = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(_perator_.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print(f"{a} {sys.argv[2]} {b} = {_perator_[sys.argv[2]](a, b)}")
