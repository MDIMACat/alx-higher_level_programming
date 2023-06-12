#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0],
    if len(tuple_a) >= 2:
        num1, num2 = tuple_a[:2]
    else:
        num1, num2 = 0, 0
    if len(tuple_b) >= 2:
        n1, n2 = tuple_b[:2]
    else:
        n1, n2 = 0, 0

    result = (num1 + n1, num2 + n2)
    return result
