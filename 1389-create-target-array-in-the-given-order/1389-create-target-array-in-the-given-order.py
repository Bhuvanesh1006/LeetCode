class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        trr=[]
        for i in range(len(nums)):
            trr.insert(index[i],nums[i])
        return trr
        