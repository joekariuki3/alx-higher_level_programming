#!/usr/bin/python3
# fuction to find a peak in a list of unsorted integers

def find_peak(list_of_integers):
    """
    function to find peak in the list
    list is unsorted
    """
    if len(list_of_integers) == 0:
        return None
    lt = list_of_integers
    firstPeak = 0
    secondPeak = 0
    i = 0
    j = 1
    while j < len(lt):
        if lt[i] > lt[j] or lt[i] == lt[j]:
            firstPeak = lt[i]
            while j < len(lt):
                if lt[i] > lt[j] and lt[i] > firstPeak:
                    secondPeak = lt[i]
                    break
                i = i + 1
                j = j + 1
            break
        i = i + 1
        j = j + 1
    if firstPeak > secondPeak:
        return firstPeak
    return secondPeak
