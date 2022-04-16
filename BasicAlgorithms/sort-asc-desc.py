"""
@author: Mehmet Baran Munar
"""
#Sort a list of numbers without built-in 
#sort(), min(), max()

def sortAscending(unsorted_list):
    sorted_list = []
    while unsorted_list:
        minimum = unsorted_list[0]
        for i in unsorted_list:
            if i<minimum:
                minimum = i
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)
    return sorted_list

def sortDescending(unsorted_list):
    sorted_list = []
    while unsorted_list:
        maximum = unsorted_list[0]
        for i in unsorted_list:
            if i>maximum:
                maximum = i
        sorted_list.append(maximum)
        unsorted_list.remove(maximum)
    return sorted_list

print(sortAscending([1,-1,1,3,5,6,13,5,9,0,56,43,12,45]))
print(sortDescending([1,-1,1,3,5,6,13,5,9,0,56,43,12,45]))
