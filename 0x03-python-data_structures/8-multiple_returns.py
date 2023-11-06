#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        frst = sentence[0]
    else:
        frst = None
    return (len(sentence), frst)
