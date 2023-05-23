class Solution(object):
    def numIdenticalPairs(self, nums):
        c  = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:c += 1
        return c
