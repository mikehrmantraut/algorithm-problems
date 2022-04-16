"""
@author: Mehmet Baran Munar
"""
#calculate standard deviation without modules.
def standardDeviation(*args):
    mean = sum(args) / len(args)
    #summation of (x-mean)**2
    sum_symbol = 0
    for i in args:
        sum_symbol += (i-mean)**2

    s_d = (sum_symbol/len(args))**0.5
    s_d = round(s_d,2)
    return s_d

print(standardDeviation(1,3,-1,6,7,8))
