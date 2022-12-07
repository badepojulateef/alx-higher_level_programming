#!/usr/bin/python3

def common_elements(set_1, set_2):
    c_set = set_1 & set_2
    if c_set:
        return c_set
