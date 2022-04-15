#!/bin/python3
"""
Hackerrank Left-Rotation Solution
@author: Mehmet Baran Munar
"""
# int a[n]: the array to rotate
# int d: the number of rotations
# returns -> int a'[n]: the rotated array

def rotLeft(a, d):
    # length of the list.
    n = len(a)
    
    # indexes of the list.
    c = [i for i in range(n)]
    newList = list()
    for x in range(n):
        if c[x]+d>=n:
            c[x]=(c[x]+d)%n
        else:
            c[x] += d

    for k in c:
        newList.append(a[k])
    return newList
