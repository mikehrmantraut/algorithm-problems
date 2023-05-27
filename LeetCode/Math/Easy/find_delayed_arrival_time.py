class Solution:
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        n = arrivalTime + delayedTime

        if n<24:
            return n
        elif n>24:
            return n%24    
        elif n==24:
            return 0
