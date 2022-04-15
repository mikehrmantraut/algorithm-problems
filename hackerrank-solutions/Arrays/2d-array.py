#!/bin/python3
"""
Hackerrank 2D Array - DS Solution
@author: Mehmet Baran Munar
"""
# input -> int arr[6][6]: an array of integers.
# return -> int: the maximum hourglass sum

#input example:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

A = []
for _ in range(6):
    A.append(list(map(int, input().strip().split(' '))))
    
m = -100
for i in range(4):
    for j in range(4):
        val = A[i][j]+A[i][j+1]+A[i][j+2]+ A[i+1][j+1] + A[i+2][j]+A[i+2][j+1]+A[i+2][j+2]
        m = max(val, m)
        
print(m)
