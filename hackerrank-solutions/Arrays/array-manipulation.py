#!/bin/python3
"""
Hackerrank Array Manipulation Solution
@author: Mehmet Baran Munar
"""

n, m = map(int, input().split())
A = [0 for i in range(n+2)]
for i in range(m):
    a, b, k = map(int, input().split())
    A[a] += k
    A[b + 1] -= k
for i in range(1, len(A)):
    A[i] += A[i-1]
print(max(A))
