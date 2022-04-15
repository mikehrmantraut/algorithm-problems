#!/bin/python3

"""
Hackerrank Two Strings Solution
@author: Mehmet Baran Munar
"""

import os

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        fptr.write(result + '\n')

    fptr.close()
