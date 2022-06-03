class Solution(object):
    def sumOfUnique(self, nums):
        arr= {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr[nums[i]] = 1
            else:
                arr[nums[i]] += 1
        
        for key, val in arr.items():
            if val == 1:
                res+=key
                
        return res