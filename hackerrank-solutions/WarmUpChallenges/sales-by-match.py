#!/bin/python3

"""
Hackerrank Sales by Match Solution
@author: Mehmet Baran Munar
"""

# n = the number of socks in the pile
# arr = the colors of each sock

def sockMerchant(n, arr):
    n = int(n)
    arr.sort()
    count = 0
    x = 0
    while x < n-1:
        if arr[x] == arr[x+1]:
            count += 1
            x += 2
        else:
            x += 1
    return count

print(sockMerchant(9,[1,3,1,2,5,2,1,2,1]))
