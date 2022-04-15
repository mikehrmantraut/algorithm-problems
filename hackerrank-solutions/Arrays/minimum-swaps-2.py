#!/bin/python3
"""
Hackerrank Minimum Swaps 2 Solution
@author: Mehmet Baran Munar
"""
def minimumSwaps(arr):
    r = 0
    i = 0
    n = len(arr)
    
    while i < n-1:
        if arr[i] == i + 1:
            i += 1
            continue
        else:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            r += 1
    return r
