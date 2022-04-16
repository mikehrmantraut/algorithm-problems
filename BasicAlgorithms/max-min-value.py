"""
@author: Mehmet Baran Munar
"""

#Maximum value of list.
def Max(list):
    maximum = list[0]
    for x in list:
        if x > maximum:
            maximum = x
    return maximum

#Minimum value of list.
def Min(list):
    minimum = list[0]
    for x in list:
        if x < minimum:
            minimum = x
    return minimum

print("Maximum value:",Max([1,5,-2,76,87,7,46,4]))
print("Minimum Value:",Min([1,5,-2,76,87,7,46,4]))
