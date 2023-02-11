#!/usr/bin/python3

def add(a, b):
    return a + b


def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)

    if l1 < 2:
        if l1 == 0:
            tuple_a[0] = 0
        tuple_a[-1] = 0
    if l2 < 2:
        if l2 == 0:
            tuple_b[0] = 0
        tuple_b[-1] = 0
    return add(tuple_a[0], tuple_b[0]), add(tuple_a[1], tuple_b[1])
