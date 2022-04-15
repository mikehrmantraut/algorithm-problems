"""
TestDome Two Sum Test Solution 
@author: Mehmet Baran Munar
"""

def find_two_sum(numbers, target_sum):
    seen = {}
    for i, num in enumerate(numbers):
        diff = target_sum - num
        if diff in seen:
            return i, seen[diff]
        seen[num] = i

my_list = [3, 1, 5, 7, 5, 9]
print(find_two_sum(my_list, 10))

"""
Run OK
(3, 0) 
Your score is 100%, perfect!
"""
