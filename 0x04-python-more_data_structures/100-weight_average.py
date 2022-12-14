#!/usr/bin/python3

def weight_average(my_list=[]):
    x = 0
    y = 0
    if my_list and len(my_list) != 0:
        for tuple in my_list:
            x += (tuple[0] * tuple[1])
            y += tuple[1]
        return (x/y)
    return 0
