#!/usr/bin/python3

def add(a, b):
    return a + b


def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)
    a = list(tuple_a)
    b = list(tuple_b)
    if l1 < 2:
        if l1 == 0:
            a[0] = 0
        a[1] = 0
    if l2 < 2:
        if l2 == 0:
            b[0] = 0
        b[1] = 0
    return add(a[0], b[0]), add(a[1], b[1])
