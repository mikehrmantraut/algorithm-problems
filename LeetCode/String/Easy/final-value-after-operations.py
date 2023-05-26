class Solution:
    def finalValueAfterOperations(self, operation):
        c = 0
        for i in operation:
            if i == '--X' or i == 'X--':c -= 1
            elif i == '++X' or i == 'X++':c += 1
        return c
