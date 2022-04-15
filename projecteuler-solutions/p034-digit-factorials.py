# Project Euler Problem 34
# Digit Factorials
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import re
import math

# As stated in the problem, 1 = 1! and 2 = 2! are excluded.
# If a number has at least n >= 8 digits, then even if every digit is 9,
# n * 9! is still less than the number (which is at least 10^n).

def comp():
    s = 0 # sum of factorials
    ans = 0
    for i in range(3, 1_000_000):
        # for 456 => re.findall('.', str(i)) = [4, 5, 6] 
        for j in re.findall('.', str(i)):
            s += math.factorial(int(j))
        if s == i:
            ans += s
            s = 0 
        else:
            s = 0
    return ans

if __name__ == '__main__':
    print(comp())
