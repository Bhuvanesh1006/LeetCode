class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                k.append(nums[i])
        for j in range(len(nums)):
            if nums[j]%2!=0:
                k.append(nums[j])
        return k
        