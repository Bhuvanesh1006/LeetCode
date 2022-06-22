class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        out=k
        s=[]
        while out!=1:
            nums.remove(max(nums))
            out-=1
        return max(nums)
        