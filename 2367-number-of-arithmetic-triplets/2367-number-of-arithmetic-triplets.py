class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        out=0
        s=set(nums)
        for i in s:
            if i+diff in s and i+ 2*diff in s:
                out+=1
        return out