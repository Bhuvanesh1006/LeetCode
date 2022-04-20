class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n=len(nums)
        k=nums[:]
        for i in range(n-1):
            if nums[i]>=nums[i+1]:
                nums.pop(i)
                k.pop(i+1)
                if nums==sorted(list(set(nums))) or k==sorted(list(set(k))):
                    return True
                else:return False
        else:
            return True