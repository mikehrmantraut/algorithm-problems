"""
Hackerrank Counting Valleys Solution
@author: Mehmet Baran Munar
"""

# int steps: the number of steps on the hike
# string path: a string describing the path
# return -> int: the number of valleys traversed

def countingValleys(steps,path):
    
    steps = 0
    count = 0
    
    for x in path:
        if x == "U":
            steps += 1
        elif x == 'D':
            steps -= 1
        if steps == 0:
            if p < steps:
                count += 1
        p = steps
    return count
print(countingValleys(8,"DDDUUUUU"))
