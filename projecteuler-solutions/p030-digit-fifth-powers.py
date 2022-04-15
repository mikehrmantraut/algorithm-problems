# Project Euler Problem 30
# Digit Fifth Powers
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
As 1 = 1⁴ is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import re

def comp():
    s #sum of fifth power = 0
    ans = 0
    for i in range(2, 1000000):
        # re.findall('.', str(i)) => 9876 = ["9", "8", "7", "6"]
        for j in re.findall('.', str(i)):
            s += (int(j))**5
        if s == i:
            ans += i
            s = 0
        else:
            s = 0
    return(ans)

if __name__ == '__main__':
    print(comp())
