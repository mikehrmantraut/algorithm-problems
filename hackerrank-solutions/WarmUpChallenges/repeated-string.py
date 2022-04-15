#!/bin/python3
"""
Hackerrank Repeated String Solution
@author: Mehmet Baran Munar
"""
s = input().strip()
n = int(input().strip())
L = len(s)
print(s.count('a') * (n//L) + s[:n % L].count('a'))
