""" 
Math Exponentiation Algorithm
@author: Mehmet Baran Munar
"""

def exponentiation(number, power):
     result = 1
     for i in range(power):
          result *= number
     return result
print(exponentiation(3,3))

""" Second Way """
# def exponentiation(number,power):
#      return number**power
# print(exponentiation(3,3))
