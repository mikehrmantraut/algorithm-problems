""" 
Bubble Sort Algorithm
@author: Mehmet Baran Munar
"""

def bubbleSort(li):
    n = len(li)
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0,n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] =  li[j+1], li[j]
                
# driver code
li = [5,7,1,3,-2,13,5,9,2,1]
 
bubbleSort(li)
 
print ("Sorted liay is:")
for i in range(len(li)):
    print (li[i])
