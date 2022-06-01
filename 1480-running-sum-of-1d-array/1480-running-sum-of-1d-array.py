class Solution(object):
    def runningSum(self, nums):
        dum=0
        out=[]
        for i in range(len(nums)):
            dum+=sum(nums[:i+1])
            out.append(dum)
            dum=0
        return out
            