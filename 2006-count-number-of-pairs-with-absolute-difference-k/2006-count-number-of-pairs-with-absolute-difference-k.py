from itertools import combinations
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        c1= combinations(nums, 2)
        for i in c1:
            if abs(i[0]-i[1])==k:
                res+=1
        return res