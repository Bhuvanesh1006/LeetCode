class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and  i<j:
                    gp+=1
        return gp
        