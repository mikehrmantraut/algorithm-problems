# Project Euler Problem 40
# Champernowne's constant

"""
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
def comp():
    x = "0."
    for i in range(1_000_001):x += str(i+1)
    return int(x[2])*int(x[11])*int(x[101])*int(x[1001])*int(x[10001])*int(x[100001])*int(x[1000001])

if __name__ == '__main__':
    print(comp())
