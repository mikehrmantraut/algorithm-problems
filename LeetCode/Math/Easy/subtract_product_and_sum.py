import re
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = []
        b = str(n)
        b = re.findall('.', b)
        for i in range(len(b)):
            a.append(n%10)
            n = floor(n/10)
        product = 1
        summ = 0
        a.sort()
        for i in (a):
            product *= i

        for j in (a):
            summ += j
        return product - summ
