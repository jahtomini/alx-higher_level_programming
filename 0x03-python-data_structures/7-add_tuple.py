#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a[0] is not None and tuple_a[1] is not None and tuple_b[0] is not None and tuple_b[1] is not None:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
