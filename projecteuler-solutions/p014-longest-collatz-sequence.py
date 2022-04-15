# Project Euler Problem 14
# Longest Collatz Sequence
"""
The following iterative sequence is defined for the set of positive integers:
      n → n/2 (n is even) 
      n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
      13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
** NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def comp():
    c = 0
    l = list()
    for n in range(1, 1_000_000):
        # finding step size (number of chain)
        while n!=1:
            if n%2==0:
                n /= 2
                c += 1
            else:
                n = 3*n + 1
                c += 1
        l.append(c)
        c = 0
    # added one because the index starts from zero
    return l.index(max(l)) + 1

if __name__ == '__main__':
    print(comp())
