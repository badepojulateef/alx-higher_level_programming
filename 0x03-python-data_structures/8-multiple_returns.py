#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ''
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[:1]
    return (len(sentence), first_char)
