#!/usr/bin/python3

"""
A script to load the security tokens from a given file
"""

def load_tokens(filename):
    """
    Return a dictionary containing the tokens
    """

    tokens={}
    with open(filename) as fileobject:
        for line in fileobject.readlines():
            category,token=line.strip().split("=")
            tokens[category]=token
    return tokens
