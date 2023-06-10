#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        num1, num2 = tuple_a[:2]
    else:
        num1, num2 = 0, 0
    if len(tuple_b) >= 2:
        n1, n2 = tuple_b[:2]
    else:
        n1, n2 = 0, 0
    total1 = num1 + n1
    total2 = num2 + n2
    return (total1, total2)
