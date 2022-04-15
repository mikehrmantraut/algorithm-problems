#!/bin/python3
"""
Hackerrank New Year Chaos Solution
@author: Mehmet Baran Munar
"""
def minimumBribes(q):
    moves = 0 
    q = [p-1 for p in q]
    for i,p in enumerate(q):
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                moves += 1
    print(moves)
