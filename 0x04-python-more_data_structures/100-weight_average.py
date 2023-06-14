#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    pairTotal = 0
    toDivWith = 0
    for pair in my_list:
        pairTotal = pairTotal + (pair[0] * pair[1])
        toDivWith = toDivWith + pair[1]
    return pairTotal / toDivWith
