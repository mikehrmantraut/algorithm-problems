class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        aa = []
        bb = []
        cc = []
        for i in range(1, a+1):
            if a%i == 0:
                aa.append(i)
        for i in range(1, b+1):
            if b%i == 0:
                bb.append(i)
        
        for i in aa:
            if i in bb:
                cc.append(i)
        return len(cc)
