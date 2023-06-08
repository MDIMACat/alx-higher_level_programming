#!/usr/bin/python3
if __name__ == "__main__":
    """print the total sum, subtraction , mulitplications
    and  division of a and b"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    total = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, total))
    total = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, total))
    total = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, total))
    total = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, total))
