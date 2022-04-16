"""
Prime Factors algorithm
@author Mehmet Baran Munar
"""
def primeFactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   #n became odd
   for i in range(3,int(n*n)+1,2):
     
      while (n % i == 0):
         print (i)
         n = n / i
    
   if n > 2:
      print (n)

primeFactors(12)
