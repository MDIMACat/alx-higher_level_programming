#!/usr/bin/python3
if __name__ == "__main__":
    """Prints"""
    from calculator_1 import add, sub, div, mul
    import sys

    num = len(sys.argv)
    if (num != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    total = 0
    operators = ['+', '-', '*', '/']
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (operator == '+'):
        total = add(a, b)
        print("{} + {} = {}".format(a, b, total))
    if (operator == '-'):
        total = sub(a, b)
        print("{} - {} = {}".format(a, b, total))
    if (operator == '*'):
        total = mul(a, b)
        print("{} * {} = {}".format(a, b, total))
    if (operator == '/'):
        total = div(a, b)
        print("{} / {} = {}".format(a, b, total))
