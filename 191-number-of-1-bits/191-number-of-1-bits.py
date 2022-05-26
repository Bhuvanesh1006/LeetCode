class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        while n :
            cnt+=1
            n = n & (n-1)
        return cnt
        