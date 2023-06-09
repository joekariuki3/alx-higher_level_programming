#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]

    # Pad tuples with 0 if they have less than 2 elements
    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))
    answer = (a[0] + b[0], a[1] + b[1])
    return answer
