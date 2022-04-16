"""
Linear search algorithm.
@author: Mehmet Baran Munar
"""
# If x is present then return its location,
# otherwise return -1
 
def search(li, length, target):
 
    for i in range(0, length):
        if (li[i] == target):
            return i
    # if the targes is not in the list.
    # return -1
    return -1
 
 
# Driver Code
li = [2, 3, 4, 10, 40]
target = 10
length = len(li)
 
# Function call
result = search(li, length, target)
if(result == -1):
    print("Element is not present in liay")
else:
    print("Element is present at index", result)
