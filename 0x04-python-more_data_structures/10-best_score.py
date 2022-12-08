#!/usr/bin/python3

def best_score(a_dictionary):
    x = 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > x:
                x = v
                d = [i for i in a_dictionary if a_dictionary[i] == x]
    else:
        return (None)
    return (d[0])
