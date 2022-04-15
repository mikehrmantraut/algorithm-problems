#!/bin/python3
"""
Hackerrank Hash Tables: Ransom Note Solution
@author: Mehmet Baran Munar
"""

from collections import Counter

def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine) == {}:
        print('Yes')
    else:
        print('No')
