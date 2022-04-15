#!/bin/python3
"""
Hackerrank Jumping on the Clouds Solution
@author: Mehmet Baran Munar
"""

# int c[n]: an array of binary integers
# return -> int: the minimum number of jumps required

def jumpingOnClouds(c):
    jump = 0
    i = 0
    n = len(c)
    while i < n:
        jump += 1
        if i + 1 == n - 1 or i + 2 == n - 1:
            break
        elif c[i+2] == 0:
            i += 2
        else:
            i += 1
    return jump
