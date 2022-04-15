# Project Euler Problem 16
# Power Digit Sum
"""
2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2¹⁰⁰⁰?
"""
import re
def comp():
    ans = sum(int(i) for i in re.findall(".", str(2**1000)))
    return ans

if __name__ == "__main__":
    print(comp())
