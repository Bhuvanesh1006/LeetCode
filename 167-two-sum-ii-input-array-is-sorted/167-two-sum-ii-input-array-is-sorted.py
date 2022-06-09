class Solution(object):
    def twoSum(self, nums, target):
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                return [l+1,r+1]