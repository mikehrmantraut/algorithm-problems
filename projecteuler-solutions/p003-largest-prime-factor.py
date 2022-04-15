# Project Euler Problem 3
# Largest Prime Factor 
"""
 The prime factors of 13195 are 5, 7, 13 and 29.
 What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
c = 0
for i in range(1, n):
    if n % i == 0 and i!=1:
        for j in range(1, i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(j)
        c=0
