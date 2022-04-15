# Project Euler Problem 48
# Self Powers
"""
The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
"""
import re

def comp():
    ans = sum(i**i for i in range(1, 1001))
    ans = str(ans)
    ans = re.findall(".", ans)
    # This will return a list.
    # You need to log all digits manually.
    return ans[-10:]

if __name__ == "__main__":
    print(comp())
