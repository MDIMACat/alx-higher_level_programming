#!/usr/bin/python3
if __name__ == "__main__":
    
    from add_0 import add
    a = 1
    b = 2
    total = 0
    total += add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, total))
