# Project Euler Problem 4
# Largest Palindrome Product
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def comp():
    ans = max(i * j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1])
    return ans

if __name__ == "__main__":
    print(comp())
