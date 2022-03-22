class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        s=[]
        for i in range(len(nums)):
            c+=nums[i]
            s.append(c)
        return s
            
            