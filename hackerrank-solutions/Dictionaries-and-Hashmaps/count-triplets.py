#!/bin/python3
"""
Hackerrank Count Triplets Solution
@author: Mehmet Baran Munar
"""
import os

from collections import defaultdict

def countTriplets(arr, r):
    res = 0
    pairs = defaultdict(int)
    triplets = defaultdict(int)

    for el in arr:
        res += triplets[el]

        triplets[r*el] += pairs[el]
        pairs[r*el] += 1
    
    return res
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()
