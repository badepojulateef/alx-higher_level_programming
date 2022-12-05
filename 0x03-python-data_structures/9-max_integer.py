#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        max_val = None
    else:
        max_val = 0
        for i in my_list:
            if len(my_list) == 0:
                max_val = None
                return max_val
            if i > max_val:
                max_val = i
        return max_val
