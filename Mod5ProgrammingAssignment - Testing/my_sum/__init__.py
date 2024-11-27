"""
Module 5 Programming Assignment - Testing
Author: Landon Ernst
File: __init__.py
"""

#Create a new function called "sum()"; It takes an iterable and adds the values
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

