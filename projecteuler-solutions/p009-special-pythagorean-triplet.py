# Project Euler Problem 9
# Special Pythagorean Triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
             a² + b² = c²
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def comp():
    for a in range(1, 1001):
        for b in range(a + 1, 1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return str(a * b * c)
                
if __name__ == '__main__':
    print(comp())
