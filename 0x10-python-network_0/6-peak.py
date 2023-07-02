#!/usr/bin/python3
# A function that finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak
    Returns: peak of list_of_integers
    """
    size = len(list_of_integers)
    mid_idx = size
    mid_val = size // 2

    if size == 0:
        return None

    while True:
        mid_idx = mid_idx // 2
        if (mid_val < size - 1 and
                list_of_integers[mid_val] < list_of_integers[mid_val + 1]):
            if mid_idx // 2:
                mid_idx = 2
            mid_val = mid_val + mid_idx // 2
        elif mid_idx > 0 and list_of_integers[mid_val] \
                < list_of_integers[mid_val - 1]:
            if mid_idx // 2 == 0:
                mid_idx = 2
            mid_val = mid_val - mid_idx // 2
        else:
            return list_of_integers[mid_val]
